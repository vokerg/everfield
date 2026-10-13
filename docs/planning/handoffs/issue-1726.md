# Issue #1726 — mandatory HTML-entity PR-retirement reference remediation

## Role, authority, and scope
- Mission: `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-08`. Existing-PR security remediation only; **noncanonical, review-only source**, not integration/retirement authority.
- Sole first winning schema-3 claim: Issue #1726 comment `6132484379`, actor `existing-pr-html-entity-remediate-1726-gpt6-20261012-cph-01`. Claim rechecked immediately before creating task branch.
- Fresh-main base: `a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`, branch `planning/issue-1726`; canonical #1147 binding `5675066392`, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, active ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Mandatory predecessor: source #1720 / OPEN DRAFT PR #1722 exact HEAD `d45397e1452561f6d6aede14129e8c2a753036ac` and script blob `e55e1d74cb28bae2ded082e872c72ed628cbc587`; independent #1724 REVIEW_STATUS(CHANGES_NEEDED) `6132279416`, 0 blocker / **1 MAJOR FSR-1724-M01** / 0 correction-requiring minor, reviewer-only OPEN DRAFT PR #1727 HEAD `324dccb0a220d035f40d13acff75e83f49110e97`. All frozen branches remain untouched.

## Exact changed-path envelope
1. `tools/planning/retire_negative_review_prs.py`: inherited frozen 903-line source, adds `html.unescape(text)` once at the start of `references_pr`, before original strict first-party URL/host/port/path/PR-number checks; extends full actual-module `self_test` with 17 positive CommonMark named/decimal/hex/mixed encoded links and 10 negative/foreign/boundary controls, exercises title, body, fully-loaded comments, first-pass and second pre-PATCH mocked execution (zero PATCH).
2. `.github/workflows/retire-negative-review-prs.yml`: inherited byte-identically, Git blob `e141fffcbb95c02fa215ffec3c403e0e93d1fc90`. PR event only invokes read-only compile/self-test; mutating `retire` job has a separate exact-main schedule/dispatch gate and MUST be SKIPPED.
3. `docs/planning/handoffs/issue-1720.md`: inherited byte-identically, Git blob `088bb6afd8651c941ba1045d3ffab9b10da5d4c1`.
4. `docs/planning/handoffs/issue-1726.md`: this new handoff and no other additional paths.

## Finding, remedy and tradeoffs
CommonMark resolves HTML character references in clickable URL destinations, so raw-only scanning of an issue/comment can miss a first-party PR that the rendered Markdown links to. Decoding HTML entities **once before matching** catches first-party URLs assembled with `&#46;`, `&#47;`, `&#58;`, `&#48;`, `&#63;`, `&#x2e;`, `&period;`, `&colon;`, `&sol;` and mixed CommonMark backslash escapes. All existing strict numeric and path boundaries remain unchanged. Conservative false-positive veto is preferable to closing a live-referenced PR. No claim is made that non-atomic GitHub GET/PATCH can be made atomic.

## Verification protocol and remaining gates
- Verify the exact final PR head against branch, changed paths/blob identities, current main and claim lease. Compile and execute the **actual composed module** through exact-head GitHub Actions `python3 -m py_compile tools/planning/retire_negative_review_prs.py` and `python3 tools/planning/retire_negative_review_prs.py --self-test`. Inspect self-test job **SUCCESS** and mutation-capable `retire` job **SKIPPED** at the exact final head. No live `--apply`, no GitHub PATCH or PR/issue closure.
- The source-author's tests/hosted CI are **not independent security acceptance**. After exact-head DRAFT PR and in-lease owner `STATUS(REVIEW_READY)`, require one **new genuinely distinct mandatory adversarial security review** of the exact final source. A negative finding requires bounded successor; clean review only unlocks a separately owned, current-main-compatible, squash-only **NONCANONICAL** integration episode.
- Frozen #1722 and reviewer-only #1727 MUST NEVER be merged under this task. No canon, game readiness, engine selection, release or production authority.

## Checkpoint
Code, inherited workflow and predecessor handoff have been published on the bounded task branch. Hosted final-head CI and a new separate reviewer route must be verified before terminal owner status; this handoff does not itself assert test PASS or authorize integration.
