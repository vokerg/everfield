# W2-REM-ACC-03 — XAG 102–106 atomic source-clause remediation

**Mission:** `W2-REM-ACC-03` / Issue #240  
**Base main:** `cc973dd5e758bef20ba588ab1440ae82ec1ec2b6`  
**Frozen predecessor:** W2-REM-ACC-02 / Issue #135 policy blob `d4f934d1731800b3966adeae82c4a57b9af737b8`  
**Formal finding route:** W2-REV-01 / Issue #84 / `W2-REV-M02` (`OPEN_BOUNDED`)  
**Observed first-party sources:** `2026-08-14`  
**Authority:** bounded noncanonical remediation input; fresh independent scoped review is required before this packet can affect readiness.

## 1. Scope and fail-closed boundary

This remediation advances only the atomic-mapping half of `W2-REV-M02` for the contiguous XAG 102–106 tranche. It composes over the exact integrated Issue #135 v2 policy and does not rewrite the inherited XAG 101/XAG 107 clause inventories, Valve compatibility mapping, platform scope, or legal/rights authority.

The aggregate deliberately remains fail closed:

```yaml
mapping_complete: false
blocker_id: IR-BLOCKER-ACCESSIBILITY-CURRENT
blocker_authority_state: OPEN
newly_atomized_pages: [XAG-102, XAG-103, XAG-104, XAG-105, XAG-106]
summary_only_pages: [XAG-108..123]
empirical_accessibility_pass_claimed: false
production_implementation_ready: false
canonicality: NOT_CANONICAL
fresh_independent_scoped_review_required: true
```

This task does **not** claim that the product implements any mapped clause. Every new empirical evidence requirement remains `NOT_RUN`.

## 2. Source discipline

The bounded source corpus is the current Microsoft Xbox Accessibility Guidelines v3.2 first-party page set:

- XAG 102 Contrast — `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/102`
- XAG 103 Additional channels for visual and audio cues — `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103`
- XAG 104 Subtitles and captions — `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/104`
- XAG 105 Audio accessibility — `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/105`
- XAG 106 Screen narration — `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/106`

All five pages report a `2026-03-04` last-updated date in the current English source surface observed on `2026-08-14`. The mapping treats the XAGs as Microsoft accessibility best practices, not legal/compliance certification.

Only normative implementation-guideline bullets and their load-bearing nested conditions are promoted to atomic clause records. Explanatory examples, screenshots, background prose, resource lists, and purely permissive suggestions are not silently upgraded into requirements.

## 3. Exact atomic inventories

The v3 overlay adds **77** stable clause IDs:

| Page | New atomic clauses | Primary mapped surface |
|---|---:|---|
| XAG 102 | 12 | contrast thresholds, high-contrast behavior, color dependence, text-in-image and contrast exemptions |
| XAG 103 | 8 | multisensory critical cues, color alternatives/configuration, narration-safe symbols, text-only dialogue location |
| XAG 104 | 29 | subtitle/caption coverage, speaker/direction semantics, startup/configuration, presentation constraints, UGC/transcripts/sign language |
| XAG 105 | 5 | independent audio controls, spatial/mono options, pause exemptions, assistive-audio ducking |
| XAG 106 | 23 | narration coverage/semantics, focus behavior, language/markup exposure, time media, tables, pronunciation |

Together with the 28 inherited exact XAG 101/XAG 107 clauses, the composed candidate has **105** atomically inventoried clauses. XAG 108–123 remain summary-only and are mechanically forbidden from contributing to `mapping_complete`.

### 3.1 XAG 102 — contrast and color dependence

The exact inventory preserves the load-bearing contrast thresholds and conditions instead of reducing the page to a page-level summary. It binds `3:1` for large-scale text/visual elements with platform-specific large-text pixel thresholds, `4.5:1` for important standard-size text/visual elements, `3:1` for inactive UI text, and `4.5:1`/`3:1` for standard/large input or placeholder text. It separately binds a high-contrast mode with a minimum `7:1` UI ratio when enabled, measurement against the lowest-contrast area for non-solid backgrounds, platform high-contrast preference use as a launch default when available, player-configurable foreground/background text colors, and a prohibition on color as the sole important-information channel.

