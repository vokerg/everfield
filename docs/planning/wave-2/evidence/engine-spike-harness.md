# W2-ENG-02 — Common autonomous engine spike harness and equivalence protocol

**Mission:** `W2-ENG-02`  
**Issue:** #72  
**Task class / decision state:** `PLANNING_EXPERIMENT / EVIDENCE_REQUIRED`  
**Task branch:** `planning/issue-72`  
**Activation/base:** `e4b7ee0a2699a57216146e99b990ab64edaae1d1`  
**Schema-3 claim:** comment `5254913179`  
**Harness state:** `EVIDENCE_REQUIRED`; this artifact defines and exercises protocol fixtures only.  
**Engine-selection authority:** NONE.

## Review Index

- **Purpose:** freeze a candidate-neutral S1–S10 comparison contract before W2-ENG-03 so candidate-native adaptations cannot silently weaken claims.
- **Invariant:** implementations may differ; scenario intent, acceptance predicates, evidence obligations, failure injections, attempt-retention rules, and continuation semantics may not weaken.
- **Repetition:** one successful attempt can never establish reliability. Every scenario begins with two independent normal attempts; disagreement, product failure, flake, or infra ambiguity requires an additional adjudication attempt. All attempts remain in lineage.
- **Adaptation rule:** each candidate publishes an `AdaptationManifest` mapping common obligations to candidate-native mechanisms. A deviation is admissible only when the mapped claim is equivalent or strictly stronger; convenience never creates equivalence.
- **Evidence identity:** every attempt binds exact candidate/toolchain, harness/scenario/adaptation versions, candidate/base/work identity, input package, environment, actions, failure injection, outputs, artifacts, operator/recovery traces, manual intervention, and cost/resource observations.
- **Exercise performed here:** twelve synthetic equivalence fixtures plus retry/failure/continuation truth cases were evaluated against the protocol. Five are admissible and seven are rejected. These are harness-validation results, not engine results.
- **Bias controls:** no candidate scoring exists here; reviewer-visible asymmetry includes adapter burden, manual intervention, hidden editor state, cache dependence, evidence substitution, weaker failure injection, and candidate-specific exceptions.
- **Required review:** `W2-REV-01` must attack scenario parity, synthetic-fixture sufficiency, repetition policy, manual-intervention semantics, and any path by which W2-ENG-03 could cherry-pick successful attempts.

## 1. Scope and non-goals

This artifact defines the common experimental harness that W2-ENG-03 must use across admitted engines. The harness compares whether fresh autonomous agents can build, change, exercise, inspect, recover, package, and continue a repository-owned game project under equivalent claims.

In scope:

- S1–S10 scenario intent, acceptance, and required evidence;
- adaptation-manifest semantics;
- equivalent-versus-weaker mapping rules;
- evidence/run identity and attempt lineage;
- repeated-run policy and failure retention;
- failure-injection requirements;
- operator, recovery, manual-intervention, and cost traces;
- fresh-context continuation semantics;
- synthetic fixtures that exercise harness validation before candidate execution;
- reviewer-visible bias indicators.

Non-goals:

- no candidate engine is executed or scored in this mission;
- no engine ranking, ADR, production recommendation, or platform commitment;
- no final gameplay architecture, save format, profiler, packaging target, or content pipeline selection;
- no disposable spike code becomes production dependency;
- no `UNKNOWN`, `NOT_RUN`, `FLAKY`, `INCONCLUSIVE`, or failed attempt is converted into PASS by retry or omission.

## 2. Authority, provenance, and constraints

Authoritative inputs are the canonical Wave 1 foundations and dependency map. They establish that:

1. engine discovery/admission and S1–S10 representative spikes remain `EVIDENCE_REQUIRED`;
2. equivalent scenario intent, adaptation manifests, repeated failures/retries/costs, and independent equivalence review are mandatory;
3. the sole acceptance chain is requirement → check plan → execution envelopes → derived satisfaction → review/verification;
4. required FAIL/FLAKY/INCONCLUSIVE/NOT_RUN cannot yield SATISFIED by convention;
5. canonical gameplay meaning remains engine-independent logical state; engine/editor/rendering types are adapters unless separately reviewed;
6. cross-runtime hash authority remains blocked on W2-HASH-01;
7. planning experiment code/artifacts are disposable/non-production by default;
8. target platform/product scope remains OPEN.

