# W2-REV-ACC-03 — degraded-independent scoped review of Issue #240

**Review mission:** `W2-REV-ACC-03` / Issue #243  
**Reviewed producer:** Issue #240 / `W2-REM-ACC-03`  
**Reviewed terminal status:** comment `5290011410`  
**Reviewed head:** `bccd22e35f84a5894586d9494e1963ebdef7dc02`  
**Reviewed work:** `f4671c3c295437a64d82ffc51e228c826fcce40e`  
**Reviewed policy blob:** `9c21efdeed2ddff96d6cc1d0ccf2893b9304ccc4`  
**Reviewed requirements blob:** `3fd5eae49f26da2f357f8a1d337a3f3f3ef0f8fa`  
**Reviewed handoff blob:** `d7bbf3ba74cf4d88cc3935072590e66280bcbea7`  
**Exact predecessor policy blob:** `d4f934d1731800b3966adeae82c4a57b9af737b8`  
**Reviewed PR:** #241, draft, exact head verified  
**Independence profile:** `DEGRADED_SINGLE_AGENT`  
**Trust:** `DEGRADED`  
**Resource-constraint authority:** Issue #5 comment `5244416013`  
**Reopen:** `MULTI_AGENT_OR_ISOLATED_CONTEXT_AVAILABLE`

## Disposition

`CHANGES_NEEDED`

Severity summary: **2 MAJOR / 2 MINOR / 0 BLOCKER** in this bounded review scope.

The packet has a coherent 77-record XAG 102–106 inventory shape, preserves the aggregate fail-closed state, and is cleanly scoped to three producer artifacts. However, the exact source-to-clause semantics are not yet faithful enough for noncanonical integration because several records weaken, narrow, or strengthen the current Microsoft implementation guidance.

## Cold-start and immutability checks

The reviewer fixed the exact identities above before judgment and did not modify Issue #240, PR #241, or `planning/issue-240`. PR #241 was re-read as open/draft at exact head `bccd22e35f84a5894586d9494e1963ebdef7dc02`, base `main@cc973dd5e758bef20ba588ab1440ae82ec1ec2b6`, with exactly three changed files. The predecessor policy on current main is exact blob `d4f934d1731800b3966adeae82c4a57b9af737b8` and declares the inherited exact atomic count of 28.

Fresh source evidence was acquired from the current Microsoft Learn XAG 102, 103, 104, 105, and 106 implementation-guideline pages before reconciling producer rationale. All five current pages report last updated `2026-03-04`.

## Structural attacks that passed

- Declared new inventory cardinality reconstructs as `12 + 8 + 29 + 5 + 23 = 77` for XAG 102–106.
- The predecessor declares 28 exact XAG 101/XAG 107 atoms, yielding declared composed total 105.
- Reviewed diff is bounded to the policy, human-readable requirements, and Issue #240 handoff.
- XAG 108–123 remain `GUIDELINE_SUMMARY_ONLY`.
- `mapping_complete` remains false.
- `empirical_accessibility_pass_claimed` remains false and new evidence requirements remain `NOT_RUN`.
- `IR-BLOCKER-ACCESSIBILITY-CURRENT` remains OPEN.
- No readiness, implementation, release, legal/compliance, Valve-verification, integration, decision, or canonical authority is asserted.

These passes do not cure semantic source-fidelity defects below.

## Findings

### `W2-REV-ACC03-M01` — applicability predicates can incorrectly suppress source requirements — MAJOR

Three reviewed records introduce narrower applicability than the implementation guidance permits:

1. `XAG105-PAUSE-AUDIO-EVENTS` uses trigger `pausable_non_live_audio_event_duration_seconds>=3`. The source requirement is that players should be able to pause audio events, with explicit exemptions for events under three seconds and real-time multiplayer. Making *already pausable* part of the trigger is circular: an implementation can evade the obligation precisely by being unpausable. The trigger must instead describe the source condition (non-exempt audio event duration / live-multiplayer status), while pause capability belongs only in required semantics.
2. `XAG104-PRESTART-OR-DEFAULT-ON` triggers only when captionable/spoken content occurs `before_first_settings_access`. Microsoft states that players can adjust the option before starting the game **or** subtitles are enabled by default; the implementation bullet is not conditioned on early content existing before first settings access. The current trigger can incorrectly mark the requirement inapplicable for games whose spoken content begins later.
3. `XAG106-CONTEXT-CHANGE-INITIATED-NARRATED` records `context_change_player_initiated_where_possible: true`. The current implementation guideline says context change should be player initiated, then the new context narrated. `where_possible` is an unregistered weakening/exception and must not be inserted into exact required semantics.

**Required correction:** make applicability predicates source-derived and non-circular; remove the invented `where_possible` relaxation; keep exceptions explicit and source-grounded.

