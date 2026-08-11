# W2-ENG-02 — Common autonomous engine spike harness and equivalence protocol

**Mission:** `W2-ENG-02`  
**Issue:** #72  
**Task class / decision state:** `PLANNING_EXPERIMENT / EVIDENCE_REQUIRED`  
**Task branch:** `planning/issue-72`  
**Activation/base:** `e4b7ee0a2699a57216146e99b990ab64edaae1d1`  
**Schema-3 claim:** comment `5254913179`  
**Harness identity:** `W2-ENG-HARNESS-v1`  
**Engine-selection authority:** NONE.

## Review Index

- **Purpose:** freeze an engine-neutral S1–S10 contract before W2-ENG-03 so candidate-native adaptations cannot silently weaken claims.
- **Equivalence invariant:** implementation mechanisms may differ; scenario intent, acceptance assertions, evidence obligations, start-state/resource profile, repetition, failure injection, failure retention, and continuation semantics may not weaken.
- **Attempt policy:** every scenario begins with two independently reset normal attempts under the same scenario resource/start-state class. One successful run can never establish reliability. Any disagreement or non-PASS keeps the aggregate non-clean; all attempts remain in lineage.
- **Adaptation manifest:** every common obligation maps to an `EQUIVALENT` or `STRICTLY_STRONGER` candidate mechanism. Missing/weaker mappings are rejected.
- **Review authority:** candidate authors may propose mappings but cannot self-accept equivalence. `EquivalenceReview` is a separate review object/episode.
- **Evidence identity:** every attempt binds exact candidate/toolchain, harness/scenario/adaptation, candidate/base/work SHA, input/start-state/resource profile, actions, failure injection, outputs/artifacts, operator/recovery/manual-intervention traces, repository churn, and resource/cost observations.
- **Protocol exercise:** twelve synthetic adaptation fixtures plus retry and continuation truth cases were evaluated. Five are admissible and seven rejected. These are harness-validator results, not engine results.
- **No scoring:** this mission produces no candidate score/rank. Reviewer-visible asymmetries remain multidimensional evidence.
- **Required review:** `W2-REV-01` must attack parity, reset/resource fairness, synthetic-fixture sufficiency, manual-intervention semantics, and cherry-pick resistance.

## 1. Scope and non-goals

This artifact defines the common experimental harness that W2-ENG-03 must use across admitted engines. It asks whether fresh autonomous agents can reconstruct, modify, execute, inspect, recover, package, and continue a repository-owned project under equivalent claims.

In scope: S1–S10 intent/acceptance/evidence parity; start-state/resource/reset rules; adaptation manifests; evidence/run identity; attempt aggregation; failure injection; operator/recovery/manual/cost traces; fresh continuation; synthetic equivalence fixtures; bias observability.

Non-goals: no engine execution or scoring here; no engine ADR; no final platform/gameplay/save/profile/package choice; no production dependency; no laundering `FAIL`, `FLAKY`, `INCONCLUSIVE`, `NOT_RUN`, or `UNKNOWN` into PASS.

## 2. Canonical constraints and provenance

The canonical Wave 1 foundations/dependency map establish:

1. engine discovery/admission and S1–S10 spikes remain `EVIDENCE_REQUIRED`;
2. equivalent scenario intent, adaptation manifests, repeated failures/retries/costs, and independent equivalence review are mandatory;
3. acceptance flows requirement → CheckPlan → execution envelopes → derived satisfaction → review/verification;
4. failed/flaky/inconclusive/not-run required evidence cannot satisfy by convention;
5. canonical gameplay meaning remains engine-independent logical state;
6. cross-runtime hash authority awaits W2-HASH-01;
7. planning-experiment code is disposable/non-production;
8. platform scope remains OPEN.

The S1–S10 names below are recovered from historical W1-TEC-01 only as provenance for the already-canonical S1–S10 family named by Wave 1 §17 and Issue #72. Historical text has no authority to override the canonical inputs.

## 3. Core harness objects

### 3.1 `EngineSpikeHarness`

