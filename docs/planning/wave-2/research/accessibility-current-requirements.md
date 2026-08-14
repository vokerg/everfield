# W2-REM-ACC-04 — XAG 102/104/105/106 source-fidelity correction

**Mission:** `W2-REM-ACC-04` / Issue #247  
**Branch base:** `df2dffdb14fc20def14aaaee4d61e0638e500f91`  
**Immutable producer input:** Issue #240 terminal comment `5290011410`, head `bccd22e35f84a5894586d9494e1963ebdef7dc02`, work `f4671c3c295437a64d82ffc51e228c826fcce40e`  
**Immutable v3 policy blob:** `9c21efdeed2ddff96d6cc1d0ccf2893b9304ccc4`  
**Required source review:** Issue #243 terminal comment `5290059882`, disposition `CHANGES_NEEDED`, head `e7fab153735b90cae4a175fb42b0546dba728f7b`, work `f2a87552756d6f9897e6349fa5b7e4cc5f677fda`  
**Observed first-party sources:** `2026-08-14`  
**Authority:** bounded noncanonical remediation; fresh independent scoped re-review is still mandatory.

## 1. Scope and composition

This packet closes only the four Issue #243 finding IDs `W2-REV-ACC03-M01`, `W2-REV-ACC03-M02`, `W2-REV-ACC03-m01`, and `W2-REV-ACC03-m02`. It does not rewrite the rejected Issue #240 branch. Instead, `ACCESSIBILITY-POLICY-OVERLAY-v4` composes over the exact immutable Issue #240 v3 policy blob and replaces exactly six affected atomic records plus the semantic validator contract.

The 77-member XAG 102–106 inventory remains identity-stable and still composes with the inherited 28 XAG 101/XAG 107 records to 105 atomic records. No XAG 108–123 page is promoted; empirical accessibility evidence remains `NOT_RUN`; `mapping_complete` remains false; and `IR-BLOCKER-ACCESSIBILITY-CURRENT` remains OPEN.

A second scoped review, Issue #242, was terminalized and integrated on `main` after this branch was claimed. That review routes an additional XAG 106 proper-name-pronunciation applicability defect to Issue #245. This Issue #247 packet does **not** disposition that parallel finding and does not claim the whole XAG 106 surface clean. This preserves scoped completion without laundering a separate negative review into acceptance.

## 2. Fresh source recheck

Current first-party Microsoft XAG v3.2 pages were re-read on `2026-08-14` before correction. The load-bearing facts for this packet are:

- **XAG 102:** where platform contrast settings are available, the implementation bullet says to read them to determine high-contrast launch defaults and adjust the UI accordingly. The later statement that the player can subsequently reconfigure settings occurs in example prose, not the implementation obligation itself.
- **XAG 104:** players can adjust subtitles before starting the game **or** subtitles are enabled by default. That implementation bullet is not conditioned on spoken/captionable content occurring before first settings access. The same page describes a significant same-speaker pause as `greater than 1-2 minutes`, which is source wording rather than a single machine-comparable threshold.
- **XAG 105:** players should be able to pause audio events, including cinematics with audio; events under three seconds and real-time multiplayer gameplay are exempt. Existing pause capability therefore cannot be an applicability precondition.
- **XAG 106:** core game UI should support the platform screen reader or voice the UI through speech synthesis; recorded audio files are also an allowed solution, although Microsoft labels that option nonideal. The context-change implementation bullet says context change should be player initiated and the new context narrated afterward; it does not contain a `where possible` relaxation.

All four pages currently report last updated `2026-03-04`. These are accessibility best-practice source semantics, not legal/compliance certification.

## 3. Finding dispositions

### `W2-REV-ACC03-M01` — RESOLVED

Three source-applicability defects are corrected.

1. `XAG105-PAUSE-AUDIO-EVENTS` now triggers on an audio event whose duration is at least three seconds. `player_can_pause: true` exists only in required semantics. Under-three-second events and real-time multiplayer are explicit source exemptions, so an unpausable implementation cannot evade the requirement by making `pausable` part of the trigger.
2. `XAG104-PRESTART-OR-DEFAULT-ON` now applies when the game has spoken content for which subtitles apply; it no longer requires content before first settings access. The source alternatives remain exactly “player can adjust before game start” or “subtitles enabled by default.”
3. `XAG106-CONTEXT-CHANGE-INITIATED-NARRATED` now requires `context_change_player_initiated: true` plus narration of the new context. The invented `where_possible` semantic field is removed.

### `W2-REV-ACC03-M02` — RESOLVED

