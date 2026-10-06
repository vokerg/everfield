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
    "IMPLEMENTATION_INCREMENT / ",
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
    # Modern fan-in integration occurs on a separate, owner-authorized
    # -INT- issue. It is eligible only after its own trusted squash
    # INTEGRATION_STATUS(DONE) proves ancestry on current main below.
    return (
        any(marker in body for marker in IMPLEMENTATION_SOURCE_MARKERS)
        or re.match(
            r"^\[PLAN-v1\]\[IMPLEMENTATION-INCREMENT-[^]]+-INT-\d+\]",
            title,
        ) is not None
    )


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
        # Bounded owner-authored W2 implementation intakes existed before the
        # generic factory naming scheme. Consume only a directly named
        # integrated source in the intake's source paragraph; a loose numeric
        # reference elsewhere is never proof of causal routing.
        title = issue.get("title") or ""
        body = issue.get("body") or ""
        if (
            title.startswith("[PLAN-v1][W2-IMPLEMENTATION-DEMAND-")
            and "IMPLEMENTATION_DEMAND_INTAKE" in body
            and v2.trusted_issue_author(issue)
            and not (
                issue.get("state") == "closed"
                and issue.get("state_reason") in {"duplicate", "not_planned"}
            )
        ):
            source_section = body.split("## Concrete next-demand signals")[0]
            source_section = source_section.split("## Exact bounded routing deliverable")[0]
            consumed.update(
                int(value) for value in re.findall(
                    r"\bafter #(\d+)'s?\b", source_section
                )
            )
            consumed.update(
                int(value) for value in re.findall(
                    r"(?m)^\s*- (?:integrated implementation issue|source integration issue): #(\d+)\b",
                    source_section,
                )
            )
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


def _integration_field(body: str, key: str) -> str | None:
    """Read exactly one *top-level* authority field inside the YAML capsule.

    Never combine a quoted example, prose, or an extension key with a capsule:
    the full-field check fails closed on missing/duplicated authority fields.
    """
    if not body.startswith("```yaml\n"):
        return None
    capsule = body.split("\n```", 1)[0].split("\n", 1)[1]
    authority = capsule.split("\nextensions:", 1)[0]
    hits = re.findall(rf"(?m)^{re.escape(key)}:\s*([^\n#]*?)\s*$", authority)
    if len(hits) != 1:
        return None
    result = hits[0].strip().strip("'\"")
    return result if result and result.lower() not in {"null", "none"} else None



def _extension_field(body: str, key: str) -> str | None:
    """Exactly one extension scalar, never a quoted/top-level authority claim."""
    if not body.startswith("```yaml\n") or "\nextensions:\n" not in body:
        return None
    section = body.split("\nextensions:\n", 1)[1].split("\n```", 1)[0]
    hits = re.findall(rf"(?m)^  {re.escape(key)}:\s*([^\n#]*?)\s*$", section)
    if len(hits) != 1:
        return None
    value = hits[0].strip().strip("'\"")
    return value if value and value.lower() not in {"null", "none"} else None


def _matching_extension(body: str, keys: tuple[str, ...], expected: str) -> bool:
    """At least one explicit causal reference; all present aliases must agree."""
    values = [_extension_field(body, key) for key in keys]
    present = [value for value in values if value is not None]
    return bool(present) and all(value == expected for value in present)


def _positive_comment_number(value: str | None) -> int | None:
    return int(value) if value and value.isdigit() and int(value) > 0 else None