The S1–S10 labels below are reconstructed from the historical W1-TEC-01 proposal only as provenance for the already-canonical S1–S10 family named by Wave 1 §17 and Issue #72. Historical text does not override the canonical foundations or this issue contract.

## 3. Harness identity and closed comparison objects

### 3.1 `EngineSpikeHarness`

```yaml
EngineSpikeHarness:
  schema_version: 1
  harness_id: W2-ENG-HARNESS-v1
  authority_state: EVIDENCE_REQUIRED
  scenario_contract_refs: [S1-v1, S2-v1, S3-v1, S4-v1, S5-v1, S6-v1, S7-v1, S8-v1, S9-v1, S10-v1]
  attempt_policy_ref: W2-ENG-ATTEMPTS-v1
  adaptation_policy_ref: W2-ENG-ADAPT-v1
  evidence_identity_ref: W2-ENG-RUN-v1
  manual_intervention_policy_ref: W2-ENG-MANUAL-v1
  continuation_policy_ref: W2-ENG-CONTINUE-v1
  candidate_scoring_authority: NONE
  production_dependency_allowed: false
```

Unknown fields or unknown policy refs fail closed for equivalence review.

### 3.2 `ScenarioContract`

```yaml
ScenarioContract:
  scenario_id: S1..S10
  version: 1
  intent: <stable claim>
  fixed_inputs: []
  required_actions: []
  acceptance_assertions: []
  required_evidence_surfaces: []
  required_failure_injections: []
  allowed_adaptation_dimensions: []
  forbidden_weakening: []
  applicability: REQUIRED | CONDITIONALLY_REQUIRED
  result_domain: PASS | FAIL | FLAKY | INCONCLUSIVE | NOT_RUN | NOT_APPLICABLE
```

`NOT_APPLICABLE` requires a pre-run applicability rationale accepted by the common contract. Candidate inconvenience is not a valid applicability reason.

### 3.3 `AdaptationManifest`

```yaml
AdaptationManifest:
  schema_version: 1
  candidate_id: <stable admitted candidate>
  candidate_version: <exact>
  harness_id: W2-ENG-HARNESS-v1
  scenario_id: <S1..S10>
  adaptation_id: <stable>
  native_mechanisms:
    project_layout: <ref>
    scripting_or_language: <ref>
    build_test_commands: []
    editor_or_headless_mechanism: <ref>
    capture_or_profile_mechanism: <ref-or-NOT_APPLICABLE>
  mappings:
    - common_obligation_ref: <exact assertion/evidence/injection id>
      candidate_mechanism_ref: <exact>
      relation: EQUIVALENT | STRICTLY_STRONGER
      rationale: <bounded>
  extra_requirements: []
  manual_interventions_expected: []
  candidate_specific_exceptions: []
  reviewer_equivalence_state: UNREVIEWED | ACCEPTED | REJECTED
```

A manifest containing `WEAKER`, missing mappings, unrecorded manual rescue, suppressed failure injection, or a substituted lower-authority evidence surface is invalid.

## 4. Attempt and result policy

### 4.1 Normal repetition

`W2-ENG-ATTEMPTS-v1`:

1. Every scenario starts with **two independent normal attempts** from the declared scenario start state.
2. Both attempts are retained whether they pass or fail.
3. If results disagree, either attempt is flaky, a required output is missing, or infra/product classification is ambiguous, run a third adjudication attempt.
4. A third attempt does not erase either earlier attempt.
5. Reliability may not be described as clean PASS when normal attempts disagree; the scenario remains `FLAKY` or `INCONCLUSIVE` unless the versioned requirement explicitly defines a stronger resolution rule reviewed before execution.
6. A product failure followed by a successful fix is represented as separate attempt generations with repair lineage, not as one successful attempt.
7. A failed failure-injection recovery is a scenario failure even if the normal path passes.
8. W2-ENG-03 may collect more attempts for variance/cost analysis, but may not lower these minima per candidate.

This is a bounded minimum, not a claim that two attempts statistically establish production reliability.

### 4.2 Failure classes

Every non-PASS attempt records exactly one primary class plus optional secondary observations:

- `PRODUCT_BEHAVIOR`
- `TOOLCHAIN_OR_ENGINE`
- `PROJECT_ADAPTER`
- `INFRASTRUCTURE`
- `HARNESS_DEFECT`
- `UNKNOWN`

