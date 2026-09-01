#!/usr/bin/env python3
"""Convergence layer for Everfield planning frontier maintenance.

This module composes the reviewed v1/v2 safety primitives while fixing routing
blind spots that stranded REVIEW_READY chains and allowed transition recursion.
It never grants planning, review, verification, integration, decision, or
canonical authority.
"""
from __future__ import annotations

import re
import sys
from typing import Any, Iterable

import frontier_maintenance_v2 as v2

base = v2.base

ROUTABLE_TERMINAL_STATES = base.TERMINAL_STATES | {"REVIEW_READY"}
NO_ROUTE_SENTINELS = {"NONE_FROM_THIS_TRANSITION"}
ADDITIONAL_SUCCESSOR_RELATION_PATTERNS = (
    r"(?i)\brecovery transition:\s*#(\d+)\b",
    r"(?im)^\s*source_transition_issue:\s*(\d+)\s*$",
)


def route_is_actionable(route: str | None) -> bool:
    return bool(route and route not in NO_ROUTE_SENTINELS)


def routable_terminal_from_comments(
    issue_number: int, comments: Iterable[dict[str, Any]]
) -> base.OperationalRecord | None:
    """Return an owner-bound terminal episode that can drive liveness routing.

    REVIEW_READY is routable but intentionally remains outside base.TERMINAL_STATES,
    so this does not broaden automatic GitHub issue closure semantics.
    """
    records = base.operational_records_from_comments(issue_number, comments)
    if not records:
        return None
    latest = max(records, key=lambda item: item.comment_id)
    if latest.kind not in base.TERMINAL_KINDS or latest.state not in ROUTABLE_TERMINAL_STATES:
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
    if not base.SHA40_RE.fullmatch(latest.head_sha) or not base.SHA40_RE.fullmatch(latest.work_sha):
        return None

    owner = next(
        (record for record in records if record.comment_id == latest.ownership_generation_comment_id),
        None,
    )
    if owner is None or owner.comment_id >= latest.comment_id:
        return None
    if owner.kind not in base.OWNERSHIP_KINDS:
        return None
    if owner.declared_issue != issue_number:
        return None
    if owner.actor_session_id != latest.actor_session_id:
        return None
    if owner.mission_id != latest.mission_id:
        return None
    return latest


def routable_terminal(issue_number: int) -> base.OperationalRecord | None:
    return routable_terminal_from_comments(
        issue_number,
        base.paged(f"/repos/{base.REPO}/issues/{issue_number}/comments?"),
    )


def predecessor_sources(issue: dict[str, Any]) -> set[int]:
    found = set(v2.predecessor_sources(issue))
    text = issue.get("body") or ""
    for pattern in ADDITIONAL_SUCCESSOR_RELATION_PATTERNS:
        found.update(int(value) for value in re.findall(pattern, text))
    return found


def successor_edges(issues: Iterable[dict[str, Any]]) -> v2.SuccessorEdgeMap:
    edges: v2.SuccessorEdgeMap = {}
    for issue in issues:
        if "pull_request" in issue or v2.factory_transition_source(issue) is not None:
            continue
        if not v2.successor_issue_eligible(issue):
            continue
        created_at = issue.get("created_at") or ""
        if not created_at:
            continue
        for source in predecessor_sources(issue):
            edges.setdefault(source, []).append((created_at, int(issue["number"])))
    return edges


def transition_redundancy_reason(
    transition: dict[str, Any],
    current_source: base.OperationalRecord | None,
    edges: v2.SuccessorEdgeMap,
    resolved_generations: set[v2.Generation],
    factory_issue_numbers: set[int],
) -> str | None:
    generation = v2.factory_transition_generation(transition)
    if generation is None:
        return None
    source_issue, _, route = generation
    if not route_is_actionable(route):
        return "NO_ROUTE_SENTINEL"
    if source_issue in factory_issue_numbers:
        return "FACTORY_TRANSITION_SOURCE_RECURSION"
    if current_source is None:
        return None
    current_generation = v2.source_generation(current_source)
    if current_generation is None:
        return None
    if generation != current_generation:
        return "STALE_TERMINAL_GENERATION"
    if v2.source_generation_consumed(current_source, edges, resolved_generations):
        return "SOURCE_GENERATION_ALREADY_CONSUMED"
    return None


