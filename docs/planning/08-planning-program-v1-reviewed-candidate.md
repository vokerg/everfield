# Planning Program v1 — Reviewed Candidate

**State:** REVIEWED-CANDIDATE  
**Bootstrap issue:** #4  
**Authority:** Candidate operating model only. It MUST NOT become CANONICAL until Bootstrap Issue #5 independently verifies this exact candidate work state and Bootstrap Issue #6 performs the verified, mechanically constrained promotion.  
**Scope:** Planning work only. This document does not authorize gameplay implementation, mass implementation issue generation, or a final engine choice.

## 1. Status

This document replaces the operational content of the Issue #2 base proposal plus Amendments 1–2 with one coherent reviewed candidate. The complete Issue #3 adversarial review was synthesized into this revision.

All Issue #3 BLOCKER and MAJOR findings are accepted and corrected. Exact dispositions are recorded in `docs/planning/reviews/issue-3-finding-dispositions.md`.

The machine-readable promotion and Wave 1 mission contract is `docs/planning/08-planning-program-v1-canonicalization-manifest.yaml`. This document, the dispositions, and that manifest are one immutable Issue #4 work state for Bootstrap Issue #5 verification.

## 2. Scope

Planning Program v1 governs autonomous planning after bootstrap canonicalization through the first bounded detailed-planning wave. It defines:

- cold-start task discovery and deterministic eligibility;
- temporary task claiming, continuation, stale/orphan recovery, and write fencing;
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

- `docs/planning/07-planning-program-v1-proposal.md`;
- `docs/planning/07-planning-program-v1-proposal-amendment-1.md`;
- `docs/planning/07-planning-program-v1-proposal-amendment-2.md`;
- `docs/planning/reviews/issue-2-adversarial-review.md`;
- bootstrap `/AGENTS.md` and `docs/planning/START-HERE.md` at the Issue #4 base `main@21a3c1a5053f3697be3f82f6fe73de42423a482b`.

No prior chat history is an authoritative input.

### 3.2 Observed evidence versus recommendation

Observed repository/GitHub constraints outrank this candidate:

- repository + GitHub state must be sufficient for cold start and continuation;
- no routine human approval state exists;
- review and verification must acquire independent evidence;
- context is budgeted;
- work must be resumable;
- canonicality is explicit;
- every accepted integration into `main` is squash-only.

During Issue #4 synthesis, the current GitHub connector was empirically checked against an individual issue-comment REST resource and it exposes immutable comment ID plus server `created_at` and `updated_at`. Therefore the capsule ordering/edit-detection rules below are executable with current repository tooling. If a future connector surface omits those fields, the agent must fetch the individual GitHub comment resource by ID before using the comment to create or expire authority.

No unstable external technical fact is asserted as settled. Missions requiring current GitHub, engine, legal, platform, or tool claims must source or empirically test them.

## 4. Goals

A fresh agent must be able to determine without hidden context:

1. current planning phase and entry path;
2. highest-priority eligible work;
3. whether a task branch is owned, handed off, stale, orphaned, review-ready, terminal, or invalid;
4. how to claim/resume without authorizing two compliant writers;
5. exact branch/base and immutable upstream inputs;
6. exact output/schema and context budget;
7. evidence/acceptance requirements;
8. exact review/synthesis/verification route;
9. stopping/handoff behavior;
10. what to do with no READY work;
11. canonicalization bound to candidate and verified `main` state;
12. bounded downstream issue generation;
13. the implementation-readiness barrier.

## 5. Non-goals

Planning Program v1 does not:

- implement gameplay;
- choose a final engine;
- freeze architecture or game design;
- instantiate the 50 seed missions;
- create a full implementation backlog;
- permit producer self-canonicalization;
- use labels as the dispatcher source of truth;
- treat a self-selected UUID as proof of independence;
- treat branch count as proof of useful parallelism.

## 6. Constraints

