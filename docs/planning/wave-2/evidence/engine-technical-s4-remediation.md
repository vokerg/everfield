# W2-ENG-TECH-S4-REM-01 — S4 reset/source/generation binding remediation

## Disposition

`REMEDIATED_S4_EVIDENCE_READY_FOR_FRESH_REVIEW`

This is a fresh empirical rerun closing the design defects identified by required review Issue #362. It does **not** itself upgrade any S4 cell to trusted comparison evidence and grants no integration authority.

## Frozen lineage

- canonical Planning Program v1: blob `e3120ec203c4156328770aa86c12fbb7187966dc`, binding Issue #6 comment `5245368879`;
- producer Issue #360 terminal `5305536469`, immutable head `942a8c05032c1506730f52e897496172fb56fcf3`;
- predecessor producer run `31924179133`, artifact `9257331215`, evidence SHA-256 `8ba3922733c4051f798dab002de4cf607f6176ffe3f66d3e85a2568473967453`;
- required review Issue #362 terminal `5305556485`, `CHANGES_NEEDED`, findings M01/M02/M03;
- remediation trigger `c6f07004db066032494e76c04da41d24a5614e15`;
- remediation Actions run `31924831337`, attempt 1, conclusion `success`;
- generated evidence commit `c9e503d9494ee2133d396929f9d612b73477b4dd`;
- artifact `9257513524`, `w2-eng-tech-s4-rem-01-31924831337-1`, digest `sha256:281bcf6ab9c6db0ec9a4bafa14b98ca252e114ee8939d1928c4bff3c7e289373`;
- `evidence.json` SHA-256 `bbeec3df3e284d1805c5fe46bcf927b86fe57eaf45b3ccf43feafd563657ad59`;
- unchanged v5 validator SHA-256 `9a50e3e21279a7a94836d6162fee218a0e187bafe292847fd5f0b108df45deea`;
- frozen producer runner SHA-256 `51c3f652d8bf9c222c83cb381b1adf8286737bcc6d11cb6fd8cd6080b0ac27ed`.

The immutable remediation artifact was independently downloaded after the run; its ZIP digest and extracted evidence digest matched the GitHub and repository identities above.

## Review findings closed by remediation design

### M01 — reset derivation

Every N1/N2/FI1 attempt is created in an exclusive fresh workspace plus an exclusive candidate-native state root. The retained reset proof records pre-workspace absence, pre-state-root absence, exclusive materialization, pre-candidate empty state, and canonical workspace/state/reset IDs. `reset_verified` is derived only from those facts; it is never a literal producer assertion. HOME and XDG data/config/cache roots are unique per attempt, including Defold native `sys.get_save_file` state.

### M02 — fail-closed source binding

Each raw attempt is a canonical digest-bound record containing candidate identity, run identity, fixture digest, semantic command/binary identity, process result, host semantic/output digests, derived reset proof, and candidate-state-after digest. Formal v5 registry refs are bound one-to-one to those raw digests. A separate verifier recomputes raw digests, source mappings, formal/raw result/reset correspondence, candidate identity, and generation identity before a result can be represented as remediation-eligible.

True mutation negatives reject missing/asserted reset proof, workspace/state-root reuse, raw-source digest substitution, formal/raw binding substitution, executable identity substitution, and toolchain identity substitution. Unchanged-v5 negatives still reject candidate-generation mismatch and duplicate registry refs; S4 semantic negatives reject schema/default/malformed-input defects.

### M03 — exact-evidence identity

Candidate identity now binds candidate/version, exact executable digest, build/lock/content identity, normalized toolchain content identity with ephemeral paths removed, exact v5 validator, frozen predecessor runner, both remediation implementation/entry byte digests, run trigger identity, scenario/harness identity, and predecessor producer/review lineage. Work/generation IDs derive from that candidate identity plus exact raw-attempt digests and v5 adaptation identity, rather than random temporary-path spelling.

## Fresh empirical result pending required review

All three public candidates freshly completed N1/N2/FI1 with derived reset proofs, fail-closed source binding, unchanged-v5 adaptation `ACCEPT`, and unchanged-v5 aggregate exactly `PASS_FOR_COMPARISON` with `valid_envelope=true`:

| Candidate | Generation | Work | Binding | v5 aggregate |
| --- | --- | --- | --- | --- |
| Bevy 0.19.0 | `GEN-S4R-6497066fc4b41018306e88fe` | `WORK-S4R-6c233d098d43ae2b27e1c62a` | PASS | PASS_FOR_COMPARISON |
| Defold 1.13.0 | `GEN-S4R-6d03077324c742a9a1189e02` | `WORK-S4R-d0ecc1252e18670be3448bb8` | PASS | PASS_FOR_COMPARISON |
| Godot 4.7.1-stable | `GEN-S4R-dd10ac7075ee1f2530085b69` | `WORK-S4R-6de47095c6d2eddd8ff6b756` | PASS | PASS_FOR_COMPARISON |

All three candidate packets report `REMEDIATED_S4_PROVISIONAL_PASS_PENDING_FRESH_REVIEW`, binding verification `{ok: true, reasons: []}`, and all required negative self-tests true.

Unity and Unreal Engine remain `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY`. Historical Issue #82 retains 50 historical `NOT_RUN` cells; reviewed S3 provenance remains separate and unchanged.

## Required next gate

Fresh independent or degraded-independent review must judge the exact remediation head/run/artifact/evidence identities and specifically re-attack M01–M03 closure: reset/state-root derivation, raw/formal binding recomputation, mutation negatives, exact candidate/toolchain/build identities, deterministic generation lineage, actual engine-process execution, unchanged-v5 invocation, S4 semantics, and authority boundaries.

Until that review passes, `trusted_comparison_authority=false`, `engine_selected=false`, `canonicality=NOT_CANONICAL`, and `integration_authority=false`. No S1/S2/S5-S10 completion, readiness, provider/legal/platform/release, verification-PASS, decision, canonical, or production authority is created.