# Planning Program v1 — Proposal

**State:** PROPOSED  
**Issue:** #2  
**Authority:** Candidate operating model only. The current `AGENTS.md` and `docs/planning/START-HERE.md` remain authoritative until bootstrap Issue #6 canonicalizes a cold-start-verified revision of this program.  
**Scope:** Planning work only. This document does not authorize gameplay implementation, mass implementation issue generation, or a final engine choice.

## 1. Status

This document turns the planning seed into a bounded executable planning program. It defines a cold-start protocol, task lifecycle, first detailed planning wave, exact artifact contracts, critique/synthesis routing, recovery behavior, and canonicalization gates.

The proposal is intentionally not self-canonical. Bootstrap Issue #3 must adversarially review it; Issue #4 must synthesize/revise it; Issue #5 must cold-start verify the synthesized candidate; and Issue #6 may canonicalize it only after a PASS.

## 2. Scope

Planning Program v1 governs the period from bootstrap canonicalization through the first bounded wave of detailed planning. Its job is to create reviewed foundations for:

- project/factory governance;
- agent operation and GitHub control-plane semantics;
- review, verification, CI, evidence, and factory measurement;
- engine evaluation and technical-foundation planning;
- game-design foundations;
- economy/progression/automation planning;
- world/social/narrative/content planning;
- UX/accessibility/media-pipeline planning;
- automated game evaluation;
- cross-domain synthesis and dependency extraction.

It also defines how later planning waves are generated without turning seed mission lists into an uncontrolled backlog.

## 3. Inputs

### 3.1 Authoritative bootstrap inputs

This proposal was derived from the Issue #2 input contract and the following repository artifacts:

- `/AGENTS.md`;
- `docs/planning/START-HERE.md`;
- `docs/planning/README.md`;
- `docs/planning/03-planning-program.md`;
- `docs/planning/05-research-agenda.md`;
- `docs/planning/06-planning-deliverables.md`.

The following seed mandates were additionally loaded because Issue #2 requires project-wide workflow, product, and evidence decisions:

- `docs/planning/00-project-charter.md`;
- `docs/planning/01-autonomous-factory-mandate.md`;
- `docs/planning/02-game-design-mandate.md`;
- `docs/planning/04-evaluation-and-evidence.md`.

### 3.2 Evidence/source basis

Observed repository constraints are treated as stronger than this proposal. In particular:

- normal work must not depend on routine human approval;
- repository + GitHub state must be sufficient for cold start and continuation;
- review must be independent of authorship;
- evidence must be inspectable and multi-signal rather than assertion-only;
- context must be progressively disclosed;
- the architecture/planning process should preserve a broad safe concurrency frontier;
- early design hypotheses remain reversible;
- every integration into `main` must use squash merge.

The 50 missions in `03-planning-program.md` are treated as seed candidates, not as an executable backlog. The first wave below is a deliberately smaller decomposition derived from the artifact classes in `06-planning-deliverables.md` and unresolved questions in `05-research-agenda.md`.

No external technical fact is asserted as settled by this proposal. First-wave missions that need current technical/legal/product evidence must collect it explicitly, preferring primary or authoritative sources and bounded empirical spikes.

## 4. Goals

Planning Program v1 must make these questions answerable by a fresh agent without hidden chat context:

1. What planning work exists now?
2. Which task is eligible and highest priority?
3. How is new work claimed atomically enough for the bootstrap environment?
4. How is handed-off or stale work resumed without creating a second task branch?
5. Which exact branch/base and immutable upstream artifact versions are used?
6. Which context is mandatory, optional, or forbidden-by-default?
7. Which exact artifact and schema does the task produce?
8. What evidence is required?
9. Which independent review follows and what can block progress?
10. How is unfinished work made reconstructable?
11. When can an artifact become canonical?
12. How does the graph keep producing bounded next work without a human gate?
13. How is all accepted work integrated through squash-only `main` history?

## 5. Non-goals

Planning Program v1 does not:

- implement gameplay;
- select a final engine;
- freeze the final architecture or game design;
- generate an implementation backlog;
- instantiate all seed planning missions;
- define a single scalar product-quality metric;
- make labels, dashboards, or issue counts the sole source of truth;
- require a human tie-breaker for normal uncertainty;
- permit an author to canonicalize its own proposal.

## 6. Constraints

1. `main` remains the stable integration base.
2. Every task branch is deterministic: `planning/issue-N`, unless an already-canonical issue contract explicitly overrides it.
3. Every task branch begins from the current `main` HEAD at claim time unless its issue names another immutable base.
4. Upstream planning artifacts that are not yet on `main` are consumed by exact recorded commit SHA, never by a moving branch name alone.
5. One normal task has at most one active task branch.
6. Session lifetime is disposable; task branch lifetime follows the task.
7. Planning artifacts use unique output paths where practical to reduce merge conflicts.
8. `main` integration is squash-only. Merge commits and rebase-merge are forbidden for normal integration even if GitHub exposes them.
9. The planning state machine has no `WAITING_FOR_HUMAN_APPROVAL` state.
10. Canonicality is explicit metadata, not inferred from branch, PR, merge, file existence, or issue closure.

## 7. Assumptions

These assumptions are recommendations awaiting Issue #3 attack and Issue #5 cold-start verification:

- deterministic branch creation is an adequate initial exclusion primitive for new planning work;
- issue comments can provide an ordered tie-break for concurrent resume attempts when a task branch already exists;
- immutable upstream SHAs plus unique output paths allow review and synthesis tasks to branch from current `main` without requiring unreviewed proposal merges first;
- 12 parallel root missions provide enough breadth to exercise the target concurrency model without exploding the backlog;
- the first wave can defer final engine choice while still producing an engine evaluation rubric and representative spike plan;
- proposal/review branches and PRs can remain non-canonical provenance until a synthesis/canonicalization task determines what should land as active rules.

## 8. Alternatives considered

