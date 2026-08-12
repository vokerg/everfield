# W2-REM-ENG-02 — Engine spike harness v2

**Source mission:** `W2-ENG-02` / Issue #72  
**Remediation mission:** `W2-REM-ENG-02` / Issue #94  
**Source frozen head/work:** `af914fa147f22af1f544f7cdeb07a5e4234c9f8c`  
**Source harness blob:** `da29b1b867f01f0efaeda28616f4f5dc329ee2c9`  
**Source handoff blob:** `3857e514f786b404c1c6948bdf7b3ed68c168920`  
**Source terminal status:** Issue #72 comment `5255039768`  
**Independent pre-gate review:** Issue #72 comment `5270974506`  
**Remediation base main:** `c7ba185ed9667b717794c19eaa0834ca41aa4c78`  
**Authoritative foundation:** `docs/planning/WAVE-1-FOUNDATIONS-v1.md` blob `a252e3c93702f3ebaecd3e888944a23dbe1b0e1d`  
**Harness ID:** `W2-ENG-HARNESS-v2`  
**Feature slice ID:** `W2-ENG-FEATURE-SLICE-v2`  
**Scenario manifest ID:** `W2-ENG-SCENARIO-INPUTS-v2`  
**Executable fixture:** `docs/planning/wave-2/evidence/engine-spike-protocol-fixtures.py`  
**Task class / decision state:** `PLANNING_REVISION / EVIDENCE_REQUIRED`  
**Required independent review:** `W2-REV-01`

## 1. Scope and authority

This remediation preserves the useful W2-ENG-02 experiment protocol and closes two auditability defects before W2-ENG-03 executes any candidate:

1. the common workload is now an exact engine-neutral feature-slice/input manifest rather than intent-level prose; and
2. the equivalence/retry/reset truth cases are now executable deterministic fixtures rather than a Markdown-only assertion table.

The harness remains a **comparative experiment protocol**. It does not score or select an engine, does not become production game logic, does not authorize implementation readiness, and does not grant canonicality.

Candidate-specific physical representation is allowed only after a candidate binds the common slice through an `AdaptationManifest` that preserves or strengthens every required obligation and measurable bound.

## 2. Frozen engine-neutral feature slice

`W2-ENG-FEATURE-SLICE-v2` is synthetic planning input. It fixes **logical work**, not engine-specific scene files, component APIs, serialization formats, profiler formats, or build-system syntax.

```yaml
feature_slice_id: W2-ENG-FEATURE-SLICE-v2
logical_state:
  entity_count: 32
  world_width: 16
  world_height: 16
  fields_per_entity: [entity_id, x, y, status, flags]
  seed: 424242
  normal_ticks: 600
action_vocabulary:
  - MOVE_NORTH
  - MOVE_SOUTH
  - MOVE_EAST
  - MOVE_WEST
  - INTERACT
  - OPEN_MENU
  - CONFIRM
  - CANCEL
  - SAVE
  - LOAD
player_surface:
  screen_ids: [BOOT_OR_MAIN, PLAY_SURFACE, SETTINGS]
  required_routes:
    - BOOT_OR_MAIN->PLAY_SURFACE
    - PLAY_SURFACE->SETTINGS
    - SETTINGS->PLAY_SURFACE
  input_classes:
    - PRIMARY_POINTER_OR_KEYBOARD
    - CONTROLLER_OR_EQUIVALENT_SEMANTIC_ROUTE
assets:
  logical_asset_ids: [ASSET-01, ASSET-02, ASSET-03, ASSET-04, ASSET-05, ASSET-06, ASSET-07, ASSET-08]
  required_asset_count: 8
  broken_reference_asset_id: ASSET-08
save_schema:
  v1_fields: [schema_version, seed, tick, entities, settings]
  v2_added_field: world_flags
  v2_default: {}
  malformed_fixture_id: SAVE-MALFORMED-UNSUPPORTED-v2
merge_fixture:
  branch_a_nonoverlap_changes: 1
  branch_b_nonoverlap_changes: 1
  semantic_overlap_locations:
    - STATE:entity-07.status
    - UI:SETTINGS.control-02.label
  required_overlap_count: 2
  generated_collision_required_when_candidate_has_generated_metadata: true
capture_fixture:
  logical_state_marker: CAPTURE-STATE-042
  viewport_width: 1280
  viewport_height: 720
  required_frame_count: 1
profiling_fixture:
  normal_logical_updates: 19200
  hotspot_extra_updates: 3200
  hotspot_id: HOTSPOT-ENTITY-UPDATE-v2
package_fixture:
  target_id: WINDOWS_X64_DEV_PACKAGE-v1
  required_entry_surface: BOOT_OR_MAIN
  required_screen_count: 3
  store_signing_required: false
  clean_extract_launch_required: true
continuation_fixture:
  partial_state_id: CONT-PARTIAL-v2
  remaining_action_ids: [CONT-A1, CONT-A2, CONT-A3]
  required_handoff_fields:
    - branch
    - head_sha
    - attempt_refs
    - failure_refs
    - remaining_actions
    - commands
    - next_acceptance_step
  negative_missing_field: next_acceptance_step
```

