# Handoff — Issue #341 / W2-CI-REV-01

## Lifecycle

- task class: `REQUIRED_REVIEW`
- reviewer branch: `planning/issue-341`
- claim comment: `5302463048`
- review mode: `DEGRADED_SINGLE_AGENT`
- source main: `92204cb2e58c792ef4199fe3562ca2192096f5c0`
- canonical binding: Bootstrap Issue #6 terminal binding comment `5245368879`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- review work commit: `2581e941cf3b1a06cc8b4495b56163a9cfa2d8a7`
- review artifact blob: `f7bc414c8a66c72b50fcb01cb992086f403fe245`
- disposition: `CHANGES_NEEDED`
- findings: `0 BLOCKER / 3 MAJOR / 0 MINOR`
- integration authority: none

## Frozen producer input

- producer issue: #339 / `W2-CI-ENABLE-01`
- producer terminal status: `5302456876`
- producer work: `8b03470f0772bc6a85a7eb915f27cee82b09a152`
- producer head: `2c0c4759b5de99c9cc292fb473888b0d4b2a5564`
- producer draft PR: #340 exact head `2c0c4759b5de99c9cc292fb473888b0d4b2a5564`
- report blob: `794a041bdd1fb59d6928b7dae9a6bd5c9ee09084`
- workflow blob: `7a83f560bfd81c91aeeedfd184679739918cd1f9`
- probe blob: `571ec96fabb0c192c83357e7a9213ae6599e4d38`
- machine capability blob: `c1ab5ca0d1944c0ec3d3e84fca112eb06081e232`
- declared machine SHA-256: `6926cf69a9e2f1a5b7a19a3ede76781045af73a02ac350bbda71ccb66c9d473d`
- CI validator output blob: `2c234e67de118659da18be582341763e2315e82f`
- producer handoff blob: `2a91f1fae287252bdc7244948bb84dbafc848d1b`

## Run provenance checked

- corrected run: `31887219066`, trigger `2517a5b62f760f916080a152d5f74269c2f65f47`, conclusion `success`
- corrected generated-evidence commit: `8ddea765c31ce8091814db41a188bd6cc837ea2f`
- corrected artifact: `9247589148`, digest `sha256:8ca677ac7adfc3a798fdad14611239b7c37a3423c4a3c480c23d2b510ce68854`
- first run: `31887099444`, trigger `6441b5bc67527888a72e0926c35987b27ad7a9c5`, conclusion `success`
- first generated-evidence commit: `c44869cc87b2ce4466b17ecff942d9868fab588b`
- first artifact: `9247557956`, digest `sha256:5a74acc251fa6c5e99230c7426359de3ade434e4859c0692b2be5f14b63d96a8`
- first-run Defold result: `FAILED` under Java 17 with class-file version 69 vs supported 61
- corrected Defold result: successful Bob 1.13.0 invocation under Temurin Java 25.0.4+7

## Findings requiring remediation

1. `W2-CI-REV-M01` — **MAJOR**: probe exits zero unconditionally, so an unexpected candidate `FAILED` can coexist with a green Actions run. Encode fail-closed allowed-state policy while retaining evidence on failure.
2. `W2-CI-REV-M02` — **MAJOR**: Bevy's generated `Cargo.lock` exists only in a temporary directory and is not durably bound; `CAPABLE_WITH_PRESEED` is not reproducibly identified. Persist exact lock/resolution identity and replay it, or narrow the classification.
3. `W2-CI-REV-M03` — **MAJOR**: Defold/Godot release downloads are version-addressed but not content-digest-bound. Record and validate exact cryptographic artifact identities for reproducible replay.

## Claims retained through remediation

- the Java-25 correction is real and first-run failure provenance is retained;
- public Bevy/Defold/Godot bootstrap/invocation occurred in the recorded run, but remains below S1–S10 evidence;
- current harness validator executed successfully in CI;
- Unity unattended activation/account/license material remains a specific non-self-grantable provider input;
- Unreal Engine 5.8 authorized source/prebuilt acquisition remains a specific non-self-grantable provider input;
- no secret values were read;
- W2-ENG #82 remains 50 historical `NOT_RUN`; none were promoted;
- no engine ranking/selection, implementation readiness, provider/legal/platform/release, verification PASS, canonicality, decision, or integration authority is created.

## Next lawful route

The required review fails closed as `CHANGES_NEEDED`. Blocking remediation/revision of the existing W2-CI-ENABLE-01 packet is now the next relevant chain step if/when lawfully routed and unowned. Do **not** create or advance the proposed Unity+Unreal provider-authority/preseed successor until a revised CI capability packet has passed fresh required review.

The bounded remediation should preserve all current producer/run lineage and add only fail-closed status policy, durable Bevy resolution identity, exact Defold/Godot artifact digests, a fresh corrected run, and fresh review.

## Authority boundary

Reviewer only. No producer-branch edits were made. This handoff grants no W2-ENG empirical PASS, engine selection, gameplay/high-throughput implementation, production/readiness, provider/legal/platform/release, canonical, verification-PASS, decision, or integration authority. Any eventual `main` integration remains separately authorized and squash-only.