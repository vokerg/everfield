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

This document repairs the auditability defect in the frozen W2-ENG-01 producer candidate. The original report named five admitted engines and three plausible exclusions but did not define a finite discovery universe or a deterministic rule proving why those were the candidates screened.

The remediation adds:

1. an explicit finite **operational discovery universe** for this planning episode;
2. one screen/admission outcome for every universe member;
3. a deterministic five-slot hypothesis-assignment rule declared before the screen result;
4. current first-party challenger evidence for Flax Engine, Cocos Creator, and MonoGame;
5. an explicit state and reopen rule for engines outside the bounded universe; and
6. dispositions for the author and independent review findings.

Authority remains unchanged: this is **admission**, not engine selection. The five admitted candidates are unordered; no scalar score, production engine decision, implementation-readiness decision, or canonicalization is created. Formal independent adversarial review remains `W2-REV-01`.

## 2. Hard admission gates preserved from W2-ENG-01

A universe member may proceed to the diversity cap only if all hard gates are satisfied or a bounded evidence path is explicitly available.

| Gate | Requirement | Fail-closed result |
|---|---|---|
| `G1_CURRENT_BASELINE` | current supported release/maintenance baseline can be identified from first-party evidence | `FAILS_ADMISSION_GATE(G1_CURRENT_BASELINE)` |
| `G2_AUTOMATION_PATH` | credible unattended CLI/headless **or** repository-native code-first build/test path exists | `FAILS_ADMISSION_GATE(G2_AUTOMATION_PATH)` |
| `G3_GAME_PRODUCTION_PATH` | candidate plausibly supports production of the still-unresolved 2D/3D game class | `FAILS_ADMISSION_GATE(G3_GAME_PRODUCTION_PATH)` |
| `G4_TERMS_EVIDENCE` | license/terms source can be identified and retained; material unknowns can be explicit | `FAILS_ADMISSION_GATE(G4_TERMS_EVIDENCE)` |
| `G5_SPIKEABLE` | a bounded equivalent feature slice can be built without making the candidate canonical | `FAILS_ADMISSION_GATE(G5_SPIKEABLE)` |

Passing these gates is necessary but not sufficient for a W2-ENG-03 spike slot.

## 3. Operational discovery universe v2

### 3.1 Bounded meaning

`ENG-UNIVERSE-v2` is a finite operational universe, not a claim to enumerate every game engine or framework in existence. It is frozen before applying gate outcomes or the five-slot cap. Adding another engine later requires a new universe version and a recorded reopen reason.

### 3.2 Construction rule

The exact universe is the union of:

1. **all eight engines named anywhere in the frozen Issue #71 report** — the five admitted candidates plus all three named plausible exclusions; and
2. **three fixed remediation challengers** chosen before the v2 screen to exercise the omission boundaries identified during review:
   - `Flax Engine`: omitted current general-purpose/source-available commercial engine with documented headless CLI;
   - `Cocos Creator`: integrated 2D/3D editor with documented CLI publishing and a material GUI-environment constraint;
   - `MonoGame`: repository-native/code-first framework boundary probe with CLI build/content tooling.

The challenger set is intentionally finite and fixed. It is not described as an exhaustive market search.

### 3.3 Exact member list

```yaml
operational_discovery_universe:
  universe_id: ENG-UNIVERSE-v2
  source_candidate: 7e5fd79a557fd404e8178b5096b476063d606ec0
  frozen_before_screen_outcomes: true
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

Any engine not on this exact list is `OUTSIDE_OPERATIONAL_UNIVERSE(ENG-UNIVERSE-v2)`, not silently rejected.

## 4. Current challenger evidence added by remediation

The original eight candidates retain the frozen Issue #71 first-party evidence and remain subject to acquisition-time freshness checks in W2-ENG-03. The three challengers were rechecked from first-party sources on 2026-08-12.

### 4.1 Flax Engine

**Baseline:** Flax Engine 1.12; first-party release post dated **2026-05-18**.

**Automation:** first-party command-line documentation exposes headless invocation and build automation, including `-headless` and `-build` usage for game targets.

**Terms:** the first-party licensing page publishes current Flax licensing/EULA and source-access/commercial terms. Exact project/account applicability remains a later spike-time evidence item.

**First-party sources:**

- `https://flaxengine.com/blog/flax-1-12-released/`
- `https://docs.flaxengine.com/manual/editor/advanced/command-line-access.html`
- `https://flaxengine.com/licensing/`

