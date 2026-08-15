# W2-CI-REV-01 — Independent review of W2-CI-ENABLE-01

**Schema:** `bounded_ci_capability_review_v1`  
**Issue:** #341  
**Review mode:** `DEGRADED_SINGLE_AGENT` fresh ownership episode, distinct from producer Issue #339.  
**Claim:** `5302463048`  
**Base:** `main@92204cb2e58c792ef4199fe3562ca2192096f5c0`  
**Canonical binding:** Bootstrap Issue #6 terminal binding comment `5245368879`; canonical program blob `e3120ec203c4156328770aa86c12fbb7187966dc`; activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e` remains in `main` ancestry.  
**Producer:** Issue #339 terminal `STATUS(REVIEW_READY)` comment `5302456876`; work `8b03470f0772bc6a85a7eb915f27cee82b09a152`; head `2c0c4759b5de99c9cc292fb473888b0d4b2a5564`; draft PR #340 exact head confirmed.  
**Disposition:** **CHANGES_NEEDED — 0 BLOCKER / 3 MAJOR / 0 MINOR**.

This review treats producer branch `planning/issue-339` as immutable input. It validates the packet only as bounded infrastructure/toolchain capability evidence. It does not execute or rank S1–S10, select an engine, alter historical evidence, or grant readiness/provider/legal/platform/release/integration/canonical authority.

## 1. Frozen producer identities and evidence checked

The declared producer identities match the exact frozen head:

- report blob `794a041bdd1fb59d6928b7dae9a6bd5c9ee09084`;
- workflow blob `7a83f560bfd81c91aeeedfd184679739918cd1f9`;
- probe blob `571ec96fabb0c192c83357e7a9213ae6599e4d38`;
- machine capability blob `c1ab5ca0d1944c0ec3d3e84fca112eb06081e232` and declared file SHA-256 `6926cf69a9e2f1a5b7a19a3ede76781045af73a02ac350bbda71ccb66c9d473d`;
- CI harness-validator output blob `2c234e67de118659da18be582341763e2315e82f`;
- run-identity blob `6de98a68207571834030bac7a7db4fe8f80bd929`;
- producer handoff blob `2a91f1fae287252bdc7244948bb84dbafc848d1b`.

Producer work `8b03470f0772bc6a85a7eb915f27cee82b09a152` is an ancestor of producer head `2c0c4759b5de99c9cc292fb473888b0d4b2a5564`; the only later frozen-head delta is the producer handoff.

Corrected GitHub Actions run `31887219066` is a completed successful run on trigger SHA `2517a5b62f760f916080a152d5f74269c2f65f47`; its single job shows the validator, probe, branch-persistence, and artifact-upload steps all completed. Artifact `9247589148` is present and unexpired with digest `sha256:8ca677ac7adfc3a798fdad14611239b7c37a3423c4a3c480c23d2b510ce68854`. The run-generated evidence commit `8ddea765c31ce8091814db41a188bd6cc837ea2f` is retained in producer ancestry.

The first run `31887099444` and artifact `9247557956` are also retained; the artifact digest matches `sha256:5a74acc251fa6c5e99230c7426359de3ade434e4859c0692b2be5f14b63d96a8`. Its generated evidence commit `c44869cc87b2ce4466b17ecff942d9868fab588b` records Defold `status: FAILED` because Java 17 cannot load class-file version 69. The corrected run records Temurin Java `25.0.4+7` and successful Bob 1.13.0 execution. The remediation claim is therefore materially supported rather than inferred.

The CI harness validator output is durable and records the expected validator/feature-slice/scenario-manifest/fixture/result identities. Historical W2-ENG Issue #82 terminal comment `5276916603` remains `INCONCLUSIVE_ENVIRONMENT_BLOCKED` with 50 `NOT_RUN` cells; this packet does not rewrite those cells.

## 2. Findings

### W2-CI-REV-M01 — Probe/job success is fail-open with respect to candidate capability failures

**Severity:** MAJOR  
**Disposition:** OPEN — correction required before the workflow is a trusted downstream capability source.

`tools/planning/engine_toolchain_probe.py` records candidate statuses but `main()` returns `0` unconditionally. The workflow then treats the probe step as successful whenever the Python process itself completes, irrespective of whether one or more candidate probes are `FAILED`.

The retained first run demonstrates the problem concretely: Defold's machine record is `FAILED` with `UnsupportedClassVersionError`, yet GitHub Actions run `31887099444` has overall conclusion `success` and continues through evidence persistence/upload. The packet correctly explains that first-run defect, so this is not a provenance-hiding finding; it is a fail-closed semantics finding.

A future regression in Bevy/Defold/Godot acquisition or execution can therefore produce a green workflow unless a consumer independently parses the JSON. That conflicts with the enablement task's required fail-closed handling and makes workflow success an unsafe proxy for capability.

**Required correction:** make the workflow mechanically fail on unexpected `FAILED` states or add a separate policy validator that exits nonzero for them. Expected authority states for Unity/Unreal may remain explicit non-success capability classifications without forcing an overall infrastructure error, but the allowed-state policy must be encoded and tested rather than left to report interpretation. Retain JSON/artifacts even on failure via `if: always()` or equivalent.

