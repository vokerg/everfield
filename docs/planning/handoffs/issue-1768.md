# Issue #1768 — independent security review and negative handoff

**Mission:** `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-12-REV-01`.
**Reviewer branch:** `planning/issue-1768` from main `7da4c2d50412fe134c8632264908560b8b7995ce`.
**Ownership:** sole schema-3 CLAIM comment `6176972844`, actor `independent-whatwg-security-review-1768-gpt6-20261014-cph-01`.
**Canonical binding:** Issue #1147 `5675066392`, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation SHA `87c85cecfa9a2ffa464c4b36816a138bf41441af`.

## Disposition and outputs

Independent security result **CHANGES_NEEDED**: 0 BLOCKER, **1 MAJOR FSR-1768-M01**, 0 correction-requiring MINOR. Complete evidence is solely in `docs/planning/wave-2/reviews/negative-review-retirement-1765-review.md`; this handoff is the second and final reviewer-owned path.

Frozen source #1765 PR #1767 stays OPEN/DRAFT unchanged at exact HEAD `4a529940ff24c10c6295606b42de884999e48d14`, script Git blob `a80b080dccbed14ed76fc8b8ec8121ded9bb7ca6`. Owner negative predecessor #1761, corrective source #1765 and its CI were checked. Read-only run #38455070860 job #115495578556 SUCCESS; mutating job #115495652976 SKIPPED.

**Finding:** in relative Markdown destinations, raw Python `urljoin` removes ordinary `..` segments before `browser_path_segments` removes browser-escaped `%2e%2e` segments. These ordered transformations do not commute. Exact independent WHATWG Node resolver proves `[review](../issues/tmp/%2e%2e/../pull/+0200)` navigates to the actual first-party PR #200 alias; exact extracted source relative-link matcher returns False. Further `.%2E`, `%2E.`, `0200` and `.patch` variants reproduce. Both initial and pre-PATCH issue-reference gates call the vulnerable matcher. There was no live `--apply`, PATCH or closure. Independent full-module positive test matrix **not completed** and does not justify CLEAN; the independently reproduced MAJOR defect justifies CHANGES_NEEDED.

## Required route and blockers

Exactly one **already-created** bounded corrective successor: Issue **#1769**. It is **BLOCKED until** this issue's authentic unedited in-lease negative schema-3 `REVIEW_STATUS`. The new corrective execution must rederive current main and then claim its own fresh branch, inherit exact eight source PR #1767 paths and preserve seven Git blobs. Correct only the script and add its own handoff; add an independent WHATWG oracle and actual full-module mocked first/fresh-scan zero-PATCH coverage. Exact-head read-only CI, new distinct independent security review and independently authorized SQUASH-only NONCANONICAL integration remain future gates.

This reviewer-only two-path draft PR **MUST NEVER MERGE**. Review completion is not source integration, canonicalization, readiness, production, gameplay, or live PR-retirement authorization. Repository issue comment `REVIEW_STATUS` and its HEAD/PR identity are authoritative; this handoff alone is not the terminal record.
