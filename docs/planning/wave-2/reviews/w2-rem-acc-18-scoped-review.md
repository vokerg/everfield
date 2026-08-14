# W2-REV-ACC-18 — scoped review of XAG 117 camera-view modality remediation

**Mission:** `W2-REV-ACC-18` / Issue #306  
**Reviewer claim:** `5296759413`  
**Trust mode:** `DEGRADED_INDEPENDENT`  
**Review base:** `main@e167931debe6e6fd0bdfc497cb7058644ea5d5d4`  
**Producer:** Issue #303 / `W2-REM-ACC-14`  
**Producer terminal:** comment `5296754811`  
**Producer head:** `09f4f3eee194b7ffa57b668db63421c8397a15b5`  
**Producer work:** `edd2de28df9c246066dd9db5e6b436d635157ef4`  
**Producer PR:** #305  
**Candidate policy v13 blob:** `3dcdaa400ffd43cea390c331f5b4f8ea62750a5c`  
**Candidate report v13 blob:** `e5f1f491a91499bef96861d2878e4fb5552a207b`  
**Immutable input policy v12 blob:** `4c10dc8969a8080a14e8f46e0d2e126bd8a1ee5e`  
**Immutable input report v12 blob:** `197a20ec3fd3cd859c4e7d96e51f7337ea7583d3`  
**Finding under review:** `W2-REV-ACC17-M01 / SOURCE_MODALITY_WEAKENING_AND_ACCEPTANCE_AUTHORITY_DRIFT / MAJOR`

## Disposition

`CLEAN_FOR_NONCANONICAL_INTEGRATION`

Scoped findings: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR**.

This disposition is limited to the exact bounded XAG 117 camera-view authority/modality remediation. It does not accept XAG 118–123, does not complete the full XAG 108–123 review, does not make empirical accessibility work eligible, and does not create readiness, implementation, release, legal/compliance, platform-certification, verification-PASS, integration-by-review, decision, or canonical authority.

## 1. Frozen identity and compatibility attack

The exact producer packet is frozen at Issue #303 terminal comment `5296754811`:

- producer head `09f4f3eee194b7ffa57b668db63421c8397a15b5`;
- producer work `edd2de28df9c246066dd9db5e6b436d635157ef4`;
- policy v13 blob `3dcdaa400ffd43cea390c331f5b4f8ea62750a5c`;
- report v13 blob `e5f1f491a91499bef96861d2878e4fb5552a207b`;
- handoff blob `2a4ddfc91bb5c198f554fcdb2bea17c370ab27f2`;
- draft PR #305 at the exact producer head.

GitHub reports PR #305 against current `main@e167931debe6e6fd0bdfc497cb7058644ea5d5d4` as mergeable. Exact compare from current main to producer head is diverged only because the producer forked at prior `main@7631dee0a166c91e383a8c2e7bd641b46e6b9821`; current main subsequently added Issue #302 negative-review provenance. The producer packet changes exactly the declared three files:

1. `docs/planning/wave-2/research/accessibility-requirements-policy.yaml`;
2. `docs/planning/wave-2/research/accessibility-current-requirements.md`;
3. `docs/planning/handoffs/issue-303.md`.

Current-main policy/report blobs remain exactly the producer's immutable v12 inputs, so the intervening review-provenance integration does not alter the semantic composition base.

## 2. Independent first-party source attack

Fresh source read on `2026-08-14`:

- XAG 117: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117`;
- XAG collection: `https://learn.microsoft.com/en-us/xbox/accessibility/guidelines`.

The XAG 117 page is current with page last-updated date `2026-03-04`. Under **Implementation guidelines**, after the field-of-view and camera-movement directives, the page states the camera-view-choice directive as an unqualified bullet: players are to be allowed to choose between first- and third-person camera views. The bullet is not introduced by `consider`, `ideally`, example-only language, or another advisory qualifier.

The XAG collection describes the XAGs as accessibility **best practices**, explicitly not a compliance/legal checklist, and describes Implementation guidelines as prescriptive guidance intended to provide a minimum accessible-component baseline. Therefore the source supports repository-native best-practice `SHOULD` strength when the mapped condition applies, but does not support `MUST`, legal/compliance, certification, or platform-authority inflation.

The inherited XAG 108–123 origin policy blob `80e278315d6b7a108d89da3f5a99086a8ef91bf7` confirms the defect and the repository-native sibling pattern:

