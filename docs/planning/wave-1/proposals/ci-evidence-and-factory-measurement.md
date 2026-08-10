# CI, Evidence Topology, and Factory Measurement — Wave 1 Proposal

**Mission:** `W1-FAC-04`  
**State:** PROPOSED / NON-CANONICAL  
**Role:** CI / evidence / factory-measurement planner  
**Required reviews:** `W1-REV-FAC`, `W1-REV-TECH`

## Review Index

**Core recommendation.** Treat CI as Everfield’s machine sensorium, not a green/red checkbox. Every material run should emit a structured **Run Report** bound to exact candidate work SHA, base, environment, workflow/evaluator versions, inputs, check/scenario/invariant results, artifact hashes, warnings, coverage gaps, and trust profile. Acceptance consumes evidence bundles; a dashboard status is only a projection.

**Evidence topology.** Store large evidence outside ordinary agent context behind immutable/content-addressed refs; keep compact indexes in task/review artifacts. Evidence has typed retention classes: `TRANSIENT_DIAGNOSTIC`, `TASK_EVIDENCE`, `CANONICAL_PROVENANCE`, `PROTECTED_EVALUATION`. Canonical verification/integration records must retain or reference enough evidence to replay why a result passed even after task-branch cleanup.

**CI classes.** `PRECHECK` producer-local evidence; `PR_FAST` deterministic build/unit/schema/static checks; `INTEGRATION` real-kernel/executable scenarios, persistence/replay/interface checks; `PROTECTED_VERIFY` held-out/independently controlled gates where gaming risk warrants it; `DEEP_PERIODIC` fuzzing, long simulations, synthetic-player/exploit/performance campaigns; `FACTORY_BENCHMARK` seeded tasks/defects for protocol changes. Task contracts choose required classes; protected/deep checks are not universal bottlenecks.

**Flake policy.** Check outcomes are `PASS | FAIL | FLAKY | INCONCLUSIVE | NOT_RUN`. Re-running does not erase prior attempts. A required flaky/inconclusive check is not PASS; acceptance needs stable replacement evidence or an explicit reviewed quarantine/change to the gate. Quarantine records owner, reason, impact, replacement evidence, expiry/reopen condition, and a defect/remediation route. Do not reward “green after N retries.”

**Factory measurement.** Measure a vector: verified outcome throughput, stage cycle/queue time, READY frontier, WIP, review/verifier escape, reopen/rollback, handoff recovery, conflict/recovery, context/evidence cost, CI reliability, protected-oracle yield, and integration latency. Normalize by task/evidence class where possible. No aggregate productivity score controls agents.

**Protocol-change benchmark.** Factory/review/evaluator/scheduler changes are judge-affecting. Compare versioned protocols on representative tasks and seeded defects with repeated paired runs, exact environments, evidence cost, completion/escape/recovery metrics, and rollback criteria. A protocol does not win because it is faster if escapes/conflicts/trust debt worsen materially.

**Primary attacks.** retry laundering; evidence links that rot; giant run reports flooding context; producer controls sole oracle; hidden evaluator drift; protected evidence too opaque to debug; CI outage silently bypassed; benchmark overfitting; metric gaming; factory “throughput” counting low-value issue churn; retained evidence leaking sensitive/held-out material; GC deleting proof; non-determinism mislabeled as flake.

**Experiments.** run-report reconstruction; deterministic replay; injected flake classification; evidence retention/GC recovery; protected-evidence access probe; reward-hacking challenge; factory protocol A/B with seeded defects; CI outage/reconciliation; context-index retrieval benchmark; benchmark-drift audit.

## 1. Status

This proposal defines the semantic CI/evidence/measurement model required before high-throughput implementation. It does not select a CI vendor, artifact store, database, observability product, or exact protected-evidence permission topology.

The proposal supplies evidence/report interfaces to control-plane and trust work; W1-REV-FAC/W1-REV-TECH should attack both factory incentives and technical reproducibility.

## 2. Scope

This proposal covers:

1. structured run reports;
2. evidence artifact identity/provenance;
3. CI class taxonomy and task gating;
4. deterministic/replay evidence;
5. flake/retry/quarantine policy;
6. protected evidence interface;
7. evidence indexing/context boundaries;
8. retention and garbage-collection requirements;
9. factory metrics and diagnostic interpretation;
10. versioned factory benchmark protocol;
11. protocol-change measurement/adoption/rollback;
12. observability/failure recovery.

## 3. Inputs and source basis

