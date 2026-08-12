# W2-ACC-01 — Current accessibility and selected-platform requirements mapping

**Mission:** `W2-ACC-01` / Issue #81  
**Branch:** `planning/issue-81`  
**Base main:** `c7ba185ed9667b717794c19eaa0834ca41aa4c78`  
**Authoritative foundation:** `docs/planning/WAVE-1-FOUNDATIONS-v1.md` blob `a252e3c93702f3ebaecd3e888944a23dbe1b0e1d`  
**W2-PLAT-01 prerequisite status:** Issue #79 terminal producer work `695d3cd1bc5a017e780db8016ffefa2379d4103d`  
**Substantive corrected platform input:** W2-REM-PLAT-01 / Issue #92 head/work `9d51099be4d53eff876104f482e3c163d34519e3`; corrected platform report blob `d6a20c2200cedad97ede36beb9871d420ca7a8ca`; source-record blob `f2a9333436c9cbc4fe91ec71507997f46f2247e4`  
**External accessibility/platform sources observed:** `2026-08-12`  
**Task class / decision state:** `PLANNING_RESEARCH / EVIDENCE_REQUIRED`  
**Required independent review:** `W2-REV-01`

## 1. Scope and authority boundary

This mission maps current authoritative accessibility guidance and current selected-platform compatibility requirements onto the corrected `PLAT-PC-FIRST-R1` planning envelope:

- supported Windows 11 64-bit desktop as the primary continuous evidence target;
- the normal Windows build on Steam Deck / SteamOS via Proton as a required compatibility, controller, small-display, and portability evidence target;
- macOS, native Linux desktop, additional PC storefronts, consoles, and mobile remain conditional or deferred exactly as the corrected platform packet declares.

This report deliberately separates three authority classes:

1. **`PLATFORM_COMPATIBILITY_REQUIRED`** — current public Valve Steam Deck compatibility criteria that are mechanically relevant to the selected Deck evidence target.
2. **`CURRENT_ACCESSIBILITY_BEST_PRACTICE`** — Microsoft Xbox Accessibility Guidelines (XAG) v3.2. Microsoft explicitly describes XAGs as design/development/test best practices and not a checklist proving legal or compliance requirements.
3. **`LEGAL_OR_PARTNER_CERTIFICATION_UNKNOWN`** — jurisdiction-specific legal obligations and partner-gated console certification requirements not established by the selected platform scope or current authoritative inputs.

No XAG item is represented as law. No public Deck criterion is represented as a legal accessibility rule. No unstated console certification requirement is inferred from memory.

`IR-BLOCKER-ACCESSIBILITY-CURRENT` remains **OPEN** at producer completion. This mission proposes a current machine-identifiable mapping and blocker-resolution packet; only the declared independent review/synthesis/verification chain may grant stronger authority.

## 2. Exact input provenance

### 2.1 Platform prerequisite chain

Issue #79 (`W2-PLAT-01`) reached terminal producer `REVIEW_READY` at work/head `695d3cd1bc5a017e780db8016ffefa2379d4103d`. A later independent pre-gate review found source-freshness/provenance defects and routed them to Issue #92 (`W2-REM-PLAT-01`).

Issue #92 reached terminal `REVIEW_READY` at work/head `9d51099be4d53eff876104f482e3c163d34519e3`, with:

- corrected platform report blob `d6a20c2200cedad97ede36beb9871d420ca7a8ca`;
- immutable platform source-record blob `f2a9333436c9cbc4fe91ec71507997f46f2247e4`;
- finding-dispositions blob `03341d3a54225571a1d4b8bfe46aa52b869e2369`.

Issue #79 durably records that the Issue #92 packet supersedes its frozen producer payload as the substantive platform input while retaining Issue #79 as historical/prerequisite provenance. This mission therefore consumes the corrected Issue #92 packet, not the stale source values in the original producer report.

### 2.2 Current platform decision consumed

The corrected platform packet keeps `PLAT-PC-FIRST-R1` as a reversible planning candidate and explicitly requires W2-ACC-01 to test whether its input/display envelope is sufficient. This report does that accessibility mapping without converting the planning candidate into a release promise.

## 3. Current external source register

The normalized facts below are frozen by the eventual Git blob of this report. Live URLs remain external authorities; a later source change is a freshness/reopen event rather than a retroactive rewrite of this candidate.

