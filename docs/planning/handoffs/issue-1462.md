# Issue #1462 handoff — fail-closed diagnostic contract

## Scope

Mission: `IMPLEMENTATION-DEMAND-DIAGNOSTICS-01`.

This packet extracts only the already-implemented `EF-*` diagnostic contract from the bounded first playable. It does not wire the component into `game/main.gd`, does not own UI nodes or gameplay state, and grants no integration, canon, persistence, production, release, or truth-resolution authority.

## Frozen source basis

- producer base main: `849642087297f8b8c83e5bda927aa6ce9d5ef899`
- source `game/main.gd` blob: `b96659a1cf461a96934666293aecaa565e68579b`
- canonical binding: Issue #1147 comment `5675066392`
- canonical program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`
- routing intake: #1460
- owner parallelism directive: Issue #84 comment `5968764259`

## Producer packet

- draft PR: #1472
- branch: `planning/issue-1462`
- diagnostic catalog: `game/components/diagnostics/diagnostic_catalog.gd`
- diagnostic catalog blob: `ef1165a53c0c94dc4d87247c2d41580487b6e0b5`
- isolated smoke: `game/components/diagnostics/diagnostic_catalog_smoke.gd`
- isolated smoke blob: `9dbc0371593263b217e94f8d1df4fd2d1dd12360`

The component preserves all 16 current codes and their current messages. Only `EF-INTERACT-UNKNOWN` and `EF-COMMIT-UNKNOWN` are error-classified in the existing playable; the extracted catalog preserves that distinction. Their variable station/choice text is supplied through explicit required context rather than inferred from gameplay state.

## Fail-closed behavior

The isolated smoke asserts:

1. all 16 current codes are represented;
2. exact message text and error classification are stable;
3. formatted output contains the stable code and nonempty message;
4. unknown and whitespace-only codes return a visible error payload and cannot be mistaken for a known diagnostic;
5. missing or invalid required dynamic context fails closed;
6. caller dictionaries and returned code lists cannot mutate catalog-owned state.

Static source inspection confirms the component has no scene/node ownership and no input, filesystem, network, persistence, provider, gameplay-state, or truth/canon mutation surface.

## Runtime status

Exact diagnostic smoke execution under the repository-locked Godot `4.7.1-stable` artifact is **NOT RUN by this producer environment**. The environment cannot resolve the external artifact host, so no runtime PASS is claimed.

The fresh required review/test must independently execute:

`godot --headless --path game --script res://components/diagnostics/diagnostic_catalog_smoke.gd`

under the repository-locked Godot 4.7.1 artifact and require process exit 0 plus sentinel:

`EVERFIELD_DIAGNOSTIC_CONTRACT_SMOKE_PASS`

Primary first-playable PR CI may provide import/regression evidence, but it is not a substitute for this exact component smoke.

## Required next route

Fresh independent required implementation review/test of the exact final producer head. Clean disposition, if justified:

`CLEAN_FOR_DIAGNOSTIC_COMPONENT_PUBLICATION`

Any publication remains a separate squash-only authority episode after exact-head/current-main compatibility re-derivation.
