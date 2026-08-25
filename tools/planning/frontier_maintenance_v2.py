#!/usr/bin/env python3
"""Successor-aware liveness layer for Everfield planning frontier maintenance.

This module reuses the reviewed safety/authority primitives from
frontier_maintenance.py and narrows graph-consumption/reconciliation. It never
grants planning, review, verification, integration, decision, or canonical
authority.
"""
from __future__ import annotations

from datetime import datetime, timezone
import re
import sys
from typing import Any, Iterable

import frontier_maintenance as base


# Only phrases that explicitly declare a graph relationship are recognized.
# Arbitrary issue-number mentions are intentionally ignored.
SUCCESSOR_RELATION_PATTERNS = (
    r"(?im)^\s*`?predecessor_issue:\s*(\d+)`?\s*$",
    r"(?i)\bimmediate predecessor:\s*Issue\s*#(\d+)\b",
    r"(?i)\bSource terminal issue:\s*#(\d+)\b",
    r"(?i)\b(?:remediation|review|recovery|continuation|integration|publication)\s+of\s+(?:terminal\s+)?Issue\s*#(\d+)\b",
    r"(?im)^\s*Required\s+(?:clean\s+)?(?:review|remediation|integration|continuation|publication):\s*Issue\s*#(\d+)\b",
    r"(?i)\brequired\s+by\s+terminal\s+Issue\s*#(\d+)\b",
)

TRANSITION_SOURCE_RE = re.compile(r"(?im)^\s*Source terminal issue:\s*#(\d+)\s*$")
TRANSITION_TERMINAL_COMMENT_RE = re.compile(r"(?im)^\s*Source terminal comment:\s*(\d+)\s*$")
TRANSITION_ROUTE_RE = re.compile(r"(?im)^\s*Required next route:\s*`([^`]+)`\s*$")
RESOLUTION_VERSION = "1"
RESOLUTION_DONE_DISPOSITIONS = {
    "TRANSITION_DISPATCH_ALREADY_ACCEPTED",
    "TRANSITION_DISPATCH_OBSERVED",
}
DISPATCH_GRACE_SECONDS = 15 * 60

Generation = tuple[int, int, str]
SuccessorEdgeMap = dict[int, list[tuple[str, int]]]


def trusted_issue_author(issue: dict[str, Any]) -> bool:
    login = ((issue.get("user") or {}).get("login") or "")
    return login == "github-actions[bot]" or issue.get("author_association") in base.TRUSTED_ASSOCIATIONS


def successor_issue_eligible(issue: dict[str, Any]) -> bool:
    if not trusted_issue_author(issue):
        return False
    if issue.get("state") == "closed" and issue.get("state_reason") in {"not_planned", "duplicate"}:
        return False
    return True


def predecessor_sources(issue: dict[str, Any]) -> set[int]:
    text = issue.get("body") or ""
    found: set[int] = set()
    for pattern in SUCCESSOR_RELATION_PATTERNS:
        found.update(int(value) for value in re.findall(pattern, text))
    return found


def factory_transition_source(issue: dict[str, Any]) -> int | None:
    if "pull_request" in issue:
        return None
    match = base.FACTORY_TRANSITION_RE.search(issue.get("title") or "")
    return int(match.group(1)) if match else None


def factory_transition_generation(issue: dict[str, Any]) -> Generation | None:
    title_source = factory_transition_source(issue)
    if title_source is None:
        return None
    body = issue.get("body") or ""
    source_match = TRANSITION_SOURCE_RE.search(body)
    comment_match = TRANSITION_TERMINAL_COMMENT_RE.search(body)
    route_match = TRANSITION_ROUTE_RE.search(body)
    if not source_match or not comment_match or not route_match:
        return None
    body_source = int(source_match.group(1))
    if body_source != title_source:
        return None
    return body_source, int(comment_match.group(1)), route_match.group(1).strip()


