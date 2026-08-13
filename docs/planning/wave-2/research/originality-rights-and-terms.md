# W2-REM-RIGHTS-05 — Duplicate derived-trigger fail-closed remediation

**Mission:** `W2-REM-RIGHTS-05` / Issue #148  
**Branch:** `planning/issue-148`  
**Base main:** `042d140b5d2e0b951da4528e1867514983418d6f`  
**Frozen remediation predecessor:** Issue #142 terminal `5277675462`, work/head `4b61b276bb28bb114a650e003a7a5d0aeb77411a`, fixture Git blob `39fcdc292cd37661a061c6d3027715106b3a3d27`  
**Independent finding:** Issue #145 terminal `5277781009`, work/head `99cb77f283f5e903cd46cec230833b4c7efee431`, `PG-REM4-RIGHTS-M01`  
**Authority:** noncanonical Wave-2 remediation input only. A fresh independently owned pre-gate review remains mandatory before formal `W2-REV-01` can consume this lane as clean.

## Bounded correction

Issue #145 showed that the exact Issue #142 `derive_state()` typed/domain guard admitted duplicate members in the set-like `material_triggers` list. Because downstream logic converted the list with `set(material_triggers)`, duplicate non-quarantine trigger values such as `TERMS_AMBIGUITY` could reach positive `CLEAR / ALL_REQUIRED_EVIDENCE_SATISFIED` when all required evidence was satisfied.

This remediation changes only that malformed structural surface. If `material_triggers` is a list whose members are all valid closed-domain trigger strings, uniqueness is now required before the inherited derived-state decision. Any duplicate member returns exact `UNKNOWN / POLICY_UNRESOLVED`. Existing null/bool/number/list/dict/nested-member handling continues through the inherited typed fail-closed guard, so malformed members do not reach set conversion. Valid unique trigger ordering remains non-authoritative.

The inherited policy semantics remain unchanged: `ORIGINALITY-RISK-v2` epoch `2`; the finite rule lattice and `REQUIRED > NOT_APPLICABLE` join; rule-order-independent compilation; stale-evidence and independent-risk quarantine precedence; canonical JSON/domain-separated content IDs; closed authority schemas; valid `SourceEvidenceRoot` ordering; and Issue #95 as immutable parallel provenance.

No legal clearance, provider permission, release approval, production/readiness authority, implementation authority, integration authority, verification authority, release authority, merge authority, or canonical status is created here.

## Executable provenance model

`docs/planning/wave-2/evidence/originality-rights-policy-fixtures.py` is a bounded delta capsule. It loads the exact frozen Issue #142 fixture by Git blob, independently verifies that blob's byte SHA-256 and Git object identity, executes the immutable base, and overlays only the duplicate-trigger guard plus the expanded malformed/regression evidence.

The current task branch deliberately preserves the exact Issue #142 tree as its direct parent commit (`7621f6fbf1b08d8ea6a904f8e3bf60ab53b5a898`), so the base Git object is durable in the review branch history. A consumer executing this noncanonical planning fixture must fetch branch history sufficient for `git cat-file blob 39fcdc292cd37661a061c6d3027715106b3a3d27`; this artifact is not represented as a standalone production runtime dependency.

Direct hashing of the exact predecessor Git bytes produced SHA-256 `6d078060db7f6a1f43fccc1c3d86cc8bacae51d61dfe40dd6e85d76bf19772f5`. The Issue #142 terminal packet published `2238b83bed5a298eb4dc9721a1d75831aa768bc70e2be3c451ff0e3126efa690`; that published source-SHA field does not reproduce from the exact Git blob and is therefore retained only as predecessor metadata, not reused as current evidence. The predecessor Git blob itself is exact and unambiguous.

## Mechanical evidence

The corrected fixture source is:

```yaml
fixture_path: docs/planning/wave-2/evidence/originality-rights-policy-fixtures.py
fixture_git_blob_sha: 3318f773b675e1bc0c5e5b41064bb1a1a2db7eea
fixture_source_sha256: bfa69936ce34a204b74a8d2a359257b73e8e917adaa4c79b2e0987d6615df09b
predecessor_fixture_git_blob_sha: 39fcdc292cd37661a061c6d3027715106b3a3d27
predecessor_fixture_actual_source_sha256: 6d078060db7f6a1f43fccc1c3d86cc8bacae51d61dfe40dd6e85d76bf19772f5
policy_id: ORIGINALITY-RISK-v2
policy_epoch: 2
serialization_version: EVERFIELD-RIGHTS-CANONICAL-JSON-v1
schema_version: EVERFIELD-RIGHTS-AUTHORITY-SCHEMA-v1
malformed_matrix_version: EVERFIELD-RIGHTS-MALFORMED-SCALAR-MATRIX-v2
tests_passed: 16
malformed_scalar_cases: 468
uncaught_exception_count: 0
malformed_matrix_digest_sha256: a1fc1fd2c78b11a5a81d8bf7b24d8ffaf3133876d70f7d5ea0400b84fd90daba
result_digest_sha256: be8f6df19367545ff2136d5c5db9c2a4c93f11f865f6d09ad4af067cb41efd4f
stdout_sha256: fef07eaaaa37b43221977b9d4eb5bbe5d22a7f9a115aa7e38c6d503886a167e1
```

Inherited `T01`–`T15` remain green. `T16_DERIVED_TRIGGER_SET_TOTAL_FAIL_CLOSED` adds all six duplicate closed-domain triggers, valid unique trigger reorder invariance, and nested malformed trigger members. The generated malformed/structural matrix expands from 462 to 468 cases and has zero uncaught exceptions.

All six duplicate trigger values now return exact `UNKNOWN / POLICY_UNRESOLVED` under the strongest positive-evidence setup (all requirements `REQUIRED`, all evidence `SATISFIED`): `CONFLICTING_SOURCE`, `CREDIBLE_COMPLAINT`, `MATERIAL_SIMILARITY_SIGNAL`, `PERMISSION_AMBIGUITY`, `SCOPE_AMBIGUITY`, and `TERMS_AMBIGUITY`.

## Finite-domain regression

The complete 802,816 valid epoch-2 combinations were independently re-executed with an optimized enumerator preserving the exact inherited domains, tuple order, canonical audit payload, and rule-order comparison. It reproduced the inherited audit digest exactly:

```yaml
valid_domain_combinations_checked: 802816
reverse_rule_order_requirement_mismatches: 0
nonclosed_requirement_outputs: 0
audit_digest_sha256: 166aebf1871a10768694790bcb936ec9ec119350676cf38fb055203259d3466c
```

Thus the malformed duplicate-set rejection changes no legitimate epoch-2 policy result and does not disturb order independence.

## Finding disposition and stopping rule

`PG-REM4-RIGHTS-M01` is **RESOLVED** mechanically. Self-review found 0 unresolved BLOCKER, 0 unresolved MAJOR, and 0 correction-requiring MINOR within this bounded remediation.

This author episode is not an independent judge. After the exact Issue #148 packet is frozen at `REVIEW_READY`, one fresh independently owned pre-gate review must attack the duplicate-trigger guard, the Git-blob provenance reconstruction, the 468-case matrix, and the inherited finite-domain preservation. If that independent review is clean, the rights lane proceeds to formal `W2-REV-01`; optional review churn is not authorized. Any eventual `main` integration remains separately authorized and squash-only.