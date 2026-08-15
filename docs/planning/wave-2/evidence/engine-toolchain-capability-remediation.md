# W2-CI-REM-01 — CI capability remediation evidence

**Issue:** #343  
**Task class:** `BLOCKING_REMEDIATION_REVISION`  
**Winning claim:** `5302487090` (lower valid claim than later contender `5302487906`)  
**Base:** `main@92204cb2e58c792ef4199fe3562ca2192096f5c0`  
**Canonical binding:** Bootstrap Issue #6 terminal binding `5245368879`; program blob `e3120ec203c4156328770aa86c12fbb7187966dc`; activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e`.  
**Frozen predecessor:** Issue #339 terminal `5302456876`, head `2c0c4759b5de99c9cc292fb473888b0d4b2a5564`, draft PR #340.  
**Required review input:** Issue #341 terminal `5302477689`, disposition `CHANGES_NEEDED`, head `faae4aa3731cccac48e783631ba4883138fbef8c`, review artifact `f7bc414c8a66c72b50fcb01cb992086f403fe245`, handoff `876b5113b1be05c7753e1a8f9972decb83213505`.

This packet remediates only `W2-CI-REV-M01`, `W2-CI-REV-M02`, and `W2-CI-REV-M03`. It does not execute or score S1–S10, select/rank an engine, change W2-ENG #82 historical results, or create implementation/readiness/provider/legal/platform/release/verification/canonical/integration authority.

## Corrected implementation identity

The coherent remediation implementation was published at `254d454a4f123fcb32ed66c14fd5829c37daaf8a`:

- workflow blob `6573cdf8d855ea92ec110703890a3a1862727a94`;
- capability probe blob `fd41c33b96602714233412bc054b541a0f22628f`;
- fail-closed policy blob `97c574899239616e056a69dd6ed2844f842f9542`.

Fresh GitHub Actions run `31888041342` was triggered by exactly that implementation commit. The capability job completed `success`; every material step completed successfully, including policy regression self-tests, the reviewed harness validator, bounded capability probes, evidence persistence, immutable artifact upload, and the final fail-closed enforcement step.

The run persisted generated evidence in commit `892bb9377a3580571c887a00b7521a3496eab6d7` (direct child of implementation commit `254d454a...`). Immutable run artifact `9247801348` is unexpired and has digest `sha256:d4ec43c649024e124bf7ab450d4c8e994575867a89036213fc2533457d1694d1`.

## Finding dispositions

### W2-CI-REV-M01 — RESOLVED

The prior probe returned process success irrespective of candidate status, allowing the retained first Defold/Java-17 `FAILED` record to coexist with an overall green workflow. The remediation adds a separate executable policy validator and changes workflow ordering so evidence is persisted/uploaded before the final enforcement gate.

The policy now mechanically requires Bevy/Defold/Godot to be `CAPABLE` or `CAPABLE_WITH_PRESEED`; Unity/Unreal may be either capable or the specifically allowed `BLOCKED_BY_SPECIFIC_EXTERNAL_AUTHORITY` state; any unexpected `FAILED`/unknown state is rejected. Credential boundaries, the 50 historical `NOT_RUN` count, result summaries, lock/digest identities, and external-authority summaries are also checked.

Fresh run policy output is exact blob `803f871d733e92e8b6371efb70939faf85c8c741` and records `pass: true`, `errors: []`. Regression self-test blob `b8f1af897dd070c4a5419e75a9f1ebb31e46271a` records all five required cases passing:

- baseline allowed;
- unexpected public `FAILED` rejected;
- Bevy lock substitution rejected;
- downloaded artifact substitution rejected;
- unexpected authority-scoped `FAILED` rejected.

The final workflow enforcement step reads the retained policy exit and fails unless it equals zero, while persistence/upload steps are `if: always()`. Workflow green is therefore no longer a fail-open proxy for candidate capability.

### W2-CI-REV-M02 — RESOLVED

The remediation persists the exact Bevy `Cargo.lock` under `docs/planning/wave-2/evidence/ci/bevy-0.19.0-Cargo.lock` rather than discarding it with a temporary probe directory. Fresh run lock SHA-256 is `fd7e1276ff5c8cde22d98c0932f70eb39383d9b60ac2d15f11d921dfa71218b0`; the retained sha256 record has blob `01918a17248f9a892f5aacd8e037e5c66ebc3564`.

