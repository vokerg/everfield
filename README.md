# Everfield

Everfield is an AI-native narrative game project with a **bounded playable Godot 4.7.1 slice** on `main`: *Accounts at the Old Works*. The original PLAN-THE-PLAN/bootstrap phases are historical provenance, **not the current game implementation status**. The canonical Planning Program v1 and active owner directives continue to govern agent ownership, review, validation, and squash integration.

## Play and verify the current slice

The game is in [`game/`](game/), with the scene entry point `game/main.tscn`. Use Godot **4.7.1-stable**, not legacy Unity or Unreal workflows.

```bash
# Interactive first playable (Godot 4.7.1-stable on PATH)
godot --path game

# Reviewed-engine smoke (set GODOT_BIN to the Godot 4.7.1 executable)
GODOT_BIN=/path/to/Godot_4.7.1-stable tools/implementation/run_godot_smoke.sh
GODOT_BIN=/path/to/Godot_4.7.1-stable tools/implementation/run_godot_movement_smoke.sh
```

Controls: WASD/arrows to move, E interact, 1/2/3 choose or defer when prompted, R reset, Z/X page approved public text, C/V page public history, H toggle controls help. See [first-playable implementation notes](docs/implementation/first-playable.md) for source boundaries and tests.

## Agents: read the current repository, not historical bootstrap assumptions

1. Start from **current `main`** and read [`AGENTS.md`](AGENTS.md), [`docs/planning/START-HERE.md`](docs/planning/START-HERE.md), and the bound canonical [Planning Program v1](docs/planning/PLANNING-PROGRAM-v1.md). Reconstruct current authority from repository and GitHub state; do not infer it from this README.
2. Follow the current **2026-10-17 and 2026-10-18 owner emergency convergence directives** in `AGENTS.md`. Historical `[PLAN-BOOTSTRAP]` issues #2-#6 are provenance; they are not today's task dispatcher.
3. Prioritize **resuming and finishing eligible existing dependency chains**, verified bounded gameplay and content work, and real integration over creating new review/remediation issue or PR chains. Do not take active/owned work or merge review-only drafts.
4. Every accepted `main` integration must be an exact-head **squash merge** after appropriate review and hosted checks. A green CI job, an open draft PR, or a chat instruction alone is not a verification or independent review terminal.
5. The guarded Copilot worker [`.github/workflows/everfield-frontier-worker.yml`](.github/workflows/everfield-frontier-worker.yml) accepts deliberate **owner-only** `/everfield worker run` comments on eligible unclaimed implementation issues and trusted-main manual dispatch. It is **not** a scheduled frontier worker; its model job has no GitHub write token, while a separate bounded patch publisher may write a draft branch.
6. **Known external blocker:** GitHub Actions currently rejects PR creation by `GITHUB_TOKEN` with `GitHub Actions is not permitted to create or approve pull requests`. Owner can enable **Settings → Actions → General → Workflow permissions → Allow GitHub Actions to create and approve pull requests**. Until then, recover the exact already-pushed branch into one draft PR using the owner GitHub connection, review and verify it, and never rerun paid inference just to retry PR creation.
7. Keep unattended frontier maintenance and negative-review PR retirement **paused** under the owner directive. Do not interpret successful manual runs or PR-count reductions as permission to restart them.

### Verified recovery evidence (18 October 2026)

- Guarded Copilot authoring + trusted patch validation/push: [Actions #39155779036](https://github.com/vokerg/everfield/actions/runs/39155779036), game controls help [PR #1823](https://github.com/vokerg/everfield/pull/1823), exact-head Godot [run #39156052333](https://github.com/vokerg/everfield/actions/runs/39156052333).
- Separate guarded authoring + **automatically dispatched** read-only Godot smoke: [Actions #39156575257](https://github.com/vokerg/everfield/actions/runs/39156575257), source [PR #1826](https://github.com/vokerg/everfield/pull/1826), final exact-head PASS [run #39157255314](https://github.com/vokerg/everfield/actions/runs/39157255314).
- Both reviewed game increments were owner-authorized, squash-merged into `main`. This demonstrates bounded execution and recovery, **not** autonomous GitHub Actions PR creation, independent schema-3 certification, release approval, or continuously running agents.

Repository + GitHub state is the durable project memory; prior conversation history is not required.
