# Issue #107 handoff — W2-REM-CI-04

**Mission:** `W2-REM-CI-04`  
**Branch:** `planning/issue-107`  
**Owner generation:** claim comment `5276293680` / actor `w2-rem-ci-04-agent-20260813-0717-01`  
**Base:** `main@042d140b5d2e0b951da4528e1867514983418d6f`  
**Pre-handoff parent:** `d3f4d5538749d0ba22417a65237cdce3118f60eb`  
**Intended terminal state:** `REVIEW_READY` after the required draft review-visibility PR is open at the exact commit containing this handoff.

## Completed work

Issue #107 recreated the frozen Issue #102 CI packet on a new branch and repaired only Issue #105 finding `PG-REM-CI3-M01`.

Artifacts:

- `docs/planning/wave-2/evidence/ci-reliability-validator.py`
- `docs/planning/wave-2/evidence/ci-reliability-experiment.md`
- `docs/planning/wave-2/reviews/w2-rem-ci-03-pre-gate-review-dispositions.md`
- `docs/planning/handoffs/issue-107.md`

The v5 validator binds every replacement record to an exact unique replacement evidence ID and exact unique content-addressed source execution envelope. Candidate, requirement/policy, replacement/check identity, result, `ArtifactIdentity`, authoritative hash, source-envelope identity/digest, and structured provenance must agree mechanically between record and frozen envelope bytes.

## Exact executable evidence

Validator Git blob before this handoff: `b951064b701045763f72bcd5247cac45329d1fe5`.

Canonical evidence identities:

- validator source: `sha256:75dc8a78c1489b0afbe39047261f5bfeed77a08d970885cb670d77f3d3d8d8d3`;
- fixture manifest: `sha256:fd16a0496085b923ea87e91f5aa211d58b281f13477a0e1fb62084247f526075`;
- fixture cases: `sha256:c6ed8dca6d4fa7c3b2f49c082070a0b081c6bd8f1f03c3869820b9066adbd069`;
- harness contract: `sha256:a7bd2145b4cc5ffea6472950305bb85f50bd12b891b45497ab7317df3b8fe33a`;
- result object: `sha256:c5c752b9fac136eb9619cabbce1b108627402686864b41738d423da46189e5fa`;
- replacement execution envelope set: `sha256:2ac80d5dd1f8e08de84d9409b37c20d99d2251420dc81c50b9ffbfbd4692b9d5`;
- predecessor evidence artifact/root: `sha256:46f6e1dfd6b56eb2d62c689e0c20de7021ff51123002655550834abd04d8107d`.

Reproducibility checks: Python syntax compile passed; two full executions emitted byte-identical 95,815-byte JSON with SHA-256 `a146b66d1378540157923dee8c67f4b319e9012274a3db004b4401ececcfa70b`; all 34 expected aggregate assertions passed; a non-digest source mutation exited nonzero on the source-identity guard.

## Finding disposition

`PG-REM-CI3-M01`: **RESOLVED**.

New executable attacks S27-S34 all derive `INCONCLUSIVE`: substituted evidence ID, duplicate evidence ID, dangling source envelope, wrong source envelope, substituted provenance, source-envelope result mismatch, source-envelope artifact mismatch, and duplicate source-envelope identity. S1-S26 reproduce the exact v4 truth classes, including positive S6 = `SATISFIED`.

Self-review: **0 unresolved BLOCKER / 0 unresolved MAJOR / 0 correction-requiring MINOR**.

## Frozen inputs / do not mutate

- Issue #102 work/head `f6e8e7ebd120fb5e1b53f0f6e5925dacbc586942` and its cited v4 blobs.
- Issue #105 work `7f91ea0ccb887218d1a428e43d998d5d4a3c24eb`, terminal review/status, and review artifact `0df963ad4eeda55e69c62627c5330185c156faea`.

## Next valid lifecycle step

Before publishing terminal schema-3 `STATUS(REVIEW_READY)`, open a **draft** PR from `planning/issue-107` to `main` and verify its head equals the exact final branch head. The PR is review visibility only and grants no integration authority.

After terminalization, the corrected packet may be consumed only through the repository's declared downstream review path. Formal aggregate `W2-REV-01` remains required. Do not treat this remediation, its draft PR, or its status as authority for CI-provider selection, production implementation, implementation readiness, integration, verification, or canonicalization.