| Source ID | Authority / source | Version/date evidence | Facts consumed | Authority class |
|---|---|---|---|---|
| `ACC-SRC-XAG-INDEX` | Microsoft Game Dev, Xbox Accessibility Guidelines | XAG v3.2, published 2023-06-08; current index last updated 2026-03-04; observed 2026-08-12 | current guideline set 101–123; XAGs are best practices for design/development/test and are not a legal/compliance checklist | `CURRENT_ACCESSIBILITY_BEST_PRACTICE` |
| `ACC-SRC-XAG-101` | Microsoft XAG 101 Text display | current v3.2 page observed 2026-08-12 | PC/VR default text target 18 px at 1080p / 36 px at 4K; glyph-contained text follows minimum; scaling to 200% without loss of content/function/meaning | `CURRENT_ACCESSIBILITY_BEST_PRACTICE` |
| `ACC-SRC-XAG-102` | Microsoft XAG 102 Contrast | current v3.2 page last updated 2026-03-04; observed 2026-08-12 | standard important text/visual elements 4.5:1; large 3:1; inactive text 3:1; high-contrast mode 7:1; configurable contrast patterns | same |
| `ACC-SRC-XAG-103` | Microsoft XAG 103 Additional channels for visual and audio cues | current v3.2 page observed 2026-08-12 | essential gameplay cues should not depend on only vision/audio/color; multiple sensory channels | same |
| `ACC-SRC-XAG-104` | Microsoft XAG 104 Subtitles and captions | current v3.2 page last updated 2026-03-04; observed 2026-08-12 | spoken content subtitles; important non-speech audio captions; configurable display; caption/subtitle text scalable to at least 200% of minimum default; captions preserve key audio information | same |
| `ACC-SRC-XAG-105` | Microsoft XAG 105 Audio accessibility | current v3.2 page observed 2026-08-12 | separate controllable audio categories, mono support, pause/ducking considerations; audio must not be the only route to essential information | same |
| `ACC-SRC-XAG-106` | Microsoft XAG 106 Screen narration | current v3.2 page observed 2026-08-12 | visual UI/gameplay information necessary to operate/play should be representable aurally through narration | same |
| `ACC-SRC-XAG-107` | Microsoft XAG 107 Input | current v3.2 page observed 2026-08-12 | alternative/configurable input; equivalent functionality; remapping labels follow mappings; avoid exclusive rapid-tap/hold/simultaneous-control barriers; sensitivity configurability | same |
| `ACC-SRC-XAG-108` | Microsoft XAG 108 Game difficulty options | current v3.2 page last updated 2026-03-04; observed 2026-08-12 | multiple/granular ways to reduce barriers; change difficulty without progress loss; regular save, ideally manual + autosave; single-player/local gameplay and cinematics should be pausable outside save/load | same |
| `ACC-SRC-XAG-109` | Microsoft XAG 109 Objective clarity | current v3.2 page last updated 2026-03-04; observed 2026-08-12 | players should be able to understand current goals/objectives and review progress without relying on memory | same |
| `ACC-SRC-XAG-110` | Microsoft XAG 110 Haptic feedback | current v3.2 page last updated 2026-03-03; observed 2026-08-12 | if haptics exist, provide disable/intensity controls; haptics must not be the only information channel | same |
| `ACC-SRC-XAG-111` | Microsoft XAG 111 Audio descriptions | current v3.2 page last updated 2026-03-04; observed 2026-08-12 | FMV/scripted cinematic essential visual context should have optional audio description or bounded alternative evidence when feature exists | same |
| `ACC-SRC-XAG-112` | Microsoft XAG 112 UI navigation | current v3.2 page observed 2026-08-12 | UI navigation should be clear, consistent, and usable through applicable input/assistive routes | same |
| `ACC-SRC-XAG-113` | Microsoft XAG 113 UI focus handling | current v3.2 page last updated 2026-03-04; observed 2026-08-12 | visible focus indicator on focused UI; focus must not disappear/move to invisible/offscreen controls | same |
| `ACC-SRC-XAG-114` | Microsoft XAG 114 UI context | current v3.2 page observed 2026-08-12 | UI must provide sufficient purpose/action/outcome context before interaction | same |
| `ACC-SRC-XAG-115` | Microsoft XAG 115 Error messages and destructive actions | current v3.2 page last updated 2026-03-04; observed 2026-08-12 | identify/correct input errors before permanent/destructive action; do not make button-hold the only destructive confirmation route | same |
| `ACC-SRC-XAG-116` | Microsoft XAG 116 Time limits | current v3.2 page observed 2026-08-12 | provide sufficient time; avoid a precise/timed interaction as the only route where alternatives/pause/skip can remove the barrier | same |
| `ACC-SRC-XAG-117` | Microsoft XAG 117 Visual distractions and motion settings | current v3.2 page last updated 2026-03-04; observed 2026-08-12 | pause/stop moving/blinking/auto-updating content; configurable camera/screen motion such as shake/bob/motion effects where relevant | same |
| `ACC-SRC-XAG-118` | Microsoft XAG 118 Photosensitivity | current v3.2 page last updated 2026-03-03; observed 2026-08-12 | all games should be tested for photosensitive seizure triggers, including unintended flashing; avoid dangerous flash/pattern conditions | same |
| `ACC-SRC-XAG-119` | Microsoft XAG 119 Speech-to-text/text-to-speech chat | current v3.2 page last updated 2026-03-04; observed 2026-08-12 | if communication exists, provide accessible text/voice transformations, accessible text entry, and narration of incoming text where applicable | same |
| `ACC-SRC-XAG-120` | Microsoft XAG 120 Communication experiences | current v3.2 page last updated 2026-03-04; observed 2026-08-12 | if communication exists, the whole navigation/configuration/use path must be accessible, not only the chat widget | same |
| `ACC-SRC-XAG-121` | Microsoft XAG 121 Accessible feature documentation | current v3.2 page observed 2026-08-12 | accessibility features/settings should be discoverable before purchase and usable as post-purchase guidance | same |
| `ACC-SRC-XAG-122` | Microsoft XAG 122 Accessible customer support | current v3.2 page last updated 2026-03-04; observed 2026-08-12 | if support is offered, provide accessible/discoverable support routes using multiple methods | same |
| `ACC-SRC-XAG-123` | Microsoft XAG 123 Mental health best practices | current v3.2 page last updated 2026-03-04; observed 2026-08-12 | if sensitive content/mental-health portrayals exist, provide discoverable warnings/context, appropriate bypass/customization where applicable, and respectful handling | same |
| `ACC-SRC-VALVE-DECK` | Valve Steamworks, Steam Deck and Steam Machine Compatibility Review | live public checklist observed 2026-08-12 | controller access to all content; correct active glyphs; controller-usable required text entry; default Deck 30 fps at 800p; no unsupported-device warning; launcher must satisfy requirements if used; supported Deck resolution; interface text >=9 px at 1280x800, with 12 px recommended; Windows builds may be exercised through Proton | `PLATFORM_COMPATIBILITY_REQUIRED` for the selected Deck evidence target |