```yaml
schema_version: 1
harness_id: W2-ENG-HARNESS-v1
scenario_refs: [S1-v1, S2-v1, S3-v1, S4-v1, S5-v1, S6-v1, S7-v1, S8-v1, S9-v1, S10-v1]
attempt_policy_ref: W2-ENG-ATTEMPTS-v1
start_state_policy_ref: W2-ENG-START-v1
adaptation_policy_ref: W2-ENG-ADAPT-v1
aggregate_policy_ref: W2-ENG-AGGREGATE-v1
manual_intervention_policy_ref: W2-ENG-MANUAL-v1
continuation_policy_ref: W2-ENG-CONTINUE-v1
candidate_scoring_authority: NONE
production_dependency_allowed: false
```

Unknown policy refs/fields fail closed for equivalence.

### 3.2 `ScenarioContract`

```yaml
scenario_id: S1..S10
version: 1
intent: <stable claim>
fixed_input_refs: []
start_state_profile_ref: <exact>
required_actions: []
acceptance_assertion_refs: []
required_evidence_surface_refs: []
required_failure_injection_refs: []
allowed_adaptation_dimensions: []
forbidden_weakening_refs: []
applicability: REQUIRED | CONDITIONALLY_REQUIRED
```

`NOT_APPLICABLE` is resolved before execution from a common applicability rule; candidate inconvenience is not applicability evidence.

### 3.3 `StartStateProfile`

```yaml
profile_id: <stable>
repo_base_sha: <exact>
workspace_mode: CLEAN_CLONE | VERIFIED_RESET_TO_BASE
cache_mode: COLD | DECLARED_COMMON_WARM
cache_identity_ref: <required when warm>
generated_state_policy: REGENERATE_FROM_REPO | DECLARED_RETAINED
host_resource_class_ref: <exact CPU/RAM/disk/OS/image class>
network_policy_ref: <exact>
credential_capability_ref: <exact>
```

Rules:

- The same scenario uses the same reviewed start-state/resource class for all candidates unless a common versioned rule says otherwise.
- Candidate-specific extra CPU/RAM/disk/privilege is a `RESOURCE_EXCEPTION`; it is retained and blocks direct performance comparison for the affected dimension until normalized/retested.
- Hidden/prewarmed cache or generated state invalidates a nominal clean/reset claim.
- Normal attempt 2 must independently reconstruct/reset to the declared profile; it is not merely “rerun immediately in attempt 1 workspace.”
- Incremental-build observations may occur inside an attempt after the clean baseline, but never substitute for the required clean/reset start.

### 3.4 `AdaptationManifest`

```yaml
schema_version: 1
candidate_id: <stable>
candidate_version: <exact>
harness_id: W2-ENG-HARNESS-v1
scenario_id: <S1..S10>
adaptation_id: <stable>
native_mechanism_refs: []
mappings:
  - common_obligation_ref: <exact>
    candidate_mechanism_ref: <exact>
    relation: EQUIVALENT | STRICTLY_STRONGER
    rationale: <bounded>
extra_requirements: []
expected_manual_interventions: []
resource_exception_refs: []
candidate_specific_exception_refs: []
```

Candidate authors propose this object. They cannot author equivalence acceptance.

### 3.5 `EquivalenceReview`

```yaml
review_id: <stable>
candidate_id: <exact>
scenario_id: <exact>
adaptation_manifest_ref: <exact>
harness_id: W2-ENG-HARNESS-v1
reviewer_context_ref: <exact>
trust_profile: <typed>
finding_refs: []
result: ACCEPTED | REJECTED | CHANGES_REQUIRED
```

W2-ENG-03 may execute an unreviewed adapter for exploratory evidence, but evidence from a `REJECTED`/unresolved manifest cannot establish cross-candidate equivalent claims. Candidate author assertions never substitute for this review state.

## 4. Attempt, failure, and aggregation policy

### 4.1 `W2-ENG-ATTEMPTS-v1`

