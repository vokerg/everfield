# W2-REM-RIGHTS-03 — Rights authority schema and fail-closed input remediation

**Mission:** `W2-REM-RIGHTS-03` / Issue #129  
**Branch:** `planning/issue-129`  
**Base main:** `042d140b5d2e0b951da4528e1867514983418d6f`  
**Frozen predecessor:** Issue #119 work/head `7b856e2589d7b98c6fa224f670c500fa2f67b6d9`  
**Frozen predecessor report blob:** `a65f31c1a39eea7f32c4de0524c118c25c07cd6e`  
**Frozen predecessor fixture blob:** `5f821bdfce5c3e75869dcddedfe816fbda17d97c`  
**Independent review:** Issue #125 work/head `a789bd9fd74c85f928d23171591adafc6f3a6fde`, terminal comment `5277037579`  
**Independent review blob:** `4bec551a6c7ba14dfcca55ed7bdd2c590675b0be`  
**Authority:** noncanonical Wave-2 remediation input only; formal `W2-REV-01` and a fresh independent pre-gate review remain required.

## 1. Composition and preserved authority boundaries

This document is a bounded successor overlay over exact Issue #119. Issue #119's `ORIGINALITY-RISK-v2` epoch-2 lattice, rule predicates/contributions, `REQUIRED > NOT_APPLICABLE` join, sorted compiler trace, stale-evidence precedence, provenance/originality separation, similarity-as-escalation-only semantics, release blocking, provider/terms freshness behavior, and no-clearance/no-readiness authority remain inherited unchanged unless explicitly replaced below.

The exact Issue #125 attack found two MAJOR defects and no other material regressions:

- `PG-REM2-RIGHTS-M01`: declared compiler authority bindings and trigger members were not totally validated before indexing/hash operations;
- `PG-REM2-RIGHTS-M02`: content-ID recomputation was not complete-record schema validation, and `SourceEvidenceRoot` accepted underspecified/conflicting entries.

Issue #95 remains prior parallel immutable remediation provenance at work/head `de96bd19d903d3fb0b9b15d0c199205f09cf7143`, terminal comment `5271670119`. The reconstructable lineage remains `#80 → #95` in parallel with `#80 → #114 → #118 → #119 → #125 → #129`; no unique-first-successor claim is made.

Nothing in this remediation provides legal advice or clearance, release approval, provider permission beyond retained evidence, production/readiness authority, implementation authority, integration authority, verification authority, or canonical status.

## 2. Total compiler-envelope validation

The executable reference implementation remains at `docs/planning/wave-2/evidence/originality-rights-policy-fixtures.py`. It preserves `ORIGINALITY-RISK-v2`, epoch `2`, and `EVERFIELD-RIGHTS-CANONICAL-JSON-v1`, while adding schema validator version `EVERFIELD-RIGHTS-AUTHORITY-SCHEMA-v1`.

A policy input is admitted only when its top-level key set is exactly:

```text
policy_id, policy_epoch, artifact_id, reference_use_id, release_scope_ref,
origin_class, reference_class, release_scope_class, material_trigger_set,
media_kind, references_exist, incorporation_or_release_intent,
legal_interpretation_material
```

Validation occurs before indexing, rule evaluation, hashing, or set construction. Unknown or missing fields return exactly `UNKNOWN(POLICY_UNRESOLVED)`.

Authority-binding identifiers are closed before compilation: `artifact_id` and `release_scope_ref` must be nonempty namespaced identifiers matching the published `namespace:value` grammar without whitespace/NUL; `reference_use_id` must be an exact `rur-sha256:<64 lowercase hex>` content identity; booleans use exact boolean type; and every enum belongs to its closed epoch-2 set.

`material_trigger_set` must be a JSON list whose members are strings before duplicate or membership checks. Unknown, duplicate, null, boolean, numeric, object, list, or otherwise malformed members return the same unresolved state. No unhashable member can reach `set(...)`, and no malformed authority identifier can reach requirement-set hashing.

## 3. Schema validation before authority identity

`EVERFIELD-RIGHTS-AUTHORITY-SCHEMA-v1` is a closed-field validator for `ReferenceUseRecord`, `OriginalityReviewRecord`, `ReleaseRightsAssessment`, `OriginalityEvidenceRequirementSet`, and `SourceEvidenceRoot`.

For every record, the executable validator requires the exact versioned field set. Missing or unknown fields are invalid. Required identifiers, enums, list/container types, semantic-set uniqueness, policy/version bindings, requirement-cell values, and content-identity forms are checked before canonical bytes are constructed.

