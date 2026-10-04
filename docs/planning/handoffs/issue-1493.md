# Issue #1493 Handoff — Exact-Head HUD Objective Model Runtime Evidence

## Role and authority
- Mission: `IMPLEMENTATION-DEMAND-HUD-OBJECTIVES-01-REM-01`
- Branch: `planning/issue-1493` / Issue #1493 claim `5977184412`, actor `frontier-drain-exact-hud-runtime-1493-gpt56sol-20261004-01`
- Canonical binding: Issue #1147 comment `5675066392`, active program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation SHA `87c85cecfa9a2ffa464c4b36816a138bf41441af`
- Branch base: `main@2f5dc5f946bdab8014427170d74d45420b1c8d4d`
- This is **verification-only infrastructure**, **not** an implementation, review, publication or integration claim.

## Immutable test subject
- Producer #1463 terminal `5972503707`, PR #1473, branch `planning/issue-1463` at exact frozen head `e2be96598dca388b84c70077b7d9b304f9a9fb1f`
- HUD model: `game/components/hud_objectives/hud_objective_model.gd`, blob `59480c7b8c7f3f8161cd261fb195704f8299679f`
- Isolated smoke: `game/components/hud_objectives/hud_objective_model_smoke.gd`, blob `821785fd941b6865e543c2bbb09fd643fcc67c1c`
- Producer handoff: `docs/planning/handoffs/issue-1463.md`, blob `2d4c9fa5039a19c0c5400458a9383747953b2b37`
- `game/project.godot` blob `9da4153ed378945ef5e9634e0e5cae48289845d8`
- Reviewed Godot lock `docs/planning/wave-2/evidence/ci/engine-toolchain-artifact-lock.json` blob `4a88990ae24768eb4f83a8a1311e2a830834649f`
- Reviewed artifact: Godot `4.7.1-stable` Linux x86_64 ZIP SHA-256 `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`

## Review defect and bounded verification
- Required Review #1474 claim `5977111702`, terminal `5977135158` / `CHANGES_NEEDED`: sole MAJOR `MISSING_REQUIRED_EXACT_HUD_RUNTIME_EVIDENCE`. Static HUD/path findings clean; generic first-playable smoke is *not* acceptable runtime evidence.
- New, temporary `.github/workflows/verify-hud-objectives-1493.yml` is the only executable mutation in this episode.
- It checks out and asserts exact frozen Producer head and five blob identities, validates reviewed Godot lock, downloads SHA-256-pinned engine, records engine banner, then runs `--headless --path game --script res://components/hud_objectives/hud_objective_model_smoke.gd` using fail-fast shell and exact-line sentinel `EVERFIELD_HUD_OBJECTIVE_MODEL_SMOKE_PASS`.
- The workflow captures exact checked-out SHA, workflow PR head SHA, source hashes, engine identity, run ID and attempt, stdout and engine version in a 30-day retained evidence artifact. Its own workflow branch is **non-integrable**.
- Evidence state **at handoff creation**: `PENDING_REPOSITORY_NATIVE_FINAL_HEAD_EXECUTION`. No runtime PASS is preclaimed. Later final-head, exact immutable job/log/artifact bindings and disposition must be recorded in terminal GitHub status and reflected in this handoff where applicable.

## Permitted branch paths
1. `.github/workflows/verify-hud-objectives-1493.yml`
2. `docs/planning/handoffs/issue-1493.md`

No producer, review, project, shared gameplay, sibling component, workflow outside the one allowed temporary file, or canonical artifact mutation permitted.

## Next route and boundary
Open an exact-head draft PR. Inspect the *final* branch-head GitHub Actions run/job/log/artifact, require exit 0 and exact sentinel. If updated after a run, demand a new final confirming run. Exact PASS must route a new **independent required HUD re-review** (not self-upgrade original Review #1474); substantive FAIL routes bounded producer remediation, while workflow-only infrastructure defects remain this verifier's responsibility. There is no integration, canon/truth-resolution, gameplay-state, persistence/save-load, accessibility-certification, legal/provider, production, or release authority.