### 3.1 Observed repository evidence

The authoritative packet establishes:

- the autonomous-factory mandate requires independently checkable evidence, machine-consumable handoffs, review/verification, factory benchmarks, observed factory metrics, explicit self-improvement governance, and no routine human approval;
- Evaluation and Evidence requires CI as structured sensorium; real executable/kernel integration evidence; deterministic evidence where practical; declarative/golden scenarios; protected evaluation surfaces; independent test authorship; player + simulation surfaces; semantic coverage; synthetic players; multidimensional quality signals; evaluator versioning; disagreement handling; and explicit Goodhart resistance;
- the research agenda calls for evidence provenance, structured run reports, CI taxonomy, flake policy, artifact retention, protected evidence, semantic/subjective evaluation, factory metrics, and benchmarks;
- the planning deliverables require machine-readable CI run-report schema, check taxonomy, flake policy, artifact retention, baseline/performance/visual evidence, semantic coverage, synthetic players, protected scenarios, evaluator versioning, and factory metrics/benchmarks before implementation readiness.

### 3.2 Inference

A CI check result cannot be durable acceptance evidence unless a later verifier can identify what candidate/environment/evaluator produced it and inspect the relevant artifacts. Conversely, loading raw logs/screenshots/traces into every agent context would violate context budgeting. Evidence therefore needs a durable artifact graph plus compact indexes.

### 3.3 Recommendation

Use the report/artifact/retention/benchmark model below and let later technical work choose implementation storage only after the semantics are reviewed.

## 4. Goals

For any material claim, an agent should be able to determine:

- which exact candidate/base/environment was exercised;
- which checks/scenarios/evaluators ran and which did not;
- which evidence artifacts prove or contradict the claim;
- whether evidence is deterministic, statistical, subjective, protected, producer-authored, or independent;
- evaluator/rubric/version identity;
- retry/flake history rather than only final color;
- known coverage gaps and warnings;
- what evidence must remain reachable for verification/canonical provenance;
- whether a factory protocol change improved verified outcomes rather than activity volume;
- how to reproduce or reopen an old judgment after evaluator/product drift.

## 5. Non-goals

This proposal does **not**:

- define one universal CI pipeline for every task class;
- require every check on every PR;
- choose exact retention durations without measured cost/risk;
- select cloud/vendor/tooling architecture;
- claim deterministic execution is possible for every evaluator/system;
- reduce game/factory quality to a single score;
- let retries convert instability into acceptance;
- make protected evidence completely opaque/unversioned;
- install CI workflows or modify protected evaluator permissions now;
- authorize gameplay implementation.

## 6. Constraints

1. Material acceptance claims must bind inspectable evidence.
2. Important integration claims should exercise the real executable or shared production kernel when the claim depends on integration.
3. Deterministic/replayable evidence is preferred where practical; unavoidable nondeterminism must be explicit.
4. Player-facing and simulation/state surfaces both matter for gameplay evidence.
5. Producer-authored tests may contribute but cannot be the sole oracle for important claims.
6. Protected evaluator surfaces require independent/meta-governed mutation paths.
7. Evidence records bind exact candidate/base/environment/evaluator versions.
8. `FLAKY`, `INCONCLUSIVE`, and `NOT_RUN` are distinct from `PASS`.
9. Retry history is retained; retry count itself is not quality evidence.
10. Evidence artifacts should be content-addressed/immutable or snapshotted sufficiently for replay.
11. Large evidence stays outside default agent context behind indexes/refs.
12. Garbage collection cannot delete evidence required to explain canonical decisions.
13. Metrics are diagnostic; factory policy changes require benchmark evidence and review.
14. Normal CI/evidence disagreement does not become a routine human gate.

## 7. Assumptions

Provisional assumptions:

- A single extensible Run Report envelope can cover planning, code, game, visual, performance, and factory evidence while allowing task-specific sections.
- Content-addressed artifacts plus compact indexes are sufficient for review/context efficiency.
- Flake classification can be based on exact-input/environment attempt history plus explicit nondeterminism boundaries rather than arbitrary retry count.
- Retention should be class/event-based before fixed time durations are known.
- A small, representative factory benchmark suite with seeded defects is more useful than raw production metrics alone for protocol changes.
- Protected checks can expose structured failure evidence without exposing every held-out case/input.

## 8. Alternatives considered

### 8.1 Green/red required checks only — rejected

A color omits candidate/environment/evidence/evaluator provenance and cannot explain whether important scenarios were skipped, flaky, or gamed.

