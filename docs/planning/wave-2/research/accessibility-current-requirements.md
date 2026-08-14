# W2-REM-ACC-08 — restore omitted XAG 112 navigation obligations

**Mission:** `W2-REM-ACC-08` / Issue #270  
**Winning claim:** comment `5292959267`  
**Claim base:** `main@ace13b7c93b037f4cfa9fb98e4f09e267db68440`  
**Source review:** Issue #269 terminal `CHANGES_NEEDED` comment `5292556689`, head `79c3ebe86eaacaedbbee6766a70aadc43845d1f1`, work `50f3cc0ace1f94ebac4130d77c1a7a2066bd03da`  
**Finding:** `W2-REV-ACC08-M01` / MAJOR  
**Immutable integrated input:** exact v7 policy blob `4cf9113bc6c4c663db360594e54b5403cc9e5588`, report blob `1a1ec00e6b8143d7f233d58ecc3889d8f7c1550f`  
**Logical v6 input:** policy blob `80e278315d6b7a108d89da3f5a99086a8ef91bf7`  
**Authority:** bounded noncanonical remediation only; fresh independent/degraded-independent review remains mandatory.

## 1. Scope

Issue #269 performed the required full corrected-v7 XAG 108–123 review and terminated negatively after reproducing one coherent material defect in XAG 112. Exact v6, inherited by v7 outside the XAG 116 correction, contains 11 XAG 112 atomic identities but omits three current implementation-guideline obligations while the inherited contract asserts source-clause candidate completeness.

This remediation consumes exact integrated v7 as immutable input and adds only those three missing XAG 112 records plus mechanically dependent inventory/validator metadata. It does not reinterpret, replace, or remove any inherited XAG 101–123 semantic record. In particular, the reviewed v7 XAG 116 default-over-20-hours exception correction remains immutable.

Issue #269 terminated after this material defect. Therefore this remediation does not claim that untouched XAG 113–123 semantics were accepted, and it does not by itself complete the required full corrected-mapping review.

## 2. Fresh first-party XAG 112 recheck

Microsoft XAG 112 (`UI navigation`) was re-read on `2026-08-14` at:

`https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/112`

The page reports XAG v3.2 and last updated `2026-03-04`. The load-bearing omitted guidance remains:

1. When a game-map interface is scaled or zoomed, provide an alternative map-navigation method that does not require scrolling. A supplementary text list of points of interest is presented as an example, not as the only permitted implementation.
2. All submenus should provide persistent links back to the main menu screen or initial interactive screen.
3. When an input method can move focus onto a UI element, that same input method should ordinarily be able to move focus away. If moving focus away necessarily uses navigation inconsistent with the rest of the interface, provide a clear interaction prompt explaining how to escape focus.

The correction preserves those conditions and alternatives rather than promoting examples or fallback language into unconditional simultaneous requirements.

## 3. Correction

`ACCESSIBILITY-POLICY-OVERLAY-v8` loads exact v7 blob `4cf9113bc6c4c663db360594e54b5403cc9e5588` and adds exactly three identities:

- `XAG112-SCALED-MAP-NONSCROLLING-NAVIGATION`;
- `XAG112-SUBMENU-PERSISTENT-RETURN-LINK`;
- `XAG112-SAME-INPUT-FOCUS-ESCAPE`.

### 3.1 Scaled/zoomed game-map navigation

Applicability is conditional on `game_map_ui_is_scaled_or_zoomed`. The record requires a non-scrolling alternative navigation method. The source's supplementary text-list example is explicitly nonexclusive, preventing example-to-requirement inflation.

### 3.2 Persistent submenu return path

Applicability is conditional on a submenu existing. Each applicable submenu requires a persistent return link, with the source-permitted targets modeled as alternatives: the main menu screen or the initial interactive screen. The overlay does not require both targets and does not invent a broader navigation architecture.

### 3.3 Same-input focus escape

Applicability is conditional on a UI element being focusable through an input method. The normal case requires focus to be movable away with the same input method. The clear-prompt rule is modeled only as a conditional fallback when moving away requires navigation inconsistent with the rest of the interface; it is not an unconditional second requirement.

## 4. Mechanical validator hardening

`ACCESSIBILITY-POLICY-VALIDATOR-v8` first binds the exact v7 input and verifies its exact v6 lineage. It then requires the inherited 11 XAG 112 identities plus exactly the three correction identities above.

Corrected inventory is mechanically fixed at:

- XAG 112: **14** atomic records;
- XAG 108–123: **113** atomic records;
- composed XAG 101–123: **218** atomic records.

The validator rejects:

- removal of any one of the three new identities;
- duplicate or extra XAG 112 identities;
- removal of the scaled-map applicability trigger;
- conversion of the source map-list example into the sole accepted implementation;
- conversion of submenu return-target alternatives into simultaneous requirements;
- unconditional promotion of the focus-escape prompt fallback;
- loss of the prompt requirement when inconsistent escape navigation is required;
- any unrelated v7 semantic redefinition;
- regression of the v7 XAG 116 default-over-20-hours correction;
- empirical PASS or `mapping_complete: true` claims while evidence remains `NOT_RUN`.

## 5. Preservation proof

The v8 overlay adds three XAG 112 records and does not replace or remove any v7 semantic record. All inherited XAG 101–111 and XAG 113–123 records remain exact logical inputs from v7. The four XAG 116 identities and the v7 `default_time_limit_exceeds_20_hours` exception correction remain preserved without reinterpretation.

The only intended mechanical count changes are therefore `11 → 14` for XAG 112, `110 → 113` for XAG 108–123, and `215 → 218` for the composed XAG 101–123 inventory.

No empirical accessibility evidence is produced by this task. The negative early termination of Issue #269 remains historical review provenance and is not rewritten into acceptance of untouched XAG 113–123.

## 6. Finding disposition and self-review

`W2-REV-ACC08-M01` is **RESOLVED_PENDING_FRESH_REVIEW** in this producer packet:

- all three omitted XAG 112 obligations represented: **YES**;
- scaled-map example kept nonexclusive: **YES**;
- submenu return-target alternatives preserved: **YES**;
- same-input focus escape and conditional prompt fallback preserved: **YES**;
- omission/duplicate/trigger/alternative/fallback regressions mechanically rejectable: **YES**;
- unrelated v7 semantic records rewritten: **NO**;
- corrected v7 XAG 116 semantics changed: **NO**;
- empirical accessibility PASS claimed: **NO**;
- aggregate blocker cleared: **NO**.

Bounded producer self-review finds 0 unresolved BLOCKER, 0 unresolved MAJOR, and 0 correction-requiring MINOR in this remediation scope. Producer self-review is provenance only and cannot satisfy the required independent review.

## 7. Preserved fail-closed state

```yaml
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
full_xag_108_123_review_complete: false
production_implementation_ready: false
legal_compliance_claimed: false
platform_certification_claimed: false
verification_pass_authority: false
integration_authorized: false
canonicality: NOT_CANONICAL
```

This task creates no accessibility PASS, readiness, implementation, release, legal/compliance, platform certification, verification-PASS, integration, decision, or canonical authority.

## 8. Required next transition

Freeze this remediation at an exact terminal head with an exact-head draft PR, then perform a fresh independent/degraded-independent review of this exact correction before any producer integration eligibility. A clean bounded remediation review would not by itself accept the XAG 113–123 surface that Issue #269 never reached; the required corrected-mapping review must still be completed for that remaining scope before an empirical accessibility evidence successor can be justified.
