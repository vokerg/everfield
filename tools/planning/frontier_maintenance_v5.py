#!/usr/bin/env python3
"""Exact-generation dedupe and explicit-successor routing for frontier maintenance.

This layer composes v4. It prevents repeated factory wrapper creation for the
same exact source generation and consumes routes that explicitly name an
already-existing trusted successor issue. It grants no planning, review,
verification, integration, decision, release, or canonical authority.
"""
from __future__ import annotations

import re
import sys
from typing import Any, Iterable

import frontier_maintenance_v4 as v4

v3 = v4.v3
v2 = v4.v2
base = v4.base

EXPLICIT_SUCCESSOR_ROUTE_PATTERNS = (
    re.compile(r"(?:^|_)ISSUE_(\d+)(?:_|$)"),
    re.compile(r"(?:^|_)INTEGRATION_(?:ISSUE_)?(\d+)(?:_|$)"),
    re.compile(r"(?:^|_)REVIEW_(?:ISSUE_)?(\d+)(?:_|$)"),
    re.compile(r"(?:^|_)REMEDIATION_(?:ISSUE_)?(\d+)(?:_|$)"),
)


def explicit_successor_issue_number(route: str | None) -> int | None:
    """Return one unambiguous issue number explicitly encoded by a route."""
    if not route:
        return None
    matches: set[int] = set()
    for pattern in EXPLICIT_SUCCESSOR_ROUTE_PATTERNS:
        matches.update(int(value) for value in pattern.findall(route))
    return next(iter(matches)) if len(matches) == 1 else None


def explicit_successor_generation_consumed(
    source: base.OperationalRecord,
    issues_by_number: dict[int, dict[str, Any]],
) -> bool:
    """Recognize a route-declared successor without inventing a graph edge.

    The route must encode exactly one issue number and that issue must already
    exist as a trusted/eligible non-PR, non-transition issue. This only proves
    liveness materialization; it does not grant any authority to the successor.
    """
    successor_number = explicit_successor_issue_number(source.route)
    if successor_number is None:
        return False
    successor = issues_by_number.get(successor_number)
    if successor is None:
        return False
    if "pull_request" in successor or v2.factory_transition_source(successor) is not None:
        return False
    if not v2.successor_issue_eligible(successor):
        return False
    print(
        f"route {source.route}: explicit trusted successor issue #{successor_number} already exists"
    )
    return True


def explicit_transition_redundancy_reason(
    transition: dict[str, Any],
    current_source: base.OperationalRecord | None,
    issues_by_number: dict[int, dict[str, Any]],
) -> str | None:
    generation = v2.factory_transition_generation(transition)
    if generation is None or current_source is None:
        return None
    current_generation = v2.source_generation(current_source)
    if current_generation is None or generation != current_generation:
        return None
    if explicit_successor_generation_consumed(current_source, issues_by_number):
        return "EXPLICIT_SUCCESSOR_ALREADY_EXISTS"
    return None


