# W2-REM-RIGHTS-03 — Rights authority schema and fail-closed input remediation

**Mission:** `W2-REM-RIGHTS-03` / Issue #129  
**Branch:** `planning/issue-129`  
**Base main:** `042d140b5d2e0b951da4528e1867514983418d6f`  
**Frozen predecessor:** Issue #119 work/head `7b856e2589d7b98c6fa224f670c500fa2f67b6d9`  
**Frozen predecessor report blob:** `a65f31c1a39eea7f32c4de0524c118c25c07cd6e`  
**Frozen predecessor fixture blob:** `5f821bdfce5c3e75869dcddedfe816fbda17d97c`  
**Independent review:** Issue #125 work/head `a789bd9fd74c85f928d23171591adafc6f3a6fde`, terminal comment `5277037579`  
**Independent review blob:** `4bec551a6c7ba14dfcca55ed7bdd2c590675b0be`  
**Authority:** noncanonical Wave-2 remediation input only; a fresh independent pre-gate review and formal `W2-REV-01` remain required.

## 1. Composition and preserved authority boundaries

This is a bounded successor overlay over exact Issue #119. The `ORIGINALITY-RISK-v2` epoch-2 lattice, rule predicates/contributions, `REQUIRED > NOT_APPLICABLE` join, sorted compiler trace, stale-evidence precedence, provenance/originality separation, similarity-as-escalation-only semantics, release blocking, provider/terms freshness behavior, and canonical JSON/domain-separation contract remain unchanged unless explicitly tightened below.

Issue #125 found exactly two MAJOR defects:

- `PG-REM2-RIGHTS-M01`: declared compiler authority bindings and trigger members were not totally validated before indexing/hash operations;
- `PG-REM2-RIGHTS-M02`: content-ID recomputation was not complete-record schema validation, and `SourceEvidenceRoot` accepted underspecified/conflicting entries.

Issue #95 remains prior parallel immutable remediation provenance at work/head `de96bd19d903d3fb0b9b15d0c199205f09cf7143`, terminal comment `5271670119`. Reconstructable lineage remains `#80 → #95` in parallel with `#80 → #114 → #118 → #119 → #125 → #129`; no unique-first-successor claim is made.

Nothing here provides legal advice or clearance, release approval, provider permission beyond retained evidence, production/readiness authority, implementation authority, integration authority, verification authority, or canonical status.

## 2. Total compiler-envelope validation

The executable reference implementation remains `docs/planning/wave-2/evidence/originality-rights-policy-fixtures.py`. It preserves `ORIGINALITY-RISK-v2`, epoch `2`, and `EVERFIELD-RIGHTS-CANONICAL-JSON-v1`, while adding validator version `EVERFIELD-RIGHTS-AUTHORITY-SCHEMA-v1`.

A compiler input is admitted only when its top-level key set is exactly:

```text
policy_id, policy_epoch, artifact_id, reference_use_id, release_scope_ref,
origin_class, reference_class, release_scope_class, material_trigger_set,
media_kind, references_exist, incorporation_or_release_intent,
legal_interpretation_material
```

Validation occurs before indexing, rule evaluation, hashing, or set construction. Missing or unknown fields and malformed values return exactly `UNKNOWN(POLICY_UNRESOLVED)`.

Authority bindings are closed before compilation: `artifact_id` and `release_scope_ref` use the versioned namespaced identity grammar; `reference_use_id` must be `rur-sha256:<64 lowercase hex>`; booleans are exact boolean values; every enum belongs to its epoch-2 set. `material_trigger_set` must be a list and every member must be a string before duplicate/membership/set operations. Unknown, duplicate, null, boolean, numeric, object, list, or otherwise malformed members fail closed without an exception.

## 3. Complete schema validation before authority identity

`EVERFIELD-RIGHTS-AUTHORITY-SCHEMA-v1` validates the complete inherited field set before canonical bytes are constructed for:

- `ReferenceUseRecord`;
- `OriginalityReviewRecord`;
- `ReleaseRightsAssessment`;
- `OriginalityEvidenceRequirementSet`;
- `SourceEvidenceRoot`.

Missing and unknown fields are rejected. Closed inherited enums and sentinels are preserved rather than replaced: the inherited `OriginalityReviewRecord.result` set (`NO_MATERIAL_SIGNAL_FOUND | MATERIAL_SIGNAL | NEAR_DUPLICATE | EXACT_DUPLICATE | INCONCLUSIVE | NOT_RUN`) remains admissible; `legal_conclusion` remains `NONE`; `ReleaseRightsAssessment` retains `NOT_APPLICABLE`; exact-or-`NOT_APPLICABLE` references remain legal where inherited; and the epoch-2 requirement/rule/trigger domains are closed mechanically. Fields whose predecessor semantics are exact opaque authority references use a closed representation grammar instead of inventing new business semantics.

