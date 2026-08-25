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
- closed `not_planned`/`duplicate` successors do not consume a route;
- resolved transitions bind exact `(source_issue, source_terminal_comment_id, route)`;
- transition body title/source/comment/route must agree;
- an old successor or resolved transition cannot consume a newer terminal generation after reopen/reterminalization;
- stale/redundant open transition cleanup preserves any transition whose latest valid schema-3 operational record remains nonterminal.

## Dispatch outcome fencing
A trusted `dispatch ACCEPTED` marker is no longer treated as permanent success. For a closed resolved transition, maintenance checks the exact workflow/head run:
- `success` or an in-flight run consumes the exact terminal generation;
- a just-accepted marker may temporarily consume it for a 15-minute propagation grace period;
- a failed run or a long-missing run makes the generation retryable;
- this prevents an accepted-but-never-successful dispatch from becoming a permanent liveness tombstone.

## Live behavior expected
- #665 is consumed by trusted successor #667.
- #680/#685/#689 are consumed by their later remediation issues.
- #693 is consumed by #695.
- #695 is consumed by explicit successor metadata on #696.
- #675 generation `5397969110` is consumed only while its exact accepted run is in-flight/successful or inside the bounded dispatch grace; active claimed transition #707 is preserved rather than force-closed.

## Verification
Deterministic tests cover trusted/untrusted successor authors, dead-successor rejection, successor timestamp ordering, exact transition generation parsing, stale/new terminal generation separation, trusted dispatch+resolution binding, edited/wrong resolution rejection, workflow-run success/in-flight/failure/missing outcomes, bounded dispatch grace, and untrusted matching-transition rejection.

## Required next gate
Fresh review of the exact remediation head. Only clean `PASS_FOR_INTEGRATION` may route squash-only integration. After integration, inspect the live maintenance run for zero recreation of the known false transition sources and no uncontrolled duplicate #675 generation materialization.
