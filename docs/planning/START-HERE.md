# START HERE — Planning Bootstrap

**Phase:** PLAN-THE-PLAN  
**Audience:** Fresh AI agent with no prior conversation context  
**Authority:** This file operationalizes the current bootstrap `AGENTS.md`; it does not replace it.

## 1. Your First Five Minutes

Do not begin by reading the entire repository.

Perform this sequence:

1. Read `/AGENTS.md`.
2. Read this file.
3. Inspect open GitHub issues whose title begins with `[PLAN-BOOTSTRAP]`.
4. Prefer resumable in-progress bootstrap work over starting additional work.
5. If no work is in progress, select the lowest-numbered eligible bootstrap issue whose prerequisites are satisfied.
6. Read only the files listed by that issue under **Authoritative inputs** plus any documents it explicitly references.
7. Claim or resume the issue using the temporary protocol below.
8. Produce the exact repository artifact required by the issue.
9. Before stopping for any reason, leave a structured handoff.

Do not select one of the 50 seed missions in `03-planning-program.md` directly unless a bootstrap issue explicitly assigns it. Those missions are candidate planning inputs, not yet an executable queue.

## 2. Current Immediately Executable Work

At the time this bootstrap entry point was created, the canonical first task is:

- GitHub Issue **#2 — `[PLAN-BOOTSTRAP] Produce Planning Program v1 entry protocol and first-wave mission graph`**.

If issue #2 is still open, inspect it before inventing any new planning task.

If it already has an active task branch, treat the issue as in progress and follow the resume rules below instead of creating parallel competing work.

If issue #2 is closed, use the open `[PLAN-BOOTSTRAP]` issue set as the work queue. The issue graph created by Planning Program v1 supersedes this hard-coded bootstrap pointer.

## 3. Temporary Planning-Phase Claim Protocol

The mature atomic dispatcher does not exist yet. During PLAN-THE-PLAN, use deterministic issue branches as the primary mutual-exclusion mechanism.

### New work

For an eligible issue `#N`:

1. Re-read the issue immediately before claiming.
2. Confirm all stated prerequisites are satisfied.
3. Use exactly this deterministic branch name unless the issue explicitly overrides it:

   `planning/issue-N`

4. Create that branch from the base branch stated by the issue. For seed-corpus work, the default base is `planning/factory-seed`.
5. If branch creation fails because `planning/issue-N` already exists, **do not create an alternate branch**. Treat the issue as already claimed/in progress and inspect it for continuation state.
6. After successfully creating the branch, leave a GitHub issue comment containing a claim capsule:

```yaml
kind: CLAIM
issue: N
branch: planning/issue-N
base: <base-branch>@<base-sha>
state: IN_PROGRESS
started_at: <ISO-8601 UTC timestamp>
role: <role from issue>
```

The exact deterministic branch creation, not the prose comment, is the temporary exclusion primitive. There must never be two normal task branches for the same bootstrap issue.

### Resume work

Resume an existing branch only when at least one of the following is true:

- the latest handoff explicitly marks it `HANDOFF_READY`;
- the previous session explicitly states that another agent should continue;
- a future stale-claim rule marks it recoverable.

Before editing:

1. read the issue;
2. read the latest handoff;
3. inspect the branch diff/history;
4. independently review existing work before extending it;
5. record a `RESUME` capsule on the issue.

Never assume incomplete work is correct merely because another agent wrote it.

## 4. Branch Semantics During Bootstrap Planning

- `main` remains the stable repository base.
- `planning/factory-seed` contains the current seed corpus and draft PR #1.
- Work that refines the seed corpus should normally branch from `planning/factory-seed` as `planning/issue-N`.
- Review PRs for bootstrap planning work should target `planning/factory-seed` unless the issue explicitly says otherwise.
- Do not push unrelated changes directly to `main`.
- Do not rewrite or force-push another task branch.

This is temporary. Planning Program v1 must replace it with the mature branch/task lifecycle.

## 5. Context Loading Rule

Load context progressively.

### Always read

- `/AGENTS.md`;
- this file;
- the selected issue.

### Then read

Only the issue's authoritative inputs.

### Retrieve additionally when needed

- project charter for project-level constraints;
- autonomous factory mandate for workflow/factory questions;
- game-design mandate for product/game questions;
- evaluation/evidence document for quality-oracle questions;
- research agenda for unresolved evidence questions;
- planning deliverables for artifact/dependency questions.

Do not preload all planning documents merely because they exist.

## 6. Required Planning Artifact Shape

Unless an issue specifies a stronger schema, substantial planning output must contain:

1. Status
2. Scope
3. Inputs
4. Goals
5. Non-goals
6. Constraints
7. Assumptions
8. Evidence / source basis
9. Alternatives considered
10. Proposed design or conclusion
11. Interfaces / dependencies
12. Observability / evaluation
13. Failure modes
14. Risks
15. Open questions
16. Reopen conditions
17. Required independent critiques
18. Downstream artifacts/work unblocked

Separate observed evidence from inference and recommendation.

Do not label a new proposal CANONICAL merely because you authored it.

## 7. Required Handoff

Every work episode that changes repository state must leave a handoff before stopping.

Default handoff path:

`docs/planning/handoffs/issue-N.md`

If the file already exists, update it rather than creating competing handoff files unless the issue defines a history format.

Minimum handoff schema:

```yaml
issue: N
role: <role>
branch: <branch>
head_sha: <sha>
base_sha: <sha>
state: IN_PROGRESS | BLOCKED | REVIEW_READY | HANDOFF_READY
completed:
  - ...
remaining:
  - ...
checks_performed:
  - ...
evidence:
  - ...
known_problems:
  - ...
decisions:
  - ...
scope_deviations:
  - ...
recommended_next_action: ...
```

A short prose section may follow, but the structured capsule must be sufficient for continuation.

If no repository changes were made, leave the equivalent structured status on the issue rather than inventing a meaningless commit.

## 8. When Is a Planning Task Ready for Review?

A planning task may move to review only when:

- every required output named in the issue exists;
- the artifact explicitly distinguishes assumptions, evidence, and decisions;
- important alternatives are represented fairly;
- unresolved questions are explicit;
- dependencies and downstream effects are explicit;
- acceptance criteria in the issue have been self-checked;
- the handoff/status points to the exact branch/head SHA;
- the artifact identifies the independent critique it requires.

The author does not canonicalize its own work.

## 9. What Not to Do

A fresh agent must not:

- start gameplay implementation;
- choose a final engine because it is familiar;
- convert the 50 seed missions directly into a giant issue backlog;
- invent a parallel planning process when an eligible bootstrap issue already exists;
- ask for routine human approval;
- read the prior chat as required project memory;
- treat draft PR #1 as reviewed truth;
- hide uncertainty in confident prose;
- leave uncommitted work as the only continuation state.

## 10. Bootstrap Exit

This file is intentionally temporary.

Planning Program v1 must define and supersede:

- task discovery;
- task claiming;
- continuation/stale-work recovery;
- exact planning roles;
- first-wave planning DAG;
- output schemas;
- critique/review routing;
- canonicalization;
- context packets;
- planning checkpoints.

When that system becomes CANONICAL, this file should either become a thin pointer to the mature dispatcher or be marked SUPERSEDED.