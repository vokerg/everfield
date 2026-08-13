# W2-REM-ENG-02 — Engine spike harness v2.1

**Source mission:** `W2-ENG-02` / Issue #72  
**Remediation mission:** `W2-REM-ENG-02` / Issue #94  
**Frozen source head/work:** `af914fa147f22af1f544f7cdeb07a5e4234c9f8c`  
**Frozen source harness blob:** `da29b1b867f01f0efaeda28616f4f5dc329ee2c9`  
**Frozen source handoff blob:** `3857e514f786b404c1c6948bdf7b3ed68c168920`  
**Source terminal status:** Issue #72 comment `5255039768`  
**Independent pre-gate review:** Issue #72 comment `5270974506`  
**Remediation base:** `main@c7ba185ed9667b717794c19eaa0834ca41aa4c78`  
**Harness ID:** `W2-ENG-HARNESS-v2.1`  
**Feature slice ID:** `W2-ENG-FEATURE-SLICE-v2`  
**Scenario manifest ID:** `W2-ENG-SCENARIO-INPUTS-v2`  
**Validator ID:** `W2-ENG-PROTOCOL-VALIDATOR-v2.1`  
**Required formal review:** `W2-REV-01`

## 1. Scope, status, and authority

This bounded remediation closes the W2-ENG-02 pre-gate defects without executing, ranking, or selecting an engine.

It changes the evidence protocol in three ways:

1. one exact engine-neutral feature slice and scenario-input manifest exist before candidate adaptation;
2. candidate-native adaptation is accepted only through explicit common-ref, obligation, lower-bound, resource, failure-injection, package, and context checks; and
3. equivalence plus attempt/reset/retry/repair-generation semantics are executable and content-addressed.

The validator is `PLANNING_EXPERIMENT` evidence only. Neither this document nor the validator is production game logic, implementation readiness, engine-selection authority, release authority, formal `W2-REV-01`, verification, integration, or canonicalization.

## 2. Frozen engine-neutral `FeatureSliceContract`

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

Semantic digest: `sha256:9a2523c4870146b09233397f3773f7a27b1e0135c24a6767d16e34a791aab104`.

Physical engine representation is candidate-native. Logical work is not. An engine may translate scenes/nodes/components/resources/saves/profilers/build targets, but may not reduce common entity, asset, state, action, UI, conflict, workload, package, or continuation obligations to obtain an easier comparison.

## 3. `ScenarioInputManifest`

Exact common refs:

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

| Scenario | Exact fixed input refs | Minimum mechanical bounds | Required injection |
|---|---|---|---|
| S1 bootstrap/build | logical_state, action_vocabulary, player_surface, assets | 32 entities; 8 assets; 3 screens | `FI-S1-CACHE-MISS-v2` |
| S2 bounded change | logical_state, action_vocabulary, player_surface, assets | 32 entities; 8 assets; 3 screens; >=1 changed logical location | `FI-S2-STALE-META-v2` |
| S3 deterministic evidence | logical_state, action_vocabulary | 32 entities; 600 ticks; 10 actions; `REAL_OR_SHARED_RULES` | `FI-S3-INPUT-PERTURB-v2` |
| S4 save/schema | logical_state, save_schema | 32 entities; 5 v1 fields; >=1 v2 field | `FI-S4-INCOMPAT-TUPLE-v2` |
| S5 parallel merge | logical_state, player_surface, merge_fixture | exact 2 semantic overlaps; >=1 non-overlap each branch | `FI-S5-OVERLAP-v2` |
| S6 capture | logical_state, player_surface, capture_fixture | 3 screens; >=1 frame; 1280×720 | `FI-S6-CAPTURE-DOWN-v2` |
| S7 malformed asset | assets, logical_state | 8 assets; exact broken `ASSET-08` fixture | `FI-S7-BROKEN-REF-v2` |
| S8 profiling | logical_state, profiling_fixture | 19,200 normal + 3,200 hotspot updates | `FI-S8-HOTSPOT-v2` |
| S9 packaging | logical_state, player_surface, assets, package_fixture | 3 screens; 8 assets; exact `WINDOWS_X64_DEV_PACKAGE-v1` | `FI-S9-PACKAGE-CONFIG-v2` |
| S10 continuation | continuation_fixture, logical_state, player_surface | 3 remaining actions; 7 handoff fields; no hidden context | `FI-S10-HANDOFF-GAP-v2` |

