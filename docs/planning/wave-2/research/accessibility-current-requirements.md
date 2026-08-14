# W2-REM-ACC-05 — remove subjective XAG 106 pronunciation applicability gate

**Mission:** `W2-REM-ACC-05` / Issue #252  
**Claim base:** `main@9b044059df07170f8db0f430451d15e1c6800f82`  
**Source review:** Issue #250 terminal `CHANGES_NEEDED` comment `5290193719`, head/work `57bb9a75e6b2cba600d75fe74d180283712abcae`  
**Finding:** `W2-REV-ACC04-M01` / MAJOR  
**Immutable reviewed producer:** Issue #247 terminal comment `5290154417`, head/work `fdc93c894e39e10a20dba81e910212dc56151441`  
**Immutable v4 policy blob:** `96a074e9c708d4ae2f86e8a70b7b4ade8202c799`  
**Authority:** bounded noncanonical remediation only; fresh independent scoped review remains mandatory.

## 1. Scope

Issue #250 independently reproduced one remaining source-semantic defect in the exact Issue #247 packet: `XAG106-PROPER-NAME-PRONUNCIATION` inherited the v3 trigger

`proper_name_technical_term_or_word_of_indeterminate_language_requires_pronunciation_help`

The trailing `requires_pronunciation_help` predicate is not present in the Microsoft XAG 106 implementation guideline. It can suppress a source-covered obligation based on a subjective product-side judgment while leaving clause identity, references, and structural validation apparently valid.

This remediation changes only that atomic record and the minimum semantic-regression contract required to prevent recurrence. The six Issue #247 corrections are immutable logical inputs through exact v4 blob `96a074e9c708d4ae2f86e8a70b7b4ade8202c799`; they are not rewritten here.

## 2. Fresh first-party source recheck

Microsoft XAG 106 was re-read on `2026-08-14`. The current page still reports last updated `2026-03-04` and its implementation guideline states that a mechanism should be provided so the player can understand the pronunciation of a proper name, technical term, or word of indeterminate language.

The covered term classes themselves establish applicability. The source does not add a separate condition that a designer or evaluator first decide the term `requires pronunciation help`.

This source is accessibility best-practice evidence, not legal/compliance or platform certification.

## 3. Correction

`ACCESSIBILITY-POLICY-OVERLAY-v5` composes over the exact v4 policy blob and replaces exactly one record:

```yaml
XAG106-PROPER-NAME-PRONUNCIATION:
  source_id: XAG-106
  authority_class: BEST_PRACTICE_REQUIRED_IF_APPLICABLE
  applicability: CONDITIONAL
  trigger: proper_name_or_technical_term_or_word_of_indeterminate_language_is_present
  required_semantics:
    pronunciation_mechanism_provided: true
  evidence_requirement_refs: [ACC-EV-NARRATION]
  gap_ref: ACC-GAP-XAG106
```

The corrected trigger is deterministic and based only on the source term classes. The required pronunciation mechanism is unchanged. Evidence and gap routing are unchanged.

## 4. Validator hardening

`ACCESSIBILITY-POLICY-VALIDATOR-v5` first requires exact v4 reconstruction, including the six already-reviewed Issue #243 correction records and the exact 77-new / 105-composed inventory. Only then may it replace the pronunciation record.

The new semantic guard requires exact trigger equality and rejects both the literal `requires_pronunciation_help` gate and any equivalent subjective product-judgment precondition. It also requires all three source term classes and `pronunciation_mechanism_provided: true`.

New adversarial cases are:

- `SUBJECTIVE_PRONUNCIATION_APPLICABILITY_GATE` → `REJECT_INVENTED_PRECONDITION`;
- `PRONUNCIATION_TERM_CLASS_DROPPED` → `REJECT_SEMANTIC_NARROWING`;
- `PRONUNCIATION_MECHANISM_DROPPED` → `REJECT_REQUIRED_SEMANTIC_LOSS`;
- `V4_CORRECTION_REDEFINED` → `REJECT_SCOPE_LEAKAGE`.

The existing fail-closed aggregate cases for XAG 108–123 promotion, empirical PASS laundering, and `mapping_complete: true` remain required.

## 5. Preservation proof

The v5 overlay does not add, remove, split, or rename any atomic clause. The inventory remains:

- XAG 102: 12;
- XAG 103: 8;
- XAG 104: 29;
- XAG 105: 5;
- XAG 106: 23;
- new XAG 102–106 total: 77;
- inherited XAG 101/XAG 107: 28;
- composed atomic total: 105.

All six v4 corrections remain logical inputs from the exact v4 blob and are outside this patch surface. XAG 108–123 remain `GUIDELINE_SUMMARY_ONLY`; no empirical accessibility evidence is produced.

## 6. Finding disposition

`W2-REV-ACC04-M01` is **RESOLVED_PENDING_FRESH_REVIEW** in this producer packet:

- subjective applicability gate removed: **YES**;
- all three source term classes preserved: **YES**;
- pronunciation mechanism preserved: **YES**;
- evidence/gap refs preserved: **YES**;
- clause identity/count changed: **NO**;
- six v4 corrections rewritten: **NO**;
- empirical accessibility PASS claimed: **NO**;
- aggregate blocker cleared: **NO**.

Producer self-review is not acceptance. A fresh independent/degraded-independent scoped reviewer must reconstruct exact v4 plus this v5 overlay, re-read current XAG 106, attack the new semantic fixtures, and verify the six v4 corrections remain unchanged before any integration eligibility can be considered.

## 7. Preserved fail-closed state

```yaml
xag_108_123: GUIDELINE_SUMMARY_ONLY
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
production_implementation_ready: false
integration_authorized: false
canonicality: NOT_CANONICAL
```

This task does not establish accessibility quality in the product, readiness, implementation, release, legal/compliance status, platform certification, verification PASS, decision authority, integration authority, or canonical status.

## 8. Required next transition

Freeze this remediation at an exact terminal head with an exact-head draft PR to `main`, then route a fresh scoped review. CLEAN review would only make the exact corrected packet eligible for separately authorized squash-only noncanonical integration; it would not close aggregate `W2-REV-M02` or `IR-BLOCKER-ACCESSIBILITY-CURRENT`.
