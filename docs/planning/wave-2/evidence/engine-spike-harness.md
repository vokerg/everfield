# W2-REM-ENG-03 — Engine spike harness v3

**Source mission:** `W2-ENG-02` / Issue #72  
**Prior remediation:** `W2-REM-ENG-02` / Issue #94  
**Current remediation:** `W2-REM-ENG-03` / Issue #104  
**Frozen Issue #94 head:** `cad3c4b546ae929668d708e6f89b58d9e0817dfb`  
**Frozen Issue #94 substantive work:** `f7e3bace17046c164751d708b0711302c2a68f5c`  
**Frozen v2.1 harness blob:** `de47169cb0647d783428514e641875d5418ae027`  
**Frozen v2.1 validator blob:** `e9699ad7d02e1d99fac6d9f41545bf9eeabe5d37`  
**Independent pre-gate review:** Issue #103 `STATUS(REVIEW_READY)` comment `5276155477`  
**Frozen review work/head:** `9fb365e2ad84c04d2e12305b38b40ddc30153530` / `00331d3cc9cbe29fa20f27be159b5730e3f3b142`  
**Review findings:** `PG-REM-HARNESS-M01`, `PG-REM-HARNESS-M02`  
**Remediation base:** `main@c7ba185ed9667b717794c19eaa0834ca41aa4c78`  
**Harness ID:** `W2-ENG-HARNESS-v3`  
**Feature slice ID:** `W2-ENG-FEATURE-SLICE-v2`  
**Scenario manifest ID:** `W2-ENG-SCENARIO-INPUTS-v2`  
**Validator ID:** `W2-ENG-PROTOCOL-VALIDATOR-v3`  
**Required formal review:** `W2-REV-01`

## 1. Scope, non-goals, and authority

This bounded remediation changes only attempt-envelope and failure-injection identity authority. It preserves the engine-neutral feature slice, S1–S10 common-input/equivalence contract, reset/workspace/resource rules, immutable repair-generation lineage, S3/S9/S10 authority limits, and all existing v2.1 truth classes.

It closes three fail-closed gaps:

1. duplicate `injection_id` values can no longer overwrite a retained failed required injection;
2. every retained attempt must bind the enclosing generation `candidate_id`; and
3. `result × failure_class` is a closed validity matrix, so malformed pairs cannot reach aggregate comparison authority.

The validator remains `PLANNING_EXPERIMENT` evidence. This packet does **not** execute, score, rank, or select an engine; authorize production/gameplay implementation or implementation readiness; turn hashes into semantic-correctness authority; create release/platform certification; replace `W2-REV-01`; or authorize integration, verification, or canonicalization.

## 2. Preserved engine-neutral `FeatureSliceContract`

The logical feature slice is unchanged from v2.1 and therefore retains the exact semantic digest `sha256:9a2523c4870146b09233397f3773f7a27b1e0135c24a6767d16e34a791aab104`.

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

Candidate-native scenes/nodes/components/resources/saves/profilers/build targets may vary only through an explicit adaptation. The common logical work cannot shrink.

## 3. Preserved `ScenarioInputManifest`

The S1–S10 manifest is semantically unchanged from v2.1 and retains digest `sha256:be4d7473b01da6b428cd5f3be48de083abd161a4899471303f3ccfeef45c725f`.

Exact common refs are `SLICE:logical_state`, `SLICE:action_vocabulary`, `SLICE:player_surface`, `SLICE:assets`, `SLICE:save_schema`, `SLICE:merge_fixture`, `SLICE:capture_fixture`, `SLICE:profiling_fixture`, `SLICE:package_fixture`, and `SLICE:continuation_fixture`.

