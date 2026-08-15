# W2-CI-ENABLE-01 — Reproducible engine toolchain capability

**Mission:** `W2-CI-ENABLE-01` / Issue #339  
**Task class:** `INTERNAL_ENABLEMENT_READY`  
**Frozen source main:** `92204cb2e58c792ef4199fe3562ca2192096f5c0`  
**Canonical program blob:** `e3120ec203c4156328770aa86c12fbb7187966dc`  
**Engine evidence source:** Issue #82 terminal comment `5276916603`, disposition `INCONCLUSIVE_ENVIRONMENT_BLOCKED`  
**Historical W2-ENG result preserved:** `50 NOT_RUN`; this infrastructure episode promotes none of them  
**Current reviewed harness exercised:** `W2-ENG-HARNESS-v5` / feature slice `W2-ENG-FEATURE-SLICE-v2` / scenario manifest `W2-ENG-SCENARIO-INPUTS-v2`  
**Capability run:** GitHub Actions run `31887219066`, triggering SHA `2517a5b62f760f916080a152d5f74269c2f65f47`  
**Run artifact:** `9247589148`, `w2-ci-enable-01-31887219066-1`, digest `sha256:8ca677ac7adfc3a798fdad14611239b7c37a3423c4a3c480c23d2b510ce68854`  
**Machine-readable capability:** `docs/planning/wave-2/evidence/ci/engine-toolchain-capability.json`, Git blob `c1ab5ca0d1944c0ec3d3e84fca112eb06081e232`, file SHA-256 `6926cf69a9e2f1a5b7a19a3ede76781045af73a02ac350bbda71ccb66c9d473d`  
**Authority:** infrastructure/toolchain capability evidence only; no engine selection, S1–S10 result, implementation readiness, provider/legal/platform/release, canonicalization, verification PASS, or integration authority.

## 1. Question answered

The post-Wave-2 frontier had classified the missing engine comparison trigger as externally blocked because the prior execution host could not resolve or materialize any admitted engine toolchain. This mission tests the narrower question required by the owner liveness directive: can repository-owned GitHub Actions construct enough real execution capability to remove the generic environment blocker, and if not, what exact non-repository authority remains?

The answer is **yes for the public/repository-acquirable toolchains, no for the two provider-gated commercial/source surfaces**. The generic `environment unavailable` diagnosis is therefore obsolete for this successor. The remaining blocker is specifically provider authority for Unity and Unreal Engine.

This does **not** complete W2-ENG-03. Its 50 candidate/scenario cells remain historical `NOT_RUN` until a fresh empirical episode executes the reviewed harness under its own lifecycle and review route.

## 2. Reproducible CI identity

The task branch adds `.github/workflows/w2-ci-engine-toolchain-probe.yml` and `tools/planning/engine_toolchain_probe.py`.

The corrected capability run used:

- GitHub-hosted `ubuntu-24.04` runner;
- runner image `ubuntu24`, image version `20260810.271.1`;
- workflow trigger SHA `2517a5b62f760f916080a152d5f74269c2f65f47`;
- `actions/checkout` pinned to commit `11d5960a326750d5838078e36cf38b85af677262`;
- `actions/setup-java` pinned to commit `cf277c60eb25467037889841efdb72551f06f6c3`;
- Temurin Java `25.0.4+7`;
- `actions/upload-artifact` pinned to commit `ea165f8d65b6e75b540449e92b4886f43607fa02`;
- probe source SHA-256 `c20b3700123c70bf4dfb56d70fdd3b2fb8f9f49d7e56ea356600df68a5636b12`;
- exact current harness-validator source SHA-256 `9a50e3e21279a7a94836d6162fee218a0e187bafe292847fd5f0b108df45deea`.

The workflow records runner/tool identities, executes the current reviewed harness validator, runs bounded real acquisition/process probes, records commands/exits/timings/stdout/stderr in JSON, commits generated evidence back to the task branch, and uploads the same evidence as a run artifact.

The current harness validator passed in CI and re-emitted its expected identities:

- validator contract `ed1de63a02872c18981259a15eb8393b3d94d5f7af774b4b1f771c1c4e2e77ef`;
- feature slice `9a2523c4870146b09233397f3773f7a27b1e0135c24a6767d16e34a791aab104`;
- scenario manifest `be4d7473b01da6b428cd5f3be48de083abd161a4899471303f3ccfeef45c725f`;
- fixture inputs `45555e8370f821d66fa8febdd58d475b88c15b0505ab996a4a8954ef8ef11613`;
- result object `8612a359c029e4d921356d214177a3478a0ee45011f8d26a629850180748a071`.

## 3. Probe history and remediation

The first run, `31887099444`, was intentionally retained as provenance. It proved network acquisition for the public artifacts but exposed a repository-fixable bootstrap defect: Defold `bob.jar` 1.13.0 is compiled for class-file version 69 while the default runner Java was 17/class-file 61. That run's artifact is `9247557956`, digest `sha256:5a74acc251fa6c5e99230c7426359de3ade434e4859c0692b2be5f14b63d96a8`.

The workflow was then corrected by pinning `actions/setup-java` and provisioning Temurin Java 25. The second run, `31887219066`, completed every workflow step successfully and is the capability result below. The failed first attempt is not hidden or rewritten.

## 4. Exact capability matrix

| Admitted candidate | Frozen acquisition baseline for this probe | Exact required executable surface tested | Result | Durable evidence / interpretation |
|---|---|---|---|---|
| Bevy | `0.19.0` | Rust/Cargo plus exact Bevy dependency materialization | `CAPABLE_WITH_PRESEED` | Cargo `1.97.1`, rustc `1.97.1`; exact `bevy = '=0.19.0'` resolves, a lockfile is materialized, locked replay succeeds, and `cargo check --locked --quiet` exits 0. This proves repository-owned dependency/bootstrap capability, not graphics/capture/package or S1–S10 completion. |
| Defold | `1.13.0` | Java plus exact `bob.jar` | `CAPABLE` | Exact 1.13.0 `bob.jar` downloads from the first-party GitHub release surface; Temurin `25.0.4+7` executes it and reports `bob.jar version: 1.13.0`, sha1 `f735c12192bf95684e6ae1ae27c400b8170fc6d8`. |
| Godot | `4.7.1-stable` | exact Linux editor/headless executable | `CAPABLE` | Exact 4.7.1 stable Linux archive downloads and extracts; the resulting executable runs `--headless --version` successfully. |
| Unity | `6000.5.6f1` acquisition-time baseline from the prior episode | Linux editor plus valid unattended activation/account state | `BLOCKED_BY_SPECIFIC_EXTERNAL_AUTHORITY` | Public Unity archive/hub network surfaces are reachable, but a lawful valid unattended-use account/license/activation state is not repository-self-grantable. No credential values were read. |
| Unreal Engine | `5.8` | Linux editor/source or prebuilt package plus required Epic entitlement | `BLOCKED_BY_SPECIFIC_EXTERNAL_AUTHORITY` | Public Unreal network surface is reachable, but the exact engine source/prebuilt acquisition path requires Epic-linked entitlement or a lawfully supplied preseeded artifact. No credential values were read. |

The machine object therefore reports:

```text
Bevy          CAPABLE_WITH_PRESEED
Defold        CAPABLE
Godot         CAPABLE
Unity         BLOCKED_BY_SPECIFIC_EXTERNAL_AUTHORITY
Unreal Engine BLOCKED_BY_SPECIFIC_EXTERNAL_AUTHORITY
```

`full_five_candidate_harness_capable = false` and `prior_not_run_promoted = false`.

## 5. Mapping to the reviewed S1–S10 prerequisite surface

The current harness requires real candidate-native work across build/launch/reconstruction (S1), fresh-agent modification (S2), real/shared deterministic rules (S3), save migration (S4), merge conflict handling (S5), identity-bound capture (S6), broken-reference recovery (S7), profiling/hotspot localization (S8), a common Windows x64 development package target (S9), and repository-only continuation (S10).