1. Each scenario starts with two normal attempts, each reset/reconstructed to the same declared `StartStateProfile`.
2. Every attempt is retained.
3. If attempts disagree, any required evidence is missing, or failure class is ambiguous, run a third adjudication attempt under the same profile.
4. Third attempt never erases earlier attempts.
5. A failure followed by a repair becomes a new attempt generation with parent lineage.
6. Required failure-injection/recovery attempts are additional to the two normal attempts.
7. W2-ENG-03 may add attempts for variance/cost analysis but may not reduce minima per candidate.
8. Two PASS attempts are a bounded anti-cherry-pick minimum, not statistical proof of production reliability.

### 4.2 Failure classes

Every non-PASS attempt has one primary class:

`PRODUCT_BEHAVIOR | TOOLCHAIN_OR_ENGINE | PROJECT_ADAPTER | INFRASTRUCTURE | HARNESS_DEFECT | UNKNOWN`.

`HARNESS_DEFECT` reopens the scenario for every candidate and yields aggregate `INCONCLUSIVE`; it may not count against one engine.

### 4.3 `ScenarioAttemptSet`

```yaml
scenario_attempt_set_id: <stable>
candidate_id: <exact>
scenario_id: <exact>
harness_id: W2-ENG-HARNESS-v1
start_state_profile_ref: <exact>
normal_attempt_refs: []
failure_injection_attempt_refs: []
repair_generation_refs: []
all_attempt_refs: []
aggregate_result: PASS_FOR_COMPARISON | FAIL | FLAKY | INCONCLUSIVE | NOT_RUN | NOT_APPLICABLE
```

`W2-ENG-AGGREGATE-v1` derives:

- `PASS_FOR_COMPARISON` only if both required normal attempts PASS, every required failure/recovery assertion passes, required evidence exists, no unresolved resource exception affects the claim, and no attempt is hidden.
- `FAIL` when a required product/toolchain/adapter assertion or required recovery behavior fails without a harness/infra ambiguity that dominates classification.
- `FLAKY` when required normal attempts disagree on product behavior or reproducibility.
- `INCONCLUSIVE` for unresolved infra/harness/unknown classification, missing authority needed to interpret evidence, or unresolved equivalence/resource exception.
- `NOT_RUN` when required attempts/evidence were not executed.
- `NOT_APPLICABLE` only from pre-run common applicability resolution.

A later successful repair does not rewrite the original aggregate history; it creates a new attempt-set generation that links the prior failure.

## 5. Manual intervention and evidence identity

### 5.1 Manual intervention

Any action needed to progress outside the normal repository/CLI/agent-operable path is recorded:

```yaml
intervention_id: <stable>
trigger: <blocking condition>
actor_kind: HUMAN | OUT_OF_BAND_OPERATOR | PRIVILEGED_AGENT
action_summary: <bounded>
reproducible_as_automation: true | false | UNKNOWN
candidate_specific: true | false
changed_project_state: true | false
evidence_refs: []
```

Human editor rescue cannot be relabeled “setup.” Manual intervention remains visible after later success.

### 5.2 `EngineSpikeRun`

```yaml
schema_version: 1
run_id: <stable/content-addressed>
harness_id: W2-ENG-HARNESS-v1
scenario_id: <S1..S10>
scenario_version: 1
adaptation_manifest_ref: <exact>
equivalence_review_ref: <exact-or-UNREVIEWED>
candidate_id: <exact>
engine_version: <exact>
toolchain_versions: []
candidate_work_sha: <exact>
comparison_base_sha: <exact>
input_package_refs: []
start_state_profile_ref: <exact>
host_environment_ref: <exact>
attempt_index: <integer>
attempt_generation: <integer>
parent_attempt_refs: []
failure_injection_ref: <exact-or-NONE>
commands_or_actions: []
expected_assertion_refs: []
observed_results: []
artifact_identity_refs: []
operator_trace_ref: <exact>
recovery_trace_ref: <exact-or-NONE>
manual_intervention_refs: []
warning_failure_refs: []
resource_exception_refs: []
resource_observations:
  wall_duration: <measured-or-UNKNOWN>
  cpu_peak_or_integral: <measured-or-UNKNOWN>
  memory_peak: <measured-or-UNKNOWN>
  disk_or_artifact_bytes: <measured-or-UNKNOWN>
  network_bytes: <measured-or-UNKNOWN>
repository_observations:
  files_changed: <count>
  generated_churn_files: <count>
  merge_conflicts: <count>
  binary_conflicts: <count>
result: PASS | FAIL | FLAKY | INCONCLUSIVE | NOT_RUN | NOT_APPLICABLE
```

