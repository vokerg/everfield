# W2-ENG-01 — Current engine candidate discovery and admission matrix

**Mission:** `W2-ENG-01`  
**Issue:** #71  
**Task class / decision state:** `PLANNING_RESEARCH / EVIDENCE_REQUIRED`  
**Task branch:** `planning/issue-71`  
**Activation/base:** `e4b7ee0a2699a57216146e99b990ab64edaae1d1`  
**Schema-3 claim:** comment `5251524014`  
**External-source observation date:** 2026-08-11  
**Decision authority:** admission to later comparative evidence only; **no engine is selected**.

## Review Index

- **Question:** Which bounded engine baselines deserve equivalent W2-ENG-03 spikes under Everfield's unresolved product/platform scope?
- **Hard filters:** current primary-source baseline; credible unattended/CLI or code-first automation path; plausible 2D/3D game-production path; terms can be screened now; no dependency on making engine-native state canonical.
- **Diversity cap:** five admitted baselines to keep comparative spikes tractable while representing distinct hypotheses rather than five near-substitutes.
- **Admitted, unordered:** Bevy 0.19.0; Defold 1.13.0; Godot 4.7.1; Unity 6000.3.21f1 (Unity 6.3 LTS); Unreal Engine 5.8.
- **Explicitly deferred, not rejected:** GameMaker; O3DE 26.05.0; Stride 4.3.
- **Material terms risks:** Unity's current terms constrain AI/agent access to authorized pathways and its source-code terms restrict source-code use with AI agents; Unreal's EULA restricts Generative-AI training/prompt uses of Licensed Technology. These are **OPEN/UNKNOWN fit questions**, not legal conclusions.
- **Primary unknowns:** target release platforms; company revenue/funding and resulting commercial tiers; final 2D/3D demands; console requirements; exact autonomous-editor interaction path; source-code/AI legal fit; equivalent S1-S10 effort/cost.
- **Result:** `ENGINE_CANDIDATE_SET = EVIDENCE_REQUIRED`; all five proceed only to equivalent reviewed spikes if downstream prerequisites remain satisfied.

## 1. Scope and non-goals

This artifact constructs a current, bounded, reconstructable engine **admission set**. Admission means only that an engine represents a sufficiently distinct and credible hypothesis to justify later equivalent evidence generation.

In scope:

- exact current baseline versions for admitted candidates;
- current primary-source evidence for automation, platforms, release/support state, and material license/terms constraints;
- explicit assumptions caused by unresolved product/platform scope;
- inclusion/defer rationale and material unknowns;
- freshness/reopen triggers for W2-ENG-03 and W2-REV-01.

Non-goals:

- selecting or ranking an engine;
- declaring any engine production-ready;
- performing S1-S10 comparative spikes;
- resolving legal questions assigned to W2-RIGHTS-01;
- establishing final platform commitments assigned to W2-PLAT-01;
- making engine/editor asset types canonical gameplay state;
- authorizing production/gameplay implementation.

## 2. Canonical constraints from Wave 1

Observed repository authority:

1. `IR-BLOCKER-ENGINE-DECISION` remains OPEN and cannot resolve from discovery alone.
2. Engine discovery/admission and representative spikes are `EVIDENCE_REQUIRED`; Wave 1 creates no engine-specific `VERIFIED_DECISION`.
3. Persistent gameplay-authoritative meaning remains engine-independent logical state with stable IDs/versioned schemas; rendering/editor/audio/platform types are adapters unless separately reviewed.
4. Cross-runtime state-hash authority remains unverified until hash-conformance evidence exists.
5. Target platform/product scope is still OPEN.
6. W2-ENG-03 cannot start until W2-AUTH-01, W2-ENG-01, W2-ENG-02, W2-HASH-01, and W2-PLAT-01 are all REVIEW_READY.

Therefore this task may admit candidates but cannot convert engine fit into empirical PASS.

## 3. Target assumptions for admission

These assumptions are intentionally weaker than release commitments.

