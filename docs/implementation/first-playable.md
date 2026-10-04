# Everfield bounded first playable — Accounts at the Old Works

This tranche is the bounded executable Godot implementation authorized by repaired readiness verifier #1367, extended by presentation fan-in #1414, and structurally modularized under Issue #1464. It consumes only clean-reviewed, squash-published noncanonical component packets on `main`; using them in the playable does not make their content canonical. Component linkage in this branch remains review-gated and noncanonical until separately authorized squash publication.

## Run

Use the selected engine, Godot `4.7.1-stable`:

```bash
GODOT_BIN=/path/to/Godot_v4.7.1-stable_linux.x86_64 \
  tools/implementation/run_godot_smoke.sh

GODOT_BIN=/path/to/Godot_v4.7.1-stable_linux.x86_64 \
  tools/implementation/run_godot_movement_smoke.sh
```

For interactive play:

```bash
/path/to/Godot_v4.7.1-stable_linux.x86_64 --path game
```

Controls: **WASD / arrows** move, **E** interacts, **1/2/3** select a hearing commitment when prompted, and **R** resets the slice.

## Integrated reviewed presentation

The playable now consumes the published presentation components directly rather than relying only on debug-style hardcoded prose:

- **Old Works world/evidence**: Archive Ledger, Material Trace, and explicit cause-deferral surfaces come from `game/components/old_works_world/old_works_world_presentation.gd`.
- **Commons Hearing**: Maelin Sor and Selka Vey, their reviewed opening/route beats, and legal refusal/nonalignment framing come from `game/components/commons_hearing/commons_hearing_presentation.gd`.
- **Commitment consequences**: repair-pilot, records-first, and explicit public-deferral presentation comes from `game/components/commitment_consequences/commitment_consequence_presentation.gd`.
- **Movement/proximity verification**: the clean-remediated `game/tests/movement_interaction_smoke.gd` exercises the real scene, production `Input.is_key_pressed` path, world bounds, proximity interaction, and fail-closed unknown interactions.

The presentation layer is visibly rendered in the playable but remains inert: the components do not mutate game state or grant canonical, truth-resolution, representation, consent, or release authority.

## Modularized playable architecture (Issue #1464)

The live `game/main.gd` controller now delegates three contracts previously coded inline, without changing the bounded route choices:

- **Transient session state and ordered history** are owned by `game/components/session_state/session_state.gd` (published Producer #1461). Every state write uses the component's bounded `set_field` API; history uses `append_history`, and external `get_game_state()` results are deep-copy `snapshot()` values. The controller cannot mutate an independently returned snapshot to change live state.
- **Fail-closed observability** is owned by `game/components/diagnostics/diagnostic_catalog.gd` (current-main-corrected Producer #1481, required clean Re-review #1490). The controller supplies stable `EF-*` codes and, for dynamic errors, typed `station_id` or `choice` context. The catalog supplies the message and severity. Missing/unknown codes or malformed context remain errors, never successful diagnostics.
- **Objective/status presentation** is derived by `game/components/hud_objectives/hud_objective_model.gd` (Producer #1463, required clean Re-review #1496 and exact runtime verifier #1493) from immutable snapshots and optional station titles. The model decides phase, objective, status and fail-closed `INVALID_STATE`; the controller only displays its output, adds the original reset hint on completion, and retains the nearby interaction hint.

All three source/smoke components are already separately squash-published on `main`; this change does not edit their component bytes. No session serialization, durable state, scene authority, new narrative outcome or historical truth selection is introduced. Original diagnostic Producer #1462 and Review #1475 remain non-integrable, `CHANGES_NEEDED`; the corrected #1481/#1490 chain is the sole integrated diagnostic source.

## Implemented loop

The player moves through one concrete Old Works scene and can:

1. inspect the required public record;
2. either inspect an independent material trace **or explicitly leave the historical cause open**;
3. open the Commons Hearing only after that investigation predicate is satisfied;
4. see the reviewed Maelin/Selka hearing presentation and choose a bounded **repair pilot**, **records-first**, or **defer commitment** route;
5. after explicit commitment deferral, reopen the hearing without erasing history;
6. complete either committed route at the project table and see the reviewed consequence presentation.

The loop preserves `MYS:FRAGMENTATION-CAUSE` as `UNKNOWN_BY_DESIGN` on every route. Archive claims remain claims rather than findings; Material Trace remains non-discriminating; action, deferral, dialogue, commitment, and completion cannot select a historical causal winner. The private Anwen provenance-gap information is not exposed by the public-record presentation.

## Failure diagnostics

Guard failures remain visible in the diagnostic UI and error output with stable `EF-*` codes, including investigation, negotiation, commitment, interaction-range, and unknown-surface failures. Codes, 16 current-main-compatible message contracts and error classification are now resolved by the independently reviewed catalog rather than duplicated in the controller. The state-machine smoke intentionally exercises fail-closed guards and exits nonzero on invariant breaks.

## Automated coverage

`game/smoke_test.gd` runs headlessly and verifies:

- the main scene, controllable player, and visible presentation surface exist;
- negotiation is blocked before investigation;
- Archive Ledger and Material Trace display exact reviewed non-resolution text;
- Commons Hearing displays exact reviewed Maelin/Selka beats;
- repair-pilot consequence presentation remains bounded and non-truth-resolving;
- public commitment deferral is explicit nonconsent and can be followed by a fresh hearing choice;
- public-record + explicit truth-deferral + records-first completes without fabricating material-trace evidence;
- both committed paths keep the world mystery `UNKNOWN_BY_DESIGN`;
- commitment is blocked before negotiation;
- unknown interaction surfaces fail visibly;
- component instances are present, and session snapshots and nested history cannot be mutated by callers;
- invalid mystery/history writes, missing diagnostic context and malformed HUD model state fail closed;
- both corrected `EF-INVESTIGATE-*` diagnostics come from the exact current-main catalog;
- HUD phase transitions track record, corroboration-or-deferral, hearing, commitment, deferral/reopening and completion.

`game/tests/movement_interaction_smoke.gd` independently verifies real input-driven movement, minimum/maximum world clamps, proximity interaction, and fail-closed unknown interactions.

The primary PR CI workflow downloads exact hash-locked Godot 4.7.1, imports the candidate project, and runs five fail-fast isolated test suites: `res://smoke_test.gd` (integrated playable/presentation), `res://tests/movement_interaction_smoke.gd` (real input/proximity/clamps), `res://components/session_state/session_state_smoke.gd`, `res://components/diagnostics/diagnostic_catalog_smoke.gd`, and `res://components/hud_objectives/hud_objective_model_smoke.gd`. It requires each component's exact PASS sentinel, uploads suite logs and run/head identity, and hashes each published source/smoke payload plus the shared integration paths. A green workflow is executable evidence for independent review, not a substitute for clean review, a separate squash integration authorization, production/provider/release, or accessibility certification.

## Scope intentionally deferred

This increment still contains no production save/load system because the bounded interaction loop does not require persistence to run or review. It also defers empirical accessibility clearance, broad platform/shipping support, production hardening, release packaging, commercial/provider authority, legal/certification authority, final canon, truth resolution, and unrelated systems. Those remain governed by their existing fail-closed routes.