`XAG106-CORE-UI-NARRATION` now represents the complete source-allowed solution set:

- platform screen reader;
- game/UI speech synthesizer;
- recorded audio files.

Recorded audio is explicitly typed `ALLOWED_BUT_NOT_IDEAL`, preserving Microsoft’s preference distinction without deleting the alternative or promoting it to the preferred implementation.

### `W2-REV-ACC03-m01` — RESOLVED

`XAG102-PLATFORM-HIGH-CONTRAST-DEFAULT.required_semantics` now contains only the implementation obligation to read an available platform setting and apply it as the launch default. The example-derived `player_may_reconfigure_after_launch` field is removed from required source semantics.

### `W2-REV-ACC03-m02` — RESOLVED

`XAG104-SPEAKER-ID-REFRESH` retains the exact source phrase `greater than 1-2 minutes` but no longer presents `'>1-2'` as an executable scalar.

The source threshold is typed `AMBIGUOUS_RANGE_NOT_EXECUTABLE`. For deterministic fail-closed project evaluation only, the overlay uses a separately typed, explicitly non-source-normative lower-bound rule of `pause_duration_seconds > 60`. This is conservative: a pause that could fall into the source’s ambiguous significant range cannot silently pass as too short. The project rule is reopened if an independently approved source interpretation replaces it.

## 4. Mechanical semantic guard

`ACCESSIBILITY-POLICY-VALIDATOR-v4` first reconstructs the exact Issue #240 v3 packet and its 77/105 inventory arithmetic, then applies exactly the six correction records. It adds exact semantic assertions that structural v3 validation lacked.

The validator now rejects all of the review attack classes:

- pause capability smuggled into its own applicability trigger;
- the pre-start/default subtitle rule narrowed by an early-content predicate;
- a source requirement weakened by `where_possible`;
- recorded audio dropped from the XAG 106 allowed solution set;
- example prose promoted to required semantics;
- the ambiguous XAG 104 source range represented as an executable scalar;
- a project fail-closed threshold mislabeled as source normative.

The aggregate assertions separately require stable inventory identity/counts, XAG 108–123 summary-only state, empirical `NOT_RUN`, `mapping_complete: false`, OPEN accessibility blocker, mandatory fresh review, and `integration_authorized: false`.

## 5. Preserved fail-closed state and parallel review

This correction does not establish empirical accessibility quality. No product applicability sweep, implementation evidence, player test, screen-reader trace, contrast measurement, caption behavior capture, or accessibility verification PASS has been produced here.

The parallel Issue #242 review is preserved as independent negative provenance on current `main`. Its additional `PG-REM-ACC03-M01` attack on `XAG106-PROPER-NAME-PRONUNCIATION` remains routed to Issue #245. Because Issue #247 did not own that finding, this packet neither edits that record nor claims that finding resolved.

Accordingly:

```yaml
xag_108_123: GUIDELINE_SUMMARY_ONLY
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
fresh_independent_scoped_review_required: true
integration_authorized: false
canonicality: NOT_CANONICAL
```

## 6. Bounded self-review

For the Issue #243 finding set only:

- unresolved BLOCKER: **0**;
- unresolved MAJOR: **0**;
- correction-requiring MINOR: **0**;
- clause identities/counts changed: **NO**;
- source example promoted to requirement: **NO**;
- source-allowed narration solution dropped: **NO**;
- circular pause applicability retained: **NO**;
- nondeterministic `'>1-2'` executable threshold retained: **NO**;
- XAG 108–123 promoted: **NO**;
- empirical PASS claimed: **NO**;
- aggregate accessibility blocker cleared: **NO**;
- readiness/integration/canonical/legal/platform authority claimed: **NO**.

This self-review is not acceptance. A fresh independent/degraded-independent scoped reviewer must reconstruct the exact v3 base plus this v4 overlay and attack the corrected semantic assertions before any integration eligibility can be considered.

## 7. Downstream contract

A successor scoped review should consume this task only at its terminal immutable head/work/blob identities, re-read current first-party XAG 102/104/105/106 source text, execute the v4 semantic fixtures, and return a typed clean/changes-needed disposition. It must keep Issue #245’s parallel finding route independent rather than treating a clean Issue #247 review as resolution of the separate pronunciation finding.

Even a clean review of this packet would create only bounded noncanonical review evidence. It would not close aggregate `W2-REV-M02`, clear `IR-BLOCKER-ACCESSIBILITY-CURRENT`, establish empirical accessibility PASS, authorize implementation/release, provide legal/compliance or platform certification, create a product decision, or make any artifact canonical. Any later `main` integration remains separately authorized and squash-only.
