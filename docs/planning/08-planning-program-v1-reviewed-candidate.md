# Planning Program v1 — Reviewed Candidate

**State:** REVIEWED-CANDIDATE  
**Bootstrap issue:** #4  
**Authority:** Candidate operating model only. It MUST NOT become CANONICAL until Bootstrap Issue #5 independently verifies this exact candidate work state and Bootstrap Issue #6 performs the verified, mechanically constrained promotion.  
**Scope:** Planning work only. This document does not authorize gameplay implementation, mass implementation issue generation, or a final engine choice.

## 1. Status

This document replaces the operational content of the Issue #2 base proposal plus Amendments 1–2 with one coherent candidate. The complete Issue #3 adversarial review was synthesized into this revision.

All Issue #3 BLOCKER and MAJOR findings are accepted and corrected. The exact dispositions are recorded in `docs/planning/reviews/issue-3-finding-dispositions.md`.

The machine-readable promotion and Wave 1 issue-instantiation contract is `docs/planning/08-planning-program-v1-canonicalization-manifest.yaml`. Bootstrap Issue #5 MUST verify this candidate and that manifest as one immutable work state.

## 2. Scope

Planning Program v1 governs autonomous planning after bootstrap canonicalization through the first bounded detailed-planning wave. It defines:

- cold-start task discovery and deterministic eligibility;
- temporary task claiming, continuation, stale recovery, and write fencing;
- branch/session/handoff semantics;
- structured status validity and state transitions;
- evidence and context-budget rules;
- independent review, synthesis, verification, and canonicalization;
- a bounded first-wave mission DAG;
- liveness recovery and planning garbage collection;
- bounded next-wave generation;
- implementation-readiness barriers.

## 3. Inputs

### 3.1 Immutable reviewed inputs

This candidate synthesizes:

- `docs/planning/07-planning-program-v1-proposal.md` — Issue #2 proposal provenance;
- `docs/planning/07-planning-program-v1-proposal-amendment-1.md`;
- `docs/planning/07-planning-program-v1-proposal-amendment-2.md`;
- `docs/planning/reviews/issue-2-adversarial-review.md` — Issue #3 independent review;
- the bootstrap instructions in `/AGENTS.md` and `docs/planning/START-HERE.md` at the Issue #4 base `main@21a3c1a5053f3697be3f82f6fe73de42423a482b`.

Seed mandate material is not re-declared as canonical truth here. Where Issue #3 relied on the autonomous-factory mandate and planning-deliverables seed to identify a defect, this candidate preserves the relevant constraint as a reviewed recommendation pending Issue #5 verification.

### 3.2 Evidence / source basis

Observed repository constraints outrank this candidate:

- repository + GitHub state must be sufficient for cold start and continuation;
- no routine human approval state exists;
- review and verification must obtain independent evidence;
- context is budgeted;
- work must be resumable;
- canonicality is explicit;
- accepted integration into `main` is squash-only.

No unstable external technical fact is asserted as settled by this candidate. Missions requiring current GitHub, engine, legal, platform, or tool claims must source or empirically test them.

## 4. Goals

A fresh agent must be able to determine, without prior chat context:

1. the current planning phase and entry path;
2. which task is eligible and highest priority;
3. whether an existing branch is owned, handed off, stale, orphaned, review-ready, terminal, or invalid;
4. how to claim or resume without authorizing two compliant writers;
5. exact branch/base and immutable upstream inputs;
6. exact output path/schema and context budget;
7. acceptance/evidence requirements;
8. exact review/synthesis/verification route;
9. stopping/handoff behavior;
10. liveness behavior when no ordinary task is READY;
11. canonicalization requirements bound to both candidate and verified `main` state;
12. bounded downstream issue generation;
13. the implementation-readiness barrier.

## 5. Non-goals

Planning Program v1 does not:

