# W2-REV-ACC-09 — scoped review of XAG 112 navigation remediation

**Mission:** `W2-REV-ACC-09` / Issue #273  
**Task class:** required scoped accessibility review  
**Trust profile:** `DEGRADED_SINGLE_AGENT` fresh reviewer episode  
**Winning claim:** Issue #273 comment `5293008919`  
**Review base:** `main@ed26280a4fd409d499a7a5e50248e980ee125dba`  
**Canonical Planning Program v1 blob:** `e3120ec203c4156328770aa86c12fbb7187966dc`  
**Reviewed producer:** Issue #270 terminal comment `5292997562`  
**Reviewed producer head:** `284b9b2723f07f828202f3ce053d7eaae51e7e89`  
**Reviewed producer work:** `1a2a97fb5561c3ec9cd1db151db18f104f2040dd`  
**Reviewed PR:** #272, draft, exact head `284b9b2723f07f828202f3ce053d7eaae51e7e89`  
**Reviewed policy v8 blob:** `f1d07ef936f6187529ffc1e84d3fd2f2b4f06b96`  
**Reviewed report v8 blob:** `260abddcec26584c62a3bb213ac6e6ea0f90ad0a`  
**Immutable integrated policy v7 blob:** `4cf9113bc6c4c663db360594e54b5403cc9e5588`  
**Source negative review:** Issue #269 terminal `5292556689`, finding `W2-REV-ACC08-M01`  
**Disposition:** `CHANGES_NEEDED`

## 1. Frozen identity and independence

This review was claimed only after Issue #270 terminalized `REVIEW_READY`. Issue #270 and PR #272 were treated as immutable producer inputs. The producer exact head remained `284b9b2723f07f828202f3ce053d7eaae51e7e89` throughout the review and PR #272 remained open/draft/mergeable against `main@ed26280a4fd409d499a7a5e50248e980ee125dba` with exactly three changed files:

- `docs/planning/handoffs/issue-270.md`;
- `docs/planning/wave-2/research/accessibility-current-requirements.md`;
- `docs/planning/wave-2/research/accessibility-requirements-policy.yaml`.

Draft and mergeable state are compatibility facts only and create no integration authority.

A duplicate routing issue, #274, was independently terminalized `SUPERSEDED` without a claim, branch, or substantive work after recognizing Issue #273 as the earlier valid route and active owner. It is not review authority.

## 2. Fresh first-party XAG 112 attack

Microsoft XAG 112 (`UI navigation`) was re-read on `2026-08-14` at:

`https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/112`

The page reports XAG v3.2 and last updated `2026-03-04`. The three routed implementation-guideline obligations are:

1. when game-map UI is scaled or zoomed, provide an alternative map-navigation method that does not require scrolling; the supplementary text-list wording is an example, not the only allowed implementation;
2. provide persistent links back to the main menu screen or initial interactive screen **on all submenus**;
3. if focus can be moved to a UI element with an input method, focus should ordinarily be movable away with the same input method; if moving away requires navigation inconsistent with the rest of the interface, clear interaction prompts should explain how to escape focus.

The second obligation contains a load-bearing universal scope: the return path must cover every applicable submenu, not merely exist somewhere in a UI that contains submenus.

## 3. Exact v8-over-v7 reconstruction

The reviewed v8 overlay binds exact integrated v7 policy blob `4cf9113bc6c4c663db360594e54b5403cc9e5588` and declares three new XAG 112 identities:

- `XAG112-SCALED-MAP-NONSCROLLING-NAVIGATION`;
- `XAG112-SUBMENU-PERSISTENT-RETURN-LINK`;
- `XAG112-SAME-INPUT-FOCUS-ESCAPE`.

The PR diff contains no producer changes outside the two accessibility research files plus the Issue #270 handoff. The overlay composition contract declares inherited v7 semantics immutable and adds rather than replaces XAG 112 identities.

The count arithmetic is internally coherent:

```yaml
inherited_xag_101_107_atomic_clause_count: 105
prior_xag_108_123_atomic_clause_count: 110
prior_xag_112_atomic_clause_count: 11
corrected_xag_112_atomic_clause_count: 14
corrected_xag_108_123_atomic_clause_count: 113
corrected_composed_atomic_clause_count: 218
xag_116_atomic_clause_count: 4
```

Thus the intended mechanical delta is `+3` identities only: XAG 112 `11 -> 14`, XAG 108-123 `110 -> 113`, composed XAG 101-123 `215 -> 218`.

## 4. Clean bounded checks

### 4.1 Scaled/zoomed game-map rule

The record is conditionally triggered by `game_map_ui_is_scaled_or_zoomed`, requires a non-scrolling alternative navigation method, explicitly marks implementation form nonexclusive, and has an adversarial fixture rejecting conversion of the text-list example into the only allowed implementation. No defect was found in this bounded semantic.

### 4.2 Same-input focus escape

The record preserves same-input escape as the normal case and models the clear-prompt behavior only when moving focus away requires navigation inconsistent with the rest of the interface. The validator declares both fallback-inversion and conditional-prompt-loss rejection fixtures. No defect was found in this bounded semantic.

