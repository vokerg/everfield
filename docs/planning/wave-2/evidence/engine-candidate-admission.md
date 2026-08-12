# W2-REM-ENG-01 — Reconstructable engine candidate admission

**Source mission:** `W2-ENG-01` / Issue #71  
**Remediation mission:** `W2-REM-ENG-01` / Issue #93  
**Source frozen head/work:** `7e5fd79a557fd404e8178b5096b476063d606ec0`  
**Source report blob:** `cfdec22eac4865bf80fd05ea3a35270828505bbc`  
**Source handoff blob:** `7ecf85da7f69a12f27f7d251da77ecde12c2be04`  
**Source terminal status:** Issue #71 comment `5251694382`  
**Author self-review:** Issue #71 comment `5252180471` (`SR-M01`)  
**Independent pre-gate review:** Issue #71 comment `5270780071` (`PG-ENG-M01`, `PG-ENG-m01`)  
**Remediation base main:** `c7ba185ed9667b717794c19eaa0834ca41aa4c78`  
**Authoritative foundation:** `docs/planning/WAVE-1-FOUNDATIONS-v1.md` blob `a252e3c93702f3ebaecd3e888944a23dbe1b0e1d`  
**External challenger evidence observed:** `2026-08-12`  
**Task class / decision state:** `PLANNING_REVISION / EVIDENCE_REQUIRED`  
**Required independent review:** `W2-REV-01`

## 1. Remediation scope and authority

This document repairs one bounded defect in the frozen W2-ENG-01 producer candidate: the original report named five admitted engines and three plausible exclusions, but did not define a finite discovery universe or a deterministic rule proving why those were the candidates screened.

The remediation therefore adds:

1. one explicit finite **operational discovery universe** for this planning episode;
2. one gate/admission outcome for every universe member;
3. a predeclared five-slot hypothesis-coverage and tie-break rule;
4. current source-backed challenger probes for Flax Engine, Cocos Creator, and MonoGame;
5. explicit handling for plausible engines outside the operational universe; and
6. finding dispositions for the author and independent pre-gate reviews.

It deliberately preserves the original authority boundary:

- this is **admission**, not engine selection;
- the five admitted candidates are unordered;
- no scalar score is produced;
- no production/runtime/renderer decision is made;
- current platform/accessibility evidence belongs to later W2-ENG-03 spikes;
- implementation readiness and canonicalization remain unclaimed;
- formal independent adversarial review remains `W2-REV-01`.

## 2. Hard admission gates preserved from W2-ENG-01

A universe member can proceed to the diversity cap only if all hard gates below are satisfied or explicitly supported by a bounded evidence plan.

| Gate | Requirement | Fail-closed meaning |
|---|---|---|
| `G1_CURRENT_BASELINE` | exact current supported release/maintenance baseline can be identified from first-party evidence | stale/unsupported/unknown baseline -> `FAILS_ADMISSION_GATE(G1_CURRENT_BASELINE)` |
| `G2_AUTOMATION_PATH` | credible unattended CLI/headless **or** repository-native code-first build/test path exists | editor-only/manual-only path with no reproducible automation plan -> `FAILS_ADMISSION_GATE(G2_AUTOMATION_PATH)` |
| `G3_GAME_PRODUCTION_PATH` | candidate plausibly supports production of the still-unresolved 2D/3D game class | tool is too specialized or cannot support representative game production -> `FAILS_ADMISSION_GATE(G3_GAME_PRODUCTION_PATH)` |
| `G4_TERMS_EVIDENCE` | license/terms source can be identified and retained; material unknowns can be made explicit | no reconstructable terms/license evidence -> `FAILS_ADMISSION_GATE(G4_TERMS_EVIDENCE)` |
| `G5_SPIKEABLE` | a bounded equivalent feature slice can be produced without making the candidate canonical | no comparable prototype/evidence path -> `FAILS_ADMISSION_GATE(G5_SPIKEABLE)` |

Passing these gates is **necessary but not sufficient** for one of the five W2-ENG-03 spike slots.

## 3. Operational discovery universe v2

### 3.1 What “universe” means here

`ENG-UNIVERSE-v2` is a finite operational universe, not a claim to enumerate every game engine or framework in existence.

It is frozen **before** applying gate outcomes or the five-slot cap. A new engine cannot be inserted into this episode after seeing results without creating a new universe version and reopening the admission decision.

### 3.2 Construction rule

The v2 universe is constructed from two explicit components:

1. **Frozen producer set:** all eight engines named anywhere in the Issue #71 admission report — the five admitted candidates plus all three named plausible exclusions.
2. **Review challenger set:** three deliberately selected challengers used to test the exact omission defect raised by review, each representing an admission boundary the frozen report did not screen:
   - `Flax Engine` — current source-available/commercial general-purpose editor/engine with documented headless CLI;
   - `Cocos Creator` — current integrated 2D/3D editor with documented command-line publishing but a GUI-environment constraint;
   - `MonoGame` — current repository-native/code-first game framework boundary probe with command-line build/content tooling.

The resulting exact member list is fixed below. The construction rule is intentionally bounded to remediate auditability; it does not claim that the challenger set is an exhaustive internet search.

### 3.3 Exact member list

```yaml
operational_discovery_universe:
  universe_id: ENG-UNIVERSE-v2
  source_candidate: 7e5fd79a557fd404e8178b5096b476063d606ec0
  frozen_before_outcomes: true
  members:
    - Bevy
    - Defold
    - Godot
    - Unity
    - Unreal Engine
    - GameMaker
    - O3DE
    - Stride
    - Flax Engine
    - Cocos Creator
    - MonoGame
```

Any engine not on this exact list is `OUTSIDE_OPERATIONAL_UNIVERSE(ENG-UNIVERSE-v2)` for this episode, not silently “rejected.” See §8 for reopen policy.

## 4. Challenger source evidence added by remediation

The original eight candidates retain the frozen Issue #71 first-party source records and observations. The independent review spot-checked the sampled current baselines on 2026-08-12 and found no material drift requiring admission changes for Bevy, Godot, or Defold.

The three challengers were evaluated from current first-party sources on 2026-08-12.

### 4.1 Flax Engine

**Baseline:** Flax 1.12, released 2026-05-19; first-party release post reports version `1.12.6912.0`.

**Automation:** first-party command-line documentation exposes headless build invocation, including `FlaxEditor.exe ... -headless ... -build "Development.Windows"`, plus command-line project/run/test-related options.

**Terms:** first-party licensing page publishes the current commercial license/EULA posture and source-access/licensing terms.

**Sources:** 

- `https://flaxengine.com/blog/flax-1-12-released/`
- `https://docs.flaxengine.com/manual/editor/advanced/command-line-access.html`
- `https://flaxengine.com/licensing/`

**Gate result:** passes the admission gates. It must therefore be dispositioned by the diversity cap rather than silently omitted.

### 4.2 Cocos Creator

**Baseline:** Cocos Creator 3.8.8 is the current maintained 3.x line evidenced by the official Cocos community release announcement and current product/manual surfaces. The Cocos team also stated in July 2026 that Creator 3.x continues to be maintained while resources are shared with PinK.

**Game path:** first-party product documentation describes Cocos Creator as an integrated cross-platform 2D/3D game-development editor/tool.

**Automation:** first-party 3.8 manual documents command-line publishing with explicit exit codes and build parameters. The same document states that Cocos Creator still needs a GUI environment when run from the command line; Jenkins agent mode is suggested where a server cannot interact with the OS window server.

**Terms:** the current first-party Cocos User Agreement records that Cocos Creator can be used free of charge for developing games and contains separate scope restrictions/terms; exact project use must still retain the applicable Cocos Creator software-license evidence.

**Sources:** 

- `https://forum.cocos.org/t/topic/172319`
- `https://www.cocos.com/en/creator`
- `https://docs.cocos.com/creator/3.8/manual/en/editor/publish/publish-in-command-line.html`
- `https://download.cocos.com/CocosUdc/agreement/Cocos_User_Service_Agreement_en_20220901.html`

**Gate result:** passes the admission gates with a material automation constraint. GUI-environment dependence is a spike risk, not an automatic gate failure because a documented unattended agent-mode path exists.

### 4.3 MonoGame

**Baseline:** MonoGame 3.8.5, released 2026-07-15 by the MonoGame Foundation.

**Game path:** first-party docs describe a cross-platform .NET framework used to build desktop/mobile/console games; Windows, macOS, and Linux are publicly supported, while console code remains partner-gated.

**Automation:** project creation/build is repository-native .NET tooling; MonoGame documents CLI project templates, CI content-building, and the `mgcb` command-line content builder.

**Terms:** official repository states the project is under the Microsoft Public License except for identified portions/third-party libraries with their own licenses.

**Sources:** 

