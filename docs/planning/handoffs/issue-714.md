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
A trusted `dispatch ACCEPTED` marker is not permanent success. Maintenance checks the exact workflow/head run:
- `success` or an in-flight run consumes the exact terminal generation;
- a just-accepted marker may temporarily consume it for a 15-minute propagation grace period;
- a failed run or a long-missing run makes the generation retryable;
- an existing nonterminal schema-3 claim causes maintenance to defer dispatch, with a second ownership check immediately before the privileged dispatch mutation.

## Live transition compatibility
The factory has emitted both of these valid wrapper terminal forms and v2 accepts either only when bound to the exact trusted dispatch marker:
1. custom immutable `factory_transition_resolution: 1` records (for example #699);
2. normal owner-bound schema-3 `STATUS(DONE)` records with `disposition: TRANSITION_DISPATCH_ALREADY_ACCEPTED`, exact `source_issue`, `source_terminal_comment_id`, `required_route`, and `accepted_dispatch_comment_id` (live #707).

The schema-3 form is validated through the already-reviewed v1 ownership/immutability/head-binding validator before it can consume a source generation.

## Live behavior expected
- #665 is consumed by trusted successor #667.
- #680/#685/#689 are consumed by their later remediation issues.
- #693 is consumed by #695.
- #695 is consumed by explicit successor metadata on #696.
- #675 generation `5397969110` is consumed only while an exact bound dispatch run is in-flight/successful or inside bounded propagation grace. Failed/old-missing dispatches remain retryable. Closed #707 is recognized through its owner-bound schema-3 terminal rather than spawning another wrapper if its exact run is valid.

## Verification
Deterministic tests cover trusted/untrusted successor authors, dead-successor rejection, successor timestamp ordering, exact transition generation parsing, stale/new terminal generation separation, custom and schema-3 transition terminal binding, edited/wrong resolution rejection, workflow-run success/in-flight/failure/missing outcomes, bounded dispatch grace, and untrusted matching-transition rejection.

## Required next gate
Fresh review of the exact remediation head. Only clean `PASS_FOR_INTEGRATION` may route squash-only integration. After integration, inspect the live maintenance run for zero recreation of known false transition sources and no uncontrolled duplicate #675 generation materialization.
