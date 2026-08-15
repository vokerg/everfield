# W2-ENG-TECH-S3-01 — technical S3 empirical tranche

Status: **producer evidence ready for required fresh review**. This is a bounded S3-only episode and is not trusted comparison evidence until that review terminalizes cleanly.

## Binding and provenance

- Task: Issue #351, claim `5303108501`, branch `planning/issue-351`.
- Source main at claim: `9f6c91031ca715f1c57da4ff047cfce6f4b5550c`.
- Active Planning Program v1 binding: Issue #6 comment `5245368879`, canonical program blob `e3120ec203c4156328770aa86c12fbb7187966dc`.
- Frozen predecessor: Issue #82 terminal `5276916603`, head/work `1575cb3a18c9c7be1776b64c9ec92cc8990a97e0`, disposition `INCONCLUSIVE_ENVIRONMENT_BLOCKED`.
- Historical predecessor matrix remains immutable: 5 candidates × S1–S10 = 50 historical `NOT_RUN` cells. This episode does not rewrite any of them.
- Current routing basis: owner product/development directive `5303081124`, which permits technically/lawfully executable evaluation slices to proceed while preserving exact authority-bound cells as `NOT_RUN`.
- Harness: `W2-ENG-HARNESS-v5`, `W2-ENG-FEATURE-SLICE-v2`, `W2-ENG-SCENARIO-INPUTS-v2`.

## S3 contract used

Common state is 32 entities, seed `424242`, 600 normal ticks, 10 actions, mechanism authority `REAL_OR_SHARED_RULES`, resource class `W2-ENG-HOST-COMMON-v2`, and required perturbation `FI-S3-INPUT-PERTURB-v2` at tick 137. The repository-derived shared oracle is:

- normal checksum: `405227`;
- perturbed checksum: `405122`.

A producer cell is represented only as `PROVISIONAL_S3_PASS_FOR_COMPARISON_PENDING_REQUIRED_REVIEW` when two fresh normal workspaces reproduce `405227` and a third fresh injected workspace reproduces the distinct `405122` using an actual candidate-native process.

## Execution history

### Run 1 — retained failed producer attempt

- Trigger SHA: `2f67cd75e1758fa01e75554805caa1df6e480f83`.
- Actions run: `31895282641`, attempt 1.
- Generated evidence commit: `5d6b940ee3c57ac78f0d40a890cdc6d48891fd4c`.
- Artifact: `9249633980`, `w2-eng-tech-s3-01-31895282641-1`, digest `sha256:dee70cb19ad8ae254e69914d5cdc0b15902aaf8410971d14217b0162868d5135`.
- Godot executed successfully against the common oracle.
- Bevy was `INCONCLUSIVE_HARNESS_OR_INFRA`: the generated root package identity did not match the retained Cargo.lock root package and `cargo build --locked` correctly refused mutation.
- Defold was `INCONCLUSIVE_HARNESS_OR_INFRA`: the generated project omitted the default `/input/game.input_binding` source resource.

### Run 2 — retained remediation attempt

- Trigger SHA: `485f5259ad4fcc93755dd2d773c9441f33ac5640`.
- Actions run: `31895462621`, attempt 1.
- Generated evidence commit: `67848934b336aa7cde5e391d5cb7fef1766cf462`.
- Artifact: `9249687249`, `w2-eng-tech-s3-01-31895462621-1`, digest `sha256:f2258a90ccd47faa6f78bc864fc3578821ca047d6abfd5f08ac7c33d6a578d2a`.
- Bevy and Godot both executed two normal plus one injected attempt and matched the common oracle.
- Defold advanced through compilation but remained `INCONCLUSIVE_HARNESS_OR_INFRA`: Bob reached bundling and failed because archive generation had not been requested, leaving `build/default/game.arci` absent. Both headless and debug bundle attempts are preserved in the evidence history.

### Run 3 — current producer packet