No scalar engine score is emitted. Operator/recovery burden and resource/cost data remain separate dimensions.

## 6. S1–S10 common contracts

| ID | Stable intent | Minimum acceptance/evidence | Required failure/recovery pressure |
|---|---|---|---|
| **S1 Clean bootstrap/build** | Fresh environment reconstructs, builds, launches minimal project from repository-owned state. | exact toolchain/env/commands; clean and incremental build observations; launch artifact/state; hidden dependencies disclosed. | remove/invalidate undeclared cache/generated state and prove reconstruction. |
| **S2 Editor-independent bounded change** | Fresh agent makes small visible/state-visible change without human-driven editor. | reviewable diff; attributable generated changes; automated build/test/state evidence; editor automation trace if used. | stale/generated metadata condition with bounded diagnosis. |
| **S3 Shared-kernel deterministic evidence** | Explicit state + seed/input exercises real/shared rules with repeatable state/event evidence under declared determinism boundary. | exact inputs/state/events; repeats; hashes only within W2-HASH authority; nondeterminism declared. | controlled input/seed/order perturbation must produce expected distinguishable evidence. |
| **S4 Save/load/schema probe** | Small logical world round-trips and handles one controlled schema/content evolution explicitly. | source/target tuple, persisted ArtifactIdentity, migration/diagnostic trace, resulting logical state. | malformed/unsupported tuple must fail diagnostically, not silently coerce. |
| **S5 Parallel change/merge** | Non-overlapping changes plus intentional overlap merge/reconcile with conflicts visible. | branch/base SHAs, diffs, conflict trace, churn counts, post-merge checks. | semantic/resource overlap plus generated-file collision where plausible. |
| **S6 Controlled player-surface capture** | Automation reaches known state and emits identity-bound screenshot/video/frame evidence, separating capture failure from state failure. | launch/state evidence + capture ArtifactIdentity + diagnostics. | disable/break capture while state path remains valid and classify correctly. |
| **S7 Malformed project/asset recovery** | Fresh agent diagnoses/repairs bounded corruption from repo/CLI evidence without undocumented human rescue. | injection ref, failing diagnostics, operator/recovery trace, repair diff, rerun. | broken reference/resource/asset/settings/import condition appropriate to candidate. |
| **S8 Observability/profiling** | Representative workload yields parseable timing/memory/trace evidence that locates injected performance problem. | workload identity, profiler/trace artifacts, resource observations, diagnosis trace; native-vs-adapter burden. | known hotspot/noise injection. |
| **S9 Packaging probe** | CI produces representative distributable with exact reproducibility inputs and failed-package diagnostics. | package ArtifactIdentity, commands/env/logs, size/time observations. | invalid package/config/input with typed failure and recovery. |
| **S10 Fresh-agent continuation** | Episode B continues partial spike using repository/GitHub state only. | frozen handoff, exact branch/head/evidence before/after, continuation trace, completed rerun. | omit one required handoff field in negative fixture; hidden context transfer invalidates clean claim. |

## 7. Equivalence law

For candidate `C`, scenario `S`, and common obligations `O`, equivalent comparison requires every `o ∈ O` to have an accepted candidate mapping with relation `EQUIVALENT` or `STRICTLY_STRONGER`.

Automatic rejection occurs if any adaptation:

- removes/weakens an acceptance assertion;
- substitutes lower-authority evidence;
- omits required failure injection;
- replaces S3 real/shared execution with abstract model evidence;
- hides manual/editor rescue;
- drops failed/flaky attempts;
- uses undeclared warm cache/generated state;
- gives candidate fewer attempts or a stronger resource/permission class without a common reviewed rule;
- materially shrinks scenario scale/input;
- cherry-picks platform/package target after comparison begins.

Extra tests/platforms/profiler richness are allowed only in addition to common obligations.

## 8. Protocol-level fixture exercise

