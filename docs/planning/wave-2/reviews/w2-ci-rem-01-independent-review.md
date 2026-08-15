# W2-CI-REV-02 — Fresh independent review of W2-CI-REM-01

**Issue:** #344  
**Task class:** `REQUIRED_REVIEW`  
**Review mode:** `DEGRADED_SINGLE_AGENT`, fresh role episode distinct from producer/remediator.  
**Claim:** `5302529939`  
**Base:** `main@92204cb2e58c792ef4199fe3562ca2192096f5c0`  
**Canonical binding:** Bootstrap #6 terminal binding `5245368879`; program blob `e3120ec203c4156328770aa86c12fbb7187966dc`; activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e` remains in main ancestry.  
**Judged remediation:** Issue #343 terminal `5302522499`, work `3cc6f039170ce0c19288426aded252a1081896fb`, exact head `8d8eee1d1b7d7cad63b3fecc52fcb6639c236160`, draft PR #345.  
**Disposition:** **PASS_BOUNDED_CAPABILITY_WITH_MINOR_NOTE — 0 BLOCKER / 0 MAJOR / 1 MINOR**.

Issue #343 / branch `planning/issue-343` was treated as immutable judged input. This review grants only bounded trust in the remediated CI/toolchain capability packet. It does not execute or score S1–S10, select/rank an engine, grant provider permission, or create implementation/readiness/legal/platform/release/verification/canonical/integration authority.

## 1. Identity and run checks

The remediation report blob `a69d0c6b74004a794842be8a6934ac772f07652e` and handoff blob `a54b9a7c81c53fc312cc45b7287b09b1aec2a274` match the routed identities. Corrected implementation commit `254d454a4f123fcb32ed66c14fd5829c37daaf8a` contains workflow blob `6573cdf8d855ea92ec110703890a3a1862727a94`, probe blob `fd41c33b96602714233412bc054b541a0f22628f`, and fail-closed policy blob `97c574899239616e056a69dd6ed2844f842f9542`.

Fresh GitHub Actions run `31888041342` executed against exact head `254d454a4f123fcb32ed66c14fd5829c37daaf8a` and completed successfully. The job record shows successful completion of policy regression validation, reviewed harness validation, bounded probes, policy evaluation, evidence persistence, artifact upload, and the final fail-closed enforcement step. Generated evidence commit `892bb9377a3580571c887a00b7521a3496eab6d7` is retained in the remediation lineage. Artifact `9247801348` is unexpired with digest `sha256:d4ec43c649024e124bf7ab450d4c8e994575867a89036213fc2533457d1694d1`.

Policy-result blob `803f871d733e92e8b6371efb70939faf85c8c741` records `pass=true` with no errors. Policy-selftest blob `b8f1af897dd070c4a5419e75a9f1ebb31e46271a` records all five cases passing: baseline allowed, public `FAILED` rejected, Bevy lock substitution rejected, artifact substitution rejected, and unexpected authority-scoped `FAILED` rejected.

## 2. Prior finding dispositions

### W2-CI-REV-M01 — RESOLVED

The corrected workflow no longer treats probe process completion as the capability gate. It evaluates a separate executable policy, records its exit code, persists/uploads evidence under `if: always()`, and only then fails or passes the job in a final enforcement step. The policy accepts public Bevy/Defold/Godot only as `CAPABLE`/`CAPABLE_WITH_PRESEED`; Unity/Unreal have a separately versioned allowance for `BLOCKED_BY_SPECIFIC_EXTERNAL_AUTHORITY`; other/failed states are rejected.

The retained negative test for a public `FAILED` state exercises the same `validate()` function used by production policy evaluation and is therefore materially connected to the gate, not a prose-only assertion. The historical first Defold/Java-17 run remains reconstructable and demonstrates why the correction matters; it is not rewritten away.

### W2-CI-REV-M02 — RESOLVED

