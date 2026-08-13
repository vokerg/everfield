# W2-REM-RIGHTS-03 — Issue #125 finding dispositions

**Mission:** `W2-REM-RIGHTS-03` / Issue #129  
**Reviewed input:** Issue #125 work/head `a789bd9fd74c85f928d23171591adafc6f3a6fde`, review blob `4bec551a6c7ba14dfcca55ed7bdd2c590675b0be`  
**Corrected predecessor input:** Issue #119 work/head `7b856e2589d7b98c6fa224f670c500fa2f67b6d9`  
**Authority:** remediation disposition only; fresh independent pre-gate review and formal `W2-REV-01` remain required.

## `PG-REM2-RIGHTS-M01` — RESOLVED

Issue #125 demonstrated missing/malformed `artifact_id`, `reference_use_id`, and `release_scope_ref` could compile or raise, while unhashable trigger members could raise before closed failure.

Correction:

- compiler inputs must be mappings with the exact declared key set;
- all authority bindings are validated before indexing/rule/hash work;
- `reference_use_id` must be `rur-sha256:<64hex>` and compiler artifact/scope bindings use the closed namespaced grammar;
- trigger container is proven a list and every member a string before duplicate/membership/set operations;
- malformed/missing/unknown cases return exactly `UNKNOWN(POLICY_UNRESOLVED)`.

Evidence: `T10_COMPILER_BINDINGS_TOTAL_FAIL_CLOSED` and `T11_TRIGGER_MEMBERS_TOTAL_FAIL_CLOSED`.

## `PG-REM2-RIGHTS-M02` — RESOLVED

Issue #125 demonstrated reduced authority payloads could self-hash and `SourceEvidenceRoot` could accept underspecified entries.

Correction:

- `EVERFIELD-RIGHTS-AUTHORITY-SCHEMA-v1` requires exact field sets before hashing for every authority record;
- inherited value domains and exact-or-`NOT_APPLICABLE` sentinels are preserved rather than silently narrowed;
- unknown/missing fields and invalid types/domains fail before canonicalization;
- `content_id` refuses invalid schema and `validate_claimed_id` returns false for invalid payloads;
- the Issue #119 canonical JSON/domain-separation contract remains unchanged for valid records;
- `SourceEvidenceRoot` requires exactly `kind`, `record_id`, `content_sha256`, and `immutable_ref`; schema-v1 has a finite source-evidence kind vocabulary; malformed identities, unknown kinds, duplicate IDs, and conflicting same-ID evidence fail closed.

Evidence: `T12_AUTHORITY_RECORD_SCHEMA_PRECEDES_ID`, `T13_SOURCE_ROOT_SCHEMA_AND_ID_UNIQUENESS`, and `T14_ALL_AUTHORITY_SCHEMAS_CLOSED`.

## Regression disposition

Preserved Issue #119 tests `T01`–`T09` all pass. Fresh finite-domain audit checks `802,816` valid policy tuples with zero forward/reverse requirement mismatches and zero nonclosed requirement outputs. Issue #95 remains immutable parallel provenance. No legal clearance, release approval, production/readiness, implementation, integration, verification, or canonicalization authority is claimed.