Every row also has a closed obligation set in the executable `SCENARIOS` object. A missing obligation mapping is rejection. Semantic digest: `sha256:be4d7473b01da6b428cd5f3be48de083abd161a4899471303f3ccfeef45c725f`.

## 4. Candidate adaptation and equivalence

Each candidate/scenario publishes:

```yaml
AdaptationManifest:
  candidate_id: <exact>
  scenario_id: S1..S10
  harness_id: W2-ENG-HARNESS-v2.1
  feature_slice_id: W2-ENG-FEATURE-SLICE-v2
  fixed_input_refs: [<all required common refs>]
  mappings:
    <every required obligation>: EQUIVALENT | STRICTLY_STRONGER
  bounds:
    <every declared scenario minimum>: <candidate value>
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

The executable validator rejects missing common refs, missing/weaker obligations, shrunk numeric bounds, missing injections, hidden/warm start state, stronger/different resource class, unresolved resource exceptions, hidden manual intervention, abstract S3 substitution, S9 package substitution, and hidden S10 context.

Extra evidence or larger work is permitted only if common acceptance and resource parity are unchanged.

## 5. Start state, attempt identity, and immutable lineage

Common normal start profile:

```yaml
profile_id: W2-ENG-START-COLD-v2
cache_mode: COLD
generated_state_policy: REGENERATE_FROM_REPO
resource_class: W2-ENG-HOST-COMMON-v2
```

W2-ENG-03 must bind the exact physical host/container/toolchain profile behind that logical class before runs and use one comparison-cohort rule.

Each executable attempt record binds:

```yaml
AttemptRecord:
  attempt_id: <stable>
  scenario_id: <S1..S10>
  candidate_id: <exact>
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

The generation object additionally binds `candidate_work_id`, optional predecessor generation, exact repair-change reference, the run-registry set, and the retained-attempt set.

Mechanical invariants:

- run registry == retained attempt IDs == `all_attempt_refs`;
- every attempt's generation/scenario/identity matches the generation object;
- at least two normal attempts are required;
- the first two normal attempts require distinct reset IDs, distinct workspaces, and verified resets;
- every required failure-injection attempt is retained;
- every attempt uses the common resource class for a comparable result;
- failed/flaky/inconclusive attempts remain in history after repair.

An omitted historical failed attempt is `INCONCLUSIVE`; it can never become a clean PASS by retry.

## 6. Aggregate and repair-generation semantics

For one immutable generation:

- `<2` normal attempts → `NOT_RUN`;
- unverified/reused reset or workspace → `NOT_RUN`;
- stronger/different resource class → `INCONCLUSIVE`;
- required injection absent → `NOT_RUN`;
- any INFRA/HARNESS/UNKNOWN failure classification → `INCONCLUSIVE`;
- normal PASS/FAIL disagreement, including a PASS/FAIL/PASS adjudication sequence → `FLAKY`;
- required recovery injection failure → `FAIL`;
- all normal attempts FAIL product behavior → `FAIL`;
- all normal attempts PASS plus required injection PASS → `PASS_FOR_COMPARISON`;
- explicit harness defect → `INCONCLUSIVE` and `reopen_scope=ALL_CANDIDATES_FOR_SCENARIO`.

A repaired product state is a **new generation**, not a rewrite. A valid successor must:

1. use a new generation ID;
2. point to the exact predecessor generation;
3. use a changed candidate-work identity; and
4. bind an exact repair-change ref.

