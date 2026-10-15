# Issue #1700 — FSR-1697-M01 mandatory retirement-URL remediation handoff

**Mission:** `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-04`  
**Owner:** sole first schema-3 CLAIM #6131125426, session `frontier-pr-retirement-port-suffix-remediate-1700-gpt6-20261012-2124-cph-01`; six-hour server-created-at lease.  
**Current main at claim:** `a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`.  
**Canonical:** Issue #1147 comment #5675066392, blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation `87c85cecfa9a2ffa464c4b36816a138bf41441af`.

## Exact negative-review dependency

Independent reviewer Issue #1697 first CLAIM #6130962944 and immutable terminal `REVIEW_STATUS(CHANGES_NEEDED)` #6131045146, 0 BLOCKER, **1 MAJOR FSR-1697-M01**, 0 correction-requiring MINOR. Review-only OPEN/DRAFT PR #1701 exact HEAD `8b01dd3e84b993d3748a7e9c0f2b44b9002b84e2`, independent report blob `3b4e78fe48f9935873f1e0bb5d4080a66e3bdc53`. Frozen source Issue #1693 owner `STATUS(REVIEW_READY)` #6130920426, OPEN/DRAFT PR #1696 exact HEAD `cb3c41aa82775e02066c99d4a901c9653a97c63f`, Python blob `368570e79f733646f44bbb42bbd617ed04407093`. Neither older source nor reviewer branch was modified, closed, approved or integrated.

## Bounded branch source and changed files

New branch `planning/issue-1700` starts at the exact claim-time main. Three authorized added paths only:

1. `tools/planning/retire_negative_review_prs.py` — ports frozen #1693 exact source and makes the narrowly requested `references_pr` plus self-test corrections.
2. `.github/workflows/retire-negative-review-prs.yml` — **byte-identical** inherited source blob `e141fffcbb95c02fa215ffec3c403e0e93d1fc90`; pull-request self-test runs compile and full suite, mutating job must be SKIPPED.
3. `docs/planning/handoffs/issue-1700.md` — this reconstruction and next-step record.

## Security correction and tests

`references_pr` parses web/API URL authority using URL `hostname` independently of `port`, permits only absent/443 HTTPS first-party ports, recognizes numeric PR references both as complete `/pull/N` or `/pulls/N` segments and `.diff`/`.patch` suffix endpoints. Recognizes query, fragment, subresources, percent-encoded paths and case/DNS-dot normalization; malformed or ambiguous first-party authority **vetoes** automatic retirement. Host impostors, foreign repositories, issue URLs and longer PR identifiers are not PR #N. Tests require actual `eligibility` veto from active issue **title**, **body** and fully loaded **comment** independently for every :443, suffix, encoded/ambiguous variant. Positive nonreference fixtures include other PR numbers, `200abc`, foreign repos/hosts and issue links. Pre-PATCH two-snapshot `execute(apply=True)` mock now introduces `https://github.com:443/.../pull/200.diff` in the second scan and asserts **no PATCH**.

Existing strict YAML, verified negative review and single owner, exact source/report/PR identities, source mission, six-hour lease, 72-hour aging, pagination/duplicate validation, fresh independent pre-PATCH read, safe nonreference witnesses and all prior fail-closed guarantees are carried forward unchanged. A non-atomic GitHub GET/PATCH race inherently remains and is explicitly not claimed solved.

## Outstanding gates and required continuation

Do **not** publish `STATUS(REVIEW_READY)` until exact-head GitHub Actions `self-test` is conclusively SUCCESS and the `retire` job SKIPPED; inspect actual final PR head and exact paths, current main, canonical binding and lease first. Open exact-head DRAFT source PR as visibility surface; it cannot be integrated based on author tests or mergeability alone. After clean authored CI, publish valid in-lease owner terminal and materialize **one genuinely distinct mandatory adversarial security review** of this exact final head. A separate, owner-authorized, current-main-compatible squash-only NONCANONICAL integration route is required after clean review.

**Prohibitions:** never run live `--apply`, close existing PRs, edit predecessor source/review, claim independent self-review, merge this PR without gate authority, or infer canonical/gameplay/engine/readiness/release/production status.

**Next operator:** independently verify source and changed-path blobs, hosted CI/job outcomes and schema-3 first-winner/lease before taking the distinct review or routing a bounded correction for a CI failure.
