# Issue #353 handoff — W2-ENG-TECH-S3-REV-01

## Terminal route

`CHANGES_NEEDED`

Required review found **0 BLOCKER / 1 MAJOR / 0 MINOR**. The raw Bevy/Defold/Godot S3 executions are credible and independently checksum-consistent, but the producer packet does not pass the reviewed `W2-ENG-HARNESS-v5` comparison-authority envelope. No executed S3 cell is yet trusted `PASS_FOR_COMPARISON` evidence.

## Ownership and judged input

- Review issue: #353.
- Winning claim: `5303187679`.
- Review mode: `DEGRADED_SINGLE_AGENT`.
- Review branch: `planning/issue-353`.
- Review base: `main@9f6c91031ca715f1c57da4ff047cfce6f4b5550c`.
- Canonical binding: Issue #6 `5245368879`, program blob `e3120ec203c4156328770aa86c12fbb7187966dc`.
- Judged producer: Issue #351 terminal `5303181547`.
- Producer exact head: `609d463077725acc2c23c894154cca169d6a75fc`.
- Producer work/report commit: `9b601d8bee3f5c713344bbd27e308e31bc2e3ebc`.
- Producer draft PR: #352.
- Final empirical run: `31895624493`, attempt 1.
- Generated evidence commit: `899e0011f49ce8a73f8b543a1c4b054ce517e715`.
- Artifact id: `9249732138`.
- Artifact digest: `sha256:068e5ee0df2802d4f52486d0ea42932bb99eaa7a04098298bca8586e65a68c72`.
- Evidence JSON SHA-256: `411641a6fbd6a27bd81adf5747c1bb961e5490fdae72d1eea15ac700dd8c85ca`.
- Review report: `docs/planning/wave-2/reviews/w2-eng-technical-s3-independent-review.md`.

## Findings that survived review

The final artifact was freshly downloaded and its ZIP SHA-256 exactly matched the GitHub artifact digest. Its evidence JSON independently hashed to the producer-declared SHA-256.

The S3 transition was independently recomputed and yields normal checksum `405227` and tick-137 injected checksum `405122`.

Source and raw command/output inspection support actual candidate-native execution:

- Bevy 0.19.0: Bevy `World`/`Resource` code, two normal process executions `405227`, required injection `405122`.
- Defold 1.13.0: exact Bob artifact, archive-enabled headless bundle, actual produced Defold engine process, two normal `405227`, injection `405122`; earlier failed bundling provenance retained.
- Godot 4.7.1-stable: exact digest-bound headless Godot process, two normal `405227`, injection `405122`.
- Unity 6000.5.6f1 and Unreal Engine 5.8 remain exact `NOT_RUN/BLOCKED_BY_SPECIFIC_AUTHORITY` cells. No credential/provider authority was fabricated.
- Issue #82's historical 50 `NOT_RUN` cells remain immutable and were not rewritten.
- No S1/S2/S4-S10 completion, engine ranking/selection, readiness, provider/legal/platform/release, verification-PASS, decision, canonical, or integration authority is claimed.

## Blocking finding

### W2-ENG-TECH-S3-REV-M01 — missing v5 authority-bearing evidence envelope

The reviewed v5 harness requires each comparison-eligible candidate generation to carry and validate:

- exact S3 adaptation fields and deterministic binding identity;
- candidate generation/work identity;
- v5 AttemptRecords including `candidate_generation_id`;
- exact unique `run_registry_refs` and `all_attempt_refs`;
- closed result/failure/reset/workspace/resource semantics;
- validation/aggregation through the unchanged reviewed v5 implementation before `PASS_FOR_COMPARISON` exists.

The producer's `evidence.json` has no adaptation object/binding, no generation/work identity, no `candidate_generation_id`, and no retained-attempt registries. Its workflow executes the v5 validator against the validator's own fixture corpus but does not feed the actual Bevy/Defold/Godot empirical records through v5 adaptation validation and aggregation. `reset_verified` is also assigned `True` by the custom producer recorder rather than adjudicated in the reviewed envelope.

Therefore credible raw observations cannot yet be promoted to trusted W2-ENG comparison evidence. Required review cannot substitute prose judgment for the executable reviewed gate.

## Required next route

Highest-priority continuation is a bounded blocking remediation/revision that preserves all producer provenance and either:

1. binds the retained exact final run into v5-conformant S3 adaptations/generations/AttemptRecords/registries and obtains exact v5 aggregate `PASS_FOR_COMPARISON`; or
2. reruns only those candidate cells for which a required v5 field cannot be established from immutable retained evidence.

The remediation must not edit or rewrite the terminal Issue #351 branch. It must fail closed and retain run-1/run-2/run-3 provenance. A fresh required review is mandatory after remediation.

Producer PR #352 must remain unintegrated while this finding is open. Review integration, if ever separately authorized, is noncanonical provenance only and squash-only; this review itself grants no integration authority.
