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

STABLE_TRANSITION_TERMINAL_STATES = {"DONE", "SUPERSEDED"}


def terminal_owner_generation_is_current(
    transition_issue_number: int,
    terminal: base.OperationalRecord,
    comments: Iterable[dict[str, Any]],
) -> bool:
    """Validate winning ownership plus canonical temporal recovery predicates."""
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

    def valid_handoff(owner: base.OperationalRecord, before_comment_id: int) -> bool:
        for record in records:
            if not (owner.comment_id < record.comment_id < before_comment_id):
                continue
            if (
                record.kind == "STATUS"
                and record.state == "HANDOFF_READY"
                and record.ownership_generation_comment_id == owner.comment_id
                and record.actor_session_id == owner.actor_session_id
                and base.schema3_owner_unexpired_at(owner, records, record) is True
            ):
                return True
        return False

    def stale_source_valid(
        owner: base.OperationalRecord,
        source: base.OperationalRecord,
        at_record: base.OperationalRecord,
    ) -> bool:
        state = base.schema3_ownership_lease_state(
            owner, records, before_comment_id=at_record.comment_id
        )
        unexpired = base.schema3_owner_unexpired_at(owner, records, at_record)
        return bool(
            state is not None
            and unexpired is False
            and source.comment_id == state.anchor_comment_id
            and not valid_handoff(owner, at_record.comment_id)
        )

    def winning_intent_for(
        grant: base.OperationalRecord,
        current_owner: base.OperationalRecord | None,
    ) -> base.OperationalRecord | None:
        intent_id = base.integer_scalar(grant.body, "winning_intent_comment_id")
        observed_head = base.scalar(grant.body, "observed_head_sha")
        if grant.kind == "RESUME":
            reason = "HANDOFF"
            source_id = base.integer_scalar(grant.body, "source_status_comment_id")
        else:
            reason = base.scalar(grant.body, "recovery_reason")
            source_id = base.integer_scalar(grant.body, "source_comment_id")
        source = by_id.get(source_id) if source_id is not None else None
        if (
            intent_id is None
            or source is None
            or observed_head is None
            or not base.SHA40_RE.fullmatch(observed_head)
        ):
            return None

        contenders: list[base.OperationalRecord] = []
        for record in records:
            if (
                record.kind != "RESUME_INTENT"
                or record.comment_id >= grant.comment_id
                or not record.actor_session_id
                or base.scalar(record.body, "reason") != reason
                or base.integer_scalar(record.body, "source_comment_id") != source_id
                or base.scalar(record.body, "observed_head_sha") != observed_head
            ):
                continue
            if reason == "HANDOFF":
                if (
                    current_owner is None
                    or source.kind != "STATUS"
                    or source.state != "HANDOFF_READY"
                    or source.ownership_generation_comment_id != current_owner.comment_id
                    or source.actor_session_id != current_owner.actor_session_id
                    or base.schema3_owner_unexpired_at(
                        current_owner, records, source
                    )
                    is not True
                ):
                    continue
            elif reason == "STALE":
                if (
                    current_owner is None
                    or not stale_source_valid(current_owner, source, record)
                ):
                    continue
            elif reason == "ORPHAN":
                if (
                    current_owner is not None
                    or source.kind != "ORPHAN_PROBE"
                    or base.schema3_orphan_probe_mature_at(source, record) is not True
                ):
                    continue
            else:
                continue
            contenders.append(record)

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
            or base.parse_github_server_time(record.created_at) is None
        ):
            continue
        observed_head = base.scalar(record.body, "observed_head_sha")
        if observed_head is None or not base.SHA40_RE.fullmatch(observed_head):
            continue
        previous_owner = base.integer_scalar(
            record.body, "previous_ownership_comment_id"
        )

        if record.kind == "CLAIM":
            if winner is None and previous_owner is None:
                winner = record
            continue
        if record.kind not in {"RESUME", "RECOVER"}:
            continue

        intent = winning_intent_for(record, winner)
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
                and source.actor_session_id == winner.actor_session_id
                and base.schema3_owner_unexpired_at(winner, records, source) is True
            ):
                winner = record
                used_intents.add(intent.comment_id)
            continue

        recovery_reason = base.scalar(record.body, "recovery_reason")
        source_id = base.integer_scalar(record.body, "source_comment_id")
        source = by_id.get(source_id) if source_id is not None else None
        if recovery_reason == "STALE":
            if (
                winner is not None
                and source is not None
                and previous_owner == winner.comment_id
                and stale_source_valid(winner, source, record)
            ):
                winner = record
                used_intents.add(intent.comment_id)
        elif recovery_reason == "ORPHAN":
            if (
                winner is None
                and previous_owner is None
                and source is not None
                and source.kind == "ORPHAN_PROBE"
                and base.schema3_orphan_probe_mature_at(source, record) is True
            ):
                winner = record
                used_intents.add(intent.comment_id)

    return bool(
        winner is not None
        and winner.comment_id == terminal.ownership_generation_comment_id
        and base.schema3_owner_unexpired_at(winner, records, terminal) is True
        and not valid_handoff(winner, terminal.comment_id)
    )


