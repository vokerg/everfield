#!/usr/bin/env python3
"""Demand-driven parallel content liveness for Everfield frontier maintenance.

This layer composes v5. It does not resurrect automatic CONT-08-style
continuation. It only ensures that an active bounded gameplay implementation
or implementation-review source cannot coexist indefinitely with an empty
content lane: when that happens, maintenance materializes exactly one bounded
content-demand intake tied to one unconsumed implementation source.

The intake itself grants no content, canon, review, verification, integration,
readiness, release, or production authority.
"""
from __future__ import annotations

import json
import re
import sys
from typing import Any, Iterable

import frontier_maintenance_v5 as v5

base = v5.base
v2 = v5.v2

CONTENT_DEMAND_INTAKE_RE = re.compile(
    r"^\[PLAN-v1\]\[FACTORY-CONTENT-DEMAND-(\d+)\]\s"
)
LIVE_CONTENT_TITLE_PATTERNS = (
    re.compile(r"\[W2-CONTENT-"),
    re.compile(r"\[CONTENT-DEMAND-"),
    re.compile(r"\[FACTORY-CONTENT-DEMAND-\d+\]"),
)
IMPLEMENTATION_PRODUCER_MARKERS = (
    "IMPLEMENTATION / FIRST_PLAYABLE_BOOTSTRAP",
    "IMPLEMENTATION / GAMEPLAY",
    "IMPLEMENTATION / PLAYABLE",
)
IMPLEMENTATION_REVIEW_MARKERS = (
    "IMPLEMENTATION_REVIEW_TEST",
    "IMPLEMENTATION / REVIEW",
)


def trusted_plan_issue(issue: dict[str, Any]) -> bool:
    if "pull_request" in issue or issue.get("state") != "open":
        return False
    title = issue.get("title") or ""
    return title.startswith("[PLAN-v1]") and v2.trusted_issue_author(issue)


def implementation_source_kind(issue: dict[str, Any]) -> str | None:
    """Classify only concrete live implementation/review work as content demand."""
    if not trusted_plan_issue(issue):
        return None
    title = issue.get("title") or ""
    body = issue.get("body") or ""
    if "[FACTORY-" in title or "IMPLEMENTATION-READINESS" in title:
        return None
    # Modern bounded playable increments use IMPLEMENTATION_INCREMENT rather
    # than the older IMPLEMENTATION / ... producer marker. A blocked shared
    # fan-in still carries specific implementation-fed content demand; the
    # content router must assess demand, not speculate new story work.
    if (
        title.startswith("[PLAN-v1][IMPLEMENTATION-INCREMENT-")
        and "-REV-" not in title
        and "-INT-" not in title
        and "IMPLEMENTATION_INCREMENT / " in body
    ):
        return "IMPLEMENTATION_INCREMENT"
    if any(marker in body for marker in IMPLEMENTATION_PRODUCER_MARKERS):
        return "IMPLEMENTATION"
    if any(marker in body for marker in IMPLEMENTATION_REVIEW_MARKERS):
        return "IMPLEMENTATION_REVIEW"
    return None


def is_live_content_work(issue: dict[str, Any]) -> bool:
    if not trusted_plan_issue(issue):
        return False
    title = issue.get("title") or ""
    return any(pattern.search(title) for pattern in LIVE_CONTENT_TITLE_PATTERNS)


def content_demand_source(issue: dict[str, Any]) -> int | None:
    title = issue.get("title") or ""
    match = CONTENT_DEMAND_INTAKE_RE.match(title)
    if not match or not v2.trusted_issue_author(issue):
        return None
    if issue.get("state") == "closed" and issue.get("state_reason") in {
        "not_planned",
        "duplicate",
    }:
        return None
    return int(match.group(1))


def consumed_content_demand_sources(
    issues: Iterable[dict[str, Any]],
) -> set[int]:
    consumed: set[int] = set()
    for issue in issues:
        source = content_demand_source(issue)
        if source is not None:
            consumed.add(source)
    return consumed


def select_content_demand_source(
    open_issues: Iterable[dict[str, Any]],
    recent_issues: Iterable[dict[str, Any]],
) -> dict[str, Any] | None:
    open_list = list(open_issues)
    if any(is_live_content_work(issue) for issue in open_list):
        return None

    consumed = consumed_content_demand_sources(recent_issues)
    candidates: list[tuple[int, int, dict[str, Any]]] = []
    for issue in open_list:
        kind = implementation_source_kind(issue)
        if kind is None:
            continue
        number = int(issue["number"])
        if number in consumed:
            continue
        # Prefer the newest concrete producer. Once producer demand has been
        # consumed, a later review/test episode can seed the next intake.
        priority = 0 if kind in {"IMPLEMENTATION", "IMPLEMENTATION_INCREMENT"} else 1
        candidates.append((priority, -number, issue))

    if not candidates:
        return None
    candidates.sort(key=lambda item: (item[0], item[1]))
    return candidates[0][2]


