# Issue #1644 — independent root authority review handoff

## Mission, ownership, scope
- Mission: `FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-13-REV-01`.
- Reviewer episode: `frontier-independent-root-review-1644-gpt6-20261011-1133-01`, separate from Issue #1638 producer `frontier-remediate-root-1638-gpt6-20261011-1102-01`.
- First valid unedited CLAIM: Issue #1644 comment **6107638204** (GitHub server `2026-10-11T09:35:08Z`); immediate recheck found no competing claims.
- Branch: `planning/issue-1644`; base and compatible current main `3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`.
- Canonical Issue #1147 binding #5675066392; program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`; activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Exclusive review-only owned paths: `docs/planning/wave-2/reviews/factory-seeding-frontier-repair-1638-review.md` and this handoff. No source code, prior review, gameplay, shared CI or canonical files were changed.

## Frozen producer, review evidence, disposition
- Source Issue #1638 in-lease `STATUS(REVIEW_READY)` #6107450556; source draft PR #1640 exact `e6bbaddf1e17b23ad9344983c3159d4f30990bfd`, unchanged base main; 19 source paths with 17 inherited exact predecessor blobs, base parser `165eb8301715947be70f67474428cc2a7bdb3e7f`, v7 pinned `28af0a1eeeddcc318b1faeca76c82dfd1efbed87`.
- Producer final exact-head Actions #38127342597 PASS, validate job #114434343946 SUCCESS, mutation-capable job #114434344834 SKIPPED. Merge ref `1dd089ecbb0d774c570db69a2ac9c1c43f34e85e` parents current main and exact frozen source, tree `40a1b7cbfe1d0afac4bdb62120ceb19d3b1fcbbd`.
- Prior distinct blocker #1632/#6107357316 has a frozen reviewer-only PR #1636, HEAD `89990216c77fdec51163cb839a00b89c9336c36b`; frozen parent source #1628 PR #1631 HEAD `27d452fe5ae03dd822e8fc357d6b72cc48913698`.
- **Independent verdict CHANGES_NEEDED: 1 BLOCKER (FSR-1644-B01), 0 other MAJOR, 0 correction-requiring MINOR.** Exact report: `docs/planning/wave-2/reviews/factory-seeding-frontier-repair-1638-review.md`.
- Found real nested authority regression: `base.list_scalar` accepts `extensions.evidence_refs` as root evidence to renew a six-hour schema-3 EVIDENCE PROGRESS lease; the same reader supplies `artifact_paths` to v7 source/review/verifier PR-path checks. PyYAML 6.0.3 semantic root-vs-nested negative independently reproduced against faithfully extracted source reader. Root-only scalar parser fixes prior fake CLAIM/DONE issue but not these list fields.
- Real legacy #1583 source publication independently verified one-parent squash `ef75cc78a217695097f5d8f6cfb48ea04beaa7de`, with source/verifier/reviewer/integrator separate and NONCANONICAL; does not cure this new blocker.

## Terminal and next route
- Keep review source PR #1640 frozen DRAFT and all predecessor/reviewer-only PRs unmerged. Publish new **review-only DRAFT PR** for this branch, verify exact two changed paths/head/blobs; only then submit an unedited in-lease schema-3 `REVIEW_STATUS(CHANGES_NEEDED)` to Issue #1644 with the source exact head, report/handoff hashes and new review-only PR number. Issue can then reconcile to closed storage state.
- Required-next-route: `MATERIALIZE_FRESH_BOUNDED_BLOCKING_REMEDIATION_OF_FSR_1644_B01_ROOT_LIST_AUTHORITY_THEN_EXACT_FINAL_HEAD_READ_ONLY_CI_AND_NEW_DISTINCT_REQUIRED_REVIEW`. Materialize **one** fresh bounded remediation issue for the base-root list-reader trust boundary; preserve inherited predecessor bytes and avoid optional issue creation.
- No integration authority, canonicality, engine selection, gameplay truth/consent, implementation readiness, accessibility, production or release authority. Separate owner-authorized **squash-only NONCANONICAL** source integration only after a later exact-head, genuinely distinct clean required review.
- Evidence limitations: local source module and full composed suite could not be cloned/executed in this episode. Producer hosted CI result independently read via GitHub; negative semantic fixture and exact reader algorithm were locally executed. Report distinguishes these explicitly.
