# Mandatory independent security review #1724 — HTML character references

**Disposition: CHANGES_NEEDED — 0 BLOCKER, 1 MAJOR FSR-1724-M01, 0 correction-requiring MINOR.** Negative review of existing source PR #1722, not CLEAN, merge, or live retirement authority.

## Frozen authority and source

- Reviewer Issue #1724 first valid unedited CLAIM **#6132218952**, GitHub timestamp **2026-10-12T20:39:06Z**, separate actor **existing-pr-independent-escaped-link-review-1724-gpt6-20261012-cph-01**, branch **planning/issue-1724** from **main@a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c**; first-winner immediately rechecked.
- Canonical Issue #1147 binding #5675066392; program blob **fd4cf1119c3f86acc3af620024eea72235e81ce4**, ancestor **87c85cecfa9a2ffa464c4b36816a138bf41441af**.
- Producer #1720 CLAIM #6131823266 at 20:12:15Z, immutable owner REVIEW_READY #6131902262 at 20:17:31Z in the six-hour lease. Source PR **#1722 OPEN/DRAFT**, HEAD **d45397e1452561f6d6aede14129e8c2a753036ac**; exact three changed paths confirmed through GitHub. Script **tools/planning/retire_negative_review_prs.py** blob **e55e1d74cb28bae2ded082e872c72ed628cbc587**; unchanged workflow blob **e141fffcbb95c02fa215ffec3c403e0e93d1fc90**; source handoff blob **088bb6afd8651c941ba1045d3ffab9b10da5d4c1**.
- Authored exact-head CI #38303065942 SUCCESS, compile/full module self-test #114990428420 SUCCESS, mutating job #114990483554 SKIPPED. Not independent security acceptance.

## FSR-1724-M01 (MAJOR) — live CommonMark HTML-entity PR links evade the reference veto

Source **references_pr(text, number)** scans raw Markdown through the frozen PR_URL regex and only normalizes backslash-escaped forward slashes. In CommonMark links, **HTML character references** within the URL destination instead decode to a first-party clickable GitHub PR link. Exact source predicate returns false, even though MarkdownIt 4.2.0 and Mistune 3.2.1 both output the real GitHub PR href.

I retrieved the **actual frozen 903-line, 42,790-character Python script** at exact HEAD through GitHub, independently ran a **verbatim isolated copy** of the source PR_URL / references_pr Python decision path with five attack variants and three controls, and independently rendered every variant in both Markdown engines. These are executed results, not merely hypothetical encodings:

| Raw Markdown URL destination | Rendered destination in both engines | references_pr(raw, 200) |
| --- | --- | --- |
| https://github&#46;com/vokerg/everfield/pull/200 | https://github.com/vokerg/everfield/pull/200 | **False (bypass)** |
| https://github.com/vokerg/everfield/pull&#47;200 | https://github.com/vokerg/everfield/pull/200 | **False (bypass)** |
| https&#58;&#47;&#47;github.com/vokerg/everfield/pull/200 | https://github.com/vokerg/everfield/pull/200 | **False (bypass)** |
| https://github.com/vokerg/everfield/pull/20&#48; | https://github.com/vokerg/everfield/pull/200 | **False (bypass)** |
| https://github.com/vokerg/everfield/pull/200&#63;tab=files | https://github.com/vokerg/everfield/pull/200?tab=files | **False (bypass)** |
| https://github.com/vokerg/everfield/pull/200 | same PR #200 | **True (positive control)** |
| https://github.com/vokerg/everfield/pull/2000 | distinct PR #2000 | **False (boundary control)** |
| https://foreign.example/vokerg/everfield/pull/200 | foreign host | **False (foreign control)** |

Every tested destination above was enclosed inside a conventional [review](URL) Markdown link. Emitted anchor href values were inspected directly and matched between MarkdownIt and Mistune.

**Production decision path inspected:** frozen eligibility scans each fully loaded open-issue title/body/comment with this predicate; execute(apply=True) invokes the *same eligibility* for both initial screening and a freshly reloaded second pre-PATCH issue/comment snapshot. An issue linking with HTML entities can escape **both** safeguards, making otherwise eligible reviewer-only PR closure unsafe despite 72-hour grace, strict task identity, authenticated source head, valid terminal and recheck.

## Precise independent execution limits

- **Independently executed:** exact extracted source URL regex and references_pr Python function (five bypass variants, three controls); real MarkdownIt 4.2.0 and Mistune 3.2.1 rendering and href inspection; no network mutations.
- **Read-only inspected but NOT independently executed:** complete source module import, full eligibility / live_open_issue_references / execute(apply=True) mocked execution, complete reviewer terminal YAML and grace tests, all comprehensive self-tests. Source-authored CI is not a substitute. This negative finding is sufficient to require correction but **not** a claim of complete security review or zero other vulnerabilities.
- **No** live --apply, GitHub PATCH, issue/PR close, source branch change, main integration, or source/reviewer self-merge. The GET-to-PATCH interval remains non-atomic, regardless of this particular defect.
- The reviewer-only evidence branch owns strictly its own two NEW documents; original source #1722 and predecessor review PRs remain untouched.

## Mandatory successor and authority boundary

**Exactly one** bounded remediation successor **Issue #1726** now exists, **BLOCKED until** reviewer-only exact-head DRAFT PR and immutable in-lease REVIEW_STATUS(CHANGES_NEEDED). A distinct producer must inherit frozen existing source PR #1722 and correct only the script plus its own handoff, preserve workflow and inherited files exactly, cover HTML named/numeric references (including combinations with backslash escapes), first-party strict hostname/repo/PR boundaries, issue title/body/all loaded comments, first and late pre-PATCH zero-PATCH mocks using the **actual full corrected module**, all previous cases, exact-head hosted CI with mutating job SKIPPED, new distinct independent security review, and only if CLEAN separately authorized squash-only NONCANONICAL source publication. This reviewer-only PR must **never merge**. No canonical, gameplay, engine/readiness, release or production authority.