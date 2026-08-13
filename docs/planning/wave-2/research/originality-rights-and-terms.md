# W2-REM-RIGHTS-01 — Rights/originality authority remediation

**Mission:** `W2-REM-RIGHTS-01` / Issue #114  
**Branch:** `planning/issue-114`  
**Base main:** `042d140b5d2e0b951da4528e1867514983418d6f`  
**Frozen predecessor:** Issue #80 work/head `3c262cbf767633e0ca42f6bdf387e262056b4fb0`  
**Frozen predecessor report blob:** `bda0551c446c93492c9d8e809d087d592dfcdae3`  
**Authority:** noncanonical Wave-2 remediation input; formal `W2-REV-01` remains required.

## 1. Composition and scope

This artifact is a bounded successor overlay over the exact frozen Issue #80 report blob `bda0551c446c93492c9d8e809d087d592dfcdae3`. Every predecessor clause remains inherited unless this remediation explicitly replaces it below. If the predecessor blob does not resolve exactly, this remediation is invalid.

The predecessor's source research, provider-terms matrix, reference-use taxonomy, provenance/originality separation, similarity-as-escalation-only semantics, release blocking, freshness triggers, and authority limits remain unchanged. This overlay repairs only independent pre-gate findings `PG-RIGHTS-M01`, `PG-RIGHTS-M02`, and `PG-RIGHTS-m01`.

No statement here is legal advice or legal clearance. No similarity score, provider term, model judgment, or this artifact alone authorizes release.

## 2. Closed reference-use authority binding — resolves `PG-RIGHTS-M01`

The predecessor `OriginalityReviewRecord` and `ReleaseRightsAssessment` are replaced by a three-record binding in which reuse context is exact and replay-resistant.

```yaml
ReferenceUseRecord:
  reference_use_id: <stable content-bound identity>
  candidate_artifact_id: <exact ArtifactIdentity>
  source_reference_ids: [<exact ArtifactIdentity/source IDs>]
  reference_class: FACTUAL_OR_FUNCTIONAL | GENERAL_CONCEPTUAL | STYLE_OR_CREATOR_NAMED | EXPRESSION_SPECIFIC | DIRECT_ASSET_OR_CODE | MARK_LIKENESS_PERSONA | CONFIDENTIAL_PRIVATE_RESTRICTED | PUBLIC_DOMAIN_CLAIM
  declared_purpose: <exact bounded purpose>
  allowed_reuse: [<explicit actions/scopes>]
  prohibited_reuse: [<explicit actions/scopes>]
  license_or_permission_refs: [<exact immutable refs>]
  provider_terms_refs: [<exact ProviderTermsRecord IDs>]
  provider_input_admission_ref: <exact or NOT_APPLICABLE>
  release_scope_ref: <exact>
  provenance_record_ref: <exact RightsProvenanceRecord>
  originality_risk_policy_ref: <exact OriginalityRiskPolicy>
  source_evidence_root: <content-addressed digest of all referenced authority records>
```

```yaml
OriginalityReviewRecord:
  review_id: <stable content-bound identity>
  candidate_artifact_id: <exact>
  reference_use_id: <exact ReferenceUseRecord>
  policy_epoch_ref: <exact OriginalityRiskPolicy>
  compiled_requirement_set_ref: <exact OriginalityEvidenceRequirementSet>
  reference_corpus_ref: <content-addressed set>
  exact_duplicate_checks: []
  near_duplicate_checks: []
  targeted_external_search_refs: []
  judgment_panel_ref: <exact or NOT_APPLICABLE>
  qualified_legal_review_ref: <exact or NOT_APPLICABLE>
  material_signals: []
  blind_spots: []
  result: NO_MATERIAL_SIGNAL_FOUND | MATERIAL_SIGNAL | NEAR_DUPLICATE | EXACT_DUPLICATE | INCONCLUSIVE | NOT_RUN
  legal_conclusion: NONE
```