| ID | Admission assumption | Status / consequence |
|---|---|---|
| A1 | Final release platforms are UNKNOWN until W2-PLAT-01. | Do not eliminate an otherwise credible candidate solely because console/mobile details are unresolved; record them as risk. |
| A2 | Both 2D and 3D remain plausible. | Do not optimize the set around a settled art/rendering direction. |
| A3 | Unattended repeatability is mandatory for the AI-native factory. | Candidate needs a credible CLI/headless/code-first path sufficient to attempt equivalent build/test/evidence workflows. |
| A4 | Canonical gameplay state remains engine-independent. | Candidate must tolerate an adapter boundary; engine-native scene/editor state cannot silently become the sole domain authority. |
| A5 | Company revenue/funding, legal entity structure, and commercial distribution economics are UNKNOWN. | Threshold-based commercial terms remain OPEN, never assumed satisfied. |
| A6 | AI agents/autonomous callers are routine development actors. | Current restrictions on agentic/editor/source interaction are material candidate-fit risks and must be exercised/reviewed. |
| A7 | Admission is deliberately bounded to five hypotheses. | Additional plausible engines are deferred unless product scope or evidence invalidates a selected hypothesis. |

## 4. Admission method

### 4.1 Required gates

A candidate is admitted only when all are true from current primary sources:

1. a current stable/LTS/release baseline can be pinned;
2. an unattended CLI/headless or code-first automation path is documented or inherent in the supported workflow;
3. it plausibly supports game development under currently unresolved 2D/3D scope;
4. material current license/terms facts can be surfaced rather than guessed;
5. it contributes a differentiated hypothesis to the bounded set.

A gate may be satisfied for **admission** while important behavior remains UNKNOWN for **selection**. W2-ENG-03 exists to measure those unknowns.

### 4.2 No scalar score

No aggregate score is used. The set is chosen by hard gates plus hypothesis diversity. W2-ENG-03 must compare equivalent scenario evidence and retain failures, retries, interventions, costs, and exit risks.

## 5. Admitted candidate matrix — unordered

### 5.1 Bevy `0.19.0` — ADMIT_FOR_SPIKE

**Exact baseline:** Bevy 0.19.0, announced 2026-06-19.

**Distinct hypothesis:** code-first Rust/ECS engine with minimal editor coupling may fit autonomous generation, deterministic logical-core separation, and repository-native review better than editor-centric engines.

**Current primary-source evidence:**

- Bevy 0.19 is the current documented release line and the official quick start pins `bevy = "0.19"` / tag `v0.19.0`.
- Official Bevy materials describe Windows, macOS, Linux, Web, iOS, and Android support.
- Standard Rust/Cargo workflows and official CI guidance provide a scriptable build/test surface.
- The official repository is dual-licensed MIT or Apache-2.0.
- The official repository also explicitly warns that Bevy is still early-stage, important features are missing, documentation is sparse, and breaking releases occur roughly every three months.

**Terms screen:** permissive open-source licenses; no engine-specific commercial royalty identified in the reviewed primary sources. This is not a W2-RIGHTS legal clearance.

**Material UNKNOWN / risks:**

- console support and target-platform fit;
- editor/content-authoring workflow fit for eventual game scope;
- migration burden across breaking releases;
- high-fidelity rendering/tooling gaps relevant to Everfield's eventual content;
- representative build, package, capture, and recovery cost.

**Why admit:** uniquely tests whether a code-first engine materially improves autonomous development enough to compensate for maturity/migration risk.

### 5.2 Defold `1.13.0` — ADMIT_FOR_SPIKE

**Exact baseline:** Defold 1.13.0 stable release line.

**Distinct hypothesis:** compact Lua/native-extension engine with integrated, scriptable build/bundle tooling may minimize autonomous setup and CI friction while retaining desktop/mobile/web/console reach.

**Current primary-source evidence:**

- Defold's official release-notes channel records 1.13.0 as released, with 1.13.1 still beta at the observation date.
- `Bob` is an official command-line builder capable of resolving, building, archiving, and bundling projects outside the editor, with documented platform targets.
- Defold describes itself as a cross-platform engine for 2D and lightweight 3D across desktop, mobile, web, and consoles.
- The Defold License permits commercial games, engine modification, and distribution subject to its custom license; the Foundation states no subscription, royalty, or main-product license fees.

**Terms screen:** custom source-available Defold License, not OSI-style Apache despite being derived from Apache 2.0. The license restricts commercialization of the engine/editor itself and requires notices. No AI-specific clearance is inferred.