1. `main` is the stable canonical base.
2. Normal task branches are deterministic: `planning/issue-N`.
3. One normal task has at most one authorized ownership generation at a time.
4. All branch mutations are expected-parent/fast-forward operations; force-push is forbidden.
5. Upstream non-main artifacts are consumed by exact immutable work SHA.
6. `BLOCKED` and `READY` are derived states, not manually flipped gates.
7. Operational capsules are append-only; edited capsules cannot create authority.
8. Lease age derives from GitHub server metadata, not a self-authored future timestamp.
9. Canonicality cannot be inferred from merge, PR, issue closure, or file location alone.
10. Every `main` integration is squash-only.
11. Wave 1 issues are instantiated only after Bootstrap Issue #6 is squash-merged and the resulting main SHA is known.
12. High-throughput implementation remains blocked until a later verified implementation-readiness decision.

## 7. Assumptions

These remain testable assumptions, not hidden facts:

- GitHub comment identity/server time plus expected-parent branch writes are adequate as a temporary planning-phase ownership protocol when all compliant agents perform the fence below;
- a six-hour lease TTL is a reasonable provisional default if renewals require substantive evidence and stale generations are fenced;
- a maximum initial READY frontier of 12 and maximum 24 newly instantiated issues per later wave are safe provisional governors;
- Review Indexes plus targeted retrieval can preserve review depth under context constraints;
- procedural cold-start separation is sufficient minimum independence until stronger platform/credential controls are designed.

## 8. Alternatives considered

- **Unfenced comment leases:** rejected because expiry changes belief, not write authority.
- **Pre-create Wave 1 before canonical merge:** rejected because the future squash SHA is unknowable.
- **Free-form canonicalization rewrite:** rejected because verification would not cover the actual authority transition.
- **Permanent reusable recovery branch:** rejected because squash integration makes repeated branch ancestry ambiguous.
- **Instantiate every next-wave candidate:** rejected because it recreates WIP/backlog explosion through the canonical path.

## 9. Canonical cold-start entry

After Bootstrap Issue #6 completes, a fresh planning agent MUST:

1. read `/AGENTS.md`;
2. read canonical `docs/planning/START-HERE.md`;
3. read canonical `docs/planning/PLANNING-PROGRAM-v1.md` from current `main`;
4. query open `[PLAN-v1]` issues;
5. validate issue contracts and latest operational capsules under Section 10;
6. derive eligibility from prerequisites, branch state, ownership generation, lease validity, and terminal state;
7. prefer queue classes: recoverable/handoff work → review/revision/verification/integration → new proposal/research;
8. within a class choose lower `priority_rank`, then lower GitHub issue number;
9. re-read selected issue immediately before claim/resume;
10. load only its bounded packet under Section 15;
11. claim/resume under Sections 11–13;
12. before every repository mutation re-check the ownership fence;
13. before stopping commit useful state and leave structured handoff/status.

If there is no READY/recoverable work, use Section 16 rather than inventing parallel work or waiting for a human.

## 10. Operational state and capsule protocol

### 10.1 Derived and recorded states

Derived eligibility states:

- `BLOCKED` — a hard prerequisite is unsatisfied;
- `READY` — prerequisites are satisfied, no terminal state exists, and no valid active owner exists.

Recorded task states:

- `IN_PROGRESS`;
- `HANDOFF_READY`;
- `REVIEW_READY`;
- `CHANGES_REQUESTED`;
- `VERIFICATION_READY`;
- `INTEGRATION_READY`;
- `DONE`;
- `SUPERSEDED`;
- `INVALIDATED`.

Derived recovery classifications:

- `ORPHANED_BRANCH` — deterministic branch exists, no valid ownership capsule exists, and orphan-probe grace matured;
- `STALE_OWNER` — latest valid ownership/renewal lease expired with no later valid ownership/handoff/review/terminal capsule.

Labels are advisory views only.

### 10.2 Valid capsule definition

Operational capsules are GitHub issue comments with YAML bodies containing `protocol: planning-v1` and `schema: 1`.

