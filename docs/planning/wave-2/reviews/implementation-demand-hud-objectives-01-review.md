# Required independent review — HUD objective/status view-model

**Issue:** #1474 (`IMPLEMENTATION-DEMAND-HUD-OBJECTIVES-01-REV-01`)  
**Producer:** #1463 / draft PR #1473, exact head `e2be96598dca388b84c70077b7d9b304f9a9fb1f`  
**Disposition:** **CHANGES_NEEDED** (0 BLOCKER, **1 MAJOR** missing exact locked-Godot runtime evidence, 0 correction-requiring MINOR).  
**Trust:** degraded single-agent fresh independent review episode; not the producer actor `frontier-drain-hud-objectives-1463-gpt56sol-20261003-01`.

## Exact scope, authority and provenance
The current canonical program remains blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, bound by #1147 comment `5675066392`; canonical activation `87c85cecfa9a2ffa464c4b36816a138bf41441af` is on current `main@9096e84612e7445e1d2285b42578fb4f5cfd5f07` ancestry. Review claim: #1474 comment `5977111702`. Source first-playable Review #1371 was clean. Producer terminal #1463 comment `5972503707` is `REVIEW_READY`; exact draft PR #1473 remains open and at the frozen head.

Reconstructed producer diff from base `849642087297f8b8c83e5bda927aa6ce9d5ef899`: **exactly three allowed paths**:
- `game/components/hud_objectives/hud_objective_model.gd`, blob `59480c7b8c7f3f8161cd261fb195704f8299679f`;
- `game/components/hud_objectives/hud_objective_model_smoke.gd`, blob `821785fd941b6865e543c2bbb09fd643fcc67c1c`;
- `docs/planning/handoffs/issue-1463.md`, blob `2d4c9fa5039a19c0c5400458a9383747953b2b37`.

No changes to shared `game/main.gd`, `game/main.tscn`, project/workflow files or sibling components. The source `game/main.gd` blob is `b96659a1cf461a96934666293aecaa565e68579b`; current `main` carries `4ea6ab02de1fa8bfde2d976b0f3f551dc8f40b97` after separate presentation fan-in. The latest post-#1487 main advance is review-provenance-only (`docs/planning/handoffs/issue-1471.md`, `docs/planning/wave-2/reviews/implementation-increment-old-works-presentation-01-review.md`), with no HUD-owned path conflict. No current-main phase semantics drift invalidating the standalone extraction was found.

## Bounded static adversarial review
**Static contract matches** (not an empirical runtime PASS):
1. `build_view` is a pure `RefCounted` dictionary-to-view adapter; no Node/scene, input, filesystem, network, persistence, mutable singleton, live gameplay or side effects.
2. First-playable precedence matches: completion > missing public record > insufficient corroboration/deferral > open hearing > uncommitted hearing navigation > project-table committed. The current program's separate old-works presentation wording changes do not establish gameplay authority in this component.
3. `record_read && (trace_inspected || deferred_truth)` gates investigation-ready presentation; record+trace and record+explicit-defer are distinct. The status string preserves `Record`, `Trace`, `Deferred truth`, `Commitment`, and `UNKNOWN_BY_DESIGN` without fabricating the other route.
4. An open hearing presents repair pilot/records-first/defer. Deferring commitment leaves commitment empty and non-complete/reopenable. Supported commitments navigate to Project Table; completion exposes only `BOUNDED_REPAIR_PILOT_STARTED` or `RECORDS_FIRST_PACKAGE_FILED` for the respective exact commitment.
5. Required fields/types, supported commitment, mystery invariant, investigation/negotiation/commitment consistency, and completion/outcome pairing fail closed with `valid:false`, `phase:INVALID_STATE`, `Progress is not inferred`. Optional station-title metadata is read-only and has typed fallbacks. No input/history mutation was identified.
6. The frozen smoke includes the above valid/invalid states, mutation guards, semantic route distinctions, and required exact sentinel `EVERFIELD_HUD_OBJECTIVE_MODEL_SMOKE_PASS`.

## Material finding

### MAJOR: MISSING_REQUIRED_EXACT_HUD_RUNTIME_EVIDENCE

Issue #1474 explicitly requires the exact frozen smoke under repository-reviewed Godot `4.7.1-stable` to exit zero and emit `EVERFIELD_HUD_OBJECTIVE_MODEL_SMOKE_PASS`. Producer #1463 explicitly did **not** execute it. The only producer-head Actions run observed, `37146421472` / job `111271201871` (`Godot first-playable smoke`), passed ordinary import/first-playable tests but does **not** execute or log the exact isolated HUD script or required sentinel. The local review environment has no Godot executable. It would be an unsupported authority upgrade to reinterpret generic regression success as the required isolated test.

**Minimal correction route:** verification-only blocking successor bound to the **read-only** exact Producer #1463 head/blobs and `game/project.godot` lock, invoking:

`godot --headless --path game --script res://components/hud_objectives/hud_objective_model_smoke.gd`

Use repository-reviewed Godot `4.7.1-stable`, artifact SHA-256 `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`; require exit 0, sentinel `EVERFIELD_HUD_OBJECTIVE_MODEL_SMOKE_PASS`, immutable exact-head run/job/log/artifact. Review-owned paths do not permit adding a workflow here. A separate verifier must obtain evidence, and **a fresh re-review** must assess it; do not self-upgrade this `CHANGES_NEEDED` review.

## Authority boundary
No clean producer approval, component publication, integration, live scene mutation, gameplay progression, truth/canon resolution, persistence/save-load, production/release, accessibility certification, provider/legal or canonical authority. This review is bounded noncanonical diagnostic provenance only and may itself be squash-published only under a separately authorized integration route.
