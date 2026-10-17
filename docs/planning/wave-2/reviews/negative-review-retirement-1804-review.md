# Independent adverse security review — Issue #1804 / source PR #1805

## Frozen authority and reviewer independence

- Reviewer Issue #1807, mission FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-21-REV-01. Winning first valid unedited claim #6232324763 at 2026-10-17T09:32:08Z, actor frontier-independent-scheme-network-security-1807-gpt6-20261017-prg-01. Later competing claim #6232332316 loses. This execution is different from source Issue #1804 actor everfield-source-commonmark-networkpath-rem21-gpt6-20261017-01.
- Fresh main 7da4c2d50412fe134c8632264908560b8b7995ce. Active canonical Issue #1147 terminal #5675066392, program blob fd4cf1119c3f86acc3af620024eea72235e81ce4, activation ancestor 87c85cecfa9a2ffa464c4b36816a138bf41441af. No main/canonical mutation.
- Frozen source: Issue #1804 first valid winning CLAIM #6232234753 (2026-10-17T09:21:50Z), losing duplicate #6232235583, unedited within-lease STATUS(REVIEW_READY) #6232304061 (2026-10-17T09:29:51Z). OPEN/DRAFT unmerged source PR #1805 branch planning/issue-1804 HEAD 7bcaf1481f4f137e61bc3f2a3f18ce3d48ddfd5a, source Python blob 9c1fcca1fd0fbb5663d27ffccb77dc09e12655d1. GitHub PR file listing confirms exactly 17 added paths, including 15 unchanged inherited non-script blobs, script and source issue handoff 0d8b804ba23575b28b7b4dd1c1e5a3114576ef9a.
- GitHub Actions exact-head run #39021277234 completed SUCCESS; authored Python compilation/self-test job #117363417274 SUCCESS, mutating retirement job #117363447239 SKIPPED. This is not independently verified security CLEAN.
- Independent adverse predecessor #1802 terminal REVIEW_STATUS(CHANGES_NEEDED) #6232221347 (0 BLOCKER/2 MAJOR), evidence-only never-integrable DRAFT PR #1803 HEAD 352335f6c9a6169609ee0c720b41ce79ec5cc810; older source #1801 remains frozen.

## Verdict: CHANGES_NEEDED — 0 BLOCKER; 1 MAJOR FSR-1807-M01; 0 correction-requiring MINOR

### FSR-1807-M01 — CommonMark autolink bypass of live PR-link veto (MAJOR)

The corrected code recognizes explicit Markdown links such as [review](https:../pull/200), but the separate **CommonMark automatic URL link** source syntax <https:../pull/200> is a clickable first-party GitHub PR anchor and is ignored by all source readers. Both Markdown-it-py 4.2.0 in CommonMark mode and Mistune 3.2.1 independently rendered this source as a paragraph with an HTML anchor whose href was exactly https:../pull/200. Both also rendered <https:/vokerg/everfield/pull/200> as a clickable anchor.

Independently executed Node.js 22.16.0 WHATWG URL normalization against base https://github.com/vokerg/everfield/issues/1 yielded:
- https:../pull/200 → https://github.com/vokerg/everfield/pull/200 (protected live reviewer PR)
- https:/vokerg/everfield/pull/200 → https://github.com/vokerg/everfield/pull/200
- https:../pull/201 → https://github.com/vokerg/everfield/pull/201 (wrong-PR negative control)
- https:../issues/200 → https://github.com/vokerg/everfield/issues/200 (wrong-route control)
- https:////evil.test/vokerg/everfield/pull/200 → https://evil.test/vokerg/everfield/pull/200 (foreign-host control)

The source's actual references_pr implementation (read directly from exact source blob via GitHub) has exhaustive relevant gates for this source text:
1. No literal #200 appears.
2. PR_URL requires the // authority delimiter; the first two positives contain no such delimiter.
3. _RelativeHtmlAnchorParser.handle_starttag extracts only raw HTML tag a with href attributes, not a CommonMark <scheme:...> autolink (which is rendered to an anchor by Markdown, after parsing).
4. RELATIVE_MD_LINK_TARGET considers only the ]( inline destination opener or [ref]: definition opener. Its new same-scheme resolver is called only *inside this matching loop*. Neither positive CommonMark autolink enters the loop.
5. Hence references_pr has no reader for either positive original Markdown token. Eligibility scans all live open issue titles/bodies/comments through this same predicate, including each initial and final immediately-before-PATCH execute(apply=True) reread. A reviewer-only negative PR otherwise eligible after 72 hours might be retired while its PR is still linked from an active issue.

The independent Python probe reused the **verbatim PR_URL and RELATIVE_MD_LINK_TARGET regexes from the exact fetched module**, and stdlib HTMLParser on the actual Markdown source. For both positive autolinks it recorded PR_URL_matches=[], MD_TARGET_matches=[], raw_a_hrefs=[]. Real renderer results independently showed valid clickable links. An absolute <https:////github.com/vokerg/everfield/pull/200> is recognized by the PR_URL matcher (non-vulnerable control). Wrong repo/PR/route/origin controls were checked separately, not misrepresented as protected links.

### Minimal runnable reproduction

    from markdown_it import MarkdownIt
    import mistune
    s = '<https:../pull/200>'
    print(MarkdownIt('commonmark', {'html': True}).render(s))
    print(mistune.create_markdown(renderer='html', escape=False)(s))

    // Node 22 browser normalization:
    new URL('https:../pull/200',
            'https://github.com/vokerg/everfield/issues/1').href
    // 'https://github.com/vokerg/everfield/pull/200'

Correction should resolve actual CommonMark autolinks as browser-equivalent first-party PR references without conflating wrong host/repo/PR, code fence/comment and unlinked text, malformed origin, numeric aliases, HTML entity/backslash/encoded-dot cases. It must cover paginated issue title/body/comments and both initial and fresh mocked pre-PATCH checks with zero write requests, including new links introduced between checks.

## Explicit limits and operational integrity

I independently inspected the complete logical source parsing/eligibility/pagination/execute code through the exact GitHub file and reverified issue/PR/file SHA/CI metadata; executed actual Markdown-it, Mistune, Node WHATWG URL and verbatim Python source-pattern/HTMLParser probes. However, the exact full 1,733-line module could not be mounted or imported into the isolated local Python runtime (raw and API GitHub host DNS blocked), so whole-module references_pr, eligibility, live_open_issue_references and mocked execute(apply=True) were **not** executed end to end. This report does **not** certify full security CLEAN or independently executed full source suite. Deterministic missing parsing gates, confirmed independently by real rendering and browser URL behavior, are sufficient for the narrowly stated adverse MAJOR. No live --apply, PATCH, PR closure or actual GitHub mutation. The unavoidable non-atomic GET/PATCH gap is acknowledged.

**Mandatory next route:** exactly one bounded correction of existing frozen source PR #1805, on a new owned branch; preserve all frozen predecessor blobs, change only correction script and own handoff, exact-final-head read-only CI SUCCESS and write-capable job SKIPPED; then a **different genuinely independent full-module security reviewer**. This report's review-only draft PR must NEVER merge. Even a later CLEAN is not integration authority; only separately claimed owner-authorized, current-main-compatible expected-head SQUASH-only NONCANONICAL source publication may integrate. No canon, gameplay, implementation readiness, engine, production or release authority.