- implement gameplay;
- choose a final engine;
- freeze architecture or game design;
- instantiate the 50 seed missions;
- create a full implementation backlog;
- permit a producer to self-canonicalize;
- use labels as the authoritative dispatcher;
- treat a self-selected UUID as proof of reviewer independence;
- treat branch count as proof of useful parallelism.

## 6. Constraints

1. `main` is the stable canonical base.
2. Normal task branches are deterministic: `planning/issue-N`.
3. One normal task has at most one authorized writer generation at a time.
4. All branch mutations are expected-parent/fast-forward operations; force-push is forbidden.
5. Upstream non-main artifacts are consumed by exact immutable work SHA.
6. `BLOCKED` and `READY` are derived states, not manually flipped gates.
7. Structured operational capsules are append-only; edited capsules are invalid.
8. Lease time derives from GitHub server metadata, never a self-authored future timestamp.
9. Canonicality is explicit and cannot be inferred from merge, PR, issue closure, or file location alone.
10. Every integration into `main` is squash-only.
11. Wave 1 issues are instantiated only after Bootstrap Issue #6 has been squash-merged and the resulting main SHA is known.
12. High-throughput implementation remains blocked until a later verified implementation-readiness decision.

## 7. Assumptions

The following remain assumptions to be tested by Issue #5 and/or Wave 1 factory work:

- GitHub comment IDs/creation metadata plus expected-parent branch writes are sufficient for a temporary planning-phase ownership protocol when all compliant agents follow the fence checks below;
- a six-hour ownership TTL is a reasonable provisional default, provided renewals require substantive evidence and stale generations are fenced;
- a maximum initial READY frontier of 12 and a maximum of 24 newly instantiated issues per later wave are safe provisional governors;
- context budgets based on compact review indexes plus targeted retrieval provide sufficient depth without requiring reviewers to load all broad artifacts simultaneously;
- procedural cold-start separation can provide minimum reviewer independence until stronger platform/credential boundaries are designed.

## 8. Alternatives considered

### 8.1 Keep comment-ordered leases without fencing

Rejected. Lease expiry changes belief, not write authority. The revised protocol adds ownership generations and expected-parent mutation checks.

### 8.2 Pre-create Wave 1 issues before the canonicalization merge

Rejected. A future squash SHA cannot be embedded as a concrete prerequisite. Issue #6 now merges first, then instantiates exactly from the verified manifest.

### 8.3 Allow canonicalization to rewrite the verified candidate freely

Rejected. Promotion is constrained by the verified canonicalization manifest and exact enumerated transformations.

### 8.4 Keep one reusable recovery branch forever

Rejected. Squash integration makes indefinite reuse ambiguous. Recovery missions are single-use episodes; each completed recovery may instantiate exactly one successor recovery issue.

### 8.5 Let synthesis instantiate every discovered next-wave candidate

Rejected. Candidate accumulation and issue instantiation are separated by a hard issue/frontier governor and issue-compiler validation.

## 9. Canonical cold-start entry

After Bootstrap Issue #6 completes, a fresh planning agent MUST:

1. Read `/AGENTS.md`.
2. Read canonical `docs/planning/START-HERE.md`.
3. Read canonical `docs/planning/PLANNING-PROGRAM-v1.md` at current `main`.
4. Query open `[PLAN-v1]` issues.
5. Validate each issue contract and latest operational capsules using Section 10.
6. Derive eligibility from hard prerequisites, branch state, ownership generation, lease validity, and terminal state.
7. Prefer queue classes in this order:
   1. intentional handoff or recoverable stale/orphan work;
   2. ready review/revision/verification/integration work;
   3. new READY proposal/research work.
8. Within a queue class choose lower `priority_rank`, then lower GitHub issue number.
9. Re-read the selected issue immediately before claiming/resuming.
10. Load only its bounded context packet under Section 15.
11. Claim/resume under Sections 11–13.
12. Before every repository mutation, re-check the ownership fence.
13. Before stopping, commit useful state and leave the structured handoff/status.

If there is no READY/recoverable work, use Section 16 rather than inventing parallel work or waiting for a human.