**Material UNKNOWN / risks:**

- fit if final game requires heavyweight 3D/rendering/editor workflows;
- exact console availability/SDK access for selected target platforms;
- native-extension burden for missing capabilities;
- autonomous editor mutation quality versus Bob-only build automation;
- representative package/profile/recovery costs.

**Why admit:** provides the lean integrated-toolchain hypothesis that is not represented by the larger general-purpose engines.

### 5.3 Godot `4.7.1-stable` — ADMIT_FOR_SPIKE

**Exact baseline:** Godot 4.7.1-stable, released 2026-07-14, build commit `a13da4feb`.

**Distinct hypothesis:** permissive open-source editor engine with first-class headless/CLI operation may combine broad authoring features with low agent/tooling restrictions and inspectable source.

**Current primary-source evidence:**

- Godot's official archive marks 4.7.1 as stable while 4.8 is still a development series.
- Official 4.7 docs state any Godot binary can run with `--headless` and document command-line automation for export/deploy/CI.
- Current 4.7 docs list editor/export support on Windows, macOS, Linux, experimental Android editor support, and web capability; console details are intentionally left to separate channels.
- Godot is MIT-licensed; commercial games may use a different license while retaining required Godot/third-party notices.

**Terms screen:** MIT engine license plus third-party notices. No commercial royalty from Godot itself is identified. This is not a complete rights review.

**Material UNKNOWN / risks:**

- selected console platform route and third-party port/provider dependencies;
- C# versus GDScript automation tradeoffs;
- large-project editor/import performance and merge behavior;
- equivalent high-fidelity rendering/profile/package performance;
- source-customization maintenance cost if required.

**Why admit:** tests an open-source, editor-capable middle ground with explicit headless automation.

### 5.4 Unity `6000.3.21f1` / Unity 6.3 LTS — ADMIT_FOR_SPIKE_WITH_TERMS_RISK

**Exact baseline:** Unity 6000.3.21f1, released 2026-07-29 on the Unity 6.3 LTS line. Unity states 6.3 LTS support through December 2027.

**Distinct hypothesis:** mature cross-platform commercial engine with a broad tooling/platform ecosystem and batch/build automation may reduce implementation risk, but current agentic-access terms may create a direct constraint for Everfield's AI-native factory.

**Current primary-source evidence:**

- Unity 6000.3.21f1 is an official Unity 6.3 LTS patch.
- Unity documents command-line builds with `-executeMethod`, `-buildTarget`, `-batchmode`, `-quit`, and project/log arguments; batch/no-graphics modes support unattended automation.
- Unity advertises 20+ end-user platforms in the Unity 6 family.
- Current plan pages show Personal free under the applicable $200k revenue/funding threshold, Pro required above $200k, and Enterprise required above $25M; current 2026 Pro list pricing is published separately.
- Unity's Terms of Service updated 2026-06-30 state that AI agents, autonomous/semi-autonomous systems, LLMs, CLI/MCP clients or servers interacting with Unity Offerings must use `Authorized Agentic Access`.
- Unity's Editor Source Code Terms updated 2026-06-30 explicitly restrict inputting Unity Source Code into coding assistants or AI agents.

**Terms screen:** **MATERIAL OPEN RISK.** The project must not infer that ordinary local automation, third-party MCP, source-code debugging, or agent-driven editor control is permitted merely because a technical API exists. W2-RIGHTS-01 must classify the exact intended workflow and W2-ENG-03 must use only an authorized path.

**Material UNKNOWN / risks:**

- Everfield's eventual financial tier and seat requirements;
- what exact Unity agentic framework is authorized for the S1-S10 harness;
- whether that authorized path allows the required autonomous scene/content/editor operations;
- whether source-code restrictions materially block AI-assisted debugging/customization;
- closed-platform requirements and target-platform-specific terms;
- package/service terms beyond the core editor.

**Why admit:** the terms risk is itself decision-critical evidence. Excluding Unity without measuring the authorized path would hide a major mainstream comparison; admitting it does not waive the terms.

### 5.5 Unreal Engine `5.8` — ADMIT_FOR_SPIKE_WITH_TERMS_RISK

**Exact baseline:** Unreal Engine 5.8, announced available at State of Unreal 2026 and described by Epic as the last planned major UE5 release (with a 5.9 still possible if needed).

