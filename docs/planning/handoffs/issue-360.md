# Issue #360 handoff — W2-ENG-TECH-S4-01

## Terminal route

`PARTIAL_EMPIRICAL_S4_EVIDENCE_READY_FOR_REVIEW`

“Partial” is relative to the five-candidate/ten-scenario W2-ENG comparison, not to the bounded public-toolchain S4 tranche: all three lawfully executable public candidates (Bevy, Defold, Godot) completed the exact S4 tranche in the terminal run. Unity and Unreal remain exact authority-bound `NOT_RUN` cells.

Fresh independent/degraded-independent review of this exact packet is mandatory before any S4 cell becomes trusted comparison evidence.

## Ownership and source

- Issue #360; winning claim `5305479805`.
- Branch `planning/issue-360`, base `main@c043c47acfa3212ca08e87725b25e47a20e8e5e6`.
- Canonical binding: Issue #6 comment `5245368879`, Planning Program blob `e3120ec203c4156328770aa86c12fbb7187966dc`.
- Owner sequencing directive: `5303081124`.
- Historical engine source: Issue #82 terminal `5276916603`; 50 historical `NOT_RUN` cells preserved unchanged.
- Reviewed S3 provenance: Issue #358 terminal `5305399666`, separately published on `main@c043c47acfa3212ca08e87725b25e47a20e8e5e6`.

## Producer packet

- Runner: `tools/planning/engine_technical_s4_probe.py`.
- Workflow: `.github/workflows/w2-eng-technical-s4.yml`.
- Evidence report: `docs/planning/wave-2/evidence/engine-technical-s4-tranche.md`.
- Machine evidence: `docs/planning/wave-2/evidence/ci/engine-technical-s4/`.
- Unchanged validator: `docs/planning/wave-2/evidence/engine-spike-protocol-fixtures.py`, `W2-ENG-HARNESS-v5` / `W2-ENG-SCENARIO-INPUTS-v2`.

### Failed/remediated producer history retained

Run `31924017117` exposed a Bevy retained-lock root-package identity mismatch. Its generated evidence commit `65f1de17944e76a2bf17692fc89aa5ef8a59e288` and artifact `9257269494` (`sha256:0370b34c16abe68f5b1ea21abf0fc43e19517268f2c3e7831b2ab10ffd45b1b2`) remain immutable branch/run provenance. No Bevy evidence from that run is promoted.

Remediation commit `c6f274f53bc14b2eb4a1da540b82994dbbdef75b` binds the temporary Bevy package/binary name to the unchanged retained lock’s root identity `everfield_bevy_probe`.

### Terminal empirical run

- trigger SHA: `c6f274f53bc14b2eb4a1da540b82994dbbdef75b`
- Actions run: `31924179133`, attempt 1, conclusion `success`
- generated evidence commit: `9a15af3895c8a0c053bf2666463910b659769121`
- artifact: `9257331215`, `w2-eng-tech-s4-01-31924179133-1`
- artifact digest: `sha256:3271072d2e75b135265bbdcd162cd9f9b4e130345e05c5c3dc3c137de0c28291`
- `evidence.json` SHA-256: `8ba3922733c4051f798dab002de4cf607f6176ffe3f66d3e85a2568473967453`

The exact terminal run has producer dispositions `PROVISIONAL_S4_PASS_FOR_COMPARISON_PENDING_REQUIRED_REVIEW` for Bevy, Defold, and Godot. Each has N1/N2/FI1 `PASS`, unchanged-v5 adaptation `ACCEPT`, and unchanged-v5 aggregate exactly `PASS_FOR_COMPARISON` with `valid_envelope=true`.

Unity and Unreal Engine remain `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY`.

## Review boundary

Reviewer must independently attack exact packet identity, first-run defect/remediation provenance, actual engine-process execution, common save semantics, v1 round-trip, v1→v2 explicit migration/default, v2 replay stability, malformed tuple diagnostics, toolchain/lock acquisition, workspace/reset independence, source binding, unchanged-v5 validation/aggregation, negative tests, authority-bound cells, historical/S3 provenance preservation, and authority inflation.

A clean review may trust only the exact executed S4 cells. It cannot complete S1/S2/S5-S10, Unity/Unreal, five-candidate comparison, engine ranking/selection, implementation/readiness, provider/legal/platform/release authority, verification-PASS, decision, canonical, or integration authority.

## Integration

No integration authority is granted by this producer handoff. The producer branch must remain unintegrated until the required review terminalizes and repository authority is re-derived separately. Any eventual integration into `main` must be squash-only.
