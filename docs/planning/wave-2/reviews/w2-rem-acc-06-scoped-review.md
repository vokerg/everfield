# W2-REV-ACC-06 — scoped review of XAG 108–123 atomization

**Mission:** `W2-REV-ACC-06` / Issue #262  
**Reviewed producer:** Issue #259 / `W2-REM-ACC-06`  
**Reviewed terminal status:** comment `5290417804`  
**Reviewed exact head:** `b8553ac83dd11193ad1f57f8b552827768ba3338`  
**Reviewed substantive work:** `14dee0852546eec43677312ce3066b811533df61`  
**Reviewed PR:** #261  
**Reviewed policy v6 blob:** `80e278315d6b7a108d89da3f5a99086a8ef91bf7`  
**Reviewed report blob:** `ec901acaf36ed4d398b127eac058537e6387a92e`  
**Reviewed handoff blob:** `fb439de3764924f1612f1f3bb3aac78d3c53a777`  
**Immutable base policy v5 blob:** `c7c3f72fb3bbd2d0e961aee94b33ce2ac93c5615`  
**Review claim:** comment `5290429736`  
**Trust profile:** `DEGRADED_SINGLE_AGENT` fresh review episode  
**Disposition:** `CHANGES_NEEDED`

## 1. Frozen identity and review boundary

The review consumed Issue #259 only at its terminal exact identity. PR #261 was re-fetched open, draft, mergeable, and exact-head at `b8553ac83dd11193ad1f57f8b552827768ba3338`, with base `main@2d3307cdc52db6e8783f7c4c4025996685934fa7` and the producer-declared three-file scope.

Issue #259 and PR #261 were read-only inputs. The review did not mutate producer artifacts. Duplicate review Issue #263 appeared after the Issue #262 claim but had no claim when ownership was re-checked, so Issue #262 remains the controlling review episode.

Because a reproducible material source-fidelity defect was found, the review terminates negatively under Issue #262's contract. This report does **not** claim exhaustive acceptance of unaffected XAG 108–123 clauses.

## 2. Independent source-modality attack

Current first-party Microsoft XAG pages were re-read independently rather than accepting producer self-review as evidence.

The initial concern that all atomized `consider` guidance had been promoted into hard requirements did **not** reproduce. In exact policy v6, for example:

- `XAG108-REDUCED-CONTROL-SCHEME` is `BEST_PRACTICE_RECOMMENDED_IF_APPLICABLE` with `source_modality: CONSIDER`;
- `XAG110-HAPTIC-ADDITIONAL-CUES` is `BEST_PRACTICE_RECOMMENDED_IF_APPLICABLE` with `source_modality: CONSIDER`;
- `XAG117-CAMERA-VIEW-CHOICE` is likewise represented as a recommendation/`CONSIDER` record.

Atomic representation of an advisory is therefore not, by itself, an authority inflation in this packet.

## 3. Material finding — W2-REV-ACC06-M01 / MAJOR

### Finding

`W2-REV-ACC06-M01` — **XAG 116 default-over-20-hours exemption is omitted from the atomic policy and validator.**

Severity: `MAJOR`.

### Fresh first-party source reconstruction

Source re-read on `2026-08-14`:

`https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/116`

The page reports last updated `2026-03-04`.

XAG 116 first scopes the guideline to UI interactions that are not core gameplay. For applicable content-imposed time limits it requires essentiality, advance warning, and a way to modify the limit. The modification alternatives include requesting a longer/no session limit, pre-adjustment to at least 10× the default, a pre-expiry warning with at least 20 seconds and at least ten simple-action extensions, or turning the limit off. For important on-screen element durations it permits pre-adjustment to at least 10× or disabling the duration and advancing/dismissing on input.

After those expectations, the source gives an explicit exception block: a content-imposed time limit is exempt if at least one listed condition is true. The list includes:

1. a required real-time event with no possible alternative;
2. a limit essential to the task;
3. **the default time limit exceeds 20 hours**.

The page separately excludes core gameplay timing and explains the multiplayer-lobby real-time case.

### Exact v6 reproduction

Exact policy v6 correctly retains several XAG 116 details, including the 10× adjustment, 20-second warning window, minimum ten extensions, and turn-off alternative. It also models exception tokens such as:

