# Issue #1626 — public text fit empirical probe and continuation

## Status: HANDOFF_READY, NOT REVIEW_READY, NOT VERIFIED

Owner: first/only valid schema-3 CLAIM **#6107400582**, session `frontier-public-text-evaluate-1626-gpt6-20261011-1103-01`, task `IMPLEMENTATION-DEMAND-PUBLIC-TEXT-PAGING-04`. Start/current main **`3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`**; canonical Planning Program #1147 binding **#5675066392**, program blob **`fd4cf1119c3f86acc3af620024eea72235e81ce4`**, activation ancestor **`87c85cecfa9a2ffa464c4b36816a138bf41441af`**. Routing source #1624 terminal #6106697850, independent sibling implementation #1627 and blocked shared fan-in #1629.

## Inspected published executable / factual boundary

- Published exact `game/project.godot` blob `9da4153ed378945ef5e9634e0e5cae48289845d8` sets 960×540. Published `game/main.gd` blob **`921ff7a1ce28ed4df4a67a7645752d7b441603f7`** creates a `PresentationPanel` at (486, 88), size (450, 154), and a `Presentation` Label at (500, 98), size (422, 134), `AUTOWRAP_WORD_SMART`, font 12. `game/main.tscn` blob `02b943321c258bb807f9496c7a270221df112b31` instantiates this scene. No next/back or page/scroll state is currently connected.
- Published provider `game/components/playable_presentation/playable_presentation.gd`, blob **`ba819915fc55e444d54d46671892cea35cb6b3cf`**, returns public text for world intro, all three Old Works stations, opening Commons Hearing, three hearing choices, combined hearing/consequence, and route endings. World/Hearing/Consequence readers are authoritative approved prose; source `UNKNOWN_BY_DESIGN` and deferral/nonconsent constraints remain intact.
- **No measured text overflow or visible crop has yet been demonstrated.** The fixed label geometry and long narrative strings form a testable hypothesis, not a verified defect. An unauthenticated estimate of line count, a static character count, or a green unrelated CI job cannot justify publishing pagination code.

## Exclusive work in this branch

Only new `game/tests/public_text_navigation/public_text_fit_smoke.gd` (Git blob **`949adfabbd685ddcfd11be823e45916b5fafe50e`**) and this own handoff are authorized. This source-free, read-only `SceneTree` Godot probe instantiates the existing published `main.tscn`, checks exact viewport/panel/label geometry and wrapping, reads the live `playable_presentation` provider without mutating approved strings, and cycles **13** independent already-reviewed cases: world intro, public record, material trace, explicit truth deferral, hearing opening, all three hearing choice texts, all three corresponding combined hearing/consequence views, and the two terminal consequences. For each, it measures actual Label line count, line heights, minimum height and available 134 px, emitting `EVERFIELD_PUBLIC_TEXT_FIT_EVIDENCE` including a text SHA-256 and whether the measured required height exceeds the label height. An error makes the probe exit nonzero; on complete measurements it emits `EVERFIELD_PUBLIC_TEXT_FIT_MEASURED scenarios=13 overflow_count=N`.

This program and its pass sentinel are **authored but have not executed**. The current agent environment does not provide the reviewed Godot executable. A `MEASURED` sentinel would certify successful *measurement*, not absence of clipping, all player-view correctness, independent verification, empirical accessibility, nor eventual approved implementation.

No code under `game/components/public_text_navigation/**` was created: paging is **intentionally deferred pending evidence**, not claimed complete. No shared scene/controller, public prose, sibling source, CI, or canonical files were changed.

## Exact required next execution

Use the independent, SHA-256 locked **Godot 4.7.1-stable** reviewed Linux executable archive with ZIP SHA-256 **`c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`** and engine version `4.7.1.stable.official.a13da4feb`. Recheck exact task branch HEAD, current-main ancestry, canonical binding, owner generation/lease, and frozen text-provider Git blobs; then run:

```bash
godot --headless --path game --script res://tests/public_text_navigation/public_text_fit_smoke.gd
```

Capture actual process exit code, all `EVERFIELD_PUBLIC_TEXT_FIT_EVIDENCE` lines and the `EVERFIELD_PUBLIC_TEXT_FIT_MEASURED` sentinel, actual runner and binary SHA-256 identities, exact checked-out head and main, and independently inspect **all** 13 cases at true rendered bounds/visible text. Do not infer successful fit from one successful base-project CI suite. Re-run normal Godot scene/movement/approved-component smokes on exact final head. If probe source itself has a parser/API error, repair only within the owned test root and rerun before claiming any measurement. An optional independent reviewer/verifier may inspect the empirical artifacts; producer authorship/CI alone is insufficient for component publication.

**Branching decision after honest measurement**:
1. If all the exact published public cases fit and no real loss of text is observed, record an evidence-backed bounded **NO_OP** and do not add unused navigation runtime code; preserve concrete successor route to blocked shared fan-in #1629 as explicitly scoped.
2. If at least one exact published case provably overflows, implement the smallest pure, fail-closed, copy-safe public text paging/navigation model **solely** in `game/components/public_text_navigation/**`, with independent tests in `game/tests/public_text_navigation/**`; preserve exact byte-for-byte source text, order, paragraph boundaries, punctuation, refusal/deferral and `UNKNOWN_BY_DESIGN`, and reject malformed inputs, unsafe split boundaries and out-of-range page indices. Do not touch `game/main.gd` or shared scene: #1629 owns actual future wiring. Require exact-final-head runtime smoke, independent verification/required distinct clean review and separate independently authorized **squash-only NONCANONICAL** integration before fan-in.
3. If runner or source validation remains unavailable or a negative test fails, remain `HANDOFF_READY` or route a genuinely scoped independent validation/correction task; **never** publish fictitious `STATUS(REVIEW_READY)` or `VERIFICATION_STATUS(PASS)`.

## Scope, risk and authority

The initial test seeks missing visibility, not new narrative/story, player route, engine selection, personal information, a new global gate, or accessibility certification. No new private Anwen information or causal mystery winner; no new consent/commitment inference. Review, runtime verification, downstream game fan-in and separate squash-only source integration are still outstanding, and no integration/canonical/implementation-readiness/production/release authority is conferred. Existing sibling #1627 and its independent verifier #1635 are different conflict domains; #1629 remains hard blocked until both roots satisfy their own independent gates.

Durable next action: independently execute exact-head viewport measurement; do **not** treat this task as done or REVIEW_READY until evidence exists.
