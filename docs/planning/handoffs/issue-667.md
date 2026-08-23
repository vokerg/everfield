# Issue #667 handoff — persistent Unity S3 reviewed-v5 lineage instrumentation

Mission: `W2-ENG-TECH-UNITY-S3-V5-RERUN-01`  
Branch: `planning/issue-667`  
Base: `ec5fc3f6313ee2e91e530ca83b1f80e2f355eeed`  
Disposition target: `LINEAGE_INSTRUMENTATION_CANDIDATE`

## Exact predecessor and authority

- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- canonical binding: Bootstrap Issue #6 comment `5245368879`;
- source verification: Issue #665 terminal comment `5381256836`;
- source work/head: `ab9fe5f34495c6643428164f278317fa1840caf4`;
- source finding: `W2-ENG-TECH-UNITY-S3-V5-VERIFY-M01` (MAJOR);
- reviewed v5 validator blob: `2c646988dc16e212f43df6a4ee5ce646622ac2a6`;
- trusted persistent runner lane: Issue #633;
- reviewed persistent evaluator blob: `e50d8125718846a871eaf7020991120d48e04eae`;
- reviewed persistent recorder blob: `3d6cdb20f1ab278aca3403491156750f3e4a480a`;
- retained exact-main Unity evidence: `docs/planning/wave-2/evidence/ci/unity-persistent-access/32552745832/effective.json` blob `3fdd02bc1249f43e7365f203cc0227282abdde57`.

The predecessor already establishes bounded native Unity `6000.5.6f1` S3 execution and the N1/N2/FI1 checksums. This episode does not reinterpret or mutate that evidence; it closes only the missing lineage surface required for a fresh rerun.

## Bounded instrumentation

New isolated surfaces:

- `tools/planning/unity_s3_v5_lineage.py`
- `tools/planning/record_unity_s3_v5_lineage.py`
- `.github/workflows/unity-s3-v5-lineage-evaluator.yml`
- `.github/workflows/unity-s3-v5-lineage-recorder.yml`

The existing provider/access evaluator, recorder, provider validator/projection, reviewed-v5 validator, and historical evidence remain unchanged.

The evaluator is `workflow_dispatch` only on exact trusted `main`, requires the existing dedicated `[self-hosted, macOS, ARM64, everfield-unity]` runner identity, reuses the reviewed pinned checkout/upload action identities, and consumes no provider credential. It executes exactly S3 N1/N2/FI1 under seed `424242`, 32 entities, 600 ticks, 10 actions and `FI-S3-INPUT-PERTURB-v2`.

Each attempt retains only sanitized authority-bearing lineage:

- actual-workspace marker digest and derived unique `workspace_id`, with no absolute path;
- mechanically derived reconstruction/reset facts, unique `reset_id`, and `reset_verified` equal to the conjunction of those facts;
- resource class exactly `W2-ENG-HOST-COMMON-v2` plus separate persistent-runner executor identity;
- exact Unity version, executable basename/digest, generated project/source digests and fixed-input digest;
- bounded process exit/timeout/timing plus expected/observed checksum;
- canonical lineage/raw-attempt digests and one-to-one `source_binding_id`;
- deterministic candidate work and generation identities bound to the exact source head/run/attempt set.

The recorder is GitHub-hosted/data-only. It binds the exact upstream workflow/run/head, checks out projection code from that exact source head, reruns deterministic self-tests, rejects missing/tampered/duplicate/wrong-resource/wrong-run/sensitive lineage, and stages exactly one evidence JSON file on an immutable evidence branch. It never pushes directly to `main` and does not create or merge a PR.

## Deterministic producer verification

Before terminal status:

- `python3 -m py_compile tools/planning/unity_s3_v5_lineage.py tools/planning/record_unity_s3_v5_lineage.py`
- `python3 tools/planning/unity_s3_v5_lineage.py --self-test`
- `python3 -m tools.planning.record_unity_s3_v5_lineage --self-test`
- static workflow inspection confirms exact trusted-main/event/runner gates, reviewed 40-hex action pins, minimum permissions, one bounded artifact, source-head projection binding, immutable evidence-branch publication, and no direct-main push;
- negative tests cover false/missing reset authority, duplicate workspace/registry lineage, tampered source/raw/source-binding data, wrong resource/run/workflow identity, absolute-path leakage, and sensitive fields.

No Unity/provider credentialed execution is performed from this producer branch.

## Required next gate

This producer grants no execution or integration authority. Route exactly one fresh independent/degraded-independent security/authority review of the exact producer head. The reviewer must attack public-repository self-hosted-runner exposure, exact-main/event/SHA fencing, runner labels/identity, permission scope, path/session leakage, reset/workspace derivation, resource-class semantics, source/raw digest recomputation, registry uniqueness, recorder trust, historical-evidence immutability, and authority inflation.

Only an explicit clean `PASS_FOR_INTEGRATION` review can unlock a separately authorized squash-only integration of this instrumentation. Only after that reviewed integration may a fresh exact-main lineage evaluator run occur. A later verifier/reviewer must construct the formal reviewed-v5 adaptation/generation and run the unchanged v5 `va()`/`agg()`; this issue itself cannot claim `PASS_FOR_COMPARISON`.

## Authority boundary

`NOT_CANONICAL`. Instrumentation candidate only. No provider PASS, Unity license authority, S3 comparison PASS, engine selection, implementation/readiness, production/commercial/legal/release, verification-PASS, decision, integration, or canonical authority. Historical Issue #82 50 `NOT_RUN` cells remain immutable.
