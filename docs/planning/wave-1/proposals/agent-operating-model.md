# Agent Operating Model and Context/Handoff Lifecycle — Wave 1 Proposal

**Mission:** `W1-FAC-01`  
**State:** PROPOSED / NON-CANONICAL  
**Role:** factory operating-model planner  
**Required review:** `W1-REV-FAC`

## Review Index

**Core model.** A **task** is persistent repository/GitHub state with one bounded objective, ownership surface, dependency contract, deterministic branch, and review route. An **episode** is a disposable execution session that temporarily owns or inspects a task. Task lifetime may span many episodes; no useful state may exist only in episode memory.

**Role model.** Roles are defined by authority and evidence obligations, not personality: producer/researcher, continuation/recovery, reviewer, synthesizer/reviser, verifier, integrator/canonicalizer, checkpoint/auditor, and dispatcher/control-plane. A role transition that changes judgment authority requires a new episode/provenance boundary. In the current single-agent environment, required independence uses separated `DEGRADED_SINGLE_AGENT` episodes with immutable candidate-under-review and explicit trust debt.

**Context model.** Every episode starts from a bounded Context Manifest: canonical entry/program, selected issue contract, exact prerequisite/status refs, issue-declared authoritative inputs, and only triggered optional retrieval. Every optional load records why it was needed and its stable ref. Silent broad preload and silent truncation are invalid. Context is progressively widened only to resolve a named uncertainty.

**Continuation/handoff.** Continuation never means “trust the prior agent.” A continuing episode reconstructs current canonical state, issue/status/ownership, branch head/diff, latest handoff, checks/evidence, then independently verifies inherited assumptions before mutating. Every repository-changing episode leaves a structured handoff that binds issue, role/episode, ownership generation, base/work/head SHAs, state, completed/remaining work, checks/evidence, known defects/risks, decisions/deviations, context manifest, and next action.

**Stopping.** Valid stop conditions include completion/role boundary, explicit block, context/budget threshold, lease boundary, required external evidence, or recoverable tool failure. Before stopping: fence ownership/head, commit useful state, run required checks or record failures, update handoff, publish progress/result status. Uncommitted useful state is never a valid handoff.

**Discovered work.** New findings are typed as DEFECT, DEPENDENCY, RESEARCH, RISK, IMPROVEMENT, or SCOPE_EXPANSION. The current task may absorb only work necessary to satisfy its contract and inside its ownership/conflict surface. Otherwise the finding becomes bounded repository-visible candidate work; agents may not create uncontrolled same-wave backlog. A finding that invalidates the current prerequisite or acceptance claim blocks/reroutes the current task.

**Primary review attacks.** role laundering; same-session self-review; context pollution; stale handoff trusted as truth; endless WIP episodes; branch ambiguity; “quick fix” scope creep; discovered-work issue explosion; handoff theater with no reproducibility; continuation racing current owner; hidden local state; context budgets that truncate critical evidence.

**Experiments.** forced agent substitution; context-ablation/retrieval benchmark; stale/incorrect handoff challenge; mid-task crash recovery; discovered-work routing drill; long-task multi-episode reconstruction; degraded-vs-isolated role-boundary comparison when capability exists.

## 1. Status

This is a proposal for the semantic operating model that future dispatcher/control-plane tooling should implement. It intentionally does not replace the current canonical schema-3 claiming/fencing protocol and does not specify GitHub API transaction details. `W1-FAC-02` owns exact scheduler/control-plane mechanics; this proposal defines the lifecycle invariants those mechanics should preserve.

## 2. Scope

This proposal defines:

1. persistent task versus disposable episode semantics;
2. role classes and authority boundaries;
3. task selection/ownership expectations at the operating-model level;
4. branch/session lifecycle semantics;
5. context packet construction and progressive disclosure;
6. continuation/recovery behavior;
7. structured handoff quality and stopping rules;
8. discovered-work classification and routing;
9. operating-model observability and experiments;
10. interfaces to scheduler, review/verification, governance, and evidence systems.

## 3. Inputs and source basis

### 3.1 Observed repository evidence

The authoritative packet establishes:

- canonical `AGENTS.md` requires repository-owned memory, resumability, independent review, bounded context, designed parallelism, evidence over assertion, no routine human gate, and squash-only integration;
- the autonomous-factory mandate separates production, verification, planning, and meta-improvement loops; treats conversation history as disposable; favors progressive context; requires exactly one active implementation owner unless coordination is explicit; describes branch lifetime as task-scale and session lifetime as disposable; requires transactional handoffs; and expects future claiming to become machine-atomic;
- the research agenda leaves entry/context loading, task granularity, forced substitution, handoff quality, dependency/conflict modeling, and GitHub enforcement as explicit research questions rather than settled assumptions;
- the planning deliverables require eventual role definitions, task selection/claiming/stale recovery, branch/session lifecycle, WIP policy, handoff schema, continuation protocol, stopping/discovered-work/context rules, and dependency-aware issue generation.

### 3.2 Inference

If tasks persist longer than execution sessions and hidden chat/local state has no project authority, the unit of reliable progress must be a repository-reconstructable task state rather than a conversational thread. A continuation agent therefore needs a deterministic reconstruction protocol and cannot inherit conclusions purely by trust.

### 3.3 Recommendation

Adopt the task/episode/context/handoff model below as the semantic interface to be implemented and enforced by W1-FAC-02/W1-FAC-03/W1-FAC-04.

## 4. Goals

A fresh or continuation agent should be able to answer, without prior chat:

- What persistent task am I acting on?
- Why is it eligible, resumable, or recoverable?
- What role/authority do I have in this episode?
- What exact branch/head/base and ownership generation may I mutate?
- What context is mandatory, optional, or forbidden-by-default?
- What inherited claims must I independently inspect?
- What evidence/checks must exist before I stop or hand off?
- What discovered work belongs inside this task versus downstream planning?
- What state must another episode see to continue safely?
- What review/verification boundary comes next?

The operating model should support many parallel sessions without allowing task identity, authority, context, or handoff ambiguity to grow with concurrency.

## 5. Non-goals

This proposal does **not**:

- define the exact GitHub labels/fields/API commands or atomic-claim implementation;
- replace the canonical schema-3 capsule registry;
- define protected-test/evidence storage permissions;
- define detailed reviewer/verifier criteria beyond role/episode boundaries;
- choose task-size thresholds from intuition alone;
- authorize multiple concurrent writers to one task by default;
- create new current-wave tasks;
- authorize gameplay implementation;
- self-canonicalize this operating model.

## 6. Constraints

1. Repository + GitHub state is durable project memory; episode/chat memory is not.
2. A task should have at most one current mutation owner unless its contract explicitly defines coordinated substructure.
3. A task branch is deterministic and task-scoped; a continuation resumes the same branch rather than creating an alternate.
4. Every branch mutation must remain fenced by the canonical control-plane protocol.
5. Context must be bounded and progressively disclosed; silent truncation is invalid.
6. Continuation must inspect inherited state independently before extending it.
7. Useful work must be committed before an episode stops.
8. Review/verifier authority cannot be obtained merely by changing an episode label or UUID.
9. Discovered work must not create uncontrolled WIP/backlog.
10. Normal uncertainty does not become a human-wait state.
11. All `main` integration remains squash-only.
12. High-throughput implementation remains blocked until the canonical readiness gate permits it.

## 7. Assumptions

Provisional assumptions to test:

- One deterministic branch per task is sufficient for normal single-owner work; explicit multi-owner substructure should be rare and separately designed.
- A concise Context Manifest plus stable refs can improve reconstruction while avoiding broad document preload.
- Handoff quality can be measured through forced substitution and reconstruction cost rather than prose completeness alone.
- Work can usually be partitioned so an episode commits a coherent checkpoint before context/lease exhaustion.
- A typed discovered-work buffer can preserve useful findings without allowing workers to inflate the active issue graph.
- Role separation can be operationally meaningful in a single-agent environment if episodes are separated and candidate state is immutable, but trust remains degraded.

## 8. Alternatives considered

### 8.1 Task = session — rejected

Long or difficult work would become non-resumable or force hidden session memory into authority. Tasks must survive sessions.

### 8.2 One agent/session owns a branch until final integration — rejected

This makes crash/context exhaustion a lifecycle failure and discourages bounded checkpoints. Ownership is episode-scoped; the task/branch persists.

### 8.3 Load all project context to avoid missing information — rejected

