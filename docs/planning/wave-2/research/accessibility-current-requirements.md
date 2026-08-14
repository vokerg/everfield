# W2-REM-ACC-14 — restore XAG 117 camera-view source modality

**Mission:** `W2-REM-ACC-14` / Issue #303  
**Winning claim:** comment `5296717456`  
**Claim base:** `main@7631dee0a166c91e383a8c2e7bd641b46e6b9821`  
**Required full-review continuation:** Issue #302 winning claim `5296669009`, terminal `CHANGES_NEEDED` comment `5296708193`, review head `6327b6b6708f5159b20e37ffe5b348963bd5d8bb`, work `1e33561de0e2afa76836910cd947b06934c0cfd4`  
**Finding:** `W2-REV-ACC17-M01` / MAJOR — `SOURCE_MODALITY_WEAKENING_AND_ACCEPTANCE_AUTHORITY_DRIFT`  
**Immutable producer input:** policy v12 blob `4c10dc8969a8080a14e8f46e0d2e126bd8a1ee5e`, report v12 blob `197a20ec3fd3cd859c4e7d96e51f7337ea7583d3`  
**Authority:** bounded noncanonical remediation only; fresh independent/degraded-independent scoped review remains mandatory.

## 1. Scope and source binding

Issue #302 resumed the still-unaccepted XAG 115 button-hold and XAG 116–123 mapping remainder. It established no new material finding in the XAG 115 button-hold or XAG 116 attack, then terminated early on the first reproducible material defect at XAG 117. XAG 118–123 therefore remain unaccepted by that episode.

Fresh first-party Microsoft XAG 117 was re-read on `2026-08-14`:

- `https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/117`
- XAG v3.2 lineage; page last updated `2026-03-04`.

Within **Implementation guidelines**, the camera-view choice appears as an unqualified directive to allow player choice between first-person and third-person camera views. It is not introduced by `consider`, `ideally`, or example-only language. The XAG collection itself remains accessibility best-practice guidance rather than a legal/compliance standard, so the source-faithful repository-native representation is the same best-practice `SHOULD` / required-if-applicable strength used for the sibling unqualified XAG 117 directives—not `MUST` or compliance authority.

## 2. Exact inherited defect

The exact XAG 108–123 origin policy blob `80e278315d6b7a108d89da3f5a99086a8ef91bf7` contains:

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

The semantic payload and conditional applicability boundary are not the finding. The defect is only the advisory downgrade: `BEST_PRACTICE_RECOMMENDED_IF_APPLICABLE` / `CONSIDER` weakens the current unqualified implementation guideline and can let a consumer treat an applicable mapped expectation as optional while still claiming source-faithful mapping.

## 3. Bounded v13 correction

The v13 overlay changes exactly two fields on that existing atom:

```yaml
XAG117-CAMERA-VIEW-CHOICE:
  source_id: XAG-117
  authority_class: BEST_PRACTICE_REQUIRED_IF_APPLICABLE
  source_modality: SHOULD
  applicability: CONDITIONAL
  trigger: game_supports_first_person_or_third_person_camera_presentation
  required_semantics:
    first_person_and_third_person_view_choice_available: true
  evidence_requirement_refs:
    - ACC-EV-XAG117
  gap_ref: ACC-GAP-XAG117
```

Preserved unchanged:

- atom identity `XAG117-CAMERA-VIEW-CHOICE`;
- source id `XAG-117`;
- `CONDITIONAL` applicability;
- trigger `game_supports_first_person_or_third_person_camera_presentation`;
- semantic payload `first_person_and_third_person_view_choice_available: true`;
- evidence requirement `ACC-EV-XAG117`;
- gap route `ACC-GAP-XAG117`.

The correction does **not** broaden the trigger into a requirement that every game introduce both camera paradigms. It preserves the inherited applicability boundary and only restores the source strength when that mapped condition applies.

## 4. Load-bearing mechanical oracles

`ACCESSIBILITY-POLICY-VALIDATOR-v13` makes the modality correction mechanically load-bearing:

| Candidate | Expected |
| --- | --- |
| `BEST_PRACTICE_REQUIRED_IF_APPLICABLE` + `SHOULD` | `PASS` |
| recommended-if-applicable + `CONSIDER` | `REJECT_SOURCE_MODALITY_WEAKENING` |
| required-if-applicable + `CONSIDER` | `REJECT_SOURCE_MODALITY_WEAKENING` |
| recommended-if-applicable + `SHOULD` | `REJECT_ACCEPTANCE_AUTHORITY_DRIFT` |
| compliance/`MUST` inflation | `REJECT_AUTHORITY_INFLATION` |

Additional adversarial assertions reject identity, trigger, applicability, semantic-payload, evidence/gap, or unrelated-record mutation. The validator therefore closes the exact review finding without laundering it into either advisory-only mapping or invented mandatory/compliance authority.

## 5. Preservation proof

The v13 overlay consumes exact v12 as immutable input. It preserves all reviewed correction lineage:

- XAG 112 scaled/zoomed-map non-scrolling alternative navigation, universal submenu return coverage, and same-input focus escape;
- XAG 114 `titles` reading-level exception;
- XAG 115 stored-data protection operator `(review AND correct) OR complete reverse/cancel`;
- XAG 115 permanent/destructive-action conjunction `review AND confirmation AND undo`;
- XAG 115 no-button-hold destructive-confirmation record;
- XAG 116 default-over-20-hours exception and reviewed timing semantics.

Inventory is unchanged:

- XAG 112: **14** atomic records;
- XAG 114: **16** atomic records;
- XAG 108–123: **113** atomic records;
- inherited XAG 101–107: **105** atomic records;
- composed XAG 101–123: **218** atomic records.

No identity is added, removed, split, or renamed. No sibling XAG 117 atom and no unrelated v12-composed record is redefined.

## 6. Finding disposition and producer self-review

`W2-REV-ACC17-M01` is **RESOLVED_PENDING_FRESH_SCOPED_REVIEW** in this producer packet:

- camera-view authority restored to required-if-applicable best-practice strength: **YES**;
- source modality restored from `CONSIDER` to `SHOULD`: **YES**;
- identity changed: **NO**;
- source id changed: **NO**;
- applicability or trigger broadened: **NO**;
- semantic payload changed: **NO**;
- evidence or gap route changed: **NO**;
- unrelated XAG 117 or other v12 record changed: **NO**;
- reviewed XAG 112/XAG 114/XAG 115/XAG 116 corrections changed: **NO**;
- atomic counts changed: **NO**;
- `MUST`, legal/compliance, or platform-certification authority invented: **NO**;
- empirical accessibility PASS claimed: **NO**;
- full corrected XAG 108–123 review claimed complete: **NO**.

Bounded producer self-review finds **0 unresolved BLOCKER / 0 unresolved MAJOR / 0 correction-requiring MINOR** in this exact remediation scope. Producer self-review does not satisfy the mandatory fresh independent/degraded-independent scoped review.

## 7. Preserved fail-closed state

```yaml
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
full_xag_108_123_review_complete: false
xag_118_123_accepted_by_issue_302: false
production_implementation_ready: false
legal_compliance_claimed: false
platform_certification_claimed: false
verification_pass_authority: false
integration_authorized: false
canonicality: NOT_CANONICAL
```

Issue #302's early-negative boundary remains controlling. This bounded repair does not accept XAG 118–123, make empirical accessibility evidence work eligible, clear the aggregate blocker, create readiness/implementation/release authority, or grant verification, integration, decision, or canonical authority.

## 8. Required next transition

Freeze this exact remediation in an exact-head draft PR and perform a fresh independent/degraded-independent scoped review. The review must independently re-read current XAG 117, verify the `SHOULD`/required-if-applicable correction, attack advisory regression and authority inflation, prove identity/trigger/semantic/evidence/gap preservation, and verify all inventory/fail-closed invariants.

A clean scoped review may make this exact producer packet eligible only for the separately authorized squash-only noncanonical integration route. After the bounded correction chain is integrated as authorized, the required full mapping review must resume from the still-unaccepted XAG 118–123 remainder before any empirical-accessibility successor can be derived.
