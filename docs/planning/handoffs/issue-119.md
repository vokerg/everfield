# Handoff — Issue #119 / W2-REM-RIGHTS-02

## Mission state

```yaml
issue: 119
mission_id: W2-REM-RIGHTS-02
branch: planning/issue-119
actor_session_id: w2-rem-rights-02-agent-20260813-0825-01
base_main_sha: 042d140b5d2e0b951da4528e1867514983418d6f
claim_comment_id: 5276780235
provenance_reconciliation_comment_id: 5276892802
substantive_work_sha: 2f5b3c22fe3c861db312f52473753dea2b4bd616
state_at_handoff_write: READY_FOR_REVIEW_VISIBILITY_PR
formal_review_required: W2-REV-01
authority: NONCANONICAL_REMEDIATION_INPUT
```

## Immutable inputs consumed

- Issue #80 / `W2-RIGHTS-01`: original frozen rights producer work/head `3c262cbf767633e0ca42f6bdf387e262056b4fb0`, report blob `bda0551c446c93492c9d8e809d087d592dfcdae3`.
- Issue #95 / earlier `W2-REM-RIGHTS-01`: **prior parallel remediation provenance**, terminal status comment `5271670119`, exact work/head `de96bd19d903d3fb0b9b15d0c199205f09cf7143`, report blob `06e04f7d707b9694f58fbe9c534bc7a99f5ed14e`, policy blob `db2eb5fe36be4ac7ed0204832a3537db0f97e1df`, disposition blob `1382500e19ab7e374f065df71248f1b15d47f007`, handoff blob `a3e51e2ba76f17d436994163f015ad855c393af5`.
- Issue #114 / later duplicate mission-ID `W2-REM-RIGHTS-01`: exact work/head `4ba39fa26404ba9564702fd385c133df75b71972`, report blob `124866c20a6082624d3beba624859273b0d5572a`.
- Issue #118 / `W2-PG-REM-RIGHTS-01`: exact review work/head `e35d83b9758dfb1ffa07747a5c60cb82e80c5411`, review artifact blob `45f513bc4e8328ed75b979b76e982a2454705956`, disposition `CHANGES_NEEDED` with findings `PG-REM-RIGHTS-M01`, `PG-REM-RIGHTS-M02`, `PG-REM-RIGHTS-m01`.
- Canonical Planning Program v1 remained bound through Bootstrap Issue #6; task branch was created from exact then-current `main@042d140b5d2e0b951da4528e1867514983418d6f`.

Issue #95 terminalized before Issue #114 was created. Therefore #114 is **not** treated as the unique or first successor of Issue #80. Issues #95 and #114 are preserved as duplicate/parallel immutable remediation provenance surfaces that reused mission ID `W2-REM-RIGHTS-01`. Issue #119 follows its explicit hard-prerequisite route through exact #114 and the exact #118 review of #114; it does not rewrite or re-own #95. Durable reconciliation is recorded on Issue #119 in comment `5276892802`.

Frozen predecessor/provenance branches were not edited or re-owned.

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

The prior Issue #95 remediation already established nonconflicting invariants including fail-closed applicability, most-restrictive aggregation, acyclic authority-identity intent, deterministic stale precedence, immutable historical assessment, and a current-source-bounded provider/legal posture. Issue #119 preserves those invariants while closing the later Issue #118 defects against #114 with a fully typed terminal compiler and exact executable content-ID/root recomputation contract. Structural record naming across #95/#114 remains provenance rather than a claim that one older branch was canonical; formal `W2-REV-01` receives the full lineage.

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

Self-review: `0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR` in the bounded Issue #119 scope after provenance reconciliation.

## Authority and downstream boundary

- No legal clearance or legal conclusion is created.
- No release approval, production/readiness, implementation, integration, verification, or canonicalization authority is created.
- Similarity remains escalation evidence only.
- Formal aggregate `W2-REV-01` remains required.
- Once this branch has an open draft review-visibility PR at its exact final head and the terminal schema-3 `STATUS(REVIEW_READY)` is published, this packet is the corrected substantive rights input for later Wave-2 review, preserving Issues #80/#95/#114/#118 as immutable lineage evidence.
- Any eventual `main` integration remains separately authorized and squash-only.

## Terminalization steps still required after this handoff commit

1. Re-fetch the task branch and Issue #119 ownership state.
2. Open a **draft** PR from exact `planning/issue-119` to `main` for review visibility only.
3. Re-fetch the PR and verify it is open/draft and its head equals the final branch head containing this handoff.
4. Only then publish terminal schema-3 `STATUS(REVIEW_READY)` on Issue #119 with exact head/work/artifact identities and the #95 provenance reconciliation.

No merge is authorized by this handoff.