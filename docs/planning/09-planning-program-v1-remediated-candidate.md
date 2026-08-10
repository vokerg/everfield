# Planning Program v1 — Remediated Reviewed Candidate

**State:** REVIEWED-CANDIDATE-REMEDIATED  
**Bootstrap remediation issue:** #11  
**Authority:** Candidate operating model only. It is NON-CANONICAL until a fresh independent Bootstrap Issue #5 verifier records PASS for this exact remediation work state and Bootstrap Issue #6 performs the verified mechanical promotion.  
**Scope:** Planning work only. This document does not authorize gameplay implementation, mass implementation issue generation, or a final engine choice.

## 1. Status

This is the complete post-Issue-5 remediation candidate for Planning Program v1. It preserves the accepted Issue #4 model while correcting:

- **V5-B01:** canonical promotion left bootstrap-next-step instructions active in the future canonical dispatcher;
- **V5-B02:** operational comment validity still depended on an incomplete per-kind schema/transition interpreter.

Exact dispositions are in `docs/planning/reviews/issue-5-finding-dispositions.md`. The normative promotion/capsule/transition manifest is `docs/planning/09-planning-program-v1-canonicalization-manifest.yaml`.

The Issue #4 candidate and manifest remain immutable provenance and are `SUPERSEDED_FOR_VERIFICATION`, not CANONICAL.

## 2. Scope

Planning Program v1 governs autonomous planning after bootstrap canonicalization through the first bounded detailed-planning wave. It defines cold-start discovery, ownership/recovery, branch/session/handoff semantics, deterministic operational-comment validity, evidence/context budgets, independent review/synthesis/verification, canonicalization, a bounded Wave 1 DAG, liveness recovery, garbage collection, and bounded next-wave generation.

## 3. Inputs

### 3.1 Immutable provenance

- Issue #4 candidate work SHA `1d7b9a980e74d6999789c86694f3c7fb99e13b99`;
- Issue #4 final branch head `a47c88151b92c45235d92b6b6bdf5d74ef4f49b6`;
- Issue #4 candidate blob `1170d97490c2a4ccbf1b9f51191ce97123536439`;
- Issue #4 manifest blob `d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd`;
- Issue #5 FAIL report work commit `26a06f9ab78ede2c69107e3df3d2327e2aed18f0`;
- remediation base `main@c59ad1ef4b9eb1cd42b2349d0f5c7ee7860bddc9`.

No prior conversation history is project authority.

### 3.2 Evidence boundary

Repository/GitHub state outranks this candidate. GitHub comment ID plus server `created_at`/`updated_at` are authoritative for ordering/edit detection; body timestamps are descriptive only. Unstable external technical/legal/tool claims require authoritative sources or explicit deferral.

## 4. Goals

A fresh agent must be able to determine, without hidden context:

1. phase and entry path;
2. highest-priority eligible work;
3. branch ownership/recovery/terminal state;
4. validity of every operational comment under one closed schema;
5. safe claim/resume/recover behavior;
6. exact branch/base and immutable inputs;
7. exact output/schema/context packet;
8. evidence/review route;
9. stopping/handoff behavior;
10. no-READY behavior;
11. exact candidate/manifest/base binding for canonicalization;
12. bounded downstream issue creation;
13. the implementation-readiness barrier.

## 5. Non-goals

This program does not implement gameplay, choose a final engine, freeze final architecture/game design, instantiate the 50 seed missions, create a full implementation backlog, permit producer self-canonicalization, use labels as dispatcher truth, treat UUIDs as proof of independence, or treat branch count as proof of useful parallelism.

## 6. Constraints

