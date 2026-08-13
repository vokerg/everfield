# W2-RIGHTS-01 pre-gate review dispositions

**Remediation mission:** `W2-REM-RIGHTS-01` / Issue #114  
**Frozen reviewed producer:** Issue #80 work/head `3c262cbf767633e0ca42f6bdf387e262056b4fb0`  
**Frozen producer report:** `bda0551c446c93492c9d8e809d087d592dfcdae3`  
**Corrected artifact:** `docs/planning/wave-2/research/originality-rights-and-terms.md`

## Dispositions

### `PG-RIGHTS-M01` — RESOLVED

The corrected packet introduces an exact `ReferenceUseRecord` binding candidate ArtifactIdentity, source/reference identities, declared purpose, allowed/prohibited reuse, license/permission refs, provider-terms refs, provider input-admission evidence, release scope, provenance, exact originality-risk policy, and a content-addressed source-evidence root.

`OriginalityReviewRecord` and `ReleaseRightsAssessment` now both consume that exact `reference_use_id`, policy epoch, and compiled requirement-set identity. Cross-record candidate/release-scope/reference-use mismatch is invalid. Any changed purpose, reuse set, source/reference set, terms/license set, or release scope requires a new reference-use identity and newly compiled evidence requirements. Therefore an old originality result cannot authorize a materially different reuse context.

### `PG-RIGHTS-M02` — RESOLVED

The corrected packet defines versioned `ORIGINALITY-RISK-v1`, a closed input tuple, deterministic compilation rules, a content-bound `OriginalityEvidenceRequirementSet`, and fail-closed behavior. Every conditional evidence class must compile to `REQUIRED` or `NOT_APPLICABLE` before assessment. Unknown origin/reference/release classes, missing policy epoch, unrecognized material trigger, unresolved conditional, stale/missing required evidence, or `NOT_RUN`/`INCONCLUSIVE` required review prevents `CLEAR`.

Exact/normalized/known-reference, near-duplicate, targeted search, judgment, and qualified legal review applicability is therefore policy-bound rather than chosen ad hoc during release assessment. Similarity scores can only strengthen/escalate requirements, never waive them or produce legal clearance.

### `PG-RIGHTS-m01` — RESOLVED

The corrected state derivation has explicit precedence. Independent material-risk/conflict triggers derive `QUARANTINED(<reason>)`; absent those, stale required provider/legal/license/permission evidence derives only `UNKNOWN(STALE_EVIDENCE)`. Prior `CLEAR` remains immutable historical evidence. There is no longer an implementation choice between two primary states for staleness alone.

## Preserved boundaries

The remediation preserves the predecessor's separation of provenance, provider/contract permission, originality signals, and release-sensitive rights state; provider-output allocation is not clearance; similarity scores are escalation-only; unknown/restricted/quarantined material cannot silently release; provider/account/product terms remain exact/freshness-sensitive; and no unsupported legal conclusion is created.

## Remediation self-review

`0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR` in the bounded Issue #114 correction scope.

This disposition record is noncanonical planning evidence. Formal aggregate `W2-REV-01` remains required; no release, legal-clearance, implementation-readiness, integration, verification, or canonicalization authority is claimed.