Canonical feature-slice digest: `sha256:9a25209da5cf037f84955a834f4e8bda5b1e1de8085ee9fc4a07679f194699d2`.

### 2.1 What a candidate may translate

A candidate may represent the common slice using native concepts: scenes, entities, nodes, resources, prefabs, ECS data, C# objects, Rust components, engine-native saves, build targets, or profiler adapters.

It may **not** reduce the common logical obligations because its native representation is inconvenient. Examples of illegal weakening include:

- fewer than 32 logical entities for a scenario whose bound is 32;
- fewer than eight logical assets when the scenario binds the asset fixture;
- replacing the ten-action S3 deterministic input vocabulary with a smaller synthetic input;
- replacing the two exact S5 semantic overlap locations with disjoint edits;
- replacing the common S9 Windows x64 development package with an easier candidate-native target;
- giving S10 a richer hidden handoff context than the frozen partial-state fixture.

Additional evidence or larger work is allowed only when it does not change the common acceptance rule or resource-parity class.

## 3. Common start and resource profile

Every normal attempt starts from:

```yaml
profile_id: W2-ENG-START-COLD-v2
cache_mode: COLD
generated_state_policy: REGENERATE_FROM_REPO
resource_class: W2-ENG-HOST-COMMON-v2
```

The exact physical host/container image, CPU/RAM/storage cap, OS build, and toolchain installation record are bound by W2-ENG-03 before execution and must be identical or explicitly unresolved for all candidates in a comparison cohort.

An attempt that secretly uses warm caches, hidden generated state, undeclared manual preparation, or a stronger resource class is not comparable. A declared resource exception is visible evidence but remains `INCONCLUSIVE` for the common comparison until the cohort is rebalanced.

## 4. Scenario contracts with exact common input refs

The following logical refs resolve to §2 and to the executable fixture:

- `SLICE:logical_state`
- `SLICE:action_vocabulary`
- `SLICE:player_surface`
- `SLICE:assets`
- `SLICE:save_schema`
- `SLICE:merge_fixture`
- `SLICE:capture_fixture`
- `SLICE:profiling_fixture`
- `SLICE:package_fixture`
- `SLICE:continuation_fixture`

| Scenario | Common fixed input refs | Required obligations | Measurable lower bounds / exact authority |
|---|---|---|---|
| `S1` clean bootstrap/build | state, actions, surface, assets | clean reconstruct; build; launch; cold start; incremental observation | 32 entities; 8 assets; 3 screens; `FI-S1-CACHE-MISS-v2` |
| `S2` editor-independent bounded change | state, actions, surface, assets | fresh-agent change; visible/state-visible change; reviewable diff; automated verification | 32 entities; 8 assets; 3 screens; >=1 changed logical location; `FI-S2-STALE-META-v2` |
| `S3` shared-kernel deterministic evidence | state, actions | real/shared production rules; exact seed/input; repeatable state/events; perturbation distinguishable | 32 entities; 600 ticks; 10 actions; mechanism authority exactly `REAL_OR_SHARED_RULES`; `FI-S3-INPUT-PERTURB-v2` |
| `S4` save/load/schema evolution | state, save | round trip; schema evolution; explicit migration; malformed tuple diagnostic | 32 entities; 5 v1 fields; >=1 v2 added field; `FI-S4-INCOMPAT-TUPLE-v2` |
| `S5` parallel change/merge | state, surface, merge | parallel non-overlap; intentional overlap; visible conflict; post-merge checks | exact two semantic overlap locations; >=1 non-overlap per branch; `FI-S5-OVERLAP-v2` |
| `S6` controlled player-surface capture | state, surface, capture | reach known state; identity-bound capture; state-vs-capture failure separated | 3 screens; >=1 frame; 1280×720 common capture surface; `FI-S6-CAPTURE-DOWN-v2` |
| `S7` malformed project/asset recovery | assets, state | broken-reference injection; repo/CLI diagnosis; bounded repair; rerun | 8 assets; exactly identified `ASSET-08` broken-ref fixture; `FI-S7-BROKEN-REF-v2` |
| `S8` observability/profiling | state, profile | representative workload; parseable profile; locate injected hotspot; resource observations | 19,200 logical updates + 3,200 injected hotspot updates; `FI-S8-HOTSPOT-v2` |
| `S9` packaging | state, surface, assets, package | common package target; exact repro inputs; clean-extract launch; typed package failure | 3 screens; 8 assets; target exactly `WINDOWS_X64_DEV_PACKAGE-v1`; `FI-S9-PACKAGE-CONFIG-v2` |
| `S10` fresh-agent continuation | continuation, state, surface | repo-only handoff; fresh-context reconstruct; complete remaining actions; rerun evidence | exactly 3 remaining action IDs; 7 required handoff fields; hidden context forbidden; `FI-S10-HANDOFF-GAP-v2` |

