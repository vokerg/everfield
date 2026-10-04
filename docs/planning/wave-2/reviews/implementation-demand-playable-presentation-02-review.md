# #1515 — Required independent review: public presentation assembler

Disposition: **CHANGES_NEEDED** (0 BLOCKER, 1 MAJOR, 1 correction-requiring MINOR).

Reviewer session: `independent-public-presentation-review-1515-gpt56sol-20261004-1244-01`; distinct from Producer #1506 and Verifier #1514.

## Frozen review and evidence

- Canonical binding: Issue #1147 comment `5675066392`, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation `87c85cecfa9a2ffa464c4b36816a138bf41441af`. Current review base `main@1adb71b8c76f3cd23c821370486915a0f1bae2c9`.
- Producer #1506 terminal `5978324440`, draft PR #1513 frozen at `37833b1e482adaa2f123edeed02b81e24a2f3688`; exactly the five GDScript modules/smoke under `game/components/playable_presentation/` and `docs/planning/handoffs/issue-1506.md`, six changed files in total.
- Exact independent verifier #1514 terminal `5978373146`, `PASS_EXACT_PUBLIC_PLAYABLE_PRESENTATION_RUNTIME_SMOKE`: draft PR #1519 final head `4ed70192922a47781a9371e7865893a24e9a0fcc`; Actions run `37191047245`/job `111403101880` success, locked Godot `4.7.1.stable.official.a13da4feb`, exact sentinel `EVERFIELD_PLAYABLE_PRESENTATION_SMOKE_PASS`, 29 PASS, 0 FAIL, exit 0. Artifact `11299506223`, digest `sha256:a0648f7410a703cdd353ca32468a3546c9634a9bfa3351de8bda14e4f82c9964`. Verifier checked producer and published-provider blobs. No additional independent runtime run is claimed in this review.
- Reviewed exact frozen producer and the published `game/main.gd` controller plus Old Works, hearing and consequence providers on main. Normal intro, 3 public stations, Maelin/Selka opening, all 3 choices and 5 consequence events have matching text IDs and line order. Archive remains contested, material trace noncausal, truth/commitment deferral nonconsenting, and private provenance not presented. Outputs are read-only; no scene/input/session/history mutation, new facts or release authority.

## MAJOR-01: malformed hearing beats are not fully validated

In `hearing_reader.gd` route composition, the code verifies `route_scope`, nonempty text and that `speaker_ref` is *some* recognized participant. It does **not** check the speaker expected for each immutable beat ID or the beat phase (`ROUTE_POSITION` for repair/records versus `DEFER_NONALIGNMENT` for deferral). An injected provider with an otherwise valid contract can swap speakers or change the deferral phase while still producing `ok: true`. This breaches the required fail-closed behavior for malformed provider metadata and the exact reviewed speaker/nonalignment contract. The published provider uses valid values; the 29-PASS smoke never injects either mismatch.

Required: reject incorrect speaker/phase for each expected beat and add injected-provider negative regression tests for swapped speaker, wrong/missing phase and route scope; preserve exact published output.

## MINOR-01 (correction required): empty station ID returns an intro

`playable_presentation.gd:old_works_station("")` invokes `world_reader.gd:compose(world, "")`. Empty ID selects the intro branch and returns `ok: true` although only `public_record`, `material_trace` and `defer_conclusion` are valid station IDs. Existing smoke tests only unknown *nonempty* station IDs.

Required: reject the empty station ID at the station entry point and test it separately; preserve `world_intro()` and all valid station outputs.

## Decision and downstream gate

**CHANGES_NEEDED**: clean review and publication are prohibited despite the exact verifier PASS. A separately owned bounded remediation must correct these findings with regression smoke without editing frozen Producer #1506/Verifier #1514 branches or published gameplay/provider files. Re-run new independent exact-head locked-Godot verification and fresh required independent re-review before separately authorized **squash-only**, **noncanonical** component publication. This document grants no integration, decision, readiness, truth, persistence or release authority.