def successor_edges(issues: Iterable[dict[str, Any]]) -> SuccessorEdgeMap:
    edges: SuccessorEdgeMap = {}
    for issue in issues:
        if "pull_request" in issue or factory_transition_source(issue) is not None:
            continue
        if not successor_issue_eligible(issue):
            continue
        created_at = issue.get("created_at") or ""
        if not created_at:
            continue
        for source in predecessor_sources(issue):
            edges.setdefault(source, []).append((created_at, int(issue["number"])))
    return edges


def normal_successor_consumes(source: base.OperationalRecord, edges: SuccessorEdgeMap) -> bool:
    if not source.created_at:
        return False
    return any(created_at >= source.created_at for created_at, _ in edges.get(source.issue_number, []))


def _trusted_resolution_author(comment: dict[str, Any]) -> bool:
    login = ((comment.get("user") or {}).get("login") or "")
    return login == "github-actions[bot]" or comment.get("author_association") in base.TRUSTED_ASSOCIATIONS


def trusted_dispatch_for_generation(
    comments: Iterable[dict[str, Any]], generation: Generation
) -> dict[str, Any] | None:
    source_issue, source_terminal_comment_id, route = generation
    comments_list = list(comments)
    dispatch = base.trusted_dispatch_marker_from_comments(comments_list, source_issue, route)
    if dispatch is None:
        return None
    dispatch_body = dispatch.get("body") or ""
    if base.integer_scalar(dispatch_body, "source_terminal_comment_id") != source_terminal_comment_id:
        return None
    workflow = base.scalar(dispatch_body, "workflow")
    main_sha = base.scalar(dispatch_body, "main_sha")
    if not workflow or not main_sha or not base.SHA40_RE.fullmatch(main_sha):
        return None
    return dispatch


def transition_resolution_from_comments(
    comments: Iterable[dict[str, Any]], generation: Generation
) -> tuple[dict[str, Any], dict[str, Any]] | None:
    source_issue, source_terminal_comment_id, route = generation
    comments_list = list(comments)
    dispatch = trusted_dispatch_for_generation(comments_list, generation)
    if dispatch is None:
        return None
    dispatch_id = int(dispatch["id"])

    for comment in comments_list:
        if not _trusted_resolution_author(comment) or not base.immutable_comment(comment):
            continue
        body = comment.get("body") or ""
        if base.scalar(body, "factory_transition_resolution") != RESOLUTION_VERSION:
            continue
        if base.integer_scalar(body, "source_issue") != source_issue:
            continue
        if base.integer_scalar(body, "source_terminal_comment_id") != source_terminal_comment_id:
            continue
        if base.scalar(body, "route") != route:
            continue
        if base.scalar(body, "state") != "DONE":
            continue
        if base.scalar(body, "disposition") not in RESOLUTION_DONE_DISPOSITIONS:
            continue
        if base.integer_scalar(body, "accepted_dispatch_comment_id") != dispatch_id:
            continue
        return dispatch, comment
    return None


def workflow_run_outcome(run: dict[str, Any] | None) -> str:
    if run is None:
        return "MISSING"
    if run.get("status") != "completed":
        return "IN_FLIGHT"
    return "SUCCESS" if run.get("conclusion") == "success" else "FAILED"


def marker_within_grace(dispatch: dict[str, Any], now: datetime | None = None) -> bool:
    created_at = dispatch.get("created_at")
    if not created_at:
        return False
    try:
        created = datetime.fromisoformat(str(created_at).replace("Z", "+00:00"))
    except ValueError:
        return False
    current = now or datetime.now(timezone.utc)
    if created.tzinfo is None:
        created = created.replace(tzinfo=timezone.utc)
    return 0 <= (current - created).total_seconds() <= DISPATCH_GRACE_SECONDS


