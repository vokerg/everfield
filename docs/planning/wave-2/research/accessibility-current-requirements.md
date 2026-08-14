# W2-REM-ACC-15 — correct XAG 120 notification-setting example inflation

**Mission:** `W2-REM-ACC-15` / Issue #310  
**Winning claim:** comment `5296883667`  
**Claim base:** `main@65d4eb8144e33d8e247c0dc0a688f6811a4225bb`  
**Required full-review continuation:** Issue #308 winning claim `5296830252`, terminal `CHANGES_NEEDED` comment `5296868370`, review head `024efaa4cc97b5af6e669cf9100b5172a2096bd4`, work `ed51563510cee7cd24463a6d1a169ec3f0f2ea3e`  
**Finding:** `W2-REV-ACC19-M01` / MAJOR — `EXAMPLE_TO_REQUIREMENT_PROMOTION_AND_FEATURE_EXISTENCE_INFLATION`  
**Immutable producer input:** policy v13 blob `3dcdaa400ffd43cea390c331f5b4f8ea62750a5c`, report v13 blob `e5f1f491a91499bef96861d2878e4fb5552a207b`  
**Authority:** bounded noncanonical remediation only; fresh independent/degraded-independent scoped review remains mandatory.

## 1. Scope and source binding

Issue #308 resumed the still-unaccepted XAG 118–123 mapping remainder. It established no material finding in its XAG 118 photosensitivity or XAG 119 speech/text communication attacks, then terminated early on the first reproducible material defect at XAG 120. XAG 121–123 therefore remain unaccepted by that episode.

Fresh first-party Microsoft XAG 120 was re-read on `2026-08-14`:

- `https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/120`
- XAG v3.2 lineage; page last updated `2026-03-04`.

The source makes accessibility/usability of the necessary communication configuration UI the applicable obligation. In the notification-management subsection, controls such as adjusting notification display duration and turning certain notifications on/off are introduced as examples. They identify settings whose UI should be accessible when those settings exist; the examples do not universally require every title with communication notifications to create both capabilities.

## 2. Exact inherited defect

The exact inherited XAG 120 atom resolved through current v13 is:

```yaml
XAG120-COMM-NOTIFICATION-SETTINGS:
  source_id: XAG-120
  authority_class: BEST_PRACTICE_REQUIRED_IF_APPLICABLE
  source_modality: SHOULD
  applicability: CONDITIONAL
  trigger: communication_notifications_are_available
  required_semantics:
    notification_settings_accessible: true
    notification_duration_adjustable_when_timed: true
    notifications_can_be_turned_on_or_off: true
  evidence_requirement_refs:
    - ACC-EV-XAG120
  gap_ref: ACC-GAP-XAG120
```

The identity, source, best-practice authority, `SHOULD` modality, conditional applicability, trigger, evidence route, and gap route are not the finding. The defect is the semantic payload: once any communication notification exists, the atom requires both example capabilities as product features. That can false-fail a source-faithful implementation whose actual notification-management UI is accessible but which does not offer one or both example controls.

## 3. Bounded v14 correction

The v14 overlay keeps the source's applicable accessibility obligation and converts the examples into conditional source-faithful semantics:

```yaml
XAG120-COMM-NOTIFICATION-SETTINGS:
  source_id: XAG-120
  authority_class: BEST_PRACTICE_REQUIRED_IF_APPLICABLE
  source_modality: SHOULD
  applicability: CONDITIONAL
  trigger: communication_notifications_are_available
  required_semantics:
    notification_settings_accessible: true
  conditional_semantics:
    - when: notification_duration_adjustment_control_is_present
      required:
        notification_duration_adjustment_control_accessible: true
    - when: notification_on_off_control_is_present
      required:
        notification_on_off_control_accessible: true
  source_examples:
    - notification_display_duration_adjustment
    - notification_on_off_control
  evidence_requirement_refs:
    - ACC-EV-XAG120
  gap_ref: ACC-GAP-XAG120
```

This preserves two distinct source truths simultaneously:

1. If the game offers applicable communication-notification management, that management UI remains required to be accessible.
2. The source examples do not require the game to add duration-adjustment or notification-toggle features. If those controls do exist, they remain inside the accessibility obligation.

The correction does not weaken XAG 120 into an advisory-only mapping and does not invent new communication capabilities.

