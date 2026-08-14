# W2-REV-ACC-10 — scoped review of all-submenus return-path remediation

## Review identity

- mission: `W2-REV-ACC-10`
- issue: #278
- winning claim: `5293126459`
- actor/session: `w2-rev-acc-10-gpt56sol-20260814-1410-frontier`
- trust profile: `DEGRADED_SINGLE_AGENT`
- claim base: `main@3f06e40020201493eaed138394889a6f7f09fda7`
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`

## Frozen reviewed producer identity

- producer issue: #275 / `W2-REM-ACC-09`
- winning producer claim: `5293060848`
- producer terminal `STATUS(REVIEW_READY)`: `5293116667`
- exact producer head: `c310dc5eb6f07ec69c1f57ae625e761ad0770a8b`
- exact producer substantive work: `29e6ecf627d36c0bf718ac3bc7512e1b7adfb02d`
- producer PR: #277, open/draft/mergeable when cold-inspected, exact head `c310dc5eb6f07ec69c1f57ae625e761ad0770a8b`, base `main@3f06e40020201493eaed138394889a6f7f09fda7`
- producer policy v9 blob: `5cf18195bdfcb377aac7727b65b2d8a479ef8ac3`
- producer report v9 blob: `3665805bb6391bc0c7b6b27ca2f70b7f0b88aaae`
- producer handoff blob: `59062e9108706351cbc4ecfae06a1920a02b07ed`
- immutable v8 policy blob: `f1d07ef936f6187529ffc1e84d3fd2f2b4f06b96`
- immutable v8 report blob: `260abddcec26584c62a3bb213ac6e6ea0f90ad0a`
- controlling negative review: Issue #273 terminal comment `5293049701`
- routed finding: `W2-REV-ACC09-M01` / MAJOR / `SOURCE_QUANTIFIER_WEAKENING_AND_INCOMPLETE_VALIDATOR_ORACLE`

Issue #275 / PR #277 was treated as immutable review input. This review did not modify the producer branch.

## Independent first-party source reconstruction

Microsoft XAG 112 (`UI navigation`) was re-read independently on `2026-08-14` at the current first-party Microsoft Learn page. The page reports XAG v3.2 and last updated `2026-03-04`.

The load-bearing source semantics in this bounded review are:

1. persistent links back to the main menu screen **or** the initial interactive screen are to be provided **on all submenus**;
2. the two destinations are source alternatives, not simultaneous required destinations;
3. the adjacent scaled/zoomed-map guidance requires a non-scrolling alternative navigation method while presenting a supplementary text list only as an example;
4. the adjacent focus guidance requires same-input focus escape in the normal case, with clear interaction prompts only when inconsistent escape navigation is required.

The review therefore reconstructed the expected correction before reconciling the producer rationale: a universal predicate over the applicable submenu set, requiring each member independently to expose at least one persistent return path to one of the two permitted targets.

## Exact v9-over-v8 reconstruction

Exact v8 models `XAG112-SUBMENU-PERSISTENT-RETURN-LINK` with `trigger: submenu_exists` and a singular `persistent_return_link_present: true`. That representation does not bind the source's universal `on all submenus` quantifier and can accept a UI where one compliant submenu masks a noncompliant sibling.

Exact v9 consumes exact v8 as immutable input and replaces only that record's semantic body plus mechanically dependent validator/report metadata. The corrected record has:

```yaml
trigger: applicable_submenu_count_gt_0
required_semantics:
  universal_scope:
    collection: applicable_submenus
    quantifier: ALL
    empty_collection_behavior: NOT_APPLICABLE
    predicate:
      persistent_return_path_present: true
      return_target_alternatives_minimum: 1
      allowed_return_targets:
        - main_menu_screen
        - initial_interactive_screen
  target_choice_semantics:
    require_both_allowed_targets: false
    at_least_one_allowed_target_per_applicable_submenu: true
