# Handoff — Issue #1448 / IMPLEMENTATION-DEMAND-MOVEMENT-INTERACTION-TEST-01-REM-02

## Identity

- issue: #1448
- mission: `IMPLEMENTATION-DEMAND-MOVEMENT-INTERACTION-TEST-01-REM-02`
- task class: `BLOCKING_REMEDIATION / HEADLESS_INPUT_TESTABILITY`
- branch: `planning/issue-1448`
- ownership generation: comment `5970962260`
- actor session: `frontier-drain-movement-testability-1448-gpt56sol-20261003-01`
- base main: `f7413002d69918968468d0dda292a0c3124755a6`
- canonical binding: Issue #1147 comment `5675066392`
- canonical program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`
- canonicality: `NOT_CANONICAL`

## Source failure

Required Review #1437 terminalized `CHANGES_NEEDED` in comment `5970895462` because exact movement runtime evidence was missing.

Runtime-evidence remediation #1442 then executed frozen Producer #1413 under repository-locked Godot `4.7.1.stable.official.a13da4feb`:

- run: `37135890987`
- job: `111240223150`
- artifact: `11278573010`
- artifact digest: `sha256:705421b0ac6ef280e11823dfee0193224cb3c4da71a85d569a34014676e8866d`
- exact frozen producer head: `819afdea0452b2176cf09749b34d019fcdb49ba1`
- result: `EVERFIELD_MOVEMENT_INTERACTION_SMOKE_FAIL`
- movement-related failures: 7

Scene loading and fail-closed interaction diagnostics passed; all movement/clamp/proximity assertions failed because the synthetic key events were not visible to the production `Input.is_key_pressed` polling path at the time `game._process` was invoked.

## Root cause and bounded remediation

Godot 4.7.1 source establishes:

- `core/input/input.h`: `use_accumulated_input = true` by default;
- `Input::parse_input_event`: with accumulated input enabled, the event is queued in `buffered_events`;
- `Input::flush_buffered_events`: drains that queue through `_parse_input_event_impl`;
- `_parse_input_event_impl`: updates `keys_pressed`, which is the state read by `Input.is_key_pressed`.

Frozen #1413 called `Input.parse_input_event` and immediately invoked production `_process` in the same frame, before the buffered key event was flushed.

The remediation changes only the testability surface:

- `game/tests/movement_interaction_smoke.gd`
  - repaired blob: `4c5bd980eecd47fcc620d72f4819e3dab687d059`;
  - calls `Input.flush_buffered_events()` immediately after each synthetic key event;
  - explicitly asserts `Input.is_key_pressed(keycode) == pressed` after the flush;
  - retains the real `res://main.tscn`, Player node, production `_process`, both world-bound clamps, real proximity interaction, and fail-closed diagnostics;
  - never assigns `player.position` directly.
- `tools/implementation/run_godot_movement_smoke.sh`
  - blob: `e913b8996052f6e21616d58b29cc132f2684eda5`;
  - carried byte-identically from frozen #1413;
  - still runs Godot with `--headless` and enforces `4.7.1-stable`.

Production gameplay remains read-only and byte-identical to the bounded first playable:

- `game/main.gd`: `b96659a1cf461a96934666293aecaa565e68579b`
- `game/main.tscn`: `02b943321c258bb807f9496c7a270221df112b31`
- `game/project.godot`: `9da4153ed378945ef5e9634e0e5cae48289845d8`

## Runtime validation

A task-owned temporary verification workflow is included only to execute this exact repaired packet against the repository-locked Godot 4.7.1 artifact and retain immutable run evidence.

Required terminal evidence:

- exact repaired test blob `4c5bd980eecd47fcc620d72f4819e3dab687d059`;
- runner blob `e913b8996052f6e21616d58b29cc132f2684eda5`;
- production `main.gd` blob `b96659a1cf461a96934666293aecaa565e68579b`;
- reviewed Godot ZIP SHA-256 `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`;
- exit success;
- sentinel `EVERFIELD_MOVEMENT_INTERACTION_SMOKE_PASS`.

Runtime disposition is pending the CI execution at the time of this handoff version. The issue terminal status must bind the final exact branch head and immutable run/job/artifact identity.

## Required next route

If the exact repaired smoke passes, materialize a fresh independent required review of the exact #1448 packet. Do not self-upgrade Review #1437 or runtime remediation #1442.

If it fails, fail closed and route only the smallest further testability remediation permitted by the observed evidence. No gameplay seam or semantics mutation is authorized here.