### 3.1 Authoritative URLs

- XAG index: `https://learn.microsoft.com/en-us/xbox/accessibility/guidelines`
- Individual XAGs: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/{101..123}`
- Valve Deck/Steam Machine compatibility: `https://partner.steamgames.com/doc/steamhardware/compat`

These sources are intentionally public and current for the scope claimed here. Partner-gated Xbox/PlayStation/Nintendo certification material is **not** admitted because those platforms remain deferred and the public platform packet explicitly marks detailed requirements unknown until access/promotion.

## 4. Applicability model

Each candidate guideline is assigned one state:

- `APPLICABLE_BASELINE` — maps to the current Windows + Deck evidence envelope regardless of unresolved product details.
- `APPLICABLE_IF_FEATURE_PRESENT` — becomes required evidence immediately when the named feature exists; architecture must avoid making future compliance impossible.
- `APPLICABLE_RELEASE_SURFACE` — evidence is required when a release/store/support surface exists, but it is not yet a gameplay-implementation precondition.
- `DEFERRED_PLATFORM_SCOPE` — not applicable to the selected current scope; promotion reopens mapping.
- `UNKNOWN_LEGAL_SCOPE` — no legal conclusion is made; exact jurisdiction/product/service scope is required before a legal gate can be claimed.

`NOT_APPLICABLE` is not used merely because implementation has not started. Missing implementation/evidence for an applicable item remains `NOT_RUN`, a named gap, or `INCONCLUSIVE` under the normal evidence model.

## 5. Hard selected-platform requirements — Steam Deck evidence target

| Requirement ID | Current Valve requirement | Applicability | Architecture/task implication | Required evidence | Current state |
|---|---|---|---|---|---|
| `ACC-DECK-01` | default controller configuration provides access to all content | `APPLICABLE_BASELINE` | semantic action layer; complete controller path through gameplay/settings/errors/launch surface | controller-only representative core-flow replay + unreachable-action scan | `GAP_OPEN` |
| `ACC-DECK-02` | on-screen glyphs match active input | same | glyphs data-driven from semantic bindings, never baked platform-specific prompts | device-switch capture + remap/glyph consistency checks | `GAP_OPEN` |
| `ACC-DECK-03` | required text entry usable with controller in the user's language | same | text-entry abstraction supports Steam on-screen keyboard or equivalent built-in controller route | controller-only name/save/text-entry fixture on Deck/SteamOS | `GAP_OPEN` |
| `ACC-DECK-04` | default Deck configuration produces playable 30 fps at 800p | same | representative default preset must be explicit and reproducible; performance separate from correctness | retained performance envelope on exact Deck/build/settings/scenario | `GAP_OPEN` |
| `ACC-DECK-05` | no unsupported Deck/Linux hardware/software warning | same | platform-detection/error text must not falsely reject supported target | launch capture + warning/assertion scan on exact Deck/SteamOS environment | `GAP_OPEN` |
| `ACC-DECK-06` | launcher, if present, must meet the same controller/access criteria | `APPLICABLE_IF_FEATURE_PRESENT` | prefer no required launcher; any launcher becomes part of accessibility/compatibility core flow | launcher controller/text/display evidence or explicit `NOT_APPLICABLE` because no launcher exists | `FEATURE_UNKNOWN` |
| `ACC-DECK-07` | game runs at a Deck-supported resolution; Valve recommends 1280x800 preferred / 1280x720 | `APPLICABLE_BASELINE` | resolution/scale-aware UI; no assumptions tied only to desktop aspect/size | 1280x800 primary capture + 1280x720 bounded smoke where supported | `GAP_OPEN` |
| `ACC-DECK-08` | interface text easily readable; absolute approval floor is 9 px character height at 1280x800, 12 px recommended | same | automated/inspectable text metrics; layout prevents clipping at larger configured sizes | full representative screen corpus metric scan + manual Deck-distance readability review | `GAP_OPEN` |
| `ACC-DECK-09` | selected envelope exercises Windows build through Proton when no native Linux build exists | same due corrected platform scope | OS/platform adapters cannot leak into canonical save/input/UI meaning | exact Windows-build-on-Deck launch/core-flow evidence, Proton failures separately classified | `GAP_OPEN` |

