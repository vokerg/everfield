# W2-REM-RIGHTS-04 pre-gate review dispositions — Issue #148

## Binding

- remediation mission: `W2-REM-RIGHTS-05`
- remediation issue: `#148`
- finding source: Issue `#145` / `W2-PG-REM-RIGHTS-04`
- review terminal comment: `5277781009`
- review exact head/work: `99cb77f283f5e903cd46cec230833b4c7efee431`
- reviewed predecessor remediation: Issue `#142` at exact head `4b61b276bb28bb114a650e003a7a5d0aeb77411a`
- finding: `PG-REM4-RIGHTS-M01`
- disposition: `RESOLVED`

## `PG-REM4-RIGHTS-M01` — RESOLVED

Issue #145 demonstrated that duplicate values in set-like `derive_state.material_triggers` were not rejected before the inherited `set(material_triggers)` conversion and authority decision. Duplicate non-quarantine trigger members could therefore yield positive `CLEAR / ALL_REQUIRED_EVIDENCE_SATISFIED` under otherwise satisfied evidence.

Issue #148 adds a uniqueness guard after typed closed-domain member validation and before the inherited derived-state decision. Every duplicate closed-domain trigger now returns exact `UNKNOWN / POLICY_UNRESOLVED`; malformed nested/list/dict/bool/number/null members continue to fail closed through the inherited typed guard; valid unique trigger order remains non-authoritative.

Mechanical correction evidence:

```yaml
current_fixture_blob: 3318f773b675e1bc0c5e5b41064bb1a1a2db7eea
current_fixture_source_sha256: bfa69936ce34a204b74a8d2a359257b73e8e917adaa4c79b2e0987d6615df09b
predecessor_fixture_blob: 39fcdc292cd37661a061c6d3027715106b3a3d27
predecessor_actual_source_sha256: 6d078060db7f6a1f43fccc1c3d86cc8bacae51d61dfe40dd6e85d76bf19772f5
malformed_matrix_version: EVERFIELD-RIGHTS-MALFORMED-SCALAR-MATRIX-v2
malformed_cases: 468
uncaught_exception_count: 0
malformed_matrix_digest_sha256: a1fc1fd2c78b11a5a81d8bf7b24d8ffaf3133876d70f7d5ea0400b84fd90daba
tests_passed: 16
result_digest_sha256: be8f6df19367545ff2136d5c5db9c2a4c93f11f865f6d09ad4af067cb41efd4f
stdout_sha256: fef07eaaaa37b43221977b9d4eb5bbe5d22a7f9a115aa7e38c6d503886a167e1
valid_domain_combinations_checked: 802816
reverse_rule_order_requirement_mismatches: 0
nonclosed_requirement_outputs: 0
audit_digest_sha256: 166aebf1871a10768694790bcb936ec9ec119350676cf38fb055203259d3466c
```

The six duplicate-domain cases covered are `CONFLICTING_SOURCE`, `CREDIBLE_COMPLAINT`, `MATERIAL_SIMILARITY_SIGNAL`, `PERMISSION_AMBIGUITY`, `SCOPE_AMBIGUITY`, and `TERMS_AMBIGUITY`. Each returns exact `UNKNOWN / POLICY_UNRESOLVED` with all requirements `REQUIRED` and all evidence `SATISFIED`.

The exact predecessor Git blob hashes directly to byte SHA-256 `6d078060...`; Issue #142's published source-SHA field `2238b83b...` does not reproduce from those exact bytes. That older field is preserved as immutable predecessor metadata but is not used as current evidence. The current delta capsule verifies the exact predecessor Git object before overlaying the bounded correction.

## Self-adjudication boundary

Self-review at the remediation boundary reports:

- unresolved BLOCKER: `0`
- unresolved MAJOR: `0`
- correction-requiring MINOR: `0`

This is producer self-check only, not independent acceptance. One fresh independently owned pre-gate review is mandatory on the exact terminal Issue #148 packet. If clean, the rights lane must converge to formal `W2-REV-01`; no optional review churn is authorized by this disposition.

No legal clearance, provider permission, release approval, production/readiness, implementation, integration, verification, release, merge, or canonicalization authority is granted. Any eventual `main` integration remains separately authorized and squash-only.