# Engine Evaluation Program and Representative Autonomous-Development Spikes — Wave 1 Proposal

**Mission:** `W1-TEC-01`  
**State:** PROPOSAL / NON-CANONICAL  
**Required review:** `W1-REV-TECH`

## Review Index

- **EEP-D1 — Engine choice is an evidence program, not a preference (§8):** no engine becomes preferred from familiarity, popularity, feature tables, or one successful prototype. Candidates must pass common admission, primary-source research, and representative measured spikes.
- **EEP-D2 — Candidate admission and disqualification (§9):** every candidate is evaluated against autonomous CLI/repository operation, test/evidence integration, asset/project recoverability, concurrency/merge behavior, packaging/tooling viability, and governance/licensing constraints; unsupported current claims remain `UNKNOWN`, not assumed PASS.
- **EEP-D3 — Common spike harness (§10):** each candidate runs the same bounded scenario family with fixed repository artifacts, operator instructions, evidence schema, repeated runs, and explicit allowed candidate-specific adaptation.
- **EEP-D4 — Autonomous-development spikes (§11):** required spikes cover clean bootstrap/build, editor-independent change, headless/shared-kernel execution, save/load, parallel content edits/merge, controlled visual capture, malformed-asset recovery, observability/profiling, packaging, and fresh-agent continuation.
- **EEP-D5 — Rubric without fake precision (§12):** use hard gates plus multidimensional scored evidence, confidence, missing-evidence penalties, sensitivity analysis, and Pareto comparison; no aggregate score alone can select the engine.
- **EEP-D6 — CI and evidence contract (§13):** every result binds candidate/version/toolchain/environment/commands/work SHA/input hashes/artifacts/timings/failures/retries/manual interventions and source references so reviewers can reproduce or challenge the result.
- **EEP-D7 — ADR protocol (§14):** engine ADR requires qualified candidates, current-base evidence, independent technical review, explicit tradeoffs, rejected alternatives, migration/exit cost, unresolved risks, and reopen conditions; conditional selection is allowed, premature permanent lock-in is not.
- **EEP-D8 — Factory-first criterion (§15):** the primary comparison question is whether many fresh agents can safely modify, build, test, inspect, recover, review, and integrate the project—not whether one expert can work quickly in the interactive editor.
- **Evidence (§5):** project seeds require comparative engine evaluation, representative autonomous-development spikes, real/shared gameplay-kernel evidence, deterministic or controlled execution, CI capture, resumability, merge-friendly concurrency, and no final engine choice yet.
- **Experiments (§18):** candidate admission research plus ten common spikes, repeated-run reliability, concurrency conflict trials, malformed-project recovery, CI-cost/build-time distributions, and decision sensitivity are required before an engine ADR can become accepted.
- **Reviewer attack points:** hidden editor dependence; unequal spike implementations; cherry-picked successful runs; current engine claims without primary sources; one scalar score hiding vetoes; prototype code becoming architecture by accident; candidate-specific tooling effort ignored; build/CI cost sampled once; weak merge/recovery testing; ADR that cannot reopen.

## 1. Objective

Define a reproducible program for selecting Everfield's eventual engine/runtime environment through current primary-source evidence and representative autonomous-development experiments.

The program must answer a stronger question than “can this engine make the game?” It must test whether the engine can support a long-running AI-native development factory in which fresh agents modify bounded repository surfaces, execute real checks, inspect machine-readable evidence, recover from damage, collaborate safely, and continue without interactive human repair.

This proposal defines the comparison protocol. It **does not select an engine** and does not assert current engine capabilities from memory.

## 2. Scope

In scope:

- engine candidate admission and research requirements;
- hard screening/disqualification rules;
- comparative rubric and evidence grades;
- representative autonomous-development spike suite;
- common harness and fairness rules;
- CLI/editor/repository/asset workflow evaluation;
- test/headless/determinism/evidence integration evaluation;
- build/package/profiling/capture evaluation;
- concurrency/merge/recovery evaluation;
- fresh-agent continuation evidence;
- cost/reliability distributions;
- score sensitivity and Pareto analysis;
- engine ADR decision/reopen protocol;
- interfaces to later runtime/data/evaluation plans.

