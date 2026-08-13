# W2-REM-RIGHTS-06 — Self-contained rights delta evidence remediation

**Mission:** `W2-REM-RIGHTS-06` / Issue #162  
**Branch:** `planning/issue-162`  
**Claim generation:** `5280305793`  
**Base main:** `373cdafef7825455f50993f67b5220c08b0e774e`  
**Reviewed predecessor remediation:** Issue #148 at exact head `91545c6121a3cf071df524fd17e5e2978f7a65b2`  
**Independent finding:** Issue #159 terminal review, `PG-REM5-RIGHTS-M01`  
**Authority:** noncanonical Wave-2 remediation input only. Fresh independent review remains mandatory before formal `W2-REV-01`.

## Bounded correction

Issue #159 found one reconstructability defect in the otherwise mechanically sound Issue #148 duplicate-trigger correction: the delta fixture loaded predecessor blob `39fcdc292cd37661a061c6d3027715106b3a3d27` with `git cat-file`, but that object was reachable only through task-branch ancestry. Squash integration would retain the resulting tree but not that ancestry, so a main-only checkout could not rely on object reachability.

This remediation makes the packet self-contained without changing the reviewed policy logic:

- the exact immutable Issue #142 predecessor fixture is retained in the resulting tree at
  `docs/planning/wave-2/evidence/originality-rights-policy-fixtures-predecessor-issue-142.py`;
- that retained path points to the exact predecessor Git blob `39fcdc292cd37661a061c6d3027715106b3a3d27`;
- its exact-byte SHA-256 remains `6d078060db7f6a1f43fccc1c3d86cc8bacae51d61dfe40dd6e85d76bf19772f5`;
- the top-level fixture reads the adjacent retained file directly with `pathlib`, verifies both byte SHA-256 and the Git-blob identity computed from `blob <len>\0<bytes>`, then executes those exact immutable bytes;
- no branch ref, `git cat-file`, non-main parent commit, or server object-retention assumption is required.

Issue #142's published source-SHA metadata `2238b83bed5a298eb4dc9721a1d75831aa768bc70e2be3c451ff0e3126efa690` remains historical metadata only and is not rewritten or promoted.

## Semantic preservation proof

The corrected wrapper differs from the exact Issue #148 wrapper only in its module description/imports, retained-file identity constant, and `_load_base_source()` implementation. From the `# Re-export the unchanged bounded policy fixture surface` marker through the end of the executable, the Issue #148 and Issue #162 source is byte-identical.

Therefore the policy/evidence computation is unchanged once the loader has verified and returned the exact predecessor bytes:

- `ORIGINALITY-RISK-v2`, epoch `2`;
- inherited T01–T15 behavior;
- `T16_DERIVED_TRIGGER_SET_TOTAL_FAIL_CLOSED`;
- all six duplicate closed-domain triggers -> exact `UNKNOWN / POLICY_UNRESOLVED`;
- malformed nested members remain total/fail-closed;
- valid unique-trigger ordering remains non-authoritative;
- stale/quarantine precedence is unchanged;
- malformed/structural matrix remains 468 cases with 0 uncaught exceptions;
- valid-domain audit remains 802,816 tuples, 0 reverse-rule-order requirement mismatches, 0 nonclosed outputs.

The reviewed Issue #148 runtime evidence identities remain the deterministic projection of the same exact predecessor bytes and byte-identical computation tail:

```yaml
malformed_matrix_version: EVERFIELD-RIGHTS-MALFORMED-SCALAR-MATRIX-v2
tests_passed: 16
malformed_scalar_cases: 468
uncaught_exception_count: 0
malformed_matrix_digest_sha256: a1fc1fd2c78b11a5a81d8bf7b24d8ffaf3133876d70f7d5ea0400b84fd90daba
result_digest_sha256: be8f6df19367545ff2136d5c5db9c2a4c93f11f865f6d09ad4af067cb41efd4f
stdout_sha256: fef07eaaaa37b43221977b9d4eb5bbe5d22a7f9a115aa7e38c6d503886a167e1
valid_domain_combinations_checked: 802816
reverse_rule_order_requirement_mismatches: 0
nonclosed_requirement_outputs: 0
audit_digest_sha256: 166aebf1871a10768694790bcb936ec9ec119350676cf38fb055203259d3466c
```

Current corrected wrapper identities before commit:

```yaml
wrapper_source_sha256: 09a823d975ecd677bd4eaad162287d539781b05d7e8950d04932f593ed03e71d
wrapper_git_blob_sha: 441a17ba2ea19681bf87439f6d4f252e2e21cd9e
retained_predecessor_git_blob_sha: 39fcdc292cd37661a061c6d3027715106b3a3d27
retained_predecessor_source_sha256: 6d078060db7f6a1f43fccc1c3d86cc8bacae51d61dfe40dd6e85d76bf19772f5
```

## Fresh-checkout / main-only reconstruction

After this packet is integrated by a separately authorized squash route, a normal checkout of that resulting tree needs only:

```text
python3 docs/planning/wave-2/evidence/originality-rights-policy-fixtures.py
```

The wrapper resolves only its adjacent retained predecessor file and Python standard-library modules. It does not inspect Git refs or object storage. A reviewer should independently reproduce the retained file's Git blob and byte SHA-256, execute the wrapper twice, compare stdout byte-for-byte, and reconcile the 468-case and 802,816-tuple evidence before a clean review.

## Finding disposition and self-review

`PG-REM5-RIGHTS-M01` is **RESOLVED** at the producer-remediation boundary: the corrected resulting tree contains the exact predecessor bytes and the executable no longer depends on hidden history.

Bounded self-review:

- unresolved BLOCKER: `0`
- unresolved MAJOR: `0`
- correction-requiring MINOR: `0`

This is producer self-review only, not independent acceptance. One fresh independently owned pre-gate review is mandatory on the exact terminal Issue #162 packet. If clean, the rights lane proceeds to formal `W2-REV-01`; no optional review churn is authorized.

No legal clearance, provider permission, release approval, production/readiness, implementation, integration, verification, release, merge, or canonicalization authority is granted. Any eventual `main` integration is separately authorized and squash-only.
