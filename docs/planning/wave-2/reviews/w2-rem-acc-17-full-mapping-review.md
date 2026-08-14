# W2-REV-ACC-17 — required full-review continuation of XAG 115–123

**Mission:** `W2-REV-ACC-17` / Issue #302  
**Task class:** required full-review continuation  
**Trust mode:** `DEGRADED_INDEPENDENT` — fresh actor/session distinct from Issue #296 production and Issue #299 scoped review, while repository writes use the shared GitHub principal.  
**Disposition:** `CHANGES_NEEDED`  
**Terminal boundary:** early-negative at XAG 117 after one reproducible MAJOR source-modality defect. XAG 118–123 remain unaccepted by this episode.  
**Authority:** noncanonical review provenance only; no empirical accessibility PASS, mapping completion, readiness, implementation, release, legal/compliance, platform certification, verification-PASS, integration, decision, or canonical authority.

## 1. Frozen reviewed identity

The review froze the following exact identities before judgment:

- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- review base/current main at claim: `8818f2ac6abb405513a787d0278670883b44df2d`;
- current integrated policy v12 blob: `4c10dc8969a8080a14e8f46e0d2e126bd8a1ee5e`;
- current integrated report v12 blob: `197a20ec3fd3cd859c4e7d96e51f7337ea7583d3`;
- inherited XAG 108–123 origin policy blob: `80e278315d6b7a108d89da3f5a99086a8ef91bf7`;
- Issue #293 required-review claim `5294404386`, terminal `5294463445`, review head `dd4ec050025d4321d9e2a0b73b0ecbc6fdc920e3`, work `247e785b20f0cdad7e78d9501e86e7450432bf3e`, disposition `CHANGES_NEEDED`;
- Issue #296 terminal producer `5294539803`, head `c356b46399e054f478dd7e7865ab108b1d1c5444`, work `a4583455d12dd922166c40b5709b3c043b0ac86a`, integrated as squash `8818f2ac6abb405513a787d0278670883b44df2d` with integration status `5296647427`;
- Issue #299 required scoped-review terminal `5296631121`, head `373ace2cca0b271f9709bf6e28062e892cf574bf`, work `5e847c527526715479ee6b66862bb76388a628b8`, disposition `CLEAN_FOR_NONCANONICAL_INTEGRATION`.

Issue #299 review PR #301 was non-mergeable at this review's claim. That review-provenance integration is not a prerequisite for validity of its terminal exact-identity review result; the frozen PR was not rebased or mutated.

## 2. Review scope and source freshness

Issue #293 terminated early on the XAG 115 permanent/destructive-action conjunction defect. Issue #296 corrected that defect and Issue #299 independently reviewed the exact correction cleanly. This episode therefore resumed only the still-unaccepted remainder: the separate XAG 115 no-button-hold surface and XAG 116–123, while treating prior bounded corrections as immutable preservation inputs.

Fresh first-party Microsoft Learn source was re-read on `2026-08-14`. The relevant pages used before the terminal finding report last update `2026-03-04` and XAG v3.2 lineage:

