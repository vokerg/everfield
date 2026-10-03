# Required Review — Issue #1437 / Movement and Proximity Interaction Coverage

## Disposition

**CHANGES_NEEDED**

Findings: **0 BLOCKER / 1 MAJOR / 0 correction-requiring MINOR / 0 informational**.

This review judges only the frozen producer packet from Issue #1413 at head `819afdea0452b2176cf09749b34d019fcdb49ba1`. It does not mutate producer or gameplay bytes and grants no publication or integration authority.

## Frozen producer identity

- producer issue: #1413
- producer terminal: comment `5970825303`
- producer branch: `planning/issue-1413`
- exact producer head: `819afdea0452b2176cf09749b34d019fcdb49ba1`
- producer PR: #1433
- movement smoke blob: `f7e2d19842763857ed0403e49ee8c7ba8489b8ce`
- runner blob: `e913b8996052f6e21616d58b29cc132f2684eda5`
- producer handoff blob: `f7f8ef3bc3070eb6f96fb49824602e2e2d4fb99c`
- producer base: `dcabab2a2f903a42ae55d6965511cf9207b0f0c6`
- active canonical binding: Issue #1147 comment `5675066392`
- canonical program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`

The producer diff is exactly the three issue-owned paths:

1. `game/tests/movement_interaction_smoke.gd`
2. `tools/implementation/run_godot_movement_smoke.sh`
3. `docs/planning/handoffs/issue-1413.md`

No gameplay, project, workflow, or sibling-component path is changed.

## Review result

### Static acceptance checks

1. **PASS — real scene / bounded start.** The smoke loads `res://main.tscn`, instantiates the real playable, obtains `Player`, and requires the exact start `Vector2(92, 286)`.
2. **NOT PROVEN — synthetic input reaches production polling in headless runtime.** The test correctly constructs `InputEventKey` press/release events and sends them through `Input.parse_input_event`, then invokes the production `_process` path while the keys should be held. Static inspection cannot establish that the repository-locked headless Godot 4.7.1 runtime updates the global key state observed by production `Input.is_key_pressed`.
3. **PASS — no direct movement substitution.** The smoke never assigns `player.position` and does not call a producer-side state mutation to simulate movement.
4. **PASS STATIC / RUNTIME DEPENDENT — world-bound clamps.** Minimum `Vector2(36, 90)` and maximum `Vector2(924, 504)` are asserted after long-duration input-driven movement. The assertions are correctly bound to the real `WORLD_BOUNDS`, but executable proof depends on item 2.
5. **PASS STATIC — out-of-range interaction.** After reset, `interact_nearest()` must return false and the diagnostic must begin `[EF-INTERACT-RANGE]`.
6. **PASS STATIC / RUNTIME DEPENDENT — input-driven in-range interaction.** The test requires D+W movement to reach the Archive Ledger radius before calling `interact_nearest()`, then requires `record_read == true`. It does not reposition the player directly; executable proof depends on item 2.
7. **PASS STATIC — unknown interaction fails closed.** `interact_with("unknown_station")` must return false and emit `[EF-INTERACT-UNKNOWN]`.
8. **MISSING REQUIRED EVIDENCE — exact Godot 4.7.1 smoke.** The producer explicitly records that the new movement smoke was not executed because its environment lacked a Godot binary/network access. Successful existing first-playable regression run `37135032100` executes the existing regression surface and is not evidence that `res://tests/movement_interaction_smoke.gd` exits 0 or emits `EVERFIELD_MOVEMENT_INTERACTION_SMOKE_PASS`.
9. **PASS — exact scope.** The producer comparison contains exactly the three owned paths above.

Current-main drift observed during review does not change the frozen producer bytes or the consumed gameplay contract: `game/main.gd` remains blob `b96659a1cf461a96934666293aecaa565e68579b`, and the producer comparison remains limited to its three owned paths.

## MAJOR-01 — Exact movement runtime gate is unproven

The required review contract makes execution of the exact new movement smoke under repository-locked Godot `4.7.1-stable` mandatory. No authoritative run currently proves:

- that `Input.parse_input_event(InputEventKey)` changes the global pressed-key state observed by the playable's `Input.is_key_pressed` polling under headless Godot 4.7.1;
- that the resulting production `_process` movement reaches the expected positions and both clamps;
- that the real proximity interaction succeeds only after input-driven movement;
- that the process exits successfully and emits `EVERFIELD_MOVEMENT_INTERACTION_SMOKE_PASS`.

The reviewer environment also has no Godot executable, so this gap cannot be converted into a runtime PASS locally. This is an evidence deficiency, not a finding that the static implementation is wrong.

**Required correction:** obtain immutable exact-head runtime evidence. Do not replace input-path testing with direct position assignment.

## Required next route

Route a bounded blocking remediation:

`IMPLEMENTATION-DEMAND-MOVEMENT-INTERACTION-TEST-01-REM-01`

That remediation must keep the frozen #1413 producer read-only and may add only verification evidence infrastructure sufficient to:

1. check out exact producer head `819afdea0452b2176cf09749b34d019fcdb49ba1`;
2. verify the three frozen producer blob identities above;
3. verify the repository-locked Godot 4.7.1 artifact identity;
4. execute the exact movement smoke (preferably through the frozen runner with the locked binary);
5. require exit code 0 and sentinel `EVERFIELD_MOVEMENT_INTERACTION_SMOKE_PASS`;
6. retain immutable run/job/log or artifact evidence.

If the exact smoke passes, route a **fresh required re-review** of the unchanged #1413 packet; this review must not self-upgrade. If the smoke fails, route the smallest testability remediation consistent with the producer contract, still without substituting direct position mutation.

## Authority boundary

This review is `NOT_CANONICAL`. It grants no producer publication, gameplay semantics change, accessibility certification, implementation-readiness expansion, production/release, final-canon, or integration authority.