Synthetic validator fixtures (not engine observations):

| Fixture | Adaptation | Expected | Result | Reason |
|---|---|---|---|---|
| EQ-01 | native test runner preserves same S2 assertions/diff/state evidence | ACCEPT | **ACCEPT** | mechanism differs; claim unchanged |
| EQ-02 | omit S7 injection because editor auto-repairs | REJECT | **REJECT** | required failure pressure removed |
| EQ-03 | use abstract simulator for S3 due difficult headless runtime | REJECT | **REJECT** | lower-authority evidence |
| EQ-04 | native screenshot API adds frame/state identity | ACCEPT | **ACCEPT** | equivalent/stronger capture |
| EQ-05 | S1 starts from undocumented prewarmed cache | REJECT | **REJECT** | invalid start-state equivalence |
| EQ-06 | no native profiler; bounded adapter emits same parseable S8 evidence and cost | ACCEPT | **ACCEPT** | equivalent evidence, burden visible |
| EQ-07 | S9 first attempt fails, second succeeds, failed run omitted | REJECT | **REJECT** | retry laundering |
| EQ-08 | candidate adds extra platform but still produces common S9 target | ACCEPT | **ACCEPT** | strictly stronger extra evidence |
| EQ-09 | S5 overlap changed to disjoint files | REJECT | **REJECT** | removes contention claim |
| EQ-10 | S2 human click recorded as “setup” | REJECT | **REJECT** | hidden manual intervention |
| EQ-11 | native serialization preserves same S4 logical fixture + explicit incompatibility diagnostics | ACCEPT | **ACCEPT** | physical format adaptable |
| EQ-12 | S10 B receives private chat summary absent from repository | REJECT | **REJECT** | hidden-context continuation |

**Fixture result:** 5 ACCEPT / 7 REJECT. No weaker adaptation passed.

### Retry/aggregate truth cases

| Case | Required attempt history | v1 aggregate |
|---|---|---|
| R-01 | PASS, PASS + required injection PASS | `PASS_FOR_COMPARISON` |
| R-02 | FAIL(product), PASS after repair | first generation `FAIL`; repaired generation linked separately, never rewritten |
| R-03 | PASS, FAIL, PASS adjudication | `FLAKY` |
| R-04 | FAIL(infra), PASS | `INCONCLUSIVE` under v1; infra failure retained |
| R-05 | normal PASS/PASS, required recovery injection FAIL | `FAIL` |
| R-06 | only one normal PASS | `NOT_RUN` for complete comparison requirement |
| R-07 | PASS/PASS but resource class stronger than common profile | `INCONCLUSIVE` for affected comparative dimension until normalized/retested |
| R-08 | harness defect observed | `INCONCLUSIVE` and scenario reopens for every candidate |

### Reset truth cases

- cold profile + hidden prewarm → reject attempt as invalid start state;
- attempt 2 reuses mutated attempt-1 workspace without verified reset → `NOT_RUN` for required independent second attempt;
- candidate needs privileged credential absent from common profile → record resource/capability exception; affected equivalence is unresolved, not PASS;
- warm cache is allowed only when the same scenario contract deliberately uses `DECLARED_COMMON_WARM` with cache identity bound for every candidate.

## 9. Failure-injection catalog

- `FI-S1-CACHE-MISS-v1`
- `FI-S2-STALE-META-v1`
- `FI-S3-INPUT-PERTURB-v1`
- `FI-S4-INCOMPAT-TUPLE-v1`
- `FI-S5-OVERLAP-v1`
- `FI-S6-CAPTURE-DOWN-v1`
- `FI-S7-BROKEN-REF-v1`
- `FI-S8-HOTSPOT-v1`
- `FI-S9-PACKAGE-CONFIG-v1`
- `FI-S10-HANDOFF-GAP-v1`

Physical injection may be candidate-native only through an accepted mapping to the same failure claim.

## 10. Fresh continuation protocol

