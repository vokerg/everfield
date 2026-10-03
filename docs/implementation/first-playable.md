# Everfield bounded first playable — Accounts at the Old Works

This tranche is the bounded executable Godot implementation authorized by repaired readiness verifier #1367 and extended by fan-in #1414. It consumes only clean-reviewed, squash-published noncanonical component packets on `main`; integrating them into the playable does not make their content canonical.

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

Guard failures remain visible in both the HUD and stderr with stable `EF-*` codes, including investigation, negotiation, commitment, interaction-range, and unknown-surface failures. The state-machine smoke intentionally exercises fail-closed guards and exits nonzero on any invariant break.

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
- unknown interaction surfaces fail visibly.

`game/tests/movement_interaction_smoke.gd` independently verifies real input-driven movement, minimum/maximum world clamps, proximity interaction, and fail-closed unknown interactions.

The primary CI workflow downloads the exact Godot artifact from the reviewed repository lock, verifies its SHA-256, imports the project, runs **both** the state-machine and movement/proximity smokes, and uploads run identity, logs, and implementation hashes. This test evidence does not create production/provider/release or accessibility-certification authority.

## Scope intentionally deferred

This increment still contains no production save/load system because the bounded interaction loop does not require persistence to run or review. It also defers empirical accessibility clearance, broad platform/shipping support, production hardening, release packaging, commercial/provider authority, legal/certification authority, final canon, truth resolution, and unrelated systems. Those remain governed by their existing fail-closed routes.
