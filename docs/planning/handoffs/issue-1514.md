# Issue #1514 — Exact Public Presentation Runtime Verification Handoff

## Scope, ownership and status

This is an evidence-only runtime verifier, not a second producer and not an independent review. The frozen six-file public presentation Producer #1506 is **read-only**. No live playable, published narrative component, sibling component, canon, project configuration or game state may be modified. This handoff is authored **before** exact runtime evidence becomes available and makes **no PASS claim** merely from creating a workflow or draft PR.

- Claimed #1514 through canonical schema-3 CLAIM GitHub comment 5978349414, actor frontier-drain-public-presentation-verifier-1514-gpt56sol-20261004-1103-a.
- Main at claim eef8a80d538a908ea685b206d97409ac48a2092f.
- Canonical Issue #1147 binding comment 5675066392, program blob fd4cf1119c3f86acc3af620024eea72235e81ce4, activation ancestor 87c85cecfa9a2ffa464c4b36816a138bf41441af.
- Producer #1506 terminal STATUS(REVIEW_READY) comment 5978324440, draft PR #1513 head 37833b1e482adaa2f123edeed02b81e24a2f3688.
- Independent required Review #1515 is already materialized but **blocked** until exact isolated runtime PASS; no reviewer authority by this task.

## Frozen input identity (Git blobs)

- game/components/playable_presentation/playable_presentation.gd: 340f955c6977d43cbe735216c1758764dd25f202
- game/components/playable_presentation/world_reader.gd: 018d3c5908eca22593c7b8a6eef4a29ed1a23f0f
- game/components/playable_presentation/hearing_reader.gd: 2c06223e5d25761523ca038e160e0bce3630f0ad
- game/components/playable_presentation/consequence_reader.gd: 3cb9cb6887508f94fba865ebc428ba43fbdd38b2
- game/components/playable_presentation/playable_presentation_smoke.gd: c4f224d93c6260e6f42b93f61d7f998544893e0c
- docs/planning/handoffs/issue-1506.md: 561be48210a2637acf37a137b6951cfbefb97aac
- game/components/old_works_world/old_works_world_presentation.gd: 8e498156bb9a5413f53a84b14fc279c4be6c8f23
- game/components/commons_hearing/commons_hearing_presentation.gd: 9682c47ee2c84ea42417651d0ca2e4f30ebf78b2
- game/components/commitment_consequences/commitment_consequence_presentation.gd: 419688e17515bf5f67b383182c0b6330111ce4be
- game/main.gd: 9b406cc0a0115f0818df633eda67d69ab7779a06
- game/project.godot: 9da4153ed378945ef5e9634e0e5cae48289845d8
- docs/planning/wave-2/evidence/ci/engine-toolchain-artifact-lock.json: 4a88990ae24768eb4f83a8a1311e2a830834649f

## Exclusive verifier-owned files

- .github/workflows/verify-playable-presentation-1514.yml: 884c6a750b694364376c64059c988005ce90423c
- docs/planning/handoffs/issue-1514.md: this file

The temporary workflow checks out the **frozen producer SHA**, checks all twelve exact frozen source/provenance/engine blobs, parses the reviewed engine lock and downloads locked Godot 4.7.1-stable Linux x86_64 ZIP with SHA-256 c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba; checks engine identity 4.7.1.stable.official.a13da4feb; executes:

Godot_v4.7.1-stable_linux.x86_64 --headless --path game --script res://components/playable_presentation/playable_presentation_smoke.gd

Runtime success requires process exit zero; exact sentinel EVERFIELD_PLAYABLE_PRESENTATION_SMOKE_PASS; no EF-PRESENTATION FAIL, FAIL sentinel or Godot parse/runtime error. This is an isolated route-parity, private-provenance, public-source, unknown-input, nonconsent, deliberate deferral and mystery-nonclosure regression. General CI run 37190643993 is NOT this test.

## Final-head verification required before terminal

1. Create/open an exact-head **draft** PR from planning/issue-1514 into main, with only workflow and handoff. Never touch Producer #1506 / PR #1513.
2. Trigger/read exact final verifier PR-head GitHub Actions run. Confirm successful job, locked checkout of immutable Producer #1506, reviewed ZIP hash and engine banner, source hash gates, process exit zero, no smoke failures, literal PASS sentinel and retained artifact with run/job/artifact ID and digest. A run from an earlier verifier workflow commit does not count.
3. Only if full final-head evidence passes, publish schema-3 VERIFICATION_STATUS(DONE) with disposition PASS_EXACT_PUBLIC_PLAYABLE_PRESENTATION_RUNTIME_SMOKE and activate **existing** separate independent required Review #1515; reviewer must differ from producer #1506 and verifier #1514. Do not issue a clean review or integrate anything in this verification task.
4. If any engine/smoke/hash/identity/execution criterion fails, retain exact logs/artifact and terminalize accurate FAIL or BLOCKED with bounded remediation and required-next-route. Fail closed; do not invent authority.

No new gameplay mechanic or narrative outcome, shared-scene wiring, implicit consent, resolution of MYS:FRAGMENTATION-CAUSE=UNKNOWN_BY_DESIGN, private Anwen provenance exposure, persistence, empirical accessibility certification, canonicalization, production/release or integration authority. The workflow is temporary **nonintegrable verification infrastructure** without a separately authorized publication route.