Canonical scenario-manifest digest: `sha256:be4f1ca72f4861325783f8975101314823648977549ddf281b73fb5a64e389eb`.

## 5. AdaptationManifest v2

Before any candidate scenario execution, the candidate publishes an exact adaptation object:

```yaml
AdaptationManifest:
  candidate_id: <exact>
  scenario_id: S1..S10
  harness_id: W2-ENG-HARNESS-v2
  feature_slice_id: W2-ENG-FEATURE-SLICE-v2
  fixed_input_refs: [<all common refs for scenario>]
  mappings:
    <required obligation>: EQUIVALENT | STRICTLY_STRONGER
  bounds:
    <scenario metric>: <candidate value>
  failure_injections: [<all required scenario injection ids>]
  start_profile:
    cache_mode: COLD
    generated_state_policy: REGENERATE_FROM_REPO
    resource_class: W2-ENG-HOST-COMMON-v2
  resource_exception: false
  undocumented_manual_intervention: false
  mechanism_authority: <S3 must be REAL_OR_SHARED_RULES>
  package_target: <S9 common target>
  hidden_context_transfer: false
  extra_evidence: []
```

### 5.1 Mechanical equivalence rule

The executable validator rejects an adaptation when any of these is true:

1. harness or feature-slice identity differs;
2. any required common input ref is absent;
3. any required obligation is absent or mapped below `EQUIVALENT`;
4. any bounded logical input/work metric is below the scenario minimum;
5. required failure injection is absent;
6. start state is not cold/repository-regenerated;
7. resource class is not the common class or an unresolved exception exists;
8. an undocumented manual intervention is required;
9. S3 uses an abstract simulator rather than real/shared production rules;
10. S9 replaces the common package target;
11. S10 transfers hidden context.

This replaces the v1 phrase “materially shrinks scenario scale/input” with explicit executable checks. A candidate may add evidence or candidate-native work without gaining weaker acceptance.

## 6. Attempt, reset, retry, and lineage policy

Every scenario uses at least two **normal** attempts under independently reset start states plus every required failure-injection attempt.

Each attempt retains:

```yaml
AttemptRecord:
  attempt_id: <stable>
  scenario_id: <S1..S10>
  candidate_id: <exact candidate>
  candidate_generation_id: <exact>
  kind: NORMAL | FAILURE_INJECTION
  normal_index: <1..n or null>
  injection_id: <exact or null>
  reset_id: <exact>
  resource_class: W2-ENG-HOST-COMMON-v2
  result: PASS | FAIL | FLAKY | INCONCLUSIVE | NOT_RUN
  artifact_refs: []
  diagnostics_refs: []
  manual_interventions: []
```

The attempt ledger also retains a run-registry reference set and an `all_attempt_refs` set. They must equal the retained attempt IDs. A missing failed attempt is `INCONCLUSIVE`, not a clean retry.

### 6.1 Aggregate semantics

