# Issue #364 handoff — W2-ENG-TECH-S4-REM-01

## Terminal route

`REMEDIATED_S4_EVIDENCE_READY_FOR_FRESH_REVIEW`

The blocking remediation closes review Issue #362 findings M01/M02/M03 by fresh empirical rerun. The exact Bevy/Defold/Godot outputs remain **provisional pending fresh required review**; no trusted-comparison or integration authority is granted by this handoff.

## Ownership / frozen lineage

- Issue #364 winning claim: `5305561429`.
- Branch `planning/issue-364`, base `main@c043c47acfa3212ca08e87725b25e47a20e8e5e6`.
- Canonical binding: Issue #6 comment `5245368879`, program blob `e3120ec203c4156328770aa86c12fbb7187966dc`.
- Producer Issue #360 terminal `5305536469`, immutable head `942a8c05032c1506730f52e897496172fb56fcf3`.
- Producer terminal run `31924179133`, artifact `9257331215`, evidence SHA-256 `8ba3922733c4051f798dab002de4cf607f6176ffe3f66d3e85a2568473967453`.
- Required review Issue #362 terminal `5305556485`, immutable review head `8a1b2a406dc00181fa805bfc38fcca3b798510bb`, disposition `CHANGES_NEEDED`, 0 BLOCKER / 3 MAJOR / 0 MINOR.

## Exact remediation run

- workflow trigger: `c6f07004db066032494e76c04da41d24a5614e15`;
- Actions run `31924831337`, attempt 1, conclusion `success`;
- generated evidence commit `c9e503d9494ee2133d396929f9d612b73477b4dd`;
- artifact `9257513524`, `w2-eng-tech-s4-rem-01-31924831337-1`;
- artifact digest `sha256:281bcf6ab9c6db0ec9a4bafa14b98ca252e114ee8939d1928c4bff3c7e289373`;
- `evidence.json` SHA-256 `bbeec3df3e284d1805c5fe46bcf927b86fe57eaf45b3ccf43feafd563657ad59`;
- unchanged validator SHA-256 `9a50e3e21279a7a94836d6162fee218a0e187bafe292847fd5f0b108df45deea`;
- frozen source producer runner SHA-256 `51c3f652d8bf9c222c83cb381b1adf8286737bcc6d11cb6fd8cd6080b0ac27ed`.

Artifact ZIP and extracted evidence hashes were independently rechecked after the run and match these identities.

## Fresh provisional candidate generations

- Bevy 0.19.0: `GEN-S4R-6497066fc4b41018306e88fe`, work `WORK-S4R-6c233d098d43ae2b27e1c62a`.
- Defold 1.13.0: `GEN-S4R-6d03077324c742a9a1189e02`, work `WORK-S4R-d0ecc1252e18670be3448bb8`.
- Godot 4.7.1-stable: `GEN-S4R-dd10ac7075ee1f2530085b69`, work `WORK-S4R-6de47095c6d2eddd8ff6b756`.

For all three exact packets:

- N1/N2/FI1 freshly executed;
- reset truth is mechanically derived from retained exclusive workspace + candidate-native state-root proofs;
- HOME/XDG roots are distinct per attempt, including Defold native saves;
- exact raw attempts are digest-bound to formal refs before trusted representation;
- candidate/work/generation identities bind executable/toolchain/build/lock/validator/remediation/run/source identities and exclude ephemeral path authority;
- binding verification is `{ok: true, reasons: []}`;
- every required remediation negative is true/fail-closed;
- unchanged-v5 adaptation is `ACCEPT`;
- unchanged-v5 aggregate is exactly `PASS_FOR_COMPARISON` with `valid_envelope=true`;
- disposition is `REMEDIATED_S4_PROVISIONAL_PASS_PENDING_FRESH_REVIEW`.

## Findings addressed

- **M01:** no hard-coded reset authority; isolated state roots and reset evidence are derived mechanically. Defold native-state roots are isolated with per-attempt HOME/XDG roots.
- **M02:** source binding is independently recomputed and checked before a candidate is representable as remediation-eligible; actual raw/binding mutation negatives fail closed.
- **M03:** generation lineage now binds exact executable/toolchain/build/lock/validator/remediation/run/raw-source identities; random temp-path spelling is not identity authority.

## Required next gate

Create exactly one fresh independent/degraded-independent review of the exact terminal remediation packet. Reviewer must treat this branch as immutable judged input and attack M01–M03 closure, exact run/artifact/evidence identity, reset and native-state isolation, raw/formal source binding, true substitution negatives, deterministic identity binding, actual engine processes, unchanged-v5 semantics, S4 fixture/migration/injection semantics, Unity/Unreal authority classification, Issue #82/S3 provenance preservation, and authority inflation.

A clean review may trust only the exact executed S4 cells. It cannot complete S1/S2/S5-S10, Unity/Unreal, five-candidate comparison, engine ranking/selection, production/readiness/provider/legal/platform/release/verification-PASS/decision/canonical authority, or grant integration authority.

## Authority boundary

Unity and Unreal Engine remain `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY`. Historical Issue #82 retains 50 `NOT_RUN` cells. Reviewed S3 provenance is unchanged. `trusted_comparison_authority=false`, `engine_selected=false`, `canonicality=NOT_CANONICAL`, `integration_authority=false` until separately reviewed/authorized. Any eventual main publication remains squash-only.