These Valve checks are necessary for the selected Deck evidence target. They do not assert a guaranteed future `Verified` rating or a launch commitment.

## 6. XAG v3.2 applicability matrix

The XAG authority class is best-practice, not legal compliance. The matrix is intentionally machine-identifiable so a downstream verifier can distinguish a mapped obligation from a deferred feature.

| XAG | Topic | Applicability | Everfield obligation / evidence mapping | Current gap or explicit condition |
|---|---|---|---|---|
| 101 | Text display | `APPLICABLE_BASELINE` | text is live UI, not baked into art where avoidable; PC/VR 18 px at 1080p best-practice baseline; scale to 200% without lost meaning/function; glyph-contained text scales with text | `ACC-GAP-TEXT-01` engine/UI text metrics and 200% layout evidence not measured |
| 102 | Contrast | `APPLICABLE_BASELINE` | important standard text/elements target 4.5:1, large 3:1, inactive text 3:1; high-contrast mode target 7:1; do not encode meaning only by color | `ACC-GAP-CONTRAST-01` automated contrast/capture process and theme evidence not selected |
| 103 | Additional sensory channels | `APPLICABLE_BASELINE` | essential gameplay state/cues have at least one meaningful alternative to a single visual/audio/color channel; semantics emitted independently of presentation | `ACC-GAP-CUES-01` gameplay cue taxonomy not yet defined |
| 104 | Subtitles/captions | `APPLICABLE_IF_FEATURE_PRESENT` | all spoken content subtitled; important non-speech audio captioned if it conveys information; configurable/scalable presentation and pre-first-audio access | condition: dialogue/FMVs/informational audio exist; media/content scope not yet fixed |
| 105 | Audio accessibility | `APPLICABLE_IF_FEATURE_PRESENT` | separate relevant volume categories; mono option where stereo content matters; essential information has non-audio route; pause/ducking policy for interruptive media | condition: final audio categories/content unknown |
| 106 | Screen narration | `APPLICABLE_BASELINE` as architecture/evidence target | semantic UI structure, labels, values, state changes, focus and necessary visual information expose a narration-capable representation; representative no-vision UI flow test after engine choice | `ACC-GAP-NARRATION-01` engine/framework narration support and gameplay-semantic coverage unmeasured |
| 107 | Input | `APPLICABLE_BASELINE` | semantic actions; remapping; visible bindings/glyph refresh; configurable alternatives for holds/rapid repeat/simultaneous inputs; sensitivity where analog/precision exists; keyboard and controller paths for core functionality | `ACC-GAP-INPUT-01` concrete action vocabulary and assist settings await gameplay/engine evidence |
| 108 | Difficulty/options/save/pause | `APPLICABLE_BASELINE` as design-system constraint, feature details conditional | challenges/assists represented as separable parameters rather than one irreversible mode; difficulty changes do not corrupt progress; regular save/recovery; single-player/local gameplay and cinematics pausable outside bounded save/load operations | `ACC-GAP-DIFFICULTY-01` core challenge model unknown; `ACC-GAP-SAVEPause-01` save/autosave/pause policy not yet specified/implemented |
| 109 | Objective clarity | `APPLICABLE_IF_FEATURE_PRESENT` | if progression/objectives exist, expose current objective/progress/history so returning players need not rely on memory | condition: objective/progression presentation not yet defined |
| 110 | Haptic feedback | `APPLICABLE_IF_FEATURE_PRESENT` | haptics disable/intensity control; no required information only in haptics | condition: haptics not yet selected |
| 111 | Audio description | `APPLICABLE_IF_FEATURE_PRESENT` | if FMV/scripted cinematics carry essential visual narrative/context, provide optional audio-description path or explicitly reviewed alternative | condition: cinematic model unknown |
| 112 | UI navigation | `APPLICABLE_BASELINE` | deterministic, consistent navigation graph across keyboard/controller; no unreachable/cyclic trap; route to accessibility settings available without inaccessible prerequisite | `ACC-GAP-UI-01` representative UI/navigation graph not implemented |
| 113 | UI focus handling | `APPLICABLE_BASELINE` | one clear visible focus; never focus hidden/offscreen controls; dialog/modal focus constrained/restored deterministically | same `ACC-GAP-UI-01` plus focus-state capture required |
| 114 | UI context | `APPLICABLE_BASELINE` | controls expose purpose, state, consequences and destination before activation; semantic labels independent of icons/color alone | `ACC-GAP-UI-CONTEXT-01` semantic-label/context contract not yet implemented |
| 115 | Errors/destructive actions | `APPLICABLE_BASELINE` | errors identify recovery; destructive/permanent actions are confirmable/correctable; button-hold is not the only confirmation route; delete/overwrite/reset operations retain recoverability policy | `ACC-GAP-DESTRUCTIVE-01` destructive action catalog/recovery policy not yet frozen |
| 116 | Time limits | `APPLICABLE_IF_FEATURE_PRESENT` with baseline timing architecture | UI/gameplay timers must declare why they exist and whether pause/extension/disable/skip is allowed; precise timed input cannot become an accidental sole route | `ACC-GAP-TIMING-01` timed mechanics/notification lifetimes unknown |
| 117 | Visual distractions/motion | `APPLICABLE_IF_FEATURE_PRESENT` | moving/blinking/auto-updating presentation can be paused/stopped where guidance applies; camera shake/bob/motion effects have reduction/disable controls where present | `ACC-GAP-MOTION-01` camera/effects stack not selected |
| 118 | Photosensitivity | `APPLICABLE_BASELINE` | every representative build/content set gets photosensitivity analysis even without intentional flashing; failures quarantine affected content until corrected/retested | `ACC-GAP-PHOTO-01` tool/process and retained evidence format not selected |
| 119 | STT/TTS communication | `APPLICABLE_IF_FEATURE_PRESENT` | if player communication exists, speech-to-text/text-to-speech/text-entry/narration paths are mapped and configurable | condition: multiplayer/chat/product scope unknown |
| 120 | Communication experiences | `APPLICABLE_IF_FEATURE_PRESENT` | if communication exists, navigation to, configuration of, and use of the entire communication path must satisfy relevant UI/input/text/audio requirements | same multiplayer/chat condition |
| 121 | Accessible feature documentation | `APPLICABLE_RELEASE_SURFACE` | before a purchase/release surface, publish accurate discoverable accessibility feature/settings documentation generated from verified feature evidence, not marketing inference | `ACC-GAP-DOC-01` no release/store documentation surface exists yet |
| 122 | Accessible customer support | `APPLICABLE_IF_FEATURE_PRESENT` / release surface | if project/publisher offers customer support, provide multiple accessible/discoverable methods and accessible web support | condition: support model not defined |
| 123 | Mental health best practices | `APPLICABLE_IF_FEATURE_PRESENT` | if sensitive themes/phobias/trauma/addictive behavior/mental-health portrayals exist, classify content, provide appropriate discoverable warnings and bypass/customization where feasible, and evidence respectful handling | `ACC-GAP-SENSITIVE-01` narrative/content taxonomy not yet defined |

