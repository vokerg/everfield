# Handoff — Issue #1505 / IMPLEMENTATION-DEMAND-TRAVERSAL-POLICY-02

## Status and scope

Producer is **frozen for required exact Godot verification and independent review**. Side-effect-free RefCounted movement/nearest-interaction policy and isolated smoke only. This packet must not be integrated on producer self-assessment. All shared gameplay/controller, existing movement smoke, published sibling components, canonical program, engine settings, main workflow, and other producer roots remain unmodified.

## Source, ownership and binding

- routing intake #1503; owner parallelism directive #84 comment 5968764259
- reviewed and separately squash-published playable #1464; independent required review #1500
- source main@eef8a80d538a908ea685b206d97409ac48a2092f
- immutable game/main.gd reference blob: 9b406cc0a0115f0818df633eda67d69ab7779a06
- existing movement smoke game/tests/movement_interaction_smoke.gd reference blob: 4c5bd980eecd47fcc620d72f4819e3dab687d059
- project config blob: 9da4153ed378945ef5e9634e0e5cae48289845d8
- reviewed engine artifact lock: 4a88990ae24768eb4f83a8a1311e2a830834649f
- active canonical binding Issue #1147 comment 5675066392, program blob fd4cf1119c3f86acc3af620024eea72235e81ce4, activation 87c85cecfa9a2ffa464c4b36816a138bf41441af
- winning ownership claim: Issue #1505 comment 5978271517, actor frontier-drain-traversal-policy-1505-gpt56sol-20261004-1052-a

## Exact component paths / identities

- game/components/traversal_policy/traversal_policy.gd: Git blob 8376bd1289890d084fc94992ba56c4cd64588a44
- game/components/traversal_policy/traversal_policy_smoke.gd: Git blob 3daed72928dbaecee0339e691e89403a7eaa98b2
- this handoff docs/planning/handoffs/issue-1505.md

## Pure API and parity

key_mapping() returns a fresh four-direction WASD/arrow key-pair mapping as data. It never calls Input. direction_from_intents() validates supplied intent names and boolean values, cancels opposing directions, and returns raw Vector2 intent. advance() validates finite position/direction/delta/speed/bounds; normalizes diagonal travel, honors zero-input or zero-delta immobility and source 230.0 speed, and clamps to an injected Rect2 in the same order as published main. No caller state is mutated. station_position() rejects unknown or malformed station IDs. nearest_station() uses injected metadata and explicitly injected order, checks complete nonduplicated station schemas/finite positions/radius, preserves original nearest-distance and first-tie behavior, and returns no interaction outside the radius. It contains **no station coordinate/ID registry**, avoiding competing ownership with station_world; published-five-station fixtures are smoke-only.

Source parity references: _process, _nearest_station_id in main.gd, PLAYER_SPEED=230.0, INTERACT_RADIUS=88.0, WORLD_BOUNDS=Rect2(36,90,888,414), STATIONS insertion order and existing movement smoke's diagonal/start/corner clamp/proximity/unknown cases. No new movement mechanism is authorized.

## Deterministic test contract

Run under repository-locked Godot **4.7.1-stable**, not an unrelated engine:

Godot_v4.7.1-stable_linux.x86_64 --headless --path game --script res://components/traversal_policy/traversal_policy_smoke.gd

Assert exact EVERFIELD_TRAVERSAL_POLICY_SMOKE_PASS and process exit zero; otherwise fail. The smoke contains cardinal/opposed/no-input and diagonal speed, source 230 and radius 88, both coordinate clamps, source five-station fixture, radius boundary, deterministic tie/order, malformed/unknown station ID and metadata, nonfinite and negative geometry/time/speed/radius, mutable key-mapping isolation, and injected source dictionary immutability. The published existing game/tests/movement_interaction_smoke.gd remains read-only and should also be regression-checked.

**Execution evidence:** No exact isolated runtime was executable in the current agent environment: Godot executable absent and local shell DNS cannot fetch the reviewed artifact. This producer explicitly claims **no Godot 4.7.1 smoke PASS** and **no independent clean review**. A separately owned exact-head locked-runtime verifier must obtain this evidence before any clean required review/test outcome is issued. Generic PR CI cannot substitute for the exact sentinel.

## Required next gate

1. Freeze this exact producer head and open draft PR to main, preserving exactly three owned files and the Git blob identities above.
2. Obtain a separate immutable-head verification workflow/PR that checks out this producer head, hashes source/smoke/handoff/project/engine lock, downloads the reviewed Godot 4.7.1 zip, verifies SHA-256 c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba, executes the isolated smoke and published movement smoke, saves logs and final-head artifact.
3. Only on exact PASS, create a fresh **independent required review/test** of this frozen producer; reviewer cannot be this producer actor. Require inspection of static contract and exact runtime results. Clean review disposition must be scoped to traversal-policy component publication, not live controller integration.
4. A separate eligible integration claimant must rederive source/current-main, canonical binding, owners, required review/verifier status, and permitted paths, then squash-only publish the component. Only a later fan-in after all three independent component roots are published may wire it into gameplay.

No production, release, persistence, legal/platform/provider, truth/canon, narrative causality, global readiness, scene-node, or live gameplay authority is granted.
