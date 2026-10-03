# Handoff — Issue #1403 / FACTORY-IMPLEMENTATION-LIVENESS-01

## Scope
Prevent the implementation frontier from falling to zero after a clean integrated playable/increment, while preserving real parallel component work.

## Owner authority
- Issue #84 comment `5968764259`: post-first-playable implementation parallelism.
- Issue #84 comment `5889817307`: implementation transition.
- Issue #84 comment `5277825639`: convergence / squash-only integration.

## Implementation
- added `tools/planning/frontier_maintenance_v7.py` as a composition layer over v6;
- recognizes only trusted closed bounded implementation producers/fan-ins whose trusted unedited schema-3 `INTEGRATION_STATUS DONE` records declare `merge_method: squash` and a valid `main_sha`;
- verifies the recorded integration SHA is current-main ancestor/equal before treating it as a continuation source;
- detects an empty implementation lane by explicit implementation root/review/fan-in/intake title namespaces;
- dedupes implementation-demand intakes by integrated source issue;
- duplicate/not-planned intakes do not permanently consume a source;
- creates at most one implementation-demand intake per maintenance execution;
- the generated intake requires 2–4 pairwise-disjoint component roots plus an explicit shared-surface fan-in whenever concrete independent work exists;
- without explicit product-complete authority, an intake may not silently terminate the implementation lane at `required_next_route: NONE`;
- v6 content-demand liveness still runs in the same maintenance execution, so content and implementation lanes may remain live concurrently;
- active maintenance workflow now validates/runs v7.

## Changed paths
- `tools/planning/frontier_maintenance_v7.py`
- `.github/workflows/planning-frontier-maintenance.yml`
- `docs/planning/handoffs/issue-1403.md`

## Validation
- exact v7/workflow blobs inspected from the branch;
- pure source-selection/dedupe scenarios independently reproduced: PASS;
- current #1343 integration lineage verified: `0ad16437...` is an ancestor of current main `4da8dcfd...` (GitHub compare status `ahead`);
- workflow validates all v1–v7 Python files, then executes `frontier_maintenance_v7.py --self-test`;
- full checkout/self-test could not be executed from this environment because shell DNS cannot resolve github.com. No full-chain preintegration PASS is claimed.

## Current expected first activation
After integration and closure of #1403, with no open implementation roots, v7 should select integrated source #1343 exactly once and materialize one `FACTORY-IMPLEMENTATION-DEMAND-1343` intake.

The immediate intake should materialize the already-concrete three implementation components:
1. Old Works world/evidence presentation module;
2. Commons Hearing participant/dialogue presentation module;
3. commitment/consequence presentation module;
plus one explicit blocked fan-in owning `game/main.gd`, `game/main.tscn`, and primary integration smoke surfaces.

## Authority boundary
Factory routing only. No component is accepted, reviewed, integrated, canonicalized, released, certified, or promoted to final canon by this repair.

## Required next route
Fresh required review of the exact branch head, then squash-only integration if clean.
