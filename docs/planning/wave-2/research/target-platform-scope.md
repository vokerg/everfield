# W2-PLAT-01 — Target platform and product-scope evidence

**Mission:** `W2-PLAT-01`  
**Task class / decision state:** `PLANNING_RESEARCH / EVIDENCE_REQUIRED`  
**Output schema:** `proposal_research_v1`  
**Base main:** `c7ba185ed9667b717794c19eaa0834ca41aa4c78`  
**Authoritative foundation:** `docs/planning/WAVE-1-FOUNDATIONS-v1.md` blob `a252e3c93702f3ebaecd3e888944a23dbe1b0e1d`  
**External evidence observed:** 2026-08-12  
**Required independent review:** `W2-REV-01`

## 1. Scope

This mission narrows the target-platform/product envelope enough for downstream engine, accessibility, packaging, input, localization, and evidence work to operate against concrete candidate scopes.

It does **not**:

- make a release-platform promise;
- select an engine, rendering stack, storefront, monetization model, or online-service stack;
- define final minimum/recommended PC hardware;
- assert current console certification rules that are available only behind partner access;
- close `IR-BLOCKER-PLATFORM-SCOPE` for production implementation by producer authorship;
- close `IR-BLOCKER-ACCESSIBILITY-CURRENT`;
- authorize gameplay/high-throughput production implementation.

The output is a planning candidate. Its job is to constrain evidence collection while keeping high-cost platform commitments reversible.

## 2. Canonical constraints carried forward

From the Wave 1 foundation:

1. `IR-BLOCKER-PLATFORM-SCOPE` is OPEN until target platform/product scope is sufficiently bounded for implementation/release requirements.
2. `IR-BLOCKER-ACCESSIBILITY-CURRENT` is OPEN until current authoritative accessibility/platform obligations are mapped and independently verified.
3. Engine/runtime-specific choices remain `EVIDENCE_REQUIRED`; no engine is selected.
4. External platform/accessibility evidence is freshness-sensitive and must record source scope/version/date plus invalidation triggers.
5. Persistent gameplay meaning remains engine-independent logical state; platform APIs are adapters unless a later reviewed contract says otherwise.
6. Planning evidence may narrow a candidate set but cannot self-authorize implementation readiness.

## 3. Current external evidence register

Only first-party platform/store documentation is used for platform facts in this report. Market-share data is used as directional evidence only, not as a release oracle.

