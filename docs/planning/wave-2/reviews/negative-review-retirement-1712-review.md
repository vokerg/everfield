# Mandatory independent review #1717 — PR-retirement Markdown escaping

**Disposition: CHANGES_NEEDED — 0 BLOCKER, 1 MAJOR FSR-1717-M01, 0 correction-requiring MINOR.** This is a negative review of exact source #1712, not a clean full-module acceptance, nor integration or PR-retirement authority.

## Exact authority / source

- Reviewer #1717 valid sole immutable first CLAIM #6131714848, created 2026-10-12T20:04:49Z, distinct actor `frontier-independent-markdown-retirement-review-1717-gpt6-20261012-2210-cph-01`, branch `planning/issue-1717`, base `main@a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`.
- Canonical Issue #1147 binding #5675066392 / program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4` / activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Producer Issue #1712 first CLAIM #6131575766 (2026-10-12T19:55:26Z); valid unedited in-lease `STATUS(REVIEW_READY)` #6131666824 (2026-10-12T20:01:36Z). OPEN/DRAFT source PR #1715 HEAD `ed5431f76e456c4e9b98f567307a3cca9ee59241`.
- Exactly three producer paths: `tools/planning/retire_negative_review_prs.py` Git blob `bc6ef813512f45120bdfbe623b417755971e301a`; unchanged `.github/workflows/retire-negative-review-prs.yml` Git blob `e141fffcbb95c02fa215ffec3c403e0e93d1fc90`; `docs/planning/handoffs/issue-1712.md`. Exact-source authored Actions run #38301241604 SUCCESS, validate #114984418496 SUCCESS, mutating retirement job #114984481653 SKIPPED. None is independent acceptance.
- Prior independent negative review Issue #1710 terminal #6131551071 and reviewer-only PR #1713 remain immutable provenance. No source, review predecessor, or main change in this review.

## FSR-1717-M01 (MAJOR) — Markdown backslash-escaped PR-link destinations not recognized

The frozen Python source's `PR_URL` (~lines 97–100) requires contiguous `https://`, `http://` or `//`. The `references_pr` predicate (~102–157) processes **raw Markdown** from open issue title/body/comment, not rendered Markdown. CommonMark backslash escapes punctuation in link destinations, including slash `/`, so the rendered link points to a real first-party GitHub PR while the raw text has no matching URL token.

I retrieved the **actual frozen source** from PR #1715's exact HEAD and independently executed its **verbatim extracted** `PR_URL` and `references_pr` logic in a Python 3 harness, together with **MarkdownIt 4.2.0** and **Mistune 3.2.1** Markdown renderers. Both renderers produced the intended clickable PR #200 for all seven bypass variants; the extracted predicate reported **False** on every one.

| Raw Markdown source (input to the frozen predicate) | Rendered href | Veto for PR 200? |
| --- | --- | --- |
| `[review](https:\/\/github.com/vokerg/everfield/pull/200)` | HTTPS GitHub PR 200 | **False — bypass** |
| `[review](https:\/\/github.com\/vokerg\/everfield\/pull\/200)` | HTTPS GitHub PR 200 | **False — bypass** |
| `[review](https://github.com\/vokerg\/everfield\/pull\/200)` | HTTPS GitHub PR 200 | **False — bypass** |
| `[review](https://github.com/vokerg/everfield/pull\/200)` | HTTPS GitHub PR 200 | **False — bypass** |
| `[review](http:\/\/github.com/vokerg/everfield/pull/200)` | HTTP GitHub PR 200 | **False — bypass** |
| `[review](\/\/github.com/vokerg/everfield/pull/200)` | protocol-relative GitHub PR 200 | **False — bypass** |
| `[review](https:\/\/api.github.com/repos/vokerg/everfield/pulls/200)` | HTTPS GitHub API PR 200 | **False — bypass** |
| `[review](https://github.com/vokerg/everfield/pull/200)` | HTTPS GitHub PR 200 | **True — control** |
| `[review](https://github.com/vokerg/everfield/pull/2000)` | different PR 2000 | **False — control** |

The separate Markdown renderer output was inspected for exact `<a href="https://github.com/vokerg/everfield/pull/200">` or matching HTTP/scheme-relative/API URL; every bypass renders the matching exact PR 200 href. This is not an invalid URL, mere text formatting, or a different repository/number. The escaped forms are normal Markdown link destinations.

**Relevant actual consumer:** `eligibility` (~225–247) invokes this exact predicate for every open issue's `title`, `body` and fully loaded comment body. `execute(apply=True)` (~426–473) re-reads live issues immediately before PATCH but invokes the same `eligibility`; a Markdown-escaped PR link is a deterministic blind spot at *both* scans. A reviewer-only draft meeting all other retirement predicates could be closed despite a still-live clickable reference. The corrected source's authored tests cover emphasis and table `|` but omit these escaped-slash destinations.

### Reproduction scope and limitations

- **Executed independently:** exact extracted source `PR_URL`/`references_pr` path; seven negative variants, one genuine-link positive control, one different-PR negative control, and MarkdownIt/Mistune actual render output; Python standard library regex/urllib and markdown-it-py 4.2.0/mistune 3.2.1. No external HTTP or live GitHub write.
- **Read-only inspected, NOT independently executed:** entire 865-line source Python module import, `eligibility` with live-data mocks, `live_open_issue_references`, `execute(apply=True)`, v1–v7 suites, actual GitHub Actions independent verifier. **Do not claim full module execution, comprehensive security PASS, zero other vulnerabilities, or clean acceptance.** A bounded correction-requiring MAJOR suffices for this negative disposition.
- Previously guarded repo/head/branch/owner/report proof, unedited operational comments, six-hour owner lease, 72h grace, bounded complete comment paging and two-snapshot PR head/state checks remain subject to new independent revalidation. The GET-to-PATCH race is still non-atomic and has no compare-and-swap guarantee.
- No `--apply`, live PATCH, PR closure, source/reviewer predecessor edit, source merge, reviewer-only merge or main mutation performed.

## Required successor / integration boundary

**One mandatory bounded corrective successor Issue #1720** materializes FSR-1717-M01; **BLOCKED until** this review's valid exact-head DRAFT reviewer-only PR and in-lease terminal `REVIEW_STATUS(CHANGES_NEEDED)`. A distinct new owner must inherit frozen three-path source PR #1715; correct only the script and own handoff, preserve identical workflow blob, and execute *actual corrected full module* with positive/negative Markdown-escaped URL, HTTP/HTTPS/protocol-relative/API path, title/body/comment, first-pass and second pre-PATCH zero-PATCH cases, strict foreign repo/number controls, existing tests and exact-head read-only CI. Require **new genuinely distinct security review** and only then separately owned/authorized current-main-compatible **SQUASH-only NONCANONICAL** integration if clean. Reviewer-only PR **never merges**. No canon, gameplay/engine/readiness, production or release authority.
