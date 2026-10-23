# 2026-10-23 continuation — exact-head seven-frame evidence independently audited (PARTIAL, NOT PLAYTEST PASS)

**Episode authority:** original Issue #1763 HANDOFF terminal #6264796234, this episode's first uncontested HANDOFF `RESUME_INTENT` #6358865594 and `RESUME` #6358871121; actor `everfield-viewport-artifact-reconcile-1763-gpt6-20261023-01`. Refreshed `main@1cf7f67d290bb01c42705610a49647c0a67199bc`. Canonical binding #1147/#5675066392 and unchanged program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4` (activation `87c85cecfa9a2ffa464c4b36816a138bf41441af` confirmed ancestor). This update adds evidence to the same two-document task branch/PR #1779; it does not grant gameplay integration, release, schema-3 verification or independent review.

## Independent artifact retrieval, integrity and execution provenance

- GitHub Actions [run #39371679794](https://github.com/vokerg/everfield/actions/runs/39371679794), artifact `godot-rendered-960x540-39371679794-1`, ID `12241576733`, downloadable at the time of this continuation. An actual artifact ZIP was retrieved and its SHA-256 independently calculated: `821dff65f9d076e88b88fb174eba637de30eb5cdfc0bbcb5175e2afd8cdc5851`, matching GitHub artifact digest. Seven PNGs, `run-identity.txt`, `render.log` and `png-sha256.txt` were present. For the seven PNGs, independent SHA-256 calculations matched all seven archived manifest hashes.
- `run-identity.txt` records checkout **PR #1838 exact source head** `12abd85a6a62aef6823b6327a69c44fb4faee987`, run ID `39371679794`, Godot `4.7.1.stable.official.a13da4feb`, engine ZIP SHA-256 `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`, and Xvfb/software OpenGL. Source PR #1838 is now squash-integrated into main at `1cf7f67d290bb01c42705610a49647c0a67199bc`; distinct branch-vs-squash commit SHAs are not conflated. Hosted capture job concluded SUCCESS. `render.log` prints `EVERFIELD_RENDERED_VIEWPORT_CAPTURE_PASS screenshots=7 width=960 height=540`; source `game/tests/viewport_capture.gd` main blob `cdfd4b4d7a05b8dc889f6946b7adce903ae76d68` was separately inspected.
- Each PNG was opened for visual inspection and verified as an actual nonempty, nonuniform **960×540 RGBA** image. This is real framebuffer evidence, not a simulated UI drawing. The archived `png-sha256.txt` uses absolute paths from GitHub's runner; independent verification resolved each path by its archived basename, not by a misleading direct `sha256sum -c` invocation against unavailable runner paths.

| Authentic frame | Individually verified SHA-256 | Visual result / limit |
|---|---|---|
| `01-intro.png` | `261a9b94d193a1149d85f5c77399b9fbd4cbc4e18862119af8bccf3eb2773e87` | Title, narrative and empty history visible; default right panels occlude part of map station labels |
| `02-world-map-unobscured.png` | `602e162f2961fe9a2e39623efc2c1ed380168ce8c111ccdad5fd0d205805e738` | All five station markers/labels exposed when TAB map mode hides panels; key method is invoked directly, not physically typed |
| `03-controls-help.png` | `3c48cf2787cb577224dcd8e16569ea7a0dcd78e87566111ff9b3b413baa87716` | Help text and key legend visible; help visibility is assigned programmatically |
| `04-commons-hearing.png` | `7314304c5f1d9044bd1ec1530d8663c2be3b453c48920b4dc66cd83e8e8a0c2f` | Hearing speaker text, three choices, three-item public history; no physical interaction proof |
| `05-repair-consequence.png` | `733dba84bbf7a22de7053e6b381efe7211a55915f524eeb540de3993eb217f1f` | Repair pilot bounded outcome and five history entries visibly render |
| `06-public-nonconsent.png` | `40b4808d51d9be424bfe2ee4d80a6ced60d8f343e0bd7db31d096ff4d2dc5989` | Explicit hearing deferral text, commitment:none, unresolved mystery, four history entries; no claim of consent |
| `07-records-first-consequence.png` | `6b15a775d835b5b038ef8ce3ef16bbfd38dfd707dc87b255699385b76971bb7a` | Records-first filed outcome, commitment:records_first and seven history entries, mystery remains unresolved |

## Coverage classification and next execution gate

The seven frames independently establish real rendered states for an initial screen, optional unobscured map, controls help, hearing, repair, explicit deferral and records-first. They do **not** demonstrate all 13 approved public presentation scenarios / 41-page coverage; page first/middle/last and no-wrap; 10+ history events or C/V input scrolling; actual hardware/virtual OS-level movement and E/1/2/3/R/Z/X/C/V/H/TAB delivery; contrast/legibility under empirical accessibility methods; or end-to-end unrestricted playthrough. In the actual source, `game._unhandled_key_input(key)` is called directly for TAB, while `help.visible`, `game.interact_with`, `game.choose_commitment` and `game.reset_slice` drive the other frames. They exercise real game state but do not inject physical input.

**Confirmed remaining affordance concern:** default presentation/history panels obscure right-side station names, while optional TAB mode provides a real visually verified workaround. This is not by itself evidence of multiple disjoint gameplay defects. The current execution container has Xvfb but no pinned Godot binary and cannot resolve the binary host, so no new physical-input/13-scenario runtime was performed. The next action is the same-issue handoff for a separately authorized, read-only pinned-Godot interactive capture matrix or independently executed physical-input test, followed by evidence-backed defect/decision routing. Do not merge diagnostic PR #1779, claim complete playtest or spawn speculative roots.

---

# 2026-10-19 continuation — independently retrieved authentic pixels (PARTIAL EVIDENCE, NOT PLAYTEST PASS)

This is a later evidence addendum to the original 2026-10-15 no-renderer diagnostic retained below as historical provenance. **The earlier `BLOCKED_ENVIRONMENT_NO_RENDERER` observation is no longer current for hosted screenshots**: an actual GitHub Actions Xvfb/llvmpipe renderer now exists on integrated `main`. The remaining blocker is **incomplete scenario and physical-input coverage**, not an absent rendering mechanism. Issue #1763 is being resumed through its *existing HANDOFF*, not a STALE reset. Canonical program binding remains Issue #1147 comment #5675066392, blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`. Present inspected `main@fe1da5d33b3f64d03b81041ee39bd62b7f20bb7c`.

## Retrievable and locally checked primary evidence

- GitHub Actions [real viewport run #39202314071](https://github.com/vokerg/everfield/actions/runs/39202314071), `SUCCESS` in existing issue's evidence record; source checkout HEAD `d4f1843c8a30c4151fd2c92b92db0b159eaf62c6` (before exact scoped PR #1834 squash-published to `main@fe1da5d...`). GitHub artifact ID **12164257635**, name `godot-rendered-960x540-39202314071-1`, digest `sha256:b144492f1495d4e2dd2b7402284d6ae4408d2922b5155d9dd02bec37c5d3181e`, expires 2026-11-18 per artifact metadata.
- **Fresh independent retrieval in this continuation:** downloaded artifact ZIP; examined `run-identity.txt`, `render.log`, and all five actual PNGs; independently ran PNG file/size/hash verification and visually inspected all five. The run identity states **Godot `4.7.1.stable.official.a13da4feb`**, locked engine ZIP SHA-256 `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`, Xvfb/software OpenGL, actual framebuffer `960×540`. The log reports `EVERFIELD_RENDERED_VIEWPORT_CAPTURE_PASS screenshots=5 width=960 height=540`. Each file was confirmed `960×540` RGBA PNG independently of that authored sentinel.
- Per-image SHA-256:
  - `01-intro.png`: `261a9b94d193a1149d85f5c77399b9fbd4cbc4e18862119af8bccf3eb2773e87`
  - `02-world-map-unobscured.png`: `602e162f2961fe9a2e39623efc2c1ed380168ce8c111ccdad5fd0d205805e738`
  - `03-controls-help.png`: `3c48cf2787cb577224dcd8e16569ea7a0dcd78e87566111ff9b3b413baa87716`
  - `04-commons-hearing.png`: `7314304c5f1d9044bd1ec1530d8663c2be3b453c48920b4dc66cd83e8e8a0c2f`
  - `05-repair-consequence.png`: `733dba84bbf7a22de7053e6b381efe7211a55915f524eeb540de3993eb217f1f`

## Visually inspected result and exact limits

| Frame | Positive visual observation | Boundary / remaining gap |
|---|---|---|
| Intro / default UI | Title, status, objective, H hint, TAB hint, narrative page controls and empty history panel visible. | Default opaque right-side story/history panels cover portions of right-side station names/markers, exactly as previously reported from real pixels. This is not an all-stations-visible default overlay. |
| TAB world map | All five station markers and their full nearby name/purpose labels are visually exposed with right-side narrative/history panels hidden; objective and header remain displayed. The optional map-mode repair is real in this image. | Does **not** prove text remains accessible in default panel mode, full keyboard input delivery, or every route. |
| Controls help | Help content visibly renders, including movement, interaction, decision, reset and paging keys. | Capture code assigns `HelpPanel.visible = true` directly; **does not exercise a physical H key**. Help intentionally overlays part of the world, not proof of no overlay anywhere. |
| Commons Hearing | Visible hearing text, choices 1/2/3, page feedback and three-event public history with completed investigation. | Direct `game.interact_with()` helper calls, not physical E/1/2/3 input; no records-first/defer-choice screenshots or page-boundary audit. |
| Repair consequence | Visible completed bounded-pilot outcome, page feedback and five-event history. The unresolved mystery remains displayed as `UNKNOWN_BY_DESIGN`. | Direct `game.choose_commitment()` and `game.interact_with()` helpers, not real physical key input. No 10+ event scroll test or explicit nonconsent route screenshot. |

The exact source renderer `game/tests/viewport_capture.gd` makes direct `_unhandled_key_input(KEY_TAB)` method calls, assigns `HelpPanel.visible` explicitly, uses `game.interact_with` / `game.choose_commitment` directly, and captures a subset of successful states. **These are authentic rendered pixels from controlled game state, but not proof of actual physical keyboard events**. The remaining required matrix includes physical movement/E/1/2/3/R/Z/X/C/V/TAB/H, all 13 approved scenarios and 41-page envelope, first/middle/last paging, records-first, explicit commitment deferral/nonconsent, 10+ history events and no-wrap/reset behavior, long title/crop/scroll checks. No accessibility certification or complete visual PASS is claimed.

## Evidence-backed next route

Continue **this same #1763 HANDOFF** with an authorized extension of the existing read-only Xvfb capture/input harness to exercise missing states, then independently inspect and record the resulting exact SHA/hash-locked artifacts. Do not create speculative component issues from this partial capture; do not mutate production game source, merge diagnostic-only PR #1779, retroactively claim scenario/keyboard coverage, or close the evaluation. The earlier blocked report below is the original historical snapshot only.

---

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
