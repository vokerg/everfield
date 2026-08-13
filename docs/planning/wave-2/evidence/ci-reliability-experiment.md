# W2-REM-CI-04 — Replacement evidence identity and executable provenance remediation

**Mission:** `W2-REM-CI-04` / Issue #107  
**Claim:** comment `5276293680`  
**Base main:** `042d140b5d2e0b951da4528e1867514983418d6f`  
**Frozen remediation input:** Issue #102 work/head `f6e8e7ebd120fb5e1b53f0f6e5925dacbc586942`  
**Frozen v4 validator blob:** `f872f8082592be8e2f067fdf4772034d25483c5e`  
**Frozen review input:** Issue #105 work `7f91ea0ccb887218d1a428e43d998d5d4a3c24eb`, review blob `0df963ad4eeda55e69c62627c5330185c156faea`  
**Finding repaired:** `PG-REM-CI3-M01`  
**Authority:** bounded noncanonical planning evidence only; formal aggregate review remains `W2-REV-01`.

## 1. Scope

Issue #105 demonstrated that the v4 quarantine path mechanically validated replacement membership and `ArtifactIdentity`/hash, but treated `replacement_evidence_id`, `source_envelope_id`, and `provenance` as presence-only fields. Substituted or duplicate replacement evidence identities, dangling/wrong source-envelope identities, and substituted provenance could therefore preserve `SATISFIED`.

This remediation changes only that evidence boundary. It preserves the v4 applicability/retry, S1-S26 aggregate semantics, quarantine expiry/set rules, retained-artifact identity/hash lineage, same-candidate reset rejection, predecessor transition reconstruction, and authority limits.

## 2. Exact v5 executable

Path: `docs/planning/wave-2/evidence/ci-reliability-validator.py`  
Git blob: `b951064b701045763f72bcd5247cac45329d1fe5`  
Validator version: `ci-reliability-reference-v5`  
Dependencies: Python standard library only.

The v4 source self-binding mechanism is retained. Exact uploaded bytes were independently matched to the locally executed bytes by Git blob identity before this report was written.

Declared/recomputed source identity:

- validator source: `sha256:75dc8a78c1489b0afbe39047261f5bfeed77a08d970885cb670d77f3d3d8d8d3`.

Canonical structured-object digests use UTF-8 JSON, sorted keys, compact separators, and SHA-256. Successful execution produced:

- fixture manifest: `sha256:fd16a0496085b923ea87e91f5aa211d58b281f13477a0e1fb62084247f526075`;
- fixture cases: `sha256:c6ed8dca6d4fa7c3b2f49c082070a0b081c6bd8f1f03c3869820b9066adbd069`;
- harness contract: `sha256:a7bd2145b4cc5ffea6472950305bb85f50bd12b891b45497ab7317df3b8fe33a`;
- result object: `sha256:c5c752b9fac136eb9619cabbce1b108627402686864b41738d423da46189e5fa`;
- replacement execution envelope set: `sha256:2ac80d5dd1f8e08de84d9409b37c20d99d2251420dc81c50b9ffbfbd4692b9d5`;
- predecessor evidence artifact: `sha256:46f6e1dfd6b56eb2d62c689e0c20de7021ff51123002655550834abd04d8107d`;
- predecessor evidence root: `sha256:46f6e1dfd6b56eb2d62c689e0c20de7021ff51123002655550834abd04d8107d`.

The exact replacement execution envelopes are embedded in the fixture manifest and retained in the emitted result object. Their individual canonical digests are:

- `repl-env-short-soak-v1`: `sha256:36ea19895b16624e8b821b7463f82879e094e29912d89d1c541523c2f510377c`;
- `repl-env-static-invariant-v1`: `sha256:1520beba77c89b44dbe01ecd20c4a2ddb1a046ce22df2e47f2495b197483fa0a`.

## 3. Replacement evidence contract

For each required replacement, v5 now binds an exact record to one exact immutable source envelope. A record is accepted only when all of the following hold mechanically:

1. the replacement-set key and `replacement_id`/`check_id` are the declared required replacement;
2. `replacement_evidence_id` equals the frozen ID for that replacement and all replacement evidence IDs are unique;
3. `source_envelope_id` equals the frozen source-envelope ID for that replacement and all accepted source-envelope IDs are unique;
4. the referenced source envelope exists in the exact frozen envelope set;
5. the canonical envelope digest equals the frozen per-envelope digest and the record's `source_envelope_digest`;
6. the envelope bytes equal the exact frozen envelope bytes;
7. candidate, requirement, policy version, replacement/check identity, result, artifact key, `ArtifactIdentity`, authoritative hash, replacement-evidence identity, and provenance match between record and envelope;
8. record/result remains `PASS` and the artifact identity/hash agrees with the frozen catalog.

