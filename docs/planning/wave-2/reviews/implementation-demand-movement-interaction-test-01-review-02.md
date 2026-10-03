# Required re-review — Remediated movement input test

**Issue:** #1450  
**Mission:** `IMPLEMENTATION-DEMAND-MOVEMENT-INTERACTION-TEST-01-REV-02`  
**Reviewer session:** `frontier-drain-movement-review2-1450-gpt56sol-20261003-01`  
**Disposition:** `CLEAN_FOR_REMEDIATED_MOVEMENT_INTERACTION_TEST_PUBLICATION`  
**Authority:** fresh independent required review only; no integration, gameplay-semantic, canonical, production, or release authority.

## Frozen remediation packet reviewed

- Remediation issue: #1448
- Remediation terminal: comment `5971038150`
- Remediation session: `frontier-drain-movement-testability-1448-gpt56sol-20261003-01`
- Branch/head: `planning/issue-1448` @ `decaf07d9dff81b966fde0e0bf035da6014183af`
- Draft remediation PR: #1449
- Repaired smoke blob: `4c5bd980eecd47fcc620d72f4819e3dab687d059`
- Runner blob: `e913b8996052f6e21616d58b29cc132f2684eda5`
- Remediation handoff blob: `33733e51a243b02474424e77041d5fbe0406a7f8`
- Evidence workflow blob: `ffe9311c7b9bbb60e77b05d069484f6b8586f919`
- Remediation base/current main at claim: `f7413002d69918968468d0dda292a0c3124755a6`

The exact remediation comparison contains only:

1. `.github/workflows/verify-movement-testability-1448.yml`
2. `docs/planning/handoffs/issue-1448.md`
3. `game/tests/movement_interaction_smoke.gd`
4. `tools/implementation/run_godot_movement_smoke.sh`

Production gameplay/project bytes remain:

- `game/main.gd`: `b96659a1cf461a96934666293aecaa565e68579b`
- `game/main.tscn`: `02b943321c258bb807f9496c7a270221df112b31`
- `game/project.godot`: `9da4153ed378945ef5e9634e0e5cae48289845d8`

## Prior failure and remediation delta

Exact frozen Producer #1413 failed under the repository-locked Godot 4.7.1 runtime in #1442: the real scene and fail-closed diagnostics passed, while seven movement/clamp/proximity assertions failed because synthetic key state was not visible when production `Input.is_key_pressed` was polled.

The repaired smoke is byte-for-byte identical to frozen #1413 after removing one bounded block in `_send_key`:

- `Input.flush_buffered_events()` immediately after `Input.parse_input_event(event)`;
- an assertion that `Input.is_key_pressed(keycode) == pressed` before production movement polling.

No other test behavior changed. The runner is carried byte-identically from #1413.

## Godot 4.7.1 root-cause verification

The diagnosis matches exact Godot `4.7.1-stable` source:

- `core/input/input.h` blob `6d732877efba9788ec3e769caf1901fb6891b86b` initializes `use_accumulated_input = true`;
- `core/input/input.cpp` blob `38da1c6e85ac43445ba1002143e3ebf16cce87b0` queues `parse_input_event` input when accumulation is enabled;
- the same source drains buffered events through `flush_buffered_events()` into `_parse_input_event_impl`;
- `_parse_input_event_impl` inserts/removes keyboard codes in `keys_pressed`;
- `is_key_pressed` reads `keys_pressed`.

Therefore flushing the synthetic event before directly invoking the playable's production `_process` is a test-timing repair consistent with engine semantics, not a gameplay-state substitute.

## Independent runtime-evidence check

Final exact-head workflow run `37136453216` is associated with remediation head `decaf07d9dff81b966fde0e0bf035da6014183af`.

Job `111241865360` / `exact-repaired-movement-smoke`:
- status/conclusion: `completed / success`;
- exact identity-verification step: success;
- reviewed Godot acquisition/checksum step: success;
- exact repaired movement-smoke step: success;
- evidence upload: success.

The run log independently shows:
- exact repaired smoke blob check `4c5bd980eecd47fcc620d72f4819e3dab687d059`;
- exact runner blob check `e913b8996052f6e21616d58b29cc132f2684eda5`;
- exact production `main.gd` blob check `b96659a1cf461a96934666293aecaa565e68579b`;
- locked Godot ZIP SHA-256 `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`;
- engine banner `Godot Engine v4.7.1.stable.official.a13da4feb`;
- flushed D/W/A/S pressed and released key-state assertions all PASS;
- right/up movement through production polling PASS;
- Archive Ledger proximity arrival and real `interact_nearest()` success PASS;
- negative and positive world-bound clamps PASS;
- required sentinel `EVERFIELD_MOVEMENT_INTERACTION_SMOKE_PASS`.

Artifact `11277948649` is unexpired, bound to the exact remediation head, and has digest:
`sha256:c4b3d52050658637ab88d662b0a544b91a65937277956328eefde28655a299b3`.

The same exact head also has successful existing first-playable regression run `37136453223`.

The reviewed artifact lock identifies Godot `4.7.1-stable` at the same ZIP digest. Its lock entry is explicitly TOFU/replay identity rather than vendor-signed identity; this review preserves that limitation and does not upgrade it.

## Acceptance review

1. **Buffering diagnosis / minimality — PASS.** Exact engine source supports the diagnosis, and the repaired smoke differs from frozen #1413 only by flush + key-state assertion in the synthetic-event helper.
2. **Real scene / production movement path — PASS.** The test still loads `res://main.tscn`, obtains the real Player, and invokes the existing playable `_process` while flushed keys are held.
3. **No state substitution — PASS.** The smoke never assigns `player.position` and does not mutate gameplay state to fabricate movement.
4. **Production immutability — PASS.** `main.gd`, `main.tscn`, and `project.godot` retain the declared blobs.
5. **Global key state — PASS.** The smoke explicitly checks `Input.is_key_pressed(keycode) == pressed`; final-head logs show all D/W/A/S assertions passing.
6. **Proximity interaction — PASS.** Input-driven movement reaches Archive Ledger range, then the real nearest-interaction path succeeds and records the public-record state.
7. **World bounds — PASS.** Both minimum and maximum clamps pass under input-driven movement.
8. **Fail-closed interaction — PASS.** Out-of-range and unknown-station behavior remain asserted; the exact smoke exits cleanly only after all assertions pass.
9. **Final exact-head runtime evidence — PASS.** Run/job/artifact/head/engine/blob identities are mutually consistent and the required sentinel is present.
10. **Scope / evidence workflow boundary — PASS.** Diff is exactly the four declared remediation paths. The workflow is evidence infrastructure only and creates no publication, runtime, gameplay, or canonical authority by itself.

## Findings

- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0
- informational: 0

## Disposition and route

`CLEAN_FOR_REMEDIATED_MOVEMENT_INTERACTION_TEST_PUBLICATION`

Publication is a separate current-authority decision. It must re-derive current main, exact remediation/review heads, workflow treatment, duplicate publication state, ownership, and squash-only authority immediately before integration. A clean review does not itself authorize landing the evidence workflow or any producer/remediation bytes.

## Authority boundary

This review is `NOT_CANONICAL`. It grants no gameplay-semantics mutation, fan-in acceptance, empirical accessibility certification, final canon, implementation-readiness expansion, production/release, or integration authority.