### 4.3 Preserved XAG 116 correction

The v8 contract loads exact v7 and explicitly preserves the reviewed XAG 116 correction, including `default_time_limit_exceeds_20_hours` exception semantics. It adds an adversarial fixture for regression of that correction. This bounded review found no v8 delta that redefines XAG 116.

### 4.4 Fail-closed aggregate state

The reviewed packet preserves:

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

Issue #269's negative early termination remains non-exhaustive for untouched XAG 113-123. This bounded review does not convert preservation of those records into fresh source-fidelity acceptance.

## 5. Finding

### `W2-REV-ACC09-M01` — MAJOR / OPEN_BOUNDED

**Class:** source-quantifier weakening / incomplete semantic-validator oracle.

**Source obligation:** persistent return links to the main menu screen or initial interactive screen are required **on all submenus**.

**Exact reviewed v8 atomic contract:**

```yaml
XAG112-SUBMENU-PERSISTENT-RETURN-LINK:
  applicability: CONDITIONAL
  trigger: submenu_exists
  required_semantics:
    persistent_return_link_present: true
    return_target_alternatives_minimum: 1
    allowed_return_targets:
      - main_menu_screen
      - initial_interactive_screen
```

The source-recheck summary correctly names `all_submenus_have_persistent_return_link_to_main_or_initial_interactive_screen`, but that universal quantifier is not carried into the atomic required semantics. `submenu_exists` is only an existence trigger, and `persistent_return_link_present: true` is singular/non-quantified.

The corresponding semantic assertion is likewise non-universal:

> submenu record applies when a submenu exists and requires a persistent return link to at least one source-allowed target

The adversarial fixture set checks target-alternative inversion but contains no partial-coverage witness such as multiple submenus where one submenu lacks the persistent return path.

**Reproduction witness:** consider two applicable submenus, A and B. A has a persistent link to the main menu; B has no persistent return link. Under the declared non-quantified contract, `submenu_exists` is true and `persistent_return_link_present` can be true because A supplies such a link. The declared target-alternative condition also passes. No v8 fixture requires the validator to reject B's missing return path.

**Impact:** exact v8 can claim its atomic submenu semantic and declared validator contract satisfied without proving the first-party `all submenus` obligation. This is the same class of mechanical-oracle weakness Issue #270 was required to eliminate: source semantics are present in prose but not made rejectable at the machine-readable contract boundary. A clean scoped-review disposition is therefore unavailable.

**Required correction:** preserve the single XAG 112 identity and all target alternatives, but make the atomic semantic explicitly universal over every applicable submenu and add a validator assertion/adversarial fixture that rejects partial submenu coverage. No new XAG identity or count change is required.

**Successor:** Issue #275 / `W2-REM-ACC-09`.

## 6. Disposition

```yaml
review_disposition: CHANGES_NEEDED
review_scope: ISSUE_270_XAG112_BOUNDED_REMEDIATION
reviewed_head_sha: 284b9b2723f07f828202f3ce053d7eaae51e7e89
reviewed_policy_v8_blob: f1d07ef936f6187529ffc1e84d3fd2f2b4f06b96
reviewed_report_v8_blob: 260abddcec26584c62a3bb213ac6e6ea0f90ad0a
blockers: 0
majors: 1
correction_requiring_minors: 0
findings:
  - id: W2-REV-ACC09-M01
    severity: MAJOR
    state: OPEN_BOUNDED
    successor_issue: 275
scaled_map_semantics_review: CLEAN_BOUNDED
focus_escape_semantics_review: CLEAN_BOUNDED
submenu_semantics_review: CHANGES_NEEDED
xag_112_declared_count: 14
xag_108_123_declared_count: 113
composed_xag_101_123_declared_count: 218
xag_116_v7_correction_preserved: true
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
aggregate_accessibility_blocker: IR-BLOCKER-ACCESSIBILITY-CURRENT
blocker_authority_state: OPEN
w2_rev_m02: OPEN_BOUNDED
full_xag_108_123_review_complete: false
producer_integration_eligible: false
production_implementation_ready: false
verification_pass_authority: false
integration_authority_created: false
canonicality: NOT_CANONICAL
```

`CLEAN_FOR_NONCANONICAL_INTEGRATION` is not available for exact Issue #270 / PR #272. PR #272 must not be integrated on the basis of this review.

## 7. Authority boundary and next transition

This review creates noncanonical negative review provenance only. It grants no empirical accessibility PASS, mapping completion, full corrected XAG 108-123 acceptance, implementation/readiness/release authority, legal/compliance status, platform certification, verification PASS, merge/integration authority, decision authority, or canonical authority.

Issue #275 is the only routed remediation successor for `W2-REV-ACC09-M01`. After it terminalizes, its exact correction must receive fresh independent/degraded-independent scoped review. Even after that bounded defect is clean, the untouched XAG 113-123 surface still requires a fresh full corrected XAG 108-123 review before any empirical accessibility successor is eligible.