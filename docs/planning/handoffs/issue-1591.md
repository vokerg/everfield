# Issue #1591 — verifier authority and alias-placement remediation

## Authority and recovery

Mission `FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-04`. Current canonical binding remains Issue #1147 terminal `5675066392`, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`. Work is based on `main@3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`.

Original #1591 CLAIM `6034561811` was created at authoritative GitHub server time `2026-10-07T08:58:53Z` and expired without renewal at `2026-10-07T14:58:53Z`. First valid STALE intent `6053478556` was published at `2026-10-08T06:03:02Z`; first recovery grant `6053482782` followed at `2026-10-08T06:03:21Z` against unchanged branch/current-main head. Recovery actor: `frontier-recover-verifieralias-1591-gpt56sol-20261008-0800-01`.

## Frozen predecessor and required findings

Required negative review #1589 terminal `6034490683` remains unedited, with review-only draft PR #1590 frozen at `61ce4a77c29b89c519e9653e7c2ba23876e6ebe0`. Frozen source #1585 draft PR #1586 remains unmerged at `d7679724712af7e97f2928d7f0075036338c18d9`.

This remediation addresses only:
- `FSR-1589-B01`: authenticate the independently required verifier as causal source authority rather than trusting verifier-shaped references.
- `FSR-1589-M01`: reject recognized provenance aliases outside their permitted `extensions:` placement, including agreeing/conflicting/null/nested cross-section forms.

## Exact inherited source surface

The branch preserves these predecessor blobs byte-for-byte:
- `.github/workflows/planning-frontier-maintenance.yml` — `999671d1ede00a25c66bd63d25bcdc14e4a9d40b`
- `tools/planning/frontier_maintenance_v5.py` — `babdd29389e06bc922d33bc285c82315fec8c237`
- `tools/planning/frontier_maintenance_v6.py` — `da8d3f40e8bded8ad2b6369c9c67c6dedf8c4e03`
- `docs/planning/handoffs/issue-1556.md` — `ea2fce80a21d932a0f8f41d261abd85aa814775a`
- `docs/planning/handoffs/issue-1570.md` — `98744c4c302a4abca7e67d36301acf6ee16b5e6d`
- `docs/planning/handoffs/issue-1579.md` — `06b2ab2ff4d3a09778de4809f77edd6d5f47684a`
- `docs/planning/handoffs/issue-1585.md` — `53422ac29b568f42edc16d30488be744c5f273c2`

Only `tools/planning/frontier_maintenance_v7.py` changes substantively. Its candidate blob is `0846ae7f1f6d0df62051f65e89fc8890fbd6f3dc`.

## Correction implemented

The v7 causal-source gate now conditionally requires exact verifier authentication whenever the immutable producer route or integration provenance declares verification. It resolves a distinct trusted closed verifier issue, reconstructs a valid unexpired schema-3 VERIFIER owner terminal, binds exact source terminal/PR/head, requires PASS with zero blocking/correction findings, validates verifier actor independence, verifies an unmerged verifier-only PR/head and exact evidence paths, and rejects missing/edited/dangling/wrong-source/wrong-terminal/wrong-actor/wrong-PR/non-PASS verifier provenance.

Recognized source/review/verifier extension aliases now fail closed if the same key appears top-level, under another pre-extension map, nested within extensions, duplicated, null, or conflicting. Self-tests include required-verifier positive/negative causal fixtures, producer/reviewer substitution negatives, verifier terminal/PR/head corruption, cross-section alias ambiguity, and literal #1583/#1575 provenance vocabulary while retaining prior v5-v7 regressions.

## Remaining gates

Open an exact-head draft PR to `main`. Require final-head `pull_request` read-only Python compile plus composed v1-v7 self-tests PASS, mutation-capable maintenance job SKIPPED, exact merge-ref compatibility with then-current main, and no unexpected changed paths. Only then may the recovered owner publish producer `STATUS(REVIEW_READY)` and route a new distinct mandatory adversarial required review. This task has no source integration, canonicalization, gameplay/truth/consent/accessibility/readiness/production/release authority.