### `W2-REV-ACC03-M02` — XAG 106 core narration omits an allowed source solution — MAJOR

`XAG106-CORE-UI-NARRATION` requires only platform screen-reader support or UI speech synthesis. The current XAG 106 implementation text additionally states that recorded audio files can be a solution, although not ideal. Omitting that alternative strengthens the source contract and can falsely fail an implementation that satisfies Microsoft’s stated solution set through recorded audio.

**Required correction:** represent the full allowed solution set while preserving the source’s preference signal (recorded audio allowed but nonpreferred), rather than silently deleting the alternative.

### `W2-REV-ACC03-m01` — XAG 102 platform high-contrast record promotes example prose into required semantics — MINOR

`XAG102-PLATFORM-HIGH-CONTRAST-DEFAULT` includes `player_may_reconfigure_after_launch: true`. The implementation bullet requires reading available platform contrast settings to determine launch defaults and adjusting the UI accordingly. The later example explains that a player may subsequently reconfigure settings; that example detail is not itself a normative implementation bullet. The Issue #240 source discipline explicitly says examples/background prose are not silently upgraded into requirements.

**Required correction:** remove the example-derived field from `required_semantics`, or explicitly type it as non-normative explanatory metadata outside the required semantic contract.

### `W2-REV-ACC03-m02` — XAG 104 speaker-pause threshold is not machine-deterministic — MINOR

`XAG104-SPEAKER-ID-REFRESH` encodes `significant_pause_minutes: '>1-2'`. This mirrors the source phrase “greater than 1-2 minutes” but is not a deterministic machine predicate: it does not specify whether the boundary is greater than 1, greater than 2, or a deliberately fuzzy editorial range. The mission requires deterministic applicability/trigger semantics.

**Required correction:** preserve the source ambiguity explicitly (for example, a typed source range plus a fail-closed project threshold decision), rather than presenting `'>1-2'` as an executable threshold.

## Source-fidelity checks with no finding

Fresh review found the main XAG 102 contrast thresholds/large-text platform values, 7:1 high-contrast mode, non-solid-background measurement rule, color-dependence rule, image-text/logotype/decorative exceptions materially represented. XAG 103’s eight declared records materially cover the implementation bullets for multisensory critical visual/audio cues, narration-safe symbols, color alternatives/configuration, disabled-control secondary cues, and text-only dialogue identity/location. XAG 104’s remaining caption/subtitle coverage, direction, toggles, presentation, UGC/transcript/sign-language records materially track the current implementation bullets. XAG 105’s independent audio/spatial/mono/assistive-ducking records materially track the current implementation bullets apart from M01. XAG 106’s remaining narration/focus/external-reader/media/table/pronunciation records materially track the current implementation bullets apart from M01/M02/m02.

## Adversarial disposition

The structural validator contract is directionally sound but would not catch all four findings because it validates set identity, trigger presence, and reference integrity without proving that trigger/required-semantic content is source-faithful. A syntactically nonempty but circular or invented trigger can therefore pass the declared mechanical checks. The remediation must add source-semantic adversarial fixtures for at least:

- `PAUSABLE_IN_TRIGGER` → reject circular applicability;
- `SOURCE_UNCONDITIONAL_NARROWED_BY_EARLY_CONTENT` → reject invented precondition;
- `SOURCE_REQUIREMENT_RELAXED_WITH_WHERE_POSSIBLE` → reject unregistered exception;
- `ALLOWED_SOURCE_SOLUTION_DROPPED` → reject semantic strengthening;
- `EXAMPLE_PROMOTED_TO_REQUIRED_SEMANTICS` → reject normative-scope leakage;
- `AMBIGUOUS_RANGE_AS_EXECUTABLE_THRESHOLD` → reject nondeterministic numeric predicate.

## Required route

Create exactly one bounded remediation successor for these four findings. It should modify only the XAG 102/104/105/106 records and validator/source-fidelity fixtures necessary to close them; the 77-clause identity may remain stable unless correction requires a source-faithful split. Preserve XAG 108–123 summary-only state, all empirical evidence as `NOT_RUN`, `mapping_complete: false`, and the aggregate accessibility blocker OPEN.

After remediation, require a **fresh** independent/degraded-independent scoped re-review of the exact remediation head. This review does not authorize integration of Issue #240 or PR #241.

## Authority boundary

This is noncanonical review provenance only. `CHANGES_NEEDED` explicitly withholds `CLEAN_FOR_NONCANONICAL_INTEGRATION`. Nothing here closes `W2-REV-M02` or grants empirical accessibility PASS, readiness, implementation, release, legal/compliance, Valve verification, integration, decision, verification-PASS, or canonical authority. Any later accepted integration remains separately authorized and squash-only.
