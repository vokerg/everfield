# Issue #134 handoff — W2-PG-REM-ACC-01

**Mission:** `W2-PG-REM-ACC-01`  
**Issue:** #134  
**Branch:** `planning/issue-134`  
**Ownership generation:** Issue #134 comment `5277143488`  
**Actor session:** `w2-pg-rem-acc-01-agent-20260813-0904-sol02`  
**Base main:** `042d140b5d2e0b951da4528e1867514983418d6f`  
**Reviewed Issue #96 work/head:** `3937f65ae4eb495420d1240c2b739841aa14a037`  
**Reviewed Issue #96 terminal status:** comment `5271849637`  
**Required formal review:** `W2-REV-01`  
**Review disposition:** `CHANGES_NEEDED`  
**Bounded successor:** Issue #135 / `W2-REM-ACC-02`

## Immutable input reproduction

The exact four published Issue #96 artifact identities were re-fetched at the reviewed terminal head and reproduced:

- remediation report: `b5f0669a5c9e8fc242b96eabf1a32bc21c0248ee`;
- machine-readable policy: `78690cf658967b2ded35e738df125959a56f0d86`;
- finding dispositions: `78576cac9f7cdeaf2552235d19cac01cba7b099b`;
- Issue #96 handoff: `261cb3a15511a2dc2be4ec810b43283edfc341ee`.

Issue #96 remained immutable throughout this review.

## Review result

Disposition is **CHANGES_NEEDED: 0 BLOCKER / 2 MAJOR / 0 correction-requiring MINOR**.

### `PG-REM-ACC-M01` — MAJOR

The policy's `ATOMICALLY_EXPANDED` source-page state is trusted rather than mechanically derived from an explicit expected source-clause inventory. A concrete failure exists in XAG 101: `XAG101-TEXT-BLOCK-SPACING` preserves the 80/40 line-width thresholds but drops the current source's required measurement conditions that the count is taken at 100% text size and excludes spaces. The packet therefore claims exact semantic preservation and atomic page coverage while required source semantics are absent.

Required repair is routed to Issue #135: define a mechanically auditable expected source-clause inventory/schema, derive expansion/completeness from it, restore the missing XAG 101 line-width measurement semantics, and add adversarial checks that fail when either condition disappears.

### `PG-REM-ACC-M02` — MAJOR

The direct Valve compatibility mapping omits the current requirement that players must not need to change an in-game setting to enable controller support/default configuration. `ACC-DECK-01` only records access to all content through the default controller configuration. This permits mapped evidence to pass after manual enablement even though Valve's direct checklist would fail.

Required repair is routed to Issue #135: bind the no-settings-enable requirement to direct Valve authority and exact evidence while preserving the separate project-selected Proton authority class.

## Confirmed controls

- `mapping_complete` remains `false`.
- `IR-BLOCKER-ACCESSIBILITY-CURRENT` remains OPEN.
- XAG 102–106 and 108–123 remain summary-only/fail-closed.
- empirical evidence remains `NOT_RUN`.
- XAG authority remains best-practice/non-legal.
- Valve direct compatibility and project-selected Proton evidence remain separately typed.
- current Microsoft XAG v3.2 / XAG 101 / XAG 107 and Valve compatibility source facts were re-observed on 2026-08-13; no material drift was found outside the omissions recorded above.
- no legal compliance, Valve `Verified` result, empirical accessibility PASS, engine selection, production/readiness, implementation, integration, verification, release, or canonicalization authority is claimed.

## Exact review artifact

- `docs/planning/wave-2/reviews/w2-rem-acc-01-pre-gate-review.md`
- this handoff: `docs/planning/handoffs/issue-134.md`

After this handoff commit, re-fetch both artifacts for exact blob identities, perform cold diff/ownership fencing, open the mandatory draft PR from `planning/issue-134` to `main` at exact branch head, verify the PR remains open + draft and its head equals the terminal `head_sha`, then publish schema-3 owner `STATUS(REVIEW_READY)` and freeze this review branch.

Formal `W2-REV-01` remains required. This pre-gate review and its draft PR are review/provenance visibility only. Any eventual `main` integration is separately authorized and squash-only.
