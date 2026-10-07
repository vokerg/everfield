# Issue #1589 — required adversarial review handoff

## Frozen review authority

- Review issue: #1589, mission `FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-03-REV-01`.
- Winning reviewer CLAIM: `6034371821`, actor `frontier-review-realalias-1589-gpt56sol-20261007-1047-01`.
- Reviewer branch: `planning/issue-1589`, from `main@3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`.
- Canonical binding: #1147 comment `5675066392`, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Frozen producer: #1585 terminal `6034246625`, draft PR #1586, exact HEAD `d7679724712af7e97f2928d7f0075036338c18d9`.
- Frozen substantive v7 blob: `87433873ecf63865587bc47381b1c6c97668833b`.

Reviewer owns only this handoff and `docs/planning/wave-2/reviews/factory-seeding-frontier-repair-1585-review.md`. Source #1585 / PR #1586 and all predecessor branches remain immutable under this review.

## Independent evidence checked

Actual PR #1586 diff contains exactly the expected eight source paths. Current main differs from the source PR base by only the disjoint #1587 review-provenance squash and does not overlap those paths.

GitHub Actions run `37595095259`, job `112705675889`, checked out merge ref `d179ef35a7f62ee57d3cfd7fe636c523608f412f` = exact source HEAD `d767972...` merged into current `main@3d7ce70...`. Python compile and v1-v7 authored self-tests reported PASS. Mutation-capable job `112705677975` was SKIPPED.

The real source-publication authority chain was independently inspected:
- source #1545 recovered owner terminal `6008457546`, with first claim `5999915299`, winning STALE intent `6008439626`, RECOVER `6008441599`;
- source PR #1568 exact HEAD `1de1155429bfa657dd6e60c4f5abc969fabd86d5`;
- distinct required independent verifier #1575 terminal `6008823087`, verifier PR #1576;
- distinct clean required review #1577 terminal `6009157969`, review PR #1582;
- source integration #1583 terminal `6009230681`;
- exact one-parent source squash `ef75cc78a217695097f5d8f6cfb48ea04beaa7de` from `e51703de82b9df3f5e676663d3a04fdc678bd5c6`, publishing exactly the six source PR blobs.

## Required review result

**CHANGES_NEEDED: 1 BLOCKER, 1 MAJOR, 0 correction-requiring MINOR.**

### FSR-1589-B01 — BLOCKER

The repaired v7 authenticates source ownership, source PR/head, distinct clean review, review PR, and actual squash, but does not authenticate the required independent verification episode. It ignores #1583's `verification_status_comment_id` and verifier issue/terminal/PR/head/evidence fields. An otherwise valid integration can therefore omit or forge required verifier provenance and still become implementation-source authority. This bypasses a required verification gate.

Required remediation: causally bind a distinct trusted verifier issue and exact immutable PASS terminal to the same source issue/terminal/PR/head, authenticate verifier ownership/independence and verifier-only evidence surface, and fail closed for missing, edited, dangling, mismatched or non-PASS verifier evidence. Add real #1575/#1583 positive and adversarial negative verifier fixtures.

### FSR-1589-M01 — MAJOR

Alias conflict handling only scans aliases inside `extensions:`. A contradictory recognized source issue/PR alias can be placed at top level while a valid extension alias is accepted; that top-level provenance key is neither compared nor rejected. This violates the explicit foreign-top-level-or-extension fail-closed requirement.

Required remediation: enforce allowed placement for recognized provenance aliases and reject cross-section duplicates/conflicts/foreign placements. Add top-level-vs-extension conflict, duplicate, null and foreign-key fixtures.

Full evidence and analysis are in `docs/planning/wave-2/reviews/factory-seeding-frontier-repair-1585-review.md`.

## Required next route

Do **not** merge source PR #1586 or treat its green CI as clean review.

Route one bounded producer remediation for FSR-1589-B01 and FSR-1589-M01, preserving all accepted frozen v5/v6/workflow/predecessor handoff blobs unless the correction itself proves a necessary scoped change. The corrected exact final source HEAD must receive fresh read-only PR CI and then a **new distinct required adversarial review**. Only a clean terminal may be followed by separately authorized compatible-current-main, expected-head, squash-only **NONCANONICAL** source publication.

This review grants no integration, canonical, gameplay, truth, consent, persistence, accessibility, readiness, production, legal, shipping, or release authority.