def resolved_transition_generations(closed_issues: Iterable[dict[str, Any]]) -> set[Generation]:
    consumed: set[Generation] = set()
    for issue in closed_issues:
        generation = factory_transition_generation(issue)
        if generation is None:
            continue
        comments_list = list(base.paged(f"/repos/{base.REPO}/issues/{int(issue['number'])}/comments?"))
        resolution = transition_resolution_from_comments(comments_list, generation)
        if resolution is None:
            continue
        dispatch, _ = resolution
        dispatch_body = dispatch.get("body") or ""
        workflow = base.scalar(dispatch_body, "workflow")
        main_sha = base.scalar(dispatch_body, "main_sha")
        if not workflow or not main_sha:
            continue
        run = base.matching_fresh_run(workflow, main_sha, "")
        outcome = workflow_run_outcome(run)
        if outcome in {"SUCCESS", "IN_FLIGHT"}:
            consumed.add(generation)
        elif outcome == "MISSING" and marker_within_grace(dispatch):
            consumed.add(generation)
    return consumed


def source_generation(source: base.OperationalRecord) -> Generation | None:
    if not source.route:
        return None
    return source.issue_number, source.comment_id, source.route


def source_generation_consumed(
    source: base.OperationalRecord,
    edges: SuccessorEdgeMap,
    resolved_generations: set[Generation],
) -> bool:
    generation = source_generation(source)
    if generation is not None and generation in resolved_generations:
        return True
    return normal_successor_consumes(source, edges)


def transition_has_active_operational_state(issue_number: int) -> bool:
    comments = base.paged(f"/repos/{base.REPO}/issues/{issue_number}/comments?")
    records = base.operational_records_from_comments(issue_number, comments)
    if not records:
        return False
    latest = max(records, key=lambda item: item.comment_id)
    return not (
        latest.kind in base.TERMINAL_KINDS
        and latest.state in base.TERMINAL_STATES
    )


def transition_redundancy_reason(
    transition: dict[str, Any],
    current_source: base.OperationalRecord | None,
    edges: SuccessorEdgeMap,
    resolved_generations: set[Generation],
) -> str | None:
    generation = factory_transition_generation(transition)
    if generation is None or current_source is None:
        return None
    current_generation = source_generation(current_source)
    if current_generation is None:
        return None
    if generation != current_generation:
        return "STALE_TERMINAL_GENERATION"
    if source_generation_consumed(current_source, edges, resolved_generations):
        return "SOURCE_GENERATION_ALREADY_CONSUMED"
    return None


def retire_redundant_transitions(
    open_issues: list[dict[str, Any]],
    edges: SuccessorEdgeMap,
    resolved_generations: set[Generation],
) -> int:
    retired = 0
    retained: list[dict[str, Any]] = []
    source_cache: dict[int, base.OperationalRecord | None] = {}

    for issue in open_issues:
        generation = factory_transition_generation(issue)
        if generation is None:
            retained.append(issue)
            continue
        source_issue = generation[0]
        if source_issue not in source_cache:
            source_cache[source_issue] = base.reconcilable_terminal(source_issue)
        reason = transition_redundancy_reason(
            issue, source_cache[source_issue], edges, resolved_generations
        )
        if reason is None:
            retained.append(issue)
            continue

        number = int(issue["number"])
        if transition_has_active_operational_state(number):
            print(f"preserve claimed transition #{number}: {reason}")
            retained.append(issue)
            continue

        print(f"retire redundant transition #{number}: {reason}")
        if not base.DRY_RUN:
            base.request(
                "PATCH",
                f"/repos/{base.REPO}/issues/{number}",
                {"state": "closed", "state_reason": "not_planned"},
            )
        retired += 1

    open_issues[:] = retained
    return retired


def find_matching_open_transition(
    open_issues: Iterable[dict[str, Any]], source: base.OperationalRecord
) -> dict[str, Any] | None:
    target = source_generation(source)
    if target is None:
        return None
    for issue in open_issues:
        if not trusted_issue_author(issue):
            continue
        if factory_transition_generation(issue) == target:
            return issue
    return None