### W2-CI-REV-M02 — Bevy `CAPABLE_WITH_PRESEED` does not bind the preseed/lock identity needed for reproducible replay

**Severity:** MAJOR  
**Disposition:** OPEN — correction required for the claimed reproducibility class.

The Bevy probe creates a temporary `Cargo.toml`, deliberately performs an unlocked resolution when no lock exists, then proves `cargo fetch --locked` and `cargo check --locked` only against the generated temporary `Cargo.lock`. That lock file is destroyed with the temporary directory and is not included in the machine evidence, run bundle, producer branch, or a durable digest binding.

The run therefore proves a useful one-run fact: the GitHub-hosted environment could resolve top-level `bevy = '=0.19.0'` and compile the resulting graph. It does **not** establish a reproducible `CAPABLE_WITH_PRESEED` identity that another run can replay from repository + bound evidence alone. The machine log itself shows compatible transitive Bevy crates at `0.19.1`, underscoring that top-level version pinning is not the same as freezing the dependency graph.

**Required correction:** durably retain the exact generated `Cargo.lock` (or an equivalent complete resolution manifest) with a cryptographic digest, and make the replay path consume that exact identity. If no preseed is actually required, reclassify the bounded claim to match what is proved rather than using `CAPABLE_WITH_PRESEED` without a bound preseed artifact.

### W2-CI-REV-M03 — Defold and Godot acquisition proves version execution but not exact downloaded artifact identity

**Severity:** MAJOR  
**Disposition:** OPEN — correction required for reproducible artifact binding.

The Defold and Godot probes download version-addressed release assets and record URLs, byte counts, command results, and executable-reported versions. They do not compute or retain a SHA-256 (or equivalent immutable content identity) for the downloaded `bob.jar` or Godot archive, and the probe does not verify an expected vendor/repository digest before execution.

That is enough to support the narrow historical observation that the exact run successfully downloaded and invoked artifacts presenting as Defold 1.13.0 and Godot 4.7.1-stable. It is not enough to make the external acquisition reproducible by exact bytes, because release assets can be replaced or served differently without changing the version-addressed URL.

**Required correction:** record cryptographic digests of acquired archives/binaries in the machine evidence and bind expected digests or a lawfully retained/preseeded exact artifact identity for replay. The correction must preserve first-run provenance and must not convert executable presence into S1–S10 scenario evidence.

## 3. Claims that survive adversarial review

Subject to the three reproducibility/fail-closed findings above, several producer boundaries are materially correct and should be preserved through remediation:

- the corrected Java-25 run genuinely repairs the observed Defold Java-17 bootstrap defect;
- GitHub-hosted CI can materially acquire/invoke the tested public Bevy/Defold/Godot surfaces in the recorded run;
- the capability labels are explicitly scoped below S1–S10 and do not constitute candidate comparison PASSes;
- the current harness validator did execute successfully in the corrected run and its output identities are durably retained;
- no secret values are read by the probe; Unity and Unreal stop at non-credentialed/public reachability checks;
- Unity unattended activation/account/license material is not shown to be repository-self-grantable;
- Unreal Engine 5.8 source/prebuilt entitlement is not shown to be repository-self-grantable;
- public network reachability is not represented as provider entitlement;
- `full_five_candidate_harness_capable=false` and historical #82 `50 NOT_RUN` remain unchanged;
- no engine ranking, engine selection, implementation readiness, provider/legal/platform/release authority, canonicality, verification PASS, or integration authority is granted.

Thus the residual Unity/Unreal provider-authority classification is plausible and correctly narrow **as a diagnosis**, but the packet is not yet trusted as the reproducible downstream execution source required to advance from this review gate.

## 4. Disposition and route

Because unresolved MAJOR findings exist, the required review disposition is **`CHANGES_NEEDED`**. Do not treat Issue #339 / PR #340 as a trusted downstream evidence source yet, do not integrate it merely because PR #340 is mergeable, and do not create the planned Unity+Unreal authority/preseed successor ahead of remediation of this required review.

The smallest next route is blocking producer remediation/revision of the existing W2-CI-ENABLE-01 packet, preserving its exact run lineage and addressing only:

1. fail-closed capability-policy evaluation;
2. durable Bevy resolution/preseed identity;
3. exact Defold/Godot downloaded artifact digest binding;
4. a fresh corrected CI run plus machine evidence demonstrating the corrections;
5. fresh required review of the revised exact head.

No new engine decision is created. No global readiness gate is invented. Provider-authority work remains a later non-review continuation only after the CI capability packet passes its required review.

## 5. Authority boundary

This review grants no W2-ENG empirical PASS, engine selection/ranking, gameplay/high-throughput implementation authority, production/implementation readiness, provider/legal/platform/release authority, canonicalization, verification-PASS authority, decision authority, or integration authority. Any eventual publication to `main` remains separately authorized and squash-only.