**Distinct hypothesis:** high-end source-available commercial engine may provide the strongest heavyweight rendering/world/tooling ceiling, at the cost of build/automation complexity and material license/AI-use constraints.

**Current primary-source evidence:**

- Epic documents UE 5.8 as the current available major release.
- UE 5.8 documentation provides extensive command-line arguments; `-unattended` disables interactive popups/input and commandlets provide command-line applet workflows.
- Epic's current licensing page says game developers can use Unreal without seat fees under the standard game-development model, with 5% royalty on attributable lifetime gross product revenue above the first $1M under the standard rate (subject to the EULA and exclusions/programs).
- The current Unreal EULA permits private source-code use/modification within its license but restricts use of Licensed Technology as training input to Generative AI and as prompt input where the Generative-AI program trains on input data.

**Terms screen:** **MATERIAL OPEN RISK.** This artifact does not interpret whether a specific coding assistant or agent workflow falls inside/outside the Generative-AI restriction. Exact prompts/data handling and source access require W2-RIGHTS-01 review.

**Material UNKNOWN / risks:**

- exact AI-agent/source-code workflow permissibility;
- build/import/cook/package time and CI resource footprint;
- repository size/binary-asset/merge/recovery burden;
- target console/platform SDK implications;
- whether heavyweight capabilities are unnecessary overhead for final game scope;
- exit cost if engine-specific content/tooling becomes entrenched before checkpoint.

**Why admit:** it represents the heavyweight/high-ceiling hypothesis and has materially different technical and commercial constraints from the other four.

## 6. Explicitly deferred plausible engines

Deferral means **not in this bounded comparative set**, not “bad engine” or permanent rejection.

### GameMaker — DEFER_NOT_ADMITTED

Primary-source snapshot: GameMaker currently positions itself specifically as a 2D engine. Current licensing separates free non-commercial use, a paid Professional commercial license, and Enterprise for console exports.

**Reason:** the five-engine cap already includes Defold as the lean 2D/lightweight-3D hypothesis. Until product scope indicates a strongly 2D-first game, adding another 2D-specialized commercial tool duplicates that axis and expands W2-ENG-03 cost.

**Reopen:** W2-PLAT-01 or game-design evidence makes 2D-first/simple-pipeline fit dominant, or Defold fails an admission assumption before comparative spikes.

### Open 3D Engine `26.05.0` — DEFER_NOT_ADMITTED

Primary-source snapshot: O3DE 26.05 is the current release; official docs emphasize Windows/Linux editor use and CMake/Ninja source/project builds, with a substantial open 3D stack.

**Reason:** it overlaps the heavyweight/open-source 3D hypothesis already bracketed by Unreal (heavyweight commercial/source-available) and Bevy/Godot (open code-first/editor-capable). Current build/setup surface is materially larger than the lean candidates, and no project-specific requirement yet makes O3DE's differentiated stack mandatory.

**Reopen:** open-source heavyweight 3D becomes a hard project requirement, Unreal's terms risk invalidates its spike, or W2-PLAT-01 exposes a platform advantage.

### Stride `4.3` — DEFER_NOT_ADMITTED

Primary-source snapshot: Stride 4.3 was released 2025-11-14 with .NET 10/C# 14; Stride is MIT-licensed and supports command-line engine builds. Current platform docs describe Windows/Linux/Android/iOS support, while parts of the Linux authoring path still depend on Windows/Game Studio.

**Reason:** it overlaps the C#/editor/general-purpose hypothesis already represented by Unity and Godot, while current cross-host authoring/build ergonomics introduce an extra uncertainty that does not add enough diversity under the five-engine cap.

**Reopen:** C#-first open-source operation becomes a project priority, Unity is removed by terms evidence, or platform-scope evidence favors Stride.

## 7. Source registry

All entries were retrieved from primary project/vendor sources on **2026-08-11**. URLs are recorded so a fresh reviewer can re-fetch them; web content itself is mutable and is not treated as immutable evidence.

### Godot

