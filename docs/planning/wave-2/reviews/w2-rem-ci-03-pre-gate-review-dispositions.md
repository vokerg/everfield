# W2-REM-CI-04 — Disposition of W2-PG-REM-CI-03 finding

**Remediation mission:** `W2-REM-CI-04` / Issue #107  
**Source review:** `W2-PG-REM-CI-03` / Issue #105  
**Source review work:** `7f91ea0ccb887218d1a428e43d998d5d4a3c24eb`  
**Source review artifact:** `0df963ad4eeda55e69c62627c5330185c156faea`  
**Frozen reviewed remediation:** Issue #102 @ `f6e8e7ebd120fb5e1b53f0f6e5925dacbc586942`  
**Authority:** remediation finding disposition only; formal aggregate review remains `W2-REV-01`.

## `PG-REM-CI3-M01` — RESOLVED

Issue #105 showed that v4 accepted replacement records after validating field presence, candidate/policy/result, and `ArtifactIdentity`/hash without mechanically validating the values of `replacement_evidence_id`, `source_envelope_id`, or retained provenance.

Issue #107 resolves that gap in exact validator blob `b951064b701045763f72bcd5247cac45329d1fe5`:

- every replacement has one frozen `replacement_evidence_id` and duplicate evidence IDs fail closed;
- every replacement has one frozen `source_envelope_id` plus canonical `source_envelope_digest`;
- every accepted source envelope must exist in the exact embedded envelope set and match its frozen bytes/digest;
- source-envelope IDs are unique across accepted replacement records;
- record and envelope must agree on replacement-evidence identity, candidate, requirement, policy version, replacement/check identity, result, artifact key, `ArtifactIdentity`, authoritative hash, and structured provenance;
- exact positive replacement records, source envelopes, and envelope digests are retained in the emitted result object.

Executable negative evidence is S27-S34:

- S27 substituted replacement evidence ID → `INCONCLUSIVE`;
- S28 duplicate replacement evidence ID → `INCONCLUSIVE`;
- S29 dangling source envelope → `INCONCLUSIVE`;
- S30 wrong but otherwise valid source envelope → `INCONCLUSIVE`;
- S31 substituted provenance → `INCONCLUSIVE`;
- S32 source-envelope result disagreement → `INCONCLUSIVE`;
- S33 source-envelope artifact-identity disagreement → `INCONCLUSIVE`;
- S34 duplicate source-envelope identity → `INCONCLUSIVE`.

The valid positive quarantine S6 remains `SATISFIED`; all prior S1-S26 truth classes reproduce unchanged.

Exact evidence identities:

- validator source: `sha256:75dc8a78c1489b0afbe39047261f5bfeed77a08d970885cb670d77f3d3d8d8d3`;
- fixture manifest: `sha256:fd16a0496085b923ea87e91f5aa211d58b281f13477a0e1fb62084247f526075`;
- fixture cases: `sha256:c6ed8dca6d4fa7c3b2f49c082070a0b081c6bd8f1f03c3869820b9066adbd069`;
- harness contract: `sha256:a7bd2145b4cc5ffea6472950305bb85f50bd12b891b45497ab7317df3b8fe33a`;
- result object: `sha256:c5c752b9fac136eb9619cabbce1b108627402686864b41738d423da46189e5fa`;
- replacement execution envelope set: `sha256:2ac80d5dd1f8e08de84d9409b37c20d99d2251420dc81c50b9ffbfbd4692b9d5`.

Reproducibility is recorded in `docs/planning/wave-2/evidence/ci-reliability-experiment.md`: syntax compilation succeeds, two complete runs are byte-identical, all 34 assertions pass, and a source-byte mutation is rejected by the retained v4-style source self-binding.

**Disposition rationale:** the finding required executable exact identity/provenance validation and reconstructable source evidence, not a prose waiver. The v5 validator now makes those values part of acceptance and freezes the source envelope bytes/digests in the emitted packet. The laundering attacks that were `SATISFIED` in Issue #105 now fail closed.

No CI-provider, universal INFRA-classifier, production, readiness, integration, verification, implementation, or canonicalization authority is granted by this disposition.