```yaml
ReleaseRightsAssessment:
  assessment_id: <stable content-bound identity>
  artifact_id: <exact>
  release_scope_ref: <exact>
  provenance_record_ref: <exact>
  reference_use_id: <exact ReferenceUseRecord>
  policy_epoch_ref: <exact OriginalityRiskPolicy>
  compiled_requirement_set_ref: <exact OriginalityEvidenceRequirementSet>
  provider_terms_refs: [<exact>]
  license_or_permission_refs: [<exact>]
  originality_review_ref: <exact when REQUIRED; NOT_APPLICABLE only when compiled as such>
  unresolved_triggers: []
  derived_rights_or_terms_state: CLEAR | RESTRICTED | QUARANTINED | UNKNOWN | NOT_APPLICABLE
  reason_code: <closed reason code>
  derivation_trace: []
  freshness_refs: []
  reopen_conditions: []
```

### Binding rules

1. `candidate_artifact_id`, `release_scope_ref`, and `reference_use_id` MUST agree across the three records.
2. `ReferenceUseRecord.source_evidence_root` MUST be recomputed from the exact referenced provenance, license/permission, provider-terms, provider-input-admission, policy, and source/reference identities.
3. An `OriginalityReviewRecord` is invalid if its `reference_use_id`, `policy_epoch_ref`, or compiled requirement set differs from the consuming `ReleaseRightsAssessment`.
4. Reusing an originality result under a different purpose, allowed/prohibited reuse set, source/reference set, provider terms epoch, license/permission set, or release scope is forbidden. A changed context requires a new `ReferenceUseRecord` and a newly compiled evidence requirement set; any required review must then be rerun or explicitly remain unresolved.
5. A `CLEAR` state is impossible from prose adjacency. The exact record graph above must close.

This makes the reviewed context part of the authority identity rather than metadata that can drift independently.

## 3. Versioned originality-risk policy — resolves `PG-RIGHTS-M02`

The predecessor phrase “optional/required by risk policy” is replaced by the following closed policy contract.

```yaml
OriginalityRiskPolicy:
  policy_id: ORIGINALITY-RISK-v1
  policy_epoch: 1
  policy_content_sha256: <digest of exact policy bytes>
  supported_origin_classes:
    - PROJECT_NATIVE
    - GENERATED_PROVIDER
    - EXTERNAL_REFERENCE
    - EXTERNAL_ASSET
    - THIRD_PARTY_OUTPUT
    - LICENSED_MATERIAL
    - PUBLIC_DOMAIN_CLAIM
  supported_reference_classes:
    - FACTUAL_OR_FUNCTIONAL
    - GENERAL_CONCEPTUAL
    - STYLE_OR_CREATOR_NAMED
    - EXPRESSION_SPECIFIC
    - DIRECT_ASSET_OR_CODE
    - MARK_LIKENESS_PERSONA
    - CONFIDENTIAL_PRIVATE_RESTRICTED
    - PUBLIC_DOMAIN_CLAIM
  release_scope_classes: INTERNAL_RESEARCH | BUILD_CANDIDATE | DISTRIBUTION_CANDIDATE | RELEASE
  unknown_policy_behavior: FAIL_CLOSED_UNKNOWN
```

For one exact `(origin_class, reference_class, release_scope_class, material_trigger_set)` tuple, the policy compiler emits exactly one `OriginalityEvidenceRequirementSet`:

```yaml
OriginalityEvidenceRequirementSet:
  requirement_set_id: <content-bound>
  policy_id: ORIGINALITY-RISK-v1
  policy_epoch: 1
  artifact_id: <exact>
  reference_use_id: <exact>
  release_scope_ref: <exact>
  requirements:
    exact_identity: REQUIRED | CONDITIONAL | NOT_APPLICABLE
    normalized_identity: REQUIRED | CONDITIONAL | NOT_APPLICABLE
    known_reference_comparison: REQUIRED | CONDITIONAL | NOT_APPLICABLE
    near_duplicate_checks: REQUIRED | CONDITIONAL | NOT_APPLICABLE
    targeted_external_search: REQUIRED | CONDITIONAL | NOT_APPLICABLE
    judgment_review: REQUIRED | CONDITIONAL | NOT_APPLICABLE
    qualified_legal_review: REQUIRED | CONDITIONAL | NOT_APPLICABLE
  material_triggers: []
  compiler_trace: []
```

### Deterministic v1 compilation rules

