# W2-REV-ACC-15 — required corrected XAG 115–123 review continuation

**Issue:** #294  
**Mission:** `W2-REV-ACC-15`  
**Trust mode:** `DEGRADED_SINGLE_AGENT` / fresh reviewer episode  
**Winning claim:** `5294404928`  
**Review base:** `main@ea7d085fd38d90658abe23ef0b315b786c6c80b4`  
**Integrated policy v11:** `b57c0aae729085c672ae9746179d76afb866a721`  
**Integrated report v11:** `cb6b2ba3d1226c912874a89a369e9acf7912a034`  
**Inherited XAG 108–123 origin policy:** `80e278315d6b7a108d89da3f5a99086a8ef91bf7`  
**Disposition:** `CHANGES_NEEDED`  
**Finding:** `W2-REV-ACC15-M01` / **MAJOR** / `SOURCE_CONJUNCTION_WEAKENED_TO_OR_AND_MISSING_VALIDATOR_ORACLE`

## 1. Review boundary

Issue #287 terminalized its required full-review continuation early-negative at XAG 115 and explicitly left the later XAG 115 remainder and XAG 116–123 unaccepted. Issue #288 repaired only `XAG115-DATA-MODIFICATION-REVIEW-CORRECT-REVERSE`; Issue #291 independently clean-reviewed only that bounded operator correction. Both packets preserve the rest of XAG 115 unchanged.

This episode therefore resumed at the still-unaccepted XAG 115 surface. The review is terminalized on the first reproducible material defect as permitted by the required-review contract. XAG 116–123 are **not adjudicated or accepted by this episode**.

## 2. Fresh source reconstruction

Current first-party Microsoft XAG 115 was re-read on 2026-08-14:

- source: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/115`
- page title: `Xbox Accessibility Guideline 115: Error messages and destructive actions`
- page last updated: `2026-03-04`
- relevant implementation sentence: permanent or destructive actions are to offer players a mechanism to **review, confirm, and undo** those actions.

The source uses a conjunctive list of capabilities. It does not say that any one of review, confirmation, or undo alone is sufficient.

## 3. Exact inherited mapping defect

The exact inherited XAG 108–123 origin packet contains:

```yaml
XAG115-PERMANENT-ACTION-CONFIRM-OR-UNDO:
  source_id: XAG-115
  authority_class: BEST_PRACTICE_REQUIRED_IF_APPLICABLE
  source_modality: SHOULD
  applicability: CONDITIONAL
  trigger: action_is_permanent_or_destructive
  required_semantics:
    review_or_confirmation_or_undo_mechanism_available: true
  evidence_requirement_refs:
    - ACC-EV-XAG115
  gap_ref: ACC-GAP-XAG115
```

The semantic field explicitly converts the source's `review AND confirm AND undo` capability surface into `review OR confirmation OR undo`. A confirmation-only candidate, a review-only candidate, or an undo-only candidate can therefore satisfy the represented atom while omitting two source-stated capabilities.

The integrated v11 overlay does not repair this record. Its composition contract says it replaces only `XAG115-DATA-MODIFICATION-REVIEW-CORRECT-REVERSE`, and its required semantic assertions explicitly state that no permanent-action XAG 115 record is redefined. The clean Issue #291 scoped review likewise verifies preservation of unrelated XAG 115 semantics rather than re-adjudicating them.

## 4. Mechanical/oracle defect

Search of the exact inherited origin packet finds the weak field `review_or_confirmation_or_undo_mechanism_available` only as the permanent-action record's represented required semantic. There is no separate load-bearing truth-table/oracle that rejects incomplete capability sets.

Required negative witnesses for a source-faithful validator include at minimum:

| Candidate | Expected |
|---|---|
| review only | REJECT |
| confirmation only | REJECT |
| undo only | REJECT |
| review + confirmation only | REJECT unless the source-faithful model explicitly and defensibly treats undo as pre-commit cancellation in that exact path |
| complete source-faithful review/confirm/undo capability surface | PASS |

A remediation should distinguish pre-commit cancellation from post-commit undo precisely rather than preserving the current lossy one-Boolean OR.

## 5. Severity and reproducibility

`W2-REV-ACC15-M01` is **MAJOR** because the current machine-readable acceptance contract can PASS implementations that do not provide the complete source-stated protection surface for permanent/destructive actions. This is source-semantic weakening, not a prose-only discrepancy.

Reproduction:

1. Load integrated v11 policy blob `b57c0aae729085c672ae9746179d76afb866a721`.
2. Resolve it through v10 and inherited origin blob `80e278315d6b7a108d89da3f5a99086a8ef91bf7`.
3. Observe v11 changes only the stored-data operator and preserves the permanent-action record.
4. Resolve `XAG115-PERMANENT-ACTION-CONFIRM-OR-UNDO`.
5. Observe `review_or_confirmation_or_undo_mechanism_available: true`.
6. Compare with current first-party XAG 115's `review, confirm, and undo` implementation sentence.
7. Construct a confirmation-only candidate. The represented Boolean can be satisfied even though review and undo are missing.
8. No dedicated operator oracle in the inherited packet rejects that weakening.

Result: reproducible material source-fidelity defect.

## 6. Preserved reviewed state

No defect is asserted here against the already-reviewed bounded corrections:

- XAG 112 scaled/zoomed-map non-scrolling alternative navigation;
- XAG 112 universal submenu return coverage;
- XAG 112 same-input focus escape;
- XAG 114 `titles` reading-level exception;
- XAG 115 stored-data operator `(review AND correct) OR complete_reverse_or_cancel` and its four witnesses;
- XAG 116 `default_time_limit_exceeds_20_hours` correction.

Inventory remains a frozen input, not newly accepted by this early-negative review:

```yaml
xag_114_atomic_clause_count: 16
xag_112_atomic_clause_count: 14
xag_108_123_atomic_clause_count: 113
inherited_xag_101_107_atomic_clause_count: 105
composed_xag_101_123_atomic_clause_count: 218
```

## 7. Fail-closed state

```yaml
review_disposition: CHANGES_NEEDED
finding: W2-REV-ACC15-M01
finding_severity: MAJOR
full_xag_108_123_review_complete: false
xag_115_remainder_accepted: false
xag_116_123_accepted_by_issue_294: false
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
empirical_accessibility_successor_eligible: false
production_implementation_ready: false
verification_pass_authority: false
canonicality: NOT_CANONICAL
```

No XAG 116–123 source semantics are accepted by this episode. Their pages were not used to claim any positive review authority after the XAG 115 material defect invalidated the clean disposition.

## 8. Required successor

Exactly one bounded remediation successor is routed: Issue #295 / `W2-REM-ACC-13`.

That remediation must correct the permanent/destructive-action capability operator and add load-bearing incomplete/complete capability witnesses while preserving the reviewed XAG 115 stored-data correction and every unrelated semantic/authority boundary. Fresh independent/degraded-independent scoped review of the exact remediation is mandatory before any producer integration eligibility.

After a clean bounded remediation review and any separately authorized squash-only integrations, the required full corrected XAG 108–123 review must resume/reperform the still-unaccepted XAG 115 remainder and XAG 116–123. Empirical accessibility work remains ineligible until that full review is genuinely clean and complete.

## 9. Authority boundary

This is noncanonical required-review provenance. `CHANGES_NEEDED` does not authorize producer integration, empirical accessibility PASS, mapping completion, implementation/readiness/release, legal/compliance status, platform certification, verification-PASS, decision authority, or canonical authority. Any later integration of this negative review provenance is a separate squash-only decision under repository authority and does not change the negative disposition.
