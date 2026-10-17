# Mandatory independent security review — source #1812 / PR #1814

**Disposition: CHANGES_NEEDED — 0 BLOCKER, 2 MAJOR (FSR-1815-M01, FSR-1815-M02), 0 correction-requiring MINOR.** No security CLEAN, merge, reviewer draft publication or live retirement authorized by source CI or this report.

## Immutable reviewed provenance

- Active canonical Issue #1147 unedited integration binding #5675066392, program blob fd4cf1119c3f86acc3af620024eea72235e81ce4, activation ancestor 87c85cecfa9a2ffa464c4b36816a138bf41441af; exact reviewed main 7da4c2d50412fe134c8632264908560b8b7995ce.
- Independent mandatory review Issue #1815; sole first valid claim #6232541190 (GitHub-created 2026-10-17T09:57:08Z); reviewer session everfield-distinct-full-module-review-1815-gpt6-20261017-01, distinct from #1812 producer and #1807 reviewer.
- Source #1812 sole CLAIM #6232411810, unedited owner STATUS(REVIEW_READY) #6232490263, source OPEN/DRAFT PR #1814 on planning/issue-1812, exact HEAD e7b02c97906e3470e896f03854ed462a40fee23f. Source full module tools/planning/retire_negative_review_prs.py Git blob b0f3ef2361b6d59d366c8fba5491a902851d9834 (1,786 lines). Exact 18 added paths: only module corrected and issue-1812 handoff added atop 16 inherited unchanged predecessor blobs, including unchanged mutating workflow. No source/predecessor files edited in this review.
- Historical independent adverse finding #1807 / terminal #6232390059 / reviewer-only draft PR #1810 head 62282a256ad397d94a338a8ec620369ebf673661 was CommonMark same-scheme angle autolink FSR-1807-M01. #1812 adds angle recognition and source-owned positive/negative assertions.
- Exact source final-head Actions #39022602559 (SUCCESS), read-only self-test job #117367232968 (SUCCESS), mutating retire job #117367260045 (SKIPPED). This is authentic authored-CI evidence, not independent review acceptance.

## FSR-1815-M01 — MAJOR: percent-encoded leading parent traversal bypasses active PR reference veto

A live issue body (or title/comment) containing the ordinary **clickable Markdown inline link**:

    [review](%2e%2e/pull/200)

or a CommonMark reference-definition equivalent:

    [ref]: %2e%2e/pull/200

    [review][ref]

links directly to GitHub PR #200 when rendered on an issue page such as https://github.com/vokerg/everfield/issues/1815. Independently executed markdown-it-py 4.2.0 and Mistune 3.2.1 both emitted an anchor with href="%2e%2e/pull/200" for each form. Independently executed Node v22.16.0 WHATWG URL:

    new URL('%2e%2e/pull/200',
            'https://github.com/vokerg/everfield/issues/1815').href
    // https://github.com/vokerg/everfield/pull/200

The same resolution holds for %2E./pull/200 and .%2e/pull/200, while controls ending in /pull/201, /pull/2000 or /issues/200 resolve to other targets. No PR number appears as a bare #200, no "//" authority is present, no raw HTML a/href tag appears in source, and no '<https:...>' angle autolink exists. Those alternative readers thus cannot supply the missing veto.

**Actual source root cause (tools/planning/retire_negative_review_prs.py, around lines 414–465):** RELATIVE_MD_LINK_TARGET correctly matches the slot and extracts destination="%2e%2e/pull/200"; the inline closing ')' is removed. After html.unescape and backslash normalization, the hard gate:

    if not destination.startswith(("/", "./", "../")):
        continue

drops this valid browser-relative destination **before** browser_path_segments can interpret the percent-encoded first ".." segment. Independently ran the literal source regex and gate in Python 3 with the three positive variants and unencoded ../pull/200 control: all encoded-leading variants reached the reader but all returned starts_allowed=False; the unencoded control was True. The source self-test covers encoded-dot segments only after an explicit prefix ('../issues/%2e%2e', '/vokerg/...') and covers an encoded-leading dot for raw HTML a/href; it omits precisely the encoded-leading Markdown destination case.

**Safety consequence:** eligibility() loops over each fully covered open issue title/body/comment and uses references_pr to veto; execute(apply=True) performs a fresh second eligibility() before PATCH. Both scans call the SAME incomplete predicate. Thus a reviewer-only draft that otherwise satisfies the narrow valid negative terminal, 72-hour grace, exact issue/PR/two-file identities, and current owner proof can still be closed despite an active clickable first-party PR link. This is a conditional source-level bypass, not a claim that GitHub already closed a PR. Source workflow is not on main and was not run in --apply mode.

