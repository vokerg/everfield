# Planning Program v1 — Remediated Reviewed Candidate

**State:** REVIEWED-CANDIDATE-REMEDIATED  
**Bootstrap remediation issue:** #11  
**Authority:** Candidate operating model only. It is NON-CANONICAL until a fresh independent Bootstrap Issue #5 verifier records PASS for this exact remediation work state and Bootstrap Issue #6 performs the verified mechanical promotion.  
**Scope:** Planning work only. This document does not authorize gameplay implementation, mass implementation issue generation, or a final engine choice.

## 1. Status

This document is the complete post-Issue-5 remediation candidate for Planning Program v1. It preserves the accepted Issue #4 operating model while correcting the two BLOCKER findings from the first Issue #5 verification attempt:

- **V5-B01:** canonical promotion left bootstrap-next-step instructions active in the future canonical program;
- **V5-B02:** operational capsule validity still depended on an incomplete per-kind schema/transition interpreter.

Exact dispositions are recorded in `docs/planning/reviews/issue-5-finding-dispositions.md`.

The normative machine-readable promotion, capsule registry, transition predicates, verification binding, and immutable Wave 1 contract adoption are in:

`docs/planning/09-planning-program-v1-canonicalization-manifest.yaml`

The Issue #4 candidate and manifest remain immutable provenance and are `SUPERSEDED_FOR_VERIFICATION`, not CANONICAL.

## 2. Scope

Planning Program v1 governs autonomous planning after bootstrap canonicalization through the first bounded detailed-planning wave. It defines:

- cold-start task discovery and deterministic eligibility;
- task claiming, continuation, stale/orphan recovery, and write fencing;
- branch/session/handoff semantics;
- a complete versioned operational-comment schema and state-transition validator;
- evidence and context-budget rules;
- independent review, synthesis, verification, and canonicalization;
- a bounded first-wave mission DAG;
- liveness recovery and planning garbage collection;
- bounded next-wave generation;
- implementation-readiness barriers.

## 3. Inputs

### 3.1 Immutable provenance inputs

This remediation consumes:

- Issue #4 candidate work SHA `1d7b9a980e74d6999789c86694f3c7fb99e13b99`;
- Issue #4 final branch head `a47c88151b92c45235d92b6b6bdf5d74ef4f49b6`;
- Issue #4 candidate blob `1170d97490c2a4ccbf1b9f51191ce97123536439`;
- Issue #4 canonicalization manifest blob `d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd`;
- Issue #5 FAIL report at work commit `26a06f9ab78ede2c69107e3df3d2327e2aed18f0`;
- current bootstrap base `main@c59ad1ef4b9eb1cd42b2349d0f5c7ee7860bddc9`.

No prior conversation history is project authority.

### 3.2 Evidence versus recommendation

Observed repository/GitHub constraints outrank this candidate:

- repository + GitHub state must be enough for cold start and continuation;
- no routine human approval state exists;
- review/verification must acquire independent evidence;
- context is budgeted;
- work is resumable;
- canonicality is explicit;
- every accepted integration into `main` is squash-only.

GitHub comment IDs plus server `created_at`/`updated_at` are authoritative for ordering/edit detection. Body timestamps are descriptive only.

## 4. Goals

A fresh agent must be able to determine without hidden context:

1. current phase and entry path;
2. highest-priority eligible work;
3. whether work is new, actively owned, handed off, stale, orphaned, review-ready, verification-ready, terminal, or invalidated;
4. whether every operational comment is valid or invalid under one exact schema;
5. how to claim/resume/recover without authorizing two compliant writers;
6. exact branch/base and immutable inputs;
7. exact output/schema/context packet;
8. required evidence and review route;
9. stopping/handoff behavior;
10. no-READY behavior;
11. canonicalization bound to exact candidate, manifest, Wave 1 contract source, and verified main state;
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
- use labels as dispatcher truth;
- treat a self-selected UUID as proof of independence;
- treat branch count as proof of useful parallelism.

## 6. Constraints

