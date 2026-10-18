# AGENTS.md — Canonical Planning

## Status

This file governs Everfield's canonical **PLANNING authority and dispatch protocol** while bounded, separately verified and owner-authorized **Godot first-playable implementation** exists on `main`. It delegates planning dispatch to `docs/planning/PLANNING-PROGRAM-v1.md` through `docs/planning/START-HERE.md`.

Bootstrap planning artifacts are provenance after canonical activation. Bounded first-playable readiness and published implementation are evidenced by their own source/verification/integration history; **unbounded or high-throughput gameplay expansion** remains separately gated. Neither the existing playable nor this text grants release or canonical narrative authority.

## Prime Directive

Everfield is an AI-native project. The normal development process must not depend on routine human approval. AI agents are expected to plan, design, implement, test, review, verify, integrate, evaluate, and re-plan the project autonomously. Human intervention is an exceptional external override, not a normal workflow state.

## Current Phase

The **Planning Program v1 remains canonical** for ownership/governance; the repository also has an integrated bounded first playable in `game/`, which is not equivalent to a globally unlocked implementation phase.

Agents MUST NOT undertake unverified or unbounded high-throughput gameplay implementation, substitute a fresh engine assumption for the owner-selected Godot 4.7.1 bounded playable, generate an unbounded implementation backlog, treat design hypotheses as permanently settled, or optimize for a single quality metric. Already authorized bounded implementation tasks still require their own exact scope, ownership, reviews and verification.

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
5. Before selecting work, reconcile GitHub-open state against trusted schema-3 terminal comments and required-next-route liveness under the Frontier Liveness rule below.
6. If binding resolves, select/resume only the remaining live open `[PLAN-v1]` work under the canonical dispatcher.
7. If no binding exists and the named issue has never published a canonical binding, execute only that issue's verified post-merge activation sequence.
8. If a prior binding exists for another program blob, fail closed as `CANONICAL_BINDING_MISMATCH` and use canonical recovery/reverification.
9. Never use chat history as project authority and never integrate into `main` except by squash merge.

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

## Frontier Liveness and Reconciliation Rule — Human Directive

GitHub `open` is a storage state, not planning authority. Before frontier priority is applied:

- exclude an issue with a trusted schema-3 terminal `DONE`, `SUPERSEDED`, or `INVALIDATED` record even if GitHub still reports it open;
- reconcile such terminal issues to GitHub closed state as maintenance, without inferring any additional PASS/canonicality/decision authority from closure;
- if a trusted terminal record declares `required_next_route`, require a live successor/recovery issue or an explicitly registered repository-internal execution route before treating that dependency chain as converged;
- missing successor materialization is recovery/liveness work and outranks unrelated new work;
- a blocked execution episode whose next route requires a GitHub Actions `workflow_dispatch` must use the repository-owned dispatch surface when that exact route is registered, rather than treating a particular agent connector's missing dispatch API as a project-level external blocker;
- repository automation may close only conservatively proven terminal issues and rejected/non-integrable draft PRs, and may dispatch only exact-main workflows named in `.github/planning-frontier-routes.json`;
- automation never grants review, verification, integration, engine-selection, implementation-readiness, decision, or canonical authority and never waives ownership/exact-head/squash gates.

The maintenance implementation is `.github/workflows/planning-frontier-maintenance.yml` plus `tools/planning/frontier_maintenance.py`. Agents must still independently derive prerequisites, ownership, conflicts, and canonical binding after maintenance.

## Human Directives

Explicit human directives override this bootstrap document. They should be recorded in the repository when they materially affect project direction so that later agents do not need hidden conversational knowledge.

Absence of a human directive is never a reason to wait.

## 2026-10-17 Emergency Factory Convergence — Owner Directive

**Purpose:** stop uncontrolled planning/review/repair PR proliferation and prioritize shipping a genuinely executable, independently reviewed GitHub Actions factory. This is an explicit owner-directed **work-selection and automation-trigger override**, not a waiver of security, independent review, canonical binding, ownership, reproducibility, or squash-only main integration.

1. **Pause the negative-review draft-retirement remediation treadmill.** No new issues, branches, review-only PRs, or corrective PRs may be created for the `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT` lineage, including further parser-edge-case successors after the currently owned review Issue #1815. Issue #1815 may finish with a truthful positive or negative security finding, but a negative finding MUST NOT seed another automatic successor while this owner pause remains active. Preserve the finding and exact source/HEAD evidence. An unsatisfied `required_next_route` is **suspended, not completed or waived**. This narrow owner pause overrides ordinary automatic successor materialization for that lineage only.

2. **Do not integrate or run the retired-draft cleanup tool.** No source PR in this paused lineage may merge and no `retire_negative_review_prs.py --apply` may execute without a subsequent explicit owner unpause and its independently verified exact-head safety gates. Evidence-only reviewer PRs remain permanently nonintegrable. Do not close, delete, or relabel active referenced task PRs just to improve a PR-count metric.