1. `main` is the stable canonical base.
2. Normal task branches are `planning/issue-N`.
3. One task has at most one authorized ownership generation.
4. Branch writes are expected-parent/fast-forward only; force-push is forbidden.
5. Upstream non-main work is consumed by immutable SHA.
6. `BLOCKED`/`READY` are derived states.
7. Authority comments are schema-versioned and edited authority comments are invalid.
8. Lease age uses GitHub server time.
9. Canonicality is explicit and is not inferred from merge/PR/closure/path.
10. Every `main` integration is squash-only.
11. Wave 1 issues are created only after Bootstrap Issue #6 squash integration yields a concrete main SHA.
12. High-throughput implementation stays blocked until a later independently verified readiness decision.

## 7. Assumptions

Temporary assumptions, all reopenable:

- procedural ownership plus expected-parent writes are sufficient for planning bootstrap;
- six hours is the provisional lease TTL;
- 12 initially READY and 24 newly instantiated issues are provisional wave governors;
- Review Indexes plus targeted retrieval can preserve review depth;
- procedural cold-start separation is the minimum independence boundary until stronger identity/permission controls exist.

## 8. Alternatives rejected

Unfenced leases, pre-merge Wave 1 creation, discretionary canonical rewrite, permanent reusable recovery branches, unbounded issue creation, prose-only capsule kinds, and a canonical dispatcher containing active bootstrap-next-step commands are rejected.

## 9. Canonical cold-start entry

When this document's header state is `CANONICAL`, `docs/planning/START-HERE.md` points here, **and Bootstrap Issue #6 has a valid terminal schema-2 `INTEGRATION_STATUS` for this exact canonical main SHA**, a fresh planning agent MUST:

1. read `/AGENTS.md`;
2. read `docs/planning/START-HERE.md`;
3. read `docs/planning/PLANNING-PROGRAM-v1.md` from current `main`;
4. query open `[PLAN-v1]` issues;
5. validate issue contracts and schema-2 operational comments;
6. derive prerequisites, ownership, lease, recovery, and terminal state;
7. prefer recoverable/handoff work → review/revision/verification/integration → new proposal/research;
8. within a class choose lower `priority_rank`, then lower issue number;
9. re-read selected issue immediately before claim/resume/recovery;
10. load only its bounded context packet;
11. apply the ownership/mutation fence before every branch write;
12. leave committed handoff/status before stopping.

If this file is not CANONICAL, or the terminal Issue #6 integration status for the exact canonical main SHA is absent, normal Wave 1 selection is not active. During the post-squash/pre-terminal activation window, only Issue #6's verified post-merge activation sequence may proceed; an absent `[PLAN-v1]` queue is not a liveness defect.

## 10. State model

Derived:

- `BLOCKED`: hard prerequisite unsatisfied;
- `READY`: prerequisites satisfied, no terminal result, no active owner;
- `ORPHANED_BRANCH`: deterministic branch exists, no valid ownership grant, mature orphan probe;
- `STALE_OWNER`: latest ownership/renewal lease expired with no later handoff/completion/terminal result.

Recorded task-result states:

- `HANDOFF_READY`;
- `REVIEW_READY`;
- `VERIFICATION_READY`;
- `DONE`;
- `SUPERSEDED`;
- `INVALIDATED`.

`IN_PROGRESS` is derived from a valid current ownership grant plus an unexpired lease.

## 11. Normative operational capsule protocol — schema 2

The normative machine-readable registry is `operational_capsules` in `docs/planning/09-planning-program-v1-canonicalization-manifest.yaml`. Prose and registry disagreement is a verification failure.

Every operational comment uses:

```yaml
protocol: planning-v1
schema: 2
kind: <registered kind>
issue: <issue number>
mission_id: <stable mission id>
branch: planning/issue-N
actor_session_id: <episode id>
```

Unknown kind, missing required field, unknown top-level authority field, edited comment, wrong issue/mission/branch, invalid SHA/reference, losing tie-break, or illegal predecessor transition makes the comment invalid. Optional non-authoritative metadata is allowed only in `extensions`.

Registered kinds are exactly:

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

## 12. Ownership and transition semantics

### 12.1 Ownership grants

