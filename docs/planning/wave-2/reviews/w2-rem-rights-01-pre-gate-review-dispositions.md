# W2-REM-RIGHTS-02 — Issue #118 finding dispositions

**Mission:** `W2-REM-RIGHTS-02` / Issue #119  
**Frozen remediation predecessor:** Issue #114 work/head `4ba39fa26404ba9564702fd385c133df75b71972`  
**Independent review:** Issue #118 work/head `e35d83b9758dfb1ffa07747a5c60cb82e80c5411`  
**Review artifact:** blob `45f513bc4e8328ed75b979b76e982a2454705956`  
**Corrected report:** `docs/planning/wave-2/research/originality-rights-and-terms.md`  
**Executable evidence:** `docs/planning/wave-2/evidence/originality-rights-policy-fixtures.py`  
**Authority:** bounded noncanonical remediation evidence only; formal `W2-REV-01` remains required.

## Evidence identity

```yaml
policy_id: ORIGINALITY-RISK-v2
policy_epoch: 2
serialization_version: EVERFIELD-RIGHTS-CANONICAL-JSON-v1
fixture_git_blob_sha: 5f821bdfce5c3e75869dcddedfe816fbda17d97c
fixture_source_sha256: 8c19575ad09769515dee74ae8462233184cf1aece07cd7e27450ba1a63aaaa8a
fixture_result_digest_sha256: 4530e561ffc8ccc85bba22ce02932300b4b7995ceb5b5979196e9dad5d588ced
fixture_tests_passed: 9
fixture_execution: syntax_compile_passed_and_two_runs_byte_identical
```

No finding below is waived by prose. `RESOLVED` means the exact corrected contract plus executable evidence closes the reviewed defect while preserving the issue's authority boundary.

## `PG-REM-RIGHTS-M01` — MAJOR — RESOLVED

### Reviewed defect

Issue #118 demonstrated that `ORIGINALITY-RISK-v1` allowed one exact tuple to match multiple rows with materially different requirement cells and supplied no precedence, row selection, or typed merge operation. The concrete attack was `PROJECT_NATIVE + STYLE_OR_CREATOR_NAMED + RELEASE` with no material trigger.

### Correction

`ORIGINALITY-RISK-v2` replaces row selection with a closed two-element requirement lattice:

```text
NOT_APPLICABLE < REQUIRED
```

Every matching rule contributes requirements and all contributions are joined cell-by-cell with `REQUIRED` dominance. The join is commutative, associative, and idempotent. The compiler cannot emit `CONDITIONAL` as a terminal state.

For the exact Issue #118 overlap tuple, `R0_TOTAL_BASELINE`, `R2_NATIVE_BUILD`, and `R3_STYLE_OR_CREATOR` all match and deterministically produce one normalized set requiring exact identity, normalized identity, known-reference comparison, near-duplicate checks, targeted external search, and judgment review. Rule order cannot weaken it.

### Mechanical evidence

- `T01_OVERLAP_JOIN_ORDER_INDEPENDENT`: compiles the exact attack tuple and recompiles with reversed rule application order; normalized requirements are identical.
- `T02_NO_CONDITIONAL_TERMINAL`: verifies terminal compiler cells are only `REQUIRED` or `NOT_APPLICABLE`.

### Disposition

`RESOLVED`. An exact valid tuple/epoch has one normalized requirement set; overlap cannot select an easier rule post hoc.

## `PG-REM-RIGHTS-M02` — MAJOR — RESOLVED

### Reviewed defect

Issue #118 found two linked authority gaps:

1. `CONDITIONAL`, `where media-appropriate`, and similar contextual cells did not have exact predicates that deterministically collapse them before assessment.
2. `ReferenceUseRecord.reference_use_id`, `OriginalityReviewRecord.review_id`, `ReleaseRightsAssessment.assessment_id`, `OriginalityEvidenceRequirementSet.requirement_set_id`, and `source_evidence_root` were described as stable/content-bound but lacked a canonical serialization, included-field contract, collection ordering, digest/domain separation, and mandatory recomputation check.

