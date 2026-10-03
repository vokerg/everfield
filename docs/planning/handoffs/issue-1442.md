# Handoff — Issue #1442 / IMPLEMENTATION-DEMAND-MOVEMENT-INTERACTION-TEST-01-REM-01

## Scope

Blocking runtime-evidence remediation only. The frozen #1413 producer movement test, runner, gameplay, and handoff bytes remain read-only.

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
- required sentinel: `EVERFIELD_MOVEMENT_INTERACTION_SMOKE_PASS`

## Verification-only paths

- `.github/workflows/verify-movement-interaction-1442.yml`
- `docs/planning/handoffs/issue-1442.md`

The workflow is temporary evidence infrastructure and has **no authority to be integrated into `main`**.

## Verification design

The workflow:
1. checks out the exact frozen producer head;
2. verifies the exact movement smoke, runner, and producer-handoff blob identities;
3. resolves the repository-reviewed Godot `4.7.1-stable` artifact lock and verifies its SHA-256;
4. executes the frozen `tools/implementation/run_godot_movement_smoke.sh` with `GODOT_BIN` bound to that exact artifact;
5. requires exit 0 and exact sentinel `EVERFIELD_MOVEMENT_INTERACTION_SMOKE_PASS`;
6. uploads engine, movement-smoke log, and run-identity evidence even on failure.

The critical runtime question is whether `Input.parse_input_event(InputEventKey)` changes the global pressed state consumed by production `Input.is_key_pressed` so the real playable `_process` path moves/clamps the player and enables proximity interaction.

## Current result

`PENDING_EXACT_RUNTIME_EVIDENCE`.

No runtime PASS is claimed by this initial handoff. After a successful primary exact-head run, update this handoff with immutable run/job/artifact evidence, then require one final-head confirmation run before terminalizing.

## Terminal routing

- PASS exact runtime evidence -> fresh required re-review of the unchanged #1413 packet; do not self-upgrade #1437.
- Runtime failure -> route the smallest bounded producer testability remediation; do not substitute direct position assignment.
- Identity/engine/evidence ambiguity -> `INVALIDATED` / bounded recovery.

## Authority boundary

Runtime evidence only. No producer mutation, test publication, gameplay semantics change, empirical accessibility certification, production/release, canonicality, or integration authority.