- fewer than two normal attempts -> `NOT_RUN`;
- first two normal attempts not independently reset -> `INCONCLUSIVE`;
- non-common resource class -> `INCONCLUSIVE`;
- required failure-injection attempt absent -> `NOT_RUN`;
- normal PASS/FAIL disagreement -> `FLAKY`;
- any required injection recovery assertion fails -> `FAIL`;
- two normal PASS attempts + all required injection PASS -> `PASS_FOR_COMPARISON`;
- a failed candidate generation may be superseded by a new exact generation, but its historical attempts remain retained and may not be erased.

Retry is therefore evidence, not a laundering mechanism.

## 7. Scenario-specific authority limits preserved

### S3 hash authority

A deterministic hash/digest proves only exact identity of the declared normalized state/event object. It does not prove semantic correctness. S3 still requires at least one independent expected-state/invariant assertion and the input-perturbation fixture. An abstract simulator that does not execute the candidate's real/shared rules is rejected even if its hashes are stable.

### S9 platform scope

The common target is only `WINDOWS_X64_DEV_PACKAGE-v1` for cross-candidate packaging comparability. A candidate may additionally package other platforms as extra evidence. Later corrected platform requirements may add required target-specific probes in W2-ENG-03, but may not remove the common package obligation without a new harness version.

### S10 fresh context

The continuation agent receives only the exact repository/handoff evidence declared by `CONT-PARTIAL-v2`. Private chat context, hidden notes, prior-agent memory, or undisclosed local state is forbidden. The negative fixture omits `next_acceptance_step` and must fail closed.

## 8. Executable protocol fixture and deterministic evidence

The planning-only reference validator is:

`docs/planning/wave-2/evidence/engine-spike-protocol-fixtures.py`

It uses only the Python standard library and does not execute an engine. Its explicit semantic identity is content-addressed independently of source formatting.

- validator contract digest: `sha256:e533414f48080e3546f928576c1af5bb31de91d7f8e44ed433f3c2c51f158ee4`
- feature-slice digest: `sha256:9a25209da5cf037f84955a834f4e8bda5b1e1de8085ee9fc4a07679f194699d2`
- scenario-manifest digest: `sha256:be4f1ca72f4861325783f8975101314823648977549ddf281b73fb5a64e389eb`
- synthetic fixture-input digest: `sha256:022bd504f69b60c35ce1f037ac225b9bbf498159481fd3df6aee4e514dfeec01`
- deterministic result-object digest: `sha256:5cbb2a4443840ccb2e66b6b1336e6f18049436138c808d473773482828505ae4`

### 8.1 Equivalence fixture outcomes

| ID | Attack / adaptation | Expected | Executable result |
|---|---|---|---|
| EQ-01 | native S2 runner, obligations/bounds preserved | ACCEPT | ACCEPT |
| EQ-02 | omit S7 failure injection | REJECT | REJECT |
| EQ-03 | substitute abstract simulator for S3 | REJECT | REJECT |
| EQ-04 | native S6 capture + stronger identity evidence | ACCEPT | ACCEPT |
| EQ-05 | hidden warm/prebuilt S1 state | REJECT | REJECT |
| EQ-06 | candidate-native S8 profiler adapter preserving workload | ACCEPT | ACCEPT |
| EQ-07 | omit a known failed S9 attempt from retained ledger | REJECT | REJECT |
| EQ-08 | add extra S9 platform while retaining common package | ACCEPT | ACCEPT |
| EQ-09 | remove required S5 semantic overlap | REJECT | REJECT |
| EQ-10 | hide required S2 manual click as setup | REJECT | REJECT |
| EQ-11 | candidate-native S4 serialization preserving fixture/diagnostics | ACCEPT | ACCEPT |
| EQ-12 | pass S10 private hidden context | REJECT | REJECT |
| EQ-13 | shrink S3 common entity bound from 32 to 16 | REJECT | REJECT |
| EQ-14 | give S8 an undeclared stronger host class | REJECT | REJECT |
| EQ-15 | omit required S1 `launch` obligation mapping | REJECT | REJECT |

The original EQ-01…EQ-12 truth set remains 5 ACCEPT / 7 REJECT. The v2 additions are three explicit rejection cases for the review findings.

### 8.2 Aggregate fixture outcomes

| ID | Case | Result |
|---|---|---|
| AG-01 | two clean independently reset normal PASS + injection PASS | `PASS_FOR_COMPARISON` |
| AG-02 | normal attempts disagree PASS/FAIL | `FLAKY` |
| AG-03 | only one normal attempt | `NOT_RUN` |
| AG-04 | required failure-injection attempt missing | `NOT_RUN` |
| AG-05 | two normal attempts reuse same reset identity | `INCONCLUSIVE` |
| AG-06 | run registry contains a failed attempt missing from retained ledger | `INCONCLUSIVE` |

