# Issue #1784 — FSR-1782-M01 bounded correction and handoff

## Frozen authority

Current main `7da4c2d50412fe134c8632264908560b8b7995ce`, Issue #1147 canonical binding #5675066392, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation `87c85cecfa9a2ffa464c4b36816a138bf41441af`. Original #1784 CLAIM #6188911555 expired at 2026-10-15T15:28:42Z without renewal or terminal. Sole STALE intent #6199478774 and winning RECOVER #6199483999 adopted the untouched branch. Source Issue #1780 OPEN/DRAFT PR #1781 HEAD `2db5c8eb4fa1877358986950113d7b3ba9f6477a`, script blob `eaea88e3acd63c2660058e7b5f2d1f81d50b090b`. Required independent adverse review #1782 terminal #6188803569; reviewer-only DRAFT PR #1783 must never merge.

## Scope and correction

Inherit exactly ten frozen non-script source file blobs without changes; replace only `tools/planning/retire_negative_review_prs.py` and add this handoff. The previous relative CommonMark destination scanner stopped at `(` even though balanced `(z)/..` is a valid browser path. Now capture a full non-whitespace non-angle target and, only for inline Markdown destinations, cut at the **first unmatched** close delimiter `)`, retaining balanced and nested path parentheses. Reference definitions remain newline-delimited. The origin/repo/exact PR route, WHATWG-style ordered dot, unsafe-percent, port, IDNA, decimal alias and lease/grace checks remain unchanged.

New source `self_test` positives cover balanced inline, nested, root-relative, LF/CRLF, reference-definition, aliases and `.diff`/`.patch`; negatives cover foreign host, another repo, PR #201, PR #2000, wrong path/number. Fixtures exercise `references_pr`, title/body/comment `eligibility`, actual mocked `live_open_issue_references`, and both early and fresh-before-PATCH mocked `execute(apply=True)` with zero real network mutation. Independent read-only Python 3 + markdown-it-py 4.2.0 URL oracle executed for representative targets and wrong-number controls; **this is not an independent full-module review**.

## Checks and next route

At writing, hosted exact-final-head `python3 -m py_compile` and `--self-test` CI pending, and write-capable `retire` must show SKIPPED. Do not publish owner `STATUS(REVIEW_READY)` absent exact-final-head CI PASS and OPEN/DRAFT PR. After PASS, require one NEW genuinely distinct independent mandatory security review with full-module execution, browser oracle and mocked initial/fresh pre-PATCH zero-PATCH evidence. Never live `--apply`, PATCH/close drafts, self-review, merge reviewer-only evidence, alter prior source, assert canonicality or production authority. Even a CLEAN review is not source integration authority; owner-authorized current-main-compatible **squash-only noncanonical** integration is separate. If CI fails, continue on this same branch within authorized scope and preserve evidence.