- `GODOT-REL-471` — https://godotengine.org/article/maintenance-release-godot-4-7-1/ — 4.7.1 stable release date and build commit.
- `GODOT-ARCHIVE` — https://godotengine.org/download/archive/ — stable versus development release state.
- `GODOT-FEATURES-47` — https://docs.godotengine.org/en/4.7/about/list_of_features.html — headless, CLI automation, editor/export platforms.
- `GODOT-LICENSE-47` — https://docs.godotengine.org/en/4.7/about/complying_with_licenses.html — MIT/license-notice obligations.

### Unity

- `UNITY-REL-6000.3.21F1` — https://unity.com/ja/releases/editor/whats-new/6000.3.21f1 — exact patch/release date.
- `UNITY-6-SUPPORT` — https://unity.com/releases/unity-6/support — 6.3 LTS support policy/end date and family guidance.
- `UNITY-CLI-BUILD` — https://docs.unity3d.com/6000.0/Documentation/Manual/build-command-line.html — command-line build pattern.
- `UNITY-PRICING` — https://unity.com/products — current tier thresholds/basic pricing surface.
- `UNITY-TOS-20260630` — https://unity.com/legal/terms-of-service — current agentic/automated-access restrictions.
- `UNITY-EDITOR-TERMS-20260630` — https://unity.com/legal/editor-terms-of-service/software — current editor/tier/platform terms.
- `UNITY-SOURCE-TERMS-20260630` — https://unity.com/cn/legal/editor-source-code-terms — current source-code/AI restrictions.

### Unreal Engine

- `UE-58-ANNOUNCE` — https://www.unrealengine.com/news/state-of-unreal-2026-top-news-from-the-show — UE 5.8 availability/release positioning.
- `UE-58-CLI` — https://dev.epicgames.com/documentation/en-us/unreal-engine/command-line-arguments-in-unreal-engine — command-line operation.
- `UE-58-CLI-REF` — https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-command-line-arguments-reference — `-unattended` and automation-related flags.
- `UE-LICENSE` — https://www.unrealengine.com/license — current high-level game royalty/seat model.
- `UE-EULA` — https://www.unrealengine.com/eula/unreal — current detailed Licensed Technology and Generative-AI restrictions.

### Defold

- `DEFOLD-1130-REL` — https://forum.defold.com/t/defold-1-13-0-has-been-released/82980 — official Defold release-notes channel for 1.13.0.
- `DEFOLD-BOB` — https://defold.com/manuals/bob/ — command-line build/bundle tool and target list.
- `DEFOLD-ABOUT` — https://defold.com/about/ — engine scope/platform positioning.
- `DEFOLD-LICENSE` — https://defold.com/license/ — current license summary/full text and Foundation fee commitment.

### Bevy

- `BEVY-019` — https://bevy.org/news/bevy-0-19/ — 0.19 release.
- `BEVY-QUICKSTART` — https://bevy.org/learn/quick-start/getting-started/ — current 0.19 dependency/tag and code-first setup.
- `BEVY-README` — https://github.com/bevyengine/bevy — maturity warning and MIT/Apache-2.0 licensing.
- `BEVY-PLATFORMS` — https://bevy.org/ — current public platform list.
- `BEVY-CI` — https://bevy.org/learn/quick-start/plugin-development/ — Cargo/CI guidance.

### Deferred alternatives

- `GM-ABOUT` — https://gamemaker.io/en — 2D focus/platform positioning.
- `GM-LICENSE-20260414` — https://gamemaker.io/en/help/articles/where-are-my-licenses-it-says-free — current license tier distinctions.
- `GM-FAQ-20260702` — https://test.gamemaker.io/en/help/articles/november-2023-pricing-terms-change-faq — current commercial/console pricing FAQ.
- `O3DE-2605` — https://docs.o3de.org/docs/release-notes/2605-0-release-notes/ — current 26.05 release.
- `O3DE-BUILD` — https://www.docs.o3de.org/docs/user-guide/build/ — current CMake/Ninja build workflow.
- `STRIDE-43` — https://doc.stride3d.net/latest/en/releasenotes/ — current 4.3 release notes.
- `STRIDE-BUILD` — https://doc.stride3d.net/latest/en/contributors/engine/building-source-windows-other-ide.html — command-line engine build.
- `STRIDE-PLATFORMS` — https://doc.stride3d.net/latest/en/manual/platforms/index.html — current documented target-platform surface.

## 8. Evidence versus inference

### Observed evidence