- `https://monogame.net/blog/2026-07-15-3.8.5-release-2026/`
- `https://docs.monogame.net/articles/getting_started/`
- `https://docs.monogame.net/articles/getting_started/content_pipeline/automating_content_builder.html`
- `https://docs.monogame.net/articles/getting_started/tools/mgcb.html`
- `https://github.com/MonoGame/MonoGame`

**Gate result:** passes the admission gates as a code-first framework boundary probe. Its framework nature is a comparative hypothesis, not a reason to erase it before the diversity cap.

## 5. Predeclared diversity-cap rule

The five-slot cap exists to maximize **decision information**, not to rank engines for production.

### 5.1 Five decision-critical hypothesis classes

Before applying the cap, every gate-passing member is mapped to one or more of these five classes:

1. `H1_CODE_FIRST_REPOSITORY_NATIVE` — minimal/editor-light, code-first engine/framework workflow.
2. `H2_LEAN_INTEGRATED_2D_FIRST` — integrated lightweight editor/runtime with strong 2D workflow and bounded 3D path.
3. `H3_OPEN_GENERAL_PURPOSE_EDITOR` — open-source/general-purpose editor engine with broad 2D/3D tooling.
4. `H4_MAINSTREAM_COMMERCIAL_ECOSYSTEM` — commercial editor/runtime with broad ecosystem/platform/tooling evidence and materially different agentic/license/terms risk.
5. `H5_HEAVYWEIGHT_3D_PLATFORM_BREADTH` — heavyweight editor/source/toolchain path that stress-tests automation, build weight, source access, and high-end 3D/platform assumptions.

A candidate may cover multiple classes; this does not create an extra slot.

### 5.2 Lexicographic tie-break within a hypothesis

When more than one gate-passing member covers the same hypothesis, choose one representative by this order:

1. **Distinct evidence contrast:** prefer the member that exposes the clearest decision-relevant contrast not already exercised by another selected class.
2. **Automation evidence strength:** repository-native/code-first or true headless/CLI path beats a path requiring a desktop GUI/window server, all else equal.
3. **Evidence maturity:** prefer exact current release + first-party automation + terms + diagnostic/evidence hooks that make the bounded spike more reproducible.
4. **Decision-critical risk exposure:** if still tied, prefer the candidate that exposes a material unresolved risk the program must learn about (for example mainstream commercial agentic terms or heavyweight build/source/platform complexity) rather than a near-duplicate of an already represented risk.
5. **Stable final tie-break:** case-insensitive canonical candidate name.

The rule is lexicographic, not a weighted score. A runner-up remains `DEFERRED_BY_DIVERSITY_CAP`; it is not ranked “worse” for production.

## 6. Complete negative screen for ENG-UNIVERSE-v2

| Candidate | Hard gates | Primary hypothesis coverage | Operational outcome | Reconstructable rationale |
|---|---|---|---|---|
| **Bevy** | PASS | H1 | `ADMITTED` | strongest code-first/repository-native engine contrast; current Rust/ECS architecture and CLI-native workflow maximize distinction from editor-first candidates |
| **MonoGame** | PASS | H1 | `DEFERRED_BY_DIVERSITY_CAP` | credible code-first framework and CLI/CI path, but within the five-slot cap Bevy provides the more engine-architecture-specific H1 contrast while MonoGame remains a retained runner-up boundary probe |
| **Defold** | PASS | H2 | `ADMITTED` | lean integrated runtime/editor with first-party headless build tooling; strongest H2 automation contrast |
| **GameMaker** | PASS | H2 | `DEFERRED_BY_DIVERSITY_CAP` | plausible lean 2D commercial candidate retained from producer; overlaps H2 and does not add a sixth decision-critical hypothesis |
| **Cocos Creator** | PASS_WITH_AUTOMATION_RISK | H2, H3 | `DEFERRED_BY_DIVERSITY_CAP` | current 2D/3D integrated editor and CLI publishing are credible, but official docs require GUI environment for CLI; Defold/Godot cover H2/H3 with stronger unattended evidence |
| **Godot** | PASS | H3 | `ADMITTED` | broad open general-purpose editor engine with documented headless/CLI operation; strongest H3 evidence contrast |
| **Stride** | PASS | H3, H5 | `DEFERRED_BY_DIVERSITY_CAP` | plausible open C# general-purpose/3D engine, but overlaps Godot/Unreal hypotheses within the cap and adds less distinct decision risk than either representative |
| **Unity** | PASS_WITH_TERMS_RISK | H4 | `ADMITTED` | uniquely represents mainstream commercial ecosystem plus unresolved agentic/editor-license/terms questions that later spikes must evidence rather than assume |
| **Flax Engine** | PASS | H3, H4, H5 | `DEFERRED_BY_DIVERSITY_CAP` | current 1.12 headless CLI and published license make it a real gate-passing challenger; however its evidence hypotheses overlap the selected Godot/Unity/Unreal representatives and do not justify displacing one under the lexicographic cap |
| **Unreal Engine** | PASS_WITH_WEIGHT_RISK | H5 | `ADMITTED` | strongest heavyweight/source/build/platform-complexity contrast; intentionally tests whether the evidence value justifies automation/build cost |
| **O3DE** | PASS_WITH_WEIGHT_RISK | H3, H5 | `DEFERRED_BY_DIVERSITY_CAP` | plausible open heavyweight candidate retained from producer; overlaps H5 and open-editor/source hypotheses without adding a distinct sixth hypothesis |

