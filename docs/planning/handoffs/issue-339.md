# Handoff — Issue #339 / W2-CI-ENABLE-01

## Lifecycle

- task: `INTERNAL_ENABLEMENT_READY`
- producer branch: `planning/issue-339`
- frozen source main: `92204cb2e58c792ef4199fe3562ca2192096f5c0`
- canonical binding: Bootstrap Issue #6 terminal binding comment `5245368879`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- producer work commit: `8b03470f0772bc6a85a7eb915f27cee82b09a152`
- required fresh review: pending route from terminal status; producer must not self-review
- integration authority: none

## Exact input provenance

- W2-ENG source Issue #82 terminal comment: `5276916603`
- W2-ENG prior disposition: `INCONCLUSIVE_ENVIRONMENT_BLOCKED`
- W2-ENG historical matrix: `50 NOT_RUN`, unchanged by this task
- current harness: `W2-ENG-HARNESS-v5`
- feature slice: `W2-ENG-FEATURE-SLICE-v2`
- scenario manifest: `W2-ENG-SCENARIO-INPUTS-v2`
- harness validator source SHA-256: `9a50e3e21279a7a94836d6162fee218a0e187bafe292847fd5f0b108df45deea`
- CI harness validator output blob: `2c234e67de118659da18be582341763e2315e82f`

## Infrastructure packet

- workflow: `.github/workflows/w2-ci-engine-toolchain-probe.yml`
- probe: `tools/planning/engine_toolchain_probe.py`
- report: `docs/planning/wave-2/evidence/engine-toolchain-capability.md`
- machine capability: `docs/planning/wave-2/evidence/ci/engine-toolchain-capability.json`
- capability JSON blob: `c1ab5ca0d1944c0ec3d3e84fca112eb06081e232`
- capability JSON SHA-256: `6926cf69a9e2f1a5b7a19a3ede76781045af73a02ac350bbda71ccb66c9d473d`
- run identity blob: `6de98a68207571834030bac7a7db4fe8f80bd929`
- corrected GitHub Actions run: `31887219066`
- corrected run trigger SHA: `2517a5b62f760f916080a152d5f74269c2f65f47`
- generated evidence commit: `8ddea765c31ce8091814db41a188bd6cc837ea2f`
- corrected artifact id: `9247589148`
- corrected artifact digest: `sha256:8ca677ac7adfc3a798fdad14611239b7c37a3423c4a3c480c23d2b510ce68854`
- first-run provenance: run `31887099444`, artifact `9247557956`, digest `sha256:5a74acc251fa6c5e99230c7426359de3ade434e4859c0692b2be5f14b63d96a8`

Pinned action commits:

- checkout: `11d5960a326750d5838078e36cf38b85af677262`
- setup-java: `cf277c60eb25467037889841efdb72551f06f6c3`
- upload-artifact: `ea165f8d65b6e75b540449e92b4886f43607fa02`

Runner identity for the corrected run:

- `ubuntu-24.04`
- image OS `ubuntu24`
- image version `20260810.271.1`
- Java `Temurin 25.0.4+7`
- probe source SHA-256 `c20b3700123c70bf4dfb56d70fdd3b2fb8f9f49d7e56ea356600df68a5636b12`

## Capability result

| Candidate | Result | Exact meaning |
|---|---|---|
| Bevy 0.19.0 | `CAPABLE_WITH_PRESEED` | exact dependency resolves; generated lock replays locked; `cargo check --locked` succeeds |
| Defold 1.13.0 | `CAPABLE` | exact Bob downloads and executes under pinned Java 25 |
| Godot 4.7.1-stable | `CAPABLE` | exact Linux archive downloads/extracts and executable runs headless |
| Unity | `BLOCKED_BY_SPECIFIC_EXTERNAL_AUTHORITY` | valid unattended-use account/license/activation material is not repository-self-grantable |
| Unreal Engine 5.8 | `BLOCKED_BY_SPECIFIC_EXTERNAL_AUTHORITY` | Epic-authorized source/prebuilt acquisition or lawful exact preseed is required |

`full_five_candidate_harness_capable=false`.

No scenario cell was executed or upgraded. The capability labels describe toolchain/bootstrap prerequisites only.

## Corrected bootstrap defect retained as provenance

Run `31887099444` downloaded Defold 1.13.0 successfully but failed to execute Bob because the default runner Java 17 supports class files only through version 61 while Bob requires class-file version 69. The producer corrected this internal defect by pinning `actions/setup-java` and Temurin Java 25. Corrected run `31887219066` then executed Bob successfully. Do not collapse the first run out of the audit trail.

## Required next gate

Fresh independent/degraded-independent review of the exact producer head, workflow, capability report, machine JSON, and corrected run is required before the environment may be treated as a trusted downstream evidence source.

The reviewer must attack at least:

1. dependency and runner reproducibility;
2. hidden manual state and undeclared assumptions;
3. false-positive capability labels;
4. durability/completeness of machine evidence;
5. credential/license/entitlement assumptions;
6. historical `NOT_RUN` laundering;
7. engine-ranking or authority inflation.

The reviewer must not edit this producer branch.

## Residual successor after review

If the capability result survives required review, the smallest remaining non-review continuation is one bounded provider-authority/preseed route covering exactly the Unity unattended activation/account/license input and Unreal Engine 5.8 Epic-authorized source/prebuilt input required by the existing five-candidate empirical set.

Do not create a duplicate generic CI/environment recovery issue. Do not run only the three public candidates and call it the five-candidate comparison. Once the exact provider inputs exist, route one fresh W2-ENG empirical episode against then-current reviewed harness identities.

## Liveness lesson

Agent-buildable evidence machinery is **internal enablement work**, not passive external wait state. Here, building GitHub Actions capability removed DNS/toolchain ambiguity for the public candidates and exposed the true remaining provider-authority boundary. Future frontier derivations should decompose similarly before declaring an `EXTERNAL_TRIGGER_REQUIRED` blocker idle.

## Authority boundary

This packet creates no engine selection, engine ranking, empirical S1–S10 PASS, provider/legal/platform/release authority, implementation readiness, gameplay/high-throughput implementation authority, downstream verification PASS, canonicality, or integration authority. Any main publication is separately authorized and squash-only.