## 7. Cross-cutting architecture obligations

### 7.1 Input and interaction

The current mapping requires a **semantic action layer** rather than device-button logic as gameplay meaning. It must support:

- keyboard/mouse and controller routes for the current Windows + Deck core flow;
- remapping with labels/glyphs derived from the actual active mapping;
- controller-only text entry;
- alternative interaction policies for hold, rapid repeat, simultaneous controls and precision/sensitivity where those mechanics exist;
- device switching without stale prompts or lost focus;
- accessibility settings reachable before a player must complete a potentially inaccessible core interaction.

This aligns both the selected Deck hard checks and XAG 107/112–115 without making an engine-specific API canonical.

### 7.2 Semantic UI / narration

UI data should expose at minimum:

- stable control identity;
- role/type;
- accessible label;
- current value/state;
- focus order and visible focus;
- enabled/disabled reason where relevant;
- action consequence/context;
- change/error/status announcements;
- modal ownership and deterministic focus restoration.

The exact platform narration API is an engine/platform adapter. The semantic information is persistent design meaning and must not exist only in rendered pixels.

### 7.3 Text, contrast, scaling, and small-display behavior

The evidence system must distinguish two simultaneous standards:

- **hard selected Deck compatibility floor:** never below 9 px character height at 1280x800, with Valve recommending 12 px where possible;
- **current XAG PC best-practice target:** 18 px at 1080p by default and text/glyph scaling to 200% without lost function/meaning, plus the XAG contrast targets.

Meeting the Deck floor does not prove the broader XAG text/contrast target. Conversely, a desktop 1080p capture does not prove Deck legibility. Both require target-specific retained evidence.

### 7.4 Audio, captions, and cues