### 8.1 Instantiate all 50 seed missions immediately

Rejected. It would confuse candidate topics with executable work, create excessive WIP, and violate the bootstrap constraint against mass issue generation.

### 8.2 One planner writes the complete factory, technical plan, and game bible

Rejected. It collapses independence, creates context overload, and makes critique mostly cosmetic.

### 8.3 Fully serial planning

Rejected. The charter explicitly targets a broad conflict-free frontier. Many first-order planning questions can be investigated independently before synthesis.

### 8.4 Merge every proposal to `main` before review

Rejected as the default. Review should judge the exact immutable proposal without making it operational merely to make it visible. Review/synthesis tasks can read exact upstream SHAs. Canonicalization decides what becomes active.

### 8.5 Rely on GitHub labels/assignees as the only dispatcher

Rejected for v1. They are useful views but are not sufficient project memory or an atomic claim protocol. Issue contracts, deterministic branches, immutable SHAs, and structured status capsules are the initial source of truth.

## 9. Proposed operating model

### 9.1 Canonical cold-start entry

After bootstrap Issue #6 canonicalizes Planning Program v1, a fresh agent must:

1. Read `/AGENTS.md`.
2. Read the canonical `docs/planning/START-HERE.md` pointer installed by Issue #6.
3. Query open planning issues with the canonical planning prefix, initially `[PLAN-v1]`.
4. Classify each issue from its prerequisites plus latest valid structured status capsule.
5. Prefer, in order:
   1. recoverable `HANDOFF_READY` work;
   2. expired/stale in-progress work eligible for recovery;
   3. ready review, revision, verification, or integration work;
   4. new READY proposal/research work.
6. Within the same class, select lower `priority_rank`, then lower GitHub issue number.
7. Read the selected issue in full.
8. Read only its declared authoritative inputs.
9. Re-check eligibility immediately before claim/resume.
10. Claim/resume using Sections 9.4–9.6.
11. Work only inside the task contract and leave a structured handoff/status before stopping.

If all unblocked work has a valid active lease, a free agent does not create duplicate work merely to remain busy. If no task is READY and no valid active work can eventually unblock the graph, the liveness rule in Section 9.11 applies.

### 9.2 Planning issue contract

Every Planning Program v1 issue must include these headings:

```text
Mission ID
Role
State at creation
Priority rank
Objective
Hard prerequisites
Conflict/ownership surface
Authoritative inputs
Optional retrieval triggers
Forbidden-by-default context
Output path(s)
Output schema
Evidence requirements
Acceptance criteria
Required independent critique/review
Downstream missions unblocked
Branch/base rule
Stopping/handoff rule
Canonicalization/integration rule
```

Mission IDs are stable identifiers; GitHub issue numbers are transport identifiers assigned at instantiation.

### 9.3 Planning states

The latest valid structured status capsule determines operational state. Labels may mirror it but are advisory until enforcement automation exists.

Allowed v1 states:

- `BLOCKED` — hard prerequisite unsatisfied;
- `READY` — prerequisites satisfied and no active owner;
- `IN_PROGRESS` — valid claim/resume lease exists;
- `HANDOFF_READY` — work intentionally yielded and safe to resume;
- `REVIEW_READY` — producer artifact is complete enough for independent critique;
- `CHANGES_REQUESTED` — review found required corrections or synthesis dispositions;
- `VERIFICATION_READY` — reviewed candidate awaits independent verification;
- `INTEGRATION_READY` — verification passed and an authorized integration task may act;
- `DONE` — task contract completed; this does not by itself imply its output is CANONICAL;
- `SUPERSEDED` — retained for provenance but no longer active;
- `INVALIDATED` — prerequisite/assumption failure requires re-planning.

State transitions that create normative authority require evidence from the prior role. A producer cannot move its own proposal from `REVIEW_READY` to `INTEGRATION_READY` or `CANONICAL`.

### 9.4 New-work claim protocol

For eligible Issue `#N`:

1. Re-read the issue and upstream status immediately before claim.
2. Confirm all hard prerequisites by exact status/SHA.
3. Resolve the current `main` HEAD SHA.
4. Attempt to create exactly `planning/issue-N` from that SHA.
5. If creation succeeds, immediately post:

```yaml
kind: CLAIM
protocol: planning-v1
issue: N
mission_id: <stable mission id>
branch: planning/issue-N
base_sha: <main sha>
state: IN_PROGRESS
session_id: <new opaque UUID for this work episode>
started_at: <ISO-8601 UTC>
lease_expires_at: <ISO-8601 UTC; default started_at + 6h>
upstream_inputs:
  - issue: <N>
    work_sha: <immutable sha>
```

6. Re-read the issue after posting and confirm no earlier valid claim exists. Branch creation should make this impossible for new work, but the check is mandatory.

If deterministic branch creation fails because the branch already exists, do not create an alternate branch. Enter the resume/recovery protocol.

A working agent may renew a lease by posting a `PROGRESS` capsule before expiry. Renewal must record current branch head, checks performed, and a new expiry no more than 6 hours later. Long-lived silent claims are intentionally unsupported.

### 9.5 Intentional resume protocol

A branch is intentionally resumable when the latest valid handoff/status is `HANDOFF_READY` and records an immutable `work_sha`.

Because branch creation cannot serialize resumes on an existing branch, v1 uses an ordered two-phase issue-comment tie-break:

1. Inspect issue, latest handoff, branch diff/history, and current head.
2. Independently review inherited work before editing.
3. Post a `RESUME_INTENT` capsule containing issue, mission ID, observed branch head, previous session/status, new `session_id`, and timestamp.
4. Immediately re-fetch issue comments.
5. The earliest valid `RESUME_INTENT` posted after the task became resumable wins. Any later contender must stop without editing.
6. The winner posts `RESUME`, sets a new 6-hour lease, re-fetches once more to confirm it is still the winner, then edits the existing branch.