The validator rejects generation-ID reuse, missing/wrong predecessor linkage, or a “repair” that keeps the same work identity. Thus `FAIL(g1) -> PASS(g2)` is allowed only as two retained records; `g1` is never rewritten to PASS.

## 7. Scenario-specific authority limits

**S3:** state/event hashes prove declared object identity only. They do not prove semantic correctness. Real/shared rules plus expected-state/invariant assertions and the perturbation fixture remain required; an abstract simulator is rejected.

**S9:** `WINDOWS_X64_DEV_PACKAGE-v1` is the common comparison package, not a final release-platform commitment. Corrected platform/accessibility evidence may add probes; it may not silently remove the common package obligation. Platform changes reopen applicability.

**S10:** continuation receives only repository/GitHub/handoff evidence from the frozen partial-state fixture. Private chat, hidden notes, unrecorded memory, or undisclosed local state rejects a clean comparison claim.

**Manual intervention:** intervention remains evidence and cannot be renamed setup. Candidate-native/editor automation is allowed only when invokable/inspectable and fully recorded.

## 8. Executable evidence

Executable artifact:

`docs/planning/wave-2/evidence/engine-spike-protocol-fixtures.py`

The continuation episode executed it locally with Python 3 standard library only. All embedded assertions passed.

Content-addressed semantic evidence:

- validator contract: `sha256:48bd4df89b653699f5ae94db267b14a5243a8f02b10a79f4c175a61eb8173e5f`
- feature slice: `sha256:9a2523c4870146b09233397f3773f7a27b1e0135c24a6767d16e34a791aab104`
- scenario manifest: `sha256:be4d7473b01da6b428cd5f3be48de083abd161a4899471303f3ccfeef45c725f`
- fixture inputs: `sha256:9ad8207e1cecdf8d0933881290888e4c1a6d85e83ccb6e377dd0ab3a52b9e565`
- result object: `sha256:ff0163f3e9e185e9eb43519bb67f2f0f138ec8f2391d97a36a8916433f5912a8`

A code/contract/fixture/result change requires re-execution and new digests before reliance.

### 8.1 Equivalence fixtures

The original EQ-01…EQ-12 set remains 5 ACCEPT / 7 REJECT. Added negative attacks remain REJECT:

- EQ-13: shrink S3 entity bound 32 → 16;
- EQ-14: give S8 a stronger undeclared host;
- EQ-15: omit S1 `launch` obligation.

The executable set also proves hidden prewarm, failure-injection omission, abstract S3, failed-attempt omission, semantic-overlap removal, hidden manual intervention, and hidden S10 context are rejected.

### 8.2 Retry/reset/aggregate fixtures

| Fixture | Original truth class / attack | Executable result |
|---|---|---|
| AG-01 | R-01 PASS/PASS + injection PASS | `PASS_FOR_COMPARISON` |
| HIST-01 | R-02 product FAIL generation then repaired generation | `GEN-1=FAIL`, linked `GEN-2=PASS_FOR_COMPARISON` |
| AG-13 | R-03 PASS/FAIL/PASS adjudication | `FLAKY` |
| AG-07 | R-04 INFRA failure then PASS | `INCONCLUSIVE` |
| AG-08 | R-05 required recovery injection FAIL | `FAIL` |
| AG-03 | R-06 only one normal PASS | `NOT_RUN` |
| AG-12 | R-07 stronger resource class | `INCONCLUSIVE` |
| AG-09 | R-08 harness defect | `INCONCLUSIVE` + all-candidate scenario reopen |
| AG-05 | same reset identity reused | `NOT_RUN` |
| AG-10 | reset not verified | `NOT_RUN` |
| AG-11 | mutated workspace reused | `NOT_RUN` |
| AG-04 | required injection omitted | `NOT_RUN` |
| AG-06 | failed run omitted from retained ledger | `INCONCLUSIVE` |

History negatives reject generation reuse, missing predecessor linkage, and same-work “repair” masquerade.

## 9. W2-ENG-03 execution packet

