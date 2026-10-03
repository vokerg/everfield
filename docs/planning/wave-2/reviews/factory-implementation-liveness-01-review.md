# Required Review — Issue #1405 / FACTORY-IMPLEMENTATION-LIVENESS-01-REV-01

## Exact subject
- producer issue: #1403
- producer terminal: comment 5968798939
- producer head: `ce875cdbb9b95291d0cf49d7874a594a41e43d8c`
- producer PR: #1404
- base: `main@4da8dcfdda4bdcd555e4b4bf637a2b5a23bf00f2`
- v7 blob: `1b443ece4bc1f3f5ed72ccd6d671b5752d71da02`
- workflow blob: `eb825762febe4124422c27da1b7dc67af2b64817`
- producer handoff blob: `43f97391b6a4bf87ae006562fac102872054243d`
- PR: draft, mergeable, exactly 3 changed paths

## Disposition
`CLEAN_FOR_PARALLEL_IMPLEMENTATION_LIVENESS_INTEGRATION`

Findings:
- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0
- informational: 1

## Adversarial review

### 1. Composition / regression boundary
PASS. v7 imports v6 and reuses existing v5 transition reconciliation plus v6 content-demand materialization. No v1–v6 source file is modified.

### 2. Integrated-source trust
PASS. Candidate sources must be trusted closed PLAN-v1 implementation producers/fan-ins, must not be factory/readiness/content/review issues, and must carry a trusted unedited schema-3 `INTEGRATION_STATUS state: DONE` with `merge_method: squash` and a valid 40-hex `main_sha`.

The actual #1343 integration terminal comment 5935663772 was independently fetched from GitHub REST during this review:
- `author_association: OWNER`;
- created_at == updated_at (`2026-10-01T16:21:56Z`);
- `merge_method: squash`;
- `main_sha: 0ad16437b9e01f5d2cbb7e5281a69c023fb985ac`.

### 3. Main ancestry
PASS. v7 verifies the integration SHA is current-main ancestor/equal via GitHub compare before accepting it as continuation authority. #1343 integration SHA compares to current main with status `ahead`, i.e. current main is ahead of and contains the integrated playable.

### 4. Empty implementation lane
PASS. New intake creation is suppressed by any open trusted implementation component, implementation review, playable fan-in, or implementation-demand intake namespace. Factory liveness repair issues themselves do not satisfy this predicate.

### 5. Dedupe / retry
PASS. Open/completed trusted `FACTORY-IMPLEMENTATION-DEMAND-<source>` consumes the source. Duplicate/not-planned closure does not consume it, permitting retry instead of permanent dead-end.

### 6. Bounded single materialization
PASS. One maintenance execution selects at most one unconsumed integrated source and creates at most one implementation-demand intake.

### 7. Parallelism semantics
PASS. Generated intake requires 2–4 pairwise-disjoint implementation component roots when concrete independent work exists, and requires a separate fan-in owning shared surfaces. This prevents the intended parallel work from collapsing into contention on `game/main.gd`.

### 8. Anti-zero liveness
PASS. Without explicit product-complete/owner authority, the intake may not close the implementation lane with `required_next_route: NONE`; when fewer than two independent roots are justified it must route bounded implementation evaluation/playtest instead.

### 9. Content + implementation concurrency
PASS. v6 content-demand materialization remains executed before the new v7 implementation-demand materialization in the same maintenance run. A content lane therefore does not serialize the implementation lane.

### 10. Workflow wiring
PASS. Workflow compiles v1–v7, executes `frontier_maintenance_v7.py --self-test`, and uses the same v7 entry point for production maintenance.

### 11. Scope
PASS. Exact diff is limited to:
- `tools/planning/frontier_maintenance_v7.py`
- `.github/workflows/planning-frontier-maintenance.yml`
- `docs/planning/handoffs/issue-1403.md`

## Validation evidence
- independent pure source-selection/dedupe reproduction: PASS;
- exact #1343 integration trust fields: PASS;
- #1343 integration-main ancestry: PASS;
- exact frozen PR/blob/path identities: PASS.

Informational limitation: this review environment's shell cannot resolve github.com, so the full repository checkout and composed v1–v7 self-test could not be run before integration. No false preintegration full-chain PASS is claimed. The integrated workflow is fail-fast: Python compile + full composed self-test run before maintenance writes.

## Integration condition
PR #1404 may be squash-integrated only if its head remains exactly `ce875cdbb9b95291d0cf49d7874a594a41e43d8c`, current main remains merge-compatible, and no newer owner directive supersedes comment `5968764259`.
