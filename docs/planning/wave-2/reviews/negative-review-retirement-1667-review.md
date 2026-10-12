# Issue #1669 — Independent adversarial review of negative-review draft retirement

## Disposition and frozen evidence

**REVIEW_STATUS(CHANGES_NEEDED): 1 BLOCKER, 3 MAJOR, 0 correction-requiring MINOR. Do not merge/deploy source PR #1668.**

Required distinct review of owner source Issue #1667 terminal `STATUS(REVIEW_READY)` #6112520409, draft PR #1668 frozen HEAD `7860a23f2f1a4dcbebdcf22db6a770febf07b3d8`, source base `3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`. Review episode begins at current main `8f8223b0c58956bbc888760ef14f63fa79d2117d` (only disjoint route-history four-path squash relative to source base). Active canon #1147 comment #5675066392 / program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`.

Frozen source exactly three new paths:
- `tools/planning/retire_negative_review_prs.py` Git blob `6c29ffa2876ef1fba3d45bb97fa22696a312ff3a`;
- `.github/workflows/retire-negative-review-prs.yml` Git blob `e141fffcbb95c02fa215ffec3c403e0e93d1fc90`;
- `docs/planning/handoffs/issue-1667.md` Git blob `af77af8d2186e073e7dc286ae7b1f71ea7799b0d`.

GitHub Actions exact PR HEAD run #38165886300 is SUCCESS: compile/self-test job #114548233770 SUCCESS; retirement job #114548262785 SKIPPED on `pull_request`. The workflow checkout is at immutable event HEAD without write credentials and the scheduled/manual `retire` job is main-ref gated. These positives do **not** test canonical owner validity or mutating TOCTOU and grant no independent acceptance.

## Independent falsification method

Read all 327 lines of frozen Python and 63 lines of workflow, source handoff, issue contract, terminal claim, current main and PR metadata. Ran independent local Python 3 / PyYAML 6.0.3 adversarial fixtures against the production `operational`, `timestamp`, and `eligibility` predicates transcribed from the frozen source (no source mutations). Fixture baseline mirrors the author's two-comment negative review, age 10 days, exact SHA, closed completed issue, main-target draft and two review paths.

Observed direct predicate results:
```text
valid reference                                               (True, terminal #2)
forged RESUME with no winning intent, source, branch or head    (True, terminal #2)
first CLAIM without branch/base/observed head                  (True, terminal #2)
unrelated review report + issue-777 handoff for issue-199      (True, terminal #2)
terminal followed by newer contradictory REVIEW_READY         (True, terminal #2)
```
These are *false positives* under the claimed strict authority policy, not successful GitHub API mutations. The fixture calls the actual source predicate logic with valid unedited owner-login comment envelopes and parsed YAML. The second/third cases deliberately omit schema-3 required generation fields, thereby proving a lack of canonical validity enforcement rather than relying on a fabricated timestamp or a supposed GitHub permission bypass. The last case tests failure to recognize conflicting subsequent operational records, not a claim that the later review is itself valid canon.

## FSR-1669-B01 — BLOCKER: invalid ownership generations can authorize retirement

At Python lines 151–182, the sole owner test accepts any one same-issue `CLAIM|RESUME|RECOVER` reference matching mission/session, `state: IN_PROGRESS`, comment order and a six-hour elapsed interval. It does **not** reconstruct first-winning claim/intent, `previous_ownership_comment_id`, `winning_intent_comment_id`, valid HANDOFF/STALE/ORPHAN recovery, root branch/observed head/base/canonical binding, intervening generations/PROGRESS lease anchors, or end-of-generation transitions. Earlier owner/progress expiration can also be misread because only initial owner created_at is checked, not its latest valid lease anchor.

An unedited same-account but structurally invalid `RESUME` with no intent or source passes the code's retirement predicate. Likewise an incomplete `CLAIM` without branch, base SHA or observed head passes. Because every agent's GitHub writes carry the owner login, owner-login matching alone is not canonical reviewer authority. **Required correction:** invoke a fail-closed complete canonical schema-3 reconstruction at the precise negative terminal comment prefix, including generation winner/lease, source/branch/actor association, mandatory fields, and later contradictory state handling. Reject incompleteness, rather than inferring eligibility.

## FSR-1669-M01 — MAJOR: mutable veto and issue state go stale before PATCH

At lines 216–246, `open_issues` is paged **once** before any candidate, and review issue, comments, and files are fetched once. On `--apply`, the script re-fetches **only the PR** and calls `eligibility(current, issue, comments, files, open_issues, now)` using the original stale snapshots. A new open remediation issue referencing `#PR`, issue reopening, a changed/edited terminal, or a newly valid owner status between initial scan and PATCH can make the close invalid while the script still returns `True`. This defeats the asserted active-open-reference veto and current-owner check even if the PR head has not moved. **Required correction:** re-fetch authoritative review issue/comments and fresh complete open-issue references immediately before each mutation; re-evaluate all gates, reject data inconsistencies and concurrent changes; where a race cannot be atomically excluded, fail closed and document the residual race. Avoid assuming only PR head can change.

## FSR-1669-M02 — MAJOR: review-only file identity is not authenticated

At lines 129–137, the program accepts any two unique paths sharing generic `docs/planning/wave-2/reviews/` and `docs/planning/handoffs/` prefixes. There is no `issue-<review issue>.md` handoff match, no reviewer report path exactness, nor file type/status/valid blob identity tied to the terminal's `artifact_paths`. The independent fixture accepted `docs/planning/wave-2/reviews/unrelated.md` plus `docs/planning/handoffs/issue-777.md` for review Issue #199 as if they were its provenance. **Required correction:** authenticate exact report and own issue-numbered handoff path, path statuses, and terminal/head-linked blob identity; do not close a mislabeled or unrelated two-file draft.

## FSR-1669-M03 — MAJOR: conflicting later operational statuses are ignored

At lines 139–149, the script filters to `REVIEW_STATUS(CHANGES_NEEDED)` records *before* checking all operational state and accepts exactly one negative even when a later contradictory `REVIEW_STATUS(REVIEW_READY)` or `STATUS(SUPERSEDED)` appears on the same reviewer issue. The fixture appended an unedited newer `REVIEW_READY` record after the one negative and eligibility remained `True`. Whether the later record is valid or invalid must be resolved via schema-3 prefix semantics, not silently disregarded. **Required correction:** reject unexpected later competing operational records and prove the negative terminal remains the authoritative latest settled state at retirement time.

## Other checks, scope, and required route

The strict PyYAML loader does reject simple alias, explicit tag, duplicate semantic string-key and malformed-document examples supplied in source self-test. The PR-trigger job is read-only and mutating job SKIPPED; the runtime API methods use GitHub REST endpoints and enumerate pages at 100 items per page. These positive observations are narrower than a security PASS.

No source, review predecessor, current active factory #1664/#1665, game, shared maintenance script, current main or CI file was modified by this review. The present source is **non-integrable** until one new bounded remediation fixes B01/M01/M02/M03, exact amended HEAD self-test/independent verification evidence is gathered, and a genuinely distinct required adversarial reviewer reaches 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR. Retain source PR #1668 and this review-only draft as frozen evidence; never deploy `--apply`, merge this reviewer-only PR, or upgrade canonicality/production/gameplay/readiness/release authority.