1. `main` is the stable canonical base.
2. Normal task branches are deterministic: `planning/issue-N`.
3. One normal task has at most one authorized ownership generation.
4. Branch mutations are expected-parent/fast-forward only; force-push is forbidden.
5. Upstream non-main artifacts are consumed by immutable SHA.
6. `BLOCKED` and `READY` are derived, not manually flipped gates.
7. Operational comments are schema-versioned and append-only for authority; edited authority comments are invalid.
8. Lease age derives from GitHub server metadata.
9. Canonicality is never inferred from merge, PR, issue closure, or file path alone.
10. Every `main` integration is squash-only.
11. Wave 1 issues are instantiated only after Bootstrap Issue #6 squash integration and concrete resulting main SHA are known.
12. High-throughput implementation remains blocked until a later independently verified readiness decision.

## 7. Assumptions

These remain explicit, reversible assumptions:

- procedural GitHub ownership plus expected-parent branch writes are sufficient for the temporary planning phase when all agents apply the fence;
- six hours is a provisional lease TTL;
- maximum 12 initially READY and maximum 24 newly instantiated issues per later wave are provisional governors;
- Review Indexes plus targeted retrieval can preserve review depth;
- procedural cold-start separation is the minimum independence boundary until stronger platform/credential controls exist.

## 8. Alternatives considered

- unfenced comment leases: rejected;
- pre-merge Wave 1 creation: rejected;
- discretionary canonicalization rewrite: rejected;
- permanent reusable recovery branch: rejected;
- unbounded next-wave instantiation: rejected;
- partial capsule schemas with prose-only kinds: rejected by V5-B02;
- a canonical program containing active bootstrap-next-step instructions: rejected by V5-B01.

## 9. Canonical cold-start entry

When this document's header state is `CANONICAL` and `docs/planning/START-HERE.md` points here, a fresh planning agent MUST:

1. read `/AGENTS.md`;
2. read `docs/planning/START-HERE.md`;
3. read `docs/planning/PLANNING-PROGRAM-v1.md` from current `main`;
4. query open `[PLAN-v1]` issues;
5. validate issue contracts and operational comments under Sections 10–12 and the exact schema-2 registry in the canonicalization manifest;
6. derive eligibility from prerequisites, branch state, ownership generation, lease validity, and terminal state;
7. prefer queue classes: recoverable/handoff work → review/revision/verification/integration → new proposal/research;
8. within a class choose lower `priority_rank`, then lower GitHub issue number;
9. re-read the selected issue immediately before claim/resume/recovery;
10. load only its bounded packet under Section 15;
11. use Sections 11–13 for ownership and mutation fencing;
12. before stopping commit useful state and leave structured handoff/status.

If this document is not CANONICAL, it is verification input only and MUST NOT activate Wave 1.

## 10. Operational state model

### 10.1 Derived states

- `BLOCKED` — at least one hard prerequisite is unsatisfied.
- `READY` — all prerequisites are satisfied, no terminal result exists, and no valid active ownership generation exists.
- `ORPHANED_BRANCH` — deterministic branch exists, no valid ownership grant exists, and a valid orphan probe has matured for at least ten GitHub-server minutes.
- `STALE_OWNER` — latest valid ownership/renewal lease expired and no later valid handoff/completion/terminal result exists.

### 10.2 Recorded task-result states

The schema-2 registry uses these recorded states only:

- `HANDOFF_READY`;
- `REVIEW_READY`;
- `VERIFICATION_READY`;
- `DONE`;
- `SUPERSEDED`;
- `INVALIDATED`.

`IN_PROGRESS` is derived from a current valid ownership grant plus unexpired lease rather than from a free-standing status comment.

Review disposition and verification result are separate typed fields on dedicated capsule kinds; they are not overloaded state names.

## 11. Normative operational capsule protocol — schema 2

### 11.1 Authority source

The normative machine-readable registry is `operational_capsules` in `docs/planning/09-planning-program-v1-canonicalization-manifest.yaml`. This section is a human-readable mirror. If prose and registry differ, verification MUST fail; Issue #6 may not choose one interpretation.

Every authority-bearing operational comment MUST use:

```yaml
protocol: planning-v1
schema: 2
kind: <registered kind>
issue: <GitHub issue number>
mission_id: <stable mission id>
branch: planning/issue-N
actor_session_id: <episode identifier>
```

GitHub comment ID, `created_at`, and `updated_at` are server metadata and MUST NOT be self-declared as authority fields.

