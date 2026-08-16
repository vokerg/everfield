# W2-ENG-TECH-S4-REV-01 — required review of public-toolchain S4 evidence

## Disposition

`CHANGES_NEEDED`

Review mode: `DEGRADED_SINGLE_AGENT`.

Finding count: **0 BLOCKER / 3 MAJOR / 0 MINOR**.

The exact Issue #360 producer packet is not eligible to upgrade Bevy, Defold, or Godot S4 cells to trusted W2-ENG comparison evidence. The observed processes and artifacts are retained as bounded producer provenance, but the v5 PASS envelope depends on unproven reset assertions and is not fail-closed against source/toolchain substitution. The judged producer branch remains immutable.

No integration authority is granted.

## Frozen judged input

- Canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`.
- Canonical binding: Issue #6 comment `5245368879`.
- Review base/current main at claim: `c043c47acfa3212ca08e87725b25e47a20e8e5e6`.
- Producer Issue #360 claim: `5305479805`.
- Producer Issue #360 terminal: `5305536469`.
- Producer branch/head: `planning/issue-360@942a8c05032c1506730f52e897496172fb56fcf3`.
- Producer PR: #361, draft/open, head `942a8c05032c1506730f52e897496172fb56fcf3`, base `main`.
- Initial run: `31924017117`; generated evidence commit `65f1de17944e76a2bf17692fc89aa5ef8a59e288`; artifact `9257269494`; artifact digest `sha256:0370b34c16abe68f5b1ea21abf0fc43e19517268f2c3e7831b2ab10ffd45b1b2`.
- Remediation commit: `c6f274f53bc14b2eb4a1da540b82994dbbdef75b`.
- Terminal run: `31924179133`, attempt 1, conclusion `success`.
- Terminal generated evidence commit: `9a15af3895c8a0c053bf2666463910b659769121`.
- Terminal artifact: `9257331215`, `w2-eng-tech-s4-01-31924179133-1`.
- Terminal artifact digest: `sha256:3271072d2e75b135265bbdcd162cd9f9b4e130345e05c5c3dc3c137de0c28291`.
- Terminal `evidence.json` SHA-256: `8ba3922733c4051f798dab002de4cf607f6176ffe3f66d3e85a2568473967453`.
- Terminal runner SHA-256 recorded in artifact: `51c3f652d8bf9c222c83cb381b1adf8286737bcc6d11cb6fd8cd6080b0ac27ed`.
- Exact v5 validator SHA-256 recorded in artifact: `9a50e3e21279a7a94836d6162fee218a0e187bafe292847fd5f0b108df45deea`.
- Retained Bevy lock SHA-256: `fd7e1276ff5c8cde22d98c0932f70eb39383d9b60ac2d15f11d921dfa71218b0`.
- Retained artifact lock SHA-256: `23f71143c3771df2f438b899a7a948e58da93bc15a3defe9cf3fb5e2b9147daf`.

The terminal artifact was independently downloaded during this review. The downloaded ZIP SHA-256 exactly matched the recorded GitHub artifact digest, and the extracted `evidence.json` SHA-256 exactly matched `8ba392...`.

## Exact S4 authority contract checked

The judged packet correctly binds unchanged `W2-ENG-HARNESS-v5`, `W2-ENG-FEATURE-SLICE-v2`, `W2-ENG-SCENARIO-INPUTS-v2`, scenario S4:

- fixed refs `SLICE:logical_state`, `SLICE:save_schema`;
- obligations `round_trip`, `schema_evolution`, `explicit_migration`, `malformed_tuple_diagnostic`;
- minimum bounds `entity_count=32`, `save_v1_field_count=5`, `save_v2_added_field_count=1`;
- required injection `FI-S4-INCOMPAT-TUPLE-v2`;
- common resource class `W2-ENG-HOST-COMMON-v2`;
- default mechanism authority `CANDIDATE_NATIVE_EQUIVALENT`.

The unchanged v5 validator is shape/lineage authority for its formal envelope. It deliberately consumes `reset_verified`, `workspace_id`, generation identity, registry membership, adaptation shape, and results supplied to it; it does not independently prove the physical truth of those producer fields. That physical binding must therefore be demonstrated by the producer/remediation evidence before v5 `PASS_FOR_COMPARISON` can be trusted.

## Positive observations retained as producer provenance

1. **Exact artifact identity is coherent.** The terminal artifact and evidence hashes match the frozen producer packet.
2. **First-run Bevy defect is retained rather than laundered.** Run `31924017117` recorded the retained-lock root-package mismatch. Commit comparison from generated evidence commit `65f1de...` to remediation commit `c6f274...` is one commit changing only `tools/planning/engine_technical_s4_probe.py`, 3 additions / 3 deletions. No Bevy result from the first run is promoted.
3. **Real candidate processes executed in the terminal run.** Bevy built and ran a Bevy-linked Rust binary; Defold built an archive bundle and ran the resulting engine binary; Godot ran the exact headless executable. All terminal commands exited 0 and emitted the expected bounded markers.
4. **Common fixture and output digests are internally coherent.** Normal attempts expose the exact v1/v2 digests, and the malformed fixture differs as expected. The host verifier records exact round-trip/migration/replay equality for normal attempts.
5. **Malformed tuples are consumed in candidate code.** The Bevy, Defold, and Godot scripts each inspect the 32 entity tuples and only emit the injection-pass marker when tuple width is invalid.
6. **Toolchain acquisition is materially recorded.** The evidence contains retained-lock identities, exact versions, process commands, download/extraction records, and candidate executable identity where the capability probe supplies it.
7. **Authority boundaries are preserved in prose and machine evidence.** Unity and Unreal remain `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY`; historical Issue #82 cells remain unchanged; S1/S2/S5-S10, engine ranking/selection, readiness, verification-PASS, decision, canonicality, and integration authority are not claimed.

These observations do not resolve the MAJOR findings below.

## MAJOR findings

### W2-ENG-TECH-S4-REV-M01 — reset verification is asserted, not mechanically derived

**Severity:** MAJOR

**Affected authority:** all three provisional Bevy/Defold/Godot S4 generations.

The producer's `attempt_record()` computes `workspace_id` only as SHA-256 of the absolute workspace pathname and sets `reset_verified: True` unconditionally. It does not derive the boolean from a reconstruction proof, pre-state absence check, cleanup result, candidate-data-directory isolation, or any other retained mechanical reset evidence.

`formalize()` then passes those producer booleans directly into unchanged v5 `gen(..., oks=...)`. Consequently the final `agg()` receives `reset_verified=true` as an asserted input. The fact that v5 rejects a *synthetic* reused workspace in `negative_selftests()` does not prove that the real producer attempts were reconstructed/reset.

This is material because the exact review contract requires `reset_verified` to be mechanically derived, and unchanged v5 treats that field as part of the comparison envelope.

Defold makes the gap stronger: each copied bundle calls `sys.get_save_file("everfield_s4", "native")` and `sys.get_save_file("everfield_s4", "native2")`, which resolve to candidate-native user save storage outside the copied attempt bundle. N1/N2 therefore do not demonstrate isolated native save roots merely by copying distinct bundle directories. The script overwrites before read, which reduces contamination risk, but does not establish the cold/reconstructed reset authority that the formal v5 records claim.

**Required correction:** a fresh bounded remediation must derive reset truth from retained evidence rather than copying/setting a boolean. At minimum it must create or prove isolated candidate state roots, prove pre-attempt absence/cleanup/reconstruction, bind the exact workspace/state-root identities to each attempt, and set formal `reset_verified=true` only from that derivation. Defold must use isolated/remediated candidate-native save roots or otherwise prove that its native state is reset per attempt.

### W2-ENG-TECH-S4-REV-M02 — source substitution is not fail-closed by the represented v5 PASS

**Severity:** MAJOR

**Affected authority:** all three provisional S4 generations and their one-to-one source claims.

`formalize()` calls unchanged v5 `va()` and `agg(g)` **before** it constructs the producer's `source_bindings` map. The map is a sibling of the already-computed aggregate; it is not consumed by `va()` or `agg()`.

The workflow only checks that the set of formal `run_registry_refs` equals the set of keys in `source_bindings`. It does not verify the binding values against immutable raw attempt bytes or candidate/toolchain identities before accepting the producer disposition.

The named negative `source_digest_substitution_detected` does not exercise a source-binding substitution. It merely checks that `sha256(fixture_v1())` differs from the SHA-256 of a locally modified fixture. That establishes hash sensitivity, not fail-closed lineage. A source-binding value, command digest, host-semantic digest, or raw source observation can be substituted while the already-computed unchanged-v5 aggregate remains `PASS_FOR_COMPARISON`.

This is exactly the kind of provenance laundering the required review must reject. A v5 aggregate can only be trusted when the producer/remediation layer mechanically proves the source-to-formal binding that v5 itself does not own.

**Required correction:** add an external fail-closed source-binding layer around unchanged v5. It must bind every formal attempt to exact immutable raw attempt evidence (including process command/result, fixture/output digests, candidate/toolchain/build identity, reset evidence, run/artifact identity), reject any missing/duplicate/substituted binding before representing a candidate as comparison-eligible, and include a negative that actually mutates a source binding/raw source digest and proves the bounded result can no longer be represented as trusted PASS.

### W2-ENG-TECH-S4-REV-M03 — generation/work identity is not bound to exact toolchain/build/source identity

**Severity:** MAJOR

**Affected authority:** all three provisional generation/work identities.

The producer derives `candidate_work_id` from candidate name plus each attempt's label, `workspace_id`, `reset_id`, and a digest of the process-command object. `candidate_generation_id` is then derived only from that work id plus candidate name.

This omits the exact toolchain/content identity, candidate binary digest, build input/lock identity, Actions run/artifact identity, raw source-evidence digest, and validator identity. A different binary or toolchain executed at the same command path with identical high-level host outputs can therefore retain the same generation/work identity inputs. Conversely, the absolute `tempfile` root appears in process paths and workspace path hashes, so unrelated random pathname allocation perturbs identity even when candidate/toolchain/build semantics are unchanged.

The terminal machine evidence separately contains useful toolchain identity, but the formal generation/work lineage does not bind it. The source-binding map also omits the toolchain/build/run identities, so it cannot close this gap.

**Required correction:** deterministically derive candidate work/generation identity from canonical exact evidence that includes candidate id/version, candidate binary or equivalent exact content identity, build/lock identity, harness/validator identity, scenario/adaptation identity, immutable run/artifact/source-evidence identity, and mechanically derived reset/workspace evidence. Random path spelling may be retained as observation metadata but must not be the only differentiator or substitute for content/provenance binding. Include negatives for candidate binary/toolchain/source substitution.

## Candidate-semantic attack result

No additional MAJOR is recorded for the use of candidate-native-equivalent save mechanisms in this review because the three processes do materially execute candidate-specific runtime code, inspect the common fixture, perform migration logic, and emit bounded diagnostics. However, this positive conclusion is **contingent on remediation of M01–M03**; it does not independently promote any cell.

Specific caveats retained for the remediation reviewer:

- Bevy uses an actual Bevy `World`/resource check but performs file persistence with Rust filesystem operations; the final remediation must keep the save operation materially coupled to the judged Bevy process and exact common logical state.
- Godot uses real headless Godot and `FileAccess` for the save surfaces.
- Defold uses a Bob-built engine process and `sys.save/sys.load` for native state, but its native save-root isolation is part of M01.

## Required negative-review conclusions

| Attack | Review result |
| --- | --- |
| Frozen producer head / run / artifact / evidence identity | PASS |
| First-run Bevy defect retained | PASS |
| Unchanged v5 implementation identity | PASS |
| Real candidate process execution | PASS bounded producer provenance |
| Common S4 fixture/bounds | PASS |
| Round-trip/migration/replay host outputs | PASS bounded producer provenance |
| Malformed tuple candidate consumption | PASS bounded producer provenance |
| Toolchain/content observation | PASS as raw provenance |
| Mechanically derived reset verification | **FAIL — M01** |
| Defold native state-root isolation | **FAIL — M01** |
| One-to-one source substitution fail-closed | **FAIL — M02** |
| Source-substitution negative | **FAIL — M02** |
| Generation/work exact toolchain/source binding | **FAIL — M03** |
| Unchanged v5 `va()`/`agg()` invocation | PASS syntactically, but trust blocked by M01–M03 |
| Unity/Unreal authority classification | PASS |
| Historical Issue #82 / reviewed S3 provenance preservation | PASS |
| Authority inflation | PASS |

## Remediation route

Route exactly one bounded fresh remediation successor. Do **not** edit `planning/issue-360`, PR #361, this review branch, or historical S3/Issue #82 provenance.

The remediation should preserve run `31924179133` as immutable producer evidence but must not simply relabel it as trusted. Because M01 lacks sufficient retained proof of candidate reset/native-state isolation, the safe route is a fresh empirical S4 rerun under a remediated harness that:

1. isolates and mechanically verifies candidate workspace plus candidate-native state roots for every N1/N2/FI1;
2. records proof inputs from which `reset_verified` is derived rather than asserted;
3. computes and verifies immutable raw-attempt/source bindings before invoking/representing unchanged v5 aggregation;
4. binds candidate work/generation ids to exact toolchain/build/binary/lock/run/artifact/source identities and exact validator/adaptation identities;
5. contains true mutation negatives for reset/source/toolchain/binary binding substitution;
6. retains the producer's first-run and terminal-run histories without laundering either into the remediated final generation;
7. keeps Unity/Unreal authority-bound and preserves all existing authority boundaries.

The remediation packet itself requires a fresh independent/degraded-independent review before any exact S4 cell becomes trusted comparison evidence.

## Authority boundary

This `CHANGES_NEEDED` review grants no trusted S4 comparison authority and no integration authority. It does not invalidate the fact that the recorded public candidate processes ran; it invalidates the requested upgrade from those observations to trusted unchanged-v5 comparison evidence.

No S1/S2/S5-S10 completion, five-candidate comparison completion, engine ranking/selection, gameplay/high-throughput implementation, implementation/production readiness, provider/commercial/legal/platform/release authority, verification-PASS, decision authority, canonicality, or integration authority is created.