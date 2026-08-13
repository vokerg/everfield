# Issue #122 handoff — W2-PG-REM-ENG-04

## Status

Independent bounded pre-gate review of Issue #112 is complete substantively. Disposition: `CHANGES_NEEDED` with **0 BLOCKER / 2 MAJOR / 1 correction-requiring MINOR**.

## Exact reviewed input

- Issue #112 work/head: `6c5777ca56d43e22cba9b5e776e436d11b846325`
- harness blob: `58e6e0832e36fdc4dd2bee7d1984e12e3fa4fc9f`
- validator blob: `7837695c91365273b2c89f3852b401c2f127af54`
- disposition blob: `fbae989e6d806788bcd22827b98e87624662e07b`
- handoff blob: `d572aeafb733b4ffbd623ca727a305abd2a15092`
- Issue #112 terminal status: comment `5276691786`
- Issue #112 draft review surface: PR #121, exact reviewed head `6c5777ca56d43e22cba9b5e776e436d11b846325`

## Independent execution evidence

The exact validator was reconstructed as 35,451 bytes and independently matched Git blob `7837695c91365273b2c89f3852b401c2f127af54`. Python syntax compilation passed. Two exact executions were byte-identical.

Reproduced identities:

- validator source SHA-256: `915d84b10fc1744af6d077bcec5025fd95f02877af341082a45e5cfaa90bc8fa`
- validator contract: `5f37d97fa2bb263d87a10bc5cfd9311c744e1b80e83d42c8d6a9b202ccfef269`
- feature slice: `9a2523c4870146b09233397f3773f7a27b1e0135c24a6767d16e34a791aab104`
- scenario manifest: `be4d7473b01da6b428cd5f3be48de083abd161a4899471303f3ccfeef45c725f`
- fixture inputs: `15fd95e053acc634a7df2953ab411895fd47b8ee6145465a7faf6623579d3a6b`
- result object: `f76a166ec79ea08ceb2dc60ad5988f33a108a59cd153fb1157ebf0817fe850ac`
- deterministic stdout: `6f194aa5426c42e545130160da3eeb2d5e36d05ea3296d2b54c4cb9add177baa`

The independent attack packet contained 64 cases and had review-local canonical JSON SHA-256 `401d656117ea287c97696f70bd63251ee4be33f23d59333661c4fb9270fd0194`.

## Findings

- `PG-REM4-M01` — **MAJOR**: unhashable/container `result` or `failure_class` values raise `TypeError` rather than producing typed invalid evidence, so the preserved closed result/failure-class contract is not total over malformed inputs.
- `PG-REM4-M02` — **MAJOR**: `run_registry_refs` and `all_attempt_refs` use set equality, allowing duplicate retained refs to preserve `PASS_FOR_COMPARISON`; exact one-to-one registry identity is not enforced.
- `PG-REM4-m01` — **MINOR**: malformed nested adaptation/registry container shapes can raise rather than reject deterministically.

## Confirmed valid corrections

Issue #112 correctly closes the targeted null/empty reset/workspace, non-boolean reset flag, malformed/duplicate normal-index, cross-candidate adaptation, adaptation-binding substitution, and linked-invalid-generation history cases. Duplicate required-injection identity, cross-candidate attempts, S3/S9/S10 weakening, reset/workspace reuse, resource mismatch, and retained-failure/flake controls also remain effective for the exercised well-shaped inputs.

## Successor route

Exactly one bounded successor was created: Issue #126 / `W2-REM-ENG-05`. It is blocked until Issue #122 publishes its valid terminal `STATUS(REVIEW_READY)` with `CHANGES_NEEDED` and these exact finding IDs. Frozen Issue #112 must not be edited.

## Remaining lifecycle step

Before terminal Issue #122 `STATUS(REVIEW_READY)`, open an **open draft PR** from `planning/issue-122` to `main`, verify its head equals the exact final branch head, then publish the terminal schema-3 status bound to ownership generation comment `5276887608`.

Formal `W2-REV-01` remains required. This review authorizes no engine selection, production/readiness, implementation, integration, verification, release, merge, or canonicalization.
