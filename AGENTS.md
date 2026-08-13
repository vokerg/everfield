# AGENTS.md — Canonical Planning

## Status

This file governs Everfield's **pre-implementation PLANNING phase** and delegates normal planning dispatch to canonical `docs/planning/PLANNING-PROGRAM-v1.md` through `docs/planning/START-HERE.md`.

Bootstrap planning artifacts are provenance after canonical activation. High-throughput gameplay implementation remains blocked until a later independently verified implementation-readiness decision.

## Prime Directive

Everfield is an AI-native project. The normal development process must not depend on routine human approval. AI agents are expected to plan, design, implement, test, review, verify, integrate, evaluate, and re-plan the project autonomously. Human intervention is an exceptional external override, not a normal workflow state.

## Current Phase

The repository is in **PLANNING** mode under canonical Planning Program v1.

Agents MUST NOT implement gameplay/high-throughput implementation before verified implementation readiness, choose an engine as an unreviewed assumption, generate an unbounded implementation backlog, treat design hypotheses as permanently settled, or optimize for a single quality metric.

Agents SHOULD execute bounded canonical planning missions, preserve evidence/provenance, and reopen assumptions when evidence requires it.

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
3. Read current canonical `docs/planning/PLANNING-PROGRAM-v1.md`.
4. Parse its `Canonicalized by` issue and resolve the active canonical binding defined by the program.
5. If binding resolves, select/resume open `[PLAN-v1]` work under the canonical dispatcher.
6. If no binding exists and the named issue has never published a canonical binding, execute only that issue's verified post-merge activation sequence.
7. If a prior binding exists for another program blob, fail closed as `CANONICAL_BINDING_MISMATCH` and use canonical recovery/reverification.
8. Never use chat history as project authority and never integrate into `main` except by squash merge.

After active canonical binding, Bootstrap Issues #2-#6, #11, and #14 are provenance only.

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

## Review Visibility Rule — Canonical Human Directive

Before publishing a terminal schema-3 `STATUS(REVIEW_READY)`, an agent MUST ensure an **open draft PR** exists from the exact task branch to `main`.

- The draft PR is a diff/provenance/review surface only. Its existence or approval grants no integration, canonicality, verification, or merge authority.
- The PR head must match the `head_sha` recorded by the terminal `REVIEW_READY` status.
- A draft PR may be converted or merged only through a separately eligible integration route.
- All integration into `main` remains squash-only.

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
