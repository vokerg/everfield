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
        raise RuntimeError(f"GitHub API {method} {url} failed: {exc.code} {detail}") from exc


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


def parse_operational(issue_number: int, comment: dict[str, Any]) -> OperationalRecord | None:
    body = comment.get("body") or ""
    if comment.get("author_association") not in TRUSTED_ASSOCIATIONS:
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
        if not trusted_author:
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
    ) -> dict[str, Any]:
        return {
            "id": cid,
            "author_association": association,
            "user": {"login": "vokerg" if association == "OWNER" else "outsider"},
            "created_at": f"2026-08-25T00:00:{cid:02d}Z",
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

    predecessor_prose = "Predecessor review disposition: `CHANGES_NEEDED`. This PR fixes it and requires fresh review."
    assert not pr_explicitly_rejected(predecessor_prose)
    assert pr_explicitly_rejected("Disposition: `CHANGES_NEEDED` — 0 blocker / 1 major")
    assert pr_explicitly_rejected("Review disposition\nCHANGES_REQUIRED")
    assert pr_explicitly_rejected("This draft PR must not be merged.")

    normal_successor = {"title": "[PLAN-v1] successor", "body": "Immediate predecessor: Issue #10"}
    transition = {"title": "[PLAN-v1][FACTORY-TRANSITION-10] Materialize", "body": "Source terminal issue: #10"}
    assert consumed_nontransition_sources([normal_successor]) == {10}
    assert consumed_nontransition_sources([transition]) == set()

    marker = {
        "id": 9,
        "author_association": "NONE",
        "user": {"login": "github-actions[bot]"},
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
