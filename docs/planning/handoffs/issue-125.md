# Handoff — Issue #125 / W2-PG-REM-RIGHTS-02

## Mission state

```yaml
issue: 125
mission_id: W2-PG-REM-RIGHTS-02
branch: planning/issue-125
actor_session_id: w2-pg-rem-rights-02-agent-20260813-0842-01
base_main_sha: 042d140b5d2e0b951da4528e1867514983418d6f
claim_comment_id: 5276939180
reviewed_issue: 119
reviewed_work_head: 7b856e2589d7b98c6fa224f670c500fa2f67b6d9
review_artifact_blob: 4bec551a6c7ba14dfcca55ed7bdd2c590675b0be
disposition: CHANGES_NEEDED
blocker: 0
major: 2
minor_requiring_correction: 0
bounded_successor: 129
state_at_handoff_write: READY_FOR_REVIEW_VISIBILITY_PR
formal_review_required: W2-REV-01
authority: NONAUTHORITY_PRE_GATE_REVIEW
```

## Immutable inputs consumed

- Issue #119 exact terminal work/head `7b856e2589d7b98c6fa224f670c500fa2f67b6d9`.
- Corrected report blob `a65f31c1a39eea7f32c4de0524c118c25c07cd6e`.
- Executable fixture Git blob `5f821bdfce5c3e75869dcddedfe816fbda17d97c`.
- Issue #119 finding-disposition blob `170f35ce2b76742155a534429af9a2831c4f6c17`.
- Issue #119 handoff blob `7f9ad281cae9b3bfcb5b9979ad87254d3b334634`.
- Issue #118 independent review blob `45f513bc4e8328ed75b979b76e982a2454705956` only to reconstruct the defects #119 claimed to close.
- Issue #95 exact prior parallel remediation provenance as recorded by #119; it was not edited or re-owned.
- Issue #119 draft PR #124, independently verified open/draft at exact reviewed head.

## Review output

Review artifact:

```yaml
path: docs/planning/wave-2/reviews/w2-rem-rights-02-pre-gate-review.md
blob: 4bec551a6c7ba14dfcca55ed7bdd2c590675b0be
result: CHANGES_NEEDED
findings:
  - PG-REM2-RIGHTS-M01: MAJOR
  - PG-REM2-RIGHTS-M02: MAJOR
bounded_remediation_successor: 129
```

### Mechanical evidence

```yaml
producer_declared_result_digest_reproduced: 4530e561ffc8ccc85bba22ce02932300b4b7995ceb5b5979196e9dad5d588ced
producer_declared_tests_reproduced: 9
fresh_execution_outputs_byte_identical: true
valid_policy_combinations_exhaustively_checked: 802816
reverse_rule_order_requirement_mismatches: 0
nonclosed_requirement_outputs: 0
trigger_permutation_same_requirement_set_id: true
adversarial_evidence_digest_sha256: ee841909435616e50803743ee82e706a2bff4388ec37358e170c245f0217153e
```

The exact Git blob identity was independently resolved. The connector exposed blob text rather than a raw byte-mounted checkout, so this review does not claim an independent second computation of the producer-published fixture source SHA-256.

### Findings

1. **`PG-REM2-RIGHTS-M01` — MAJOR.** `_validate_policy_input` does not validate the declared authority bindings `artifact_id`, `reference_use_id`, or `release_scope_ref`. `None`/wrong-type values can still produce `COMPILED`; missing fields raise uncaught `KeyError`; unhashable trigger members raise uncaught `TypeError` before closed failure. Epoch 2 is deterministic for valid inputs but not a total fail-closed compiler over malformed input.
2. **`PG-REM2-RIGHTS-M02` — MAJOR.** Canonical hashing/recomputation does not itself enforce complete authority-record schemas. Empty/incomplete `ReferenceUseRecord` payloads and incomplete `SourceEvidenceRoot` entries can receive self-consistent recomputable identities. Machine-checkable schema validation must precede identity/root authority.

The valid overlap lattice, 802,816 finite-domain order-independence check, trigger ordering normalization, all-seven-kind stale-state precedence, #95 provenance reconciliation, draft-PR binding, and authority boundaries passed attack.

## Routing

Issue #129 / `W2-REM-RIGHTS-03` was created as the single bounded remediation route. It is **unclaimed** by this reviewer episode and remains blocked until Issue #125 terminalizes at an exact immutable review head. A distinct session must own it.

Formal `W2-REV-01` remains required after the dependency/remediation graph is satisfied.

## Authority boundary

- No legal clearance or legal conclusion is created.
- No release approval or provider permission is created.
- No implementation/production readiness is created.
- No integration, verification, or canonicalization authority is created.
- No merge is authorized.
- Frozen Issues #95/#114/#118/#119 were not edited or re-owned.

## Terminalization steps after this handoff commit

1. Re-fetch Issue #125 operational comments and `planning/issue-125`; prove claim `5276939180` still owns the exact branch head.
2. Open a **draft** PR from exact `planning/issue-125` to `main` for review visibility only.
3. Re-fetch that PR and verify `open=true`, `draft=true`, and PR head equals the final branch head containing this review and handoff.
4. Only then publish exact schema-3 `STATUS(REVIEW_READY)` on Issue #125 with review/handoff blobs, disposition, findings, successor #129, and exact head/work identity.

No squash merge or other integration occurs in this task.