| Scenario | Exact fixed input refs | Minimum mechanical bounds | Required injection |
|---|---|---|---|
| S1 bootstrap/build | logical_state, action_vocabulary, player_surface, assets | 32 entities; 8 assets; 3 screens | `FI-S1-CACHE-MISS-v2` |
| S2 bounded change | logical_state, action_vocabulary, player_surface, assets | 32 entities; 8 assets; 3 screens; >=1 changed logical location | `FI-S2-STALE-META-v2` |
| S3 deterministic evidence | logical_state, action_vocabulary | 32 entities; 600 ticks; 10 actions; `REAL_OR_SHARED_RULES` | `FI-S3-INPUT-PERTURB-v2` |
| S4 save/schema | logical_state, save_schema | 32 entities; 5 v1 fields; >=1 v2 field | `FI-S4-INCOMPAT-TUPLE-v2` |
| S5 parallel merge | logical_state, player_surface, merge_fixture | exact 2 semantic overlaps; >=1 non-overlap each branch | `FI-S5-OVERLAP-v2` |
| S6 capture | logical_state, player_surface, capture_fixture | 3 screens; >=1 frame; 1280×720 | `FI-S6-CAPTURE-DOWN-v2` |
| S7 malformed asset | assets, logical_state | 8 assets; exact broken `ASSET-08` | `FI-S7-BROKEN-REF-v2` |
| S8 profiling | logical_state, profiling_fixture | 19,200 normal + 3,200 hotspot updates | `FI-S8-HOTSPOT-v2` |
| S9 packaging | logical_state, player_surface, assets, package_fixture | 3 screens; 8 assets; `WINDOWS_X64_DEV_PACKAGE-v1` | `FI-S9-PACKAGE-CONFIG-v2` |
| S10 continuation | continuation_fixture, logical_state, player_surface | 3 remaining actions; 7 handoff fields; no hidden context | `FI-S10-HANDOFF-GAP-v2` |

The executable `SCENARIOS` object remains the closed obligation set. Missing refs/obligations, smaller bounds, missing injections, hidden prewarm, stronger resource classes, hidden manual intervention, abstract S3 substitution, S9 package substitution, and hidden S10 context remain rejected.

## 4. Candidate adaptation contract

Every candidate/scenario must publish:

```yaml
AdaptationManifest:
  candidate_id: <exact>
  scenario_id: S1..S10
  harness_id: W2-ENG-HARNESS-v3
  feature_slice_id: W2-ENG-FEATURE-SLICE-v2
  fixed_input_refs: [<all required common refs>]
  mappings:
    <every required obligation>: EQUIVALENT | STRICTLY_STRONGER
  bounds:
    <every scenario minimum>: <candidate value>
  failure_injections: [<every required injection>]
  start_profile:
    cache_mode: COLD
    generated_state_policy: REGENERATE_FROM_REPO
    resource_class: W2-ENG-HOST-COMMON-v2
  resource_exception: false
  undocumented_manual_intervention: false
  mechanism_authority: <S3 REAL_OR_SHARED_RULES>
  package_target: <S9 WINDOWS_X64_DEV_PACKAGE-v1>
  hidden_context_transfer: false
  extra_evidence: []
```

Additional evidence is allowed only if it does not weaken common acceptance or resource parity.

## 5. Attempt identity and closed envelope

Each retained attempt binds:

```yaml
AttemptRecord:
  attempt_id: <stable>
  scenario_id: <S1..S10>
  candidate_id: <exact enclosing generation candidate>
  candidate_generation_id: <exact>
  kind: NORMAL | FAILURE_INJECTION
  normal_index: <integer-or-null>
  injection_id: <exact-or-null>
  result: PASS | FAIL | INCONCLUSIVE | NOT_RUN
  failure_class: NONE | PRODUCT | INFRA | HARNESS | UNKNOWN
  reset_id: <exact>
  reset_verified: true | false
  workspace_id: <exact>
  resource_class: W2-ENG-HOST-COMMON-v2
```

The enclosing generation binds exact `candidate_id`, `candidate_work_id`, optional predecessor generation, repair-change ref, run-registry set, and retained-attempt set.

Before any outcome aggregation, v3 validates all of the following:

- `run_registry_refs == all_attempt_refs == attempts.keys()`;
- `AttemptRecord.attempt_id` equals its map key;
- every attempt `scenario_id == generation.scenario_id`;
- every attempt `candidate_generation_id == generation.generation_id`;
- **every attempt `candidate_id == generation.candidate_id`**;
- NORMAL attempts have no `injection_id`;
- FAILURE_INJECTION attempts have a nonempty `injection_id`;
- every result/failure-class pair is in the closed matrix below.

Closed matrix:

| Result | Allowed failure classes |
|---|---|
| `PASS` | `NONE` |
| `FAIL` | `PRODUCT`, `INFRA`, `HARNESS`, `UNKNOWN` |
| `INCONCLUSIVE` | `PRODUCT`, `INFRA`, `HARNESS`, `UNKNOWN` |
| `NOT_RUN` | `NONE` |

Any unlisted pair is structurally invalid and returns `INCONCLUSIVE` with `valid_envelope=false`. In particular, `PASS + PRODUCT` cannot contribute comparison authority.

## 6. Required-injection uniqueness and no laundering

For every generation, v3 groups all retained FAILURE_INJECTION attempts by `injection_id` **before** creating the required-injection lookup.

Rules:

1. every FAILURE_INJECTION attempt must have exactly one nonempty `injection_id`;
2. an `injection_id` may occur only once in the generation;
3. each scenario-required injection ID must therefore resolve to exactly one retained attempt;
4. any duplicate ID is an invalid envelope and returns `INCONCLUSIVE` before result authority is computed; and
5. no retained failed injection can be hidden by dictionary overwrite, retry ordering, or a later duplicate PASS.

This is deliberately stricter than v2.1. A fresh v3 negative keeps both a PRODUCT FAIL and a later PASS under `FI-S1-CACHE-MISS-v2`; because the ID is duplicated, the generation is non-comparable rather than `PASS_FOR_COMPARISON`.

## 7. Aggregate semantics preserved

After structural validity:

- fewer than two normal attempts -> `NOT_RUN`;
- unverified/reused reset or workspace -> `NOT_RUN`;
- non-common resource class -> `INCONCLUSIVE`;
- required injection absent -> `NOT_RUN`;
- any used INFRA/HARNESS/UNKNOWN failure class -> `INCONCLUSIVE`;
- normal PASS/FAIL disagreement, including PASS/FAIL/PASS -> `FLAKY`;
- required injection result other than PASS -> `FAIL` unless a prior structural/non-product ambiguity already failed closed;
- all normal attempts FAIL product behavior -> `FAIL`;
- all normal attempts PASS plus all required injection attempts PASS -> `PASS_FOR_COMPARISON`;
- explicit harness defect -> `INCONCLUSIVE` and `reopen_scope=ALL_CANDIDATES_FOR_SCENARIO`.

A prior failed/flaky/inconclusive generation remains immutable evidence after repair.

## 8. Repair-generation lineage

A repaired product state is a new generation. A valid successor must:

1. use a new generation ID;
2. reference the exact predecessor generation;
3. use a changed `candidate_work_id`;
4. bind an exact `repair_change_ref`; and
5. preserve the same `candidate_id` unless a future separately typed candidate-transition protocol explicitly authorizes a change.

The v3 history validator rejects generation-ID reuse, missing/wrong predecessor linkage, same-work repair masquerade, and cross-candidate generation substitution. `FAIL(g1) -> PASS(g2)` remains valid only as two retained records for the same candidate with changed work.

## 9. Executable evidence and exact digests

Executable artifact: `docs/planning/wave-2/evidence/engine-spike-protocol-fixtures.py`.

The Issue #104 episode syntax-compiled and executed the standard-library-only validator. All embedded assertions passed.

Exact v3 identities:

