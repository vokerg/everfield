# Handoff — Issue #119 / W2-REM-RIGHTS-02

## Mission state

```yaml
issue: 119
mission_id: W2-REM-RIGHTS-02
branch: planning/issue-119
actor_session_id: w2-rem-rights-02-agent-20260813-0825-01
base_main_sha: 042d140b5d2e0b951da4528e1867514983418d6f
claim_comment_id: 5276780235
substantive_work_sha: 2f5b3c22fe3c861db312f52473753dea2b4bd616
state_at_handoff_write: READY_FOR_REVIEW_VISIBILITY_PR
formal_review_required: W2-REV-01
authority: NONCANONICAL_REMEDIATION_INPUT
```

## Immutable inputs consumed

- Issue #114 / `W2-REM-RIGHTS-01`: exact work/head `4ba39fa26404ba9564702fd385c133df75b71972`, report blob `124866c20a6082624d3beba624859273b0d5572a`.
- Issue #118 / `W2-PG-REM-RIGHTS-01`: exact review work/head `e35d83b9758dfb1ffa07747a5c60cb82e80c5411`, review artifact blob `45f513bc4e8328ed75b979b76e982a2454705956`, disposition `CHANGES_NEEDED` with findings `PG-REM-RIGHTS-M01`, `PG-REM-RIGHTS-M02`, `PG-REM-RIGHTS-m01`.
- Canonical Planning Program v1 remained bound through Bootstrap Issue #6; task branch was created from exact then-current `main@042d140b5d2e0b951da4528e1867514983418d6f`.

Frozen predecessor branches were not edited or re-owned.

## Outputs at substantive work SHA

```yaml
corrected_report:
  path: docs/planning/wave-2/research/originality-rights-and-terms.md
  blob: a65f31c1a39eea7f32c4de0524c118c25c07cd6e
executable_fixture:
  path: docs/planning/wave-2/evidence/originality-rights-policy-fixtures.py
  git_blob: 5f821bdfce5c3e75869dcddedfe816fbda17d97c
  source_sha256: 8c19575ad09769515dee74ae8462233184cf1aece07cd7e27450ba1a63aaaa8a
finding_dispositions:
  path: docs/planning/wave-2/reviews/w2-rem-rights-01-pre-gate-review-dispositions.md
  blob: 170f35ce2b76742155a534429af9a2831c4f6c17
```

## Correction summary

1. `PG-REM-RIGHTS-M01`: `ORIGINALITY-RISK-v2` epoch 2 uses a closed `NOT_APPLICABLE < REQUIRED` lattice. All matching rules join with `REQUIRED` dominance, making overlap order-independent and preventing post-hoc easier-row selection. The exact Issue #118 `PROJECT_NATIVE + STYLE_OR_CREATOR_NAMED + RELEASE` overlap is executable evidence.
2. `PG-REM-RIGHTS-M02`: former `CONDITIONAL`/contextual choices are replaced by exact typed predicates and unknown state fails closed. `ReferenceUseRecord`, `OriginalityReviewRecord`, `ReleaseRightsAssessment`, `OriginalityEvidenceRequirementSet`, and `SourceEvidenceRoot` now have versioned canonical JSON, declared set/list normalization, SHA-256 domain separation, and mandatory recomputation/equality validation.
3. `PG-REM-RIGHTS-m01`: stale-state derivation now covers every evidence kind that can compile `REQUIRED`; independent material-risk triggers retain quarantine precedence and historical `CLEAR` remains immutable history.

## Mechanical verification

The exact frozen fixture blob was reconstructed from its Git blob identity and verified locally as exact bytes.

```yaml
python_syntax_compile: PASS
fresh_execution_count: 2
fresh_execution_outputs_byte_identical: true
policy_id: ORIGINALITY-RISK-v2
policy_epoch: 2
serialization_version: EVERFIELD-RIGHTS-CANONICAL-JSON-v1
fixture_source_sha256: 8c19575ad09769515dee74ae8462233184cf1aece07cd7e27450ba1a63aaaa8a
result_digest_sha256: 4530e561ffc8ccc85bba22ce02932300b4b7995ceb5b5979196e9dad5d588ced
tests_passed: 9
```

Passing test IDs:

- `T01_OVERLAP_JOIN_ORDER_INDEPENDENT`
- `T02_NO_CONDITIONAL_TERMINAL`
- `T03_UNKNOWN_FAILS_CLOSED`
- `T04_SET_ORDER_CANONICAL`
- `T05_BOUND_FIELDS_CHANGE_REFERENCE_USE_ID`
- `T06_SOURCE_ROOT_RECOMPUTABLE`
- `T07_ALL_REQUIRED_KINDS_HAVE_STALE_PRECEDENCE`
- `T08_CLEAR_REQUIRES_ALL_REQUIRED_SATISFIED`
- `T09_ALL_AUTHORITY_RECORD_IDS_RECOMPUTABLE`

Self-review: `0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR` in the bounded Issue #119 scope.

## Authority and downstream boundary

- No legal clearance or legal conclusion is created.
- No release approval, production/readiness, implementation, integration, verification, or canonicalization authority is created.
- Similarity remains escalation evidence only.
- Formal aggregate `W2-REV-01` remains required.
- Once this branch has an open draft review-visibility PR at its exact final head and the terminal schema-3 `STATUS(REVIEW_READY)` is published, this packet is the corrected substantive rights input for later Wave-2 review, preserving Issues #80/#114/#118 as immutable provenance.
- Any eventual `main` integration remains separately authorized and squash-only.

## Terminalization steps still required after this handoff commit

1. Re-fetch the task branch and Issue #119 ownership state.
2. Open a **draft** PR from exact `planning/issue-119` to `main` for review visibility only.
3. Re-fetch the PR and verify it is open/draft and its head equals the final branch head containing this handoff.
4. Only then publish terminal schema-3 `STATUS(REVIEW_READY)` on Issue #119 with exact head/work/artifact identities.

No merge is authorized by this handoff.