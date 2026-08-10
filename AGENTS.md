# AGENTS.md — Planning Bootstrap

## Status

This file governs the **pre-implementation planning phase** of Everfield. It is intentionally provisional. Future planning work is expected to replace or substantially expand it before implementation begins.

## Prime Directive

Everfield is an AI-native project. The normal development process must not depend on routine human approval. AI agents are expected to plan, design, implement, test, review, verify, integrate, evaluate, and re-plan the project autonomously. Human intervention is an exceptional external override, not a normal workflow state.

## Current Phase

The repository is currently in **PLAN-THE-PLAN** mode.

Agents working under this version of `AGENTS.md` MUST NOT:

- implement gameplay;
- choose an engine as an unreviewed assumption;
- generate a large implementation backlog;
- treat any current design hypothesis as permanently settled;
- optimize for issue count, code volume, or token efficiency.

Agents SHOULD:

- refine the autonomous development model;
- research relevant software-engineering, agentic, game-development, testing, evaluation, and CI practices;
- define measurable decision processes;
- identify unresolved design questions;
- propose competing approaches;
- design planning-agent missions;
- define how planning outputs will be criticized and synthesized;
- preserve important conclusions in repository-owned artifacts.

## Canonical Working Principles

1. **The repository is memory.** Important knowledge must not exist only in chat history.
2. **Execution must be resumable.** Every meaningful work episode must leave a continuation artifact.
3. **Review must be independent.** Authors/implementers cannot be the final judges of their own work.
4. **Evidence beats assertion.** Tests, executable scenarios, telemetry, screenshots, traces, reproducible state, and authoritative research are preferred over prose claims.
5. **No routine human gate.** Uncertainty should trigger more evidence, more independent evaluation, or re-planning before it triggers human escalation.
6. **Context is a budgeted resource.** Agents should load only the context required for their role and task.
7. **Parallelism must be designed.** Architecture and task decomposition should target large safe READY frontiers for many concurrent agents.
8. **The factory is itself a product.** Agent protocols, schedulers, evaluators, CI, handoffs, review loops, and planning mechanisms must be versioned, measured, and improved.
9. **Goodhart resistance is mandatory.** No single metric or self-authored test suite may become the sole quality oracle.
10. **Reversibility matters.** Early plans should record assumptions and reopen conditions rather than pretending uncertainty does not exist.

## Mandatory Cold-Start Entry Point

A fresh agent with no prior conversation context MUST:

1. Read this file.
2. Read `docs/planning/START-HERE.md`.
3. Inspect open GitHub issues beginning with `[PLAN-BOOTSTRAP]`.
4. Follow the eligibility, claim/resume, branch, context-loading, output, review, and handoff rules in `START-HERE.md` and in the selected issue.
5. Read `docs/planning/README.md` only after the entry protocol tells it what planning context is relevant.

Do **not** choose one of the candidate missions in `docs/planning/03-planning-program.md` directly. Those missions are seed material until Planning Program v1 turns them into an executable mission graph.

At the current bootstrap state, Issue #2 is the first executable planning task after seed PR #1 is integrated. Issues #3–#6 form its gated review/synthesis/verification/canonicalization chain and are not eligible until their stated prerequisites are met.

## Planning Work Output Rule

A planning agent must produce a bounded repository-owned artifact using the schema required by its issue. Unless the issue is stricter, the artifact must explicitly separate:

- scope and non-goals;
- constraints and assumptions;
- evidence from inference;
- alternatives from recommendations;
- dependencies/interfaces;
- observability/evaluation;
- failure modes and risks;
- unresolved questions;
- reopen conditions;
- required independent critiques;
- downstream work unblocked.

The author must not mark its own new proposal CANONICAL unless an already-canonical protocol explicitly permits that transition.

## Stopping Rule

A session may stop before its planning task is complete, but it must leave the repository in a reconstructable state. A future agent must be able to continue from repository + GitHub state alone, without access to prior conversation context.

Before stopping after modifying repository state:

- commit useful work to the task branch;
- ensure the task branch is pushed/visible;
- update the structured handoff required by `docs/planning/START-HERE.md` or the issue contract;
- record what is complete, what remains, known problems, checks/evidence, and the next recommended action;
- do not leave uncommitted local state as the only copy of useful work.

A continuation agent must independently inspect/review inherited work before extending it.

## Main Integration Rule — Canonical Human Directive

All changes integrated into `main` MUST use **squash merge**.

- Task/feature branches may contain multiple WIP, review, and correction commits.
- Integration into `main` produces one squash commit representing the accepted task/PR outcome.
- Normal agents MUST NOT use merge commits or rebase-merge to integrate a PR into `main`.
- If repository settings permit other merge methods, this rule still governs agent behavior until explicitly superseded by a later human directive.
- Planning Program v1 and all later workflow specifications must preserve this rule.

## Human Directives

Explicit human directives override this bootstrap document. They should be recorded in the repository when they materially affect project direction so that later agents do not need hidden conversational knowledge.

Absence of a human directive is never a reason to wait.
