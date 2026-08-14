# W2-REM-ACC-17 — correct XAG 123 resource-localization advisory promotion

**Mission:** `W2-REM-ACC-17` / Issue #324  
**Winning claim:** comment `5297219148`  
**Claim base:** `main@4421a79e5647ab53afa28f49b68b72ef630556de`  
**Required full-review continuation:** Issue #323 winning claim `5297163566`, terminal `CHANGES_NEEDED` comment `5297205043`, review head `0ed9caf6e73ad15c741f20b740645a6a4ccc2e60`, work `47efe2cf9bcaa5e448910ffc59714494d5e8e1f9`  
**Finding:** `W2-REV-ACC23-M01` / MAJOR — `RESOURCE_LOCALIZATION_ADVISORY_PROMOTION`  
**Immutable producer input:** policy v15 blob `bba27a68a6922751c4b2c1ccdc3a6c164ac3a2dd`, report v15 blob `b46e924dff194a61993d445ad66cbee5fb79d1df`  
**Authority:** bounded noncanonical remediation only; fresh independent/degraded-independent scoped review remains mandatory.

## 1. Scope and source binding

Issue #323 resumed the still-unaccepted XAG 123 mapping remainder after the XAG 122 correction/review chain. It accepted the first five XAG 123 atoms with no material finding, then terminalized early on `XAG123-MENTAL-HEALTH-RESOURCES`. The final two XAG 123 atoms therefore remain explicitly unaccepted.

Fresh first-party Microsoft XAG 123 was re-read on `2026-08-14`:

- `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/123`
- Xbox Accessibility Guidelines v3.2 lineage; page last updated `2026-03-04`.

The implementation guidance requires in-game resources that support players with mental-health conditions or help them learn more about mental health. Regional helplines, mental-health websites, and similar resources are examples of what those resources can include. Separately, the broader approaches section tells developers to consider locale- or region-specific resources.

The parent XAG corpus remains accessibility best-practice guidance rather than a legal/compliance-validation checklist. This correction therefore retains repository-native `BEST_PRACTICE_REQUIRED_IF_APPLICABLE / SHOULD` authority and does not introduce `MUST`, certification, or legal authority.

## 2. Exact inherited defect

The exact inherited atom reviewed by Issue #323 is:

```yaml
XAG123-MENTAL-HEALTH-RESOURCES:
  source_id: XAG-123
  authority_class: BEST_PRACTICE_REQUIRED_IF_APPLICABLE
  source_modality: SHOULD
  applicability: CONDITIONAL
  trigger: game_contains_content_related_to_mental_health_self_harm_suicide_eating_disorders_addiction_or_other_serious_psychological_risk
  required_semantics:
    in_game_resources_for_support_or_learning_more_available: true
    resources_localized_or_region_appropriate_when_applicable: true
  evidence_requirement_refs:
    - ACC-EV-XAG123
  gap_ref: ACC-GAP-XAG123
```

The identity, source, best-practice authority, `SHOULD` modality, conditional applicability, trigger, evidence route, and gap route are not the finding. The defect is the second load-bearing required semantic. It promotes advisory/example-level locale/region guidance into a rejection condition.

That promotion creates the material false-negative path reproduced by Issue #323: an applicable candidate can provide suitable in-game support/learning resources and still fail solely because the resources are not locale-specific.

## 3. Bounded v16 correction

The v16 overlay changes only the resource atom's required semantic set:

```yaml
XAG123-MENTAL-HEALTH-RESOURCES:
  source_id: XAG-123
  authority_class: BEST_PRACTICE_REQUIRED_IF_APPLICABLE
  source_modality: SHOULD
  applicability: CONDITIONAL
  trigger: game_contains_content_related_to_mental_health_self_harm_suicide_eating_disorders_addiction_or_other_serious_psychological_risk
  required_semantics:
    in_game_resources_for_support_or_learning_more_available: true
  evidence_requirement_refs:
    - ACC-EV-XAG123
  gap_ref: ACC-GAP-XAG123
```

Suitable in-game resources remain mandatory under the mapped best-practice `SHOULD` when the atom applies. Locale/region specificity is no longer load-bearing and cannot independently fail a candidate. The packet records that context only in source-fidelity metadata; it does not pin live helpline identities or require any particular regional service.

No other XAG 123 atom is redefined.

## 4. Load-bearing mechanical oracles

`ACCESSIBILITY-POLICY-VALIDATOR-v16` establishes the required boundary:

| Candidate / mutation | Expected |
| --- | --- |
| applicable game provides suitable in-game support/learning resources; resources are not locale-specific | `PASS` |
| applicable game provides suitable in-game support/learning resources and region-specific resources | `PASS` |
| applicable game provides no in-game support/learning resources | `REJECT_REQUIRED_IN_GAME_RESOURCES_MISSING` |
| locale/region specificity is reintroduced into `required_semantics` | `REJECT_ADVISORY_PROMOTION` |
| source authority is inflated to `MUST` / compliance | `REJECT_AUTHORITY_INFLATION` |
| atom/source/trigger/evidence/gap identity changes | `REJECT_SCOPE_LEAKAGE` |
| live helpline identity is pinned into the policy | `REJECT_SCOPE_AND_FRESHNESS_ERROR` |