### 8.2 Store all raw evidence in Git — rejected as default

Large traces, captures, profiles, and repeated CI artifacts would bloat repository history and agent context. Keep compact manifests/indexes in Git and immutable external artifact refs where appropriate.

### 8.3 Keep evidence only in ephemeral CI logs — rejected

Canonical/review decisions can outlive log retention and become unverifiable. Material evidence needs retention by authority class.

### 8.4 Retry flaky checks until green — rejected

This hides reliability risk and biases final status. Attempts remain evidence; instability must be classified and resolved/quarantined explicitly.

### 8.5 Block all work on any flake — rejected

A low-impact quarantined check should not freeze unrelated work indefinitely. Quarantine requires scoped impact, replacement evidence, owner, and remediation; gates affected by the flake remain blocked until sufficient evidence exists.

### 8.6 One factory throughput metric — rejected

Issue/commit/task count can be gamed and ignores review escapes, recovery, conflicts, and queue debt. Use a diagnostic vector and benchmark controlled protocol changes.

### 8.7 Hidden tests are the primary quality system — rejected

Visible specifications/invariants aid development and debugging. Protect only high-Goodhart subsets, while versioning and auditing protected oracles.

## 9. Evidence object model

### 9.1 Run Report

Every material CI/evaluation execution should emit a machine-readable report conceptually like:

```yaml
run_report_version: 1
run_id: <stable>
run_class: PRECHECK | PR_FAST | INTEGRATION | PROTECTED_VERIFY | DEEP_PERIODIC | FACTORY_BENCHMARK
trigger: <pr/push/manual/scheduled/verifier/benchmark>
candidate:
  work_sha: <sha>
  branch_head_sha: <sha>
  base_main_sha: <sha>
environment:
  environment_id: <stable config/version>
  platform: <when relevant>
  toolchain_refs: []
  build_config: <ref>
workflow:
  workflow_id: <stable>
  workflow_version: <sha/version>
inputs:
  artifact_refs: []
  scenario_ids: []
  seeds: []
results:
  build: []
  tests: []
  scenarios: []
  invariants: []
  integration: []
  persistence_replay: []
  architecture: []
  content_validation: []
  performance: []
  visual: []
  simulation: []
  synthetic_players: []
  telemetry: []
  factory_checks: []
coverage:
  semantic_dimensions: {}
  known_gaps: []
warnings: []
evaluator_refs: []
artifact_manifest_ref: <immutable ref>
trust_profile: <producer/independent/protected metadata>
summary_result: PASS | FAIL | FLAKY | INCONCLUSIVE
```

The report envelope is stable; task-specific result entries can use separately versioned schemas.

### 9.2 Evidence Artifact

```yaml
evidence_id: <stable>
kind: LOG | TRACE | TEST_REPORT | SCENARIO_TRACE | STATE_SNAPSHOT | REPLAY | SAVE | SCREENSHOT | VIDEO | PROFILE | METRIC_SERIES | REVIEW | OTHER
content_hash: <hash>
storage_ref: <immutable or snapshotted locator>
produced_by_run: <run id>
producer_or_evaluator: <identity/version>
input_hashes: []
candidate_work_sha: <sha>
visibility: NORMAL | PROTECTED
retention_class: TRANSIENT_DIAGNOSTIC | TASK_EVIDENCE | CANONICAL_PROVENANCE | PROTECTED_EVALUATION
redaction_or_access_policy_ref: null
```

Artifact location is not identity; content hash + production/run provenance establishes what evidence was judged.

### 9.3 Check result

Each check/scenario record should distinguish:

```text
PASS        deterministic/declared acceptance satisfied
FAIL        observed evidence violates acceptance
FLAKY       materially different results across equivalent declared inputs/environment beyond accepted nondeterminism
INCONCLUSIVE evidence insufficient/infra instability/ambiguous evaluator prevents valid verdict
NOT_RUN     check did not execute or was intentionally not applicable
```

A task contract states which results are required and which classes may satisfy one another.

## 10. CI taxonomy

### 10.1 `PRECHECK`

Fast producer-local/task-branch checks before handoff. Useful evidence, not an independent oracle.

Examples during planning/code phases:

- schema/format validation;
- local/unit/property checks;
- artifact/link/SHA validation;
- task-specific static checks.

### 10.2 `PR_FAST`

Deterministic, relatively fast checks expected on most integration PRs for the relevant task class:

- build/compile;
- unit/property/static checks;
- planning artifact schemas/link integrity;
- dependency/cycle/output ownership checks;
- focused task tests.

Target: fast feedback and obvious integration safety, not complete quality proof.

### 10.3 `INTEGRATION`

Evidence for claims requiring real subsystem/executable behavior:

- production executable/shared gameplay kernel scenarios;
- end-to-end integration scenarios;
- save/load/replay/migration;
- interface/architecture validation;
- controlled visual captures;
- representative performance checks.

### 10.4 `PROTECTED_VERIFY`

High-Goodhart/held-out evidence controlled by verifier/protected policy:

- held-out scenarios;
- independently authored invariants/tests;
- architecture/reward-hacking probes;
- verifier configuration/thresholds;
- selected golden/protected game/factory benchmarks.

Protection is selective and versioned; detailed failure diagnostics should be exposed as far as safely possible.

### 10.5 `DEEP_PERIODIC`

Expensive or probabilistic evidence unsuitable for every PR:

- long fuzz/property campaigns;
- soak/performance/memory runs;
- large economy/progression simulations;
- synthetic-player populations;
- exploit search;
- semantic coverage campaigns;
- wide visual/reference sweeps.

A deep finding can reopen already-integrated assumptions through canonical defect/replanning routes; periodic does not mean advisory-only.

### 10.6 `FACTORY_BENCHMARK`

Controlled tasks/scenarios for testing the autonomous factory itself:

- seeded implementation/planning defects;
- continuation/handoff tasks;
- claim/recovery races;
- merge/conflict tasks;
- evaluator/reward-hacking traps;
- planning/dependency graph cases;
- visual/gameplay judgment benchmarks.

Factory benchmark artifacts and expected-defect ground truth may require protected access.

## 11. Evidence gating by task contract

Do not hard-code one pipeline. A task compiler should declare required evidence classes and concrete checks.

Example planning-task gate:

```yaml
required:
  - artifact_schema
  - exact_dependency_refs
  - acceptance_self_check
review_route:
  - ADVERSARIAL_REVIEW
canonicalization_gate:
  - INDEPENDENT_VERIFICATION
```

Example future gameplay feature gate:

```yaml
required:
  - PR_FAST: [build, unit, invariants]
  - INTEGRATION: [real_gameplay_scenario, save_load_if_relevant]
conditional:
  - visual_change -> controlled_visual_evidence
  - performance_sensitive -> benchmark
  - high_goodhart_risk -> PROTECTED_VERIFY
```

The task/result should record `NOT_APPLICABLE` through contract logic rather than silently omitting a relevant check.

## 12. Determinism, replay, and nondeterminism

For reproducible scenarios, record where applicable:

```text
candidate/build SHA
canonical initial state/snapshot hash
random seed(s)
action/input sequence
simulation clock/time controls
external dependency versions
final state/event hashes
telemetry/log refs
visual artifact refs
```

If full determinism is impossible or undesirable:

- declare nondeterministic dimensions;
- bound expected variance/statistical distribution;
- record repeated attempts rather than one representative run;
- distinguish infrastructure variance from product/evaluator variance;
- use confidence/distribution evidence without treating a p-value or confidence scalar as sole authority.

Do not label unexplained nondeterminism as “flake” merely to quarantine it.

## 13. Flake, retry, and quarantine policy

### 13.1 Retry rules

- record every attempt and its exact candidate/environment/input/evaluator version;
- retries are evidence collection, not status erasure;
- an infrastructure failure can be rerun, but the original failure remains in the run lineage;
- a later PASS does not automatically make earlier FAIL irrelevant;
- result aggregation rules must be check-specific and versioned.

### 13.2 Flake classification

Classify `FLAKY` only when equivalent declared conditions produce materially inconsistent check results beyond accepted nondeterminism **and** evidence indicates the instability lies in test/product/environment interaction rather than a known deterministic product defect.

Unknown cause defaults to `INCONCLUSIVE`/investigation, not automatic flake.

### 13.3 Required flaky checks

A required gate whose authoritative check is FLAKY/INCONCLUSIVE cannot report PASS merely by retrying until green. Options:

1. fix the check/product/environment and obtain stable evidence;
2. obtain an explicitly allowed independent replacement evidence path;
3. review and quarantine/change the gate through a judge-affecting policy change.

### 13.4 Quarantine record

