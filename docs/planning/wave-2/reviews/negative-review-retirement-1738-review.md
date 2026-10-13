# Mandatory independent security review of Issue #1738, PR #1742

**Review:** Issue #1743, mission `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-09-REV-01`; genuinely separate from source owner session `existing-pr-escaped-punctuation-remediation-1738-gpt6-20261013-cph-01`. Reviewer sole CLAIM #6138072082 at GitHub 2026-10-13T04:12:58Z; actor `existing-pr-independent-escaped-punctuation-review-1743-gpt6-20261013-cph-01`. Baseline main `a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`. Canonical Issue #1147 binding #5675066392 / program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation `87c85cecfa9a2ffa464c4b36816a138bf41441af`.

**Verdict: CHANGES_NEEDED — 0 BLOCKER, 1 MAJOR (FSR-1743-M01), 0 correction-requiring MINOR.** This is NOT a clean review, integration authority, or proof that all other failure modes are excluded.

## Frozen evidence and scope

- Source Issue #1738 first CLAIM #6137872988; immutable owner `STATUS(REVIEW_READY)` #6137936343, exact OPEN/DRAFT PR #1742 HEAD `9f83051b6b34187a4a0209a7daf03cdb73891082`, 5 paths. Actual Python blob `tools/planning/retire_negative_review_prs.py` `1d88dc2c7ac2828bfc314b832636a273dad21986`; unchanged workflow `.github/workflows/retire-negative-review-prs.yml` `e141fffcbb95c02fa215ffec3c403e0e93d1fc90`; source handoff `docs/planning/handoffs/issue-1738.md` blob `ef7a69bafa5949bee8c16f0605340980529b736a`. Inherited other handoffs #1720/#1726 remained inherited.
- Source-authored exact-final-head hosted CI #38344252548, read-only `self-test` job #115121877363 SUCCESS, mutation-capable `retire` job #115121907813 SKIPPED. This does not establish independent acceptance.
- Frozen predecessor Issue #1726 / PR #1728 HEAD `c51789012237523d7ac01f70b3e34f10dfc6191e`; distinct CHANGES_NEEDED security review #1729 terminal #6137634646 / reviewer-only PR #1739 HEAD `7c8b3667443479172e5275d74586984e12ac9fdc`, finding FSR-1729-M01. Those branches, source PR #1742 and main were not modified in this review.

## FSR-1743-M01 — first-party relative Markdown links bypass active-reference veto (MAJOR)

Frozen `references_pr(text,number)` performs HTML-entity decoding and CommonMark backslash-punctuation unescaping, checks `#200`, then iterates only `PR_URL` values matching `(?:https?:)?//...` (fully qualified or protocol-relative). It has **no check for same-repository Markdown root-relative or path-relative hyperlink targets**. A real GitHub issue page resolves root-relative `/vokerg/everfield/pull/200` to that PR. URL joining relative `../pull/200` from `https://github.com/vokerg/everfield/issues/1234` yields the same first-party PR.

Both MarkdownIt **4.2.0** and Mistune **3.2.1** independently render the following as clickable `<a href>` links. A Python reproduction containing the exact frozen `PR_URL` and `references_pr` function logic, transcribed from the source blob rather than altering it, returned:

| Active issue Markdown | Frozen predicate `references_pr(text,200)` | Resolved URL from an issue page |
| --- | --- | --- |
| `[review](/vokerg/everfield/pull/200)` | **False** | `https://github.com/vokerg/everfield/pull/200` |
| `[review](../pull/200)` | **False** | same PR |
| `[review](../../everfield/pull/200)` | **False** | same PR |
| `[review](../pull/200.diff)` | **False** | `https://github.com/vokerg/everfield/pull/200.diff` |
| `[review](../pull/200#issuecomment-123)` | **False** | same PR with fragment |
| control `[review](https://github.com/vokerg/everfield/pull/200)` | **True** | same PR |
| nonreference `[review](../pull/201)` | **False** | distinct PR |

Independent executable reproduction:
```bash
python /tmp/everfield_review_1743.py
```
The script imported `markdown_it.MarkdownIt`, `mistune`, `html`, `re`, `urllib.parse` and `string`, used frozen regex and function body, rendered each Markdown link in both engines, extracted MarkdownIt's `href`, resolved it with `urllib.parse.urljoin('https://github.com/vokerg/everfield/issues/1234', href)` and printed predicate result. All five above positive-relative misses reproduced; both controls matched. This isolated reproduction does **not** import or execute the entire frozen module or invoke GitHub.

Actual frozen `eligibility` directly invokes `references_pr` on every active open issue's `title + body` and loaded comments; when it returns false the reference veto does not fire. `execute(apply=True)` calls that same eligibility predicate again after fresh PR, issue, review-comment, file and active-open-issue scans **immediately before PATCH**. Therefore a legitimate live repository-relative link can be overlooked at both protection points, while otherwise-proven negative reviewer-only drafts become eligible for irreversible storage closure. The PR still can be closed only if its separate owner/terminal/age/files conditions pass; this finding does not claim arbitrary PR closure.

## Review limits and required next route

Inspected actual frozen function, consumer and recheck control flow, original five-path scope and hosted CI results; independently executed isolated frozen predicate plus two independent Markdown engines and URL resolution. Did **not** run full module's comprehensive self-test independently, fully import it, execute a mocked `execute(apply=True)`, make GitHub PATCH, close any PR, verify GitHub's exact production Markdown renderer, or claim API GET/PATCH atomicity. The first-party absolute-path witness alone is sufficient for a security correction under browser-resolved anchor semantics; no clean approval is implied.

**Exactly one mandatory bounded successor Issue #1746** materialized for FSR-1743-M01, BLOCKED until this review's unedited in-lease `REVIEW_STATUS(CHANGES_NEEDED)` and exact-head review-only OPEN/DRAFT PR. A later owner must inherit frozen #1742 five-path source packet, modify only retirement script plus its own new handoff, preserve workflow and inherited blobs, add title/body/comment and two-snapshot pre-PATCH positive/negative regressions, and run hosted exact-head read-only CI; then a genuinely distinct new security review. No live `--apply`, closure, merge, canonicalization, production, gameplay or release authority. Review-only PR is permanent nonintegrable provenance.
