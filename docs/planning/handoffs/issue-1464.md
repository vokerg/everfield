# Handoff — Issue #1464 / IMPLEMENTATION-INCREMENT-PLAYABLE-MODULARIZATION-01

## State and ownership

- State: implementation candidate prepared; **required independent implementation review and exact final-head Godot 4.7.1 smoke remain gates**.
- Claim: schema-3 Issue #1464 comment `5978160714`, actor `frontier-drain-playable-modularization-1464-gpt56sol-20261004-1035-01`, no competing claim at immediate contention re-check.
- Task branch: `planning/issue-1464`, from `main@531911fbdbd84ab1cc749b9f46b6fcaf87200718`.
- Canonical binding unchanged: Issue #1147 terminal `5675066392`, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation `87c85cecfa9a2ffa464c4b36816a138bf41441af`.

## Verified prerequisite chains, separate publication

- Old Works/Commons/consequence presentation fan-in #1414 and clean required review #1471: accepted presentation unchanged.
- Bounded transient session component: #1461 clean independent re-review #1485, separately squash-published by #1461 at `61756a44efc8bb1af775cdf8196caf14d145d211`; source `game/components/session_state/session_state.gd` unchanged.
- Diagnostic component: original #1462 and Review #1475 remain `CHANGES_NEEDED`. The corrected successor **#1481** passed exact runtime Verification #1487 and required independent Re-review **#1490**, `CLEAN_FOR_DIAGNOSTIC_CONTRACT_PUBLICATION`, separately squash-published at `63f7cde7bf4b0002cd2ea337f723b51998da99e9`. No original producer clean status is inferred.
- HUD objective model: #1463 exact runtime Verification #1493, fresh independent required Re-review #1496 `CLEAN_FOR_HUD_OBJECTIVE_COMPONENT_PUBLICATION`, separately squash-published at `21ce89e3b06ecced527abbb7a253e8b069ce4b00`; review provenance subsequently published by `531911fbdbd84ab1cc749b9f46b6fcaf87200718`.

## Scope of implementation

Only issue-owned shared-playable paths are changed:
1. `game/main.gd`: instantiate the three *published* components and delegate all bounded session state writes/history, 16 `EF-*` catalog lookups, and HUD phase/objective/status to their reviewed interfaces.
2. `game/smoke_test.gd`: retain both complete playable loops and reviewed presentation assertions; add live integration, snapshot-isolation, error classification and malformed-state fail-closed assertions.
3. `.github/workflows/godot-first-playable-smoke.yml`: hash-locked repository Godot 4.7.1; require primary playable smoke, input movement/proximity smoke, and three separately published component smoke scripts, including exact PASS sentinels.
4. `docs/implementation/first-playable.md`: describe noncanonical modularization and five-scope executable evidence.
5. `docs/planning/handoffs/issue-1464.md`: this continuation artifact.

No changes to `game/main.tscn`, component source/smoke, sibling presentation components, `game/project.godot`, reviewed engine lock, or provider/canonical artifacts.

## Invariants and exact expected evidence

- Primary sentinel `EVERFIELD_SMOKE_PASS`.
- Input/proximity sentinel `EVERFIELD_MOVEMENT_INTERACTION_SMOKE_PASS`.
- Session sentinel `EVERFIELD_SESSION_STATE_SMOKE_PASS`.
- Diagnostic sentinel `EVERFIELD_DIAGNOSTIC_CONTRACT_SMOKE_PASS`.
- HUD sentinel `EVERFIELD_HUD_OBJECTIVE_MODEL_SMOKE_PASS`.
- Reviewed Godot `4.7.1-stable` ZIP SHA-256 `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`.
- Public record/material trace/repair pilot and public record/explicit truth deferral/records-first both remain complete. Deferred public commitment remains noncomplete/reopenable and recorded; unknown and out-of-range interactions visibly fail; `UNKNOWN_BY_DESIGN` is never promoted or fabricated.
- All existing reviewed Old Works / Commons / consequence presentation text assertions remain in primary smoke.
- Runtime evidence is **not** preclaimed by source or this handoff. The GitHub Actions result for the final frozen PR head must be confirmed, with exact run/job/log/artifact and all sentinels. If it fails, remediate within owned paths, refreeze and rerun. If the exact engine cannot be executed, report missing evidence and route a blocking verification successor; never assume PASS.

## Review and integration gates

Open an **exact-head draft PR** before publishing terminal schema-3 `STATUS(REVIEW_READY)`. Freeze component-subject and shared file identities, materialize fresh **independent required implementation review/test**. Allowed clean review result: `CLEAN_FOR_PLAYABLE_MODULARIZATION_INCREMENT_INTEGRATION`. Independent reviewer must inspect exact diff, current-main compatibility and final-head CI evidence. This producer does **not** claim clean review, authority to merge, gameplay production-readiness, persistent state, final canon/truth, empirical accessibility, provider/legal/certification or release authority. All accepted integration into `main` remains **separate, explicitly authorized squash-only**.

## Continuation

Confirm exact PR/head after the handoff is frozen, inspect head-locked GitHub Actions status and logs/artifacts, and publish terminal GitHub schema-3 `STATUS(REVIEW_READY)` bound to the exact branch head/PR only when the packet and the required next review are materialized. If review finds a defect, use a bounded correction without mutating the reviewed components. No optional review may replace the required independent review.
