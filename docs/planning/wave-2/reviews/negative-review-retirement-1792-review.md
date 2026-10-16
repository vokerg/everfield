# Independent required security review — source Issue #1792 / draft PR #1793

**Disposition: CHANGES_NEEDED. 0 BLOCKER, 1 MAJOR (FSR-1794-M01), 0 correction-requiring MINOR.** This is a security-negative result, not a full-module CLEAN certification and not integration/retirement authority.

## Authority, independence and immutable source

- Reviewer Issue #1794, genuinely distinct execution `existing-pr-distinct-html-anchor-security-review-1794-gpt6-20261016-prg-01`, first winning immutable CLAIM `6211280155` (GitHub server `2026-10-16T08:22:14Z`), branch `planning/issue-1794` from `main@7da4c2d50412fe134c8632264908560b8b7995ce`.
- Active canonical Planning Program Issue #1147 terminal `5675066392`, program Git blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`; activation `87c85cecfa9a2ffa464c4b36816a138bf41441af` is ancestor of current main (compare: 152 ahead, 0 behind).
- Separate source author/owner Issue #1792 first CLAIM `6211042106` at `2026-10-16T08:08:26Z`; exact owner terminal `STATUS(REVIEW_READY)` `6211125437` at `08:13:44Z`; both unedited and within six-hour lease, no competing source ownership at freeze.
- Existing OPEN/DRAFT source PR #1793, base `main@7da4c2d...`, exact HEAD `dd0afd5de2961eaf1db2e7b8e235da2d9b5bd346`; `tools/planning/retire_negative_review_prs.py` blob `b3d03feab7b74eeca15ea1fd97bf2242ab7fcacd`. Exact changed packet: fourteen paths, twelve protected inherited blobs, corrected module and author handoff `d40e050c19b66cc86426370e7e593f69964841fb`.
- Hosted exact-HEAD GitHub Actions `38872158799`: `completed/success`; read-only `self-test` job `116878549980` `success`; write-capable `retire` job `116878603449` `skipped`. These are source-authored tests, **not** independent security approval.
- Predecessor independent reviewer #1790 negative `6210947527`; predecessor frozen source PR #1789 HEAD `d89cc524e7aece029246e3670a121d4ae8b9e810` and reviewer-only #1791 remain untouched.

## FSR-1794-M01 — raw HTML relative first-party PR anchor omitted (MAJOR)

The frozen source `references_pr(text, number)` has exactly three entry routes: a textual `#N` scanner, `PR_URL` requiring an absolute/protocol-relative authority, and `RELATIVE_MD_LINK_TARGET` requiring a Markdown inline `](...)` or reference-definition opener. It has **no raw HTML `<a href=...>` relative-destination reader**. Because GitHub Flavored Markdown admits raw HTML tags (GFM §6.10), an active issue/comment can retain a clickable relative raw HTML anchor to a reviewer PR while both the initial eligibility and fresh pre-PATCH live-open-issue scans report no reference.

Reproducible issue-body witness, with target reviewer PR #200:

```html
<a href="../pull/200">review evidence</a>
```

Both independent Markdown renderers produce `<a href="../pull/200">review evidence</a>`; Node WHATWG `new URL('../pull/200', 'https://github.com/vokerg/everfield/issues/1').href` gives `https://github.com/vokerg/everfield/pull/200`. But the exact source entry-pattern evaluations are all FALSE: no `#200`, no authority containing `//`, no Markdown opener `](...` or `[label]:`. This is a reachable *false negative*, not an inference from lack of tests. The same `references_pr` is called in both initial and immediate fresh pre-PATCH live-reference vetoes; absent another veto, a real linked reviewer-only draft could be closed. This is narrower than asserting all raw HTML links evade the detector: absolute HTML links still match `PR_URL`.

### Independently executed evidence

Environment: Python, markdown-it-py **4.2.0**, Mistune **3.2.1**, Node **v22.16.0**. A local independent script parsed actual anchor `href`s from both engines, resolved each using Node WHATWG, and reproduced the three **entry predicates from the exact frozen HEAD** (not the source-authored `self_test()`).

| Case (raw issue Markdown) | Rendered href (both engines) | WHATWG resolved path | Frozen scanner entry |
| --- | --- | --- | --- |
| `<a href="../pull/200">review</a>` | `../pull/200` | `/vokerg/everfield/pull/200` | **NONE** |
| `<a href="/vokerg/everfield/pull/200">review</a>` | `/vokerg/everfield/pull/200` | `/vokerg/everfield/pull/200` | **NONE** |
| `<a href="../a/../pull/200">review</a>` | `../a/../pull/200` | `/vokerg/everfield/pull/200` | **NONE** |
| `<a href="https://github.com/vokerg/everfield/pull/200">review</a>` | full URL | `/vokerg/everfield/pull/200` | `PR_URL` YES |
| `[review](../pull/200)` | `../pull/200` | `/vokerg/everfield/pull/200` | Markdown slot YES |
| `<a href="../pull/201">review</a>` | `../pull/201` | wrong target PR #201 | no PR #200 reference |
| `<a href="/vokerg/other/pull/200">review</a>` | root-relative | foreign repository | no same-repo PR #200 |
| `<a href="../notes/readme">review</a>` | `../notes/readme` | ordinary path | no PR route |

Relevant standard: https://github.github.com/gfm/#raw-html ; source inspected from `planning/issue-1792` at exact blob `b3d03f...` around `references_pr`, `PR_URL`, `RELATIVE_MD_LINK_TARGET`, `eligibility`, `live_open_issue_references` and `execute(apply=True)`.

### Scope limitation and risk

This reviewer independently executed both Markdown engines, WHATWG URL resolution, and the source-extracted entry predicates. **The complete 75KB Python module was not imported/executed locally, and neither full `eligibility` nor mocked `execute(apply=True)` was independently executed.** This evidence is sufficient for a specific MAJOR negative outcome, **not** a full-module CLEAN verdict. Neither a real GitHub `--apply`, PATCH/close, nor integration occurred. GitHub's GET/PATCH non-atomic race remains independently relevant even after this bug is corrected.

## Required resolution and authority boundary

One **bounded mandatory corrective continuation of existing OPEN/DRAFT PR #1793** must preserve the frozen 14-file provenance while adding a strict rendered/raw-HTML relative first-party PR href safety veto (including attribute quote/whitespace/entity variants and negative wrong-host/repo/PR controls), with real exact-module initial and fresh mocked pre-PATCH zero-PATCH evidence. It must produce exact-head read-only full-module CI and then another genuinely distinct mandatory **full-module** adversarial security review. Do **not** self-certify CLEAN, alter/merge old source or reviewer PRs, perform live retirement, or integrate any source until separately owner-authorized, current-main-compatible **SQUASH-only NONCANONICAL** integration after independent CLEAN. This reviewer-only report PR is permanently nonintegrable; no canon, gameplay, engine, readiness, release or production authority.