`CLAIM`, `RESUME`, and `RECOVER` create ownership generations. The generation is the GitHub comment ID of the current winning valid grant. A later arbitrary grant does not supersede a winner merely because its ID is larger.

Lease start is the server creation time of the winning grant or valid `PROGRESS`. Default TTL is six hours.

### 12.2 Tie-breaks

Intentional handoff, stale recovery, and mature-orphan recovery first use `RESUME_INTENT` against one exact source comment/head. The lowest GitHub comment ID among valid intents for that same source/head wins. Only the winner can authorize `RESUME`/`RECOVER`; only the first valid grant referencing that winning intent is valid.

### 12.3 Kind effects

- `CLAIM`: derived READY → owner.
- `ORPHAN_PROBE`: non-owning evidence; matures after ten server minutes if no later owner appears.
- `RESUME_INTENT`: non-owning HANDOFF/STALE/ORPHAN contention record.
- `RESUME`: winning HANDOFF intent → owner.
- `RECOVER`: winning STALE/ORPHAN intent → owner.
- `PROGRESS`: renews the current lease only; does not create a new generation.
- `STATUS`: owner-authored task result/status or explicitly authorized external supersession/invalidation.
- `REVIEW_STATUS`: independent review completion/disposition.
- `VERIFICATION_STATUS`: independent PASS/FAIL bound to exact candidate/manifest/Wave1 source/base.
- `INTEGRATION_STATUS`: post-squash terminal integration/canonicality record.

The manifest defines exact required fields, enums/constants, predecessor/source conditions, winner predicates, external authorization references, and downstream effects for every kind.

## 13. Claim/resume/recovery and mutation fence

### New claim

Re-read issue/prerequisites/branch/capsules; create exactly `planning/issue-N` from current main; post schema-2 `CLAIM`; re-fetch state; edit only if it is the winning grant.

### Orphan

Branch without owner → `ORPHAN_PROBE`; after ten server minutes, valid contenders post `RESUME_INTENT(reason=ORPHAN)`; winner posts `RECOVER` if condition/head still match.

### Handoff

Valid `STATUS(state=HANDOFF_READY)` → `RESUME_INTENT(reason=HANDOFF)` → winning `RESUME`.

### Stale

Expired owner → `RESUME_INTENT(reason=STALE)` → winning `RECOVER` if stale condition/head still match.

### Fence

Before every task-branch mutation:

1. re-fetch schema-valid comments;
2. verify current generation + lease;
3. fetch remote branch head;
4. require remote head equals proposed commit parent;
5. create commit with that exact parent;
6. update branch ref with `force=false` only;
7. abort on mismatch/non-fast-forward.

## 14. Mission-class completion

- Root proposals → `STATUS(REVIEW_READY)`.
- Domain syntheses → `STATUS(REVIEW_READY)`.
- Final synthesis → `STATUS(VERIFICATION_READY)`.
- Reviews → `REVIEW_STATUS` with `PASS_FOR_SYNTHESIS | CHANGES_REQUIRED | INVALIDATED`.
- Verification → `VERIFICATION_STATUS(PASS|FAIL)`.
- Integration/canonicalization → post-merge `INTEGRATION_STATUS`.
- Retirement/invalidation uses exact schema-2 external authorization references where no current task owner exists.

`CHANGES_REQUIRED` may unlock only the declared synthesis/revision task; `INVALIDATED` unlocks only declared recovery/replanning. Authors cannot self-promote to verification PASS or canonicality.

## 15. Context and evidence budget

Always read `/AGENTS.md`, canonical `START-HERE`, selected issue, canonical Planning Program at activation SHA, and issue-declared authoritative packet. Everything else is forbidden-by-default unless an optional trigger is satisfied.

Every root proposal begins with a Review Index ≤4,000 UTF-8 characters. Simultaneously mandatory review/synthesis context is capped at 100,000 UTF-8 characters. If a known execution context is smaller than 200,000 characters, additionally cap at 50% of that known window. If the execution limit is unknown, deterministic fallback is 100,000. Silent truncation is forbidden; use stable-pointer retrieval or an explicitly authorized bounded split.

