# Handoff — Issue #250 / W2-REV-ACC-04

## Identity

- Mission: `W2-REV-ACC-04`
- Issue: #250
- Branch: `planning/issue-250`
- Winning claim comment: `5290162605`
- Actor session: `w2-rev-acc-04-gpt56sol-20260814-0820-frontier`
- Claim/base main: `262013df3bdc5db2da63eb48f2e1365906be3c12`
- Trust mode: `DEGRADED_SINGLE_AGENT`

A later duplicate review surface, Issue #251, was created and claimed after this issue's earlier valid review claim. This review does not modify Issue #251 or its branch; Issue #250 remains the earlier claimed review episode used for this handoff.

## Immutable reviewed inputs

- Issue #247 terminal status: comment `5290154417`
- Issue #247 exact head/work: `fdc93c894e39e10a20dba81e910212dc56151441`
- Issue #247 draft PR: #249, exact reviewed head `fdc93c894e39e10a20dba81e910212dc56151441`
- Report blob: `218cd69d400e14bca55620ef30968fe37e46db58`
- Policy v4 blob: `96a074e9c708d4ae2f86e8a70b7b4ade8202c799`
- Issue #247 handoff blob: `1c531769cb01dcfa816f55e3ce49970eebacebe7`
- Predecessor Issue #240 policy v3 blob: `9c21efdeed2ddff96d6cc1d0ccf2893b9304ccc4`
- Authoritative source review Issue #243 terminal comment: `5290059882`
- Narrower review Issue #242 terminal comment: `5290068415`

The producer packet is read-only. PR #249 changes exactly the producer handoff, accessibility report, and accessibility policy.

## Fresh evidence and result

Current first-party Microsoft XAG 102, 103, 104, 105, and 106 pages were checked on `2026-08-14`; all current English pages report last updated `2026-03-04`.

The fresh review independently confirms the six Issue #247 v4 corrections for the Issue #243 finding set:

- XAG105 pause applicability is no longer circular and retains under-three-second / real-time-multiplayer exemptions;
- XAG104 pre-start/default subtitle applicability is not narrowed by an early-content predicate;
- XAG106 context change has no invented `where_possible` weakening;
- XAG106 core narration preserves screen-reader, speech-synthesis, and recorded-audio alternatives, with recorded audio nonpreferred;
- XAG102 post-launch reconfiguration remains example prose rather than source-required semantics;
- XAG104 `greater than 1-2 minutes` is preserved as ambiguous source wording and separated from the deterministic, explicitly non-source project rule.

The required narrower-risk re-attack fails. Exact v3 record `XAG106-PROPER-NAME-PRONUNCIATION`, inherited unchanged by v4, still uses trigger:

`proper_name_technical_term_or_word_of_indeterminate_language_requires_pronunciation_help`

Current XAG 106 instead requires a pronunciation mechanism when a proper name, technical term, or word of indeterminate language is present; it does not add the subjective `requires_pronunciation_help` applicability gate.

## Finding and disposition

```yaml
review_disposition: CHANGES_NEEDED
findings:
  - id: W2-REV-ACC04-M01
    severity: MAJOR
    state: OPEN
    affected_record: XAG106-PROPER-NAME-PRONUNCIATION
    defect: subjective non-source applicability predicate can suppress a source-covered pronunciation obligation
blockers: 0
majors: 1
correction_requiring_minors: 0
producer_packet_accepted: false
producer_integration_eligible: false
```

The v4 semantic validator protects the six Issue #243 corrections but has no exact assertion/adversarial fixture that rejects the inherited pronunciation narrowing. Inventory/set/reference validity therefore cannot make this packet CLEAN.

## Routed successor

Exactly one bounded correction successor is Issue #252 / `W2-REM-ACC-05`.

It must:

1. make pronunciation applicability deterministic from presence of a proper name, technical term, or word of indeterminate language;
2. retain the required pronunciation mechanism;
3. add a semantic fixture rejecting extra subjective applicability gates;
4. preserve all six v4 corrections, the 77-new / 105-composed inventory, XAG 108-123 summary-only state, empirical `NOT_RUN`, `mapping_complete: false`, and OPEN accessibility blocker;
5. require a fresh independent/degraded-independent scoped review before integration eligibility.

Do not claim or work Issue #252 from this review handoff; it is a separately owned remediation generation after this review terminalizes.

## Preserved authority boundary

- XAG 108-123: `GUIDELINE_SUMMARY_ONLY`
- empirical accessibility evidence: `NOT_RUN`
- `mapping_complete`: `false`
- `IR-BLOCKER-ACCESSIBILITY-CURRENT`: `OPEN`
- `W2-REV-M02`: `OPEN_BOUNDED`
- production implementation ready: `false`
- Issue #247 integration eligible from this review: `false`
- canonicality: `NOT_CANONICAL`

This review grants no accessibility empirical PASS, legal/compliance or platform certification, readiness, implementation, release, verification-PASS, integration, merge, decision, or canonical authority. Any later `main` integration remains separately authorized and squash-only.