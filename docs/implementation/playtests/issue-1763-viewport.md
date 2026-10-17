# Issue #1763 — 960×540 viewport evaluation: blocked evidence intake

**Mission:** `IMPLEMENTATION-EVALUATION-LIVE-PLAYABLE-VIEWPORT-05`  
**Disposition:** `BLOCKED_ENVIRONMENT_NO_RENDERER` — **not** a playtest PASS, implementation defect finding, accessibility evaluation, clean review, or completion decision.  
**Observation date:** 2026-10-15 (UTC); diagnostic runtime check at `2026-10-15T08:58:22Z`.  
**Frozen baseline checked:** `main@7da4c2d50412fe134c8632264908560b8b7995ce`; no gameplay files modified.  
**Canonical authority:** Issue #1147 terminal #5675066392; program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`. This evidence record adds no canonical or implementation-completion authority.

## Scope and sources

This issue requires an **actual rendered** pinned-Godot 4.7.1 960×540 evaluation, genuine screenshot/frame evidence and keyboard interactions across public evidence, hearing, commitments, explicit deferral, public text paging, route history and reset. The source is current integrated first-playable; intake Issue #1759 completed and identifies integrated gameplay `ef75cc78a217695097f5d8f6cfb48ea04beaa7de`. Issue #1763 identifies prior exact-head headless scenario proof, which does **not** establish physical legibility or nonoverlap.

Exact main Git blobs read:

| Surface | SHA / read-only observation |
|---|---|
| `game/project.godot` | `9da4153ed378945ef5e9634e0e5cae48289845d8`; sets viewport and window overrides 960×540, canvas-items stretching and GL compatibility |
| `game/main.gd` | `df3d7cbc7a8048803870e9ab12a06d7d249a1792`; builds screen UI and keyboard interaction |
| `game/main.tscn` | `02b943321c258bb807f9496c7a270221df112b31` |
| `game/components/public_text_navigation/public_text_navigation.gd` | `b081bfe234c18884650992d7251b55effbec8c2f` |
| `game/components/route_history_view/route_history_view.gd` | `8f32a8e925d8fb0765e91ef102ad0827a0b88958` |
| `.github/workflows/godot-first-playable-smoke.yml` | `9b914e62f715630cb02b035cf996bfdbc3779e6c`; pinned Godot 4.7.1 full **headless** smoke and logging, not interactive pixel capture |
| `.github/planning-frontier-routes.json` | `6672d64b72232a4022c55a3a68ca1d0c6938489c`; current `routes` map empty (no registered internal automation dispatch) |

## Executed environment diagnostic — BLOCKED

Commands executed in the supplied task execution container:

```sh
command -v godot
command -v godot4
command -v Godot_v4.7.1-stable_linux.x86_64
python - <<'PY'
import shutil
for b in ('godot','godot4','Godot_v4.7.1-stable_linux.x86_64'):
    print(b, shutil.which(b))
PY
```

All three Python `shutil.which` results were `None`; none of the executable lookups resolved. A filesystem search under `/opt`, `/usr/local/bin`, and `/home/oai` found no Godot installation. Direct external artifact acquisition is not available to this container: HTTPS test for `raw.githubusercontent.com` returned `curl: (6) Could not resolve host`. Consequently no Godot 4.7.1 engine was launched, no genuine window rendered, no game input was sent, and **no screenshot, font-layout measurements or accessibility certification** was produced.

The repository's main `godot-first-playable-smoke.yml` downloads and cryptographically checks the reviewed Linux Godot binary on a hosted runner, then executes `--headless` smoke scripts and uploads logs. A headless log PASS is not the missing 960×540 pixel test. Its `workflow_dispatch` declaration does not alone create an authorized repository-internal automation route: `.github/planning-frontier-routes.json` has no route registered. Do not substitute logs for an authentic GUI run or invent a hosted run identity.

## Read-only source geometry (not visual PASS or a confirmed defect)

Static `game/main.gd` layout declares: title `(24,14)` size `900×42`, status `(26,52)` size `908×32`, presentation panel `(486,88)` size `450×154`, presentation label `(500,98)` size `422×134`, navigation label `(500,242)` size `422×22`, history panel `(486,276)` size `450×182`, rich history text `(500,308)` size `422×140` with scrollbar enabled, objective `(26,474)` size `908×30`, and diagnostic line `(26,506)` size `908×26`. These are source declarations only. Font metrics, line wraps, clipping, scroll interactions and panel stacking have **not** been observed at runtime. The title/status declared rectangles touch/overlap by four pixels in geometry; this is a **visual check target**, not a verified text collision.

The source maps `Z/X` to public presentation paging and `C/V` to history paging, and includes session event/route state, but physical key operation was not witnessed.

## Recovery test matrix — required before any implementation roots

1. Acquire/verify the **exact pinned Godot 4.7.1-stable** binary against the repository's reviewed artifact lock; capture `--version`, checksum, checkout HEAD, display backend, and actual pixel dimensions. Use an actual non-headless 960×540 window/framebuffer, screenshots or equivalent authentic renders, and reproducible input traces. A simulated text rendering or headless log cannot satisfy this gate.
2. From a clean playable reset, record authentic first frame and Old Works approaches. Exercise movement, `E/1/2/3/R`, record/trace/defer, Commons Hearing, repair, records-first and explicit nonconsent/deferral. Capture frame+state/input provenance for every significant transition and both successful outcomes.
3. Reopen all **13 approved public-text scenarios**, checking first/middle/last page where applicable and the full existing 41-page evidence envelope. Check top/bottom of text, navigation feedback and invisible/offscreen text; preserve exact approved prose and `MYS:FRAGMENTATION-CAUSE = UNKNOWN_BY_DESIGN`.
4. Produce **10+ authentic** history events and exercise `C/V` previous/next, both no-wrap boundaries, long titles, actual scroll and reset; preserve evidence/claim and nonconsent separation.
5. Record for each genuine failure its screenshot, scenario, input, view size, exact main/engine SHA, severity and independently reproducible steps. Separate confirmed on-screen failures from hypotheses inferred by static geometry.
6. Only when evidence establishes multiple truly disjoint implementable defects, materialize 2–4 bounded component roots and one shared fan-in, each under the original issue's review and verification gates. Otherwise name one bounded fix or a product-evaluation continuation. **Never terminate implementation with `required_next_route: NONE` without specific owner authority.**

## Risk, alternatives and limits

**Unresolved BLOCKING evaluation prerequisite:** a render-capable pinned Godot runtime and authentic physical input/screenshot capture. Available main CI offers hash-locked headless contract checks, valuable as adjunct evidence but not a substitute. Neither gameplay quality, legibility, viewport completeness, renderer compatibility nor accessibility can be judged from the present inspection. No gameplay implementation, review approval, code changes, rollout, PR integration, or canonical status is authorized by this blocked diagnostic.

**Exact next action:** resume **this same Issue #1763**, not a speculative parallel gameplay task, with a compatible render-capable execution environment. Follow the canonical `HANDOFF` intent and winning `RESUME` transition, revalidate main and ownership, then execute the missing runtime matrix. Keep this branch as diagnostic provenance; do not merge documentation merely to imply validation.