```

This is the minimum coherent repair for `W2-REV-ACC09-M01`. No XAG identity is added, removed, split, or renamed.

## Mechanical/adversarial attacks

### Universal quantifier

**PASS.** The contract applies `ALL` to `applicable_submenus`; the validator's pass condition requires every applicable submenu independently to have a source-allowed persistent return path. A compliant sibling cannot mask a failing submenu.

### Partial multi-submenu coverage

**PASS.** The load-bearing fixture has two applicable submenus, one with `main_menu_screen` and one with an empty return-path set, and requires `REJECT_UNIVERSAL_COVERAGE_FAILURE`. The adversarial fixture table separately requires the same rejection class for partial multi-submenu coverage and rejects removal of the universal quantifier as `REJECT_QUANTIFIER_WEAKENING`.

### Return-target alternatives

**PASS.** Allowed targets remain exactly `main_menu_screen` and `initial_interactive_screen`; `require_both_allowed_targets: false` is explicit. A one-submenu fixture using only `initial_interactive_screen` must PASS, while simultaneous-target inflation and unallowed-target-only coverage are explicit rejection cases.

### Scope leakage

**PASS.** Exact v9 declares exact v8 policy/report blobs as immutable inputs, replaces exactly the submenu record semantic body, requires every other v8 semantic record to remain byte-logically unchanged, and has explicit `REJECT_SCOPE_LEAKAGE` fixtures for changes to the scaled-map record, same-input focus-escape record, or any unrelated v8 record.

### Inventory and preserved correction

**PASS.** The expected XAG 112 identity set remains the exact 14 identities from v8. Declared/reconstructed counts remain:

- XAG 112: `14`
- XAG 108–123: `113`
- composed XAG 101–123: `218`
- inherited XAG 101–107: `105`

The exact v8 XAG 116 default-over-20-hours correction remains an immutable preservation requirement, with a dedicated regression rejection case.

### Fail-closed aggregate state

**PASS.** Exact v9 and its report preserve:

```yaml
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
full_xag_108_123_review_complete: false
untouched_xag_113_123_accepted: false
production_implementation_ready: false
legal_compliance_claimed: false
platform_certification_claimed: false
verification_pass_authority: false
integration_authorized: false
canonicality: NOT_CANONICAL
```

Issue #269's negative early termination therefore remains authoritative history: untouched XAG 113–123 are not accepted by this bounded review, and no empirical-accessibility successor is unlocked by this review alone.

### PR #277 cold inspection

**PASS.** PR #277 was re-fetched open, draft, mergeable, base `main`, exact head `c310dc5eb6f07ec69c1f57ae625e761ad0770a8b`, with exactly three declared producer files:

- `docs/planning/handoffs/issue-275.md`
- `docs/planning/wave-2/research/accessibility-current-requirements.md`
- `docs/planning/wave-2/research/accessibility-requirements-policy.yaml`

Draft/mergeable status is treated only as compatibility/visibility evidence and does not itself grant integration authority.

## Findings

- unresolved BLOCKER: **0**
- unresolved MAJOR: **0**
- correction-requiring MINOR: **0**

No material defect was reproduced in this bounded remediation scope.

## Disposition

`CLEAN_FOR_NONCANONICAL_INTEGRATION`

Exact Issue #275 / PR #277 closes `W2-REV-ACC09-M01` within the bounded all-submenus remediation scope and is eligible for a **separately authorized squash-only noncanonical integration** under repository authority, subject to a fresh exact-head/current-main compatibility check at integration time.

This disposition does **not** complete the full corrected XAG 108–123 review, accept untouched XAG 113–123, produce empirical accessibility evidence, set `mapping_complete: true`, clear `IR-BLOCKER-ACCESSIBILITY-CURRENT` or `W2-REV-M02`, create implementation/readiness/release authority, establish legal/compliance or platform certification, grant verification-PASS/decision authority, or create canonical authority.

The later full corrected XAG 108–123 review remains mandatory before any empirical-accessibility successor may be derived.