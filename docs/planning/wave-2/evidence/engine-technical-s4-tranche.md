# W2-ENG-TECH-S4-01 — public-toolchain S4 save/schema empirical tranche

## Scope and authority

This packet is a fresh bounded S4 producer episode under Planning Program v1 and owner sequencing directive `5303081124`. It exercises only the unchanged `W2-ENG-HARNESS-v5` / `W2-ENG-SCENARIO-INPUTS-v2` S4 contract. Historical Issue #82 remains immutable with its 50 historical `NOT_RUN` cells, and the reviewed S3 packet remains separate provenance.

No engine is ranked or selected. No S1/S2/S5-S10 completion, production implementation/readiness, provider/legal/platform/release permission, verification-PASS, decision, canonical, or integration authority is created. Unity and Unreal Engine remain `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY` for S4.

## Exact S4 contract

- fixed refs: `SLICE:logical_state`, `SLICE:save_schema`
- obligations: `round_trip`, `schema_evolution`, `explicit_migration`, `malformed_tuple_diagnostic`
- bounds: 32 entities, 5 v1 fields, 1 v2 added field
- required injection: `FI-S4-INCOMPAT-TUPLE-v2`
- resource class: `W2-ENG-HOST-COMMON-v2`
- mechanism authority: `CANDIDATE_NATIVE_EQUIVALENT`

The common repository fixture uses v1 fields `schema_version`, `seed`, `tick`, `entities`, `settings`; v2 adds `world_flags={}`. Normal attempts require exact v1 round-trip, explicit v1→v2 migration, and stable v2 replay. The injection corrupts one entity tuple and must be explicitly rejected/diagnosed.

Fixture SHA-256 identities from the terminal run:

- v1: `c47666d7212644bbf089c476b4cbc18f8ceb6dec1689967fa1d955ad69fb07ff`
- v2: `b7fffabfe080fc2c9c9b5ba019da103e1cc10dd45a26bddc87b76d0b1e88dd56`
- malformed: `93971ed64cd173fade5a764d6047c982a31867d7ad3a92760c7251c4819b2233`

## Producer execution history

### Run 1 — retained Bevy-lock mismatch discovered

- trigger commit: `f3b4d2abfdbc4de4f5da52378b2ae3758692aded`
- Actions run: `31924017117`, attempt 1, conclusion `success`
- generated evidence commit: `65f1de17944e76a2bf17692fc89aa5ef8a59e288`
- artifact: `9257269494`, `w2-eng-tech-s4-01-31924017117-1`
- artifact digest: `sha256:0370b34c16abe68f5b1ea21abf0fc43e19517268f2c3e7831b2ab10ffd45b1b2`

The workflow itself was healthy and Defold/Godot produced provisional S4 v5 passes, but Bevy did not execute: the first runner named the temporary root package `everfield_bevy_s4`, which did not match retained `Cargo.lock` root package `everfield_bevy_probe` under `cargo build --locked`. This was treated as a producer/harness defect, not as Bevy product evidence.

### Bounded remediation and terminal run

- remediation commit: `c6f274f53bc14b2eb4a1da540b82994dbbdef75b`
- change: bind the temporary Bevy root package and binary to retained lock identity `everfield_bevy_probe`; the retained lock itself is unchanged
- Actions run: `31924179133`, attempt 1, conclusion `success`
- generated evidence commit: `9a15af3895c8a0c053bf2666463910b659769121`
- artifact: `9257331215`, `w2-eng-tech-s4-01-31924179133-1`
- artifact digest: `sha256:3271072d2e75b135265bbdcd162cd9f9b4e130345e05c5c3dc3c137de0c28291`
- `evidence.json` SHA-256: `8ba3922733c4051f798dab002de4cf607f6176ffe3f66d3e85a2568473967453`

All workflow steps completed successfully, including unchanged-v5 validation, fail-closed envelope checks, exact evidence persistence, and immutable artifact upload.

## Terminal empirical result pending required review

The terminal run produced exactly three provisional public-toolchain S4 generations:

| Candidate | Real candidate process | N1 | N2 | FI-S4 | unchanged-v5 aggregate |
| --- | --- | --- | --- | --- | --- |
| Bevy 0.19.0 | retained-lock `cargo build --locked`; Bevy `World`/resource binary | PASS | PASS | PASS | `PASS_FOR_COMPARISON` |
| Defold 1.13.0 | Bob `--archive` bundle; Defold engine process using native `sys.save`/`sys.load` | PASS | PASS | PASS | `PASS_FOR_COMPARISON` |
| Godot 4.7.1-stable | exact headless Godot process using `FileAccess` | PASS | PASS | PASS | `PASS_FOR_COMPARISON` |

Exact formal generation identities include:

- Bevy: `GEN-S4-ec818ae3ac554ebfba86f15a`, work `WORK-S4-b7f28035388d6d46bf8cd1fe`
- Defold: `GEN-S4-ca9548c6df05aac6f00159a5`, work `WORK-S4-aad875f7fa88500c129f8a31`
- Godot: `GEN-S4-041a4fe7b604b4d6c07c4c5c`

Each final generation has two distinct normal workspace/reset identities, one distinct required-injection workspace/reset identity, one-to-one run registry/source bindings, `va()`=`ACCEPT`, and `agg()` exactly `PASS_FOR_COMPARISON` with `valid_envelope=true`.

All producer negative self-tests fail closed: candidate-generation mismatch, duplicate registry, workspace reuse, reduced schema bound, missing migration obligation, omitted schema field, missing migration default, malformed tuple handling, and source-digest substitution.

## Required review attacks

Fresh independent or degraded-independent review must attack, at minimum:

1. exact run/head/artifact/evidence identities and run-1 defect/remediation provenance;
2. real-engine-process authenticity for each candidate;
3. common fixture semantics and candidate-native equivalence;
4. exact v1 round-trip, explicit v1→v2 migration/default, and stable v2 replay;
5. malformed-tuple fail-closed behavior;
6. toolchain/content acquisition and retained-lock/artifact-lock identity;
7. distinct workspace/reset derivation and one-to-one source bindings;
8. unchanged-v5 adaptation/AttemptRecord/registry/aggregate semantics;
9. negative self-tests;
10. Unity/Unreal authority classification and preservation of Issue #82/S3 provenance;
11. any authority inflation beyond exact executed S4 cells.

Until that review terminalizes cleanly, these S4 outcomes are producer evidence only and are not trusted W2-ENG comparison evidence.
