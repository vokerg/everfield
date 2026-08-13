# W2-REM-PLAT-01 — Corrected target-platform and product-scope evidence

**Source mission:** `W2-PLAT-01` / Issue #79  
**Remediation mission:** `W2-REM-PLAT-01` / Issue #92  
**Source frozen head/work:** `695d3cd1bc5a017e780db8016ffefa2379d4103d`  
**Source report blob:** `f47ad96baea765580ad9d016d527c932ce3b2768`  
**Source handoff blob:** `479a0b6dfeeec838b60593819ff355c2fb66ec2e`  
**Pre-gate review:** Issue #79 comment `5270240728`  
**Remediation base main:** `c7ba185ed9667b717794c19eaa0834ca41aa4c78`  
**Authoritative foundation:** `docs/planning/WAVE-1-FOUNDATIONS-v1.md` blob `a252e3c93702f3ebaecd3e888944a23dbe1b0e1d`  
**Immutable external-fact packet:** `docs/planning/wave-2/research/target-platform-source-records.yaml` blob `f2a9333436c9cbc4fe91ec71507997f46f2247e4`  
**External verification session:** `2026-08-12T19:37:30+02:00`  
**Task class / decision state:** `PLANNING_REVISION / EVIDENCE_REQUIRED`  
**Required independent review:** `W2-REV-01`

## 1. Scope and authority

This remediation keeps the useful scope of W2-PLAT-01 and corrects three review findings:

1. refresh the stale monthly Steam survey input;
2. bind every consumed external fact to an immutable project citation record;
3. make the platform-envelope reassessment rule explicit enough to determine whether source drift should change the recommendation.

The output remains a planning/research candidate. It does **not**:

- make a release-platform or storefront promise;
- select an engine, renderer, account/backend, monetization model, or online-service stack;
- set final PC minimum/recommended hardware;
- claim partner-gated console certification requirements are known;
- close `IR-BLOCKER-PLATFORM-SCOPE` for production implementation;
- close `IR-BLOCKER-ACCESSIBILITY-CURRENT`;
- authorize gameplay/high-throughput implementation;
- replace the independent `W2-REV-01` gate.

## 2. Evidence identity and freshness contract

External facts used below are admitted only through source-record blob `f2a9333436c9cbc4fe91ec71507997f46f2247e4`. The record contains, per source, authority, URL, observation time, explicit version/month/last-updated data where available, normalized facts consumed by this report, mutable/versionless status, freshness/reopen rule, and source drift from the frozen Issue #79 candidate.

This creates an immutable **project citation record** without copying unnecessary third-party page content. A later change at a live URL does not rewrite what this candidate consumed; it creates a freshness/reopen question instead.

### 2.1 Monthly-current rule

For a monthly first-party source:

`CURRENT(month, observed_at) := month == newest_first_party_month_visible_at(observed_at)`

If a newer first-party month is visible, the older monthly record is `STALE` and cannot support a producer claim that the source packet is current. Stale data may remain historical provenance but is not silently treated as current evidence.

### 2.2 Corrected survey input

The frozen Issue #79 producer used **June 2026** Steam survey values (`94.10%` Windows; `70.44%` Windows 11 64-bit) while claiming observation on 2026-08-12. The remediation verification found **July 2026** was already the newest first-party month available at the same calendar date.

The admitted current record is therefore:

- month: **July 2026**;
- Windows: **93.67%** of participating systems;
- Windows 11 64-bit: **70.26%** of participating systems;
- participation: optional and anonymous;
- authority class: **directional Steam-user evidence only**, not total-market truth or product-demand research.

The quantitative drift does not by itself change the recommended sequence because market-share survey data is not a decisive input under §5.

## 3. Canonical constraints carried forward

The Wave-1 foundation continues to require:

1. `IR-BLOCKER-PLATFORM-SCOPE` remains OPEN until target platform/product scope is sufficiently bounded through the declared authority chain.
2. `IR-BLOCKER-ACCESSIBILITY-CURRENT` remains OPEN until current applicable accessibility/platform obligations are mapped and independently verified.
3. Engine/runtime-specific choices remain `EVIDENCE_REQUIRED`; this mission cannot select an engine.
4. Freshness-sensitive external evidence must preserve source scope/version/date and invalidation triggers.
5. Persistent gameplay meaning remains engine/platform independent; platform services are adapters unless later reviewed authority changes that boundary.
6. Planning evidence can narrow a candidate set but cannot self-authorize implementation readiness.

