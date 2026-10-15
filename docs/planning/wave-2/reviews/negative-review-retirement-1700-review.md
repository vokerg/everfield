# Required independent adversarial security review — retirement source #1700 / PR #1704

**Mission:** `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-04-REV-01`  
**Reviewer Issue / first sole claim:** #1705 / GitHub immutable comment #6131213868 at 2026-10-12T19:32:06Z  
**Reviewer actor:** `frontier-independent-retirement-port-review-1705-gpt6-20261012-2132-cph-01`  
**Disposition: CHANGES_NEEDED — 0 BLOCKER, 1 MAJOR (FSR-1705-M01), 0 correction-requiring MINOR.** No source change, live --apply, or PR closure was performed.

## Exact frozen provenance, separation, current-main and hosted evidence

- Canonical Planning Program v1: Issue #1147 unedited schema-3 binding comment #5675066392; `docs/planning/PLANNING-PROGRAM-v1.md` Git blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`; activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`; current main at reviewer claim/inspection `a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`.
- Producer #1700 valid first CLAIM #6131125426 (2026-10-12T19:26:34Z, same unedited update), followed by later **losing** CLAIM #6131130185 (19:26:52Z). Genuine first owner #6131125426 published in-lease source `STATUS(REVIEW_READY)` #6131197911 (19:31:05Z), exact source `planning/issue-1700` OPEN DRAFT PR [#1704](https://github.com/vokerg/everfield/pull/1704) HEAD `e1e673f6690dd1e285752cdc00bd0b216decd5db` -> `main@a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`. This is NOT independent acceptance or merger authority.
- PR exact 3 added allowlisted paths: `tools/planning/retire_negative_review_prs.py` blob `a7fbe811d440b86abeaab364ea7b4b6f1c7458b7`; byte-identically inherited `.github/workflows/retire-negative-review-prs.yml` blob `e141fffcbb95c02fa215ffec3c403e0e93d1fc90`; producer handoff `docs/planning/handoffs/issue-1700.md` blob `c5ae2f2ae2b9b80971a49ef2c6af3858659b1f2d`. Frozen earlier source #1693 PR #1696 HEAD `cb3c41aa82775e02066c99d4a901c9653a97c63f`, mandatory prior negative reviewer #1697 terminal #6131045146 and review-only PR #1701 HEAD `8b01dd3e84b993d3748a7e9c0f2b44b9002b84e2` remain untouched. This reviewer did not author any #1700 source or earlier reviewer packet; a prior losing contender claim on #1693 created no code ownership and no source mutation.
- Frozen hosted exact-source-HEAD GitHub Actions [run #38297961451](https://github.com/vokerg/everfield/actions/runs/38297961451): `pull_request`, completed **SUCCESS**, `self-test` job #114973555625 **SUCCESS** (exact event HEAD checkout, PyYAML install, Python compile + self-test), mutation-capable `retire` job #114973612259 **SKIPPED**. Green **authored** fixture execution cannot replace a genuinely independent security review.
- Reviewer independently inspected the 754-line actual frozen script's `StrictLoader`, `operational`, `timestamp`, `PR_URL`, `references_pr`, `eligibility`, `paged`, `live_open_issue_references`, `execute` and embedded test corpus, plus exact workflow, PR path/blobs, GitHub PR/issue claim/terminal created_at and job metadata. Ran independent Python on the exact **verbatim copied** source `PR_URL` and `references_pr` predicates and an exact-location active-issue loop from `eligibility`. This was **not** a full imported 754-line source module test or a live GitHub mutating dry-run, and does not claim it was. The independent code-level negative is deterministically shown below.

## FSR-1705-M01 — MAJOR: HTTP-upgraded and protocol-relative PR hyperlinks evade the live-reference veto

**Mandatory safety contract:** a negative reviewer-only draft must not be retired while **any** currently open issue directly references that PR in title, body or fetched comment, regardless of whether the open issue is in remediation. The source aims to cover actual first-party link forms, but `tools/planning/retire_negative_review_prs.py` at line ~96 sets:

```python
PR_URL = re.compile(r"https://[^\s<>\[\](){}\"'\x60]+", re.IGNORECASE)
```

The subsequent `references_pr(text, number)` only scans `PR_URL.finditer(text)` and the literal `#NUMBER` regex. Thus a human-clickable full **HTTP** GitHub PR URL is absent from both iterators. GitHub's known HTTP-to-HTTPS redirection/HSTS means `http://github.com/vokerg/everfield/pull/200` directly links the **same** review PR as its HTTPS form. Public documentation records `http://github.com` 301 redirect to `https://github.com/` and GitHub HSTS header: [GSA HTTPS/HSTS analysis](https://github.com/GSA/https/blob/master/pages/hsts.md). The same omission exists for the first-party API HTTP variant and Markdown's browser-resolvable protocol-relative `[review](//github.com/vokerg/everfield/pull/200)`; a scheme-relative link in an HTTPS GitHub issue resolves to HTTPS GitHub.

**Independent exact-predicate Python falsification** with `REPO = "vokerg/everfield"`, candidate `number=200`:

| Exact first-party direct-reference text in active issue | Source `references_pr(...,200)` | Required |
|---|---:|---:|
| `http://github.com/vokerg/everfield/pull/200` | **False** | True |
| `http://api.github.com/repos/vokerg/everfield/pulls/200` | **False** | True |
| `[review](//github.com/vokerg/everfield/pull/200)` | **False** | True |
| `https://github.com:443/vokerg/everfield/pull/200` | True | True |
| `https://api.github.com:443/repos/vokerg/everfield/pulls/200.patch` | True | True |
| `https://github.com/vokerg/everfield/pull/200.diff` | True | True |
| `https://github.com/vokerg/everfield/pull/2000` | False | False |
| `https://github.com.evil.test/vokerg/everfield/pull/200` | False | False |
| `https://github.com/vokerg/everfield/issues/200` | False | False |

For each of the first **three** missed reference forms, independently invoked the source's exact active-issue decision shape against a fully populated open Issue #300 with one existing comment, placing that URL **separately in (a) title, (b) body, and (c) fetched `live_comments[0].body`**. All **nine** cases returned **no veto**, while each location holding a valid HTTPS :443 + .patch URL returned a veto. This is not a mere theoretical class gap: one adversarial active issue with no `#200` literal, just an HTTP or protocol-relative link, is sufficient to let the current `eligibility` consider an otherwise genuinely negative, 72h-aged, two-file reviewer-only PR **eligible**. `execute(apply=True)` immediately rereads the SAME `references_pr` predicate in the fresh pre-PATCH snapshot, so it cannot repair this persistent false-negative. The residual last-millisecond non-atomicity of GitHub GET/PATCH is a separate accepted limitation; it does not excuse an identical failing predicate on two scans.

**Minimal independent reproduction with the exact frozen predicate:**

```python
# Copy source PR #1704's PR_URL/references_pr verbatim (lines 96–145).
assert references_pr("Keep https://github.com:443/vokerg/everfield/pull/200.patch", 200)
assert not references_pr("Keep http://github.com/vokerg/everfield/pull/200", 200)
assert not references_pr("Keep http://api.github.com/repos/vokerg/everfield/pulls/200", 200)
assert not references_pr("[review](//github.com/vokerg/everfield/pull/200)", 200)
# These three NOT clauses describe the current defect; after repair every
# first-party direct-reference case should instead assert True.
```

No actual otherwise eligible reviewer PR was closed. No repository API GET/PATCH atomicity, independent imported-module CI, or real HTTP redirect test was asserted from this predicate exercise. Bounded correction should add a precise fail-closed handling of first-party `http://` and protocol-relative `//` forms (without misclassifying attacker domains or foreign repositories), and exercise each at issue title/body/comment plus changed-second-snapshot mocked `execute(apply=True)` zero-PATCH.

## Other frozen gates independently checked

The source positively corrects the predecessor #1697 `FSR-1697-M01`: it parses `url.hostname` separate from `url.port`, admits `:443` and preserves hard numeric segment boundaries including `.diff/.patch`. The live issues are loaded with bounded full pagination/count checks and comment IDs are de-duplicated; malformed API structure fails with `RuntimeError`, rather than permitting optimistic retirement. `eligibility` restricts to owner-authored same-repo, same-task-branch, unmerged DRAFT PR with exact two newly added reviewer files, issue contract mission/report identity, closed/completed reviewer Issue, single first-valid CLAIM, immutable negative `REVIEW_STATUS(CHANGES_NEEDED)` linked to exact PR HEAD and 6-hour lease, minimum 72-hour terminal age, and no later operational claim or status. The source's hosted test exercises a mocked two-pass PRE-PATCH changed-HTTPS-link veto and skips mutating PR job. These improvements cannot cancel FSR-1705-M01's direct-reference false-negative.

Review limitation: the authoring source self-test passing is evidence of covered HTTPS variants, not evidence that it detects omitted HTTP/scheme-relative variants. Requiring a negative review issue to be GitHub-closed/completed can be highly conservative but is not itself authorization to add optional review, forcibly close source issues, or bypass a currently active reference. No new canonical content, gameplay, owner integration or PR-readiness fact is implied.

## Disposition and mandatory single successor

**CHANGES_NEEDED — 0 BLOCKER, 1 MAJOR FSR-1705-M01, 0 correction-requiring MINOR.** The reviewer-only DRAFT PR for Issue #1705 must remain OPEN/DRAFT/UNMERGED, forever nonintegrable. Frozen corrected source #1700 PR #1704 remains OPEN/DRAFT/UNMERGED and **NOT** independently security-approved; previous sources/reviewers remain frozen.

Exactly one bounded mandatory remediation Issue **#1707** has been created, blocked until this exact reviewer terminal. It is authorized to repair only first-party HTTP-upgraded/protocol-relative link veto in the own source file, preserve inherited workflow byte-identically and add own handoff. After hosted exact-final-HEAD read-only CI with mutation skipped, owner `STATUS(REVIEW_READY)` and a **genuinely different required independent adversarial code/security review** must occur. A clean result can unlock only *separately owned and explicitly authorized*, current-main-compatible expected-HEAD **SQUASH-only NONCANONICAL** source integration; no live --apply, PR closure, release, gameplay, engine, content, production, or canonicalization authority exists now.