This protocol is temporary and must be replaced by an atomic dispatcher/lease mechanism when the factory control plane is implemented.

### 9.6 Stale-claim recovery

An `IN_PROGRESS` task becomes recoverable when:

- its latest claim/progress lease is expired; and
- no later valid `PROGRESS`, `HANDOFF_READY`, `REVIEW_READY`, or terminal status exists.

Recovery follows the same `RESUME_INTENT` ordering rule as intentional resume. The winning recovery agent must first create a recovery note in its handoff describing:

- previous lease/session;
- observed branch head;
- whether useful committed work exists;
- independent assessment of inherited changes;
- any missing handoff data;
- decision to continue, repair, or invalidate the work.

A stale branch with no useful work is not a reason to create a parallel branch. The recovery agent continues on the deterministic branch or marks the task `INVALIDATED` with a bounded remediation path.

### 9.7 Branch, commit, PR, and integration semantics

- New tasks branch from current `main` at claim time unless the issue specifies an immutable base.
- Upstream non-main artifacts are fetched/read at exact `work_sha` values recorded by prerequisite status capsules.
- WIP commits are allowed and encouraged when they preserve useful resumable state.
- Force-pushing another task branch is forbidden.
- At `REVIEW_READY`, the task should have a PR targeting `main` for diff visibility unless its issue explicitly says no PR is useful. The PR title includes the mission ID and issue number.
- Opening a PR does not make an artifact canonical and does not authorize merge.
- Review/revision/verification may occur while a proposal PR remains open and unmerged.
- Only the task's defined integration/canonicalization path may merge to `main`.
- Every merge to `main` is `squash`, without exception under this version of the program.
- The integration agent must pass the expected head SHA to the merge operation and re-check verification status immediately before merge.

### 9.8 Handoff protocol

Every repository-changing episode writes or updates:

`docs/planning/handoffs/issue-N.md`

The handoff records the immutable work state being handed off, not a self-referential claim about the commit that contains the handoff:

```yaml
protocol: planning-v1
issue: N
mission_id: <id>
role: <role>
branch: planning/issue-N
base_sha: <claim base>
work_sha: <latest commit containing the substantive work inspected by the next agent>
session_id: <episode UUID>
state: IN_PROGRESS | HANDOFF_READY | REVIEW_READY | BLOCKED | INVALIDATED
completed: []
remaining: []
checks_performed: []
evidence: []
known_problems: []
decisions: []
open_questions: []
scope_deviations: []
recommended_next_action: <single concrete action>
```

After the handoff commit is pushed, the agent posts a final `STATUS` capsule on the issue with the exact resulting branch `head_sha` and the handoff path. This avoids the impossible requirement for a file to contain the SHA of the commit that contains itself.

### 9.9 Context-loading protocol

Always read only:

- `/AGENTS.md`;
- canonical `docs/planning/START-HERE.md`;
- the selected issue.

Then read exactly the issue's authoritative inputs. Optional sources are retrieved only when their trigger is met. A task must not preload the entire planning corpus unless its issue explicitly requires a whole-corpus synthesis.

Reviewers first inspect the proposal they are assigned. They load seed/mandate material only to test claims, find omissions, or resolve intent.

External research should prefer primary/authoritative sources for unstable technical, legal, platform, API, or tool facts. A research result is not a link list; it must map evidence to claims and uncertainty.

### 9.10 Evidence protocol

Substantial planning artifacts must distinguish:

- **Observed evidence** — repository constraints, primary/authoritative external sources, or empirical results;
- **Inference** — conclusions drawn from evidence;
- **Recommendation/decision** — proposed action;
- **Assumption** — unresolved premise being temporarily accepted.

For externally researched claims, record at least source, source type, retrieval date, claim supported, and uncertainty. For empirical questions, record reproduction steps, environment, inputs, outputs, and artifact locations. A mission must convert unresolved material uncertainty into a bounded follow-up question/spike rather than disguising it as certainty.

### 9.11 No-READY/liveness rule

A cold-start agent that finds no normal READY task must perform a bounded liveness classification:

1. If valid active leases exist and every blocked task is downstream of those leases, the graph is live; do not duplicate work.
2. If `HANDOFF_READY` or expired work exists, recover it before inventing new work.
3. If a review/revision/verification/integration task is eligible, it outranks new proposal work.
4. If no active/recoverable work can satisfy the remaining blockers, classify the graph as a liveness defect: cycle, invalidated dependency, orphan prerequisite, or missing transition.
5. Use the pre-instantiated first-wave recovery/checkpoint issue (`W1-REC-01`) to record the defect and produce the smallest remediation set. Do not create an unbounded replacement backlog.

`W1-REC-01` is a special reusable service task. Issue #6 should instantiate it in `BLOCKED` state with eligibility defined as “planning graph has no READY/recoverable work and no valid active lease can unblock it.” After a recovery episode, it returns to `BLOCKED`; the same deterministic branch may be resumed for later liveness incidents, with each episode recorded in its handoff history/status comments.

## 10. Standard artifact schemas

### 10.1 Proposal/research artifact

Every root planning proposal uses this section order:

1. Status
2. Scope
3. Inputs
4. Goals
5. Non-goals
6. Constraints
7. Assumptions
8. Evidence / source basis
9. Alternatives considered
10. Proposed design / conclusions
11. Interfaces / dependencies
12. Observability / evaluation
13. Failure modes
14. Risks
15. Open questions
16. Reopen conditions
17. Required independent critiques
18. Downstream artifacts/work unblocked

A research-heavy mission additionally includes an evidence ledger and experiment/spike backlog limited to unresolved questions necessary for its own downstream decisions.

### 10.2 Review artifact

Every review artifact contains:

```text
Status
Reviewed mission IDs and immutable SHAs
Reviewer session_id
Review scope and attack plan
Findings table: ID | severity | affected section | failure scenario | evidence | required correction
Cross-domain contradictions
Unresolved empirical questions
Disposition: PASS_FOR_SYNTHESIS | CHANGES_REQUIRED | INVALIDATED
Required next action
```