## 4. Reverified external evidence register

This table is a readable index into source-record blob `f2a9333436c9cbc4fe91ec71507997f46f2247e4`; the blob is the immutable evidence packet.

| ID | Source version/status | Facts consumed here | Freshness posture |
|---|---|---|---|
| `PLAT-SRC-STEAM-OS` | live Steamworks page, observed 2026-08-12 | Steam workflows support Windows/macOS/Linux-SteamOS and platform-specific depots/build testing | historical OS minima on that page are explicitly not used |
| `PLAT-SRC-STEAM-DECK` | live compatibility checklist, observed 2026-08-12 | controller-complete content access, active glyphs, controller text entry, 30 fps at 800p default Deck target, no device-warning failure, Proton path | recheck on Valve criteria/hardware change and before engine/readiness gates |
| `PLAT-SRC-STEAM-SURVEY` | **July 2026; latest month verified** | Windows 93.67%; Win11 64-bit 70.26%; optional anonymous sample | directional only; monthly-current rule applies |
| `PLAT-SRC-STEAM-LANG` | live language documentation | full-platform vs game-support-only language classes; game support appears in store metadata | does not determine Everfield shipping languages |
| `PLAT-SRC-WIN10` | Microsoft lifecycle | Win10 Home/Pro support ended 2025-10-14; 22H2 final | LTSC separate; legacy target requires explicit promotion |
| `PLAT-SRC-WIN11` | Microsoft lifecycle, observed 2026-08-12 | Win11 Home/Pro family in support; version lifecycles are version-specific | recheck active versions before freezing test/minimum-OS matrix |
| `PLAT-SRC-XAG` | XAG v3.2; page last updated 2026-03-04 | best-practice accessibility guidance across relevant UX surfaces; not a legal-compliance checklist | W2-ACC-01 owns current applicability mapping |
| `PLAT-SRC-XAG-INPUT` | live XAG 107 | goal is operation through input mechanisms of the player's choice; alternative input paths are a design concern | recheck with XAG changes |
| `PLAT-SRC-MSSTORE` | page last updated 2026-06-19 | self-service Win32 PC GDK/MSIXVC path; Xbox console path is separately managed; Xbox services optional for PC-only path | recheck if Store/GDK becomes promoted target |
| `PLAT-SRC-APPLE-PORT` | Game Porting Toolkit 4 | Apple-silicon Windows-executable evaluation, Metal 4, shader/profiling/debugging/remote tooling | tooling does not prove acceptable port cost/performance |
| `PLAT-SRC-APPLE-NOTARY` | live notarization documentation | Developer ID distribution uses notarization; Mac App Store path differs; automation supports notarytool/API | recheck before macOS packaging commitment |
| `PLAT-SRC-APPLE-INPUT` | live Game Controller framework docs | physical/virtual controllers plus common controller/mouse/keyboard device coverage | API presence does not prove engine abstraction quality |
| `PLAT-SRC-NINTENDO` | live developer-process page | registration + NDA/terms precede SDK details; Switch access requires separate application; release includes Nintendo review | detailed certification remains partner-gated/UNKNOWN |
| `PLAT-SRC-PLAYSTATION` | published 2026-04-07 | public path begins with PlayStation Partner registration; deeper publishing/development material is partner-scoped | detailed certification remains partner-gated/UNKNOWN |

### 4.1 Source drift outcome

Material drift found: only `PLAT-SRC-STEAM-SURVEY` required a correction that changes a consumed numeric value/version.

Non-material drift/clarification:

- Valve's compatibility page now jointly describes Deck and Steam Machine; this candidate consumes only the Deck requirements relevant to its current scope.
- Microsoft's Windows 11 lifecycle page contains newer release rows; the candidate deliberately consumes only the current-family support fact and the requirement for version-specific revalidation.

