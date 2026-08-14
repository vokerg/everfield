# W2-REV-ACC-23 — full mapping review continuation for XAG 123

**Issue:** #323  
**Mission:** `W2-REV-ACC-23`  
**Winning claim:** `5297163566`  
**Trust mode:** `DEGRADED_INDEPENDENT`  
**Review base:** `main@4421a79e5647ab53afa28f49b68b72ef630556de`  
**Current integrated policy/report:** v15 blobs `bba27a68a6922751c4b2c1ccdc3a6c164ac3a2dd` / `b46e924dff194a61993d445ad66cbee5fb79d1df`  
**Inherited XAG 108–123 origin:** `80e278315d6b7a108d89da3f5a99086a8ef91bf7`  
**Disposition:** `CHANGES_NEEDED`

## 1. Review boundary and frozen lineage

This episode resumes exactly the still-unaccepted XAG 123 remainder left by Issue #316 after the separately remediated and reviewed XAG 122 finding. It does not redo already accepted/reviewed XAG 108–122 scope and does not treat bounded clean reviews as authority outside their exact scopes.

Frozen predecessor lineage:

- Issue #316 / `W2-REV-ACC-21`: winning claim `5297013118`, terminal `5297053703`, head `ec7c3fd306649ece3968c612e01847c50bf4bc55`, work `e0304f34365cd6c6ff40a9eb61a3ef1827e66519`, `CHANGES_NEEDED`. That episode accepted all six XAG 121 atoms and found no defect in `XAG122-SUPPORT-NO-EXTRA-COST`, then terminalized at `XAG122-MULTIPLE-ACCESSIBLE-SUPPORT-METHODS`; XAG 123 remained explicitly unaccepted.
- Issue #319 / `W2-REM-ACC-16`: winning claim `5297064545`, terminal `5297097682`, head `8f56a8da6fec83e8ff8eb38780d29c4340f73691`, work `bf9e96aaa261c75f78f30cf1229e71c9581d27e1`. Its v15 packet corrected only the XAG 122 named accessible support-method set and was squash-published at `main@dd80aeee4b8dca26ab6bbe4a19444b843a01645d`.
- Issue #321 / `W2-REV-ACC-22`: winning claim `5297104041`, terminal `5297129105`, head `35798c2805c42a1195e24e53f1ec707142457790`, work `04860705ce1ce649594809fc4b291993c99e142d`, `CLEAN_FOR_NONCANONICAL_INTEGRATION` for that bounded XAG 122 remediation. Its review provenance was squash-published at the review base `main@4421a79e5647ab53afa28f49b68b72ef630556de`.

The v15 composition contract changes only XAG 122 and preserves every unrelated v14-composed semantic record. XAG 123 therefore resolves from the inherited XAG 108–123 origin unchanged by the v15 remediation overlay.

