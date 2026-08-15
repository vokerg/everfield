# Issue #351 handoff — W2-ENG-TECH-S3-01

## Terminal route

`PARTIAL_EMPIRICAL_S3_EVIDENCE_READY_FOR_REVIEW`

This is producer-only evidence. Fresh independent/degraded-independent review is mandatory before any S3 cell is trusted as W2-ENG comparison evidence.

## Ownership and source

- Issue: #351.
- Winning schema-3 claim: `5303108501`.
- Branch: `planning/issue-351`.
- Base main at claim: `9f6c91031ca715f1c57da4ff047cfce6f4b5550c`.
- Canonical binding: Issue #6 `5245368879`, program blob `e3120ec203c4156328770aa86c12fbb7187966dc`.
- Frozen predecessor: Issue #82 terminal `5276916603`, work/head `1575cb3a18c9c7be1776b64c9ec92cc8990a97e0`.
- Owner sequencing directive: `5303081124`.
- Draft producer PR: #352. Draft/mergeability does not grant integration authority.

## Current evidence packet

- Final empirical trigger SHA: `a8023054415fb941ff6ee743ee28387baaf5ace3`.
- Final empirical Actions run: `31895624493`, attempt 1, successful workflow envelope.
- Run-generated evidence commit: `899e0011f49ce8a73f8b543a1c4b054ce517e715`.
- Immutable Actions artifact: id `9249732138`, name `w2-eng-tech-s3-01-31895624493-1`, digest `sha256:068e5ee0df2802d4f52486d0ea42932bb99eaa7a04098298bca8586e65a68c72`.
- Evidence JSON SHA-256: `411641a6fbd6a27bd81adf5747c1bb961e5490fdae72d1eea15ac700dd8c85ca`.
- Report: `docs/planning/wave-2/evidence/engine-technical-s3-tranche.md`.
- Machine packet: `docs/planning/wave-2/evidence/ci/engine-technical-s3/evidence.json` plus `evidence.sha256`, `run-identity.txt`, harness validator, and logs.

## Producer findings pending review

The shared S3 oracle is normal `405227`, perturbed `405122`.

- Bevy 0.19.0: actual Bevy ECS binary; N1 `405227`, N2 `405227`, FI `405122`; producer disposition `PROVISIONAL_S3_PASS_FOR_COMPARISON_PENDING_REQUIRED_REVIEW`.
- Defold 1.13.0: Bob archive/headless bundle plus produced engine process; N1 `405227`, N2 `405227`, FI `405122`; same provisional producer disposition.
- Godot 4.7.1-stable: exact digest-bound headless Godot process; N1 `405227`, N2 `405227`, FI `405122`; same provisional producer disposition.
- Unity 6000.5.6f1: `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY` because unattended editor activation/account-license state is not repository-self-grantable.
- Unreal Engine 5.8: `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY` because Epic-linked entitlement/preseeded engine acquisition is not repository-self-grantable.

Issue #82's historical 50 `NOT_RUN` cells remain unchanged and are explicitly preserved in the new packet.

## Retained failed/remediation provenance

- Run `31895282641`, evidence commit `5d6b940ee3c57ac78f0d40a890cdc6d48891fd4c`, artifact `9249633980` / `sha256:dee70cb19ad8ae254e69914d5cdc0b15902aaf8410971d14217b0162868d5135`: Godot executed; Bevy failed retained-lock root-package identity; Defold missing input binding.
- Run `31895462621`, evidence commit `67848934b336aa7cde5e391d5cb7fef1766cf462`, artifact `9249687249` / `sha256:f2258a90ccd47faa6f78bc864fc3578821ca047d6abfd5f08ac7c33d6a578d2a`: Bevy and Godot executed; Defold compiled but bundle failed because archive generation was omitted.
- Run 3 preserves its own pre-remediation Defold result under `producer_remediation_history`, then applies the bounded Bob `--archive` correction and executes the headless bundle.

## Exact required review attacks

Reviewer must inspect the exact producer branch/PR packet and attack:

1. whether each claimed executed cell truly ran candidate-native engine/library code rather than a smoke/version-only surrogate;
2. equivalence of the S3 transition implementation across Bevy, Defold, Godot, and the common oracle;
3. correctness and independence of expected checksum derivation;
4. fresh workspace/reset semantics for N1/N2/FI;
5. `FI-S3-INPUT-PERTURB-v2` semantics and distinguishability;
6. exact toolchain/content identity and retained locks/digests;
7. failed-attempt preservation and the Defold archive remediation, including whether any build-only evidence leaked into PASS;
8. Unity/Unreal `BLOCKED_BY_SPECIFIC_AUTHORITY` classification under directive `5303081124`;
9. preservation of Issue #82 historical provenance;
10. absence of engine ranking/selection or readiness inflation from a partial S3-only tranche.

## Authority boundary

No engine ranking/selection, S1/S2/S4-S10 completion, implementation/production readiness, commercial provider/legal/platform/release authority, verification-PASS authority, decision authority, canonical status, or integration authority is granted here. Any integration remains separate, explicitly authorized, and squash-only.