1. Episode A starts from declared base/profile and performs a bounded subset.
2. A commits useful state and records exact head, attempts/evidence, failures, remaining actions, commands, and next acceptance step in repository/GitHub handoff.
3. No continuation-critical instruction remains chat-only.
4. Episode B is a fresh context receiving repository/GitHub state and normal entry path, not A's private reasoning.
5. B reconstructs state before mutation, records discrepancies, completes/rejects, reruns required evidence, and updates lineage.
6. Hidden transfer or human explanation is a manual intervention and invalidates a clean S10 claim.

## 11. Bias/asymmetry observability

W2-ENG-03/W2-REV-01 must expose rather than normalize away:

- manual interventions;
- hidden/editor-only state;
- adapter count/maintenance surface;
- generated/binary churn;
- cache/bootstrap sensitivity;
- conflict count/semantic conflict visibility;
- failure/retry/recovery actions;
- action/context/operator burden;
- exact host/resource/capability exceptions;
- wall/resource/artifact-size observations;
- candidate-specific exceptions;
- UNKNOWN/unproduced evidence.

These remain dimensions. No universal scalar score is produced here.

## 12. Experimental-code lifecycle

W2-ENG-03 adapters/sample projects are `PLANNING_EXPERIMENT`: disposable, non-production, no canonical game authority, retained only when required as evidence/fixture, and promotable only through a later reviewed/verified production route after implementation readiness.

## 13. Interfaces

**W2-ENG-01:** supplies admitted candidate/version set. Its recorded self-review concern about deterministic discovery completeness remains review input; this harness does not make the set final.

**W2-HASH-01:** S3 local hashes are diagnostic unless/until canonical cross-runtime hash authority is established; semantic state/events remain required independently.

**W2-PLAT-01:** S9 representative target must be common/versioned. Platform-scope change reopens applicability; per-candidate target cherry-picking is forbidden.

**W2-AUTH-01:** this harness fits the canonical evidence chain but does not resolve W2-AUTH-01's recorded machine-shape/retry/RiskFloor self-review findings.

**W2-ENG-03:** may start only after its declared prerequisites. Before relying on comparative claims it must freeze the harness/profile versions, publish adaptation manifests, retain equivalence review state, execute all attempts/injections, retain every failure/retry/manual intervention, and emit multidimensional evidence rather than a winner by familiarity.

## 14. Risks and unresolved questions

- Two normal attempts are only a bounded anti-cherry-pick minimum; high-variance scenarios may need more after review.
- Exact common host resource class is intentionally not chosen here; W2-ENG-03 execution planning must freeze it before runs.
- Some engines may require editor automation; it is allowed only when invokable/inspectable and its state/intervention effects remain visible.
- Full packaging parity depends on W2-PLAT-01.
- Terms/authorized-agent restrictions may invalidate technically workable paths; W2-RIGHTS-01 remains separate authority.
- Synthetic fixtures test protocol logic but are not a substitute for W2-REV-01 or real W2-ENG-03 runs.

## 15. Reopen conditions

Reopen/version the harness if review or execution finds:

- a weakening path that passes equivalence;
- unfair reset/resource/capability semantics;
- a scenario that cannot fairly represent its claim across admitted candidates;
- platform scope changes S9 applicability;
- W2-HASH changes S3 evidence authority;
- two-attempt minimum hides material variance;
- terms/permission changes alter allowed autonomous actions;
- a harness defect in any candidate run;
- fresh continuation depends on hidden context.

Harness changes after candidate execution create a new version; old runs remain historical and are never silently reinterpreted.

## 16. Required independent critique

`W2-REV-01` should attack:

1. S1–S10 claim parity and hidden weakening;
2. start-state/cache/resource/credential fairness;
3. model/proxy substitution for real/shared evidence;
4. attempt aggregation and repair/retry laundering;
5. manual intervention relabeling;
6. semantic equivalence of failure injections;
7. hidden-context S10 transfer;
8. host/target/cost asymmetry;
9. whether synthetic fixtures are sufficient or executable validator fixtures are required;
10. any accidental engine-selection or production authority.

## 17. Downstream

Exact `REVIEW_READY` contributes the W2-ENG-02 prerequisite token to W2-ENG-03 and W2-REV-01. It authorizes no engine decision, no implementation-readiness transition, and no production/gameplay implementation.
