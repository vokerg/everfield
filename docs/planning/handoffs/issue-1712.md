# Issue #1712 — Markdown-delimited live PR retirement reference remediation

**Mission:** `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-06`  
**Owner:** sole first unedited schema-3 CLAIM #6131575766, actor `frontier-markdown-retirement-remediate-1712-gpt6-20261012-2157-cph-01`, branch `planning/issue-1712`; immediately rechecked no competing claim.  
**Current-main base:** `a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`; canonical binding Issue #1147 terminal #5675066392, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.

## Immutable security provenance
Genuinely distinct independent reviewer Issue #1710 terminal `REVIEW_STATUS(CHANGES_NEEDED)` #6131551071 (0 BLOCKER / 1 MAJOR `FSR-1710-M01` / 0 correction-requiring MINOR), reviewer-only OPEN/DRAFT PR #1713 exact HEAD `8c8f28ac2447e2af04dc2a4538adb3b159593084` and immutable report `docs/planning/wave-2/reviews/negative-review-retirement-1707-review.md` blob `87612c9466ac1dd34fc19918d6a5c3c2c816481c`. Source #1707 first CLAIM #6131364086 and in-lease `STATUS(REVIEW_READY)` #6131423081, frozen OPEN/DRAFT source PR #1709 HEAD `c5d1a94122ca8a97430a0bbf4e3be66438f5f520`, source Python blob `ee76f90ba782848e412bf7e0f8ad80936bdc152e`; prior HTTP/API/protocol-relative security fix must remain intact. Neither source #1707 nor reviewer #1710 is approved for merging.

## Exact owned correction
Fresh-main task branch changes only these three paths:
1. `tools/planning/retire_negative_review_prs.py`: inherit frozen #1707 implementation, split unescaped Markdown table pipes out of extracted URL tokens and strip only trailing Markdown emphasis `*`/`_` from the decoded PR path segment. Preserve exact numeric and repository matching; `/pull/2000`, `/pull/200abc`, `/issues/200`, attacker hosts and other repositories stay nonreferences.
2. `.github/workflows/retire-negative-review-prs.yml`: inherited byte-identical from frozen #1707, Git blob `e141fffcbb95c02fa215ffec3c403e0e93d1fc90`. Pull-request read-only compile/`--self-test`; mutation job runs only on reviewed, squash-published main schedule/explicit dispatch.
3. `docs/planning/handoffs/issue-1712.md`: this task's durable continuation evidence.

Embedded actual-module regression covers first-party HTTPS, HTTP and protocol-relative web/API references surrounded by bold/italic/underscore Markdown, adjacent table pipes/next cells, `.diff`/`.patch`, explicit `:443`, including active issue title, body, completely loaded comments, direct matcher, and mocked real `execute(apply=True)` on both initially linked and newly linked second pre-PATCH snapshots with **zero PATCH**. Inherited owner six-hour lease, first-winner/reviewer-head/report provenance, 72h grace, complete issue/comment pagination and predecessor malformed-host/port tests are retained.

## Verification and next gates
Run exact-final-HEAD hosted read-only GitHub Actions Python compile/full `--self-test` and confirm `retire` mutation job SKIPPED; distinguish that authored CI from **genuinely independent adversarial review**. Freeze exact branch/head/changed path and evidence in owner terminal only after verifying. Route exactly one new required distinct independent security review; do not self-review, self-integrate, live `--apply` or close any PR. Even a CLEAN reviewer grants no direct publication: a separately eligible owner must authorize expected-head/current-main-compatible **SQUASH-only NONCANONICAL** source integration. All original negative/reviewer-only drafts remain immutable; no canon/gameplay/engine/readiness/production/release authority. GitHub's GET-to-PATCH check is non-atomic and cannot eliminate a last-millisecond race.