def _valid_owner_terminal(
    issue_number: int, records: list[Any], terminal: Any,
) -> bool:
    """Fail-closed canonical first winner or matured winning STALE recovery.

    The shared base lease helper tracks PROGRESS but does not itself validate
    recovery grants or competing generations. Reconstruct those explicitly.
    """
    if (
        terminal.declared_issue != issue_number
        or _integration_field(terminal.body, "branch") != f"planning/issue-{issue_number}"
        or _integration_field(terminal.body, "actor_session_id") != terminal.actor_session_id
        or not terminal.mission_id
        or _integration_field(terminal.body, "terminal") != "true"
        or not terminal.actor_session_id
        or terminal.ownership_generation_comment_id is None
        or _integration_field(terminal.body, "authority_mode")
        not in {"OWNER", "REVIEWER"}
        or not all(
            value and base.SHA40_RE.fullmatch(value)
            for value in (terminal.head_sha, terminal.work_sha)
        )
    ):
        return False

    owner = next(
        (r for r in records if r.comment_id == terminal.ownership_generation_comment_id),
        None,
    )
    claims = [
        r for r in records
        if r.kind == "CLAIM"
        and r.state == "IN_PROGRESS"
        and r.declared_issue == issue_number
        and r.mission_id == terminal.mission_id
        and _integration_field(r.body, "branch") == f"planning/issue-{issue_number}"
        and _integration_field(r.body, "previous_ownership_comment_id") is None
        and (base_sha := _integration_field(r.body, "base_sha")) is not None
        and base.SHA40_RE.fullmatch(base_sha)
        and _integration_field(r.body, "observed_head_sha") == base_sha
        and base.parse_github_server_time(r.created_at) is not None
    ]
    if not claims or owner is None:
        return False
    first = min(claims, key=lambda r: r.comment_id)
    if (
        first.comment_id >= terminal.comment_id
        or owner.comment_id >= terminal.comment_id
        or owner.declared_issue != issue_number
        or owner.mission_id != terminal.mission_id
        or owner.actor_session_id != terminal.actor_session_id
        or owner.state != "IN_PROGRESS"
        or _integration_field(terminal.body, "base_sha")
        != _integration_field(first.body, "base_sha")
    ):
        return False
    if owner.kind == "CLAIM":
        if owner.comment_id != first.comment_id:
            return False
    elif owner.kind == "RECOVER":
        if (
            _integration_field(owner.body, "recovery_reason") != "STALE"
            or _integration_field(owner.body, "previous_ownership_comment_id")
            != str(first.comment_id)
            or any(
                r.kind in {"RECOVER", "RESUME"}
                and first.comment_id < r.comment_id < owner.comment_id
                and r.declared_issue == issue_number
                for r in records
            )
        ):
            return False
        intent_id = _positive_comment_number(
            _integration_field(owner.body, "winning_intent_comment_id")
        )
        intent = next((r for r in records if r.comment_id == intent_id), None)
        if (
            intent is None
            or intent.kind != "RESUME_INTENT"
            or intent.declared_issue != issue_number
            or intent.mission_id != terminal.mission_id
            or intent.actor_session_id != owner.actor_session_id
            or _integration_field(intent.body, "reason") != "STALE"
            or _integration_field(intent.body, "branch")
            != f"planning/issue-{issue_number}"
            or not first.comment_id < intent.comment_id < owner.comment_id
        ):
            return False
        lease_at_intent = base.schema3_ownership_lease_state(
            first, records, before_comment_id=intent.comment_id,
        )
        lease_at_recover = base.schema3_ownership_lease_state(
            first, records, before_comment_id=owner.comment_id,
        )
        intent_time = base.parse_github_server_time(intent.created_at)
        recover_time = base.parse_github_server_time(owner.created_at)
        if (
            lease_at_intent is None or lease_at_recover is None
            or lease_at_recover != lease_at_intent
            or intent_time is None or recover_time is None
            or intent_time < lease_at_intent.anchor_created_at
            + base.timedelta(seconds=base.SCHEMA3_TASK_OWNERSHIP_LEASE_SECONDS)
            or recover_time < intent_time
            or _integration_field(intent.body, "source_comment_id")
            != str(lease_at_intent.anchor_comment_id)
            or _integration_field(owner.body, "source_comment_id")
            != str(lease_at_intent.anchor_comment_id)
            or (observed_recovery_head := _integration_field(
                owner.body, "observed_head_sha"
            )) is None
            or base.SHA40_RE.fullmatch(observed_recovery_head) is None
            or _integration_field(intent.body, "observed_head_sha")
            != observed_recovery_head
        ):
            return False
        eligible_intents = [
            r for r in records
            if r.kind == "RESUME_INTENT"
            and r.declared_issue == issue_number
            and r.mission_id == terminal.mission_id
            and first.comment_id < r.comment_id <= intent.comment_id
            and _integration_field(r.body, "branch")
            == f"planning/issue-{issue_number}"
            and _integration_field(r.body, "reason") == "STALE"
            and _integration_field(r.body, "source_comment_id")
            == str(lease_at_intent.anchor_comment_id)
            and _integration_field(r.body, "observed_head_sha")
            == observed_recovery_head
            and (t := base.parse_github_server_time(r.created_at)) is not None
            and t >= lease_at_intent.anchor_created_at
            + base.timedelta(seconds=base.SCHEMA3_TASK_OWNERSHIP_LEASE_SECONDS)
        ]
        if not eligible_intents or min(r.comment_id for r in eligible_intents) != intent_id:
            return False
    else:
        # HANDOFF/ORPHAN/other grants require their distinct full route.
        return False
    if any(
        r.kind in {"CLAIM", "RESUME", "RECOVER"}
        and r.state == "IN_PROGRESS"
        and owner.comment_id < r.comment_id < terminal.comment_id
        and r.declared_issue == issue_number
        for r in records
    ):
        return False
    lease = base.schema3_ownership_lease_state(
        owner, records, before_comment_id=terminal.comment_id,
    )
    return bool(
        lease is not None
        and terminal.head_sha == terminal.work_sha
        and base.schema3_owner_unexpired_at(owner, records, terminal) is True
    )


