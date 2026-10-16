# Independent security review of corrected retirement PR #1789 (Issue #1790)

**Disposition: CHANGES_NEEDED.** 0 BLOCKER; **1 MAJOR FSR-1790-M01**; 0 correction-requiring MINOR. This is genuinely separate reviewer execution from the #1788 source-author episode. This is a negative bounded security finding, **not** comprehensive full-module CLEAN certification. This reviewer-only evidence is NOT integrable and confers no source integration, live retirement, production, or canonical authority.

## Frozen identities and gates

- Current main at claim: 7da4c2d50412fe134c8632264908560b8b7995ce (no drift on immediate claimant recheck).
- Canonical Planning Program v1: Issue #1147 unedited binding #5675066392, program blob fd4cf1119c3f86acc3af620024eea72235e81ce4; activation 87c85cecfa9a2ffa464c4b36816a138bf41441af is ancestor of main (GitHub compare: 152 ahead / 0 behind).
- Producer Issue #1788: sole winning CLAIM #6200549253, GitHub created_at 2026-10-15T19:29:40Z; unedited terminal STATUS(REVIEW_READY) #6200656618, created_at 2026-10-15T19:35:32Z, within the six-hour ownership generation.
- Existing source PR #1789: OPEN/DRAFT, base main@7da4c2d50412fe134c8632264908560b8b7995ce, exact HEAD d89cc524e7aece029246e3670a121d4ae8b9e810, 13 changed paths. Source blob tools/planning/retire_negative_review_prs.py@bd2e1e28c2ea52ca5fee0f5001fd6ab5dd40c606; source handoff blob c6440a022a1354bd4c669ebfab00059700af7d71. All other eleven inherited protected paths individually checked against exact frozen Git tree SHAs: MATCH.
- Hosted exact-head run #38794980778 completed SUCCESS. Read-only self-test job #116628878743 SUCCESS. Write-capable retire job #116628942623 SKIPPED. Authored CI is not independent security review.
- Reviewer Issue #1790 first and sole unedited CLAIM #6210843821, GitHub created_at 2026-10-16T07:56:49Z, session existing-pr-distinct-retirement-security-review-1790-gpt6-20261016-prg-01. Current main/source PR were unchanged immediately after claim; reviewer branch planning/issue-1790 created from exact main.
- Old source #1785 and predecessor security reviewer-only PR #1787 remain frozen; they are never merge authorized.

## FSR-1790-M01 (MAJOR): HTML-decoded closing delimiter evades active-PR reference veto

**Impact.** A GitHub issue body, issue title, or comment can contain a genuinely clickable relative Markdown link to a live reviewer PR but the retirement reference detector misses it. Both initial scan and fresh pre-PATCH scan in execute(apply=True) call the same references_pr parser through eligibility, so the error can permit unsafe PR closure if every other retirement gate passes. This is distinct from repaired backslash-escaped closing parentheses (FSR-1786-M01).

**Exact frozen source defect.** At tools/planning/retire_negative_review_prs.py lines 172-184, references_pr applies html.unescape(text) into raw_markdown **before** the inline Markdown destination delimiter scanner. Line 263 iterates RELATIVE_MD_LINK_TARGET against that already-decoded copy. Lines 269-288 terminate on the first unescaped unmatched right parenthesis; they recognize a backslash escape but cannot distinguish an HTML character reference that *was not* a delimiter in the original CommonMark source. The parser consequently mistakes HTML-entity-derived literal path data for the closing Markdown delimiter, contrary to actual CommonMark destination parsing. The absolute PR_URL and literal #N readers do not catch this witness.

**Positive witness:**

    [review](../a&#41;b/../pull/200)

Both markdown-it-py 4.0.0/MarkdownIt and Mistune 3.2.1 independently rendered the linked destination as:

    <a href="../a)b/../pull/200">review</a>

Node 22 WHATWG new URL('../a)b/../pull/200', 'https://github.com/vokerg/everfield/issues/1') resolves to:

    https://github.com/vokerg/everfield/pull/200

But the frozen scanner takes the entity-decoded form [review](../a)b/../pull/200), finds the first right parenthesis at zero nesting depth, and reduces destination to **../a**; its final path cannot match /vokerg/everfield/pull/200. The full detector therefore has no matching absolute authority, literal #200 or surviving relative PR route on this witness. The scoped independent reproduction re-executed the exact source inline-delimiter scanning logic on the affected strings. This demonstrates a deterministic false negative on the exact frozen source code path.

**Independent controls:** source [review](../a\\)b/../pull/200) remains intact as ../a)b/../pull/200 under the corrected backslash scanner (FSR-1786-M01 case). Numeric hexadecimal &#x29; also renders a literal right parenthesis; both markdown-it and Mistune resolve to the target same-repo PR. A wrong target ../pull/201 remains /pull/201 and must not veto retirement of PR #200; a foreign-origin link must remain excluded. The entity witness does **not** rely on a live GitHub PATCH or production retirement.

**Suggested narrowly scoped correction:** perform CommonMark structural destination extraction from original un-decoded Markdown text, keeping HTML character references and backslash-escaped punctuation as destination data until the true closing delimiter has been found; **then** decode entity/escape data for strict WHATWG-equivalent first-party URL/path/PR validation. Preserve root-relative, reference-definition, LF/CRLF, escaped-parenthesis, absolute/protocol-relative URL, Unicode host, encoded-dot, numeric alias, .diff/.patch and foreign/wrong-PR tests. Independently test initial and late/fresh pre-PATCH veto with zero PATCH, plus 72-hour candidate, invalid owner, pagination and error controls. No relaxed blocker policy, no blanket foreign-link veto.

## Validation boundary and limitations

- **Independently executed:** markdown-it-py / Mistune rendering on the exact hostile Markdown, positive escaped-backslash control, negative wrong-number target; Node 22 WHATWG URL resolution; exact frozen-source relative destination scanner control flow reproduced in a targeted Python harness.
- **Inspected:** exact complete 1,490-line source module, key references_pr/eligibility/live_open_issue_references/execute control flow; immutable source Git blob and 13-file tree; CI run/job status; source owner and reviewer ownership GitHub API comments and server timestamps.
- **Not independently executed:** importing all 73 KB of the exact frozen source module, real/mock paged execute(apply=True) end-to-end, exhaustive cold-start 72-hour/ownership/page/race controls. Hosted author full-module self-test SUCCESS does not fill that distinct-review gap. Do not claim independent full-module PASS/CLEAN. The reproducible security-negative scanner evidence is sufficient for **CHANGES_NEEDED**, not a positive certification.
- **No mutations:** no live --apply, API PATCH/closure, source branch edits, source PR review approval, previous reviewer edits, main integration, canonicality or production activation. GitHub GET-to-PATCH non-atomic residual race remains a separate documented limitation.

## Disposition and required next route

**CHANGES_NEEDED: 0 BLOCKER / 1 MAJOR FSR-1790-M01 / 0 correction-requiring MINOR.** Retain existing source PR #1789 OPEN/DRAFT/frozen and never integrate it on its present security evidence. Materialize **one bounded corrective continuation of this existing source-PR chain**, correcting only the active retirement source module while preserving frozen inherited blobs and the separately scoped successor handoff. Require exact-head hosted full self-test SUCCESS and mutating job SKIPPED, then a new genuinely distinct independent *full-module* adversarial review before any separately owner-authorized expected-head/current-main-compatible **SQUASH-only NONCANONICAL** source integration. This reviewer-only PR is NEVER MERGE; no review or producer activity grants live --apply/PATCH, readiness, engine, gameplay, canonical, release or production authority.
