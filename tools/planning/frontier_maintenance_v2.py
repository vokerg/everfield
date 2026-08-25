#!/usr/bin/env python3
"""Successor-aware liveness layer for Everfield planning frontier maintenance.

This module deliberately reuses the reviewed safety/authority primitives from
frontier_maintenance.py and narrows only graph-consumption/reconciliation.
It does not grant planning, review, verification, integration, or decision
authority.
"""
from __future__ import annotations

import re
import sys
from typing import Any, Iterable

import frontier_maintenance as base


# Only phrases that explicitly declare a graph relationship are recognized.
# Arbitrary mentions of an issue number are intentionally ignored.
SUCCESSOR_RELATION_PATTERNS = (
    r"(?im)^\s*predecessor_issue:\s*(\d+)\s*$",
    r"(?i)\bimmediate predecessor:\s*Issue\s*#(\d+)\b",
    r"(?i)\bSource terminal issue:\s*#(\d+)\b",
    r"(?i)\b(?:remediation|review|recovery|continuation|integration|publication)\s+of\s+(?:terminal\s+)?Issue\s*#(\d+)\b",
    r"(?im)^\s*Required\s+(?:clean\s+)?(?:review|remediation|integration|continuation|publication):\s*Issue\s*#(\d+)\b",
    r"(?i)\brequired\s+by\s+terminal\s+Issue\s*#(\d+)\b",
)

TRANSITION_ROUTE_RE = re.compile(r"(?im)^\s*Required next route:\s*`([^`]+)`\s*$")
RESOLUTION_VERSION = "1"
RESOLUTION_DONE_DISPOSITIONS = {
    "TRANSITION_DISPATCH_ALREADY_ACCEPTED",
    "TRANSITION_DISPATCH_OBSERVED",
}


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


def factory_transition_route(issue: dict[str, Any]) -> str | None:
    match = TRANSITION_ROUTE_RE.search(issue.get("body") or "")
    return match.group(1).strip() if match else None


def consumed_nontransition_sources(issues: Iterable[dict[str, Any]]) -> set[int]:
    consumed: set[int] = set()
    for issue in issues:
        if "pull_request" in issue or factory_transition_source(issue) is not None:
            continue
        consumed.update(predecessor_sources(issue))
    return consumed


def _trusted_resolution_author(comment: dict[str, Any]) -> bool:
    login = ((comment.get("user") or {}).get("login") or "")
    return login == "github-actions[bot]" or comment.get("author_association") in base.TRUSTED_ASSOCIATIONS


def transition_resolution_from_comments(
    comments: Iterable[dict[str, Any]], source_issue: int, route: str
) -> dict[str, Any] | None:
    comments_list = list(comments)
    dispatch = base.trusted_dispatch_marker_from_comments(comments_list, source_issue, route)
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
        if base.scalar(body, "route") != route:
            continue
        if base.scalar(body, "state") != "DONE":
            continue
        if base.scalar(body, "disposition") not in RESOLUTION_DONE_DISPOSITIONS:
            continue
        if base.integer_scalar(body, "accepted_dispatch_comment_id") != dispatch_id:
            continue
        return comment
    return None


def resolved_transition_sources(closed_issues: Iterable[dict[str, Any]]) -> set[int]:
    consumed: set[int] = set()
    for issue in closed_issues:
        source = factory_transition_source(issue)
        route = factory_transition_route(issue)
        if source is None or not route:
            continue
        comments = base.paged(f"/repos/{base.REPO}/issues/{int(issue['number'])}/comments?")
        if transition_resolution_from_comments(comments, source, route) is not None:
            consumed.add(source)
    return consumed


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


def retirable_transition_numbers(
    open_issues: Iterable[dict[str, Any]], consumed_sources: set[int]
) -> list[int]:
    numbers: list[int] = []
    for issue in open_issues:
        source = factory_transition_source(issue)
        if source is not None and source in consumed_sources:
            numbers.append(int(issue["number"]))
    return numbers


def retire_consumed_transitions(
    open_issues: list[dict[str, Any]], consumed_sources: set[int]
) -> int:
    retired = 0
    retained: list[dict[str, Any]] = []
    for issue in open_issues:
        source = factory_transition_source(issue)
        if source is None or source not in consumed_sources:
            retained.append(issue)
            continue
        number = int(issue["number"])
        if transition_has_active_operational_state(number):
            print(f"preserve claimed transition #{number} for consumed source #{source}")
            retained.append(issue)
            continue
        print(f"retire redundant transition #{number}: source #{source} already has a successor/resolution")
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
    consumed_sources = consumed_nontransition_sources(recent_issues)
    consumed_sources.update(resolved_transition_sources(closed))
    retired = retire_consumed_transitions(open_issues, consumed_sources)

    dispatch_keys: set[tuple[str, str]] = set()
    for issue in closed:
        if "pull_request" in issue:
            continue
        number = int(issue["number"])
        source = base.reconcilable_terminal(number)
        if not source or not source.route or number in consumed_sources:
            continue
        transition = base.find_open_transition(open_issues, number)
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
    assert predecessor_sources({"body": "Context mentions Issue #680 and Issue #693, but declares no dependency."}) == set()

    normal = {"number": 20, "title": "[PLAN-v1] remediation", "body": "Minimal remediation of Issue #10."}
    transition = {
        "number": 21,
        "title": "[PLAN-v1][FACTORY-TRANSITION-10] Materialize required next route from #10",
        "body": "Source terminal issue: #10\nRequired next route: `NEXT`",
    }
    assert consumed_nontransition_sources([normal, transition]) == {10}
    assert retirable_transition_numbers([transition], {10}) == [21]
    assert retirable_transition_numbers([transition], {11}) == []

    created = "2026-08-25T00:00:00Z"
    dispatch = {
        "id": 100,
        "author_association": "NONE",
        "user": {"login": "github-actions[bot]"},
        "created_at": created,
        "updated_at": created,
        "body": (
            "factory_frontier_dispatch: 1\n"
            "source_issue: 10\n"
            "route: NEXT\n"
            "status: ACCEPTED\n"
            f"main_sha: {'a' * 40}\n"
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
            "route: NEXT\n"
            "state: DONE\n"
            "disposition: TRANSITION_DISPATCH_ALREADY_ACCEPTED\n"
            "accepted_dispatch_comment_id: 100\n"
        ),
    }
    assert transition_resolution_from_comments([dispatch, resolution], 10, "NEXT") is resolution
    edited_resolution = dict(resolution, updated_at="2026-08-25T00:01:00Z")
    assert transition_resolution_from_comments([dispatch, edited_resolution], 10, "NEXT") is None
    wrong_dispatch = dict(resolution, body=resolution["body"].replace("100", "999"))
    assert transition_resolution_from_comments([dispatch, wrong_dispatch], 10, "NEXT") is None

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