def _exact_causal_source_review(
    integrator_issue: int, integration: Any, source_pr: int, source_head: str,
) -> bool:
    """Check real producer, immutable final-head source, and distinct clean review.

    An unrelated real review-only squash must never become a playable source.
    All source and reviewer identities are fetched from their actual issue
    histories; comment IDs alone carry no trust or scope.
    """
    source_id = _positive_comment_number(
        _extension_field(integration.body, "source_producer_issue")
    )
    review_id = _positive_comment_number(
        _extension_field(integration.body, "required_independent_review_issue")
        or _extension_field(integration.body, "required_review_issue")
    )
    source_terminal_id = _positive_comment_number(
        _integration_field(integration.body, "source_terminal_comment_id")
    )
    review_terminal_id = _positive_comment_number(
        _integration_field(integration.body, "review_status_comment_id")
    )
    if (
        not all((source_id, review_id, source_terminal_id, review_terminal_id))
        or len({integrator_issue, source_id, review_id}) != 3
        or not _matching_extension(
            integration.body,
            ("source_producer_pr_number", "source_producer_pr", "source_pr_number"),
            str(source_pr),
        )
        or not _matching_extension(
            integration.body,
            ("source_producer_head_sha", "published_source_head"),
            source_head,
        )
    ):
        return False
    if (
        _integration_field(integration.body, "canonical_binding_comment_id")
        != "5675066392"
        or _integration_field(integration.body, "canonical_program_blob_sha")
        != "fd4cf1119c3f86acc3af620024eea72235e81ce4"
    ):
        return False

    source_issue = base.request("GET", f"/repos/{base.REPO}/issues/{source_id}")
    review_issue = base.request("GET", f"/repos/{base.REPO}/issues/{review_id}")
    if (
        not trusted_plan_issue(source_issue)
        or source_issue.get("state") != "closed"
        or source_issue.get("state_reason") in {"duplicate", "not_planned"}
        or not (
            "[IMPLEMENTATION-" in (source_issue.get("title") or "")
        )
        or "[FACTORY-" in (source_issue.get("title") or "")
        or not trusted_plan_issue(review_issue)
        or review_issue.get("state") != "closed"
        or "-REV-" not in (review_issue.get("title") or "")
    ):
        return False

    src_comments = list(base.paged(f"/repos/{base.REPO}/issues/{source_id}/comments?"))
    rev_comments = list(base.paged(f"/repos/{base.REPO}/issues/{review_id}/comments?"))
    source_records = base.operational_records_from_comments(source_id, src_comments)
    review_records = base.operational_records_from_comments(review_id, rev_comments)
    source = next(
        (r for r in source_records if r.comment_id == source_terminal_id), None
    )
    review = next(
        (r for r in review_records if r.comment_id == review_terminal_id), None
    )
    if (
        source is None or source.kind != "STATUS"
        or source.state != "REVIEW_READY"
        or source.authority_mode != "OWNER"
        or review is None or review.kind != "REVIEW_STATUS"
        or review.state != "REVIEW_READY"
        or review.authority_mode != "REVIEWER"
        or not _valid_owner_terminal(source_id, source_records, source)
        or not _valid_owner_terminal(review_id, review_records, review)
        or any(r.kind == "STATUS" and r.comment_id > source.comment_id
               for r in source_records)
        or any(r.kind == "REVIEW_STATUS" and r.comment_id > review.comment_id
               for r in review_records)
        or not source.comment_id < review.comment_id < integration.comment_id
        or len({source.actor_session_id, review.actor_session_id,
                 integration.actor_session_id}) != 3
        or _integration_field(source.body, "pr_number") != str(source_pr)
        or _integration_field(source.body, "pr_head_sha") != source_head
        or source.head_sha != source_head
        or _integration_field(source.body, "canonical_binding_comment_id")
        != "5675066392"
        or _integration_field(source.body, "canonical_program_blob_sha")
        != "fd4cf1119c3f86acc3af620024eea72235e81ce4"
        or _integration_field(review.body, "canonical_binding_comment_id")
        != "5675066392"
        or _integration_field(review.body, "canonical_program_blob_sha")
        != "fd4cf1119c3f86acc3af620024eea72235e81ce4"
        or not _matching_extension(
            review.body,
            ("immutable_source_issue", "immutable_producer_issue",
             "source_producer_issue", "producer_issue"), str(source_id),
        )
        or not _matching_extension(
            review.body,
            ("immutable_source_terminal_comment_id", "producer_terminal_comment_id",
             "source_producer_terminal_comment_id"), str(source_terminal_id),
        )
        or not _matching_extension(
            review.body,
            ("immutable_source_pr", "producer_source_pr",
             "frozen_source_pr", "source_producer_pr"), str(source_pr),
        )
        or not _matching_extension(
            review.body,
            ("immutable_source_head_sha", "producer_source_head",
             "frozen_source_pr_head_sha", "source_producer_head_sha"), source_head,
        )
    ):
        return False
    disposition = _extension_field(review.body, "disposition")
    declared_disposition = _integration_field(review.body, "review_disposition")
    if (
        disposition is None or not disposition.startswith("CLEAN_FOR_")
        or (declared_disposition is not None and declared_disposition != disposition)
        or _extension_field(integration.body, "required_review_disposition")
        != disposition
        or any(
            _extension_field(review.body, key) != "0"
            for key in ("blocker_count", "major_count", "correction_requiring_minor_count")
        )
    ):
        return False
    # The reviewed source's *actual* original PR must be the merged PR; a
    # borrowed report/verification PR is not a valid source even if its bytes
    # match a one-parent squash and its comment refs look plausible.
    pr = base.request("GET", f"/repos/{base.REPO}/pulls/{source_pr}")
    reviewer_pr = _positive_comment_number(
        _integration_field(review.body, "pr_number")
    )
    if reviewer_pr is None:
        return False
    review_pr = base.request("GET", f"/repos/{base.REPO}/pulls/{reviewer_pr}")
    if (
        pr.get("head", {}).get("ref") != f"planning/issue-{source_id}"
        or pr.get("head", {}).get("sha", "").lower() != source_head
        or review_pr.get("head", {}).get("ref") != f"planning/issue-{review_id}"
        or review_pr.get("head", {}).get("sha") != review.head_sha
        or review_pr.get("base", {}).get("ref") != "main"
        or reviewer_pr == source_pr
    ):
        return False
    source_files = list(base.paged(f"/repos/{base.REPO}/pulls/{source_pr}/files?"))
    review_files = list(base.paged(f"/repos/{base.REPO}/pulls/{reviewer_pr}/files?"))
    paths = {f["filename"] for f in source_files}
    reviewed_paths = {f["filename"] for f in review_files}
    return bool(
        paths
        and any(p.startswith("game/") for p in paths)
        and paths == set(base.list_scalar(source.body, "artifact_paths"))
        and len(paths) == len(source_files)
        and reviewed_paths
        and len(reviewed_paths) == len(review_files)
        and reviewed_paths == set(base.list_scalar(
            review.body, "artifact_paths"
        ))
        and all(p.startswith("docs/") for p in reviewed_paths)
        and all(base.SHA40_RE.fullmatch(f.get("sha", ""))
                and f.get("status") in {"added", "modified"}
                for f in review_files)
    )