`content_id(record_type, payload)` refuses a schema-invalid payload and `validate_claimed_id(...)` returns false for malformed/incomplete data. For valid data, Issue #119's canonicalization is unchanged: `EVERFIELD-RIGHTS-CANONICAL-JSON-v1` hashes the exact `{payload, record_type, serialization_version}` envelope after semantic-set normalization with the same per-record domain separators. Schema version is validation provenance and is not silently injected into that v1 envelope.

Consequently an empty or reduced record cannot gain authority merely by self-hashing, an unknown field cannot be smuggled into a v1 payload, and invalid ordered/set values fail before identity acceptance.

## 4. Closed `SourceEvidenceRoot` entry contract

Every `SourceEvidenceRoot.evidence_entries` member is exactly:

```yaml
kind: <one EVERFIELD-RIGHTS-AUTHORITY-SCHEMA-v1 source-evidence kind>
record_id: <exact content-bound, immutable, policy, or namespaced authority identity>
content_sha256: <64 lowercase hex>
immutable_ref: <git-blob:SHA40 | git-commit:SHA40 | repo:path@SHA40 | protected:content-addressed-token>
```

Schema-v1 source-evidence kinds are the finite set:

```text
ArtifactIdentity
RightsProvenanceRecord
SourceReferenceIdentity
LicenseOrPermissionRecord
ProviderTermsRecord
ProviderInputAdmissionRecord
OriginalityRiskPolicy
```

A new authority kind requires a schema-version revision rather than an unversioned string. The entry list must be nonempty and every `record_id` unique. Incomplete entries, unknown kinds, malformed identities/digests/immutable refs, exact duplicates, and same-ID/different-content conflicts fail before root authority. The inherited semantic-set canonicalization remains: reordering distinct valid entries leaves the root unchanged; changing an authority entry changes the root.

## 5. Mechanical evidence and reproducibility

The exact corrected fixture is independently bound by both Git blob and source-byte SHA-256:

```yaml
fixture_path: docs/planning/wave-2/evidence/originality-rights-policy-fixtures.py
fixture_git_blob_sha: 8777e6eb45a47fd82b3dc976ab2a5a416fb909fb
fixture_source_sha256: 7f4f4b7755e51c8dafbe89e3690098089b47b776ee35329ee08a40f0810c151f
fixture_size_bytes: 38752
policy_id: ORIGINALITY-RISK-v2
policy_epoch: 2
serialization_version: EVERFIELD-RIGHTS-CANONICAL-JSON-v1
schema_version: EVERFIELD-RIGHTS-AUTHORITY-SCHEMA-v1
tests_passed: 14
result_digest_sha256: b27e214b5dc8d5bc9353d65dacc795e01148d09f2f23e9a3433099f89c330698
stdout_sha256: 0a0f57bbcf32e88c22a55f6949ffaca19fb9e15ba8db21cb43bd13a185d0133c
two_fresh_stdout_runs_byte_identical: true
```

Tests `T01`–`T09` preserve Issue #119's overlap/order/stale/content-identity behavior. New groups are:

1. `T10_COMPILER_BINDINGS_TOTAL_FAIL_CLOSED`;
2. `T11_TRIGGER_MEMBERS_TOTAL_FAIL_CLOSED`;
3. `T12_AUTHORITY_RECORD_SCHEMA_PRECEDES_ID`, including inherited exact-or-`NOT_APPLICABLE` representation;
4. `T13_SOURCE_ROOT_SCHEMA_AND_ID_UNIQUENESS`, including unknown-kind and malformed-record-ID rejection;
5. `T14_ALL_AUTHORITY_SCHEMAS_CLOSED`, including the inherited review-result domain and assessment `NOT_APPLICABLE` state.

A fresh exhaustive valid-domain audit traversed all `802,816` epoch-2 policy tuples through exact input validation and forward/reverse rule joins. It deliberately audits the finite policy lattice directly rather than repeatedly hashing identical schema mechanics:

```yaml
valid_combinations_checked: 802816
reverse_rule_order_requirement_mismatches: 0
nonclosed_requirement_outputs: 0
audit_digest_sha256: 6cf96c14a56e4ed7ebcfda827acdff9af1a5bd2621f353c82a787e2244e81b47
```

## 6. Finding dispositions and downstream use

`PG-REM2-RIGHTS-M01` is **RESOLVED** mechanically: every declared compiler field is validated before indexing, authority identifiers have closed forms, and trigger-member type precedes set/hash operations. The review crash/false-admission classes are executable negatives.

`PG-REM2-RIGHTS-M02` is **RESOLVED** mechanically: complete versioned authority schemas precede content-ID/root acceptance, inherited value domains are preserved, unknown/missing fields fail closed, and source-root entries have complete typed structure with finite kind vocabulary and one-to-one record identity.

This corrected packet remains noncanonical input only. A fresh independently owned pre-gate review must attack the exact frozen Issue #129 work/head before formal `W2-REV-01` may consume it as clean rights evidence. Any eventual `main` integration remains separately authorized and squash-only.
