# Issue #1720 — bounded existing-PR security remediation handoff

**Role:** mandatory FSR-1717-M01 correction of previously rejected source Issue #1712 / OPEN-DRAFT PR #1715. This branch is NOT independently reviewed or merge-authorized. No live PR retirement, `--apply`, GitHub PATCH, issue closure, or main integration performed.

## Authority / frozen provenance

- Sole claimed schema-3 owner Issue #1720 CLAIM **#6131823266**, actor `frontier-existing-pr-escaped-markdown-remediate-1720-gpt6-20261012-01`, branch `planning/issue-1720`, initial main base `a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`.
- Canonical Issue #1147 terminal binding #5675066392, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Frozen source Issue #1712 claimant #6131575766 and `STATUS(REVIEW_READY)` #6131666824; PR #1715 OPEN/DRAFT at `ed5431f76e456c4e9b98f567307a3cca9ee59241`, Python blob `bc6ef813512f45120bdfbe623b417755971e301a`, workflow blob `e141fffcbb95c02fa215ffec3c403e0e93d1fc90`, authored exact-head hosted CI #38301241604 SUCCESS (validate #114984418496 SUCCESS, mutating retire #114984481653 SKIPPED).
- Genuinely distinct negative reviewer Issue #1717 CLAIM #6131714848, `REVIEW_STATUS(CHANGES_NEEDED)` #6131815559 (0 BLOCKER, 1 MAJOR FSR-1717-M01, 0 correction-requiring MINOR), immutable reviewer-only OPEN/DRAFT PR #1721 exact HEAD `07c99e75bb5a6e00b13e08dfbf8fef01e876020c` and source review report `docs/planning/wave-2/reviews/negative-review-retirement-1712-review.md` blob `35f98b28d0de25af38d92448928b52a164b60de3`.

## Exclusive three-path correction

1. `tools/planning/retire_negative_review_prs.py` — inherited frozen source full module; conservative `references_pr` now recognizes CommonMark escaped URL forward slashes by replacing **only** backslash-slash pairs in the scanned raw Markdown before existing first-party authority, exact repo, path, numeric PR segment and suffixed endpoint checks. No changes to first-winner/lease, 72-hour grace, complete active-issue-comment pagination, second pre-PATCH validation or mutation semantics. The module's actual built-in self-test now covers seven first-party CommonMark escaped web/API HTTP/HTTPS/scheme-relative destinations plus seven nonreference controls in title, body and loaded comment positions, and mock `execute(apply=True)`'s first-pass and late pre-PATCH zero-PATCH scenarios. Prior HTTP, .diff/.patch, encoded-path, emphasis, table-boundary and false-positive tests are preserved.
2. `.github/workflows/retire-negative-review-prs.yml` — transplanted verbatim from frozen source blob `e141fffcbb95c02fa215ffec3c403e0e93d1fc90` (same bytes); PR self-test job has read-only permissions and gated mutating `retire` skips pull requests.
3. `docs/planning/handoffs/issue-1720.md` — this new task handoff.

No other repo paths authorized or changed. Original producer and reviewer PRs remain immutable, draft and non-integrated. Any hosted successful self-test is authored evidence, NOT independent security acceptance.

## Mandatory gates, stop conditions and next route

Publish exact final-head source OPEN/DRAFT PR with exactly the three paths and inspect hosted Python compile/full `--self-test` PASS on **final source head**, mutation job SKIPPED. If CI fails, correct only own source branch and rerun at exact new final HEAD. After valid self-test and live main/head/canonical/lease recheck, record in-lease owner `STATUS(REVIEW_READY)`, then route **one truly distinct mandatory adversarial security review**, different from source and Issue #1717. The reviewer must independently exercise actual corrected module, open-issue title/body/all comments, seven escaped links, mixed suffixes and strict negative controls, first-pass and second pre-PATCH zero-PATCH behavior, and predecessor safety gates. Only a CLEAN terminal with 0 BLOCKER/MAJOR/correction-requiring MINOR can permit a **separately owned and authorized**, expected-head/current-main-compatible, **SQUASH-only NONCANONICAL** source publication. No self-review, self-merge, reviewer-only PR merge, live `--apply`, canon, gameplay/engine/readiness, production or release authority. GitHub GET/PATCH remains non-atomic; no compare-and-swap guarantee.
