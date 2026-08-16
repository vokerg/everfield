# W2-ENG-TECH-S5-01 — public-toolchain S5 merge/conflict tranche

Status: **producer evidence complete; fresh required review still mandatory**.

Authority: bounded noncanonical planning evidence only. Nothing in this packet selects an engine, completes the five-candidate comparison, grants implementation/readiness/production/provider/legal/platform/release authority, establishes verification-PASS, authorizes integration, or changes canonical status.

## Frozen authority and claim

- Issue: `#433` / `W2-ENG-TECH-S5-01`
- winning schema-3 claim: `5308441704`
- claim/base main: `3de6f8f276cd1479ceccdea7362420f1e0efa030`
- current main observed before terminal reporting: `cf65031bfa3275b674e8232734176cac67485c8d`
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical binding comment: `5245368879`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- owner convergence directive: Issue #84 comment `5277825639`
- owner parallel-frontier directive: Issue #84 comment `5305563203`
- validator path: `docs/planning/wave-2/evidence/engine-spike-protocol-fixtures.py`
- validator blob: `2c646988dc16e212f43df6a4ee5ce646622ac2a6`
- validator byte SHA-256 in final run: `9a50e3e21279a7a94836d6162fee218a0e187bafe292847fd5f0b108df45deea`
- harness / feature / scenario authority: `W2-ENG-HARNESS-v5` / `W2-ENG-FEATURE-SLICE-v2` / `W2-ENG-SCENARIO-INPUTS-v2`

The branch remained owned only by the claim above. `main` advanced concurrently through disjoint reviewed WSN/provider publication work; no such advancement changed the frozen S5 validator or S4 predecessor authority.

## Reviewed predecessor

S5 continues the exact reviewed S4 line:

- remediation Issue #364 terminal `5305583040`
- fresh review Issue #374 terminal `5305617167`
- review disposition `PASS_BOUNDED_REMEDIATED_S4_V5_ENVELOPE`, 0 BLOCKER / 0 MAJOR / 0 MINOR
- review provenance publication `b0b87a4ca05f7f21595bb2303978cb7dd0d5791e`
- reviewed remediation publication `6f9e56f1d822ed2e2b18fa10a2bf29927efebe3e`

No S4 result is rewritten by this episode.

## Exact S5 contract executed

The unchanged v5 S5 contract requires:

- fixed refs: `SLICE:logical_state`, `SLICE:player_surface`, `SLICE:merge_fixture`
- obligations: `parallel_nonoverlap`, `intentional_overlap`, `visible_conflict`, `post_merge_checks`
- bounds: `overlap_count=2`, `branch_a_nonoverlap=1`, `branch_b_nonoverlap=1`
- injection: `FI-S5-OVERLAP-v2`
- semantic overlap locations:
  - `STATE:entity-07.status`
  - `UI:SETTINGS.control-02.label`
- generated collision when candidate-generated metadata exists: **required**
- common cold/reconstruct resource class: `W2-ENG-HOST-COMMON-v2`
- candidate mechanism authority: `CANDIDATE_NATIVE_EQUIVALENT`

For each represented public candidate, N1 merges branch A then B and N2 merges B then A with one independent non-overlap edit per branch. FI1 gives both branches incompatible edits at both required semantic locations and independently generates `generated/candidate-metadata.txt` from the actual candidate process. The merge must expose all three conflicts. Resolution takes state from branch A (`ACTIVE`), UI label from branch B (`Volume`), then regenerates metadata from the resolved candidate state. Candidate-native post-merge execution must succeed.

## Implementation identity

Final run identity records:

- base runner SHA-256: `59dcb0bce2c2037d35370ef49306f2964f49871f7d91ebc11c98e918cae502b0`
- first correction entry SHA-256: `5e98ab3a29b61425df8db729cc7c90a880b61953baa63a85350a5ace6c768210`
- final correction entry v2 SHA-256: `d6786f04a6d505201dbee4f900e2813a06126d0cf7342b341642ff4cb51e8b68`
- independent verifier SHA-256: `cea0f839d39722bea7971bfcfc836cab53b257c96f19f7aeeb4f5636f931fcd7`
- toolchain probe SHA-256: `bf7de805a0bb941055466c4972d0f405b14f19f7e8d7196c9db07ab568fc5eac`
- retained Bevy lock SHA-256: `fd7e1276ff5c8cde22d98c0932f70eb39383d9b60ac2d15f11d921dfa71218b0`
- retained artifact-lock SHA-256: `23f71143c3771df2f438b899a7a948e58da93bc15a3defe9cf3fb5e2b9147daf`