def _integration_provenance(
    issue_number: int, comments: list[dict[str, Any]]
) -> tuple[str, str, int, str] | None:
    """Prove a valid winning owner, exact PR and expected single-parent squash.

    This is deliberately a conservative schema-3 subset: incomplete or
    contested histories must *not* create implementation demand authority.
    """
    records = base.operational_records_from_comments(issue_number, comments)
    terminal_records = [
        rec for rec in records
        if rec.kind == "INTEGRATION_STATUS" and rec.state == "DONE"
    ]
    if len(terminal_records) != 1:
        return None
    rec = terminal_records[0]
    fields = {
        key: _integration_field(rec.body, key)
        for key in (
            "protocol", "schema", "kind", "state", "merge_method", "main_sha",
            "pr_number", "canonicality",
        )
    }
    if (
        fields["protocol"] != "planning-v1"
        or fields["schema"] != "3"
        or fields["kind"] != "INTEGRATION_STATUS"
        or fields["state"] != "DONE"
        or fields["merge_method"] != "squash"
        or fields["canonicality"] not in {"NOT_CANONICAL", "NON_CANONICAL_PROVENANCE"}
    ):
        return None
    main_sha = fields["main_sha"]
    if main_sha is None or not base.SHA40_RE.fullmatch(main_sha):
        return None
    pr_number = fields["pr_number"]
    if pr_number is None or not pr_number.isdigit() or int(pr_number) <= 0:
        return None

    # The original first-playable publication used a narrowly scoped legacy
    # externally authorized integration form. Accept only its exact immutable
    # pinned record and owner directive, never a general EXTERNAL escape.
    legacy = issue_number == 1343 and rec.comment_id == 5935663772
    if legacy:
        source_head = _integration_field(rec.body, "expected_head_sha")
        parent = _integration_field(rec.body, "observed_pre_merge_main_sha")
        if (
            _integration_field(rec.body, "authority_mode") != "EXTERNAL"
            or _integration_field(rec.body, "external_authorization_comment_id")
            != "5277825639"
            or _integration_field(rec.body, "producer_terminal_comment_id")
            != "5935515528"
            or _integration_field(rec.body, "review_terminal_comment_id")
            != "5935624483"
            or int(pr_number) != 1370
        ):
            return None
    else:
        keys = (
            "issue", "mission_id", "branch", "actor_session_id",
            "authority_mode", "ownership_generation_comment_id",
            "head_sha", "work_sha", "expected_pre_merge_head_sha",
            "observed_pre_merge_main_sha", "source_terminal_comment_id",
            "review_status_comment_id",
        )
        f = {key: _integration_field(rec.body, key) for key in keys}
        if (
            f["issue"] != str(issue_number)
            or f["branch"] != f"planning/issue-{issue_number}"
            or f["authority_mode"] != "OWNER"
            or rec.declared_issue != issue_number
            or rec.actor_session_id != f["actor_session_id"]
            or rec.mission_id != f["mission_id"]
            or not f["actor_session_id"]
            or not f["mission_id"]
            or not f["source_terminal_comment_id"]
            or not f["review_status_comment_id"]
            or not all(
                f[key] and base.SHA40_RE.fullmatch(f[key])
                for key in ("head_sha", "work_sha")
            )
        ):
            return None

        # Reconstruct first-winner or canonical valid STALE recovery; a raw
        # matching RECOVER record is never sufficient to confer authority.
        if not _valid_owner_terminal(issue_number, records, rec):
            return None
        lease = base.schema3_ownership_lease_state(
            next(record for record in records
                 if record.comment_id == rec.ownership_generation_comment_id),
            records, before_comment_id=rec.comment_id,
        )
        if lease is None or lease.observed_head_sha.lower() != f["head_sha"].lower():
            return None
        # An integrator branch may remain at its claim base when publishing
        # only the independently reviewed source PR.
        if (
            f["work_sha"] != f["head_sha"]
            or not base.SHA40_RE.fullmatch(f["head_sha"])
        ):
            return None
        source_head = f["expected_pre_merge_head_sha"]
        parent = f["observed_pre_merge_main_sha"]
        if (
            _integration_field(rec.body, "expected_pre_merge_main_sha") != parent
            or _integration_field(rec.body, "expected_source_head_sha") != source_head
        ):
            return None

    if not all(
        sha is not None and base.SHA40_RE.fullmatch(sha)
        for sha in (parent, source_head)
    ):
        return None
    return main_sha.lower(), parent.lower(), int(pr_number), source_head.lower()


def _real_squash_main_sha(
    main_sha: str, parent: str, pr_number: int, source_head: str
) -> bool:
    """Bind GitHub's merged PR, exact source blobs, and one-parent main commit."""
    try:
        pr = base.request("GET", f"/repos/{base.REPO}/pulls/{pr_number}")
        commit = base.request("GET", f"/repos/{base.REPO}/commits/{main_sha}")
        if (
            not pr.get("merged")
            or pr.get("state") != "closed"
            or pr.get("merge_commit_sha", "").lower() != main_sha
            or pr.get("base", {}).get("ref") != "main"
            or pr.get("head", {}).get("sha", "").lower() != source_head
            or len(commit.get("parents", [])) != 1
            or commit["parents"][0].get("sha", "").lower() != parent
            or commit.get("sha", "").lower() != main_sha
        ):
            return False
        source_files = list(base.paged(
            f"/repos/{base.REPO}/pulls/{pr_number}/files?"
        ))
        squash = base.request(
            "GET", f"/repos/{base.REPO}/compare/{parent}...{main_sha}"
        )
        published_files = squash.get("files", [])
        if (
            squash.get("status") != "ahead"
            or squash.get("ahead_by") != 1
            or len(source_files) == 0
            or len(source_files) != len(published_files)
            or len(squash.get("commits", [])) != 1
        ):
            return False
        original = {
            file["filename"]: (file.get("sha", "").lower(), file.get("status"))
            for file in source_files
        }
        published = {
            file["filename"]: (file.get("sha", "").lower(), file.get("status"))
            for file in published_files
        }
        return (
            len(original) == len(source_files)
            and len(published) == len(published_files)
            and all(
                base.SHA40_RE.fullmatch(sha) and status in {"added", "modified"}
                for sha, status in original.values()
            )
            and original == published
        )
    except base.GitHubRateLimitExceeded:
        raise
    except (KeyError, TypeError, ValueError, RuntimeError):
        return False


