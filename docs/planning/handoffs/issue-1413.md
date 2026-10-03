# Handoff — Issue #1413 / IMPLEMENTATION-DEMAND-MOVEMENT-INTERACTION-TEST-01

## Identity

- issue: #1413
- mission: `IMPLEMENTATION-DEMAND-MOVEMENT-INTERACTION-TEST-01`
- task class: `IMPLEMENTATION_COMPONENT / GAMEPLAY_INPUT_INTERACTION_TEST`
- branch: `planning/issue-1413`
- ownership generation: comment `5970763632`
- actor session: `frontier-drain-movement-interaction-1413-gpt56sol-20261003-01`
- base main: `dcabab2a2f903a42ae55d6965511cf9207b0f0c6`
- active canonical binding: Issue #1147 comment `5675066392`
- canonical program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`
- canonical activation: `87c85cecfa9a2ffa464c4b36816a138bf41441af`
- canonicality: `NOT_CANONICAL`

## Frozen gameplay surface consumed read-only

Current main carries the clean-reviewed bounded first playable and remains byte-identical on the gameplay paths this task consumes:

- `game/main.gd`: `b96659a1cf461a96934666293aecaa565e68579b`
- `game/main.tscn`: `02b943321c258bb807f9496c7a270221df112b31`
- `game/project.godot`: `9da4153ed378945ef5e9634e0e5cae48289845d8`
- prior required review: #1371, clean disposition `CLEAN_FOR_BOUNDED_FIRST_PLAYABLE_INTEGRATION_REVIEW_GATE`
- integrated first-playable main provenance: `0ad16437b9e01f5d2cbb7e5281a69c023fb985ac`

No existing gameplay file or workflow was modified.

## Work produced

Only the issue-owned test surfaces were added before this handoff:

1. `game/tests/movement_interaction_smoke.gd`
   - blob: `f7e2d19842763857ed0403e49ee8c7ba8489b8ce`
   - loads the real `res://main.tscn`;
   - asserts the exact player start `Vector2(92, 286)`;
   - uses `Input.parse_input_event(InputEventKey)` press/release events for WASD;
   - invokes the existing gameplay `_process` movement path while synthetic keys are held;
   - proves movement reaches the Archive Ledger radius before calling `interact_nearest()`;
   - proves both minimum and maximum `WORLD_BOUNDS` clamps;
   - proves out-of-range and unknown-station interactions return false and expose the expected `EF-INTERACT-*` diagnostics;
   - never assigns `player.position` directly.

2. `tools/implementation/run_godot_movement_smoke.sh`
   - blob: `e913b8996052f6e21616d58b29cc132f2684eda5`
   - requires reviewed Godot `4.7.1-stable`;
   - imports the existing project headlessly;
   - executes only `res://tests/movement_interaction_smoke.gd`;
   - relies on the test process exit code and terminal marker `EVERFIELD_MOVEMENT_INTERACTION_SMOKE_PASS`.

The work head before writing this handoff was `8da987d2c8aa05829f01c2d845ce49a99c979634`. The terminal schema-3 status on Issue #1413 is the authority for the final exact branch head.

## Validation performed

Static/repository checks completed:

- the active canonical program blob on current main is exactly `fd4cf1119c3f86acc3af620024eea72235e81ce4`;
- canonical activation `87c85cecfa9a2ffa464c4b36816a138bf41441af` is an ancestor of current main;
- integrated first playable `0ad16437b9e01f5d2cbb7e5281a69c023fb985ac` is an ancestor of current main;
- branch scope contains only issue-owned paths;
- Godot 4.7 documents `Input.parse_input_event` as the API for artificially feeding input events to the game, matching the test approach;
- test code does not mutate production gameplay state to simulate movement.

Runtime movement smoke was **not executed in this connector session**: the available shell has no Godot binary and outbound DNS to GitHub is unavailable. Therefore this handoff does not claim `EVERFIELD_MOVEMENT_INTERACTION_SMOKE_PASS` or any selected-engine runtime PASS.

## Required next route

Fresh independent required review must inspect the exact frozen #1413 head and, before any publication disposition, execute the new movement smoke with the repository-locked Godot `4.7.1-stable` artifact. In particular it must prove that the synthetic `InputEventKey` path actually changes the global key state observed by the existing `Input.is_key_pressed` calls. If that runtime contract fails, the review must return `CHANGES_NEEDED` and route the smallest testability remediation rather than substituting direct position assignment.

Allowed clean review disposition remains:

`CLEAN_FOR_MOVEMENT_INTERACTION_TEST_PUBLICATION`.

Any publication is a separate squash-only integration decision and grants no gameplay semantics, accessibility, production/release, or canonical authority.