```yaml
quarantine_id: <stable>
check_id: <id/version>
reason: <evidence-backed>
first_seen_run: <id>
last_reproduced_run: <id>
affected_claims_or_tasks: []
severity: <qualitative>
replacement_evidence_required: []
owner_or_route: <task/domain>
expiry_or_review_condition: <condition>
remediation_ref: <task/candidate>
```

Quarantine does not mean ignore: track age, impact, and whether it masks required evidence.

## 14. Player and simulation evidence

For game-facing features, CI/evaluation should pair:

**Player surface**
- rendered state/screenshots/video;
- interaction affordances/feedback;
- audio/visual/accessibility evidence;
- input/task traces.

**Simulation surface**
- canonical state/events;
- invariants;
- progression/economy/world telemetry;
- performance/resource signals;
- save/replay state.

Acceptance should not infer one from the other. A screenshot can be visually correct while state is wrong; state can be correct while presentation is unusable.

## 15. Semantic coverage

Coverage should eventually index **game/system possibility-space dimensions**, not just code lines:

- interaction verbs;
- item/state transitions;
- quest objective/branch types;
- region/gate/progression transitions;
- NPC schedule/social-state transitions;
- production/automation operations;
- save-schema/migration variants;
- economy/progression graph regions;
- accessibility/input-mode scenarios;
- failure/recovery states.

A Run Report can reference a versioned semantic coverage schema and list dimensions exercised/missing. Coverage is diagnostic: 100% of a poorly chosen taxonomy is not proof of quality.

## 16. Evidence indexing and context boundaries

Ordinary agents should not load raw CI corpus.

Use a compact **Evidence Index** per task/review/candidate:

```yaml
candidate_work_sha: <sha>
run_reports: []
required_claims:
  <claim_id>:
    status: PASS | FAIL | FLAKY | INCONCLUSIVE | NOT_RUN
    evidence_refs: []
    evaluator_refs: []
coverage_gaps: []
known_flakes: []
protected_results: []
large_artifact_manifest_refs: []
```

Context policy:

1. load index + relevant claim rows first;
2. retrieve raw artifact only for a concrete question/failure;
3. preserve artifact hash/ref in findings;
4. never paste giant logs/traces into durable handoff when a stable artifact ref suffices;
5. if protected, expose only the authorized summary/detail level.

## 17. Retention model

Use authority/event-based classes before choosing fixed durations.

### `TRANSIENT_DIAGNOSTIC`

Reproducible low-value logs/intermediates not used by a durable decision. May expire after reproducibility/retention policy permits.

### `TASK_EVIDENCE`

Evidence supporting an open/reviewable task or unresolved defect. Retain through task review/revision/integration and any declared reopen window.

### `CANONICAL_PROVENANCE`

Evidence directly supporting verification/canonicalization/release-critical decisions or irreversible migration. Must remain reachable as long as the authority record depends on it, or be replaced by an independently verifiable durable summary/snapshot under explicit retention policy.

### `PROTECTED_EVALUATION`

Held-out/protected scenarios, benchmark ground truth, evaluator configuration, or artifacts whose disclosure changes trust. Retention/access governed by the protected evaluation owner/meta-review policy.

Garbage collection must prove no retained authority/evidence index references an artifact scheduled for deletion. Storage lifecycle changes are evidence-governance changes, not ad hoc cleanup.

## 18. Factory measurement model

Measure the system that turns tasks into verified/canonical outcomes, not agent activity.

### 18.1 Flow / queue

- READY frontier width by class/domain;
- active WIP by producer/review/verification/integration;
- queue age/wait time by stage;
- cycle time from claim → role boundary → accepted integration;
- tasks/episodes per accepted result;
- stale/orphan/handoff recovery incidents;
- integration conflict/rebase/base-drift failures.

### 18.2 Quality / escapes

- producer self-check findings;
- reviewer BLOCKER/MAJOR yield;
- verifier findings missed by review;
- post-integration reopen/rollback defects;
- seeded-defect benchmark detection rate by role/class;
- specification-gaming/reward-hacking probe detections;
- protected-oracle unique yield versus visible tests.

### 18.3 Evidence / CI health

- required evidence completeness;
- run latency/cost by class;
- FLAKY/INCONCLUSIVE rate by check/version;
- retry distribution without collapsing history;
- quarantine count/age/impact;
- evidence artifact retrieval/replay success;
- evaluator version drift;
- protected artifact access violations;
- semantic coverage dimensions exercised/gaps.

### 18.4 Factory robustness