No current first-party recheck invalidated the core platform workflow, Deck UX, Windows lifecycle, XAG, Apple-porting, Microsoft Store, Nintendo-access, or PlayStation-partner facts used by this candidate.

## 5. Explicit reassessment and decision rule

`PLAT-PC-FIRST-R1` is not selected by a scalar platform score. The sequencing decision is evaluated in the following order.

### 5.1 Hard constraints — must not be violated

1. **Authority/freshness:** required external facts must be current enough for their declared use and bound to immutable project evidence.
2. **No invented gated requirements:** partner-gated console rules remain `UNKNOWN` until authoritative access exists.
3. **No false release commitment:** a research/evidence target cannot be presented as shipping-platform authority.
4. **Required downstream coverage:** the envelope must let W2-ACC-01 and W2-ENG-03 exercise the input, display, portability, packaging, retention/capture, and platform-seam questions they are expected to answer.

Any candidate violating a hard constraint is inadmissible regardless of market-share evidence.

### 5.2 Primary decision dimensions — decisive among admissible candidates

In order of importance:

1. **reversibility / exit cost:** avoid high-cost platform commitments before engine, accessibility, and product evidence exists;
2. **evidence coverage per commitment:** prefer a scope that exercises materially different input/form-factor/OS/packaging constraints without turning every exercise into a launch promise;
3. **supported baseline:** use a currently supported consumer OS family for the primary continuous execution target;
4. **unknown containment:** defer partner-gated or product-undefined surfaces while preserving adapter seams and explicit reopen routes.

### 5.3 Constraining evidence — can reject or reopen a candidate

- comparative engine evidence showing required targets are infeasible or impose disproportionate irreversible cost;
- accessibility evidence showing the input/display envelope is insufficient;
- partner access or product requirements that turn a deferred platform into a mandatory constraint;
- measured port/package/support cost that materially changes reversibility.

### 5.4 Directional evidence — may inform but cannot decide alone

- Steam Hardware & Software Survey platform percentages;
- storefront reach indicators;
- availability of porting tools without measured project performance/cost;
- brochure-level engine/platform support claims.

The July survey therefore supports Windows as a sensible PC evidence baseline but cannot alone choose the storefront, final platform set, or release strategy.

### 5.5 Explicit flip/reopen conditions

Reopen or replace `PLAT-PC-FIRST-R1` if any of the following occurs:

- Windows ceases to be a credible supported primary consumer-PC baseline for the target audience/product evidence;
- required Deck/SteamOS evidence no longer provides useful portability/controller/form-factor coverage or becomes materially incompatible with the product;
- W2-ENG-03 shows the Deck requirement eliminates otherwise viable engines at disproportionate cost without corresponding product/evidence value;
- W2-ACC-01 shows the selected input/display envelope cannot meet applicable requirements;
- measured macOS/native-Linux evidence makes a tri-platform baseline lower-regret than the current conditional approach;
- partner access plus product/commercial intent promotes a console before readiness;
- product evidence supports a simultaneous-platform strategy strongly enough to justify its lower reversibility;
- a load-bearing external source becomes stale or materially changes.

A normal month-to-month change in Steam survey percentages does **not** flip the recommendation unless accompanied by material product/audience evidence or a larger change that affects the primary decision dimensions.

## 6. Candidate platform envelopes reassessed

### Alternative A — Windows-only narrow scope

**Definition:** supported Windows 11 desktop only; no required handheld/controller compatibility evidence target.

**Advantage:** smallest immediate matrix.

**Failure:** under-exercises controller-complete UI, small-display behavior, non-Windows portability, Proton behavior, and engine exit cost. It reduces evidence coverage too far under §5.2.

**Disposition:** `NOT_RECOMMENDED`.

### Alternative B — PC-first reversible envelope

**Definition:** supported Windows desktop is the primary continuous evidence target; Steam Deck/SteamOS via the normal Windows build is a required portability/UX evidence target; macOS Apple silicon, native Linux desktop, and additional PC storefronts remain conditional; consoles/mobile remain deferred until explicit promotion.

**Advantages:** high evidence coverage per irreversible commitment; exercises controller/form-factor/non-Windows constraints; keeps partner-gated unknowns explicit; preserves later platform choices.