def content_demand_intake_body(source: dict[str, Any]) -> str:
    source_number = int(source["number"])
    kind = implementation_source_kind(source)
    assert kind is not None
    return f"""## Mission ID
`W2-CONTENT-DEMAND-FROM-IMPLEMENTATION-{source_number}`

## Role / task class
`CONTENT_DEMAND_INTAKE / IMPLEMENTATION_FED_FRONTIER_COMPILER`.

## State
`READY / DEMAND_DRIVEN_CONTENT_INTAKE`.

## Source
- source implementation issue: #{source_number}
- source class: `{kind}`
- owner parallel-content directive: Issue #84 comment `5511637902`
- owner implementation-transition directive: Issue #84 comment `5889817307`

## Objective
Inspect the exact current implementation/review/playtest surface of source #{source_number}
against the existing reviewed content contracts and materialize only concrete content work
needed by the running slice.

This is deliberately **not** CONT-08 and must not restart a self-feeding generic continuation
chain.

## Required behavior
1. Re-derive current main, canonical binding, source ownership/terminal state, source PR/evidence,
   and current open CONTENT work before claim and before materializing successors.
2. Identify concrete implementation-fed content demand only: missing world/location detail,
   character/relationship material, dialogue/narrative/quest consequences, institutions/social
   conflict, content consistency/evaluation, or a similarly bounded content contract required by
   the current executable/review surface.
3. Materialize 1–4 genuinely independent content roots only when concrete demand exists. Mutable
   paths must be disjoint and each root must have an explicit review/test/fan-in route appropriate
   to its artifact.
4. If no concrete content demand exists, terminalize a bounded no-op result. Do not invent backlog
   merely to keep agents busy.
5. Preserve unresolved mystery, refusal/nonalignment, evidence/claim separation, accessibility,
   legal/provider, production/release, and final-canon boundaries already present in reviewed
   content contracts.
6. Do not modify gameplay code from this intake. Implementation findings may be cited as demand
   evidence but do not grant content canon or implementation authority.
7. Do not create another automatic CONTENT continuation tranche. New work must remain causally
   traceable to source #{source_number} or its exact review/playtest evidence.

## Terminal
Open an exact-head draft PR for any repository-owned intake artifact required by the selected
route, materialize the bounded successor roots, and publish the normal schema-3 terminal/handoff.
Successor authorship does not satisfy their required reviews.

## Authority boundary
`NOT_CANONICAL`. Demand routing only. No final canon, gameplay implementation, verification PASS,
implementation readiness, integration, production/release, legal/provider, or certification authority.
"""


def create_content_demand_intake(
    source: dict[str, Any],
) -> dict[str, Any] | None:
    source_number = int(source["number"])
    title = (
        f"[PLAN-v1][FACTORY-CONTENT-DEMAND-{source_number}] "
        f"Materialize implementation-fed content work from #{source_number}"
    )
    body = content_demand_intake_body(source)
    if base.DRY_RUN:
        print(f"would create content-demand intake for implementation source #{source_number}")
        return None
    created = base.request(
        "POST",
        f"/repos/{base.REPO}/issues",
        {"title": title, "body": body},
    )
    print(
        f"created content-demand intake #{int(created['number'])} "
        f"for implementation source #{source_number}"
    )
    return created


def materialize_content_demand_intake(
    open_issues: list[dict[str, Any]],
    recent_issues: list[dict[str, Any]],
) -> int:
    source = select_content_demand_source(open_issues, recent_issues)
    if source is None:
        return 0
    created = create_content_demand_intake(source)
    if created is not None:
        open_issues.append(created)
        recent_issues.append(created)
    return 1


