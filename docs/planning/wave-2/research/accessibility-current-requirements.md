# W2-REM-ACC-01 — Clause-level accessibility requirement remediation

**Mission:** `W2-REM-ACC-01` / Issue #96  
**Source candidate:** W2-ACC-01 / Issue #81 head/work `e009dd2e2deb9006f864e851ea84880ecc64cec2`  
**Source report blob:** `cd97806a06cd2aa3f97689ab7c32b3b631449b09`  
**Source handoff blob:** `a480ece0eb0cc4d3c2f674f3577c1a4f6a07f7aa`  
**Source terminal status:** Issue #81 comment `5270745594`  
**Independent pre-gate review:** Issue #81 comment `5271715858`  
**Machine-readable policy:** `docs/planning/wave-2/research/accessibility-requirements-policy.yaml` blob `78690cf658967b2ded35e738df125959a56f0d86`  
**Observed current first-party sources:** `2026-08-12`  
**Authority:** bounded remediation candidate only; formal review remains `W2-REV-01`.

## 1. Purpose and authority boundary

This file is the substantive remediation overlay for the frozen W2-ACC-01 producer payload. The producer report remains immutable provenance and is not edited. Unchanged architectural guidance from that payload remains available at the exact source work/blob above; this remediation replaces only the producer claims affected by pre-gate findings `PG-ACC-M01` and `PG-ACC-m01`.

No output here is:

- a legal accessibility conclusion;
- an Xbox/platform certification statement;
- a Steam Deck `Verified` result;
- evidence that any accessibility check has actually run;
- an implementation-readiness decision;
- an engine selection; or
- canonical planning authority.

Microsoft XAG v3.2 remains classified as `CURRENT_ACCESSIBILITY_BEST_PRACTICE`, not law or a compliance checklist. Public Valve Deck checklist clauses remain `PLATFORM_COMPATIBILITY_REQUIRED` only for the selected Deck evidence target.

## 2. Exact remediation result

### 2.1 `PG-ACC-M01` — accepted

The frozen producer report grouped whole XAG pages into coarse rows/evidence IDs and then asserted:

```yaml
every_applicable_or_conditional_guideline_has_evidence_or_gap: true
```

That assertion is withdrawn. A guideline-level summary is not proof that every current source clause is represented.

The new machine-readable policy makes **source clause** the acceptance unit. Its fail-closed rules require:

1. an exact source/page identity and version/scope;
2. deterministic applicability;
3. exact threshold/semantic preservation when the source provides one;
4. non-empty evidence-requirement or gap references for every applicable/triggered clause; and
5. `MAPPING_INCOMPLETE` for unknown, unmapped, or summary-only current-scope source material.

`XAG-101` and `XAG-107`, the pages specifically attacked by pre-gate review, are now atomically expanded into stable clause records. The policy separately binds text-size/scaling, font alternatives, language/spacing behavior, digital/analog navigation, remapping, input alternatives, pointer cancellation semantics, keyboard-only flow, sensitivity bounds, dictation applicability, and accessibility of the customization flow.

For XAG 102–106 and 108–123, the policy deliberately records `GUIDELINE_SUMMARY_ONLY` rather than pretending clause completeness. Each page has an exact source URL/version identity and a required atomic-expansion flag. Therefore equivalent omissions cannot silently produce a mapping PASS: the derived aggregate remains incomplete until those pages are atomically expanded or explicitly deferred by scope.

This is a bounded correction, not a hidden claim that all 23 XAG pages were exhaustively atomized in this remediation episode.

### 2.2 Derived blocker state

The corrected machine state is:

```yaml
blocker_id: IR-BLOCKER-ACCESSIBILITY-CURRENT
blocker_authority_state: OPEN
catalog_derived_mapping_complete: false
mapping_state: PARTIAL_ATOMIC_MAPPING_REMEDIATED_PENDING_EXPANSION_AND_INDEPENDENT_REVIEW
reason_codes:
  - XAG_102_TO_106_NOT_ATOMICALLY_EXPANDED
  - XAG_108_TO_123_NOT_ATOMICALLY_EXPANDED
required_next_authority: W2-REV-01
```

This replaces the producer's hand-authored completeness boolean. `NOT_RUN` cannot become `NOT_APPLICABLE`, and a summary row cannot authorize closure.

The current state is intentionally conservative: the remediation fixes the **false-positive path** first. A later bounded research/review episode may atomically expand the remaining pages, but until then the accessibility-current mapping blocker stays OPEN.

## 3. XAG 101 clause coverage added by remediation

Current Microsoft XAG 101 was rechecked from:

`https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/101`

The policy now separately binds, among other source clauses:

- PC/VR minimum default body-height text targets: 18 px at 1080p and 36 px at 4K;
- text inside icons/glyphs meeting the same minimum and glyph scaling with text;
- text scaling to 200% of minimum without loss of content, functionality, or meaning;
- readable overflow, preserved header differentiation, and no forced two-axis scrolling for one UI;
- at least one sans-serif option;
- a non-stylized option when stylized fonts are used;
- complete character sets for every supported language;
- configurable spacing or the source's bounded line/paragraph/letter/word spacing defaults for multi-line blocks;
- sentence-case availability when lines use all caps/all lowercase, subject to the source's short-label exemption; and
- language-direction-aware alignment or equivalent player configurability.

Each clause points to an exact `ACC-EV-*` requirement and `ACC-GAP-*` record. All such evidence is currently `NOT_RUN`; the mapping does not fabricate empirical satisfaction.

## 4. XAG 107 clause coverage added by remediation

Current Microsoft XAG 107 was rechecked from:

`https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/107`

The policy now separately binds:

