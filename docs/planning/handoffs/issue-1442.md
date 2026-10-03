# Handoff — Issue #1442 / IMPLEMENTATION-DEMAND-MOVEMENT-INTERACTION-TEST-01-REM-01

## Scope

Blocking runtime-evidence remediation only. The frozen #1413 producer movement test, runner, gameplay, and handoff bytes remained read-only.

## Authority and activation

- ownership: Issue #1442 comment `5970904902`
- actor: `frontier-drain-movement-runtime-1442-gpt56sol-20261003-01`
- claim base main: `edae5795ff5e8fccfe08b4aaf46568230fb6b99e`
- source required review: #1437 terminal comment `5970895462`
- source disposition: `CHANGES_NEEDED`
- sole material finding: missing exact Godot 4.7.1 movement-smoke runtime evidence
- canonical binding: Issue #1147 comment `5675066392`
- canonical program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`

## Frozen producer

- producer issue: #1413
- producer terminal: comment `5970825303`
- producer PR: #1433
- exact producer head: `819afdea0452b2176cf09749b34d019fcdb49ba1`
- movement smoke blob: `f7e2d19842763857ed0403e49ee8c7ba8489b8ce`
- runner blob: `e913b8996052f6e21616d58b29cc132f2684eda5`
- producer handoff blob: `f7f8ef3bc3070eb6f96fb49824602e2e2d4fb99c`
- required PASS sentinel: `EVERFIELD_MOVEMENT_INTERACTION_SMOKE_PASS`

## Verification-only paths

- `.github/workflows/verify-movement-interaction-1442.yml`
- `docs/planning/handoffs/issue-1442.md`

The workflow is temporary evidence infrastructure and has **no authority to be integrated into `main`**.

## Verifier-infrastructure correction

Initial PR run `37135833933` reached the exact frozen producer and locked Godot artifact but failed before smoke execution because the frozen runner file is not executable in Git. The temporary workflow was corrected—without changing the frozen runner blob—to invoke that exact runner via `bash`, which is explicitly equivalent under the #1442 contract and preserves every runner check.

## Authoritative runtime evidence — FAIL

Draft verification PR: #1446.

Exact run after the verifier-only correction:
- workflow run: `37135890987`
- run number/attempt: `2 / 1`
- job: `111240223150` / `exact-movement-smoke`
- workflow conclusion: `failure`
- frozen producer checkout: `819afdea0452b2176cf09749b34d019fcdb49ba1`
- verified movement smoke blob: `f7e2d19842763857ed0403e49ee8c7ba8489b8ce`
- verified runner blob: `e913b8996052f6e21616d58b29cc132f2684eda5`
- verified producer handoff blob: `f7f8ef3bc3070eb6f96fb49824602e2e2d4fb99c`
- Godot runtime: `4.7.1.stable.official.a13da4feb`
- repository-locked Godot ZIP SHA-256: `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`
- evidence artifact: `11278573010`
- artifact digest: `sha256:705421b0ac6ef280e11823dfee0193224cb3c4da71a85d569a34014676e8866d`

Passing assertions before the movement failure:
- real `res://main.tscn` loads;
- Player and Diagnostic nodes exist;
- exact bounded start is correct;
- out-of-range interaction fails with `EF-INTERACT-RANGE`;
- unknown interaction fails closed with `EF-INTERACT-UNKNOWN`.

Failing movement/testability assertions:
1. synthetic D does not move the player right through production input;
2. synthetic W does not move the player up;
3. input-driven movement does not reach Archive Ledger radius;
4. proximity interaction therefore does not succeed;
5. the expected Archive Ledger state change does not occur;
6. negative bound-clamp assertion fails;
7. positive bound-clamp assertion fails.

The exact smoke terminates with:
`EVERFIELD_MOVEMENT_INTERACTION_SMOKE_FAIL count=7`.

This closes the evidence gap with a **runtime FAIL**, not a PASS. In this headless execution shape, the current `Input.parse_input_event(InputEventKey)` harness does not establish the global pressed-key state consumed by production `Input.is_key_pressed`.

## Required next route

Issue #1448 — `IMPLEMENTATION-DEMAND-MOVEMENT-INTERACTION-TEST-01-REM-02` — is the bounded producer-testability remediation.

It may change only the movement test/runner/handoff (plus temporary task-owned verification infrastructure if required), must keep production gameplay read-only, must not assign `player.position` directly, and must fail closed again if no supported headless mechanism can exercise the real production input path.

After successful repaired runtime evidence, route a fresh independent required review; do not self-upgrade #1437 or #1442.

## Authority boundary

Runtime evidence only. No producer publication, test publication, gameplay semantics change, empirical accessibility certification, production/release, canonicality, or integration authority.