- forced-substitution/handoff continuation success;
- duplicate-claim/CAS conflict events;
- scheduler/reconciliation disagreements;
- context budget/optional retrieval behavior;
- garbage-collection mistakes prevented/escaped;
- protocol-change rollback frequency/success;
- current decisions still under DEGRADED trust debt.

Normalize/stratify by task class, risk/evidence class, and benchmark identity. Do not compare a tiny documentation fix to a cross-system implementation task as equivalent throughput units.

## 19. Factory benchmark protocol

### 19.1 Benchmark suite

Maintain a versioned suite with representative classes:

- planning/dependency tasks;
- bounded code implementation;
- integration/refactor;
- continuation/handoff recovery;
- concurrency/conflict;
- visual/UX judgment;
- gameplay/economy reasoning;
- verifier/reward-hacking traps;
- control-plane race/recovery;
- intentionally invalid or underspecified tasks.

Include seeded known defects/ground truth for some protected cases.

### 19.2 Protocol comparison

A judge-affecting factory change (scheduler, context policy, reviewer prompt/protocol, evaluator, metric, permission, handoff format) should record:

```yaml
factory_change_id: <id>
baseline_protocol_version: <ref>
candidate_protocol_version: <ref>
benchmark_suite_version: <ref>
paired_tasks: []
run_count_and_seeds: <declared>
environments: []
metrics:
  completion_validity: []
  defect_detection_escape: []
  cycle_queue_time: []
  conflicts_recovery: []
  context_evidence_cost: []
  trust_profile: []
known_confounders: []
rollback_trigger: <condition>
```

Compare repeated paired runs where stochasticity matters. A faster protocol is not an improvement if escapes, conflicts, missing evidence, or trust degradation materially worsen.

### 19.3 Benchmark evolution

Benchmarks themselves are judge-affecting:

- version changes;
- preserve historical versions needed to interpret older decisions;
- add new failure modes after real escapes;
- avoid tuning all visible benchmark tasks until they cease to represent general work;
- keep selected protected cases/variants;
- periodically test whether benchmark performance predicts production review/verifier outcomes.

## 20. Protocol-change adoption

Recommended route:

```text
defect/improvement hypothesis
 -> candidate protocol change
 -> versioned benchmark plan
 -> before/after evidence
 -> independent/meta review
 -> verification of benchmark + safety invariants
 -> bounded/staged adoption
 -> live measurement
 -> retain or rollback
```

No ordinary producer may modify a metric/evaluator/benchmark that currently blocks its work and then use the modified version as acceptance evidence without this separate route.

## 21. Baselines and performance evidence

Baseline comparison records should bind:

- baseline candidate/build SHA;
- candidate SHA;
- identical/declared workload and environment;
- metric definition/version;
- distribution/variance when relevant;
- warmup/cache/sample policy;
- raw artifact refs;
- threshold/rationale version.

Thresholds should come from requirements/benchmarks/evidence, not unexplained round numbers. A later task can establish concrete budgets once representative runtime exists.

## 22. Subjective and multimodal evidence

Subjective results should use structured protocols:

- atomic rubric dimensions;
- exact visual/gameplay evidence refs;
- randomized candidate order where comparison is used;
- multiple runs/judges where useful;
- evaluator/rubric version;
- disagreement record;
- objective failure checks before subjective scoring;
- additional evidence or competing alternatives when uncertainty is material.

Store judgments as evidence items, not as a single `fun_score` or opaque “looks good” result.

## 23. Interfaces and dependencies

| Interface | This proposal supplies | Downstream/owner |
|---|---|---|
| control plane | Run Report/evidence state semantics for required checks, flake, retention, GC, scheduler diagnostics | W1-FAC-02 |
| trust/review | evidence bundles, protected-result interface, evaluator versioning, flake/inconclusive gating | W1-FAC-03 |
| operating model | compact Evidence Index and durable artifact refs for handoff/context | W1-FAC-01 |
| automated game evaluation | run-report envelope, player/simulation evidence, semantic coverage, synthetic-player artifact/provenance requirements | W1-EVAL-01 |
| technical/runtime | reproducibility, persistence/replay, performance baseline, artifact-store requirements | W1-TEC-02 / W1-SYN-TECH |
| governance | benchmark/metric/evaluator changes are judge-affecting factory changes | W1-GOV-01 / W1-SYN-FAC |

Conflicts to resolve in synthesis:

- W1-FAC-03 owns exact trust/review class; this proposal must not make every CI result independent by definition.
- W1-FAC-02 owns check enforcement/ruleset mechanics; this proposal defines evidence semantics and required outcome states.
- Exact artifact storage/permission implementation may require technical infrastructure not yet selected.

## 24. Observability of the evidence system

In addition to factory metrics, measure the sensorium itself:

- Run Report schema validation failure;
- missing candidate/base/evaluator binding;
- evidence artifact hash/retrieval failure;
- orphaned artifacts with no index;
- indexes pointing to expired/deleted artifacts;
- protected visibility violations;
- run-result disagreement under exact replay;
- unexplained nondeterminism rate;
- FLAKY→stable remediation time;
- quarantined required gates without replacement evidence;
- CI service outage/reconciliation recovery time;
- evidence index size/context retrieval depth;
- benchmark version drift and production-predictiveness.

## 25. Bounded experiments

| ID | Experiment | Pass signal | Failure implication |
|---|---|---|---|
| FAC4-E1 | Run-report reconstruction from a finished representative task | fresh verifier can reproduce why result passed/failed from index + artifact refs without chat/raw-log preload | report/provenance schema insufficient |
| FAC4-E2 | Deterministic replay of same build/state/seed/actions | stable state/event hashes within declared determinism boundary | runtime/evidence determinism boundary unclear |
| FAC4-E3 | Inject deterministic failure, infrastructure failure, and true flake into checks with retries | policy preserves all attempts and classifies FAIL/INCONCLUSIVE/FLAKY correctly; no retry laundering | flake policy unsafe |
| FAC4-E4 | Retention/GC drill over mixed transient/task/canonical/protected artifacts | deletable artifacts removed while every authoritative evidence ref remains valid/reproducible | retention graph/GC unsafe |
| FAC4-E5 | Protected-evidence access/redaction probe | producer sees allowed diagnostics but cannot retrieve/modify protected ground truth/oracle | protected topology leaks or is unusable |
| FAC4-E6 | Reward-hacking candidate tuned to visible metric | independent/protected/multisignal evidence catches violation | Goodhart controls insufficient |
| FAC4-E7 | Factory protocol A/B on paired tasks with seeded defects | result reports quality/escape/flow/trust tradeoffs rather than one speed score; rollback criterion usable | benchmark cannot govern self-improvement |
| FAC4-E8 | CI outage + later reconciliation | task cannot fake missing evidence as PASS; queued evidence resumes/reconciles without human gate | CI availability becomes unsafe hidden bypass/deadlock |
| FAC4-E9 | Evidence-index context benchmark | reviewers answer targeted questions by loading compact indexes then minimal artifacts, without quality loss from broad preload | indexing/context boundary ineffective |
| FAC4-E10 | Benchmark-drift audit after protocol tuning | protected/new variants reveal whether benchmark gains transfer to production-like tasks | benchmark overfit / Goodhart risk |

## 26. Failure modes and defenses

### Green-status compression
**Failure:** one checkmark hides missing/skipped/flaky/irrelevant evidence.  
**Defense:** structured report + per-claim evidence index + explicit result enums.

### Retry laundering
**Failure:** repeated run eventually green and earlier failures vanish.  
**Defense:** immutable attempt lineage; FLAKY/INCONCLUSIVE distinct from PASS.

### Flake quarantine as bypass
**Failure:** required evidence disappears under “quarantine.”  
**Defense:** replacement evidence + impact scope + owner/remediation + expiry/review condition.

### Ephemeral evidence loss
**Failure:** canonical PASS cites logs/artifacts later deleted.  
**Defense:** retention classes + immutable hashes/refs + GC reachability validation.

### Evidence context flood
**Failure:** reviewers load all logs/captures and miss key claims.  
**Defense:** Evidence Index first, targeted retrieval, stable large-artifact refs.

### Producer oracle monoculture
**Failure:** implementation and tests share same bug.  
**Defense:** task trust route requires independent/integration/protected evidence where material.

### Hidden evaluator drift
**Failure:** product verdict changes because evaluator/rubric changed.  
**Defense:** evaluator version, replay against frozen evidence, benchmark/drift monitoring.

### Protected evidence opacity
**Failure:** failures cannot be debugged or challenged.  
**Defense:** expose structured failure categories/minimal reproducible diagnostics; protect ground truth/cases, not accountability.

### CI outage bypass
**Failure:** missing check treated as advisory or manually waved through.  
**Defense:** `NOT_RUN/INCONCLUSIVE` blocks claims whose contract requires evidence; recovery waits/retries/replans without claiming PASS.