def self_test() -> None:
    v5.self_test()

    def issue(
        number: int,
        title: str,
        body: str = "",
        *,
        state: str = "open",
        state_reason: str | None = None,
        login: str = "vokerg",
        association: str = "OWNER",
    ) -> dict[str, Any]:
        return {
            "number": number,
            "title": title,
            "body": body,
            "state": state,
            "state_reason": state_reason,
            "author_association": association,
            "user": {"login": login},
        }

    producer = issue(
        1343,
        "[PLAN-v1][W2-GODOT-FIRST-PLAYABLE-BOOTSTRAP-01] Build bounded Godot first playable",
        "## Role / task class\n`IMPLEMENTATION / FIRST_PLAYABLE_BOOTSTRAP`.",
    )
    review = issue(
        1371,
        "[PLAN-v1][W2-GODOT-FIRST-PLAYABLE-BOOTSTRAP-01-REV-01] Review and test bounded Godot first playable",
        "## Role / task class\n`REQUIRED_REVIEW / IMPLEMENTATION_REVIEW_TEST`.",
    )
    liveness_fix = issue(
        1373,
        "[PLAN-v1][FACTORY-CONTENT-DEMAND-LIVENESS-01] Restore demand-driven parallel content frontier",
        "factory maintenance",
    )
    assert implementation_source_kind(producer) == "IMPLEMENTATION"
    assert implementation_source_kind(review) == "IMPLEMENTATION_REVIEW"
    assert implementation_source_kind(liveness_fix) is None
    current_increment = issue(
        1545,
        "[PLAN-v1][IMPLEMENTATION-INCREMENT-PLAYABLE-FEEDBACK-COMMANDS-03] Fan in",
        "IMPLEMENTATION_INCREMENT / POST_THREE_SEAM_FEEDBACK_COMMAND_FAN_IN; BLOCKED",
    )
    assert implementation_source_kind(current_increment) == "IMPLEMENTATION_INCREMENT"
    assert implementation_source_kind(
        issue(1540, "[PLAN-v1][IMPLEMENTATION-INCREMENT-SOMETHING-REV-INT-01] Review publication",
              "IMPLEMENTATION_INCREMENT / PLAYABLE_FAN_IN")
    ) is None
    assert select_content_demand_source(
        [current_increment], [current_increment]
    ) is current_increment
    existing_increment_intake = issue(
        1557,
        "[PLAN-v1][FACTORY-CONTENT-DEMAND-1545] Materialize content from #1545",
        state="closed", state_reason="completed",
        login="github-actions[bot]", association="NONE",
    )
    assert select_content_demand_source(
        [current_increment], [current_increment, existing_increment_intake]
    ) is None

    selected = select_content_demand_source(
        [producer, review, liveness_fix],
        [producer, review, liveness_fix],
    )
    assert selected is producer

    live_root = issue(
        1400,
        "[PLAN-v1][CONTENT-DEMAND-OLD-WORKS-WORLD-01] Deepen implemented Old Works location",
    )
    assert is_live_content_work(live_root)
    assert select_content_demand_source(
        [producer, review, live_root],
        [producer, review, live_root],
    ) is None

    producer_intake = issue(
        1401,
        "[PLAN-v1][FACTORY-CONTENT-DEMAND-1343] Materialize implementation-fed content work from #1343",
        state="closed",
        state_reason="completed",
        login="github-actions[bot]",
        association="NONE",
    )
    selected = select_content_demand_source(
        [producer, review],
        [producer, review, producer_intake],
    )
    assert selected is review

    duplicate_intake = issue(
        1402,
        "[PLAN-v1][FACTORY-CONTENT-DEMAND-1343] Materialize implementation-fed content work from #1343",
        state="closed",
        state_reason="duplicate",
        login="github-actions[bot]",
        association="NONE",
    )
    assert 1343 not in consumed_content_demand_sources([duplicate_intake])
    assert 1343 in consumed_content_demand_sources([producer_intake])

    assert select_content_demand_source([], []) is None
    print("frontier maintenance v6 self-test: PASS")


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
        readiness_dead_ends_created = base.materialize_readiness_dead_end_diagnostics(
            open_items
        )
        transition_created, dispatched, transition_retired, transition_reused = (
            v5.materialize_missing_transitions(open_items, base.load_routes())
        )

        closed_recent = list(
            base.paged(
                f"/repos/{base.REPO}/issues?state=closed&sort=updated&direction=desc&"
                "since=2026-09-29T00:00:00Z&"
            )
        )
        recent_issues = [
            item
            for item in open_items + closed_recent
            if "pull_request" not in item
        ]
        content_demand_intakes_created = materialize_content_demand_intake(
            open_items, recent_issues
        )
    except base.GitHubRateLimitExceeded as exc:
        print(f"::warning title=Frontier maintenance deferred::{exc}")
        print(
            json.dumps(
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
        json.dumps(
            {
                "dry_run": base.DRY_RUN,
                "terminal_issues_closed": issue_closed,
                "rejected_prs_closed": pr_closed,
                "readiness_dead_ends_created": readiness_dead_ends_created,
                "redundant_transitions_closed": transition_retired,
                "transitions_created": transition_created,
                "transitions_reused": transition_reused,
                "registered_routes_dispatched": dispatched,
                "content_demand_intakes_created": content_demand_intakes_created,
                "reconciliation_complete": True,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
