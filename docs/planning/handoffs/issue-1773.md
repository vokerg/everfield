# Issue #1773 — browser-equivalent first-party PR authority correction handoff

**Mission:** `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-14`.  
**Owner:** first winning unedited schema-3 CLAIM `6187358832` (2026-10-15T07:58:17Z); actor `browser-authority-remediation-1773-gpt6-20261015-cph-01`, branch `planning/issue-1773`, base `main@7da4c2d50412fe134c8632264908560b8b7995ce`. Sole claimant immediately rechecked.  
**Canonical:** Issue #1147 binding `5675066392`, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.

## Prerequisites / strictly frozen inheritance

Mandatory independent reviewer Issue #1772 terminal `REVIEW_STATUS(CHANGES_NEEDED)` `6187205068`, reviewer-only OPEN/DRAFT PR #1774, **never merge**. Two independently supported MAJOR findings `FSR-1772-M01` and `FSR-1772-M02`. Frozen predecessor Issue #1769 owner terminal `6177247211`, source OPEN/DRAFT PR #1771 exact HEAD `1a224210fb402cabfaa2230c9b8521d29f62de85`, script blob `b7aec6e8b5be095dad495623dc3dcf7f345ad92c`, exact-head source CI #38628771703 read-only SUCCESS / mutating job SKIPPED. Frozen source remains unchanged and unmerged.

Exactly **eight unchanged inherited Git blobs** from #1771:

- `.github/workflows/retire-negative-review-prs.yml`: `e141fffcbb95c02fa215ffec3c403e0e93d1fc90`
- `docs/planning/handoffs/issue-1720.md`: `088bb6afd8651c941ba1045d3ffab9b10da5d4c1`
- `docs/planning/handoffs/issue-1726.md`: `904dd95551d79991f546317ae71283891a165dec`
- `docs/planning/handoffs/issue-1738.md`: `ef7a69bafa5949bee8c16f0605340980529b736a`
- `docs/planning/handoffs/issue-1746.md`: `f686b32aaebc387fbcac3d2cf5856853bb17cd54`
- `docs/planning/handoffs/issue-1756.md`: `d2ddd859a277bfdaeb2843aa2ee87b58b5160e54`
- `docs/planning/handoffs/issue-1765.md`: `a74397422eb7ddceabc4b00f3d8d93d20dbf7348`
- `docs/planning/handoffs/issue-1769.md`: `72b4ad4435170e97893b17b0f1b6fd17674853d3`

Only inherited `tools/planning/retire_negative_review_prs.py` is corrected; new script blob `610c923de03d238984a8f5e50af62be43404e0d9`. Only one new path `docs/planning/handoffs/issue-1773.md` is added. Exactly **ten changed paths**, no other source, review, predecessor or main mutation.

## Bounded repair

`references_pr` now normalizes first-party browser-equivalent special-scheme URLs containing three or more authority slashes to two before applying Python URL parsing (`FSR-1772-M02`), preserving the exact scheme/hostname/port/userinfo route boundaries and foreign-origin exclusion. The decoded UTF-8 hostname is IDNA-normalized before exact `github.com`/`api.github.com` comparison so Unicode U+3002/U+FF0E/U+FF61, percent-encoded forms and ASCII equivalents map to actual browser first-party hostnames (`FSR-1772-M01`). Malformed unparseable encodings fail closed.

Adds separate browser-authority positive and genuine negative controls to the complete module self-test, including open issue title, body, comments; page-scanned live issue comments; and both first and second mock `execute(apply=True)` veto loops with **zero mocked PATCH** expected if a live reference exists. Includes web/API, decimal aliases, diff/patch and wrong PR/repo/host/route cases. These are authored assertions; not an independent security approval.

## Required evidence and next step

Publish OPEN/DRAFT exact-head source PR to main and obtain hosted exact final-head `py_compile` + **actual full-module `--self-test` SUCCESS** with mutating retirement job **SKIPPED**. If CI fails, revise only the same allowed script and handoff on this task branch and repeat hosted exact-head CI; do not publish a premature terminal. Reconfirm current main compatible with this base, exact 10 files and eight frozen unchanged blobs, sole owner and six-hour claim lease. Then publish immutable schema-3 owner `STATUS(REVIEW_READY)` with exact head/work/PR/CI identities and a single mandatory **genuinely distinct** next reviewer issue of the frozen source. New reviewer must independently run actual full module with independent WHATWG/Markdown oracles and mock both initial/fresh PATCH scans; source selftest is not a review.

No live `--apply`, PR PATCH/close, reviewer-only merge, source integration, canon, gameplay, readiness, production or release. Even later clean review requires separately authorized then-current-main-compatible **SQUASH-only NONCANONICAL** integration. The reviewer and all predecessors remain frozen. 
