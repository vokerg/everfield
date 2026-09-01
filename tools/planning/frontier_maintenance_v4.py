#!/usr/bin/env python3
"""Semantic-consumption ledger layer for Everfield frontier maintenance.

This module composes the reviewed v3 convergence behavior and closes one
remaining ledger gap: a trusted owner-bound factory transition that terminally
materializes or reconciles an exact semantic successor must durably consume the
exact source generation. It grants no planning, review, verification,
integration, decision, release, or canonical authority.
"""
from __future__ import annotations

import sys
from typing import Any, Iterable

import frontier_maintenance_v3 as v3

v2 = v3.v2
base = v3.base

SEMANTIC_RESOLUTION_DISPOSITIONS = {
    "EXACT_REQUIRED_REVIEW_SUCCESSOR_MATERIALIZED",
    "REQUIRED_ROUTE_ALREADY_CONSUMED_BY_TERMINAL_SUCCESSOR",
}


def _eligible_semantic_successor(issue: dict[str, Any] | None) -> bool:
    if not issue or "pull_request" in issue:
        return False
    if v2.factory_transition_source(issue) is not None:
        return False
    return v2.successor_issue_eligible(issue)


def semantic_generation_from_terminal(
    transition_issue: dict[str, Any],
    terminal: base.OperationalRecord,
    issues_by_number: dict[int, dict[str, Any]],
    *,
    successor_terminals: dict[int, base.OperationalRecord | None] | None = None,
) -> v2.Generation | None:
    """Return the exact source generation consumed by one semantic wrapper.

    The caller must obtain ``terminal`` through the reviewed schema-3 terminal
    validator. This helper additionally binds the terminal to the wrapper's
    exact source generation and to a narrowly validated real successor issue.
    """
    generation = v2.factory_transition_generation(transition_issue)
    if generation is None:
        return None
    if transition_issue.get("state") != "closed":
        return None
    if transition_issue.get("state_reason") in {"not_planned", "duplicate"}:
        return None
    if terminal.issue_number != int(transition_issue["number"]):
        return None
    if terminal.kind not in base.TERMINAL_KINDS or terminal.state != "DONE":
        return None
    if terminal.authority_mode != "OWNER":
        return None

    source_issue, source_terminal_comment_id, route = generation
    body = terminal.body
    disposition = base.scalar(body, "disposition")
    if disposition not in SEMANTIC_RESOLUTION_DISPOSITIONS:
        return None
    if base.integer_scalar(body, "source_issue") != source_issue:
        return None
    if base.integer_scalar(body, "source_terminal_comment_id") != source_terminal_comment_id:
        return None
    terminal_route = (
        base.scalar(body, "source_required_route")
        or base.scalar(body, "required_route")
    )
    if terminal_route != route:
        return None

    if disposition == "EXACT_REQUIRED_REVIEW_SUCCESSOR_MATERIALIZED":
        successor_number = base.integer_scalar(body, "successor_issue")
        successor = issues_by_number.get(successor_number or -1)
        if not _eligible_semantic_successor(successor):
            return None
        transition_created = transition_issue.get("created_at") or ""
        successor_created = successor.get("created_at") or ""
        if not transition_created or not successor_created:
            return None
        if successor_created < transition_created:
            return None
        return generation

    if base.scalar(body, "route_consumed") != "true":
        return None
    successor_number = base.integer_scalar(body, "resolved_successor_issue")
    successor_comment_id = base.integer_scalar(
        body, "resolved_successor_terminal_comment_id"
    )
    successor = issues_by_number.get(successor_number or -1)
    if not _eligible_semantic_successor(successor) or successor_comment_id is None:
        return None

    if successor_terminals is not None:
        successor_terminal = successor_terminals.get(successor_number or -1)
    else:
        successor_terminal = base.reconcilable_terminal(successor_number or -1)
    if successor_terminal is None:
        return None
    if successor_terminal.comment_id != successor_comment_id:
        return None
    return generation


def semantic_generation_from_comments(
    transition_issue: dict[str, Any],
    comments: Iterable[dict[str, Any]],
    issues_by_number: dict[int, dict[str, Any]],
) -> v2.Generation | None:
    number = int(transition_issue["number"])
    terminal = base.reconcilable_terminal_from_comments(number, comments)
    if terminal is None:
        return None
    return semantic_generation_from_terminal(
        transition_issue, terminal, issues_by_number
    )