The retained provenance is structured data with an exact `provenance_id` and value rather than an unchecked producer string. The emitted result retains both the positive replacement records and exact source-envelope bytes/digests, so later review can reconstruct the chain without following a dangling identifier or trusting producer prose.

## 4. Executable regression corpus

The v5 corpus contains 34 cases. S1-S26 preserve the frozen v4 truth classes exactly. In particular, the valid active quarantine remains `SATISFIED`; expiry/set-membership, replacement artifact substitution, predecessor transition/root/artifact substitution, same-candidate reset, retention loss, PRODUCT laundering, FLAKY laundering, and required `NOT_RUN` remain fail-closed or gating exactly as before.

Eight new cases target `PG-REM-CI3-M01`:

| ID | Attack | Derived aggregate |
|---|---|---|
| S27 | substitute `replacement_evidence_id` | `INCONCLUSIVE` |
| S28 | duplicate a replacement evidence ID across records | `INCONCLUSIVE` |
| S29 | point at a dangling source envelope | `INCONCLUSIVE` |
| S30 | point one replacement at the other replacement's valid envelope/digest | `INCONCLUSIVE` |
| S31 | substitute retained provenance | `INCONCLUSIVE` |
| S32 | mutate the exact source envelope result to `FAIL` | `INCONCLUSIVE` |
| S33 | mutate the exact source envelope `ArtifactIdentity` | `INCONCLUSIVE` |
| S34 | duplicate a source-envelope identity across replacement records | `INCONCLUSIVE` |

These are evaluated by the generic validator path; scenario IDs do not directly select outcomes.

## 5. Reproducibility checks

The exact local bytes whose Git blob is `b951064b701045763f72bcd5247cac45329d1fe5` were checked as follows:

- `python -m py_compile` succeeded;
- two complete executions succeeded and emitted byte-identical 95,815-byte JSON outputs;
- both outputs had SHA-256 `a146b66d1378540157923dee8c67f4b319e9012274a3db004b4401ececcfa70b`;
- all 34 derived aggregates matched the frozen `EXPECTED` map;
- a non-digest source-byte mutation exited nonzero before fixture evaluation with source identity mismatch: declared `sha256:75dc8a78c1489b0afbe39047261f5bfeed77a08d970885cb670d77f3d3d8d8d3`, observed tampered identity `sha256:bdc79c2c83600b7398ec621eb6dd8af8a692970dea85102c1b501f6cab3f83d1`.

The predecessor evidence digest/root remained byte-for-byte identical to v4, demonstrating that the remediation did not rewrite that frozen lineage anchor.

## 6. Finding disposition

`PG-REM-CI3-M01` — **RESOLVED**.

The formerly decorative identity/provenance fields now participate in exact acceptance logic and are reconstructably tied to immutable source evidence. Arbitrary identity/provenance edits, duplicate evidence identity, dangling/wrong source-envelope selection, and source-envelope result/artifact mutation all fail closed in the executable corpus. No waiver-by-prose is used.

## 7. Self-review

Self-review result: **0 unresolved BLOCKER / 0 unresolved MAJOR / 0 correction-requiring MINOR**.

Checks performed against the Issue #107 contract:

- exact `replacement_evidence_id` value and uniqueness: PASS;
- exact source-envelope ID, bytes, digest, and uniqueness: PASS;
- candidate/requirement/policy/replacement/check/result/ArtifactIdentity/hash equivalence between record and envelope: PASS;
- exact structured provenance equality: PASS;
- exact record + source evidence retained in result: PASS;
- required new laundering negatives executable and fail closed: PASS;
- S1-S26 prior truth classes preserved: PASS;
- v4 source self-binding and predecessor reconstruction preserved: PASS;
- authority boundaries unchanged: PASS.

## 8. Authority boundaries and reopen conditions

This packet does not select a CI provider, define a universal INFRA classifier, prove production storage durability, authorize implementation/gameplay work, establish implementation readiness, authorize integration, perform formal verification, or canonicalize anything. Formal aggregate independent review remains `W2-REV-01`.

Reopen if a descendant can preserve quarantine `SATISFIED` while substituting/duplicating replacement evidence identity; using a dangling, wrong, duplicated, or mutated source envelope; changing retained provenance; creating record↔envelope disagreement in candidate/policy/check/result/artifact identity/hash; changing executable semantics without changing the bound source identity; or regressing any S1-S26 truth class.