## 3. Non-goals

This proposal does **not**:

- name a winning engine;
- claim that any named engine currently satisfies a criterion without current primary-source or measured evidence;
- choose the final programming language, scripting language, ECS, physics stack, renderer, database, serialization library, networking model, or platform targets;
- implement gameplay;
- treat a throwaway spike architecture as canonical runtime architecture;
- require all candidate engines to use identical internal implementation techniques;
- promise deterministic rendering/physics where the project may only need deterministic gameplay evidence;
- optimize for one benchmark number.

## 4. Constraints and assumptions

### 4.1 Observed project constraints

The authoritative packet establishes that:

1. Everfield is intended to be developed predominantly by autonomous AI agents.
2. The mature factory should support roughly 10–20 or more useful concurrent sessions when the graph permits it.
3. Sessions are disposable; repository state and resumable artifacts are durable memory.
4. Important claims need inspectable evidence, preferably through the real executable or the same gameplay kernel.
5. Deterministic or controlled scenarios, state evidence, screenshots/capture, profiling, and structured run reports are expected.
6. Continuous expansion requires merge-friendly content/runtime workflows and safe parallel ownership surfaces.
7. The project explicitly forbids choosing a final engine before comparative evaluation.
8. The research agenda requires representative autonomous-development spikes rather than feature-table comparison alone.
9. High-throughput implementation remains blocked until later verified readiness.

### 4.2 Assumptions to test

- The best engine for an AI-native project may differ from the engine that is easiest for a human expert in an interactive editor.
- Repository-text/data ergonomics, deterministic command-line operation, recoverability, and observability materially affect agent throughput.
- A common spike family can compare engines fairly while allowing candidate-native implementation where equivalent outcomes are preserved.
- Repeated runs and fresh-agent continuation expose failure modes that a single successful prototype hides.
- Build and CI cost should be treated as distributions under representative change patterns rather than one clean-build stopwatch result.
- Exit/migration cost matters because an early engine choice may later be disproved.

## 5. Evidence, inference, and recommendation

### 5.1 Evidence from the authoritative packet

The project asks the engine program to investigate:

- command-line build/test reliability;
- editor-independent scene/resource/asset modification;
- merge behavior under many agents;
- deterministic or semi-deterministic headless scenarios;
- CI screenshots/video;
- runtime-state inspection;
- testing/profiling/packaging/localization/accessibility/platform workflows;
- build times/CI costs;
- malformed-project recovery;
- editor automation/API surfaces;
- representative autonomous-development spikes.

The evaluation seed further requires production/shared-kernel evidence, deterministic inputs where practical, structured evidence, player and simulation surfaces, and multiple oracles.

### 5.2 Inference

A feature matrix cannot establish autonomous operability. Documentation may say a CLI command exists while repository changes still require opaque generated metadata, interactive imports, undocumented editor state, or fragile repair steps. Conversely, an engine with a less convenient editor may be highly suitable if its project/runtime surfaces are deterministic, scriptable, inspectable, and recoverable.

The decision object should therefore be **evidence from repeated end-to-end agent tasks**, supplemented by primary documentation—not a popularity or familiarity ranking.

### 5.3 Recommendation

Adopt the admission, common harness, spike suite, evidence schema, rubric, and ADR protocol below as the candidate Wave 1 engine-selection process. Keep all candidate-specific capability cells `UNKNOWN` until current primary-source evidence or measured spike evidence is attached.

## 6. Alternatives considered

### A. Pick the most familiar/common engine now — reject

This minimizes initial research but violates the explicit project constraint and risks optimizing for human familiarity rather than autonomous operability.

### B. Compare published feature tables only — reject

