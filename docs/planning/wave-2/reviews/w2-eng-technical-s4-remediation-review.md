# W2-ENG-TECH-S4-REV-02 — required review of remediated S4 reset/source/generation evidence

## Disposition

`PASS_BOUNDED_REMEDIATED_S4_V5_ENVELOPE`

Review mode: `DEGRADED_SINGLE_AGENT`.

Finding count: **0 BLOCKER / 0 MAJOR / 0 MINOR**.

The exact Issue #364 remediation packet closes the three MAJOR findings from required review Issue #362 for the exact fresh Bevy, Defold, and Godot S4 generations listed below. Those generations may now be trusted only as bounded `W2-ENG-HARNESS-v5` S4 comparison evidence. This review does not complete any other scenario or candidate, does not select an engine, and grants no integration, readiness, production, provider, commercial, legal, platform, release, verification-PASS, decision, or canonical authority by itself.

## Frozen judged input

- Canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`.
- Canonical binding: Issue #6 comment `5245368879`; activation SHA `413e729e8d2d5ac2eb138903f3f2ace07283b23e` remains in current-main ancestry.
- Review base/current main at claim and immediately before review write: `c043c47acfa3212ca08e87725b25e47a20e8e5e6`.
- Review Issue #374 claim: `5305597286`; branch `planning/issue-374`.
- Judged remediation Issue #364 claim: `5305561429`; terminal schema-3 status: `5305583040`.
- Judged remediation branch/head: `planning/issue-364@c68c3063082692addba7615b4f372f58bb7617e0`.
- Judged draft PR #371: open/draft, exact head `c68c3063082692addba7615b4f372f58bb7617e0`, base `main@c043c47acfa3212ca08e87725b25e47a20e8e5e6` at review freeze.
- Remediation workflow trigger: `c6f07004db066032494e76c04da41d24a5614e15`.
- Actions run `31924831337`, attempt 1, conclusion `success`; generated evidence commit `c9e503d9494ee2133d396929f9d612b73477b4dd`.
- Artifact `9257513524`, `w2-eng-tech-s4-rem-01-31924831337-1`; artifact ZIP SHA-256 `281bcf6ab9c6db0ec9a4bafa14b98ca252e114ee8939d1928c4bff3c7e289373`.
- Extracted `evidence.json` SHA-256 `bbeec3df3e284d1805c5fe46bcf927b86fe57eaf45b3ccf43feafd563657ad59`.
- Frozen producer runner SHA-256 `51c3f652d8bf9c222c83cb381b1adf8286737bcc6d11cb6fd8cd6080b0ac27ed`.
- Remediation implementation SHA-256 `8154cc3f944149b0ea67ac50d58bec55a4722d18ebb5569e70638881ac3d80cc` and entry shim SHA-256 `a60985f37d5c51ca7d0640fbb3622f46994ef9ddd30ae17138863347e56dc416` as recorded by the exact run.
- Unchanged v5 validator SHA-256 `9a50e3e21279a7a94836d6162fee218a0e187bafe292847fd5f0b108df45deea`.
- Retained Bevy lock SHA-256 `fd7e1276ff5c8cde22d98c0932f70eb39383d9b60ac2d15f11d921dfa71218b0`.
- Retained artifact lock SHA-256 `23f71143c3771df2f438b899a7a948e58da93bc15a3defe9cf3fb5e2b9147daf`.
- Predecessor producer Issue #360 terminal `5305536469`, immutable head `942a8c05032c1506730f52e897496172fb56fcf3`, terminal run `31924179133`, artifact `9257331215`, evidence SHA-256 `8ba3922733c4051f798dab002de4cf607f6176ffe3f66d3e85a2568473967453`.
- Predecessor required review Issue #362 terminal `5305556485`, immutable head `8a1b2a406dc00181fa805bfc38fcca3b798510bb`, disposition `CHANGES_NEEDED`, findings exactly `W2-ENG-TECH-S4-REV-M01`, `M02`, `M03`.

The immutable Actions artifact was independently downloaded in this review episode. Its ZIP SHA-256 exactly matched the GitHub artifact digest and workflow upload digest. After extraction, `evidence.json` and `source-producer-runner.py` independently matched the frozen hashes above. The artifact contains the expected seven retained files, including machine evidence, validator output, run identity, frozen producer source, and summary. This removes prose-only trust from the judged evidence packet. The review mode remains `DEGRADED_SINGLE_AGENT` because stronger reviewer-process isolation is unavailable; no stronger independence is claimed.

## Exact S4 authority contract checked

The remediated packet binds unchanged `W2-ENG-HARNESS-v5` / `W2-ENG-SCENARIO-INPUTS-v2`, scenario S4 only:

- fixed refs `SLICE:logical_state`, `SLICE:save_schema`;
- obligations `round_trip`, `schema_evolution`, `explicit_migration`, `malformed_tuple_diagnostic`;
- minimum bounds `entity_count=32`, `save_v1_field_count=5`, `save_v2_added_field_count=1`;
- required injection `FI-S4-INCOMPAT-TUPLE-v2`;
- common resource class `W2-ENG-HOST-COMMON-v2` with cold/reconstruct start semantics;
- default mechanism authority `CANDIDATE_NATIVE_EQUIVALENT`;
- trusted representation only when the remediation binding verifier passes, the unchanged-v5 adaptation validates as `ACCEPT`, and unchanged-v5 aggregation is exactly `PASS_FOR_COMPARISON` with `valid_envelope=true`.

The exact validator self-test output is retained in the artifact and the exact validator bytes are hash-bound in every represented candidate identity.

## Predecessor finding closure

### M01 — reset derivation and Defold candidate-native state isolation: CLOSED

The remediation no longer assigns reset truth as a producer assertion. `reset_prepare()` creates per-candidate/per-attempt workspace and state-root directories with exclusive creation, records that each root was absent before creation, materializes a distinct HOME/XDG data/config/cache hierarchy, verifies the candidate state root contains no files before candidate execution, and derives logical workspace/state/reset IDs from candidate, label, run identity, and role.

`verify_reset()` mechanically requires all retained pre-absence/exclusive-creation/empty-state facts and exact environment-isolation keys. `verify_reset_set()` additionally requires the workspace, candidate-native state-root, and reset IDs to be unique across N1/N2/FI1. `reset_verified_derived` is computed only from that proof and is what is transferred into the unchanged-v5 formal attempt. Negatives for missing reset proof, asserted reset without proof, reused workspace, and reused state root all fail closed in every represented candidate packet.

Defold receives the distinct per-attempt HOME/XDG roots before its candidate process starts. The frozen candidate Lua calls `sys.get_save_file`, `sys.save`, and `sys.load` for both v1 and v2 native state. The remediated evidence records different state-root identities across N1/N2/FI1 and non-empty post-candidate state-tree digests on the normal Defold attempts, while the real process output identifies `Defold Engine 1.13.0 (f735c12)`. This is mechanically stronger than merely copying a bundle and establishes that the candidate-native save surface is routed through the isolated attempt environment.

The entry shim also corrects the host verifier for Defold: if the outer attempt workspace does not directly contain `input.save`, it requires exactly one candidate input within the copied bundle and runs the unchanged producer host verifier against that exact directory. Candidate output is therefore not laundered through a host-side copy.

### M02 — fail-closed raw/formal source binding: CLOSED

Each fresh N1/N2/FI1 execution is first represented as a canonical `S4-RAW-ATTEMPT-v1` record. The record binds candidate identity digest, scenario, run identity, fixture digest, semantic command/binary identity, process exit/timeout/stdout/stderr, host semantic evidence and output digests, reset proof and mechanically derived reset truth, post-candidate state-tree digest, and the formal result/failure class. The raw record digest is SHA-256 over its canonical JSON body; timing observation is explicitly outside authority-bearing digest material.

`formalize()` creates the unchanged-v5 generation, maps each exact `run_registry_ref` one-to-one to the ordered raw-attempt digest, and calls the remediation `verify_packet()` before representing the candidate as trusted. `verify_packet()` independently recomputes the candidate identity digest and every raw-attempt digest, validates candidate/run identity, validates the reset set, validates binding cardinality and registry membership, checks each formal ref against the exact raw digest, checks formal/raw candidate/result/failure/reset/workspace equality, and recomputes expected work/generation identity.

Only after that external binding verification does the packet compute the unchanged-v5 aggregate and set `trusted_representation_ok`; trusted representation requires binding verification `{ok:true,reasons:[]}`, adaptation `ACCEPT`, and exact `PASS_FOR_COMPARISON` / `valid_envelope=true`.

The required negatives are real binding attacks rather than hash-sensitivity demonstrations: mutation of a raw fixture/source field without recomputing its digest is rejected by digest verification, and substitution of one formal ref's raw binding for another is rejected by `verify_packet()`. Both negatives are retained as `true` for Bevy, Defold, and Godot. Candidate-generation mismatch and duplicate registry attacks are also rejected by unchanged v5.

### M03 — deterministic exact-evidence work/generation identity: CLOSED

The candidate identity binds candidate/version, exact executable SHA-256, canonical toolchain/content identity, build identity digest, exact unchanged validator SHA-256, frozen producer runner SHA-256, harness/scenario identities, exact run trigger/run identity, and predecessor producer/review provenance. The entry shim additionally binds the exact remediation implementation and entry-shim byte hashes and recomputes the candidate identity digest.

The remediated `derive_ids()` then derives work/generation identity from candidate name, that candidate identity digest, the ordered canonical raw-attempt digests, unchanged-v5 adaptation identity, exact run identity, and scenario. Candidate work/generation therefore changes if binary/build/toolchain/source/reset/run/adaptation authority-bearing evidence changes.

The review specifically attacked the predecessor's random-temporary-path problem. The exact entry shim overrides the base sanitizer with a recursive `_scrub()` that removes ephemeral `path`, `executable`, command, timing, stdout/stderr, download/probe, unzip, and version-probe fields at any nesting depth before toolchain identity is hashed. The full raw toolchain observation intentionally retains temporary paths as provenance metadata, but those paths are not candidate/work/generation identity authority. Exact executable/content/build/lock digests remain bound separately.

The candidate-binary and toolchain identity substitution negatives both mutate authority-bearing candidate identity material while leaving the stored identity digest unchanged; `verify_packet()` therefore rejects them. Raw/source substitution likewise invalidates packet identity/binding. All three classes of negative are retained as passing fail-closed tests for all three exact candidates.

## Candidate authenticity and common S4 semantics

### Bevy 0.19.0

The exact retained Cargo.lock is replayed and a real Bevy-linked Rust binary is built and executed. Candidate code instantiates a Bevy `World` and resource carrying the judged logical state before it performs round-trip/migration work. Fresh N1/N2/FI1 process results exit successfully and emit only the expected bounded markers. Exact represented generation: `GEN-S4R-6497066fc4b41018306e88fe`; work: `WORK-S4R-6c233d098d43ae2b27e1c62a`.

### Defold 1.13.0

An exact digest-bound Bob toolchain builds a Defold Linux bundle and the produced engine binary executes. The candidate performs native `sys.get_save_file` / `sys.save` / `sys.load` operations inside the isolated HOME/XDG state root and separately writes the bounded round-trip/migration/replay surfaces. Fresh N1/N2/FI1 process output proves the real Defold engine process consumed the candidate program. Exact represented generation: `GEN-S4R-6d03077324c742a9a1189e02`; work: `WORK-S4R-d0ecc1252e18670be3448bb8`.

### Godot 4.7.1-stable

The exact digest-bound Linux archive is extracted and its exact executable SHA is bound. A real headless Godot process executes candidate GDScript using `FileAccess` for judged save surfaces. Fresh N1/N2/FI1 outputs identify Godot 4.7.1 and emit the expected bounded markers. Exact represented generation: `GEN-S4R-dd10ac7075ee1f2530085b69`; work: `WORK-S4R-6de47095c6d2eddd8ff6b756`.

Across all three candidates, the common normal input contains 32 five-field entities and the exact v1 field set. Candidate output is independently checked for exact v1 round-trip equality, exact v2 migration with default `world_flags={}`, and replay equality. The malformed-input fixture changes one entity tuple width; each candidate process itself inspects tuple structure and emits the injection-pass marker only on the expected incompatibility path. The host verifier also independently parses the malformed fixture and records the expected `malformed_entity_tuple` reason. The failure injection is therefore candidate-consumed rather than host-only detected or crash-laundered.

## Unchanged-v5 envelope check

For all three exact represented generations:

- remediation `binding_verification == {"ok": true, "reasons": []}`;
- unchanged-v5 adaptation result is exactly `ACCEPT`;
- unchanged-v5 aggregate is exactly `{"aggregate":"PASS_FOR_COMPARISON","reasons":[],"valid_envelope":true}`;
- `trusted_representation_ok == true`;
- every required remediation-specific and generic negative retained in the packet is `true`.

The remediation imports and invokes the exact unchanged validator implementation. No copied, weakened, post-hoc-overridden, or bypassed v5 aggregator was found. The remediation layer adds the physical provenance/reset/source checks that v5 intentionally does not own, then requires the unchanged v5 envelope as the final bounded formal condition.

## Predecessor provenance and authority preservation

The original first/terminal producer runs and the Issue #362 `CHANGES_NEEDED` review remain immutable predecessor provenance. They are not relabeled as remediated evidence. The newly trusted S4 authority attaches only to the exact fresh generations from run `31924831337` after this review.

Unity 6000.5.6f1 and Unreal Engine 5.8 remain exactly `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY`. Historical Issue #82 retains its 50 `NOT_RUN` cells and reviewed S3 provenance remains unchanged. This review creates no global gate from those provider-specific blocks and no synthetic completion for those candidates.

No S1/S2/S5-S10 completion, five-candidate completion, engine ranking/selection, gameplay/high-throughput implementation, implementation readiness, production/release, provider/commercial/legal/platform authority, verification-PASS, decision authority, or canonical authority is created.

## Adversarial attack results

| Attack | Result |
| --- | --- |
| Frozen #364 terminal/head/PR identity | PASS |
| Run / generated commit / artifact metadata identity | PASS |
| Independent artifact ZIP SHA-256 | PASS |
| Independent extracted evidence/source hashes | PASS |
| Unchanged v5 validator identity | PASS |
| M01 mechanical reset derivation | PASS |
| M01 Defold native-state isolation | PASS |
| Reset proof omission/assertion/reuse negatives | PASS |
| M02 canonical raw-attempt digests | PASS |
| M02 one-to-one formal/raw binding | PASS |
| M02 raw/source and binding-substitution negatives | PASS |
| M03 exact binary/build/toolchain/run/source binding | PASS |
| M03 recursive exclusion of ephemeral temp-path authority | PASS |
| M03 binary/toolchain/source substitution negatives | PASS |
| Bevy real-process authenticity | PASS |
| Defold Bob-built/native-save authenticity | PASS |
| Godot real-headless/FileAccess authenticity | PASS |
| Common 32-entity v1/v2 migration semantics | PASS |
| Candidate-consumed malformed tuple injection | PASS |
| Exact unchanged-v5 `va()`/`agg()` semantics | PASS |
| Generic schema/default/generation/registry negatives | PASS |
| Predecessor defect provenance preserved | PASS |
| Unity/Unreal authority classification | PASS |
| Historical Issue #82 / reviewed S3 preservation | PASS |
| Authority inflation | PASS |

## Result and next gate

The exact Bevy, Defold, and Godot S4 generations from remediation run `31924831337` are accepted as **reviewed bounded S4 v5 comparison evidence**. No finding remains that requires correction.

This review does not itself authorize a merge. Under owner convergence directive Issue #84 comment `5277825639`, reviewed terminal noncanonical provenance may be considered for separately authorized squash-only publication after the review terminal state and exact-head merge compatibility are durably verified. Integration remains separate from this review and separate from canonicalization; publication must not upgrade the bounded review result into readiness, production, decision, or canonical authority.