Unknown `kind`, missing required field, unknown top-level authority field, edited comment, wrong issue/mission/branch, invalid SHA/reference, losing tie-break, or illegal predecessor transition makes the comment invalid for authority. Optional non-authoritative metadata is allowed only inside the `extensions` mapping.

### 11.2 Registered kinds

Schema 2 defines exactly these operational kinds:

1. `CLAIM`
2. `ORPHAN_PROBE`
3. `RESUME_INTENT`
4. `RESUME`
5. `RECOVER`
6. `PROGRESS`
7. `STATUS`
8. `REVIEW_STATUS`
9. `VERIFICATION_STATUS`
10. `INTEGRATION_STATUS`

No other comment kind changes operational state under schema 2.

### 11.3 Ownership grants

`CLAIM`, `RESUME`, and `RECOVER` are ownership grants. The ownership generation is the GitHub comment ID of the current winning valid ownership grant.

A grant is valid only when its exact source/tie predicate in the manifest is satisfied. A later arbitrary grant does not supersede a winner merely because its comment ID is larger.

Lease start is the server creation time of the winning ownership grant or a valid `PROGRESS` renewal. Default TTL is six hours.

### 11.4 Tie-break semantics

For intentional handoff, stale recovery, and mature-orphan recovery, contenders first post `RESUME_INTENT` against one exact source comment and observed branch head.

The winner is the lowest GitHub comment ID among valid intents with the same source reference and observed head. Only that winning intent can authorize the subsequent `RESUME`/`RECOVER`. A later intent remains evidence but has no authority effect.

Only the first valid ownership grant referencing the winning intent is valid. Duplicate later grants are ignored for authority.

## 12. Exact capsule kinds and transitions

The manifest is normative for every required field. The operational effects are:

### `CLAIM`

Allowed only from derived `READY` with no task branch before the claimant atomically creates `planning/issue-N`. It must reference the exact created head and claim base. The earliest valid claim for that created branch/head wins.

### `ORPHAN_PROBE`

Non-owning. Allowed only when the deterministic branch exists and no valid ownership grant exists. It records the exact observed head and the latest issue-comment ID inspected. A mature probe can become the source of `RESUME_INTENT(reason=ORPHAN)` only if no valid ownership grant appeared later.

### `RESUME_INTENT`

Non-owning. `reason` is exactly `HANDOFF | STALE | ORPHAN`. It references the exact source status/ownership/probe comment and observed branch head. Earliest valid intent for that source/head wins.

### `RESUME`

Ownership grant. Allowed only for `reason=HANDOFF`, only from a valid `HANDOFF_READY` source, only by the actor/session of the winning intent, and only if observed head still matches.

### `RECOVER`

Ownership grant. Allowed only for `reason=STALE | ORPHAN`, only by the winning intent actor/session, and only while the referenced stale/orphan condition remains true and head still matches.

### `PROGRESS`

Lease renewal only; not a new ownership generation. It must reference the current ownership generation and be posted before expiry. It is valid only with either a new remote head containing substantive committed progress or an immutable bounded experiment/check result. No more than three consecutive evidence-only renewals without head advance extend the lease.

### `STATUS`

Result/status from the current owner generation. `state` is exactly one of `HANDOFF_READY | REVIEW_READY | VERIFICATION_READY | DONE | SUPERSEDED | INVALIDATED` and must satisfy the task-class transition predicate in the manifest.

### `REVIEW_STATUS`

Completes an independent review task. `disposition` is exactly `PASS_FOR_SYNTHESIS | CHANGES_REQUIRED | INVALIDATED`. `PASS_FOR_SYNTHESIS` and `CHANGES_REQUIRED` may unlock the declared synthesis/revision task; `INVALIDATED` unlocks only declared recovery/replanning.

### `VERIFICATION_STATUS`

Completes an independent verification task with `result: PASS | FAIL`. PASS must bind exact candidate work SHA, exact manifest identity, exact adopted Wave 1 contract blob, and exact `verified_base_main_sha`. PASS is invalid while any BLOCKER/MAJOR remains unresolved.

### `INTEGRATION_STATUS`

Posted only after a controlled squash integration. It records expected pre-merge branch head, verified candidate/base tuple, resulting `main_sha`, merge method, canonicality/result, and prior verification status. `merge_method` must be `squash`.