| ID | Source / observed scope | Current evidence used | Limitation / freshness note |
|---|---|---|---|
| `PLAT-SRC-STEAM-OS` | Valve, Steamworks “Platforms”, observed 2026-08-12 — https://partner.steamgames.com/doc/store/application/platforms | Steam release workflows support Windows, macOS, and Linux/SteamOS; additional OS support uses separate depots/build testing. macOS Steam releases require 64-bit/notarized apps; Steam’s macOS build and Mac App Store sandbox requirements differ. | The page still contains old minimum-OS language, so its release workflow is authoritative here but its historical minimum-OS examples are **not** used as a 2026 support baseline. Recheck on Valve workflow/platform updates. |
| `PLAT-SRC-STEAM-DECK` | Valve, Steam Deck and Steam Machine Compatibility Review, observed 2026-08-12 — https://partner.steamgames.com/doc/steamhardware/compat | Compatibility review requires controller-accessible content, active-input glyph behavior, controller-usable text entry, no device-compatibility warning, and a playable default; Valve currently gives 30 fps at 800p for Deck as the default-configuration threshold. | Compatibility criteria can change independently of the game. Recheck before engine decision, Milestone Zero, and release-readiness review. |
| `PLAT-SRC-STEAM-SURVEY` | Valve, Steam Hardware & Software Survey, June 2026 snapshot observed 2026-08-12 — https://store.steampowered.com/hwsurvey/ | The June 2026 Steam survey reports Windows at 94.10% of participating Steam systems and Windows 11 64-bit at 70.44% of the combined survey. Participation is optional and anonymous. | Steam-user sample only; not total addressable market and not a product-demand study. Recheck newest available month before a commercial platform commitment. |
| `PLAT-SRC-STEAM-LANG` | Valve, Steamworks supported languages, observed 2026-08-12 — https://partner.steamgames.com/doc/store/localization/languages | Steam exposes a broad platform-language set plus additional game-support-only languages; language support is surfaced in store metadata. | This does not establish Everfield’s translation budget or launch languages. Recheck when localization commitments are proposed. |
| `PLAT-SRC-WIN10` | Microsoft Lifecycle, Windows 10 Home and Pro, observed 2026-08-12 — https://learn.microsoft.com/en-us/lifecycle/products/windows-10-home-and-pro | Windows 10 Home/Pro support ended 2025-10-14; 22H2 was its final version. | LTSC/ESU cases have different lifecycles and are not used as the normal consumer baseline. |
| `PLAT-SRC-WIN11` | Microsoft Lifecycle, Windows 11 Home and Pro, observed 2026-08-12 — https://learn.microsoft.com/en-us/lifecycle/products/windows-11-home-and-pro | Windows 11 Home/Pro remains in support; Microsoft publishes version-specific lifecycle windows. | Recheck active supported versions before freezing test matrices or minimum OS. |
| `PLAT-SRC-XAG` | Microsoft, Xbox Accessibility Guidelines v3.2 and current guideline pages, observed 2026-08-12 — https://learn.microsoft.com/en-us/xbox/accessibility/guidelines | XAGs are current game-accessibility best-practice guidance spanning input, UI, text, audio, timing, motion, difficulty and related concerns. Microsoft explicitly does not present XAGs as a legal-compliance checklist. | Use as an engineering/research baseline only; `W2-ACC-01` must map actual applicable requirements for the selected scope. Recheck version/change history. |
| `PLAT-SRC-XAG-INPUT` | Microsoft, XAG 107 Input, page observed 2026-08-12 — https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/107 | The goal is to let players operate game interfaces through input mechanisms of their choice and avoid unnecessary input-form assumptions. | Best practice, not a platform certification claim. Recheck with XAG version changes. |
| `PLAT-SRC-MSSTORE` | Microsoft, “Publish PC games to the Microsoft Store using GDK”, updated 2026-06-19, observed 2026-08-12 — https://learn.microsoft.com/en-us/windows/apps/publish/whats-new-game-publishing | A self-service Win32/GDK path exists for PC-only Microsoft Store publishing; Xbox-console publishing requires enrollment in the appropriate managed Xbox program. | Storefront packaging is separate from the core Windows runtime target. Recheck GDK/store program changes if this channel is promoted. |
| `PLAT-SRC-APPLE-PORT` | Apple, Game Porting Toolkit 4, observed 2026-08-12 — https://developer.apple.com/games/game-porting-toolkit | Apple provides current Apple-silicon evaluation/porting tooling, Metal 4 evaluation, shader conversion, profiling/debugging, and remote build workflows. | Availability of tools does not prove acceptable port cost/performance. Requires engine/spike evidence. |
| `PLAT-SRC-APPLE-NOTARY` | Apple, notarizing macOS software, observed 2026-08-12 — https://developer.apple.com/documentation/security/notarizing-macos-software-before-distribution | Directly distributed macOS software uses Developer ID signing/notarization; current automation uses `notarytool`/Notary API, with hardened-runtime requirements. | Exact distribution requirements differ for Mac App Store versus direct/Steam distribution. Recheck before packaging commitment. |
| `PLAT-SRC-APPLE-INPUT` | Apple, Game Controller framework, observed 2026-08-12 — https://developer.apple.com/documentation/gamecontroller | Apple’s game-controller framework covers physical/virtual controllers and common controller, mouse, and keyboard devices. | API availability does not prove engine abstraction quality; test in comparative engine work. |
| `PLAT-SRC-NINTENDO` | Nintendo Developer Portal registration/process, observed 2026-08-12 — https://developer.nintendo.com/the-process | Nintendo platform SDK information is obtained after registration/NDA; Switch access requires a separate application; release includes Nintendo review. | Detailed current certification requirements are gated. They cannot be treated as known until access exists and scope is promoted. |
| `PLAT-SRC-PLAYSTATION` | Sony Interactive Entertainment, “Showing your Game to PlayStation”, 2026-04-07, observed 2026-08-12 — https://sonyinteractive.com/en/news/blog/showing-your-game-to-playstation/ | The public indie roadmap begins with PlayStation Partner registration; approved partners gain development/publishing documentation and tools. | Detailed current certification/SDK obligations are partner-gated and remain unknown here. |

## 4. Evidence versus inference

### 4.1 Observed evidence

