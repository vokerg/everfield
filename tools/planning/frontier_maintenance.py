#!/usr/bin/env python3
"""Conservative GitHub-state reconciliation for Everfield planning-v1.

Maintenance never grants planning authority. It only reconciles storage state,
materializes missing required transitions, and dispatches exact-main workflows
from a repository-owned allowlist.
"""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Any, Iterable

API = os.environ.get("GITHUB_API_URL", "https://api.github.com").rstrip("/")
REPO = os.environ.get("GITHUB_REPOSITORY", "vokerg/everfield")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
DRY_RUN = os.environ.get("FRONTIER_MAINTENANCE_DRY_RUN", "").lower() in {"1", "true", "yes"}
ROUTES_PATH = os.environ.get("FRONTIER_ROUTES_PATH", ".github/planning-frontier-routes.json")

TRUSTED_ASSOCIATIONS = {"OWNER", "MEMBER", "COLLABORATOR"}
OPERATIONAL_KINDS = {
    "CLAIM", "ORPHAN_PROBE", "RESUME_INTENT", "RESUME", "RECOVER", "PROGRESS",
    "STATUS", "REVIEW_STATUS", "VERIFICATION_STATUS", "INTEGRATION_STATUS",
    "BOOTSTRAP_RESUME", "BOOTSTRAP_VERIFICATION_STATUS",
}
OWNERSHIP_KINDS = {"CLAIM", "RESUME", "RECOVER", "BOOTSTRAP_RESUME"}
TERMINAL_STATES = {"DONE", "SUPERSEDED", "INVALIDATED"}
TERMINAL_KINDS = {"STATUS", "REVIEW_STATUS", "VERIFICATION_STATUS", "INTEGRATION_STATUS"}
SHA40_RE = re.compile(r"^[0-9a-fA-F]{40}$")
FACTORY_TRANSITION_RE = re.compile(r"\[FACTORY-TRANSITION-(\d+)\]")
DISPATCH_MARKER_VERSION = "1"
DISPATCH_MARKER_STATES = {"ACCEPTED", "OBSERVED"}
RATE_LIMIT_MESSAGE_MARKERS = (
    "api rate limit exceeded",
    "secondary rate limit",
)

SCHEMA3_TASK_OWNERSHIP_LEASE_SECONDS = 21_600
SCHEMA3_ORPHAN_PROBE_MATURITY_SECONDS = 600


class GitHubRateLimitExceeded(RuntimeError):
    """Retryable GitHub API rate exhaustion; grants no maintenance authority."""


def github_api_error(method: str, url: str, code: int, detail: str) -> RuntimeError:
    message = detail
    try:
        parsed = json.loads(detail)
        if isinstance(parsed, dict):
            message = str(parsed.get("message") or detail)
    except json.JSONDecodeError:
        pass

    normalized = message.lower()
    if code in {403, 429} and any(marker in normalized for marker in RATE_LIMIT_MESSAGE_MARKERS):
        return GitHubRateLimitExceeded(
            f"GitHub API {method} {url} deferred by rate limit: {code} {detail}"
        )
    return RuntimeError(f"GitHub API {method} {url} failed: {code} {detail}")


@dataclass(frozen=True)
class OperationalRecord:
    issue_number: int
    comment_id: int
    created_at: str
    kind: str
    state: str | None
    route: str | None
    body: str
    declared_issue: int | None
    mission_id: str | None
    actor_session_id: str | None
    authority_mode: str | None
    ownership_generation_comment_id: int | None
    head_sha: str | None
    work_sha: str | None


