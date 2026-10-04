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


## Recovered continuation: independently observed prior-head executable evidence
- The first verifier owner left a frozen open draft PR #1517. Its corrected workflow head was `f8e810eea3a5ad4536129ff9fd0c307074a10d10`, with exact two-path diff (workflow Git blob `e966bf3f96d99a8be601c213dbce2b49b903fa68`, this handoff's prior Git blob `da90e241d50c2e819667bf9e258b3c2d59577314`).
- First owner CLAIM `5978320931` created 2026-10-04 08:59:34 UTC; no valid renewal, terminal, handoff or later ownership generation occurred before the 14:59:34 UTC six-hour lease expiry. Fresh recovery intent `5982995041` and winner RECOVER `5982997440`, distinct actor session `frontier-drain-station-verifier-1511-recover-gpt56sol-20261004-2018-01` re-established ownership after checking frozen producer PR #1509, current-main compatibility and active canonical binding.
- Prior-head GitHub Actions verifier run `37190887391` attempt 1, job `111402620773`, successful exact workflow run head `f8e810eea3a5ad4536129ff9fd0c307074a10d10`: checkout and hash guards passed; ZIP `godot.zip: OK` with reviewed SHA256; observed `4.7.1.stable.official.a13da4feb`; **73 actual isolated smoke PASS assertions**, **0 actual smoke FAIL assertions**, process exit 0, exact `EVERFIELD_STATION_WORLD_SMOKE_PASS`. Prior unsuccessful workflow run `37190804824` at older workflow head `316a1ba7f8d26bfe31195f5ac97b7d79287747da` is **not** acceptance evidence.
- Retained prior-head artifact ID `11299500434`, `1833` bytes, digest `sha256:38dba7ecac01f50a20211272836cba67a02c863c0ca173d9aef42c864dbca7e0`; decoded job log SHA-256 `2286f3841d7fecd2364d00ae7eca8b88aa60766a0a5b42408cd05b7abd2d850a`. Source producer `54a4a044ea56e10bf3dd26e358ead7353fd4d438` and frozen three component/handoff blob IDs remain unchanged.
- Current main `d02bb66a134d5ec35c54782cb9b7d1d96e0db4ea` advances source base `eef8a80d538a908ea685b206d97409ac48a2092f` by five disjoint squash commits; zero overlap with producer station-world root or this verifier's two owned files.

**Final-head re-execution gate:** Appending this evidence to the handoff changes the verifier PR head. Thus the prior-head PASS above is *reproducible historical evidence, not final-head terminal PASS*; the required next workflow run on the new immutable PR head must independently repeat all locks, sentinel, exit, and retained run/job/artifact/log before schema-3 `VERIFICATION_STATUS(DONE)` and activation of Review #1512. The terminal GitHub issue comment must record that exact newly observed final run. This temporary workflow/handoff packet is not source/review/main/canon/integration authority.