Canonical Planning Program blob remains `e3120ec203c4156328770aa86c12fbb7187966dc`; activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e` is in the review-base ancestry.

## 2. Fresh first-party source attack

Fresh Microsoft Learn XAG 123 was independently re-read on `2026-08-14`:

- `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/123`
- title: **Mental health best practices**
- XAG version represented by the repository/source lineage: `XAG-v3.2`
- page last updated: `2026-03-04`

The review distinguishes the page's implementation-guideline directives from broader approaches, examples, notes, and recommendations. Advisory/example language is not promoted into a load-bearing rejection condition merely because it appears elsewhere on the page.

The inherited XAG 123 expected set contains exactly eight atoms:

1. `XAG123-HARMFUL-CONTENT-DESCRIPTIONS`
2. `XAG123-LAUNCH-CONTENT-WARNINGS`
3. `XAG123-CONTEXTUAL-CONTENT-WARNINGS`
4. `XAG123-HARMFUL-CONTENT-CUSTOMIZATION`
5. `XAG123-SKIP-CHALLENGING-CONTENT`
6. `XAG123-MENTAL-HEALTH-RESOURCES`
7. `XAG123-WARNINGS-SETTINGS-ACCESSIBLE`
8. `XAG123-RESPECTFUL-MENTAL-HEALTH-REPRESENTATION`

All eight inherit `XAG-123`, best-practice `SHOULD` authority, conditional applicability, `ACC-EV-XAG123`, and `ACC-GAP-XAG123`. The review proceeds in that source/inventory order and terminalizes at the first reproducible material defect.

## 3. XAG 123 atoms 1–5 — no material finding

### `XAG123-HARMFUL-CONTENT-DESCRIPTIONS`

The atom requires detailed descriptions when the game contains content that may cause adverse emotional or psychological responses, including free online pre-purchase description, in-game description, and accessible online documentation. This matches the implementation guidance: detailed descriptions are required, the online form is free and available before purchase in addition to appearing in-game, and online warning/description documentation is called out as needing web accessibility. No example or advisory subclause is promoted beyond that source directive.

Result: `NO_MATERIAL_FINDING / ACCEPTED_IN_THIS_REVIEW_EPISODE`.

### `XAG123-LAUNCH-CONTENT-WARNINGS`

The atom requires a warning at game launch when the sensitive-content applicability condition is met. That is the direct implementation-guideline behavior. The mapping does not make the source examples' specific warning presentation or acknowledgement mechanics universally mandatory.

Result: `NO_MATERIAL_FINDING / ACCEPTED_IN_THIS_REVIEW_EPISODE`.

### `XAG123-CONTEXTUAL-CONTENT-WARNINGS`

The atom requires an option to enable in-game warnings before relevant areas, cutscenes, or dialogue under the corresponding sensitive-content trigger. This preserves the source's optional-player-control structure rather than requiring every warning to be permanently enabled. No material modality or condition inversion was reproduced.

Result: `NO_MATERIAL_FINDING / ACCEPTED_IN_THIS_REVIEW_EPISODE`.

### `XAG123-HARMFUL-CONTENT-CUSTOMIZATION`

The atom makes a customization option load-bearing when potentially harmful content is applicable to being lessened or removed, while keeping gore, profanity, and animal killing as covered examples rather than independent universal feature-existence requirements. The mapping remains under best-practice `SHOULD` authority and does not manufacture a legal/platform mandate. The source's broader creative-autonomy framing and `when applicable` qualifier are preserved by conditional applicability rather than erased.

Result: `NO_MATERIAL_FINDING / ACCEPTED_IN_THIS_REVIEW_EPISODE`.

### `XAG123-SKIP-CHALLENGING-CONTENT`

The atom requires an option to skip cutscenes or missions containing psychologically or emotionally challenging content. It does not promote the broader approach section's ideal of mid-event bypass timing into a separate mandatory semantic. That keeps the atom aligned with the implementation directive.

Result: `NO_MATERIAL_FINDING / ACCEPTED_IN_THIS_REVIEW_EPISODE`.

## 4. XAG 123 atom 6 — material finding

### W2-REV-ACC23-M01 — MAJOR

**Class:** `RESOURCE_LOCALIZATION_ADVISORY_PROMOTION`  
**Affected atom:** `XAG123-MENTAL-HEALTH-RESOURCES`

The current inherited atom resolves to the following load-bearing shape:

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

Current first-party XAG 123 implementation guidance makes **in-game support/learning resources** the load-bearing directive. The implementation bullet explains that such resources can include regional helplines, mental-health websites, and similar resources. Separately, the broader approaches section advises developers to consider locale- or region-specific resources.

Those two source layers are not equivalent:

- `in_game_resources_for_support_or_learning_more_available: true` is faithful to the implementation directive;
- `resources_localized_or_region_appropriate_when_applicable: true` promotes an advisory/example-level source consideration into a second required semantic.

That promotion is mechanically material because it can reject a source-faithful implementation solely for lacking locale/region specialization.

### Reproducible adversarial witness

```yaml
candidate:
  finding_trigger_applies: true
  in_game_resources_for_support_or_learning_more_available: true
  resources:
    - globally_accessible_mental_health_information_site
    - globally_accessible_support_information
  resources_localized_or_region_appropriate: false
current_mapping_result: REJECT_CAPABLE
source_faithful_result: PASS_FOR_THIS_ATOM
```

The candidate supplies the source-required in-game support/learning resources but no locale-specific variant. Current first-party implementation guidance does not make region specificity a mandatory condition; therefore the inherited required semantic creates a false-negative path.

A converse witness remains correctly rejectable:

```yaml
candidate:
  finding_trigger_applies: true
  in_game_resources_for_support_or_learning_more_available: false