- Windows 11 is a currently supported consumer Windows family while ordinary Windows 10 Home/Pro support has ended.
- Windows is the dominant OS in Valve’s June 2026 optional Steam survey.
- Steam supports Windows/macOS/Linux release workflows and exposes explicit Deck compatibility criteria.
- Deck compatibility criteria impose useful concrete constraints on controller completeness, text entry, glyphs, default performance, and device-warning behavior.
- Current Microsoft accessibility guidance treats broad input accessibility as a design/test concern rather than a console-only concern.
- macOS distribution and porting introduce distinct signing/notarization/Metal/tooling work.
- PC Microsoft Store publishing can be evaluated independently of Xbox-console enrollment.
- Nintendo, PlayStation, and Xbox console programs have partner/program gates before their complete current release requirements become authoritative to this project.

### 4.2 Inference

The lowest-regret planning scope is therefore **not** “support every platform” and not “Windows only forever.” The evidence supports using a currently supported Windows desktop build as the primary execution baseline while deliberately exercising portability through Steam Deck/SteamOS compatibility and retaining macOS/console seams for later evidence.

This is an inference about sequencing and reversibility, not a market forecast or release decision.

## 5. Candidate platform envelopes

### Alternative A — Windows-only narrow scope

**Definition:** Windows 11 desktop only; keyboard/mouse primary; no required handheld/controller compatibility target.

**Advantages:** smallest immediate matrix and packaging burden.

**Problems:** weak evidence for controller-complete UI, portability, small-screen legibility, Linux/Proton behavior, and engine exit options. It risks making later platform work an expensive retrofit and under-serves the explicit downstream engine/accessibility questions.

**Disposition:** `NOT_RECOMMENDED` as the Wave 2 planning envelope.

### Alternative B — PC-first reversible envelope

**Definition:** supported Windows desktop is the primary build/evidence target; Steam Deck/SteamOS compatibility is a required portability/UX evidence target; macOS Apple silicon is a conditional port candidate; native Linux desktop and additional PC storefront packages remain conditional; consoles/mobile remain deferred until explicit promotion.

**Advantages:** keeps the high-volume PC path concrete, exercises non-Windows/controller constraints early, and avoids pretending partner-gated console requirements are known. It gives `W2-ENG-03` and `W2-ACC-01` a bounded target without creating a multi-platform launch commitment.

**Costs:** requires controller-first parity work, Deck/Proton test coverage, responsive UI/performance evidence, and at least bounded macOS portability analysis.

**Disposition:** `RECOMMENDED_PLANNING_CANDIDATE`.

### Alternative C — desktop tri-platform launch assumption

**Definition:** Windows + native Linux + native macOS are all treated as launch requirements now.

**Advantages:** maximizes desktop-native portability pressure.

**Problems:** forces three production packaging/support stacks before engine/platform cost evidence exists; duplicates some Linux evidence that Deck/Proton can produce earlier; converts a planning question into an implicit release promise.

**Disposition:** `DEFERRED_PENDING_ENGINE_AND_COST_EVIDENCE`.

### Alternative D — simultaneous PC + console launch assumption

**Definition:** PC plus one or more Xbox/PlayStation/Nintendo targets become hard release requirements now.

**Advantages:** would expose certification/input/performance constraints early after partner access.

**Problems:** current detailed requirements are partly partner-gated; partner access, commercial scope, hardware targets, and engine evidence are not yet established. This is high-cost and low-reversibility at the current planning stage.

**Disposition:** `DEFERRED`.

## 6. Recommended planning candidate: `PLAT-PC-FIRST-R1`

`PLAT-PC-FIRST-R1` is a **research and architecture target**, not a release promise.

