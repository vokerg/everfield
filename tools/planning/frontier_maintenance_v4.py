#!/usr/bin/env python3
"""Semantic-consumption ledger layer for Everfield frontier maintenance.

This module composes the reviewed v3 convergence behavior and closes one
remaining ledger gap: a trusted owner-bound factory transition that terminally
materializes or reconciles an exact semantic successor must durably consume the
exact source generation. It grants no planning, review, verification,
integration, decision, release, or canonical authority.
"""
from __future__ import annotations

import re
import sys
from typing import Any, Iterable

import frontier_maintenance_v3 as v3

v2 = v3.v2
base = v3.base

SEMANTIC_RESOLUTION_DISPOSITIONS = {
    "EXACT_REQUIRED_REVIEW_SUCCESSOR_MATERIALIZED",
    "REQUIRED_ROUTE_ALREADY_CONSUMED_BY_TERMINAL_SUCCESSOR",
}
MATERIALIZED_SUCCESSOR_RELATION_PATTERNS = (
    r"(?i)\bfactory transition\s*#(\d+)\b",
    r"(?im)^\s*source_transition_issue:\s*(\d+)\s*$",
)


def _eligible_semantic_successor(issue: dict[str, Any] | None) -> bool:
    if not issue or "pull_request" in issue:
        return False
    if v2.factory_transition_source(issue) is not None:
        return False
    return v2.successor_issue_eligible(issue)