def materialize_missing_transitions(
    open_issues: list[dict[str, Any]], routes: dict[str, dict[str, Any]]
) -> tuple[int, int, int]:
    created = dispatched = 0
    closed = list(
        base.paged(
            f"/repos/{base.REPO}/issues?state=closed&sort=updated&direction=desc&since=2026-08-20T00:00:00Z&"
        )
    )
    recent_issues = [item for item in open_issues + closed if "pull_request" not in item]
    edges = successor_edges(recent_issues)
    resolved_generations = resolved_transition_generations(closed)
    retired = retire_redundant_transitions(open_issues, edges, resolved_generations)

    dispatch_keys: set[tuple[str, str]] = set()
    for issue in closed:
        if "pull_request" in issue:
            continue
        number = int(issue["number"])
        source = base.reconcilable_terminal(number)
        if not source or not source.route:
            continue
        if source_generation_consumed(source, edges, resolved_generations):
            continue

        transition = find_matching_open_transition(open_issues, source)
        cfg = routes.get(source.route)
        if not transition:
            transition = base.create_transition(source, cfg)
            created += 1
            if transition:
                open_issues.append(transition)
        if cfg and transition:
            key = (str(cfg.get("workflow")), base.current_main_sha())
            if key not in dispatch_keys and base.dispatch_registered_route(source, cfg, transition):
                dispatch_keys.add(key)
                dispatched += 1
    return created, dispatched, retired


