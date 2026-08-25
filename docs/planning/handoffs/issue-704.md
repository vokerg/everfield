# Issue #704 — factory cleanup / successor hardening

## Scope
Bounded follow-up to the live planning-frontier maintenance rollout. Prevent false/repeated transition materialization without weakening terminal ownership validation, route allowlists, exact-main dispatch, or authority gates.

## Producer changes
- added `tools/planning/frontier_maintenance_v2.py`, reusing the reviewed v1 safety/authority primitives;
- recognizes only explicit successor relationship phrases, including the live repair forms `remediation of Issue #N`, `review of Issue #N`, `Required clean review: Issue #N`, and `required by terminal Issue #N`;
- treats a closed factory transition as source consumption only when an immutable trusted resolution is bound to an actual trusted dispatch marker;
- retires redundant open factory transitions when a real non-transition successor/resolution exists, but preserves a transition whose latest valid schema-3 operational record is nonterminal/active;
- workflow now compiles v1+v2, runs v2 deterministic self-tests, then executes v2 maintenance.

## Cleanup already performed
Superseded repair PRs #679, #684, #688 were closed. Completed repair issues #676, #682, #687, #691, #696 were closed. False transition issues #697, #701, #702, #703 and repeated false transitions #705, #706, #708, #709, #710, #711 were closed `not_planned`.

Issue #707 was deliberately not closed because it has a live schema-3 claim and an accepted exact-main Unity dispatch. The hardening must preserve that ownership episode.

## Verification
- branch diff from `main@300dc88827b7709d9733d30b57de4dcb1669b532` is bounded to workflow + v2 module + this handoff;
- regex counterexamples verified for live #680/#682, #685/#687, #689/#691, #693/#695, and #665/#667 relationships;
- arbitrary issue-number mentions remain non-edges;
- deterministic v2 self-test includes resolved-dispatch binding, edited resolution rejection, wrong dispatch-ID rejection, transition/non-transition consumption, and redundant transition identification.

## Notes
Two no-op direct-main commits (`bac1a9f...` then `300dc888...`) were created and immediately reversed during cleanup setup; current tree after `300dc888...` is identical to the pre-accident `792185ac...` tree. No functional repository content remained from that mistake.

## Required next gate
Fresh review of the exact producer head. Only a clean `PASS_FOR_INTEGRATION` may route squash-only integration. After integration, inspect the triggered maintenance run and ensure it does not recreate known false transitions or redispatch a resolved source indefinitely.
