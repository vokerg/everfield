# W2-REM-RIGHTS-05 pre-gate review dispositions — Issue #162

## Binding

- remediation mission: `W2-REM-RIGHTS-06`
- remediation issue: `#162`
- finding source: Issue `#159` / `W2-PG-REM-RIGHTS-05`
- reviewed predecessor remediation: Issue `#148` at exact head `91545c6121a3cf071df524fd17e5e2978f7a65b2`
- finding: `PG-REM5-RIGHTS-M01`
- producer disposition: `RESOLVED`

## `PG-REM5-RIGHTS-M01` — RESOLVED

Issue #159 showed that Issue #148's executable delta capsule depended on `git cat-file blob 39fcdc...`, while that exact predecessor object was reachable only through task-branch ancestry. A squash result could therefore retain the delta file without guaranteeing the predecessor object in a main-only checkout.

Issue #162 retains the exact predecessor bytes directly in the resulting tree as
`docs/planning/wave-2/evidence/originality-rights-policy-fixtures-predecessor-issue-142.py`
with exact Git blob `39fcdc292cd37661a061c6d3027715106b3a3d27` and exact-byte SHA-256
`6d078060db7f6a1f43fccc1c3d86cc8bacae51d61dfe40dd6e85d76bf19772f5`.

The corrected top-level fixture reads that adjacent file, verifies both identities without invoking Git, and then executes the exact bytes. The Issue #148 computation tail is byte-identical from the re-export marker onward, so the duplicate-trigger correction and bounded evidence semantics are unchanged.

Corrected wrapper identities:

```yaml
wrapper_git_blob_sha: 441a17ba2ea19681bf87439f6d4f252e2e21cd9e
wrapper_source_sha256: 09a823d975ecd677bd4eaad162287d539781b05d7e8950d04932f593ed03e71d
retained_predecessor_git_blob_sha: 39fcdc292cd37661a061c6d3027715106b3a3d27
retained_predecessor_actual_source_sha256: 6d078060db7f6a1f43fccc1c3d86cc8bacae51d61dfe40dd6e85d76bf19772f5
```

Preserved deterministic evidence:

```yaml
tests_passed: 16
malformed_cases: 468
uncaught_exception_count: 0
malformed_matrix_digest_sha256: a1fc1fd2c78b11a5a81d8bf7b24d8ffaf3133876d70f7d5ea0400b84fd90daba
result_digest_sha256: be8f6df19367545ff2136d5c5db9c2a4c93f11f865f6d09ad4af067cb41efd4f
stdout_sha256: fef07eaaaa37b43221977b9d4eb5bbe5d22a7f9a115aa7e38c6d503886a167e1
valid_domain_combinations_checked: 802816
reverse_rule_order_requirement_mismatches: 0
nonclosed_requirement_outputs: 0
audit_digest_sha256: 166aebf1871a10768694790bcb936ec9ec119350676cf38fb055203259d3466c
```

Issue #142's older published non-reproducing source-SHA remains historical metadata only.

## Self-adjudication boundary

Producer self-review reports 0 unresolved BLOCKER, 0 unresolved MAJOR, and 0 correction-requiring MINOR. This does not constitute independent acceptance. One fresh independently owned pre-gate review is required on the exact terminal Issue #162 packet; if clean, proceed to formal `W2-REV-01`.

No legal clearance, provider permission, release approval, production/readiness, implementation, integration, verification, release, merge, or canonicalization authority is granted.
