# Issue #1667 — Negative reviewer-only draft retirement handoff

## Exact scope and origin
Owner-directed fix of an excessive frozen/rejected PR backlog. The source immediately reduces GitHub-open PR storage clutter by retiring only proven **terminal CHANGES_NEEDED** reviewer-only draft PRs that no longer have an active open-issue reference. This is independently ownable storage cleanup, not source validation, review PASS, a source PR merge, or integration authority.

Canonical Planning Program #1147 binding #5675066392 / blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation SHA `87c85cecfa9a2ffa464c4b36816a138bf41441af`; base main `3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`. This issue first winning owner CLAIM #6112473402. Current independent factory remediation #1664 / PR #1665 already edits existing base parser/workflow; **none of its shared source paths is modified** here.

## Owned exact paths
- `tools/planning/retire_negative_review_prs.py`: standalone strict PyYAML-6.0.3 eligibility guard. Defaults to read-only dry run. Requires owner-authored open main draft, stable reviewer issue #N, closed/completed reviewer issue, exactly two review/handoff files, unedited YAML-only terminal and six-hour owner generation, exact PR head and reviewer head, aged 72 hours and no currently open issue mentioning that PR number. Safeguards reject duplicate YAML keys, aliases, explicit tags, edited records, unknown/unsupported shapes, parser ambiguity and source (nonreview) PRs.
- `.github/workflows/retire-negative-review-prs.yml`: PR-only read access and self-test; a separate daily 03:41 UTC schedule / manual main dispatch can act **only after** a clean independently reviewed squash publication into main. Runs self-tests and default dry-run first, with write permission only on the integration/main path.
- This handoff file.

## Boundaries and limitations
- Never close the current negative reviewer #1663 while an open remediation #1664 refers to it. Never touch producer #1660, current game candidates #1653/#1641, needed verifier evidence or any task.
- Existing old negative review and frozen source PRs have been manually reconciled by exact source/review terminal IDs and immutable head SHAs, leaving the GitHub diff, reports and comments accessible in closed PRs.
- The scheduled tool is intentionally **more conservative** than manual reconciliation: it handles only exact two-path negative reviewer PRs, not rejected source versions, and refuses recently terminalized reviews for 72h. It also skips any open issue mentioning the PR. It can miss ambiguous/legacy records without ever granting extra authority.
- On PRs, the workflow has no write token and cannot mutate GitHub.
- GitHub Actions PR self-test is required; do not treat source authorship as PASS. An independent adversarial code/security reviewer must challenge YAML behavior, owner lease linkage, GitHub trust assumptions, head drift, file path/name parsing, open-reference scanning and event permission restrictions before integration. A successful self-test is not independent review approval.

## Required next gates
1. Compile and run the new source on exact final PR head through GitHub Actions. Confirm review-only self-test passes and mutation job is SKIPPED for pull_request event.
2. Reviewer must be truly distinct from producer. Any negative review routes bounded repairs; no self-approval.
3. Separately authorized integration owner may later squash-publish exact compatible source as NONCANONICAL. A main scheduled run is the first possible mutating automation; no branch or review PR can itself run `--apply`.
4. After integration, compare PR counts and verify no active source/review candidate closed, and that every closed review can still be linked to its original issue comment and exact head.
5. Do not conflate storage closure with canonical, implementation-readiness, engine, release or production authority.
