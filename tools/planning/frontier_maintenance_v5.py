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
from typing import Any, Callable, Iterable

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

TERMINAL_NO_ROUTE_STATES = {"DONE", "SUPERSEDED"}

def terminal_owner_generation_is_current(
    transition_issue_number: int,
    terminal: base.OperationalRecord,
    comments: Iterable[dict[str, Any]],
) -> bool:
    """Fail closed unless the terminal references the winning owner generation.

    The shared v1 terminal parser proves linkage to one trusted ownership
    record. This liveness-suppressing v5 consumer additionally reconstructs the
    winning ownership chain for the terminal mission. Initial CLAIM contention
    is first-valid-wins; RESUME/RECOVER generations must bind the winning
    RESUME_INTENT and the current generation. Losing contenders therefore have
    zero authority effect.
    """
    records = sorted(
        (
            record
            for record in base.operational_records_from_comments(
                transition_issue_number, comments
            )
            if record.declared_issue == transition_issue_number
            and record.mission_id == terminal.mission_id
            and record.comment_id < terminal.comment_id
        ),
        key=lambda record: record.comment_id,
    )
    by_id = {record.comment_id: record for record in records}
    used_intents: set[int] = set()

    def winning_intent_for(grant: base.OperationalRecord) -> base.OperationalRecord | None:
        intent_id = base.integer_scalar(grant.body, "winning_intent_comment_id")
        observed_head = base.scalar(grant.body, "observed_head_sha")
        if grant.kind == "RESUME":
            reason = "HANDOFF"
            source_id = base.integer_scalar(grant.body, "source_status_comment_id")
        else:
            reason = base.scalar(grant.body, "recovery_reason")
            source_id = base.integer_scalar(grant.body, "source_comment_id")
        if (
            intent_id is None
            or source_id is None
            or observed_head is None
            or not base.SHA40_RE.fullmatch(observed_head)
        ):
            return None

        contenders = [
            record
            for record in records
            if record.kind == "RESUME_INTENT"
            and record.comment_id < grant.comment_id
            and record.actor_session_id
            and base.scalar(record.body, "reason") == reason
            and base.integer_scalar(record.body, "source_comment_id") == source_id
            and base.scalar(record.body, "observed_head_sha") == observed_head
        ]
        if not contenders:
            return None
        intent = min(contenders, key=lambda record: record.comment_id)
        if (
            intent.comment_id != intent_id
            or intent.actor_session_id != grant.actor_session_id
            or intent.comment_id in used_intents
        ):
            return None
        return intent

    winner: base.OperationalRecord | None = None
    for record in records:
        if (
            record.kind not in base.OWNERSHIP_KINDS
            or record.state != "IN_PROGRESS"
            or not record.actor_session_id
        ):
            continue

        previous_owner = base.integer_scalar(
            record.body, "previous_ownership_comment_id"
        )
        observed_head = base.scalar(record.body, "observed_head_sha")
        if observed_head is None or not base.SHA40_RE.fullmatch(observed_head):
            continue

        if record.kind == "CLAIM":
            base_sha = base.scalar(record.body, "base_sha")
            if (
                winner is None
                and previous_owner is None
                and base_sha is not None
                and base.SHA40_RE.fullmatch(base_sha)
            ):
                winner = record
            continue

        if record.kind not in {"RESUME", "RECOVER"}:
            continue

        intent = winning_intent_for(record)
        if intent is None:
            continue

        if record.kind == "RESUME":
            source_id = base.integer_scalar(record.body, "source_status_comment_id")
            source = by_id.get(source_id) if source_id is not None else None
            if (
                winner is not None
                and previous_owner == winner.comment_id
                and source is not None
                and source.kind == "STATUS"
                and source.state == "HANDOFF_READY"
                and source.ownership_generation_comment_id == winner.comment_id
            ):
                winner = record
                used_intents.add(intent.comment_id)
            continue

        recovery_reason = base.scalar(record.body, "recovery_reason")
        source_id = base.integer_scalar(record.body, "source_comment_id")
        source = by_id.get(source_id) if source_id is not None else None
        if recovery_reason == "STALE":
            source_matches_winner = (
                winner is not None
                and source is not None
                and (
                    source.comment_id == winner.comment_id
                    or (
                        source.kind == "PROGRESS"
                        and source.ownership_generation_comment_id
                        == winner.comment_id
                    )
                )
            )
            if (
                source_matches_winner
                and previous_owner == winner.comment_id
            ):
                winner = record
                used_intents.add(intent.comment_id)
        elif recovery_reason == "ORPHAN":
            if (
                winner is None
                and previous_owner is None
                and source is not None
                and source.kind == "ORPHAN_PROBE"
            ):
                winner = record
                used_intents.add(intent.comment_id)

    return (
        winner is not None
        and winner.comment_id == terminal.ownership_generation_comment_id
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


def terminal_no_route_generation_from_comments(
    transition_issue: dict[str, Any],
    comments: Iterable[dict[str, Any]],
) -> v2.Generation | None:
    """Resolve one exact wrapper generation from a trusted terminal no-route outcome.

    This is intentionally narrower than general terminal handling: INVALIDATED
    remains unresolved, and an actionable terminal route cannot suppress future
    liveness work.
    """
    generation = v2.factory_transition_generation(transition_issue)
    if generation is None or not v2.trusted_issue_author(transition_issue):
        return None
    if transition_issue.get("state") != "closed":
        return None

    number = int(transition_issue["number"])
    comments_list = list(comments)
    terminal = base.reconcilable_terminal_from_comments(number, comments_list)
    if terminal is None or terminal.state not in TERMINAL_NO_ROUTE_STATES:
        return None
    if not terminal_owner_generation_is_current(
        number, terminal, comments_list
    ):
        return None
    if v3.route_is_actionable(terminal.route):
        return None
    return generation


def v5_resolved_transition_generations(
    closed_issues: Iterable[dict[str, Any]],
    recent_issues: Iterable[dict[str, Any]],
) -> set[v2.Generation]:
    """Compose v4 semantic consumption with terminal no-route resolution.

    Comments are fetched once per closed transition for both checks, avoiding a
    third API pass while preserving all existing v4 validation.
    """
    issues_by_number = {int(issue["number"]): issue for issue in recent_issues}
    consumed: set[v2.Generation] = set()
    for issue in closed_issues:
        if v2.factory_transition_generation(issue) is None:
            continue
        number = int(issue["number"])
        comments = list(base.paged(f"/repos/{base.REPO}/issues/{number}/comments?"))

        semantic = v4.semantic_generation_from_comments(
            issue, comments, issues_by_number
        )
        if semantic is not None:
            consumed.add(semantic)

        terminal_no_route = terminal_no_route_generation_from_comments(
            issue, comments
        )
        if terminal_no_route is not None:
            consumed.add(terminal_no_route)
    return consumed


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
    *,
    active_state_checker: Callable[[int], bool] | None = None,
    perform_reopen: bool = True,
) -> dict[str, Any] | None:
    """Return one existing wrapper to reuse instead of creating another.

    Prefer an open wrapper. Otherwise reuse the newest duplicate/not-planned
    wrapper only when it has no live trusted schema-3 operational state. A
    completed wrapper is never reopened here. The injectable checker/reopen
    switch exists only to keep the deterministic self-test network-free.
    """
    candidates = transitions_by_generation.get(generation, [])
    open_candidates = [item for item in candidates if item.get("state") == "open"]
    if open_candidates:
        return max(open_candidates, key=lambda item: int(item["number"]))

    checker = active_state_checker or v2.transition_has_active_operational_state
    reopenable = [
        item
        for item in candidates
        if item.get("state") == "closed"
        and item.get("state_reason") in {"duplicate", "not_planned"}
        and not checker(int(item["number"]))
    ]
    if not reopenable:
        return None
    chosen = max(reopenable, key=lambda item: int(item["number"]))
    print(
        f"reuse transition #{int(chosen['number'])} for exact generation {generation}; reopen instead of duplicating"
    )
    if perform_reopen and not base.DRY_RUN:
        base.request(
            "PATCH",
            f"/repos/{base.REPO}/issues/{int(chosen['number'])}",
            {"state": "open"},
        )
    if perform_reopen:
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
    resolved_generations |= v5_resolved_transition_generations(
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
    assert stable_transition_for_generation(
        old_generation,
        mapping,
        active_state_checker=lambda _: False,
        perform_reopen=False,
    ) is open_wrapper

    chosen_closed = stable_transition_for_generation(
        old_generation,
        {old_generation: [old]},
        active_state_checker=lambda _: False,
        perform_reopen=False,
    )
    assert chosen_closed is old
    assert stable_transition_for_generation(
        old_generation,
        {old_generation: [old]},
        active_state_checker=lambda _: True,
        perform_reopen=False,
    ) is None

    completed = dict(old, number=102, state_reason="completed")
    assert stable_transition_for_generation(
        old_generation,
        {old_generation: [completed]},
        active_state_checker=lambda _: False,
        perform_reopen=False,
    ) is None

    terminal_wrapper = {
        "number": 103,
        "title": "[PLAN-v1][FACTORY-TRANSITION-10] Materialize required next route from #10",
        "body": (
            "Source terminal issue: #10\n"
            "Source terminal comment: 2\n"
            "Required next route: `NEXT`"
        ),
        "state": "closed",
        "state_reason": "not_planned",
        "author_association": "CONTRIBUTOR",
        "user": {"login": "github-actions[bot]"},
    }
    terminal_claim = v3._comment(
        1,
        "CLAIM",
        "IN_PROGRESS",
        issue=103,
        actor="actor-103",
        mission="M-103",
    )
    superseded_no_route = v3._comment(
        2,
        "STATUS",
        "SUPERSEDED",
        issue=103,
        actor="actor-103",
        mission="M-103",
        extra=(
            "authority_mode: OWNER\n"
            "ownership_generation_comment_id: 1\n"
            f"head_sha: {'a' * 40}\n"
            f"work_sha: {'b' * 40}\n"
            "required_next_route: NONE_SOURCE_ROUTE_ALREADY_CONSUMED\n"
        ),
    )
    assert terminal_no_route_generation_from_comments(
        terminal_wrapper, [terminal_claim, superseded_no_route]
    ) == (10, 2, "NEXT")

    done_null_route = v3._comment(
        3,
        "STATUS",
        "DONE",
        issue=103,
        actor="actor-103",
        mission="M-103",
        extra=(
            "authority_mode: OWNER\n"
            "ownership_generation_comment_id: 1\n"
            f"head_sha: {'a' * 40}\n"
            f"work_sha: {'b' * 40}\n"
            "required_next_route: null\n"
        ),
    )
    assert terminal_no_route_generation_from_comments(
        terminal_wrapper, [terminal_claim, done_null_route]
    ) == (10, 2, "NEXT")

    invalidated = v3._comment(
        4,
        "STATUS",
        "INVALIDATED",
        issue=103,
        actor="actor-103",
        mission="M-103",
        extra=(
            "authority_mode: OWNER\n"
            "ownership_generation_comment_id: 1\n"
            f"head_sha: {'a' * 40}\n"
            f"work_sha: {'b' * 40}\n"
            "required_next_route: NONE\n"
        ),
    )
    assert terminal_no_route_generation_from_comments(
        terminal_wrapper, [terminal_claim, invalidated]
    ) is None

    superseded_actionable = v3._comment(
        5,
        "STATUS",
        "SUPERSEDED",
        issue=103,
        actor="actor-103",
        mission="M-103",
        extra=(
            "authority_mode: OWNER\n"
            "ownership_generation_comment_id: 1\n"
            f"head_sha: {'a' * 40}\n"
            f"work_sha: {'b' * 40}\n"
            "required_next_route: REQUIRED_REVIEW\n"
        ),
    )
    assert terminal_no_route_generation_from_comments(
        terminal_wrapper, [terminal_claim, superseded_actionable]
    ) is None

    untrusted_wrapper = dict(
        terminal_wrapper,
        author_association="NONE",
        user={"login": "outsider"},
    )
    assert terminal_no_route_generation_from_comments(
        untrusted_wrapper, [terminal_claim, superseded_no_route]
    ) is None
    open_terminal_wrapper = dict(terminal_wrapper, state="open", state_reason=None)
    assert terminal_no_route_generation_from_comments(
        open_terminal_wrapper, [terminal_claim, superseded_no_route]
    ) is None

    recovery_intent = v3._comment(
        6,
        "RESUME_INTENT",
        "IN_PROGRESS",
        issue=103,
        actor="actor-103-b",
        mission="M-103",
        extra=(
            "reason: STALE\n"
            "source_comment_id: 1\n"
            f"observed_head_sha: {'c' * 40}\n"
        ),
    )
    recovered_owner = v3._comment(
        7,
        "RECOVER",
        "IN_PROGRESS",
        issue=103,
        actor="actor-103-b",
        mission="M-103",
        extra=(
            "recovery_reason: STALE\n"
            f"observed_head_sha: {'c' * 40}\n"
            "previous_ownership_comment_id: 1\n"
            "winning_intent_comment_id: 6\n"
            "source_comment_id: 1\n"
        ),
    )
    stale_prior_owner_terminal = v3._comment(
        8,
        "STATUS",
        "SUPERSEDED",
        issue=103,
        actor="actor-103",
        mission="M-103",
        extra=(
            "authority_mode: OWNER\n"
            "ownership_generation_comment_id: 1\n"
            f"head_sha: {'a' * 40}\n"
            f"work_sha: {'b' * 40}\n"
            "required_next_route: NONE_SOURCE_ROUTE_ALREADY_CONSUMED\n"
        ),
    )
    ownership_race = [
        terminal_claim,
        recovery_intent,
        recovered_owner,
        stale_prior_owner_terminal,
    ]
    # The shared parser accepts this stale-A terminal because it validates the
    # referenced prior owner but not ownership supersession. v5 must not.
    assert base.reconcilable_terminal_from_comments(103, ownership_race) is not None
    assert terminal_no_route_generation_from_comments(
        terminal_wrapper, ownership_race
    ) is None

    current_owner_terminal = v3._comment(
        9,
        "STATUS",
        "SUPERSEDED",
        issue=103,
        actor="actor-103-b",
        mission="M-103",
        extra=(
            "authority_mode: OWNER\n"
            "ownership_generation_comment_id: 7\n"
            f"head_sha: {'c' * 40}\n"
            f"work_sha: {'d' * 40}\n"
            "required_next_route: NONE_SOURCE_ROUTE_ALREADY_CONSUMED\n"
        ),
    )
    assert terminal_no_route_generation_from_comments(
        terminal_wrapper,
        [terminal_claim, recovery_intent, recovered_owner, current_owner_terminal],
    ) == (10, 2, "NEXT")

    losing_duplicate_claim = v3._comment(
        9,
        "CLAIM",
        "IN_PROGRESS",
        issue=103,
        actor="actor-103-c",
        mission="M-103",
    )
    current_owner_after_losing_claim = v3._comment(
        10,
        "STATUS",
        "SUPERSEDED",
        issue=103,
        actor="actor-103-b",
        mission="M-103",
        extra=(
            "authority_mode: OWNER\n"
            "ownership_generation_comment_id: 7\n"
            f"head_sha: {'c' * 40}\n"
            f"work_sha: {'d' * 40}\n"
            "required_next_route: NONE_SOURCE_ROUTE_ALREADY_CONSUMED\n"
        ),
    )
    losing_claim_race = [
        terminal_claim,
        recovery_intent,
        recovered_owner,
        losing_duplicate_claim,
        current_owner_after_losing_claim,
    ]
    assert base.reconcilable_terminal_from_comments(103, losing_claim_race) is not None
    assert terminal_no_route_generation_from_comments(
        terminal_wrapper, losing_claim_race
    ) == (10, 2, "NEXT")

    losing_duplicate_recover = v3._comment(
        9,
        "RECOVER",
        "IN_PROGRESS",
        issue=103,
        actor="actor-103-c",
        mission="M-103",
        extra=(
            "recovery_reason: STALE\n"
            f"observed_head_sha: {'e' * 40}\n"
            "previous_ownership_comment_id: 1\n"
            "winning_intent_comment_id: 6\n"
            "source_comment_id: 1\n"
        ),
    )
    losing_recover_race = [
        terminal_claim,
        recovery_intent,
        recovered_owner,
        losing_duplicate_recover,
        current_owner_after_losing_claim,
    ]
    assert terminal_no_route_generation_from_comments(
        terminal_wrapper, losing_recover_race
    ) == (10, 2, "NEXT")

    print("frontier maintenance v5 self-test: PASS")


def main() -> int:
    if "--self-test" in sys.argv:
        self_test()
        return 0
    try:
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
    except base.GitHubRateLimitExceeded as exc:
        print(f"::warning title=Frontier maintenance deferred::{exc}")
        print(
            base.json.dumps(
                {
                    "authority_created": False,
                    "deferred": True,
                    "deferred_reason": "GITHUB_API_RATE_LIMIT",
                    "dry_run": base.DRY_RUN,
                    "reconciliation_complete": False,
                },
                sort_keys=True,
            )
        )
        return 0

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
                "reconciliation_complete": True,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
