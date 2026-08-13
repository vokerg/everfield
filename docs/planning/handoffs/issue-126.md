# Handoff — Issue #126 / W2-REM-ENG-05

## Mission

Close only the engine-validator gaps found by independent pre-gate review Issue #122: malformed result/failure value types, duplicate/malformed retained-attempt registries, and malformed adaptation/container shapes.

## Immutable inputs

- canonical Planning Program v1 active binding: Issue #6 activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- Issue #112 exact work/head: `6c5777ca56d43e22cba9b5e776e436d11b846325`;
- Issue #112 validator blob: `7837695c91365273b2c89f3852b401c2f127af54`;
- Issue #122 exact review work/head: `c535bb9e94cb0da3aeb0d66dcc2606c034d7412f`;
- Issue #122 terminal status comment: `5276962394`;
- findings: `PG-REM4-M01`, `PG-REM4-M02`, `PG-REM4-m01`.

## Produced surfaces

- `docs/planning/wave-2/evidence/engine-spike-harness.md`;
- `docs/planning/wave-2/evidence/engine-spike-protocol-fixtures.py`;
- `docs/planning/wave-2/reviews/w2-rem-eng-04-pre-gate-review-dispositions.md`;
- `docs/planning/handoffs/issue-126.md`.

## Result

All three Issue #122 findings are mechanically resolved in the bounded v5 packet.

The corrected validator:

- validates result/failure scalar shape before matrix membership;
- validates both retained-attempt registries as unique exact one-to-one ID lists;
- validates adaptation and registry container/key shapes before set/dict/hash/numeric operations;
- preserves the complete 51-case Issue #112 declared corpus;
- adds 20 fresh remediation regressions, all typed fail-closed;
- preserves candidate/adaptation binding, common S1–S10 bounds, attempt identity, no-laundering, reset/workspace/resource, required-injection, repair-history, S3/S9/S10, and authority semantics.

## Reproduction

Run:

`python -m py_compile docs/planning/wave-2/evidence/engine-spike-protocol-fixtures.py`

then execute twice:

`python docs/planning/wave-2/evidence/engine-spike-protocol-fixtures.py`

Expected evidence identities:

- validator source SHA-256 `9a50e3e21279a7a94836d6162fee218a0e187bafe292847fd5f0b108df45deea`;
- validator Git blob `2c646988dc16e212f43df6a4ee5ce646622ac2a6`;
- validator contract `ed1de63a02872c18981259a15eb8393b3d94d5f7af774b4b1f771c1c4e2e77ef`;
- feature slice `9a2523c4870146b09233397f3773f7a27b1e0135c24a6767d16e34a791aab104`;
- scenario manifest `be4d7473b01da6b428cd5f3be48de083abd161a4899471303f3ccfeef45c725f`;
- fixture inputs `45555e8370f821d66fa8febdd58d475b88c15b0505ab996a4a8954ef8ef11613`;
- result object `8612a359c029e4d921356d214177a3478a0ee45011f8d26a629850180748a071`;
- deterministic stdout `e4a5279f4abb0a5b7eb4cfc2b4e64615be966c9e656dc4d6a610741b66a82ff0`;
- remediation attack evidence `58294d195025f32235bac3b6a7d4ea0eb20aebe0a79fb760fe80750eb069b9ef`.

## Review and authority

Self-review: 0 unresolved BLOCKER / 0 unresolved MAJOR / 0 correction-requiring MINOR in Issue #126 scope.

Before terminal `STATUS(REVIEW_READY)`, the owner must open and re-fetch an open draft PR from `planning/issue-126` to `main` and verify the PR head equals the terminal branch head. That PR is review visibility only.

Formal aggregate review `W2-REV-01` remains required. No engine execution/scoring/selection, production/readiness, implementation, integration, verification, release, merge, or canonicalization authority is claimed. Any future main integration is separately authorized and squash-only.
