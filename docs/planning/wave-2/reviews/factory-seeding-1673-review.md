# Independent required adversarial security review — factory source #1673 / PR #1675

**Mission:** FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-16-CI-CONVERGENCE-01-REV-01  
**Review issue / claim:** #1677 / immutable GitHub comment #6118729031 (2026-10-12T06:05:50Z)  
**Review actor:** frontier-independent-factory-audit-1677-gpt6-20261012-0810-cph-01  
**Disposition: CHANGES_NEEDED — 1 BLOCKER, 1 MAJOR, 0 correction-requiring MINOR.**

## Frozen authority and limits

- Current main on inspection: `8f8223b0c58956bbc888760ef14f63fa79d2117d`; canonical Planning Program v1 blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, Issue #1147 binding #5675066392, ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Producer Issue #1673 sole source `STATUS(REVIEW_READY)` #6118356905, draft source PR #1675 `planning/issue-1673` -> `main`, exact HEAD `b8c4d54b80fbc360c2c036ffe886371d545edbc9`; 22 changed paths, of which base, v5, v6 and v7 modules and 16 historical handoffs are inherited in the separately scoped source. Source ownership actor differs from this review execution.
- Exact frozen GitHub Actions PR run #38208211580: completed/success, `validate-pr` job #114676323766 success, mutating `maintain` job #114676325037 skipped. These are producer-authored self-tests, **not** independent security acceptance.
- Independently inspected full source code and relevant predecessor contract, read-only GitHub PR file list, base parser, `schema3_ownership_lease_state`, `github_verified_head_advance`, closure consumer, v5 successor recognition and v7 integration/owner paths. No source, verifier, gameplay, prior reviewer, or main write was made. The findings concern the *actual deployed routing/closure consumers*, not merely synthetic fixture statements.

## FSR-1677-B01 — BLOCKER: terminal storage closure accepts an expired/nonwinning owner

**Evidence:** `tools/planning/frontier_maintenance.py`, exact blob `1a4774f894d18f5df11fccbf0d29792ad157e81e`, `reconcilable_terminal_from_comments` approximately lines 677–719 and `close_terminal_open_issues` approximately lines 886–901; `frontier_maintenance_v7.py::main` calls that closure path before the strictly authenticated v5/v7 routing consumers.

`reconcilable_terminal_from_comments` recognizes the latest terminal and *any preceding* same-actor/same-mission owner-shaped `CLAIM|RESUME|RECOVER`. It never verifies first winning schema-3 ownership generation, valid intent/grant transitions, owner lease, `PROGRESS` renewal, current generation, real branch/head, or that the terminal was created before the six-hour lease expired. `close_terminal_open_issues` then unconditionally PATCHes such a GitHub-open issue to `closed` outside DRY_RUN. The new GitHub-backed `github_verified_head_advance` is passed in some v5/v7 consumers but **never invoked on the base closure route**. This violates the canonical “conservatively proven terminal” maintenance constraint. Even a valid root YAML parser cannot repair absent ownership authorization.

**Minimal executable read-only reproduction from checkout at PR #1675 HEAD:**

```python
import sys
sys.path.insert(0, "tools/planning")
import frontier_maintenance as b

H = "a" * 40
def comment(number, at, capsule):
    return {
        "id": number, "created_at": at, "updated_at": at,
        "author_association": "OWNER",
        "body": "```yaml\n" + capsule + "\n```",
    }

base = ("protocol: planning-v1\nschema: 3\nissue: 987654\n"
        "mission_id: SECURITY-REPRO\nbranch: planning/issue-987654\n"
        "actor_session_id: repro-owner\n")
claim = comment(1, "2026-10-12T00:00:00Z",
    base + "kind: CLAIM\nstate: IN_PROGRESS\nbase_sha: " + H +
    "\nobserved_head_sha: " + H + "\nprevious_ownership_comment_id: null")
late_terminal = comment(2, "2026-10-12T07:00:00Z",
    base + "kind: STATUS\nstate: DONE\nterminal: true\n"
    "authority_mode: OWNER\nownership_generation_comment_id: 1\n"
    "head_sha: " + H + "\nwork_sha: " + H)
records = b.operational_records_from_comments(987654, [claim, late_terminal])
assert b.schema3_owner_unexpired_at(records[0], records, records[1]) is False
assert b.reconcilable_terminal_from_comments(987654, [claim, late_terminal]) is not None
# The production close_terminal_open_issues() treats this as closeable.
```

The `07:00Z` terminal is an hour after exact lease expiry (`06:00Z`), yet storage closure grants it terminal effect. Replacing `CLAIM` with a syntactically valid unlinked `RESUME`, or adding a later valid generation, exposes the same missing owner-graph check. The test uses mock comment data in memory and makes no GitHub mutation. The insecure decision follows directly from the named source predicates; do not claim this snippet exercised hosted CI independently.