def integration_main_sha_from_comments(
    issue_number: int,
    comments: Iterable[dict[str, Any]],
) -> str | None:
    """Only actual reviewed, owned or pinned-legacy squash commits are usable."""
    all_comments = list(comments)
    trusted_comments = [
        comment for comment in all_comments
        if _trusted_unedited_comment(comment)
    ]
    provenance = _integration_provenance(issue_number, trusted_comments)
    if provenance is None:
        return None
    main_sha, parent, pr_number, source_head = provenance
    if issue_number != 1343:
        records = base.operational_records_from_comments(issue_number, trusted_comments)
        integration = next(r for r in records if r.kind == "INTEGRATION_STATUS" and r.state == "DONE")
        if not _exact_causal_source_review(issue_number, integration, pr_number, source_head):
            return None
    if not _real_squash_main_sha(main_sha, parent, pr_number, source_head):
        return None
    return main_sha

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
    integrated_sources: dict[int, str],
) -> dict[str, Any] | None:
    """Pick latest *verified squash*, not highest issue number.

    The latest verified source is selected before the consumed test. Older
    unconsumed sources are never replayed after a newer milestone is consumed.
    """
    recent_list = list(recent_issues)
    candidates = [
        issue for issue in recent_list
        if int(issue.get("number", 0)) in integrated_sources
        and implementation_source_candidate(issue)
    ]
    if not candidates:
        return None
    newest = candidates[0]
    newest_sha = integrated_sources[int(newest["number"])]
    for candidate in candidates[1:]:
        other_sha = integrated_sources[int(candidate["number"])]
        if not all(
            base.SHA40_RE.fullmatch(sha) for sha in (newest_sha, other_sha)
        ) or newest_sha == other_sha:
            return None
        # Github 'ahead' means candidate is newer; 'behind' means older.
        ancestry = base.request(
            "GET", f"/repos/{base.REPO}/compare/{newest_sha}...{other_sha}"
        )
        if ancestry.get("status") == "ahead":
            newest, newest_sha = candidate, other_sha
        elif ancestry.get("status") != "behind":
            return None  # diverged/unknown; never guess chronology
    # Verify every candidate really precedes the winner, not merely that
    # pairwise tournament results happened to be favorable.
    for issue in candidates:
        sha = integrated_sources[int(issue["number"])]
        if sha == newest_sha:
            if issue is not newest:
                return None
            continue
        comparison = base.request(
            "GET", f"/repos/{base.REPO}/compare/{sha}...{newest_sha}"
        )
        if comparison.get("status") != "ahead":
            return None
    if int(newest["number"]) in consumed_implementation_sources(recent_list):
        return None
    return newest

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
        open_issues, recent_issues, integrated_sources
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

    # Explicit adversarial regression: six-field faux integration capsule
    # must not gain ownership or cause any GitHub lookups.
    faux = {
        "id": 101, "created_at": "2026-10-05T10:00:00Z",
        "updated_at": "2026-10-05T10:00:00Z",
        "author_association": "OWNER", "user": {"login": "vokerg"},
        "body": (
            "```yaml\nprotocol: planning-v1\nschema: 3\n"
            "kind: INTEGRATION_STATUS\nstate: DONE\n"
            "merge_method: squash\nmain_sha: " + "a" * 40 + "\n```\n"
        ),
    }
    assert integration_main_sha_from_comments(1539, [faux]) is None
    assert integration_main_sha_from_comments(1558, [dict(
        faux, body=faux["body"].replace("main_sha:", "issue: 999\\nmain_sha:"),
    )]) is None
    # Spoofed ownership, nonexistent source PR and unverified Git commit
    # cannot be repaired merely by adding plausible scalar fields.

    # Literal v7 module regression fixtures: the real merged PR must match
    # the independently reviewed producer, and canonical STALE recovery is
    # valid only after the original lease and exact winning intent mature.
    original_paged, original_api = base.paged, base.request
    clock = (
        "2026-10-04T00:00:00Z", "2026-10-04T00:10:00Z",
        "2026-10-04T06:11:00Z", "2026-10-04T06:12:00Z",
        "2026-10-04T07:05:00Z", "2026-10-04T07:15:00Z",
        "2026-10-04T07:20:00Z", "2026-10-04T07:30:00Z",
        "2026-10-04T07:40:00Z",
    )
    base_a, main_b, work_c, review_d, squash_f = (
        "a" * 40, "b" * 40, "c" * 40, "d" * 40, "f" * 40,
    )

    def cmt(n: int, issue_n: int, when: str, capsule: str) -> dict[str, Any]:
        return {
            "id": n, "created_at": when, "updated_at": when,
            "author_association": "OWNER", "user": {"login": "vokerg"},
            "issue_url": f"https://api.github.com/repos/vokerg/everfield/issues/{issue_n}",
            "body": "```yaml\nprotocol: planning-v1\nschema: 3\n" + capsule + "\n```\n",
        }

    source_claim = cmt(100, 9001, clock[0],
        f"kind: CLAIM\nissue: 9001\nmission_id: PRODUCER\n"
        "branch: planning/issue-9001\nactor_session_id: producer-original\n"
        "state: IN_PROGRESS\nprevious_ownership_comment_id: null\n"
        f"base_sha: {base_a}\nobserved_head_sha: {base_a}")
    source_advance = cmt(105, 9001, clock[1],
        f"kind: PROGRESS\nissue: 9001\nmission_id: PRODUCER\n"
        "branch: planning/issue-9001\nactor_session_id: producer-original\n"
        "state: IN_PROGRESS\nownership_generation_comment_id: 100\n"
        f"progress_basis: HEAD_ADVANCE\nobserved_head_sha: {work_c}\n"
        f"evidence_refs:\n  - {work_c}")
    source_intent = cmt(115, 9001, clock[2],
        "kind: RESUME_INTENT\nissue: 9001\nmission_id: PRODUCER\n"
        "branch: planning/issue-9001\nactor_session_id: producer-recovered\n"
        "reason: STALE\nsource_comment_id: 105\n"
        f"observed_head_sha: {work_c}")
    source_recover = cmt(117, 9001, clock[3],
        "kind: RECOVER\nissue: 9001\nmission_id: PRODUCER\n"
        "branch: planning/issue-9001\nactor_session_id: producer-recovered\n"
        "state: IN_PROGRESS\nrecovery_reason: STALE\n"
        "previous_ownership_comment_id: 100\n"
        "winning_intent_comment_id: 115\nsource_comment_id: 105\n"
        f"observed_head_sha: {work_c}")
    source_terminal = cmt(120, 9001, clock[4],
        "kind: STATUS\nissue: 9001\nmission_id: PRODUCER\n"
        "branch: planning/issue-9001\nactor_session_id: producer-recovered\n"
        "state: REVIEW_READY\nterminal: true\nauthority_mode: OWNER\n"
        "ownership_generation_comment_id: 117\n"
        f"base_sha: {base_a}\nwork_sha: {work_c}\nhead_sha: {work_c}\n"
        f"pr_number: 9901\npr_head_sha: {work_c}\n"
        "canonical_binding_comment_id: 5675066392\n"
        "canonical_program_blob_sha: fd4cf1119c3f86acc3af620024eea72235e81ce4\n"
        "artifact_paths:\n  - game/main.gd\n  - docs/planning/handoffs/source.md")
    reviewer_claim = cmt(200, 9002, clock[5],
        "kind: CLAIM\nissue: 9002\nmission_id: REQUIRED-REVIEW\n"
        "branch: planning/issue-9002\nactor_session_id: distinct-reviewer\n"
        "state: IN_PROGRESS\nprevious_ownership_comment_id: null\n"
        f"base_sha: {main_b}\nobserved_head_sha: {main_b}")
    reviewer_advance = cmt(205, 9002, clock[5],
        "kind: PROGRESS\nissue: 9002\nmission_id: REQUIRED-REVIEW\n"
        "branch: planning/issue-9002\nactor_session_id: distinct-reviewer\n"
        "state: IN_PROGRESS\nownership_generation_comment_id: 200\n"
        f"progress_basis: HEAD_ADVANCE\nobserved_head_sha: {review_d}\n"
        f"evidence_refs:\n  - {review_d}")
    reviewer_terminal = cmt(220, 9002, clock[6],
        "kind: REVIEW_STATUS\nissue: 9002\nmission_id: REQUIRED-REVIEW\n"
        "branch: planning/issue-9002\nactor_session_id: distinct-reviewer\n"
        "state: REVIEW_READY\nterminal: true\nauthority_mode: REVIEWER\n"
        "ownership_generation_comment_id: 200\n"
        f"base_sha: {main_b}\nwork_sha: {review_d}\nhead_sha: {review_d}\n"
        "pr_number: 9902\ncanonical_binding_comment_id: 5675066392\n"
        "canonical_program_blob_sha: fd4cf1119c3f86acc3af620024eea72235e81ce4\n"
        "artifact_paths:\n  - docs/planning/reviews/review.md\n"
        "extensions:\n"
        "  disposition: CLEAN_FOR_SOURCE_PUBLICATION\n"
        "  blocker_count: 0\n  major_count: 0\n"
        "  correction_requiring_minor_count: 0\n"
        "  immutable_source_issue: 9001\n"
        "  immutable_source_terminal_comment_id: 120\n"
        "  immutable_source_pr: 9901\n"
        f"  immutable_source_head_sha: {work_c}")
    integrator_claim = cmt(300, 9003, clock[7],
        "kind: CLAIM\nissue: 9003\nmission_id: INTEGRATION\n"
        "branch: planning/issue-9003\nactor_session_id: integrator\n"
        "state: IN_PROGRESS\nprevious_ownership_comment_id: null\n"
        f"base_sha: {main_b}\nobserved_head_sha: {main_b}")
    integration_terminal = cmt(320, 9003, clock[8],
        "kind: INTEGRATION_STATUS\nissue: 9003\nmission_id: INTEGRATION\n"
        "branch: planning/issue-9003\nactor_session_id: integrator\n"
        "state: DONE\nterminal: true\nauthority_mode: OWNER\n"
        "ownership_generation_comment_id: 300\n"
        f"base_sha: {main_b}\nwork_sha: {main_b}\nhead_sha: {main_b}\n"
        f"observed_pre_merge_main_sha: {main_b}\n"
        f"expected_pre_merge_main_sha: {main_b}\n"
        f"expected_pre_merge_head_sha: {work_c}\n"
        f"expected_source_head_sha: {work_c}\n"
        f"pr_number: 9901\nmain_sha: {squash_f}\n"
        "merge_method: squash\n"
        "source_terminal_comment_id: 120\nreview_status_comment_id: 220\n"
        "canonicality: NOT_CANONICAL\n"
        "canonical_binding_comment_id: 5675066392\n"
        "canonical_program_blob_sha: fd4cf1119c3f86acc3af620024eea72235e81ce4\n"
        "extensions:\n  source_producer_issue: 9001\n"
        "  source_producer_pr_number: 9901\n"
        f"  source_producer_head_sha: {work_c}\n"
        "  required_independent_review_issue: 9002\n"
        "  required_review_disposition: CLEAN_FOR_SOURCE_PUBLICATION")
    source_first_terminal = dict(
        source_terminal,
        created_at="2026-10-04T01:05:00Z",
        updated_at="2026-10-04T01:05:00Z",
        body=source_terminal["body"].replace(
            "actor_session_id: producer-recovered", "actor_session_id: producer-original"
        ).replace(
            "ownership_generation_comment_id: 117", "ownership_generation_comment_id: 100"
        ),
    )
    producer_issue = issue(
        9001, "[PLAN-v1][IMPLEMENTATION-INCREMENT-TEST-01] Source",
        "IMPLEMENTATION_INCREMENT / TEST", state="closed",
        state_reason="completed",
    )
    reviewer_issue = issue(
        9002, "[PLAN-v1][IMPLEMENTATION-INCREMENT-TEST-REV-01] Review",
        state="closed", state_reason="completed",
    )
    producer_files = [
        {"filename": "game/main.gd", "sha": "1" * 40, "status": "modified"},
        {"filename": "docs/planning/handoffs/source.md", "sha": "2" * 40,
         "status": "added"},
    ]
    reviewer_files = [
        {"filename": "docs/planning/reviews/review.md", "sha": "3" * 40,
         "status": "added"},
    ]
    api_map = {
        f"/repos/{base.REPO}/issues/9001": producer_issue,
        f"/repos/{base.REPO}/issues/9002": reviewer_issue,
        f"/repos/{base.REPO}/pulls/9901": {
            "merged": True, "state": "closed",
            "merge_commit_sha": squash_f, "base": {"ref": "main"},
            "head": {"sha": work_c, "ref": "planning/issue-9001"},
        },
        f"/repos/{base.REPO}/pulls/9902": {
            "merged": False, "base": {"ref": "main"},
            "head": {"sha": review_d, "ref": "planning/issue-9002"},
        },
        f"/repos/{base.REPO}/commits/{squash_f}": {
            "sha": squash_f, "parents": [{"sha": main_b}],
        },
        f"/repos/{base.REPO}/compare/{main_b}...{squash_f}": {
            "status": "ahead", "ahead_by": 1,
            "files": producer_files, "commits": [{"sha": squash_f}],
        },
    }
    archive = {
        9001: [source_claim, source_advance, source_intent,
               source_recover, source_terminal],
        9002: [reviewer_claim, reviewer_advance, reviewer_terminal],
        9003: [integrator_claim, integration_terminal],
    }

    def fixture_request(method: str, path: str,
                        payload: Any = None) -> Any:
        assert method == "GET"
        return api_map[path]

    def fixture_paged(path: str) -> Iterable[dict[str, Any]]:
        match = re.search(r"/issues/(\d+)/comments", path)
        if match:
            return archive[int(match.group(1))]
        if "/pulls/9901/files" in path:
            return producer_files
        if "/pulls/9902/files" in path:
            return reviewer_files
        raise AssertionError(path)

    base.request, base.paged = fixture_request, fixture_paged
    try:
        assert integration_main_sha_from_comments(9003, archive[9003]) == squash_f
        # Legitimate real-history shape (#1507): owner pushed the exact frozen
        # producer branch before expiry without a PROGRESS renewal. The STALE
        # intent observes that immutable branch HEAD rather than claim-base.
        # GitHub source PR/terminal checks, not PROGRESS, bind that final head.
        unrenewed_intent = dict(source_intent, body=source_intent["body"].replace(
            "source_comment_id: 105", "source_comment_id: 100",
        ))
        unrenewed_recover = dict(source_recover, body=source_recover["body"].replace(
            "source_comment_id: 105", "source_comment_id: 100",
        ))
        archive[9001] = [source_claim, unrenewed_intent,
                         unrenewed_recover, source_terminal]
        assert integration_main_sha_from_comments(9003, archive[9003]) == squash_f
        archive[9001] = [source_claim, source_advance, source_intent,
                         source_recover, source_terminal]
        # Positive original first-winner producer (no recovery), same reviewed
        # source and immutable PR, even while code advances HEAD.
        archive[9001] = [source_claim, source_first_terminal]
        assert integration_main_sha_from_comments(9003, archive[9003]) == squash_f
        archive[9001] = [source_claim, source_advance, source_first_terminal]
        assert integration_main_sha_from_comments(9003, archive[9003]) == squash_f
        archive[9001] = [source_claim, source_advance, source_intent,
                         source_recover, source_terminal]
        # Required positive canonical recovered INTEGRATOR owner: #1572-like
        # expiry route, separate from a recovered producer/reviewer route.
        integ_intent = cmt(310, 9003, "2026-10-04T13:31:00Z",
            "kind: RESUME_INTENT\nissue: 9003\nmission_id: INTEGRATION\n"
            "branch: planning/issue-9003\nactor_session_id: integrator-recovered\n"
            "reason: STALE\nsource_comment_id: 300\n"
            f"observed_head_sha: {main_b}")
        integ_recover = cmt(315, 9003, "2026-10-04T13:32:00Z",
            "kind: RECOVER\nissue: 9003\nmission_id: INTEGRATION\n"
            "branch: planning/issue-9003\nactor_session_id: integrator-recovered\n"
            "state: IN_PROGRESS\nrecovery_reason: STALE\n"
            "previous_ownership_comment_id: 300\n"
            "winning_intent_comment_id: 310\nsource_comment_id: 300\n"
            f"observed_head_sha: {main_b}")
        recovered_integration = dict(
            integration_terminal,
            created_at="2026-10-04T13:40:00Z",
            updated_at="2026-10-04T13:40:00Z",
            body=integration_terminal["body"]
            .replace("actor_session_id: integrator\n",
                     "actor_session_id: integrator-recovered\n")
            .replace("ownership_generation_comment_id: 300",
                     "ownership_generation_comment_id: 315"),
        )
        archive[9003] = [
            integrator_claim, integ_intent, integ_recover, recovered_integration,
        ]
        assert integration_main_sha_from_comments(9003, archive[9003]) == squash_f
        for bad_record in (
            dict(integ_intent, created_at="2026-10-04T13:29:00Z",
                 updated_at="2026-10-04T13:29:00Z"),
            dict(integ_intent, body=integ_intent["body"].replace(
                "source_comment_id: 300", "source_comment_id: 999")),
            dict(integ_recover, body=integ_recover["body"].replace(
                "winning_intent_comment_id: 310",
                "winning_intent_comment_id: 999")),
            dict(integ_recover, body=integ_recover["body"].replace(
                "previous_ownership_comment_id: 300",
                "previous_ownership_comment_id: 999")),
        ):
            history = [
                integrator_claim,
                bad_record if bad_record["id"] == 310 else integ_intent,
                bad_record if bad_record["id"] == 315 else integ_recover,
                recovered_integration,
            ]
            assert integration_main_sha_from_comments(9003, history) is None
        archive[9003] = [
            integrator_claim,
            dict(integ_intent, body=integ_intent["body"].replace(
                "actor_session_id: integrator-recovered",
                "actor_session_id: unrelated-winner")),
            integ_intent, integ_recover, recovered_integration,
        ]
        # The actual duplicate has a prior comment ID and wins contention.
        archive[9003][1]["id"] = 309
        assert integration_main_sha_from_comments(9003, archive[9003]) is None
        archive[9003] = [integrator_claim, integration_terminal]
        # Reviewer-only documentation changes may not pose as producer paths.
        archive[9002] = [reviewer_claim, reviewer_terminal]
        assert integration_main_sha_from_comments(9003, archive[9003]) == squash_f
        archive[9002] = [reviewer_claim, reviewer_advance, reviewer_terminal]

        # Absent/dangling source and reviewer; unrelated real review PR cannot
        # be substituted for the true source PR/squash.
        for original, tamper in (
            ("source_terminal_comment_id: 120",
             "source_terminal_comment_id: 999999"),
            ("review_status_comment_id: 220",
             "review_status_comment_id: 999999"),
            ("source_producer_issue: 9001", "source_producer_issue: 9002"),
            ("pr_number: 9901", "pr_number: 9902"),
            (f"expected_pre_merge_head_sha: {work_c}",
             f"expected_pre_merge_head_sha: {review_d}"),
        ):
            bad = dict(integration_terminal,
                       body=integration_terminal["body"].replace(original, tamper))
            assert integration_main_sha_from_comments(
                9003, [integrator_claim, bad]
            ) is None, original
        for original, tamper in (
            ("mission_id: INTEGRATION", "mission_id: FOREIGN"),
            ("issue: 9003", "issue: 9002"),
            ("state: DONE", "state: REVIEW_READY"),
            ("authority_mode: OWNER", "authority_mode: EXTERNAL"),
            ("merge_method: squash", "merge_method: rebase"),
            ("ownership_generation_comment_id: 300",
             "ownership_generation_comment_id: 999"),
        ):
            bad = dict(integration_terminal, body=integration_terminal[
                "body"].replace(original, tamper))
            assert integration_main_sha_from_comments(
                9003, [integrator_claim, bad]
            ) is None, original
        edited_integrator = dict(integration_terminal,
                                 updated_at="2026-10-04T09:00:00Z")
        assert integration_main_sha_from_comments(
            9003, [integrator_claim, edited_integrator]
        ) is None

        # Strict canonical STALE intent maturity, winning source/head and
        # same-generation recovery; rejected recovered owner cannot publish.
        for item, original, tamper in (
            (source_intent, "source_comment_id: 105", "source_comment_id: 100"),
            (source_intent, "observed_head_sha: " + work_c,
             "observed_head_sha: " + base_a),
            (source_recover, "winning_intent_comment_id: 115",
             "winning_intent_comment_id: 9999"),
            (source_recover, "previous_ownership_comment_id: 100",
             "previous_ownership_comment_id: 9999"),
        ):
            archive[9001] = [
                dict(c, body=c["body"].replace(original, tamper)) if c is item else c
                for c in [source_claim, source_advance, source_intent,
                          source_recover, source_terminal]
            ]
            assert integration_main_sha_from_comments(
                9003, archive[9003]
            ) is None, original
        archive[9001] = [source_claim, source_advance,
                         dict(source_intent, created_at=clock[1],
                              updated_at=clock[1]),
                         source_recover, source_terminal]
        assert integration_main_sha_from_comments(9003, archive[9003]) is None
        archive[9001] = [source_claim, source_advance, source_intent,
                         source_recover, source_terminal]
        archive[9002] = [reviewer_claim, reviewer_advance,
                         dict(reviewer_terminal, updated_at=clock[8])]
        assert integration_main_sha_from_comments(9003, archive[9003]) is None
        archive[9002] = [reviewer_claim, reviewer_advance, reviewer_terminal,
            cmt(221, 9002, clock[6],
                "kind: REVIEW_STATUS\nissue: 9002\n"
                "mission_id: REQUIRED-REVIEW\nstate: CHANGES_NEEDED\n"
                "branch: planning/issue-9002\n"
                "actor_session_id: distinct-reviewer")]
        assert integration_main_sha_from_comments(9003, archive[9003]) is None
        archive[9002] = [reviewer_claim, reviewer_advance, reviewer_terminal]
        review_file_original = reviewer_files[0]
        reviewer_files[0] = dict(review_file_original, filename="game/main.gd")
        assert integration_main_sha_from_comments(9003, archive[9003]) is None
        reviewer_files[0] = review_file_original
        print("frontier v7 source/review causal authority and STALE recovery fixtures: PASS")
    finally:
        base.request, base.paged = original_api, original_paged


    original_request = base.request
    tested_comparisons: list[str] = []
    def mock_ancestry(method: str, path: str, payload: Any = None) -> dict[str, Any]:
        assert method == "GET" and "/compare/" in path
        tested_comparisons.append(path)
        refs = path.rsplit("/compare/", 1)[1].split("...")
        assert len(refs) == 2
        positions = {"a" * 40: 0, "b" * 40: 1, "c" * 40: 2}
        if refs[0] not in positions or refs[1] not in positions:
            return {"status": "diverged"}
        if positions[refs[0]] < positions[refs[1]]:
            return {"status": "ahead"}
        if positions[refs[0]] > positions[refs[1]]:
            return {"status": "behind"}
        return {"status": "identical"}
    base.request = mock_ancestry
    try:
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
            {1343: 'a' * 40},
        )
        assert selected is first_playable

        component = issue(
            1410,
            "[PLAN-v1][IMPLEMENTATION-DEMAND-OLD-WORKS-WORLD-01] Implement world presentation",
            "IMPLEMENTATION_COMPONENT / WORLD_PRESENTATION",
        )
        assert is_live_implementation_work(component)
        # A blocked issue is not a global veto on new integration-driven work.
        assert select_implementation_demand_source(
            [component],
            [first_playable, component],
            {1343: 'a' * 40},
        ) is first_playable

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
            {1343: 'a' * 40},
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
            {1343: 'a' * 40},
        ) is first_playable

        assert select_implementation_demand_source(
            [], [first_playable], {}
        ) is None

        later_integration = issue(
            1539,
            "[PLAN-v1][IMPLEMENTATION-INCREMENT-PLAYABLE-SEAMS-02-INT-01] Squash fan-in",
            "AUTHORIZED_INTEGRATION / NONCANONICAL_PLAYABLE_SOURCE",
            state="closed", state_reason="completed",
        )
        assert implementation_source_candidate(later_integration)
        assert not implementation_source_candidate(
            issue(1540, "[PLAN-v1][IMPLEMENTATION-INCREMENT-PLAYABLE-SEAMS-02-REV-INT-01] Review publication",
                  "AUTHORIZED_INTEGRATION / REVIEW_PROVENANCE",
                  state="closed", state_reason="completed")
        )
        source_history = [first_playable, completed_intake, later_integration]
        assert select_implementation_demand_source(
            [component], source_history, {1343: 'a' * 40, 1539: 'b' * 40}
        ) is later_integration
        owner_intake = issue(
            1542,
            "[PLAN-v1][W2-IMPLEMENTATION-DEMAND-POST-PLAYABLE-SEAMS-01] Route bounded increment",
            "IMPLEMENTATION_DEMAND_INTAKE / ROUTING ONLY; after #1539's "
            "clean-reviewed source squash and #1540's review-provenance squash.",
            state="closed", state_reason="completed",
        )
        assert 1539 in consumed_implementation_sources([owner_intake])
        assert select_implementation_demand_source(
            [component], source_history + [owner_intake], {1343: 'a' * 40, 1539: 'b' * 40}
        ) is None
        # An explicit owner intake makes history terminal even if no issues are open.
        assert select_implementation_demand_source(
            [], source_history + [owner_intake], {1343: 'a' * 40, 1539: 'b' * 40}
        ) is None
        invalid_owner_intake = dict(owner_intake, user={"login": "attacker"},
                                    author_association="NONE")
        assert 1539 not in consumed_implementation_sources([invalid_owner_intake])

        fan_in = issue(
            1420,
            "[PLAN-v1][IMPLEMENTATION-INCREMENT-OLD-WORKS-PRESENTATION-01] Integrate presentation",
            "## Role / task class\n`IMPLEMENTATION_INCREMENT / PLAYABLE_FAN_IN`.",
            state="closed",
            state_reason="completed",
        )
        assert implementation_source_candidate(fan_in)
        # Inverted historical issue numbers: the later actual squash wins,
        # even where its issue number is lower.
        assert select_implementation_demand_source(
            [], [first_playable, later_integration],
            {1343: "c" * 40, 1539: "b" * 40},
        ) is first_playable
        # A consumed latest squash does not backfill older integrated work.
        assert select_implementation_demand_source(
            [], [first_playable, later_integration, completed_intake],
            {1343: "c" * 40, 1539: "b" * 40},
        ) is None
        assert tested_comparisons
    finally:
        base.request = original_request
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