**Gate result:** `PASS`. Flax therefore requires an explicit diversity-cap disposition rather than omission.

### 4.2 Cocos Creator

**Baseline:** Cocos Creator **3.8.8**, first-party release notes dated **2025-12-16**. A Cocos staff response on the official Cocos community stated on 2026-07-01 that the 3.x line would continue to be maintained, while acknowledging slower updates as resources were shared with PinK.

**Game path:** first-party Cocos product/terms material describes Creator as a scripted, component/data-driven integrated tool for 2D and 3D interactive/game content across multiple platforms.

**Automation:** the first-party 3.8 manual documents command-line publishing with build parameters and exit codes. The same documentation states that Cocos Creator still requires a GUI environment when invoked from the command line; Jenkins agent mode is suggested for server automation where the service process cannot interact with the window server.

**Terms:** the currently published Cocos User Agreement is dated **2022-09-01**. It states that Cocos Creator may be used free of charge for developing games, but also states that specific Cocos products may have their own Software License and Services Agreement and that such specific terms must also be accepted. Therefore G4 passes only as **terms evidence available with exact-product-license follow-up required**; this report does not treat the general User Agreement as complete release clearance.

**First-party sources:**

- `https://www.cocos.com/en/update`
- `https://forum.cocos.org/t/topic/176410`
- `https://www.cocos.com/en/creator`
- `https://docs.cocos.com/creator/3.8/manual/en/editor/publish/publish-in-command-line.html`
- `https://download.cocos.com/CocosUdc/agreement/Cocos_User_Service_Agreement_en_20220901.html`

**Gate result:** `PASS_WITH_AUTOMATION_AND_TERMS_FOLLOWUP`. GUI-environment dependence and exact product-license capture are spike risks, not silent exclusions.

### 4.3 MonoGame

**Baseline:** MonoGame **3.8.5**, first-party release post dated **2026-07-15**.

**Game path:** first-party documentation describes MonoGame as a cross-platform .NET framework for building games. Public desktop support includes Windows, macOS, and Linux; console access remains partner-gated.

**Automation:** first-party documentation covers CLI project/build workflows, CI content building, and the `mgcb` command-line content builder.

**Terms:** the official MonoGame repository states that MonoGame is released under the Microsoft Public License except for identified portions/third-party libraries with their own licenses.

**First-party sources:**

- `https://monogame.net/blog/2026-07-15-3.8.5-release-2026/`
- `https://docs.monogame.net/articles/getting_started/`
- `https://docs.monogame.net/articles/getting_started/content_pipeline/automating_content_builder.html`
- `https://docs.monogame.net/articles/getting_started/tools/mgcb.html`
- `https://github.com/MonoGame/MonoGame`

**Gate result:** `PASS` as a code-first framework boundary probe. Framework status is a comparative hypothesis, not a pre-cap failure.

## 5. Deterministic five-slot diversity-cap rule

The cap exists to maximize distinct decision information without ranking engines for production.

### 5.1 Five experiment hypotheses

The v2 experiment reserves one slot for each hypothesis:

1. `H1_CODE_FIRST_REPOSITORY_NATIVE`
2. `H2_LEAN_INTEGRATED_2D_FIRST`
3. `H3_OPEN_GENERAL_PURPOSE_EDITOR`
4. `H4_MAINSTREAM_COMMERCIAL_EDITOR_TERMS_RISK`
5. `H5_HEAVYWEIGHT_3D_SOURCE_PLATFORM_BREADTH`