## 13. Claim, resume, recovery, and mutation fence

### 13.1 New work

1. re-read issue/prerequisites/branch/capsules;
2. resolve current `main` SHA;
3. create exactly `planning/issue-N` from that SHA;
4. immediately post schema-2 `CLAIM`;
5. re-fetch comment/head state and verify the claim is the winning valid grant;
6. before first edit perform the mutation fence.

### 13.2 Orphan recovery

If branch exists without valid ownership:

1. do not edit or create an alternate branch;
2. post or observe a schema-2 `ORPHAN_PROBE`;
3. after ten server minutes, if condition remains true, contenders post `RESUME_INTENT(reason=ORPHAN)`;
4. the winning intent may post one valid `RECOVER`.

### 13.3 Intentional handoff

A valid `STATUS(state=HANDOFF_READY)` with exact `work_sha`, `head_sha`, and handoff path is resumable. Contenders post `RESUME_INTENT(reason=HANDOFF)`; winner posts `RESUME`.

### 13.4 Stale recovery

After lease expiry, contenders post `RESUME_INTENT(reason=STALE)` referencing the exact expired ownership generation/head. Winner posts `RECOVER` if the stale condition still holds.

### 13.5 Mandatory mutation fence

Immediately before every task-branch repository mutation, the actor MUST:

1. fetch latest schema-valid operational comments;
2. confirm its ownership generation is still the current valid grant and its lease is unexpired;
3. fetch remote branch head;
4. confirm head equals the exact parent on which the proposed commit is based;
5. create a commit with that parent and move the branch only by non-force fast-forward;
6. abort on generation/head/ref mismatch and re-enter resume/recovery logic.

## 14. Mission-class completion rules

- Root/producer proposals complete with `STATUS(state=REVIEW_READY)` after acceptance criteria.
- Domain syntheses complete with `STATUS(state=REVIEW_READY)` after every required BLOCKER/MAJOR disposition.
- Final synthesis candidates complete with `STATUS(state=VERIFICATION_READY)` when candidate + promotion manifest are one immutable work state.
- Review tasks complete with `REVIEW_STATUS`.
- Verification tasks complete with `VERIFICATION_STATUS`.
- Canonicalization/integration completes only with post-merge `INTEGRATION_STATUS`.
- `STATUS(state=SUPERSEDED|INVALIDATED)` requires the exact supersession/remediation references defined in the manifest.

Authors cannot advance their own proposals directly to verification PASS, canonicality, or integration result.

## 15. Context-loading and evidence budget

Always-read Wave 1 context:

- `/AGENTS.md`;
- canonical `docs/planning/START-HERE.md`;
- selected issue;
- canonical `docs/planning/PLANNING-PROGRAM-v1.md` at activation SHA;
- issue-declared authoritative packet.

Everything else is forbidden-by-default unless an optional retrieval trigger is met.

Every root proposal begins with a Review Index no larger than 4,000 UTF-8 characters containing stable pointers for claims/decisions, interfaces/dependencies, assumptions/open questions, evidence, conflicts, and attack points.

Simultaneously mandatory review/synthesis context is limited to 100,000 UTF-8 characters; when an execution context limit is known and smaller than 200,000 characters, the limit is additionally capped at 50% of that known context window. If the execution context limit is unknown, the deterministic fallback is 100,000 characters. Silent truncation is forbidden; use stable-pointer retrieval or an explicitly authorized bounded split.

Artifacts distinguish observed evidence, inference, recommendation/decision, and assumption. Current external technical/legal/tool claims require authoritative sources or explicit deferral.

## 16. No-READY liveness and recovery lifecycle

When no ordinary READY task exists:

1. valid active ownership that can unblock the graph → graph live;
2. valid handoff/mature orphan/stale owner → recover it;
3. eligible review/revision/verification/integration → execute before new proposals;
4. otherwise classify a liveness defect: cycle, orphan prerequisite, invalidated dependency, missing transition, or corrupted status.

`W1-REC-01` is a single-use recovery task initially BLOCKED and conditionally READY only for case 4. It cannot waive review, verification, canonicalization, or squash integration. An accepted recovery may create exactly one blocked successor recovery issue for future incidents.

## 17. Branch, handoff, PR, and integration semantics

