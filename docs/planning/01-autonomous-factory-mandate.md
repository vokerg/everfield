# Autonomous Factory Mandate — Seed

**State:** SEED

## 1. Core Requirement

Everfield must be buildable through a long-running autonomous AI development factory with no routine human gate.

The factory must be capable of selecting work, executing it, judging it, correcting it, integrating it, generating future work, and periodically reconsidering its own assumptions.

This is a stronger requirement than "use AI to write code."

## 2. Required Nested Loops

The planning process should assume at least four persistent loops.

### Production Loop

Transforms a bounded work contract into repository changes.

```text
select/resume
  -> claim
  -> load bounded context
  -> implement
  -> run required checks
  -> inspect evidence
  -> revise
  -> commit
  -> handoff
```

### Verification Loop

Attempts to disprove the producer's claim that the work is ready.

```text
independent inspection
  -> independent execution
  -> adversarial review
  -> revision
  -> second independent review
  -> protected verification
```

### Planning Loop

Maintains a useful supply and ordering of future work.

```text
inspect current project state
  -> inspect metrics and unresolved design
  -> refine plans
  -> generate/retire tasks
  -> update dependencies
  -> maintain READY frontier
```

### Meta-Improvement Loop

Treats the factory itself as a versioned system.

```text
measure process
  -> detect repeated failure modes
  -> propose protocol/tool change
  -> benchmark old vs new behavior
  -> independently review
  -> adopt or revert
```

## 3. No Human Waiting State

The normal state machine must not contain `WAITING_FOR_HUMAN_APPROVAL`.

Human input is an exceptional directive that can override priorities or assumptions. In its absence, the system continues autonomously.

Uncertainty should normally cause one or more of:

- additional evidence gathering;
- independent evaluation;
- adversarial review;
- prototype/spike work;
- alternative candidate generation;
- checkpoint re-planning.

It should not automatically cause human escalation.

## 4. Repository-Owned Memory

Conversation history is disposable execution context.

Canonical project memory must live in repository or issue artifacts such as:

- specifications;
- ADRs / design decision records;
- schemas;
- tests;
- issues;
- handoffs;
- CI reports;
- evidence manifests;
- checkpoint reports;
- benchmark results.

A fresh agent should not require hidden knowledge from an earlier chat session.

## 5. Context Discipline

The mature factory should use progressive context disclosure.

A normal worker should receive only:

- global constitution;
- role;
- issue/work contract;
- dependency status;
- relevant module instructions;
- referenced specifications;
- required evidence and quality gates.

Global project material should be retrieved only when necessary.

Excessive computation is acceptable. Excessive irrelevant context is not.

## 6. Role Separation

Potential autonomous roles include:

- dispatcher;
- planner;
- researcher;
- specification author;
- architecture agent;
- implementer;
- continuation agent;
- test author;
- reviewer 1;
- reviewer 2 / adversarial reviewer;
- verifier;
- integration agent;
- game playtester;
- visual critic;
- narrative critic;
- balance agent;
- performance investigator;
- dependency auditor;
- checkpoint agent;
- factory auditor.

The important property is not artificial personality differentiation. It is independent evidence acquisition and bounded authority.

## 7. Task Claiming

Claiming must eventually become an atomic machine operation rather than a social convention.

Before work begins, the scheduler/claim mechanism should verify:

- task is eligible;
- hard dependencies are satisfied;
- no incompatible ownership surface is currently claimed;
- claim is not stale/duplicated;
- branch/base state is valid.

A task should have exactly one active implementation owner at a time unless its contract explicitly defines a coordinated multi-agent substructure.

## 8. Work-In-Progress Policy

Parallelism is valuable, but starting new work is not always the best use of a free agent.

The future dispatcher should generally favor finishing and validating existing work over creating excessive partially completed branches.

Planning must explicitly design WIP control and prioritization between:

- broken-main recovery;
- stale task continuation;
- review queues;
- revision queues;
- verification queues;
- integration queues;
- new implementation;
- planning/refinement.

## 9. Branch and Session Semantics

Working hypothesis:

- branch lifetime corresponds to task lifetime;
- session lifetime is disposable;
- a new task branches from current `main`;
- a continuation agent resumes the existing task branch;
- sessions commit useful resumable states before stopping;
- the completed task is squash-integrated into `main` through the controlled integration path.

This hypothesis must be challenged during planning.

## 10. Transactional Handoffs

Every useful stopping point must leave reconstructable state.

A handoff should ultimately include machine-readable fields such as:

```yaml
issue: null
role: null
branch: null
head_sha: null
base_sha: null
state: null
completed: []
remaining: []
tests_run: []
tests_failed: []
scenario_runs: []
evidence: []
known_defects: []
suspected_risks: []
decisions: []
scope_deviations: []
files_changed: []
modules_changed: []
recommended_next_action: null
```

Uncommitted local modifications are not a valid handoff.

## 11. Independent Review

A task should not progress because the implementing agent believes it is correct.

Current directional model:

1. implementation;
2. independent review 1;
3. revision;
4. blind or semi-blind independent review 2;
5. protected verification;
6. integration.

Review 2 should not merely inherit Review 1's framing. For important work it should first inspect independently, then reconcile findings.

## 12. Protected Evaluation

Some quality surfaces must not be editable by ordinary implementation agents.

Potential protected surfaces include:

- held-out tests;
- hidden scenarios;
- architecture checks;
- verifier logic;
- anti-metric-gaming probes;
- factory benchmarks;
- evidence integrity rules.

The exact trust boundary and storage topology remain open research questions.

## 13. Scheduler Objective

A scheduler should optimize for **verified throughput**, not activity.

Relevant variables may include:

- task priority;
- dependency depth;
- current READY frontier width;
- review/integration queues;
- stale work;
- ownership conflicts;
- failure severity;
- checkpoint directives;
- expected unblock value.

The scheduler itself should eventually be benchmarked.

## 14. Checkpoints

Local task success is not evidence of global project health.

Checkpoint agents must periodically inspect cross-cutting state and be authorized to:

- create remediation work;
- reprioritize work;
- split or retire tasks;
- reopen design decisions;
- propose architectural change;
- trigger research;
- halt expansion of unhealthy systems;
- revise future plans.

Checkpoints are the autonomous substitute for routine executive judgment.

## 15. Factory Self-Measurement

Candidate process metrics include:

- issue cycle length;
- first-pass review success;
- review findings per task;
- review escape rate;
- protected-verification failure rate;
- handoff resume success;
- reconstruction cost;
- branch conflict rate;
- merge-queue failure rate;
- revert rate;
- CI flake rate;
- READY frontier width;
- blocked issue ratio;
- average dependency depth;
- spec ambiguity rate;
- scope expansion rate;
- architecture violation rate;
- agent retry count.

Metrics are evidence, not objectives to optimize blindly.

## 16. Self-Modification Governance

Ordinary implementation agents must not casually modify the rules that judge them.

Changes to the factory constitution, scheduler, claim protocol, review protocol, verifier, protected tests, or quality metrics should become explicit factory-change work with:

- defect hypothesis;
- proposed change;
- benchmark plan;
- before/after evidence;
- independent meta-review;
- adoption/revert decision.

## 17. Factory Success Condition

The factory is mature when many fresh AI sessions with no hidden project history can repeatedly make safe, measurable, reviewable, resumable progress, while the system itself detects and repairs bad work and bad plans.