The image-text and contrast exceptions are explicit rather than implicit: text embedded in images is prohibited except for logotypes; logotypes and purely decorative/non-visible/picture-incidental elements are separately typed as exceptions to minimum-contrast requirements. These exception records cannot erase a non-exempt clause because their triggers are distinct.

### 3.2 XAG 103 — multisensory critical information

The inventory requires critical visual content to have at least one additional sensory channel and requires critical information represented by multiple visual affordances to have a nonvisual identification path. It captures narration-safe graphical symbols with contextual text alternatives, a non-color signifier for critical color-coded information, player color configuration when color is the primary information channel, and an additional non-color cue when controls are grayed or recolored to signal state.

Critical audio similarly requires an additional sensory method, with haptics explicitly forbidden as the sole alternative. Text-only dialogue without a spoken audio track is routed to both speaker identity and spatial-location presentation evidence. These records remain conditional on the relevant feature/content being present.

### 3.3 XAG 104 — subtitles, captions, presentation, and scripted media

The inventory separately binds subtitles for all spoken content; speaker identification; spatial indication when the speaker direction is unclear; speaker-name refresh on speaker changes or after a significant pause; and a prohibition on speaker color as the only identifier. It preserves the startup rule that players can adjust subtitles before play begins or subtitles are enabled by default, plus captioning of important non-visualized sounds and direction indication when needed.

Configuration requirements are independent records: captions/subtitles must be discoverable and togglable during play, distinct information types are independently configurable, and available platform caption preferences are used as defaults. Presentation rules preserve the XAG 101 minimum-size binding, at least 200% scaling, readable spacing, avoidance of lines over 40 characters, normal two-line and exceptional three-line bounds, editorially sensible manual line breaks where feasible, mixed case, at least one sans-serif option, configurable solid backgrounds and color, opacity from 0–100%, and placement that does not obscure important UI/gameplay at the largest supported size.

The packet also maps configuration preview, realistic preview context where feasible, persistence of caption information into recording/capture/UGC when applicable, accessible full-motion-video transcripts, sign-language interpretation for scripted/prerecorded spoken media, and localization of that interpretation for the target language/region. None of these records is treated as empirically satisfied by being mapped.

### 3.4 XAG 105 — audio control and pause semantics

The exact inventory requires independent adjustment or muting of the relevant audio classes, including at minimum music, voice-over, active gameplay-critical effects, background/ambient effects, narration, and voice chat where those classes exist. Spatial audio is mapped as an applicable directional-sound option; stereo output is mapped to a mono conversion option sent to both channels.

Audio events of at least three seconds are mapped to a player-pause requirement when pausing is applicable, while short events and real-time multiplayer gameplay remain explicit exceptions. A separate clause requires an option to lower or mute game audio automatically when assistive-technology audio output is detected. These controls remain `NOT_RUN` evidence obligations.

### 3.5 XAG 106 — narration, focus, external readers, media, and tables

The inventory maps core UI text/state to platform screen-reader or speech-synthesis support, function-and-input text alternatives for interactable elements, enumeration/state narration for composite controls, equivalent auditory text alternatives for informative non-text content, purpose/operation alternatives for graphics acting as controls, and suppression of purely decorative content from narration.

Focus and narration behavior are separate mechanical obligations: focus order follows meaning/operation (falling back to visual flow where independent), linear one-axis menus loop in both directions unless structurally multidirectional, narration can be quickly cancelled/repeated across input methods, changing focus interrupts obsolete narration, and narration exposes rate/pitch controls. Context changes should be player-initiated where possible and the new context narrated; user-relevant state/value/timed-event changes are narrated at a non-interfering cadence.