def retire_explicit_successor_transitions(
    open_issues: list[dict[str, Any]],
    issues_by_number: dict[int, dict[str, Any]],
) -> int:
    """Close unowned wrappers made unnecessary by an explicit route successor."""
    retired = 0
    retained: list[dict[str, Any]] = []
    source_cache: dict[int, base.OperationalRecord | None] = {}
    for issue in open_issues:
        generation = v2.factory_transition_generation(issue)
        if generation is None:
            retained.append(issue)
            continue
        source_issue = generation[0]
        if source_issue not in source_cache:
            source_cache[source_issue] = v3.routable_terminal(source_issue)
        reason = explicit_transition_redundancy_reason(
            issue, source_cache[source_issue], issues_by_number
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


def transition_generations(
    issues: Iterable[dict[str, Any]],
) -> dict[v2.Generation, list[dict[str, Any]]]:
    found: dict[v2.Generation, list[dict[str, Any]]] = {}
    for issue in issues:
        generation = v2.factory_transition_generation(issue)
        if generation is None or not v2.trusted_issue_author(issue):
            continue
        found.setdefault(generation, []).append(issue)
    return found


def stable_transition_for_generation(
    generation: v2.Generation,
    transitions_by_generation: dict[v2.Generation, list[dict[str, Any]]],
) -> dict[str, Any] | None:
    """Return one existing wrapper to reuse instead of creating another.

    Prefer an open wrapper. Otherwise reuse the newest duplicate/not-planned
    wrapper by reopening it. A completed wrapper is never reopened here.
    """
    candidates = transitions_by_generation.get(generation, [])
    open_candidates = [item for item in candidates if item.get("state") == "open"]
    if open_candidates:
        return max(open_candidates, key=lambda item: int(item["number"]))

    reopenable = [
        item
        for item in candidates
        if item.get("state") == "closed"
        and item.get("state_reason") in {"duplicate", "not_planned"}
    ]
    if not reopenable:
        return None
    chosen = max(reopenable, key=lambda item: int(item["number"]))
    print(
        f"reuse transition #{int(chosen['number'])} for exact generation {generation}; reopen instead of duplicating"
    )
    if not base.DRY_RUN:
        base.request(
            "PATCH",
            f"/repos/{base.REPO}/issues/{int(chosen['number'])}",
            {"state": "open"},
        )
    chosen["state"] = "open"
    chosen["state_reason"] = None
    return chosen


def materialize_missing_transitions(
    open_issues: list[dict[str, Any]], routes: dict[str, dict[str, Any]]
) -> tuple[int, int, int, int]:
    created = dispatched = reused = 0
    closed = list(
        base.paged(
            f"/repos/{base.REPO}/issues?state=closed&sort=updated&direction=desc&since=2026-08-20T00:00:00Z&"
        )
    )
    recent_issues = [item for item in open_issues + closed if "pull_request" not in item]
    issues_by_number = {int(item["number"]): item for item in recent_issues}
    edges = v3.successor_edges(recent_issues)
    resolved_generations = v2.resolved_transition_generations(closed)
    resolved_generations |= v4.semantic_resolved_transition_generations(
        closed, recent_issues
    )
    factory_issue_numbers = {
        int(item["number"])
        for item in recent_issues
        if v2.factory_transition_source(item) is not None
    }
    registered_routes = set(routes)
    retired = v3.retire_redundant_transitions(
        open_issues,
        edges,
        resolved_generations,
        factory_issue_numbers,
        registered_routes,
    )
    retired += retire_explicit_successor_transitions(
        open_issues, issues_by_number
    )

    # Rebuild after retirement because the live list may have changed, while
    # retaining closed history for exact-generation reuse.
    recent_issues = [item for item in open_issues + closed if "pull_request" not in item]
    issues_by_number = {int(item["number"]): item for item in recent_issues}
    transitions_by_generation = transition_generations(recent_issues)

    dispatch_keys: set[tuple[str, str]] = set()
    seen_source_numbers: set[int] = set()
    for issue in recent_issues:
        number = int(issue["number"])
        if number in seen_source_numbers:
            continue
        seen_source_numbers.add(number)
        source = v3.routable_terminal(number)
        if not source or not v3.route_is_actionable(source.route):
            continue
        generation = v2.source_generation(source)
        if generation is None:
            continue
        if v2.source_generation_consumed(source, edges, resolved_generations):
            continue
        if explicit_successor_generation_consumed(source, issues_by_number):
            continue

        cfg = routes.get(source.route)
        if cfg is not None:
            key = (str(cfg.get("workflow")), base.current_main_sha())
            if key not in dispatch_keys and v3.direct_dispatch_registered_route(
                source, cfg, issue
            ):
                dispatch_keys.add(key)
                dispatched += 1
            continue

        if number in factory_issue_numbers:
            print(
                f"skip unregistered transition-source recursion from #{number}: {source.route}"
            )
            continue

        transition = v2.find_matching_open_transition(open_issues, source)
        if transition is None:
            transition = stable_transition_for_generation(
                generation, transitions_by_generation
            )
            if transition is not None:
                reused += 1
                if transition not in open_issues:
                    open_issues.append(transition)
        if transition is None:
            transition = base.create_transition(source, None)
            created += 1
            if transition:
                open_issues.append(transition)
                transitions_by_generation.setdefault(generation, []).append(transition)
    return created, dispatched, retired, reused


def self_test() -> None:
    v4.self_test()

    assert explicit_successor_issue_number("ISSUE_895_FORMAL_ENGINE_SELECTION_READINESS_DECISION_GATE") == 895
    assert explicit_successor_issue_number("EXISTING_REQUIRED_REVIEW_917") == 917
    assert explicit_successor_issue_number("BLOCKING_REMEDIATION_ISSUE_833") == 833
    assert explicit_successor_issue_number("AUTHORIZED_INTEGRATION_ISSUE_819_EXACT_HEAD") == 819
    assert explicit_successor_issue_number("CONTINUE_AUTHORIZED_INTEGRATION_788_WITH_PR_793_AFTER_VERIFY") == 788
    assert explicit_successor_issue_number("NO_EXPLICIT_TARGET") is None
    assert explicit_successor_issue_number("ISSUE_10_THEN_ISSUE_11") is None

    source = base.OperationalRecord(
        issue_number=10,
        comment_id=2,
        created_at="2026-09-08T00:00:00Z",
        kind="STATUS",
        state="DONE",
        route="EXISTING_REQUIRED_REVIEW_917",
        body="",
        declared_issue=10,
        mission_id="M-10",
        actor_session_id="actor-10",
        authority_mode="OWNER",
        ownership_generation_comment_id=1,
        head_sha="a" * 40,
        work_sha="b" * 40,
    )
    trusted_successor = {
        "number": 917,
        "title": "[PLAN-v1] required review",
        "body": "review",
        "state": "open",
        "state_reason": None,
        "author_association": "OWNER",
        "user": {"login": "vokerg"},
    }
    assert explicit_successor_generation_consumed(source, {917: trusted_successor})
    assert not explicit_successor_generation_consumed(source, {})
    dead_successor = dict(trusted_successor, state="closed", state_reason="duplicate")
    assert not explicit_successor_generation_consumed(source, {917: dead_successor})

    generation = (10, 2, "EXISTING_REQUIRED_REVIEW_917")
    wrapper = {
        "number": 100,
        "title": "[PLAN-v1][FACTORY-TRANSITION-10] Materialize required next route from #10",
        "body": (
            "Source terminal issue: #10\n"
            "Source terminal comment: 2\n"
            "Required next route: `EXISTING_REQUIRED_REVIEW_917`"
        ),
        "state": "open",
        "state_reason": None,
        "author_association": "CONTRIBUTOR",
        "user": {"login": "github-actions[bot]"},
    }
    assert explicit_transition_redundancy_reason(
        wrapper, source, {917: trusted_successor, 100: wrapper}
    ) == "EXPLICIT_SUCCESSOR_ALREADY_EXISTS"

    old = dict(
        wrapper,
        state="closed",
        state_reason="duplicate",
        body="Source terminal issue: #10\nSource terminal comment: 2\nRequired next route: `NEXT`",
    )
    old_generation = (10, 2, "NEXT")
    open_wrapper = dict(old, number=101, state="open", state_reason=None)
    mapping = transition_generations([old, open_wrapper])
    assert mapping[old_generation] == [old, open_wrapper]
    assert stable_transition_for_generation(old_generation, mapping) is open_wrapper

    completed = dict(old, number=102, state_reason="completed")
    assert stable_transition_for_generation(
        old_generation, {old_generation: [completed]}
    ) is None

    print("frontier maintenance v5 self-test: PASS")


def main() -> int:
    if "--self-test" in sys.argv:
        self_test()
        return 0
    open_items = list(
        base.paged(f"/repos/{base.REPO}/issues?state=open&sort=created&direction=asc&")
    )
    open_prs = list(
        base.paged(f"/repos/{base.REPO}/pulls?state=open&sort=created&direction=asc&")
    )
    issue_closed = base.close_terminal_open_issues(open_items)
    pr_closed = base.close_rejected_open_prs(open_prs)
    transition_created, dispatched, transition_retired, transition_reused = (
        materialize_missing_transitions(open_items, base.load_routes())
    )
    print(
        base.json.dumps(
            {
                "dry_run": base.DRY_RUN,
                "terminal_issues_closed": issue_closed,
                "rejected_prs_closed": pr_closed,
                "redundant_transitions_closed": transition_retired,
                "transitions_created": transition_created,
                "transitions_reused": transition_reused,
                "registered_routes_dispatched": dispatched,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