```yaml
exceptions:
  - real_time_event_with_no_alternative
  - time_limit_is_essential_to_task
  - core_gameplay_timing
```

and for the important-element duration record:

```yaml
exceptions:
  - real_time_event_with_no_alternative
  - duration_is_essential_to_task
  - core_gameplay_timing
```

However, exact policy blob `80e278315d6b7a108d89da3f5a99086a8ef91bf7` contains **no representation anywhere** of the source exemption for a default time limit exceeding 20 hours.

The producer's validator/self-attack nevertheless reports the XAG 116 semantics as passing. Therefore the missing exception can coexist with candidate validator PASS.

### Why this is material

This is not a harmless omission of explanatory prose. It changes the applicability/acceptance semantics of a source-defined exception. A non-core-UI time limit whose default exceeds 20 hours is source-exempt, but the exact v6 model can continue to demand the mapped XAG 116 expectations because that exemption cannot be represented or evaluated.

The candidate is therefore stricter than the first-party source. That is source-semantic inflation and violates the producer acceptance contract requiring preservation of source conditions, exceptions, alternatives, and ambiguity, plus a validator that rejects semantic inflation/weakening.

### Required correction

A bounded successor must:

- restore `default_time_limit_exceeds_20_hours` (or an exactly equivalent deterministic predicate) to every XAG 116 expectation to which the source exception block applies;
- preserve the existing core-gameplay, real-time/no-alternative, essential-task, 10×, 20-second, ten-extension, and disable semantics;
- add an adversarial validator fixture proving removal of the >20-hour exemption fails;
- prevent inversion of the exception into a positive requirement;
- leave unrelated XAG 108–123 and XAG 101–107 records untouched.

Successor routed as Issue #264 / `W2-REM-ACC-07`.

## 4. Other sampled attacks before negative termination

The review sampled several high-risk areas before the MAJOR was established:

- XAG 118 quantitative luminance/red-flash/spatial-pattern thresholds in v6 correspond to the current first-party page at the sampled load-bearing values: 10% luminance change, darker value below 0.8, approximately >3 flashes/second, approximately 20% area, saturated-red ratio >=0.8, `(R-G-B)*320 > 20`, and >10% spatial contrast.
- XAG 121 preserves the website WCAG 2 Level AA reference as accessibility best-practice source material rather than upgrading it to legal/compliance authority.
- Aggregate state remains fail-closed in the producer packet: empirical accessibility evidence `NOT_RUN`, `mapping_complete: false`, `IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN`, `W2-REV-M02: OPEN_BOUNDED`, production implementation readiness false, and no legal/platform/canonical/integration authority.

These sampled observations do not convert the negative review into exhaustive acceptance of those pages or of the remaining XAG 108–123 inventory.

## 5. Disposition

```yaml
review_disposition: CHANGES_NEEDED
findings:
  - id: W2-REV-ACC06-M01
    severity: MAJOR
    state: OPEN
    summary: XAG 116 default-over-20-hours exemption omitted from policy and validator
    successor_issue: 264
blockers: 0
majors: 1
correction_requiring_minors: 0
reviewed_packet_accepted: false
reviewed_packet_integration_eligible: false
source_modality_consider_inflation_sample: NOT_REPRODUCED
xag116_exception_fidelity: FAIL
xag116_validator_exception_loss_guard: FAIL
xag118_threshold_sample: PASS_SAMPLED
aggregate_state_fail_closed: PASS
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
production_implementation_ready: false
integration_authorized: false
canonicality: NOT_CANONICAL
review_exhaustiveness: NEGATIVE_EARLY_TERMINAL_NOT_EXHAUSTIVE
```

Exact Issue #259 / PR #261 is **not eligible for integration** under this review. Remediation and a fresh scoped review of the corrected exact packet are required before integration eligibility can be re-derived.

## 6. Authority boundary

This is noncanonical negative review provenance only. It grants no empirical accessibility PASS, mapping completion, implementation/readiness/release authority, legal/compliance status, platform certification, verification PASS, merge/integration authority, decision authority, or canonical status. Mergeability and draft state are compatibility facts only.