Severities: `BLOCKER`, `MAJOR`, `MINOR`, `NOTE`. Every BLOCKER/MAJOR requires a concrete correction or bounded empirical question.

### 10.3 Synthesis artifact

Every synthesis artifact contains the proposal schema plus:

- immutable inputs and review SHAs;
- a finding-disposition table for every BLOCKER/MAJOR;
- explicit interface contracts between merged domains;
- conflicts that remain intentionally unresolved;
- candidate canonical decisions and their reopen conditions;
- exact downstream verification mission.

### 10.4 Verification artifact

Every verification artifact contains:

```text
Status: PASS | FAIL
Candidate SHAs verified
Verifier session_id
Cold-start procedure followed
Scenarios exercised
Contradictions found
BLOCKER/MAJOR defects
Evidence inspected/reproduced
Liveness/claim/recovery simulation results
Self-canonicalization checks
Squash-integration checks
Required remediation if FAIL
```

PASS is forbidden while any BLOCKER/MAJOR remains unresolved.

## 11. First-wave mission graph

### 11.1 Instantiation rule

After bootstrap Issue #5 records PASS and Issue #6 canonicalizes the reviewed Planning Program v1, Issue #6 creates exactly the missions in this section plus `W1-REC-01`. It must not instantiate the 50 seed missions.

All 12 root missions below become READY concurrently after Issue #6 completes canonicalization. Each owns a unique output file. This intentionally creates a 12-wide safe planning frontier.

Issue titles use:

`[PLAN-v1][<MISSION-ID>] <title>`

Issue #6 assigns `priority_rank` from the numeric order below. Blocked review/synthesis nodes may be created at the same time so the full bounded DAG is visible, but they remain `BLOCKED` until their exact prerequisites are `REVIEW_READY` or otherwise satisfy their contract.

### 11.2 Root missions — concurrent frontier

#### W1-GOV-01 — Governance, canonicality, and provenance

**Role:** governance planner  
**Priority rank:** 10  
**Output:** `docs/planning/wave-1/proposals/governance-and-canonicality.md`  
**Authoritative inputs:** `AGENTS.md`, `00-project-charter.md`, `01-autonomous-factory-mandate.md`, `05-research-agenda.md`, `06-planning-deliverables.md`.  
**Objective:** propose the autonomy constitution, human-directive/override semantics, planning canonicality and decision-record rules, risk register model, self-modification authority boundaries, and legal/IP/provenance research/policy requirements.  
**Required evidence:** distinguish binding human directives from seed hypotheses; current legal/tool claims require authoritative sourcing or explicit deferral.  
**Critique dependency:** `W1-REV-FAC`.  
**Downstream:** `W1-SYN-FAC`.

#### W1-FAC-01 — Agent operating model and context/handoff lifecycle

**Role:** factory operating-model planner  
**Priority rank:** 20  
**Output:** `docs/planning/wave-1/proposals/agent-operating-model.md`  
**Authoritative inputs:** `AGENTS.md`, `01-autonomous-factory-mandate.md`, `05-research-agenda.md`, `06-planning-deliverables.md`.  
**Objective:** define roles, episode/task lifecycle, continuation, work packets, context disclosure, branch/session semantics, stopping rules, handoff quality, and discovered-work routing.  
**Required evidence:** compare plausible handoff/context models; define measurable reconstruction/handoff-success experiments.  
**Critique dependency:** `W1-REV-FAC`.  
**Downstream:** `W1-SYN-FAC`.

#### W1-FAC-02 — GitHub control plane, dependencies, and scheduler

**Role:** control-plane/scheduler planner  
**Priority rank:** 30  
**Output:** `docs/planning/wave-1/proposals/github-control-plane-and-scheduler.md`  
**Authoritative inputs:** `AGENTS.md`, `01-autonomous-factory-mandate.md`, `05-research-agenda.md`, `06-planning-deliverables.md`, this Planning Program v1 candidate/canonical version.  
**Objective:** design issue taxonomy/state machine, atomic mature claiming, stale-claim recovery, dependency/conflict types, READY algorithm, WIP control, priority model, PR/merge lifecycle, garbage collection, and machine API/automation plan.  
**Required evidence:** current GitHub capabilities must be sourced from authoritative GitHub documentation or tested; explicitly identify what cannot be enforced natively.  
**Critique dependency:** `W1-REV-FAC` and `W1-REV-TECH`.  
**Downstream:** `W1-SYN-FAC`, `W1-SYN-TECH`.

#### W1-FAC-03 — Independent review, verification, and trust boundaries

**Role:** verification/trust planner  
**Priority rank:** 40  
**Output:** `docs/planning/wave-1/proposals/review-verification-and-trust.md`  
**Authoritative inputs:** `01-autonomous-factory-mandate.md`, `04-evaluation-and-evidence.md`, `05-research-agenda.md`, `06-planning-deliverables.md`.  
**Objective:** define review classes, reviewer independence, disagreement resolution, protected evaluation surfaces, permission/change boundaries, evidence sufficiency, anti-Goodhart controls, and integration eligibility.  
**Required evidence:** concrete specification-gaming/reviewer-failure scenarios and benchmark proposals.  
**Critique dependency:** `W1-REV-FAC` and `W1-REV-TECH`.  
**Downstream:** `W1-SYN-FAC`, `W1-SYN-TECH`.

#### W1-FAC-04 — CI, evidence topology, and factory measurement

