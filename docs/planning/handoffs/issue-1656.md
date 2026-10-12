# Issue #1656 — root operational list cardinality remediation

**Owner work staged on planning/issue-1656. This handoff is initially PRE-CI; later exact-head GitHub operational terminal and PR metadata, not this historical file, govern final verification state.**

## Authority / strict scope

Canonical Issue #1147 binding #5675066392; immutable program blob fd4cf1119c3f86acc3af620024eea72235e81ce4. Base main 3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d. First winning owner CLAIM #6109670908, actor frontier-remediate-root-list-1656-gpt6-20261011-1544-cph-01, six-hour GitHub-server lease.

Required independent negative review Issue #1650 terminal #6108889365, FSR-1650-B01 1 BLOCKER, 0 MAJOR, 0 correction-requiring MINOR; frozen review-only draft PR #1652 HEAD 021fafc34c3fe632bd05072a9dccd4a4f4281fc0 and report blob bda4fde232998cdccdcb506278f8bf0de79bde0b. Frozen prior producer Issue #1647 terminal #6107749574 / source draft PR #1648 exact HEAD 4059ee74e96e064f8a99bd011ef9f33f9867a6ad, base parser blob b4cd006d0dcb0175556e9bdfeb3f058045a5a113. Preserve all predecessor PR heads, reviewer/verifier branches, main and canonical code unchanged.

## Surgical source correction

Only `tools/planning/frontier_maintenance.py` differs from frozen #1648 inherited source: `list_scalar` now denies nonempty root YAML scalar authority (plain or quoted) rather than wrapping it into a singleton list. The legitimate direct-root indented `- item` list and bracket flow list continue to parse. Direct-root mapping identity, quoted/complex/escaped/duplicate keys, nested extensions fields, tagged/aliased/block scalar shadows and YAML prose/fence restrictions remain fail-closed. No v5/v6/v7 or shared workflow rewrite.

Added base self-tests for raw/quoted/tagged/aliased scalar evidence_refs and artifact_paths; real root flow and indented list positives; each of v7 source/reviewer/verifier's single-file PR set predicate now rejects scalar paths and accepts real lists. Added full `schema3_ownership_lease_state` and `schema3_owner_unexpired_at` invalid scalar EVIDENCE at 17:59 vs real list renewal and 18:01 expiration on 12:00 claim; unchanged/real HEAD_ADVANCE, expiry, original E1/E2/E3 cap with invalid fourth and exact ORPHAN 600-second tests remain. These tests exercise the actual base API shared by v7 and do not invent an independent reviewer verdict.

## Immutable inherited packet

All **19 other PR #1648 changed paths** are exact Git blob references in the produced tree; original workflow and v5/v6/v7 code unchanged. Source PR contains 20 inherited paths plus new own `docs/planning/handoffs/issue-1656.md`, expected 21 changed paths. No unrelated, sibling gameplay or canonical files.

## Validation and continuation

The official PR workflow `.github/workflows/planning-frontier-maintenance.yml` runs on PR changes to base parser: `validate-pr` checks Python compile of composed tools and runs v7 selftests (which run v1-v7 regression suites). The state-mutating `maintain` job must be **SKIPPED** for pull_request. Final GitHub Actions run/job/head evidence must be inspected and recorded by a subsequent in-lease owner schema-3 STATUS comment before declaring REVIEW_READY; failures warrant HANDOFF_READY with honest defects. The frozen source/old reviewer drafts must remain DRAFT/UNMERGED. A separate genuinely independent required adversarial review of the final corrected source is mandatory before any separately authorized squash-only NONCANONICAL integration. No canon, gameplay truth, consent, accessibility certification, engine selection, implementation readiness, production or release authority.