| Scope dimension | Planning state | Required meaning now | Explicitly not implied |
|---|---|---|---|
| Windows desktop | `PRIMARY_EVIDENCE_TARGET` | Continuously exercise a supported Windows 11 64-bit desktop build. Treat Windows 10 only as optional legacy compatibility evidence unless a later scope decision explicitly supports it. | Final minimum OS/hardware; Microsoft Store exclusivity; production readiness. |
| Steam / standard PC distribution | `REFERENCE_DISTRIBUTION_SURFACE` | Use Steam-compatible packaging/depot assumptions as the first concrete storefront evidence surface because it also exposes Deck/SteamOS workflows. Keep core save/state/content independent of storefront APIs. | Final storefront exclusivity or commercial launch commitment. |
| Steam Deck / SteamOS via Proton | `REQUIRED_COMPATIBILITY_EVIDENCE_TARGET` | Core content usable with controller alone; active input glyphs; controller-capable text entry; readable/responsive small-display UI; representative default performance evidence against current Valve compatibility criteria. Test the normal Windows build through the compatibility layer before requiring native Linux. | Guaranteed Verified rating; native Linux release; fixed production performance budget. |
| Native Linux desktop | `CONDITIONAL_PORT_CANDIDATE` | Engine candidate must disclose support quality/tooling/CI/packaging cost. Promote to a hard target only if evidence shows material benefit over the Windows+Proton path. | Launch support. |
| macOS Apple silicon | `CONDITIONAL_PORT_CANDIDATE` | Comparative engine evidence must assess build/sign/notarize pipeline, controller/input abstraction, rendering portability, representative performance, and automated evidence capture. | Intel Mac support, Mac App Store release, or launch parity. |
| Microsoft Store on Windows | `OPTIONAL_DISTRIBUTION_CANDIDATE` | Preserve runtime/store abstraction so standard Win32 PC build can be evaluated for GDK/MSIXVC packaging later. | Xbox services, Xbox console target, or Store launch commitment. |
| Xbox console | `DEFERRED_PARTNER_GATED` | Preserve platform-service/input/save/entitlement adapter seams; gather exact requirements only after managed-program access and explicit scope promotion. | Certification compliance or launch target. |
| PlayStation | `DEFERRED_PARTNER_GATED` | Preserve portability seams; obtain current SDK/certification requirements only after partner approval and explicit scope promotion. | Certification compliance or launch target. |
| Nintendo platforms | `DEFERRED_PARTNER_GATED` | Preserve portability seams; obtain current SDK/certification requirements only after Nintendo access and explicit scope promotion. | Certification compliance or launch target. |
| iOS/iPadOS/Android | `DEFERRED_PRODUCT_SCOPE` | No touch/mobile UX, thermal, store, or entitlement requirement is imposed by this mission. Reopen if product design or market evidence promotes mobile/tablet. | Mobile launch or touch-first UX. |

## 7. Product-scope constraints attached to the candidate

### 7.1 Input

For the primary Windows + Deck evidence envelope:

- every core gameplay/navigation flow must have a keyboard/mouse route and a controller route;
- gameplay commands are exposed through semantic input actions rather than platform-specific button identifiers;
- active input glyphs are data-driven and switchable;
- text-entry flows have a controller-usable path;
- remapping, focus/navigation behavior, hold/toggle timing, and device switching are evidence surfaces for `W2-ACC-01`, not late polish;
- touch, motion, platform-specific adaptive features, and specialist peripherals are optional extensions unless later scope promotes them.

This requirement intentionally goes beyond “the PC can technically accept a controller.” It creates an engine-neutral testable contract for downstream work.

### 7.2 Display and performance

- UI/layout must be resolution- and scale-aware rather than authored to one fixed desktop resolution.
- Deck-class 800p behavior is a required compatibility evidence case while the current Valve criterion remains applicable.
- Final PC minimum/recommended hardware remains `EVIDENCE_REQUIRED`; no GPU/CPU/RAM floor is invented here.
- Performance evidence must retain exact device/build/settings identity and distinguish correctness from performance acceptance.
- high-refresh, HDR, ultrawide, 4K, and platform-specific upscaling are optional capability candidates until evidence/product scope promotes them.

### 7.3 Save/state and platform services

- canonical save/state identity and migration semantics must not depend on Steam, Microsoft, Apple, or console-native object types;
- cloud save, achievements, presence, entitlement, commerce, social graph, multiplayer/networking, and cross-play are **not** mandatory requirements introduced by this scope;
- if game design later requires any service-dependent feature, its platform matrix, offline behavior, privacy/account implications, migration, and test evidence must be explicitly added before implementation readiness.

This keeps the current scope from silently choosing a backend or account model.

### 7.4 Localization

The **architecture/evidence requirement** is broader than the **translation commitment**:

- externalize player-visible strings and avoid using localized text as durable IDs;
- support Unicode text and variable-length layouts;
- test pseudo-localization plus representative expansion, CJK, and right-to-left stress cases before claiming layout robustness;
- keep text embedded in images/content assets machine-identifiable for localization review;
- separate store-page localization from in-game localization;
- choose actual shipping languages later using product/market/content-cost evidence.

No language other than the project’s working/source language is promised for launch by this mission.

### 7.5 Accessibility

`W2-ACC-01` must use this scope to map current requirements and evidence obligations. Until then:

- Microsoft XAG categories are an admitted best-practice research baseline, not a legal/certification assertion;
- input flexibility, UI focus, text legibility/scaling, subtitle/caption behavior where media exists, timing/pause semantics, motion effects, audio alternatives, color/contrast, difficulty/assist options, and destructive-action recovery are architecture/test concerns;
- platform-specific mandatory rules remain `UNKNOWN` until the platform is promoted and current authoritative requirements are available.