Feature presence does not establish reliable AI operation, recoverability, repository concurrency, deterministic evidence, or CI cost.

### C. Build a large prototype in every engine — reject

Too expensive and likely to create accidental architecture lock-in. Use small representative spikes that isolate the project-specific risks.

### D. Use one weighted total score and select the maximum — reject

A high aggregate can hide a fatal weakness such as non-reproducible automation or unmanageable repository conflicts. Use gates + dimensions + confidence + sensitivity + Pareto analysis.

### E. Require identical source code/architecture across engines — reject

Unfairly penalizes native strengths and may create unnatural implementations. Hold **scenario intent, evidence contract, inputs, and acceptance conditions** constant; allow candidate-native implementations with documented deviations.

### F. Delay all engine investigation until final game design is complete — reject

Some technical evidence can be gathered now without selecting final gameplay details. The spike suite should use abstract representative mechanics and infrastructure risks, not final content.

## 7. Decision vocabulary

- **candidate** — engine/runtime option admitted to comparative evaluation;
- **primary-source evidence** — current official engine/vendor/project documentation, release notes, licensing/terms, or source repository material relevant to a claim;
- **spike** — bounded disposable implementation/evidence experiment, not production architecture;
- **common harness** — shared scenario intent, inputs, evidence schema, run rules, and comparison boundaries;
- **hard gate** — criterion whose evidenced failure disqualifies a candidate for the current project assumptions;
- **dimension score** — bounded comparative judgment supported by evidence; not authority by itself;
- **confidence** — strength/currentness/repeatability of supporting evidence;
- **manual intervention** — any step not executable by the normal autonomous tool/CLI/repository path;
- **operator burden** — agent actions/context/retries needed to complete a representative task;
- **recovery burden** — work needed to restore a valid project after intentional corruption or failed change;
- **exit cost** — expected cost of moving canonical domain/content state away from the engine if later required.

## 8. EEP-D1 — Decision stages

The engine program has five stages.

### Stage 1 — Candidate discovery

Build a bounded candidate set using current primary sources. Record why each candidate is plausible for the project and any obvious target/platform/license constraints.

No candidate receives preference for popularity or prior agent familiarity.

### Stage 2 — Admission research

For every candidate, populate the research matrix with current primary-source references. Unsupported cells remain `UNKNOWN`.

### Stage 3 — Common spikes

Run the required spike family on every admitted candidate. A candidate may be removed early only for a documented hard-gate failure that makes remaining spikes wasteful.

### Stage 4 — Comparative analysis

Compare dimensions, confidence, distributions, intervention burden, failure modes, Pareto position, and sensitivity to weighting/assumptions.

### Stage 5 — ADR

Produce an engine ADR only after independent technical review of the exact evidence set and unresolved risks.

## 9. EEP-D2 — Candidate admission and hard gates

### 9.1 Research matrix

For each candidate record at least:

```yaml
candidate_id: <stable>
engine_name: <name>
engine_version_or_channel: <exact tested/current ref>
research_date: <date>
primary_sources: []
license_and_terms: <evidence ref or UNKNOWN>
supported_host_ci_environments: <evidence or UNKNOWN>
command_line_build: <evidence or UNKNOWN>
command_line_tests: <evidence or UNKNOWN>
headless_or_nonvisual_execution: <evidence or UNKNOWN>
project_asset_representation: <evidence or UNKNOWN>
editor_automation_surface: <evidence or UNKNOWN>
profiling_observability: <evidence or UNKNOWN>
packaging_targets: <evidence or UNKNOWN>
localization_accessibility_workflows: <evidence or UNKNOWN>
known_repository_generated_artifact_constraints: <evidence or UNKNOWN>
```

Current claims expire when their source/version is no longer applicable to the tested engine/toolchain.

### 9.2 Hard-gate candidates

A candidate is disqualified for the current project assumptions only when measured or authoritative evidence establishes one of these conditions and no bounded workaround preserves the requirement:

- normal build/test/package operation cannot be automated without routine human interactive intervention;
- representative project state cannot be kept in versioned/reconstructable repository-owned form;
- the project cannot expose a real/shared gameplay execution surface suitable for automated evidence;
- common project corruption cannot be diagnosed/recovered within a bounded autonomous workflow;
- required project/platform/license constraints are incompatible with declared targets once those targets exist;
- repository/project representation creates unavoidable ownership conflicts that collapse planned concurrency;
- a required evidence surface cannot be produced and no equivalent oracle is available.

A missing feature is not automatically a hard failure if a narrow maintainable project-owned adapter can satisfy the requirement. Adapter cost becomes evidence.

### 9.3 Unknown is not pass

`UNKNOWN` never becomes `PASS` by omission. The ADR must list every unresolved high-risk unknown and either close it or explain why the decision remains reversible despite it.

## 10. EEP-D3 — Common spike harness

### 10.1 Harness identity

Every comparative run records:

```yaml
engine_eval_run_version: <schema version>
candidate_id: <stable>
engine_and_toolchain: <exact versions>
work_sha: <spike repository SHA>
scenario_id: <stable>
scenario_version: <version>
host_environment: <image/os/tool refs>
inputs_hashes: []
commands: []
expected_outputs: []
run_index: <integer>
start_end_or_duration: <measurement>
artifacts: []
manual_interventions: []
retries: []
warnings_failures: []
resource_metrics: {}
operator_trace_ref: <artifact>
primary_source_refs: []
```

### 10.2 Fairness rule

Hold constant:

- scenario intent;
- functional acceptance conditions;
- evidence required;
- approximate content/scene scale;
- run repetition count;
- host resource class where practical;
- branch/concurrency pattern;
- failure injection.

Allow candidate-specific:

- project layout;
- native scene/resource representation;
- scripting language/toolchain;
- test framework;
- build command;
- editor automation mechanism;
- equivalent native profiling/capture method.

Every candidate-specific deviation is recorded so convenience does not masquerade as capability.

### 10.3 Repetition

One successful run is insufficient for reliability claims. Representative spikes should include clean and incremental runs, repeated execution, and at least one fresh-agent continuation where applicable.

## 11. EEP-D4 — Required representative spikes

These are experiment definitions, not implementation backlog authorization.

### S1 — Clean bootstrap and command-line build

A fresh environment obtains the repository, installs/resolves the declared toolchain through the candidate procedure, imports/compiles as required, builds, and runs a minimal executable using scripted commands.

Measure setup actions, hidden state, cache dependence, clean build time, incremental build time, failures, diagnostics, and retained artifacts.

### S2 — Editor-independent bounded feature change

A fresh agent adds or changes a small player-visible/state-visible behavior using repository-owned files and normal tools without relying on a human driving the editor.

If editor automation is required, it must be invokable and inspectable by the agent and its generated changes must be deterministic/reviewable enough for source control.

### S3 — Headless/shared-kernel deterministic evidence

Create a tiny canonical state + explicit seed/input sequence and execute a gameplay-relevant transition through the real/shared rules surface. Repeat and compare state/events/hashes under the declared determinism boundary.

This does not require deterministic rendering.

### S4 — Save/load and schema-change probe

Persist a small logical world, load it, validate state, make one controlled schema/content change, exercise a migration or compatibility path, and emit diagnostics for incompatible input.

The spike tests engine impedance and tooling, not the final save architecture.

### S5 — Parallel content/scene/resource change and merge

From one base, create several non-overlapping agent changes plus one intentionally overlapping change across representative project/content resources. Merge/reconcile them using normal repository tooling.

Measure conflict count, semantic conflict detectability, generated-file churn, reviewability, and recovery burden.

### S6 — Controlled player-surface capture in CI

Launch the representative scene/state from command line or automation, reach a known state, capture screenshot/video/frame evidence with scenario/build identity, and distinguish capture failure from gameplay-state failure.

### S7 — Malformed project/asset recovery