Canonical gameplay events should emit semantic cue information before audio/visual/haptic rendering. That permits:

- visual + audio + optional haptic representations of important state;
- captions/subtitles driven from exact dialogue/cue identity rather than transcription as an afterthought;
- alternate sensory channels without duplicating gameplay logic;
- configurable audio categories and mono/ducking/pause policies when audio features exist.

### 7.5 Timing, pause, save, and recovery

Timing/pause/save is part of the accessibility architecture, not solely a quality-of-life feature.

Required design hooks:

- distinguish simulation/gameplay time, presentation time, UI timeout, network/real-time authority, and non-pausable save/load critical sections;
- every time limit/auto-dismiss declares accessibility behavior (extend/disable/pause/replay/skip/not applicable with reason);
- single-player/local gameplay and cinematics must have a pause design unless an explicit reviewed exception exists;
- save/autosave/recovery points preserve enough progress that difficulty/accessibility adjustment does not require destructive restart;
- destructive save/delete/overwrite operations follow XAG 115 recovery/confirmation semantics;
- accessibility settings persist consistently with the project's settings/save model and can be changed without invalidating canonical gameplay state.

### 7.6 Motion and photosensitivity

The rendering/content pipeline needs evidence surfaces for:

- camera shake/bob/motion blur and other motion controls if those effects exist;
- blinking/scrolling/auto-updating UI behavior;
- photosensitivity analysis for representative gameplay/cinematics/UI even when flashing is accidental;
- exact content/build/scenario identity for a failing photosensitivity result so a new locator cannot bypass quarantine.

## 8. Evidence requirements

The downstream evidence model should instantiate explicit checks rather than a single “accessibility score.” Suggested evidence requirement IDs follow.

| Evidence ID | Check | Minimum retained evidence | Failure semantics |
|---|---|---|---|
| `ACC-EV-INPUT-KBM-01` | keyboard/mouse representative core flow | build/input map/replay + failures | required `FAIL/NOT_RUN` gates |
| `ACC-EV-INPUT-CONTROLLER-01` | controller-only representative core flow incl settings/errors/text entry | build/controller map/Deck replay + screenshots/logs | same |
| `ACC-EV-GLYPH-01` | live device/remap glyph correctness | remap/device-switch sequence + captured prompts | stale/wrong glyph = FAIL |
| `ACC-EV-TEXT-DESKTOP-01` | XAG text size/200% scale on representative Windows screens | exact UI corpus, text metrics, before/after captures, clipping report | any required screen below declared target or lost function = FAIL |
| `ACC-EV-TEXT-DECK-01` | Deck 1280x800 text floor/readability | exact UI corpus + pixel metrics + manual Deck-distance review | <9 px = hard platform FAIL |
| `ACC-EV-CONTRAST-01` | contrast/high-contrast theme | exact element/background measurements + tool/version + exceptions | unmet declared XAG target = FAIL in best-practice gate |
| `ACC-EV-NARRATION-01` | semantic narration of representative startup/settings/core UI | exact UI build + traversal transcript/capture + unnamed/unannounced elements | required traversal gap = FAIL/INCONCLUSIVE |
| `ACC-EV-FOCUS-NAV-01` | keyboard/controller focus/navigation graph | graph traversal + hidden/offscreen/trap detection + captures | unreachable/trapped/invisible focus = FAIL |
| `ACC-EV-CUES-01` | essential cue multi-channel coverage | cue registry maps semantic event -> visual/audio/haptic/caption alternatives | essential single-channel-only cue = FAIL |
| `ACC-EV-CAPTIONS-01` | spoken/non-speech information coverage | dialogue/audio cue corpus + subtitle/caption mapping + display settings | applicable missing information = FAIL; feature absent = explicit N/A |
| `ACC-EV-AUDIO-01` | audio categories/mono/essential-info alternatives | settings manifest + playback fixtures | feature-dependent |
| `ACC-EV-SAVE-PAUSE-01` | pause/save/difficulty continuity | deterministic pause/resume + save/reload + difficulty-change fixtures | progress loss or inaccessible non-pausable route = FAIL unless reviewed exception |
| `ACC-EV-TIMING-01` | timers/auto-dismiss/timed input | timer registry + alternative policy + fixture | unexplained required timing-only route = FAIL |
| `ACC-EV-MOTION-01` | motion/distraction controls | settings + capture/replay with effects on/off | feature-dependent |
| `ACC-EV-PHOTO-01` | photosensitivity | tool/version/config + retained analyzed capture + result | required `NOT_RUN`/FAIL gates; tool uncertainty -> INCONCLUSIVE |
| `ACC-EV-DECK-PERF-01` | default 30 fps at 800p | exact device/build/settings/scenario frame evidence | platform FAIL if not met |
| `ACC-EV-DOC-01` | public accessibility feature documentation | generated/verified feature matrix vs actual build | release-surface gate only |

For all applicable checks:

