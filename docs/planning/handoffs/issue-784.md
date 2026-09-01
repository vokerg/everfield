# Issue #784 handoff — semantic transition consumption

## Scope
Bounded factory-process remediation only. `NOT_CANONICAL`.

Current base at claim: `main@7769fbd28453b723bc49e9cf1716b6866d800977`.
Active Planning Program v1 binding remains Issue #6 comment `5245368879`.

## Live defect reproduced
- #780 terminal comment `5490561941` exactly materialized successor review #781 for source generation `(738, 5437117901, FRESH_INDEPENDENT_SECURITY_AUTHORITY_REVIEW_OF_EXACT_REMEDIATION_HEAD)`, but a later scheduled maintenance run created duplicate #783.
- #779 terminal comment `5490482687` exactly reconciled source generation `(776, 5489375430, CONTINUE_AUTHORIZED_INTEGRATION_775_WITH_PR_777)` to already-terminal integration #775 / merged PR #777, but a later run created duplicate #782.
- #778 remains an owned cleanup wrapper for old source #714 and is intentionally not auto-closed until its exact existing integration successor is terminally bound.

## Repair
`tools/planning/frontier_maintenance_v4.py` composes v3 and adds a narrow semantic consumption ledger for closed factory transitions.

A semantic wrapper consumes a source generation only when all of the following hold:
1. the wrapper body binds an exact `(source_issue, source_terminal_comment_id, route)` generation;
2. the wrapper is closed as completed, not `not_planned`/duplicate;
3. the wrapper has a trusted owner-bound schema-3 `STATUS(DONE)` terminal accepted by the existing reconcilable-terminal validator;
4. the terminal repeats the exact source generation;
5. the terminal disposition is one of two live, enumerated cases only:
   - `EXACT_REQUIRED_REVIEW_SUCCESSOR_MATERIALIZED`;
   - `REQUIRED_ROUTE_ALREADY_CONSUMED_BY_TERMINAL_SUCCESSOR`;
6. the referenced successor exists, is trusted/eligible, is not a PR, and is not another factory-transition wrapper;
7. for newly materialized successors, successor creation is not older than the wrapper;
8. for already-terminal successors, `route_consumed: true` is mandatory and the recorded successor terminal comment id must equal the successor's current trusted terminal record.

The resulting exact generations are unioned with the existing v2 dispatch-backed resolved-generation set before both redundant-wrapper retirement and new transition materialization.

## Preserved boundaries
No route registry changes. No workflow permission changes. No action pin changes. No direct-dispatch/retry semantic changes. No ownership, review, verification, exact-head, squash-only integration, decision, release, or canonical authority expansion.

## Required verification
- `py_compile` v1/v2/v3/v4;
- complete v1→v2→v3→v4 self-tests;
- positive controls for #780→#781-style successor materialization and #779→#775-style already-terminal reconciliation;
- negative controls for generation mismatch, untrusted successor, transition successor, wrong disposition, wrong successor terminal comment, and missing owner-bound terminal comments.

After clean review and squash-only publication, live maintenance must retire #782/#783 without recreating them. #778 should be terminally reconciled to #726 separately, then become durably consumed by the same ledger.
