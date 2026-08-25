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
TERMINAL_STATES = {"DONE", "SUPERSEDED", "INVALIDATED"}
TERMINAL_KINDS = {"STATUS", "REVIEW_STATUS", "VERIFICATION_STATUS", "INTEGRATION_STATUS"}


@dataclass(frozen=True)
class OperationalRecord:
    issue_number: int
    comment_id: int
    created_at: str
    kind: str
    state: str | None
    route: str | None
    body: str


def request(method: str, path: str, payload: Any | None = None) -> Any:
    if not TOKEN:
        raise RuntimeError("GITHUB_TOKEN is required")
    url = path if path.startswith("http") else f"{API}{path}"
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "everfield-frontier-maintenance/2",
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
    )


def latest_operational_from_comments(issue_number: int, comments: Iterable[dict[str, Any]]) -> OperationalRecord | None:
    records = [record for comment in comments if (record := parse_operational(issue_number, comment))]
    return max(records, key=lambda item: item.comment_id) if records else None


def latest_operational(issue_number: int) -> OperationalRecord | None:
    return latest_operational_from_comments(
        issue_number,
        paged(f"/repos/{REPO}/issues/{issue_number}/comments?"),
    )


def terminal_if_latest(record: OperationalRecord | None) -> OperationalRecord | None:
    if not record or record.kind not in TERMINAL_KINDS or record.state not in TERMINAL_STATES:
        return None
    return record


def close_terminal_open_issues(open_issues: list[dict[str, Any]]) -> int:
    closed = 0
    for issue in open_issues:
        if "pull_request" in issue:
            continue
        number = int(issue["number"])
        terminal = terminal_if_latest(latest_operational(number))
        if not terminal:
            continue
        reason = "completed" if terminal.state == "DONE" else "not_planned"
        print(f"reconcile issue #{number}: latest {terminal.kind}/{terminal.state} -> closed/{reason}")
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


def dispatch_registered_route(source: OperationalRecord, cfg: dict[str, Any], transition: dict[str, Any] | None) -> bool:
    if cfg.get("type") != "workflow_dispatch":
        return False
    workflow = cfg.get("workflow")
    if not workflow or cfg.get("ref", "main") != "main":
        raise RuntimeError(f"unsafe route registration for {source.route}: exact main workflow required")
    main_sha = current_main_sha()
    if matching_fresh_run(workflow, main_sha, source.created_at):
        print(f"route {source.route}: fresh exact-main run already exists at {main_sha}")
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
        if transition:
            request("POST", f"/repos/{REPO}/issues/{int(transition['number'])}/comments", {
                "body": f"Factory dispatched `{workflow}` via `workflow_dispatch` on exact `main@{main_sha}` for route `{source.route}`. Run identity must be resolved from Actions before downstream authority is claimed."
            })
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


def materialize_missing_transitions(open_issues: list[dict[str, Any]], routes: dict[str, dict[str, Any]]) -> tuple[int, int]:
    created = dispatched = 0
    closed = list(paged(f"/repos/{REPO}/issues?state=closed&sort=updated&direction=desc&since=2026-08-20T00:00:00Z&"))
    recent_issues = [item for item in open_issues + closed if "pull_request" not in item]
    consumed_sources: set[int] = set()
    for item in recent_issues:
        consumed_sources.update(predecessor_sources(item))
    dispatch_keys: set[tuple[str, str]] = set()
    for issue in closed:
        if "pull_request" in issue:
            continue
        number = int(issue["number"])
        source = terminal_if_latest(latest_operational(number))
        if not source or not source.route or number in consumed_sources:
            continue
        transition = find_open_transition(open_issues, number)
        cfg = routes.get(source.route)
        if not transition:
            transition = create_transition(source, cfg)
            created += 1
            if transition:
                open_issues.append(transition)
        if cfg:
            key = (str(cfg.get("workflow")), current_main_sha())
            if key not in dispatch_keys and dispatch_registered_route(source, cfg, transition):
                dispatch_keys.add(key)
                dispatched += 1
    return created, dispatched


def self_test() -> None:
    def c(cid: int, kind: str, state: str, body_extra: str = "") -> dict[str, Any]:
        return {
            "id": cid,
            "author_association": "OWNER",
            "created_at": f"2026-08-25T00:00:{cid:02d}Z",
            "body": f"protocol: planning-v1\nschema: 3\nkind: {kind}\nstate: {state}\n{body_extra}",
        }

    done = c(1, "STATUS", "DONE", "required_next_route: NEXT")
    claim = c(2, "CLAIM", "IN_PROGRESS")
    assert terminal_if_latest(latest_operational_from_comments(10, [done])) is not None
    assert terminal_if_latest(latest_operational_from_comments(10, [done, claim])) is None
    assert latest_operational_from_comments(10, [done, claim]).kind == "CLAIM"

    predecessor_prose = "Predecessor review disposition: `CHANGES_NEEDED`. This PR fixes it and requires fresh review."
    assert not pr_explicitly_rejected(predecessor_prose)
    assert pr_explicitly_rejected("Disposition: `CHANGES_NEEDED` — 0 blocker / 1 major")
    assert pr_explicitly_rejected("Review disposition\nCHANGES_REQUIRED")
    assert pr_explicitly_rejected("This draft PR must not be merged.")

    outsider_done = dict(done, id=3, author_association="NONE")
    assert latest_operational_from_comments(10, [outsider_done]) is None
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
