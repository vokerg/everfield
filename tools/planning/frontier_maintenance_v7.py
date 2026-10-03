#!/usr/bin/env python3
"""Post-integration implementation liveness for Everfield frontier maintenance.

This layer composes v6. It preserves the existing planning/content liveness
behavior and adds one invariant: a trusted integrated playable/increment cannot
leave the implementation frontier empty unless an explicit later product
milestone ends implementation continuation.

When continuation is needed, v7 materializes one bounded implementation-demand
intake for one unconsumed integrated implementation source. The intake must
prefer 2-4 pairwise-disjoint implementation roots plus an explicit fan-in so
agents can implement concurrently without contending on shared gameplay files.

The maintenance layer itself grants no gameplay, review, integration, canon,
production, release, accessibility-certification, legal, or provider authority.
"""
from __future__ import annotations

import json
import re
import sys
from typing import Any, Iterable

import frontier_maintenance_v6 as v6

base = v6.base
v2 = v6.v2

IMPLEMENTATION_INTAKE_RE = re.compile(
    r"^\[PLAN-v1\]\[FACTORY-IMPLEMENTATION-DEMAND-(\d+)\]\s"
)
LIVE_IMPLEMENTATION_TITLE_PATTERNS = (
    re.compile(r"\[IMPLEMENTATION-DEMAND-"),
    re.compile(r"\[IMPLEMENTATION-INCREMENT-"),
    re.compile(r"\[FACTORY-IMPLEMENTATION-DEMAND-\d+\]"),
)
IMPLEMENTATION_SOURCE_MARKERS = (
    "IMPLEMENTATION / FIRST_PLAYABLE_BOOTSTRAP",
    "IMPLEMENTATION_INCREMENT / PLAYABLE_FAN_IN",
)
OWNER_PARALLEL_IMPLEMENTATION_DIRECTIVE_ISSUE = 84
OWNER_PARALLEL_IMPLEMENTATION_DIRECTIVE_COMMENT_ID = 5_968_764_259


def trusted_plan_issue(issue: dict[str, Any]) -> bool:
    if "pull_request" in issue:
        return False
    title = issue.get("title") or ""
    return title.startswith("[PLAN-v1]") and v2.trusted_issue_author(issue)


def implementation_source_candidate(issue: dict[str, Any]) -> bool:
    """Recognize only bounded playable producers/fan-ins, never factory/content work."""
    if not trusted_plan_issue(issue):
        return False
    if issue.get("state") != "closed":
        return False
    if issue.get("state_reason") in {"not_planned", "duplicate"}:
        return False
    title = issue.get("title") or ""
    body = issue.get("body") or ""
    if (
        "[FACTORY-" in title
        or "IMPLEMENTATION-READINESS" in title
        or "[CONTENT-" in title
        or "-REV-" in title
    ):
        return False
    return any(marker in body for marker in IMPLEMENTATION_SOURCE_MARKERS)


def is_live_implementation_work(issue: dict[str, Any]) -> bool:
    if not trusted_plan_issue(issue) or issue.get("state") != "open":
        return False
    title = issue.get("title") or ""
    return any(pattern.search(title) for pattern in LIVE_IMPLEMENTATION_TITLE_PATTERNS)


def implementation_intake_source(issue: dict[str, Any]) -> int | None:
    title = issue.get("title") or ""
    match = IMPLEMENTATION_INTAKE_RE.match(title)
    if not match or not v2.trusted_issue_author(issue):
        return None
    if issue.get("state") == "closed" and issue.get("state_reason") in {
        "not_planned",
        "duplicate",
    }:
        return None
    return int(match.group(1))


def consumed_implementation_sources(
    issues: Iterable[dict[str, Any]],
) -> set[int]:
    consumed: set[int] = set()
    for issue in issues:
        source = implementation_intake_source(issue)
        if source is not None:
            consumed.add(source)
    return consumed


def _trusted_unedited_comment(comment: dict[str, Any]) -> bool:
    association = comment.get("author_association")
    login = ((comment.get("user") or {}).get("login") or "")
    trusted = association in base.TRUSTED_ASSOCIATIONS or login == "github-actions[bot]"
    return bool(
        trusted
        and comment.get("created_at")
        and comment.get("created_at") == comment.get("updated_at")
    )


def integration_main_sha_from_comments(
    issue_number: int,
    comments: Iterable[dict[str, Any]],
) -> str | None:
    """Return the newest trusted squash INTEGRATION_STATUS DONE main SHA."""
    found: list[tuple[int, str]] = []
    for comment in comments:
        if not _trusted_unedited_comment(comment):
            continue
        body = comment.get("body") or ""
        if not re.search(r"(?m)^protocol:\s*planning-v1\s*$", body):
            continue
        if not re.search(r"(?m)^schema:\s*3\s*$", body):
            continue
        if not re.search(r"(?m)^kind:\s*INTEGRATION_STATUS\s*$", body):
            continue
        if not re.search(r"(?m)^state:\s*DONE\s*$", body):
            continue
        if not re.search(r"(?m)^merge_method:\s*squash\s*$", body):
            continue
        main_sha = base.scalar(body, "main_sha")
        if main_sha is None or not base.SHA40_RE.fullmatch(main_sha):
            continue
        found.append((int(comment["id"]), main_sha.lower()))
    if not found:
        return None
    return max(found, key=lambda item: item[0])[1]