The exact Bevy dependency resolution is now durable at `docs/planning/wave-2/evidence/ci/bevy-0.19.0-Cargo.lock` with SHA-256 `fd7e1276ff5c8cde22d98c0932f70eb39383d9b60ac2d15f11d921dfa71218b0`. The probe copies that exact retained lock into a fresh replay project, runs `cargo fetch --locked`, then `cargo check --locked --quiet`. Machine evidence marks the locked replay bound, and policy validation hashes the actual retained lock and cross-checks it against both machine evidence and the artifact-lock record.

The substitution self-test exercises the actual lock-identity check. `CAPABLE_WITH_PRESEED` remains appropriately bounded to exact locked dependency/bootstrap replay and is not represented as graphical harness or S1–S10 success.

### W2-CI-REV-M03 — RESOLVED for exact-content integrity and replay

The corrected Defold/Godot paths hash downloaded content before execution. If a retained expected digest exists, a mismatch makes `verified=false` and prevents the version/extraction execution path. The policy independently checks expected/observed equality, verified state, and agreement with the retained artifact lock.

The retained exact identities are:

- Defold 1.13.0 `bob.jar`: `22e651025834603794ba6873b09924f11412dff66eee0e38aaef8955eb534655`;
- Godot 4.7.1-stable Linux x86_64 ZIP: `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`.

A fresh independent read of public GitHub release metadata during this review confirms the Defold `bob.jar` release asset advertises the first digest and the Godot Linux x86_64 release asset advertises the second digest. The remediation therefore binds the same exact bytes currently identified by GitHub's release metadata, while the repository machine record conservatively retains its weaker source label described below.

## 3. Non-blocking finding

### W2-CI-REV2-m01 — Release-metadata helper conservatively misses available authoritative digest metadata

**Severity:** MINOR / non-blocking.  
**Disposition:** ACCEPTED_AS_BOUNDED_NOTE.

`release_asset_digest()` obtains the full GitHub release JSON through the generic `run()` helper, but that helper retains only the final 4000 stdout characters. Large release responses are therefore truncated before `json.loads`, causing the probe to miss an otherwise available release-asset digest and initialize the artifact lock as `OBSERVED_RUN_TOFU_LOCK`.

This is a provenance-quality false negative, not an integrity fail-open: the machine packet does not falsely claim vendor authority; exact content hashes are retained; subsequent replay rejects substitutions; the policy checks those retained identities; and this review independently confirmed both hashes against public GitHub release metadata. The bounded packet therefore remains valid for the capability claim under review.

A future producer may improve the helper by parsing the full response or querying the individual asset endpoint, but this note does not justify blocking remediation, duplicate review, or delaying the existing provider-authority continuation. Any such cleanup is lower priority than the now-unlocked chain.

## 4. Authority / regression review

The fresh packet still reports Bevy `CAPABLE_WITH_PRESEED`, Defold `CAPABLE`, Godot `CAPABLE`, Unity `BLOCKED_BY_SPECIFIC_EXTERNAL_AUTHORITY`, and Unreal Engine `BLOCKED_BY_SPECIFIC_EXTERNAL_AUTHORITY`; it does not claim five-candidate harness capability.

Unity's unresolved input remains valid unattended account/license/activation material for the exact editor baseline. Unreal Engine 5.8's unresolved input remains Epic-authorized source/prebuilt artifact access suitable for unattended CI. Public reachability is not provider permission, and the packet records no credential-value consumption.

The predecessor first-run Java-17 Defold failure and later Java-25 correction remain preserved. W2-ENG Issue #82 terminal comment `5276916603` remains the historical source of 50 `NOT_RUN` cells; this chain promotes none of them. No S1–S10 empirical PASS, ranking, selection, gameplay/high-throughput implementation authority, implementation/production readiness, provider/legal/platform/release authority, verification PASS, decision authority, canonicality, or integration authority is created.

## 5. Review result and next route

The required remediation review passes for **bounded CI/toolchain capability use**. All three prior MAJOR findings are closed. The single MINOR note is conservative provenance labeling and is non-blocking.

The next lawful frontier may therefore consider the already-scoped Unity+Unreal provider-authority/preseed continuation. That continuation may diagnose, request, or bind real provider-controlled inputs; it may not manufacture permission from this review. Integration of the remediation/review material remains a separate authority question and, if later authorized, must be squash-only.

This review itself grants no integration or canonicalization authority.