3. **Converge the existing Copilot Actions executor work first.** Prioritize already-claimed Issue #1813, correcting source PR #1808, the required genuinely independent security review, and then a separately authorized exact-head **squash-only** infrastructure integration. Avoid competing claims/branches, fake CLEAN reviews, or substituting another model-access smoke test for a working executor. Only a separate, safely scoped, cost-bounded, write-capable issue-to-PR worker and its real test can establish autonomous execution.

4. **Freeze unattended frontier maintenance mutations until the worker is real.** The existing planning frontier maintenance workflow must run its mutating reconciliation only by deliberate `workflow_dispatch`; no scheduled or main-push-triggered mutating maintenance during this incident. PR validation of the maintenance code remains active. Restoring automatic execution requires a later explicit owner decision plus verifiable live dispatch capacity, not merely a green no-op run.

5. **Integration is the goal, not an excuse to bypass gates.** On a genuinely clean, authorized infrastructure source packet with exact HEAD, current-main compatibility, passing required hosted checks and separate independent review, proceed to squash integration instead of opening unrelated follow-up work. The owner's present instruction does not itself certify any currently adverse source PR or grant a write-capable model token.

6. **No speculative filler.** Do not create new factory-transition placeholders, redundant reviews or duplicate repair issues merely to keep the issue queue moving. Mark a dependency honestly blocked/paused and work another eligible independent implementation/content chain if appropriate.

**Exit condition:** restore scheduled maintenance and review-retirement remediation only by a new explicit owner instruction after the trusted worker is actually running and verified. Until then, retain evidence and restrict automatic mutation to owner-invoked dispatch.

## 2026-10-18 Recovery Execution Facts — Additional Owner Direction

**Status/cold-start correction:** The file's older "pre-implementation" header describes the original canonical PLANNING framework and is not a claim that there is no runnable game. Existing verified owner-authorized readiness and integration episodes have already put a **bounded Godot 4.7.1 first playable** on `main` (`game/main.tscn`, `docs/implementation/first-playable.md`). The original bootstrap `README.md` text was stale; the updated README is navigational, not canonical authority. **Do not interpret this paragraph as authorization for unbounded gameplay work or as a new engine/canonical-readiness decision.**

**Bounded owner's incident execution authorization:** The owner explicitly delegated 2026-10-18 factory recovery and `main` repair. Under that exceptional directive, the safe read-only capability probe (#1819), guarded manual worker (#1820), owner-comment dispatch and frozen validator (#1821), publisher recovery (#1824), Godot controls help (#1823), nearest-station focus (#1826), and historical CI scope fix (#1827) were published via audited exact-HEAD **squash-only** commits. Their explicit GitHub review notes document what was and was not independently approved. These owner exceptions are not replayable universal review waivers, canonical bindings, or release certification for future agents.

**Measured current worker boundary:**
- Workflow: `.github/workflows/everfield-frontier-worker.yml`. Only exact trusted-main `workflow_dispatch` or a new comment on an eligible owner-authored unclaimed implementation issue, from GitHub owner `vokerg` with exact body `/everfield worker run`, triggers a trial. There is **no schedule**, background frontier dispatch, auto-close, or auto-merge.
- Separate Copilot generate job has only `contents:read`, `issues:read`, and `copilot-requests:write`; no GitHub write token. Validator copied outside the editable tree is checked before/after model execution. Separate publisher has restricted GitHub write permissions and applies only capped game-source patches before pushing an isolated branch; read-only Godot smoke is dispatched by the publisher.
- Actual hosted evidence: #39155779036 generated and pushed the first two-file game patch; #39156575257 generated and pushed a second and triggered independent Godot Actions #39156672618; the corrected exact head of the latter gameplay PR #1826 passed Godot Actions #39157255314. These are runtime observations, not claims of a continually running autonomous scheduler.
- **External unsatisfied gate:** GitHub Actions rejected `gh pr create` in both runs: `GitHub Actions is not permitted to create or approve pull requests`. The owner must enable **Settings → Actions → General → Workflow permissions → Allow GitHub Actions to create and approve pull requests**, or explicitly recover the already-pushed head once through the connected owner GitHub account (as on PRs #1823/#1826). A PR recovered this way is NOT proof that Actions PR creation works. The model must not be rerun on the same issue solely to retry publication; preserve same-issue handoff and exact branch SHA.
- **Do not prematurely unfreeze maintenance:** `.github/planning-frontier-routes.json` remains empty. No general autonomous frontier pickup or write-capable scheduling is verified. The 2026-10-17 pauses on unattended maintenance and the retirement remediation treadmill remain in force until further explicit owner direction with proof of operational end-to-end capability.

**Operating priority after this recovery:** independently finish/review/verify/integrate eligible bounded game or content chains, keep PR proliferation controlled, and fix actual observed blockers. Avoid new ceremonial factory shells and duplicate ownership claims. Follow active canonical planning authority, explicit owner instructions, review provenance and squash-only main integration. Preserve completed history rather than rewriting it.