def _successor_binds_transition(
    successor: dict[str, Any], transition_issue_number: int
) -> bool:
    text = successor.get("body") or ""
    for pattern in MATERIALIZED_SUCCESSOR_RELATION_PATTERNS:
        if transition_issue_number in {
            int(value) for value in re.findall(pattern, text)
        }:
            return True
    return False


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
    if not v2.trusted_issue_author(transition_issue):
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

    # FSR-1745-M01: an authenticated *successor* cannot legitimize a terminal
    # issued by a losing/expired *transition wrapper* owner. Authenticate
    # the complete fresh comment stream, first-winner and six-hour lease
    # before either materialized or already-consumed early-return path.
    wrapper_number = int(transition_issue["number"])
    try:
        live_wrapper_comments = list(base.paged(
            f"/repos/{base.REPO}/issues/{wrapper_number}/comments?"
        ))
        real_wrapper = base.closure_authorized_terminal_from_comments(
            wrapper_number, live_wrapper_comments,
        )
    except (RuntimeError, ValueError, TypeError, KeyError, AttributeError):
        return None
    if real_wrapper is None or real_wrapper != terminal:
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
        if not _successor_binds_transition(successor, int(transition_issue["number"])):
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

    # FSR-1733-M01: A matching live Git commit is NOT proof that the
    # terminal was issued by the winning, in-lease schema-3 owner. The
    # reconciliation parser alone checks syntactic linkage, not contention,
    # recovery, PROGRESS or canonical six-hour expiry. Load the COMPLETE live
    # GitHub comment stream even when an injected terminal map was supplied;
    # injected/earlier snapshots may not confer ownership authority.
    try:
        authenticated = base.closure_authorized_terminal_from_comments(
            successor_number,
            base.paged(f"/repos/{base.REPO}/issues/{successor_number}/comments?"),
        )
    except (RuntimeError, ValueError, TypeError, KeyError, AttributeError):
        return None
    if (
        authenticated is None
        or authenticated.issue_number != successor_number
        or authenticated.comment_id != successor_comment_id
        or authenticated.kind not in base.TERMINAL_KINDS
        or authenticated.state != "DONE"
        or authenticated.authority_mode != "OWNER"
        or (
            successor_terminals is not None
            and successor_terminals.get(successor_number) != authenticated
        )
        # Retain an explicit exact result-head check even though the strict
        # closure validator authenticates both SHAs, including in mock tests.
        or not base.github_verified_terminal_result_heads(
            successor_number, authenticated.head_sha, authenticated.work_sha
        )
    ):
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
    # FSR-1716-M01: syntax/owner linkage is not source-commit provenance.
    # A semantic-generation consumption can suppress live successor work.
    # Authenticate BOTH terminal result SHAs against one live task branch tip.
    if not base.github_verified_terminal_result_heads(
        number, terminal.head_sha, terminal.work_sha
    ):
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

    # Read-only authenticated-wrapper fixture: tests below exercise actual
    # semantic consumption, while a separate live-validator adversarial suite
    # verifies winning owner / six-hour terminal independently.
    outer_paged = base.paged
    outer_closure = base.closure_authorized_terminal_from_comments
    authorized_wrapper: base.OperationalRecord | None = None
    def wrapper_paged(path: str) -> Iterable[dict[str, Any]]:
        if path == f"/repos/{base.REPO}/issues/30/comments?":
            return iter([{"id": 1}])
        return outer_paged(path)
    def wrapper_closure(number: int, comments: Iterable[dict[str, Any]]) -> base.OperationalRecord | None:
        items = list(comments)
        if number == 30:
            return authorized_wrapper if items else None
        return outer_closure(number, items)
    base.paged = wrapper_paged
    base.closure_authorized_terminal_from_comments = wrapper_closure

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
        "body": "Exact successor materialized from factory transition #30.",
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
    authorized_wrapper = materialized
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

    wrong_route = _terminal(
        30,
        6,
        materialized_body.replace("source_required_route: NEXT", "source_required_route: OTHER"),
    )
    assert semantic_generation_from_terminal(transition, wrong_route, issues) is None

    untrusted_transition = dict(transition)
    untrusted_transition["author_association"] = "NONE"
    untrusted_transition["user"] = {"login": "outsider"}
    assert semantic_generation_from_terminal(
        untrusted_transition, materialized, issues
    ) is None

    not_planned_transition = dict(transition)
    not_planned_transition["state_reason"] = "not_planned"
    assert semantic_generation_from_terminal(
        not_planned_transition, materialized, issues
    ) is None

    duplicate_transition = dict(transition)
    duplicate_transition["state_reason"] = "duplicate"
    assert semantic_generation_from_terminal(
        duplicate_transition, materialized, issues
    ) is None

    assert semantic_generation_from_terminal(
        transition, materialized, {30: transition}
    ) is None

    untrusted_successor = dict(successor)
    untrusted_successor["author_association"] = "NONE"
    untrusted_successor["user"] = {"login": "outsider"}
    assert semantic_generation_from_terminal(
        transition, materialized, {20: untrusted_successor, 30: transition}
    ) is None

    unbound_successor = dict(successor)
    unbound_successor["body"] = "Review of Issue #10 without a transition binding."
    assert semantic_generation_from_terminal(
        transition, materialized, {20: unbound_successor, 30: transition}
    ) is None

    transition_successor = dict(successor)
    transition_successor["title"] = (
        "[PLAN-v1][FACTORY-TRANSITION-99] Materialize required next route from #99"
    )
    transition_successor["body"] = (
        "Source terminal issue: #99\nSource terminal comment: 7\nRequired next route: `X`\n"
        "source_transition_issue: 30"
    )
    assert semantic_generation_from_terminal(
        transition, materialized, {20: transition_successor, 30: transition}
    ) is None

    older_successor = dict(successor)
    older_successor["created_at"] = "2026-09-01T00:00:04Z"
    assert semantic_generation_from_terminal(
        transition, materialized, {20: older_successor, 30: transition}
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
    existing = _terminal(30, 7, existing_body)
    authorized_wrapper = existing
    successor_terminal = _terminal(20, 50, "disposition: DONE\n")
    # FSR-1725-M01: run the actual successor SHA verifier with two separate
    # mocked task refs and honest GitHub compare responses. It must validate
    # the *successor* even where wrapper result SHAs have already been checked.
    original_successor_reader = base.reconcilable_terminal
    original_successor_request = base.request
    original_wrapper_parser = base.reconcilable_terminal_from_comments
    original_successor_paged = base.paged
    original_successor_closure = base.closure_authorized_terminal_from_comments
    successor_tip = "a" * 40
    successor_ancestors = {"b" * 40}
    successor_result = successor_terminal
    compare_status = "ahead"
    api_calls: list[str] = []

    def successor_request(method: str, path: str, *args: Any) -> dict[str, Any]:
        if method != "GET":
            raise AssertionError("unexpected GitHub mutation in security test")
        api_calls.append(path)
        prefix = f"/repos/{base.REPO}"
        if path == prefix + "/git/ref/heads/planning/issue-20":
            return {"object": {"sha": successor_tip}}
        if path == prefix + "/git/ref/heads/planning/issue-30":
            return {"object": {"sha": "a" * 40}}
        if path.startswith(prefix + "/compare/"):
            start, end = path.rsplit("/", 1)[-1].split("...", 1)
            if end == successor_tip and start in successor_ancestors:
                return (
                    {"status": compare_status, "ahead_by": 1,
                     "behind_by": 0 if compare_status == "ahead" else 1}
                )
            if end == "a" * 40 and start == "b" * 40:
                return {"status": "ahead", "ahead_by": 1, "behind_by": 0}
            return {"status": "diverged", "ahead_by": 1, "behind_by": 1}
        raise RuntimeError("unrecognized read-only endpoint")

    try:
        base.request = successor_request
        base.paged = lambda path: iter([{"id": 50}]) if (
            path.endswith("/issues/20/comments?") or path.endswith("/issues/30/comments?")
        ) else iter([])
        base.closure_authorized_terminal_from_comments = (
            lambda number, comments: (
                successor_result if number == 20 and list(comments)
                else authorized_wrapper if number == 30 and list(comments)
                else None
            )
        )
        base.reconcilable_terminal = lambda number: (
            successor_result if number == 20 else None
        )
        base.reconcilable_terminal_from_comments = lambda number, comments: (
            existing if number == 30 and list(comments) else None
        )
        # Positive same-tip and benign behind-free ancestor; no false drop.
        assert semantic_generation_from_terminal(
            transition, existing, issues, successor_terminals={20: successor_terminal}
        ) == (10, 2, "NEXT")
        assert semantic_generation_from_terminal(
            transition, existing, issues
        ) == (10, 2, "NEXT")
        assert semantic_generation_from_comments(
            transition, [object()], issues
        ) == (10, 2, "NEXT")
        assert any("/git/ref/heads/planning/issue-20" in p for p in api_calls)
        assert any("/git/ref/heads/planning/issue-30" in p for p in api_calls)
        assert semantic_generation_from_terminal(
            transition, existing, issues,
            successor_terminals={20: _terminal(20, 51, "disposition: DONE\n")}
        ) is None
        # Independently forge only the successor's HEAD, WORK, then both;
        # even a fully authenticated wrapper must not consume this route.
        for false_head, false_work in (
            ("c" * 40, "b" * 40),
            ("a" * 40, "c" * 40),
            ("c" * 40, "c" * 40),
        ):
            successor_result = successor_terminal.__class__(**{
                **vars(successor_terminal), "head_sha": false_head,
                "work_sha": false_work,
            })
            assert semantic_generation_from_terminal(
                transition, existing, issues
            ) is None
            assert semantic_generation_from_comments(
                transition, [object()], issues
            ) is None
        successor_result = successor_terminal
        # A missing/deleted/moved ref, diverged/behind/unknown comparison,
        # wrong target issue or malformed source SHA fail closed.
        successor_tip = ""
        assert semantic_generation_from_terminal(transition, existing, issues) is None
        successor_tip = "c" * 40
        successor_ancestors = set()
        assert semantic_generation_from_terminal(transition, existing, issues) is None
        successor_tip = "a" * 40
        successor_ancestors = {"b" * 40}
        for compare_status in ("diverged", "behind", "unknown"):
            assert semantic_generation_from_terminal(transition, existing, issues) is None
        compare_status = "ahead"
        successor_result = successor_terminal.__class__(**{
            **vars(successor_terminal), "issue_number": 99
        })
        assert semantic_generation_from_terminal(transition, existing, issues) is None
        successor_result = successor_terminal.__class__(**{
            **vars(successor_terminal), "head_sha": "not-a-sha"
        })
        assert semantic_generation_from_terminal(transition, existing, issues) is None
        successor_result = successor_terminal
        base.request = lambda *args, **kwargs: (_ for _ in ()).throw(
            RuntimeError("GitHub ref/compare unavailable")
        )
        assert semantic_generation_from_terminal(transition, existing, issues) is None
    finally:
        base.reconcilable_terminal = original_successor_reader
        base.request = original_successor_request
        base.reconcilable_terminal_from_comments = original_wrapper_parser
        base.closure_authorized_terminal_from_comments = original_successor_closure
        base.paged = original_successor_paged

    # FSR-1733-M01: call the ACTUAL strict base closure validator, not a
    # source-authored replacement. Valid branch ancestry cannot rescue either
    # a losing CLAIM or a terminal published after the six-hour lease.
    def live_comment(cid: int, created: str, operational: str) -> dict[str, Any]:
        return {
            "id": cid, "created_at": created, "updated_at": created,
            "author_association": "OWNER", "user": {"login": "vokerg"},
            "body": operational,
        }

    def owner_capsule(cid: int, actor: str) -> str:
        return (
            "protocol: planning-v1\n"
            "schema: 3\n"
            "kind: CLAIM\n"
            "issue: 20\n"
            "mission_id: M-20\n"
            "branch: planning/issue-20\n"
            f"actor_session_id: {actor}\n"
            "state: IN_PROGRESS\n"
            f"observed_head_sha: {'a' * 40}\n"
            "previous_ownership_comment_id: null\n"
        )

    def done_capsule(actor: str, owner_id: int) -> str:
        return (
            "protocol: planning-v1\n"
            "schema: 3\n"
            "kind: STATUS\n"
            "issue: 20\n"
            "mission_id: M-20\n"
            "branch: planning/issue-20\n"
            f"actor_session_id: {actor}\n"
            "state: DONE\n"
            "terminal: true\n"
            "authority_mode: OWNER\n"
            f"ownership_generation_comment_id: {owner_id}\n"
            f"head_sha: {'a' * 40}\n"
            f"work_sha: {'b' * 40}\n"
        )

    original_live_paged = base.paged
    original_live_request = base.request
    first_claim = live_comment(
        40, "2026-09-01T00:00:00Z", owner_capsule(40, "actor-20")
    )
    genuine_done = live_comment(
        50, "2026-09-01T00:00:10Z", done_capsule("actor-20", 40)
    )
    parsed_done = base.parse_operational(20, genuine_done)
    assert parsed_done is not None
    live_successor_comments = [first_claim, genuine_done]
    try:
        base.request = successor_request
        base.paged = lambda path: (
            iter(live_successor_comments) if path == f"/repos/{base.REPO}/issues/20/comments?"
            else iter([{"id": 1}]) if path == f"/repos/{base.REPO}/issues/30/comments?"
            else iter([])
        )
        successor_tip = "a" * 40
        successor_ancestors = {"b" * 40}
        compare_status = "ahead"
        # Validate the genuine owner and both authenticated result SHAs.
        assert base.closure_authorized_terminal_from_comments(
            20, live_successor_comments
        ) == parsed_done
        assert semantic_generation_from_terminal(
            transition, existing, issues, successor_terminals={20: parsed_done}
        ) == (10, 2, "NEXT")
        assert semantic_generation_from_terminal(
            transition, existing, issues
        ) == (10, 2, "NEXT")

        # A later losing claimant, even with both true tip/ancestor SHAs,
        # cannot publish a terminal suppressing required downstream work.
        losing_claim = live_comment(
            45, "2026-09-01T00:00:05Z", owner_capsule(45, "losing-actor")
        )
        losing_done = live_comment(
            50, "2026-09-01T00:00:10Z", done_capsule("losing-actor", 45)
        )
        losing_record = base.parse_operational(20, losing_done)
        assert losing_record is not None
        live_successor_comments = [first_claim, losing_claim, losing_done]
        assert base.closure_authorized_terminal_from_comments(
            20, live_successor_comments
        ) is None
        assert semantic_generation_from_terminal(
            transition, existing, issues, successor_terminals={20: losing_record}
        ) is None
        assert semantic_generation_from_terminal(
            transition, existing, issues
        ) is None

        # Expiry is based on immutable GitHub created_at, not supplied SHA.
        expired_done = live_comment(
            50, "2026-09-01T07:00:10Z", done_capsule("actor-20", 40)
        )
        expired_record = base.parse_operational(20, expired_done)
        assert expired_record is not None
        live_successor_comments = [first_claim, expired_done]
        assert semantic_generation_from_terminal(
            transition, existing, issues, successor_terminals={20: expired_record}
        ) is None
        assert semantic_generation_from_terminal(
            transition, existing, issues
        ) is None

        # Even an otherwise valid injected snapshot must match the full live
        # terminal identity; callers cannot inject a different actor/result.
        live_successor_comments = [first_claim, genuine_done]
        assert semantic_generation_from_terminal(
            transition, existing, issues, successor_terminals={20: losing_record}
        ) is None
        edited_done = dict(genuine_done, updated_at="2026-09-01T00:00:11Z")
        live_successor_comments = [first_claim, edited_done]
        assert semantic_generation_from_terminal(
            transition, existing, issues, successor_terminals={20: parsed_done}
        ) is None
        base.paged = lambda path: (_ for _ in ()).throw(
            RuntimeError("incomplete GitHub comments pagination")
        )
        assert semantic_generation_from_terminal(
            transition, existing, issues, successor_terminals={20: parsed_done}
        ) is None
    finally:
        base.paged = original_live_paged
        base.request = original_live_request

    route_not_consumed = _terminal(
        30,
        8,
        existing_body.replace("route_consumed: true", "route_consumed: false"),
    )
    assert semantic_generation_from_terminal(
        transition,
        route_not_consumed,
        issues,
        successor_terminals={20: successor_terminal},
    ) is None

    wrong_disposition = _terminal(
        30,
        9,
        materialized_body.replace(
            "EXACT_REQUIRED_REVIEW_SUCCESSOR_MATERIALIZED", "UNTRUSTED_SHORTCUT"
        ),
    )
    assert semantic_generation_from_terminal(
        transition, wrong_disposition, issues
    ) is None
    assert semantic_generation_from_comments(transition, [], issues) is None

    # FSR-1716-M01: exercise the actual semantic consumption predicate with
    # the real live-branch GitHub comparison helper, not a copied regex.
    # Only terminal parsing and GitHub I/O are mocked; no live PATCH.
    original_parser = base.reconcilable_terminal_from_comments
    original_request = base.request
    terminal_for_test = materialized
    authorized_wrapper = terminal_for_test
    tip = "a" * 40
    ancestors = {"b" * 40}
    api_calls: list[str] = []
    def mocked_request(method: str, path: str, *args: Any) -> dict[str, Any]:
        if method != "GET":
            raise AssertionError("unexpected mutation")
        api_calls.append(path)
        if path == f"/repos/{base.REPO}/git/ref/heads/planning/issue-30":
            return {"object": {"sha": tip}}
        if path.startswith(f"/repos/{base.REPO}/compare/"):
            candidate = path.rsplit("/", 1)[-1].split("...", 1)[0]
            return (
                {"status": "ahead", "ahead_by": 1, "behind_by": 0}
                if candidate in ancestors
                else {"status": "diverged", "ahead_by": 1, "behind_by": 1}
            )
        raise AssertionError("unknown read-only GitHub request")
    try:
        base.reconcilable_terminal_from_comments = lambda number, comments: (
            terminal_for_test if number == 30 and list(comments) else None
        )
        base.request = mocked_request
        assert semantic_generation_from_comments(transition, [1], issues) == (10, 2, "NEXT")
        assert any("/compare/" in path for path in api_calls)
        terminal_for_test = materialized.__class__(**{
            **vars(materialized), "work_sha": "a" * 40
        })
        authorized_wrapper = terminal_for_test
        assert semantic_generation_from_comments(transition, [1], issues) == (10, 2, "NEXT")
        for fake_head, fake_work in (
            ("c" * 40, "a" * 40),
            ("a" * 40, "c" * 40),
            ("c" * 40, "c" * 40),
        ):
            terminal_for_test = materialized.__class__(**{
                **vars(materialized), "head_sha": fake_head, "work_sha": fake_work
            })
            assert semantic_generation_from_comments(transition, [1], issues) is None
        terminal_for_test = materialized
        tip, ancestors = "c" * 40, set()
        assert semantic_generation_from_comments(transition, [1], issues) is None
        tip = ""
        assert semantic_generation_from_comments(transition, [1], issues) is None
        base.request = lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError("ref unavailable"))
        assert semantic_generation_from_comments(transition, [1], issues) is None
    finally:
        base.reconcilable_terminal_from_comments = original_parser
        base.request = original_request

    base.paged = outer_paged
    base.closure_authorized_terminal_from_comments = outer_closure

    # FSR-1745-M01: exercise the REAL imported strict closure validator on
    # the WRAPPER, not only its successor. A SHA-authenticated losing owner
    # or a seven-hour terminal cannot suppress a required successor.
    def wrapper_capsule(actor: str, owner_id: int) -> str:
        return (
            done_capsule(actor, owner_id)
            .replace("issue: 20\\n", "issue: 30\\n")
            .replace("mission_id: M-20\\n", "mission_id: M-30\\n")
            .replace("branch: planning/issue-20\\n", "branch: planning/issue-30\\n")
            + materialized_body
        )

    def wrapper_claim(actor: str) -> str:
        return (
            owner_capsule(40, actor)
            .replace("issue: 20\\n", "issue: 30\\n")
            .replace("mission_id: M-20\\n", "mission_id: M-30\\n")
            .replace("branch: planning/issue-20\\n", "branch: planning/issue-30\\n")
        )

    root_prefix = f"/repos/{base.REPO}"
    def wrapper_request(method: str, path: str, *args: Any) -> dict[str, Any]:
        if method != "GET":
            raise RuntimeError("no mutating GitHub API in adversarial test")
        if path == root_prefix + "/git/ref/heads/planning/issue-30":
            return {"object": {"sha": "a" * 40}}
        if path == root_prefix + "/compare/" + "b" * 40 + "..." + "a" * 40:
            return {"status": "ahead", "ahead_by": 1, "behind_by": 0}
        raise RuntimeError(f"unrecognized wrapper-proof endpoint: {path}")

    valid_claim = live_comment(
        40, "2026-09-01T00:00:00Z", wrapper_claim("actor-30")
    )
    valid_terminal_comment = live_comment(
        50, "2026-09-01T00:00:10Z", wrapper_capsule("actor-30", 40)
    )
    wrapper_terminal = base.parse_operational(30, valid_terminal_comment)
    assert wrapper_terminal is not None
    live_wrapper_comments = [valid_claim, valid_terminal_comment]
    saved_wrapper_request, saved_wrapper_paged = base.request, base.paged
    try:
        base.request = wrapper_request
        base.paged = lambda path: (
            iter(live_wrapper_comments)
            if path == root_prefix + "/issues/30/comments?"
            else iter([])
        )
        assert base.closure_authorized_terminal_from_comments(
            30, live_wrapper_comments
        ) == wrapper_terminal
        assert semantic_generation_from_terminal(
            transition, wrapper_terminal, issues
        ) == (10, 2, "NEXT")
        assert semantic_generation_from_comments(
            transition, live_wrapper_comments, issues
        ) == (10, 2, "NEXT")

        losing_claim = live_comment(
            45, "2026-09-01T00:00:05Z", wrapper_claim("losing-actor")
        )
        losing_done = live_comment(
            50, "2026-09-01T00:00:10Z", wrapper_capsule("losing-actor", 45)
        )
        losing_terminal = base.parse_operational(30, losing_done)
        assert losing_terminal is not None
        live_wrapper_comments = [valid_claim, losing_claim, losing_done]
        assert base.closure_authorized_terminal_from_comments(
            30, live_wrapper_comments
        ) is None
        assert semantic_generation_from_terminal(
            transition, losing_terminal, issues
        ) is None
        assert semantic_generation_from_comments(
            transition, live_wrapper_comments, issues
        ) is None

        expired_done = live_comment(
            50, "2026-09-01T07:00:10Z", wrapper_capsule("actor-30", 40)
        )
        expired_terminal = base.parse_operational(30, expired_done)
        assert expired_terminal is not None
        live_wrapper_comments = [valid_claim, expired_done]
        assert base.closure_authorized_terminal_from_comments(
            30, live_wrapper_comments
        ) is None
        assert semantic_generation_from_terminal(
            transition, expired_terminal, issues
        ) is None
        assert semantic_generation_from_comments(
            transition, live_wrapper_comments, issues
        ) is None

        live_wrapper_comments = [valid_claim, valid_terminal_comment]
        base.request = lambda *args, **kwargs: (_ for _ in ()).throw(
            RuntimeError("wrapper GitHub ref unavailable")
        )
        assert semantic_generation_from_terminal(
            transition, wrapper_terminal, issues
        ) is None
    finally:
        base.request, base.paged = saved_wrapper_request, saved_wrapper_paged

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