This violates progressive disclosure, increases stale/conflicting instructions, and scales poorly. Missing context should trigger targeted widening with an explicit reason.

### 8.4 Trust the latest handoff and continue immediately — rejected

A handoff is evidence and navigation, not proof. Continuation must independently inspect branch/status/checks and inherited assumptions.

### 8.5 Create an issue for every discovered idea immediately — rejected

This optimizes issue count, causes WIP/backlog growth, and bypasses planning/synthesis. Findings should be typed, bounded, and promoted through the declared planning compiler/governor.

### 8.6 Allow “small opportunistic fixes” outside the task surface — rejected

Unreviewed scope expansion increases conflicts and destroys task-level evidence. Only contract-required, bounded work inside the owned surface may be absorbed without rerouting.

### 8.7 Same episode can produce and independently review if it promises objectivity — rejected

Independence is an evidence/context/authority boundary, not a stated intention. Current single-agent operation must use explicit degraded role separation rather than claim full independence.

## 9. Proposed operating model

### 9.1 Core entities

#### Task

A persistent unit of project work with:

- stable issue number and mission/task ID;
- role and objective;
- hard prerequisites and priority;
- deterministic branch rule;
- conflict/ownership surface;
- authoritative and optional context rules;
- exact output paths/schema;
- evidence and acceptance requirements;
- review/verification/integration route;
- downstream edges;
- current valid operational state/capsules;
- structured handoff history.

A task exists independently of any active agent session.

#### Episode

One bounded execution interval acting in one declared role on one task. Proposed identity fields:

```yaml
episode_id: <platform/run id or explicit session id>
task_id: <mission/issue>
role: <role class>
started_from:
  canonical_main_sha: <sha>
  branch_head_sha: <sha>
  ownership_generation: <comment/ref or null>
context_manifest_ref: <path/blob>
independence_profile: FULL | DEGRADED_SINGLE_AGENT | NOT_REQUIRED
```

An episode may stop before task completion. It must not become the only location of useful project state.

#### Work state

The durable combination of:

- valid issue/task contract;
- current canonical dependency/binding state;
- branch head/history;
- valid operational comments/ownership generation;
- handoff artifact;
- immutable evidence/check refs.

Labels and chat messages are advisory unless the canonical control plane explicitly gives them authority.

### 9.2 Role classes

Roles should encode **authority + required evidence**, not personas.

| Role class | May mutate task artifact? | Primary obligation | Must not do |
|---|---:|---|---|
| producer / planner / researcher | yes, owned surface | produce bounded evidence-backed candidate | self-approve canonicality |
| continuation / recovery | yes after valid ownership transition | reconstruct and safely continue/recover inherited work | trust handoff without inspection |
| reviewer / adversarial reviewer | review artifact/evidence surface only | attempt to invalidate producer claims | silently rewrite reviewed candidate and then pass it |
| synthesizer / reviser | synthesis-owned surface | disposition findings and reconcile candidates | pretend review findings do not exist |
| verifier | verification evidence/report surface | independently test exact candidate/base | edit candidate under verification |
| integrator / canonicalizer | verified promotion surface | apply exact accepted transformation and bind result | invent new semantics during promotion |
| checkpoint / auditor | checkpoint/report/remediation planning surface | inspect cross-task health and route corrective work | bypass task review gates to “fix” metrics |
| dispatcher / control plane | scheduling/state surface | derive eligibility/ownership safely | judge substantive artifact correctness |

A task contract can specialize these roles, but any authority expansion must be explicit.

### 9.3 Role-transition rule

When an execution context moves from a producing role to a judging role for the same provenance chain:

- start a new episode identity;
- freeze the candidate/work state being judged;
- load the judging role's context packet from repository + GitHub state rather than private producer notes;
- acquire new evidence before reconciling earlier rationale;
- record excluded prior roles and trust mode where independence is required.

In `DEGRADED_SINGLE_AGENT`, this is a liveness fallback with trust debt, not proof of independent cognition. A later stronger isolation capability is a reopen trigger for high-risk judgments.

### 9.4 Task/branch lifecycle

Recommended semantic lifecycle:

```text
eligible task
 -> deterministic task branch created/claimed
 -> one current mutation owner
 -> one or more bounded episodes
 -> checkpoints/progress/handoffs
 -> producer result state (e.g. REVIEW_READY)
 -> review/revision/verification episodes
 -> verified integration episode
 -> squash main integration where required
 -> task result terminal / branch becomes provenance
```

