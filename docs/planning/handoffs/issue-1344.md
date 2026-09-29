# Issue #1344 handoff — readiness dead-end liveness guard

## Status

Producer candidate for `FACTORY-READINESS-LIVENESS-REM-01`.

- ownership generation: Issue #1344 comment `5890010568`
- execution base: `main@271ceee5a8af967403b2cba460afdb493fa14ac1`
- current-main compatibility check: `main@765177165339039dab6f60a6f3dc315cd09b583f`
- intervening main commits: 2
- overlap with producer-owned paths: 0
- canonical binding: Issue #1147 terminal `5675066392`
- canonical program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`
- canonical activation: `87c85cecfa9a2ffa464c4b36816a138bf41441af`

This packet is **not canonical** and grants no review, verification, implementation-readiness, gameplay implementation, release, production, or integration authority.

## Controlling authority and defect

The guard binds the immutable owner implementation-transition directive at Issue #84 comment `5889817307`. That directive requires a verified blocked readiness state to route exact remaining internally resolvable blockers instead of terminating with no successor.

Historical Issue #1038 terminal verification `5651326367` is the motivating shape:

- `verified_candidate_outcome: BLOCKED`
- `implementation_ready: false`
- three readiness predicates remained `OPEN_BOUNDED`
- `required_next_route: NONE`

The later immutable owner recovery note `5889876653` already materialized live successors #1335–#1343. The new guard recognizes that recovery and therefore must not duplicate it.

## Changed runtime surface

### `tools/planning/frontier_maintenance.py`

Candidate blob before this handoff commit: `a10bb696f351816f532b510172618934ad0e7bd7`.

Adds a conservative readiness-dead-end detector that requires all of the following before a diagnostic may be materialized:

1. the exact owner directive comment `5889817307` is still immutable, trusted, on Issue #84, and contains the two routing clauses bound by the implementation;
2. the latest trusted schema-3 operational record is a terminal `STATUS` or `VERIFICATION_STATUS` for an implementation-readiness mission;
3. terminal state is `DONE` or `VERIFICATION_READY`;
4. authority mode matches the record class (`OWNER` for producer status, `VERIFIER` for verification status);
5. the ownership-generation linkage is exact and the canonical six-hour owner lease is valid at terminal time;
6. `head_sha` and `work_sha` are valid exact SHA-40 values;
7. no actionable `required_next_route` survives scalar normalization;
8. the terminal explicitly says `candidate_outcome: BLOCKED`, `verified_candidate_outcome: BLOCKED`, or `implementation_ready: false`;
9. the terminal is at/after the controlling directive, except for explicitly named historical source #1038;
10. no later immutable trusted owner recovery note already records explicit live successors;
11. no existing readiness-dead-end diagnostic for the source issue already exists.

When all predicates hold, maintenance creates only a recovery/diagnostic issue. It does not invent a route, readiness PASS, implementation authority, or canonical authority.

### `tools/planning/frontier_maintenance_v5.py`

Candidate blob: `dd79a64b28449cfb5dc076d4a327e03d87b4a964`.

The scheduled workflow executes v5. v5 already composes v4 -> v3 -> v2 -> the base module, so the base self-tests are inherited; however v5's runtime `main()` did not call the base `main()`. The candidate therefore wires `base.materialize_readiness_dead_end_diagnostics(open_items)` into the active v5 runtime and reports `readiness_dead_ends_created` in the existing JSON summary. No v2/v3/v4 transition semantics, route allowlist, dispatch semantics, or merge policy are changed.

## Regression coverage added

The base self-test now covers:

- historical #1038-shaped blocked/not-ready + `NONE` input is detected;
- the same blocked packet with an exact successor route is untouched;
- an unrelated legitimate `required_next_route: NONE` terminal is untouched;
- pre-directive implementation-readiness dead ends are untouched unless they are the explicitly recovered historical #1038 source;
- a ready/not-blocked terminal is untouched;
- an edited or wrong directive comment fails closed;
- the immutable #1038-style owner recovery note suppresses duplicate recovery;
- readiness diagnostic titles are deterministic.

The active test chain remains `v5.self_test -> v4.self_test -> v3.self_test -> v2.self_test -> base.self_test`, so these regressions are part of the v5 self-test surface.

## Validation performed

- exact historical #1038 CLAIM `5651304162` and terminal `5651326367` were re-read; the terminal occurs about five minutes after claim, within the canonical six-hour lease;
- exact owner directive `5889817307` and recovery note `5889876653` were re-read and are immutable;
- scheduled workflow `.github/workflows/planning-frontier-maintenance.yml` was re-read; it executes `frontier_maintenance_v5.py` and its v5 self-test;
- v4/v3/v2 self-test chaining was re-read and proves the base self-test is invoked by v5;
- current-main drift from the producer base was compared and is path-disjoint.

No live maintenance workflow was dispatched from the producer branch because the production workflow has issue/PR write authority and its normal runtime step is not a branch-only dry-run harness. Fresh review should independently execute or otherwise validate the exact frozen candidate before integration.

## Required fresh review

Review mission: `FACTORY-READINESS-LIVENESS-REM-01-REV-01`.

The reviewer must judge the exact producer head and attack at minimum:

- false positives on legitimate `NONE` terminals;
- directive spoofing/editing or over-broad retroactive scope;
- malformed ownership linkage, expired ownership, wrong authority mode, and malformed SHAs;
- duplicate diagnostics and the #1038 already-recovered case;
- accidental authority inflation or fabricated successors;
- active v5 wiring and inherited self-test execution;
- preservation of existing transition dedupe, route allowlist, workflow dispatch, canonical ownership, exact-head, and squash-only semantics.

A clean review may grant only bounded factory-remediation integration eligibility for the exact reviewed packet. Integration remains a separate squash-only authority episode.
