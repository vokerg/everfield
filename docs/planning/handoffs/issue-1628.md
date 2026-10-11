# Issue #1628 — bounded operational YAML scalar authority remediation

## Mission, current owner and immutable source
- Task: `FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-12`. First uncontested schema-3 CLAIM #6106714285 at GitHub-created `2026-10-11T07:33:06Z`, session `frontier-remediate-1628-gpt6-20261011-0933-01`.
- Main base `3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`, canonical Planning Program Issue #1147 binding #5675066392, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Hard prerequisite: distinct required negative review Issue #1623 terminal #6106678132; frozen reviewer-only draft PR #1625 HEAD `ca9aa3a4f12b5983ee223f9a547bae4daf27cec4`, immutable report blob `546d89ecef3fed5085b69a8d52c07ac22e078672`, one BLOCKER FSR-1623-B01, no MAJOR/minor.
- Frozen predecessor producer Issue #1621 terminal #6104020075, draft PR #1622 HEAD `18a23b61d4fafd68d0def4c8fe8cfcc34ac4139e`, v7 blob `5c5f26ea583b2d37792e31f38b5abab01d3afc2b`. Distinct from new owner; all predecessor branches/PRs are untouched.

## Scope and concrete correction
- Inherit **15** paths from exact PR #1622 with their identical Git blobs: maintenance workflow, v5/v6 scripts and twelve predecessor handoffs #1556 through #1621. Neither reformat nor re-author inherited content.
- Repair `tools/planning/frontier_maintenance.py` base `scalar()` by calling new `yaml_scalar_identity()`, a fail-closed single-layer scalar decoder for plain, YAML single-quoted (doubled quote) and JSON-compatible YAML double-quoted string scalars. Preserve quote characters that are *semantic data* instead of stripping arbitrarily many envelope layers. Unsupported ambiguous/escaped forms are rejected; no dependency added.
- Repair `tools/planning/frontier_maintenance_v7.py` `_integration_field()` to consume that same exact helper, preventing disagreement between base `parse_operational` and the integration provenance checker.
- Add composed v7 adversarial regression fixtures comparing layered single/double authority values for protocol, schema, kind, state, merge_method, canonicality, actor, role, source/review, PR and main identity, including operational record acceptance, against plain/single-quoted/double-quoted positives. Keep genuine scoped verifier-free sources and all previous negative YAML fixtures.
- Add this handoff only. Expected **18 total changed paths** versus unchanged main: 15 identical inherited blobs plus corrected v7, narrowly corrected base, this handoff. Original source and required review drafts remain frozen. No game/canon/root entry changes.

## Checks and next execution route
1. Open own `planning/issue-1628` draft producer PR to `main` after confirming exact final HEAD and the 18-path/blob allowlist. Required *new* final-head `pull_request` read-only Actions compile plus composed v1–v7 `--self-test` must PASS; mutation-capable `maintain` must be SKIPPED. This handoff does **not** predeclare CI successful.
2. Authenticate actual PR checkout merge-ref parents/tree, unchanged current main, all source frozen refs/blobs, current unexpired winning issue owner, and no unrelated regression. If CI fails, fix solely bounded code then rerun final-head CI; do not claim review readiness prematurely.
3. Only when all gates succeed, publish in-lease unedited schema-3 `STATUS(REVIEW_READY)` with exact PR HEAD, source/review evidence and the required route to a **new genuinely distinct independent adversarial review**. That reviewer is not the producer and has a separate review-only branch/PR. This owner must not self-review.
4. A clean required review still does **not** confer integration authority; separately authorized, independently owned exact-current-main-compatible **squash-only NONCANONICAL** source publication would be a distinct subsequent task. This remediation creates no game, canonical, verification, readiness, engine-selection, production or release authority.

## Evidence status
Root discrepancy independently reproduced with PyYAML 6.0.3 by required Issue #1623. Previous source CI `38100497282`, validation `114355266109` PASS / mutation job `114355266875` SKIPPED only applies to frozen predecessor and cannot certify this code. New final-head CI and distinct required independent review are outstanding until recorded with real GitHub evidence.
