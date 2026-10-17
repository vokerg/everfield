# Issue #1809 — distinct mandatory Copilot Actions security review handoff

## Immutable review scope and ownership

- Mission: `FACTORY-ACTIONS-COPILOT-EXECUTOR-BOOTSTRAP-01-REV-01`. Reviewer execution `everfield-distinct-copilot-actions-security-1809-gpt6-20261017-01`, first sole valid schema3 `CLAIM` #6232359434 at GitHub `2026-10-17T09:35:57Z`, distinct from source actor `frontier-executor-capability-probe-1806-gpt6-20261017-01`. Own branch `planning/issue-1809` based on main `7da4c2d50412fe134c8632264908560b8b7995ce`.
- Active canonical planning binding Issue #1147 comment #5675066392; exact canonical Planning Program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation `87c85cecfa9a2ffa464c4b36816a138bf41441af` main ancestor.
- Producer Issue #1806 first CLAIM #6232301797, immutable in-lease terminal `STATUS(REVIEW_READY)` #6232347936. Existing OPEN/DRAFT PR #1808 exact head `cecb683a10beb082a2721fdf04cfd69fdfb092df` and main base above. Precisely two added files: `.github/workflows/everfield-frontier-copilot-probe.yml` blob `d9f228afa301dfabe075d888b9f700918d94dcea`, `docs/planning/handoffs/issue-1806.md` blob `b7c9b14b62adea299d07f27ec92b2c99fecc92b0`.
- Original raw hosted job logs from **exact-head** Actions run #39021587655 / job #117364316709: both SUCCESS, permission `CopilotRequests: write`, genuine npm-install of Copilot CLI, real inference output `EVERFIELD_COPILOT_ACTIONS_PROBE_OK`. Successful model reachability established; never a complete autonomous write-capable executor.

## Review disposition and risk

**`REVIEW_STATUS(CHANGES_NEEDED)`: 0 BLOCKER / 2 MAJOR (FCE-1809-M01, FCE-1809-M02) / 1 correction-requiring MINOR (FCE-1809-m01)**.

1. **FCE-1809-M01 (MAJOR):** unversioned `npm install --global @github/copilot` in workflow executable path immediately precedes token-bearing call with `GITHUB_TOKEN` / `copilot-requests:write`. No immutable npm package and transitive code integrity; future run differs despite reviewed source.
2. **FCE-1809-M02 (MAJOR):** `pull_request` on changes to self-referential workflow runs PR-selected workflow code with `copilot-requests:write`; the `same-repo` condition rejects forks but not unreviewed same-repo collaborator changes. Run #39021587655 proves the newly added workflow ran despite not existing on main. Privileged billing and token available to unmerged branch's modifiable instructions. Require privileged model call on reviewed immutable main/owner-approved manual route only; safe PR static validation separately without Copilot permission.
3. **FCE-1809-m01 (MINOR correction):** `grep -Fxq` checks whether *any* line equals sentinel, whereas acceptance contract demands exact one-line response. A real Bash `printf 'unexpected extra line\nEVERFIELD_COPILOT_ACTIONS_PROBE_OK\n' | grep -Fxq ...` returned success; compare entire output string instead. Actual final hosted log displayed exactly the sentinel once.

Reviewer's executed work: exact GitHub source files and two-path diff, winning-owner claim/terminal, read-only GitHub Actions full job logs and step conclusions, Node/npm dependency trust static audit, official current GitHub workflow security references, Bash negative-control run. No malicious PR payload, token exfiltration, billed model replay or deployment executed; privileged PR finding is derived from documented GitHub semantics and exact hosted observable run.

## Next mandatory route and non-authority

One mandatory bounded **existing-source** correction of frozen PR #1808 for all three findings, preserving both source blobs and source/review PR history untouched. Fix trust boundary first: no billable `copilot-requests:write` on unreviewed PR-selected workflow, immutable verified version/integrity dependency, strict single-line sentinel; bound spend and owner dispatch. Require trusted-ref model verification where feasible and honest no-inference limitation otherwise, safe exact-head static CI and **new genuinely different full-module security review** of the corrected workflow. No optional reviews, no premature write-capable dispatcher or route registration.

This reviewer creates **exactly two** new docs (`docs/planning/wave-2/reviews/factory-actions-copilot-executor-1806-review.md`, `docs/planning/handoffs/issue-1809.md`) in its own **OPEN/DRAFT reviewer-only PR**, permanently **NONINTEGRABLE** and never merged. Terminal review comment must bind exact PR head and these two blob SHAs after publication. Keep source PR #1808 OPEN/DRAFT. Never merge this reviewer PR, never integrate source based on authored success, and never grant canonical, gameplay, engine, readiness, release, production, or independent AI-dispatch authority.

Any eventual source integration needs separately valid owner authorization of currently verified head on then-current main and must be **SQUASH ONLY**, noncanonical.
