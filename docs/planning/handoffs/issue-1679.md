# Issue #1679 — negative mandatory independent PR retirement security review

## Active task and frozen evidence

Mission `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-01-REV-01`. Only first valid GitHub-server claim on Issue #1679: #6118874788 at 2026-10-12T06:18:30Z, reviewer session `frontier-independent-pr-retirement-audit-1679-gpt6-20261012-0820-cph-01`, truly different from #1676 remediation, original #1667 author and #1669 reviewer. Review branch `planning/issue-1679`, created at fresh main `8f8223b0c58956bbc888760ef14f63fa79d2117d`; canonical binding #1147 terminal #5675066392, Planning Program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.

Frozen reviewed source Issue #1676 owner `STATUS(REVIEW_READY)` terminal #6118444170; source DRAFT PR #1678 HEAD `d8f580233307b919167fa9e80e9e69b7d3ae24d4`, script blob `a155ecf0c48ba9f49ae906a00d737ced7e1fc0a3`, unchanged workflow blob `e141fffcbb95c02fa215ffec3c403e0e93d1fc90`, source handoff blob `08988e9487925e4795d9c652bdf6164fc64f3fdf`. Exact PR-head hosted Actions #38208828431 SUCCESS, self-test job #114678215180 SUCCESS, mutation job #114678243295 SKIPPED. Original rejected source #1667/PR #1668 and prior independent review #1669/PR #1674 untouched and unmerged.

## Independent negative disposition and report

**CHANGES_NEEDED — one BLOCKER, two MAJOR, zero correction-requiring MINOR.**

- **FSR-1679-B01 BLOCKER:** `retire_negative_review_prs.py::eligibility` ignores PR head branch/ref and source repository, even while checking a separate issue-local claim branch. Replayed same-SHA PR from wrong task branch and different head repo: both false-positive eligibility `True`.
- **FSR-1679-M01 MAJOR:** live-reference veto sees only open issue title/body, not issue comments. Independent comment-only reference fixture remains eligible despite a current issue asking to preserve the reviewer PR.
- **FSR-1679-M02 MAJOR:** report identification uses generic `*-review.md` syntax plus terminal artifact paths, but not the exact task-contract review report path. A wrong but pattern-compliant filename accepted after matched terminal/file mutation.

Independently inspected 422-line frozen script and exact main-only workflow; executed Python 3 + PyYAML 6.0.3 read-only predicates transcribed from the frozen source. Full methods, immutable blobs, test fixtures, result table and bounded remedial acceptance are in reviewer-only report `docs/planning/wave-2/reviews/negative-review-retirement-1676-review.md`. No `--apply` or any main/source/other-agent branch writes.

## Review-only artifact and next route

Exactly two reviewer-owned docs: the report above and this `docs/planning/handoffs/issue-1679.md`. Publish OPEN DRAFT reviewer PR to main before terminal `REVIEW_STATUS(CHANGES_NEEDED)`; exact PR/head and immutable report/handoff blob SHA recorded in the terminal issue comment. Never merge reviewer-only PR, no source review PASS.

Materialize one bounded **blocking** corrective source Issue for all B01/M01/M02, owned by a **different execution** than this reviewer and source producer #1676. New source on current main may modify only standalone PR retirement script and own handoff, port unchanged workflow byte-for-byte, preserve prior branches. Require real PR-head read-only CI self-test with mutating job SKIPPED, and a **new genuinely distinct independent mandatory security reviewer**. Separately owner-authorized exact-head current-main-compatible **SQUASH-only NONCANONICAL** integration only after genuinely CLEAN required review. No factory parser, gameplay, canonical, engine, readiness, legal/truth/consent/accessibility, production or release authority.

Next agent must reconstruct from repository + GitHub; refresh current main, canonical binding, all owner generations, PR exact SHA, review blobs and competing successor routes before touching anything.
