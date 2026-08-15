# W2-ENG-TECH-S3-REV-01 — Required review of public-toolchain S3 empirical tranche

**Issue:** #353  
**Task class:** `REQUIRED_REVIEW`  
**Review mode:** `DEGRADED_SINGLE_AGENT`, fresh role episode distinct from the producer episode but not represented as independently isolated.  
**Claim:** `5303187679`  
**Base:** `main@9f6c91031ca715f1c57da4ff047cfce6f4b5550c`  
**Canonical binding:** Bootstrap #6 terminal binding `5245368879`; program blob `e3120ec203c4156328770aa86c12fbb7187966dc`; activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e` remains in main ancestry.  
**Judged producer:** Issue #351 terminal `5303181547`, exact head `609d463077725acc2c23c894154cca169d6a75fc`, work/report commit `9b601d8bee3f5c713344bbd27e308e31bc2e3ebc`, draft PR #352.  
**Disposition:** **CHANGES_NEEDED — 0 BLOCKER / 1 MAJOR / 0 MINOR**.

The producer branch was treated as immutable judged input. The review distinguishes two questions that the producer packet currently conflates: (1) whether real candidate-native processes produced the reported deterministic observations, and (2) whether those observations satisfy the reviewed `W2-ENG-HARNESS-v5` authority-bearing evidence envelope required to become trusted W2-ENG comparison evidence. The first question survives review for Bevy, Defold, and Godot; the second does not. Therefore no executed cell may yet be upgraded to `PASS_FOR_COMPARISON` or equivalent trusted comparison authority.

This review grants no integration, canonicalization, engine ranking/selection, implementation/readiness, production/commercial/provider/legal/platform/release, verification-PASS, or decision authority.

## 1. Exact input, artifact, and provenance checks

The exact final empirical inputs are internally coherent:

- producer final trigger `a8023054415fb941ff6ee743ee28387baaf5ace3`;
- generated evidence commit `899e0011f49ce8a73f8b543a1c4b054ce517e715`;
- Actions run `31895624493`, attempt 1;
- Actions artifact id `9249732138`, name `w2-eng-tech-s3-01-31895624493-1`;
- GitHub artifact digest `sha256:068e5ee0df2802d4f52486d0ea42932bb99eaa7a04098298bca8586e65a68c72`;
- independently downloaded artifact ZIP SHA-256: `068e5ee0df2802d4f52486d0ea42932bb99eaa7a04098298bca8586e65a68c72`, exact match;
- contained `evidence.json` independently hashed to `411641a6fbd6a27bd81adf5747c1bb961e5490fdae72d1eea15ac700dd8c85ca`, exact match to the committed/report-declared evidence identity;
- harness validator source SHA-256 `9a50e3e21279a7a94836d6162fee218a0e187bafe292847fd5f0b108df45deea`, matching reviewed v5;
- retained Bevy Cargo.lock SHA-256 `fd7e1276ff5c8cde22d98c0932f70eb39383d9b60ac2d15f11d921dfa71218b0`;
- toolchain artifact lock SHA-256 `23f71143c3771df2f438b899a7a948e58da93bc15a3defe9cf3fb5e2b9147daf`.

The producer also preserves the first two failed/remediation runs by immutable generated commits/artifacts and records the run-3 pre-remediation Defold result under `producer_remediation_history`. No hidden overwrite of the failed attempts was found.

Issue #82 remains the frozen historical predecessor. Its 5-candidate × S1–S10 = 50 historical `NOT_RUN` cells are not rewritten by the new packet.

## 2. Independent S3 oracle and transition-equivalence attack

The documented S3 transition was independently recomputed without reading the producer checksum constants as an oracle:

- initialize 32 entity values as `i*17 + (424242 % 97)`;
- execute 600 ticks;
- normal action `a = (tick + 424242) % 10`;
- injected run changes the action at tick 137 to `(a + 1) % 10`;
- entity index `(tick*7 + a) % 32`;
- update selected value by `a*3 + (tick % 11) + 1`, modulo `1000003`;
- final weighted checksum `sum((i+1)*value[i]) % 1000000007`.

Fresh recomputation yields normal `405227` and injected `405122`, matching the producer.

A source-level comparison of the Python oracle, Bevy Rust, Defold Lua, and Godot GDScript found the same initialization, tick count, action calculation, tick-137 perturbation, entity index, update, moduli, and final checksum. No candidate-specific easier transition was found.

