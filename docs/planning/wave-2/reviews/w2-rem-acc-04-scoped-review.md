# W2-REV-ACC-04 — scoped review of Issue #247 accessibility fidelity correction

## Review identity

- Review mission: `W2-REV-ACC-04`
- Review issue: #251
- Review branch: `planning/issue-251`
- Winning ownership claim: `5290165652`
- Reviewer actor/session: `w2-rev-acc-04-gpt56sol-20260814-frontier`
- Independence/trust mode: `DEGRADED_SINGLE_AGENT` / `DEGRADED`
- Resource-constraint authority: Issue #5 comment `5244416013`
- Cold-start manifest: `docs/planning/wave-2/reviews/w2-rem-acc-04-cold-start-inputs.yaml`
- Reviewed producer issue: #247 / `W2-REM-ACC-04`
- Reviewed terminal status: `5290154417`
- Exact reviewed head/work: `fdc93c894e39e10a20dba81e910212dc56151441`
- Reviewed draft PR: #249 at exact head `fdc93c894e39e10a20dba81e910212dc56151441`
- Exact v3 predecessor policy blob: `9c21efdeed2ddff96d6cc1d0ccf2893b9304ccc4`
- Exact v4 policy blob: `96a074e9c708d4ae2f86e8a70b7b4ade8202c799`
- Exact v4 report blob: `218cd69d400e14bca55620ef30968fe37e46db58`
- Exact v4 handoff blob: `1c531769cb01dcfa816f55e3ce49970eebacebe7`

The producer packet was immutable read-only input. The review froze exact identities before judgment, then re-read current first-party Microsoft XAG source and attacked the candidate semantics before reconciling producer rationale.

## Fresh first-party source evidence

Observed `2026-08-14`; the relevant Microsoft Learn XAG pages report last updated `2026-03-04`.

- XAG 102: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/102`
- XAG 104: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/104`
- XAG 105: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/105`
- XAG 106: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/106`

Fresh source reconstruction independently supports the Issue #247 repairs for platform high-contrast launch defaults, subtitle pre-start/default behavior, pauseable audio-event applicability/exemptions, the ambiguous XAG 104 significant-pause wording, the XAG 106 narration solution set, and player-initiated/narrated UI context changes.

The same XAG 106 source also establishes a material defect in an inherited v3 record that Issue #247 intentionally did not modify: proper names, technical terms, words whose language cannot be determined, and vernacular phrases are exceptions to the additional language-attribute guidance for external screen readers. The inherited policy instead creates a positive pronunciation-mechanism obligation gated by a subjective `requires_pronunciation_help` predicate. That semantic role is not source-faithful.

## Exact composition / scope check

The v4 packet composes over the exact v3 blob and replaces exactly six atomic records:

1. `XAG102-PLATFORM-HIGH-CONTRAST-DEFAULT`
2. `XAG104-SPEAKER-ID-REFRESH`
3. `XAG104-PRESTART-OR-DEFAULT-ON`
4. `XAG105-PAUSE-AUDIO-EVENTS`
5. `XAG106-CORE-UI-NARRATION`
6. `XAG106-CONTEXT-CHANGE-INITIATED-NARRATED`

PR #249 changes only the bounded accessibility report, policy, and Issue #247 handoff. No implementation, release, legal/platform, readiness, verification-PASS, decision, or canonical-authority surface was added.

The unchanged inherited v3 record remains effective under v4:

```yaml
XAG106-PROPER-NAME-PRONUNCIATION:
  source_id: XAG-106
  authority_class: BEST_PRACTICE_REQUIRED_IF_APPLICABLE
  applicability: CONDITIONAL
  trigger: proper_name_technical_term_or_word_of_indeterminate_language_requires_pronunciation_help
  required_semantics:
    pronunciation_mechanism_provided: true
```

## Re-test of Issue #243 findings

### `W2-REV-ACC03-M01` — independently resolved in Issue #247 scope

PASS.

