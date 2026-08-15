# Handoff — Issue #344 / W2-CI-REV-02

## Lifecycle

- task class: `REQUIRED_REVIEW`
- review mode: `DEGRADED_SINGLE_AGENT`
- branch: `planning/issue-344`
- claim: `5302529939`
- base: `92204cb2e58c792ef4199fe3562ca2192096f5c0`
- canonical binding comment: `5245368879`
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- review work commit: `c0624781bd72ca79224bc688862ae726f6f86ce9`
- review artifact blob: `2c387c0daadf15139f4ca3b68b3b6827c9a0f24b`
- disposition: `PASS_BOUNDED_CAPABILITY_WITH_MINOR_NOTE`
- findings: `0 BLOCKER / 0 MAJOR / 1 MINOR`
- integration authority: none

## Immutable judged remediation

- Issue #343 terminal status comment `5302522499`
- work `3cc6f039170ce0c19288426aded252a1081896fb`
- exact head `8d8eee1d1b7d7cad63b3fecc52fcb6639c236160`
- draft PR #345
- remediation report `a69d0c6b74004a794842be8a6934ac772f07652e`
- remediation handoff `a54b9a7c81c53fc312cc45b7287b09b1aec2a274`
- corrected implementation `254d454a4f123fcb32ed66c14fd5829c37daaf8a`
- generated evidence `892bb9377a3580571c887a00b7521a3496eab6d7`
- workflow blob `6573cdf8d855ea92ec110703890a3a1862727a94`
- probe blob `fd41c33b96602714233412bc054b541a0f22628f`
- policy blob `97c574899239616e056a69dd6ed2844f842f9542`

## Fresh CI evidence rechecked

- run `31888041342`, head `254d454a4f123fcb32ed66c14fd5829c37daaf8a`, conclusion `success`
- final fail-closed enforcement step: `success`
- artifact `9247801348`, unexpired
- artifact digest `sha256:d4ec43c649024e124bf7ab450d4c8e994575867a89036213fc2533457d1694d1`
- policy-result blob `803f871d733e92e8b6371efb70939faf85c8c741`: pass, no errors
- policy-selftest blob `b8f1af897dd070c4a5419e75a9f1ebb31e46271a`: five required cases pass
- Bevy retained lock SHA-256 `fd7e1276ff5c8cde22d98c0932f70eb39383d9b60ac2d15f11d921dfa71218b0`
- artifact-lock blob `4a88990ae24768eb4f83a8a1311e2a830834649f`
- Defold `bob.jar` SHA-256 `22e651025834603794ba6873b09924f11412dff66eee0e38aaef8955eb534655`
- Godot Linux x86_64 ZIP SHA-256 `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`

Fresh independent GitHub release-metadata reads during this review confirm the retained Defold and Godot hashes equal the corresponding public release-asset digest fields.

## Prior findings

1. `W2-CI-REV-M01` — `RESOLVED`: executable fail-closed policy is distinct from probe process success; evidence persists before final enforcement; public/authority-scoped status policies are explicit; regression negatives exercise the actual validator.
2. `W2-CI-REV-M02` — `RESOLVED`: exact Bevy Cargo.lock is durable/hash-bound and replayed in a fresh project under `cargo fetch/check --locked`; substitution is rejected.
3. `W2-CI-REV-M03` — `RESOLVED`: exact Defold/Godot downloaded content is hash-bound before execution, retained for replay, policy-checked, and substitution-rejected.

## Non-blocking note

`W2-CI-REV2-m01` — **MINOR / ACCEPTED_AS_BOUNDED_NOTE**: the in-run release-metadata helper routes full release JSON through a generic stdout helper that retains only the final 4000 characters, so large release JSON is not parseable and the machine packet conservatively initializes the source as `OBSERVED_RUN_TOFU_LOCK` rather than using the available GitHub release-asset digest. This is a false-negative provenance label, not an integrity bypass: exact hashes are retained/enforced, replay rejects substitution, and the machine record does not falsely claim vendor authority.

This cleanup is non-blocking and lower priority than the now-unlocked chain.

## Preserved boundaries

- predecessor first-run Java-17 Defold failure and Java-25 correction remain reconstructable;
- W2-ENG #82 terminal `5276916603` remains 50 historical `NOT_RUN`; zero promoted;
- current bounded statuses remain Bevy `CAPABLE_WITH_PRESEED`, Defold/Godot `CAPABLE`, Unity/Unreal `BLOCKED_BY_SPECIFIC_EXTERNAL_AUTHORITY`;
- Unity still needs valid unattended account/license/activation material;
- Unreal Engine 5.8 still needs Epic-authorized source/prebuilt access suitable for unattended CI;
- public reachability is not provider permission and no secret values were consumed;
- no S1–S10 empirical PASS, engine ranking/selection, gameplay/high-throughput implementation, implementation/production readiness, provider/legal/platform/release, verification-PASS, decision, canonical, or integration authority is created.

## Next lawful route

The required review passes for bounded CI/toolchain capability use. The frontier may now consider the narrowly scoped Unity+Unreal provider-authority/preseed continuation. That successor may bind or diagnose real provider-controlled inputs only; it may not manufacture permission from this review.

Integration/canonicalization remain separate. Any eventual integration to `main` requires separate authority and must be squash-only.