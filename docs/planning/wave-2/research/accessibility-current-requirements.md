# W2-REM-ACC-09 — enforce persistent return links on every submenu

**Mission:** `W2-REM-ACC-09` / Issue #275  
**Winning claim:** comment `5293060848`  
**Claim base:** `main@3f06e40020201493eaed138394889a6f7f09fda7`  
**Required review:** Issue #273 terminal `CHANGES_NEEDED` comment `5293049701`, head `ff66673fa36bae8a190a2bd3205f3059e2fb1b67`, work `791a3991c135a4a2d842f86242a88eaeda172a26`  
**Finding:** `W2-REV-ACC09-M01` / MAJOR — `SOURCE_QUANTIFIER_WEAKENING_AND_INCOMPLETE_VALIDATOR_ORACLE`  
**Immutable producer input:** Issue #270 policy v8 blob `f1d07ef936f6187529ffc1e84d3fd2f2b4f06b96`, report v8 blob `260abddcec26584c62a3bb213ac6e6ea0f90ad0a`  
**Authority:** bounded noncanonical remediation only; fresh independent/degraded-independent review remains mandatory.

## 1. Scope

Issue #273 accepted the v8 scaled/zoomed-map semantics, same-input focus-escape semantics, inventory arithmetic, preserved XAG 116 correction, and fail-closed aggregate state within its bounded review scope. It found one remaining MAJOR: v8 describes persistent submenu return navigation with `trigger: submenu_exists` and a singular `persistent_return_link_present` predicate, so a mechanically evaluated candidate can satisfy the record even when only some of several submenus expose a persistent return path.

This remediation consumes exact v8 as immutable input and changes exactly that quantifier/oracle defect. It adds, removes, splits, or renames no XAG identity and does not change the two other XAG 112 additions from Issue #270.

## 2. Source-faithful correction

The current Microsoft XAG 112 guidance requires persistent links back to the main menu screen or initial interactive screen **on all submenus**. The v9 correction therefore models the applicable submenu set explicitly and quantifies over it with `ALL`.

For every applicable submenu, the predicate requires at least one persistent return path whose target is one of the source-permitted alternatives:

- `main_menu_screen`; or
- `initial_interactive_screen`.

The two targets remain alternatives. A submenu is not required to expose both.

If there are no applicable submenus, this clause is not applicable rather than vacuously claiming positive coverage.

## 3. Mechanical oracle

`ACCESSIBILITY-POLICY-VALIDATOR-v9` binds exact v8 and replaces only the semantic body of `XAG112-SUBMENU-PERSISTENT-RETURN-LINK`.

The load-bearing universal coverage oracle is:

> For every applicable submenu `s`, `s` has at least one persistent return path whose target is `main_menu_screen` or `initial_interactive_screen`.

The validator must reject if any applicable submenu lacks such a path. A compliant sibling submenu cannot mask a noncompliant submenu.

Three explicit fixtures make the quantifier mechanically visible:

1. two submenus, each with one allowed return path → **PASS**;
2. two submenus, one with an allowed return path and one with none → **REJECT_UNIVERSAL_COVERAGE_FAILURE**;
3. one submenu returning only to `initial_interactive_screen` → **PASS**, proving the two allowed targets were not accidentally converted into simultaneous requirements.

The adversarial contract also rejects removal of the universal quantifier, partial multi-submenu coverage, unallowed-target-only coverage, target-alternative inversion, unrelated v8 changes, regression of the XAG 116 correction, and fail-open empirical/readiness state.

## 4. Preservation proof

The exact XAG identity/count contract remains unchanged from v8:

- XAG 112: **14** atomic records;
- XAG 108–123: **113** atomic records;
- composed XAG 101–123: **218** atomic records;
- inherited XAG 101–107: **105** atomic records.

`XAG112-SCALED-MAP-NONSCROLLING-NAVIGATION` remains exact v8 semantics, including the nonexclusive source-example treatment.

`XAG112-SAME-INPUT-FOCUS-ESCAPE` remains exact v8 semantics, including same-input normal behavior and the clear-prompt requirement only as the source-conditional fallback.

The inherited XAG 116 default-over-20-hours exception remains preserved. No unrelated v8 semantic record is redefined.

Issue #269 still did not accept untouched XAG 113–123. This bounded correction does not turn that historical review gap into full corrected-mapping acceptance.

## 5. Finding disposition and self-review

`W2-REV-ACC09-M01` is **RESOLVED_PENDING_FRESH_REVIEW** in this producer packet:

- every applicable submenu explicitly covered by a universal quantifier: **YES**;
- partial multi-submenu coverage mechanically rejected: **YES**;
- main-menu vs initial-interactive-screen target choice remains alternative: **YES**;
- XAG identity/count changes: **NO**;
- scaled-map record changed: **NO**;
- same-input focus-escape record changed: **NO**;
- corrected XAG 116 semantics changed: **NO**;
- unrelated v8 semantics changed: **NO**;
- empirical accessibility PASS claimed: **NO**;
- mapping completion or aggregate blocker clearance claimed: **NO**.

Bounded producer self-review finds 0 unresolved BLOCKER, 0 unresolved MAJOR, and 0 correction-requiring MINOR in this remediation scope. Producer self-review is provenance only and cannot satisfy the required fresh independent review.

## 6. Preserved fail-closed state

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

This task creates no accessibility PASS, full corrected XAG 108–123 acceptance, readiness, implementation, release, legal/compliance, platform certification, verification-PASS, integration, decision, or canonical authority.

## 7. Required next transition

Freeze this remediation at an exact terminal head with an exact-head draft PR, then perform a fresh independent/degraded-independent scoped review of this exact v9 correction before any producer integration eligibility.

A clean bounded review may make this remediation packet separately eligible for noncanonical squash integration under repository authority, but it still cannot substitute for the later fresh full corrected XAG 108–123 review covering the untouched XAG 113–123 surface before an empirical accessibility successor is derived.