def semantic_resolved_transition_generations(
    closed_issues: Iterable[dict[str, Any]],
    recent_issues: Iterable[dict[str, Any]],
) -> set[v2.Generation]:
    issues_by_number = {int(issue["number"]): issue for issue in recent_issues}
    consumed: set[v2.Generation] = set()
    for issue in closed_issues:
        if v2.factory_transition_generation(issue) is None:
            continue
        number = int(issue["number"])
        comments = list(base.paged(f"/repos/{base.REPO}/issues/{number}/comments?"))
        generation = semantic_generation_from_comments(
            issue, comments, issues_by_number
        )
        if generation is not None:
            consumed.add(generation)
    return consumed


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
    edges = v3.successor_edges(recent_issues)
    resolved_generations = v2.resolved_transition_generations(closed)
    resolved_generations |= semantic_resolved_transition_generations(
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
        if v2.source_generation_consumed(source, edges, resolved_generations):
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
        if not transition:
            transition = base.create_transition(source, None)
            created += 1
            if transition:
                open_issues.append(transition)
    return created, dispatched, retired


def _terminal(
    issue_number: int,
    comment_id: int,
    body: str,
) -> base.OperationalRecord:
    return base.OperationalRecord(
        issue_number=issue_number,
        comment_id=comment_id,
        created_at="2026-09-01T00:00:10Z",
        kind="STATUS",
        state="DONE",
        route=None,
        body=body,
        declared_issue=issue_number,
        mission_id=f"M-{issue_number}",
        actor_session_id=f"actor-{issue_number}",
        authority_mode="OWNER",
        ownership_generation_comment_id=1,
        head_sha="a" * 40,
        work_sha="b" * 40,
    )


def self_test() -> None:
    v3.self_test()

    transition = {
        "number": 30,
        "title": "[PLAN-v1][FACTORY-TRANSITION-10] Materialize required next route from #10",
        "body": "Source terminal issue: #10\nSource terminal comment: 2\nRequired next route: `NEXT`",
        "state": "closed",
        "state_reason": "completed",
        "created_at": "2026-09-01T00:00:05Z",
        "author_association": "CONTRIBUTOR",
        "user": {"login": "github-actions[bot]"},
    }
    successor = {
        "number": 20,
        "title": "[PLAN-v1] exact review successor",
        "body": "review of Issue #10",
        "state": "open",
        "state_reason": None,
        "created_at": "2026-09-01T00:00:06Z",
        "author_association": "OWNER",
        "user": {"login": "vokerg"},
    }
    materialized_body = (
        "disposition: EXACT_REQUIRED_REVIEW_SUCCESSOR_MATERIALIZED\n"
        "source_issue: 10\n"
        "source_terminal_comment_id: 2\n"
        "source_required_route: NEXT\n"
        "successor_issue: 20\n"
    )
    materialized = _terminal(30, 4, materialized_body)
    issues = {20: successor, 30: transition}
    assert semantic_generation_from_terminal(transition, materialized, issues) == (
        10,
        2,
        "NEXT",
    )

    wrong_generation = _terminal(
        30,
        5,
        materialized_body.replace("source_terminal_comment_id: 2", "source_terminal_comment_id: 99"),
    )
    assert semantic_generation_from_terminal(transition, wrong_generation, issues) is None

    untrusted_successor = dict(successor)
    untrusted_successor["author_association"] = "NONE"
    untrusted_successor["user"] = {"login": "outsider"}
    assert semantic_generation_from_terminal(
        transition, materialized, {20: untrusted_successor, 30: transition}
    ) is None

    transition_successor = dict(successor)
    transition_successor["title"] = (
        "[PLAN-v1][FACTORY-TRANSITION-99] Materialize required next route from #99"
    )
    transition_successor["body"] = (
        "Source terminal issue: #99\nSource terminal comment: 7\nRequired next route: `X`"
    )
    assert semantic_generation_from_terminal(
        transition, materialized, {20: transition_successor, 30: transition}
    ) is None

    existing_body = (
        "disposition: REQUIRED_ROUTE_ALREADY_CONSUMED_BY_TERMINAL_SUCCESSOR\n"
        "source_issue: 10\n"
        "source_terminal_comment_id: 2\n"
        "source_required_route: NEXT\n"
        "resolved_successor_issue: 20\n"
        "resolved_successor_terminal_comment_id: 50\n"
        "route_consumed: true\n"
    )
    existing = _terminal(30, 6, existing_body)
    successor_terminal = _terminal(20, 50, "disposition: DONE\n")
    assert semantic_generation_from_terminal(
        transition,
        existing,
        issues,
        successor_terminals={20: successor_terminal},
    ) == (10, 2, "NEXT")
    assert semantic_generation_from_terminal(
        transition,
        existing,
        issues,
        successor_terminals={20: _terminal(20, 51, "disposition: DONE\n")},
    ) is None

    wrong_disposition = _terminal(
        30,
        7,
        materialized_body.replace(
            "EXACT_REQUIRED_REVIEW_SUCCESSOR_MATERIALIZED", "UNTRUSTED_SHORTCUT"
        ),
    )
    assert semantic_generation_from_terminal(
        transition, wrong_disposition, issues
    ) is None
    assert semantic_generation_from_comments(transition, [], issues) is None

    print("frontier maintenance v4 self-test: PASS")


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
    transition_created, dispatched, transition_retired = materialize_missing_transitions(
        open_items, base.load_routes()
    )
    print(
        base.json.dumps(
            {
                "dry_run": base.DRY_RUN,
                "terminal_issues_closed": issue_closed,
                "rejected_prs_closed": pr_closed,
                "redundant_transitions_closed": transition_retired,
                "transitions_created": transition_created,
                "registered_routes_dispatched": dispatched,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
