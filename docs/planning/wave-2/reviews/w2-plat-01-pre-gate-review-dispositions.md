# W2-PLAT-01 pre-gate review finding dispositions

**Remediation mission:** `W2-REM-PLAT-01` / Issue #92  
**Source mission:** `W2-PLAT-01` / Issue #79  
**Source frozen head/work:** `695d3cd1bc5a017e780db8016ffefa2379d4103d`  
**Source report blob:** `f47ad96baea765580ad9d016d527c932ce3b2768`  
**Source handoff blob:** `479a0b6dfeeec838b60593819ff355c2fb66ec2e`  
**Pre-gate review:** Issue #79 comment `5270240728`  
**Remediation claim:** Issue #92 comment `5270264203`  
**Corrected report blob:** `d6a20c2200cedad97ede36beb9871d420ca7a8ca`  
**Immutable source-record blob:** `f2a9333436c9cbc4fe91ec71507997f46f2247e4`  
**Formal independent review:** still `W2-REV-01`; this document is remediation provenance, not a schema-3 `REVIEW_STATUS`.

## Disposition summary

| Finding | Severity | Disposition | Evidence |
|---|---|---|---|
| `PG-PLAT-M01` monthly Steam survey already stale at claimed observation date | MAJOR | RESOLVED | July 2026 latest-month record; corrected 93.67% Windows / 70.26% Win11 64-bit; explicit monthly-current fail-closed rule; recommendation re-evaluated |
| `PG-PLAT-M02` mutable external sources not reconstructably version-bound | MAJOR | RESOLVED | immutable normalized project citation packet at blob `f2a933...`, bound from corrected report |
| `PG-PLAT-m01` lowest-regret recommendation lacked explicit reassessment rule | MINOR | RESOLVED | ordered hard/decisive/constraining/directional evidence classes plus explicit flip/reopen conditions |

No finding is waived, downgraded by assertion, or treated as resolved by prose alone.

## PG-PLAT-M01 — RESOLVED

### Source defect

The frozen Issue #79 report labeled a June 2026 Steam Hardware & Software Survey snapshot as current evidence observed on 2026-08-12. At remediation review time, Valve's first-party page already exposed July 2026 as the newest month available, with different values.

This invalidated the producer's `current first-party source/date/scope: PASS` claim for that source even though the qualitative Windows-dominance inference remained plausible.

### Correction

The remediation source packet records the newest first-party month visible during the verification session:

- `source_version: July 2026`;
- Windows: `93.67%`;
- Windows 11 64-bit: `70.26%`;
- sample limitation: optional and anonymous Steam participants;
- `latest_month_check.newest_first_party_month_visible: July 2026`;
- `latest_month_check.record_month: July 2026`;
- `latest_month_check.current: true`.

The packet also records the exact drift from Issue #79's June values.

### Fail-closed freshness control

The source-record policy now states:

`CURRENT(month, observed_at) := month == newest_first_party_month_visible_at(observed_at)`

An older monthly snapshot is `STALE`; it may remain historical provenance but cannot satisfy a current-source acceptance claim when a newer first-party month is already available.

### Recommendation reassessment

The corrected report explicitly re-ran the platform-envelope recommendation under July data. The result remains `PLAT-PC-FIRST-R1`, but not because the numeric drift was ignored:

- Steam survey data is now classified as **directional**;
- it cannot override supported-baseline status, evidence coverage per irreversible commitment, partner-gated unknowns, measured platform/engine cost, or accessibility constraints;
- July still supports Windows as a sensible PC evidence baseline, but no monthly percentage is allowed to choose the final storefront/platform release set by itself.

Thus the recommendation is preserved through an explicit decision rule rather than copied from the stale producer output.

## PG-PLAT-M02 — RESOLVED

### Source defect

The frozen Issue #79 evidence register generally stored live URLs plus an observation date. Several authoritative pages are mutable/versionless, and the Steam survey demonstrated the failure mode directly: the same URL can later expose a different month/value set. The repository therefore lacked an immutable reconstruction of the external fact state consumed by the frozen candidate.

### Correction

Created `docs/planning/wave-2/research/target-platform-source-records.yaml`, immutable at blob:

`f2a9333436c9cbc4fe91ec71507997f46f2247e4`

Every external fact consumed by the corrected report is mapped to a source record containing:

