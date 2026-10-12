# Issue #1710 — genuinely distinct mandatory PR-retirement security review

**Disposition: CHANGES_NEEDED — 0 BLOCKER, 1 MAJOR FSR-1710-M01, 0 correction-requiring MINOR.** Security review **rejects** frozen Issue #1707 / DRAFT PR #1709. The author tests are green but omit an active-reference bypass. Reviewer-only draft/report are provenance, never integrable. No live `--apply`, PATCH, PR close, main mutation or implementation/canonical/production approval.

## Exact sources and independent authority
- Canonical program: Issue #1147 unedited terminal #5675066392, `docs/planning/PLANNING-PROGRAM-v1.md` blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation `87c85cecfa9a2ffa464c4b36816a138bf41441af`; source review main `a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`.
- Producer #1707 sole valid owner CLAIM #6131364086 at `2026-10-12T19:41:33Z`, in-lease `STATUS(REVIEW_READY)` #6131423081 at `19:45:24Z`. Original source #1700 and distinct negative predecessor reviewer #1705 (`REVIEW_STATUS(CHANGES_NEEDED)` #6131337677 / FSR-1705-M01) frozen. Reviewer #1710's independent first unedited CLAIM #6131487608 at `2026-10-12T19:49:39Z`, actor `frontier-distinct-retirement-markdown-security-1710-gpt6-20261012-2150-cph-01`.
- Exact source OPEN/DRAFT PR #1709, head `c5d1a94122ca8a97430a0bbf4e3be66438f5f520`, exactly 3 ADDED paths, independently read via GitHub changed-files API: `tools/planning/retire_negative_review_prs.py` blob `ee76f90ba782848e412bf7e0f8ad80936bdc152e`, byte-identical inherited workflow `.github/workflows/retire-negative-review-prs.yml` blob `e141fffcbb95c02fa215ffec3c403e0e93d1fc90`, own producer handoff `docs/planning/handoffs/issue-1707.md` blob `dd793d26879b008eeedd8e2ff116209a4bce2291`.
- Hosted source Actions run [#38299568763](https://github.com/vokerg/everfield/actions/runs/38299568763) at exact head completed SUCCESS, compiled self-test job #114978900722 SUCCESS and mutating job #114978955852 SKIPPED. Authored coverage is not independent security acceptance.
- Independent reviewer read exact source matcher lines 96–153, issue active-reference consumer around 226–248 and `execute(apply=True)` initial/second-pass scan around 418–460. Executed a stand-alone Python 3 reproduction of the frozen source's exact `PR_URL` regular expression and `references_pr` function logic against PR #200. The source comment prose was omitted in the test harness; operational matcher statements were preserved. **Not** a claim that the full 891-line module, complete `eligibility` fixtures or `execute` were imported or exercised independently. The caller paths were inspected statically and their shared predicate defect is deterministic. Review is negative on this demonstrated finding alone; it does not certify all other gates.

## FSR-1710-M01 — Markdown-emphasized first-party PR URLs bypass the reference veto (MAJOR)

In `tools/planning/retire_negative_review_prs.py` exact source blob `ee76f90...`, `PR_URL` at lines 96–99 captures all nonexcluded bytes including Markdown `*`, `_` and `|`. `references_pr` at lines 117–151 strips only trailing `.,;!:` then compares the URL path's PR segment *exactly* with `200`, `200.diff`, or `200.patch`. As a result, Markdown formatting attached to a canonical, real URL is misconstrued as part of the PR number, even though the open issue explicitly contains an actionable first-party reference.

Independent runnable Python regression (PR #200, repo `vokerg/everfield`):

| Actual open-issue title/body/comment text | Observed `references_pr(text,200)` | Required storage safety |
| --- | --- | --- |
| `https://github.com/vokerg/everfield/pull/200` | True | veto |
| `http://github.com/vokerg/everfield/pull/200` | True | veto |
| `//github.com/vokerg/everfield/pull/200` | True | veto |
| `**https://github.com/vokerg/everfield/pull/200**` | **False** | **veto** |
| `*https://github.com/vokerg/everfield/pull/200*` | **False** | **veto** |
| `__https://github.com/vokerg/everfield/pull/200__` | **False** | **veto** |
| `https://github.com/vokerg/everfield/pull/200|` (Markdown table boundary) | **False** | **veto** |
| `[review](https://github.com/vokerg/everfield/pull/200)` | True | veto |
| `https://github.com/vokerg/everfield/pull/2000` | False | unrelated |
| `https://github.com/vokerg/everfield/issues/200` | False | unrelated |
| `https://github.com/vokerg/other/pull/200` | False | unrelated |

Example actual regex match for bold Markdown: `https://github.com/vokerg/everfield/pull/200**`. The parsed numeric URL path segment is `200**`, not `200`. The bare-URL and HTTP fixes pass, showing this is specifically a new Markdown delimiters bypass rather than a repeat of FSR-1705-M01.

**Real closure impact:** `eligibility` lines ~226–248 tests the result against every complete live open-issue title/body and loaded comment and returns ineligible only if `references_pr` returns True. `execute(apply=True)` calls the same function for its first and immediate fresh pre-PATCH snapshot. An otherwise proven aged, rejected reviewer-only draft can therefore remain eligible for retirement even when the live open issue expressly identifies the PR via bold or italic Markdown. The re-read cannot repair a deterministic missed reference. **No live mutation was tested**, and the GitHub GET/PATCH interval remains unavoidably non-atomic.

## Acceptance boundary and required correction
- One and only one bounded mandatory successor: [Issue #1712](https://github.com/vokerg/everfield/issues/1712), **blocked until** the immutable negative reviewer terminal below and exact reviewer-only OPEN/DRAFT PR exists. Do not modify/rewrite the frozen source #1707, predecessor sources or any reviewer-only branch.
- A new source actor must preserve direct HTTPS/HTTP/protocol-relative web/API references, :443/.diff/.patch, encoded paths, complete issues/comments, first-winning owner/6h lease, negative reviewer-only head/report authentication, 72h grace, no unsafe GitHub API PATCH, and deterministic no-reference positives. Correct Markdown delimiting without accepting attacker-host/foreign-repo/PR number lookalikes.
- Independent **actual full-module** positive/negative fixtures are required in remediation, especially active issue title/body/comments and mocked `execute(apply=True)` with changed comment only in second snapshot, **zero PATCH**; full authored exact-final-head CI with mutating job SKIPPED; another distinct mandatory independent adversarial security review before separate owner-authorized current-main-compatible SQUASH-only NONCANONICAL integration.
- Never treat this negative report as permission to integrate, canonicalize, or close any live PR. Rejected historical reviewer-only DRAFT PRs remain stored until the dedicated security-reviewed retirement source is separately published under canonical authority.