**Costs:** controller parity, Deck/Proton test coverage, responsive UI, representative performance evidence, and bounded macOS portability analysis.

**Disposition:** `RECOMMENDED_PLANNING_CANDIDATE` after refreshed evidence review.

### Alternative C — desktop tri-platform launch assumption

**Definition:** Windows + native Linux + native macOS become hard production/launch requirements now.

**Advantage:** strongest native desktop portability pressure.

**Failure:** creates three production packaging/support commitments before comparative cost and engine evidence; lower reversibility with no current evidence that the additional commitment is necessary.

**Disposition:** `DEFERRED_PENDING_ENGINE_PRODUCT_AND_COST_EVIDENCE`.

### Alternative D — simultaneous PC + console launch assumption

**Definition:** PC plus one or more Xbox/PlayStation/Nintendo targets become hard release requirements now.

**Advantage:** would expose certification/platform constraints early after access.

**Failure:** detailed requirements are partly gated; access/commercial/hardware/engine evidence is absent; highest irreversible commitment among the candidates.

**Disposition:** `DEFERRED`.

## 7. Recommendation — `PLAT-PC-FIRST-R1`

The refreshed evidence **does not change** the producer's bounded recommendation. It changes the evidence provenance and makes the decision rule explicit.

| Scope | Planning state | Required meaning now | Not implied |
|---|---|---|---|
| Windows desktop | `PRIMARY_EVIDENCE_TARGET` | continuously exercise a supported Windows 11 64-bit desktop build; freeze exact supported version later | final minimum OS/hardware; release commitment |
| Steam / standard PC distribution | `REFERENCE_DISTRIBUTION_SURFACE` | use Steam-compatible packaging/depot assumptions as first concrete storefront evidence surface; keep canonical state storefront-independent | Steam exclusivity or launch commitment |
| Steam Deck / SteamOS via Proton | `REQUIRED_COMPATIBILITY_EVIDENCE_TARGET` | controller-only core flow, active glyphs, controller text input, small-display/readability, representative default performance, Windows-build Proton execution | guaranteed Verified rating; native Linux release |
| Native Linux desktop | `CONDITIONAL_PORT_CANDIDATE` | engine evidence must disclose tooling/CI/package cost; promote only on material benefit | launch support |
| macOS Apple silicon | `CONDITIONAL_PORT_CANDIDATE` | assess build/sign/notarize, input abstraction, rendering portability, representative performance, evidence capture | Intel Mac or launch parity |
| Microsoft Store PC | `OPTIONAL_DISTRIBUTION_CANDIDATE` | preserve a standard Win32/GDK-evaluable packaging seam | Xbox services/console or Store launch commitment |
| Xbox console | `DEFERRED_PARTNER_GATED` | preserve adapters; acquire exact rules only after managed-program access and scope promotion | certification compliance |
| PlayStation | `DEFERRED_PARTNER_GATED` | preserve adapters; acquire exact rules after partner approval/scope promotion | certification compliance |
| Nintendo platforms | `DEFERRED_PARTNER_GATED` | preserve adapters; acquire exact rules after Nintendo access/scope promotion | certification compliance |
| iOS/iPadOS/Android | `DEFERRED_PRODUCT_SCOPE` | no touch/mobile/thermal/store obligation introduced here | mobile launch |

## 8. Product-scope constraints attached to the candidate

### 8.1 Input

For the Windows + Deck evidence envelope:

- core gameplay/navigation must have keyboard/mouse and controller routes;
- commands use semantic actions rather than platform button IDs;
- active input glyphs are data-driven/switchable;
- required text entry has a controller-usable route;
- focus/navigation, remapping, hold/toggle timing, device switching, and alternative input concerns are evidence surfaces for W2-ACC-01;
- touch/motion/adaptive or specialist peripherals remain optional unless promoted.

### 8.2 Display and performance

- UI/layout must be resolution- and scale-aware;
- Deck-class 800p/default-performance behavior is a required compatibility evidence case while the current Valve criterion applies;
- final PC hardware floor remains `EVIDENCE_REQUIRED`;
- performance evidence retains exact device/build/settings/scenario identity and is separated from correctness;
- HDR, high-refresh, ultrawide, 4K, upscaling, and platform-specific premium features remain optional candidates.