def integration_sha_is_on_current_main(integration_sha: str) -> bool:
    current = base.current_main_sha().lower()
    if integration_sha.lower() == current:
        return True
    comparison = base.request(
        "GET",
        f"/repos/{base.REPO}/compare/{integration_sha}...{current}",
    )
    return comparison.get("status") in {"ahead", "identical"}


def integrated_implementation_sources(
    recent_issues: Iterable[dict[str, Any]],
) -> dict[int, str]:
    integrated: dict[int, str] = {}
    for issue in recent_issues:
        if not implementation_source_candidate(issue):
            continue
        number = int(issue["number"])
        comments = list(base.paged(f"/repos/{base.REPO}/issues/{number}/comments?"))
        main_sha = integration_main_sha_from_comments(number, comments)
        if main_sha is None:
            continue
        if not integration_sha_is_on_current_main(main_sha):
            print(
                f"ignore implementation source #{number}: integration SHA "
                f"{main_sha} is not on current main"
            )
            continue
        integrated[number] = main_sha
    return integrated


def select_implementation_demand_source(
    open_issues: Iterable[dict[str, Any]],
    recent_issues: Iterable[dict[str, Any]],
    integrated_source_numbers: set[int],
) -> dict[str, Any] | None:
    open_list = list(open_issues)
    if any(is_live_implementation_work(issue) for issue in open_list):
        return None

    recent_list = list(recent_issues)
    consumed = consumed_implementation_sources(recent_list)
    candidates = [
        issue
        for issue in recent_list
        if int(issue.get("number", 0)) in integrated_source_numbers
        and implementation_source_candidate(issue)
        and int(issue["number"]) not in consumed
    ]
    if not candidates:
        return None
    return max(candidates, key=lambda issue: int(issue["number"]))


def implementation_intake_body(source: dict[str, Any], integration_sha: str) -> str:
    source_number = int(source["number"])
    return f"""## Mission ID
`W2-IMPLEMENTATION-DEMAND-FROM-INTEGRATED-{source_number}`

## Role / task class
`IMPLEMENTATION_DEMAND_INTAKE / PARALLEL_INCREMENT_COMPILER`.

## State
`READY / IMPLEMENTATION_CONTINUATION`.

## Source
- integrated implementation issue: #{source_number}
- integrated implementation main SHA: `{integration_sha}`
- owner post-first-playable parallelism directive: Issue #84 comment `5968764259`
- owner implementation-transition directive: Issue #84 comment `5889817307`

## Objective
Derive the next concrete bounded Godot implementation increment from the exact integrated
playable, its required review/playtest evidence, already-clean reviewed content packets,
defects, missing implementation contracts, or bounded product questions.

This is executable implementation continuation, not a generic planning tranche.

## Parallelism contract
When concrete independent work exists:
1. materialize **2–4 implementation component roots** with pairwise-disjoint mutable paths;
2. each component must be independently buildable/testable/reviewable without writing the shared
   fan-in surfaces owned by sibling roots;
3. materialize one explicit **playable fan-in** issue blocked on the exact clean-reviewed component
   packets; the fan-in alone may own shared surfaces such as `game/main.gd`, `game/main.tscn`,
   primary integration smoke tests, or equivalent common wiring;
4. component authorship does not satisfy component review, and fan-in authorship does not satisfy
   final implementation review/test.

## Liveness rule
Do not terminate the implementation lane with `required_next_route: NONE` merely because the
previous bounded increment completed. If fewer than two mechanically independent component roots
can be justified, route a bounded implementation evaluation/playtest root that must either expose
the next concrete increment or identify the exact explicit product milestone/owner authority that
ends implementation continuation.

## Scope discipline
- consume only reviewed/canonical-compatible content; implementation does not promote candidate
  content to final canon;
- preserve `MYS:FRAGMENTATION-CAUSE = UNKNOWN_BY_DESIGN` and all reviewed refusal/deferral
  semantics unless later authority explicitly changes them;
- no broad production hardening, release packaging, unrelated platform work, or speculative engine
  architecture unless demanded by the current increment;
- prefer small executable modules/scenes/resources with direct tests over prose-only output.

## Terminal
The intake is routing-only: materialize the bounded parallel roots and their explicit fan-in, then
publish a schema-3 terminal naming every successor. A concrete implementation increment must remain
live unless explicit product-complete authority exists.

## Authority boundary
`NOT_CANONICAL`. Routing only. No gameplay artifact is accepted by this issue itself. No final
canon, production/release, empirical-accessibility certification, legal/provider, verification PASS,
or integration authority is granted.
"""