### CI outage deadlock
**Failure:** entire factory stops indefinitely.  
**Defense:** scope required checks by task, continue unaffected work, detect service incident, use only pre-declared replacement evidence paths; never invent a waiver.

### Factory metric gaming
**Failure:** agents optimize issue count, cycle time, pass rate, or low findings.  
**Defense:** metric vector, benchmark ground truth, escape/protected evidence, independent meta-review.

### Benchmark overfit
**Failure:** protocol memorizes benchmark patterns but worsens real work.  
**Defense:** protected variants, suite versioning, production-predictiveness check, new cases from escapes.

### GC deletes protected/canonical proof
**Failure:** storage cleanup makes old decision unverifiable.  
**Defense:** authority-aware retention graph + GC checks + audit.

## 27. Risks

- Structured evidence can become expensive; indexes, retention classes, and task-specific CI classes must keep cost proportional to claim risk.
- Protected evidence can become a privileged opaque subsystem; meta-review and versioned diagnostics are mandatory.
- Fixed retention durations chosen too early can either waste storage or lose proof; begin with authority/event-based classes and measure.
- Deep periodic checks may discover defects after integration; reopening/rollback must be normal autonomous behavior.
- Factory benchmark results can be noisy/correlated; use repeated paired runs and preserve raw evidence rather than overstate significance.
- CI service availability can become a central bottleneck; architecture should support distributed/unaffected work and deterministic recovery without bypass.
- Semantic coverage taxonomy itself can become a target; rotate/add dimensions based on escaped failures.

## 28. Open questions

1. Which artifact store and hash/index strategy provides durable protected/canonical evidence without bloating Git?
2. Which Run Report fields must be universal versus task-domain extensions?
3. What retention durations/cost budgets correspond to each authority class after real CI volume exists?
4. What exact evidence lets a verifier distinguish product flake, test flake, evaluator stochasticity, and infrastructure instability?
5. Which checks should be required PR gates versus asynchronous deep detectors with reopen authority?
6. How should protected evidence diagnostics be redacted so they remain actionable but not trivially gameable?
7. What benchmark task set predicts verified production throughput for a 10–20+ agent factory?
8. How many repeated benchmark runs are needed before protocol-change evidence is decision-useful?
9. Which metric changes themselves require historical recomputation versus new-version baselines?
10. What evidence should survive indefinitely after canonical decisions, and what may be summarized/compacted safely?

## 29. Reopen conditions

Reopen if:

- a canonical/verified decision cannot reproduce its evidence because artifacts expired or identifiers drifted;
- required flaky/inconclusive checks are routinely retried until green;
- CI statuses pass while contract-required evidence is NOT_RUN/missing;
- evidence indexes require broad raw-artifact preload for routine review;
- protected oracles can be modified/read by judged producers beyond declared permissions;
- evaluator-version drift materially changes decisions without being detected;
- factory metrics drive issue/commit/pass-rate gaming;
- benchmark improvements fail to predict production-like task quality/throughput;
- protocol changes are adopted without before/after benchmark and rollback evidence;
- retention/GC repeatedly threatens protected/canonical provenance;
- CI outages either cause unsafe bypass or unnecessary global factory shutdown;
- game semantic/player/simulation evidence shows that code-level checks miss important failures;
- later technical evidence proves the proposed report/storage boundaries too expensive or insufficient.

## 30. Required independent critique

`W1-REV-FAC` should attack factory metric incentives, benchmark Goodhart paths, CI outage liveness, WIP/queue interactions, self-improvement governance, and whether measurement encourages activity instead of verified outcomes.

`W1-REV-TECH` should attack Run Report reproducibility, determinism boundaries, artifact identity/retention, flake classification, protected evidence implementation, baseline/performance evidence, and whether player/simulation evidence can be produced from real systems rather than test doubles.

Both reviewers should attempt retry laundering, evidence deletion, evaluator drift, and benchmark-overfit failure scenarios.

## 31. Downstream work unblocked

This proposal supplies required inputs to `W1-REV-FAC` and `W1-REV-TECH`, and interfaces for W1-FAC-01/FAC-02/FAC-03, W1-EVAL-01, W1-TEC-02, and later synthesis.

It does not create CI infrastructure, alter current protected checks, instantiate extra Wave 1 work, or become canonical by authorship. Any adopted evidence/measurement system follows the Wave 1 review/synthesis/verification/canonicalization route and preserves squash-only integration.