| Condition | Exact identity | Normalized identity | Known-reference comparison | Near-duplicate | Targeted external search | Judgment review | Qualified legal review |
|---|---|---|---|---|---|---|---|
| `INTERNAL_RESEARCH` with no incorporation/release trigger | `CONDITIONAL` | `CONDITIONAL` | `REQUIRED` when references exist, else `NOT_APPLICABLE` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `NOT_APPLICABLE` | `NOT_APPLICABLE` |
| `BUILD_CANDIDATE` or stronger + `PROJECT_NATIVE`/`GENERAL_CONCEPTUAL` and no material signal | `REQUIRED` | `CONDITIONAL` | `REQUIRED` when references exist | `CONDITIONAL` | `NOT_APPLICABLE` | `CONDITIONAL` | `NOT_APPLICABLE` |
| `STYLE_OR_CREATOR_NAMED` at `DISTRIBUTION_CANDIDATE` or `RELEASE` | `REQUIRED` | `REQUIRED` | `REQUIRED` | `REQUIRED` | `REQUIRED` | `REQUIRED` | `CONDITIONAL` |
| `EXPRESSION_SPECIFIC` or `DIRECT_ASSET_OR_CODE` at distribution/release | `REQUIRED` | `REQUIRED` | `REQUIRED` | `REQUIRED` where media-appropriate | `CONDITIONAL` | `REQUIRED` | `CONDITIONAL`; becomes `REQUIRED` on unresolved scope/permission interpretation |
| `MARK_LIKENESS_PERSONA` at distribution/release | `REQUIRED` | `CONDITIONAL` | `REQUIRED` | `CONDITIONAL` | `REQUIRED` | `REQUIRED` | `REQUIRED` before `CLEAR` when a legal-rights interpretation is material |
| `CONFIDENTIAL_PRIVATE_RESTRICTED` | checks do not cure restriction | checks do not cure restriction | checks do not cure restriction | checks do not cure restriction | checks do not cure restriction | checks do not cure restriction | permission/contract resolution required before broader scope |
| material signal, credible complaint, conflicting source, or unresolved permission/terms ambiguity | previous requirements remain | previous requirements remain | `REQUIRED` | media-appropriate `REQUIRED` | `REQUIRED` | `REQUIRED` | `REQUIRED` when project policy cannot resolve the legal interpretation itself |

Additional rules:

- `CONDITIONAL` MUST be compiled to either `REQUIRED` or `NOT_APPLICABLE` with a reason before assessment. Runtime ambiguity is invalid.
- Unknown origin/reference/release class, missing policy epoch, unrecognized material trigger, or missing compiler trace yields `UNKNOWN(POLICY_UNRESOLVED)` and cannot yield `CLEAR`.
- `NO_MATERIAL_SIGNAL_FOUND` is evidence only; it never changes license/permission/provider-terms requirements and never constitutes legal clearance.
- Any required evidence in `NOT_RUN`, `INCONCLUSIVE`, stale, mismatched, or missing state blocks `CLEAR`.
- Scores/thresholds may trigger stronger requirements but may not reduce them or directly derive `CLEAR`.

This policy is intentionally conservative and project-operational. It does not claim to encode legal doctrine.

## 4. Deterministic stale-evidence precedence — resolves `PG-RIGHTS-m01`

The predecessor's overlapping freshness transitions are replaced by reason-coded precedence:

```text
if independent material-risk/conflict trigger is active:
    QUARANTINED(<specific material-risk reason>)
else if any required provider/legal/license/permission evidence is stale:
    UNKNOWN(STALE_EVIDENCE)
else if evidence is missing/conflicting/out-of-scope:
    UNKNOWN(<specific reason>)
else if explicit scope restriction applies:
    RESTRICTED(<specific restriction>)
else if all compiled requirements and authority bindings are satisfied:
    CLEAR
```

Rules:

1. Staleness alone derives `UNKNOWN(STALE_EVIDENCE)`, not `QUARANTINED`.
2. A separate material-risk/conflict trigger has precedence and derives `QUARANTINED(<reason>)`; staleness is retained as an additional unresolved trigger but does not create a second competing primary state.
3. The prior `CLEAR` assessment remains immutable history with its exact evidence/policy epoch. It is never rewritten to make the stale state appear historically true.
4. Clearing requires a new assessment at a fresh exact evidence/policy epoch; changing a locator or wrapper is insufficient.