A capsule is valid for authority only if:

- the individual GitHub comment resource confirms it is unedited (`created_at == updated_at`);
- required fields for its `kind` are present/type-valid;
- `issue`, `mission_id`, and branch agree with the issue contract;
- referenced SHAs exist and match relevant branch/artifact state;
- predecessor/state transition is allowed by Section 14;
- required prerequisite predicate is satisfied;
- no later valid capsule supersedes the authority it claims.

Capsules are ordered by immutable GitHub comment ID/server creation order. Body timestamps are descriptive only. Lease start is the GitHub server creation time of the winning `CLAIM`, `RESUME`, `RECOVER`, or valid renewing `PROGRESS` capsule.

Edited, malformed, impossible-transition, wrong-branch, wrong-mission, or unsupported-version capsules are ignored for operational authority and recorded as invalid evidence when relevant.

### 10.3 Ownership generation

Every ownership-granting capsule records:

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

The ownership generation is the GitHub comment ID of the latest valid ownership-granting capsule. The default lease expires six hours after that comment's GitHub server creation time or a valid renewal.

## 11. New-work claim and orphan recovery

For eligible Issue `#N`:

1. re-read issue/prerequisites/branch/capsules;
2. resolve current `main` SHA;
3. create exactly `planning/issue-N` from that SHA;
4. immediately post `CLAIM` with the created branch head;
5. re-fetch comments/head; claim is active only if it is the earliest valid ownership capsule for that created branch/head;
6. before first edit perform Section 13 fence.

If the deterministic branch exists but no valid ownership capsule exists:

1. do not edit or create an alternate branch;
2. if a valid `ORPHAN_PROBE` already exists and its GitHub-server age is at least ten minutes with no later ownership capsule, classify `ORPHANED_BRANCH`;
3. otherwise post one best-effort `ORPHAN_PROBE` with issue, branch, observed head and base relation, then leave this issue unedited for the current episode; another eligible task may be selected;
4. a later agent observing the mature probe re-checks history and posts `RECOVER` referencing the probe; earliest valid recovery by GitHub order wins.

The grace prevents takeover during the normal branch-create→claim window while guaranteeing eventual repository-visible recovery without a human gate.

## 12. Intentional resume, stale recovery, and renewal

### 12.1 Intentional handoff

A task is resumable when latest valid status is `HANDOFF_READY` with exact `work_sha` and branch `head_sha`. Contenders post `RESUME_INTENT`; earliest valid intent wins, then posts `RESUME`. Later contenders stop without editing.

### 12.2 Stale owner

An owner is stale when latest valid ownership/renewal server time is older than six hours and no later valid handoff/review/terminal status exists. Recovery uses the same intent ordering, then winner posts `RECOVER` referencing expired ownership and exact observed head.

Expiry alone is not revocation; Section 13 fencing revokes stale-generation authorization.

### 12.3 Renewal quality

A valid `PROGRESS` renewal references current ownership generation and includes either:

- a new remote branch head with substantive committed work; or
- immutable evidence for a bounded check/experiment that materially advances the task.

No more than three consecutive renewals without branch-head advance are valid. A fourth is ignored for lease extension.

## 13. Mandatory mutation fence

Immediately before **every** task-branch repository mutation, the agent MUST:

1. fetch latest valid operational comments;
2. confirm its ownership-generation comment is still latest valid owner grant and lease is unexpired;
3. fetch remote task-branch head;
4. confirm head equals the exact parent on which the mutation is based;
5. perform only expected-parent/fast-forward write;
6. on generation/head mismatch abort, inspect new state, and follow resume/recovery rather than force history.

A compliant stale session therefore loses authorization as soon as a later valid ownership generation exists.

## 14. Mission-class transitions and review dispositions

### 14.1 Producer/root proposal missions

`READY` → valid claim/resume/recover → `IN_PROGRESS` → intentional yield `HANDOFF_READY` or completed producer acceptance → `REVIEW_READY`.

