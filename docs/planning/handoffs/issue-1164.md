# Issue #1164 handoff — CONT-02 evaluator-output remediation

## Identity

- mission: `W2-CONTENT-SYN-CONT-02-REM-01`
- ownership claim: Issue #1164 comment `5743289463`
- remediation base: `main@34df68804c6ec29f3a62b1ed8d252c26d367b862`
- active canonical binding: Issue #1147 terminal comment `5675066392`
- active canonical program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`
- source producer: Issue #1160 terminal `5743174617`, PR #1161, head `11430c00ff81f6ba2160ed78805cd2dba7b877e3`
- required review: Issue #1163 terminal `5743246705`, disposition `CHANGES_NEEDED`
- finding closed: `SYN-CONT02-REV-MAJ-01`

## Completed work

Only the two frozen synthesis artifacts were copied from exact producer #1160 and remediated.

1. Added explicit route-cardinality measurement/status output for all six reviewed structural objective contracts:
   - inherited `OBJ_CONT:COMPARE_PERSPECTIVES`;
   - inherited `OBJ_CONT:SELECT_DIRECTION`;
   - inherited `OBJ_CONT:CHOOSE_CONTINUED_GOAL`;
   - `OBJ_CONT02:COMPARE_CAUSAL_ACCOUNTS`;
   - `OBJ_CONT02:SELECT_RESPONSE_PORTFOLIO`;
   - `OBJ_CONT02:CHOOSE_CONTINUED_GOAL`.
2. Because this synthesis authors zero concrete quests and instantiates no predecessor concrete quest, every measurement is explicitly `NOT_APPLICABLE_NO_ACTIVE_CONCRETE_OBJECTIVE_INSTANCE` with `observed_active_route_count: null`; no runtime evidence or route count was fabricated.
3. Preserved every reviewed cardinality minimum and route/response/goal-family inventory, including both the #1053/#1089 `OBJ_CONT:*` contract and the packet-declared `OBJ_CONT02:*` constraints.
4. Expanded the reopen-condition inventory to the exact 17 conditions required by reviewed evaluator #1053/#1089 and classified every one as `CLEARED_IN_THIS_SYNTHESIS` with concise evidence references.
5. Preserved all five reviewed input identities, OPEN/BOUNDED_SET semantics, private-information and epistemic firewalls, relative chronology, append-only material history, relationship/legitimacy multidimensionality, foundational-play protections, consequence boundaries, WSN E3/E4/E5/E8 states, engine neutrality, and all negative authority claims.
6. Updated packet identity and downstream route to this remediation mission and one fresh required remediation review.

## Scope / non-goals

Owned paths only:

- `docs/planning/wave-2/content/content-fan-in-continuation-02.md`
- `docs/planning/wave-2/content/content-fan-in-continuation-02.yaml`
- `docs/planning/handoffs/issue-1164.md`

The #1160 producer branch and #1163 review branch are immutable provenance. This remediation does not add concrete fiction, runtime/empirical evidence, WSN upgrades, integration authority, verification-PASS, implementation readiness, gameplay implementation authority, engine selection, release/production authority, decision/final-canon authority, or canonical authority.

## Validation / self-review

Required exact-head checks before terminalization:

- branch diff contains exactly the three owned paths;
- Markdown and YAML agree on no-active-instance cardinality semantics;
- all six structural objective contracts are reported;
- all 17 reviewed evaluator reopen conditions are present and explicitly classified;
- no `TRIGGERED` condition is hidden by a clean result;
- reviewed source identities and authority boundaries remain unchanged;
- draft PR head equals the final branch head.

Self-review target: 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR.

## Next required route

After the exact remediation head is frozen and the draft PR exists, materialize exactly one fresh independent/degraded-independent remediation review mission `W2-CONTENT-SYN-CONT-02-REM-REV-01` against the immutable Issue #1164 packet. Only a clean review may grant bounded CONT-02 consumption authority. Any publication remains separately authorized and squash-only.
