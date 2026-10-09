# Issue #1598 — required independent negative review handoff

## Canonical authority, claim and frozen source
- Mission: `FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-05-REV-01`.
- Current main at claim and review: `3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`.
- Canonical binding #1147 `5675066392`; program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`; ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Own valid first-winner CLAIM comment `6085816104`, actor `frontier-required-review-1598-gpt6-20261009-2121-01`, created `2026-10-09T17:22:26Z`, branch `planning/issue-1598` from exact main. No competing claim on immediate ownership recheck. Independent from producer #1596 actor `frontier-remediate-1596-gpt6-20261009-1140-01`.
- Frozen producer #1596 terminal `6076787868`; evidence addendum `6076796827`; draft PR #1597 HEAD `c46c32aa03eb261c5438a5f96b335aee8cc793cb`, 10 allowed paths, v7 blob `97161ea4c2c9ce1173eea987f3f6568f914295ee`. Frozen predecessors #1593 HEAD `fa0c552bab1577f088dba271aeebe64f5150b1e0`, #1595 HEAD `6cc2a06914548e71fdaf3c4bf7af9d3d855c24be`. All remain unchanged and unmerged.

## Independently checked evidence
- Final-head producer workflow `37901191543` on PR merge ref `b5633023c4f7958a98b27a99393b078b01854954`; `validate-pr` job `113723900726` success with actual Python compile and v1–v7 self-tests PASS in retrieved logs, `maintain` job `113723902083` skipped.
- Examined actual corrected source v7 lines 140–1038, including provenance alias scanner, owner terminal prefix, stale recovery, distinct verifier/reviewer/source binding, one-parent squash gate, and authored tests. Reviewed inherited ten-path blob identities and unmodified current main/predecessor PR metadata.
- Verified actual unedited real #1545→#1575→#1577→#1583 terminal chronology and exact historical squash. Tested isolated Python regex behavior for legitimate direct YAML alias forms with inline comments/quoted keys (direct match fails). No independent entire workflow replay claimed.

## Required result
- Report: `docs/planning/wave-2/reviews/factory-seeding-frontier-repair-1596-review.md`.
- **CHANGES_NEEDED: 1 BLOCKER (FSR-1598-B01), 1 MAJOR (FSR-1598-M01), 0 correction-requiring MINOR**.
  - B01: prefix owner reconstruction fails to end a generation on valid earlier terminal states except `STATUS(HANDOFF_READY)`; later terminal reuses ended owner.
  - M01: regex-based extension alias key scan rejects valid direct quoted keys, inline comments and commented extensions headers; valid source liveness may be suppressed.
- Publish report and this handoff in an own two-file **draft review-only PR to main** and terminal schema-3 `REVIEW_STATUS(CHANGES_NEEDED)` with exact PR/head/owner binding.
- Materialize mandatory fresh bounded blocking-remediation successor, preserving all immutable upstream source/review PRs. A corrected producer needs exact-head read-only CI, distinct new required review and separately authorized squash-only NONCANONICAL integration if clean.
- Reviewer has no source, verification, integration or canonicality authority. No `game/` changes, source branch edits, producer/self-review, main mutation, production or release readiness.