## 8. Engine-fit implications for `W2-ENG-03`

A comparative engine candidate cannot score “platform support” as a brochure checkbox. For `PLAT-PC-FIRST-R1`, equivalent engine spikes should gather evidence for:

1. supported Windows 11 build generation and unattended packaging;
2. controller + keyboard/mouse semantic input abstraction and live glyph switching;
3. small-display/resolution/UI-scale behavior suitable for Deck evidence;
4. running/debugging the Windows build on SteamOS/Proton or equivalent Deck hardware workflow;
5. save/config path portability without platform API leakage into canonical game state;
6. localization pipeline behavior for Unicode, expansion, CJK, RTL, fonts/fallback, and asset text;
7. headless/noninteractive test surfaces where the engine permits them;
8. profiling/capture/replay artifacts that can be retained in the project evidence chain;
9. macOS Apple-silicon build, signing/notarization feasibility and representative rendering/input evidence as a conditional spike;
10. native Linux, GDK/MSIXVC, and console adapter costs as conditional evidence rather than automatic hard failures when the target itself is deferred.

A candidate engine may remain admissible with a weak deferred-platform story if its exit/reopen cost is explicit; it must not hide failure on a **required evidence target**.

## 9. Packaging and CI implications

The current minimum evidence matrix is:

| Evidence surface | Required in Wave 2 engine/platform evidence? | Result classes |
|---|---|---|
| Windows 11 build/package/install/launch | yes | PASS / FAIL / INCONCLUSIVE / NOT_RUN |
| Keyboard+mouse core navigation/play path | yes | PASS / FAIL / INCONCLUSIVE / NOT_RUN |
| Controller-only core navigation/play path | yes | PASS / FAIL / INCONCLUSIVE / NOT_RUN |
| Deck/SteamOS execution of representative Windows build | yes for promoted comparative engine spike | PASS / FAIL / INCONCLUSIVE / NOT_RUN |
| Deck UI/glyph/text-entry/default-performance checks | yes for promoted comparative engine spike | per-check result + evidence |
| macOS Apple-silicon build/sign/notarize smoke | conditional; required only when engine remains in the admitted comparative candidate set and tooling/access is available | PASS / FAIL / INCONCLUSIVE / NOT_RUN with applicability rationale |
| native Linux package | conditional | same |
| Microsoft Store package | conditional | same |
| console package/certification | not applicable until partner-gated scope promotion | `NOT_APPLICABLE` with scope reason, never fabricated PASS |

`NOT_RUN` for a required target cannot be reclassified as `NOT_APPLICABLE` merely because the task lacks hardware or time; that becomes an evidence gap.

## 10. Dependencies and interfaces

### Inputs

- Canonical Wave 1 foundation blob `a252e3c93702f3ebaecd3e888944a23dbe1b0e1d`.
- Current first-party external sources listed in §3.

### Interfaces produced

- `W2-ACC-01`: concrete target scope for current accessibility/platform requirement mapping.
- `W2-ENG-03`: required versus conditional platform scenarios for engine-comparative spikes.
- `W2-REV-01`: exact source/freshness trail and candidate-scope assumptions for adversarial review.
- Later synthesis/readiness work: one bounded platform-scope candidate plus explicit unresolved release commitments.

No other mission is authorized to treat `PLAT-PC-FIRST-R1` as a verified release decision before the required review/synthesis/readiness route.

## 11. Observability and evaluation

Downstream evidence should make these dimensions reconstructable rather than reduce them to one platform score:

- build/package success by exact OS/toolchain/engine version;
- launch and core-flow completion by input class;
- device/input glyph switching correctness;
- resolution/UI-scale/text-overflow failures;
- representative performance by device/settings/scenario;
- save/state portability and migration behavior;
- localization stress-case failures;
- signing/notarization/package failures;
- manual intervention count and reason;
- unavailable/gated requirements recorded as `UNKNOWN`/`NOT_APPLICABLE`, not PASS;
- exact source freshness for every platform rule used as authority.

An aggregate engine/platform score may summarize but may never erase a hard failure or `UNKNOWN` on a required target.

## 12. Failure modes and risks