## 10. Operational state and capsule protocol

### 10.1 Derived states

`BLOCKED` and `READY` are derived from prerequisites and current ownership/terminal state.

Operational recorded states are:

- `IN_PROGRESS`;
- `HANDOFF_READY`;
- `REVIEW_READY`;
- `CHANGES_REQUESTED`;
- `VERIFICATION_READY`;
- `INTEGRATION_READY`;
- `DONE`;
- `SUPERSEDED`;
- `INVALIDATED`.

Recovery classifications are derived, not durable task states:

- `ORPHANED_BRANCH` — deterministic branch exists but no valid ownership capsule exists after the orphan-probe grace;
- `STALE_OWNER` — latest ownership lease expired with no later valid ownership/status capsule.

Labels are advisory views only.

### 10.2 Valid capsule definition

Operational capsules are GitHub issue comments with YAML bodies and `protocol: planning-v1`, `schema: 1`.

A capsule is valid only if:

- it is an unedited comment: GitHub `updated_at` equals `created_at` where that metadata is exposed; if edit state cannot be established, the capsule cannot be used to create authority;
- required fields for its `kind` are present and type-valid;
- `issue`, `mission_id`, and deterministic branch agree with the issue contract;
- its referenced SHAs exist and match the relevant branch/artifact;
- its predecessor/state transition is allowed by Section 14;
- any prerequisite predicate required by the transition is satisfied;
- it does not claim authority superseded by a later valid capsule.

Capsules are ordered by GitHub immutable comment identity / server creation order. Body timestamps are descriptive only. Lease start is the GitHub server creation time of the winning `CLAIM`, `RESUME`, `RECOVER`, or valid renewing `PROGRESS` capsule.

Edited, malformed, impossible-transition, wrong-branch, wrong-mission, or unsupported-version capsules are ignored for operational authority and SHOULD be reported in the next status/handoff as invalid evidence.

### 10.3 Ownership generation

Every valid ownership-granting capsule records:

```yaml
protocol: planning-v1
schema: 1
kind: CLAIM | RESUME | RECOVER
issue: <N>
mission_id: <id>
branch: planning/issue-N
session_id: <episode UUID>
observed_head_sha: <remote branch head>
base_sha: <claim base>
previous_ownership_comment_id: <id-or-null>
state: IN_PROGRESS
```

The **ownership generation** is the GitHub comment ID of the latest valid ownership-granting capsule. Agents MUST NOT invent a separate numeric epoch.

The default lease expires six hours after the GitHub server creation time of the ownership capsule or a valid renewal.

## 11. New-work claim protocol

For eligible Issue `#N`:

1. Re-read issue, prerequisites, branch existence, and latest valid capsules.
2. Resolve current `main` SHA.
3. Attempt to create exactly `planning/issue-N` from that SHA.
4. If branch creation succeeds, immediately post the `CLAIM` capsule with `observed_head_sha` equal to the created branch head and `previous_ownership_comment_id: null`.
5. Re-fetch comments and branch head. The claim is active only if it is the earliest valid ownership capsule for that just-created branch and head.
6. Before the first edit, perform the mutation fence in Section 13.

### 11.1 Orphan branch crash recovery

If the deterministic branch exists but no valid ownership capsule exists:

1. Do not edit and do not create an alternate branch.
2. If a valid `ORPHAN_PROBE` comment already exists and its GitHub server age is at least ten minutes with no later valid ownership capsule, the branch is `ORPHANED_BRANCH` and may enter recovery.
3. Otherwise post exactly one best-effort `ORPHAN_PROBE` containing issue, branch, observed head, and base/main relationship, then stop claiming this issue for the current episode. Other eligible work may be selected normally.
4. A later agent observing the mature probe re-checks branch history, posts `RECOVER` referencing the probe comment ID, and becomes owner only if no earlier valid competing recovery capsule exists.

The ten-minute grace prevents takeover during the normal branch-create → claim-comment window while guaranteeing eventual repository-visible recovery without a human gate.