Branch principles:

- `planning/issue-N` (or canonical domain equivalent) identifies task lifetime, not one episode;
- new normal work branches from the contract's declared/current `main` base;
- continuation/recovery uses the existing branch;
- no force-push in normal operation;
- upstream branch work is consumed by immutable work SHA, not by “latest branch” assumption;
- WIP commits are acceptable when they improve reconstruction;
- branch existence alone does not establish current ownership or result validity;
- after accepted integration, branch retention/deletion is provenance/housekeeping, not authority.

Exact branch creation/CAS/lease mechanics belong to W1-FAC-02.

### 9.5 Context Manifest

Each substantial episode should be able to record or reconstruct a `ContextManifest`:

```yaml
context_manifest_version: 1
episode_id: <id>
task: <issue/mission>
canonical_entry:
  main_sha: <sha>
  program_blob: <blob>
required:
  - ref: <stable path@sha/blob/comment>
    reason: CANONICAL_ENTRY | TASK_CONTRACT | PREREQUISITE | AUTHORITATIVE_INPUT
optional_loaded:
  - ref: <stable ref>
    trigger: <named uncertainty / issue clause>
    reason: <why needed>
forbidden_or_not_loaded:
  - <category/ref>
size:
  required_utf8_bytes: <n or unknown>
  optional_utf8_bytes: <n or unknown>
truncation: NONE | EXPLICIT_SPLIT
```

Rules:

1. Always load the current canonical entry/program, selected task contract, exact dependency/status refs needed to derive eligibility/ownership, and task-declared authoritative packet.
2. Everything else is forbidden-by-default unless the issue/canonical program supplies an optional trigger.
3. Optional widening begins from a **named question**, not “read more for context.”
4. Record stable refs and the reason for each optional load.
5. Prefer indexes/summaries and targeted retrieval before whole large artifacts.
6. If the known input set exceeds the canonical context budget, split/restructure the task or use stable retrieval pointers; never silently truncate.
7. Private chat/scratch reasoning is not a context dependency and must not be referenced as required project state.

### 9.6 Context widening decision

An episode may widen context only when one of these is true:

- an acceptance criterion cannot be evaluated from current packet;
- a referenced interface/decision is unresolved;
- evidence needed to test a concrete claim is absent;
- branch/status state contradicts the handoff;
- a failure indicates a prerequisite assumption may be false;
- an optional retrieval trigger in the issue is satisfied.

The episode should record:

```text
question -> missing evidence/ref -> smallest retrieval -> result -> stop or widen again
```

This makes context growth inspectable and benchmarkable.

### 9.7 Continuation protocol

Before a continuation/recovery episode mutates inherited work:

1. read canonical entry/program and selected issue;
2. resolve task eligibility/ownership/recovery state from current valid operational records;
3. read latest committed handoff;
4. fetch current task branch head and compare with handoff head;
5. inspect branch diff/history since base and since handoff work SHA;
6. verify referenced checks/evidence exist and correspond to the claimed work state;
7. identify known defects, assumptions, unresolved decisions, and scope deviations;
8. independently sample or rerun the highest-risk inherited checks/claims;
9. acquire valid resume/recovery ownership through the control plane;
10. only then mutate the branch.

A stale or wrong handoff should not prevent recovery. Repository/GitHub state outranks it; the continuation records the discrepancy and corrects the durable handoff.

### 9.8 Handoff schema

Every repository-changing episode that may stop before another actor/role takes over should update one canonical task handoff path (history is in Git):

```yaml
handoff_version: 1
issue: <n>
mission_id: <id>
role: <role>
episode_id: <id>
branch: <branch>
base_sha: <sha>
ownership_generation: <ref>
work_sha: <substantive checkpoint/result sha>
head_sha: <head containing this handoff or final status notes>
state: <IN_PROGRESS/BLOCKED/HANDOFF_READY/REVIEW_READY/...>
context_manifest_ref: <ref or reconstructable packet>
completed: []
remaining: []
checks_performed: []
checks_failed: []
evidence: []
known_defects: []
suspected_risks: []
assumptions: []
decisions: []
scope_deviations: []
files_or_surfaces_changed: []
next_role_or_action: <bounded action>
```

