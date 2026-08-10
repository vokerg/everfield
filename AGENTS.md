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
3. **Review must be independent.** Implementers cannot be the final judges of their own work.
4. **Evidence beats assertion.** Tests, executable scenarios, telemetry, screenshots, traces, and reproducible state are preferred over prose claims.
5. **No routine human gate.** Uncertainty should trigger more evidence, more independent evaluation, or re-planning before it triggers human escalation.
6. **Context is a budgeted resource.** Agents should load only the context required for their role and task.
7. **Parallelism must be designed.** Architecture and task decomposition should target large safe READY frontiers for many concurrent agents.
8. **The factory is itself a product.** Agent protocols, schedulers, evaluators, CI, handoffs, review loops, and planning mechanisms must be versioned, measured, and improved.
9. **Goodhart resistance is mandatory.** No single metric or self-authored test suite may become the sole quality oracle.
10. **Reversibility matters.** Early plans should record assumptions and reopen conditions rather than pretending uncertainty does not exist.

## Planning Work Entry Point

Until a later agent-dispatch mechanism exists, a planning agent should:

1. Read this file.
2. Read `docs/planning/README.md`.
3. Read only the planning documents relevant to its assigned mission.
4. Inspect unresolved questions and dependencies before adding conclusions.
5. Produce a bounded artifact with assumptions, evidence, alternatives, decisions, unresolved questions, and explicit downstream dependencies.
6. Request or create an independent critique pass before treating major conclusions as canonical.
7. Leave a concise structured handoff when stopping.

## Stopping Rule

A session may stop before its planning task is complete, but it must leave the repository in a reconstructable state. A future agent must be able to continue from repository state alone, without access to prior conversation context.

## Human Directives

Explicit human directives override this bootstrap document. They should be recorded in the repository when they materially affect project direction so that later agents do not need hidden conversational knowledge.
