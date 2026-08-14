# W2-REM-ACC-13 — restore the XAG 115 permanent-action protection conjunction

**Mission:** `W2-REM-ACC-13` / Issue #296  
**Winning claim:** comment `5294479716`  
**Claim base:** `main@ea7d085fd38d90658abe23ef0b315b786c6c80b4`  
**Required full-review continuation:** Issue #293 winning claim `5294404386`, terminal `CHANGES_NEEDED` comment `5294463445`, review head `dd4ec050025d4321d9e2a0b73b0ecbc6fdc920e3`, work `247e785b20f0cdad7e78d9501e86e7450432bf3e`  
**Finding:** `W2-REV-ACC15-M01` / MAJOR — `SOURCE_LOGICAL_OPERATOR_WEAKENING_AND_INCOMPLETE_VALIDATOR_ORACLE`  
**Immutable producer input:** policy v11 blob `b57c0aae729085c672ae9746179d76afb866a721`, report v11 blob `cb6b2ba3d1226c912874a89a369e9acf7912a034`  
**Authority:** bounded noncanonical remediation only; fresh independent/degraded-independent scoped review remains mandatory.

## 1. Scope

Issue #293 resumed the still-unaccepted XAG 115 remainder after the earlier stored-data operator remediation/review chain. It terminated early on the first reproducible material defect: the inherited record `XAG115-PERMANENT-ACTION-CONFIRM-OR-UNDO` encoded the permanent/destructive-action protection surface as `review OR confirmation OR undo`, while current first-party Microsoft XAG 115 states that permanent or destructive actions should offer a mechanism to **review, confirm, and undo** the action.

This remediation consumes exact v11 as immutable input and changes only that permanent/destructive-action semantic body plus the minimum validator/report metadata needed to make the conjunction mechanically enforceable. It preserves the record identity despite the legacy OR-oriented name, source id, SHOULD modality, conditional applicability, trigger, evidence requirement, gap route, every unrelated XAG 115 record, and every unrelated v11-composed semantic record.

The separate no-button-hold destructive-confirmation guideline remains a separate record and is not folded into this finding.

## 2. Corrected machine-readable protection surface

The v12 overlay represents the source conjunction explicitly:

```yaml
XAG115-PERMANENT-ACTION-CONFIRM-OR-UNDO:
  source_id: XAG-115
  authority_class: BEST_PRACTICE_REQUIRED_IF_APPLICABLE
  source_modality: SHOULD
  applicability: CONDITIONAL
  trigger: action_is_permanent_or_destructive
  required_semantics:
    permanent_or_destructive_action_protection:
      all_of:
        - review_available_for_action
        - confirmation_available_for_action
        - undo_available_for_action
  evidence_requirement_refs:
    - ACC-EV-XAG115
  gap_ref: ACC-GAP-XAG115
```

All three capabilities are conjunctive. Review alone, confirmation alone, undo alone, or any two-capability subset is insufficient. The complete review + confirmation + undo surface is the only source-faithful PASS case represented by this atom.

## 3. Load-bearing validator/oracle coverage

`ACCESSIBILITY-POLICY-VALIDATOR-v12` requires the complete truth surface:

| Candidate capability set | Expected |
| --- | --- |
| none | `REJECT_INCOMPLETE_PROTECTION_SURFACE` |
| review only | `REJECT_INCOMPLETE_PROTECTION_SURFACE` |
| confirmation only | `REJECT_INCOMPLETE_PROTECTION_SURFACE` |
| undo only | `REJECT_INCOMPLETE_PROTECTION_SURFACE` |
| review + confirmation only | `REJECT_INCOMPLETE_PROTECTION_SURFACE` |
| review + undo only | `REJECT_INCOMPLETE_PROTECTION_SURFACE` |
| confirmation + undo only | `REJECT_INCOMPLETE_PROTECTION_SURFACE` |
| review + confirmation + undo | `PASS` |

Adversarial assertions reject any validator that accepts any one-of-three or two-of-three candidate, rejects the complete three-capability set, changes the permanent-action record identity/trigger/evidence/gap routing, mutates the reviewed stored-data operator or its witnesses, or redefines the separate button-hold record.

## 4. Preservation proof

### Reviewed XAG 115 stored-data operator

The exact v11 `XAG115-DATA-MODIFICATION-REVIEW-CORRECT-REVERSE` semantics remain immutable:

