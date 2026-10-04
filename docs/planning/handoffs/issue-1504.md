# Handoff — Issue #1504 / IMPLEMENTATION-DEMAND-STATION-WORLD-02

## Status and ownership
- Mission: `IMPLEMENTATION-DEMAND-STATION-WORLD-02`; producer of a new, data-only station-world component.
- Valid first owner CLAIM: #1504 comment `5978270304`, actor `frontier-drain-station-world-1504-gpt56sol-20261004-1051-01`; first-claim ownership was immediately rechecked with no competitors.
- Branch: `planning/issue-1504`, base `eef8a80d538a908ea685b206d97409ac48a2092f`.
- Source-of-truth `game/main.gd` blob `9b406cc0a0115f0818df633eda67d69ab7779a06`, following reviewed #1464/#1500 modularization.
- Owner parallelism directive: Issue #84 comment `5968764259`; routing intake #1503; binding #1147 comment `5675066392`, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.

## Exclusive changed paths
1. `game/components/station_world/station_world.gd` — source blob `87fefab8816a2ab8795c54877299716ec86b227e`.
2. `game/components/station_world/station_world_smoke.gd` — source blob `0c972e251de6e4fb1a86bbecbce757eaa56999ce`.
3. `docs/planning/handoffs/issue-1504.md` — this handoff.

No writes to sibling `traversal_policy` or `playable_presentation` roots, the live `game/main.gd` or `game/main.tscn`, existing published components, test workflows or project settings.

## Implementation contract
- Pure `RefCounted` metadata provider; no Node/scene, input, actor movement, session state, diagnostics, IO, network, persistence, provider, narrative-truth or canonical decision authority.
- `get_station_ids()`, `has_station()`, `get_station()`, `lookup_station()`, `get_stations()`, `get_layout()`, `get_contract()` are read-only metadata APIs. Invalid IDs and non-string IDs fail visibly with empty-result lookups.
- Five **exact ordered** stations `public_record`, `material_trace`, `defer_conclusion`, `commons_hearing`, `project_table` preserve current-main Vector2 positions, fallback titles/hints and RGB marker colors.
- WalkPath six points/width/color, floor polygon/color, world movement Rect2 bounds, marker polygon, original label offset/dimensions and player spawn are copied exactly.
- Every public station and layout snapshot uses deep-copy or fresh typed array values. Mutation of IDs, returned dictionaries, nested dictionaries, floor/path arrays or bounds is not allowed to corrupt shared definitions.
- Published Old Works world presentation retains authoritative inspected station text; these are *unchanged fallback metadata* only. No new map, place, story, or historical fact introduced.

## Verification and remaining independent gate
- Isolated headless entry point: `godot --headless --path game --script res://components/station_world/station_world_smoke.gd`.
- Required exact sentinel `EVERFIELD_STATION_WORLD_SMOKE_PASS` on 0 failures, else nonzero exit and explicit failure sentinel.
- Smoke independently embeds the reviewed `game/main.gd` literal fixture, checks all five IDs/order/position/color/title/hint tuples, source geometry and palette, nested snapshot immutability, typed invalid/unknown fail closure and absence of live scene/movement/truth authority.
- **Runtime status: NOT_EXECUTED in producer environment**: repository-locked Godot `4.7.1-stable` binary is not installed; acquisition is unavailable due to DNS restrictions. No exact runtime PASS, final-head workflow PASS, or any stronger review decision is claimed here. The next independent reviewer/test route must obtain exact locked-engine 4.7.1 execution evidence or register the exact bounded verifier successor before any clean review/publication.
- Reviewed engine lock: `docs/planning/wave-2/evidence/ci/engine-toolchain-artifact-lock.json`, ZIP SHA-256 `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`.
- Preserve immutable source/smoke/head/blobs after freeze. Independent required review/test must be performed by another session/actor, inspect current-main compatibility, and publish its own scoped result; producer must not self-certify.
- A draft PR is only a source/diff surface. Neither producer terminal nor review-ready grants integration, final mystery/canon, accessibility certification, production, release or persistence authority. Publication requires separate exact-head compatible squash-only authorization.

## Resume
Recheck main, binding, claimed generation, exact three paths, branch+PR frozen head, review issue, runtime gate and locked ZIP, then independently review. If locked Godot cannot be run, route exact verifier evidence rather than substitute generic PR CI or self-upgrade. Once clean, use only separately authorized noncanonical squash publication; sibling components and future shared fan-in remain blocked until their own distinct gates.