A handoff is **navigation + evidence**, not an authority grant. Valid ownership/status remains in the control-plane state.

### 9.9 Handoff quality definition

A handoff is good if a replacement episode can, without hidden context:

- identify exact current work state;
- reproduce why the task is in its recorded state;
- find evidence/check failures;
- determine what remains and which assumptions are unsafe;
- continue without redoing large amounts of avoidable discovery;
- detect if the handoff itself is stale or wrong.

Recommended benchmark: forced substitution after randomly selected checkpoints; measure successful reconstruction, time/context to first safe mutation, duplicated work, missed defect rate, and incorrect-trust incidents.

### 9.10 Stopping rules

Valid stopping triggers include:

- task reaches its role-specific result boundary;
- next action belongs to another role;
- hard prerequisite/evidence is unavailable and a bounded blocked state is recorded;
- canonical context/episode budget is approaching a safe checkpoint threshold;
- ownership lease/agent runtime requires a handoff;
- tool/service failure prevents safe continuation but committed state can be preserved;
- newly discovered defect invalidates the current acceptance premise and must route through remediation/replanning.

Before stopping after repository mutation:

1. revalidate current ownership and branch head;
2. commit useful work at a coherent checkpoint;
3. run the checks appropriate to that checkpoint or record exact failures/non-runs;
4. update the task handoff;
5. publish canonical progress/result status with exact head/work refs;
6. leave no useful uncommitted local-only state;
7. do not claim completion if acceptance/evidence is incomplete.

“Context is large,” “another agent can figure it out,” or “waiting for human approval” are not sufficient handoff states.

### 9.11 Discovered-work routing

Classify every material discovery outside the current planned steps:

| Kind | Meaning | Default routing |
|---|---|---|
| DEFECT | current/inherited behavior contradicts requirement/evidence | fix only if required, bounded, owned; otherwise block/reroute |
| DEPENDENCY | missing prerequisite/interface prevents valid completion | record exact dependency; current task becomes/remaining BLOCKED as appropriate |
| RESEARCH | claim cannot be resolved without evidence/experiment | bounded research candidate/experiment |
| RISK | plausible failure not yet realized | risk register/candidate work with trigger/severity |
| IMPROVEMENT | non-required betterment | defer to candidate backlog/checkpoint unless canonical priority says otherwise |
| SCOPE_EXPANSION | useful work beyond contract/ownership | do not absorb silently; route to planning compiler/synthesis |

Current-task absorption is allowed only when **all** are true:

- necessary for current acceptance or safe repair of an introduced defect;
- inside owned/conflict-safe surface;
- bounded enough not to invalidate context/review assumptions;
- does not alter task role/verification independence;
- is recorded as a scope decision if not explicitly listed.

Otherwise create a **discovered-work candidate record**, not an immediate active issue unless the canonical contract/dispatcher explicitly authorizes issue creation.

Suggested candidate fields:

```yaml
discovery_id: <stable id>
source_issue: <n>
source_work_sha: <sha>
kind: <enum>
summary: <bounded>
evidence_refs: []
affected_missions_or_surfaces: []
severity_or_unblock_value: <qualitative>
proposed_owner_domain: <domain>
prerequisites: []
recommended_route: REMEDIATION | RESEARCH | NEXT_WAVE | CHECKPOINT | RETIRE
```

This prevents workers from converting every idea into WIP and preserves the canonical next-wave governor.

### 9.12 Work-in-progress semantics

At an operating-model level, prefer:

1. broken canonical/main or invalid active ownership recovery;
2. resumable handoff/stale work;
3. review/revision/verification/integration queues;
4. high-unblock-value ready work;
5. new root/proposal work.

Exact scheduler ordering belongs to W1-FAC-02, but the semantic rule is **finish and validate before proliferating** when both options have comparable priority/unblock value.

An episode should not create extra branches/tasks merely to remain busy.

## 10. Interfaces, dependencies, and conflict surfaces