These are experiment-design classes, not engine quality tiers.

### 5.2 Frozen representative priority lists

The following lists are declared before §6 applies them. For each hypothesis in H1→H5 order, select the **first hard-gate-passing member not already assigned to an earlier slot**. A member later in the same list is `DEFERRED_BY_DIVERSITY_CAP` if it passes gates but is not selected. These priority lists are experiment assignment preferences, not production rankings.

```yaml
hypothesis_representative_priority:
  H1_CODE_FIRST_REPOSITORY_NATIVE:
    - Bevy
    - MonoGame
  H2_LEAN_INTEGRATED_2D_FIRST:
    - Defold
    - GameMaker
    - Cocos Creator
  H3_OPEN_GENERAL_PURPOSE_EDITOR:
    - Godot
    - Stride
    - O3DE
    - Cocos Creator
    - Flax Engine
  H4_MAINSTREAM_COMMERCIAL_EDITOR_TERMS_RISK:
    - Unity
    - Flax Engine
    - GameMaker
    - Cocos Creator
  H5_HEAVYWEIGHT_3D_SOURCE_PLATFORM_BREADTH:
    - Unreal Engine
    - O3DE
    - Stride
    - Flax Engine
```

### 5.3 Why these experiment priorities are frozen this way

- H1 prefers an engine-architecture/ECS code-first probe before the lower-level framework boundary probe.
- H2 prefers a lean integrated engine with documented true headless build evidence before commercial/GUI-dependent alternatives.
- H3 prefers the broad open general-purpose editor representative with strong documented headless evidence; additional open/source-available editors remain runner-ups.
- H4 intentionally uses Unity as the representative for mainstream commercial editor/account/license/agentic-terms risk already identified by the producer evidence; Flax and other commercial editors remain challengers rather than duplicating that slot.
- H5 intentionally uses Unreal as the representative for the heavyweight source/build/platform-complexity hypothesis; O3DE/Stride/Flax are retained alternatives.

Because the exact lists are frozen in this remediation before the outcome table, the five-slot result is mechanically reproducible even where qualitative experiment-design judgments are involved. Changing a priority list requires a new admission-universe/cap version and provenance.

## 6. Complete negative screen for ENG-UNIVERSE-v2

| Candidate | Hard-gate state | Hypothesis membership | Operational outcome | Reason |
|---|---|---|---|---|
| **Bevy** | PASS | H1 | `ADMITTED` | first passing H1 representative |
| **MonoGame** | PASS | H1 | `DEFERRED_BY_DIVERSITY_CAP` | H1 already represented by Bevy; retained code-first framework runner-up |
| **Defold** | PASS | H2 | `ADMITTED` | first passing H2 representative |
| **GameMaker** | PASS | H2, H4 | `DEFERRED_BY_DIVERSITY_CAP` | H2 represented by Defold; H4 priority selects Unity |
| **Cocos Creator** | PASS_WITH_AUTOMATION_AND_TERMS_FOLLOWUP | H2, H3, H4 | `DEFERRED_BY_DIVERSITY_CAP` | H2/H3/H4 already receive earlier representatives; GUI-environment constraint remains explicit |
| **Godot** | PASS | H3 | `ADMITTED` | first passing H3 representative |
| **Stride** | PASS | H3, H5 | `DEFERRED_BY_DIVERSITY_CAP` | H3 represented by Godot; H5 priority selects Unreal |
| **Unity** | PASS_WITH_TERMS_RISK | H4 | `ADMITTED` | first passing H4 representative; exact account/license/automation terms remain spike evidence |
| **Flax Engine** | PASS | H3, H4, H5 | `DEFERRED_BY_DIVERSITY_CAP` | explicit gate-passing challenger; all represented hypotheses have earlier frozen representatives |
| **Unreal Engine** | PASS_WITH_WEIGHT_RISK | H5 | `ADMITTED` | first passing H5 representative |
| **O3DE** | PASS_WITH_WEIGHT_RISK | H3, H5 | `DEFERRED_BY_DIVERSITY_CAP` | H3 represented by Godot; H5 priority selects Unreal |