## 12. Intentional resume and stale recovery

### 12.1 Intentional handoff

A task is intentionally resumable when the latest valid task status is `HANDOFF_READY` and records `work_sha` plus branch `head_sha`.

Contenders post `RESUME_INTENT` referencing that exact status comment/head. The earliest valid intent by GitHub comment order wins. The winner posts `RESUME`; later contenders stop without editing.

### 12.2 Stale owner

An owner is stale when its latest valid ownership/renewal server time is older than six hours and no later valid terminal/handoff/review status exists.

Recovery contenders use the same intent ordering, then the winner posts `RECOVER` referencing the expired ownership comment and exact observed branch head.

Expiry alone does not revoke the stale writer. The branch-write fence in Section 13 does.

### 12.3 Renewal quality

A `PROGRESS` renewal is valid only if it references the current ownership generation and includes either:

- a new remote branch head containing substantive committed work; or
- an immutable evidence result for a bounded check/experiment that materially advances the task.

No more than three consecutive renewals without a branch-head advance are valid. A fourth no-head-advance renewal is ignored for lease extension, allowing ordinary stale recovery.

## 13. Mandatory mutation fence

Immediately before **every** repository mutation to a task branch, the agent MUST:

1. re-fetch latest valid operational comments;
2. confirm its ownership-generation comment ID is still the latest valid owner grant and the lease is unexpired;
3. fetch the remote task-branch head;
4. confirm the head equals the exact parent/observed head on which the mutation is based;
5. perform only an expected-parent / fast-forward write;
6. if the ownership generation or branch head changed, abort the write, inspect the new state, and follow resume/recovery rules rather than forcing history.

A compliant stale session therefore loses authorization as soon as another valid ownership generation exists. The protocol is procedural until the mature control plane replaces it, but stale generations fail closed.

## 14. Mission-class transitions and review dispositions

### 14.1 Producer missions

- prerequisites satisfied + no branch → derived `READY`;
- valid claim/resume/recover → `IN_PROGRESS`;
- intentional yield → `HANDOFF_READY`;
- producer acceptance criteria satisfied → `REVIEW_READY`;
- producer may not advance itself to `VERIFICATION_READY`, `INTEGRATION_READY`, or CANONICAL.

### 14.2 Review missions

A review task finishes as `DONE` with exactly one disposition:

- `PASS_FOR_SYNTHESIS` — no BLOCKER/MAJOR requiring revision before synthesis;
- `CHANGES_REQUIRED` — findings are bounded and MUST be dispositioned by the declared synthesis/revision mission; this **does unlock that synthesis mission**;
- `INVALIDATED` — reviewed path is not safe to synthesize as-is; it unlocks only the declared recovery/replanning path, not normal synthesis.

Thus “completed review” is never a sufficient prerequisite. Downstream issue contracts name the exact allowed disposition predicate.

### 14.3 Synthesis/revision missions

A synthesis becomes `VERIFICATION_READY` only when:

- all required review inputs have an allowed disposition;
- every BLOCKER/MAJOR has `ACCEPTED`, `REJECTED_WITH_EVIDENCE`, or `CONVERTED_TO_EXPERIMENT`;
- no unresolved BLOCKER remains on a transition the candidate claims is safe;
- exact candidate and canonicalization-manifest SHAs are recorded.

### 14.4 Verification missions

Verification records `PASS` or `FAIL` for:

- exact candidate work SHA;
- exact canonicalization manifest from that work state;
- exact `verified_base_main_sha`;
- exact issue-graph/contract simulation inputs.

PASS is forbidden with unresolved BLOCKER/MAJOR defects.

### 14.5 Integration/canonicalization missions

`INTEGRATION_READY` requires a PASS tied to the exact candidate and base. If current `main` differs from `verified_base_main_sha`, the prior PASS is insufficient until an independent bounded compatibility/reverification covers every intervening main commit.

## 15. Context-loading and evidence budgets

