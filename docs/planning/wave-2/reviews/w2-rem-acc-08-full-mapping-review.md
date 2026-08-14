# W2-REV-ACC-08 — full corrected XAG 108–123 mapping review

**Mission:** `W2-REV-ACC-08` / Issue #269  
**Trust profile:** `DEGRADED_SINGLE_AGENT` fresh reviewer episode  
**Winning claim:** comment `5292529597`  
**Reviewed integrated main:** `ace13b7c93b037f4cfa9fb98e4f09e267db68440`  
**Canonical program blob:** `e3120ec203c4156328770aa86c12fbb7187966dc`  
**Reviewed policy v7 blob:** `4cf9113bc6c4c663db360594e54b5403cc9e5588`  
**Reviewed report v7 blob:** `1a1ec00e6b8143d7f233d58ecc3889d8f7c1550f`  
**Immutable v6 policy blob:** `80e278315d6b7a108d89da3f5a99086a8ef91bf7`  
**Controlling v6 review:** Issue #262 terminal `5290467457` / `CHANGES_NEEDED`  
**Bounded XAG 116 correction review:** Issue #267 terminal `5291976901` / `CLEAN_FOR_NONCANONICAL_INTEGRATION` for `W2-REV-ACC06-M01` only  
**Disposition:** `CHANGES_NEEDED`

## 1. Frozen identity and review boundary

This review was created only after the reviewed XAG 116 remediation and its bounded review provenance had been squash-integrated. At claim time and again before materialization:

- `main` was exactly `ace13b7c93b037f4cfa9fb98e4f09e267db68440`;
- canonical Planning Program v1 remained blob `e3120ec203c4156328770aa86c12fbb7187966dc`;
- Issue #269 had no competing claim and `planning/issue-269` was created from that exact main;
- exact v7 policy blob `4cf9113bc6c4c663db360594e54b5403cc9e5588` and report blob `1a1ec00e6b8143d7f233d58ecc3889d8f7c1550f` were treated as immutable reviewed inputs;
- exact v6 policy blob `80e278315d6b7a108d89da3f5a99086a8ef91bf7` was treated as the immutable logical base for every non-XAG116 v7 record.

Issue #262 is the controlling negative review of v6. It terminalized after finding one reproducible material XAG 116 source-fidelity defect and did not claim exhaustive acceptance of unaffected v6 clauses. Issue #267 then reviewed only the bounded XAG 116 correction and explicitly did not exhaustively re-adjudicate unrelated v6 atomization. This review therefore attacks the corrected final mapping rather than treating either earlier review as whole-tranche acceptance.

## 2. Fresh first-party source attack

Fresh Microsoft XAG source was consulted on `2026-08-14` before reconciling the inherited v6 expected inventory. The first materially failing untouched page is:

`https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/112`

The page reports last updated `2026-03-04` and is XAG v3.2 accessibility best-practice guidance.

The XAG 112 implementation-guideline sequence includes, after the text/UI scaling reflow rule represented by the producer, three additional load-bearing navigation expectations:

1. **Scaled/zoomed game-map alternative navigation.** When a game-map UI is scaled or zoomed, the source expects an alternative way to navigate the map that does not require scrolling. A supplementary text list of points of interest is given as an example, not as the sole allowed implementation.
2. **Persistent submenu return path.** All submenus should provide persistent links back to the main menu screen or the initial interactive screen.
3. **Same-input focus escape with conditional prompt fallback.** If focus can be moved to a UI element using an input method, the player should be able to move focus away using that same input method. If moving away necessarily uses navigation inconsistent with the rest of the interface, clear interaction prompts should explain how to move focus away.

These are implementation-guideline bullets, not example-only prose. The third rule contains an explicit conditional fallback that must not be flattened into an unconditional simultaneous prompt requirement.

## 3. Exact policy reproduction

Exact v6 policy blob `80e278315d6b7a108d89da3f5a99086a8ef91bf7` declares:

```yaml
per_page_new_clause_counts:
  XAG-112: 11
```

Its exact XAG 112 expected identity set is:

```text
XAG112-INITIAL-ACCESSIBILITY-PATH
XAG112-LOGICAL-CONSISTENT-NAVIGATION-ORDER
XAG112-KEYBOARD-CONTROLLER-DIGITAL-NAVIGATION
XAG112-MULTI-INPUT-NAVIGATION
XAG112-REPEATED-COMPONENT-ORDER
XAG112-SEQUENTIAL-FOCUS-ORDER
XAG112-FOCUS-ALIGNS-MEANING-OR-VISUAL-FLOW
XAG112-LINEAR-MENU-LOOP
XAG112-MULTIPLE-CONTENT-LOCATION-METHODS
XAG112-NAVIGATION-UPDATES-WITH-LAYOUT
XAG112-SCALED-TEXT-ONE-DIRECTION-SCROLL
```

The exact expected list ends at `XAG112-SCALED-TEXT-ONE-DIRECTION-SCROLL`.

Cold searches of the exact v6 policy produce no atomic record or required semantic corresponding to:

