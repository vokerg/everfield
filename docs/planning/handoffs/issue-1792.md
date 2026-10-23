# Issue #1792 — HTML-entity Markdown delimiter source correction handoff

## Ownership, scope and canonical binding

- Mission: `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-18`.
- Owner CLAIM: Issue #1792 #6211042106, actor session `existing-pr-retirement-source-1792-entity-delimiter-gpt6-20261016-prg-01`, created 2026-10-16T08:08:26Z, immediately rechecked sole winner.
- Base: `main@7da4c2d50412fe134c8632264908560b8b7995ce`.
- Active planning canonical binding: Issue #1147 terminal #5675066392, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Frozen predecessor source Issue #1788 REVIEW_READY #6200656618; OPEN/DRAFT PR #1789 immutable HEAD `d89cc524e7aece029246e3670a121d4ae8b9e810`, module blob `bd2e1e28c2ea52ca5fee0f5001fd6ab5dd40c606`.
- Genuinely distinct independent rejection Issue #1790 terminal REVIEW_STATUS(CHANGES_NEEDED) #6210947527 (0 BLOCKER, 1 MAJOR FSR-1790-M01, 0 correction-requiring MINOR); reviewer-only PR #1791 HEAD `630a2c0ef18000ebdbedf37e2fb2d47d05e97198`, permanently nonintegrable.

## Exclusive corrected source packet

New source branch `planning/issue-1792` was created from exact main after winning claim. This bounded corrective source packet inherits all **13** prior source-PR paths and preserves **12** inherited protected Git file blobs byte-identically. The sole modified pre-existing source path is `tools/planning/retire_negative_review_prs.py` (new Git blob `b3d03feab7b74eeca15ea1fd97bf2242ab7fcacd`), plus this single new handoff `docs/planning/handoffs/issue-1792.md`. Exactly 14 paths relative to main. No changes to frozen PR #1789, reviewer-only #1791, main, gameplay, program, or workflow code.

## FSR-1790-M01 correction

Before scanning for CommonMark's unmatched closing delimiter, retain `original_markdown = text` rather than pre-decoded `html.unescape(text)`. Match link-target structural delimiters only against `original_markdown`; **after** finding the actual unescaped unmatched delimiter, decode HTML character references in `destination` and then Markdown backslash punctuation before URL identity/path matching. Preserve the separate existing decoded absolute/GitHub hash reference reader.

This protects a rendered live same-repo PR URL in `[review](../a&#41;b/../pull/200)`: HTML-encoded `)` remains *URL data*, not an early Markdown delimiter. Add source-authored self-tests for decimal/hex entity, root and issue-directory relative, nested parentheses, escaped-plus-entity, one LF/CRLF after opener, reference definitions, wrong PR/repo/origin negatives. Exercise eligibility in active title/body/comments, actual paged live-issue reference reader and mocked `execute(apply=True)` initial/fresh pre-PATCH veto with **zero PATCH**, preserving previous authored coverage.

## Validation and remaining authority

- The code and authored tests must complete hosted **exact-final-HEAD** read-only Python compile/full `--self-test` SUCCESS, with write-capable retirement workflow job SKIPPED. Do not claim these tests have already passed until GitHub verifies them on the immutable final head.
- Source-author tests are not an independent final security review. After successful hosted CI, publish only valid in-six-hour-lease `STATUS(REVIEW_READY)` for an exact OPEN/DRAFT source PR head. Require one new genuinely distinct mandatory independent **full-module** adversarial code/security review. No CLEAN was inherited from the negative predecessor.
- Independent source-module and mock execution beyond hosted authored `--self-test` was not executed in the connector-only source-author environment; no false independent PASS is asserted.
- Only a later separately owner-authorized current-main/exact-head-compatible **SQUASH-only NONCANONICAL** integration route after genuine CLEAN may integrate. No live `--apply`, PATCH, PR closure, reviewer-only merge, canonicality, implementation/game/engine-readiness, release or production authority. Keep predecessor PRs frozen.
- If hosted CI fails, or main/source/head/ownership changes, remain nonterminal with an exact status/handoff and correct or rederive; never represent REVIEW_READY without its gates.