**Required correction:** Guard every mutating closure with actual first-winning prefix-scoped current-owner and in-lease terminal validation, including authenticated HEAD_ADVANCE where a PROGRESS renewal is needed. Unknown/malformed/edited history must **not** authorize closure. Add regression proofs for expiry, losing CLAIM, unlinked RESUME, nonwinning RECOVER, later owner generation, false SHA-only PROGRESS and valid current terminal. Do not simply disable all terminal reconciliation or accept GitHub-open as planning authority.

## FSR-1677-M01 — MAJOR: real live factory successors are missed by source v5 grammar

**Evidence:** `tools/planning/frontier_maintenance_v5.py`, blob `d2b55cfe84e3c243e5fc9b3e2a5c0433352887ab`, `explicit_successor_issue_numbers` approximately lines 300–330, `explicit_successor_generation_consumed` lines 337–355, `retire_explicit_successor_transitions` lines 373–412 and `materialize_missing_transitions` lines 510 onward.

The source attempts to stop recursive wrappers for already-materialized exact successors. However, it accepts multiple `ISSUE_N` tokens **only** when the literal route contains `_THEN_ISSUE_`. Actual terminal #1664 comment #6118374703 names existing live successor #1673 plus mandatory reviewer #1677 via `EXISTING_ISSUE_1673_..._REVIEW_ISSUE_1677_THEN_ONLY_...`. That is not `_THEN_ISSUE_`. Terminal #1673 comment #6118356905 has an existing required reviewer #1677 but does not encode a numeric `_ISSUE_1677` token at all.

**Reproduce with exact source function (no GitHub writes):**

```python
from frontier_maintenance_v5 import explicit_successor_issue_numbers as successors
route_1664 = (
    "EXISTING_ISSUE_1673_SCOPED_FACTORY_V5_V7_REGRESSION_REPAIR_READY_"
    "FOR_DISTINCT_MANDATORY_REVIEW_ISSUE_1677_THEN_ONLY_SEPARATELY_OWNER_"
    "AUTHORIZED_SQUASH_SOURCE_PUBLICATION"
)
route_1673 = (
    "NEW_GENUINELY_DISTINCT_MANDATORY_ADVERSARIAL_SECURITY_REVIEW_OF_"
    "FACTORY_1673_PR_1675_EXACT_HEAD_THEN_IF_CLEAN_SEPARATELY_AUTHORIZED_"
    "CURRENT_MAIN_COMPATIBLE_SQUASH_ONLY_NONCANONICAL_SOURCE_PUBLICATION"
)
assert successors(route_1664) == ()
assert successors(route_1673) == ()
```

Independent replay of the precise regular expressions returned `()` for both routes. GitHub already contains open transition wrappers #1681 (from #1664) and #1680 (from #1673), opened after source #1673 and review #1677 were materialized. Their existence is direct observable frontier churn; it is **not** evidence of a missing successor or authorization to invent another. The inherited v5 `--self-test` fixtures only exercise `ISSUE_1547_THEN_ISSUE_1548` and `TWO_INDEPENDENT_COMPONENT_PRODUCERS_...`, not these actual terminal strings.

**Required correction:** Preserve conservative grammar and source-generation exactness, but explicitly recognize an authenticated already-existing successor for these real route forms (through an exact route binding, canonical successor edge, or safe registered route); close/reconcile unclaimed redundant wrapper storage without treating closure as review or source integration. Test the actual two terminal route strings and genuine live/absent/closed/stale successor cases. Never make generic prose issue numbers into authority, and do not bypass ownership or squash gates.

## Other checked boundaries

The proposed base parser rejects unsupported root keys, non-scalar operational lists, duplicate simple keys, nested mappings under inline scalars and malformed indented children. The new `github_verified_head_advance` explicitly requires the current branch tip equal the advanced SHA, an ahead-only ancestor comparison and commit time not later than the GitHub PROGRESS time; v5/v7 show explicit verifier call sites. These are meaningful improvements but cannot cancel B01’s *unverified closure callsite*. No affirmative security approval is issued for YAML equivalence, full GitHub API provenance, or all historical source-review-verifier branches; unresolved blocker and major make further CLEAN disposition prohibited.

## Disposition, impact and next route

**CHANGES_NEEDED: 1 BLOCKER (FSR-1677-B01), 1 MAJOR (FSR-1677-M01), 0 correction-requiring MINOR.** This is a mandatory noncanonical source security review, not an implementation readiness/canon or integration decision. PR #1675 remains DRAFT/UNMERGED and must not be integrated, deployed as a mutating workflow, or labeled clean. Issue #1673 owner REVIEW_READY and its exact-head CI remain provenance only. The earlier superseded #1664/PR #1665 and reviewer-only branches remain frozen.

Materialize **one** narrowly scoped blocking remediation owner route for B01 + M01 from fresh main, with exact changed-path authorization and negative regression fixtures; then exact-final-head read-only hosted CI and a **new genuinely distinct independent required review**. Only after a clean required terminal may a separate owner-authorized expected-head, current-main-compatible **squash-only NONCANONICAL** source integration be considered. The reviewer-only PR containing this report must never be integrated.