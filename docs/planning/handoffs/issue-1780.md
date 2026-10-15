# Issue #1780 — bounded source correction and review handoff

**Mission:** `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-15`  
**Task class:** required security remediation of existing OPEN/DRAFT source PR #1775; NOT canonical, NOT production/live-retirement-authorized.  
**Owner CLAIM:** Issue #1780 comment #6188479971; session `existing-retirement-commonmark-correction-1780-gpt6-20261015-cph-01`.  
**Based on:** current main `7da4c2d50412fe134c8632264908560b8b7995ce`, active canonical Issue #1147 binding #5675066392 / program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4` / activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.

## Exact provenance and exclusive mutation

Required independent negative review #1776 terminal #6188416710, evidence-only DRAFT PR #1778 exact HEAD `d5f38c331c28682aeab411e9350d92b1b3bdbe33` (NEVER MERGE), report blob `5e2f93bc4d6a642fa68b6abc262c0bfa9fe8edef`. Source #1773 owner terminal #6187477771; frozen OPEN/DRAFT PR #1775 exact HEAD `13fea3d90fa2e439df1373c8c448c8eb26046d3e`, script blob `610c923de03d238984a8f5e50af62be43404e0d9`, ten changed paths, read-only CI #38702950145 SUCCESS and write-capable retire SKIPPED.

This correction is a new `planning/issue-1780` branch created from exact current main. Preserve **all nine non-script paths** from frozen #1775 byte-identically: the retirement workflow and handoffs #1720, #1726, #1738, #1746, #1756, #1765, #1769, #1773. Source contract #1780 abbreviated the #1720 blob identity; its authoritative exact frozen PR #1775 blob is `088bb6afd8651c941ba1045d3ffab9b10da5d4c1`, verified by fetching that path from frozen SHA. This is not a change to the inherited artifact or a waiver of any gate.

Only correct `tools/planning/retire_negative_review_prs.py` (new authored source blob `eaea88e3acd63c2660058e7b5f2d1f81d50b090b`) and create this handoff as the eleventh changed path. Do not mutate predecessor PRs, reviewer-only evidence, main, any gameplay or factory source, or workflows.

## Changes, adversarial regressions, known limits

**FSR-1776-M01:** accept at most one CRLF/LF after CommonMark inline opener or reference-definition colon, with horizontal whitespace, so clickable multiline relative PR links are recognized. Do not consume arbitrary blank paragraphs. New actual-module self-tests cover body/title/comment and line endings, relative and angle-delimited destinations, reference definitions.

**FSR-1776-M02:** permit balanced parentheses within absolute PR URL path tokens and discard only extra unmatched *terminal* `)` introduced by a CommonMark closing delimiter; keep internal `(z)/..` so existing strict ordered browser path normalization resolves the real target GitHub web/API PR. Reuse existing strict host/IDNA, port, userinfo, owner/repo/number, encoded-path validation and foreign-origin controls. New full-module self-tests include web/API, aliases, subresources, prior Unicode-dot and extra-solidus composition, and negative wrong-PR/repo/route/host cases.

Ten new positive and seven new negative explicit variants were added. Each positive drives `references_pr` and `eligibility` for title/body/loaded-comment veto; all positives were additionally added to the existing actual live issue comment reader and mocked `execute(apply=True)` FIRST-scan and FRESH pre-PATCH-scan zero-PATCH regression loops. Prior source-authored self-tests remain included. A separate local read-only Python regex selector check was performed; **do not claim independent full-module validation before hosted exact-head read-only tests actually complete**. A hosted source CI PASS still is not independent security approval or proof of no GET/PATCH race.

## Required gate before REVIEW_READY

1. Verify exact branch/PR changed-path envelope (11 paths), exact nine inherited Git blobs, frozen source PR unchanged and matching new script blob; confirm current main remains compatible.
2. Obtain hosted exact final HEAD `py_compile` and complete `--self-test` SUCCESS, mutating job SKIPPED. If red, remediate within this existing task and retest; do not claim PASS from source assertion alone.
3. Only then publish in-six-hour-lease immutable schema-3 owner `STATUS(REVIEW_READY)` at matching OPEN/DRAFT PR head, and materialize a NEW genuinely distinct mandatory independent adversarial review. If tests/environment block, publish `HANDOFF_READY` with exact failure/run identity and same-issue valid RESUME; no claim of REVIEW_READY.
4. Reviewer independently execute full corrected module, first/fresh mocked consumer cases and foreign-origin controls. CHANGES_NEEDED -> bounded next remediation; CLEAN only if independently established. Separately owner-authorized, current-main compatible **SQUASH-only NONCANONICAL** source integration thereafter; never merge reviewer-only PRs.

## Strict prohibitions

No `--apply`, live GitHub PATCH, retirement/closure, integration, schema canonicality, engine/readiness, production or release authority. Source authored fixtures are evidence, not independent code/security review. Exact GitHub comment timestamps and first-winning schema-3 ownership must continue to be observed at terminalization.

## Hosted CI correction episode

Initial exact HEAD `7549c131b53286e8de91e736b35fd0abb2688360`, hosted run #38710943897 self-test job #116341858044 FAILED on an inherited HTML-entity + emphasis control at source line 820: `**[review](https://github&#46;com/vokerg/everfield/pull/200)**`. Its write-capable retire job #116341932484 was SKIPPED. Root cause: broadening the URL scanner to preserve balanced inner parentheses also preserved a closing Markdown `)` followed by trailing `**`, so the unmatched closing delimiter escaped the terminal trimming loop. The same task branch was corrected to remove trailing Markdown emphasis marks `*_ ` (actual code `.rstrip("*_")`) *before* removing excess terminal `)`. This preserves the original scanner's existing emphasis handling while preserving true inner balanced URL path data. **Only a new exact-HEAD CI success can upgrade this from correction attempt to verified source readiness.**