source_faithful_result: REJECT
```

The correction must not weaken the actual in-game-resource requirement while removing only the advisory promotion.

### Minimum coherent correction boundary

A bounded remediation must:

- preserve identity `XAG123-MENTAL-HEALTH-RESOURCES`;
- preserve source id `XAG-123`, best-practice `SHOULD` authority, conditional applicability, trigger, `ACC-EV-XAG123`, and `ACC-GAP-XAG123`;
- keep suitable in-game support/learning resources load-bearing;
- remove locale/region specificity from `required_semantics`;
- if locale/region guidance is retained, encode it only as advisory/recommended/example metadata that cannot independently fail a candidate;
- avoid hard-coding live helpline identities or creating a legal/compliance/platform claim;
- preserve all already accepted/reviewed XAG 108–122 lineage and the first five XAG 123 atoms reviewed without a material finding here;
- preserve exact inventory identities/counts and fail-closed aggregate state.

Bounded remediation successor: **Issue #324 / `W2-REM-ACC-17`**.

## 5. Early-negative boundary

Per the required-review lifecycle, this episode terminalizes at the first reproducible material defect. Therefore:

- XAG 123 atoms 1–5: `ACCEPTED_NO_MATERIAL_FINDING` in this episode.
- `XAG123-MENTAL-HEALTH-RESOURCES`: **MAJOR finding `W2-REV-ACC23-M01`**.
- `XAG123-WARNINGS-SETTINGS-ACCESSIBLE`: **NOT REVIEWED TO ACCEPTANCE / REMAINS UNACCEPTED**.
- `XAG123-RESPECTFUL-MENTAL-HEALTH-REPRESENTATION`: **NOT REVIEWED TO ACCEPTANCE / REMAINS UNACCEPTED**.

The source was read through the later bullets to establish the page boundary and preserve review context, but no statement in this packet may be used to infer acceptance of atoms 7–8 after the early-negative terminal point.

## 6. Inventory, preservation, and fail-closed checks

The review mutates no integrated mapping. Current expected inventory remains:

- XAG 112: `14` atomic records;
- XAG 114: `16` atomic records;
- XAG 108–123: `113` atomic records;
- inherited XAG 101–107: `105` atomic records;
- composed XAG 101–123: `218` atomic records.

Preservation authority remains exact and bounded for reviewed corrections through XAG 122, including:

- XAG 112 navigation corrections;
- XAG 114 `titles` reading-level exception;
- XAG 115 stored-data logical-operator correction;
- XAG 115 permanent-action conjunction correction and preserved button-hold surface;
- XAG 116 timing correction;
- XAG 117 camera-view `BEST_PRACTICE_REQUIRED_IF_APPLICABLE / SHOULD` correction;
- XAG 120 notification example-semantics correction;
- all six XAG 121 atoms accepted by Issue #316;
- XAG 122 no-extra-cost atom;
- XAG 122 named accessible support-method remediation cleanly reviewed by Issue #321.

No atom/source/evidence/gap identity drift was introduced by this review. XAG 123 continues to route through `ACC-EV-XAG123` / `ACC-GAP-XAG123` and remains fail-closed pending correction and later review continuation.

Fail-closed authority state remains:

```yaml
empirical_accessibility_evidence: NOT_RUN
empirical_accessibility_successor_eligible: false
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
full_corrected_xag_108_123_review_complete: false
xag_123_review_complete: false
production_implementation_ready: false
legal_compliance_claimed: false
platform_certification_claimed: false
verification_pass_authority: false
decision_authority: false
integration_authority_by_review_alone: false
canonicality: NOT_CANONICAL
```

Because the completed corrected XAG 108–123 mapping review is not clean, an empirical-accessibility evidence successor is **not eligible**.

## 7. Review disposition

```yaml
disposition: CHANGES_NEEDED
findings:
  blockers: 0
  majors: 1
  correction_requiring_minors: 0
material_findings:
  - id: W2-REV-ACC23-M01
    severity: MAJOR
    class: RESOURCE_LOCALIZATION_ADVISORY_PROMOTION
    affected_atom: XAG123-MENTAL-HEALTH-RESOURCES
xag_123_atoms_1_5: ACCEPTED_NO_MATERIAL_FINDING
xag_123_resource_atom: EARLY_NEGATIVE
xag_123_final_two_atoms: UNACCEPTED_NOT_REVIEWED_TO_COMPLETION
bounded_remediation_successor: 324
empirical_accessibility_successor_eligible: false
mapping_complete: false
```

Route exactly Issue #324 for the minimum coherent correction. After that correction receives its own fresh required scoped review and any separately authorized noncanonical integration, the full mapping review must resume from the still-unaccepted final two XAG 123 atoms before empirical accessibility evidence can be derived.
