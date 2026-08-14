# W2-REM-ACC-12 — correct the XAG 115 stored-data protection operator

**Mission:** `W2-REM-ACC-12` / Issue #288  
**Winning claim:** comment `5294237608`  
**Claim base:** `main@d8445512718e00c8f223f9249b433b471ac2b70c`  
**Required full-review continuation:** Issue #287 winning claim `5293624794`, terminal `CHANGES_NEEDED` comment `5293661376`, review head `539f8bfe35f0b25854cc7d740bbf3ca8b215d829`, work `04ed012577d85eba5d060fe88a5d89b192163e57`  
**Finding:** `W2-REV-ACC13-M01` / MAJOR — `SOURCE_LOGICAL_OPERATOR_WEAKENING_AND_INCOMPLETE_VALIDATOR_ORACLE`  
**Immutable producer input:** policy v10 blob `12c1af5bd6ae88a549e575c594f8ec2afa387705`, report v10 blob `fc826cf315b0bda8308aecbc63364f6977be39d1`  
**Authority:** bounded noncanonical remediation only; fresh independent/degraded-independent scoped review remains mandatory.

## 1. Scope

Issue #287 resumed the required corrected XAG 108–123 review and terminated early on one reproducible XAG 115 defect. The inherited record `XAG115-DATA-MODIFICATION-REVIEW-CORRECT-REVERSE` flattened the source protection path from `(review AND correct) OR complete reversal` into `review OR correct OR reverse`, so a review-only or correction-only candidate could satisfy the mapping.

This remediation consumes exact v10 as immutable input and changes only that XAG 115 semantic operator plus the minimum validator/report metadata needed to make the weakening mechanically rejectable. It preserves the record identity, source id, SHOULD modality, applicability, trigger, evidence requirement, gap route, every unrelated XAG 115 record, and every unrelated composed semantic record.

## 2. Corrected machine-readable operator

The current first-party XAG 115 stored-data guidance, as frozen by Issue #287, requires a pre-commit protection path equivalent to:

```text
(review AND correct) OR complete_reverse_or_cancel
```

The v11 overlay expresses that structure explicitly:

```yaml
required_semantics:
  precommit_protection_path:
    any_of:
      - all_of:
          - review_available_before_commit
          - correction_available_before_commit
      - complete_reverse_or_cancel_available_before_commit
```

The first alternative is conjunctive: both review and correction must be available. The second alternative is a complete reversal/cancellation path. Neither review alone nor correction alone is sufficient.

## 3. Load-bearing validator/oracle coverage

`ACCESSIBILITY-POLICY-VALIDATOR-v11` requires all four operator witnesses:

1. review only → **REJECT_INCOMPLETE_PROTECTION_PATH**;
2. correction only → **REJECT_INCOMPLETE_PROTECTION_PATH**;
3. review + correction → **PASS**;
4. complete reversal/cancellation → **PASS**.

Adversarial assertions also reject any validator implementation that accepts the two incomplete paths or rejects either source-valid complete path. This closes the exact oracle gap identified by `W2-REV-ACC13-M01`.

## 4. Preservation proof

The identity/count contract is unchanged:

- XAG 114: **16** atomic records;
- XAG 112: **14** atomic records;
- XAG 108–123: **113** atomic records;
- inherited XAG 101–107: **105** atomic records;
- composed XAG 101–123: **218** atomic records.

The overlay preserves:

- reviewed XAG 112 corrections;
- reviewed XAG 114 title-exception correction;
- reviewed XAG 116 default-over-20-hours correction;
- XAG 115 permanent/destructive-action and button-hold semantics outside this finding;
- all evidence/gap routing;
- all fail-closed aggregate and authority state.

No identity is added, removed, split, or renamed.

## 5. Finding disposition and bounded self-review

`W2-REV-ACC13-M01` is **RESOLVED_PENDING_FRESH_SCOPED_REVIEW** in this producer packet:

- review-only candidate rejected: **YES**;
- correction-only candidate rejected: **YES**;
- review + correction candidate accepted: **YES**;
- complete-reversal/cancellation candidate accepted: **YES**;
- record identity/source/modality/trigger changed: **NO**;
- evidence or gap route changed: **NO**;
- unrelated XAG 115 semantics changed: **NO**;
- reviewed XAG 112/XAG 114/XAG 116 corrections changed: **NO**;
- atomic counts changed: **NO**;
- empirical accessibility PASS claimed: **NO**;
- full corrected XAG 108–123 review claimed complete: **NO**.

Bounded producer self-review finds **0 unresolved BLOCKER / 0 unresolved MAJOR / 0 correction-requiring MINOR** in this remediation scope. Producer self-review is provenance only and does not satisfy the mandatory fresh independent scoped review.

## 6. Preserved fail-closed state

```yaml
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
full_xag_108_123_review_complete: false
xag_115_remainder_accepted: false
xag_116_123_accepted_by_issue_287: false
production_implementation_ready: false
legal_compliance_claimed: false
platform_certification_claimed: false
verification_pass_authority: false
integration_authorized: false
canonicality: NOT_CANONICAL
```

Issue #287's early-negative boundary remains authoritative. This bounded repair does not accept later XAG 115 surfaces or XAG 116–123, does not make an empirical accessibility successor eligible, and does not clear `IR-BLOCKER-ACCESSIBILITY-CURRENT` or `W2-REV-M02`.

## 7. Required next transition

Freeze this remediation at an exact terminal head with an exact-head draft PR, then perform a fresh independent/degraded-independent scoped review of this exact v11 correction.

A clean bounded review may make this exact producer packet eligible for a separately authorized squash-only noncanonical integration decision. It does not itself accept the XAG 115–123 remainder left unreviewed by Issue #287. After any authorized integration, the required full corrected XAG 108–123 review must resume across that still-unaccepted remainder before empirical accessibility evidence work can become eligible.