Artifacts separate observed evidence, inference, recommendation/decision, and assumption.

## 16. No-READY liveness

When no ordinary READY task exists:

1. valid active ownership can unblock graph → graph live;
2. handoff/mature orphan/stale owner → recover;
3. eligible review/revision/verification/integration → execute before new proposals;
4. otherwise classify cycle/orphan prerequisite/invalidated dependency/missing transition/corrupted status.

`W1-REC-01` is a single-use recovery task for case 4 only and cannot waive review, verification, canonicalization, or squash integration. Accepted recovery may create one blocked successor recovery issue.

The special post-Issue-6-squash/pre-terminal activation window is handled by Section 9 and is not a normal liveness failure.

## 17. Branch, handoff, PR, integration

New tasks branch from current `main` unless an immutable alternative is stated. WIP commits preserve reconstructable state. Every repository-changing episode updates `docs/planning/handoffs/issue-N.md`; handoff records substantive `work_sha`, while the final operational comment records resulting branch head. PR existence is visibility/provenance, not authority. All `main` integration is squash-only.

## 18. Artifact schemas

- Proposal/research: status, Review Index, scope, inputs, goals/non-goals, constraints, assumptions, evidence, alternatives, design, interfaces, evaluation, failure modes, risks, open questions, reopen conditions, critiques, downstream work.
- Review: reviewed IDs/SHAs, independent execution provenance, attack plan, findings, contradictions, empirical questions, disposition, next action.
- Synthesis: proposal schema + exact producer/review SHAs, all BLOCKER/MAJOR dispositions, interfaces, unresolved conflicts/experiments, decisions/reopen conditions, verification contract.
- Verification: PASS/FAIL, exact candidate work SHA, manifest identity, adopted Wave 1 source blob, verified base main SHA, independent provenance, scenarios, defects/evidence/remediation.

## 19. Independent critique boundary

Required reviewer/verifier independence means a distinct cold-start execution context without producer private context, starting from repository + GitHub state, recording platform run identity when exposed, recording excluded prior roles, and acquiring its own evidence before reconciling previous conclusions. Session IDs alone do not prove independence.

## 20. First-wave mission DAG

The exact reviewed Wave 1 issue contracts are immutably adopted from Issue #4 manifest blob `d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd`, and only these sections are adopted:

- `issue_compiler`;
- `universal_root_acceptance`;
- `wave_1`;
- `non_root_optional_retrieval`;
- `next_wave_candidate_schema`.

Issue #4 `verification_contract` and `bootstrap_canonicalization` are explicitly not adopted.

The graph remains exactly 23 initial missions: 12 roots, 3 domain reviews, 3 domain syntheses, cross review, final synthesis, verifier, canonicalizer, and one recovery task.

After Issue #6 squash integration, Issue #6 obtains the concrete main SHA, instantiates/validates exactly those 23 contracts with that activation SHA, posts mission-ID→issue mapping, then posts terminal schema-2 `INTEGRATION_STATUS`. Only after that terminal status do derived prerequisites make the 12 roots READY.

## 21. Safe concurrency

Root missions own unique output paths. Filesystem ownership, semantic conflicts, hard prerequisites, and review dependencies are explicit. Shared canonical edits converge through synthesis rather than concurrent sibling edits. Useful parallelism means independently progressing conflict-free work, not branch count.

## 22. Canonicalization and verified promotion

### Verification binding

A fresh valid Issue #5 PASS binds the exact Issue #11 candidate work SHA, Issue #11 manifest identity, adopted Wave 1 blob `d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd`, exact `verified_base_main_sha`, and simulated generated issue graph.

### Mechanical promotion

Issue #6 may apply only the **three header literal replacements** enumerated in the verified Issue #11 manifest; all other candidate bytes remain identical. This body is deliberately valid in both pre-canonical and post-canonical states.