def self_test() -> None:
    base.self_test()

    assert predecessor_sources({"body": "Bounded remediation of Issue #680 terminal review."}) == {680}
    assert predecessor_sources({"body": "Fresh degraded-independent review of Issue #682 / draft PR #684."}) == {682}
    assert predecessor_sources({"body": "Required clean review: Issue #693 terminal comment 123."}) == {693}
    assert predecessor_sources({"body": "This is the single remediation route required by terminal Issue #665."}) == {665}
    assert predecessor_sources({"body": "predecessor_issue: 695"}) == {695}
    assert predecessor_sources({"body": "Context mentions Issue #680 and Issue #693, but declares no dependency."}) == set()

    trusted_successor = {
        "number": 20,
        "title": "[PLAN-v1] remediation",
        "body": "Minimal remediation of Issue #10.",
        "created_at": "2026-08-25T00:00:06Z",
        "state": "open",
        "state_reason": None,
        "author_association": "OWNER",
        "user": {"login": "vokerg"},
    }
    untrusted_successor = dict(
        trusted_successor,
        number=21,
        author_association="NONE",
        user={"login": "outsider"},
    )
    dead_successor = dict(
        trusted_successor,
        number=22,
        state="closed",
        state_reason="not_planned",
    )
    assert successor_edges([trusted_successor]) == {10: [("2026-08-25T00:00:06Z", 20)]}
    assert successor_edges([untrusted_successor]) == {}
    assert successor_edges([dead_successor]) == {}

    def source(comment_id: int, created_at: str, route: str = "NEXT") -> base.OperationalRecord:
        return base.OperationalRecord(
            issue_number=10,
            comment_id=comment_id,
            created_at=created_at,
            kind="STATUS",
            state="DONE",
            route=route,
            body="",
            declared_issue=10,
            mission_id="M-10",
            actor_session_id="actor-a",
            authority_mode="OWNER",
            ownership_generation_comment_id=1,
            head_sha="a" * 40,
            work_sha="b" * 40,
        )

    old_source = source(2, "2026-08-25T00:00:05Z")
    new_source = source(3, "2026-08-25T00:00:10Z")
    edges = successor_edges([trusted_successor])
    assert normal_successor_consumes(old_source, edges)
    assert not normal_successor_consumes(new_source, edges)

    transition = {
        "number": 30,
        "title": "[PLAN-v1][FACTORY-TRANSITION-10] Materialize required next route from #10",
        "body": "Source terminal issue: #10\nSource terminal comment: 2\nRequired next route: `NEXT`",
        "created_at": "2026-08-25T00:00:07Z",
        "author_association": "CONTRIBUTOR",
        "user": {"login": "github-actions[bot]"},
    }
    assert factory_transition_generation(transition) == (10, 2, "NEXT")

    created = "2026-08-25T00:00:08Z"
    dispatch = {
        "id": 100,
        "author_association": "NONE",
        "user": {"login": "github-actions[bot]"},
        "created_at": created,
        "updated_at": created,
        "body": (
            "factory_frontier_dispatch: 1\n"
            "source_issue: 10\n"
            "source_terminal_comment_id: 2\n"
            "route: NEXT\n"
            "status: ACCEPTED\n"
            "workflow: evaluator.yml\n"
            f"main_sha: {'c' * 40}\n"
        ),
    }
    resolution = {
        "id": 101,
        "author_association": "OWNER",
        "user": {"login": "vokerg"},
        "created_at": created,
        "updated_at": created,
        "body": (
            "factory_transition_resolution: 1\n"
            "source_issue: 10\n"
            "source_terminal_comment_id: 2\n"
            "route: NEXT\n"
            "state: DONE\n"
            "disposition: TRANSITION_DISPATCH_ALREADY_ACCEPTED\n"
            "accepted_dispatch_comment_id: 100\n"
        ),
    }
    old_generation = (10, 2, "NEXT")
    new_generation = (10, 3, "NEXT")
    pair = transition_resolution_from_comments([dispatch, resolution], old_generation)
    assert pair is not None and pair[0] is dispatch and pair[1] is resolution
    assert transition_resolution_from_comments([dispatch, resolution], new_generation) is None
    edited_resolution = dict(resolution, updated_at="2026-08-25T00:01:08Z")
    assert transition_resolution_from_comments([dispatch, edited_resolution], old_generation) is None
    wrong_dispatch = dict(resolution, body=resolution["body"].replace("100", "999"))
    assert transition_resolution_from_comments([dispatch, wrong_dispatch], old_generation) is None

    assert workflow_run_outcome(None) == "MISSING"
    assert workflow_run_outcome({"status": "queued", "conclusion": None}) == "IN_FLIGHT"
    assert workflow_run_outcome({"status": "completed", "conclusion": "success"}) == "SUCCESS"
    assert workflow_run_outcome({"status": "completed", "conclusion": "failure"}) == "FAILED"
    grace_now = datetime.fromisoformat("2026-08-25T00:10:00+00:00")
    assert marker_within_grace(dispatch, grace_now)
    late_now = datetime.fromisoformat("2026-08-25T00:30:00+00:00")
    assert not marker_within_grace(dispatch, late_now)

    resolved = {old_generation}
    assert source_generation_consumed(old_source, {}, resolved)
    assert not source_generation_consumed(new_source, {}, resolved)
    assert transition_redundancy_reason(transition, old_source, {}, resolved) == "SOURCE_GENERATION_ALREADY_CONSUMED"
    assert transition_redundancy_reason(transition, new_source, {}, resolved) == "STALE_TERMINAL_GENERATION"

    fake_transition = dict(
        transition,
        number=31,
        author_association="NONE",
        user={"login": "outsider"},
    )
    assert find_matching_open_transition([fake_transition], old_source) is None
    assert find_matching_open_transition([transition], old_source) is transition

    print("frontier maintenance v2 self-test: PASS")


def main() -> int:
    if "--self-test" in sys.argv:
        self_test()
        return 0

    open_items = list(base.paged(f"/repos/{base.REPO}/issues?state=open&sort=created&direction=asc&"))
    open_prs = list(base.paged(f"/repos/{base.REPO}/pulls?state=open&sort=created&direction=asc&"))
    issue_closed = base.close_terminal_open_issues(open_items)
    pr_closed = base.close_rejected_open_prs(open_prs)
    transition_created, dispatched, transition_retired = materialize_missing_transitions(
        open_items, base.load_routes()
    )
    print(base.json.dumps({
        "dry_run": base.DRY_RUN,
        "terminal_issues_closed": issue_closed,
        "rejected_prs_closed": pr_closed,
        "redundant_transitions_closed": transition_retired,
        "transitions_created": transition_created,
        "registered_routes_dispatched": dispatched,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
