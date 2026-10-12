# Issue #1698 — bounded factory HANDOFF/STALE source-head remediation

**Mission:** `FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-18`
**Owner:** sole first immutable schema-3 CLAIM #6131001591, GitHub server `created_at=2026-10-12T19:18:59Z`, session `frontier-factory-handoff-head-remediate-1698-gpt6-20261012-2120-cph-01`.
**Claim base:** `main@a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`.
**Canonical:** Issue #1147 terminal binding #5675066392, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation `87c85cecfa9a2ffa464c4b36816a138bf41441af`.

## Frozen source and independent review

Mandatory corrective route from truly independent #1691, unedited in-lease `REVIEW_STATUS(CHANGES_NEEDED)` #6130964726 (1 BLOCKER FSR-1691-B01 / 0 MAJOR / 0 correction-requiring MINOR), reviewer-only OPEN/DRAFT PR #1699 exact `5208af50226b531e8c5f4287e15c7aa9bb4fb1bd`, report `docs/planning/wave-2/reviews/factory-seeding-1683-review.md`. Rejected source #1683 `STATUS(REVIEW_READY)` #6130231359 and OPEN/DRAFT PR #1690 head `3d849fb1b3b7bd1d2601f152c30cb367183decfa` stay untouched.

New branch `planning/issue-1698` created from fresh main and inherits the **exact 22 source files and original blob SHA identities** from frozen #1690 by Git object tree commit `80d454a6b834fdb966dbb87229314baa6f627cf8`. The workflow, v6/v7, old handoffs and other inherited files are byte-identical. Only `tools/planning/frontier_maintenance_v5.py` and `tools/planning/frontier_maintenance.py` have corrective modifications. The 23rd changed path is this handoff; no predecessor/reviewer source, gameplay, canon, or main mutation.

## Correction

- `terminal_owner_generation_is_current` now authenticates each handoff head against `STATUS(HANDOFF_READY).head_sha == .work_sha ==` the *prior owner generation* canonical lease-observed head at that handoff. HANDOFF intent and RESUME must match that exact source head, and all participating owner/source/intent/grant records must retain the exact task branch. A self-consistent but unrelated 40-hex SHA can no longer manufacture a new owner.
- STALE intent/recovery now must agree with the prior generation's **reconstructed authentic lease head** (including authenticated HEAD_ADVANCE); the precise stale source anchor comment must also match its own `observed_head_sha`. The six-hour boundary, valid E1-E3/invalid E4, earlier valid handoff/terminal veto and first-winner intent semantics are preserved.
- ORPHAN intent/grant source SHA now matches the source probe; its ten-minute 600s maturity and no-later-claim semantics remain intact.
- Before terminal issue storage closure, the base `closure_authorized_terminal_from_comments` passes a fresh **read-only live GitHub task branch/head ancestry verifier** for HANDOFF and STALE recovery. It verifies the transition source SHA is the current branch tip or its provable behind-free ancestor; unknown, missing, moved/diverged or unreadable GitHub refs fail closed rather than blessing a PATCH. GitHub has no historical branch reflog, so current ancestry is strong storage reconciliation evidence, **not** a historical timestamp attestation or an atomic compare-and-swap. The existing last GET-to-PATCH race remains.
- Embedded v5 regression fixtures exercise real v5 and base closure consumers: legitimate in-lease HANDOFF→RESUME→SUPERSEDED and mature STALE→RECOVER→SUPERSEDED; both forged SHA transitions reject; live-branch proof positive, diverged branch negative, unavailable branch negative; original v1–v7 suites remain required. All tests are read-only mocked, no live GitHub mutation.

## Remaining mandatory gates

A fresh **DRAFT source PR** to main and exact changed-path envelope, hosted exact-final-head **read-only** compile/complete v1–v7 regression CI success with maintenance mutation job SKIPPED, plus owner terminal status are prerequisites to new genuinely distinct mandatory code/security reviewer route. The authored regression tests do **not** constitute independent acceptance. A new security reviewer must not be this source execution, #1691 negative reviewer, or #1683 producer. Only later separate owner-authorized current-main compatible **SQUASH-only NONCANONICAL** publication could integrate corrected source. No `--apply` deployment, closure authority, canonicality, gameplay, release, engine/readiness, production, or accessibility decision is created by this handoff.

**Continuation:** recheck current main, canonical binding, first owner lease, exact PR/head/blobs and hosted CI from GitHub; independently challenge malformed ownership capsules, stale/handed-off source/intent head, branch ancestry and preservation of authorized positives. If hosted CI fails, correct only owned files before owner `STATUS(REVIEW_READY)`; if branch cannot safely advance, publish a reconstructable handoff rather than asserting PASS.
