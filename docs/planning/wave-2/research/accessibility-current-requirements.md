# W2-REM-ACC-02 — mechanically total accessibility source-clause remediation

**Mission:** `W2-REM-ACC-02` / Issue #135  
**Base main:** `042d140b5d2e0b951da4528e1867514983418d6f`  
**Frozen predecessor:** W2-REM-ACC-01 / Issue #96 work/head `3937f65ae4eb495420d1240c2b739841aa14a037`  
**Predecessor policy blob:** `78690cf658967b2ded35e738df125959a56f0d86`  
**Independent review:** W2-PG-REM-ACC-01 / Issue #134 terminal comment `5277197150`, head `771cec9d69483b5d2411b40b3d133b024d1e7aba`  
**Findings:** `PG-REM-ACC-M01`, `PG-REM-ACC-M02`  
**Observed first-party sources:** `2026-08-13`  
**Authority:** bounded noncanonical remediation input; formal `W2-REV-01` remains required.

## 1. Scope and preserved fail-closed state

This revision repairs only the two MAJOR findings from Issue #134. The exact Issue #96 packet is immutable input. Its valid authority boundaries remain unchanged: Microsoft XAG is accessibility best-practice evidence rather than legal certification; direct Valve compatibility requirements remain distinct from project-selected Proton evidence; empirical accessibility checks remain `NOT_RUN`; and no engine, production, release, readiness, verification, or canonicalization authority is created here.

The aggregate remains intentionally fail closed:

```yaml
mapping_complete: false
blocker_id: IR-BLOCKER-ACCESSIBILITY-CURRENT
blocker_authority_state: OPEN
summary_only_pages:
  - XAG-102..106
  - XAG-108..123
required_formal_review: W2-REV-01
```

This task does not broaden into atomic expansion of the remaining XAG pages.

## 2. `PG-REM-ACC-M01` — source-page atomicity is now derived

Issue #134 showed that Issue #96 trusted the page-level `ATOMICALLY_EXPANDED` flag. A clause could therefore lose a source semantic while the page still appeared fully expanded.

The v2 policy fixes that by composing over the exact Issue #96 policy blob and adding an explicit expected source-clause inventory for every page currently marked `ATOMICALLY_EXPANDED`: XAG 101 has 11 expected clause IDs and XAG 107 has 17, for exactly 28 inherited atomic records. The validator contract requires exact set-and-count equality, unique identities, valid source bindings, deterministic applicability, required triggers, resolvable evidence/gap references, and required semantic contracts before an atomic page can remain accepted.

A page marked `ATOMICALLY_EXPANDED` without an expected inventory, or with a missing/extra/duplicate clause, is mechanically rejected. Summary-only XAG pages therefore cannot be upgraded by changing a flag alone.

### 2.1 XAG 101 line-width semantics

The current first-party Microsoft XAG 101 text-spacing guidance was rechecked on `2026-08-13`. The v2 semantic contract now retains all load-bearing line-width conditions together:

```yaml
line_width_max_characters: 80
line_width_max_characters_cjk: 40
line_width_measurement_text_resize_percent: 100
line_width_character_count_excludes_spaces: true
```

The previously preserved spacing thresholds remain bound as well: line spacing `1.5`, paragraph spacing `2x` line spacing, letter spacing `0.12x` font size, and word spacing `0.16x` font size.

The deterministic adversarial fixtures require rejection if either the 100%-resize condition or the exclusion-of-spaces condition is removed or altered while XAG 101 remains marked atomic.

## 3. `PG-REM-ACC-M02` — direct Valve controller criterion completed

The current first-party Valve Steam Deck / Steam Machine compatibility checklist was rechecked on `2026-08-13`. Alongside the existing requirement that the default controller configuration access all content, Valve currently requires that players not need to change an in-game setting to enable controller support or that configuration.

The v2 policy adds the missing direct requirement:

```yaml
ACC-DECK-09:
  authority_class: PLATFORM_COMPATIBILITY_REQUIRED
  semantics:
    no_in_game_setting_change_required_to_enable_controller_support_or_default_configuration: true
  evidence_requirement_refs:
    - ACC-EV-INPUT-CONTROLLER-01
```

`ACC-PROJECT-DECK-PROTON-01` remains separately typed `PROJECT_SELECTED_PLATFORM_EVIDENCE`; it is not promoted into the direct Valve checklist.

## 4. Mechanical validation contract

`ACCESSIBILITY-POLICY-VALIDATOR-v2` is encoded in the machine-readable policy as a deterministic composition/validation procedure over the exact frozen v1 blob plus this bounded overlay. It checks:

1. exact expected-vs-actual atomic clause set and count for each atomic page;
2. unique/source-valid clause identities;
3. applicability and trigger totality;
4. evidence/gap reference integrity;
5. exact required semantic values, including the two XAG 101 measurement conditions;
6. presence of the new direct Valve `ACC-DECK-09` requirement; and
7. aggregate completeness derived only after those checks.

The expected valid state is 28 inherited atomic clauses, XAG 101 and XAG 107 inventory PASS, semantic/reference/applicability checks PASS, direct Valve criterion PASS, summary-only pages fail closed, `mapping_complete: false`, and blocker OPEN.

The declared mutation corpus requires deterministic rejection for: an omitted expected XAG 101 clause; missing or altered 100%-resize semantics; missing or false space exclusion; a dangling evidence ref; a conditional clause without a trigger; a summary page falsely switched to atomic without an inventory; and omission of `ACC-DECK-09`.

## 5. Current-source drift check

The corrected load-bearing facts were checked against current first-party sources on `2026-08-13`:

- Microsoft XAG index remains v3.2 and continues to characterize XAGs as best practices rather than legal/compliance proof.
- XAG 101 retains the 80/40 line-width bounds together with measurement at 100% resize and exclusion of spaces from the character count.
- Valve's current compatibility checklist retains default-controller access to all content and the no-in-game-setting-change criterion for enabling controller support/default configuration.

No material drift was observed for the claims corrected in this task. This source check does not upgrade any summary-only XAG page or any empirical evidence state.

## 6. Finding dispositions and self-review

`PG-REM-ACC-M01` is `RESOLVED`: page atomicity is no longer trusted solely from a flag, expected inventories are explicit for both atomic pages, and the attacked XAG 101 semantics are exact required values with adversarial rejection cases.

`PG-REM-ACC-M02` is `RESOLVED`: the missing direct Valve controller criterion is represented and mechanically required while Proton evidence remains separately typed.

Bounded self-review:

- unresolved BLOCKER: **0**;
- unresolved MAJOR: **0**;
- correction-requiring MINOR: **0**;
- XAG 102–106 and 108–123 still summary-only: **PASS**;
- `IR-BLOCKER-ACCESSIBILITY-CURRENT` still OPEN: **PASS**;
- `mapping_complete` still false: **PASS**;
- direct Valve vs project-selected Proton authority separation: **PASS**;
- empirical accessibility PASS claimed: **NO**;
- legal/Valve certification claimed: **NO**;
- implementation/integration/verification/release/canonicalization authority claimed: **NO**;
- formal `W2-REV-01` still required: **PASS**.

## 7. Downstream contract

Formal `W2-REV-01` should reconstruct the corrected accessibility packet from immutable Issue #96 provenance plus this Issue #135 v2 overlay, finding dispositions, and handoff. No artifact becomes canonical by this remediation or by its mandatory draft PR. Any eventual `main` integration remains separately authorized and squash-only.