Where an external screen reader is supported, the page is atomized into main-language exposure, embedded-language change exposure with explicit source exceptions, alt-text wording rules, markup validity, and programmatic UI name/role/state/property/value semantics. Time-based media receives descriptive text alternatives, while live media can use a sufficient descriptive title rather than continuous real-time value narration. Tables require screen-narration accessibility and programmatic row/column header association. Pronunciation support for proper names/technical or indeterminate-language terms is a distinct record.

## 4. Evidence and gap routing

Every new atomic record resolves to a named evidence requirement and one page-scoped gap record. The evidence catalog distinguishes contrast/high-contrast/color-cue evidence, multisensory/narration/dialogue evidence, caption presentation/UGC/transcript/sign-language evidence, audio controls/pause/ducking evidence, focus and external-reader evidence, and time-media/table evidence.

All of those empirical requirements are `NOT_RUN`. The page gaps `ACC-GAP-XAG102` through `ACC-GAP-XAG106` remain `OPEN`: the source mapping is now explicit, but product applicability and implementation evidence have not been acquired or independently reviewed.

## 5. Mechanical validation contract

`ACCESSIBILITY-POLICY-VALIDATOR-v3` composes the exact v2 blob with this bounded overlay and requires:

1. exact first-party source/version/observed-date binding for XAG 102–106;
2. exact set-and-count equality between each atomic page and its expected clause inventory;
3. rejection of duplicate, missing, or extra clause IDs;
4. deterministic applicability plus a nonempty trigger for every conditional clause;
5. explicit exceptions wherever source semantics make a clause conditional or exempted;
6. resolvable evidence-requirement and gap references for every atomic clause;
7. XAG 108–123 to remain `GUIDELINE_SUMMARY_ONLY`;
8. every new empirical evidence requirement to remain `NOT_RUN` until separately produced; and
9. aggregate `IR-BLOCKER-ACCESSIBILITY-CURRENT` derivation only after mapping and empirical predicates, with the current expected state still `OPEN`.

The expected composed inventory is 28 inherited + 77 new = **105** atomic clauses. Adversarial fixtures reject an omitted expected clause, an unregistered extra clause, duplicate identity, triggerless conditional, dangling evidence/gap refs, unauthorized XAG 108–123 promotion, premature `mapping_complete: true`, and any empirical PASS claim while evidence remains `NOT_RUN`.

## 6. Finding disposition and bounded self-review

`W2-REV-M02` is **PARTIALLY_ADVANCED / OPEN_BOUNDED**. This packet addresses the atomic-source-mapping subcondition for XAG 102–106 only. It does not close the formal MAJOR because XAG 108–123 remain summary-only and required empirical accessibility evidence remains absent.

Bounded self-review result:

- unresolved mapping defect identified in XAG 102–106 inventory: **0 known**;
- new atomic clauses: **77**;
- expected composed atomic clauses: **105**;
- XAG 108–123 remain summary-only: **PASS**;
- empirical accessibility evidence remains `NOT_RUN`: **PASS**;
- `mapping_complete` remains false: **PASS**;
- `IR-BLOCKER-ACCESSIBILITY-CURRENT` remains OPEN: **PASS**;
- readiness/implementation/release/legal/Valve-certification/canonical authority claimed: **NO**;
- fresh independent scoped review required: **YES**.

Producer self-review is not independent acceptance and does not satisfy the downstream review gate.

## 7. Downstream contract

A fresh independent scoped reviewer must attack the exact Issue #240 terminal head and reconstruct the v3 policy from the exact v2 predecessor. At minimum the reviewer must independently check the 77-member XAG 102–106 inventory against the current Microsoft implementation-guideline surfaces, verify load-bearing thresholds/conditions/exceptions, attack applicability/trigger and evidence/gap reference totality, and confirm that no empirical or aggregate readiness authority was upgraded.

A clean review makes this packet eligible only for whatever separately authorized noncanonical integration route the repository permits. It does not close `W2-REV-M02`; later bounded work still must address XAG 108–123 and the required empirical accessibility evidence. Every eventual `main` integration remains squash-only and separate from canonicalization/readiness authority.
