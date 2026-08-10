# GitHub Control Plane, Dependencies, and Scheduler — Wave 1 Proposal

**Mission:** `W1-FAC-02`  
**State:** PROPOSED / NON-CANONICAL  
**Role:** control-plane / scheduler planner  
**Required reviews:** `W1-REV-FAC`, `W1-REV-TECH`  
**External evidence snapshot:** 2026-08-10, official GitHub documentation only

## Review Index

**Core recommendation.** Treat GitHub Issues/PRs/refs/checks as the durable execution substrate, but not every GitHub field as authority. The canonical task graph/contract remains repository-owned and content-addressed; GitHub native issue dependencies mirror hard `BLOCKED_BY` edges; issue bodies/Projects are query/UX projections; schema-valid operational events and branch/ref transactions carry authority.

**Atomic ownership.** New task claim can continue using deterministic task-branch creation as exclusion. Mature resume/recovery/conflict locking should move to a GitHub App transaction that creates a same-tree **ownership fence commit** and atomically compare-and-swaps the task ref plus one or more deterministic conflict-lock refs. GitHub GraphQL `updateRefs` supports atomic multi-ref updates and `beforeOid` assertions, including zero OID to require nonexistence. This exact lock-ref protocol must be empirically spiked before adoption; labels, assignees, Projects fields, or comments alone are not atomic locks.

**READY derivation.** Derive, do not manually label: activation/canonical binding valid; all hard dependencies satisfied by valid exact results; task not terminal/superseded/invalidated; no current owner; no incompatible active conflict lock; branch/recovery state coherent; required independence mode available; wave/WIP governor permits admission. Native GitHub dependencies are a visibility/query mirror, while typed richer edges remain in immutable task/graph manifests.

**Scheduler.** Use deterministic class-first scheduling: canonical/main recovery → resumable/stale/orphan recovery → review/revision/verification/integration → new production/proposal. Within class use explicit `priority_rank`, then measured/declared unblock value only as a versioned secondary policy, then issue number. Enforce per-class/domain/global WIP caps and prefer finishing evidence/review queues over starting comparable-priority work.

**Merge/integration.** Protect `main` with PR requirement, required checks from expected Apps, no force-push, linear history, and no bypass where feasible. Repository settings should disable merge-commit/rebase methods and allow squash. Integration must re-fetch current base, valid verification, expected PR head, and use the merge API head-SHA guard with `merge_method=squash`. Do not adopt merge queue until an empirical spike proves it preserves the project’s one-squash-commit-per-task directive under repository/ruleset configuration.

**Automation architecture.** Prefer a least-privilege GitHub App + reconciliation loop over agent convention: webhook/event wakeup → fresh state read → deterministic derivation → compare-and-swap mutation → append immutable evidence/status. Projects/custom fields are derived dashboards/caches, never authority. Separate verifier/check-producing permissions from ordinary producer/control-plane permissions where W1-FAC-03 requires trust isolation.

**Primary review attacks.** lock-ref namespace unsupported/ruleset-conflicted; lease races; ref lock orphaning; multi-lock deadlocks; stale derived caches; dependency cycles; issue edits diverging from canonical contracts; expected-head merge without expected-base protection; status spoofing; scheduler starvation; WIP metric gaming; merge queue violating squash; App over-permission; webhook loss/duplication; garbage collection deleting evidence.

**Decisive spikes.** GraphQL `updateRefs` multi-ref claim/lock CAS; crash points around lock/comment/handoff; native dependency mirror drift; ruleset + required-App check enforcement; expected-head/current-base squash merge; merge-queue squash behavior; webhook replay/reconciliation; WIP scheduler benchmark; lock/ref garbage collection.

## 1. Status

This proposal defines the target GitHub-centered control plane and scheduler. It extends the semantic task/episode requirements planned by W1-FAC-01 but owns the exact machine state, dependency mirroring, claim/fence mechanics, scheduling, PR integration, and garbage-collection recommendations.

It does not modify repository rulesets or install a GitHub App in this mission. Several enforcement mechanisms are intentionally **proposal + spike** until validated against this repository and account/plan configuration.

## 2. Scope

This proposal covers:

1. authoritative versus derived control-plane state;
2. issue contract/graph representation;
3. native and typed dependency modeling;
4. atomic claim/resume/recovery/conflict locking;
5. lease/fencing semantics;
6. deterministic READY derivation;
7. WIP and scheduler policy;
8. PR/review/integration mechanics;
9. GitHub App, webhook, and reconciliation architecture;
10. Projects/dashboard role;
11. garbage collection and retirement;
12. control-plane observability and failure recovery.

## 3. Inputs and evidence

