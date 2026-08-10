# Planning Program v1 — Bootstrap Canonicalization Report

## Status

**Bootstrap issue:** #6  
**Mission ID:** `BOOTSTRAP-CANON-06`  
**Branch:** `planning/issue-6`  
**Ownership generation:** Issue #6 `CLAIM` comment `5245233112`  
**State:** PRE_MERGE_INTEGRATION_READY  
**Canonicality before squash:** NON-CANONICAL MATERIALIZATION  
**Verified base:** `main@a611c4540df1693fb3536a59f032f1a79b51cdc5`

## Verified authority tuple

Issue #6 is bound to the valid, unedited Bootstrap Issue #5 PASS comment `5245221974`:

- verified candidate work SHA: `00df46cae3230f380bcee9dd24442d984c73fea0`;
- verified candidate path: `docs/planning/12-planning-program-v1-bootstrap-safe-candidate.md`;
- verified candidate blob: `261d7e5f7f9f1412415116b3e0f127f3e3f1bec7`;
- verified manifest path: `docs/planning/12-planning-program-v1-canonicalization-manifest.yaml`;
- verified manifest identity/blob: `f4e65f408b77a917d1fc61a1dbaee808e978f072`;
- adopted Wave 1 contract blob: `d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd`;
- verification result: PASS;
- verification BLOCKER count: 0;
- verification MAJOR count: 0;
- verification trust mode: `DEGRADED_SINGLE_AGENT` under repository-visible constraint comment `5244416013`;
- verified base: `a611c4540df1693fb3536a59f032f1a79b51cdc5`.

No gameplay implementation authority is conveyed by the PASS.

## Pre-merge materialization

### Canonical Planning Program

Created `docs/planning/PLANNING-PROGRAM-v1.md` by the verified deterministic transform from the Issue #18 candidate. The only semantic byte changes are the four allowed header literals:

1. title → `# Planning Program v1 — Canonical`;
2. state → `**State:** CANONICAL`;
3. remediation header → `**Canonicalized by:** Bootstrap Issue #6`;
4. authority → canonical pre-implementation PLANNING authority.

All remaining candidate body content, including the canonical applicability guard, is preserved. The materialized branch blob is `e3120ec203c4156328770aa86c12fbb7187966dc`.

### Root entry path

Applied the verified deterministic root transformations:

- `/AGENTS.md` now reports canonical pre-implementation **PLANNING**, points fresh agents to `START-HERE` + `PLANNING-PROGRAM-v1.md`, resolves the active canonical binding, preserves squash-only integration, and retains the gameplay/high-throughput implementation barrier.
- `docs/planning/START-HERE.md` is replaced by the canonical PLANNING entry pointer and binding-based dispatcher.

The canonical program's `CANONICAL_ACTIVE` applicability guard is authoritative for all fixed bootstrap-numbered clauses, including later remediation Issues #16/#18; after terminal binding these clauses are provenance-only even where older root prose lists only earlier bootstrap issues.

## Activation barrier

**No `[PLAN-v1]` Wave 1 issue may be created before the Issue #6 squash commit exists.**

The pre-merge branch therefore contains only canonical materialization/report/handoff changes. The concrete activation SHA cannot be known until the squash merge succeeds.

After the squash commit exists, Issue #6 must, in order:

1. verify canonical program and root entry files at the resulting main SHA;
2. compute/record the canonical program blob at that main SHA;
3. load only the adopted Wave 1 sections from exact blob `d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd`;
4. instantiate exactly 23 `[PLAN-v1]` issues with that concrete activation SHA and canonical program path;
5. validate mission IDs, prerequisites, output/conflict surfaces, review routes, schemas, evidence/acceptance, branch/handoff/integration rules, and activation binding;
6. post mission-ID → GitHub issue-number mapping on Issue #6;
7. publish terminal schema-3 `INTEGRATION_STATUS` with canonicality `CANONICAL_PLANNING_PROGRAM`, issue count 23, mapping comment ID, canonical program blob, exact PASS, expected PR head, verified base, and squash main SHA.

Only the terminal binding activates normal `[PLAN-v1]` selection. The 12 root proposal missions then derive READY; `W1-REC-01` remains conditional recovery rather than ordinary initial READY work.

## Preserved implementation barrier

Wave 1 is detailed **planning**. It may produce factory, technical, evaluation, evidence, UX, and game-design planning artifacts, but it does not authorize gameplay implementation, a final engine choice, or an unbounded implementation backlog. High-throughput implementation remains blocked until a later independently verified implementation-readiness decision.

## Integration rule

Immediately before merge:

- current `main` must still equal verified base `a611c4540df1693fb3536a59f032f1a79b51cdc5`;
- PR head must equal the expected materialized head;
- Issue #5 PASS `5245221974` must remain valid/unedited;
- no unresolved BLOCKER/MAJOR may exist;
- no Wave 1 issue may have been created;
- merge method must be `squash`.

Any pre-merge base movement invalidates readiness and requires the verification lifecycle rather than an inferred compatibility waiver.