| Risk | Failure mode | Required control |
|---|---|---|
| release promise leakage | Planning target is presented as announced platform support. | Keep candidate state explicit in issue, artifacts, review and later synthesis. |
| Windows monoculture lock-in | Platform APIs/types leak into canonical state/UI/input. | Adapter boundaries plus required Deck/portability evidence. |
| “supports controller” checkbox theater | Menus/text entry/glyphs still require mouse/keyboard. | Controller-only core-flow evidence and Deck criteria. |
| survey Goodharting | Steam OS percentages become the sole platform decision oracle. | Treat survey as directional; retain product/port cost/accessibility/engine evidence separately. |
| stale platform rules | Old OS/certification guidance remains in requirements. | Freshness triggers and first-party recheck before dependent decisions. |
| hidden console unknowns | Gated rules are guessed from memory/community posts. | Keep console requirements `UNKNOWN` until official access/current evidence. |
| macOS optimism | “Engine exports to Mac” is treated as distribution readiness. | Require Apple-silicon build/performance/sign/notarization evidence. |
| localization retrofit | Strings/layout/assets become unlocalizable before language decision. | Architecture-level internationalization now; shipping language list later. |
| accessibility retrofit | Platform/accessibility work is postponed until content freeze. | `W2-ACC-01` consumes this scope before production readiness. |
| conditional-target inflation | Every optional platform becomes a required matrix row. | Required/conditional/deferred applicability is explicit and compiler-visible. |

## 13. Unresolved questions

1. Which PC storefront(s), if any, become actual launch commitments?
2. Does product evidence justify native Linux in addition to SteamOS/Proton compatibility?
3. Is macOS Apple silicon economically/product-relevant enough to become a launch or Milestone Zero hard target?
4. Which supported Windows 11 versions and hardware classes become the production test floor after engine evidence?
5. Which languages become launch commitments, and what localization/QA budget follows?
6. Does the game design require online accounts, multiplayer, cloud state, achievements, cross-play, commerce/DLC, or other platform services?
7. Will partner access and commercial intent promote any console before implementation readiness?
8. Do accessibility findings require widening or narrowing the platform/input scope?
9. Does an admitted engine fail a required PC/Deck evidence target badly enough to reopen this platform sequencing rather than eliminate the engine?

## 14. Freshness and reopen conditions

Reopen or refresh this evidence when any of the following occurs:

- Valve changes Steam Deck/SteamOS compatibility criteria or the Steam hardware target materially changes;
- a newer Steam survey or other authoritative product research materially changes the platform-priority rationale;
- Microsoft changes supported Windows consumer versions in a way that invalidates the test baseline;
- Microsoft XAG/current target-platform guidance changes materially;
- Apple changes macOS signing/notarization, Metal, supported-device, or game-porting requirements used by the conditional port analysis;
- Nintendo/PlayStation/Xbox partner access becomes available and a console is promoted into the candidate release scope;
- `W2-ENG-03` finds a required target infeasible or disproportionately costly across otherwise-admissible engines;
- `W2-ACC-01` finds applicable requirements that conflict with this input/display/platform envelope;
- product/game-design scope introduces touch-first interaction, mandatory network services, multiplayer/cross-play, platform-dependent persistence, or another platform-affecting requirement;
- later market/product evidence justifies a simultaneous-platform strategy rather than PC-first sequencing;
- `W2-REV-01` returns a BLOCKER/MAJOR against this candidate or its source freshness.

No maximum-age number is invented. Revalidation is event/version-sensitive, with a mandatory current-source recheck before an engine ADR, implementation-readiness PASS, or shipping-platform commitment.

## 15. Recommendation and decision state

**Recommendation:** advance `PLAT-PC-FIRST-R1` to independent `W2-REV-01` critique as the bounded Wave 2 platform/product-scope candidate.

**Decision state:** `EVIDENCE_REQUIRED / REVIEW_READY_CANDIDATE` after producer completion; **not** `VERIFIED_DECISION`.

**Production-readiness effect:** narrows `IR-BLOCKER-PLATFORM-SCOPE` enough for downstream research to execute, but does not resolve the production blocker. Resolution requires the declared review/synthesis/verification authority chain and zero applicable OPEN readiness blockers.

## 16. Producer acceptance check

- bounded scope without false release commitment: PASS;
- current first-party source/date/scope recorded: PASS;
- evidence separated from inference: PASS;
- alternatives separated from recommendation: PASS;
- engine/accessibility/packaging/input/localization implications explicit: PASS;
- open commitments explicit: PASS;
- source freshness/reopen triggers explicit: PASS;
- partner-gated unknowns preserved rather than guessed: PASS;
- production implementation/readiness leakage identified: none found;
- required independent critique retained: `W2-REV-01`.