## 3. Candidate-native process authenticity

### Bevy 0.19.0

The producer does more than invoke Cargo or a version command. It builds a binary whose source imports `bevy::prelude::*`, creates a Bevy `World`, installs a Bevy `Resource`, and performs the S3 state mutation through that resource. The corrected root package identity is `everfield_bevy_probe`, matching the retained Cargo.lock, and `cargo build --locked` prevents dependency-resolution mutation.

The final evidence executes copied candidate binaries from three distinct attempt workspaces. Raw stdout is:

- N1: `EVERFIELD_S3:405227`;
- N2: `EVERFIELD_S3:405227`;
- FI: `EVERFIELD_S3:405122`.

All three exit successfully. This is credible real Bevy-library execution rather than smoke-test laundering.

### Defold 1.13.0

Run 1 failed before valid project input construction. Run 2 advanced through compilation but Bob bundling failed because archive generation had not been requested. Run 3 retains that pre-remediation result, then performs the bounded `--archive` correction.

The final Bob command uses the exact digest-bound `bob-1.13.0.jar`, produces a headless Linux bundle, and the attempt commands execute the produced `EverfieldS3` engine process rather than Bob itself. Raw process output contains the Defold engine runtime banner/initialization followed by:

- N1: `EVERFIELD_S3:405227`;
- N2: `EVERFIELD_S3:405227`;
- FI: `EVERFIELD_S3:405122`.

All three final engine processes exit successfully. Build-only evidence was not used as the positive result.

### Godot 4.7.1-stable

Each attempt runs the exact digest-bound Godot executable with `--headless --path` against a separately generated project/script workspace. Raw output identifies `Godot Engine v4.7.1.stable.official.f5f3b3f78` and reports:

- N1: `405227`;
- N2: `405227`;
- FI: `405122`.

All three exit successfully. This is candidate-native engine execution.

### Unity / Unreal Engine

The final packet does not manufacture credentials or convert network reachability into execution. The retained toolchain probes show public vendor/network reachability but no repository-self-grantable unattended Unity activation/license input and no repository-self-grantable Epic-linked Unreal entitlement/preseeded engine input. Under owner directive `5303081124`, keeping these exact S3 cells `NOT_RUN/BLOCKED_BY_SPECIFIC_AUTHORITY` is correctly scoped and does not globally block the technically executable public-toolchain cells.

## 4. Workspace, reset, and injection attack

For each executed candidate, N1, N2, and FI use distinct temporary workspace paths and distinct evidence `workspace_id` / `reset_id` values. The perturbation is passed through `EVERFIELD_PERTURB=1` to the actual candidate process; each candidate source reads that environment variable and changes the tick-137 action. The normal attempts agree and the injected attempt differs exactly as independently predicted.

The workflow is also run inside a fresh Actions checkout and the S3 runner uses a fresh top-level `TemporaryDirectory`; the attempt workspaces are created under that run-local root. This is strong raw evidence of independent process/workspace execution. However, the producer's `reset_verified` field is assigned `True` by `record()` rather than being the output of the reviewed v5 attempt-envelope validator or a separately evidenced reset-verification operation. That defect is included in the MAJOR finding below rather than treated as a second finding.

## 5. MAJOR finding

### W2-ENG-TECH-S3-REV-M01 — Real attempts are not bound into the reviewed v5 authority-bearing evidence envelope

**Severity:** MAJOR / blocking comparison authority.  
**Disposition:** `CHANGES_NEEDED`.

The current raw engine observations are credible, but the producer labels them `PROVISIONAL_S3_PASS_FOR_COMPARISON_PENDING_REQUIRED_REVIEW` without constructing the formal `W2-ENG-HARNESS-v5` generation/adaptation/AttemptRecord envelope that the reviewed harness requires before `PASS_FOR_COMPARISON` can exist.

The exact reviewed v5 validator requires, among other things:

1. an authority-bearing candidate adaptation with exact `candidate_id`, `scenario_id`, `harness_id`, `feature_slice_id`, all fixed common input refs, obligation mappings, minimum bounds, required failure injections, cold/reconstruct/common-resource `start_profile`, and S3 `REAL_OR_SHARED_RULES` mechanism authority;
2. a deterministic adaptation binding identity;
3. a candidate generation and candidate work identity;
4. every retained AttemptRecord bound to the exact `candidate_generation_id` as well as candidate/scenario identity;
5. closed attempt shape, result/failure semantics, reset/workspace/resource fields, and exact required-injection identity;
6. unique one-to-one `run_registry_refs` and `all_attempt_refs` covering all retained attempts;
7. actual validation/aggregation of that generation through v5 before `PASS_FOR_COMPARISON` authority can be emitted.

