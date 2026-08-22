# W2-ENG technical Unity S3 v5 verification

Mission: `W2-ENG-TECH-UNITY-S3-V5-VERIFY-01`  
Issue: #665  
Verification base: `main@ec5fc3f6313ee2e91e530ca83b1f80e2f355eeed`  
Disposition: `RERUN_REQUIRED_FOR_UNITY_S3_V5_BINDING`

## Purpose

This verification asks one bounded question: can the exact retained persistent-workstation Unity S3 packet already on `main` be consumed as a reviewed-v5 Unity S3 comparison generation **without inventing missing evidence lineage**?

The answer is **no**. The packet is credible bounded evidence of real Unity `6000.5.6f1` S3 execution, but its retained projection is intentionally narrower than the reviewed `W2-ENG-PROTOCOL-VALIDATOR-v5` authority envelope.

No Unity S3 `PASS_FOR_COMPARISON` is created by this verification.

## Frozen inputs

- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- canonical binding: Bootstrap Issue #6 comment `5245368879`;
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- reviewed v5 validator: `docs/planning/wave-2/evidence/engine-spike-protocol-fixtures.py` blob `2c646988dc16e212f43df6a4ee5ce646622ac2a6`;
- reviewed public S3 authority: Issue #358 terminal comment `5305399666`;
- persistent Unity source issue: #633;
- exact committed source evidence: `docs/planning/wave-2/evidence/ci/unity-persistent-access/32552745832/effective.json` blob `3fdd02bc1249f43e7365f203cc0227282abdde57`;
- exact source run: `32552745832`, attempt 1, event SHA `1f66cc0745a840f5eb4f5b4d4869e2e31e38c1bd`;
- persistent evaluator workflow blob: `e50d8125718846a871eaf7020991120d48e04eae`;
- provider-effective validator blob: `c12f159a1536660a6a296b81b25c5be796a01890`;
- persistent evidence projection blob: `0dbbae3cfb820f163c5c7f015a4263c5bf662ecd`.

The committed run directory contains only `effective.json`; there is no second committed raw-attempt packet from which omitted lineage fields can be recovered.

## What the retained packet establishes

The packet establishes a trusted exact-main persistent runner context (`everfield-unity-mac`, macOS/ARM64), Unity `6000.5.6f1`, validated development access, installed/executed editor, and native Unity S3 execution under `W2-ENG-HARNESS-v5`.

The retained attempts are:

| Attempt | Kind | Expected | Observed | Injection | Process |
| --- | --- | ---: | ---: | --- | --- |
| `UNITY-S3-N1` | normal | 405227 | 405227 | — | exit 0, not timed out |
| `UNITY-S3-N2` | normal | 405227 | 405227 | — | exit 0, not timed out |
| `UNITY-S3-FI1` | failure injection | 405122 | 405122 | `FI-S3-INPUT-PERTURB-v2` | exit 0, not timed out |

The exact executable validator source additionally shows the Unity C# transition uses seed `424242`, `600` ticks, `10` actions, `32` entities, and the tick-137 perturbation. It creates three distinct `N1` / `N2` / `FI1` project subdirectories inside a Python `TemporaryDirectory` and runs the Unity Editor against each.

Those facts support bounded **native execution authenticity**. They do not, by themselves, supply the retained runtime lineage required below.

## Fail-closed field analysis

The persistent evidence projector deliberately reduces the native S3 packet to candidate/scenario identity, result/checksum, a sanitized command description, and process exit/timing. It does not retain the actual runtime project paths or per-attempt source/reset identities.

The following reviewed-v5 lineage cannot be mechanically reconstructed from the retained packet without introducing facts that were not retained:

- per-attempt runtime workspace/project identity;
- per-attempt reset/reconstruction identity and mechanically derived reset proof;
- per-attempt `W2-ENG-HOST-COMMON-v2` resource-class binding;
- exact per-attempt generated Unity project/script/source digest and one-to-one raw-attempt digest;
- authoritative source-attempt binding sufficient to derive candidate work/generation identity;
- therefore, a non-invented `candidate_generation_id` for N1/N2/FI1 and its formal registry bindings.

Formal v5 adaptation, work/generation IDs, AttemptRecords, `run_registry_refs`, `all_attempt_refs`, and `va()` / `agg()` outputs can be created **after** the missing raw lineage exists. Creating them now by hashing attempt labels, successful exits, or invented workspace/reset identifiers would repeat the evidence-envelope failure that the earlier public S3 remediation was designed to prevent.

### Finding `W2-ENG-TECH-UNITY-S3-V5-VERIFY-M01` — MAJOR

The retained packet proves bounded native Unity S3 execution but does not retain the per-attempt workspace/reset/resource/source lineage necessary for a reviewed-v5 comparison generation.

Effect: Unity S3 remains **not trusted as `PASS_FOR_COMPARISON`**. This is an evidence-binding gap, not a finding that the observed native checksums are false.

## Exact next route

Route exactly one bounded persistent-runner instrumentation/rerun successor. It should preserve the working Unity access path and add only the evidence needed for v5 binding:

1. retain immutable N1/N2/FI1 runtime workspace/project identities;
2. retain mechanically derived reconstruction/reset facts and distinct reset IDs;
3. bind each attempt to exact `W2-ENG-HOST-COMMON-v2` resource semantics;
4. retain exact Unity editor identity, generated project/script/source digest, command/process result, fixed S3 inputs and injection identity;
5. retain canonical raw-attempt digests and one-to-one source bindings;
6. derive deterministic Unity work/generation IDs and formal v5 AttemptRecords/registries from those retained facts;
7. execute the unchanged reviewed v5 adaptation validator and aggregate;
8. route fresh required review only if the result is exact `PASS_FOR_COMPARISON` with `valid_envelope=true`.

No optional review should be created before that blocking evidence gap is remediated.

## Preservation and authority

Issue #82 remains immutable historical provenance with 50 historical `NOT_RUN` cells. Reviewed Bevy/Defold/Godot S3 generations remain unchanged. The persistent Unity provider/access packet remains valid for its own bounded development-access/native-execution purpose.

This verification grants no engine selection, five-candidate comparison completion, S1/S2/S4-S10 completion, gameplay/high-throughput implementation authority, implementation/readiness, commercial/provider/legal/platform/release authority, verification-PASS authority, decision authority, integration authority, or canonical authority.

Machine-readable verification: `docs/planning/wave-2/evidence/ci/engine-technical-unity-s3-v5-verification/verification.json`.