This validation is deliberately pre-hash. `content_id(record_type, payload)` refuses a schema-invalid payload; `validate_claimed_id(...)` returns `false` for malformed/incomplete data rather than treating a self-consistent reduced-payload digest as authority. The valid-data canonicalization and domain-separation contract from Issue #119 is unchanged: `EVERFIELD-RIGHTS-CANONICAL-JSON-v1` still hashes the exact envelope `{payload, record_type, serialization_version}` after set normalization. Schema version is validation provenance and is not injected into the existing v1 canonical envelope.

Thus `{}` cannot receive an authoritative `ReferenceUseRecord` identity; omitting `provider_terms_refs` or another required field is invalid even if remaining bytes hash; wrong container/identifier types fail before hashing; and unknown fields cannot be smuggled into a v1 authority payload.

## 4. Closed `SourceEvidenceRoot` entry contract

Every `SourceEvidenceRoot.evidence_entries` member is exactly:

```yaml
kind: <nonempty record-kind string>
record_id: <nonempty namespaced exact record identity>
content_sha256: <64 lowercase hex>
immutable_ref: <git-blob:SHA40 | git-commit:SHA40 | repo:path@SHA40 | protected:content-addressed-token>
```

The entry list must be nonempty and every `record_id` unique across the root. Exact duplicates and same-ID/different-content conflicts fail closed before hashing. Every entry must have all four fields and no extras, a syntactically closed SHA-256, and an immutable-reference form.

The prior semantic-set canonicalization remains: ordering of distinct valid entries does not change the root; changing any entry's record identity, evidence digest, immutable reference, or kind changes the root. Root authority is impossible when an entry is underspecified or conflicts with another entry carrying the same record identity.

## 5. Mechanical evidence

The corrected standard-library-only planning fixture preserves all nine Issue #119 checks and adds five exact closure groups for Issue #125 attacks. Its repository object is bound by exact Git identity rather than an unverified external byte hash:

```yaml
fixture_path: docs/planning/wave-2/evidence/originality-rights-policy-fixtures.py
fixture_git_blob_sha: 479798a18a68230110c07348a6792809904e1ae6
fixture_size_bytes: 35536
policy_id: ORIGINALITY-RISK-v2
policy_epoch: 2
serialization_version: EVERFIELD-RIGHTS-CANONICAL-JSON-v1
schema_version: EVERFIELD-RIGHTS-AUTHORITY-SCHEMA-v1
tests_passed: 14
result_digest_sha256: b27e214b5dc8d5bc9353d65dacc795e01148d09f2f23e9a3433099f89c330698
stdout_sha256: 0a0f57bbcf32e88c22a55f6949ffaca19fb9e15ba8db21cb43bd13a185d0133c
two_fresh_stdout_runs_byte_identical: true
```

The preserved tests are `T01`–`T09` from Issue #119. New groups are `T10_COMPILER_BINDINGS_TOTAL_FAIL_CLOSED`, `T11_TRIGGER_MEMBERS_TOTAL_FAIL_CLOSED`, `T12_AUTHORITY_RECORD_SCHEMA_PRECEDES_ID`, `T13_SOURCE_ROOT_SCHEMA_AND_ID_UNIQUENESS`, and `T14_ALL_AUTHORITY_SCHEMAS_CLOSED`.

A fresh exhaustive valid-domain audit separately traversed all `802,816` epoch-2 policy combinations using the corrected validation/rule functions:

```yaml
valid_combinations_checked: 802816
reverse_rule_order_requirement_mismatches: 0
nonclosed_requirement_outputs: 0
audit_digest_sha256: 9dbbe1c7d694b985dabe716d1764797d78eab2a2d5c35490291b17b3dfedcb8d
```

This confirms the Issue #125-clean overlap lattice and closed terminal requirement values did not regress while the malformed-input boundary was strengthened.

## 6. Finding dispositions and downstream use

`PG-REM2-RIGHTS-M01` is **RESOLVED** mechanically: all declared compiler fields are checked before indexing, authority identifiers have closed forms, and trigger member type precedes set/hash operations. The exact review crash/false-admission classes are executable negatives.

`PG-REM2-RIGHTS-M02` is **RESOLVED** mechanically: complete versioned authority-record schemas precede content-ID/root acceptance, unknown/missing fields fail closed, and source-root entries have complete typed structure plus one-to-one record identity.

The corrected packet is noncanonical input only. A fresh independently owned pre-gate review must attack the exact frozen Issue #129 work/head before formal `W2-REV-01` can treat it as clean rights evidence. Any eventual `main` integration remains separately authorized and squash-only.
