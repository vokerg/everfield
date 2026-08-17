# Issue #543 handoff — review of trusted-main Unity license configuration diagnostic

Mission: `W2-ENG-PROVIDER-UNITY-LICENSE-CONFIG-MAIN-REV-01`

## Disposition

`CHANGES_NEEDED`

Severity: 0 BLOCKER / 1 MAJOR / 0 MINOR.

Trust profile: `DEGRADED_SINGLE_AGENT`.

## Ownership / review identity

- winning claim comment: `5313105415`
- reviewer actor: `unity-license-config-main-review-gpt56sol-20260817-01`
- review branch: `planning/issue-543`
- review base: `67134734904dace3384e95efadff0894b5a4d762`
- report path: `docs/planning/wave-2/reviews/w2-eng-provider-unity-license-config-main-diag-review.md`
- report blob before this handoff: `ec168fe32fac3bddb4025033d133eb18d8db0faa`

## Frozen judged producer

- producer Issue #539 terminal: `5313098630`
- producer branch: `planning/issue-539`
- producer draft PR: #541
- judged producer head: `8d4a4d60d6842bca5dab3714100ecc23d205072c`
- workflow blob: `c3941aa7aca6e4ca93d67d95dacdd7d8e11f70ee`
- helper blob: `fd8097ec314826265484c5d0a5b1aa0bf184a791`
- producer handoff blob: `97e82b9282391ed9d6f68f6820bc8d402238ef44`
- exact changed paths: workflow + helper + producer handoff only
- producer branch remained immutable during review.

## Mechanical review evidence

Branch validation run `32005667992`, job `95314516056`, is trusted only for bounded synthetic behavior:
- exact source head `646c994816d8b58b0ecd5ff04ef16a347ab777bd`;
- `py_compile` PASS;
- all seven deterministic self-test cases PASS;
- trusted-main protected job correctly skipped on branch;
- artifact `9279907578`;
- artifact ZIP SHA-256 `7b3f2dbf3c15cba8d5ebb9ba3d49ed1064eb9f4bd462d3636fb245e2c5931ff0` reproduced independently by reviewer;
- contained `selftest.json` SHA-256 `6bb40ee940a66c16816a3e86d0309f0c1da4cfc79086b40b2833d02b61cf6ad2`.

Review passed the candidate's branch/main environment separation, read-only workflow permissions, exact contract binding, boolean-only secret-presence boundary, three-mode classification, false-authority guard, and bounded raw-help handling.

## Blocking finding

`W2-ENG-PROVIDER-UNITY-LICENSE-CONFIG-MAIN-REV-M01` — MAJOR

The workflow retains top-level `workflow_dispatch`. This bypasses the intended one-shot/path-scoped publication trigger: after publication an authorized actor can manually dispatch the workflow on `main` repeatedly, causing repeated protected `engine-eval` presence measurements and multiple valid-looking artifacts. If protected configuration changes between runs, artifacts may disagree, while the candidate defines no attempt-selection rule. This makes the future verification identity non-deterministic.

## Exact remediation required

Route one bounded remediation episode. Do not mutate #539/#541 or this review branch.

Required changes only:
1. remove `workflow_dispatch`;
2. preserve narrow push branch/path triggers and trusted job `refs/heads/main` gate;
3. preserve non-secret branch validation, adapting its planning-branch identity only as needed for the remediation branch;
4. add a deterministic structural check that manual/schedule triggers are absent;
5. preserve contents-read-only permissions, exact input-contract binding, boolean presence-only semantics, raw-help boundary, no repo writes, and all false-authority fields;
6. fresh required review of the corrected exact head.

PR #541 must not integrate.

## Authority boundary

`NOT_CANONICAL`. Review provenance only. No integration-by-review, provider authentication/PASS, Unity license, editor/native execution, engine selection, implementation/readiness, production/commercial/legal/release, verification-PASS, decision, or canonical authority.

Mandatory reopen condition: `MULTI_AGENT_OR_ISOLATED_CONTEXT_AVAILABLE`.
