# Issue #714 — generation-aware successor remediation

## Review addressed
Issue #713 reviewed immutable Issue #704 / PR #712 and returned `CHANGES_NEEDED` with three MAJOR findings.

## M01 — untrusted successor injection
Closed. Successor edges now require a trusted issue author (`OWNER`/`MEMBER`/`COLLABORATOR` or `github-actions[bot]`). Arbitrary external issue prose cannot suppress a trusted terminal route. Matching factory transitions are likewise required to be trusted before they can block creation of a real transition.

## M02 — missing #695 -> #696 edge
Closed. Completed Issue #696 now contains explicit `predecessor_issue: 695` cleanup metadata. No vague-prose inference is required.

## M03 — stale generation suppression
Closed. Consumption is now bound to the current terminal generation:
- normal successor issue creation time must be at/after the current terminal record time;
- resolved transitions bind exact `(source_issue, source_terminal_comment_id, route)`;
- transition body title/source/comment/route must agree;
- an old successor or resolved transition cannot consume a newer terminal generation after reopen/reterminalization;
- stale/redundant open transition cleanup preserves any transition whose latest valid schema-3 operational record remains nonterminal.

## Live behavior expected
- #665 is consumed by trusted successor #667.
- #680/#685/#689 are consumed by their later remediation issues.
- #693 is consumed by #695.
- #695 is consumed by explicit successor metadata on #696.
- #675 generation `5397969110` is consumed by resolved transition #699; active claimed transition #707 is preserved rather than force-closed, but no further duplicate transition should be materialized for that same generation.

## Verification
Deterministic tests cover trusted/untrusted successor authors, successor timestamp ordering, exact transition generation parsing, stale/new terminal generation separation, trusted dispatch+resolution binding, edited/wrong resolution rejection, and untrusted matching-transition rejection.

## Required next gate
Fresh review of the exact remediation head. Only clean `PASS_FOR_INTEGRATION` may route squash-only integration. After integration, inspect the live maintenance run for zero recreation of the known false transition sources and no duplicate #675 generation materialization.