- source ID;
- first-party authority;
- authoritative URL;
- source title;
- exact observation time;
- explicit source version/month/last-updated value where available;
- mutable/versionless classification;
- normalized facts actually consumed by the project;
- verification status;
- freshness/reopen rule;
- drift from the frozen Issue #79 source where applicable.

The corrected report binds this packet by exact blob SHA. Later live-page changes therefore cannot retroactively mutate what this candidate claims to have consumed.

### Bounded-copy discipline

The citation packet stores only normalized facts needed by the planning decision plus source identity/freshness metadata. It does not vendor full third-party pages or treat the project record as replacement authority for the source itself. A freshness trigger requires re-observation when the external source matters again.

### Coverage check

The corrected report consumes records for:

- Valve platform workflow;
- Valve Deck/SteamOS compatibility;
- Valve monthly survey;
- Valve language support classes;
- Microsoft Windows 10 lifecycle;
- Microsoft Windows 11 lifecycle;
- Microsoft XAG v3.2;
- Microsoft XAG 107 input;
- Microsoft Store/GDK PC publishing;
- Apple Game Porting Toolkit 4;
- Apple notarization;
- Apple Game Controller framework;
- Nintendo developer process;
- Sony/PlayStation partner-entry roadmap.

No external fact is intentionally consumed outside the immutable packet.

## PG-PLAT-m01 — RESOLVED

### Source defect

Issue #79 compared alternatives and called the recommended envelope "lowest-regret," but did not provide an explicit reassessment rule identifying which facts were decisive, constraining, or merely directional. Therefore a reviewer could not determine mechanically whether correcting stale survey data should change the recommendation.

### Correction

The corrected report defines a decision order:

1. **hard constraints:** authority/freshness, no invented gated rules, no false release promise, sufficient downstream evidence coverage;
2. **primary decisive dimensions:** reversibility/exit cost, evidence coverage per commitment, supported baseline, unknown containment;
3. **constraining evidence:** measured engine cost/infeasibility, accessibility conflicts, promoted partner/product requirements, measured port/package/support cost;
4. **directional evidence:** monthly survey percentages, storefront reach indicators, tool availability without measured project evidence, brochure platform-support claims.

The report also names explicit flip/reopen conditions, including supported-baseline change, loss of Deck evidence value, disproportionate engine cost, accessibility conflict, strong measured tri-platform evidence, partner/product promotion, simultaneous-platform product evidence, or stale/materially changed load-bearing sources.

Normal month-to-month Steam survey movement is explicitly insufficient by itself to flip the recommendation.

## Current source re-verification outcome

During remediation, all load-bearing external claims retained by the corrected report were rechecked against current first-party sources. One material source drift required correction: the Steam survey month and values. Other observed updates did not invalidate the facts actually consumed:

- Valve's Deck compatibility criteria still support the controller/glyph/text-entry/default-performance/Proton evidence used here;
- Windows 10 Home/Pro lifecycle and Windows 11 current-family support remain compatible with the report's bounded baseline claim;
- XAG v3.2 remains the admitted best-practice version and is not promoted to legal/certification authority;
- Microsoft Store PC publishing remains separable from managed Xbox-console enrollment;
- Apple GPTK 4/notarization/controller tooling continues to support conditional macOS evidence gathering without proving port readiness;
- Nintendo and PlayStation detailed platform requirements remain appropriately bounded behind developer/partner access.

## Remediation self-review

Against Issue #92 acceptance criteria and only the declared remediation scope:

- unresolved BLOCKER: 0;
- unresolved MAJOR: 0;
- correction-requiring MINOR: 0;
- `PG-PLAT-M01`: resolved with current month, exact values, drift record, fail-closed rule, and reassessment;
- `PG-PLAT-M02`: resolved with exact immutable project citation packet and report binding;
- `PG-PLAT-m01`: resolved with explicit evidence classes and flip/reopen rule;
- source facts versus project inference: separated;
- partner-gated unknowns: retained;
- alternatives and reversibility: retained;
- engine/accessibility/input/display/packaging/localization interfaces: retained;
- release/engine/readiness/canonicalization authority leakage: none identified;
- required independent review: still `W2-REV-01`.

## Authority limits and next gate

This remediation provides a cleaner substantive `W2-PLAT-01` input for eventual aggregate review. It does not independently validate the platform strategy, engine fit, accessibility applicability, commercial prioritization, partner requirements, or production readiness.

`W2-REV-01` remains the required formal independent adversarial review after its complete Wave-2 prerequisite set becomes eligible. No implementation-readiness blocker is closed here, and no canonicalization is claimed.