def terminal_no_route_generation_from_comments(
    transition_issue: dict[str, Any],
    comments: Iterable[dict[str, Any]],
) -> v2.Generation | None:
    generation = v2.factory_transition_generation(transition_issue)
    if generation is None or not v2.trusted_issue_author(transition_issue):
        return None
    if transition_issue.get("state") != "closed":
        return None
    number = int(transition_issue["number"])
    comments_list = list(comments)
    terminal = base.reconcilable_terminal_from_comments(number, comments_list)
    if terminal is None or terminal.state not in STABLE_TRANSITION_TERMINAL_STATES:
        return None
    if not terminal_owner_generation_is_current(number, terminal, comments_list):
        return None
    if v3.route_is_actionable(terminal.route):
        return None
    return generation


def v5_resolved_transition_generations(
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


def stable_transition_terminal(
    terminal: base.OperationalRecord | None,
) -> bool:
    """Return whether a wrapper terminal makes exact-generation reuse unsafe."""
    return bool(
        terminal
        and terminal.kind in base.TERMINAL_KINDS
        and terminal.state in STABLE_TRANSITION_TERMINAL_STATES
    )


def transition_has_stable_terminal_state(issue_number: int) -> bool:
    """Recognize only temporally valid DONE/SUPERSEDED wrapper terminals."""
    comments = list(base.paged(f"/repos/{base.REPO}/issues/{issue_number}/comments?"))
    terminal = base.reconcilable_terminal_from_comments(issue_number, comments)
    return bool(
        stable_transition_terminal(terminal)
        and terminal is not None
        and terminal_owner_generation_is_current(issue_number, terminal, comments)
    )


def stable_transition_for_generation(
    generation: v2.Generation,
    transitions_by_generation: dict[v2.Generation, list[dict[str, Any]]],
    *,
    active_state_checker: Callable[[int], bool] | None = None,
    terminal_state_checker: Callable[[int], bool] | None = None,
    perform_reopen: bool = True,
) -> tuple[dict[str, Any] | None, bool]:
    """Return a reusable wrapper plus whether the generation is terminally settled.

    Prefer an open wrapper. A closed exact-generation wrapper with a trusted
    DONE/SUPERSEDED terminal is a durable maintenance stop: do not reopen it and
    do not create another wrapper for the same source generation. Otherwise a
    duplicate/not-planned wrapper may be reused only when it has no live trusted
    schema-3 operational state.
    """
    candidates = transitions_by_generation.get(generation, [])
    open_candidates = [item for item in candidates if item.get("state") == "open"]
    if open_candidates:
        return max(open_candidates, key=lambda item: int(item["number"])), False

    terminal_checker = terminal_state_checker or transition_has_stable_terminal_state
    closed_candidates = [
        item for item in candidates if item.get("state") == "closed"
    ]
    terminal_candidates = [
        item
        for item in closed_candidates
        if terminal_checker(int(item["number"]))
    ]
    if terminal_candidates:
        chosen = max(terminal_candidates, key=lambda item: int(item["number"]))
        print(
            f"exact generation {generation} already has terminal transition "
            f"#{int(chosen['number'])}; do not reopen or duplicate"
        )
        return None, True

    checker = active_state_checker or v2.transition_has_active_operational_state
    reopenable = [
        item
        for item in closed_candidates
        if item.get("state_reason") in {"duplicate", "not_planned"}
        and not checker(int(item["number"]))
    ]
    if not reopenable:
        return None, False
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
    return chosen, False


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
            transition, terminally_settled = stable_transition_for_generation(
                generation, transitions_by_generation
            )
            if terminally_settled:
                continue
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

    def timed_comment(
        cid: int,
        created_at: str,
        kind: str,
        state: str,
        *,
        actor: str,
        extra: str = "",
        issue: int = 104,
        mission: str = "M-104",
    ) -> dict[str, Any]:
        return {
            "id": cid,
            "author_association": "OWNER",
            "user": {"login": "vokerg"},
            "created_at": created_at,
            "updated_at": created_at,
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

    def owner_terminal(
        cid: int, created_at: str, actor: str, generation: int, head: str
    ) -> dict[str, Any]:
        return timed_comment(
            cid,
            created_at,
            "STATUS",
            "SUPERSEDED",
            actor=actor,
            extra=(
                "authority_mode: OWNER\n"
                f"ownership_generation_comment_id: {generation}\n"
                f"head_sha: {head}\n"
                f"work_sha: {'d' * 40}\n"
                "required_next_route: NONE_SOURCE_ROUTE_ALREADY_CONSUMED\n"
            ),
        )

    def parsed_terminal(comments: list[dict[str, Any]]) -> base.OperationalRecord:
        terminal = base.reconcilable_terminal_from_comments(104, comments)
        assert terminal is not None
        return terminal

    claim = timed_comment(
        1, "2026-09-15T12:00:00Z", "CLAIM", "IN_PROGRESS", actor="actor-a",
        extra=f"observed_head_sha: {'a' * 40}\nprevious_ownership_comment_id: null\n",
    )
    premature_intent = timed_comment(
        2, "2026-09-15T17:00:00Z", "RESUME_INTENT", "IN_PROGRESS", actor="actor-b",
        extra=(
            "reason: STALE\nsource_comment_id: 1\n"
            f"observed_head_sha: {'a' * 40}\n"
        ),
    )
    premature_recover = timed_comment(
        3, "2026-09-15T17:01:00Z", "RECOVER", "IN_PROGRESS", actor="actor-b",
        extra=(
            "recovery_reason: STALE\n"
            f"observed_head_sha: {'a' * 40}\n"
            "previous_ownership_comment_id: 1\n"
            "winning_intent_comment_id: 2\nsource_comment_id: 1\n"
        ),
    )
    old_owner_terminal = owner_terminal(
        4, "2026-09-15T17:02:00Z", "actor-a", 1, "a" * 40
    )
    premature = [claim, premature_intent, premature_recover, old_owner_terminal]
    assert terminal_owner_generation_is_current(
        104, parsed_terminal(premature), premature
    )

    premature_new_terminal = owner_terminal(
        4, "2026-09-15T17:02:00Z", "actor-b", 3, "a" * 40
    )
    premature_new = [claim, premature_intent, premature_recover, premature_new_terminal]
    assert not terminal_owner_generation_is_current(
        104, parsed_terminal(premature_new), premature_new
    )

    exact_intent = timed_comment(
        2, "2026-09-15T18:00:00Z", "RESUME_INTENT", "IN_PROGRESS", actor="actor-b",
        extra=(
            "reason: STALE\nsource_comment_id: 1\n"
            f"observed_head_sha: {'a' * 40}\n"
        ),
    )
    exact_recover = timed_comment(
        3, "2026-09-15T18:00:01Z", "RECOVER", "IN_PROGRESS", actor="actor-b",
        extra=(
            "recovery_reason: STALE\n"
            f"observed_head_sha: {'a' * 40}\n"
            "previous_ownership_comment_id: 1\n"
            "winning_intent_comment_id: 2\nsource_comment_id: 1\n"
        ),
    )
    recovered_terminal = owner_terminal(
        4, "2026-09-15T18:00:02Z", "actor-b", 3, "a" * 40
    )
    exact = [claim, exact_intent, exact_recover, recovered_terminal]
    assert terminal_owner_generation_is_current(104, parsed_terminal(exact), exact)

    stale_old_terminal = owner_terminal(
        4, "2026-09-15T18:00:02Z", "actor-a", 1, "a" * 40
    )
    stale_old = [claim, exact_intent, exact_recover, stale_old_terminal]
    assert not terminal_owner_generation_is_current(
        104, parsed_terminal(stale_old), stale_old
    )

    progress = timed_comment(
        2, "2026-09-15T17:00:00Z", "PROGRESS", "IN_PROGRESS", actor="actor-a",
        extra=(
            "ownership_generation_comment_id: 1\n"
            f"observed_head_sha: {'b' * 40}\n"
            "progress_basis: HEAD_ADVANCE\nevidence_refs: []\n"
        ),
    )
    renewed_intent = timed_comment(
        3, "2026-09-15T18:00:00Z", "RESUME_INTENT", "IN_PROGRESS", actor="actor-b",
        extra=(
            "reason: STALE\nsource_comment_id: 2\n"
            f"observed_head_sha: {'b' * 40}\n"
        ),
    )
    renewed_recover = timed_comment(
        4, "2026-09-15T18:01:00Z", "RECOVER", "IN_PROGRESS", actor="actor-b",
        extra=(
            "recovery_reason: STALE\n"
            f"observed_head_sha: {'b' * 40}\n"
            "previous_ownership_comment_id: 1\n"
            "winning_intent_comment_id: 3\nsource_comment_id: 2\n"
        ),
    )
    renewed_terminal = owner_terminal(
        5, "2026-09-15T18:02:00Z", "actor-a", 1, "b" * 40
    )
    renewed = [claim, progress, renewed_intent, renewed_recover, renewed_terminal]
    assert terminal_owner_generation_is_current(
        104, parsed_terminal(renewed), renewed
    )

    probe = timed_comment(
        1, "2026-09-15T12:00:00Z", "ORPHAN_PROBE", "IN_PROGRESS", actor="actor-p",
        extra=f"observed_head_sha: {'c' * 40}\n",
    )
    orphan_intent = timed_comment(
        2, "2026-09-15T12:10:00Z", "RESUME_INTENT", "IN_PROGRESS", actor="actor-b",
        extra=(
            "reason: ORPHAN\nsource_comment_id: 1\n"
            f"observed_head_sha: {'c' * 40}\n"
        ),
    )
    orphan_recover = timed_comment(
        3, "2026-09-15T12:10:01Z", "RECOVER", "IN_PROGRESS", actor="actor-b",
        extra=(
            "recovery_reason: ORPHAN\n"
            f"observed_head_sha: {'c' * 40}\n"
            "previous_ownership_comment_id: null\n"
            "winning_intent_comment_id: 2\nsource_comment_id: 1\n"
        ),
    )
    orphan_terminal = owner_terminal(
        4, "2026-09-15T12:10:02Z", "actor-b", 3, "c" * 40
    )
    orphan_exact = [probe, orphan_intent, orphan_recover, orphan_terminal]
    assert terminal_owner_generation_is_current(
        104, parsed_terminal(orphan_exact), orphan_exact
    )

    early_orphan_intent = timed_comment(
        2, "2026-09-15T12:09:59Z", "RESUME_INTENT", "IN_PROGRESS", actor="actor-b",
        extra=(
            "reason: ORPHAN\nsource_comment_id: 1\n"
            f"observed_head_sha: {'c' * 40}\n"
        ),
    )
    early_orphan_recover = timed_comment(
        3, "2026-09-15T12:09:59.500000Z", "RECOVER", "IN_PROGRESS", actor="actor-b",
        extra=(
            "recovery_reason: ORPHAN\n"
            f"observed_head_sha: {'c' * 40}\n"
            "previous_ownership_comment_id: null\n"
            "winning_intent_comment_id: 2\nsource_comment_id: 1\n"
        ),
    )
    later_claim = timed_comment(
        4, "2026-09-15T12:10:00Z", "CLAIM", "IN_PROGRESS", actor="actor-a",
        extra=f"observed_head_sha: {'c' * 40}\nprevious_ownership_comment_id: null\n",
    )
    later_claim_terminal = owner_terminal(
        5, "2026-09-15T12:10:01Z", "actor-a", 4, "c" * 40
    )
    orphan_early = [
        probe, early_orphan_intent, early_orphan_recover, later_claim, later_claim_terminal
    ]
    assert terminal_owner_generation_is_current(
        104, parsed_terminal(orphan_early), orphan_early
    )

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
    selected, settled = stable_transition_for_generation(
        old_generation,
        mapping,
        active_state_checker=lambda _: False,
        terminal_state_checker=lambda _: False,
        perform_reopen=False,
    )
    assert selected is open_wrapper and not settled

    chosen_closed, settled = stable_transition_for_generation(
        old_generation,
        {old_generation: [old]},
        active_state_checker=lambda _: False,
        terminal_state_checker=lambda _: False,
        perform_reopen=False,
    )
    assert chosen_closed is old and not settled
    blocked, settled = stable_transition_for_generation(
        old_generation,
        {old_generation: [old]},
        active_state_checker=lambda _: True,
        terminal_state_checker=lambda _: False,
        perform_reopen=False,
    )
    assert blocked is None and not settled

    terminal_wrapper = dict(old, number=102, state_reason="not_planned")
    blocked, settled = stable_transition_for_generation(
        old_generation,
        {old_generation: [terminal_wrapper]},
        active_state_checker=lambda _: False,
        terminal_state_checker=lambda _: True,
        perform_reopen=False,
    )
    assert blocked is None and settled

    completed = dict(old, number=103, state_reason="completed")
    blocked, settled = stable_transition_for_generation(
        old_generation,
        {old_generation: [completed]},
        active_state_checker=lambda _: False,
        terminal_state_checker=lambda _: True,
        perform_reopen=False,
    )
    assert blocked is None and settled

    assert stable_transition_terminal(source)
    invalidated = base.OperationalRecord(
        issue_number=100,
        comment_id=3,
        created_at="2026-09-08T00:00:01Z",
        kind="STATUS",
        state="INVALIDATED",
        route=None,
        body="",
        declared_issue=100,
        mission_id="M-100",
        actor_session_id="actor-100",
        authority_mode="OWNER",
        ownership_generation_comment_id=1,
        head_sha="a" * 40,
        work_sha="b" * 40,
    )
    assert not stable_transition_terminal(invalidated)

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
