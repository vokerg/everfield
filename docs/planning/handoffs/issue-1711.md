# Issue #1711 — terminal result SHA branch-provenance remediation

**Mission:** `FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-19`. **Single owner CLAIM:** #6131528483, `frontier-terminal-head-provenance-1711-gpt6-20261012-2154-cph-01`. Current-main base: `a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`. Canonical planning program: Issue #1147 terminal #5675066392, Git blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.

## Immutable causality and limited envelope

Required genuinely independent security review #1703 `REVIEW_STATUS(CHANGES_NEEDED)` #6131487384 found **1 MAJOR FSR-1703-M01** against source Issue #1698 `STATUS(REVIEW_READY)` #6131140141; frozen source OPEN/DRAFT PR #1702 HEAD `7a3a67cfafb5f8f9d28ce40c6e5b10eb1f78eb9a`, review-only draft #1706 HEAD `822879d3801d26059035a425a2981c5da7fe319a`. All predecessor branches and PRs are unchanged. Exactly the 23 changed-file blobs in frozen #1702 are inherited, except **only** `tools/planning/frontier_maintenance.py` and `tools/planning/frontier_maintenance_v5.py` are corrected. This issue-specific handoff is the 24th path. No main mutation, live `--apply`, or Github PATCH.

## Correction and conservative limitations

The base storage closure consumer now requires an additional read-only `github_verified_terminal_result_heads` check for **both** owner terminal `head_sha` and `work_sha`: SHA40 syntax, one fresh live `planning/issue-N` task ref, and either exact tip equality or individually verified behind-free GitHub commit ancestry to that same tip. Missing/moved/deleted/refused refs, unrelated commits, ambiguous compare results, and malformed SHAs fail closed. The same proof is enforced for applicable v5 closed-wrapper transition-resolution checks. Existing first-winning owner, six-hour lease, HEAD_ADVANCE/PROGRESS, HANDOFF/STALE/ORPHAN, source-head proof and source compatibility logic remain unchanged.

The real base closure self-test includes mocked read-only branch/compare positives (genuine owner CLAIM→DONE, no-work same-base, valid ancestor), forged terminal head, forged work, diverged/moved and deleted ref negatives, plus inherited malformed/edited, losing-owner and lease tests. v5's synthetic old work SHA fixture now models a real terminal result on the source HEAD. Inherited v1–v7 suites are not discarded.

**Evidence boundaries:** live branch ancestry is not historical GitHub reflog authentication or a storage PATCH compare-and-swap. An exact-final-head read-only GitHub Actions PR workflow PASS, skipped mutating job, and genuinely distinct adversarial review remain mandatory before any terminal REVIEW_READY/integration. The source is **NOT automatically security accepted** and **NOT integrable** without separately owned/authorized expected-head current-main compatible SQUASH-only NONCANONICAL publication. Reviewer-only drafts never merge. No canon, gameplay/engine/readiness, production or release authority.

## Resumption / required next route

Fetch the branch and draft PR exact HEAD; check CI run and affected-file blobs. If hosted full `python3 -m py_compile tools/planning/frontier_maintenance*.py` and `python3 tools/planning/frontier_maintenance_v7.py --self-test` fail, continue fixing **only** the two permitted scripts and this handoff, then re-run exact-final-head CI. With true PASS and mutating job SKIPPED, the owning generation may publish `STATUS(REVIEW_READY)` only after open exact-head draft PR. Then materialize exactly one **new genuinely independent mandatory adversarial security review** of the frozen corrected source. No source self-review or integration.