The producer's final `evidence.json` does not contain an adaptation object or `adaptation_binding_id`; it has no candidate generation/work identities; its attempts omit `candidate_generation_id`; and it has no v5 `run_registry_refs` / `all_attempt_refs`. The workflow executes the v5 validator only against the validator's own regression fixture corpus. It does not construct the real Bevy/Defold/Godot packet as a v5 generation and does not call v5 adaptation validation/aggregation on these empirical attempts.

Consequently, a green workflow proves that the reviewed harness fixture suite still passes and that the producer's custom evidence-envelope assertions pass. It does **not** prove that these actual empirical records satisfy v5's authority-bearing comparison envelope. The hard-coded `reset_verified=True` is another symptom of the same missing binding: the final comparison claim is outside the validator that is supposed to adjudicate those fields.

This is not a finding that the engines failed to run, that the checksums are false, or that the common S3 transition is inconsistent. It is a finding that credible raw observations have not passed the repository's reviewed comparison-authority gate. Required review cannot substitute its own prose judgment for that executable gate.

### Required correction

A bounded remediation must preserve the immutable run-1/run-2/run-3 provenance and then bind the exact final empirical observations to the reviewed v5 contract. At minimum it must:

- construct one exact S3 adaptation per executed candidate with the required fixed refs, all four obligations, minimum bounds, `FI-S3-INPUT-PERTURB-v2`, the common cold/reconstruct/resource start profile, and `REAL_OR_SHARED_RULES` mechanism authority;
- derive deterministic candidate generation/work identities tied to the exact engine/toolchain/build/run evidence;
- emit v5-conformant AttemptRecords including `candidate_generation_id` for N1/N2/FI;
- emit exact one-to-one retained-attempt registries;
- justify `reset_verified` from the actual reconstruction/reset evidence rather than asserting it as an unchecked custom field;
- feed the resulting exact final candidate generations through the unchanged reviewed v5 adaptation validator and aggregate function, preserving the emitted aggregate and reasons;
- retain the historical failed producer/remediation runs without laundering them into the final generation or deleting their provenance;
- fail closed: no cell becomes trusted comparison evidence unless the exact reviewed v5 aggregate for that candidate/S3 generation is `PASS_FOR_COMPARISON`.

The existing real-engine run need not be repeated merely to change serialization if the remediation can bind all required v5 fields from immutable evidence without invention. If a required field—especially reset/reconstruction evidence—cannot be established from the retained run, that candidate must be rerun rather than fabricated.

## 6. Authority-inflation and historical-provenance checks

No producer claim of S1, S2, or S4–S10 completion was found. The packet explicitly prohibits partial-candidate ranking, records `engine_selected=false`, and grants no implementation/production readiness, provider permission, verification-PASS, decision, canonical, or integration authority. Unity/Unreal remain exact authority-bound S3 `NOT_RUN` cells, not global blockers.

The producer report/handoff accurately distinguish this fresh episode from Issue #82's historical 50 `NOT_RUN` cells. The old episode is retained rather than rewritten.

These boundaries are correct and must remain unchanged in remediation.

## 7. Review result and next route

**Disposition: `CHANGES_NEEDED`.** The raw deterministic execution facts for Bevy, Defold, and Godot are well supported, and the common oracle/injection survive review. Nevertheless, the required reviewed v5 comparison envelope is absent, leaving **1 unresolved MAJOR**. Therefore none of the three cells may yet be consumed as trusted W2-ENG `PASS_FOR_COMPARISON` evidence.

The next lawful route is a bounded blocking remediation/revision that binds the existing empirical evidence into the unchanged reviewed v5 adaptation/generation/AttemptRecord/registry/aggregation contract, or reruns only where a required field cannot be evidenced. Producer PR #352 must remain unintegrated while this finding is open.

After that remediation terminalizes, a fresh required review of the exact remediated packet is required. Integration remains separate from review and, if later authorized, squash-only. This review itself grants no integration authority.