- `XAG117-CAMERA-VIEW-CHOICE` is the sole target and is currently `BEST_PRACTICE_RECOMMENDED_IF_APPLICABLE / CONSIDER`;
- sibling unqualified camera guidance such as `XAG117-FIELD-OF-VIEW-ADJUST` and `XAG117-CAMERA-MOVEMENT-SETTINGS` is represented as `BEST_PRACTICE_REQUIRED_IF_APPLICABLE / SHOULD`.

The v13 correction therefore restores consistency with both the current first-party source and the repository's existing authority taxonomy without promoting XAG guidance into mandatory compliance authority.

## 3. Exact v13-over-v12 semantic reconstruction

The v13 composition contract loads exact v12 policy/report blobs as immutable inputs and declares a single `atomic_clause_correction_patch`:

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

Against the inherited atom, exactly two semantic authority fields change:

- `authority_class`: `BEST_PRACTICE_RECOMMENDED_IF_APPLICABLE` → `BEST_PRACTICE_REQUIRED_IF_APPLICABLE`;
- `source_modality`: `CONSIDER` → `SHOULD`.

The following are preserved exactly:

- atom identity `XAG117-CAMERA-VIEW-CHOICE`;
- source id `XAG-117`;
- `CONDITIONAL` applicability;
- trigger `game_supports_first_person_or_third_person_camera_presentation`;
- semantic payload `first_person_and_third_person_view_choice_available: true`;
- evidence requirement `ACC-EV-XAG117`;
- gap `ACC-GAP-XAG117`.

The overlay does not broaden the inherited trigger, does not redefine a sibling XAG 117 record, and does not create a universal requirement outside the inherited conditional applicability boundary.

## 4. Validator/oracle attack

`ACCESSIBILITY-POLICY-VALIDATOR-v13` makes the correction load-bearing rather than documentary only. The declared fixtures cover all material authority-pair regressions:

| Candidate | Expected |
| --- | --- |
| required-if-applicable + `SHOULD` | `PASS` |
| recommended-if-applicable + `CONSIDER` | `REJECT_SOURCE_MODALITY_WEAKENING` |
| required-if-applicable + `CONSIDER` | `REJECT_SOURCE_MODALITY_WEAKENING` |
| recommended-if-applicable + `SHOULD` | `REJECT_ACCEPTANCE_AUTHORITY_DRIFT` |
| compliance / `MUST` | `REJECT_AUTHORITY_INFLATION` |

Adversarial fixtures separately reject mutation of identity, trigger, applicability, semantic payload, evidence/gap routing, any unrelated v12-composed record, and the previously reviewed XAG 112/XAG 114/XAG 115/XAG 116 corrections. This closes both halves of `W2-REV-ACC17-M01`: advisory weakening cannot pass, and stronger-than-source authority cannot pass.

No material missing witness was found in this bounded authority/modality scope.

## 5. Preservation and inventory attack

The v13 packet preserves the reviewed lineage rather than re-adjudicating it:

- XAG 112 reviewed navigation corrections: preserved;
- XAG 114 `titles` exception: preserved;
- XAG 115 stored-data operator: preserved;
- XAG 115 permanent/destructive-action conjunction: preserved;
- XAG 115 no-button-hold destructive-confirmation record: preserved;
- XAG 116 default-over-20-hours exception and reviewed timing semantics: preserved.

Exact inventory assertions remain:

- XAG 112 = `14`;
- XAG 114 = `16`;
- XAG 108–123 = `113`;
- inherited XAG 101–107 = `105`;
- composed XAG 101–123 = `218`.

The v13 overlay adds no atom identity and removes, splits, or renames none. The only corrected semantic authority surface is the target XAG 117 camera-view-choice atom.

## 6. Fail-closed authority attack

The exact candidate continues to state and validate:

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

Issue #302 terminalized early at XAG 117. This scoped review does not extend judgment into XAG 118–123 and does not convert a clean bounded remediation review into aggregate accessibility acceptance.

## 7. Finding resolution and next gate

Within the exact reviewed scope, `W2-REV-ACC17-M01` is **RESOLVED_BOUNDED** by the candidate v13 overlay and this fresh scoped review.

A separately authorized squash-only integration episode may now consider exact producer Issue #303 / PR #305 as noncanonical remediation provenance. Integration remains a separate authority gate. Even after any authorized integration of producer and review provenance, the required full corrected XAG 108–123 review must resume from XAG 118–123 before empirical accessibility evidence work can become eligible.

**Final disposition:** `CLEAN_FOR_NONCANONICAL_INTEGRATION`.
