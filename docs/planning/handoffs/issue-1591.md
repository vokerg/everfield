# Issue #1591 — verifier authority and alias-placement remediation

## Authority and recovery

Mission `FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-04`. Canonical binding remains Issue #1147 terminal `5675066392`, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`. Work began from `main@3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`.

Original CLAIM `6034561811` was created at GitHub server time `2026-10-07T08:58:53Z` and expired without renewal at `2026-10-07T14:58:53Z`. First valid STALE intent `6053478556` was published at `2026-10-08T06:03:02Z`; RECOVER grant `6053482782` followed at `2026-10-08T06:03:21Z` against the unchanged task branch. Recovery actor is `frontier-recover-verifieralias-1591-gpt56sol-20261008-0800-01`.

## Frozen predecessors

Required negative review #1589 terminal `6034490683` remains unedited, review-only draft PR #1590 remains frozen at `61ce4a77c29b89c519e9653e7c2ba23876e6ebe0`, and source #1585 draft PR #1586 remains frozen/unmerged at `d7679724712af7e97f2928d7f0075036338c18d9`.

Exact inherited predecessor blobs:
- `.github/workflows/planning-frontier-maintenance.yml` — `999671d1ede00a25c66bd63d25bcdc14e4a9d40b`
- `tools/planning/frontier_maintenance_v5.py` — `babdd29389e06bc922d33bc285c82315fec8c237`
- `tools/planning/frontier_maintenance_v6.py` — `da8d3f40e8bded8ad2b6369c9c67c6dedf8c4e03`
- `docs/planning/handoffs/issue-1556.md` — `ea2fce80a21d932a0f8f41d261abd85aa814775a`
- `docs/planning/handoffs/issue-1570.md` — `98744c4c302a4abca7e67d36301acf6ee16b5e6d`
- `docs/planning/handoffs/issue-1579.md` — `06b2ab2ff4d3a09778de4809f77edd6d5f47684a`
- `docs/planning/handoffs/issue-1585.md` — `53422ac29b568f42edc16d30488be744c5f273c2`

Only `tools/planning/frontier_maintenance_v7.py` changes substantively. Final code blob before this documentation-only handoff update is `cfd19d5f8f02d48239660a3f94a01cba35e10c5c`.

## Findings remediated

`FSR-1589-B01`: whenever the immutable source route or integration provenance declares verification, v7 now requires a distinct trusted closed verifier issue and validates its exact unedited `VERIFICATION_STATUS(DONE)`, schema-3 VERIFIER ownership generation/lease, source terminal/PR/head binding, PASS disposition and zero blocker/major/corrective-minor counts, actor independence from producer/reviewer/integrator, immutable verifier PR/head, verifier-only evidence paths, and source-verifier aliases. Missing, dangling, edited, wrong-source, wrong-terminal, wrong-actor, wrong-PR/head or non-PASS verifier provenance fails closed.

`FSR-1589-M01`: recognized source/review/verifier provenance aliases are valid only as direct children of the top-level `extensions:` map. Same-name aliases at top level, beneath another pre-extension map, nested below extensions, duplicated, null or conflicting are rejected. Extension-only regression capsules remain accepted to preserve existing offline fixtures.

Self-tests add a required-verifier causal positive path, omission/tampering/substitution negatives, producer/reviewer/verifier actor-collision negatives, verifier PR/head/source corruption, cross-section alias placement ambiguity, and literal current #1583/#1575 vocabulary while retaining all prior v1-v7 regressions.

## Validation evidence

Draft PR #1593 remains producer-only and unmerged. At code HEAD `09ff2fbebecb12eef51f467a03248db9d9535a65`, pull-request workflow run `37736960028` succeeded. Read-only job `113178582954` passed Python compile plus composed v1-v7 self-tests; the log includes `frontier v7 source/review causal authority and STALE recovery fixtures: PASS` and `frontier maintenance v7 self-test: PASS`. Mutation-capable job `113178584308` was SKIPPED. The workflow checked proposed merge ref `1a55145b6358d95a0090e25213fbb9baeb206ca5`, explicitly `Merge 09ff2fb... into 3d7ce70...`.

This handoff update is documentation-only. Its resulting PR HEAD still requires one final exact-HEAD pull-request run with read-only validation PASS and mutation job SKIPPED before terminal producer status.

## Authority boundary and next route

No self-review or source integration is authorized. After final exact-head CI and compatibility recheck, publish recovered-owner `STATUS(REVIEW_READY)` for #1591 and route a **new distinct required adversarial review** of this exact corrected candidate. Source #1585/#1586 and negative review #1589/#1590 remain immutable. No canonical, gameplay/truth/consent/persistence/accessibility/readiness/production/release authority is granted.
