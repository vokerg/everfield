# Issue #81 handoff — W2-ACC-01

**Mission:** `W2-ACC-01`  
**Issue:** #81  
**Branch:** `planning/issue-81`  
**Ownership generation:** Issue #81 comment `5270537366`  
**Base main:** `c7ba185ed9667b717794c19eaa0834ca41aa4c78`  
**W2-PLAT-01 prerequisite producer:** Issue #79 head/work `695d3cd1bc5a017e780db8016ffefa2379d4103d`  
**Substantive corrected platform input:** W2-REM-PLAT-01 / Issue #92 head/work `9d51099be4d53eff876104f482e3c163d34519e3`  
**Corrected platform report blob:** `d6a20c2200cedad97ede36beb9871d420ca7a8ca`  
**Platform source-record blob:** `f2a9333436c9cbc4fe91ec71507997f46f2247e4`  
**Accessibility report:** `docs/planning/wave-2/research/accessibility-current-requirements.md`  
**Accessibility report blob:** `cd97806a06cd2aa3f97689ab7c32b3b631449b09`  
**External accessibility/platform research observed:** `2026-08-12`  
**Intended terminal state:** `REVIEW_READY`  
**Required formal review:** `W2-REV-01`

## Completed work

Produced the current accessibility/selected-platform requirements mapping for the corrected `PLAT-PC-FIRST-R1` planning envelope.

The report:

- consumes the exact corrected Issue #92 platform packet while retaining Issue #79 as immutable prerequisite provenance;
- separates `PLATFORM_COMPATIBILITY_REQUIRED`, `CURRENT_ACCESSIBILITY_BEST_PRACTICE`, and `LEGAL_OR_PARTNER_CERTIFICATION_UNKNOWN` authority classes;
- maps current Microsoft Xbox Accessibility Guidelines v3.2, XAG 101–123, from current first-party pages observed on 2026-08-12;
- maps current public Valve Steam Deck compatibility requirements relevant to the selected Deck evidence target;
- assigns every XAG guideline an explicit applicability class and an architecture/evidence obligation or explicit feature/release/legal gap;
- records hard Deck evidence checks separately from XAG best-practice targets so the Deck 9 px text floor cannot be mistaken for the broader accessibility target;
- defines cross-cutting semantic input, semantic UI/narration, text/contrast/scaling, cue/audio/caption, timing/save/pause, motion, and photosensitivity architecture obligations;
- defines explicit `ACC-EV-*` evidence requirements rather than an aggregate accessibility score;
- defines a machine-identifiable `ACC-GAP-*` gap register;
- records a producer candidate for `IR-BLOCKER-ACCESSIBILITY-CURRENT` as `MAPPED_PENDING_INDEPENDENT_REVIEW` while keeping the actual blocker authority state `OPEN`;
- keeps legal accessibility applicability and partner-gated certification requirements explicitly outside current authority.

## Current authoritative source posture

### Microsoft XAG

The current Microsoft XAG index states XAG **v3.2**, published 2023-06-08, with the index last updated 2026-03-04. The report uses XAG as current design/development/test **best-practice guidance**, not as law or a legal/certification checklist.

Every guideline 101–123 has a source record, applicability state, and mapped evidence/gap.

### Valve Steam Deck

The current public Valve compatibility checklist is mapped as hard compatibility evidence for the selected Deck target, including:

- controller access to all content;
- active glyph correctness;
- controller-usable required text entry;
- default playable 30 fps at 800p;
- no unsupported-device warning;
- launcher compatibility when a launcher exists;
- supported Deck resolution behavior;
- interface text absolute approval floor of 9 px character height at 1280x800, with 12 px recommended;
- Windows-build execution through Proton in the selected evidence envelope.

The report does not claim a guaranteed future Steam Deck `Verified` rating or a release-platform promise.

## Producer self-review correction

The initial report draft overstated XAG 116 by allowing its timing guidance to read as applying to core gameplay mechanics.

The final report corrects that before terminalization:

- XAG 116 is limited to applicable non-core/UI time limits such as notifications, auto-advancing messages, UI input windows, and pause-at-rest behavioral menus;
- the report explicitly records that Microsoft's current XAG 116 page excludes core gameplay mechanics and platform-specific timing windows;
- core gameplay timing barriers are mapped through XAG 108 difficulty/assist design instead;
- `ACC-EV-TIMING-01` requires each timer to bind its exact authority class (`XAG116_NONCORE_UI`, `XAG108_CORE_DIFFICULTY_ASSIST`, or another exact source);
- the project may still require every timer to declare accessibility behavior, but that is labeled as an Everfield architecture rule derived from the combined mapping rather than falsely attributed to XAG 116.

## Key machine-identifiable gaps

Open baseline gaps include:

- text/scaling evidence;
- contrast/high-contrast evidence;
- semantic gameplay cue taxonomy;
- narration-capable semantic UI evidence;
- semantic/remappable input evidence;
- save/pause/recovery evidence;
- UI navigation/focus/context evidence;
- destructive-action recovery evidence;
- photosensitivity tooling/evidence.

Conditional gaps cover difficulty/challenge mechanics, non-core timing, motion effects, sensitive content, and communication. Release-surface documentation remains pending until a purchase/release surface exists. Legal accessibility scope is explicitly `UNKNOWN_NOT_CLAIMED` until a separate authorized legal-evidence task has concrete jurisdiction/service scope.

## Self-review

Final producer self-review against Issue #81 acceptance criteria and the canonical Wave-1 foundation:

- unresolved BLOCKER: 0;
- unresolved MAJOR: 0;
- correction-requiring MINOR: 0;
- exact platform prerequisite and corrected-input provenance: PASS;
- current XAG version/date/source evidence: PASS;
- every XAG 101–123 classified with applicability rationale: PASS;
- every applicable/conditional guideline has mapped evidence or explicit gap: PASS;
- selected Deck hard requirements mapped separately from best-practice guidance: PASS;
- input/UI/text/media/timing/save/pause/interaction/evidence obligations: PASS;
- `NOT_RUN` versus `NOT_APPLICABLE`: preserved;
- XAG 116 core-gameplay overreach: corrected before terminalization;
- machine-identifiable gap/blocker candidate: PASS;
- stale remembered checklist used as evidence: NO;
- legal/certification conclusions outside current authority: NOT CLAIMED;
- implementation/readiness/canonicalization authority: NOT CLAIMED;
- required formal review remains `W2-REV-01`: PASS.

## Remaining risks / open questions

- engine/UI narration and semantic focus capabilities are not yet measured;
- photosensitivity tool/version/capture protocol is not selected;
- actual challenge/difficulty/save/autosave semantics are not yet designed;
- dialogue/FMVs/audio/haptics/player communication/timed mechanics/sensitive narrative content remain product-conditional;
- exact release jurisdictions/services remain unknown, so legal accessibility applicability is not resolved here;
- XAG and Valve criteria are freshness-sensitive and must be rechecked before engine ADR/readiness and later release claims;
- formal aggregate adversarial review has not run.

## Next action

Cold-review exact branch diff against current `main`, verify ownership remains uncontested, then publish owner schema-3 `STATUS(REVIEW_READY)` for the exact final branch head and report/handoff blobs if clean. Freeze the producer branch after terminal status.

Do **not** interpret this producer research, self-review, a PR, or any future noncanonical main integration as the formal `W2-REV-01` disposition, legal compliance certification, Valve compatibility result, implementation-readiness decision, or canonicalization authority.