## 5. Release-gate correction

The predecessor release gate item 8 is replaced with:

> The exact `OriginalityRiskPolicy` epoch MUST compile an exact `OriginalityEvidenceRequirementSet` for the artifact/reference-use/release scope. Every `REQUIRED` item must resolve to current exact evidence with a non-`NOT_RUN`, non-`INCONCLUSIVE` outcome where applicable. Every `NOT_APPLICABLE` item must carry the compiler reason. Missing/unknown policy or an unresolved `CONDITIONAL` fails closed as `UNKNOWN(POLICY_UNRESOLVED)`.

Additionally, release assessment MUST verify exact `ReferenceUseRecord` identity and source-evidence root before using any originality result.

## 6. Negative authority cases

The following MUST fail closed and cannot derive `CLEAR`:

1. replaying one originality review under a different `ReferenceUseRecord`;
2. same candidate hash with a changed declared purpose or release scope;
3. substituting provider-terms or license/permission refs while retaining an old originality result;
4. missing or unknown `OriginalityRiskPolicy` epoch;
5. unresolved `CONDITIONAL` requirement at assessment time;
6. required near-duplicate/search/judgment/legal review recorded as `NOT_RUN` or `INCONCLUSIVE`;
7. stale required provider/legal evidence without a separate material-risk trigger — derives `UNKNOWN(STALE_EVIDENCE)`;
8. stale evidence plus an independent credible complaint/material similarity conflict — derives `QUARANTINED(<material-risk reason>)` with staleness retained secondarily;
9. a low similarity score attempting to waive a missing license, provider-contract ambiguity, or required review.

## 7. Preserved predecessor semantics

The following predecessor semantics remain unchanged and normative through exact blob import:

- provenance, provider/contract permission, originality/similarity signal, and release-sensitive rights state remain orthogonal;
- provider output allocation is not release clearance;
- provider input/data-use/training terms remain a separate admission dimension;
- unknown/restricted/quarantined material cannot silently satisfy the release gate;
- public accessibility does not imply reuse permission;
- exact provider/account/product terms epoch remains required where applicable;
- similarity scoring is escalation-only and cannot prove infringement, non-infringement, originality, or independent creation;
- protected/private evidence must remain protected rather than copied into ordinary public artifacts;
- freshness/reopen triggers remain active;
- legal/IP conclusions remain scoped and unresolved questions remain OPEN where evidence does not decide them.

## 8. Self-review and finding disposition

- `PG-RIGHTS-M01`: **RESOLVED** — exact `ReferenceUseRecord` plus cross-record identity/root validation prevents originality evidence replay across changed purpose/reuse/terms/license/release scope.
- `PG-RIGHTS-M02`: **RESOLVED** — `ORIGINALITY-RISK-v1` deterministically compiles exact evidence applicability; unknown/unmatched/unresolved policy state fails closed.
- `PG-RIGHTS-m01`: **RESOLVED** — stale evidence alone has one primary state `UNKNOWN(STALE_EVIDENCE)`; independent material-risk triggers take explicit quarantine precedence.

Self-review: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR** in Issue #114 scope.

## 9. Reopen conditions

Reopen this remediation if:

- a consumer can reuse an originality review under a materially different reference-use or release context without a new exact binding;
- policy compilation admits two different requirement sets for the same exact tuple/epoch;
- an unknown/unmatched policy state can produce `CLEAR`;
- a stale-evidence-only case can nondeterministically become either `UNKNOWN` or `QUARANTINED`;
- a similarity score can reduce required legal/license/terms evidence;
- the frozen predecessor blob cannot be resolved exactly;
- formal `W2-REV-01` identifies a new BLOCKER/MAJOR.

## 10. Authority boundary

This remediation is `EVIDENCE_REQUIRED` planning material. It does not provide legal clearance, release approval, implementation readiness, production authority, integration authority, verification authority, or canonical status. Any eventual integration to `main` is squash-only through a separately valid route.