## 4. Load-bearing mechanical oracles

`ACCESSIBILITY-POLICY-VALIDATOR-v14` makes the correction mechanically load-bearing:

| Candidate | Expected |
| --- | --- |
| notifications exist; management UI accessible; neither example control exists | `PASS` |
| duration control exists and is accessible | `PASS` |
| duration control exists but is inaccessible | `REJECT_EXISTING_NOTIFICATION_CONTROL_INACCESSIBLE` |
| notification toggle exists but is inaccessible | `REJECT_EXISTING_NOTIFICATION_CONTROL_INACCESSIBLE` |
| mapping universally requires both example controls to exist | `REJECT_EXAMPLE_TO_REQUIREMENT_PROMOTION` |
| notification-management UI is inaccessible | `REJECT_NOTIFICATION_MANAGEMENT_ACCESSIBILITY_WEAKENING` |

Additional adversarial assertions reject mutation of the atom identity, trigger, authority/modality, evidence/gap routing, any unrelated v13 record, or any previously reviewed correction. The validator therefore prevents both directions of semantic drift: false feature-existence inflation and fail-open accessibility weakening.

## 5. Preservation proof

The v14 overlay consumes exact v13 as immutable input and replaces only the XAG 120 notification-setting semantic encoding described above.

Reviewed correction lineage remains unchanged:

- XAG 112 scaled/zoomed-map non-scrolling alternative navigation, universal submenu return coverage, and same-input focus escape;
- XAG 114 `titles` reading-level exception;
- XAG 115 stored-data protection operator `(review AND correct) OR complete reverse/cancel`;
- XAG 115 permanent/destructive-action conjunction `review AND confirmation AND undo`;
- XAG 115 no-button-hold destructive-confirmation semantics;
- XAG 116 default-over-20-hours exception and reviewed timing semantics;
- XAG 117 camera-view `BEST_PRACTICE_REQUIRED_IF_APPLICABLE / SHOULD` correction with the inherited conditional trigger and semantic payload.

Inventory is unchanged:

- XAG 112: **14** atomic records;
- XAG 114: **16** atomic records;
- XAG 108–123: **113** atomic records;
- inherited XAG 101–107: **105** atomic records;
- composed XAG 101–123: **218** atomic records.

No identity is added, removed, split, or renamed. No sibling XAG 120 atom and no unrelated v13-composed record is redefined.

## 6. Finding disposition and producer self-review

`W2-REV-ACC19-M01` is **RESOLVED_PENDING_FRESH_SCOPED_REVIEW** in this producer packet:

- notification-management accessibility remains required when applicable: **YES**;
- duration-adjustment example promoted to universal feature existence: **NO**;
- notification-toggle example promoted to universal feature existence: **NO**;
- existing duration-control accessibility allowed to fail open: **NO**;
- existing toggle-control accessibility allowed to fail open: **NO**;
- atom identity changed: **NO**;
- source id changed: **NO**;
- authority/modality changed: **NO**;
- applicability or trigger broadened: **NO**;
- evidence or gap route changed: **NO**;
- sibling XAG 120 or unrelated v13 record changed: **NO**;
- reviewed XAG 112–117 corrections changed: **NO**;
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
xag_121_123_accepted_by_issue_308: false
production_implementation_ready: false
legal_compliance_claimed: false
platform_certification_claimed: false
verification_pass_authority: false
integration_authorized: false
canonicality: NOT_CANONICAL
```

Issue #308's early-negative boundary remains controlling. This bounded repair does not accept XAG 121–123, make empirical accessibility evidence work eligible, clear the aggregate blocker, create readiness/implementation/release authority, or grant verification, integration, decision, or canonical authority.

## 8. Required next transition

Freeze this exact remediation in an exact-head draft PR and perform a fresh independent/degraded-independent scoped review. The review must independently re-read current XAG 120, attack both example-to-required-feature inflation and accessibility weakening, prove identity/authority/trigger/evidence/gap preservation, and verify all inventory/fail-closed invariants.

A clean scoped review may make this exact producer packet eligible only for the separately authorized squash-only noncanonical integration route. After the bounded correction chain is integrated as authorized, the required full mapping review must resume from the still-unaccepted XAG 121–123 remainder before any empirical-accessibility successor can be derived.