**Role:** CI/evidence/factory-measurement planner  
**Priority rank:** 50  
**Output:** `docs/planning/wave-1/proposals/ci-evidence-and-factory-measurement.md`  
**Authoritative inputs:** `01-autonomous-factory-mandate.md`, `04-evaluation-and-evidence.md`, `05-research-agenda.md`, `06-planning-deliverables.md`.  
**Objective:** propose structured run reports, evidence storage/provenance/retention, CI taxonomy, flaky-evidence policy, factory metrics, benchmark suites, and protocol-change measurement.  
**Required evidence:** identify which evidence surfaces require empirical prototypes and which are design contracts only.  
**Critique dependency:** `W1-REV-FAC` and `W1-REV-TECH`.  
**Downstream:** `W1-SYN-FAC`, `W1-SYN-TECH`.

#### W1-TEC-01 — Engine evaluation program and representative spikes

**Role:** engine evaluation planner  
**Priority rank:** 60  
**Output:** `docs/planning/wave-1/proposals/engine-evaluation-program.md`  
**Authoritative inputs:** `00-project-charter.md`, `01-autonomous-factory-mandate.md`, `04-evaluation-and-evidence.md`, `05-research-agenda.md`, `06-planning-deliverables.md`.  
**Objective:** define candidate-screening criteria, weighted/non-scalar rubric, representative autonomous-development spikes, CI/headless/asset/mergeability/determinism/agent-ergonomics tests, and an ADR decision protocol.  
**Non-goal:** do not choose the final engine unless a later empirical mission has actually produced the required comparative evidence.  
**Required evidence:** current engine/tool claims use primary documentation plus reproducible spikes; feature-table comparison alone is insufficient.  
**Critique dependency:** `W1-REV-TECH`.  
**Downstream:** empirical engine-spike missions and `W1-SYN-TECH`.

#### W1-TEC-02 — Runtime, data, determinism, persistence, and content foundation

**Role:** technical-foundation planner  
**Priority rank:** 70  
**Output:** `docs/planning/wave-1/proposals/runtime-data-foundation.md`  
**Authoritative inputs:** `00-project-charter.md`, `02-game-design-mandate.md`, `04-evaluation-and-evidence.md`, `05-research-agenda.md`, `06-planning-deliverables.md`.  
**Objective:** define engine-independent runtime boundaries, canonical state concepts, determinism boundaries, save/migration needs, IDs/registries/schema/versioning principles, content-validation interfaces, performance observability, and extension/conflict constraints.  
**Non-goal:** no engine-specific production architecture before engine evidence exists.  
**Critique dependency:** `W1-REV-TECH` and `W1-REV-GAME`.  
**Downstream:** `W1-SYN-TECH`, `W1-SYN-GAME`.

#### W1-DES-01 — Game-design foundation and possibility-space model

**Role:** game-design foundation planner  
**Priority rank:** 80  
**Output:** `docs/planning/wave-1/proposals/game-design-foundation.md`  
**Authoritative inputs:** `00-project-charter.md`, `02-game-design-mandate.md`, `05-research-agenda.md`, `06-planning-deliverables.md`.  
**Objective:** propose game pillars, minute/day/season/long-horizon loops, player possibility-space model, sandbox specialization principles, discovery/unlock philosophy, system-family decomposition criteria, chore/repetition policy, and extensibility/late-game principles.  
**Required evidence:** explicitly separate Stardew Valley as a coherence/complexity reference from Everfield-original recommendations; represent competing loop/sandbox structures fairly.  
**Critique dependency:** `W1-REV-GAME`.  
**Downstream:** `W1-SYN-GAME`.

#### W1-DES-02 — Economy, progression, automation, and sandbox viability

**Role:** economy/progression/automation planner  
**Priority rank:** 90  
**Output:** `docs/planning/wave-1/proposals/economy-progression-automation.md`  
**Authoritative inputs:** `00-project-charter.md`, `02-game-design-mandate.md`, `04-evaluation-and-evidence.md`, `05-research-agenda.md`, `06-planning-deliverables.md`.  
**Objective:** propose progression graph principles, automation tier/value model, capital/labor tradeoffs, late-game sinks, lifestyle viability criteria, dominant-strategy detection, and simulation requirements.  
**Required evidence:** quantitative hypotheses must be framed as simulation targets/unknowns rather than invented balance numbers; define falsifiable viability metrics.  
**Critique dependency:** `W1-REV-GAME`.  
**Downstream:** `W1-SYN-GAME` and later balance-simulation missions.

#### W1-DES-03 — World, NPC, social, narrative, quest, and content architecture

**Role:** world/narrative systems planner  
**Priority rank:** 100  
**Output:** `docs/planning/wave-1/proposals/world-social-narrative-content.md`  
**Authoritative inputs:** `00-project-charter.md`, `02-game-design-mandate.md`, `04-evaluation-and-evidence.md`, `05-research-agenda.md`, `06-planning-deliverables.md`.  
**Objective:** propose interfaces among world state, NPC simulation, relationships, dialogue, quest grammar, narrative facts/chronology, authored/generative content, consistency validation, and progression consequences.  
**Required evidence:** define structural solvability/consistency checks separately from subjective narrative-quality judgment.  
**Critique dependency:** `W1-REV-GAME`.  
**Downstream:** `W1-SYN-GAME`.

#### W1-EXP-01 — UX, accessibility, visual, and audio production/evaluation foundations

**Role:** experience-pipeline planner  
**Priority rank:** 110  
**Output:** `docs/planning/wave-1/proposals/experience-accessibility-media.md`  
**Authoritative inputs:** `00-project-charter.md`, `02-game-design-mandate.md`, `04-evaluation-and-evidence.md`, `05-research-agenda.md`, `06-planning-deliverables.md`.  
**Objective:** define UX/onboarding/discovery/accessibility constraints that must influence architecture early, plus visual/audio bible, AI asset-production, provenance, consistency, and multimodal evaluation requirements.  
**Non-goal:** no final visual style or asset catalog.  
**Critique dependency:** `W1-REV-GAME`.  
**Downstream:** `W1-SYN-GAME`.

#### W1-EVAL-01 — Automated game evaluation and synthetic players