### 15.1 Always-read context

Every normal mission reads only:

- `/AGENTS.md`;
- canonical `docs/planning/START-HERE.md`;
- selected issue;
- canonical `docs/planning/PLANNING-PROGRAM-v1.md` at the issue activation SHA.

Then it loads the issue’s authoritative packet.

### 15.2 Root artifact review index

Every root proposal MUST begin with a **Review Index** no larger than 4,000 UTF-8 characters containing:

- claims/decisions with stable section IDs;
- interfaces/dependencies;
- assumptions/open questions;
- evidence pointers;
- known conflict surfaces;
- required reviewer attack points.

Full evidence may live in the same artifact or referenced repository artifacts, but the index is the mandatory review entry surface.

### 15.3 Mandatory packet budget

For a review/synthesis task, the mandatory simultaneously loaded packet is limited to the lesser of:

- 100,000 UTF-8 characters; or
- 50% of the execution context window when that limit is known to the agent.

The mandatory packet consists of entry documents, issue contract/status capsules, upstream Review Index sections, required finding tables, and interface/evidence indexes—not every full upstream artifact.

If the mandatory packet exceeds the budget, the task MUST NOT silently truncate. It must either:

- split into bounded sub-review work explicitly authorized by its issue/manifest; or
- load indexes first and retrieve full source sections only by stable section/evidence pointer as concrete findings require.

Review findings must cite the exact full sections actually inspected.

### 15.4 Evidence classification

Artifacts distinguish:

- observed evidence;
- inference;
- recommendation/decision;
- assumption.

Current external technical/legal/tool claims require authoritative sources or explicit deferral. Empirical claims require reproducible inputs, outputs, environment, and artifact pointers.

## 16. No-READY liveness and recovery episodes

A cold-start agent with no ordinary READY task classifies:

1. valid active ownership that can still unblock the graph → graph live; do not duplicate;
2. intentional handoff, mature orphan probe, or stale owner → recover that work;
3. eligible review/revision/verification/integration → execute it before new proposal work;
4. otherwise → liveness defect: cycle, orphan prerequisite, invalidated dependency, missing transition, or corrupted status state.

`W1-REC-01` is a **single-use** recovery mission, initially `BLOCKED`, conditionally READY only for case 4.

A recovery mission may diagnose and propose/apply the smallest bounded remediation but may not waive review, verification, canonicalization, or squash-only integration.

After a recovery episode is accepted/integrated, its task becomes `DONE`. If planning remains active, that recovery integration may instantiate exactly one successor recovery service issue (`W1-REC-02`, then `W1-REC-03`, etc.) in `BLOCKED` state. Each recovery issue has an ordinary one-task/one-branch lifetime. There is never a permanently reused post-squash task branch.

## 17. Branch, handoff, PR, and integration semantics

- New tasks branch from current `main` unless the issue names another immutable base.
- WIP commits are encouraged when they preserve resumable state.
- Every repository-changing episode updates `docs/planning/handoffs/issue-N.md`.
- The handoff records substantive `work_sha`; the final issue `STATUS` records the resulting branch `head_sha` after the handoff commit.
- PRs may be opened for diff/provenance visibility without conferring authority.
- A provenance merge does not make an artifact CANONICAL.
- All `main` integration is squash-only.
- Canonical integrations check both expected candidate/head and verified base/current-main compatibility.

Minimum handoff fields:

```yaml
protocol: planning-v1
issue: <N>
mission_id: <id>
role: <role>
branch: planning/issue-N
base_sha: <sha>
work_sha: <substantive sha>
session_id: <episode id>
state: IN_PROGRESS | HANDOFF_READY | REVIEW_READY | VERIFICATION_READY | BLOCKED | INVALIDATED
completed: []
remaining: []
checks_performed: []
evidence: []
known_problems: []
decisions: []
open_questions: []
scope_deviations: []
recommended_next_action: <one action>
```

## 18. Standard artifact schemas

### 18.1 Proposal/research