### Correction — closed applicability

Epoch 2 makes the contextual inputs explicit and typed: `references_exist`, `media_kind`, `incorporation_or_release_intent`, `legal_interpretation_material`, release scope, and the closed material-trigger set. Unknown values fail closed as `UNKNOWN(POLICY_UNRESOLVED)`. Terminal requirements have no `CONDITIONAL` state.

### Correction — canonical content identity

The corrected contract defines `EVERFIELD-RIGHTS-CANONICAL-JSON-v1`, exact UTF-8 canonical JSON behavior, record-type domain separation, SHA-256, textual ID prefixes, semantic-set normalization/duplicate rejection, ordered-list behavior, and exact `SourceEvidenceRoot` entries. The claimed ID itself is excluded from its own canonical payload; every declared authority-bearing payload field is included.

Consumers must recompute and compare each claimed record ID/root before it can contribute authority. Mismatched purpose, reuse permissions, terms, license/permission evidence, source/reference identity, release scope, policy requirement identity, or source evidence invalidates the old claimed identity rather than inheriting its assessment.

### Mechanical evidence

- `T02_NO_CONDITIONAL_TERMINAL`: no unresolved terminal contextual state.
- `T03_UNKNOWN_FAILS_CLOSED`: undeclared contextual enum fails closed.
- `T04_SET_ORDER_CANONICAL`: semantic-set reorder is stable; the canonicalizer rejects duplicate semantic-set members.
- `T05_BOUND_FIELDS_CHANGE_REFERENCE_USE_ID`: purpose, release scope, provider terms, license/permission, and source/reference substitution changes identity.
- `T06_SOURCE_ROOT_RECOMPUTABLE`: exact evidence-set reorder remains stable while evidence-content substitution changes the root.
- `T09_ALL_AUTHORITY_RECORD_IDS_RECOMPUTABLE`: each authority-bearing record type recomputes; bound-payload mutation changes the identity.

### Disposition

`RESOLVED`. Applicability and authority identity are now reconstructable from exact frozen bytes rather than an implementation's unstated choice or producer assertion.

## `PG-REM-RIGHTS-m01` — MINOR — RESOLVED

### Reviewed defect

Issue #114 explicitly mapped stale provider/legal/license/permission evidence to `UNKNOWN(STALE_EVIDENCE)` but did not state the same deterministic primary state for every other originality evidence kind that can compile `REQUIRED`.

### Correction

Epoch 2 applies the stale branch to every compiled `REQUIRED` kind:

- exact identity;
- normalized identity;
- known-reference comparison;
- near-duplicate checks;
- targeted external search;
- judgment review;
- qualified legal review.

Independent material-risk triggers (`MATERIAL_SIMILARITY_SIGNAL`, `CREDIBLE_COMPLAINT`, `CONFLICTING_SOURCE`) retain higher quarantine precedence. Historical `CLEAR` remains immutable history and is not rewritten.

### Mechanical evidence

- `T07_ALL_REQUIRED_KINDS_HAVE_STALE_PRECEDENCE`: iterates all seven requirement kinds and verifies `UNKNOWN(STALE_EVIDENCE)`; repeats each case with a credible complaint and verifies quarantine precedence.
- `T08_CLEAR_REQUIRES_ALL_REQUIRED_SATISFIED`: verifies `CLEAR` only when every compiled required kind is satisfied.

### Disposition

`RESOLVED`. No compiled required evidence kind is left without an exact stale-state route.

## Self-review

The exact frozen fixture blob syntax-compiles and two fresh executions produce byte-identical output with the published result digest. Fresh self-review against the bounded Issue #119 contract and the exact Issue #118 findings records:

```yaml
unresolved_blocker: 0
unresolved_major: 0
correction_requiring_minor: 0
legal_clearance_claimed: false
release_approval_claimed: false
production_or_readiness_authority_claimed: false
integration_authority_claimed: false
verification_or_canonicalization_authority_claimed: false
formal_review_still_required: W2-REV-01
```

The fixture is planning evidence only. It does not encode legal doctrine and cannot become production logic or release authority by being executable.