- validator source bytes: `sha256:306285bed232161d63ba52330f785e2bcaab00cd3b574d65fc584fc56a0132d7`
- validator contract: `sha256:357e25f9af9ac71804f322797c3ea1aa0c923167178b9c2eb8c84ef3280cbe23`
- feature slice: `sha256:9a2523c4870146b09233397f3773f7a27b1e0135c24a6767d16e34a791aab104`
- scenario manifest: `sha256:be4d7473b01da6b428cd5f3be48de083abd161a4899471303f3ccfeef45c725f`
- fixture inputs: `sha256:3172768f6288135c4b99dfd802882a5394b709b3fa0f74688bd17106a6b3c8ff`
- result object: `sha256:d79120f698bd9409bc6956162216a36a85f62592f4eff5db39b6fdc288149029`

A code/contract/fixture/result change requires re-execution and new digests.

### 9.1 Preserved equivalence fixtures

EQ-01…EQ-15 retain the exact v2.1 outcomes: 5 ACCEPT / 10 REJECT. The common-slice anti-shrink tests still reject missing injection, abstract S3, hidden warm state, failed-attempt omission, overlap shrink, hidden manual intervention, hidden S10 context, smaller S3 entity bound, stronger host, and missing S1 launch obligation.

### 9.2 Preserved aggregate/history fixtures

The v2.1 outcomes remain unchanged:

| Fixture | v3 result |
|---|---|
| AG-01 clean PASS/PASS + injection PASS | `PASS_FOR_COMPARISON` |
| AG-02 PASS/FAIL | `FLAKY` |
| AG-03 one normal | `NOT_RUN` |
| AG-04 missing injection | `NOT_RUN` |
| AG-05 reused reset | `NOT_RUN` |
| AG-06 omitted retained failed run | `INCONCLUSIVE` |
| AG-07 INFRA fail then PASS | `INCONCLUSIVE` |
| AG-08 required injection FAIL | `FAIL` |
| AG-09 harness defect | `INCONCLUSIVE` + all-candidate reopen |
| AG-10 unverified reset | `NOT_RUN` |
| AG-11 reused workspace | `NOT_RUN` |
| AG-12 stronger resource | `INCONCLUSIVE` |
| AG-13 PASS/FAIL/PASS | `FLAKY` |
| HIST-01 linked repair | `GEN-1=FAIL`, `GEN-2=PASS_FOR_COMPARISON` |
| HIST-02 generation reuse | invalid |
| HIST-03 missing predecessor | invalid |
| HIST-04 same-work repair | invalid |

### 9.3 New Issue #104 attacks

| Fixture | Attack | v3 result |
|---|---|---|
| AG-14 | retained required-injection PRODUCT FAIL + duplicate PASS with same `injection_id` | `INCONCLUSIVE`, `valid_envelope=false` |
| AG-15 | one normal attempt belongs to another candidate | `INCONCLUSIVE`, `valid_envelope=false` |
| AG-16 | required injection belongs to another candidate | `INCONCLUSIVE`, `valid_envelope=false` |
| AG-17 | `PASS` attempt mislabeled `failure_class=PRODUCT` | `INCONCLUSIVE`, `valid_envelope=false` |
| HIST-05 | repair generation switches candidate identity without typed transition | invalid |

These cases reproduce the Issue #103 attack paths and close them mechanically.

## 10. W2-ENG-03 execution packet

Before any candidate execution, W2-ENG-03 must freeze:

- this exact v3 harness/validator identity and five semantic digests plus validator source identity;
- corrected W2-ENG-01 admission provenance;
- exact platform/accessibility provenance;
- common physical host/container resource profile;
- exact toolchain/account/plugin/terms baselines;
- one adaptation manifest per candidate/scenario;
- validator ACCEPT for every adaptation;
- exact candidate identity for every generation and attempt;
- run registry, reset verification, workspace lineage, and evidence-retention policy;
- one unique attempt per required injection ID;
- manual-intervention policy; and
- exact repair-generation lineage.

A candidate unable to preserve a common bound is `INCONCLUSIVE` unless an equivalent/stronger mapping passes the exact validator. The workload is never silently reduced.

