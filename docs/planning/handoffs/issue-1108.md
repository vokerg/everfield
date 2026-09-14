# Issue #1108 — Factory terminal-transition reopen regression

## Mission
`FACTORY-CONVERGENCE-06` — bounded factory-liveness remediation only.

## Ownership
- winning claim: Issue #1108 comment `5659344391`;
- branch: `planning/issue-1108`;
- base/current main at claim: `98f0e66c1332f9a3ce47cf56ad352fab2223e8cd`;
- later claim `5659345909` lost contention and was explicitly excluded by correction comment `5659347724`;
- canonical binding remains Issue #6 comment `5245368879`, program blob `e3120ec203c4156328770aa86c12fbb7187966dc`, activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e`.

## Observed regression
Push-triggered frontier maintenance repeatedly reopened terminal factory-transition wrappers. Representative observed wrappers included:
- #1071 from source #948 route `NONE_FACTORY_V5_CHAIN_COMPLETE`;
- #1072 from source #950 route `NONE_REVIEW_ROUTE_CONSUMED`;
- #1035 from source #952 route `NONE_FACTORY_V5_INTEGRATION_COMPLETE`;
- #1022, #943, and #1105 after trusted terminal reconciliation of already-consumed routes.

The prior required review #950 explicitly required an attack on same-run close→reopen behavior, so this is a regression against the accepted v5 convergence contract.

## Repair
1. `frontier_maintenance_v3.route_is_actionable` now treats exactly `NONE` and `NONE_*` as non-actionable sentinels while leaving values such as `NONEISH` and `SOME_NONE_ROUTE` actionable.
2. v5 adds exact-generation consumption for trusted closed factory wrappers whose latest owner-bound schema-3 terminal is `DONE` or `SUPERSEDED` and declares no actionable next route.
3. `INVALIDATED`, untrusted/open wrappers, and terminals that still declare an actionable route are explicitly not consumed by the new rule.
4. v5 composes this check with existing v4 semantic consumption in the same closed-transition comment pass, avoiding a third API pass.
5. Deterministic regression assertions cover observed `NONE_*` forms plus `DONE`, `SUPERSEDED`, `INVALIDATED`, trust, open-state, and actionable-route boundaries.

## Verification
- exact branch diff before this handoff: two owned maintenance files only, base `98f0e66c1332f9a3ce47cf56ad352fab2223e8cd`, head `21519f96055da88abb099219ded6f8fee3ca9f8e`;
- targeted local decision matrix for route classification and terminal-consumption boundaries: PASS;
- exact source inspection of inserted Python blocks: PASS;
- baseline current-main v1→v5 maintenance workflow had already passed before this bounded patch;
- environment limitation: no local GitHub checkout is available because outbound GitHub DNS is unavailable, and the repository has no pull-request-triggered workflow. Therefore no claim is made that the patched full v1→v5 chain executed locally.

The fresh required review must treat full patched-chain execution as a verification limitation. Any clean integration route must retain mandatory exact-new-main push-triggered v1→v5 acceptance; failure must route blocking remediation rather than being ignored.

## Self-review
- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0
- INFO: 1 — full patched v1→v5 execution is deferred to mandatory post-publication acceptance because this environment cannot run the repository checkout and no PR workflow exists.

## Authority
`NOT_CANONICAL`. This packet grants no review, verification, integration, engine-selection, implementation-readiness, release, decision, or canonical authority. Integration, if later authorized by a clean required review and owner convergence directive, must be a separate squash-only episode.
