# Issue #1600 — Recovery handoff

**Mission:** `FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-06`  
**State:** IN_PROGRESS / recovered by STALE; **not REVIEW_READY**.  
**Canonical binding:** Issue #1147 terminal #5675066392; program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`; activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.  
**Base main:** `3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`.  
**Own branch:** `planning/issue-1600`.  
**Recovered ownership:** Original CLAIM #6085975637 (2026-10-09T17:32:41Z) expired at 2026-10-09T23:32:41Z, no owner renewal or terminal; winning STALE RESUME_INTENT #6093620686 and RECOVER #6093622351 by `frontier-recover-1600-gpt6-20261010-0608-01`, immediately rechecked.

## Scope and inherited provenance

Blocking remediation after required independent review #1598, REVIEW_STATUS(CHANGES_NEEDED) #6085913655, frozen negative reviewer PR #1599 HEAD `a32b0fe6e2d8f6a5a9c36bb1797689dc31951238`, and frozen producer #1596 PR #1597 HEAD `c46c32aa03eb261c5438a5f96b335aee8cc793cb`.

Fix FSR-1598-B01: reconstruct prefix-valid schema-3 terminal ownership, rejecting ended-generation reuse and losing contenders while preserving valid HANDOFF/RESUME and STALE continuation. Fix FSR-1598-M01: accept real directly scoped quoted/commented YAML `extensions` aliases while rejecting foreign/nested/sequence/flow/duplicate/null/conflicting aliases.

Preserve the pinned predecessor blobs in exactly nine existing paths (six inherited handoffs, workflow, v5 and v6). The v7 file `tools/planning/frontier_maintenance_v7.py` contains recovered work from previous partial attempt, initially blob `af7f04e9387e06c2f48daf5002566c678f9fd347`; its quality and tests have **not yet been independently verified**. This handoff is the eleventh path, `docs/planning/handoffs/issue-1600.md`. No game or other unrelated paths.

## Read-only acceptance to complete

1. Inspect exact own-branch and PR-to-main diff: exactly eleven paths with workflow `999671d1ede00a25c66bd63d25bcdc14e4a9d40b`, v5 `babdd29389e06bc922d33bc285c82315fec8c237`, v6 `da8d3f40e8bded8ad2b6369c9c67c6dedf8c4e03`; six inherited handoffs #1556 `ea2fce80a21d932a0f8f41d261abd85aa814775a`, #1570 `98744c4c302a4abca7e67d36301acf6ee16b5e6d`, #1579 `06b2ab2ff4d3a09778de4809f77edd6d5f47684a`, #1585 `53422ac29b568f42edc16d30488be744c5f273c2`, #1591 `3908f26b92cccd77b9ad65e2fab8ecc130062e51`, #1596 `b74e545b7f99b24ab8d0be391124f787666d8ff5`.
2. Run and independently inspect exact-final-HEAD `pull_request` GitHub Actions validation: compile `tools/planning/frontier_maintenance*.py` and run composed v1–v7 tests, including negative owner, malformed YAML, real #1545→#1575→#1577→#1583 causality fixtures. Require read-only PASS, mutation-capable `maintain` job SKIPPED, checkout merge ref tied to exact HEAD/current-main and no compatibility regression.
3. Create an open **draft** producer PR to main before any `STATUS(REVIEW_READY)`. A passed test alone is not independent review, integration, or canonical authority.
4. Only after independent read-only evidence and exact head checks, publish a valid current-owner `STATUS(REVIEW_READY)` with PR/head/base, evidence and required distinct mandatory adversarial review route; commission new independent review in a new issue. Separately owner-authorized squash-only NONCANONICAL integration may follow clean review and independent integration gates; never self-review or merge this producer on draft/CI authority.

## Operational cautions

Original branch had only v7 `af7f04e...` and inherited v5; omitted v6, workflow, handoffs due prior tool safety rejections. No prior final-head CI or source review for #1600 exists. All frozen PRs (#1597, #1599, and predecessors) must remain untouched. No gameplay, canon, truth, consent, accessibility, readiness, production, engine or release authority is granted. Verify current canonical binding, ownership generation, and main before each further action.
