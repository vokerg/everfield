# Required review — Old Works world/evidence presentation component

## Review identity
- review issue: #1416
- mission: `IMPLEMENTATION-DEMAND-OLD-WORKS-WORLD-01-REV-01`
- winning ownership generation: comment `5970316755`
- reviewer session: `frontier-drain-review-1416-gpt56sol-20261003-01`
- later competing claim: comment `5970319695` (losing by the canonical lowest-valid-comment-ID rule)
- trust mode: `DEGRADED_SINGLE_AGENT`
- review base/current main: `848acba1bba430170265b56d3f2de71b3268b7df`
- canonical binding: Issue #1147 comment `5675066392`
- canonical program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`
- canonical activation: `87c85cecfa9a2ffa464c4b36816a138bf41441af`

## Frozen producer
- producer issue: #1410
- ownership generation: comment `5969135749`
- terminal: comment `5969178423`
- producer session: `frontier-drain-old-works-world-1410-gpt56sol-20261003-01`
- branch: `planning/issue-1410`
- exact head: `20284fa9171d1d6f91e3e930d627f587062485cb`
- draft PR: #1415
- component blob: `8e498156bb9a5413f53a84b14fc279c4be6c8f23`
- smoke blob: `a69e4c93960cf459544d42a160cc532d03401e5d`
- producer base: `848acba1bba430170265b56d3f2de71b3268b7df`

The producer head is frozen and this review did not mutate it.

## Reviewed source packet
Current main contains the exact clean-reviewed content consumed by the component:
- `docs/planning/wave-2/content/demand/old-works-world-evidence-01.md` blob `d2140477a3107319ea47335402289e922d1e225b`;
- `docs/planning/wave-2/content/demand/old-works-world-evidence-01.yaml` blob `f80299d04765aa68c8516d4c458372f356ad3bc8`;
- required content Review #1383 terminal `5927436241`, disposition `CLEAN_FOR_BOUNDED_OLD_WORKS_PRESENTATION_CONSUMPTION`, zero BLOCKER / MAJOR / correction-requiring MINOR;
- Review #1383 provenance publication `5927510024`.

## Diff hygiene
Compare `848acba1bba430170265b56d3f2de71b3268b7df...20284fa9171d1d6f91e3e930d627f587062485cb` is ahead by exactly three commits and changes exactly:
1. `game/components/old_works_world/old_works_world_presentation.gd`;
2. `game/components/old_works_world/old_works_world_presentation_smoke.gd`;
3. `docs/planning/handoffs/issue-1410.md`.

No shared gameplay, project, workflow, or sibling component path is changed.

## Objective results

### 1. Exact implementation-facing IDs and text — PASS
The component `STRINGS` table matches the reviewed #1378/#1383 packet for the world title/subtitle/entry/route cue, Archive Ledger strings, Material Trace strings, explicit truth-deferral strings, and all six bounded environmental cues. No extra player-facing Old Works content contract is introduced.

### 2. Fragmentation mystery state — PASS
The component binds `MYS:FRAGMENTATION-CAUSE` to `UNKNOWN_BY_DESIGN` and exposes the same state from `get_contract()` without any truth-resolution mutation.

### 3. Both fragmentation accounts remain claims with zero truth effect — PASS
`CLM:FRAGMENTATION-ACCOUNT-A` and `CLM:FRAGMENTATION-ACCOUNT-B` are each mapped to truth effect `NONE`. Archive prose preserves accounts-as-accounts, not findings.

### 4. Public record does not reveal private provenance gap — PASS
The private identifier is retained only as a non-player-facing guard constant; `public_record_exposes_private_information` is false, and no Archive Ledger string reveals `INFO:anwen_contested_record_provenance_gap`.

### 5. Material Trace remains bounded and non-discriminating — PASS
The reviewed trace language is copied exactly. The contract sets `material_trace_may_select_causal_winner`, `record_count_is_truth_strength`, and `visual_difference_alone_proves_independence` to false.

### 6. Explicit truth deferral remains legal and nonfailure — PASS
The `defer_conclusion` station is `EXPLICIT_LEGAL_TRUTH_DEFERRAL`; `truth_deferral_is_legal` is true.

### 7. Presentation-only authority boundary — PASS
The component extends `RefCounted`, exposes lookup/contract data only, and sets `presentation_mutates_game_state` and `presentation_grants_canonical_authority` to false.

### 8. Unknown IDs and stations fail closed visibly — PASS by exact code inspection; runtime exercise is covered by objective 9
Unknown text IDs call `push_error` and return `""`. Unknown station IDs call `push_error` and return an empty dictionary. The exact component smoke asserts both paths.

### 9. Exact Godot 4.7.1 component smoke — CHANGES_NEEDED
This mandatory runtime gate lacks authoritative PASS evidence.

Available evidence:
- producer terminal `5969178423` explicitly records `godot_4_7_1_runtime_smoke: NOT_RUN_ENVIRONMENT_DNS_LIMIT` and `runtime_pass_claimed: false`;
- GitHub Actions run `37123032451` checked out exact producer head `20284fa9171d1d6f91e3e930d627f587062485cb`;
- job `111202747529` acquired the repository-locked Godot `4.7.1-stable` artifact, reported engine `4.7.1.stable.official.a13da4feb`, imported the project successfully, and completed the existing first-playable smoke with `EVERFIELD_SMOKE_PASS`;
- the workflow invokes `tools/implementation/run_godot_smoke.sh`, not `res://components/old_works_world/old_works_world_presentation_smoke.gd`;
- therefore run `37123032451` cannot be substituted for the required sentinel `EVERFIELD_OLD_WORKS_WORLD_PRESENTATION_SMOKE_PASS`.

The reviewer runtime has no Godot executable/cache and outbound DNS is unavailable, so the locked engine artifact could not be reacquired locally. That limitation does not prove a producer-code defect, but it cannot satisfy a mandatory runtime acceptance gate.

**Finding R-01 — MAJOR (acceptance-evidence gate):** exact component-smoke PASS is absent. Clean publication is forbidden until an authoritative exact-head Godot 4.7.1 run exits 0 and emits `EVERFIELD_OLD_WORKS_WORLD_PRESENTATION_SMOKE_PASS`.

### 10. Exact producer path scope — PASS
The frozen producer compare contains exactly the three declared producer-owned paths and no forbidden shared path.

## Findings
- BLOCKER: 0
- MAJOR: 1
- correction-requiring MINOR: 0
- informational: 0

The sole material finding is missing required runtime PASS evidence. No static content-contract or component-code defect was found.

## Disposition
`CHANGES_NEEDED`

This is narrowly evidence-gated. It does not authorize edits to the frozen producer packet and does not assert that the component is runtime-defective.

The single remediation successor is Issue #1421 / `IMPLEMENTATION-DEMAND-OLD-WORKS-WORLD-01-REM-01`. It must bind the exact frozen producer head and blobs, execute the dedicated component smoke under the repository-locked Godot 4.7.1 artifact, and retain immutable run/log evidence. A PASS returns to a **fresh required review**; it does not self-upgrade this review.

No integration, component publication, final canon, live-scene integration, truth resolution, production/release, empirical accessibility certification, or canonical authority is granted.