- `NOT_RUN` is not `NOT_APPLICABLE`;
- a feature-conditional requirement becomes `NOT_APPLICABLE` only when the exact candidate demonstrates the feature is absent and the condition is explicit;
- manual judgment must record evaluator/tool identity and limits;
- aggregate results cannot average away a required hard platform failure, photosensitivity failure, inaccessible core route, or stale authority source.

## 9. Machine-identifiable current gaps

```yaml
accessibility_gap_register:
  ACC-GAP-TEXT-01:
    state: OPEN
    closes_when: exact Windows and Deck UI text/scaling evidence satisfies declared target-specific checks
  ACC-GAP-CONTRAST-01:
    state: OPEN
    closes_when: contrast/high-contrast evidence tool and representative corpus are implemented and pass
  ACC-GAP-CUES-01:
    state: OPEN
    closes_when: gameplay cue taxonomy exists and essential cues have mapped alternate sensory channels
  ACC-GAP-NARRATION-01:
    state: OPEN
    closes_when: engine/UI semantic narration path passes representative traversal evidence
  ACC-GAP-INPUT-01:
    state: OPEN
    closes_when: semantic action/remap/alternative-input model passes keyboard-mouse and controller core flows
  ACC-GAP-DIFFICULTY-01:
    state: CONDITIONAL_OPEN
    closes_when: core challenge/barrier mechanics are defined and adjustable/assist policies are mapped
  ACC-GAP-SAVEPAUSE-01:
    state: OPEN
    closes_when: pause/save/autosave/recovery/difficulty-change fixtures pass or exact reviewed exceptions exist
  ACC-GAP-UI-01:
    state: OPEN
    closes_when: navigation/focus graph and representative UI are implemented and pass
  ACC-GAP-UI-CONTEXT-01:
    state: OPEN
    closes_when: semantic control purpose/state/consequence contract is evidenced
  ACC-GAP-DESTRUCTIVE-01:
    state: OPEN
    closes_when: destructive/error action catalog has correction/confirmation/recovery evidence
  ACC-GAP-TIMING-01:
    state: CONDITIONAL_OPEN
    closes_when: all actual timers/timed mechanics have explicit accessibility policy and passing evidence
  ACC-GAP-MOTION-01:
    state: CONDITIONAL_OPEN
    closes_when: actual camera/motion/auto-updating effects have disable/reduction/pause evidence
  ACC-GAP-PHOTO-01:
    state: OPEN
    closes_when: photosensitivity analysis tool/process is selected, fingerprinted, retained, and passes representative content
  ACC-GAP-DOC-01:
    state: RELEASE_SURFACE_PENDING
    closes_when: verified accessibility feature documentation exists before a promoted purchase/release surface
  ACC-GAP-SENSITIVE-01:
    state: CONDITIONAL_OPEN
    closes_when: actual narrative/content taxonomy determines XAG-123 applicability and mapped controls/evidence
  ACC-GAP-COMMS-01:
    state: CONDITIONAL_OPEN
    closes_when: product decision explicitly excludes player communication or XAG-119/120 evidence passes
  ACC-GAP-LEGAL-SCOPE-01:
    state: UNKNOWN_NOT_CLAIMED
    closes_when: promoted release jurisdictions/services have authoritative legal applicability research through an authorized legal-evidence task
```

The gap register is intentionally stricter than “implementation has not started.” It tells downstream planners which architecture/evidence work is mandatory, conditional, release-surface-specific, or outside this mission's legal authority.

## 10. `IR-BLOCKER-ACCESSIBILITY-CURRENT` candidate resolution

Producer assessment:

```yaml
blocker_resolution_candidate:
  blocker_id: IR-BLOCKER-ACCESSIBILITY-CURRENT
  current_authority_state: OPEN
  mapping_state: MAPPED_PENDING_INDEPENDENT_REVIEW
  selected_platform_requirements_mapped: true
  current_xag_v3_2_guidelines_classified: true
  every_applicable_or_conditional_guideline_has_evidence_or_gap: true
  stale_remembered_checklist_used: false
  legal_compliance_claimed: false
  partner_gated_console_requirements_claimed: false
  required_next_authority: W2-REV-01
```

The machine-identifiable **producer candidate** is therefore that the current mapping obligation has been met at research level, but the blocker remains OPEN until the declared independent authority verifies/dispositions the candidate. Implementation gaps do not make the mapping incomplete; they are precisely the output that subsequent engine/task/evidence planning must consume.

## 11. Downstream interfaces

### W2-ENG-03 / engine comparative spikes

Engine spikes must evidence, not merely advertise:

- semantic keyboard/mouse/controller input + remapping;
- live glyph switching;
- semantic/narration-capable UI metadata and focus control;
- text sizing/scaling and layout behavior;
- Windows + Deck/Proton build/run/capture;
- accessibility settings persistence;
- headless/automatable accessibility-related UI/capture hooks where available;
- profiling and retained artifact identity for performance/photosensitivity/media evidence.