**Role:** game-evaluation planner  
**Priority rank:** 120  
**Output:** `docs/planning/wave-1/proposals/automated-game-evaluation.md`  
**Authoritative inputs:** `00-project-charter.md`, `02-game-design-mandate.md`, `04-evaluation-and-evidence.md`, `05-research-agenda.md`, `06-planning-deliverables.md`.  
**Objective:** define semantic coverage, synthetic-player interfaces/personas, economy/progression simulation, exploit search, difficulty/engagement proxies, visual/narrative judge protocols, evaluator versioning, and golden-scenario strategy.  
**Required evidence:** explicitly prevent a single `fun_score`; specify evaluator disagreement/escalation and held-out/protected surfaces.  
**Critique dependency:** `W1-REV-TECH` and `W1-REV-GAME`.  
**Downstream:** `W1-SYN-TECH`, `W1-SYN-GAME`.

### 11.3 Independent review missions

#### W1-REV-FAC — Factory/governance adversarial review

**Prerequisites:** `W1-GOV-01`, `W1-FAC-01`, `W1-FAC-02`, `W1-FAC-03`, `W1-FAC-04` at `REVIEW_READY`.  
**Output:** `docs/planning/wave-1/reviews/factory-and-governance.md`  
**Attack focus:** hidden human gates, ambiguous authority, non-atomic claiming, stale recovery races, context overload, self-modification loopholes, Goodhart paths, WIP explosion, weak garbage collection, unsafe merge semantics, and inability to maintain a broad READY frontier.  
**Independence:** reviewer session must differ from every producer session it reviews.  
**Downstream:** `W1-SYN-FAC`.

#### W1-REV-TECH — Technical/evidence adversarial review

**Prerequisites:** `W1-FAC-02`, `W1-FAC-03`, `W1-FAC-04`, `W1-TEC-01`, `W1-TEC-02`, `W1-EVAL-01` at `REVIEW_READY`.  
**Output:** `docs/planning/wave-1/reviews/technical-and-evidence.md`  
**Attack focus:** premature engine assumptions, fake integration evidence, nondeterminism blind spots, unversioned evidence, protected-oracle weakness, merge-hostile architecture, content-schema bottlenecks, and untestable technical requirements.  
**Independence:** reviewer session differs from all reviewed producers.  
**Downstream:** `W1-SYN-TECH`.

#### W1-REV-GAME — Game/experience adversarial review

**Prerequisites:** `W1-TEC-02`, `W1-DES-01`, `W1-DES-02`, `W1-DES-03`, `W1-EXP-01`, `W1-EVAL-01` at `REVIEW_READY`.  
**Output:** `docs/planning/wave-1/reviews/game-and-experience.md`  
**Attack focus:** nominal rather than real sandbox diversity, dominant progression, automation eliminating play, content-count inflation, shallow system interaction, narrative/mechanics disconnects, inaccessible complexity, evaluator blind spots, and Stardew-cloning risk.  
**Independence:** reviewer session differs from all reviewed producers.  
**Downstream:** `W1-SYN-GAME`.

### 11.4 Synthesis missions

#### W1-SYN-FAC — Factory/governance synthesis candidate

**Prerequisites:** all inputs to `W1-REV-FAC` plus completed `W1-REV-FAC`.  
**Output:** `docs/planning/wave-1/synthesis/factory-governance-candidate.md`  
**Role:** synthesizer distinct from reviewed producers and reviewer.  
**Required behavior:** disposition every BLOCKER/MAJOR; define coherent interfaces among governance, agent lifecycle, control plane, review trust, CI/evidence, measurement, and self-improvement; identify empirical factory benchmarks/spikes still required.  
**Downstream:** `W1-REV-CROSS`.

#### W1-SYN-TECH — Technical/evidence synthesis candidate

**Prerequisites:** all inputs to `W1-REV-TECH` plus completed `W1-REV-TECH`.  
**Output:** `docs/planning/wave-1/synthesis/technical-evidence-candidate.md`  
**Role:** synthesizer distinct from reviewed producers and reviewer.  
**Required behavior:** disposition every BLOCKER/MAJOR; produce an engine-decision evidence path rather than an unsupported engine choice; reconcile runtime/data/evidence/evaluation contracts; identify required empirical spikes.  
**Downstream:** `W1-REV-CROSS`.

#### W1-SYN-GAME — Game/experience synthesis candidate

**Prerequisites:** all inputs to `W1-REV-GAME` plus completed `W1-REV-GAME`.  
**Output:** `docs/planning/wave-1/synthesis/game-experience-candidate.md`  
**Role:** synthesizer distinct from reviewed producers and reviewer.  
**Required behavior:** disposition every BLOCKER/MAJOR; reconcile core loops, sandbox, progression/economy/automation, world/social/narrative/content, UX/accessibility/media, technical-content constraints, and automated evaluation.  
**Downstream:** `W1-REV-CROSS`.

### 11.5 Cross-domain review and final synthesis

#### W1-REV-CROSS — Cross-domain interface/parallelism adversarial review

**Prerequisites:** `W1-SYN-FAC`, `W1-SYN-TECH`, `W1-SYN-GAME` at `REVIEW_READY`.  
**Output:** `docs/planning/wave-1/reviews/cross-domain-interface-and-parallelism.md`  
**Role:** independent cross-domain reviewer.  
**Attack focus:** contradictory assumptions, hidden serial dependencies, giant shared ownership surfaces, circular interfaces, untestable requirements, evaluator/control-plane conflicts, implementation-readiness leakage, and architecture choices that collapse future concurrency.  
**Downstream:** `W1-SYN-FINAL`.

#### W1-SYN-FINAL — Wave-1 canonicalization candidate and dependency map

**Prerequisites:** all three synthesis candidates plus `W1-REV-CROSS`.  
**Outputs:**

- `docs/planning/wave-1/synthesis/wave-1-canonicalization-candidate.md`;
- `docs/planning/wave-1/synthesis/dependency-map.yaml`.

