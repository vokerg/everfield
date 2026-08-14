# W2-REV-ACC-04 — independent scoped review of Issue #247 accessibility source-fidelity remediation

**Mission:** `W2-REV-ACC-04` / Issue #250  
**Reviewed producer:** `W2-REM-ACC-04` / Issue #247  
**Reviewed terminal status:** comment `5290154417`  
**Reviewed exact head/work:** `fdc93c894e39e10a20dba81e910212dc56151441`  
**Reviewed PR:** #249  
**Reviewed report blob:** `218cd69d400e14bca55620ef30968fe37e46db58`  
**Reviewed policy v4 blob:** `96a074e9c708d4ae2f86e8a70b7b4ade8202c799`  
**Reviewed handoff blob:** `1c531769cb01dcfa816f55e3ce49970eebacebe7`  
**Immutable predecessor policy v3 blob:** `9c21efdeed2ddff96d6cc1d0ccf2893b9304ccc4`  
**Review claim:** comment `5290162605`  
**Review trust mode:** `DEGRADED_SINGLE_AGENT` fresh review episode  
**Disposition:** `CHANGES_NEEDED`

## 1. Immutable input and scope reconstruction

The review consumed Issue #247 only at its terminal exact identity. PR #249 remains an exact-head draft over `planning/issue-247` and changes exactly these three declared files:

- `docs/planning/handoffs/issue-247.md`;
- `docs/planning/wave-2/research/accessibility-current-requirements.md`;
- `docs/planning/wave-2/research/accessibility-requirements-policy.yaml`.

The v4 policy composes over the exact v3 policy blob and replaces exactly six declared atomic records while preserving every other v3 record logically unchanged. The preserved inventory is 12 / 8 / 29 / 5 / 23 records for XAG 102 / 103 / 104 / 105 / 106, respectively: 77 new records. Together with the inherited 28 XAG 101/XAG 107 records, the composed inventory remains 105. No reviewed producer branch mutation was performed by this review.

The repository-visible independence constraint remains degraded single-agent. Producer assertions were treated as hypotheses, not acceptance evidence; current first-party source semantics and immutable policy bytes were checked before disposition.

## 2. Current first-party source reconstruction

The reviewer independently re-read the current Microsoft XAG v3.2 implementation surfaces on 2026-08-14:

- XAG 102: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/102`
- XAG 103: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103`
- XAG 104: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/104`
- XAG 105: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/105`
- XAG 106: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/106`

All five current English pages report `Last updated on 2026-03-04`. No source-version drift invalidates the reviewed identity wholesale.

Load-bearing source observations for this review:

- XAG 102's implementation bullet requires reading available platform contrast settings to determine high-contrast launch defaults and adjusting the game UI accordingly. The later player reconfiguration statement is example prose, not part of that implementation bullet.
- XAG 104 requires that players can adjust subtitles before starting the game or that subtitles are enabled by default. It also uses the source phrase `greater than 1-2 minutes` for a significant same-speaker pause, which is not a single executable scalar.
- XAG 105 requires pause capability for audio events including cinematics, with events under three seconds and real-time multiplayer gameplay exempt.
- XAG 106 allows platform screen readers or speech synthesis for core UI narration and also allows recorded audio files while calling them nonideal. It states that context change should be player initiated and that the new context should be narrated afterward; no `where possible` relaxation appears in that implementation bullet.
- XAG 106 separately requires a mechanism for the player to understand how to pronounce a proper name, technical term, or word of indeterminate language. That obligation is keyed to the presence of those term classes; the source does not add a further subjective predicate that the term first be judged to `require pronunciation help`.

These XAGs are retained here as accessibility best-practice evidence, not legal/compliance certification.

## 3. Re-attack of Issue #243 findings

### `W2-REV-ACC03-M01` — corrected for the Issue #243 subconditions

The v4 overlay corrects all three Issue #243 applicability defects:

1. `XAG105-PAUSE-AUDIO-EVENTS` triggers on event duration and keeps under-three-second / real-time-multiplayer exemptions explicit. Existing pause capability is not an applicability precondition.
2. `XAG104-PRESTART-OR-DEFAULT-ON` applies when subtitle-relevant spoken content exists and preserves the source alternatives `player_can_adjust_before_game_start` or `subtitles_enabled_by_default`; it no longer introduces an early-content predicate.
3. `XAG106-CONTEXT-CHANGE-INITIATED-NARRATED` requires player initiation and narration of the new context and contains no `where_possible` field or exception.

### `W2-REV-ACC03-M02` — corrected

`XAG106-CORE-UI-NARRATION` contains the complete source-allowed solution set: platform screen reader, game/UI speech synthesizer, and recorded audio files. Recorded audio is typed `ALLOWED_BUT_NOT_IDEAL`, preserving the source preference distinction without deleting an allowed solution.

### `W2-REV-ACC03-m01` — corrected

`XAG102-PLATFORM-HIGH-CONTRAST-DEFAULT` now retains only `read_platform_setting: true` and `apply_as_launch_default: true` as source-required semantics. The example-derived `player_may_reconfigure_after_launch` field is absent from the v4 record.

### `W2-REV-ACC03-m02` — corrected

`XAG104-SPEAKER-ID-REFRESH` preserves the exact source phrase `greater than 1-2 minutes` as `AMBIGUOUS_RANGE_NOT_EXECUTABLE`. A separate project evaluation rule uses `pause_duration_seconds > 60`, explicitly marks itself `PROJECT_EVALUATION_RULE_NOT_SOURCE_REQUIREMENT` and `source_normative: false`, and therefore fails closed without laundering the ambiguous source phrase into an asserted Microsoft scalar.

## 4. Fresh finding

### `W2-REV-ACC04-M01` — MAJOR — pronunciation applicability remains narrowed by a subjective non-source gate

**Affected logical record:** `XAG106-PROPER-NAME-PRONUNCIATION` inherited unchanged from exact v3 policy blob `9c21efdeed2ddff96d6cc1d0ccf2893b9304ccc4`.

**Current inherited trigger:**

`proper_name_technical_term_or_word_of_indeterminate_language_requires_pronunciation_help`

**Current source obligation:**

Microsoft XAG 106 requires providing a mechanism for the player to understand how to pronounce a proper name, technical term, or word of indeterminate language. The implementation guideline does not add a separate subjective applicability decision that such a term `requires pronunciation help`.

**Why this is material:**

The inherited trigger can evaluate a source-covered term as out of scope solely because a product-side evaluator decides it does not `require pronunciation help`. That extra predicate can therefore suppress the pronunciation mechanism while the atomic record still appears structurally present, referenced, and conditionally well formed. This is the same semantic-narrowing class that the v4 validator is intended to reject elsewhere.

Issue #247 explicitly did not patch this record and explicitly required the fresh review to re-attack it. The v4 `atomic_clause_correction_patch` names six other records only. Its `required_semantic_assertions` do not add a source-faithful pronunciation applicability assertion or an adversarial fixture rejecting this subjective gate. The narrower Issue #242 finding is therefore independently reproduced rather than cured by Issue #245's routing supersession.

**Required correction:** Issue #252 / `W2-REM-ACC-05` must replace the trigger with deterministic presence of a proper name, technical term, or word of indeterminate language; retain `pronunciation_mechanism_provided: true`; and add a semantic validator/adversarial fixture that rejects any extra subjective applicability predicate of this class.

## 5. Mechanical and aggregate attacks

The v4 validator contract correctly hardens the six Issue #243 correction classes. It requires exact v3 reconstruction, exact 77-member XAG 102-106 inventory before patching, replacement of exactly the six named records, preservation of every other v3 record, and explicit semantic assertions for those six corrections. The declared adversarial cases reject circular pause applicability, early-content narrowing, `where_possible` relaxation, dropped narration alternatives, example-to-requirement leakage, ambiguous-range-as-executable-threshold, and project/source authority conflation.

That contract is not sufficient for a CLEAN result because the reproduced pronunciation narrowing is inherited outside the six-record patch and has no corresponding v4 semantic assertion. Structural inventory PASS cannot substitute for source-semantic fidelity.

The aggregate fail-closed state remains intact:

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

No accessibility empirical PASS, legal/compliance certification, platform certification, readiness, implementation, release, verification-PASS, decision, integration, merge, or canonical authority is created by Issue #247 or this review.

## 6. Disposition and route

`CHANGES_NEEDED`.

Finding counts for this exact review scope:

- unresolved BLOCKER: **0**;
- unresolved MAJOR: **1** — `W2-REV-ACC04-M01`;
- correction-requiring MINOR: **0**.

The six Issue #243 corrections survive the fresh re-attack, but `XAG106-PROPER-NAME-PRONUNCIATION` remains source-narrowed. Therefore exact Issue #247 is **not** clean for noncanonical integration and PR #249 is **not** integration-eligible on the basis of this review.

Exactly one bounded remediation successor is routed: Issue #252 / `W2-REM-ACC-05`. It is limited to the pronunciation trigger plus the minimum semantic-regression fixture and must preserve all other v4 corrections and aggregate fail-closed state. A fresh independent/degraded-independent review remains required after that successor terminalizes.

This review is noncanonical negative review provenance only. Any later integration of review provenance or corrected producer evidence remains separately authorized and squash-only.