- Exact release/support/license/automation facts above are sourced from current primary project/vendor materials.
- Wave 1 requires engine-independent canonical gameplay meaning and leaves engine selection blocked.
- Unity and Unreal have current terms clauses materially relevant to AI-native workflows.
- Bevy's own project warns about early-stage/breaking-change risk.
- All five admitted candidates expose at least a plausible scriptable/code-first route to later evidence generation.

### Inference / recommendation

- Five candidates are enough to represent the principal differentiated hypotheses while keeping W2-ENG-03 bounded.
- GameMaker, O3DE, and Stride are more valuable as explicit reopen candidates than as immediate sixth-through-eighth spike targets.
- Terms friction should be measured and reviewed rather than used as an unsourced veto.
- Open-source/source-available access may improve autonomous debugging, but the actual benefit must be measured by W2-ENG-03; source availability alone is not engine fit.

## 9. Interfaces and downstream contract

### W2-ENG-02

The common S1-S10 harness must not encode conveniences that only one admitted engine supports. Candidate-specific adaptation belongs in an adaptation manifest and may not weaken scenario acceptance.

### W2-PLAT-01

Platform scope may invalidate or reprioritize this admission set. Console/mobile/desktop/web support claims remain conditional on exact selected target and vendor requirements.

### W2-RIGHTS-01

Must examine current provider/license terms, particularly:

- Unity Authorized Agentic Access and Unity Source Code restrictions;
- Unreal Generative-AI restrictions;
- Defold custom license obligations;
- open-source third-party notices/dependency licenses for Godot/Bevy;
- target-platform SDK/store terms once selected.

This artifact is not a legal opinion and cannot mark those obligations resolved.

### W2-ENG-03

Before executing comparative spikes, bind:

- exact admitted engine baseline;
- exact source/terms snapshot date;
- host/toolchain/environment;
- adaptation manifest;
- all failed/retried attempts;
- manual intervention count/type;
- build/test/profile/package/capture/recovery costs;
- exit/migration risks.

A source change may require refreshing this admission artifact before the candidate is compared.

### W2-REV-01

Must attack candidate-set bias, especially:

- hidden preference for open source or mainstream popularity;
- whether five candidates actually span distinct hypotheses;
- whether Unity/Unreal terms risks are understated;
- whether Bevy maturity risk is understated;
- whether deferred alternatives were excluded for convenience rather than evidence;
- whether unresolved platform scope makes any admission claim too strong.

## 10. Failure modes

- accidental engine ranking through prose order or adjectives;
- current primary sources becoming stale before W2-ENG-03;
- using technical CLI availability as proof that autonomous use is contractually allowed;
- treating open-source licensing as full rights clearance;
- excluding a candidate because current product/platform scope is unknown;
- allowing a candidate adaptation to weaken S1-S10 acceptance;
- hiding failed installs/builds behind a later successful run;
- allowing engine-native state to become canonical gameplay meaning;
- letting spike code become production dependency;
- treating source availability, ecosystem size, or one aggregate score as sole authority.

## 11. Freshness and reopen conditions

Reopen/refetch this admission matrix when any occurs:

1. an admitted engine ships a new stable/LTS/major release before its W2-ENG-03 spike begins;
2. Unity, Epic, Defold, Godot, or Bevy materially changes applicable license/terms or AI/automation policy;
3. W2-PLAT-01 sets a target that an admitted candidate cannot credibly reach;
4. W2-RIGHTS-01 finds an intended AI workflow prohibited or requiring an unavailable authorization;
5. W2-ENG-02 defines a harness requirement that one admitted baseline cannot attempt without weakening equivalence;
6. a deferred engine gains a project-specific differentiator not represented by the five admitted hypotheses;
7. one admitted candidate is withdrawn/unavailable or its required tooling cannot be reproduced;
8. W2-REV-01 finds material candidate-set bias or a source/version error.

A new release is not silently substituted. Refresh the source/version binding and preserve the old baseline as provenance.

## 12. Required independent critique and downstream

Required review: `W2-REV-01`.

This mission contributes `W2-ENG-01_REVIEW_READY` only. It does **not** by itself make W2-ENG-03 READY; all other declared hard prerequisites remain required.

No engine is selected, no implementation-readiness blocker is resolved, and no production/gameplay implementation is authorized.