| Interface | This proposal supplies | Downstream/owner |
|---|---|---|
| governance | role/episode authority boundary and durable memory semantics | W1-GOV-01 / W1-SYN-FAC |
| scheduler/control plane | Task/Episode/ContextManifest/Handoff/Discovery semantics and invariants | W1-FAC-02 |
| review/trust | role-transition freeze, candidate immutability, independence/degraded-mode requirements | W1-FAC-03 |
| CI/evidence | check/evidence refs and forced-substitution metrics | W1-FAC-04 |
| planning compiler | discovered-work candidate format and no-uncontrolled-WIP rule | W1-SYN-FINAL / later compiler work |

Potential conflicts to reconcile:

- W1-FAC-02 may define more exact lifecycle states; its machine state model should implement, not silently contradict, task/episode semantics.
- W1-FAC-03 may define stronger role separation; stronger trust requirements should supersede this proposal's minimum boundary.
- W1-FAC-04 may choose a different evidence/context manifest storage topology; stable references and reconstructability matter more than the exact file location.
- W1-GOV-01 may define more exact authority/directive rules; this proposal should consume them rather than duplicate governance precedence.

## 11. Observability and evaluation

Use a diagnostic vector:

- continuation success rate after forced substitution;
- median reconstruction context/steps before first safe mutation;
- handoff/head mismatch incidents;
- useful-work lost to uncommitted episode state;
- duplicate/repeated work after continuation;
- stale-hand-off trust incidents;
- context manifest required/optional byte totals;
- optional-retrieval count and reason distribution;
- silent/budget-overflow prevention incidents;
- task episodes per completion and reason for episode boundaries;
- branch conflict/non-fast-forward aborts;
- scope-deviation frequency and review findings caused by scope creep;
- discovered-work candidates created/promoted/retired;
- active-issue growth attributable to worker discoveries;
- role-separation/degraded-trust review escapes;
- percentage of handoffs with reproducible evidence refs.

Do not optimize a scalar “handoff score.” For example, extremely short handoffs may reduce bytes while increasing reconstruction cost; extremely long handoffs may hide critical state in noise.

## 12. Bounded experiments

| ID | Experiment | Pass signal | Failure implication |
|---|---|---|---|
| FAC1-E1 | Forced substitution at early/mid/late checkpoints | replacement reconstructs state and reaches first safe mutation without hidden context or major duplicate work | handoff/context schema inadequate |
| FAC1-E2 | Context ablation: run comparable task with minimal declared packet vs broad preload | bounded packet preserves result quality with less irrelevant context; widening events are explainable | context rules too narrow or indexes missing |
| FAC1-E3 | Corrupt/stale handoff challenge | continuation detects mismatch from branch/status/evidence and repairs handoff before mutation | handoff is being trusted as authority |
| FAC1-E4 | Crash-after-commit / crash-before-handoff scenarios | repository state remains recoverable; orphan/stale recovery can reconstruct intended next action from history/status | stopping/recovery contract incomplete |
| FAC1-E5 | Discovered-work storm: seed 20 mixed findings in one task | agent absorbs only contract-required bounded work and routes the rest without creating uncontrolled active issues | scope/backlog governor weak |
| FAC1-E6 | Multi-episode long planning task | work/checks/assumptions remain reconstructable across several episode boundaries without growing hidden context dependency | task granularity or handoff model fails |
| FAC1-E7 | When isolation becomes available, compare degraded single-agent review transitions with isolated review | measurable escape/disagreement data guides trust policy | current degraded role separation may be over-trusted |

## 13. Failure modes and defenses

### Session-bound task identity
**Failure:** work is “owned by this chat” and dies when the session ends.  
**Defense:** persistent issue/branch/status/handoff; episode is disposable.

### Role laundering
**Failure:** same execution simply renames itself reviewer/verifier.  
**Defense:** new episode, frozen candidate, repository-only judging packet, independent evidence, trust profile.

### Context pollution
**Failure:** every session loads all project docs and inherits stale contradictions.  
**Defense:** task-declared packet, trigger-based optional retrieval, Context Manifest.

### Critical context omission
**Failure:** strict minimal context hides required interface/evidence.  
**Defense:** named-question widening, acceptance-driven retrieval, explicit split instead of silent truncation.

### Handoff theater
**Failure:** long prose exists but replacement cannot reproduce state.  
**Defense:** exact SHAs/evidence/checks + forced-substitution benchmark.

### Stale handoff authority
**Failure:** continuation follows obsolete handoff over newer branch/status state.  
**Defense:** repository/GitHub state outranks handoff; mandatory branch/status reconciliation.

