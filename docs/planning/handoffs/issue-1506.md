# Handoff — Issue #1506 / IMPLEMENTATION-DEMAND-PLAYABLE-PRESENTATION-02

## Ownership and binding
- Winning schema-3 CLAIM: Issue #1506 comment `5978273922`, actor `frontier-drain-public-presentation-1506-gpt56sol-20261004-1053-b`.
- Branch `planning/issue-1506`, base `main@eef8a80d538a908ea685b206d97409ac48a2092f`.
- Canonical binding: Issue #1147 comment `5675066392`, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Routing authority #1503, owner parallel implementation directive #84 comment `5968764259`, prior implemented/frozen #1464 and clean review #1500. Original diagnostic #1462 remains CHANGES_NEEDED; successor #1481 is the only published diagnostic component.

## Implemented read-only scope
- `game/components/playable_presentation/playable_presentation.gd`: scene-independent public presentation API, injected published providers; exact route/outcome match guards.
- `game/components/playable_presentation/world_reader.gd`: intro and three known station text compositions, strict validation.
- `game/components/playable_presentation/hearing_reader.gd`: reviewed Maelin/Selka opening, repair, records-first, and explicit nonalignment/deferral.
- `game/components/playable_presentation/consequence_reader.gd`: five known selection/completion consequence events, route/phase guard.
- `game/components/playable_presentation/playable_presentation_smoke.gd`: isolated Godot 4.7.1 executable contract smoke; required sentinel `EVERFIELD_PLAYABLE_PRESENTATION_SMOKE_PASS`.
- This exact issue handoff. No edits to sibling station-world/traversal components, original published providers, live `game/main.gd` or scene/tests, Godot project/toolchain, or workflows.

## Verification gates
The isolated smoke covers exact public Old Works station assembly against the published source IDs, safe public/archive/trace/defer prose, Maelin/Selka opening, three hearing choices, five named outcomes, refusal to mismatch consequence and route, caller-array isolation, injected-provider immutability, absent provider methods and unknown inputs. It requires zero failing checks, exit 0 and the exact sentinel above. **No runtime PASS is claimed by this producer**, because a locked Godot 4.7.1 executable is unavailable in the current execution environment. Independent review must execute the exact final-head isolated smoke under repository-locked Godot 4.7.1, or route a blocking verifier. Generic playable CI is not a substitute. The source provider scripts and their contracts remain immutable/read-only.

## Fresh review and publication
A frozen **open draft PR** must match the schema-3 final terminal head. Create one separate fresh independent required implementation review/test of this exact packet. Reviewer must not mutate the source or review own work, and must check exact source blob identities, injected-provider contracts, privacy, explicit nonconsent, truth deferral, unknown input behavior and isolated executable evidence. A clean result requires all runtime and contract gates, not this handoff or generic CI. Any later component publication requires fresh current-main compatibility and independent clean review plus separately authorized squash-only merge; future shared controller fan-in is separately blocked on three independently published roots. No canon, historical truth, save/load, persistence, production/release, legal/provider, empirical accessibility authority follows.
