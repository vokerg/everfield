# W2-ENG-TECH-S7-01 — broken-reference diagnosis and repair tranche

## Scope

This packet continues the independently reviewed S6 evidence line from Issue #462 without modifying S3/S4/S5/S6 provenance. It executes unchanged-v5 scenario `S7` for the lawfully materializable public candidates Bevy 0.19.0, Defold 1.13.0, and Godot 4.7.1-stable. Unity and Unreal remain `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY` under the current provider evidence.

The exact contract is eight logical assets, one injected broken reference at `ASSET-08`, candidate-native diagnosis, one bounded repair restoring only that reference, and a clean rerun. The unchanged authority remains `W2-ENG-HARNESS-v5`, `W2-ENG-FEATURE-SLICE-v2`, `W2-ENG-SCENARIO-INPUTS-v2`, and `W2-ENG-PROTOCOL-VALIDATOR-v5` blob `2c646988dc16e212f43df6a4ee5ce646622ac2a6`.

## Final empirical identity

- Final successful trigger: `0bb0596b1440759d73a7282d2daee28ef13fb560`
- Actions run: `31992873649`, attempt 1, success
- Evidence-recording commit: `5ceddbf696432cb069db5461c48c2b4e66d67121`
- Immutable artifact: `9275925526`, `w2-eng-tech-s7-01-r2-31992873649-1`
- Artifact digest: `sha256:9356f81d96c9f7804b68f9fed65f82e9b621c5076f020e64f5df570144c244da`
- Evidence SHA-256: `4900306a228e2ede28c8699b21dee15fabfc1d52a7b354938536d15fd1e25123`
- Base runner SHA-256: `7e0d152822afe79872166fa8b17dc5f3685454fd37cf1222abc04a07bf366c51`
- Bounded Godot remediation runner SHA-256: `0666779f55f002c416d05d416a64a24536d4bae7858b6480669ceb8230d480e7`

Earlier producer attempts are retained as immutable correction provenance: run `31991497890` exposed Bevy/Defold/Godot harness defects; run `31992586423` established clean Bevy/Defold evidence but retained two Godot-only producer defects. The final R2 run changes only the bounded Godot fixture type/SceneTree quit path and preserves the base runner identity.

## Candidate results

### Bevy 0.19.0

Generation `GEN-S7-544c85823f09e1a866b79c58` has two distinct cold normal workspaces plus one `FI-S7-BROKEN-REF-v2` workspace. Candidate-native `cargo check --locked --quiet` diagnoses the missing `MISSING-ASSET-08.txt` reference with exit 101; the bounded repair restores only the `ASSET-08` reference and the same path reruns cleanly. Unchanged-v5 adaptation is accepted and aggregate is `PASS_FOR_COMPARISON`, `valid_envelope=true`.

### Defold 1.13.0

Generation `GEN-S7-ec551632e42e05e85eb872e7` has two distinct cold normal workspaces plus one failure-injection workspace. Candidate-native Bob `resolve build` participates in normal diagnosis/rerun, the injected defect is exactly one `ASSET-08` reference, and the bounded repair restores only that reference. Unchanged-v5 adaptation is accepted and aggregate is `PASS_FOR_COMPARISON`, `valid_envelope=true`.

### Godot 4.7.1-stable

Generation `GEN-S7-6a86e8eb88e02c6d7c76dc18` has two distinct cold normal workspaces plus one failure-injection workspace. Candidate-native Godot 4.7.1 headless execution validates the eight-asset binding; the injected `ASSET-08` defect is mechanically attributed, repaired within the bounded reference-only scope, and rerun cleanly. Unchanged-v5 adaptation is accepted and aggregate is `PASS_FOR_COMPARISON`, `valid_envelope=true`.

## Fail-closed controls

For every represented candidate the retained packet records passing negatives for wrong broken asset, more than one broken reference, host-only diagnosis, missing diagnostic attribution, unbounded repair, rerun bypass, candidate-generation mismatch, duplicate registry reference, reused workspace/reset, source/raw substitution, and candidate-native validation bypass. Reset/workspace identities are distinct and mechanically bound to exact attempt records.

The unchanged-v5 harness self-test packet is retained in `harness-validator.json`; exact machine evidence and source/raw registries are retained under `docs/planning/wave-2/evidence/ci/engine-technical-s7/` and in the immutable Actions artifact.

## Preserved states and authority

Issue #82's historical 50 `NOT_RUN` cells remain preserved. This S7 packet does not upgrade Bevy/Defold S6, complete S1/S2/S8-S10, complete five-candidate comparison, rank or select an engine, authorize gameplay/high-throughput implementation, establish implementation/production readiness, change provider/commercial/legal/platform/release authority, grant verification-PASS, integrate itself, make a decision, or become canonical.

Producer disposition: `PARTIAL_EMPIRICAL_S7_EVIDENCE_READY_FOR_REVIEW`.

Exactly one fresh required independent/degraded-independent review must judge the exact terminal packet and attack candidate-native diagnosis authenticity, exact `ASSET-08` one-reference injection, diagnostic attribution, bounded repair and clean rerun authenticity, reset/source/toolchain/generation binding, unchanged-v5 aggregation, negative controls, blocked candidates, predecessor preservation, and authority inflation.