### 6.1 Resulting five-slot spike set

The corrected deterministic screen reproduces the original five admitted candidates:

```yaml
w2_eng_03_admitted_set:
  - Bevy
  - Defold
  - Godot
  - Unity
  - Unreal Engine
ordering_semantics: unordered
selection_authority: none
selection_happens_in: later_engine_decision_chain_after_equivalent_spikes_and_review
```

The **set is unchanged**, but its provenance is now reconstructable. Flax is the most important correction: it is explicitly recognized as a gate-passing challenger and then diversity-deferred rather than silently absent.

## 7. Selected-candidate baselines and original evidence posture preserved

The five admitted baselines remain the frozen W2-ENG-01 source baselines unless a freshness trigger fires before W2-ENG-03 execution:

| Candidate | Frozen producer baseline | Automation/evidence posture | Material unresolved risk retained |
|---|---|---|---|
| Bevy | 0.19.0 | code-first Cargo/Rust workflow; deterministic test/build evidence | smaller editor/content workflow; platform/tooling evidence must be measured |
| Defold | 1.13.0 | editor plus documented headless builder path | narrower 3D/editor assumptions; service/tool terms need exact spike capture |
| Godot | 4.7.1-stable | documented headless/CLI editor/import/export path | engine/UI/platform fit must be measured, not inferred from openness |
| Unity | 6000.3.21f1 | batch-mode/editor CLI path | commercial/editor automation, account/license/terms and agentic policy evidence are material and freshness-sensitive |
| Unreal Engine | 5.8 | commandlets/automation/build tooling | heavyweight setup/build/storage/source/platform cost and account/license evidence are material |

The remediation does **not** claim those version strings remain valid forever. W2-ENG-03 must recheck current release/terms/platform-sensitive evidence at spike acquisition and record any version drift rather than silently reusing stale values.

## 8. Engines outside ENG-UNIVERSE-v2

An engine not listed in §3 is not “failed.” It has status:

`OUTSIDE_OPERATIONAL_UNIVERSE(ENG-UNIVERSE-v2)`.

This bounded episode intentionally excludes additional families because the purpose is to repair and make reproducible the five-hypothesis comparative set, not to perform an unbounded market census.

Examples of outside-universe classes and reopen triggers:

| Outside class | Examples | Why outside this universe version | Reopen trigger |
|---|---|---|---|
| specialized genre/narrative/template engines | RPG Maker, Ren'Py and similar | unresolved product scope currently requires a broader 2D/3D/general gameplay hypothesis | product scope narrows enough that specialized tooling becomes a first-class hypothesis |
| additional browser/no-code/visual-authoring engines | Construct, GDevelop and similar | v2 already includes Cocos as an editor/automation boundary probe; no distinct sixth hypothesis is allocated | visual/no-code authoring becomes a required product/agentic hypothesis or selected candidates fail automation evidence |
| additional framework/library candidates | raylib, FNA, custom SDL stacks and similar | v2 includes MonoGame as the code-first framework boundary probe and Bevy as the code-first engine representative | W2-ENG-03 shows engine/editor overhead is itself disqualifying or framework-first architecture becomes a required hypothesis |
| additional commercial/source-available general-purpose engines | other maintained editor engines | v2 includes Flax as the explicit omitted-candidate challenger and Unity/Unreal as commercial/heavy representatives | new evidence reveals a materially distinct automation/platform/terms hypothesis not covered by the five classes |
| unsupported/abandoned or no-current-first-party-baseline tools | any such engine | fail the purpose of current reproducible evidence before screening | supported release and primary-source evidence becomes available |

A reviewer may propose `ENG-UNIVERSE-v3` if a specific outside candidate exposes a decision-critical hypothesis not represented here. That is a **reopen event**, not evidence that v2 secretly screened the candidate.