- scaled/zoomed **map** alternative navigation without scrolling;
- persistent links from **all submenus** back to the main/initial interactive screen;
- moving focus away using the **same input** method, with the source's conditional clear-prompt fallback.

The only `persistent` match in v6 is an unrelated XAG 108 trigger (`game_has_persistent_progress`). No `zoom` or `same input` mapping exists in the XAG 112 policy surface.

## 4. Why v7 does not repair the defect

Exact v7 blob `4cf9113bc6c4c663db360594e54b5403cc9e5588` states that its composition algorithm:

- loads exact v6;
- replaces only `XAG116-UI-TIME-LIMIT-MODIFIABLE` and `XAG116-IMPORTANT-ELEMENT-DURATION-MODIFIABLE`;
- preserves every non-XAG116 v6 record, source registration, evidence/gap record, empirical state, blocker state, and authority boundary.

Therefore the XAG 112 omission is inherited byte-for-logical-byte into v7. The bounded XAG 116 correction cannot supply or authorize missing XAG 112 semantics.

The inherited v6 contract nevertheless asserts:

```yaml
source_clause_mapping_candidate_complete: true
summary_only_pages_after_patch: []
```

and its validator's expected-set checks are self-consistent only against the incomplete producer-declared 11-member XAG 112 set. The generic fixture `MISSING_XAG108_123_CLAUSE: REJECT_EXPECTED_SET_MISMATCH` cannot reject a first-party source obligation that was never placed into the expected set in the first place.

## 5. Finding

### `W2-REV-ACC08-M01` — MAJOR / OPEN_BOUNDED

**Class:** source-clause omission / incomplete expected-set oracle.

**Reproduction:** current Microsoft XAG 112 contains the three implementation-guideline obligations described above; exact v6/v7 contains none of them while claiming source-clause candidate completeness.

**Impact:** the current mapping can mechanically PASS its declared 110-record XAG 108–123 expected-set contract while omitting three current first-party XAG 112 obligations. Consequently the mapping component cannot receive a clean whole-tranche review disposition, and no empirical accessibility successor may treat `source_clause_mapping_candidate_complete: true` as independently accepted.

**Required correction:** route exactly one bounded successor that adds source-faithful atomic records for the three XAG 112 obligations, updates the exact expected XAG 112/composed inventory mechanically, and adds negative fixtures that reject omission and condition/fallback inversion without rewriting unrelated XAG 101–123 semantics.

**Successor:** Issue #270 / `W2-REM-ACC-08`.

## 6. Non-exhaustive negative termination

The material XAG 112 defect is sufficient to invalidate the clean disposition for the full corrected XAG 108–123 mapping. In accordance with the repository's fail-closed negative-review pattern, this review stops substantive source acceptance at that point.

This artifact therefore **does not assert exhaustive acceptance or rejection of XAG 113–123** and does not upgrade any unaffected v7 record. Any later clean whole-tranche review must re-attack the corrected complete mapping from fresh first-party source rather than treating this negative review as positive authority for untouched pages.

The previously reviewed XAG 116 >20-hour correction remains immutable reviewed provenance and is not reopened by this finding; Issue #270 must preserve it.

## 7. Disposition and aggregate state

```yaml
review_disposition: CHANGES_NEEDED
review_scope: CORRECTED_V7_XAG108_123_MAPPING
review_exhaustiveness: NEGATIVE_EARLY_TERMINATION_AFTER_MATERIAL_XAG112_DEFECT
findings:
  - id: W2-REV-ACC08-M01
    severity: MAJOR
    state: OPEN_BOUNDED
    successor_issue: 270
blockers: 0
majors: 1
correction_requiring_minors: 0
xag112_declared_atomic_clause_count: 11
xag112_missing_source_obligations: 3
source_clause_mapping_candidate_complete_review_result: FAIL
current_v7_integration_status: INTEGRATED_NONCANONICAL_PROVENANCE
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
aggregate_accessibility_blocker: IR-BLOCKER-ACCESSIBILITY-CURRENT
blocker_authority_state: OPEN
w2_rev_m02: OPEN_BOUNDED
production_implementation_ready: false
legal_compliance_claimed: false
platform_certification_claimed: false
verification_pass_authority: false
decision_authority: false
integration_authority_created: false
canonicality: NOT_CANONICAL
```

`CLEAN_FOR_EMPIRICAL_ACCESSIBILITY_SUCCESSOR` is not available for this exact v7 mapping.

## 8. Authority boundary and next transition

This review creates only noncanonical negative review provenance. It grants no empirical accessibility PASS, no mapping completion, no implementation/readiness/release authority, no legal/compliance status, no platform certification, no verification PASS, no integration/merge authority, no decision authority, and no canonical authority.

Issue #270 remains blocked until this review terminalizes `CHANGES_NEEDED` at an exact review head. After that terminal status, the bounded XAG 112 remediation becomes the next accessibility continuation; it must itself receive fresh independent/degraded-independent scoped review before any corrected mapping can be considered for later convergence.