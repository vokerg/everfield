# Issue #1617 — mandatory bounded remediation handoff

## Ownership, source and authority

- Task `FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-10`, first winning schema-3 CLAIM **#6101749398**, server time **2026-10-10T20:15:57Z**, reviewer-independent producer `frontier-remediate-1617-gpt6-20261011-0015-01`.
- Own branch `planning/issue-1617` created from `main@3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`, canonical #1147/#5675066392, program `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`. GitHub-created six-hour lease and canonical first-winner checks remain mandatory.
- Hard predecessor: independent required negative reviewer Issue #1615 terminal #6101708763, PR #1616 exact frozen HEAD `ee8ff112f0c5a7191258c4cccc618593e92b638f`, report blob `80a8993fb08c3c74a1d32109269ccdee70e6f8c4`. Source producer #1613 terminal #6101067517, draft PR #1614 unchanged HEAD `faca0341a1d73702bc384f501712a105a97c2f50`, prior v7 `c35f895a0121ce329bda6f7220378c9f43e11335`. Both remain frozen/unmerged.

## Bounded changes and evidence

- Preserve byte-identical original source PR #1614 workflow, v5/v6, and all 10 inherited handoffs (#1556/#1570/#1579/#1585/#1591/#1596/#1600/#1604/#1608/#1613); total 13 source artifacts pinned. Amend **only** `tools/planning/frontier_maintenance_v7.py` from the final #1613 source, plus create this own handoff. Result should contain **15** paths relative to unchanged `main`.
- **FSR-1615-B01 BLOCKER:** reject unsafe YAML anchor/alias node names of *any* first character, including digit names `&7` / `*7`, before trusting aliases or conditional verifier marker. Regression covers real numeric-key duplicate source/review identities and numeric-key hidden verifier; maintain accepted scoped sources with no verifier and ordinary quoted scalar notes.
- **FSR-1615-M01 MAJOR:** `_integration_field` now checks all structurally meaningful capsule lines, rejects unsafe node and escaped mapping keys, and requires one semantically unique unquoted root authority key (including across the extensions section). Exact top-level quoted/escaped duplicate `canonicality` fixtures are rejected; ordinary single root keys remain accepted.
- Corrected v7 immutable candidate blob **`9646a8ceca5dfeb56303d10d553e8137500549c3`**. The patch extends final #1613 source conservatively, does not mutate original code/PR, and preserves independent provenance/integrator/lease/squash checks and v5/v6 multi-demand/no-global-veto behavior.
- Independently reproduced reviewer counterexamples with PyYAML 6.0.3 and source-accurate regular-expression behavior before remediation. Added source-owned regression checks for both failed classes and positive scoped controls. This is *producer* evidence; it is NOT an independent approval.

## Required final-head, review and integration gates

1. Ensure branch PR changes exactly 15 authorized paths, the original 13 inherited blobs are SHA-identical to PR #1614 and current `main` is compatible. A draft PR to `main` is mandatory before `STATUS(REVIEW_READY)`.
2. Run `python3 -m py_compile tools/planning/frontier_maintenance*.py` and `python3 tools/planning/frontier_maintenance_v7.py --self-test` on the **actual final PR merge checkout** using read-only `pull_request` Actions. Examine exact HEAD, job logs, merge-ref parents/tree and mutating job SKIPPED; if FAIL, revise source on own branch under valid owner and rerun exact final-head CI before terminal.
3. Before owner terminal, recheck active canonical binding, first-valid ownership/lease, actual source/review PR frozen identities and current-main compatibility. Terminal may declare `STATUS(REVIEW_READY)` only for exact draft PR final HEAD and documented passing read-only CI.
4. **Next required route:** materialize a new *genuinely distinct mandatory independent adversarial review* of this exact source PR. Negative -> another bounded remediation; independently clean -> separate eligible owner-authorized exact-current-main compatible **squash-only NONCANONICAL** integration task. No source/required-review self-merge, canonical, gameplay, truth/consent/accessibility, engine, readiness, production or release authority.

The durable terminal schema-3 issue comment (when eligible) carries the exact final PR/CI IDs, owner lease and outcome. Nothing in this handoff asserts CI or review approval before the actual checks.
