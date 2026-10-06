# Issue #1556 — bounded factory seeding remediation

- Branch: `planning/issue-1556`; starting main `781d65ca07c7b410faaecfa1e8cbfd6f5fc8ed48`.
- Current canonical: #1147 comment `5675066392`, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Owner winning claim: #1556 comment `5999767236`; actor `factory-seeding-repair-1556-gpt56sol-20261005-01`.
- Scope: maintenance v5/v6/v7, maintenance workflow and this handoff only; no code in `game/`, canon or any other agent-owned surface.

## Root causes corrected

1. The explicit-successor grammar in v5 accepted only a single successor. Terminal #1542 declared exact producer #1543, #1544 and fan-in #1545; terminal #1543 declared verifier #1547 and distinct review #1548. Both generations were already represented, yet automation created redundant wrappers #1554/#1553. Now an exact multi-target route is consumed only after all successor issues exist and are trusted/eligible. Unknown/partial/untrusted/rejected/wrapper successors fail closed, without weakening single-route behavior.
2. The v6 content liveness detector ignored the `IMPLEMENTATION_INCREMENT /...` task class in active implementation fan-in #1545, even though no content issue remained open. The new rule recognizes current bounded incremental demand, excludes review/integration provenance tasks, preserves causal attribution and deduplication, and requires the downstream compiler to produce a bounded no-op if no concrete content need exists (never auto CONT-08).
3. The v7 implementation liveness rule globally vetoed new demand whenever any implementation issue was open, including BLOCKED tasks in unrelated dependency chains. It now considers **only the newest integrated source**, and only when no factory/owner intake has consumed that exact source. Older integrated history cannot be replayed when latest source already has an intake. The post-playable owner intake #1542 citing exact integrated publication #1539 is consumed. Separately authorized `-INT-` fan-ins may be recognized only with a source's actual squash `INTEGRATION_STATUS(DONE)` and current-main ancestry.
4. The maintenance workflow adds a read-only offline PR validation job (py_compile and composed self-tests through v7) and explicitly prevents mutation-capable reconciliation on `pull_request`.

## Required checks / independent gates

Run `python3 -m py_compile tools/planning/frontier_maintenance*.py` and `python3 tools/planning/frontier_maintenance_v7.py --self-test` on the **final PR HEAD**, including regression tests for both real multi-target routes, partial/rejected/untrusted successors, exact content intake from blocked bounded incremental demand, one-per-source consumption, and no old implementation backfill. Examine CI logs before terminal.

Review must be fresh and **independent** of this producer: inspect exact five-path diff, current main compatibility, potential false-positive successor-parse matches, source-class exclusions, malformed ownership cases, zero speculative historical backfill, denied PR mutations, and retained test output. Route changes needed to separate remediation and revalidation. A green self-test alone is not a clean required review.

Only a separately authorized review-clean and exact-current-main-compatible **squash-only** integration may publish this fix. This work does not grant gameplay/canon/truth/accessibility/readiness/production/release, independent review or merge authority.