A change to the validator, feature slice, scenario manifest, fixture inputs, or result object requires new exact digests and re-execution before W2-ENG-03 may rely on it.

## 9. W2-ENG-03 execution packet

Before starting candidate work, W2-ENG-03 must freeze one comparison cohort record containing:

- `W2-ENG-HARNESS-v2` identity and the five digests in §8;
- exact admitted candidate set and corrected W2-ENG-01 provenance;
- exact current platform/accessibility provenance;
- physical common host/container resource profile behind `W2-ENG-HOST-COMMON-v2`;
- candidate-specific toolchain/account/plugin/terms baselines;
- exact candidate AdaptationManifest for every S1–S10 scenario;
- equivalence-validator PASS for every adaptation;
- run registry and reset strategy;
- exact manual-intervention recording policy;
- evidence output paths/retention policy.

If a candidate cannot satisfy a common bound because the engine's physical model differs, the candidate must either provide an equivalent/stronger translation that passes the validator or remain `INCONCLUSIVE` for that scenario. The common workload is not silently reduced.

## 10. Bias controls

| Bias/failure mode | Control |
|---|---|
| candidate gets a smaller/easier slice | common logical refs + executable minimum bounds |
| editor-heavy candidate gets prebuilt state | cold/repository-regenerated start profile |
| faster machine hides tooling cost | exact common resource class |
| failed retry disappears | run registry must equal retained ledger |
| candidate-specific failure mode omitted | required injection IDs bound by scenario |
| native representation excuses missing assertion | every obligation maps EQUIVALENT/STRICTLY_STRONGER |
| S3 simulator produces convenient hashes | real/shared-rules authority check |
| candidate packages an easier platform | common Windows x64 dev package retained |
| continuation uses private agent memory | hidden-context rejection + exact partial-state fixture |
| one aggregate score masks hard failure | scenario/attempt results retained separately; no scalar engine score |

## 11. Freshness and reopen conditions

Reopen/reversion the harness when:

- corrected W2-ENG-01 changes the admitted hypothesis set enough that a scenario no longer measures comparable decision information;
- platform/accessibility evidence requires a common scenario workload that cannot be represented by v2 without weakening or disproportionate engine-specific work;
- W2-ENG-03 finds that a common logical bound systematically favors/penalizes one architecture for a non-decision-relevant reason;
- executable fixture results/digests no longer reproduce;
- a validator defect allows one of the declared negative fixtures to ACCEPT;
- attempt registry/reset/resource evidence cannot be retained as specified;
- W2-REV-01 finds a BLOCKER/MAJOR against equivalence, input parity, retry lineage, or authority limits.

Any modified harness becomes a new exact version; evidence from incompatible harness versions is not silently pooled.

## 12. Remediation acceptance check

Against Issue #94:

- exact Issue #72 source provenance retained: **PASS**;
- one exact common feature slice exists before adaptation: **PASS**;
- every S1–S10 binds exact common input refs: **PASS**;
- measurable logical/workload bounds replace vague shrink language: **PASS**;
- candidate-native translations require explicit obligation/bound mapping: **PASS**;
- executable deterministic validator exists: **PASS**;
- original EQ-01…EQ-12 truth cases executable: **PASS**;
- smaller-workload attack rejected: **PASS**;
- stronger-resource attack rejected: **PASS**;
- omitted-obligation attack rejected: **PASS**;
- failed-attempt omission rejected: **PASS**;
- hidden warm state rejected: **PASS**;
- omitted failure injection rejected: **PASS**;
- abstract S3 substitution rejected: **PASS**;
- hidden S10 context rejected: **PASS**;
- retry/reset aggregate outcomes executable: **PASS**;
- validator and results content-addressed: **PASS**;
- no engine execution/scoring/selection authority: **PASS**;
- formal independent review remains `W2-REV-01`: **PASS**.

**Producer remediation disposition:** `REVIEW_READY_CANDIDATE / EVIDENCE_REQUIRED`. This v2 packet may supersede the frozen Issue #72 harness as the substantive W2-ENG-02 input to W2-ENG-03 once terminal provenance is bound; it is not an engine decision or implementation artifact.