Inject bounded failures such as broken reference, malformed resource, missing asset, stale import metadata, or invalid project setting appropriate to the candidate. A fresh agent diagnoses from repository/CLI evidence and repairs without undocumented human editor rescue.

### S8 — Runtime observability and profiling

Run a representative workload and obtain structured or parseable timing/memory/trace evidence sufficient to locate an intentionally injected performance problem. Record native-tool versus adapter effort.

### S9 — Packaging/release-shaped build probe

Produce at least one declared representative distributable through CI automation, record artifact identity and reproducibility inputs, and exercise a failed-package diagnostic. Final target platforms remain a later decision.

### S10 — Fresh-agent continuation benchmark

Agent A leaves a partially complete spike with branch, evidence, and handoff. A fresh Agent B, using repository state only, diagnoses current status, completes it, reruns evidence, and produces a reviewable diff.

This is crucial because session disposability is a first-class project constraint.

## 12. EEP-D5 — Comparative rubric

### 12.1 Dimensions

Score only from attached evidence. Candidate dimensions:

1. **autonomous operability** — CLI/scripted workflows, hidden interactive dependencies, operator burden;
2. **repository/source-control ergonomics** — stable diffs, generated churn, text/binary ownership, merge behavior;
3. **test and evidence integration** — real/shared-kernel execution, headless/controlled runs, structured outputs;
4. **determinism/control** — ability to establish the project-required deterministic gameplay envelope;
5. **recoverability** — diagnostics and repair after malformed assets/project state;
6. **observability** — logs, state inspection, profiling, trace/capture support;
7. **build/CI economics** — setup, clean/incremental build distributions, cache behavior, artifact size/cost drivers;
8. **content/extensibility ergonomics** — high-volume data/assets/scenes and validation/compile hooks;
9. **tooling/API stability** — documented automation surfaces and versioned behavior;
10. **packaging/platform path** — evidence for declared target class, once targets exist;
11. **governance/legal/terms** — license, automation/tool/service constraints, provenance implications;
12. **exit/reversibility** — how strongly domain state/content becomes trapped in engine-specific forms.

### 12.2 Evidence grade

For each dimension record:

```text
PASS_STRONG      repeated measured evidence + clear reproducibility
PASS_BOUNDED     evidence supports current need with known limits
MIXED            material strengths and weaknesses / unstable evidence
FAIL             evidenced requirement failure
UNKNOWN          insufficient or stale evidence
```

Also record confidence and evidence refs.

### 12.3 Numeric scoring

A bounded numeric score may be used for sorting/sensitivity analysis **after** qualitative evidence, but:

- weights are versioned assumptions;
- hard gates cannot be compensated by unrelated scores;
- `UNKNOWN` carries an explicit uncertainty penalty;
- reviewers see raw dimensions before aggregate score;
- decision sensitivity is recomputed across plausible weight sets;
- close candidates remain a Pareto/tournament decision rather than false decimal precision.

### 12.4 Cost normalization

Do not compare only machine time. Include:

- agent actions/retries;
- context/reconstruction burden;
- adapter/tooling code required;
- flaky reruns;
- manual interventions;
- merge/recovery labor;
- CI compute/storage;
- evidence extraction effort.

## 13. EEP-D6 — Evidence and observability contract

### 13.1 Evidence bundle

Each candidate should end with an evidence index containing:

- research matrix and source versions;
- spike source/work SHAs;
- run manifests;
- build/test logs;
- state/hash/replay-like evidence where relevant;
- visual captures;
- profiling artifacts;
- merge/conflict trials;
- failure/recovery traces;
- continuation benchmark result;
- run distributions;
- known invalid/flaky runs;
- manual-intervention ledger;
- unresolved unknowns;
- scored rubric + confidence;
- cost summary.

### 13.2 Evidence integrity

Failed or inconclusive runs remain visible. Re-running until success and discarding failures is invalid evidence.

### 13.3 Current-source boundary

