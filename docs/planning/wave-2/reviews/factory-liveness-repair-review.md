# Factory liveness repair review — Issue #680

Reviewed immutable producer: Issue #676 / draft PR #679 at `a98172932bd1c22ec9531b15d73d2ac1a2b5e046`.

Trust mode: `DEGRADED_SINGLE_AGENT`.

Disposition: `CHANGES_NEEDED` — 0 BLOCKER / 2 MAJOR / 0 correction-requiring MINOR.

## M01 — stale terminal can close a live restarted/recovered issue

`latest_terminal()` selects the highest terminal record but ignores later trusted schema-3 operational comments. A valid sequence such as terminal `DONE` followed by a legitimate restart/recovery `CLAIM` therefore still appears terminal to `close_terminal_open_issues()`, which can close a live issue. Maintenance must gate closure on the latest trusted schema-3 operational state-bearing comment, not merely the latest terminal subset. A later operational comment must conservatively suppress auto-closure unless it is itself terminal.

## M02 — rejected-PR cleanup matches predecessor prose

`close_rejected_open_prs()` searches raw substrings (`CHANGES_NEEDED`, `CHANGES_REQUIRED`) anywhere in a draft PR body. Live remediation PRs commonly quote or reference a predecessor review disposition, so this can close valid current work. Retirement must require an explicit self-disposition form (for example an anchored `Disposition: CHANGES_NEEDED` / `Review disposition` record) or an unambiguous self-prohibition such as `must not integrate` / `must not be merged`.

## Clean properties retained

- untrusted issue comments cannot create terminal maintenance authority because author association is constrained;
- workflow dispatch is allowlist-only and exact-main-only;
- route text is never evaluated as code or shell;
- the target Unity workflow independently fences repository/ref/SHA/current-main/runner identity;
- closure/dispatch does not grant review, verification, integration, readiness, decision, or canonical authority;
- predecessor recognition for #674 -> #675 is structurally present.

## Required remediation

Create one bounded remediation preserving PR #679 immutable. Fix M01 and M02, add deterministic self-tests for both counterexamples, then perform fresh review before squash integration.
