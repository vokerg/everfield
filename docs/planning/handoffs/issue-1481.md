# Issue #1481 Handoff — Current-Main Diagnostic Contract Reconciliation

## Status

Bounded remediation packet frozen pending exact isolated runtime verification. This issue reconciles the diagnostic component with current `main`; it does not publish or wire the component.

## Authority and source

- mission: `IMPLEMENTATION-DEMAND-DIAGNOSTICS-01-REM-02`
- owner claim: Issue #1481 comment `5972715795`
- source Review #1475 terminal: `5972609153` / `CHANGES_NEEDED`
- source review provenance publication: `5972665885`
- predecessor Producer #1462 terminal: `5972513046`
- predecessor exact head: `8e18b0093743ae8c9b1e77f97554b773f6355a4a`
- remediation base/current main: `16cceaf5a8d861daf8422a26024a00fb668a453b`
- current `game/main.gd` blob: `4ea6ab02de1fa8bfde2d976b0f3f551dc8f40b97`
- canonical binding: Issue #1147 comment `5675066392`
- canonical program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`

## Exact remediation

The predecessor catalog/smoke were structurally correct against their frozen source. Current main changed exactly two presentation-aware diagnostic messages after #1414 publication:

- `EF-INVESTIGATE-RECORD` -> `Reviewed Archive Ledger presentation; competing accounts remain claims, not findings.`
- `EF-INVESTIGATE-TRACE` -> `Reviewed Material Trace presentation; alteration evidence does not select a causal winner.`

This remediation changes only those two message expectations in:

- `game/components/diagnostics/diagnostic_catalog.gd`
- `game/components/diagnostics/diagnostic_catalog_smoke.gd`

No new diagnostic codes, gameplay behavior, error classifications, or dynamic-context behavior are introduced.

## Frozen revised identities

- revised catalog blob: `f37d93783dd9d206ba6d7a4bd050c9ff8c3ad1b3`
- revised smoke blob: `dd73c221d6764d734f630c0bef389c22eaa0d133`

Static current-main parity check:

- current diagnostic code count: 16
- revised ordered code count: 16
- code ordering parity: PASS
- message-template parity: PASS for all 16
- error-classification parity: PASS for all 16
- current error codes remain only `EF-INTERACT-UNKNOWN` and `EF-COMMIT-UNKNOWN`
- changed current-main messages: exactly the two codes named above

The component remains pure `RefCounted` observability infrastructure with no scene/input/filesystem/network/persistence/gameplay-state/truth/canon effect.

## Runtime evidence state

Exact isolated runtime evidence is still required:

`godot --headless --path game --script res://components/diagnostics/diagnostic_catalog_smoke.gd`

Required sentinel:

`EVERFIELD_DIAGNOSTIC_CONTRACT_SMOKE_PASS`

This code-remediation issue owns no workflow path, so it does not create verification infrastructure itself. After the exact remediation head is frozen, a dedicated verification-only successor must execute the smoke under the repository-reviewed Godot `4.7.1-stable` artifact and retain immutable run/job/artifact evidence.

Ordinary repository PR regression CI may establish import/first-playable regression health but is not a substitute for this exact isolated smoke.

## Forward route

1. freeze an exact-head draft PR containing only the two diagnostic files plus this handoff;
2. retain ordinary repository regression evidence if it runs;
3. materialize a dedicated verification-only successor bound to the exact revised head/blobs;
4. after exact isolated runtime PASS, require a fresh independent review of the revised packet;
5. only a later separately authorized squash publication may publish a clean-reviewed exact packet.

No publication, live-gameplay integration, persistence/save-load, truth/canon resolution, accessibility certification, production/release, provider/legal, or final-canon authority is granted.