The final v2 correction is narrowly fail-closed: Defold prefixes script output with `DEBUG:SCRIPT:`; the parser searches for the exact marker `EVERFIELD_S5_METADATA:` within a line and retains only the exact suffix. The final candidate identity binds the v2 entry plus predecessor entry identity.

## Producer correction / failed-run provenance

No failed or incomplete producer packet is promoted.

1. Run `31959088675`, artifact `9266757869`, digest `sha256:aaec74a44c4de8e4b8e0843c764afbdaa26e8e39bb5af478172a37491d1d5b84`, evidence SHA-256 `a8dca2083d0c5f132e74f410f49fab4b3687914a8281189718fe5001ba897bbe`.
   - defect: `BEVY_RETAINED_LOCK_ROOT_PACKAGE_IDENTITY_MISMATCH`
   - Bevy was correctly retained `INCONCLUSIVE`; no Bevy result from this run is promoted.
2. Run `31959336546`, artifact `9266839656`, digest `sha256:4bb52e98c7e77a1adcfe6106e06d9de23acadc9cbe01d09aed8cea7f33bd92ca`, evidence SHA-256 `51f43ec15093b21e95a2b8d5f4f1896efc70bc23c0a6a397ab5e228578b3ef6b`.
   - defect: generated-metadata collision required by exact v5 feature slice was not exercised.
   - otherwise-clean S5 generations from this run remain incomplete producer provenance only.
3. Run `31959682648`, artifact `9266948644`, digest `sha256:dacf1e880a4ffc24de3919a4d4e1f44cf8eb4a1d499eaf8b5f8118977393836c`.
   - partial metadata-collision correction executed, but the then-stale independent verifier rejected the new three-conflict shape; persistence failed safely because the branch had advanced.
4. Run `31959719316` was cancelled by workflow concurrency while superseded by a newer exact correction head; it created no promoted packet.
5. Run `31959757285`, artifact `9266994724`, digest `sha256:c1fd4cc41c989af24b38727f9c1e481b364678ec056ab2c1e9eda1636034a827`, evidence SHA-256 `17d9f597566642f1dda1d621dc940942d08bfbbdf077ab93f83de2a105c3167a`.
   - defect: `DEFOLD_METADATA_LOG_PREFIX_PARSER_MISMATCH`.
   - Defold processes exited 0 and emitted correct metadata under the normal `DEBUG:SCRIPT:` prefix, but the producer parser required the marker at column zero; the Defold FI generation was correctly retained `INCONCLUSIVE` rather than promoted.

## Final empirical packet

Final trigger / run / generated evidence:

- trigger SHA: `f515bbcba6e53f56534bce5f58a3869d006aa3d5`
- Actions run: `31960259059`, attempt 1, conclusion `success`
- runner image: `ubuntu24` / `20260810.271.1`, `Linux X64`
- generated evidence commit: `c8e5b102c8f1798e7df7c631f8344ea203d22cb0`
- artifact: `9267094933`, `w2-eng-tech-s5-01-31960259059-1`
- artifact digest: `sha256:1dd12fb8436b0949ccf890dfb2a7233a5e73335cdfbb17d633b0c1b8e4bfd55c`
- `evidence.json` SHA-256: `3e7dfdf8323caeb061027e2435fb6a3c20748802c34d10f49c42aa496f5f1107`
- `independent-verification.json` SHA-256: `1ffa031649b7aafeca8cda3c0a33e577a6ac17a27b74f81ed547a221a8704e04`
- independent verifier schema: `W2-ENG-TECHNICAL-S5-INDEPENDENT-VERIFY-v2`
- `all_provisional_verified: true`

### Bevy 0.19.0

- final generation: `GEN-S5-d973bfa614c120e3099bcab7`
- work: `WORK-S5-9416eddd5c88619eee82e3b6`
- N1/N2/FI1: PASS / PASS / PASS
- adaptation: `ACCEPT`
- aggregate: exact `PASS_FOR_COMPARISON`, `valid_envelope=true`
- generated FI metadata:
  - branch A: `ACTIVE|Sound|true|Back`
  - branch B: `PAUSED|Volume|false|Return`
  - resolved: `ACTIVE|Volume|true|Return`