### 8.3 Save/state and platform services

- canonical save/state identity and migration semantics remain independent of Steam/Microsoft/Apple/console-native object types;
- cloud save, achievements, presence, entitlement, commerce, social graph, multiplayer, cross-play, and accounts are not made mandatory by this mission;
- if later product design requires a service-dependent feature, its platform matrix/offline/privacy/migration/test obligations must be added before readiness.

### 8.4 Localization

Architecture/evidence requirements remain broader than translation commitments:

- player-visible strings externalized; localized text never used as durable IDs;
- Unicode and variable-length layout support;
- pseudo-localization and representative expansion/CJK/RTL stress before layout-robustness claims;
- text embedded in assets identified for localization/evidence handling;
- shipping languages and QA budget remain future product decisions.

### 8.5 Accessibility

W2-ACC-01 must map current applicable obligations against this exact platform/input scope. Until then:

- XAG v3.2 is admitted as best-practice research guidance, not legal/certification authority;
- input flexibility, focus, text legibility/scaling, media alternatives, timing/pause, motion, audio alternatives, contrast, assist/difficulty, and destructive-action recovery remain architecture/test concerns;
- mandatory platform-specific rules remain `UNKNOWN` until scope/access makes them authoritative.

## 9. Engine-fit implications for W2-ENG-03

Equivalent engine spikes should gather evidence for:

1. supported Windows 11 build generation and unattended packaging;
2. keyboard/mouse + controller semantic input and live glyph switching;
3. Deck-class resolution/UI-scale behavior;
4. Windows-build execution/debugging on SteamOS/Proton or equivalent hardware workflow;
5. save/config portability without platform API leakage into canonical state;
6. Unicode/expansion/CJK/RTL/font/fallback/asset-text behavior;
7. headless/noninteractive test surfaces where available;
8. profiling/capture/replay artifacts retainable in the evidence chain;
9. macOS Apple-silicon build/sign/notarization feasibility plus representative rendering/input evidence as conditional spike;
10. native Linux, Microsoft Store, and console adapter costs as conditional/deferred evidence rather than automatic hard failures when their targets are not promoted.

Brochure claims cannot substitute for these measurements.

## 10. Packaging and CI evidence matrix

| Surface | Wave-2 requirement | Result posture |
|---|---|---|
| Windows 11 build/package/install/launch | required | PASS / FAIL / INCONCLUSIVE / NOT_RUN |
| keyboard+mouse core flow | required | same |
| controller-only core flow | required | same |
| representative Windows build on Deck/SteamOS | required for promoted comparative engine spike | same |
| Deck UI/glyph/text-entry/default-performance | required for promoted comparative engine spike | per-check evidence |
| macOS Apple-silicon build/sign/notarize smoke | conditional when candidate/tooling/access makes it applicable | explicit applicability + result |
| native Linux package | conditional | explicit applicability + result |
| Microsoft Store package | conditional | explicit applicability + result |
| console package/certification | not applicable until partner-gated promotion | `NOT_APPLICABLE` with scope reason, never fabricated PASS |

Lack of hardware/time cannot convert a required `NOT_RUN` into `NOT_APPLICABLE`.

## 11. Observability and evaluation

Downstream evidence must keep reconstructable:

- exact OS/toolchain/engine/build/package identity;
- core-flow completion by input class;
- glyph/device-switching behavior;
- resolution/UI-scale/text failures;
- performance device/settings/scenario;
- save/state portability/migration;
- localization stress failures;
- signing/notarization/package failures;
- manual interventions and reasons;
- gated/unavailable requirements as `UNKNOWN` or explicit applicability states;
- external authority source-record blob and freshness status.

An aggregate score may summarize but cannot erase hard failure, `UNKNOWN`, stale authority, or required `NOT_RUN`.

## 12. Failure modes and controls

