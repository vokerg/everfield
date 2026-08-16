# Issue #402 handoff — provider remediation required review

## State

`REVIEW_READY / CHANGES_NEEDED`

This handoff records the fresh required review of exact remediation Issue #400. It grants no integration, provider credential, engine-selection, commercial/production/legal/release, readiness, verification-PASS, decision, or canonical authority.

## Ownership and trust

- issue: #402
- mission: `W2-ENG-PROVIDER-EFFECTIVE-REM-REV-01`
- branch: `planning/issue-402`
- winning claim: `5306312793`
- reviewer actor/session: `w2-eng-provider-effective-rem-rev-01-gpt56sol-20260816-02`
- trust mode: `DEGRADED_SINGLE_AGENT`
- review base: `08a89092a9e9b2bae6f8bd34dd29dd85a8d97bcf`
- review work SHA: `c40ab61712db4615705a92d316834253697b049b`
- draft review PR: #403, opened at exact review work SHA `c40ab61712db4615705a92d316834253697b049b`; the final handoff/status commit head is bound by terminal schema-3 status.
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical binding comment: `5245368879`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`

The reviewer ownership episode is distinct from remediation #400, but stronger agent isolation was unavailable. No full-independence claim is made.

## Frozen judged identities

- producer Issue #373 terminal `5306084733`, head `75728cade4c1646f9a1006e89ccc026234958a2b`, PR #397;
- first review Issue #398 terminal `5306215159`, disposition `CHANGES_NEEDED`, head `8e001aa76d68e0bf04ac44e04d694e27215d8b58`, PR #399;
- first-review findings: `W2-ENG-PROVIDER-EFFECTIVE-REV-M01`, `W2-ENG-PROVIDER-EFFECTIVE-REV-M02`;
- remediation Issue #400 claim `5306254156`, terminal `5306282246`;
- remediation implementation work `d504aa4aa86a27e56329865b7e9af74b87dd0919`;
- remediation terminal head `2f6202747bc517202b406dc2f97e138d21294780`;
- draft remediation PR #401, base `main@08a89092a9e9b2bae6f8bd34dd29dd85a8d97bcf`, same exact head;
- remediation changed-file set: six files exactly.

All predecessor branches/PRs remained immutable during review.

## Disposition

`CHANGES_NEEDED`

Finding count: **0 BLOCKER / 1 MAJOR / 0 correction-requiring MINOR**.

The two original #398 MAJOR findings are closed in the modified code:

- original M01: direct recorder publication to `main` is removed and replaced by a bounded evidence branch plus draft PR with separate squash-only integration authority;
- original M02: evaluator, upstream Actions run/workflow, source head, and projection code are mechanically bound to exact identities and fail closed on mismatch.

A new integration-blocking reconstruction defect prevents `PASS_BOUNDED_PROVIDER_EFFECTIVE_ACCESS`.

## New finding

`W2-ENG-PROVIDER-EFFECTIVE-REM-REV-M01` — MAJOR — the exact #400 successor drops unchanged producer runtime/support/provenance surfaces while retaining references to them.

Frozen #373 supplied nine files. Exact #400/#401 carries only six. The exact remediation head lacks:

- `tools/planning/engine_provider_effective_validator.py`, even though the credentialed evaluator compiles/self-tests/executes it;
- `.github/workflows/engine-eval-health.yml`, even though the contract names it;
- `docs/planning/wave-2/evidence/provider-effective-access-local-unity.json`, even though the prose says the durable local Unity S3 result remains preserved local evidence.

Therefore PR #401 cannot be integrated as a complete provider-access successor. Rejected producer PR #397 is not a valid implicit dependency because it contains the exact old M01/M02 defects.

Full reasoning and all required attack results are in `docs/planning/wave-2/reviews/w2-eng-provider-effective-remediation-review.md`.

## Review publication check

- PR #403 targets `main` from `planning/issue-402` and is intentionally draft.
- PR #403 contains only the review report and this handoff.
- The terminal schema-3 status binds the final exact review head, PR head/base/draft state, changed-file count, and reported status-check state.

## Required next route

After the exact review head/PR and terminal schema-3 status are frozen, route exactly one bounded blocking-remediation successor for `W2-ENG-PROVIDER-EFFECTIVE-REM-REV-M01`.

That successor must reconstruct the complete provider packet from current `main`, carry forward the unchanged review-clean runtime/support/provenance surfaces needed by the retained contract, preserve #400's M01/M02 corrections, avoid integrating rejected PR #397 as a prerequisite, and require one fresh review of the resulting exact packet.

## Authority boundary

`NOT_CANONICAL`. No integration authority. No provider credential or engine selection. No commercial, production, legal, or release authority. No readiness or verification-PASS. No decision authority. PR #401 remains blocked from integration by this review disposition.