A producer cannot advance its own work to `VERIFICATION_READY`, `INTEGRATION_READY`, or CANONICAL.

### 14.2 Review missions

A review task finishes `DONE` with exactly one disposition:

- `PASS_FOR_SYNTHESIS` — no BLOCKER/MAJOR requiring revision before synthesis;
- `CHANGES_REQUIRED` — bounded findings MUST be dispositioned by declared synthesis/revision mission; **this unlocks that synthesis mission**;
- `INVALIDATED` — path is unsafe to synthesize as-is; unlocks only declared recovery/replanning path.

“Completed review” alone is never a sufficient prerequisite; issue contracts name allowed dispositions.

### 14.3 Domain synthesis missions

`W1-SYN-FAC`, `W1-SYN-TECH`, and `W1-SYN-GAME` become `REVIEW_READY` only when:

- required review has an allowed disposition (`PASS_FOR_SYNTHESIS` or `CHANGES_REQUIRED`);
- every BLOCKER/MAJOR is dispositioned `ACCEPTED`, `REJECTED_WITH_EVIDENCE`, or `CONVERTED_TO_EXPERIMENT`;
- unresolved conflicts/experiments are explicit;
- their cross-domain review inputs and exact work SHAs are recorded.

They are then reviewed by `W1-REV-CROSS`; they do **not** become `VERIFICATION_READY` directly.

### 14.4 Final synthesis / bootstrap synthesis