Primary documentation is evidence for documented capability/constraint, not proof that Everfield's workflow works. Spike evidence is required for project-specific behavior.

### 13.4 No hidden editor proof

A successful interactive-editor demonstration is supplemental unless the normal agent pipeline can reproduce the operation autonomously and inspect the resulting project state.

## 14. EEP-D7 — Engine ADR protocol

The eventual ADR should contain:

```yaml
adr_id: <stable>
decision_state: PROPOSED | ACCEPTED | SUPERSEDED
candidate_evidence_set: <exact refs>
engine_choice: <candidate>
qualified_alternatives: []
hard_gate_results: {}
key_dimension_results: {}
weight_and_sensitivity_version: <ref>
independent_review_ref: <ref>
primary_reasons: []
accepted_tradeoffs: []
unresolved_risks: []
required_followup_evidence: []
exit_cost_and_mitigation: []
reopen_conditions: []
```

### 14.1 ADR acceptance requirements

An engine ADR cannot be accepted merely because one candidate has the top aggregate score. Require:

- no unresolved hard-gate failure;
- current evidence for material candidate-specific claims;
- all mandatory spikes completed or explicitly waived by reviewed evidence showing non-applicability;
- failed/inconclusive runs accounted for;
- independent `W1-REV-TECH`-derived scrutiny or its later canonical successor;
- sensitivity analysis showing whether the decision is robust to reasonable weight changes;
- explicit reasons for rejecting other qualified Pareto candidates;
- exit/reopen plan.

### 14.2 Conditional decision

The ADR may choose a candidate conditionally for Milestone Zero while retaining a mandatory checkpoint before broader implementation if unresolved risk can only be measured on a slightly larger slice.

Conditional selection must name the falsifier and exit path.

## 15. EEP-D8 — Factory-first interpretation

The engine is infrastructure for two coupled products: the game and the autonomous factory.

The preferred candidate should make these loops cheap and reliable:

```text
fresh agent
 -> inspect task/repository
 -> make bounded change
 -> build/test/headless-run
 -> inspect state/logs/captures
 -> repair failures
 -> commit/handoff
 -> independent reviewer reproduces
 -> squash integration later
```

A candidate that produces excellent runtime output but requires frequent invisible editor state or human repair is structurally weak for Everfield. A candidate that is automation-friendly but cannot meet eventual game/runtime/platform needs is also weak. Both sides remain evidence dimensions.

## 16. Interfaces and dependencies

### 16.1 Runtime/data architecture

The engine program must expose evidence to later runtime/data synthesis rather than deciding canonical state representation inside the engine spike. Spikes should test whether engine-specific facilities can remain adapters around project-owned domain state where later architecture requires it.

### 16.2 Evaluation system

The common spike evidence schema should be consumable by later CI/evaluator planning: exact build/work identity, scenario, state evidence, capture, performance, logs, and failures.

### 16.3 Factory/governance

Candidate research and runs need provenance, issue/work ownership, immutable evidence refs, current-source recording, and independent review. Tool/service permissions must not be silently expanded for a favored engine.

### 16.4 Game design

Engine comparison should use representative abstract interactions and scale envelopes, not freeze final game mechanics, visual style, calendar, balance, or content.

## 17. Failure modes and reviewer probes

| Failure mode | Required probe/response |
|---|---|
| winner chosen by familiarity | remove familiarity as evidence; rerun rubric from attached sources/runs |
| official docs treated as operational proof | require project-specific spike |
| different candidates get easier spikes | compare harness deviations and rerun equivalent acceptance |
| successful runs cherry-picked | preserve all valid attempts/failures/retries |
| one scalar hides fatal weakness | enforce hard gates and raw-dimension review |
| spike architecture leaks into production | mark spike code disposable; later runtime synthesis owns architecture |
| editor automation works only with hidden state | clean environment + fresh-agent replay |
| merge test uses only trivial text files | include representative scene/resource/content ownership surfaces |
| build benchmark sampled once | repeated clean/incremental distributions |
| malformed project needs human repair | record intervention and treat recoverability accordingly |
| candidate needs large custom adapter | charge adapter build/maintenance/review burden |
| engine update invalidates evidence | source/tool version change triggers affected reruns |
| ADR becomes permanent ideology | explicit checkpoint and reopen conditions |

