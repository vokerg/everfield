# Handoff — Issue #343 / W2-CI-REM-01

## Lifecycle

- task class: `BLOCKING_REMEDIATION_REVISION`
- branch: `planning/issue-343`
- winning claim: `5302487090`
- later losing claim: `5302487906`
- base/current-main-at-claim: `92204cb2e58c792ef4199fe3562ca2192096f5c0`
- canonical binding comment: `5245368879`
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- corrected implementation commit: `254d454a4f123fcb32ed66c14fd5829c37daaf8a`
- generated-evidence commit: `892bb9377a3580571c887a00b7521a3496eab6d7`
- remediation work commit: `3cc6f039170ce0c19288426aded252a1081896fb`
- remediation report blob: `a69d0c6b74004a794842be8a6934ac772f07652e`
- disposition: `REMEDIATION_COMPLETE_REVIEW_REQUIRED`
- integration authority: none

## Frozen chain inputs

### Original producer
- Issue #339 / `W2-CI-ENABLE-01`
- terminal status comment `5302456876`
- work `8b03470f0772bc6a85a7eb915f27cee82b09a152`
- head `2c0c4759b5de99c9cc292fb473888b0d4b2a5564`
- draft PR #340

### Required review that routed this remediation
- Issue #341 / `W2-CI-REV-01`
- terminal status comment `5302477689`
- work `2581e941cf3b1a06cc8b4495b56163a9cfa2d8a7`
- head `faae4aa3731cccac48e783631ba4883138fbef8c`
- draft PR #342
- review artifact `f7bc414c8a66c72b50fcb01cb992086f403fe245`
- review handoff `876b5113b1be05c7753e1a8f9972decb83213505`
- disposition `CHANGES_NEEDED`, findings `0 BLOCKER / 3 MAJOR / 0 MINOR`

## Corrected code identities

- workflow `.github/workflows/w2-ci-engine-toolchain-probe.yml`: blob `6573cdf8d855ea92ec110703890a3a1862727a94`
- probe `tools/planning/engine_toolchain_probe.py`: blob `fd41c33b96602714233412bc054b541a0f22628f`
- policy `tools/planning/engine_toolchain_policy.py`: blob `97c574899239616e056a69dd6ed2844f842f9542`

## Fresh CI evidence

- run `31888041342`, attempt 1
- trigger/head `254d454a4f123fcb32ed66c14fd5829c37daaf8a`
- job conclusion `success`
- all material steps success, including final fail-closed policy enforcement
- generated-evidence commit `892bb9377a3580571c887a00b7521a3496eab6d7`
- immutable Actions artifact `9247801348`
- artifact digest `sha256:d4ec43c649024e124bf7ab450d4c8e994575867a89036213fc2533457d1694d1`
- policy-result blob `803f871d733e92e8b6371efb70939faf85c8c741`, `pass=true`, `errors=[]`
- policy-selftest blob `b8f1af897dd070c4a5419e75a9f1ebb31e46271a`, five of five required cases pass
- retained Bevy lock SHA-256 `fd7e1276ff5c8cde22d98c0932f70eb39383d9b60ac2d15f11d921dfa71218b0`
- Bevy lock-sha record blob `01918a17248f9a892f5aacd8e037e5c66ebc3564`
- artifact-lock blob `4a88990ae24768eb4f83a8a1311e2a830834649f`
- Defold `bob.jar` retained SHA-256 `22e651025834603794ba6873b09924f11412dff66eee0e38aaef8955eb534655`
- Godot Linux x86_64 ZIP retained SHA-256 `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`

An independent freeze-time GitHub release-metadata read confirms those Defold/Godot hashes equal the public release-asset digest values. The machine helper itself conservatively labels them `OBSERVED_RUN_TOFU_LOCK` because its generic command capture truncates long stdout before JSON parsing. Exact-content binding and mismatch rejection are nevertheless executable; the next reviewer must independently assess this retained source-label limitation rather than accepting a self-granted upgrade.

## Finding dispositions

1. `W2-CI-REV-M01` — `RESOLVED`: explicit executable allowed-state policy; public `FAILED` rejected; evidence persists before final nonzero enforcement; negative regression cases pass.
2. `W2-CI-REV-M02` — `RESOLVED`: exact Bevy Cargo.lock is persisted, SHA-256-bound, copied into a fresh replay project, and used by `cargo fetch/check --locked`; substitution negative passes.
3. `W2-CI-REV-M03` — `RESOLVED` at exact-content/replay layer: Defold/Godot downloads are SHA-256-bound before execution, retained in artifact lock, policy-checked, and substitution negative passes. Conservative TOFU source label remains visible and requires fresh review.

## Preserved provenance and boundaries

- predecessor corrected run `31887219066` / artifact `9247589148` / digest `sha256:8ca677ac7adfc3a798fdad14611239b7c37a3423c4a3c480c23d2b510ce68854` remains immutable provenance;
- predecessor first run `31887099444` / evidence `c44869cc87b2ce4466b17ecff942d9868fab588b` / artifact `9247557956` / digest `sha256:5a74acc251fa6c5e99230c7426359de3ade434e4859c0692b2be5f14b63d96a8` remains immutable, including Defold Java-17 failure;
- Java-25 correction remains explicit;
- W2-ENG #82 terminal `5276916603` remains 50 historical `NOT_RUN`; no cell was promoted;
- fresh machine status remains Bevy `CAPABLE_WITH_PRESEED`, Defold/Godot `CAPABLE`, Unity/Unreal `BLOCKED_BY_SPECIFIC_EXTERNAL_AUTHORITY`;
- Unity unattended account/license/activation and Unreal 5.8 Epic-authorized source/prebuilt access remain specific provider-authority inputs;
- no credentials were consumed to manufacture authority.

## Next lawful route

Route exactly one fresh required independent/degraded-independent review of this exact remediation packet. The reviewer must treat this branch as immutable, explicitly re-attack M01/M02/M03, the TOFU source-label limitation, regression behavior, historical provenance, and authority inflation. Do not advance the Unity+Unreal provider-authority/preseed successor unless that review passes.

## Authority boundary

No W2-ENG empirical PASS, engine selection/ranking, gameplay/high-throughput implementation authority, production/implementation readiness, provider/legal/platform/release authority, verification-PASS authority, decision authority, canonicalization, or integration authority. Any eventual `main` integration is separately authorized and squash-only.