def create_implementation_demand_intake(
    source: dict[str, Any], integration_sha: str
) -> dict[str, Any] | None:
    source_number = int(source["number"])
    title = (
        f"[PLAN-v1][FACTORY-IMPLEMENTATION-DEMAND-{source_number}] "
        f"Materialize parallel implementation increment from #{source_number}"
    )
    if base.DRY_RUN:
        print(
            f"would create implementation-demand intake for integrated source "
            f"#{source_number}"
        )
        return None
    created = base.request(
        "POST",
        f"/repos/{base.REPO}/issues",
        {"title": title, "body": implementation_intake_body(source, integration_sha)},
    )
    print(
        f"created implementation-demand intake #{int(created['number'])} "
        f"for integrated source #{source_number}"
    )
    return created


def materialize_implementation_demand_intake(
    open_issues: list[dict[str, Any]],
    recent_issues: list[dict[str, Any]],
    integrated_sources: dict[int, str],
) -> int:
    source = select_implementation_demand_source(
        open_issues, recent_issues, set(integrated_sources)
    )
    if source is None:
        return 0
    source_number = int(source["number"])
    created = create_implementation_demand_intake(
        source, integrated_sources[source_number]
    )
    if created is not None:
        open_issues.append(created)
        recent_issues.append(created)
    return 1


def self_test() -> None:
    v6.self_test()

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

    first_playable = issue(
        1343,
        "[PLAN-v1][W2-GODOT-FIRST-PLAYABLE-BOOTSTRAP-01] Build bounded Godot first playable",
        "## Role / task class\n`IMPLEMENTATION / FIRST_PLAYABLE_BOOTSTRAP`.",
        state="closed",
        state_reason="completed",
    )
    factory = issue(
        1403,
        "[PLAN-v1][FACTORY-IMPLEMENTATION-LIVENESS-01] Keep implementation alive",
        "factory maintenance",
        state="closed",
        state_reason="completed",
    )
    content = issue(
        1378,
        "[PLAN-v1][CONTENT-DEMAND-OLD-WORKS-WORLD-01] Content",
        "CONTENT_ROOT",
        state="closed",
        state_reason="completed",
    )
    assert implementation_source_candidate(first_playable)
    assert not implementation_source_candidate(factory)
    assert not implementation_source_candidate(content)

    selected = select_implementation_demand_source(
        [],
        [first_playable, factory, content],
        {1343},
    )
    assert selected is first_playable

    component = issue(
        1410,
        "[PLAN-v1][IMPLEMENTATION-DEMAND-OLD-WORKS-WORLD-01] Implement world presentation",
        "IMPLEMENTATION_COMPONENT / WORLD_PRESENTATION",
    )
    assert is_live_implementation_work(component)
    assert select_implementation_demand_source(
        [component],
        [first_playable, component],
        {1343},
    ) is None

    completed_intake = issue(
        1411,
        "[PLAN-v1][FACTORY-IMPLEMENTATION-DEMAND-1343] Materialize parallel implementation increment from #1343",
        state="closed",
        state_reason="completed",
        login="github-actions[bot]",
        association="NONE",
    )
    assert 1343 in consumed_implementation_sources([completed_intake])
    assert select_implementation_demand_source(
        [],
        [first_playable, completed_intake],
        {1343},
    ) is None

    duplicate_intake = issue(
        1412,
        "[PLAN-v1][FACTORY-IMPLEMENTATION-DEMAND-1343] Materialize parallel implementation increment from #1343",
        state="closed",
        state_reason="duplicate",
        login="github-actions[bot]",
        association="NONE",
    )
    assert 1343 not in consumed_implementation_sources([duplicate_intake])
    assert select_implementation_demand_source(
        [],
        [first_playable, duplicate_intake],
        {1343},
    ) is first_playable

    assert select_implementation_demand_source(
        [], [first_playable], set()
    ) is None

    fan_in = issue(
        1420,
        "[PLAN-v1][IMPLEMENTATION-INCREMENT-OLD-WORKS-PRESENTATION-01] Integrate presentation",
        "## Role / task class\n`IMPLEMENTATION_INCREMENT / PLAYABLE_FAN_IN`.",
        state="closed",
        state_reason="completed",
    )
    assert implementation_source_candidate(fan_in)
    print("frontier maintenance v7 self-test: PASS")


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
            v6.v5.materialize_missing_transitions(open_items, base.load_routes())
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

        content_demand_intakes_created = v6.materialize_content_demand_intake(
            open_items, recent_issues
        )

        integrated_sources = integrated_implementation_sources(recent_issues)
        implementation_demand_intakes_created = (
            materialize_implementation_demand_intake(
                open_items, recent_issues, integrated_sources
            )
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
                "implementation_demand_intakes_created": implementation_demand_intakes_created,
                "reconciliation_complete": True,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