- New tasks branch from current `main` unless the issue names an immutable alternative.
- WIP commits preserve reconstructable state.
- Every repository-changing episode updates `docs/planning/handoffs/issue-N.md`.
- Handoff records substantive `work_sha`; the final operational comment records the resulting branch head.
- PR existence is visibility/provenance, not authority.
- Provenance merge does not confer CANONICAL state.
- All `main` integration is squash-only.
- Canonical integration checks expected candidate head and verified-base/current-main compatibility.

## 18. Artifact schemas

### Proposal/research

Status; Review Index; Scope; Inputs; Goals; Non-goals; Constraints; Assumptions; Evidence; Alternatives; Proposed design; Interfaces/dependencies; Observability/evaluation; Failure modes; Risks; Open questions; Reopen conditions; Required critiques; Downstream work.

### Review

Status; reviewed mission IDs/work SHAs; independent execution-context provenance; attack plan; findings; contradictions; empirical questions; disposition; required next action.

### Synthesis

Proposal schema plus exact producer/review SHAs, every BLOCKER/MAJOR disposition, interfaces, unresolved conflicts/experiments, candidate decisions/reopen conditions, downstream verification contract.

### Verification

Result PASS/FAIL; exact candidate work SHA; manifest identity; adopted Wave 1 contract blob; verified base main SHA; independent execution provenance; scenarios; contradictions; BLOCKER/MAJOR defects; evidence; required remediation.

## 19. Independent critique boundary

Required reviewer/verifier independence means a distinct cold-start execution context that:

- lacks producer private conversation/scratch context;
- starts from repository + GitHub entry state;
- records platform run identity when exposed;
- records prior mission roles excluded from the gate;
- acquires its own evidence before reconciling prior conclusions.

Self-selected session IDs are episode metadata only. If stronger platform identity is unavailable, procedural cold-start separation is recorded as a trust risk.

## 20. First-wave mission DAG

The exact Wave 1 mission contracts remain the already-reviewed machine-readable sections of Issue #4 manifest blob `d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd`, adopted immutably and narrowly by the Issue #11 manifest. The flawed Issue #4 bootstrap-canonicalization and verification sections are explicitly **not** adopted.

Adopted sections are exactly:

- `issue_compiler`;
- `universal_root_acceptance`;
- `wave_1`;
- `non_root_optional_retrieval`;
- `next_wave_candidate_schema`.

Initial graph remains exactly 23 missions:

- 12 roots;
- 3 domain reviews;
- 3 domain syntheses;
- 1 cross-domain review;
- 1 final synthesis;
- 1 verifier;
- 1 canonicalizer;
- 1 recovery task.

After Bootstrap Issue #6 squash integration, Issue #6 obtains the concrete resulting main SHA, instantiates and validates exactly those 23 contracts, posts the mission-ID→issue mapping, then posts terminal integration status. Only then do derived prerequisites make the 12 roots READY.

## 21. Safe concurrency boundaries

Root missions own unique output paths. Filesystem ownership, semantic conflicts, hard prerequisites, and review dependencies are explicit. Siblings that need the same canonical file emit unique proposals and converge through synthesis rather than concurrent canonical edits.

Useful parallelism is independently progressing conflict-free work, not branch count.

## 22. Canonicalization and verified promotion

### 22.1 Verification binding

A valid fresh Issue #5 PASS must bind:

- exact Issue #11 candidate work SHA;
- exact Issue #11 canonicalization manifest blob/work SHA;
- adopted Issue #4 Wave 1 contract source blob `d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd`;
- exact `verified_base_main_sha`;
- exact simulated generated issue graph.

### 22.2 Mechanical promotion

Issue #6 may only apply the literal header replacements enumerated in the verified Issue #11 manifest and otherwise preserve candidate bytes. This candidate is deliberately written so its body is valid in both pre-canonical verification form and post-canonical operational form.

Immediately before merge:

- PR head equals expected materialized head;
- current `main == verified_base_main_sha`, otherwise independent compatibility/reverification is mandatory;
- no unresolved verification BLOCKER/MAJOR exists;
- canonical file and entry-document changes match the verified manifest exactly.

Every merge to `main` is squash-only.

### 22.3 Post-merge activation

