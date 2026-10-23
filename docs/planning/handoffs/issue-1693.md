# Issue #1693 — mandatory security remediation handoff

**Mission:** `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-03`
**Owner:** sole first CLAIM GitHub comment #6130818930, GitHub server `created_at=2026-10-12T19:07:41Z`; session `frontier-retirement-remediate-1693-gpt6-20261012-2105-cph-01`.
**Current-main base at claim:** `a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`.
**Canonical binding:** Issue #1147 immutable INTEGRATION_STATUS #5675066392, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.

## Scope and provenance

Mandatory single bounded correction of independent negative reviewer Issue #1689, valid terminal `REVIEW_STATUS(CHANGES_NEEDED)` #6130426848, 0 BLOCKER / **1 MAJOR FSR-1689-M01** / 0 correction-requiring MINOR, reviewer-only OPEN/DRAFT PR #1692 frozen HEAD `dd03686faee4640df7d164d0f5643dfa329948d2`. Prior source #1685 REVIEW_READY #6127516839, DRAFT PR #1688 HEAD `53b298d2c2189fc9ede6137655a977f54862cd5a`, is not accepted or integrable. This execution is separate from #1685 source author and #1689 reviewer.

New branch `planning/issue-1693` starts at the exact current main from claim and ports the frozen source script blob `caf8d61687874479978df9a834511b85b7a583bd` and the byte-identical read-only-on-PR workflow blob `e141fffcbb95c02fa215ffec3c403e0e93d1fc90`. Only the issue-specific Python script and this handoff have new bytes. No predecessor, reviewer, shared factory, gameplay or main changes.

## Corrective implementation

- `references_pr()` now vetoes the literal `#N` and exact repository-qualified GitHub web `/pull/N` or API `/pulls/N` canonical URLs in open issue titles, bodies **and all loaded live comments**. It uses complete path-segment comparison after URL splitting, accepts unambiguous subresources, query and fragment, and does not treat `/pull/2000`, foreign repository/host or issue paths as PR #200. Parsing uncertainty vetoes rather than granting permission.
- Existing authenticated first-claim, independent negative review, strict YAML/lease, 72h, frozen branch/repo/mission, exact report SHA/diff path, complete issue-and-comment pagination/count and later-conflict checks remain unchanged.
- Added self-test cases for web/API comment-only and body-only links, title-only `#N`, safe suffixes, foreign/substring nonreferences, actual `live_open_issue_references()` capture, and an in-memory `execute(apply=True)` two-snapshot race: initial no-reference followed by linked comment immediately before PATCH must veto without any PATCH. All mocked; no live API mutation.
- The real GitHub GET/scan-to-PATCH interval remains **non-atomic**. No compare-and-swap PR-close guarantee, deployment, `--apply` or auto-merge is claimed.

## Evidence and remaining gates

The unchanged inherited workflow runs Python compile + full `--self-test` on the exact PR HEAD and skips the mutating `retire` job on PR. Hosted CI results, actual final PR HEAD and changed-path verification must be attached to the **owner terminal comment** after they exist; this handoff records test design, not self-certifies pending CI.

Before `STATUS(REVIEW_READY)`: confirm fresh main/binding/ownership lease; exact authorized three-path draft PR; hosted exact-final-head self-test SUCCESS and mutating job SKIPPED. Then create exactly one new mandatory distinct independent adversarial security review successor. A clean reviewer never merges this branch itself; a separate owner-authorized current-main-compatible **SQUASH-only NONCANONICAL** source integration is required. Old PRs remain DRAFT/UNMERGED.

**Next agent:** independently inspect inherited and corrective source, perform genuinely distinct required negative-case security review at frozen exact HEAD. Do not use this author session for that review; never close draft review PRs or run `--apply` based on these authored tests alone.