## 11. Scenario authority limits preserved

**S3:** state/event hashes prove declared object identity only, not semantic correctness. `REAL_OR_SHARED_RULES`, expected-state/invariant assertions, and perturbation evidence remain required.

**S9:** `WINDOWS_X64_DEV_PACKAGE-v1` is a common comparison package, not a release commitment. Platform changes reopen applicability rather than silently removing the common package obligation.

**S10:** continuation receives only repository/GitHub/handoff evidence from the frozen partial-state fixture. Private chat, hidden notes, unrecorded memory, and undisclosed local state invalidate clean comparison authority.

**Manual intervention:** intervention remains evidence and cannot be renamed setup; automation is acceptable only when invokable, inspectable, and fully recorded.

## 12. Failure controls

| Failure mode | Control |
|---|---|
| easier candidate-specific slice | frozen common refs + lower bounds |
| candidate-native mechanism drops assertion | closed obligation mappings |
| hidden warm/editor state | cold/repository-regenerated start profile |
| reset reuses mutated workspace | exact reset/workspace identities + verification |
| stronger machine hides tooling cost | common resource class |
| failed retry disappears | registry/retained-set equality |
| duplicate injection launders failure | unique `injection_id` validation before lookup |
| candidate B evidence credited to candidate A | attempt `candidate_id == generation.candidate_id` |
| malformed PASS/failure label survives | closed result/failure-class matrix |
| repair rewrites old failure | immutable linked generations + changed work |
| repair silently switches candidate | same candidate identity across history absent typed transition |
| harness defect benefits one candidate | all-candidate scenario reopen |
| S3 proxy produces convenient hashes | `REAL_OR_SHARED_RULES` authority |
| candidate packages easier target | exact common package target |
| continuation uses private memory | hidden-context rejection |
| one score hides hard failures | scenario/generation/attempt evidence retained; no scalar score |

## 13. Evidence, inference, assumptions, and reopen conditions

**Observed evidence:** exact frozen v2.1 bytes, exact Issue #103 review bytes, executable v3 fixtures, and deterministic digest output.

**Inference:** rejecting structurally ambiguous duplicate/cross-candidate/malformed attempt envelopes as non-comparable is the smallest correction consistent with the foundation rule that EvidenceSatisfaction is derived from exact evidence identity rather than asserted.

**Assumption:** the same candidate identity is expected across repair generations; no current authoritative packet defines a typed candidate-transition rule inside one history. A future reviewed protocol may introduce one explicitly, but v3 does not infer it.

Reopen/version this harness if any v3 negative fixture accepts, any published digest stops reproducing, attempt/reset/resource/history evidence cannot be retained, a later typed candidate-transition protocol changes history semantics, platform/accessibility evidence invalidates the common slice, or `W2-REV-01` finds a BLOCKER/MAJOR.

## 14. Finding disposition and bounded self-review

- `PG-REM-HARNESS-M01`: **RESOLVED** — duplicate required-injection IDs fail closed before lookup/result authority; retained FAIL + duplicate PASS is executable AG-14.
- `PG-REM-HARNESS-M02`: **RESOLVED** — every attempt candidate binds to generation candidate; normal and injection substitutions are executable AG-15/AG-16; history candidate substitution is HIST-05.
- Issue #103 additional envelope observation: **RESOLVED** — closed result/failure-class matrix; malformed `PASS + PRODUCT` is executable AG-17.
- prior common-slice/equivalence/reset/resource/repair semantics: **NO REGRESSION FOUND** — all prior asserted fixtures reproduce their original truth classes.

Final bounded self-review: **0 unresolved BLOCKER / 0 unresolved MAJOR / 0 correction-requiring MINOR**.

Disposition: `REVIEW_READY_CANDIDATE / EVIDENCE_REQUIRED`. This packet may supersede Issue #94 only as the substantive W2-ENG-02 remediation input once Issue #104 publishes exact terminal provenance. Formal aggregate `W2-REV-01` remains the authority gate.