## 9. Downstream W2-ENG-03 requirements preserved

All five admitted candidates must receive the same capability-equivalent feature slice and evidence envelope. The spike must record at minimum:

- exact engine/toolchain/plugin/account baseline;
- exact source/base/candidate identity;
- unattended setup/build/package/test path;
- deterministic simulation/replay or equivalent reproducible behavior;
- representative input/UI/accessibility hooks required by current platform/accessibility evidence;
- save/state serialization and migration seam;
- asset/import/build pipeline behavior;
- diagnostics/log/capture/profiling evidence;
- Windows + selected Steam Deck/Proton platform evidence as applicable to the corrected platform scope;
- terms/license/account evidence and unresolved restrictions;
- time/resource/manual-intervention costs as evidence, not as a weighted score.

A `DEFERRED_BY_DIVERSITY_CAP` candidate can be promoted only by reopening the universe/cap decision with exact reason/provenance; it cannot be silently substituted mid-spike.

## 10. Failure modes and controls

| Failure mode | Consequence | Control |
|---|---|---|
| post-hoc candidate list | omitted engines cannot be distinguished from screened failures | exact frozen ENG-UNIVERSE-v2 member list |
| plausible omitted candidate disappears | admission completeness overstated | Flax/Cocos/MonoGame explicit challenger screen |
| diversity cap becomes ranking | admission stage selects an engine | hypothesis coverage + unordered admitted set; no scalar score |
| tie-break changes after outcome | desired candidate rationalized after the fact | lexicographic rule declared before negative-screen result |
| gate-passing runner-up treated as failure | useful alternatives lost | `DEFERRED_BY_DIVERSITY_CAP` distinct from gate failure |
| outside engine treated as rejected | false exhaustiveness | `OUTSIDE_OPERATIONAL_UNIVERSE` + explicit reopen rule |
| GUI CLI treated as equivalent to true headless | automation risk hidden | Cocos records GUI-environment constraint and loses tie-break on automation strength |
| source/version drift | spike starts from stale facts | acquisition-time freshness recheck and exact evidence record |
| current platform/accessibility changes | wrong spike workload | W2-ENG-03 consumes corrected platform/accessibility provenance and reopens admission if a hypothesis becomes invalid |

## 11. Freshness and reopen conditions

Reopen this admission set when:

- any admitted candidate loses current support, automation path, or usable terms evidence;
- a deferred member materially changes automation/platform/terms posture such that the predeclared tie-break would select it instead;
- W2-PLAT-01/W2-REM-PLAT-01 or W2-ACC-01 changes the required platform/input/UI evidence envelope enough to invalidate a gate or hypothesis;
- an outside-universe engine is shown from current primary evidence to expose a materially distinct decision-critical hypothesis not represented by H1–H5;
- equivalent spikes reveal that one hypothesis is not actually testable by its selected representative;
- W2-REV-01 finds a BLOCKER/MAJOR against the universe, gates, tie-break, or source evidence.

Provider/license/terms evidence remains freshness-sensitive. No admission state authorizes production use or waives a later terms recheck.

## 12. Remediation acceptance check

Against Issue #93 acceptance criteria:

- exact frozen Issue #71 provenance retained: **PASS**;
- finite operational universe explicit and versioned: **PASS**;
- construction rule declared and intentionally non-exhaustive: **PASS**;
- all 11 members have a gate/admission outcome: **PASS**;
- `ADMITTED` distinct from `DEFERRED_BY_DIVERSITY_CAP`: **PASS**;
- outside-universe state/reopen rule explicit: **PASS**;
- Flax current release/headless/license evidence screened: **PASS**;
- Cocos current 3.8 CLI/GUI-environment/terms evidence screened: **PASS**;
- MonoGame current 3.8.5 code-first/CLI/license evidence screened: **PASS**;
- five-slot tie-break declared before application and non-scalar: **PASS**;
- original five-engine admitted set reproduced without engine-selection authority: **PASS**;
- current platform/terms/source risks preserved: **PASS**;
- implementation/readiness/canonicalization authority: **NOT CLAIMED**;
- required formal independent critique remains `W2-REV-01`: **PASS**.

**Producer remediation disposition:** `REVIEW_READY_CANDIDATE / EVIDENCE_REQUIRED`. This corrected packet may supersede the frozen Issue #71 report as the substantive W2-ENG-01 input to W2-ENG-03 once terminal provenance is bound; it is not an engine decision.
