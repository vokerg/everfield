# W2-REM-RIGHTS-03 — Issue #125 finding dispositions

**Mission:** `W2-REM-RIGHTS-03` / Issue #129  
**Reviewed input:** Issue #125 review work/head `a789bd9fd74c85f928d23171591adafc6f3a6fde`, review blob `4bec551a6c7ba14dfcca55ed7bdd2c590675b0be`  
**Corrected predecessor input:** Issue #119 work/head `7b856e2589d7b98c6fa224f670c500fa2f67b6d9`  
**Authority:** remediation disposition only; fresh independent pre-gate review and formal `W2-REV-01` remain required.

## `PG-REM2-RIGHTS-M01` — RESOLVED

Issue #125 demonstrated that missing/malformed `artifact_id`, `reference_use_id`, and `release_scope_ref` could compile or raise, and unhashable trigger members could raise before closed failure.

Correction in the exact executable fixture:

- policy inputs must be mappings with the exact declared key set;
- all three authority bindings are validated before indexing/rule/hash work;
- `reference_use_id` must be `rur-sha256:<64hex>`; generic artifact/scope identifiers must satisfy the closed namespaced grammar;
- trigger container is verified as a list and every member is proven a string before membership/duplicate set operations;
- every malformed/missing/unknown case returns exactly `UNKNOWN(POLICY_UNRESOLVED)`.

Evidence: `T10_COMPILER_BINDINGS_TOTAL_FAIL_CLOSED` and `T11_TRIGGER_MEMBERS_TOTAL_FAIL_CLOSED`; no uncaught `KeyError`/`TypeError` path is used for the review's attacks.

## `PG-REM2-RIGHTS-M02` — RESOLVED

Issue #125 demonstrated that recomputing a digest over an incomplete record could self-validate and that `SourceEvidenceRoot` accepted underspecified entries.

Correction:

- `EVERFIELD-RIGHTS-AUTHORITY-SCHEMA-v1` defines exact field sets and closed types/value domains for every authority record;
- unknown/missing fields fail before canonicalization;
- `content_id` refuses invalid schema and `validate_claimed_id` returns false for invalid payloads;
- the canonical JSON/domain-separation contract for valid records remains `EVERFIELD-RIGHTS-CANONICAL-JSON-v1` unchanged;
- `SourceEvidenceRoot` entries require exactly `kind`, `record_id`, `content_sha256`, and `immutable_ref`, with typed forms and unique record identity; duplicate/conflicting IDs fail closed.

Evidence: `T12_AUTHORITY_RECORD_SCHEMA_PRECEDES_ID`, `T13_SOURCE_ROOT_SCHEMA_AND_ID_UNIQUENESS`, and `T14_ALL_AUTHORITY_SCHEMAS_CLOSED`.

## Regression disposition

Preserved Issue #119 tests `T01`–`T09` all pass. Fresh full-domain audit checks `802,816` valid policy combinations with zero reverse-rule-order requirement mismatches and zero nonclosed requirement outputs. Issue #95 remains immutable parallel provenance. No legal clearance, release approval, production/readiness, implementation, integration, verification, or canonicalization authority is claimed.