The probe constructs a fresh replay project, copies the exact retained lock into it, performs `cargo fetch --locked`, and then `cargo check --locked --quiet`. The machine evidence records `lock_replay_bound: true`, both replay commands exit zero, and capability remains truthfully bounded as `CAPABLE_WITH_PRESEED` rather than an S1–S10 empirical PASS. The policy verifies the actual retained lock hash against both machine evidence and the artifact-lock record; its negative self-test proves a substituted lock is rejected.

### W2-CI-REV-M03 — RESOLVED, with source-label limitation retained

The remediation computes exact SHA-256 identities before executing the downloaded Defold/Godot artifacts, stores expected/observed identities, prevents execution on mismatch, retains those identities in `engine-toolchain-artifact-lock.json`, and policy-checks them mechanically.

Fresh retained identities are:

- Defold 1.13.0 `bob.jar`: `22e651025834603794ba6873b09924f11412dff66eee0e38aaef8955eb534655`;
- Godot 4.7.1-stable Linux x86_64 ZIP: `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`.

The generated artifact-lock blob is `4a88990ae24768eb4f83a8a1311e2a830834649f`. An independent freeze-time read of the public GitHub release metadata confirms those exact hashes are the release-asset `digest` values for `bob.jar` and `Godot_v4.7.1-stable_linux.x86_64.zip` respectively.

The probe's own best-effort release-metadata lookup retained the conservative source label `OBSERVED_RUN_TOFU_LOCK`: its generic command-capture helper retains only the tail of long stdout, so the full release JSON was not parseable inside that helper. That implementation limitation does **not** remove the exact-content binding or mismatch rejection and is not represented as vendor-signed verification by the machine packet. The external freeze-time cross-check is therefore supplementary evidence, while the repository-enforced claim remains exact retained content identity. A fresh reviewer must decide whether this source-label limitation warrants any residual finding; this remediation does not self-upgrade it.

## Fresh capability result

Fresh machine status summary remains intentionally bounded:

- Bevy — `CAPABLE_WITH_PRESEED`;
- Defold — `CAPABLE`;
- Godot — `CAPABLE`;
- Unity — `BLOCKED_BY_SPECIFIC_EXTERNAL_AUTHORITY`;
- Unreal Engine — `BLOCKED_BY_SPECIFIC_EXTERNAL_AUTHORITY`.

The run does not claim all five candidates are harness-capable. Unity still requires valid unattended-use account/license/activation material for the exact editor baseline. Unreal Engine 5.8 still requires Epic-authorized source/prebuilt artifact access suitable for unattended CI. No credential values were consumed to manufacture those authorities.

## Historical provenance preserved

The remediation retains predecessor provenance rather than overwriting it:

- corrected predecessor run `31887219066`, trigger `2517a5b62f760f916080a152d5f74269c2f65f47`, generated evidence `8ddea765c31ce8091814db41a188bd6cc837ea2f`, artifact `9247589148`, digest `sha256:8ca677ac7adfc3a798fdad14611239b7c37a3423c4a3c480c23d2b510ce68854`;
- first predecessor run `31887099444`, generated evidence `c44869cc87b2ce4466b17ecff942d9868fab588b`, artifact `9247557956`, digest `sha256:5a74acc251fa6c5e99230c7426359de3ade434e4859c0692b2be5f14b63d96a8`, including the Java-17 Defold failure;
- the Java-25 correction remains explicit rather than collapsing the first run;
- W2-ENG Issue #82 terminal comment `5276916603` remains `INCONCLUSIVE_ENVIRONMENT_BLOCKED` with 50 historical `NOT_RUN` cells and zero cells promoted by this remediation.

## Route and authority boundary

All three required-review MAJOR findings are dispositioned `RESOLVED` at the remediation layer, subject to one fresh required independent/degraded-independent review of the exact final remediation head. Do not advance the Unity+Unreal provider-authority/preseed successor before that review passes.

This remediation grants no W2-ENG empirical PASS, engine selection/ranking, gameplay/high-throughput implementation authority, production/implementation readiness, provider/legal/platform/release authority, verification PASS, decision authority, canonicality, or integration authority. Any eventual publication to `main` remains separately authorized and squash-only.