- Trigger SHA: `a8023054415fb941ff6ee743ee28387baaf5ace3`.
- Actions run: `31895624493`, attempt 1, conclusion `success`.
- Generated evidence commit: `899e0011f49ce8a73f8b543a1c4b054ce517e715`.
- Artifact: `9249732138`, `w2-eng-tech-s3-01-31895624493-1`, digest `sha256:068e5ee0df2802d4f52486d0ea42932bb99eaa7a04098298bca8586e65a68c72`.
- Current evidence JSON SHA-256: `411641a6fbd6a27bd81adf5747c1bb961e5490fdae72d1eea15ac700dd8c85ca`.
- Runner SHA-256: `d972a657654db6104d801d544feb3b7a4d0fb73c984d85585f17073685aa3534`.
- Defold remediation helper SHA-256: `a010734081aa8d4a2962712fd092a40a0ba64c1c9e3fa343283f9e3d413b8820`.
- Reviewed capability probe SHA-256: `bf7de805a0bb941055466c4972d0f405b14f19f7e8d7196c9db07ab568fc5eac`.
- Harness validator SHA-256: `9a50e3e21279a7a94836d6162fee218a0e187bafe292847fd5f0b108df45deea`.
- Bevy retained Cargo.lock SHA-256: `fd7e1276ff5c8cde22d98c0932f70eb39383d9b60ac2d15f11d921dfa71218b0`.
- Toolchain artifact lock SHA-256: `23f71143c3771df2f438b899a7a948e58da93bc15a3defe9cf3fb5e2b9147daf`.
- Runner image: Ubuntu 24 (`ImageVersion=20260810.271.1`), Linux X64.

## Current producer outcomes

| Candidate | Native mechanism exercised | N1 | N2 | FI-S3 | Producer disposition |
|---|---|---:|---:|---:|---|
| Bevy 0.19.0 | Bevy ECS `World`/`Resource` in the exact retained dependency resolution | 405227 | 405227 | 405122 | `PROVISIONAL_S3_PASS_FOR_COMPARISON_PENDING_REQUIRED_REVIEW` |
| Defold 1.13.0 | Bob archive + headless Linux bundle, followed by produced engine process | 405227 | 405227 | 405122 | `PROVISIONAL_S3_PASS_FOR_COMPARISON_PENDING_REQUIRED_REVIEW` |
| Godot 4.7.1-stable | exact digest-bound Godot binary, headless generated project/GDScript | 405227 | 405227 | 405122 | `PROVISIONAL_S3_PASS_FOR_COMPARISON_PENDING_REQUIRED_REVIEW` |
| Unity 6000.5.6f1 | no lawful unattended editor activation/account-license state available to this repository run | — | — | — | `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY` |
| Unreal Engine 5.8 | no repository-self-grantable Epic-linked entitlement/preseeded engine input | — | — | — | `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY` |

For Defold, the run-3 remediation explicitly retains the run-3 pre-remediation Defold result under `producer_remediation_history`, then adds Bob `--archive`; the headless bundle succeeds and the actual produced process supplies all three checksums. The earlier run-1 and run-2 generated commits/artifacts remain immutable provenance and are not hidden by the final packet.

## Required review and authority boundary

A fresh independent/degraded-independent review must attack actual engine-process execution versus smoke-test laundering, common transition equivalence, checksum/oracle derivation, fresh workspace/reset independence, injection semantics, exact toolchain/content identities, retained failed-attempt provenance, the Defold archive remediation, Unity/Unreal authority classification, and any partial-candidate ranking inflation.

A clean review may trust only the exact executed S3 cells above. It cannot complete S1/S2/S4–S10, rank or select an engine, create implementation or production readiness, grant commercial/provider/legal/platform/release authority, create verification-PASS or decision authority, canonicalize this packet, or authorize integration. Draft PR #352 is review visibility only; integration remains separately authorized and squash-only.