1. Status
2. Review Index
3. Scope
4. Inputs
5. Goals
6. Non-goals
7. Constraints
8. Assumptions
9. Evidence/source basis
10. Alternatives considered
11. Proposed design/conclusions
12. Interfaces/dependencies
13. Observability/evaluation
14. Failure modes
15. Risks
16. Open questions
17. Reopen conditions
18. Required independent critiques
19. Downstream work unblocked

### 18.2 Review

```text
Status
Reviewed mission IDs + immutable work SHAs
Independent execution-context provenance
Review scope/attack plan
Findings table: ID | severity | affected section | failure scenario | evidence | required correction
Cross-domain contradictions
Unresolved empirical questions
Disposition: PASS_FOR_SYNTHESIS | CHANGES_REQUIRED | INVALIDATED
Required next action
```

### 18.3 Synthesis

Proposal schema plus:

- exact producer/review input SHAs;
- disposition for every BLOCKER/MAJOR;
- interface contracts;
- unresolved conflicts/experiments;
- canonicalization candidate decisions/reopen conditions;
- exact downstream verification contract.

### 18.4 Verification

```text
Status: PASS | FAIL
Candidate work_sha
Canonicalization-manifest path + blob/work SHA
verified_base_main_sha
Independent execution-context provenance
Cold-start procedure
Scenarios exercised
Contradictions
BLOCKER/MAJOR defects
Evidence inspected/reproduced
Claim/recovery/fencing simulations
State-transition simulations
Context-budget simulation
Canonical-promotion simulation
Squash/base-drift simulation
Required remediation if FAIL
```

## 19. Independent critique boundary

Minimum acceptable independence for a required review/verifier is a **distinct cold-start execution context** that:

- does not have producer private conversation/scratch context;
- begins from repository + GitHub entry state;
- records a new execution-context/run identifier when the platform exposes one;
- records prior mission roles that are excluded from satisfying this gate;
- obtains its own evidence before reconciling prior reviewer conclusions.

A self-selected `session_id` alone is episode tracking, not proof of independence.

If platform-level run identity is unavailable, procedural cold-start separation is permitted temporarily but must be recorded as such and remains a first-wave trust-model risk. An explicit human directive may override workflow ordering, but such an override is recorded as directive provenance and does not silently masquerade as independent evidence.

## 20. First-wave mission DAG

### 20.1 Activation and count

Bootstrap Issue #6 does **not** pre-create Wave 1 issues.

After its canonicalization PR is squash-merged:

1. obtain the resulting `main` SHA;
2. verify the canonical program exists at that SHA and matches the verified promotion manifest;
3. instantiate exactly the 23 initial Wave 1 issues from `docs/planning/08-planning-program-v1-canonicalization-manifest.yaml`;
4. every issue records the now-concrete activation `required_main_sha` and remains blocked until Issue #6 posts terminal `DONE` after validating all issue contracts;
5. post the mission-ID → GitHub-issue mapping and `DONE` status;
6. derived eligibility then makes eligible roots READY automatically.

Initial missions:

- 12 roots: `W1-GOV-01`, `W1-FAC-01`, `W1-FAC-02`, `W1-FAC-03`, `W1-FAC-04`, `W1-TEC-01`, `W1-TEC-02`, `W1-DES-01`, `W1-DES-02`, `W1-DES-03`, `W1-EXP-01`, `W1-EVAL-01`;
- domain reviews: `W1-REV-FAC`, `W1-REV-TECH`, `W1-REV-GAME`;
- domain syntheses: `W1-SYN-FAC`, `W1-SYN-TECH`, `W1-SYN-GAME`;
- cross review: `W1-REV-CROSS`;
- final synthesis: `W1-SYN-FINAL`;
- verification: `W1-VERIFY-01`;
- canonicalization: `W1-CANON-01`;
- recovery: `W1-REC-01`.

Exact titles, priorities, prerequisites, inputs, outputs, review routes, and acceptance/schema classes are in the machine-readable manifest and are part of the verified candidate.