Additional adversarial assertions reject mutation of any XAG 123 atom already accepted by Issue #323, either final unaccepted XAG 123 atom, any reviewed XAG 122 record, any earlier reviewed correction, or any unrelated v15-composed record.

## 5. Preservation proof

The v16 overlay consumes exact v15 as immutable input and replaces only the one material semantic identified by Issue #323, plus minimum audit/validator/report metadata needed to make the correction mechanically testable.

Preserved reviewed lineage includes:

- XAG 112 navigation corrections;
- XAG 114 `titles` reading-level exception;
- XAG 115 stored-data `(review AND correct) OR complete reverse/cancel` operator;
- XAG 115 permanent/destructive-action `review AND confirmation AND undo` conjunction;
- XAG 115 no-button-hold record;
- XAG 116 reviewed timing correction;
- XAG 117 camera-view required-if-applicable / `SHOULD` correction;
- XAG 120 notification-management accessibility without example-feature existence inflation;
- all six XAG 121 records accepted by Issue #316;
- XAG 122 no-extra-cost atom and the named accessible support-method set resolved/reviewed by Issue #321;
- XAG 123 atoms 1–5 accepted with no material finding by Issue #323.

Issue #323's early-negative boundary is also preserved:

- `XAG123-MENTAL-HEALTH-RESOURCES`: corrected here, pending fresh scoped review;
- `XAG123-WARNINGS-SETTINGS-ACCESSIBLE`: `UNACCEPTED_NOT_REVIEWED_TO_COMPLETION`;
- `XAG123-RESPECTFUL-MENTAL-HEALTH-REPRESENTATION`: `UNACCEPTED_NOT_REVIEWED_TO_COMPLETION`.

Inventory remains unchanged:

- XAG 112: **14** atomic records;
- XAG 114: **16** atomic records;
- XAG 108–123: **113** atomic records;
- inherited XAG 101–107: **105** atomic records;
- composed XAG 101–123: **218** atomic records.

No identity is added, removed, split, or renamed.

## 6. Finding disposition and producer self-review

`W2-REV-ACC23-M01` is **RESOLVED_PENDING_FRESH_SCOPED_REVIEW** in this producer packet:

- suitable in-game support/learning resources remain load-bearing: **YES**;
- nonlocalized but otherwise suitable in-game resources can pass: **YES**;
- region-specific resources can still be provided: **YES**;
- locale/region specificity can independently fail a candidate: **NO**;
- live helpline identity is pinned: **NO**;
- atom identity/source/authority/modality/applicability/trigger changed: **NO**;
- evidence or gap route changed: **NO**;
- XAG 108–122 reviewed lineage changed: **NO**;
- XAG 123 atoms 1–5 accepted scope changed: **NO**;
- XAG 123 final two atoms accepted or redefined: **NO**;
- atomic counts changed: **NO**;
- `MUST`, legal/compliance, or platform-certification authority invented: **NO**;
- empirical accessibility eligibility or PASS claimed: **NO**.

Bounded producer self-review finds **0 unresolved BLOCKER / 0 unresolved MAJOR / 0 correction-requiring MINOR** in this exact remediation scope. Producer self-review does not satisfy the mandatory fresh independent/degraded-independent scoped review.

## 7. Preserved fail-closed state

```yaml
empirical_accessibility_evidence: NOT_RUN
empirical_accessibility_successor_eligible: false
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
full_xag_108_123_review_complete: false
xag_121_review: ACCEPTED_NO_MATERIAL_FINDING_BY_ISSUE_316
xag_122_review: RESOLVED_BOUNDED_REVIEWED_BY_ISSUE_321
xag_123_atoms_1_5: ACCEPTED_NO_MATERIAL_FINDING_BY_ISSUE_323
xag123_resource_finding: RESOLVED_PENDING_FRESH_SCOPED_REVIEW
xag123_final_two_atoms: UNACCEPTED_NOT_REVIEWED_TO_COMPLETION
production_implementation_ready: false
legal_compliance_claimed: false
platform_certification_claimed: false
verification_pass_authority: false
integration_authorized: false
canonicality: NOT_CANONICAL
```

This bounded repair does not accept the final two XAG 123 atoms, complete the corrected XAG 108–123 review, make empirical accessibility evidence eligible, clear aggregate blockers, create readiness/implementation/release authority, or grant verification, integration, decision, or canonical authority.

## 8. Required next transition

Freeze this exact remediation in an exact-head draft PR and perform a fresh independent/degraded-independent scoped review. That review must independently re-read current XAG 123, verify nonlocalized suitable resources pass while missing in-game resources fail, attack advisory promotion and authority inflation, prove atom/trigger/evidence/gap and all reviewed-lineage preservation, and verify inventory/fail-closed invariants.

A clean scoped review may make this exact producer packet eligible only for the separately authorized squash-only noncanonical integration route. After the bounded correction and its scoped review are published as authorized, the required full mapping review must resume from the two still-unaccepted XAG 123 atoms before any empirical-accessibility successor can be derived.