# Handoff — Issue #1373 / FACTORY-CONTENT-DEMAND-LIVENESS-01

## Scope
Restore demand-driven parallel content liveness after CONT-07 without restarting speculative automatic CONT-08-style planning.

## Implementation
- added `tools/planning/frontier_maintenance_v6.py`, composing v5 rather than modifying prior maintenance semantics;
- classifies only trusted open concrete implementation producers/review-test issues as demand sources;
- treats open content roots/intakes as satisfying the content lane;
- when the content lane is empty, selects one unconsumed implementation source and creates exactly one `FACTORY-CONTENT-DEMAND-<source>` intake;
- intake contract permits only 1–4 concrete implementation-fed content roots and explicitly permits a bounded no-op when no real demand exists;
- closed duplicate/not-planned intakes do not consume a source, while open/completed intakes do;
- factory and implementation-readiness issues are excluded as sources;
- active maintenance workflow now validates/runs v6.

## Changed paths
- `tools/planning/frontier_maintenance_v6.py`
- `.github/workflows/planning-frontier-maintenance.yml`
- `docs/planning/handoffs/issue-1373.md`

## Validation
- direct Python syntax compilation of the exact v6 source: PASS;
- deterministic v6 selection/dedupe self-test: PASS in an isolated harness;
- v6 self-test composes `v5.self_test()` in repository execution, so the deployed workflow preserves all prior v1–v5 tests before the new assertions;
- workflow YAML was inspected after edit and points both validation and execution to v6.

Local full-repository execution was unavailable because this environment cannot resolve github.com from the shell. No claim is made that GitHub Actions has executed v6 before integration.

## Behavioral examples covered by self-test
1. live first-playable producer + empty content lane -> producer selected;
2. live content root -> no intake selected;
3. completed producer intake -> producer is deduped and live implementation review may seed the next intake;
4. duplicate/not-planned intake -> does not permanently consume the source;
5. factory liveness issue -> never treated as implementation source;
6. no implementation source -> no intake.

## Authority boundary
Factory liveness only. No content root is made canonical by materialization, no implementation/review authority is granted, and automatic CONT-08 remains forbidden.

## Required next route
Fresh independent/degraded-independent review of the exact branch head before squash integration.
