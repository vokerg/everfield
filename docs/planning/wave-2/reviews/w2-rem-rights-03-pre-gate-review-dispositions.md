# W2-REM-RIGHTS-04 — Issue #141 finding disposition

**Mission:** `W2-REM-RIGHTS-04` / Issue #142  
**Reviewed predecessor:** Issue #129 exact work/head `714394de603dd425a2cb9d2fd2eea1b7cb6135ca`  
**Routing review:** Issue #141 exact work/head `9033fec21c5f48935923c1eda3fee5d8694aba1a`, terminal status comment `5277452429`  
**Finding:** `PG-REM3-RIGHTS-M01`  
**Disposition:** `RESOLVED`

## Mechanical closure

Issue #141 demonstrated that malformed externally supplied scalar/domain values could reach hash-based set/dict membership in the Issue #129 executable fixture before scalar type validation. In particular, list/dict substitutions could raise `TypeError: unhashable type` instead of returning the declared fail-closed result.

The Issue #142 fixture closes that root cause rather than suppressing exceptions after the fact:

1. closed-domain set membership is guarded by exact string-type validation before membership;
2. closed mapping membership/indexing is guarded by exact string-type validation before lookup;
3. compiler scalar/domain inputs reject before `_rule_contributions` can index `RELEASE_SCOPES` or build authority-bearing sets;
4. authority-record enums, requirement values, record-type dispatch, content-ID record type, and `SourceEvidenceRoot.kind` use the same typed guard;
5. derived-state evidence values and material-trigger values are validated before closed membership semantics are consumed.

## Regression evidence

```yaml
fixture_git_blob_sha: 39fcdc292cd37661a061c6d3027715106b3a3d27
fixture_source_sha256: 2238b83bed5a298eb4dc9721a1d75831aa768bc70e2be3c451ff0e3126efa690
tests_passed: 15
malformed_scalar_cases: 462
uncaught_exception_count: 0
result_digest_sha256: b4d401765ae8447a6a5afeccdcd28e8bbbca9a21d8b84e85b81edb5ec8fe7c9b
stdout_sha256: 09609122666dfb040188661aaf362ee6af66fae56bf9dd43271275ccff3b7cd4
two_fresh_stdout_runs_byte_identical: true
valid_domain_combinations_checked: 802816
reverse_rule_order_requirement_mismatches: 0
nonclosed_requirement_outputs: 0
audit_digest_sha256: 166aebf1871a10768694790bcb936ec9ec119350676cf38fb055203259d3466c
```

The first fourteen regression groups remain the Issue #129 inherited suite. `T15_ALL_AUTHORITY_SCALARS_TOTAL_FAIL_CLOSED` adds the generated `EVERFIELD-RIGHTS-MALFORMED-SCALAR-MATRIX-v1` attack. All 462 malformed substitutions reject without an uncaught exception. The complete 802,816-tuple valid epoch-2 lattice remains closed and rule-order independent.

## Authority boundary

This disposition is author-side remediation evidence only. It does not constitute the required fresh independent review and creates no legal clearance, release approval, provider permission, production/readiness, implementation, integration, verification, release, merge, or canonicalization authority. A fresh independently owned pre-gate review must attack the exact final Issue #142 branch. If clean, the rights lane proceeds to formal `W2-REV-01` rather than another optional review loop.