- conflict paths exactly: `src/state.rs`, `src/ui.rs`, `generated/candidate-metadata.txt`

### Defold 1.13.0

- final generation: `GEN-S5-19071a679f17a453a680a2a5`
- work: `WORK-S5-c878e41cc82a6d1af29c1119`
- N1/N2/FI1: PASS / PASS / PASS
- adaptation: `ACCEPT`
- aggregate: exact `PASS_FOR_COMPARISON`, `valid_envelope=true`
- generated FI metadata:
  - branch A: `ACTIVE|Sound|true|Back`
  - branch B: `PAUSED|Volume|false|Return`
  - resolved: `ACTIVE|Volume|true|Return`
- conflict paths exactly: `state.lua`, `settings.lua`, `generated/candidate-metadata.txt`
- metadata is emitted by the built Defold engine process and parsed through the exact marker inside its normal log prefix.

### Godot 4.7.1-stable

- final generation: `GEN-S5-9a4eb68ccb19ba8ca84aa7c9`
- work: `WORK-S5-cd2b8d29d3f915d1a8e1c1ef`
- N1/N2/FI1: PASS / PASS / PASS
- adaptation: `ACCEPT`
- aggregate: exact `PASS_FOR_COMPARISON`, `valid_envelope=true`
- generated FI metadata:
  - branch A: `ACTIVE|Sound|true|Back`
  - branch B: `PAUSED|Volume|false|Return`
  - resolved: `ACTIVE|Volume|true|Return`
- conflict paths exactly: `state.gd`, `settings.gd`, `generated/candidate-metadata.txt`

For all three candidates, independent verification recomputed the v5 aggregate, reset/source bindings, deterministic generation identity, semantic merge shape, metadata generation/collision/resolution, and all retained negative attacks without findings.

## Negative / fail-closed coverage

The independent verifier confirms all attacks reject as intended for each represented candidate:

- missing required semantic overlap
- lost non-overlap update
- silent overlap acceptance
- generated-metadata collision omission
- generated-metadata resolution bypass
- candidate-native validation bypass
- formal/raw source-binding substitution
- workspace reuse
- toolchain identity substitution

The base producer additionally retains v5-level candidate-generation mismatch, duplicate registry, raw/source substitution, formal/raw binding substitution, and post-merge validation negatives. No expectation mismatch is averaged away.

## Blocked candidates and preserved history

- Unity 6000.5.6f1: `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY`
- Unreal Engine 5.8: `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY`
- Issue #82 historical 50 `NOT_RUN` cells remain immutable.
- Reviewed S3/S4 provenance remains separate and unchanged.

Provider-effective evidence published concurrently on current `main` still leaves Unity blocked by a specific external condition and Unreal not configured; it does not grant S5 execution authority and was not used to fabricate either candidate.

## Producer disposition and self-review

Producer disposition: `PARTIAL_EMPIRICAL_S5_EVIDENCE_READY_FOR_REVIEW`.

“Partial” means three lawfully executable public candidates have complete producer evidence while Unity/Unreal remain exact authority-bound `NOT_RUN`; it does **not** mean any of the three represented public generations is incomplete.

Self-review after the final run:

- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0

The producer found and corrected three material harness/evidence defects before terminalization and preserved each defective packet as predecessor provenance. The final packet is internally consistent with the exact S5 feature-slice requirement, including candidate-generated metadata collision. This self-review is not the required fresh review.

## Required next gate

A fresh independent/degraded-independent required review must freeze the exact terminal producer head and attack at minimum:

- exact claim/head/run/artifact/evidence identities and all predecessor defect provenance;
- candidate-native authenticity for Bevy, Defold and Godot;
- N1/N2 non-overlap preservation in both merge directions;
- both required semantic conflict locations;
- mandatory candidate-generated metadata collision and post-resolution regeneration;
- Defold log-prefix parser correction and fail-closed marker semantics;
- post-merge native execution/build validity;
- reset/workspace/source/toolchain/generation binding;
- unchanged v5 `va()` / `agg()` semantics and exact final aggregate;
- negative attacks and no historical-evidence laundering;
- Unity/Unreal authority classification;
- authority inflation.

No S5 generation becomes trusted reviewed comparison evidence until that review terminalizes cleanly. Any later publication/integration is a separate authority episode and must be squash-only.