`HARNESS_DEFECT` reopens the affected common scenario for every candidate; it may not be counted against one engine.

### 4.3 Manual intervention

A manual intervention is any action required to progress that is not represented by the normal repository/CLI/agent-operable path. It records:

```yaml
ManualIntervention:
  intervention_id: <stable>
  trigger: <what blocked autonomous progress>
  actor_kind: HUMAN | OUT_OF_BAND_OPERATOR | PRIVILEGED_AGENT
  action_summary: <bounded>
  reproducible_as_automation: true | false | UNKNOWN
  candidate_specific: true | false
  changed_project_state: true | false
  evidence_refs: []
```

Manual intervention never disappears from a later successful run. Routine human editor operation is evidence against autonomous-operability claims even if functional output is ultimately correct.

## 5. Execution evidence identity

Each run attempt uses one immutable logical envelope:

```yaml
EngineSpikeRun:
  schema_version: 1
  run_id: <stable/content-addressed>
  harness_id: W2-ENG-HARNESS-v1
  scenario_id: <S1..S10>
  scenario_version: 1
  adaptation_manifest_ref: <exact>
  candidate_id: <exact>
  engine_version: <exact>
  toolchain_versions: []
  candidate_work_sha: <exact>
  comparison_base_sha: <exact>
  input_package_refs: []
  host_environment_ref: <exact image/os/resources>
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

No scalar “engine score” is produced by this object. Costs and burdens remain multidimensional observations for later reviewed comparison.

## 6. S1–S10 common scenario contracts

| ID | Stable intent | Minimum acceptance assertions | Required evidence | Required failure/recovery pressure |
|---|---|---|---|---|
| **S1 Clean bootstrap/build** | A fresh environment can reconstruct, build, and launch the declared minimal project from repository-owned instructions/state. | toolchain resolves; scripted build succeeds; minimal executable launches; hidden state/cache dependencies are disclosed. | environment/toolchain identity, commands, build artifacts, diagnostics, clean + incremental observations. | invalidate/omit cache or generated state and prove recovery/reconstruction. |
| **S2 Editor-independent bounded change** | A fresh agent can make a small player/state-visible change through inspectable repository/automation surfaces without a human driving the editor. | change is reviewable; generated changes are attributable; build/test path detects it. | diff, commands/actions, resulting state/player evidence, editor-automation trace if used. | introduce one stale/generated/project metadata condition and show bounded diagnosis. |
| **S3 Shared-kernel deterministic evidence** | Explicit state + seed/input sequence exercises gameplay-relevant transition through real/shared rules with repeatable state/event evidence under declared determinism boundary. | same inputs yield contract-equivalent outputs; nondeterministic surfaces declared; no rendering determinism implied. | input package, state/events, hashes only where W2-HASH authority permits, repeat attempts. | perturb seed/order/input and prove expected evidence distinction rather than false equality. |
| **S4 Save/load/schema probe** | Small logical state persists, reloads, validates, and reacts explicitly to one controlled schema/content evolution. | round-trip state valid; compatible migration works or incompatibility fails diagnostically; no final save format implied. | source/target tuple, persisted artifact, migration/diagnostic trace, resulting state evidence. | malformed/unsupported tuple must fail boundedly without silent coercion. |
| **S5 Parallel change/merge** | Several non-overlapping repository changes and one intentional overlap can be merged/reconciled with conflicts visible rather than silently lost. | non-overlap merges preserve semantics; overlap is detected/reviewable; generated churn measured. | branch/base SHAs, diffs, merge/conflict trace, post-merge build/check evidence. | deliberate semantic/text/resource overlap plus one generated-file collision where candidate representation makes it plausible. |
| **S6 Controlled player-surface capture** | Automation reaches a known state and emits identity-bound screenshot/video/frame evidence while distinguishing capture failure from game-state failure. | capture is tied to scenario/build; known state independently evidenced; capture-tool failure is typed. | launch actions, state evidence, capture ArtifactIdentity, capture diagnostics. | break/disable capture path while preserving game-state path and classify correctly. |
| **S7 Malformed project/asset recovery** | A fresh agent can diagnose and repair bounded project/resource corruption from repository/CLI evidence without undocumented human rescue. | injected defect detected; cause localized; repair reviewable; project returns to valid evidence state. | injection ref, failing diagnostics, operator trace, repair diff, rerun evidence. | at least one broken reference/resource/asset/settings/import-state defect appropriate to candidate. |
| **S8 Observability/profiling** | Representative workload exposes parseable timing/memory/trace evidence sufficient to locate an injected performance problem. | injected hotspot visible; evidence attributable to exact run; native-vs-adapter burden disclosed. | workload identity, profiler/trace artifacts, resource observations, diagnosis trace. | inject one known hotspot/noise source and require evidence to distinguish it. |
| **S9 Packaging/release-shaped probe** | CI automation produces at least one declared representative distributable with reproducibility inputs and bounded failed-package diagnostics. | package artifact identity retained; exact inputs/toolchain recorded; failed packaging is diagnosable. | package ArtifactIdentity, commands, environment, logs, size/time observations. | intentionally invalid package/config/input causes typed failure and recovery path. |
| **S10 Fresh-agent continuation** | A second fresh context can continue a partially complete spike using repository/GitHub state only. | handoff reconstructs status; no hidden chat state required; second context completes/reruns evidence and leaves reviewable diff/evidence. | frozen handoff, branch/head, evidence refs before/after, continuation operator trace. | first episode stops at a deliberately incomplete but reconstructable point; missing required handoff field must fail continuation fixture. |

## 7. Equivalence law

For candidate `C`, scenario `S`, and common obligation set `O`:

`Equivalent(C,S)` is true only when every required obligation `o ∈ O` has a candidate mapping whose semantics are `EQUIVALENT` or `STRICTLY_STRONGER`, and none of the following occur:

- acceptance assertion removed, weakened, or made candidate-specific;
- required evidence surface replaced by a lower-authority proxy;
- required failure injection omitted because it is inconvenient;
- real/shared gameplay execution replaced by an abstract model for S3;
- hidden editor/manual repair is excluded from operator burden;
- failed/flaky attempts are deleted or ignored;
- cache/generated state makes a nominal clean run non-clean without disclosure;
- candidate receives fewer required normal attempts;
- scenario inputs/scale are materially reduced without a reviewed common-contract version change;
- platform/package target is changed for one candidate after comparison begins without the common applicability rule changing for all affected candidates.

A candidate may use a stronger native test, extra platform, richer profiler, or additional evidence. Extra capability does not let it skip common obligations.

## 8. Protocol-level fixture exercise

This mission exercises the harness validator with synthetic adaptation cases. These are not engine capability observations.

| Fixture | Proposed adaptation | Expected | Observed protocol result | Reason |
|---|---|---|---|---|
| EQ-01 | Candidate-native unit/integration runner replaces common runner while exercising same S2 assertion and preserving diff/state evidence. | ACCEPT | **ACCEPT** | mechanism differs; obligation/evidence unchanged. |
| EQ-02 | S7 malformed-resource injection omitted because candidate editor auto-repairs it. | REJECT | **REJECT** | convenience removes required failure pressure; auto-repair itself must be evidenced. |
| EQ-03 | S3 uses an abstract simulator because candidate runtime headless mode is difficult. | REJECT | **REJECT** | lower-authority surface; S3 requires real/shared rules execution. |
| EQ-04 | S6 uses a candidate-native screenshot API and additionally records frame/state identity. | ACCEPT | **ACCEPT** | equivalent capture with stronger identity evidence. |
| EQ-05 | S1 begins from a prewarmed undocumented import cache for one candidate. | REJECT | **REJECT** | violates clean bootstrap and hides reconstructability dependency. |
| EQ-06 | S8 lacks native profiler; project-owned adapter exports parseable timing/memory evidence and adapter effort is retained. | ACCEPT | **ACCEPT** | equivalent evidence may be produced by bounded adapter; cost remains visible. |
| EQ-07 | First normal S9 attempt fails; second succeeds; manifest reports only successful run. | REJECT | **REJECT** | retry laundering deletes attempt lineage. |
| EQ-08 | Candidate packages an additional platform while still producing the common representative target. | ACCEPT | **ACCEPT** | strictly stronger extra evidence; common obligation preserved. |
| EQ-09 | S5 reduces overlapping edit to disjoint files because candidate resource merge is difficult. | REJECT | **REJECT** | removes the conflict claim being tested. |
| EQ-10 | S2 requires one human editor click but records it only as “setup.” | REJECT | **REJECT** | manual intervention is material autonomous-operability evidence. |
| EQ-11 | S4 uses candidate-native serialization but persists the same logical fixture and emits explicit incompatible-input diagnostics. | ACCEPT | **ACCEPT** | physical format is adaptable; logical claim/evidence preserved. |
| EQ-12 | S10 second episode receives private chat summary not present in repo/GitHub handoff. | REJECT | **REJECT** | violates fresh continuation and repository-as-memory constraint. |

Exercise summary: **5 ACCEPT / 7 REJECT**. No fixture exposed a rule allowing weaker acceptance to masquerade as equivalence.

### 8.1 Retry truth cases

| Case | Attempts | Derived harness interpretation |
|---|---|---|
| R-01 | PASS, PASS | normal-path evidence may be considered clean for later review; not a production reliability proof. |
| R-02 | FAIL(product), PASS(after repair) | retain both; scenario records repair generation and failure; never collapse to single PASS. |
| R-03 | PASS, FAIL, PASS | `FLAKY`/`INCONCLUSIVE` under v1; third attempt does not erase disagreement. |
| R-04 | FAIL(infra), PASS | infra classification retained; candidate claim is not product FAIL if evidence supports infra classification, but history remains. |
| R-05 | PASS normal path, FAIL required injection recovery | scenario FAIL for the tested recovery claim. |
| R-06 | PASS only once | insufficient repetition; second normal attempt is `NOT_RUN`, so reliability claim remains incomplete. |

### 8.2 Continuation truth cases

A valid S10 handoff minimally binds mission/scenario, branch, exact head, current attempt lineage, completed/remaining actions, known failures, required commands, evidence locations, and next acceptance step. A missing exact head, missing failure history, or hidden-only instruction causes the synthetic continuation fixture to fail before execution.

## 9. Bias and asymmetry observability

W2-ENG-03 and W2-REV-01 must expose—not normalize away—the following candidate-specific asymmetries:

- number and type of manual interventions;
- hidden/editor-only state dependencies;
- number of project-owned adapters required;
- adapter code/maintenance surface;
- generated/unreviewable repository churn;
- cache/bootstrap sensitivity;
- conflict count and semantic-conflict visibility;
- build/package/capture/profile failure rates;
- recovery actions and context needed;
- total commands/actions and retries;
- resource/time/artifact-size observations;
- candidate-specific exception count;
- areas left UNKNOWN because equivalent evidence could not be produced.

These are dimensions/evidence, not a scalar score. Later comparison may use Pareto/sensitivity reasoning but cannot derive a winner from one aggregate number.

## 10. Failure-injection catalog

Failure injections are versioned inputs, not ad hoc sabotage. The common catalog begins with:

- `FI-S1-CACHE-MISS-v1` — remove undeclared cache/generated prerequisites;
- `FI-S2-STALE-META-v1` — stale/project metadata mismatch appropriate to candidate;
- `FI-S3-INPUT-PERTURB-v1` — controlled seed/order/input perturbation;
- `FI-S4-INCOMPAT-TUPLE-v1` — unsupported or malformed persistence tuple;
- `FI-S5-OVERLAP-v1` — deliberate concurrent semantic/resource overlap;
- `FI-S6-CAPTURE-DOWN-v1` — capture mechanism unavailable while state path remains runnable;
- `FI-S7-BROKEN-REF-v1` — broken reference/resource/settings/import condition;
- `FI-S8-HOTSPOT-v1` — known workload hotspot/noise source;
- `FI-S9-PACKAGE-CONFIG-v1` — invalid packaging input/configuration;
- `FI-S10-HANDOFF-GAP-v1` — one required continuation field omitted in a negative fixture.

Candidate-specific physical injections may differ only through an accepted adaptation mapping to the same failure claim.

## 11. Fresh continuation protocol

For S10:

1. Episode A starts from the same declared scenario base and performs a bounded subset.
2. Episode A commits useful state and writes the repository/GitHub handoff with exact head and evidence lineage.
3. No continuation-critical instruction may remain chat-only.
4. Episode B is treated as a fresh context: it receives repository/GitHub state and the normal task entry path, not Episode A private reasoning.
5. Episode B reconstructs current state before mutation, records reconstruction discrepancies, completes or rejects the task, reruns required evidence, and updates handoff/result lineage.
6. Hidden transfer or human explanation is a manual intervention and invalidates a clean continuation claim.

## 12. Experimental-code lifecycle

Any W2-ENG-03 candidate-specific harness adapters or sample projects are `PLANNING_EXPERIMENT` material:

- disposable by default;
- no production/gameplay dependency;
- no canonical game-content authority;
- retained only when required as immutable evidence/fixture;
- promotion requires a later reviewed/verified production task after implementation readiness permits it;
- cleanup/retention must preserve evidence ArtifactIdentity and consumed lineage.

## 13. Interfaces and downstream contract

### W2-ENG-01

Provides the admitted candidate set and exact candidate versions. The self-review concern about a reconstructable discovery universe is review input; this harness does not cure candidate-admission completeness and must not infer that the current candidate set is final.

### W2-HASH-01

S3 may retain local hashes as diagnostics, but cross-runtime canonical hash authority is unavailable unless W2-HASH-01 establishes it. Equivalence must therefore bind semantic state/events independently of an unverified hash claim.

### W2-PLAT-01

S9 uses a representative packaging target only. Once platform scope changes, applicability/target requirements must be versioned commonly; candidate-specific target cherry-picking is forbidden.

### W2-AUTH-01

The harness is designed to compile into the canonical evidence chain, but unresolved authority-contract review findings remain review input. This artifact does not claim the current W2-AUTH-01 candidate has resolved its self-review MAJORs.

### W2-ENG-03

May begin only after all declared hard prerequisites are REVIEW_READY. It must:

- freeze this harness version before comparative attempts;
- publish one adaptation manifest per candidate/scenario;
- obtain equivalence review before relying on candidate-specific weakening;
- retain every attempt/failure/retry/manual intervention;
- preserve common repetition and failure-injection minima;
- emit multidimensional observations, not a winner by familiarity or one scalar score.

## 14. Risks and unresolved questions

- Two normal attempts are a bounded anti-cherry-pick minimum, not statistical reliability proof; W2-REV-01 may require stronger repetition for high-variance scenarios.
- Exact host resource class remains unresolved until W2-ENG-03 execution planning; differences must be recorded rather than normalized by assertion.
- Some engines may require editor automation for S2/S6/S7. That is allowed only when invokable/inspectable and intervention/state effects remain visible.
- Cross-platform packaging cannot be made fully equivalent until W2-PLAT-01 bounds target scope.
- The harness needs W2-REV-01 to challenge whether synthetic fixtures cover enough weakening paths.
- Candidate terms/authorized-agent constraints may make a technically equivalent path impermissible; W2-RIGHTS-01 remains authoritative for that question.
- Protected evaluator/oracle requirements, if later applied to comparative judgment, remain bounded by W2-PROTECT-01/W2-EVAL-01 evidence.

## 15. Reopen conditions

Reopen/version this harness if:

- W2-REV-01 finds a route for candidate adaptation to weaken a common claim;
- W2-ENG-03 discovers a scenario whose common contract cannot be executed fairly across admitted candidates;
- target platform/product scope materially changes S9 or host requirements;
- W2-HASH-01 changes the admissible S3 cross-runtime evidence semantics;
- evidence shows two-attempt minimum systematically hides variance;
- a candidate terms/permissions constraint changes what autonomous actions are allowed;
- a harness defect is observed in any candidate run;
- a fresh continuation depends on hidden context despite a nominally complete handoff.

A harness change after candidate execution creates a new harness/scenario version; old runs are historical evidence and are not silently reinterpreted as if run under the new contract.

## 16. Required independent critique

`W2-REV-01` should specifically attack:

1. whether any S1–S10 assertion is materially weaker than the intended autonomous-development claim;
2. whether an adaptation can substitute lower-authority/model evidence for real/shared execution;
3. whether the two-attempt + adjudication policy is sufficient to prevent cherry-picking without creating false statistical confidence;
4. whether manual interventions can be relabeled as setup or privileged automation;
5. whether failure injections are equivalent rather than physically identical but semantically different;
6. whether S10 can be gamed through hidden context transfer;
7. whether host/resource asymmetry, cache state, or target selection can bias comparison;
8. whether failure/repair generations and costs remain visible through later synthesis;
9. whether synthetic equivalence fixtures are sufficient or require executable validator fixtures before W2-ENG-03;
10. whether any wording accidentally grants engine-selection or production authority.

## 17. Downstream work unblocked

When this mission reaches exact `REVIEW_READY`, it contributes one prerequisite token to W2-ENG-03 and W2-REV-01. It authorizes no engine execution by itself, no engine decision, no implementation-readiness transition, and no production/gameplay implementation.
