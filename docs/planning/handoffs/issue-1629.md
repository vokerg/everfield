# Issue #1629 — shared playable public text and route-history fan-in handoff

**Mission:** IMPLEMENTATION-INCREMENT-PUBLIC-TEXT-AND-ROUTE-HISTORY-04.  
**First-winning owner claim:** #6130526634, GitHub `created_at=2026-10-12T18:48:50Z`, actor `frontier-independent-ui-fanin-1629-gpt6-20261012-2115-cph-01`, immediate contention recheck passed.  
**Base main:** `a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`.  
**Canonical binding:** Issue #1147 #5675066392, active program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.  
**State:** BOUNDED IMPLEMENTATION CANDIDATE, **not yet externally verified or independently reviewed and not integration-authorized**.

## Prerequisite sources truly integrated

Source route-history #1651 / exact-head Godot verification #1654 / clean required code review #1659 / separately owner-authorized **squash** Issue #1670 `INTEGRATION_STATUS(DONE)` #6118200016 -> published NONCANONICAL main `8f8223b0c58956bbc888760ef14f63fa79d2117d`; true frozen component blob `8f32a8e925d8fb0765e91ef102ad0827a0b88958`.

Source public-text-navigation #1626 / locked Godot verification #1655 / genuinely distinct required clean review #1671 / separately owner-authorized **squash** Issue #1687 `INTEGRATION_STATUS(DONE)` #6127155018 -> published NONCANONICAL current main `a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`; true frozen component blob `b081bfe234c18884650992d7251b55effbec8c2f`. No sibling component root is changed in this fan-in.

## Exclusive six changed paths

- `game/main.gd`: glue-only scenario mapping; compare exact 13-scenario published text model source SHA-256/full concatenation before displaying approved pages, route Z/X to UI-only previous/next, full-source getter retained for regression/audit, new real visible-page getter, page-count UI only for actual multipage cases. Consume only genuine `session_state.snapshot()` and exact reviewed providers via the published route-history model, expose bounded scrollable right-side history with eight entries per page and C/V history navigation. Preserve E/1/2/3/R and WASD/arrow logic.
- `game/smoke_test.gd`: actual scene source-byte reconstruction, visible label and page count, first/last no-wrap, real repair and reopen/deferral/records-first history, 10-event history page boundaries and state immutability.
- `game/tests/movement_interaction_smoke.gd`: real Godot Input dispatch Z/X/C/V, release/echo/physical-only negatives, unaffected state/consent and R reset.
- `.github/workflows/godot-first-playable-smoke.yml`: retains exact reviewed Godot 4.7.1 zip SHA-256, existing shared scene/player/isolated suite harness; adds exact published prerequisite blob locks and execution of both independently published isolated nav/history smokes, logging PASS and script faults with immutable evidence.
- `docs/implementation/first-playable.md`: player-facing new keys, complete source-vs-page and history semantics, exact-source and headless evidence limits.
- `docs/planning/handoffs/issue-1629.md`: task-owned provenance, gates, next route (this file).

No `game/main.tscn`, common components, public approved prose/content, other `game/tests/**`, state provider, canonical/production/release files or sibling roots are altered. Shared right-side history is read-only and controls cannot synthesize future events or route outcomes.

## Pending exact final HEAD gates

1. Open source **DRAFT PR** from `planning/issue-1629` into latest main with exactly these six paths and no sibling overlap; re-derive current main and first winning owner before any terminal.
2. Inspect exact PR HEAD and hosted, fully immutable SHA-256-locked Godot **4.7.1** workflow run: primary `EVERFIELD_SMOKE_PASS`, movement `EVERFIELD_MOVEMENT_INTERACTION_SMOKE_PASS`, both independent-root `EVERFIELD_PUBLIC_TEXT_NAV_PASS` and `EVERFIELD_ROUTE_HISTORY_VIEW_PASS`, all existing component suites SUCCESS; capture exact run/job/hash-logged artifact ID. If failed, remediate on this same branch within six scoped paths, never falsely report PASS.
3. Genuine **distinct independent exact-final-head scene verification** is required before clean mandatory adversarial code/security review of this joint scene. The author and this execution cannot self-certify either; do not call source-authored CI independent verification. If verifier is outstanding, publish a recoverable `STATUS(HANDOFF_READY)` with one required verification successor, not a `REVIEW_READY` or source integration.
4. After independent verification PASS, a different authorized owner episode may resume #1629 (proper GitHub claim/intent/lease) to publish source `STATUS(REVIEW_READY)` on unchanged exact HEAD and materialize one **fresh genuinely distinct mandatory independent adversarial review**. Then, and only after CLEAN, permit separately claimed, current-main-compatible, expected-head **SQUASH-only NONCANONICAL source publication**. No self-review/self-merge.
5. After independently authorized source publication, reevaluate the actual playable at 960×540 for visual/pixel fit and accessibility, without turning a headless-only test into display or production certification; #84 implementation continuation route stays active.

**Authority:** draft implementation and authored executable evidence only. No canonical narrative, private/Anwen mystery, truth/consent, accessibility, production, release, legal/provider, or engine-readiness promotion.
