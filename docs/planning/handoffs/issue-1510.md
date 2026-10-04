# Issue #1510 — Exact Traversal Policy Runtime Verification Handoff

## Status and gate

Verifier-only packet for immutable Producer #1505. **Runtime not yet verified; PASS MUST NOT be inferred from authoring this workflow, generic CI, draft state or a nonfinal PR run.** Execute the final verifier PR head through repository-native GitHub Actions, independently inspect exact GitHub run, job, sentinel, exit, log, artifact and hashes, and publish only supported schema-3 outcome. This PR has no integration/publication authority.

## Ownership and canon

- mission: `IMPLEMENTATION-DEMAND-TRAVERSAL-POLICY-02-REM-01`
- ownership CLAIM: Issue #1510 comment `5978319044`
- verifier branch: `planning/issue-1510`
- base current main at claim: `eef8a80d538a908ea685b206d97409ac48a2092f`
- canonical binding: Issue #1147 comment `5675066392`, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`
- predecessor frozen producer: Issue #1505 terminal `5978299201`, PR #1508, head `755b50d9ef0b125fef1f4358b5a4004a9d427696`. Producer and shared gameplay are read-only.
- source `game/main.gd` blob `9b406cc0a0115f0818df633eda67d69ab7779a06`; published movement smoke blob `4c5bd980eecd47fcc620d72f4819e3dab687d059`.

## Frozen source checks

The verifier workflow checks out **the source producer head** `755b50d9ef0b125fef1f4358b5a4004a9d427696`, not the verifier PR head. Check the immutable Git blobs:

- `game/components/traversal_policy/traversal_policy.gd`: `8376bd1289890d084fc94992ba56c4cd64588a44`
- `game/components/traversal_policy/traversal_policy_smoke.gd`: `3daed72928dbaecee0339e691e89403a7eaa98b2`
- `docs/planning/handoffs/issue-1505.md`: `84608ffd05a15cc83126c1319d770e0c3e592123`
- `game/tests/movement_interaction_smoke.gd`: `4c5bd980eecd47fcc620d72f4819e3dab687d059`
- `game/main.gd`: `9b406cc0a0115f0818df633eda67d69ab7779a06`
- `game/project.godot`: `9da4153ed378945ef5e9634e0e5cae48289845d8`
- reviewed engine lock `docs/planning/wave-2/evidence/ci/engine-toolchain-artifact-lock.json`: `4a88990ae24768eb4f83a8a1311e2a830834649f`

## Permitted verifier-owned files

- `.github/workflows/verify-traversal-policy-1510.yml`: initial blob `2e29583a46e3826dfab49450c148cca2055dcd3c`
- `docs/planning/handoffs/issue-1510.md`: this handoff only

Only these two verifier files may change. Neither is integrable into main by this task. Locked Godot `4.7.1-stable` ZIP digest `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba` is checked before execution. The workflow runs both `godot --headless --path game --script res://components/traversal_policy/traversal_policy_smoke.gd` and `godot --headless --path game --script res://tests/movement_interaction_smoke.gd`, with nonzero failure propagation.

Required exact sentinels: `EVERFIELD_TRAVERSAL_POLICY_SMOKE_PASS`, `EVERFIELD_MOVEMENT_INTERACTION_SMOKE_PASS`; no policy failing assertions. Expected evidence: retained `issue-1510-evidence/engine.txt`, traversal and movement smoke logs, `run-identity.txt`, immutable Actions run/job and uploaded artifact digest tied to exact verifier final PR HEAD. Existing generic CI is not equivalent.

## Reconstructable next operation

1. Open an exact-head draft PR from `planning/issue-1510` to `main` and require the path-triggered verifier GitHub Actions run to reach terminal status.
2. Independently confirm final PR HEAD, workflow file blob, producer hash checks, Godot engine lock SHA-256, both process exit statuses, Godot banner, both sentinels and zero assertion failures; retain run/job/artifact IDs and digest.
3. If PASS, terminalize schema-3 `VERIFICATION_STATUS(DONE)` bound to **the exact final workflow HEAD and immutable run**, then materialize the fresh required independent review successor (not author and not this verifier) for Producer #1505. No previous review status is upgraded.
4. If runtime FAIL or blocked, preserve failure evidence and route bounded remediation/re-execution; do not fabricate a PASS or integrate temporary workflow into main.

This is verification evidence only. No canonical, truth, persistence, gameplay wiring, provider/legal, empirical accessibility, release, production or integration authority.