def retire_redundant_transitions(
    open_issues: list[dict[str, Any]],
    edges: v2.SuccessorEdgeMap,
    resolved_generations: set[v2.Generation],
    factory_issue_numbers: set[int],
) -> int:
    retired = 0
    retained: list[dict[str, Any]] = []
    source_cache: dict[int, base.OperationalRecord | None] = {}

    for issue in open_issues:
        generation = v2.factory_transition_generation(issue)
        if generation is None:
            retained.append(issue)
            continue
        source_issue = generation[0]
        if source_issue not in source_cache and source_issue not in factory_issue_numbers:
            source_cache[source_issue] = routable_terminal(source_issue)
        reason = transition_redundancy_reason(
            issue,
            source_cache.get(source_issue),
            edges,
            resolved_generations,
            factory_issue_numbers,
        )
        if reason is None:
            retained.append(issue)
            continue

        number = int(issue["number"])
        if v2.transition_has_active_operational_state(number):
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
    resolved_generations = v2.resolved_transition_generations(closed)
    factory_issue_numbers = {
        int(item["number"])
        for item in recent_issues
        if v2.factory_transition_source(item) is not None
    }
    retired = retire_redundant_transitions(
        open_issues, edges, resolved_generations, factory_issue_numbers
    )

    dispatch_keys: set[tuple[str, str]] = set()
    for issue in closed:
        if "pull_request" in issue:
            continue
        number = int(issue["number"])
        if number in factory_issue_numbers:
            continue
        source = routable_terminal(number)
        if not source or not route_is_actionable(source.route):
            continue
        if v2.source_generation_consumed(source, edges, resolved_generations):
            continue

        transition = v2.find_matching_open_transition(open_issues, source)
        cfg = routes.get(source.route)
        if not transition:
            transition = base.create_transition(source, cfg)
            created += 1
            if transition:
                open_issues.append(transition)
        if cfg and transition:
            key = (str(cfg.get("workflow")), base.current_main_sha())
            if key not in dispatch_keys and v2.dispatch_registered_route(source, cfg, transition):
                dispatch_keys.add(key)
                dispatched += 1
    return created, dispatched, retired


def _comment(
    cid: int,
    kind: str,
    state: str,
    *,
    issue: int = 10,
    actor: str = "actor-a",
    mission: str = "M-10",
    extra: str = "",
) -> dict[str, Any]:
    created = f"2026-08-25T00:00:{cid:02d}Z"
    return {
        "id": cid,
        "author_association": "OWNER",
        "user": {"login": "vokerg"},
        "created_at": created,
        "updated_at": created,
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


def self_test() -> None:
    v2.self_test()

    claim = _comment(1, "CLAIM", "IN_PROGRESS")
    review_ready = _comment(
        2,
        "STATUS",
        "REVIEW_READY",
        extra=(
            "authority_mode: OWNER\n"
            "ownership_generation_comment_id: 1\n"
            f"head_sha: {'a' * 40}\n"
            f"work_sha: {'b' * 40}\n"
            "required_next_route: FRESH_REVIEW\n"
        ),
    )
    assert base.reconcilable_terminal_from_comments(10, [claim, review_ready]) is None
    routed = routable_terminal_from_comments(10, [claim, review_ready])
    assert routed is not None and routed.state == "REVIEW_READY" and routed.route == "FRESH_REVIEW"

    assert route_is_actionable("FRESH_REVIEW")
    assert not route_is_actionable("NONE_FROM_THIS_TRANSITION")
    assert not route_is_actionable(None)

    recovery_successor = {
        "number": 20,
        "title": "[PLAN-v1] remediation",
        "body": "- recovery transition: #10 ownership comment 123",
        "created_at": "2026-08-25T00:00:06Z",
        "state": "closed",
        "state_reason": "completed",
        "author_association": "OWNER",
        "user": {"login": "vokerg"},
    }
    assert predecessor_sources(recovery_successor) == {10}
    assert successor_edges([recovery_successor]) == {10: [("2026-08-25T00:00:06Z", 20)]}

    source = base.OperationalRecord(
        issue_number=10,
        comment_id=2,
        created_at="2026-08-25T00:00:05Z",
        kind="STATUS",
        state="DONE",
        route="NEXT",
        body="",
        declared_issue=10,
        mission_id="M-10",
        actor_session_id="actor-a",
        authority_mode="OWNER",
        ownership_generation_comment_id=1,
        head_sha="a" * 40,
        work_sha="b" * 40,
    )
    transition = {
        "number": 30,
        "title": "[PLAN-v1][FACTORY-TRANSITION-10] Materialize required next route from #10",
        "body": "Source terminal issue: #10\nSource terminal comment: 2\nRequired next route: `NEXT`",
    }
    none_transition = {
        "number": 31,
        "title": "[PLAN-v1][FACTORY-TRANSITION-10] Materialize required next route from #10",
        "body": "Source terminal issue: #10\nSource terminal comment: 2\nRequired next route: `NONE_FROM_THIS_TRANSITION`",
    }
    recursive_transition = {
        "number": 32,
        "title": "[PLAN-v1][FACTORY-TRANSITION-30] Materialize required next route from #30",
        "body": "Source terminal issue: #30\nSource terminal comment: 9\nRequired next route: `NEXT`",
    }
    assert transition_redundancy_reason(transition, source, {}, set(), set()) is None
    assert transition_redundancy_reason(none_transition, source, {}, set(), set()) == "NO_ROUTE_SENTINEL"
    assert transition_redundancy_reason(recursive_transition, None, {}, set(), {30}) == "FACTORY_TRANSITION_SOURCE_RECURSION"

    consumed_edges = successor_edges([recovery_successor])
    assert transition_redundancy_reason(transition, source, consumed_edges, set(), set()) == "SOURCE_GENERATION_ALREADY_CONSUMED"

    print("frontier maintenance v3 self-test: PASS")


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