**Role:** final planning synthesizer distinct from `W1-REV-CROSS`.  
**Required behavior:** disposition all cross-domain BLOCKER/MAJOR findings; separate candidate canonical rules from deferred questions; emit typed dependencies, unresolved empirical spikes, conflict surfaces, proposed next-wave missions, and explicit implementation-readiness blockers.  
**Dependency-map minimum schema:**

```yaml
version: 1
nodes:
  - id: <artifact-or-decision-id>
    state: PROPOSED | REVIEWED_CANDIDATE | DEFERRED
    artifact: <path>
    work_sha: <sha>
edges:
  - from: <id>
    to: <id>
    type: HARD | INTERFACE | EVIDENCE | REVIEW | CONFLICT
    rationale: <text>
reopen_conditions: []
implementation_readiness_blockers: []
next_wave_candidates: []
```

**Downstream:** `W1-VERIFY-01`.

### 11.6 Verification and canonicalization

#### W1-VERIFY-01 — Independent wave-1 cold-start/coherence verification

**Prerequisite:** `W1-SYN-FINAL` at `VERIFICATION_READY`.  
**Output:** `docs/planning/wave-1/reviews/wave-1-cold-start-verification.md`  
**Role:** verifier who did not author `W1-SYN-FINAL` and did not perform `W1-REV-CROSS`.  
**Required simulations:** cold-start task selection, duplicate claim, intentional handoff resume, expired-lease recovery race, invalidated dependency, no-READY liveness path, review rejection, evaluator self-modification attempt, premature implementation attempt, and squash-only integration.  
**Result:** PASS or FAIL.  
**Downstream:** PASS unlocks `W1-CANON-01`; FAIL unlocks only bounded remediation identified by the report.

#### W1-CANON-01 — Canonicalize accepted wave-1 foundations and instantiate next bounded wave

**Prerequisite:** `W1-VERIFY-01` PASS for the exact `W1-SYN-FINAL` SHA.  
**Role:** integration/canonicalization agent distinct from final synthesizer and verifier.  
**Required actions:** verify candidate SHA and findings; materialize accepted active rules/artifacts into canonical repository locations; mark superseded material; preserve provenance to proposals/reviews/syntheses; instantiate only the bounded next-wave missions justified by the dependency map; close/retire obsolete first-wave work; squash-merge the canonicalization PR into `main`.  
**Forbidden:** gameplay implementation and unbounded implementation issue generation.

### 11.7 Recovery/checkpoint service mission

#### W1-REC-01 — Planning liveness recovery

**Initial state:** BLOCKED.  
**Eligibility:** only when Section 9.11 classifies the graph as not live.  
**Output:** `docs/planning/wave-1/recovery/liveness-recovery.md` (updated per episode with dated sections) plus structured handoff/status.  
**Role:** checkpoint/recovery agent.  
**Authority:** diagnose cycles/orphans/invalidations, retire or split bounded planning work, propose the smallest remediation set, and restore at least one credible READY path. It may not bypass review/canonicalization gates or authorize implementation.

## 12. Concurrency and conflict model

The 12 root missions are intentionally concurrent because each writes a unique proposal path and consumes only seed/canonical inputs. Their primary conflicts are semantic, not filesystem conflicts; those are resolved by reviews/synthesis rather than shared editing.

The graph then narrows deliberately:

```text
Issue #6 canonicalizes Planning Program v1
        |
        +--> 12 root proposals in parallel
                |
                +--> REV-FAC ----> SYN-FAC --+
                +--> REV-TECH ---> SYN-TECH -+--> REV-CROSS --> SYN-FINAL --> VERIFY --> CANON
                +--> REV-GAME ---> SYN-GAME -+

REC-01 is conditionally eligible only on liveness failure.
```

A task issue must name its filesystem ownership surface. Two tasks that need to edit the same canonical file concurrently are not safe siblings; they must instead emit unique proposals and use a synthesis task.

## 13. Independent critique rules

1. An author session cannot be the reviewer session for its own artifact.
2. A review task begins with independent inspection before reading other reviewer conclusions when multiple reviews exist.
3. A synthesizer cannot silently discard BLOCKER/MAJOR findings; each gets ACCEPTED, REJECTED_WITH_EVIDENCE, or CONVERTED_TO_EXPERIMENT.
4. A verifier cannot be the final synthesizer it verifies.
5. A canonicalization/integration agent cannot be the author of the candidate being canonicalized or the verifier that passed it.
6. Identity is recorded through per-episode `session_id` capsules. This is an auditable procedural boundary, not a cryptographic identity guarantee; the mature factory trust model must strengthen it.

## 14. Canonicalization criteria

A planning artifact or synthesis may become CANONICAL only when all applicable conditions hold:

- exact candidate SHA is recorded;
- all required producer outputs exist;
- required independent reviews exist at immutable SHAs;
- every BLOCKER/MAJOR finding has an explicit disposition;
- material empirical claims have evidence or are clearly deferred;
- assumptions/open questions/reopen conditions are explicit;
- interfaces/dependencies/conflict surfaces are explicit;
- no hidden human approval is required for continuation;
- verifier records PASS for the exact candidate SHA;
- canonicalization is performed by an independent integration role;
- operational entry-point docs are updated consistently;
- superseded instructions are marked rather than silently contradicted;
- the integration PR is merged to `main` using squash merge with expected head SHA checked immediately before merge.

Merging a `PROPOSED` or review artifact for provenance does not, by itself, confer CANONICAL state.

## 15. Observability and evaluation of the planning program

Planning Program v1 should be evaluated as a factory protocol, not only read as prose. At minimum record during the first wave:

- successful/failed cold starts;
- duplicate-claim attempts prevented;
- resume-reconstruction success and missing-context incidents;
- stale-recovery incidents and races;
- average mandatory-context count per mission;
- READY frontier width over time;
- number/severity of cross-domain findings;
- number of BLOCKER/MAJOR findings escaping one review layer into the next;
- tasks invalidated/retired versus only created;
- branch/ownership conflicts;
- review and verification turnaround states;
- liveness incidents;
- any attempt to bypass squash-only integration;
- any attempt by an author to self-canonicalize.

