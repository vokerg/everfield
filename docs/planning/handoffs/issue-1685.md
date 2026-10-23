# Issue #1685 — required PR-retirement security remediation

## Exact provenance and authority

Mission `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-02`, canonical Planning Program #1147 terminal binding #5675066392, immutable active blob `fd4cf1119c3f86acc3af620024eea72235e81ce4` activated at `87c85cecfa9a2ffa464c4b36816a138bf41441af`. Sole first schema-3 CLAIM on #1685: #6127268023, GitHub-created_at 2026-10-12T15:23:34Z, execution `frontier-independent-retirement-remediate-1685-gpt6-20261012-1720-cph-01`. Branch `planning/issue-1685` from then-current `main@a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`. No previous retirement author/review actor owns this execution. Six-hour owner lease anchored by authoritative GitHub-created timestamp, subject to normal rechecks before terminal.

Inherited *immutable* unsafe source #1676 / DRAFT PR #1678 HEAD `d8f580233307b919167fa9e80e9e69b7d3ae24d4` script blob `a155ecf0c48ba9f49ae906a00d737ced7e1fc0a3`, strict workflow blob `e141fffcbb95c02fa215ffec3c403e0e93d1fc90`. Mandatory genuinely distinct independent negative review #1679 terminal #6118961848, reviewer-only DRAFT PR #1684 HEAD `f0ef7c688e38ae7276a2ad2fea92b38285d1a41b`, immutable report `docs/planning/wave-2/reviews/negative-review-retirement-1676-review.md` blob `747f03cd490fdf1d63a862e7c26dd35d5c7116f2`. **CHANGES_NEEDED: 1 BLOCKER FSR-1679-B01 and 2 MAJOR FSR-1679-M01/M02.** Neither source, reviewer nor earlier negative branches were mutated, merged or approved.

## Bounded changes

Only three task-owned paths:
- `tools/planning/retire_negative_review_prs.py`, corrected script authored from immutable source #1678, current candidate blob `caf8d61687874479978df9a834511b85b7a583bd`;
- `.github/workflows/retire-negative-review-prs.yml`, ported **byte-identically** from rejected source, Git blob `e141fffcbb95c02fa215ffec3c403e0e93d1fc90`;
- this issue-numbered handoff.

### FSR-1679-B01 — actual source PR identity

Even when identical HEAD SHA, title and author, an unrelated task branch or fork can point at that commit. `eligibility()` now authenticates actual `pr.head.ref` against `planning/issue-N` and actual `pr.head.repo.full_name` plus `pr.base.repo.full_name` against `vokerg/everfield`, rejecting null/missing metadata. It also reads the reviewer issue's mission and independent-review role contract and requires it to match original first winning CLAIM, rather than trusting the PR title or terminal alone. Negative fixtures exercise alternate ref, fork, wrong base, missing repo, mismatch mission.

### FSR-1679-M01 — comments on active issues

The complete active-open-issue reference scan loads and count-checks every live issue's comments (except pull requests), with bounded 200-issue/1000-comment-per-issue conservative stop. Duplicated issue/comment IDs, unavailable text, mismatched GitHub comment counts, pagination/API/rate limit failures and incomplete coverage fail closed. `eligibility()` vetoes the draft for PR references in title, body **or any live comment**, and refuses any incomplete coverage. Both initial eligibility and immediately-before-PATCH checks read exhaustive fresh issue/comment snapshots, and the latter also compares exact original PR head branch and repository identities. A separately performed GitHub PATCH is not atomic with these reads; the residual last-millisecond race remains explicitly unwaived. Fixtures include an active remediation referencing only `PR #200` in a comment, a successfully complete nonmatching issue, incomplete coverage and a stubbed GitHub live scan/count mismatch.

### FSR-1679-M02 — exact report identity

The issue's separately declared mission and unique required review report filename are extracted from the trusted reviewer *issue body*; terminal `artifact_paths` and two SHA-bound added GitHub diff files must match this independently required path. Another `*-review.md` filename cannot substitute, even if a terminal and report diff collude. Negative fixtures vary both terminal and added file, missing/ambiguous contract and mission mismatch.

## Preserved controls, evidence and limitations

Preserves the original strict complete sole-CLAIM in-lease unedited schema-3 `REVIEW_STATUS(CHANGES_NEEDED)` terminal check, six-hour lease based on GitHub `created_at`, 72-hour aged negative-only grace, exact unchanged review HEAD, only exactly two added SHA-bound reviewer docs, any subsequent operational ownership disqualifier, source and verifier PR non-integrability. Script defaults to DRY-RUN and the unchanged workflow runs `pull_request` only in read-only `self-test`; the mutation job is restricted to separately published current `main` schedule/dispatch. Neither authored tests nor this handoff are independent security approval.

For exact HEAD verification, require actual GitHub Actions workflow **Retire provably rejected reviewer-only draft PRs** triggered on the DRAFT PR's precise final HEAD, self-test Python compile and all embedded negative tests SUCCESS, `retire` job SKIPPED. Inspect actual PR changed-file list, HEAD SHA and git blobs after final handoff commit. Record corresponding hosted run/job IDs and all immutable evidence in #1685 schema-3 terminal if eligible. No source deployment or `--apply` is authorized from this draft.

## Downstream transition / recoverability

A valid exact-head draft PR into then-current main MUST pre-exist before owner `STATUS(REVIEW_READY)`. If hosted compile/selftest or source integrity fails, leave recoverable HANDOFF_READY rather than claiming verification/review. Once exact-head authored CI passes, publish only owner `STATUS(REVIEW_READY)` to task Issue #1685; then materialize **one newly genuinely distinct mandatory independent adversarial code/security review** of frozen final HEAD. The #1679 reviewer or this producer cannot self-review, and a new actor name in the same execution is not independence. Source merge requires a subsequent clean required review and **separate owner-authorized, current-main-compatible, expected-HEAD SQUASH-only NONCANONICAL** publication. No shared factory/parser, game, canon, engine/readiness, truth/consent, accessibility, production or release authority.