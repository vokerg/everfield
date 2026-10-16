# Issue #1769 — ordered WHATWG dot-segment correction handoff

**Mission:** `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-13`.
**Ownership:** first schema-3 CLAIM `6177153290`, branch `planning/issue-1769` from then-main `7da4c2d50412fe134c8632264908560b8b7995ce`; actor `ordered-dot-security-remediation-1769-gpt6-20261014-cph-01`.
**Binding:** Issue #1147 terminal `5675066392`; canonical program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`; activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.

## Frozen source, inheritance and finding

Genuinely distinct independent reviewer #1768 negative terminal `REVIEW_STATUS(CHANGES_NEEDED)` `6177042717` found MAJOR `FSR-1768-M01`; evidence-only reviewer DRAFT PR #1770 **MUST NEVER MERGE**. Frozen corrective source #1765, OPEN/DRAFT PR #1767 exact HEAD `4a529940ff24c10c6295606b42de884999e48d14`, script blob `a80b080dccbed14ed76fc8b8ec8121ded9bb7ca6`.

Exact seven inherited blobs preserved byte-identically from source #1767:
- `.github/workflows/retire-negative-review-prs.yml` `e141fffcbb95c02fa215ffec3c403e0e93d1fc90`
- `docs/planning/handoffs/issue-1720.md` `088bb6afd8651c941ba1045d3ffab9b10da5d4c1`
- `docs/planning/handoffs/issue-1726.md` `904dd95551d79991f546317ae71283891a165dec`
- `docs/planning/handoffs/issue-1738.md` `ef7a69bafa5949bee8c16f0605340980529b736a`
- `docs/planning/handoffs/issue-1746.md` `f686b32aaebc387fbcac3d2cf5856853bb17cd54`
- `docs/planning/handoffs/issue-1756.md` `d2ddd859a277bfdaeb2843aa2ee87b58b5160e54`
- `docs/planning/handoffs/issue-1765.md` `a74397422eb7ddceabc4b00f3d8d93d20dbf7348`

Only original `tools/planning/retire_negative_review_prs.py` is modified (new blob `b7aec6e8b5be095dad495623dc3dcf7f345ad92c`), and this new task handoff is added. No source/reviewer or main branch edits.

## Mechanism of the bounded fix

Prior relative-link detection did `urljoin(base, destination)` and then `browser_path_segments(urljoin_path)`: Python removed unescaped `..` against still-opaque `%2e%2e`, unlike a browser. Now the relative Markdown target's **raw path** is resolved against the GitHub issue **directory**, not first normalized by `urljoin`; a single `browser_path_segments` pass applies unescaped/escaped `.` and `..` in order. Root-relative paths use their original raw root, and `//authority` targets are left to the first-party absolute URL scanner (cannot become local relative paths). Existing malformed/encoded separators, strict origins, numeric aliases, pager, owner, lease, two-snapshot and 72-hour gates are unchanged.

Eight positive ordered-dot cases added (inline/angle/reference, mixed encoding, two levels, root relative, numeric aliases and suffixes), five negative controls for wrong PR/route/repo/foreign origin and harmless encoded filename. All positives run the actual `references_pr` and `eligibility` on title/body/full live comments and are additionally included in `execute(apply=True)` mock first-scan and fresh pre-PATCH loops; added an `live_open_issue_references` mocked paged comment case. Independent Node 22 WHATWG `new URL` URL-resolution oracle confirms the representative positive paths; `urljoin` is not used as expected behavior oracle.

## Remaining required gates and authority

Before valid `STATUS(REVIEW_READY)`: publish exact-head OPEN/DRAFT diff PR to main; verify exactly nine paths, all seven inherited blobs, fresh compatible main, and hosted exact-head `py_compile` + read-only full module `--self-test` **SUCCESS**, mutation job **SKIPPED**. A failure or missing CI is **not** review readiness: remediate on the task branch or preserve HANDOFF/BLOCKED. Then materialize a new genuinely distinct mandatory security review of the frozen exact source. **Do not claim source CLEAN, integration, live --apply/PATCH, closure, canonicality, readiness, production or release.** Even clean review would require separately owner-authorized current-main-compatible **SQUASH-only NONCANONICAL** integration. All reviewer-only PRs MUST NEVER MERGE.
