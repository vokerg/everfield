# Issue #1627 — Public route-history view component handoff

## State and authority
Producer work-in-progress, **NOT REVIEW_READY / NOT VERIFIED**. First winner schema-3 CLAIM #6106708252 by `frontier-implement-route-history-1627-gpt6-20261011-0932-01`; source routing intake #1624 terminal #6106697850 and independent sibling #1626. Current main at episode start `3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`. Canonical #1147 binding #5675066392 / blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`; earlier gameplay source #1545 was reviewed/verified and squash-published by #1583 into `ef75cc78a217695097f5d8f6cfb48ea04beaa7de`.

## Files and implementation
- `game/components/route_history_view/route_history_view.gd`: pure read-only projection of immutable `SessionState.snapshot()` history into a numbered list of existing public event titles. All nine allowed source events are mapped only to existing published World and Consequence titles plus the literal already-published Commons Hearing title. Unknown/private/malformed events, unsafe/missing source contract or mystery state change fail closed without echoing secret event contents; the model does not mutate the session or reviewed providers.
- `game/tests/route_history_view/route_history_view_smoke.gd`: an isolated Godot SceneTree test for empty history, approved public event ordering, deferral→reopened hearing→records-first completion, deep-copy isolation, unknown/private IDs, malformed/missing history and sources, immutable mystery, and reset.
- This document is the only other owned path. The sibling `game/components/public_text_navigation/**`, shared `game/main.gd` / `game/main.tscn` / `game/smoke_test.gd`, Godot CI and all canon/source content remain unchanged.

## Test and verification limitation
The source and tests are **authored, not runtime verified** at this handoff. The present connector/container cannot acquire the reviewed Godot 4.7.1 executable (no locally installed Godot and container network access is unavailable). The current `.github/workflows/godot-first-playable-smoke.yml` executes existing integrated suite files but does NOT invoke the new isolated `res://tests/route_history_view/route_history_view_smoke.gd`; even a green existing PR CI does not establish that this test ran or this component passed.

Run on exact candidate HEAD with the reviewed immutable Godot 4.7.1 binary `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`:

```bash
godot --headless --path game --script res://tests/route_history_view/route_history_view_smoke.gd
```

Demand the exact `EVERFIELD_ROUTE_HISTORY_VIEW_PASS checks=N` sentinel, exit code zero, no parser errors, and archived exact run/head/binary identity. A separately eligible exact-HEAD read-only CI validation workflow and independent reviewer must verify the component; **do not** reinterpret old CI's fixed-suite PASS as this new smoke. No current authorization to modify shared CI in this source PR; if only GitHub-hosted runtime is available, materialize a small separate, properly owned validation route/PR rather than edit shared workflow through #1627.

## Required next route
1. Reconcile current main, branch and first-owner lease. Inspect source for GDScript parse/typing and contract/security defects before finalizing.
2. On an authorized locked Godot 4.7.1 runner, run this isolated new suite at actual final PR head plus full existing main scene/movement smokes. Archive proof and check changed-path identity. Any failure requires own remediation/continuation.
3. Only after that, current owner may publish `STATUS(REVIEW_READY)` with an exact-head **draft** PR already open, then route a genuinely independent required code/security/runtime review and independent verification where required.
4. Only a distinct separately authorized owner may later squash-publish clean, verified component as NONCANONICAL. Shared scene integration is exclusively the blocked fan-in #1629, after sibling #1626 meets its gates.

## Exclusions
No final canon or mystery truth, no private Anwen content, no invented narrative text, no implication that deferral is assent, no persistent save, no empirical accessibility claims, no release/production or integration authority. This handoff does not certify a passing smoke or integrated gameplay.
