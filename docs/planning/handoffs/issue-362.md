# Issue #362 handoff — W2-ENG-TECH-S4-REV-01

## Terminal disposition

`CHANGES_NEEDED`

Review mode: `DEGRADED_SINGLE_AGENT`.

Finding count: **0 BLOCKER / 3 MAJOR / 0 MINOR**.

Judged Issue #360 / PR #361 remains immutable producer provenance. No Bevy, Defold, or Godot S4 cell is upgraded to trusted W2-ENG comparison evidence by this review.

## Frozen judged identities

- Review base main: `c043c47acfa3212ca08e87725b25e47a20e8e5e6`.
- Canonical binding: Issue #6 comment `5245368879`, Planning Program blob `e3120ec203c4156328770aa86c12fbb7187966dc`.
- Producer terminal: Issue #360 comment `5305536469`.
- Producer branch/head: `planning/issue-360@942a8c05032c1506730f52e897496172fb56fcf3`.
- Producer draft PR: #361.
- Terminal producer run: `31924179133`, attempt 1.
- Terminal generated evidence commit: `9a15af3895c8a0c053bf2666463910b659769121`.
- Terminal artifact: `9257331215`, digest `sha256:3271072d2e75b135265bbdcd162cd9f9b4e130345e05c5c3dc3c137de0c28291`.
- Terminal `evidence.json`: `sha256:8ba3922733c4051f798dab002de4cf607f6176ffe3f66d3e85a2568473967453`.
- Initial Bevy-defect run: `31924017117`, artifact `9257269494`, generated evidence commit `65f1de17944e76a2bf17692fc89aa5ef8a59e288`.
- Bounded producer remediation: `c6f274f53bc14b2eb4a1da540b82994dbbdef75b`.

The terminal artifact was independently downloaded during review; the ZIP and extracted evidence hashes matched the frozen packet.

## Findings

### M01 — reset truth is asserted, not derived

`attempt_record()` hashes only the absolute workspace path and then sets `reset_verified=true` unconditionally. The unchanged v5 generation directly consumes that boolean. The synthetic reused-workspace negative does not prove real reconstruction/reset.

Defold also uses static native `sys.get_save_file("everfield_s4", ...)` slots outside the copied per-attempt bundle, so distinct copied workspaces do not establish isolated candidate-native state roots.

Required remediation: mechanically derive reset truth from retained reconstruction/cleanup/state-root evidence and isolate or prove reset candidate-native state for every N1/N2/FI1.

### M02 — source binding is not fail-closed

The producer computes v5 `va()`/`agg()` before constructing `source_bindings`. The workflow verifies only equality of registry-ref key sets. The named source-substitution negative merely compares two locally computed fixture hashes; it does not mutate a raw/formal source binding and prove the candidate can no longer be represented as trusted PASS.

Required remediation: add an external fail-closed source-binding layer that binds every formal attempt to immutable raw process/result/fixture/output/toolchain/reset/run/artifact evidence before representing unchanged-v5 PASS, with true substitution negatives.

### M03 — work/generation identity omits exact toolchain/build/source identity

The producer's work id is based on candidate, label, workspace/reset ids and process-command digests; generation id derives from work id + candidate. Exact candidate binary/content, build/lock, validator, Actions run/artifact, and raw source-evidence identities are not in that derivation. Random tempfile paths influence identity while candidate content substitution at the same command path need not.

Required remediation: deterministically bind formal work/generation identity to exact candidate version/content/binary, build/lock, harness/validator, scenario/adaptation, run/artifact/source-evidence, and mechanically derived reset identities; add toolchain/binary/source substitution negatives.

## Retained positive producer observations

- The terminal artifact and evidence identities are coherent.
- The first-run Bevy defect is retained and not promoted.
- Real Bevy, Defold, and Godot processes executed and returned the expected bounded normal/injection markers.
- Common fixture/output digests are internally coherent.
- Unity and Unreal remain `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY`.
- Historical Issue #82 cells and reviewed S3 provenance remain unchanged.

These facts remain producer provenance only until a remediation packet and fresh required review close M01–M03.

## Next route

Exactly one bounded fresh remediation successor is required. Do not edit `planning/issue-360`, PR #361, or this review branch.

Because M01 lacks retained proof of candidate-native reset isolation, remediation should perform a fresh S4 empirical rerun rather than merely relabel the terminal run. The remediated runner must:

1. mechanically establish isolated/reconstructed workspace and candidate-native state roots per attempt;
2. derive formal `reset_verified` from those proofs;
3. fail closed on missing/substituted raw source bindings before unchanged-v5 PASS can be represented;
4. bind work/generation ids to exact toolchain/build/binary/lock/run/artifact/source/validator identity;
5. add real reset/source/toolchain/binary substitution negatives;
6. preserve run `31924017117` and run `31924179133` as immutable predecessor provenance;
7. preserve Unity/Unreal authority blockers and all existing authority boundaries.

The remediation requires a fresh independent/degraded-independent review. Integration remains separately authorized and squash-only.

## Authority boundary

This review grants no trusted S4 comparison evidence, integration authority, engine ranking/selection, S1/S2/S5-S10 completion, implementation/readiness, provider/legal/platform/release authority, verification-PASS, decision authority, or canonicality.