- XAG 115: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/115`
- XAG 116: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/116`
- XAG 117: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117`

The review stopped after the first reproducible material defect at XAG 117, as allowed by the required-review contract. No acceptance is claimed for XAG 118–123.

## 3. XAG 115 remainder — no new finding before continuation

The current first-party XAG 115 implementation guidance separately states that destructive-action confirmation should not require button holds and should provide alternatives to button holds. The inherited exact atom is:

`XAG115-NO-BUTTON-HOLD-DESTRUCTIVE-CONFIRMATION`

with:

- `source_id: XAG-115`;
- `authority_class: BEST_PRACTICE_REQUIRED_IF_APPLICABLE`;
- `source_modality: SHOULD`;
- conditional trigger `permanent_or_destructive_action_requires_confirmation`;
- required semantics `button_hold_not_required_as_only_confirmation_method: true` and `non_hold_alternative_available: true`;
- evidence `ACC-EV-XAG115` and gap `ACC-GAP-XAG115`.

That bounded atom matches the separate current source surface. The v12 overlay explicitly preserves it byte-logically from the reviewed lineage. No new material finding was established in the XAG 115 button-hold remainder.

The two previously reviewed XAG 115 corrections remain preservation inputs only:

- stored-data protection: `(review AND correct) OR complete_reverse_or_cancel`;
- permanent/destructive-action protection: `review AND confirmation AND undo`.

## 4. XAG 116 — no new finding before continuation

Fresh XAG 116 source recheck preserved the non-core-gameplay scope and the load-bearing modification alternatives:

- request longer/no session limit before start;
- adjust before encounter to at least `10×` the default;
- warning plus at least `20` seconds for a simple extension action and at least `10` extensions;
- turn the time limit off;
- for important-element duration, either adjust to at least `10×` or disable duration and dismiss/advance on input.

The source exception surface includes real-time events with no alternative, essential task timing, and default limits exceeding 20 hours, while core-gameplay timing is outside XAG 116. The reviewed v7 correction preserves these semantics on the duration-modification records and preserves the other XAG 116 atoms. No new reproducible material defect was established before advancing to XAG 117.

This paragraph is not a new global acceptance of XAG 116 beyond the exact attack performed here; it records only that no earlier terminal defect was found in the required continuation order.

## 5. XAG 117 source reconstruction through the terminal boundary

Fresh first-party XAG 117 implementation guidance includes, in order relevant here:

1. controls for auto-updating content on UI screens with text, including update-frequency control and pause/stop/hide;
2. controls for moving/blinking/scrolling/flashing content on UI screens with text, including disable plus pause/hide, with ancillary gameplay around text UI excluded;
3. avoid camera shake/bobbing/motion blur/etc. **or** provide an option to turn those behaviors off;
4. avoid repetitive side-to-side/up-down movement except core gameplay;
5. provide adjustable field-of-view settings;
6. provide camera-movement settings including horizontal/vertical sensitivity and disabling automatic camera movement;
7. **allow players to choose between first- and third-person camera views.**

The first six current inherited XAG 117 atoms are represented as `BEST_PRACTICE_REQUIRED_IF_APPLICABLE` / `SHOULD` conditional records, consistent with the source-strength pattern used by this policy lineage. The seventh atom diverges materially.

## 6. Finding `W2-REV-ACC17-M01` — XAG 117 camera-view source-modality weakening

**Severity:** MAJOR  
**Class:** `SOURCE_MODALITY_WEAKENING_AND_ACCEPTANCE_AUTHORITY_DRIFT`  
**Affected atom:** `XAG117-CAMERA-VIEW-CHOICE`

### Current first-party source

Under XAG 117 **Implementation guidelines**, Microsoft gives the unqualified directive:

> Allow players to choose between 1st and 3rd person camera views.

It is presented at the same implementation-guideline level as the immediately preceding directives to provide adjustable field of view and camera movement settings. It is not introduced by `consider`, `ideally`, an example-only qualifier, or other advisory language.

### Current preserved mapping

The exact inherited origin policy maps the atom as:

```yaml
XAG117-CAMERA-VIEW-CHOICE:
  source_id: XAG-117
  authority_class: BEST_PRACTICE_RECOMMENDED_IF_APPLICABLE
  source_modality: CONSIDER
  applicability: CONDITIONAL
  trigger: game_supports_first_person_or_third_person_camera_presentation
  required_semantics:
    first_person_and_third_person_view_choice_available: true
  evidence_requirement_refs:
    - ACC-EV-XAG117
  gap_ref: ACC-GAP-XAG117
```

The v7, v8/v9, v10, v11, and v12 bounded overlays do not redefine this XAG 117 atom; v12 expressly preserves every unrelated composed record from its predecessor lineage. Therefore this advisory classification remains the effective current mapping at exact integrated v12.

### Why this is material

`CONSIDER` / `BEST_PRACTICE_RECOMMENDED_IF_APPLICABLE` is weaker than the source's unqualified implementation directive. A consumer of the machine-readable policy can treat the camera-view choice as merely optional advisory material rather than an applicable XAG 117 acceptance expectation while still claiming the source clause is faithfully mapped. That is source-modality weakening and can permit false-positive mapping acceptance.

The atom's semantic payload itself requires the view choice when evaluated, so the defect is specifically the authority/modality classification and any validator/oracle that permits that weakened classification to pass. The correction should not rename/split the atom or invent a stronger trigger; it should restore source-faithful authority/modality and mechanically reject regression to advisory classification.

### Required bounded remediation

Route exactly one remediation successor that:

1. consumes exact current v12 lineage as immutable input;
2. changes only `XAG117-CAMERA-VIEW-CHOICE` authority/modality metadata plus the minimum validator/report metadata needed for a load-bearing source-modality oracle;
3. preserves the atom identity, conditional applicability, trigger, semantic requirement, evidence/gap routing, all other XAG 101–123 records, all reviewed XAG 112/114/115/116 corrections, and inventory counts;
4. adds an adversarial fixture that rejects `CONSIDER` / recommended-only classification for this source directive;
5. keeps empirical accessibility `NOT_RUN`, `mapping_complete: false`, `IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN`, `W2-REV-M02: OPEN_BOUNDED`, and all higher authority false/absent;
6. requires one fresh independent/degraded-independent scoped review of the exact remediation before any integration eligibility.

## 7. Inventory, evidence, and authority boundary

No identity add/remove/split/rename is implied by this finding. The current declared corrected lineage remains:

- XAG 112 = `14`;
- XAG 114 = `16`;
- XAG 108–123 = `113`;
- inherited XAG 101–107 = `105`;
- composed XAG 101–123 = `218`.

Fail-closed state remains unchanged:

```yaml
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
full_xag_108_123_review_complete: false
production_implementation_ready: false
legal_compliance_claimed: false
platform_certification_claimed: false
verification_pass_authority: false
canonicality: NOT_CANONICAL
```

## 8. Disposition

**`CHANGES_NEEDED`**.

Finding `W2-REV-ACC17-M01` is one reproducible MAJOR defect. Because a clean full-review disposition is no longer possible, this episode terminalizes at the XAG 117 camera-view modality boundary. XAG 118–123 remain unaccepted and must be resumed only after the bounded remediation receives its mandatory fresh scoped review.

No empirical-accessibility successor is eligible. No mapping-complete, readiness, implementation, release, legal/platform, verification-PASS, integration, decision, or canonical authority is created by this review.