Immediately before merge, expected PR head and verified base/current-main compatibility are rechecked; any drift requires independent compatibility/reverification. No unresolved BLOCKER/MAJOR may remain. Every merge is squash-only.

### Post-merge activation

The squash commit creates canonical files and entry docs. Until Issue #6 completes the verified post-merge sequence and posts terminal schema-2 `INTEGRATION_STATUS` for that exact main SHA, Issue #6 remains the sole bootstrap completion surface and normal Wave 1 selection is inactive. Only then is bootstrap provenance-only and Wave 1 active.

## 23. Backlog retirement and next-wave governor

Obsolete work is superseded/invalidated or closed with provenance; invalid edges are removed; duplicates merge/defer; unselected candidates remain data. Later-wave activation may instantiate at most 24 new issues and at most 12 initially READY issues. Compiler checks IDs, acyclic hard dependencies, ownership conflicts, review routes, output collisions, and activation prerequisites.

## 24. Observability

Track cold-start success/failure, invalid capsules by kind/reason, duplicate claims, orphan/stale recovery, fence aborts, handoff reconstruction, context packet sizes, useful READY frontier, review findings/escapes, liveness incidents, retired/created work, ownership conflicts, self-canonicalization attempts, base drift, and non-squash integration attempts.

## 25. Failure modes defended

Branch-create/claim crash, competing takeover, stale writer, malformed/edited/unknown capsule, hidden transition interpreter, ambiguous review routing, fake independence, context overload, canonical rewrite drift, stale bootstrap dispatcher text, post-squash activation window, moving main, pre-activation claim, recovery branch reuse, unbounded backlog, hidden human approval, provenance/canonicality confusion, and premature implementation.

## 26. Risks

Procedural fencing, procedural identity separation, context thresholds, and wave caps remain explicit Wave 1 research/measurement targets.

## 27. Open questions

Which machine claim primitive replaces procedural fencing; which identity/permission boundary strengthens review independence; what measured context budget predicts deep review; which evidence surfaces need protection; which engine candidates deserve spikes; which game-system boundaries preserve sandbox depth and technical concurrency.

## 28. Reopen conditions

Reopen v1 if a fresh verifier cannot derive one next task; two compliant owners can remain authorized; any schema-2 kind needs invented validity policy; orphan recovery needs a human; context packets repeatedly overflow; canonicalization changes verified semantics; base drift bypasses re-verification; useful concurrency collapses; recovery repeats without root-cause work; wave caps fail; or a later explicit human directive supersedes a binding constraint.

## 29. Bootstrap provenance invariant

The bootstrap authority chain is:

`#2 proposal → #3 review → #4 candidate → #5 FAIL → #11 remediation → fresh #5 re-verification → #6 canonicalization`

Before this file is CANONICAL, unresolved bootstrap state is represented by repository/GitHub issue state and the verified manifest. **After this file is CANONICAL and Issue #6 has posted a valid terminal schema-2 `INTEGRATION_STATUS` for this exact canonical main SHA, Bootstrap Issues #2–#6 and #11 are historical provenance only and MUST NOT be selected as normal planning work. Before that terminal status, Issue #6 is the sole bootstrap completion surface.**

A canonical reader never interprets this provenance chain as an instruction to repeat #5 or #6 after terminal activation.

## 30. Canonical downstream selection invariant

- Non-CANONICAL state never activates Wave 1.
- CANONICAL state without terminal Issue #6 integration status is the bounded post-merge activation window; only Issue #6 completion may proceed.
- CANONICAL state + matching `START-HERE` + terminal Issue #6 status + Wave 1 issues carrying that activation SHA activates the open `[PLAN-v1]` queue.
- Fully activated fresh agents follow Section 9 and schema 2 and do not re-enter bootstrap.
- No transition here authorizes gameplay implementation or mass implementation backlog generation.
