# W2-REV-ACC-19 — required full-review continuation of XAG 118–123

**Mission:** `W2-REV-ACC-19` / Issue #308  
**Task class:** required full-review continuation  
**Trust mode:** `DEGRADED_INDEPENDENT` — fresh actor/session distinct from Issue #303 production and Issue #306 scoped review, while repository writes use the shared GitHub principal.  
**Disposition:** `CHANGES_NEEDED`  
**Terminal boundary:** early-negative at XAG 120 after one reproducible MAJOR source-semantics inflation. XAG 121–123 remain unaccepted by this episode.  
**Authority:** noncanonical review provenance only; no empirical accessibility PASS, mapping completion, readiness, implementation, release, legal/compliance, platform certification, verification-PASS, integration, decision, or canonical authority.

## 1. Frozen reviewed identity

The review froze the following exact identities before judgment:

- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- review base/current main at claim: `65d4eb8144e33d8e247c0dc0a688f6811a4225bb`;
- current integrated policy v13 blob: `3dcdaa400ffd43cea390c331f5b4f8ea62750a5c`;
- current integrated report v13 blob: `e5f1f491a91499bef96861d2878e4fb5552a207b`;
- inherited XAG 108–123 origin policy blob: `80e278315d6b7a108d89da3f5a99086a8ef91bf7`;
- Issue #302 required-review claim `5296669009`, terminal `5296708193`, review head `6327b6b6708f5159b20e37ffe5b348963bd5d8bb`, work `1e33561de0e2afa76836910cd947b06934c0cfd4`, disposition `CHANGES_NEEDED`, terminal boundary XAG 117;
- Issue #303 terminal producer `5296754811`, head `09f4f3eee194b7ffa57b668db63421c8397a15b5`, work `edd2de28df9c246066dd9db5e6b436d635157ef4`, integrated as squash `e8c30602e94e857ffb52d05a72e9b2c3615bd581` under integration claim `5296792164` / status `5296800479`;
- Issue #306 required scoped-review terminal `5296785707`, head `c89a507b7c01be3f3c611718923859a2967fd3d3`, work `8e95ed5a2d6efa4f84689c23f6b748c1dbe84c69`, disposition `CLEAN_FOR_NONCANONICAL_INTEGRATION`, integrated as squash at `main@65d4eb8144e33d8e247c0dc0a688f6811a4225bb` under integration claim `5296798277`.

Current v13 explicitly replaces only the XAG 117 camera-view authority/modality metadata and preserves every other v12-composed semantic record, inventory identity/count, prior reviewed correction, evidence/gap route, and fail-closed aggregate state. Therefore the XAG 118–123 records reviewed here remain the inherited current records unless separately overlaid.

## 2. Review scope and source freshness

Issue #302 validly stopped at XAG 117 and explicitly left XAG 118–123 unaccepted. Issue #303 corrected that bounded defect and Issue #306 independently reviewed the exact correction cleanly. This episode therefore resumed only XAG 118–123, while treating all reviewed XAG 108–117 corrections as immutable preservation inputs.

Fresh first-party Microsoft Learn source was re-read on `2026-08-14`. The pages attacked before the terminal finding report last update `2026-03-04`:

- XAG 118: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/118`
- XAG 119: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/119`
- XAG 120: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/120`

The review stopped after the first reproducible material defect at XAG 120, as allowed by the required-review contract. No acceptance is claimed for XAG 121–123.

## 3. XAG 118 — no material finding before continuation

Fresh XAG 118 recheck preserved the source's key photosensitivity semantics:

- all relevant game visual content should be tested for photosensitive seizure triggers and adverse-reaction imagery should be avoided;
- luminance flash definition: 10% luminance change with the darker value below 0.8;
- luminance-flash failure: approximately more than three flashes per second, approximately 20% or more of the screen, with lower-intensity extended flashing also able to fail;
- red-flash saturation ratio `R/(R+G+B) >= 0.8`, `(R-G-B) × 320 > 20`, the same approximate frequency/area failure bounds, and extended lower-intensity failure condition;
- spatial-pattern failure: alternating high-contrast bands, contrast difference greater than 10%, and approximately 20% or more screen area.

The exact inherited atoms `XAG118-PHOTOSENSITIVITY-TEST-AND-AVOID`, `XAG118-LUMINANCE-FLASH-LIMITS`, `XAG118-RED-FLASH-LIMITS`, and `XAG118-SPATIAL-PATTERN-LIMITS` preserve those definition/failure/mitigation bundles with `SHOULD` best-practice authority and page-scoped evidence/gap routing. No reproducible material mismatch was established before continuing.

## 4. XAG 119 — no material finding before continuation

Fresh XAG 119 recheck preserved the source's directional and applicability distinctions:

- speech-to-text transcribes incoming player voice into text in real time;
- text-to-speech turns the local player's entered outgoing text into synthesized audio on the voice channel;
- text entry is available where communication is available;
- incoming text and non-text communication are locally narrated when screen narration is enabled;
- player-initiated character voice conveying communication intent is transcribed for players using speech-to-text;
- predefined-message review is narrated on focus when narration is enabled;
- supported platform STT/TTS defaults are read/applied where available, while game-level overrides remain available for supported communication accessibility features.

The nine inherited XAG 119 atoms retain these channels and triggers separately. No reproducible material defect was established before continuing.

## 5. XAG 120 source reconstruction through the terminal boundary

Fresh XAG 120 states that when a game offers one-to-one or one-to-many communication, the necessary access, configuration, and usage pathways should be accessible in accordance with relevant XAGs.

For configuration, the source's normative object is the **accessibility/usability of the necessary UI and settings that exist**. It introduces concrete settings as examples. In the communications-notification portion, the source says the necessary menus or settings used to manage communication-related notifications should be usable by a player with a disability, then illustrates that category with examples such as notification display-duration controls and notification on/off controls.

This distinction is load-bearing: the source requires accessibility of applicable controls and pathways; it does not say every game with any communication notification must add both a duration-adjustment feature and an on/off feature.

## 6. Finding `W2-REV-ACC19-M01` — XAG 120 notification-setting example promoted to required feature existence

**Severity:** MAJOR  
**Class:** `EXAMPLE_TO_REQUIREMENT_PROMOTION_AND_FEATURE_EXISTENCE_INFLATION`  
**Affected atom:** `XAG120-COMM-NOTIFICATION-SETTINGS`

### Current first-party source

Under XAG 120 **Configuring the communication experience**, Microsoft requires the necessary configuration UI to be accessible and explicitly introduces the subsequent concrete controls as examples. For communication-related notifications, the source requires the relevant menus/settings to be usable by players with disabilities. Duration adjustment and on/off controls illustrate possible notification settings; they are not stated as universal capabilities that every communication notification must provide.

### Current preserved mapping

The exact inherited current atom is:

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

Current v13's composition contract explicitly preserves every v12-composed semantic record other than the XAG 117 camera-view authority/modality correction, so this atom remains effective at the reviewed current identity.

### Why this is material

The trigger is merely `communication_notifications_are_available`. Once true, the policy requires both `notification_duration_adjustable_when_timed` and `notifications_can_be_turned_on_or_off`. A game can therefore fail the machine-readable mapping solely because it does not implement optional example capabilities that the source did not universally require, even if every notification setting/control it actually exposes is fully accessible.

That is semantic/source-modality inflation and can create a false-negative accessibility acceptance result. The source-faithful obligation is accessibility of existing/applicable notification-management UI, while any specific duration/toggle capability must be gated on that capability existing or represented as illustrative/recommended semantics rather than unconditional required feature existence.

The v6 validator also declares XAG 120 coverage of “settings, notifications, social actions, and chat operations” as a required semantic assertion, so the affected atom is part of the load-bearing mechanical contract rather than dead prose.

### Required bounded remediation

Route exactly one remediation successor that:

1. consumes exact current integrated v13 policy/report as immutable input;
2. corrects only `XAG120-COMM-NOTIFICATION-SETTINGS` and the minimum validator/report metadata required to encode the source-faithful boundary;
3. preserves atom identity, source id, page-scoped evidence/gap route, all unrelated XAG records, all prior reviewed corrections, and inventory counts;
4. keeps `notification_settings_accessible: true` as the applicable normative obligation;
5. does **not** require duration-adjustment or notification-toggle feature existence merely because communication notifications exist; either condition those semantics on the corresponding controls being present, or classify them as source examples/recommended semantics using repository-native mechanics;
6. adds adversarial fixtures that reject both (a) universal promotion of the example controls to required feature existence and (b) weakening accessibility of controls that do exist;
7. preserves XAG 120's communication-offered applicability boundary and does not create mandatory communication features where none are offered;
8. preserves exact inventory counts: XAG 112 = `14`, XAG 114 = `16`, XAG 108–123 = `113`, inherited XAG 101–107 = `105`, composed XAG 101–123 = `218`;
9. keeps empirical accessibility `NOT_RUN`, `mapping_complete: false`, `IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN`, `W2-REV-M02: OPEN_BOUNDED`, full corrected XAG 108–123 review incomplete, and XAG 121–123 unaccepted;
10. requires one fresh independent/degraded-independent scoped review of the exact remediation before any integration eligibility.

## 7. Preservation / authority boundary

No identity add/remove/split/rename is implied by this finding. The reviewed lineage remains fail-closed:

```yaml
xag_112_atomic_clause_count: 14
xag_114_atomic_clause_count: 16
xag_108_123_atomic_clause_count: 113
inherited_xag_101_107_atomic_clause_count: 105
composed_xag_101_123_atomic_clause_count: 218
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
full_xag_108_123_review_complete: false
xag_121_123_accepted: false
production_implementation_ready: false
legal_compliance_claimed: false
platform_certification_claimed: false
verification_pass_authority: false
canonicality: NOT_CANONICAL
```

Reviewed corrections through XAG 117 remain immutable preservation inputs, including XAG 112 navigation corrections, XAG 114 title exception, both XAG 115 operator corrections and button-hold semantics, XAG 116 timing exception/correction, and XAG 117 camera-view `BEST_PRACTICE_REQUIRED_IF_APPLICABLE / SHOULD` authority with its conditional applicability boundary.

## 8. Disposition

**`CHANGES_NEEDED`**.

Finding `W2-REV-ACC19-M01` is one reproducible MAJOR source-semantic defect. Because a clean full-review disposition is no longer possible, this episode terminalizes at the XAG 120 communication-notification-settings boundary. XAG 121–123 remain unaccepted and must be resumed only after the bounded remediation receives its mandatory fresh scoped review.

No empirical-accessibility successor is eligible. No mapping-complete, readiness, implementation, release, legal/platform, verification-PASS, integration, decision, or canonical authority is created by this review.