### Endless WIP episodes
**Failure:** task never reaches review because agents repeatedly “make progress.”  
**Defense:** checkpoint/result boundaries, WIP observability, scheduler preference for finishing/review, task split trigger.

### Quick-fix scope creep
**Failure:** worker modifies adjacent surfaces without review ownership.  
**Defense:** strict absorption conditions + scope deviation record + discovered-work route.

### Discovered-work explosion
**Failure:** each finding becomes an issue/branch.  
**Defense:** candidate records and canonical compiler/governor; issue creation is an authority, not a default reaction.

### Continuation races active owner
**Failure:** handoff-looking branch causes second writer.  
**Defense:** valid ownership transition required immediately before mutation; handoff never grants ownership.

### Hidden local evidence
**Failure:** checks/screenshots/notes exist only in session filesystem.  
**Defense:** durable evidence refs or explicit non-run/failure record before stop.

### Single-agent independence laundering
**Failure:** separated episodes are later called fully independent.  
**Defense:** typed DEGRADED trust and mandatory reopen condition.

## 14. Risks

- Context-manifest bookkeeping can become ceremony; W1-FAC-02/FAC-04 should automate collection and measure whether it improves reconstruction.
- Too-frequent episode checkpoints may increase commit/handoff overhead; benchmark task size and checkpoint cadence rather than fixing arbitrary limits.
- “Independent sample/recheck” during continuation could duplicate expensive work; risk-based sampling should focus on claims whose failure would invalidate the next mutation.
- Discovered-work candidate buffers can become unreviewed graveyards; checkpoints/synthesis need retirement/promotion metrics and ownership.
- A strict single-owner task model may be insufficient for future coordinated subtasks; explicit multi-agent substructure should be designed rather than implicitly allowing concurrent writers.
- Single-agent degraded review remains correlated and may miss shared reasoning errors.

## 15. Open questions

1. What measured context size/structure best predicts successful continuation and deep review?
2. What task-size or episode-count signals should trigger task splitting rather than another handoff?
3. Should Context Manifests be committed files, generated status artifacts, or derivable from issue + tool traces?
4. Which checks must a continuation rerun versus verify by immutable evidence?
5. What exact machine API should create discovered-work candidates without active issue proliferation?
6. When should a branch be deleted/archived after integration, and how is provenance retained cheaply?
7. What coordinated multi-agent subtask model can preserve one-task ownership semantics without serializing truly separable work?
8. Which role transitions require FULL isolation once multiple agents/context isolation are available?

## 16. Reopen conditions

Reopen this proposal or its descendants if:

- fresh continuation repeatedly needs hidden chat history;
- forced substitution has high reconstruction failure/duplicate-work rates;
- handoff size grows without reducing reconstruction cost;
- bounded context causes repeated escaped interface/requirement defects;
- broad optional retrieval becomes the norm rather than an exception;
- one task routinely needs concurrent writers on the same surface;
- discovered-work candidate volume grows faster than retirement/promotion;
- issue/branch proliferation rises because workers route every finding as active work;
- role transitions permit self-review or candidate mutation during verification;
- task episodes repeatedly exceed safe context/runtime without coherent checkpoints;
- stronger multi-agent/isolation capability invalidates assumptions behind DEGRADED role separation.

## 17. Required independent critique

`W1-REV-FAC` should attack:

- task/episode definitions that hide ownership ambiguity;
- role-transition loopholes and fake independence;
- context manifests that become bureaucracy or omit critical state;
- continuation protocol that trusts handoffs too much or duplicates all prior work;
- branch semantics that conflict with W1-FAC-02 atomic control-plane design;
- stopping rules that permit endless WIP or premature handoff;
- discovered-work rules that either swallow unsafe scope or lose important findings;
- WIP preference that reduces useful concurrency;
- benchmarks/metrics susceptible to Goodharting;
- single-agent trust debt being mislabeled as sufficient long-term independence.

## 18. Downstream work unblocked

This proposal supplies one required input to `W1-REV-FAC` and semantic interfaces for W1-FAC-02, W1-FAC-03, W1-FAC-04, and later W1-SYN-FAC.

It does not create additional current-wave issues, modify canonical control-plane state, or become authoritative by authorship. Promotion requires the declared Wave 1 review/synthesis/verification/canonicalization route.