This infrastructure task deliberately does not execute those scenarios. It establishes only the precondition needed to begin a lawful empirical episode: a reproducible host can acquire and invoke the public candidate toolchains, retains `xvfb-run` for virtual-display work, records sufficient CPU/memory/disk/tool identity for a later common-resource adaptation, and can persist exact run artifacts. Candidate-native capture/profile/export support and scenario adaptations remain evidence obligations of the fresh W2-ENG episode, not facts inferred from executable presence.

Because Unity and Unreal cannot yet be lawfully materialized, a five-candidate S1–S10 episode cannot start without violating the reviewed equivalence set. Running only the three public candidates and treating that as the comparison would silently alter the admitted set and is therefore not authorized here.

## 6. Residual blocker — exact non-repository authority

The residual blocker is **not** generic CI, DNS, download access, Java, Rust, or Linux process execution. Repository-owned CI has materially removed those classes for Bevy/Defold/Godot.

The smallest remaining authority inputs are:

1. **Unity:** valid, project-authorized unattended-use account/license/activation material for the exact Linux editor baseline, represented in a way that a fresh CI episode can consume without hidden manual state; and
2. **Unreal Engine:** Epic-authorized access to an exact 5.8 source/prebuilt Linux artifact path, or an equivalently exact lawfully preseeded artifact, suitable for unattended CI.

These are provider/entitlement grants. This agent cannot mint or infer them, and repository-owned automation must not treat a public website response as equivalent to editor/source entitlement.

The next non-review continuation after this packet is trusted is therefore a **single bounded provider-authority/preseed successor for the Unity + Unreal acquisition surfaces required by the existing five-candidate set**, not a duplicate generic CI task and not an engine-selection task. If those exact inputs later become available, the canonical dispatcher can route one fresh W2-ENG empirical continuation against the then-current reviewed harness identities.

## 7. Security, credential, and dependency posture

- No task code reads, prints, uploads, or tests secret values.
- Unity and Unreal probes intentionally stop before credentialed acquisition/activation.
- GitHub Actions dependencies are pinned to commit SHAs rather than floating tags.
- Public engine artifacts/dependencies are version-bound in the probe and their executed versions are recorded.
- The runner image is identified by OS and image version, but GitHub-hosted image contents remain an upstream service dependency; a reviewer must assess whether this is sufficient for the bounded evidence-source use.
- The Bevy probe creates a lockfile at run time and proves locked replay in the same run. A later empirical successor should retain the exact generated lock/materialization identity it actually uses rather than relying on this smoke workspace.
- The run artifact has finite retention; the generated evidence is also committed to the task branch so review does not depend on artifact retention alone.

## 8. Required independent review before downstream trust

This producer packet does not self-certify the environment. Fresh independent/degraded-independent review is required to attack:

- reproducibility and pinned dependency claims;
- hidden/manual setup or undeclared runner assumptions;
- whether probes are false positives for the exact prerequisite they claim;
- whether logs/artifacts are sufficient and durable;
- Unity/Unreal credential/license/entitlement assumptions;
- any accidental engine ranking or authority inflation;
- whether any infrastructure detail incorrectly suggests a historical `NOT_RUN` became PASS.

Until that review is terminal, this packet is noncanonical producer evidence and must not be treated as a trusted W2-ENG execution source.

## 9. Disposition

**Disposition: `PARTIAL_CAPABILITY_WITH_EXACT_PROVIDER_AUTHORITY_BLOCKERS`.**

The liveness directive changed the work decomposition productively: the project did not need to remain idle on an undifferentiated `EXTERNAL_TRIGGER_REQUIRED` state. Repository-owned CI could remove the public-toolchain environment blocker and expose the actual remaining boundary. The remaining boundary is now narrow enough for an authority-specific successor rather than another environment-recovery loop.

No engine is ranked or selected. No S1–S10 cell is executed. No historical evidence is upgraded. No implementation, provider, legal, platform, release, readiness, decision, canonicalization, verification-PASS, or integration authority is created by this report.
