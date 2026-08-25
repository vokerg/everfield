# Issue #682 — factory liveness remediation handoff

Source review: Issue #680 / PR #681, disposition `CHANGES_NEEDED` with findings M01/M02 over immutable producer #676 / PR #679 at `a98172932bd1c22ec9531b15d73d2ac1a2b5e046`.

## Remediation
- M01: terminal auto-close now requires the latest trusted schema-3 operational comment itself to be terminal. A later claim/recovery/progress/handoff conservatively suppresses closure.
- M02: draft PR retirement now requires an explicit self-disposition (`Disposition: CHANGES_NEEDED|CHANGES_REQUIRED`, review-disposition block) or an unambiguous `This PR must not ...` prohibition. Predecessor prose alone is ignored.
- Added deterministic no-network self-tests for terminal->claim restart, predecessor disposition prose, explicit rejection forms, and outsider terminal comments.
- Maintenance workflow runs compile + self-test before any mutating step.

## Verification
Local Python compile and `--self-test` pass for the exact remediated script content. Route registry, exact-main dispatch fencing, entry directives, and authority boundaries are unchanged.

Fresh review of this remediation head is mandatory before squash integration.
