# W2-ENG-TECH-S3-REM-01 — v5 comparison-envelope remediation

Status: **producer remediation ready for fresh required review**. This packet closes only the structural v5-envelope defect identified by Issue #353. It does not itself create reviewed comparison authority or any integration authority.

## Binding and source provenance

- Remediation issue: #355; claim `5303217026`; branch `planning/issue-355`.
- Base: `main@9f6c91031ca715f1c57da4ff047cfce6f4b5550c`.
- Canonical binding: Issue #6 terminal `5245368879`; program blob `e3120ec203c4156328770aa86c12fbb7187966dc`.
- Source producer: Issue #351 terminal `5303181547`, exact producer head `609d463077725acc2c23c894154cca169d6a75fc`.
- Blocking review: Issue #353 terminal `5303205496`, finding `W2-ENG-TECH-S3-REV-M01`.
- Exact retained empirical source: run `31895624493`, generated evidence commit `899e0011f49ce8a73f8b543a1c4b054ce517e715`, artifact `9249732138` / `sha256:068e5ee0df2802d4f52486d0ea42932bb99eaa7a04098298bca8586e65a68c72`.
- Exact retained source `evidence.json` SHA-256: `411641a6fbd6a27bd81adf5747c1bb961e5490fdae72d1eea15ac700dd8c85ca`.
- Historical failed producer runs remain separately referenced: run `31895282641` artifact `9249633980`, and run `31895462621` artifact `9249687249`. Issue #82's historical 50 `NOT_RUN` cells remain unchanged.

The remediation workflow fetches `planning/issue-351`, materializes the source evidence with `git show 899e001...:docs/planning/wave-2/evidence/ci/engine-technical-s3/evidence.json`, and verifies its exact SHA-256 before conversion. It does not consume a rewritten copy or producer prose as source authority.

## Unchanged reviewed v5 gate

The binder imports the repository's unchanged `W2-ENG-PROTOCOL-VALIDATOR-v5` from `docs/planning/wave-2/evidence/engine-spike-protocol-fixtures.py` only after verifying validator SHA-256 `9a50e3e21279a7a94836d6162fee218a0e187bafe292847fd5f0b108df45deea`.

For Bevy, Defold, and Godot it creates exact S3 adaptations using the reviewed validator's own `adaptation()` implementation and obtains `va(...)=ACCEPT`. Each adaptation therefore carries the required common inputs, obligation mappings, bounds, `FI-S3-INPUT-PERTURB-v2`, cold/reconstruct/common-resource start profile, and `REAL_OR_SHARED_RULES` mechanism authority.

Candidate work and generation identities are deterministic hashes of the immutable source evidence, source producer identity, exact candidate/toolchain/build evidence, and source attempt identities. Each converted AttemptRecord contains `candidate_generation_id`; exact `run_registry_refs` and `all_attempt_refs` cover the full final generation.

## Source-to-formal conversion gate

No source attempt becomes a formal PASS merely because the producer marked it PASS. Before conversion the binder independently requires:

- exact candidate/scenario identity and exactly N1/N2/FI1;
- exact required injection identity;
- source `result=PASS` / `failure_class=NONE`;
- process exit 0 and `timed_out=false`;
- expected and observed checksum `405227` for normal or `405122` for injected;
- common resource class `W2-ENG-HOST-COMMON-v2`;
- unique reset and workspace identities;
- candidate-native command explicitly bound to the attempt-specific `/runs/<candidate>/<N1|N2|FI1>` workspace.

`reset_verified` is then derived from unique reset/workspace identities, command-to-attempt-workspace binding, and a fresh successful candidate process for each attempt. The producer's original `reset_verified` boolean is deliberately not consumed.

Every formal attempt has a separate machine-readable source binding back to its exact source attempt JSON pointer, checksum, process command digest, exit state, and timeout state.

## Remediation CI result

- Trigger SHA: `ce608f2b890425c08900177ab10be12905f1e3bc`.
- Actions run: `31896413284`, attempt 1, conclusion `success`.
- Run-generated evidence commit: `08d10351ad4bb56a9f4f0a7017258f28bd47c383`.
- Artifact: `9249912272`, `w2-eng-tech-s3-v5-rem-01-31896413284-1`, digest `sha256:04c32d8d6c1d3d7642eb595adb10957c134d18c3d7642f9186633a327546f092`.
- Remediation packet SHA-256: `a427cca4dddeb8b5c8d8b42261cbe6c7e88a47946cb36fa2411ccaf09f98ffd0`.

Unchanged v5 aggregate results are exact:

| Candidate | Adaptation | v5 aggregate | Envelope |
|---|---|---|---|
| Bevy | `ACCEPT` | `PASS_FOR_COMPARISON` | `valid_envelope=true` |
| Defold | `ACCEPT` | `PASS_FOR_COMPARISON` | `valid_envelope=true` |
| Godot | `ACCEPT` | `PASS_FOR_COMPARISON` | `valid_envelope=true` |

These are **remediation producer outputs pending fresh review**, not yet reviewed comparison facts.

## Negative self-tests

All required negative tests passed fail-closed:

- missing `candidate_generation_id` cannot aggregate PASS;
- mechanism authority downgraded below `REAL_OR_SHARED_RULES` is rejected;
- duplicate registry reference cannot aggregate PASS;
- reused reset/workspace yields non-PASS (`NOT_RUN`);
- checksum substitution is rejected by source conversion;
- substituted source evidence hash is rejected;
- a formal attempt lacking a source binding is rejected by the binder packet gate.

## Preserved boundaries

Unity and Unreal Engine remain exact `NOT_RUN/BLOCKED_BY_SPECIFIC_AUTHORITY`; no formal PASS generation is fabricated for either. No S1/S2/S4-S10 cell is completed. No engine ranking/selection, implementation or production readiness, provider/commercial/legal/platform/release permission, verification-PASS, decision, canonical, or integration authority is created.

The machine evidence is authoritative for exact process/version strings. Any earlier prose transcription mismatch in a version suffix does not change the source artifact/evidence identity and is not used by this remediation gate.

## Required next route

Fresh independent/degraded-independent review must cross-check the exact source evidence hash/artifact against the remediation source snapshot, conversion fidelity, reset derivation, adaptation/generation/AttemptRecord/registry structure, unchanged validator identity, all negative tests, exact v5 aggregate outputs, failed-history preservation, Unity/Unreal boundaries, and authority inflation.

Only a clean required review can resolve `W2-ENG-TECH-S3-REV-M01` for trusted bounded S3 comparison consumption. Integration remains a separate authority decision and, if later authorized, squash-only.