No universe member is left with an implicit outcome.

### 6.1 Resulting five-slot spike set

Applying §5 mechanically reproduces the original five-engine set:

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

The set is unchanged, but its discovery and cap provenance are now reconstructable. Flax is explicitly a gate-passing challenger that is diversity-deferred rather than silently absent.

## 7. Selected baselines and original risk posture preserved

The five admitted baselines remain the frozen W2-ENG-01 producer baselines **only as starting evidence**; W2-ENG-03 must recheck current releases, account/tool terms, and platform-sensitive facts at spike acquisition.

| Candidate | Frozen producer baseline | Automation/evidence posture | Material unresolved risk |
|---|---|---|---|
| Bevy | 0.19.0 | code-first Cargo/Rust workflow | editor/content workflow and platform fit must be measured |
| Defold | 1.13.0 | editor plus documented headless builder path | 3D/editor assumptions and service/tool terms require spike evidence |
| Godot | 4.7.1-stable | documented headless/CLI editor/import/export | UI/platform fit must be measured |
| Unity | 6000.3.21f1 | batch-mode/editor CLI | commercial/account/license/agentic automation terms are freshness-sensitive |
| Unreal Engine | 5.8 | commandlets/automation/build tooling | heavyweight setup/build/storage/source/platform cost and account/license evidence |

A version change does not automatically invalidate the hypothesis, but it must create a new exact spike baseline rather than silently reusing a stale string.

## 8. Engines outside ENG-UNIVERSE-v2

An unlisted engine has state `OUTSIDE_OPERATIONAL_UNIVERSE(ENG-UNIVERSE-v2)` for this episode. It has not failed a gate.

| Outside class | Examples | Why outside v2 | Reopen trigger |
|---|---|---|---|
| specialized genre/narrative/template engines | RPG Maker, Ren'Py, similar | unresolved product scope still requires broad game-production hypotheses | product scope narrows enough to make specialization decision-critical |
| additional visual/no-code/browser engines | Construct, GDevelop, similar | Cocos already probes editor/GUI automation boundary; no sixth hypothesis allocated | visual/no-code authoring becomes a first-class requirement or selected automation paths fail |
| additional frameworks/libraries | raylib, FNA, custom SDL stacks, similar | MonoGame is the framework boundary probe and Bevy represents H1 | W2-ENG-03 shows engine/editor overhead itself is disqualifying |
| additional commercial/source-available editors | other maintained engines | Flax is the explicit omitted-candidate challenger; H4/H5 already have representatives | new evidence exposes a distinct decision-critical hypothesis not covered by H1–H5 |
| unsupported/no-current-primary-baseline tools | any such tool | outside current reproducible evidence purpose | supported current release + primary evidence becomes available |

A reviewer may propose `ENG-UNIVERSE-v3` if a specific outside engine exposes a materially distinct decision-critical hypothesis. That is a reopen event, not proof that v2 had silently screened it.

## 9. W2-ENG-03 input requirements preserved

Every admitted candidate must receive a capability-equivalent feature slice and comparable evidence envelope. At minimum the spike must retain:

- exact engine/toolchain/plugin/account baseline;
- exact source/base/candidate identity;
- unattended setup/build/package/test path;
- deterministic simulation/replay or equivalent reproducible behavior;
- current platform/accessibility input/UI evidence required by the corrected W2-PLAT/W2-ACC packets;
- save/state serialization and migration seam;
- asset/import/build pipeline behavior;
- diagnostics/log/capture/profiling evidence;
- Windows + selected Steam Deck/Proton evidence as applicable;
- exact terms/license/account evidence and unresolved restrictions;
- manual-intervention/time/resource costs as evidence, not a weighted score.