### 3.1 Repository evidence

The canonical/repository packet establishes:

- `AGENTS.md` requires canonical entry, repository-owned memory, resumability, evidence, review independence, designed parallelism, Goodhart resistance, and squash-only `main` integration;
- the autonomous-factory mandate requires eventual machine-atomic claiming, one active owner unless coordinated structure is explicit, WIP prioritization, deterministic handoffs, independent verification, checkpoint authority, and verified-throughput-oriented scheduling;
- the research agenda explicitly asks which GitHub-native relationships can represent issues/dependencies/projects/PRs, how atomic claim/stale recovery should work, how permissions should be divided, and how READY/conflicts should be derived;
- planning deliverables require issue taxonomy/state machine, dependency/conflict schema, READY algorithm, WIP/scheduler, stale-work/cycle handling, branch/PR/merge rules, automation permissions, and machine APIs;
- current canonical Planning Program v1 already proves a schema-3 event model, deterministic task branches, expected-parent mutation fencing, exact-work-SHA consumption, current-base verification, and squash-only integration;
- this repository successfully used head-SHA-protected squash merges during bootstrap (for example PR #20), and current connector ref updates use non-force fast-forward semantics.

### 3.2 Current official GitHub capability evidence

Only official GitHub documentation is used for current product/API claims:

| Ref | Capability used by this proposal | Official source |
|---|---|---|
| GH-REFS | REST ref update supports `force=false` for fast-forward-only update | https://docs.github.com/en/rest/git/refs |
| GH-ATOMIC-REFS | GraphQL `updateRefs` performs multiple ref updates atomically; `beforeOid` asserts prior OID and zero OID can assert nonexistence | https://docs.github.com/en/graphql/reference/git |
| GH-DEPS | REST API can list/add/remove issue `blocked by` / `blocking` dependencies | https://docs.github.com/en/rest/issues/issue-dependencies |
| GH-SUBISSUES | REST API can list/manage issue sub-issues | https://docs.github.com/en/rest/issues/sub-issues |
| GH-RULESETS | Rulesets can require PRs/status checks and block force-push among other controls; bypass actors can be configured | https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets |
| GH-PROTECTION | Protected branches can require PR review/checks, linear history, merge queue, deployment, restrict push, and disallow bypass | https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches |
| GH-MERGE | PR merge REST endpoint accepts `sha` that must match PR head and `merge_method` including `squash`; head mismatch returns conflict | https://docs.github.com/en/rest/pulls/pulls |
| GH-METHODS | Repository configuration can allow only chosen PR merge methods; squash combines PR commits into one commit | https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github |
| GH-REPO-CONFIG | Repository API exposes `allow_squash_merge`, `allow_merge_commit`, and `allow_rebase_merge` settings | https://docs.github.com/en/rest/repos/repos |
| GH-APP-PERMS | GitHub Apps use granular permissions; documentation recommends minimum required permissions | https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app |
| GH-PROJECTS | Projects has built-in status/auto-add/archive workflows and GraphQL/API automation; useful for derived views | https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations |

### 3.3 Important evidence limits

The documentation proves API/feature availability, **not** that every proposed combination works safely under Everfield’s current rulesets, repository plan, connector, permissions, race timing, or desired branch namespace. Specifically:

- this mission has not executed GraphQL `updateRefs` on this repository;
- arbitrary lock-ref/branch namespace behavior and its interaction with rulesets must be tested;
- GitHub does not provide a turnkey “exclusive issue lease with multi-resource locks” primitive in the evidence above;
- issue labels, assignees, comments, and Projects fields are mutable collaboration metadata and are not documented as compare-and-swap locks;
- merge-queue behavior must be tested against the project’s stricter squash-only history directive before adoption.

These remain explicit spikes, not assumptions.

## 4. Goals

The mature control plane should let a scheduler or fresh agent determine and enforce:

- exact canonical task contract/version;
- hard and typed dependencies;
- whether task state is BLOCKED/READY/owned/recoverable/terminal;
- one current mutation owner and ownership generation;
- atomic conflict-surface acquisition/release;
- safe task-branch mutation against expected head;
- lease/stale recovery without two authorized writers;
- deterministic work priority and WIP admission;
- exact review/verification/integration route;
- current-base/head eligibility for merge;
- task retirement, supersession, and evidence retention;
- reconstruction after webhook loss, scheduler crash, or stale cache.

The system should scale to many concurrent sessions without making GitHub UI state or agent convention the single source of truth.

## 5. Non-goals

This proposal does **not**:

- install/configure production rulesets or Apps now;
- claim that Projects/labels/assignees are authoritative state;
- choose exact task-size thresholds without measurement;
- define detailed reviewer/verifier evidence policy owned by W1-FAC-03;
- define CI/evidence schemas owned by W1-FAC-04;
- replace W1-FAC-01 task/episode/handoff semantics;
- require GitHub merge queue before its squash behavior is empirically verified;
- create a custom external database as the default authority without first exhausting GitHub-native/content-addressed options;
- authorize gameplay implementation.

## 6. Constraints

1. `main` remains the stable canonical base and is squash-only.
2. Task authority must be reconstructable from repository + GitHub state.
3. Exactly one current mutation owner per normal task unless explicit coordinated structure exists.
4. Stale writers must be mechanically fenced, not merely told to stop.
5. Conflict locks must not depend only on advisory labels/assignees.
6. Invalid/malformed/edited authority events fail closed.
7. Dependency cycles and missing transitions must be detectable before activation or during liveness recovery.
8. Scheduler policy must be deterministic enough for two compliant agents to choose the same work from the same snapshot.
9. WIP governors must limit issue/branch proliferation without starving recovery/review/integration.
10. Automation should use least privilege and separate quality/check authority where feasible.
11. Webhooks/events may wake reconciliation but cannot be assumed lossless/unique authoritative history.
12. A derived cache/dashboard may be rebuilt from authoritative state.
13. No routine human approval state may be introduced.

## 7. Assumptions

Provisional assumptions to test:

- GitHub GraphQL atomic ref updates can provide the CAS substrate for task ownership/conflict locking without an external transactional database.
- Using task-branch fence commits is acceptable because final integration squashes WIP/control commits.
- A modest number of deterministic lock refs/branches is operationally manageable if garbage-collected and excluded from normal task discovery.
- Native GitHub issue dependencies are valuable as a mirror of hard blocking edges, while richer edge semantics remain content-addressed in the canonical graph.
- A reconciliation GitHub App can derive state frequently enough that event delivery is an optimization rather than a correctness dependency.
- Project views/custom fields are useful for humans/agents inspecting queues even if they remain non-authoritative.

## 8. Alternatives considered

### 8.1 Labels/assignees as authoritative claim locks — rejected

They are convenient UI state but do not supply a documented compare-and-swap ownership transaction or multi-resource lock. Two actors can reason from stale reads.

### 8.2 Issue comments alone as lease/ownership authority — rejected as mature mechanism

Comments provide append-only-ish audit ordering when unedited, but posting a comment does not itself atomically fence the task branch or multiple conflict surfaces. Keep comments as audit/status evidence, not the sole write lock.

### 8.3 Central scheduler database is the only authority — rejected initially

It creates a new availability/provenance dependency and can diverge from GitHub/repository state. Prefer reconstructable GitHub/repo authority plus a derived scheduler cache. An external transactional store remains a fallback if ref-lock spikes fail.

### 8.4 Canonical graph entirely in GitHub issue bodies — rejected

Issue bodies are editable presentation surfaces and lack typed immutable version binding. Canonical activated graph/task contracts should be content-addressed repository artifacts; issue bodies mirror a bounded execution contract and link activation/version.

### 8.5 Canonical graph entirely in repository files with no native dependencies — rejected

This loses useful GitHub dependency visibility/query/UX. Mirror hard `blocked by` edges natively and continuously audit mirror drift.

### 8.6 Dynamic priority score as scheduler truth — rejected

One opaque scalar is hard to reproduce and easy to game. Use deterministic class/priority ordering first; benchmark any unblock-value heuristic before promotion.

### 8.7 Merge queue immediately — deferred

GitHub merge queue can protect a busy branch, but the project’s canonical human directive is one squash integration per accepted task. Adopt only after a repository spike verifies exact history semantics and expected verification/base behavior.

## 9. Proposed control-plane model

### 9.1 Authority layers

Use four layers with explicit precedence:

1. **Canonical graph/contract manifest on `main`** — task IDs, activation, typed dependencies, priority, conflict keys, output/schema, review route, wave governor.
2. **GitHub issue/PR/ref operational state** — task projection, native dependency mirror, branch/ref ownership, immutable operational events, PR/check/integration state.
3. **Derived scheduler/cache/Projects state** — READY indexes, dashboards, queue views, WIP metrics; rebuildable and never authoritative.
4. **Agent local state** — disposable and non-authoritative.

An issue body should include the readable contract plus immutable `contract_ref`/activation identity. If body text diverges from the referenced canonical contract, dispatcher fails closed and creates repair/reconciliation evidence; it does not guess which prose is newer.

### 9.2 Dependency model

Recommended typed edge taxonomy in the canonical graph:

```yaml
BLOCKED_BY: prerequisite terminal/result predicate required
REVIEW_OF: reviewer consumes exact producer work state
SYNTHESIZES: synthesis consumes named producer/review states
VERIFIES: verifier consumes exact candidate/manifest/base
CANONICALIZES: integrator consumes exact PASS/promotion
INTERFACE_WITH: non-blocking interface coordination/evidence edge
CONFLICTS_WITH: ownership/resource exclusion edge
SUPERSEDES: later task/result retires earlier authority/work
INVALIDATES: finding/result makes earlier premise unusable
```

Mirroring rules:

- `BLOCKED_BY` should be mirrored to GitHub native issue dependencies where one task issue blocks another. GH-DEPS currently exposes list/add/remove APIs.
- Parent/child decomposition may mirror to GitHub sub-issues (GH-SUBISSUES), but hierarchy is not equivalent to a blocking edge.
- Rich semantic edges remain canonical graph data; do not overload GitHub labels to encode them.
- A reconciliation job compares canonical hard edges against GitHub native mirrors and reports drift.
- Mirror failure is a control-plane defect; canonical graph remains source authority.

### 9.3 Task state model

Derived states:

```text
BLOCKED
READY
ORPHANED_BRANCH
STALE_OWNER
ACTIVE
```

Recorded result states are those declared by the canonical task class (for example HANDOFF_READY, REVIEW_READY, VERIFICATION_READY, DONE, SUPERSEDED, INVALIDATED).

`ACTIVE` requires a current valid ownership generation **and** a valid ownership fence at the task branch head/control transaction.

A UI label/project status may mirror these values but cannot create them.

### 9.4 New-task claim transaction

Baseline current behavior—deterministic branch creation—already provides useful exclusion for first claim. Mature proposal:

1. dispatcher obtains one fresh state snapshot;
2. verifies task READY, branch absent, all hard dependencies/current canonical binding valid, WIP governor permits admission, conflict keys free;
3. constructs an immutable **ownership fence commit** with the task base tree and trailers/metadata referencing task/actor/generation/observed base;
4. atomically creates the deterministic task branch and all required deterministic lock refs using GraphQL `updateRefs`, each with `beforeOid=ZERO` and `afterOid=<fence-commit>`;
5. only after the atomic ref transaction succeeds, append the schema-valid CLAIM audit/status event referencing the fence commit/ref generation;
6. reconciliation verifies event ↔ refs and repairs/classifies a crash between steps 4–5 as `CLAIM_EVENT_MISSING`, not a free task.

If step 4 fails, the claimant owns nothing and re-derives state.

**Important:** exact lock-ref namespace, permission/ruleset interaction, empty/same-tree control commit construction, and transaction limits require FAC2-E1 empirical validation before this replaces current schema-3 mechanics.

### 9.5 Resume/recovery transaction

Handoff/stale/orphan recovery requires stronger fencing than a winning comment:

1. derive valid source state and winning resume/recovery intent by canonical rules;
2. fetch current task branch and lock-ref OIDs;
3. construct a new ownership fence commit whose parent is the observed task head and tree is unchanged unless the same transaction includes a justified checkpoint change;
4. atomically CAS task branch `beforeOid=observed_head → afterOid=fence_commit` and transfer/recreate required lock refs with expected prior OIDs;
5. publish RESUME/RECOVER audit event bound to the new fence commit/generation;
6. every later task-branch mutation requires expected parent at or after this fence generation.

A stale owner whose local commit still uses the pre-recovery head will fail branch CAS/non-fast-forward and cannot publish a valid terminal result because status validation requires the current ownership generation/head.

### 9.6 Conflict-lock model

Each task contract declares deterministic `conflict_keys`, not arbitrary prose locks. Examples may include:

```text
path:docs/planning/canonical/
module:runtime/save-schema
resource:protected-verifier-rules
integration:main
```

Scheduler computes incompatibility from active lock keys and contract rules.

Proposed lock ref identity:

```text
<tested internal branch/ref namespace>/<sha256(normalized conflict key)>
```

The exact namespace is deliberately **not** fixed by this proposal until FAC2-E1 proves what GitHub supports cleanly with rulesets, branch discovery, and garbage collection.

Multi-key acquisition must be all-or-none using one atomic transaction; otherwise tasks can deadlock by partially acquiring locks.

Lock order is still normalized for diagnostics, but atomic acquisition should remove classic sequential multi-lock deadlock.

### 9.7 Lease semantics

GitHub refs do not themselves provide a documented expiring lease primitive. Therefore separate:

- **ownership fence** — mechanical write authority, represented by CAS-ref generation;
- **lease freshness** — time-based recovery eligibility, represented by trusted control-plane event/server-time evidence;
- **audit event** — issue comment/status capsule linking generation, actor, lease/evidence.

Recommended control-plane App behavior:

- App records lease start/renewal using trusted service time plus GitHub event timestamps where available;
- substantive branch-head advance or explicit evidence checkpoint may renew within policy;
- after expiry, task becomes `STALE_OWNER` but old owner is not fenced until recovery CAS succeeds;
- recovery CAS creates the new generation; stale writer then loses expected-head authority;
- crash after ref CAS but before event publication is reconciled as a special incomplete transaction state, never silently freed.

The exact durable lease timestamp store is an open implementation choice: signed App-produced event, repository control object, or small transactional service. It must be reconstructable/auditable and benchmarked; do not use client-supplied body timestamps as sole authority.

### 9.8 READY algorithm

For task `T`, `READY(T)` iff all are true at one reconciled state version:

```text
canonical_binding(T.activation) valid
AND T not terminal/superseded/invalidated
AND every BLOCKED_BY/result predicate satisfied by exact valid upstream state
AND task branch absent OR branch is in a canonical claimable/recoverable state appropriate to selection class
AND no current valid mutation owner
AND all conflict_keys available
AND role/independence constraints are satisfiable (including explicit DEGRADED mode only where canonical policy permits)
AND wave/role/domain/global WIP admission permits new ownership
AND no higher-priority canonical recovery condition preempts normal work
```

For ordinary **new** work, branch should be absent before claim. Handoff/stale/orphan work belongs to recovery/resume selection classes, not ordinary READY.

The dispatcher should return not just `READY=true`, but a `ready_proof` containing:

- state version/snapshot ref;
- canonical graph/contract ref;
- satisfied prerequisite result refs;
- observed branch/lock refs;
- WIP counters/policy version;
- priority tuple;
- conflict keys;
- intended claim transaction preconditions.

The proof expires when any referenced state changes.

### 9.9 Cycle and invalid-dependency validation

Before wave activation and after graph mutation:

- hard `BLOCKED_BY` graph must be acyclic;
- review/synthesis/verification/canonicalization routes must terminate or declare bounded remediation;
- every target mission exists exactly once;
- terminal predicates reference supported result kinds;
- no task's required outputs collide with an incompatible sibling without an explicit sequencing/conflict edge;
- superseded/invalidated nodes cannot remain hard prerequisites without a replacement route;
- native GitHub dependency mirror should match canonical hard edges.

Runtime liveness detects cycle/orphaned prerequisite/missing transition/mirror corruption and routes to recovery rather than inventing a task.

## 10. Scheduler and WIP policy

### 10.1 Deterministic selection classes

Baseline scheduler class order:

1. `CANONICAL_RECOVERY` — broken/invalid current main/binding or unsafe integration state;
2. `OWNERSHIP_RECOVERY` — HANDOFF, orphan, stale-owner continuation/recovery;
3. `QUALITY_PIPELINE` — review, requested revision/synthesis, verification, integration;
4. `PRODUCTION_READY` — new proposal/research/implementation work allowed by current phase;
5. `PLANNING_REPLENISHMENT` — only when canonical planning/checkpoint logic says frontier needs expansion.

Within a class:

```text
(priority_rank, scheduler_policy_secondary_keys..., issue_number)
```

Version 1 secondary key should be empty or only deterministic explicit contract data. “Unblock value” may later be added only after benchmark evidence defines it reproducibly and Goodhart risk is reviewed.

### 10.2 WIP governors

Track separate counts:

- active mutation owners total;
- active owners by conflict domain/module;
- outstanding producer work awaiting review;
- review queue;
- revision queue;
- verification queue;
- integration queue;
- stale/handoff tasks;
- open discovered-work candidates versus activated issues.

Suggested policy shape, values empirical:

```yaml
wip_policy_version: 1
global_active_owner_cap: <measured>
new_production_cap: <measured>
per_conflict_domain_cap: <measured>
quality_queue_high_watermark:
  review: <measured>
  verification: <measured>
  integration: <measured>
admission_rule: stop_starting_comparable_priority_production_when_quality_queue_exceeds_high_watermark
```

Current Planning Program wave caps (12 initially READY / 24 new issues) remain authoritative until superseded by verified evidence.

### 10.3 Starvation resistance

A strict priority class can starve lower work under repeated recovery noise. Measure age and repeated-preemption counts. A later scheduler may add bounded aging inside a class, but **must not** age ordinary production above broken-canonical or required verification/integration safety work.

Scheduler changes are judge-affecting factory changes: version, benchmark, independently review, and rollback.

## 11. PR, checks, and integration lifecycle

### 11.1 Main protection target

Subject to repository/account feature availability and FAC2-E4 validation, configure `main` so normal agents cannot bypass:

- pull request required;
- required status/checks for the relevant task class;
- required checks tied to expected GitHub App sources where trust policy needs it;
- conversation/review requirements as W1-FAC-03 defines;
- linear history;
- force push disabled;
- branch deletion/direct push restricted;
- bypass minimized/disabled for normal automation.

GH-RULESETS/GH-PROTECTION document these mechanisms. Exact plan/account constraints must be validated before treating configuration as enforced.

### 11.2 Squash-only enforcement

Two layers:

1. **Repository configuration:** allow squash merge, disable merge commit and rebase merge (GH-REPO-CONFIG / GH-METHODS).
2. **Integrator transaction:** re-fetch PR/base/verification, require expected PR head, call merge endpoint with `sha=<expected head>` and `merge_method=squash` (GH-MERGE).

Before merge also require current `main` equals verified base or an explicit valid verification-refresh/reverification result covers the new base.

Head-SHA protection alone does **not** protect against base movement; Everfield must keep its current-base verification invariant.

### 11.3 Merge queue

Do not enable as canonical default until spike FAC2-E6 proves:

- exactly one squash commit per accepted task/PR under chosen repository settings;
- verification/check results are bound to the exact queued synthetic/base state needed by the trust model;
- the queue does not bypass expected-head/current-base invariants;
- terminal integration provenance can identify the resulting main SHA deterministically.

If it cannot preserve these invariants, use a serialized integration agent/lock instead.

## 12. Automation and permission architecture

### 12.1 Control-plane GitHub App

Recommended future App roles, exact permissions to be minimized after endpoint inventory:

**Scheduler/control-plane App**
- Issues: read/write for status/mirror/reconciliation;
- Contents: write only if required for branch/ref CAS and control commits;
- Pull requests: read/write for PR lifecycle operations;
- Metadata: read;
- required webhook events for issues, comments, PRs, refs/pushes/check state.

Do **not** grant Administration or workflow modification merely for convenience. If ruleset provisioning requires higher privilege, use a separate provisioning path/role rather than keeping high privilege in the routine scheduler.

GH-APP-PERMS recommends selecting minimum required permissions and documents granular App permissions.

**Verifier/check App** should be permission-separated where W1-FAC-03 requires protected evidence: ideally able to publish required checks/statuses without write access to candidate source surfaces it judges.

Exact check/status permission design belongs to W1-FAC-03/FAC-04.

### 12.2 Reconciliation loop

Correctness pattern:

```text
webhook / timer / agent request
 -> fetch fresh canonical graph + GitHub authoritative state
 -> validate event/comment/ref history
 -> derive task states and READY frontier
 -> compare with derived caches/Projects/native dependency mirrors
 -> repair safe mirrors or open bounded control-plane defect
 -> perform one CAS-protected mutation
 -> re-fetch and verify result
 -> append audit/evidence
```

Webhook delivery is a wake-up signal. Duplicates, reordering, or missed delivery must not make the authoritative state unrecoverable because reconciliation re-reads durable GitHub/repository state.

### 12.3 Projects role

Projects/custom fields are recommended for:

- human/agent queue views;
- READY/ACTIVE/REVIEW/VERIFY derived status;
- priority/domain/age/WIP visualization;
- dashboards and archival views.

GH-PROJECTS documents built-in status/auto-add/archive workflows and API automation. Treat these as **derived projections** because project workflow updates are not the canonical ownership/dependency transaction.

## 13. Garbage collection and retirement

Garbage collection is correctness-sensitive, not cosmetic.

### Task/issue retirement

- close terminal producer/review tasks once authoritative result status exists;
- mark superseded/invalidated tasks with exact replacement/authorizing refs before closing;
- preserve PR/issue/status provenance;
- remove native dependency mirrors that no longer correspond to active canonical graph edges;
- archive Project items as derived UI housekeeping.

### Branch/ref cleanup

- never delete an active task/lock ref;
- after accepted squash integration and terminal status, task branch may be deleted only when all required work/evidence SHAs remain reachable through PR/GitHub objects or other retained refs according to evidence-retention policy;
- stale orphan lock refs require reconciliation with ownership/event state before release;
- control-plane lock/ref GC must use CAS against the expected generation so it cannot delete a newly reacquired lock;
- keep audit counters for orphaned locks and failed GC attempts.

### Evidence retention

FAC-04 defines retention topology. Control-plane GC may not delete protected verification/evidence solely to reduce clutter.

## 14. Observability and evaluation

Diagnostic vector:

- duplicate claim attempts prevented;
- CAS conflicts by operation type;
- claim/recover transaction latency;
- crash-between-ref-and-event reconciliation incidents;
- orphan lock count/age;
- stale-writer mutation failures;
- dependency mirror drift count/repair latency;
- cycle/invalid-edge detections;
- READY derivation disagreement across independent scheduler runs;
- READY frontier width and eligible-but-WIP-blocked count;
- active WIP by class/domain;
- review/verification/integration queue age;
- production started while quality queue above high-watermark;
- scheduler starvation/preemption count;
- branch conflict/non-fast-forward failures;
- PR expected-head failures;
- pre-merge base-drift invalidations;
- non-squash merge attempts/preventions;
- required-check source violations;
- webhook replay/reconciliation lag;
- task/lock ref GC failures;
- stale Projects/cache mismatch rate.

No single “throughput score” should drive the scheduler. Version scheduler policy and compare verified throughput, escapes, WIP, recovery, and frontier health together.

## 15. Bounded experiments / implementation spikes

| ID | Experiment | Evidence required | Pass signal |
|---|---|---|---|
| FAC2-E1 | GraphQL `updateRefs` atomic claim + 2 conflict-lock refs on a disposable test issue/refs | request/response, before/after refs, losing concurrent request | exactly one transaction wins; no partial lock acquisition; namespace/rulesets workable |
| FAC2-E2 | Crash matrix at claim/recover steps (before CAS, after CAS before event, after event before handoff) | resulting refs/comments/task state and reconciliation report | every crash maps to deterministic recoverable state; never two valid writers |
| FAC2-E3 | Native dependency mirror audit | canonical graph vs GH-DEPS list/add/remove behavior | drift is detected/repaired; canonical graph still deterministic if mirror temporarily fails |
| FAC2-E4 | Ruleset/branch protection + required check from expected App | attempted direct push/force push/untrusted check/merge | unauthorized paths blocked, required trusted check enforced |
| FAC2-E5 | Expected-head + current-base squash integration race | concurrent base movement/head movement traces | head mismatch and base drift both prevent stale integration; successful result one squash commit |
| FAC2-E6 | Merge queue compatibility | queued PR history/check/base/provenance trace | one squash commit per task and exact verification/base invariants retained, else reject queue |
| FAC2-E7 | Webhook loss/duplicate/reorder replay | withheld/replayed events then full reconciliation | final derived state equals clean run |
| FAC2-E8 | Scheduler/WIP benchmark with synthetic graph and quality backlog | deterministic choices, verified throughput, queue age, frontier width | same snapshot yields same choice; quality queues bounded without starving production |
| FAC2-E9 | Lock/branch garbage collection race | GC vs concurrent reacquire CAS trace | GC cannot remove new generation; evidence remains reachable |

## 16. Failure modes and defenses

### Advisory claim race
**Failure:** two agents read “unassigned” and both start.  
**Defense:** branch/ref CAS transaction; assignee/label only mirrors state.

### Partial conflict-lock acquisition
**Failure:** task owns one of several resources and deadlocks another claimant.  
**Defense:** atomic multi-ref transaction or reject ref-lock design if spike cannot guarantee it.

### Lease race
**Failure:** progress renewal and stale recovery both appear valid.  
**Defense:** recovery creates new CAS fence generation; terminal/mutation validity bound to current generation; trusted lease evidence reconciled.

### Crash after lock before comment
**Failure:** branch/locks exist but issue says READY.  
**Defense:** refs outrank derived cache; reconciliation classifies missing event and recovers, never grants second normal claim.

### Editable issue contract drift
**Failure:** issue body silently changes task semantics.  
**Defense:** canonical `contract_ref`/activation is authority; body is projection and drift is detectable.

### Native dependency drift
**Failure:** GitHub `blocked by` differs from canonical graph.  
**Defense:** canonical graph wins; mirror audit/repair; scheduler uses canonical edge + exact result predicates.

### Dependency cycle / dead graph
**Failure:** no READY work due cycle/missing transition.  
**Defense:** activation-time DAG validation + runtime liveness/recovery classification.

### Scheduler activity bias
**Failure:** starts many tasks while reviews/integration age.  
**Defense:** class priority + WIP quality high-watermarks + verified-throughput diagnostics.

### Starvation
**Failure:** recurring recovery permanently prevents useful lower work.  
**Defense:** measure/prevent pathological repeated incidents; aging only inside safe classes; root-cause recovery work.

### Status spoofing
**Failure:** writer posts a successful check/status itself.  
**Defense:** required check tied to expected App source where available; permission split; schema-valid evidence provenance.

### Expected-head but stale-base merge
**Failure:** PR head unchanged while `main` moves after verification.  
**Defense:** explicit verified-base equality/refresh rule in addition to GitHub merge head guard.

### Merge queue history violation
**Failure:** queue produces history inconsistent with squash directive.  
**Defense:** no queue adoption until FAC2-E6 passes; repository merge-method restrictions and post-merge validation.

### App compromise / over-permission
**Failure:** routine scheduler can change rules/verifiers or bypass quality gates.  
**Defense:** least privilege, separate provisioning/verifier identities, ruleset bypass minimization, audit.

### Webhook dependence
**Failure:** missed event strands task.  
**Defense:** reconciliation re-derives from durable state; events only wake it.

### GC destroys provenance
**Failure:** branch/evidence removed before durable references exist.  
**Defense:** reachability/evidence-retention check + CAS generation check before GC.

## 17. Risks

- Ref-lock branches may create operational clutter or interact poorly with branch rules/search; FAC2-E1 decides whether the design is viable.
- A GitHub App becomes critical infrastructure; deploy it with reconciliation, observability, least privilege, and recoverable derived cache rather than opaque local state.
- Native issue dependencies can improve UX but may encourage operators to edit the mirror directly; reconciliation must detect manual drift.
- WIP policy can reduce parallelism if thresholds are guessed; benchmark before changing current wave governors.
- Strict required checks can deadlock if the check-producing App is unavailable; recovery policy must distinguish service outage from passing evidence, without bypassing the check silently.
- A merge queue could improve throughput but only if its synthetic merge state/provenance fits verification semantics.
- Control-plane complexity itself can become a factory bottleneck; maintain a minimal deterministic baseline and justify optimizations with evidence.

## 18. Open questions

1. Does GitHub permit a clean non-user-facing ref namespace for lock refs through the required APIs, or should lock refs be dedicated branch names?
2. What is the practical limit/performance/ruleset interaction of one atomic `updateRefs` mutation with many conflict locks?
3. Where should authoritative lease timestamps live so they are auditable, durable, and not forgeable by a task worker?
4. What exact GitHub App permission split best separates scheduler, verifier/check producer, and high-privilege repository provisioning?
5. Can required check source pinning plus branch/rulesets prevent all intended bypasses on this repository/account plan?
6. Does merge queue preserve one squash commit per Everfield task and current-base verification semantics?
7. What WIP cap/high-watermark policy maximizes verified throughput for 10–20+ agents without starving proposal work?
8. When should richer semantic dependencies be materialized as native GitHub dependencies versus remain graph-only?
9. How should task contract manifests be partitioned to avoid central-file merge conflicts during future wave generation?
10. What control-plane state requires long-term retention after task branch deletion?

## 19. Reopen conditions

Reopen this proposal or later canonical descendants if:

- FAC2-E1 cannot produce an atomic all-or-none task+lock transaction;
- two valid mutation owners can exist after any crash/race scenario;
- authoritative state cannot be reconstructed without an opaque scheduler database;
- GitHub native dependency/project state becomes a hidden source of authority inconsistent with canonical graph data;
- stale writers can publish valid terminal results after recovery;
- READY derivation differs between compliant schedulers given the same snapshot;
- WIP governors materially collapse useful concurrency without reducing quality-queue debt;
- branch/ruleset configuration cannot enforce the required integration restrictions;
- merge queue violates squash/current-base/provenance invariants;
- required-check source protection can be spoofed or bypassed;
- control-plane App permissions must be broader than its role can safely justify;
- reconciliation cannot recover from event loss/reordering;
- garbage collection removes evidence needed for canonical provenance;
- a later GitHub API/feature change invalidates current capability assumptions;
- stronger evidence shows a simpler transactional substrate is safer than the proposed ref-lock scheme.

## 20. Required independent critique

`W1-REV-FAC` should attack claim/recovery races, WIP/scheduler Goodhart paths, backlog/GC behavior, authority drift, hidden human gates, and factory liveness.

`W1-REV-TECH` should independently attack the GitHub/API transaction assumptions, ref-lock feasibility, ruleset/permission model, status-check trust, merge/current-base races, webhook/reconciliation correctness, and evidence/provenance retention.

Neither reviewer should treat official feature availability as proof that the proposed composition is safe without the named spikes.

## 21. Downstream work unblocked

This proposal supplies required inputs to both `W1-REV-FAC` and `W1-REV-TECH`. It also defines interfaces for W1-FAC-01, W1-FAC-03, W1-FAC-04, and later factory/technical synthesis.

It does not install automation, create extra current-wave work, or become canonical by authorship. Any adopted control-plane implementation must follow the Wave 1 review/synthesis/verification/canonicalization route and preserve squash-only `main` integration.