Severity MAJOR: violates the explicit open-reference preservation invariant and affects both first and last-moment safety checks. No further exploit chain or secret access is claimed.

## FSR-1815-M02 — MAJOR: even-count CommonMark backslashes leave active autolinks invisible

A separate non-operational evidence comment #6232548674 brought forward a second candidate. The **claimed reviewer independently reproduced it** using real markdown-it-py 4.2.0, Mistune 3.2.1, and the actual source-exact regex in Python 3 before accepting it as a separate correction-requiring finding.

For Markdown containing exactly **two literal backslashes immediately before** an angle autolink, both renderers emit a literal displayed backslash **followed by a clickable anchor**; four literal backslashes leave two displayed backslashes plus the same clickable anchor. Single or triple backslashes escape the opening angle and produce no link. Source test vector construction avoiding ambiguity:

    s = '\\' * 2 + '<https:../pull/200>'
    # rendered: one visible backslash followed by <a href="https:../pull/200">

The source regex at about lines 384–386,

    r"(?i)(?<!\\)<(https?:[^<>\s]+)>"

returns **no match for every n=1,2,3,4** leading backslashes; it falsely assumes any immediately preceding backslash escapes the opening angle. Real CommonMark escapes operate on *parity*, so even n=2 and n=4 produce a live automatic link. WHATWG Node 22 resolves its same-scheme href on the issue page to https://github.com/vokerg/everfield/pull/200. The bare-#N, //-authority, raw HTML anchor and Markdown destination readers do not catch this standalone angle token. Both first and immediately before-PATCH scanners reuse references_pr and can therefore miss it.

Falsifying controls executed: n=0 is correctly detected and rendered clickable; n=1 and n=3 render inert angle text and regex rejects; n=2 and n=4 render clickable while regex also rejects. This is a **second independent MAJOR** because it bypasses the exact new autolink correction in source #1812 itself, distinct from the encoded-leading relative Markdown destination M01. No full-module independent execution or real PATCH is claimed.

One bounded successor correction MUST address **both** FSR-1815-M01 and FSR-1815-M02 together: fix browser-relative percent-encoded leading dot segment handling AND CommonMark angle-opening escape parity; include independent equivalent real-renderer positive/negative controls, first and pre-PATCH mocked zero-write scenarios, and a NEW genuinely distinct full-module review. Do not create parallel remediation chains.

## Independent review method, regression gap and limits

Read the actual source's complete functional path: StrictLoader/operational identity, URL/raw-HTML/autolink/relative readers, eligibility's owner/terminal/draft/two-path/72-hour tests, paged open issue/comment scan, execute's initial and fresh pre-PATCH eligibility and source self-test coverage; compared exact file SHA, 18-path GitHub PR file list, main binding and hosted CI job conclusions. Reproduced Markdown rendering and WHATWG browser resolution on an isolated runner, and independently exercised source-verbatim URL-target regex plus the decisive prefix gate. The source-authored full --self-test passed on the hosted immutable PR head. **Did not import/run the entire 1,786-line module independently, did not run complete mocked execute(apply=True), and did not perform any real GitHub PATCH or reviewer PR closure.** The two directly falsifying predicate differentials are enough to reject CLEAN without inventing comprehensive independent execution evidence.

Required joint M01/M02 correction: on a NEW owned continuation of the existing frozen PR #1814, preserve all inherited non-script SHA blobs; correct only the retirement Python module and add the correction issue's own handoff. Apply browser-equivalent relative-path normalization to actual Markdown destinations without treating explicitly foreign authorities as first-party and without false positives on non-link text. Cover percent-encoded first-segment dot variants, even/odd CommonMark autolink escape counts, title/body/comments, reference definitions, first and pre-PATCH mocked zero-write vetoes, wrong-PR/wrong-route/foreign host controls, and exact head source CI before a NEW genuinely distinct mandatory full-module security review. Source #1814 remains OPEN/DRAFT/frozen and NOT integrable pending that review. Even a future CLEAN requires separately owner-authorized current-main compatible exact-head SQUASH-only NONCANONICAL integration.

## Non-goals and remaining boundaries

No live --apply, PR PATCH/close, merge, canonicality promotion, production/factory dispatcher authorization, gameplay/engine/readiness/release decision or self-certified security PASS. GitHub GET-before-PATCH checks also cannot remove the last-millisecond non-atomic race. Reviewer-only artifact/PR must NEVER MERGE.
