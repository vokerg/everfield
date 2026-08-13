# W2-REM-RIGHTS-04 — Total rights-authority scalar/domain validation

**Mission:** `W2-REM-RIGHTS-04` / Issue #142  
**Branch:** `planning/issue-142`  
**Base main:** `042d140b5d2e0b951da4528e1867514983418d6f`  
**Frozen substantive predecessor:** Issue #129 work/head `714394de603dd425a2cb9d2fd2eea1b7cb6135ca`, report blob `c141b4f0db79390228c4088439f2396db56d26b8`, fixture blob `8777e6eb45a47fd82b3dc976ab2a5a416fb909fb`  
**Independent review:** Issue #141 terminal comment `5277452429`, work/head `9033fec21c5f48935923c1eda3fee5d8694aba1a`, finding `PG-REM3-RIGHTS-M01`  
**Authority:** noncanonical Wave-2 remediation input only. A fresh independent pre-gate review remains mandatory before formal `W2-REV-01` may treat the rights lane as clean.

## Scope and preserved semantics

This is a bounded successor overlay over exact Issue #129. It repairs only the fresh totality defect identified by Issue #141: externally supplied scalar/domain values could reach Python set/dict membership or indexing before their scalar/string type was proven, so malformed JSON-shaped lists or objects could raise `TypeError` rather than fail closed.

The following Issue #129 semantics are preserved unchanged: `ORIGINALITY-RISK-v2` epoch `2`; the finite rule lattice and `REQUIRED > NOT_APPLICABLE` join; order-independent compiler results; stale-evidence and independent-risk quarantine precedence; the canonical JSON/domain-separated content-ID contract; complete authority-record field sets; `SourceEvidenceRoot` valid ordering; and Issue #95 as prior parallel immutable provenance. This remediation does not reinterpret provider permission, originality, legal meaning, release scope, or any readiness decision.

No legal clearance, release approval, provider permission, production/readiness authority, implementation authority, integration authority, verification authority, release authority, or canonical status is created here.

## Total scalar/domain guard

The executable reference remains `docs/planning/wave-2/evidence/originality-rights-policy-fixtures.py`. The corrected implementation introduces typed membership helpers that prove `type(value) is str` before any membership or mapping lookup whose key domain is a closed string vocabulary.

The compiler now rejects malformed values before policy evaluation or indexing for all closed scalar/domain inputs, including at minimum:

- `origin_class`;
- `reference_class`;
- `release_scope_class`;
- `media_kind`;
- `policy_id` and exact integer `policy_epoch`;
- exact boolean policy predicates;
- every `material_trigger_set` member.

Malformed inputs return exactly `{"status":"UNKNOWN","reason":"POLICY_UNRESOLVED"}`. Lists, dictionaries, nulls, booleans in non-boolean domains, numbers, empty strings, and unknown strings cannot reach authority-bearing set/dict membership.

The same rule is applied to the closed authority schema and derived-state surfaces, including:

- the `record_type` dispatch key itself;
- `ReferenceUseRecord.reference_class` and policy-ref scalar;
- `OriginalityReviewRecord.result`, policy-ref scalar, and legal-conclusion scalar;
- `ReleaseRightsAssessment.derived_rights_or_terms_state`, `reason_code`, and policy-ref scalar;
- every `OriginalityEvidenceRequirementSet.requirements` value plus policy ID/epoch;
- every `SourceEvidenceRoot.evidence_entries[].kind`;
- externally supplied evidence-state and material-trigger values consumed by `derive_state`.

Invalid record/root values are rejected through the declared validation API. `content_id(...)` still refuses invalid records, and `validate_claimed_id(...)` still returns false rather than upgrading malformed data.

## Generated malformed-value matrix

`EVERFIELD-RIGHTS-MALFORMED-SCALAR-MATRIX-v1` is generated from the closed authority scalar/domain surfaces rather than hand-picking only the Issue #141 examples. It substitutes malformed JSON-shaped values across those fields and requires deterministic rejection without an uncaught exception.

The exact corrected executable evidence is:

```yaml
fixture_path: docs/planning/wave-2/evidence/originality-rights-policy-fixtures.py
fixture_git_blob_sha: 39fcdc292cd37661a061c6d3027715106b3a3d27
fixture_source_sha256: 2238b83bed5a298eb4dc9721a1d75831aa768bc70e2be3c451ff0e3126efa690
policy_id: ORIGINALITY-RISK-v2
policy_epoch: 2
serialization_version: EVERFIELD-RIGHTS-CANONICAL-JSON-v1
schema_version: EVERFIELD-RIGHTS-AUTHORITY-SCHEMA-v1
malformed_matrix_version: EVERFIELD-RIGHTS-MALFORMED-SCALAR-MATRIX-v1
tests_passed: 15
malformed_scalar_cases: 462
uncaught_exception_count: 0
result_digest_sha256: b4d401765ae8447a6a5afeccdcd28e8bbbca9a21d8b84e85b81edb5ec8fe7c9b
stdout_sha256: 09609122666dfb040188661aaf362ee6af66fae56bf9dd43271275ccff3b7cd4
two_fresh_stdout_runs_byte_identical: true
```

Tests `T01`–`T14` retain the Issue #129 regression groups. `T15_ALL_AUTHORITY_SCALARS_TOTAL_FAIL_CLOSED` adds the generated malformed-domain attack. The resulting matrix has 462 substitutions and zero uncaught exceptions.

## Finite-domain regression

The complete valid epoch-2 lattice was re-run after the scalar hardening:

```yaml
valid_domain_combinations_checked: 802816
reverse_rule_order_requirement_mismatches: 0
nonclosed_requirement_outputs: 0
audit_digest_sha256: 166aebf1871a10768694790bcb936ec9ec119350676cf38fb055203259d3466c
```

Thus the correction strengthens malformed-input rejection without narrowing or changing legitimate epoch-2 policy results. The audit also retains deterministic rule-order independence.

## Finding disposition

`PG-REM3-RIGHTS-M01` is **RESOLVED** mechanically. No externally supplied authority scalar/domain covered by the closed contract may reach the relevant set/dict membership/indexing operation before type/domain rejection. The generated matrix proves the malformed list/dict/null/bool/number/string classes fail closed with zero uncaught exceptions, while all inherited tests and the 802,816-tuple valid-domain audit remain green.

This author episode is not the independent judge of the correction. One fresh independently owned pre-gate review must attack the exact frozen Issue #142 packet. If that review is clean, the rights lane proceeds to formal `W2-REV-01`; optional review churn is not authorized by this remediation. Any eventual `main` integration is separately authorized and squash-only.