### 20.2 DAG

```text
Issue #6 squash integration + post-merge issue instantiation + DONE
        |
        +--> 12 root proposals in parallel
                |
                +--> REV-FAC ----> SYN-FAC --+
                +--> REV-TECH ---> SYN-TECH -+--> REV-CROSS --> SYN-FINAL --> VERIFY --> CANON
                +--> REV-GAME ---> SYN-GAME -+

REC-01 is conditionally eligible only on a liveness defect.
```

`CHANGES_REQUIRED` review dispositions unlock the declared synthesis/revision mission. `INVALIDATED` does not; it unlocks recovery/replanning only.

## 21. Safe concurrency and conflict boundaries

Root missions own unique output paths. Shared semantic interfaces are reviewed/synthesized rather than co-edited.

Each issue contract names:

- filesystem ownership surface;
- semantic conflict surface;
- hard prerequisites;
- review dependencies.

Two sibling tasks that must mutate the same canonical file are not safe siblings. They emit unique proposals and converge through synthesis.

Useful parallelism is measured by independently progressing conflict-free work, not by number of branches created.

## 22. Canonicalization and verified promotion

### 22.1 Bootstrap candidate verification

Issue #5 verifies this exact Issue #4 work state, including:

- candidate content;
- finding-disposition artifact;
- canonicalization manifest;
- simulated generated Wave 1 issue graph;
- capsule/state/claim/recovery/fence rules;
- context-budget behavior;
- canonical transformation rules;
- current `main` base.

PASS records `candidate_work_sha`, manifest blob/path, and `verified_base_main_sha`.

### 22.2 Bootstrap Issue #6

Issue #6 may act only on that exact PASS. It constructs the canonicalization PR using only transformations enumerated in the verified manifest.

Immediately before merge:

- PR head must equal the expected materialized head;
- current `main` must equal `verified_base_main_sha`; otherwise compatibility/reverification is required;
- no unresolved verification BLOCKER/MAJOR may exist;
- generated canonical files must match the manifest’s deterministic transformation rules.

The PR is squash-merged. Only after obtaining the resulting main SHA does Issue #6 instantiate Wave 1, validate all 23 issue contracts, and post terminal `DONE`.

### 22.3 Wave-1 canonicalization

`W1-SYN-FINAL` MUST emit a machine-readable promotion/next-wave manifest. `W1-VERIFY-01` verifies it. `W1-CANON-01` may only perform enumerated transformations and bounded issue creation from that verified manifest, with the same verified-base/current-main rule.

## 23. Backlog retirement, garbage collection, and next-wave governor

Planning state is not append-only backlog growth.

At every final synthesis/canonicalization checkpoint:

- obsolete issues are closed or marked `SUPERSEDED`/`INVALIDATED` with provenance;
- branches/PRs no longer needed are explicitly retired according to repository policy;
- invalid dependency edges are removed from the active manifest;
- duplicate candidate missions are merged or deferred;
- candidate work not selected for the next wave remains data, not active GitHub issues.

`next_wave_candidates` use the same minimum contract fields as Planning Program issues: mission ID, role, priority, objective, prerequisites, ownership surface, inputs, output, evidence, acceptance, review, downstream, and integration rule.

A canonicalization may instantiate at most:

- **24 total new issues** in one next-wave activation; and
- **12 initially READY issues**.

The issue compiler/auditor must validate uniqueness, dependency acyclicity, ownership conflicts, required review routes, output-path collisions, and activation prerequisites before creation. Candidates above the cap remain deferred in the dependency map for later checkpoint selection.

## 24. Observability / evaluation

Track at minimum:

- cold-start success/failure;
- invalid capsule count/reasons;
- duplicate claim attempts prevented;
- orphan probes/recoveries;
- stale-ownership takeovers and fence aborts;
- handoff reconstruction success;
- context packet sizes and split/retrieval incidents;
- useful READY frontier width;
- review findings and escape rate;
- liveness incidents;
- retired versus created work;
- branch/ownership conflicts;
- attempts to self-review/self-canonicalize;
- base-drift invalidations;
- non-squash integration attempts.