| Risk | Failure | Control |
|---|---|---|
| stale-source laundering | old monthly/live value labeled current | immutable source record + monthly-current rule |
| mutable-URL provenance loss | live page changes and frozen claim cannot be reconstructed | exact source-record blob with normalized consumed facts |
| release-promise leakage | research target presented as launch support | explicit planning states/authority limits |
| survey Goodharting | Steam percentages decide platform strategy | survey classed directional; §5 decision order |
| Windows lock-in | platform APIs leak into canonical state/input/UI | adapters + Deck/non-Windows evidence |
| controller checkbox theater | menus/text entry still require mouse | controller-only core-flow and current Deck criteria |
| hidden console unknowns | gated rules guessed from memory | `UNKNOWN` until official access |
| macOS optimism | export capability treated as distribution readiness | measured build/performance/sign/notarize evidence |
| localization retrofit | strings/layout/assets become late blockers | architecture-level i18n now; languages later |
| accessibility retrofit | accessibility deferred until content freeze | W2-ACC-01 consumes this scope before readiness |
| optional-target inflation | every candidate becomes mandatory | explicit required/conditional/deferred states |

## 13. Unresolved questions

1. Which PC storefronts, if any, become launch commitments?
2. Does measured evidence justify native Linux beyond SteamOS/Proton compatibility?
3. Is macOS Apple silicon product-relevant enough to become a hard milestone or launch target?
4. Which supported Windows 11 versions and hardware classes become the production floor?
5. Which languages become shipping commitments and what localization/QA budget follows?
6. Does game design require accounts, multiplayer, cloud state, achievements, cross-play, commerce/DLC, or other platform services?
7. Does partner access/commercial intent promote a console before readiness?
8. Do W2-ACC-01 findings require widening/narrowing platform/input scope?
9. Does W2-ENG-03 find a required target costly enough to reopen platform sequencing rather than simply eliminate an engine?

## 14. Freshness and reopen conditions

Revalidate this packet when:

- a monthly source is used again and a newer month exists;
- Valve changes Deck/SteamOS compatibility criteria or hardware materially;
- Microsoft changes the supported Windows consumer-version picture relevant to the test baseline;
- XAG/current applicable accessibility guidance changes;
- Apple changes a macOS port/sign/notarization fact consumed here;
- Nintendo/PlayStation/Xbox access becomes available and a console is promoted;
- W2-ENG-03 or W2-ACC-01 produces evidence conflicting with this envelope;
- product scope introduces touch-first UX, mandatory online/platform services, multiplayer/cross-play, or platform-dependent persistence;
- commercial/product evidence materially supports simultaneous platforms;
- W2-REV-01 finds a BLOCKER/MAJOR against this candidate or source record.

A current-source recheck is mandatory before engine ADR, implementation-readiness PASS, or shipping-platform commitment. No arbitrary maximum-age number is invented where the source's own version/event cadence is the meaningful freshness trigger.

## 15. Recommendation and decision state

**Recommendation:** advance corrected `PLAT-PC-FIRST-R1` to eventual independent `W2-REV-01` critique as the bounded Wave-2 platform/product-scope candidate.

**Reassessment result after source refresh:** `UNCHANGED_RECOMMENDATION_WITH_CORRECTED_EVIDENCE_PROVENANCE`.

**Decision state:** `EVIDENCE_REQUIRED / REVIEW_READY_CANDIDATE` after producer remediation completion; **not** `VERIFIED_DECISION`.

**Production-readiness effect:** sufficient to keep downstream research concrete, but `IR-BLOCKER-PLATFORM-SCOPE` remains OPEN for production authority until the declared review/synthesis/verification chain resolves it together with all applicable blockers.

## 16. Producer remediation acceptance check

- exact immutable provenance to source #79 candidate: PASS;
- stale June monthly input replaced by newest available July 2026 first-party month: PASS;
- July values recorded exactly in immutable project citation packet: PASS;
- monthly-current fail-closed rule explicit: PASS;
- every external fact consumed in this report mapped to immutable source record: PASS;
- facts separated from project inference: PASS;
- explicit decisive/constraining/directional decision rule: PASS;
- explicit flip/reopen conditions: PASS;
- recommendation re-evaluated rather than copied by assertion: PASS;
- alternatives/tradeoffs retained: PASS;
- engine/accessibility/packaging/input/localization interfaces retained: PASS;
- partner-gated unknowns retained: PASS;
- release/engine/readiness/canonicalization authority leakage: none identified;
- required independent critique retained: `W2-REV-01`.