Before candidate execution, W2-ENG-03 must freeze:

- this exact harness/validator identity and five digests;
- corrected W2-ENG-01 admission provenance;
- exact platform/accessibility provenance;
- common physical host/container resource profile;
- exact toolchain/account/plugin/terms baselines;
- one adaptation manifest per candidate/scenario;
- validator ACCEPT for every adaptation;
- run registry, reset verification, workspace lineage, and evidence-retention policy;
- manual-intervention policy;
- exact attempt-generation and repair-lineage records.

A candidate unable to preserve a common bound is `INCONCLUSIVE` for that claim unless it supplies an equivalent/stronger mapping that passes the exact validator. The workload is never silently reduced.

## 10. Bias/failure controls

| Failure mode | Control |
|---|---|
| easier candidate-specific slice | frozen common refs + lower bounds |
| candidate-native mechanism drops assertion | closed obligation mappings |
| hidden warm/editor state | cold/repository-regenerated profile + adaptation reject |
| reset reuses mutated workspace | exact reset/workspace identities + verification |
| stronger machine hides tooling cost | exact common resource class |
| failed retry disappears | registry/retained-set equality |
| repair rewrites old failure | immutable linked generations |
| infra failure is called product or vice versa | explicit failure class; non-product ambiguity is INCONCLUSIVE |
| harness defect benefits one candidate | scenario reopens across candidates |
| failure mode omitted | exact required injection IDs |
| S3 proxy produces convenient hashes | `REAL_OR_SHARED_RULES` authority |
| candidate packages easier target | exact common package target |
| continuation uses private memory | hidden-context rejection |
| one score hides hard failures | scenario/generation/attempt evidence retained; no scalar score |

## 11. Freshness and reopen conditions

Reopen/version the harness when:

- W2-ENG-01 admission evidence changes the hypothesis set materially;
- platform/accessibility evidence makes the common slice invalid or unfair;
- W2-ENG-03 demonstrates a non-decision-relevant architecture bias in a bound;
- any executable negative fixture unexpectedly accepts;
- any declared digest stops reproducing;
- attempt/reset/resource/history evidence cannot be retained;
- W2-REV-01 finds a BLOCKER/MAJOR in parity, retry lineage, failure classification, or authority limits.

Evidence from incompatible harness versions is never silently pooled.

## 12. Remediation acceptance and self-review

Issue #94 acceptance:

- immutable provenance to frozen Issue #72 and pre-gate review: **PASS**
- exact feature slice exists before adaptation: **PASS**
- S1–S10 exact common refs and measurable bounds: **PASS**
- candidate-native adaptation weakening mechanically rejected: **PASS**
- executable validator consumes adaptation/attempt/history objects: **PASS**
- original EQ-01…12 executable: **PASS**
- original retry/reset truth classes executable: **PASS**
- smaller input, hidden prewarm, stronger resource, missing obligation/injection, abstract S3, failed-attempt omission, hidden S10 context rejected or fail-closed: **PASS**
- repaired generation cannot erase predecessor failure: **PASS**
- harness defect reopens all candidates for the scenario: **PASS**
- validator/results content-addressed and reproduced: **PASS**
- no engine executed/scored/selected: **PASS**
- no readiness/canonicalization authority: **PASS**
- formal aggregate review remains W2-REV-01: **PASS**

Continuation self-review found one material defect in inherited Issue #94 work: its executable v2 fixture did not reproduce several original retry/reset truth classes while claiming full executable coverage. That defect was corrected in v2.1 before terminal status.

**Final bounded self-review:** 0 unresolved BLOCKER / 0 unresolved MAJOR / 0 correction-requiring MINOR.

**Producer remediation disposition:** `REVIEW_READY_CANDIDATE / EVIDENCE_REQUIRED`. This exact v2.1 packet may supersede frozen Issue #72 as the substantive W2-ENG-02 input for W2-ENG-03/W2-REV-01 only after Issue #94 terminal provenance is published. It creates no stronger authority.