def request(method: str, path: str, payload: Any | None = None) -> Any:
    if not TOKEN:
        raise RuntimeError("GITHUB_TOKEN is required")
    url = path if path.startswith("http") else f"{API}{path}"
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "everfield-frontier-maintenance/3",
    }
    if data is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            raw = response.read()
            return None if not raw else json.loads(raw.decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise github_api_error(method, url, exc.code, detail) from exc


def paged(path: str) -> Iterable[dict[str, Any]]:
    sep = "&" if "?" in path else "?"
    page = 1
    while True:
        batch = request("GET", f"{path}{sep}per_page=100&page={page}")
        if not isinstance(batch, list):
            raise RuntimeError(f"expected list from {path}")
        yield from batch
        if len(batch) < 100:
            return
        page += 1


def scalar(body: str, key: str) -> str | None:
    match = re.search(rf"(?m)^\s*{re.escape(key)}:\s*([^#\n]+?)\s*$", body)
    if not match:
        return None
    value = match.group(1).strip().strip("'\"")
    return None if value.lower() in {"null", "none", ""} else value


def integer_scalar(body: str, key: str) -> int | None:
    value = scalar(body, key)
    return int(value) if value and value.isdigit() else None


def list_scalar(body: str, key: str) -> list[str]:
    """Read one conservative YAML-like scalar/list field from an operational body."""
    lines = body.splitlines()
    key_re = re.compile(rf"^(?P<indent>\s*){re.escape(key)}:\s*(?P<value>.*?)\s*$")
    for index, line in enumerate(lines):
        match = key_re.match(line)
        if not match:
            continue
        value = match.group("value").strip()
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            if not inner:
                return []
            return [
                item.strip().strip("'\\\"")
                for item in inner.split(",")
                if item.strip().strip("'\\\"")
            ]
        if value and value.lower() not in {"null", "none"}:
            return [value.strip("'\\\"")]

        indent = len(match.group("indent"))
        values: list[str] = []
        for following in lines[index + 1 :]:
            if not following.strip():
                continue
            leading = len(following) - len(following.lstrip())
            item = re.match(r"^\s*-\s*(.+?)\s*$", following)
            if item and leading > indent:
                parsed = item.group(1).strip().strip("'\\\"")
                if parsed:
                    values.append(parsed)
                continue
            if leading <= indent:
                break
        return values
    return []


def immutable_ref(value: str) -> bool:
    """Validate the canonical immutable-ref forms maintenance can prove locally."""
    candidate = value.strip()
    if SHA40_RE.fullmatch(candidate):
        return True
    if candidate.isdigit() and int(candidate) > 0:
        return True
    if "@" in candidate:
        path, work_sha = candidate.rsplit("@", 1)
        return bool(path and SHA40_RE.fullmatch(work_sha))
    return False


def parse_github_server_time(value: str | None) -> datetime | None:
    """Parse authoritative GitHub `created_at`; naive/malformed values fail closed."""
    if not value:
        return None
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        return None
    return parsed.astimezone(timezone.utc)


@dataclass(frozen=True)
class OwnershipLeaseState:
    anchor_comment_id: int
    anchor_created_at: datetime
    observed_head_sha: str
    consecutive_evidence: int


def schema3_ownership_lease_state(
    owner: OperationalRecord,
    records: Iterable[OperationalRecord],
    *,
    before_comment_id: int,
) -> OwnershipLeaseState | None:
    """Reconstruct the canonical lease anchor through valid PROGRESS renewals.

    This helper intentionally evaluates only temporal/current-generation PROGRESS
    predicates that maintenance can prove from immutable operational comments.
    Ambiguous records have zero renewal effect.
    """
    if (
        owner.kind not in OWNERSHIP_KINDS
        or owner.state != "IN_PROGRESS"
        or not owner.actor_session_id
        or owner.comment_id >= before_comment_id
    ):
        return None
    anchor = parse_github_server_time(owner.created_at)
    observed_head = scalar(owner.body, "observed_head_sha")
    if anchor is None or observed_head is None or not SHA40_RE.fullmatch(observed_head):
        return None

    anchor_comment_id = owner.comment_id
    consecutive_evidence = 0
    for record in sorted(records, key=lambda item: item.comment_id):
        if not (owner.comment_id < record.comment_id < before_comment_id):
            continue
        if (
            record.kind != "PROGRESS"
            or record.state != "IN_PROGRESS"
            or record.declared_issue != owner.declared_issue
            or record.mission_id != owner.mission_id
            or record.actor_session_id != owner.actor_session_id
            or record.ownership_generation_comment_id != owner.comment_id
        ):
            continue
        progress_time = parse_github_server_time(record.created_at)
        progress_head = scalar(record.body, "observed_head_sha")
        progress_basis = scalar(record.body, "progress_basis")
        if (
            progress_time is None
            or progress_time < anchor
            or progress_head is None
            or not SHA40_RE.fullmatch(progress_head)
            or progress_time >= anchor + timedelta(seconds=SCHEMA3_TASK_OWNERSHIP_LEASE_SECONDS)
        ):
            continue

        if progress_basis == "HEAD_ADVANCE":
            if progress_head == observed_head:
                continue
            observed_head = progress_head
            consecutive_evidence = 0
        elif progress_basis == "EVIDENCE":
            evidence_refs = list_scalar(record.body, "evidence_refs")
            if (
                progress_head != observed_head
                or not evidence_refs
                or not all(immutable_ref(ref) for ref in evidence_refs)
            ):
                continue
            if consecutive_evidence >= 3:
                continue
            consecutive_evidence += 1
        else:
            continue

        anchor = progress_time
        anchor_comment_id = record.comment_id

    return OwnershipLeaseState(
        anchor_comment_id=anchor_comment_id,
        anchor_created_at=anchor,
        observed_head_sha=observed_head,
        consecutive_evidence=consecutive_evidence,
    )


def schema3_owner_unexpired_at(
    owner: OperationalRecord,
    records: Iterable[OperationalRecord],
    at_record: OperationalRecord,
) -> bool | None:
    """Return owner lease liveness at an operational record, or None on bad time."""
    at_time = parse_github_server_time(at_record.created_at)
    if at_time is None:
        return None
    state = schema3_ownership_lease_state(
        owner, records, before_comment_id=at_record.comment_id
    )
    if state is None or at_time < state.anchor_created_at:
        return None
    return at_time < state.anchor_created_at + timedelta(
        seconds=SCHEMA3_TASK_OWNERSHIP_LEASE_SECONDS
    )


def schema3_orphan_probe_mature_at(
    probe: OperationalRecord,
    at_record: OperationalRecord,
) -> bool | None:
    """Return canonical 600-second ORPHAN maturity at a later record."""
    if probe.kind != "ORPHAN_PROBE" or probe.comment_id >= at_record.comment_id:
        return False
    probe_time = parse_github_server_time(probe.created_at)
    at_time = parse_github_server_time(at_record.created_at)
    if probe_time is None or at_time is None:
        return None
    return at_time >= probe_time + timedelta(
        seconds=SCHEMA3_ORPHAN_PROBE_MATURITY_SECONDS
    )


def immutable_comment(comment: dict[str, Any]) -> bool:
    created_at = comment.get("created_at")
    updated_at = comment.get("updated_at")
    return bool(created_at and updated_at and created_at == updated_at)


def parse_operational(issue_number: int, comment: dict[str, Any]) -> OperationalRecord | None:
    body = comment.get("body") or ""
    if comment.get("author_association") not in TRUSTED_ASSOCIATIONS:
        return None
    if not immutable_comment(comment):
        return None
    if scalar(body, "protocol") != "planning-v1" or scalar(body, "schema") != "3":
        return None
    kind = scalar(body, "kind")
    if kind not in OPERATIONAL_KINDS:
        return None
    return OperationalRecord(
        issue_number=issue_number,
        comment_id=int(comment["id"]),
        created_at=comment.get("created_at") or "",
        kind=kind,
        state=scalar(body, "state"),
        route=scalar(body, "required_next_route"),
        body=body,
        declared_issue=integer_scalar(body, "issue"),
        mission_id=scalar(body, "mission_id"),
        actor_session_id=scalar(body, "actor_session_id"),
        authority_mode=scalar(body, "authority_mode"),
        ownership_generation_comment_id=integer_scalar(body, "ownership_generation_comment_id"),
        head_sha=scalar(body, "head_sha"),
        work_sha=scalar(body, "work_sha"),
    )


def operational_records_from_comments(issue_number: int, comments: Iterable[dict[str, Any]]) -> list[OperationalRecord]:
    return [record for comment in comments if (record := parse_operational(issue_number, comment))]


def latest_operational_from_comments(issue_number: int, comments: Iterable[dict[str, Any]]) -> OperationalRecord | None:
    records = operational_records_from_comments(issue_number, comments)
    return max(records, key=lambda item: item.comment_id) if records else None


def reconcilable_terminal_from_comments(issue_number: int, comments: Iterable[dict[str, Any]]) -> OperationalRecord | None:
    """Return a terminal only when its owner linkage is conservatively provable.

    This deliberately implements a strict subset of schema-3. Ambiguous or
    externally-retired records remain open for an agent to reconcile rather
    than being auto-closed by maintenance.
    """
    records = operational_records_from_comments(issue_number, comments)
    if not records:
        return None
    latest = max(records, key=lambda item: item.comment_id)
    if latest.kind not in TERMINAL_KINDS or latest.state not in TERMINAL_STATES:
        return None
    if latest.declared_issue != issue_number:
        return None
    if latest.authority_mode != "OWNER":
        return None
    if not latest.mission_id or not latest.actor_session_id:
        return None
    if latest.ownership_generation_comment_id is None:
        return None
    if not latest.head_sha or not latest.work_sha:
        return None
    if not SHA40_RE.fullmatch(latest.head_sha) or not SHA40_RE.fullmatch(latest.work_sha):
        return None

    owner = next(
        (record for record in records if record.comment_id == latest.ownership_generation_comment_id),
        None,
    )
    if owner is None or owner.comment_id >= latest.comment_id:
        return None
    if owner.kind not in OWNERSHIP_KINDS:
        return None
    if owner.declared_issue != issue_number:
        return None
    if owner.actor_session_id != latest.actor_session_id:
        return None
    if owner.mission_id != latest.mission_id:
        return None
    return latest


def reconcilable_terminal(issue_number: int) -> OperationalRecord | None:
    return reconcilable_terminal_from_comments(
        issue_number,
        paged(f"/repos/{REPO}/issues/{issue_number}/comments?"),
    )


def close_terminal_open_issues(open_issues: list[dict[str, Any]]) -> int:
    closed = 0
    for issue in open_issues:
        if "pull_request" in issue:
            continue
        number = int(issue["number"])
        terminal = reconcilable_terminal(number)
        if not terminal:
            continue
        reason = "completed" if terminal.state == "DONE" else "not_planned"
        print(f"reconcile issue #{number}: bound {terminal.kind}/{terminal.state} -> closed/{reason}")
        if not DRY_RUN:
            request("PATCH", f"/repos/{REPO}/issues/{number}", {"state": "closed", "state_reason": reason})
        closed += 1
    return closed


def pr_explicitly_rejected(body: str) -> bool:
    disposition = re.search(
        r"(?im)^\s*(?:review\s+)?disposition\s*:\s*`?(CHANGES_NEEDED|CHANGES_REQUIRED)`?(?:\s*[—-].*)?\s*$",
        body,
    )
    disposition_block = re.search(
        r"(?im)^\s*(?:review\s+)?disposition\s*$\n\s*`?(CHANGES_NEEDED|CHANGES_REQUIRED)`?\s*$",
        body,
    )
    self_prohibition = re.search(
        r"(?i)\bthis\s+(?:draft\s+)?PR\s+must\s+not\s+(?:integrate|be\s+merged)\b",
        body,
    )
    return bool(disposition or disposition_block or self_prohibition)


def close_rejected_open_prs(open_prs: list[dict[str, Any]]) -> int:
    closed = 0
    for pr in open_prs:
        if not pr.get("draft") or pr.get("author_association") not in TRUSTED_ASSOCIATIONS:
            continue
        if not pr_explicitly_rejected(pr.get("body") or ""):
            continue
        number = int(pr["number"])
        print(f"retire explicitly rejected draft PR #{number}")
        if not DRY_RUN:
            request("PATCH", f"/repos/{REPO}/pulls/{number}", {"state": "closed"})
        closed += 1
    return closed


def load_routes() -> dict[str, dict[str, Any]]:
    import base64

    encoded = urllib.parse.quote(ROUTES_PATH, safe="/")
    data = request("GET", f"/repos/{REPO}/contents/{encoded}?ref=main")
    raw = base64.b64decode(data["content"]).decode("utf-8")
    routes = json.loads(raw).get("routes", {})
    if not isinstance(routes, dict):
        raise RuntimeError("routes must be an object")
    return routes


def current_main_sha() -> str:
    return request("GET", f"/repos/{REPO}/branches/main")["commit"]["sha"]


def transition_title(source_issue: int) -> str:
    return f"[PLAN-v1][FACTORY-TRANSITION-{source_issue}] Materialize required next route from #{source_issue}"


def is_factory_transition(issue: dict[str, Any]) -> bool:
    return FACTORY_TRANSITION_RE.search(issue.get("title") or "") is not None


def find_open_transition(open_issues: list[dict[str, Any]], source_issue: int) -> dict[str, Any] | None:
    marker = f"[FACTORY-TRANSITION-{source_issue}]"
    return next((item for item in open_issues if "pull_request" not in item and marker in (item.get("title") or "")), None)


def create_transition(source: OperationalRecord, route_cfg: dict[str, Any] | None) -> dict[str, Any] | None:
    body = (
        "## Factory liveness recovery\n\n"
        f"Source terminal issue: #{source.issue_number}\n"
        f"Source terminal comment: {source.comment_id}\n"
        f"Required next route: `{source.route}`\n\n"
        "This issue exists because a terminal episode declared a required continuation but no live selectable "
        "transition was present. Re-derive current main/canonical binding/ownership before acting. Preserve all "
        "review, verification, authority, exact-head, and squash-only gates.\n\n"
        + ("The route is registered for repository-internal workflow dispatch; maintenance may dispatch it on exact current `main`.\n"
           if route_cfg else
           "The route is not executable by maintenance. Materialize the smallest exact successor/recovery issue required by the source contract; do not invent authority.\n")
    )
    print(f"materialize transition from #{source.issue_number}: {source.route}")
    if DRY_RUN:
        return None
    return request("POST", f"/repos/{REPO}/issues", {"title": transition_title(source.issue_number), "body": body})


def matching_fresh_run(workflow: str, main_sha: str, source_created_at: str) -> dict[str, Any] | None:
    path = urllib.parse.quote(workflow, safe="")
    runs = request("GET", f"/repos/{REPO}/actions/workflows/{path}/runs?event=workflow_dispatch&branch=main&per_page=30")
    for run in runs.get("workflow_runs", []):
        if run.get("head_sha") == main_sha and (not source_created_at or (run.get("created_at") or "") >= source_created_at):
            return run
    return None


def trusted_dispatch_marker_from_comments(
    comments: Iterable[dict[str, Any]], source_issue: int, route: str
) -> dict[str, Any] | None:
    for comment in comments:
        body = comment.get("body") or ""
        user_login = ((comment.get("user") or {}).get("login") or "")
        trusted_author = user_login == "github-actions[bot]" or comment.get("author_association") in TRUSTED_ASSOCIATIONS
        if not trusted_author or not immutable_comment(comment):
            continue
        if scalar(body, "factory_frontier_dispatch") != DISPATCH_MARKER_VERSION:
            continue
        if integer_scalar(body, "source_issue") != source_issue:
            continue
        if scalar(body, "route") != route:
            continue
        if scalar(body, "status") not in DISPATCH_MARKER_STATES:
            continue
        main_sha = scalar(body, "main_sha")
        if not main_sha or not SHA40_RE.fullmatch(main_sha):
            continue
        return comment
    return None


def transition_has_dispatch_marker(transition: dict[str, Any], source_issue: int, route: str) -> bool:
    number = int(transition["number"])
    comments = paged(f"/repos/{REPO}/issues/{number}/comments?")
    return trusted_dispatch_marker_from_comments(comments, source_issue, route) is not None


def record_dispatch_marker(
    transition: dict[str, Any], source: OperationalRecord, workflow: str, main_sha: str,
    status: str, run_id: int | None = None,
) -> None:
    if DRY_RUN:
        return
    lines = [
        f"factory_frontier_dispatch: {DISPATCH_MARKER_VERSION}",
        f"source_issue: {source.issue_number}",
        f"source_terminal_comment_id: {source.comment_id}",
        f"route: {source.route}",
        f"status: {status}",
        f"workflow: {workflow}",
        f"main_sha: {main_sha}",
    ]
    if run_id is not None:
        lines.append(f"run_id: {run_id}")
    lines.extend([
        "authority_created: false",
        "note: Repository factory dispatch marker only; downstream evidence and authority gates remain separate.",
    ])
    request("POST", f"/repos/{REPO}/issues/{int(transition['number'])}/comments", {"body": "\n".join(lines)})


def dispatch_registered_route(source: OperationalRecord, cfg: dict[str, Any], transition: dict[str, Any] | None) -> bool:
    if cfg.get("type") != "workflow_dispatch" or transition is None:
        return False
    workflow = cfg.get("workflow")
    if not workflow or cfg.get("ref", "main") != "main":
        raise RuntimeError(f"unsafe route registration for {source.route}: exact main workflow required")
    if source.route is None:
        raise RuntimeError("registered dispatch requires a source route")
    if transition_has_dispatch_marker(transition, source.issue_number, source.route):
        print(f"route {source.route}: transition already has trusted dispatch marker")
        return False

    main_sha = current_main_sha()
    existing = matching_fresh_run(workflow, main_sha, source.created_at)
    if existing:
        print(f"route {source.route}: observed fresh exact-main run {existing.get('id')} at {main_sha}")
        record_dispatch_marker(
            transition, source, workflow, main_sha, "OBSERVED",
            int(existing["id"]) if existing.get("id") is not None else None,
        )
        return False

    inputs = dict(cfg.get("inputs") or {})
    if "reason" in inputs:
        inputs["reason"] = str(inputs["reason"]).format(source_issue=source.issue_number, main_sha=main_sha)
    payload: dict[str, Any] = {"ref": "main"}
    if inputs:
        payload["inputs"] = inputs
    print(f"dispatch {workflow} on main@{main_sha} for route {source.route}")
    if not DRY_RUN:
        path = urllib.parse.quote(workflow, safe="")
        request("POST", f"/repos/{REPO}/actions/workflows/{path}/dispatches", payload)
        record_dispatch_marker(transition, source, workflow, main_sha, "ACCEPTED")
    return True


def predecessor_sources(issue: dict[str, Any]) -> set[int]:
    text = issue.get("body") or ""
    patterns = (
        r"(?im)^\s*predecessor_issue:\s*(\d+)\s*$",
        r"(?i)immediate predecessor:\s*Issue\s*#(\d+)",
        r"(?i)Source terminal issue:\s*#(\d+)",
    )
    found: set[int] = set()
    for pattern in patterns:
        found.update(int(value) for value in re.findall(pattern, text))
    return found


def consumed_nontransition_sources(issues: Iterable[dict[str, Any]]) -> set[int]:
    consumed: set[int] = set()
    for issue in issues:
        if "pull_request" in issue or is_factory_transition(issue):
            continue
        consumed.update(predecessor_sources(issue))
    return consumed


def materialize_missing_transitions(open_issues: list[dict[str, Any]], routes: dict[str, dict[str, Any]]) -> tuple[int, int]:
    created = dispatched = 0
    closed = list(paged(f"/repos/{REPO}/issues?state=closed&sort=updated&direction=desc&since=2026-08-20T00:00:00Z&"))
    recent_issues = [item for item in open_issues + closed if "pull_request" not in item]
    consumed_sources = consumed_nontransition_sources(recent_issues)
    dispatch_keys: set[tuple[str, str]] = set()
    for issue in closed:
        if "pull_request" in issue:
            continue
        number = int(issue["number"])
        source = reconcilable_terminal(number)
        if not source or not source.route or number in consumed_sources:
            continue
        transition = find_open_transition(open_issues, number)
        cfg = routes.get(source.route)
        if not transition:
            transition = create_transition(source, cfg)
            created += 1
            if transition:
                open_issues.append(transition)
        if cfg and transition:
            key = (str(cfg.get("workflow")), current_main_sha())
            if key not in dispatch_keys and dispatch_registered_route(source, cfg, transition):
                dispatch_keys.add(key)
                dispatched += 1
    return created, dispatched


def self_test() -> None:
    def c(
        cid: int, kind: str, state: str, *, issue: int = 10, actor: str = "actor-a",
        mission: str = "M-10", extra: str = "", association: str = "OWNER",
        edited: bool = False,
    ) -> dict[str, Any]:
        created_at = f"2026-08-25T00:00:{cid:02d}Z"
        updated_at = f"2026-08-25T00:01:{cid:02d}Z" if edited else created_at
        return {
            "id": cid,
            "author_association": association,
            "user": {"login": "vokerg" if association == "OWNER" else "outsider"},
            "created_at": created_at,
            "updated_at": updated_at,
            "body": (
                "protocol: planning-v1\n"
                "schema: 3\n"
                f"kind: {kind}\n"
                f"issue: {issue}\n"
                f"mission_id: {mission}\n"
                f"actor_session_id: {actor}\n"
                f"state: {state}\n"
                f"{extra}"
            ),
        }

    claim = c(1, "CLAIM", "IN_PROGRESS")
    valid_done = c(
        2, "STATUS", "DONE",
        extra=(
            "authority_mode: OWNER\n"
            "ownership_generation_comment_id: 1\n"
            f"head_sha: {'a' * 40}\n"
            f"work_sha: {'b' * 40}\n"
            "required_next_route: NEXT\n"
        ),
    )
    assert reconcilable_terminal_from_comments(10, [claim, valid_done]) is not None

    later_claim = c(3, "CLAIM", "IN_PROGRESS")
    assert reconcilable_terminal_from_comments(10, [claim, valid_done, later_claim]) is None

    malformed_done = c(
        2, "STATUS", "DONE",
        extra=f"authority_mode: OWNER\nhead_sha: {'a' * 40}\nwork_sha: {'b' * 40}\n",
    )
    assert reconcilable_terminal_from_comments(10, [claim, malformed_done]) is None

    wrong_actor_done = c(
        2, "STATUS", "DONE", actor="actor-b",
        extra=(
            "authority_mode: OWNER\n"
            "ownership_generation_comment_id: 1\n"
            f"head_sha: {'a' * 40}\n"
            f"work_sha: {'b' * 40}\n"
        ),
    )
    assert reconcilable_terminal_from_comments(10, [claim, wrong_actor_done]) is None

    outsider_done = dict(valid_done, id=4, author_association="NONE", user={"login": "outsider"})
    assert reconcilable_terminal_from_comments(10, [claim, outsider_done]) is None

    edited_done = c(
        2, "STATUS", "DONE", edited=True,
        extra=(
            "authority_mode: OWNER\n"
            "ownership_generation_comment_id: 1\n"
            f"head_sha: {'a' * 40}\n"
            f"work_sha: {'b' * 40}\n"
        ),
    )
    assert reconcilable_terminal_from_comments(10, [claim, edited_done]) is None
    edited_claim = c(1, "CLAIM", "IN_PROGRESS", edited=True)
    assert reconcilable_terminal_from_comments(10, [edited_claim, valid_done]) is None

    predecessor_prose = "Predecessor review disposition: `CHANGES_NEEDED`. This PR fixes it and requires fresh review."
    assert not pr_explicitly_rejected(predecessor_prose)
    assert pr_explicitly_rejected("Disposition: `CHANGES_NEEDED` — 0 blocker / 1 major")
    assert pr_explicitly_rejected("Review disposition\nCHANGES_REQUIRED")
    assert pr_explicitly_rejected("This draft PR must not be merged.")

    normal_successor = {"title": "[PLAN-v1] successor", "body": "Immediate predecessor: Issue #10"}
    transition = {"title": "[PLAN-v1][FACTORY-TRANSITION-10] Materialize", "body": "Source terminal issue: #10"}
    assert consumed_nontransition_sources([normal_successor]) == {10}
    assert consumed_nontransition_sources([transition]) == set()

    marker_created_at = "2026-08-25T00:00:09Z"
    marker = {
        "id": 9,
        "author_association": "NONE",
        "user": {"login": "github-actions[bot]"},
        "created_at": marker_created_at,
        "updated_at": marker_created_at,
        "body": (
            "factory_frontier_dispatch: 1\n"
            "source_issue: 10\n"
            "route: NEXT\n"
            "status: ACCEPTED\n"
            f"main_sha: {'c' * 40}\n"
        ),
    }
    assert trusted_dispatch_marker_from_comments([marker], 10, "NEXT") is not None
    assert trusted_dispatch_marker_from_comments([marker], 10, "OTHER") is None
    edited_marker = dict(marker, updated_at="2026-08-25T00:01:09Z")
    assert trusted_dispatch_marker_from_comments([edited_marker], 10, "NEXT") is None

    rate_limited = github_api_error(
        "GET",
        "https://api.github.com/repos/vokerg/everfield/pulls",
        403,
        '{"message":"API rate limit exceeded for installation."}',
    )
    assert isinstance(rate_limited, GitHubRateLimitExceeded)
    generic_forbidden = github_api_error(
        "GET",
        "https://api.github.com/repos/vokerg/everfield/pulls",
        403,
        '{"message":"Resource not accessible by integration"}',
    )
    assert isinstance(generic_forbidden, RuntimeError)
    assert not isinstance(generic_forbidden, GitHubRateLimitExceeded)

    assert parse_github_server_time("2026-09-15T12:00:00Z") is not None
    assert parse_github_server_time("2026-09-15T12:00:00") is None
    assert parse_github_server_time("not-a-time") is None

    owner = OperationalRecord(
        issue_number=77, comment_id=1, created_at="2026-09-15T12:00:00Z",
        kind="CLAIM", state="IN_PROGRESS", route=None,
        body=f"observed_head_sha: {'a' * 40}\n", declared_issue=77,
        mission_id="M-77", actor_session_id="actor-77", authority_mode=None,
        ownership_generation_comment_id=None, head_sha=None, work_sha=None,
    )
    progress = OperationalRecord(
        issue_number=77, comment_id=2, created_at="2026-09-15T17:00:00Z",
        kind="PROGRESS", state="IN_PROGRESS", route=None,
        body=(
            f"observed_head_sha: {'b' * 40}\n"
            "progress_basis: HEAD_ADVANCE\n"
            "evidence_refs: []\n"
        ),
        declared_issue=77, mission_id="M-77", actor_session_id="actor-77",
        authority_mode=None, ownership_generation_comment_id=1,
        head_sha=None, work_sha=None,
    )
    before_old_boundary = OperationalRecord(
        issue_number=77, comment_id=3, created_at="2026-09-15T18:00:00Z",
        kind="RESUME_INTENT", state="IN_PROGRESS", route=None, body="",
        declared_issue=77, mission_id="M-77", actor_session_id="actor-78",
        authority_mode=None, ownership_generation_comment_id=None,
        head_sha=None, work_sha=None,
    )
    exact_new_boundary = OperationalRecord(
        issue_number=77, comment_id=4, created_at="2026-09-15T23:00:00Z",
        kind="RESUME_INTENT", state="IN_PROGRESS", route=None, body="",
        declared_issue=77, mission_id="M-77", actor_session_id="actor-78",
        authority_mode=None, ownership_generation_comment_id=None,
        head_sha=None, work_sha=None,
    )
    assert schema3_owner_unexpired_at(owner, [owner, progress], before_old_boundary) is True
    assert schema3_owner_unexpired_at(owner, [owner, progress], exact_new_boundary) is False

    evidence_records = [owner]
    for cid, hour in ((2, 13), (3, 14), (4, 15), (5, 16)):
        evidence_records.append(
            OperationalRecord(
                issue_number=77, comment_id=cid,
                created_at=f"2026-09-15T{hour:02d}:00:00Z",
                kind="PROGRESS", state="IN_PROGRESS", route=None,
                body=(
                    f"observed_head_sha: {'a' * 40}\n"
                    "progress_basis: EVIDENCE\n"
                    f"evidence_refs:\n  - {'e' * 40}\n"
                ),
                declared_issue=77, mission_id="M-77", actor_session_id="actor-77",
                authority_mode=None, ownership_generation_comment_id=1,
                head_sha=None, work_sha=None,
            )
        )
    evidence_state = schema3_ownership_lease_state(
        owner, evidence_records, before_comment_id=6
    )
    assert evidence_state is not None
    assert evidence_state.anchor_comment_id == 4
    assert evidence_state.consecutive_evidence == 3

    probe = OperationalRecord(
        issue_number=77, comment_id=10, created_at="2026-09-15T12:00:00Z",
        kind="ORPHAN_PROBE", state=None, route=None, body="",
        declared_issue=77, mission_id="M-77", actor_session_id="actor-78",
        authority_mode=None, ownership_generation_comment_id=None,
        head_sha=None, work_sha=None,
    )
    early = OperationalRecord(
        issue_number=77, comment_id=11, created_at="2026-09-15T12:09:59Z",
        kind="RESUME_INTENT", state=None, route=None, body="",
        declared_issue=77, mission_id="M-77", actor_session_id="actor-78",
        authority_mode=None, ownership_generation_comment_id=None,
        head_sha=None, work_sha=None,
    )
    mature = OperationalRecord(
        issue_number=77, comment_id=12, created_at="2026-09-15T12:10:00Z",
        kind="RESUME_INTENT", state=None, route=None, body="",
        declared_issue=77, mission_id="M-77", actor_session_id="actor-78",
        authority_mode=None, ownership_generation_comment_id=None,
        head_sha=None, work_sha=None,
    )
    assert schema3_orphan_probe_mature_at(probe, early) is False
    assert schema3_orphan_probe_mature_at(probe, mature) is True

    print("frontier maintenance self-test: PASS")


def main() -> int:
    if "--self-test" in sys.argv:
        self_test()
        return 0
    open_items = list(paged(f"/repos/{REPO}/issues?state=open&sort=created&direction=asc&"))
    open_prs = list(paged(f"/repos/{REPO}/pulls?state=open&sort=created&direction=asc&"))
    issue_closed = close_terminal_open_issues(open_items)
    pr_closed = close_rejected_open_prs(open_prs)
    transition_created, dispatched = materialize_missing_transitions(open_items, load_routes())
    print(json.dumps({
        "dry_run": DRY_RUN,
        "terminal_issues_closed": issue_closed,
        "rejected_prs_closed": pr_closed,
        "transitions_created": transition_created,
        "registered_routes_dispatched": dispatched,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