These are diagnostic signals, not a scalar success score. W1-FAC-04 must refine them into versioned factory metrics/benchmarks.

## 16. Failure modes

Planning Program v1 must explicitly defend against:

- two agents editing the same task branch after a resume race;
- expired claims that permanently block work;
- active claims with no useful commits or handoff;
- review tasks accidentally depending on proposal merge to `main`;
- moving upstream branches changing what a reviewer thought it reviewed;
- proposal authors editing reviewer artifacts;
- synthesis becoming a disguised single-author rewrite;
- unresolved major findings disappearing between stages;
- labels disagreeing with repository artifacts;
- all tasks becoming blocked due a dependency cycle;
- issue generation outpacing review capacity;
- giant shared canonical files becoming merge bottlenecks;
- current engine/tool assumptions leaking into engine-independent plans;
- game-design breadth collapsing into feature-count inflation;
- automation becoming the mandatory dominant playstyle;
- evaluator metrics becoming targets that can be gamed;
- implementation starting before implementation-readiness blockers are cleared;
- non-squash integration into `main`.

## 17. Risks

### 17.1 Resume serialization is not truly atomic

The comment-order protocol reduces but does not eliminate race windows. It is acceptable only as a temporary planning protocol and is a required target of `W1-FAC-02`.

### 17.2 Session identity is procedural

`session_id` prevents accidental role reuse in project memory but is not a cryptographic proof of independent models/operators. The trust planner must define stronger enforcement where necessary.

### 17.3 First-wave scope may still be broad

Some root missions may discover they need splitting. They may propose bounded follow-up missions but must not self-expand their current issue. `W1-SYN-FINAL` decides which follow-ups enter the next wave.

### 17.4 Cross-domain synthesis can become a bottleneck

The design keeps three parallel synthesis tracks and uses a single cross-domain review only after domain candidates exist. If that final narrowing repeatedly blocks throughput, the parallelism review should reopen the decomposition.

## 18. Open questions

- What native or automated GitHub mechanism should replace comment-ordered resume leasing?
- What identity/permission boundary can enforce reviewer/verifier independence when agents share repository credentials?
- Which protected evaluation surfaces require separate repositories/services versus permissions inside one repository?
- What evidence retention topology is affordable and reconstructable at game scale?
- Which engine candidates survive initial hard constraints and deserve representative spikes?
- Which game-system boundaries best preserve sandbox depth and technical parallelism?
- What quantitative thresholds indicate acceptable planning-frontier width, handoff quality, or evaluator reliability?
- When should planning proposals themselves be merged to `main` for provenance versus retained only through PR/GitHub history until synthesis?

These are first-wave planning questions, not reasons to wait for a human.

## 19. Reopen conditions

Planning Program v1 must be reconsidered if any of the following occurs:

- cold-start verification cannot reproduce task eligibility without hidden context;
- duplicate claims or resume races cause conflicting writes;
- stale recovery requires routine manual/human arbitration;
- more than one first-wave task is blocked by an undocumented shared ownership surface;
- READY frontier width collapses because of avoidable planning serialization;
- review independence cannot be demonstrated even procedurally;
- important planning claims repeatedly reach synthesis without evidence paths;
- the program creates more obsolete work than it retires;
- a canonicalization step can occur without an independent PASS;
- future repository/tool constraints make deterministic branch claims unreliable;
- any later explicit human directive supersedes the squash-only rule or another binding constraint.

## 20. Required independent critiques

Bootstrap Issue #3 must adversarially review this proposal at:

`docs/planning/reviews/issue-2-adversarial-review.md`

At minimum it must attack:

- the new-work and resume race semantics;
- stale leases and liveness behavior;
- the 12-root/three-review decomposition;
- whether exact inputs/outputs are sufficient for cold start;
- whether review/synthesis independence is meaningful;
- whether proposal branches can safely remain unmerged while downstream work consumes immutable SHAs;
- whether the canonicalization path can accidentally grant authority too early;
- whether the recovery service can become a policy-bypass backdoor;
- whether the first wave is bounded enough while still covering implementation-readiness foundations;
- whether squash-only integration is preserved end-to-end.

## 21. Bootstrap synthesis and transition conditions

This proposal does not replace the bootstrap chain. Transition is:

1. **Issue #2:** this proposal reaches `REVIEW_READY` with exact branch/head status.
2. **Issue #3:** independent adversarial review produces findings and a synthesis readiness disposition.
3. **Issue #4:** a distinct synthesizer revises this program and records dispositions for all BLOCKER/MAJOR findings.
4. **Issue #5:** a fresh verifier enters from repository/GitHub state and exercises the protocol adversarially. FAIL keeps the program non-canonical and creates/identifies bounded remediation; PASS points to one exact candidate SHA.
5. **Issue #6:** an independent canonicalization agent verifies the PASS SHA, updates entry-point docs, marks temporary bootstrap rules superseded/thin-pointer as appropriate, instantiates only the first-wave mission graph above, and squash-merges the canonicalization change to `main`.

Only after Step 5 may `[PLAN-v1]` first-wave tasks become the normal planning queue.

## 22. Downstream work unblocked

When Issue #2 marks this proposal `REVIEW_READY`, only bootstrap Issue #3 is newly eligible.

When the full #2 → #3 → #4 → #5 → #6 chain completes with verification PASS, the program unblocks the bounded Wave 1 graph in Section 11. It still does **not** authorize high-throughput gameplay implementation.

Implementation throughput remains blocked until later canonical planning explicitly demonstrates the readiness conditions in `06-planning-deliverables.md`, including safe claiming, machine-readable dependencies/conflicts, resumability, structured CI evidence, independent review/protected verification, parallel architecture, and a coherent first gameplay slice.