- digital and analog UI navigation;
- single, non-simultaneous UI key presses;
- in-game remapping of all relevant controls, including independent X/Y inversion and PC escape-key coverage;
- remapped-label synchronization in hints/tutorials/control maps;
- digital equivalents for functions whose primary control is analog;
- alternatives/bypass for rapid-repeat, prolonged-hold, and simultaneous-button barriers;
- alternatives for multipoint and path-based gestures when present;
- pointer/touch up-event activation plus cancel/undo semantics, with explicit essential exceptions;
- alternative digital input for gameplay-critical speech/motion defaults;
- alternatives to requiring two analog sticks/stick-plus-D-pad;
- keyboard-only start/settings/play/exit when keyboard input is supported;
- per-analog-control sensitivity adjustment of at least ±50% from default;
- dictation/speech-to-text applicability for text-entry/chat surfaces; and
- accessibility of the customization process itself.

Again, these are **mapped requirements**, not passing implementation evidence.

## 5. `PG-ACC-m01` — accepted

The producer report placed Windows-build-on-Deck/Proton execution beside direct Valve compatibility checklist requirements as if they shared the same source authority.

That is corrected.

### 5.1 Direct Valve checklist requirements

The policy retains direct `PLATFORM_COMPATIBILITY_REQUIRED` records for the public checklist items currently relevant to the selected Deck target:

- default controller configuration reaches all content;
- displayed glyphs match active input;
- required text entry is controller-usable in the player's language;
- default Deck configuration reaches playable 30 fps at 800p;
- no unsupported Deck/Linux hardware/software warning;
- a launcher, if present, must meet applicable compatibility requirements;
- the game runs at a Deck-supported resolution, with Valve recommending 1280x800 / 1280x720; and
- interface text remains readable at 30 cm, never below 9 px character height at 1280x800, with 12 px recommended where possible.

Current source:

`https://partner.steamgames.com/doc/steamhardware/compat`

### 5.2 Project-selected Proton evidence

`ACC-PROJECT-DECK-PROTON-01` is now typed `PROJECT_SELECTED_PLATFORM_EVIDENCE`.

Its authority comes from:

- the corrected `PLAT-PC-FIRST-R1` project input at W2-REM-PLAT-01 / Issue #92 work `9d51099be4d53eff876104f482e3c163d34519e3`; plus
- Valve's public documentation that Windows games without native Linux builds run on Deck through Proton.

The Windows-build-on-Deck/SteamOS core-flow check remains required by the project-selected evidence envelope, but it is no longer mislabeled as a separate Valve `Verified` checklist requirement.

## 6. Current-source spot check

On `2026-08-12`, current first-party pages were rechecked for the load-bearing remediation claims:

- Microsoft XAG index remains v3.2, published 2023-06-08, and continues to describe XAGs as design/development/test best practices rather than legal/compliance proof.
- XAG 101 still contains the PC/VR 18 px-at-1080p default target, 200% scaling guidance, font/style/spacing/case/alignment guidance used by the new atomic records.
- XAG 107 still contains the digital/analog, remap, single-input, alternative-input, pointer, keyboard-only, and sensitivity semantics encoded by the policy.
- XAG 108 still covers difficulty options, progress-preserving difficulty changes, regular save, and pausable single/local play/cinematics.
- XAG 116 still scopes time-limit guidance to UI/non-core interactions and excludes core gameplay timing mechanisms from that XAG.
- Valve's public Deck compatibility page still exposes the controller, glyph, text-entry, default-performance, warning, launcher, resolution, text-legibility, and Proton behavior used here.

No material drift was found in those load-bearing facts. This spot check does not upgrade summary-only XAG 102–106/108–123 pages to atomic coverage; the policy keeps them fail-closed.

## 7. Downstream contract

`W2-REV-01` should consume:

1. frozen W2-ACC-01 producer provenance at `e009dd2e2deb9006f864e851ea84880ecc64cec2`;
2. this remediation report;
3. `accessibility-requirements-policy.yaml` blob `78690cf658967b2ded35e738df125959a56f0d86`; and
4. `w2-acc-01-pre-gate-review-dispositions.md`.

For source-clause completeness and Deck/Proton authority, this remediation supersedes the affected producer statements. Unchanged producer architecture/gap guidance remains provenance, but cannot override the policy's fail-closed aggregate.

No downstream task may treat the current `mapping_complete: false` as a producer failure to be hidden; it is the explicit corrected truth state.

## 8. Self-review

Against Issue #96 acceptance criteria:

- immutable source-candidate/review provenance: **PASS**;
- `PG-ACC-M01` disposition/correction: **PASS**;
- `PG-ACC-m01` disposition/correction: **PASS**;
- versioned machine-readable source-clause policy: **PASS**;
- current XAG 101 clauses attacked by review represented atomically: **PASS**;
- current XAG 107 clauses attacked by review represented atomically: **PASS**;
- remaining XAG summary-only pages cannot produce aggregate mapping PASS: **PASS**;
- `IR-BLOCKER-ACCESSIBILITY-CURRENT` truth derives from catalog state: **PASS**;
- direct Valve checklist vs project-selected Proton evidence authority separated: **PASS**;
- current first-party load-bearing source spot-check: **PASS**;
- empirical accessibility PASS claimed: **NO**;
- legal/certification conclusion claimed: **NO**;
- implementation/readiness/canonicalization authority claimed: **NO**;
- required formal review remains `W2-REV-01`: **PASS**.

**Self-review disposition:** 0 unresolved BLOCKER / 0 unresolved MAJOR in the bounded remediation scope.

The intentionally retained `mapping_complete: false` is not a concealed remediation defect; it is the mechanism that prevents the original coarse-grained completeness overclaim from surviving into formal review.