An engine that cannot expose the semantic UI/input/capture surfaces required above can be rejected even if it exports a Windows build.

### Task planning

Future implementation tasks should not be “make game accessible” monoliths. They should be split by durable seam/evidence requirement, for example:

- semantic input/remap/glyph model;
- semantic UI/focus/narration model;
- text/style/contrast/settings model;
- caption/cue/audio semantics;
- save/pause/timing policy;
- motion/photosensitivity pipeline;
- accessibility feature documentation generated from verified state.

## 12. Failure modes and controls

| Failure mode | Consequence | Control |
|---|---|---|
| XAG treated as law/certification | unsupported compliance claim | authority-class field; explicit no-legal-compliance statement |
| Deck hard floor confused with broad accessibility target | 9 px becomes universal design target | separate target-specific Valve floor and XAG best-practice evidence |
| `NOT_RUN` changed to N/A because feature not implemented yet | missing accessibility work disappears | explicit applicability state + gap register |
| accessibility reduced to menu settings | gameplay/save/timing/cues remain barriers | cross-cutting semantic/timing/save evidence requirements |
| controller checkbox theater | menus/text/error flows still require mouse | controller-only full representative core-flow replay |
| screen narration bolt-on | rendered pixels lack semantics | semantic UI contract before engine-specific narration adapter |
| photosensitivity only checked when flashing is intentional | accidental hazard ships | XAG-118 baseline check for representative content |
| score/aggregate masks a hard failure | false PASS | hard platform/accessibility checks retain individual gate state |
| platform scope changes silently | wrong obligations retained | reopen on target promotion/removal |
| XAG/Valve source drifts | stale mapping used forever | exact source/version/date + freshness triggers |

## 13. Freshness and reopen conditions

Revalidate this mapping when any of the following occurs:

- Microsoft publishes a new XAG version or materially changes a load-bearing guideline page;
- Valve changes Steam Deck compatibility criteria, display/text requirements, hardware assumptions, controller/text-entry behavior, or Proton review semantics;
- the corrected platform candidate changes Windows/Deck status or promotes macOS/native Linux/console/mobile into a hard target;
- game scope adds/removes dialogue, FMV, haptics, multiplayer communication, timed mechanics, sensitive content, or customer-support/purchase surfaces;
- engine selection changes semantic input/UI/narration/capture capabilities;
- target release jurisdiction/service scope becomes concrete enough that legal accessibility applicability is material;
- a photosensitivity/accessibility test tool changes version/threshold/calibration;
- W2-REV-01 finds a BLOCKER/MAJOR against this mapping.

Current-source recheck is mandatory before engine ADR/readiness verification and again before any release/accessibility marketing claim whose truth depends on these records.

## 14. Open questions

1. Which engine/UI stack can expose semantic narration/focus metadata without coupling canonical gameplay state to platform APIs?
2. What exact photosensitivity analysis tool/version and capture protocol will become authoritative project evidence?
3. What is Everfield's core challenge model, and which difficulty/assist variables preserve intended experience while reducing barriers?
4. What save/autosave cadence and rewind/recovery semantics best satisfy both deterministic persistence and accessibility?
5. Will the product contain spoken dialogue/FMVs, informational audio, haptics, player communication, time-critical mechanics, or sensitive narrative content?
6. Which accessibility settings must be available before first-run media/gameplay, and how are they persisted/migrated?
7. Which release jurisdictions/services will require a separate legal accessibility applicability analysis?
8. How will accessible feature documentation be generated from verified build evidence so marketing cannot drift from implementation?

## 15. Producer acceptance check

Against Issue #81 acceptance criteria:

- exact source/version/date for current authoritative accessibility/platform sources: **PASS**;
- corrected W2-PLAT-01 substantive input bound by immutable SHA/blob provenance: **PASS**;
- every XAG v3.2 guideline classified with applicability rationale: **PASS**;
- every applicable/conditional guideline has mapped architecture/task evidence or explicit gap/condition: **PASS**;
- hard selected Deck compatibility requirements mapped separately from best-practice guidance: **PASS**;
- input/UI/text/media/timing/save/pause/interaction/evidence obligations mapped: **PASS**;
- `NOT_RUN` versus `NOT_APPLICABLE` distinction preserved: **PASS**;
- current gaps/blocker resolution machine-identifiable: **PASS**;
- stale remembered checklist used as evidence: **NO**;
- legal/certification conclusions outside current authority: **NOT CLAIMED**;
- implementation/readiness/canonicalization authority: **NOT CLAIMED**;
- required independent critique: **`W2-REV-01` remains required**.

**Producer disposition:** `REVIEW_READY_CANDIDATE / EVIDENCE_REQUIRED`. The mapping is ready for independent adversarial review after exact terminal provenance is bound; it is not a legal compliance certificate, Valve compatibility result, or implementation-readiness decision.
