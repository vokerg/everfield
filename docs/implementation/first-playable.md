# Everfield bounded first playable — Accounts at the Old Works

This tranche is the first executable Godot implementation authorized by repaired readiness verifier #1367. It implements only the bounded `VS:OLD-WORKS-ACCOUNTS-01` slice from the clean-reviewed noncanonical content packet on `main`; it does not make that content canonical.

## Run

Use the selected engine, Godot `4.7.1-stable`:

```bash
GODOT_BIN=/path/to/Godot_v4.7.1-stable_linux.x86_64 \
  tools/implementation/run_godot_smoke.sh
```

For interactive play:

```bash
/path/to/Godot_v4.7.1-stable_linux.x86_64 --path game
```

Controls: **WASD / arrows** move, **E** interacts, **1/2/3** select a hearing commitment when prompted, and **R** resets the slice.

## Implemented loop

The player moves through one concrete Old Works scene and can:

1. inspect the required public record;
2. either inspect an independent material trace **or explicitly defer a truth conclusion**;
3. open the Commons Hearing only after that investigation predicate is satisfied;
4. choose a bounded **repair pilot**, **records-first**, or **defer commitment** route;
5. complete either committed route at the project table.

The loop deliberately preserves `MYS:FRAGMENTATION-CAUSE` as `UNKNOWN_BY_DESIGN`. A claim, evidence interaction, branch choice, or completion cannot promote the world mystery to truth. The private Anwen secret is not required or implemented in this bootstrap, matching the reviewed slice's solvability-without-secret constraint.

## Failure diagnostics

Guard failures are visible in both the HUD and stderr with stable `EF-*` codes, including investigation, negotiation, commitment, interaction-range, and unknown-surface failures. The smoke script intentionally exercises fail-closed guards and exits nonzero on any invariant break.

## Smoke coverage

`game/smoke_test.gd` runs headlessly and verifies:

- the main scene and controllable player exist;
- negotiation is blocked before investigation;
- public-record + material-trace + repair-pilot completes;
- public-record + explicit-defer + records-first completes without fabricating material-trace evidence;
- both paths keep the world mystery unresolved;
- commitment is blocked before negotiation;
- unknown interaction surfaces fail visibly.

The CI workflow downloads the exact Godot artifact from the already-reviewed repository lock at `docs/planning/wave-2/evidence/ci/engine-toolchain-artifact-lock.json`, verifies the retained SHA-256, imports the project, runs the smoke driver, and uploads run identity/log/hash evidence. It does not create production/provider/release authority.

## Scope intentionally deferred

This bootstrap contains no production save/load system because the bounded interaction loop does not require persistence to run or review. It also defers empirical accessibility clearance, broad platform/shipping support, production hardening, release packaging, commercial/provider authority, legal/certification authority, final canon, and unrelated systems. Those remain governed by their existing fail-closed routes.
