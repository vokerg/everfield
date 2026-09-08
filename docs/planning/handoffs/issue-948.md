# Issue #948 handoff — factory convergence v5

## Scope
Bounded factory liveness remediation only. `NOT_CANONICAL`.

Base/current main at materialization: `96384e0bb80e8225ba41346f6f942b66c0a5081b`.
Canonical Planning Program v1 binding remains Issue #6 comment `5245368879`, blob `e3120ec203c4156328770aa86c12fbb7187966dc`.

## Defect reproduced
The current scheduled maintenance entry point is v4. v4 durably consumes only trusted semantic transition terminals. When an exact wrapper is instead closed as `duplicate` or `not_planned`, the exact `(source_issue, source_terminal_comment_id, route)` is forgotten, so a later hourly reconciliation creates another wrapper for the same generation.

On 2026-09-08 this recurred across old source generations including #792, #801, #810, #811, #812, #814, #815, #821, #871, #894, #909, and #918.

A second avoidable path exists when `required_next_route` already names a concrete successor issue. Examples observed in the live queue include:
- `ISSUE_895_FORMAL_ENGINE_SELECTION_READINESS_DECISION_GATE`;
- `EXISTING_REQUIRED_REVIEW_917`;
- `BLOCKING_REMEDIATION_ISSUE_833`;
- `AUTHORIZED_INTEGRATION_ISSUE_819_...`;
- `CONTINUE_AUTHORIZED_INTEGRATION_788_WITH_PR_793_...`.

Current v1-v4 successor-edge matching can miss these even though the source route itself already names the live issue.

## Repair
`tools/planning/frontier_maintenance_v5.py` composes v4 and adds two narrow liveness rules:

1. **Explicit route-declared successor consumption.** A route consumes wrapper materialization only if it encodes exactly one unambiguous issue number using bounded `ISSUE`, `INTEGRATION`, `REVIEW`, or `REMEDIATION` route forms, and that target already exists as a trusted/eligible non-PR, non-factory-transition issue. This proves only that the successor is materialized; it grants no authority to that successor.
2. **Exact-generation wrapper reuse.** If the exact source generation already has an open trusted wrapper, maintenance reuses it. If all prior wrappers were conservatively closed as `duplicate`/`not_planned`, maintenance may reopen the newest one instead of creating another issue, but only when that wrapper has no nonterminal trusted schema-3 operational state. A completed wrapper is never reopened and remains governed by the v4 semantic terminal rules.

v5 also retires an unowned open wrapper immediately when its exact current source route already names a trusted live successor issue. Claimed wrappers are preserved.

## Producer self-review recovery
The first producer REVIEW_READY head `766abda23f671238cafea3831f9227f660864d93` was superseded before any independent review after producer self-review found `FACTORY_V5_REOPEN_STALE_OWNERSHIP_GUARD`: a closed duplicate/not-planned wrapper with a nonterminal trusted operational ownership record must not be reopened. Recovery comment `5589428167` records the finding. The successor head adds the active-operational-state guard plus a deterministic negative control.

## Workflow
`.github/workflows/planning-frontier-maintenance.yml` now compiles v1-v5, runs the complete v5 self-test chain, and uses v5 for scheduled/push/manual reconciliation.

## Deterministic regression coverage
The v5 self-test covers the live route forms above, ambiguity rejection, trusted-successor eligibility, explicit-successor wrapper redundancy, open exact-generation reuse, duplicate/not-planned history reuse, stale-ownership non-reopen, and completed-wrapper non-reopen behavior. Existing v1-v4 self-tests run transitively first.

A separate local route-grammar spot check reproduced the v5 parser expectations for all listed live forms. The execution environment used for this producer could not resolve `github.com` for a local clone, so no local repository self-test PASS is claimed. Full repository-native v1→v5 self-test remains the post-publication workflow acceptance gate.

## Expected effect after publication
- wrappers such as current #939/#941/#943/#944-class routes whose source route already points at a real successor become redundant and are retired when unowned;
- repeated hourly recreation of a previously retired exact generation stops because one safe historical wrapper is reused instead of minting another issue;
- wrappers carrying unresolved trusted ownership are not revived;
- the factory spends fewer agent sessions on bookkeeping and leaves the frontier to real review/remediation/integration work.

## Preserved boundaries
No route registry changes. No workflow permission changes. No direct-dispatch/retry changes. No weakening of trusted-author, schema-3 ownership, exact-head, review, verification, squash-only integration, engine-selection, implementation-readiness, release, decision, or canonical gates.

## Required next gate
Fresh degraded-independent review of the exact successor PR head. If clean, squash-only integration under the 2026-09-08 owner convergence directive recorded in Issue #948, followed by inspection of the push-triggered maintenance run and live wrapper count.
