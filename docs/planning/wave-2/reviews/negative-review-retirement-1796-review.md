# Independent adverse security review — source Issue #1796 / PR #1797

## Identity and scope

- Review issue: **#1798**; independent reviewer actor `existing-pr-independent-encoded-dot-html-security-1798-gpt6-20261016-01`; sole first CLAIM **#6216642060**. This is a separate execution from source actor `existing-pr-source-html-relative-anchor-rem-1796-gpt6-20261016-prg-01`.
- Canonical active binding: Issue #1147 comment **#5675066392**, blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af` (confirmed ancestor of `main@7da4c2d50412fe134c8632264908560b8b7995ce`).
- Frozen source: **OPEN/DRAFT, unmerged PR #1797**, `planning/issue-1796@0196971ab71d20eb8cb55f0ceb1f5407adfd050f`, base main `7da4c2d50412fe134c8632264908560b8b7995ce`, source module blob `b259e62491b1b6aa128f29b213b4e3760de9de06`. Source owner terminal `STATUS(REVIEW_READY)` #6211658613, not independent security approval.
- Source PR contains **exactly 15 paths**, including all **13 frozen inherited non-script blobs** matching issue #1796, corrected module `b259e62491b1b6aa128f29b213b4e3760de9de06`, and owner handoff `d26280a5da18b248378a7460285dd03d15c8741a`. Each SHA was independently read from the frozen exact ref. Hosted exact-head run **#38875445063** success; `self-test` job **#116889272894** success; write-capable `retire` job **#116889335779** skipped.
- Reviewer PR contains only this report and `docs/planning/handoffs/issue-1798.md`; it is permanently nonintegrable evidence. No source branch, preceding PR, main, or live GitHub issue/PR state is modified by the review.

## Adverse disposition: CHANGES_NEEDED

**0 BLOCKER, 1 MAJOR (FSR-1798-M01), 0 correction-requiring MINOR.** This review does **not** claim CLEAN, full-module acceptance, live `--apply` safety, or integration authority.

### FSR-1798-M01 — browser-equivalent raw HTML relative links evade first-party reviewer-PR veto (MAJOR)

The newly added `raw_html_relative_references_pr` in exact frozen source `tools/planning/retire_negative_review_prs.py` lines 179–218 uses `HTMLParser` to extract `<a href>` attributes, but *before* browser path processing it discards any destination that does not start literally with `/`, `./`, or `../`:

```python
candidate = href.strip()
if not candidate.startswith(("/", "./", "../")) or candidate.startswith("//"):
    continue
```

This is not equivalent to browser resolution. WHATWG treats percent-encoded dot segments as literal `..` while resolving HTTPS URLs and treats backslash as a path delimiter for special schemes. A GitHub-rendered issue/comment can therefore contain a **clickable same-repository reviewer PR link** that the proposed raw anchor reader ignores. The remaining `references_pr` readers cannot rescue these inputs: no bare `#200`, no absolute `//` URL for `PR_URL`, and no Markdown `](...)` / reference-definition target slot.

| Raw HTML anchor href | Node 22 WHATWG browser destination against `https://github.com/vokerg/everfield/issues/1` | Source literal-prefix gate |
|---|---|---|
| `%2e%2e/pull/200` | `https://github.com/vokerg/everfield/pull/200` | ignored |
| `%2E%2E/pull/0200.diff` | `https://github.com/vokerg/everfield/pull/0200.diff` | ignored |
| `..\\pull\\200` | `https://github.com/vokerg/everfield/pull/200` | ignored |
| `%2e%2e\\pull\\200.patch` | `https://github.com/vokerg/everfield/pull/200.patch` | ignored |
| `../pull/200` (positive control) | `https://github.com/vokerg/everfield/pull/200` | processed |
| `/vokerg/everfield/pull/200` (positive control) | `https://github.com/vokerg/everfield/pull/200` | processed |

Both Markdown-it-py **4.2.0** `MarkdownIt('commonmark', {'html': True})` and Mistune **3.2.1** `mistune.create_markdown(renderer='html', escape=False)` independently preserved these raw anchor elements and href attributes. Python stdlib `HTMLParser(convert_charrefs=True)` produced the expected href strings, *without* the forbidden literal prefixes. An attribute written as `&#37;2e&#37;2e/pull/200` also decodes to `%2e%2e/pull/200` before that check. An HTML comment containing the anchor did not produce a starttag (negative control).

Reproduce directly:

```bash
node - <<'JS'
const base = 'https://github.com/vokerg/everfield/issues/1';
for (const href of ['%2e%2e/pull/200',
                    '%2E%2E/pull/0200.diff',
                    '..\\pull\\200',
                    '%2e%2e\\pull\\200.patch']) {
  console.log(href, new URL(href, base).href);
}
JS
```

Source path: `references_pr` calls `raw_html_relative_references_pr(original_markdown, number, owner, repository)` at ~315, and both `live_open_issue_references` and eligibility consume that predicate before mutating retirement. An open issue title/body/comment with such an href can therefore fail the initial veto or the later pre-PATCH recheck for the very reviewer-only PR number being considered for retirement. The bypass is on the **safety boundary**, not merely output formatting. The intended fix is narrowly to normalize browser-special-scheme relative paths, including encoded-dot and backslash variants, *before* deciding whether a raw anchor has a PR destination; preserve strict first-party host/repo/number and wrong-target/HTML-comment controls. Unknown first-party navigation must fail closed.

## Evidentiary boundaries

The finding was independently reproduced with actual Node 22 URL resolution, two real Markdown renderers, and stdlib HTML anchor decoding; it was checked against the **exact fetched frozen source function body and call site**, not inferred from authored tests or a prior review. **The full 79,829-byte Python module was read over the GitHub connector but could not be transferred into the isolated Python runtime; it was not imported or executed end-to-end.** Consequently, actual full-module `execute(apply=True)` zero-PATCH mocked runs, paging/API-error matrix, malformed/edited ownership matrix, and new hosted independent tests have **not** been performed and are *not* claimed. A negative safety-finding alone is sufficient to reject CLEAN; these omitted tests remain mandatory for the corrective successor and its next genuinely distinct full-module review.

Neither source-authored CI nor this bounded reproduction certifies safe production, GitHub API race freedom, a full accessibility/GFM browser contract, or the retirement automation's non-atomic GET/PATCH interval. No real PATCH, retire/close, merge, or workflow mutation was executed.

## Required next route

**ONE mandatory bounded corrective successor of frozen existing OPEN/DRAFT source PR #1797 for FSR-1798-M01**: fresh main and canonical/ownership re-derivation; preserve its exact frozen 15-path source packet while changing only the retirement source module and adding the new owner's handoff; prove encoded-dot/backslash raw HTML links block retirement in title/body/fully paged comments at both initial and fresh pre-PATCH scans with actual complete-module mocked `execute(apply=True)` zero PATCH; retain old positives and foreign/wrong-target negatives; source exact-head read-only hosted CI success and mutation job skipped; new genuinely distinct mandatory full-module independent security review. The old source/review branches and this reviewer-only PR must stay unmodified/unmerged. Only separately owner-authorized exact-head **squash-only NONCANONICAL** integration after genuinely CLEAN review can ever merge an eligible corrected source packet.

**Final disposition: CHANGES_NEEDED; source PR #1797 NOT INTEGRABLE.**