```yaml
precommit_protection_path:
  any_of:
    - all_of:
        - review_available_before_commit
        - correction_available_before_commit
    - complete_reverse_or_cancel_available_before_commit
```

Its reviewed four witnesses remain unchanged:

1. review only → `REJECT_INCOMPLETE_PROTECTION_PATH`;
2. correction only → `REJECT_INCOMPLETE_PROTECTION_PATH`;
3. review + correction → `PASS`;
4. complete reversal/cancellation → `PASS`.

Thus `W2-REV-ACC13-M01` remains preserved as resolved in its bounded reviewed scope; this producer packet does not reopen or rewrite that correction.

### Separate destructive-confirmation record

`XAG115-NO-BUTTON-HOLD-DESTRUCTIVE-CONFIRMATION` remains byte-logically unchanged from the exact v11 composed lineage. Its source bullet is separate from the permanent/destructive-action review+confirm+undo conjunction and is outside this remediation finding.

### Inventory and reviewed lineage

The identity/count contract remains unchanged:

- XAG 114: **16** atomic records;
- XAG 112: **14** atomic records;
- XAG 108–123: **113** atomic records;
- inherited XAG 101–107: **105** atomic records;
- composed XAG 101–123: **218** atomic records.

The overlay also preserves the reviewed XAG 112 corrections, XAG 114 title-exception correction, XAG 116 default-over-20-hours correction, all evidence/gap routing, and every unrelated v11-composed semantic record.

No identity is added, removed, split, or renamed.

## 5. Finding disposition and bounded producer self-review

`W2-REV-ACC15-M01` is **RESOLVED_PENDING_FRESH_SCOPED_REVIEW** in this producer packet:

- no-capability candidate rejected: **YES**;
- review-only candidate rejected: **YES**;
- confirmation-only candidate rejected: **YES**;
- undo-only candidate rejected: **YES**;
- review+confirmation-only candidate rejected: **YES**;
- review+undo-only candidate rejected: **YES**;
- confirmation+undo-only candidate rejected: **YES**;
- review+confirmation+undo candidate accepted: **YES**;
- permanent-action record identity/source/modality/applicability/trigger changed: **NO**;
- evidence or gap route changed: **NO**;
- reviewed XAG 115 stored-data operator or its four witnesses changed: **NO**;
- separate XAG 115 no-button-hold record changed: **NO**;
- reviewed XAG 112/XAG 114/XAG 116 corrections changed: **NO**;
- atomic counts changed: **NO**;
- empirical accessibility PASS claimed: **NO**;
- full corrected XAG 108–123 review claimed complete: **NO**.

Bounded producer self-review finds **0 unresolved BLOCKER / 0 unresolved MAJOR / 0 correction-requiring MINOR** in this remediation scope. Producer self-review is provenance only and does not satisfy the mandatory fresh independent/degraded-independent scoped review.

## 6. Preserved fail-closed state

```yaml
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
full_xag_108_123_review_complete: false
xag_115_button_hold_surface_accepted_by_issue_293: false
xag_116_123_accepted_by_issue_293: false
production_implementation_ready: false
legal_compliance_claimed: false
platform_certification_claimed: false
verification_pass_authority: false
integration_authorized: false
canonicality: NOT_CANONICAL
```

Issue #293's early-negative boundary remains authoritative. This bounded repair does not accept the separate XAG 115 button-hold surface or XAG 116–123, does not make an empirical accessibility successor eligible, and does not clear `IR-BLOCKER-ACCESSIBILITY-CURRENT` or `W2-REV-M02`.

## 7. Required next transition

Freeze this remediation at an exact terminal head with an exact-head draft PR, then perform a fresh independent/degraded-independent scoped review of this exact v12 correction.

That scoped review must attack the all-of operator, all one-of-three/two-of-three rejection witnesses, complete three-of-three PASS witness, exact preservation of the reviewed v11 stored-data operator and four witnesses, preservation of the separate no-button-hold record, inventory counts, evidence/gap routing, and fail-closed authority state.

A clean bounded review may make this exact producer packet eligible only for a separately authorized squash-only noncanonical integration decision. It does not complete the still-unaccepted XAG 115/XAG 116–123 remainder. After any authorized integration of producer and review provenance, the required full corrected XAG 108–123 review must resume across that remainder before empirical accessibility evidence work can become eligible.