These are diagnostic signals, not a scalar reward function.

## 25. Failure modes

The program explicitly defends against:

- branch created before claim then abandoned;
- stale writer continuing after recovery;
- malformed/edited/future-dated status comments changing authority;
- ambiguous review disposition transitions;
- reviewer independence faked by a new UUID;
- review fan-in exceeding reliable context;
- canonical files/issues transformed after verification without constraint;
- `main` changing after verification;
- Wave 1 issue activation before canonical merge;
- reusable recovery branches diverging after squash;
- unbounded next-wave issue generation;
- hidden human approval gates;
- proposal provenance being mistaken for canonicality;
- implementation beginning before readiness.

## 26. Risks

### 26.1 Procedural fencing is not a mature dispatcher

The expected-parent + ownership-generation checks are a temporary compliance protocol. W1-FAC-02 must design/test a stronger machine-enforced claim/control plane.

### 26.2 Independence is only minimally enforceable

Cold-start context separation is stronger than UUID separation but weaker than credential/service isolation. W1-FAC-03 must design stronger trust boundaries.

### 26.3 Context thresholds are provisional

The 100k-character/50%-window rule is a guardrail, not an optimized value. W1-FAC-01/FAC-04 should benchmark review depth versus packet size and revise it through reviewed factory change work.

### 26.4 Wave-size caps may be conservative or too permissive

The 24-total/12-READY governor is intentionally reversible. Useful-throughput evidence may justify a reviewed change.

## 27. Open questions

- Which GitHub/native automation should replace procedural branch fences?
- What platform/run identity and permission boundaries can strongly enforce reviewer independence?
- What measured context budget best predicts deep review success?
- Which evidence surfaces require protected storage/services?
- Which engine candidates survive hard constraints and deserve empirical spikes?
- Which game-system boundaries preserve both sandbox depth and technical parallelism?

These are bounded planning questions, not reasons for routine human escalation.

## 28. Reopen conditions

Reconsider Planning Program v1 if:

- Issue #5 cannot derive one deterministic next task from repository + GitHub state;
- two compliant sessions can remain authorized writers after a recovery;
- capsule validity requires agent-invented policy;
- orphan recovery cannot make progress without a human;
- mandatory review packets repeatedly exceed the budget or produce shallow inspection;
- canonicalization can change verified semantics without a new verification gate;
- `main` base drift is accepted without compatibility/reverification;
- useful READY frontier width collapses because of avoidable serialization;
- recovery episodes recur without root-cause remediation;
- next-wave caps routinely cause harmful starvation or fail to prevent WIP explosion;
- explicit later human directives supersede binding constraints.

## 29. Required independent critique / verification

Bootstrap Issue #5 is the required next independent role. It MUST begin cold from repository + GitHub state and verify the exact Issue #4 candidate work SHA and manifest, including adversarial simulations of:

- two simultaneous new claimants;
- branch-create/claim-comment crash;
- intentional handoff resume race;
- expired owner continuing after recovery;
- malformed/edited capsule ordering;
- `CHANGES_REQUIRED` versus `INVALIDATED` downstream routing;
- context budget overflow;
- no-READY liveness path;
- canonical-promotion transformation;
- `main` advancing after PASS;
- pre-activation Wave 1 claim attempt;
- author/reviewer identity reuse;
- squash-only integration.

PASS is prohibited while a BLOCKER/MAJOR remains.

## 30. Downstream work unblocked

When Issue #4 records this complete work state as `VERIFICATION_READY`, only Bootstrap Issue #5 is newly eligible.

A PASS from #5 may unlock Bootstrap Issue #6 for the exact candidate/base pair. Only #6 may promote this program and instantiate the first planning wave. None of these transitions authorizes gameplay implementation or a mass implementation backlog.