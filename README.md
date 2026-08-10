# Everfield

Everfield is currently in the **PLAN-THE-PLAN** bootstrap phase. Gameplay implementation is not authorized yet.

## AI Agent Entry Point

If you are a fresh agent with no prior conversation context:

1. Start from the current `main` branch.
2. If `/AGENTS.md` and `docs/planning/START-HERE.md` exist on `main`, read them in that order and follow them exactly.
3. Inspect open GitHub issues whose titles begin with `[PLAN-BOOTSTRAP]` and select only work whose stated hard prerequisites are satisfied. Prefer resumable in-progress work over starting competing work.
4. If `/AGENTS.md` is not yet present on `main`, seed PR #1 has not been integrated yet. In that state, do not claim Issue #2 or invent substitute planning work; inspect PR #1 only as the pending seed corpus.
5. Once seed PR #1 is integrated, Issue #2 is the first executable bootstrap planning task unless repository/GitHub state explicitly records otherwise.
6. Do not start game implementation, make a final engine choice, or generate a mass implementation backlog unless a later canonical planning protocol explicitly authorizes it.

All accepted changes integrated into `main` use **squash merge**. Task branches may contain iterative/WIP commits, but normal merge-commit and rebase-merge integration into `main` are prohibited by the project operating directive.

Repository + GitHub state is the project memory. Prior chat history must not be required.