## 18. Required experiments

The following remain **UNRUN** after this proposal and are required evidence before an accepted engine ADR:

1. `EEP-X1 Candidate discovery/current-source matrix` — bounded candidate set; current primary sources; material unknowns.
2. `EEP-X2 Clean bootstrap/build reliability` — S1 repeated across candidates.
3. `EEP-X3 Autonomous bounded edit` — S2 with clean/fresh-agent reproduction.
4. `EEP-X4 Deterministic/shared-kernel evidence` — S3 repeated and state compared.
5. `EEP-X5 Persistence/schema probe` — S4.
6. `EEP-X6 Parallel merge/conflict trial` — S5 with multiple branches and intentional overlap.
7. `EEP-X7 CI visual capture` — S6.
8. `EEP-X8 Malformed-project recovery` — S7.
9. `EEP-X9 Observability/performance` — S8 with injected diagnostic target.
10. `EEP-X10 Packaging` — S9 for a later-declared representative target class.
11. `EEP-X11 Continuation benchmark` — S10 with genuinely fresh continuation context when available; otherwise degraded mode must be labeled.
12. `EEP-X12 Cost/reliability distribution` — repeated build/test/capture/recovery runs under representative change classes.
13. `EEP-X13 Decision sensitivity` — compare plausible weight sets, hard gates, Pareto frontier, and unknown penalties.

No experiment result is implied by this document.

## 19. Open questions and deferred choices

Remain unresolved until evidence or downstream planning:

- exact candidate engine set;
- exact tested engine versions;
- final target platforms;
- final programming/runtime language choices;
- exact deterministic gameplay boundary;
- whether engine physics participates in canonical gameplay state;
- exact project/content schema and compiler;
- final visual pipeline/rendering needs;
- final performance budgets;
- acceptable CI cost envelope;
- acceptable custom adapter/tooling maintenance cost;
- exact protected engine benchmark variants;
- how much Milestone Zero evidence is required before final versus conditional ADR acceptance.

## 20. Reopen conditions

Reopen the engine decision or this evaluation protocol if:

- selected engine/toolchain materially changes or deprecates the automation surface used by the factory;
- a previously unknown hard-gate failure appears;
- CI/build/recovery cost grows beyond the accepted evidence envelope;
- representative merge-conflict or content-scale behavior diverges materially from spikes;
- platform targets change incompatibly;
- licensing/terms/tool-service constraints change materially;
- runtime architecture requires a capability not included in the original spike set;
- deterministic/player-surface evidence cannot be reproduced by independent reviewers;
- engine-specific state begins trapping canonical domain/content semantics beyond accepted exit assumptions;
- fresh-agent continuation repeatedly fails because of candidate-specific hidden state;
- decision sensitivity shows the choice was not robust to reasonable project priorities.

## 21. Required independent critique

`W1-REV-TECH` must independently attack:

- whether the harness is actually equivalent across candidates;
- whether hard gates are too strict, too weak, or easy to game;
- whether autonomous/editor/concurrency/recovery evidence is sufficient;
- whether current claims are primary-sourced or measured;
- whether failed runs and adapter burden are preserved;
- whether the scoring/sensitivity model can launder a preferred engine;
- whether the ADR remains reversible;
- whether the spike suite meaningfully represents the AI-native factory rather than a conventional human workflow.

## 22. Downstream work unblocked

Once this proposal is `REVIEW_READY`, it unblocks its declared input edge to `W1-REV-TECH`.

It does **not** authorize engine selection, engine implementation, gameplay implementation, extra Wave 1 issues, or canonicalization.