Only after the squash main SHA exists may Issue #6 instantiate Wave 1 contracts, validate them, and publish terminal integration status. The concrete activation main SHA is written into every Wave 1 issue.

## 23. Backlog retirement and next-wave governor

At each final checkpoint:

- obsolete work becomes SUPERSEDED/INVALIDATED or is closed with provenance;
- invalid dependency edges are removed from the active manifest;
- duplicate candidates merge/defer;
- unselected candidates remain data, not active issues.

Later-wave canonicalization may instantiate at most 24 new issues and at most 12 initially READY issues per activation. Compiler checks unique IDs, acyclic hard dependencies, ownership conflicts, review routes, output collisions, and activation prerequisites.

## 24. Observability and evaluation

Track:

- cold-start success/failure;
- invalid capsule count/reasons by kind;
- duplicate claim attempts;
- orphan probes/recoveries;
- stale takeovers/fence aborts;
- handoff reconstruction success;
- context packet sizes/splits;
- useful READY frontier width;
- review findings/escape rate;
- liveness incidents;
- retired versus created work;
- ownership conflicts;
- self-canonicalization attempts;
- base-drift invalidations;
- non-squash integration attempts.

These are diagnostic signals, not one scalar reward.

## 25. Failure modes explicitly defended

- branch-created-before-claim abandonment;
- competing handoff/stale/orphan takeovers;
- stale writer after recovery;
- malformed/edited/partial/unknown capsule kinds;
- hidden capsule-transition interpreter;
- ambiguous review dispositions;
- independence faked by UUID;
- review fan-in overload;
- post-verification canonical rewrite drift;
- stale bootstrap instructions in canonical dispatcher;
- main changing after verification;
- pre-activation Wave 1 claims;
- recovery branch reuse after squash;
- unbounded next-wave generation;
- hidden human approval;
- provenance mistaken for canonicality;
- premature implementation.

## 26. Risks

- Procedural fencing should be replaced by stronger machine enforcement in `W1-FAC-02`.
- Procedural independence should be strengthened in `W1-FAC-03`.
- Context thresholds should be benchmarked by Wave 1 factory/evidence work.
- Wave caps should be tuned from verified throughput evidence.

## 27. Open questions

- Which GitHub/native automation should replace procedural fences?
- What platform identity/permissions strongly enforce review independence?
- What measured context budget predicts deep review success?
- Which evidence surfaces need protected storage/services?
- Which engine candidates deserve empirical spikes?
- Which game-system boundaries preserve sandbox depth and technical concurrency?

## 28. Reopen conditions

Reconsider v1 if:

- a fresh verifier cannot derive one deterministic next task;
- two compliant sessions remain authorized after recovery;
- any operational kind requires an invented validity rule;
- orphan recovery needs a human;
- required review packets repeatedly overflow the deterministic budget;
- canonicalization changes verified semantics without new verification;
- base drift is accepted without compatibility/reverification;
- useful READY frontier collapses due avoidable serialization;
- recovery incidents recur without root-cause work;
- wave caps starve useful work or fail to limit WIP;
- a later explicit human directive supersedes a binding constraint.

## 29. Bootstrap provenance invariant

The bootstrap authority chain is provenance, not a post-canonical work queue:

`#2 proposal → #3 adversarial review → #4 reviewed candidate → #5 FAIL → #11 remediation → fresh #5 re-verification → #6 canonicalization`

Before this file is CANONICAL, the unresolved bootstrap gate is represented by repository/GitHub issue state and the verified manifest. **After this file is CANONICAL, Bootstrap Issues #2–#6 and #11 are historical provenance only and MUST NOT be selected as normal planning work.**

A canonical reader therefore never interprets this section as an instruction to repeat #5 or #6.

## 30. Canonical downstream selection invariant

- If this file's header state is not `CANONICAL`, it does not activate Wave 1.
- If this file's header state is `CANONICAL`, `docs/planning/START-HERE.md` points here, Issue #6 terminal integration status records the exact squash main SHA, and Wave 1 issues carry that activation SHA, the normal queue is the open `[PLAN-v1]` issue set.
- In canonical state, fresh agents follow Section 9 and the schema-2 registry. They do **not** re-enter the bootstrap chain.
- No transition in this document authorizes gameplay implementation or a mass implementation backlog.