- XAG 105 pause applicability no longer depends on already having a pause capability; the duration trigger and source exemptions are separated from required pause semantics.
- XAG 104 pre-start/default subtitle semantics are no longer narrowed by an invented early-content predicate.
- XAG 106 context-change semantics no longer contain the invented `where_possible` relaxation.

### `W2-REV-ACC03-M02` — independently resolved in Issue #247 scope

PASS. The XAG 106 core UI narration record preserves platform screen reader, speech synthesis, and recorded audio as allowed solutions, while retaining the source preference distinction that recorded audio is allowed but nonideal.

### `W2-REV-ACC03-m01` — independently resolved in Issue #247 scope

PASS. XAG 102 example prose about later player reconfiguration is no longer promoted into the implementation requirement for platform-derived launch defaults.

### `W2-REV-ACC03-m02` — independently resolved in Issue #247 scope

PASS. The source phrase `greater than 1-2 minutes` is retained as an ambiguous, non-executable source range. The candidate's deterministic `>60s` behavior is separately typed as a conservative project evaluation rule with `source_normative: false`; it is not represented as Microsoft normative text.

## New / reproduced material finding

### `W2-REV-ACC04-M01` — MAJOR — XAG 106 language exception is inverted into an invented pronunciation obligation

**Evidence.** Current first-party XAG 106 external-screen-reader guidance requires appropriate language exposure for the main UI language and differing language spans, then identifies proper names, technical terms, words of indeterminate language, and vernacular phrases as exceptions to that additional language-attribute guidance. The exact v3 predecessor instead models those term classes as a positive pronunciation-assistance requirement and adds the non-source predicate `requires_pronunciation_help`. Issue #247 explicitly leaves this record unchanged, so v4 inherits the defect.

**Impact.** The 77/105 clause identity arithmetic can remain mechanically consistent while XAG 106 source semantics are strengthened/inverted. A subjective trigger can also suppress or activate a requirement that Microsoft did not state in this form. Therefore source-fidelity acceptance is not valid and PR #249 is not integration-eligible.

**Required bounded correction.** A single successor must repair only this XAG 106 semantic defect. It must model the cited term classes as source-faithful exceptions to the additional language-attribute rule, rather than inventing a positive pronunciation mechanism obligation. If stable clause identity is retained, the semantic role must be retyped accordingly; if source-faithful modeling mechanically requires an inventory change, that change must be explicit and recomputed. The validator must reject reintroduction of the subjective pronunciation-help trigger or the invented positive obligation.

## Mechanical / aggregate checks

PASS for the Issue #247 bounded correction surface:

- exact six-record v4 overlay is reconstructable from the frozen v3 blob;
- targeted semantic guards cover the Issue #243 regression classes;
- new XAG 102–106 clause count remains 77 and composed atomic count remains 105 in the reviewed candidate;
- XAG 108–123 remain `GUIDELINE_SUMMARY_ONLY`;
- empirical accessibility evidence remains `NOT_RUN`;
- `mapping_complete` remains `false`;
- `IR-BLOCKER-ACCESSIBILITY-CURRENT` remains `OPEN`;
- `W2-REV-M02` remains open;
- no readiness, implementation, release, legal/compliance, Valve/platform, verification-PASS, decision, integration, or canonical authority is created.

The proper-name/language-exception MAJOR means those structural passes are insufficient for a clean disposition.

## Disposition

```yaml
disposition: CHANGES_NEEDED
blocker_count: 0
major_count: 1
correction_requiring_minor_count: 0
findings:
  - id: W2-REV-ACC04-M01
    severity: MAJOR
    state: OPEN
reviewed_issue_247_integration_eligible: false
aggregate_accessibility_blocker: OPEN
canonicality: NOT_CANONICAL
```

Issue #247 correctly repairs the four Issue #243 findings, but it cannot be accepted for noncanonical integration because the mandated re-attack independently reproduced a material inherited XAG 106 source-fidelity defect. Route exactly one bounded remediation successor for `W2-REV-ACC04-M01`; require a fresh independent/degraded-independent scoped review of that successor before any later integration decision.