A `DEFERRED_BY_DIVERSITY_CAP` candidate can be promoted only by reopening the admission/cap decision with exact provenance. It cannot be silently substituted mid-spike.

## 10. Failure modes and controls

| Failure mode | Consequence | Control |
|---|---|---|
| post-hoc candidate list | omissions cannot be distinguished from screened failures | frozen ENG-UNIVERSE-v2 list |
| plausible omitted candidate disappears | admission completeness overstated | explicit Flax/Cocos/MonoGame challenger screen |
| diversity cap becomes ranking | admission stage selects production engine | five experiment hypotheses + unordered output; no scalar score |
| subjective tie resolved differently later | set not reproducible | exact frozen representative-priority lists |
| gate-passing runner-up treated as failure | useful alternative erased | `DEFERRED_BY_DIVERSITY_CAP` distinct from gate failure |
| outside engine treated as rejected | false exhaustiveness | `OUTSIDE_OPERATIONAL_UNIVERSE` + reopen rule |
| GUI CLI equated to true headless | automation risk hidden | Cocos GUI-environment constraint explicit |
| general terms treated as exact product clearance | license risk hidden | Cocos exact-product license follow-up explicit; all terms refreshed at spike time |
| source/version drift | spike starts from stale facts | acquisition-time freshness recheck |
| platform/accessibility change | wrong spike workload | consume corrected W2-PLAT/W2-ACC provenance and reopen admission when needed |

## 11. Freshness and reopen conditions

Reopen this admission set when:

- any admitted representative loses current support, viable automation, or reconstructable terms evidence;
- a deferred member materially changes automation/platform/terms posture and the frozen experiment assignment itself is no longer fit for purpose;
- W2-PLAT/W2-ACC changes the required platform/input/UI evidence envelope enough to invalidate a gate/hypothesis;
- a specific outside-universe candidate is shown from current primary evidence to expose a materially distinct decision-critical hypothesis not represented by H1–H5;
- equivalent spikes show that a selected representative cannot actually test its assigned hypothesis;
- W2-REV-01 finds a BLOCKER/MAJOR against the universe, gates, cap rule, or source evidence.

Provider/license/terms evidence remains freshness-sensitive. Admission never authorizes production use.

## 12. Remediation acceptance check

Against Issue #93 acceptance criteria:

- exact frozen Issue #71 provenance retained: **PASS**;
- finite operational universe explicit/versioned: **PASS**;
- construction rule intentional and non-exhaustive: **PASS**;
- every one of 11 members has an explicit screen outcome: **PASS**;
- `ADMITTED`, `DEFERRED_BY_DIVERSITY_CAP`, gate failure, and outside-universe states are distinguishable: **PASS**;
- Flax 1.12 current release/headless/license evidence screened: **PASS**;
- Cocos Creator 3.8.8 CLI/GUI-environment/general-terms + product-license follow-up screened: **PASS**;
- MonoGame 3.8.5 code-first/CLI/license evidence screened: **PASS**;
- deterministic five-slot assignment rule declared before outcome and contains no scalar score: **PASS**;
- original five-engine spike set mechanically reproduced: **PASS**;
- terms/platform/source risks preserved: **PASS**;
- engine selection/readiness/canonicalization authority: **NOT CLAIMED**;
- required independent critique remains `W2-REV-01`: **PASS**.

Producer self-review correction before terminalization: the first remediation draft misstated Flax 1.12's first-party release-post date as 2026-05-19 and asserted an unverified exact build-version string. The final report uses the verified **2026-05-18** post date and omits the unsupported build string. The first draft also used a qualitative lexicographic cap tie-break; the final report replaces it with exact frozen representative-priority lists so the five-slot assignment is mechanically reproducible.

**Producer remediation disposition:** `REVIEW_READY_CANDIDATE / EVIDENCE_REQUIRED`. Once terminal provenance is bound, this packet may supersede the frozen Issue #71 producer report as the substantive W2-ENG-01 input to W2-ENG-03; it is not an engine decision.