A final synthesis candidate (`W1-SYN-FINAL`, and analogously this Bootstrap Issue #4 candidate) becomes `VERIFICATION_READY` only when:

- all required review inputs have allowed dispositions;
- every BLOCKER/MAJOR is explicitly dispositioned;
- no unresolved BLOCKER remains on a transition claimed safe;
- exact candidate plus promotion/canonicalization manifest are in one immutable work state;
- required downstream verification contract is explicit.

### 14.5 Verification

Verification records PASS/FAIL for:

- exact candidate work SHA;
- exact promotion/canonicalization manifest from that work state;
- exact `verified_base_main_sha`;
- exact issue-graph/contract simulation inputs.

PASS is forbidden with unresolved BLOCKER/MAJOR defects.

### 14.6 Integration/canonicalization

`INTEGRATION_READY` requires PASS tied to exact candidate and base. If current `main != verified_base_main_sha`, prior PASS is insufficient until independent bounded compatibility/reverification covers every intervening main commit. A changed binding directive invalidates the old PASS until reverified.

## 15. Context-loading and evidence budgets

### 15.1 Always-read context

Every normal Wave 1 mission reads only:

- `/AGENTS.md`;
- canonical `docs/planning/START-HERE.md`;
- selected GitHub issue;
- canonical `docs/planning/PLANNING-PROGRAM-v1.md` at activation SHA;
- issue-declared authoritative packet.

Everything else is forbidden-by-default unless an optional retrieval trigger is met.

### 15.2 Root Review Index

Every root proposal begins with a **Review Index** no larger than 4,000 UTF-8 characters containing stable section IDs for:

- claims/decisions;
- interfaces/dependencies;
- assumptions/open questions;
- evidence pointers;
- conflict surfaces;
- reviewer attack points.

### 15.3 Mandatory packet budget

For review/synthesis, simultaneously mandatory context is limited to the lesser of:

- 100,000 UTF-8 characters; or
- 50% of known execution context window.

Mandatory packet = entry docs + issue/status + upstream Review Indexes + required finding/interface/evidence indexes, not every full source artifact.

If over budget, silently truncating is forbidden. The task must use stable-pointer targeted retrieval or a bounded sub-review split explicitly authorized by its contract/manifest. Findings cite full sections actually inspected.

### 15.4 Evidence protocol

Artifacts distinguish observed evidence, inference, recommendation/decision, and assumption. Current external technical/legal/tool claims require authoritative sources or explicit deferral. Empirical claims record reproducible inputs, outputs, environment, and artifact pointers.

## 16. No-READY liveness and recovery lifecycle

When no ordinary READY task exists:

1. valid active ownership that can unblock graph → graph live, do not duplicate;
2. `HANDOFF_READY`, mature orphan, or stale owner → recover it;
3. eligible review/revision/verification/integration → execute before new proposals;
4. otherwise classify liveness defect: cycle, orphan prerequisite, invalidated dependency, missing transition, or corrupted status.

`W1-REC-01` is a **single-use** recovery task initially `BLOCKED`, conditionally READY only for case 4. It may restore the smallest credible READY path but cannot waive review, verification, canonicalization, or squash integration.

After accepted/integrated recovery, that task is `DONE`. If planning remains active, the recovery integration may instantiate exactly one successor (`W1-REC-02`, then `W1-REC-03`, etc.) in `BLOCKED`. Every recovery issue has ordinary one-task/one-branch lifetime; no post-squash branch is reused indefinitely.

## 17. Branch, handoff, PR, integration semantics

- New tasks branch from current `main` unless issue names immutable alternative.
- WIP commits should preserve reconstructable state.
- Every repository-changing episode updates `docs/planning/handoffs/issue-N.md`.
- Handoff records substantive `work_sha`; final issue `STATUS` records resulting branch `head_sha` after handoff commit.
- PRs may exist for diff/provenance visibility without authority transition.
- Provenance merge does not confer CANONICAL state.
- All `main` integration is squash-only.
- Canonical integration checks expected candidate/head and verified base/current-main compatibility.

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

Status; Review Index; Scope; Inputs; Goals; Non-goals; Constraints; Assumptions; Evidence/source basis; Alternatives; Proposed design; Interfaces/dependencies; Observability/evaluation; Failure modes; Risks; Open questions; Reopen conditions; Required independent critiques; Downstream work.

### 18.2 Review

Status; reviewed mission IDs/work SHAs; independent execution-context provenance; attack plan; findings table; contradictions; empirical questions; disposition (`PASS_FOR_SYNTHESIS | CHANGES_REQUIRED | INVALIDATED`); required next action.

### 18.3 Synthesis

Proposal schema plus exact producer/review SHAs, every BLOCKER/MAJOR disposition, interface contracts, unresolved conflicts/experiments, candidate decisions/reopen conditions, downstream review/verification contract.

### 18.4 Verification

```text
Status: PASS | FAIL
Candidate work_sha
Promotion/canonicalization manifest path + blob/work SHA
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

Minimum acceptable independence for required reviewer/verifier is a **distinct cold-start execution context** that:

- lacks producer private conversation/scratch context;
- begins from repository + GitHub entry state;
- records platform execution/run identity when exposed;
- records prior mission roles excluded from satisfying the gate;
- obtains its own evidence before reconciling prior reviewer conclusions.

Self-selected `session_id` is episode tracking, not proof of independence.

If platform run identity is unavailable, procedural cold-start separation is temporarily permitted but explicitly recorded as a trust risk. A human directive may override workflow ordering when explicitly recorded, but it does not silently masquerade as independent evidence.

## 20. First-wave mission DAG

### 20.1 Activation and exact contracts

Bootstrap Issue #6 does **not** pre-create Wave 1 issues.

After its canonicalization PR is squash-merged:

1. obtain resulting `main` SHA;
2. verify canonical program exists at that SHA and matches verified promotion transform;
3. instantiate exactly 23 initial Wave 1 issues from `docs/planning/08-planning-program-v1-canonicalization-manifest.yaml`;
4. each issue records concrete activation main SHA and remains blocked until Issue #6 terminal `DONE`;
5. validate every created issue contract against manifest;
6. post mission-ID→GitHub-issue mapping and Issue #6 `DONE`;
7. derived eligibility makes the 12 roots READY.

The manifest is the normative machine-readable source for exact mission titles, priorities, prerequisites, context packets, output paths/schemas, review routes, acceptance classes, and integration rules.

Initial 23 missions:

- roots: `W1-GOV-01`, `W1-FAC-01`, `W1-FAC-02`, `W1-FAC-03`, `W1-FAC-04`, `W1-TEC-01`, `W1-TEC-02`, `W1-DES-01`, `W1-DES-02`, `W1-DES-03`, `W1-EXP-01`, `W1-EVAL-01`;
- reviews: `W1-REV-FAC`, `W1-REV-TECH`, `W1-REV-GAME`;
- syntheses: `W1-SYN-FAC`, `W1-SYN-TECH`, `W1-SYN-GAME`;
- cross review: `W1-REV-CROSS`;
- final synthesis: `W1-SYN-FINAL`;
- verification: `W1-VERIFY-01`;
- canonicalization: `W1-CANON-01`;
- recovery: `W1-REC-01`.

```text
Issue #6 squash merge -> post-merge instantiate + validate 23 issues -> Issue #6 DONE
        |
        +--> 12 roots in parallel
                |
                +--> REV-FAC ----> SYN-FAC --+
                +--> REV-TECH ---> SYN-TECH -+--> REV-CROSS --> SYN-FINAL --> VERIFY --> CANON
                +--> REV-GAME ---> SYN-GAME -+

REC-01: conditionally eligible only on liveness defect.
```

`CHANGES_REQUIRED` unlocks declared synthesis/revision. `INVALIDATED` does not; it routes to recovery/replanning.

## 21. Safe concurrency boundaries

Root missions own unique output paths. Each issue names filesystem ownership, semantic conflict surface, hard prerequisites, and review dependencies. Two siblings that must mutate the same canonical file are not safe siblings; they emit unique proposals and converge through synthesis.

Useful parallelism is measured by independently progressing conflict-free work, not number of branches.

## 22. Canonicalization and verified promotion

### 22.1 Bootstrap Issue #5

Issue #5 verifies the exact Issue #4 work state containing:

- this candidate;
- finding-disposition artifact;
- canonicalization manifest;
- simulated generated Wave 1 issue graph;
- capsule/state/claim/recovery/fence rules;
- context budget;
- canonical transformation rules;
- current `main` base.

PASS records `candidate_work_sha`, manifest identity, and `verified_base_main_sha`.

### 22.2 Bootstrap Issue #6

Issue #6 acts only on that exact PASS and constructs canonicalization PR using transformations enumerated in verified manifest.

Immediately before merge:

- PR head equals expected materialized head;
- current `main == verified_base_main_sha`, otherwise independent compatibility/reverification is mandatory;
- no unresolved verification BLOCKER/MAJOR exists;
- generated canonical files match deterministic transformation rules.

PR is squash-merged. Only after resulting main SHA is known does Issue #6 instantiate Wave 1, validate all 23 contracts, and post terminal `DONE`.

### 22.3 Wave-1 canonicalization

`W1-SYN-FINAL` emits a machine-readable promotion/next-wave manifest. `W1-VERIFY-01` verifies it. `W1-CANON-01` performs only enumerated transformations and bounded issue creation from that verified manifest, with the same verified-base/current-main rule.

## 23. Backlog retirement, garbage collection, and next-wave governor

At each final synthesis/canonicalization checkpoint:

- obsolete issues become `SUPERSEDED`/`INVALIDATED` or are closed with provenance;
- obsolete branch/PR state is retired under repository policy;
- invalid dependency edges leave active manifest;
- duplicate candidates merge/defer;
- unselected candidate work remains data, not active issues.

Every `next_wave_candidate` must carry mission ID, role, priority, objective, prerequisites, ownership surface, inputs, outputs/schema, evidence, acceptance, review, downstream, integration rule.

Per next-wave activation, canonicalization may instantiate at most:

- **24 total new issues**;
- **12 initially READY issues**.

Issue compiler/auditor validates unique IDs, acyclic hard dependencies, ownership conflicts, review routes, output collisions, and activation prerequisites before creation. Excess candidates remain `DEFERRED` in dependency map.

## 24. Observability / evaluation

Track at minimum:

- cold-start success/failure;
- invalid capsule count/reasons;
- duplicate-claim attempts;
- orphan probes/recoveries;
- stale takeovers and fence aborts;
- handoff reconstruction success;
- context packet sizes and split/retrieval incidents;
- useful READY frontier width;
- review findings/escape rate;
- liveness incidents;
- retired versus created work;
- branch/ownership conflicts;
- self-review/self-canonicalization attempts;
- base-drift invalidations;
- non-squash integration attempts.

These are diagnostic signals, not a scalar reward.

## 25. Failure modes

The program explicitly defends against:

- branch-created-before-claim abandonment;
- stale writer continuing after recovery;
- malformed/edited/future-dated status comments creating authority;
- ambiguous review-disposition transitions;
- independence faked by new UUID;
- review fan-in exceeding reliable context;
- post-verification canonical transformation drift;
- `main` changing after verification;
- Wave 1 activation before canonical merge;
- recovery branch reuse after squash;
- unbounded next-wave issue generation;
- hidden human approval;
- provenance mistaken for canonicality;
- implementation beginning before readiness.

## 26. Risks

- **Procedural fencing:** temporary; W1-FAC-02 must design/test stronger machine-enforced control plane.
- **Independence:** cold-start separation is weaker than credential/service isolation; W1-FAC-03 must strengthen it.
- **Context thresholds:** 100k/50% is a provisional guardrail; W1-FAC-01/FAC-04 should benchmark it.
- **Wave caps:** 24-total/12-READY is reversible and should be tuned from verified throughput evidence.

## 27. Open questions

- Which GitHub/native automation should replace procedural fences?
- What platform/run identity and permission boundaries strongly enforce reviewer independence?
- What measured context budget best predicts deep review success?
- Which evidence surfaces require protected storage/services?
- Which engine candidates survive hard constraints and deserve empirical spikes?
- Which game-system boundaries preserve sandbox depth and technical parallelism?

These are bounded planning questions, not reasons for routine human escalation.

## 28. Reopen conditions

Reconsider v1 if:

- Issue #5 cannot derive one deterministic next task from repository + GitHub state;
- two compliant sessions can remain authorized writers after recovery;
- capsule validity requires invented policy;
- orphan recovery cannot progress without a human;
- mandatory review packets repeatedly exceed budget or induce shallow inspection;
- canonicalization changes verified semantics without new verification;
- base drift is accepted without compatibility/reverification;
- useful READY frontier collapses due avoidable serialization;
- recovery episodes recur without root-cause remediation;
- wave caps cause harmful starvation or fail to prevent WIP explosion;
- a later explicit human directive supersedes a binding constraint.

## 29. Required independent verification

Bootstrap Issue #5 is the required next role. It MUST cold-start from repository + GitHub state and verify exact Issue #4 work SHA and manifest with adversarial simulations of:

- simultaneous new claimants;
- branch-create/claim-comment crash;
- intentional handoff race;
- expired owner continuing after recovery;
- malformed/edited capsule ordering;
- `CHANGES_REQUIRED` versus `INVALIDATED` routing;
- domain synthesis `REVIEW_READY` versus final synthesis `VERIFICATION_READY`;
- context-budget overflow;
- no-READY liveness;
- canonical-promotion transformation;
- `main` advancing after PASS;
- pre-activation Wave 1 claim attempt;
- author/reviewer identity reuse;
- squash-only integration.

PASS is prohibited while a BLOCKER/MAJOR remains.

## 30. Downstream work unblocked

When Issue #4 records this complete immutable work state as `VERIFICATION_READY`, only Bootstrap Issue #5 is newly eligible.

A PASS from #5 may unlock Bootstrap Issue #6 for the exact candidate/base pair. Only #6 may promote this program and instantiate the first planning wave. None of these transitions authorizes gameplay implementation or a mass implementation backlog.