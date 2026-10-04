# Handoff — Issue #1511 / exact station-world runtime verifier

## Scope, authority and ownership
- Mission: `IMPLEMENTATION-DEMAND-STATION-WORLD-02-REM-01`, blocking exact-head Godot 4.7.1 runtime verification.
- Issue #1511 winning CLAIM `5978320931`, actor `frontier-drain-station-world-verifier-1511-gpt56sol-20261004-1059-01`, ownership verified before branch creation.
- Branch `planning/issue-1511`, initial base `main@eef8a80d538a908ea685b206d97409ac48a2092f`.
- Active canonical binding: Issue #1147 comment `5675066392`; program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`; activation `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- This packet is temporary **verification-only evidence infrastructure**. It is not an independent review, component correction, publication, canonicalization, game integration, persistence, accessibility certification, production or release authority.

## Immutable source under verification
- Producer #1504 claim `5978270304`, terminal `5978306462`, exact frozen draft PR #1509, branch `planning/issue-1504`, HEAD `54a4a044ea56e10bf3dd26e358ead7353fd4d438`.
- Station metadata `game/components/station_world/station_world.gd` blob `87fefab8816a2ab8795c54877299716ec86b227e`.
- Isolated smoke `game/components/station_world/station_world_smoke.gd` blob `0c972e251de6e4fb1a86bbecbce757eaa56999ce`.
- Producer handoff `docs/planning/handoffs/issue-1504.md` blob `cc492f3671d884ea3e9c05995cdeab66af4b46c7`.
- Current shared playable source reference `game/main.gd` blob `9b406cc0a0115f0818df633eda67d69ab7779a06`.
- Godot project `game/project.godot` blob `9da4153ed378945ef5e9634e0e5cae48289845d8`; reviewed lock `docs/planning/wave-2/evidence/ci/engine-toolchain-artifact-lock.json` blob `4a88990ae24768eb4f83a8a1311e2a830834649f`.
- Lock entry: `4.7.1-stable`, Linux x86_64 ZIP, SHA-256 `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`. This is an observed hash lock, not a vendor signature.

## Only permitted verifier changes
1. `.github/workflows/verify-station-world-1511.yml`.
2. `docs/planning/handoffs/issue-1511.md`.

The dedicated PR workflow checks out the producer's **exact frozen head** by SHA, asserts all six producer/reference/toolchain Git blob hashes, downloads the hash-locked engine, checks the exact reviewed engine version, and runs the isolated GDScript script headlessly under fail-fast exit status. It requires an exact full-line `EVERFIELD_STATION_WORLD_SMOKE_PASS` and zero failure assertions. The workflow stores decoded stdout, engine banner, run/head/hash identity and the retained evidence artifact for reconstruction. Producer, game, sibling components and normal CI workflow remain strictly read-only.

## Initial evidence status and required next gate
**PENDING_FINAL_VERIFIER_PR_HEAD_EXECUTION**. At handoff creation no station-world runtime PASS is claimed; ordinary first-playable CI `37190490452` did not run the isolated station-world script. Open a draft verifier-only PR, then obtain the repository-native run/job/full logs and evidence artifact for the exact **final** verifier PR head. If this verifier branch changes after a run, previous results are nonfinal and must be rerun. Terminal `VERIFICATION_STATUS(DONE)` may claim PASS only if exact checkout, locked artifact, sentinel, script exit, run/job/head and retained artifact all match. Otherwise report the true FAIL or BLOCKED outcome, and route a narrow correction.

Upon independently verified PASS, activate existing required fresh independent Review **#1512**; its review actor must differ from both Producer #1504 and this verifier. Never directly integrate this temporary workflow, infer that REVIEW_READY is clean, or grant main/gameplay/canon/persistence/production/release authority.
