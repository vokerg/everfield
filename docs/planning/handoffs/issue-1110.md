# Handoff — Issue #1110 / FACTORY-CONVERGENCE-06-REV-01

## State

Required degraded-independent review disposition: `CHANGES_NEEDED`.

Trust mode: `DEGRADED_SINGLE_AGENT`. Reviewer actor `frontier-review-factory-convergence-06-1110-gpt56sol-20260914-01` is distinct from producer actor `factory-convergence-06-gpt56sol-20260914-01`. The immutable producer branch and PR were not modified.

Finding counts: **0 BLOCKER / 1 MAJOR / 0 correction-requiring MINOR**.

## Frozen judged producer

- producer Issue #1108 / `FACTORY-CONVERGENCE-06`;
- winning producer claim `5659344391`;
- producer terminal `5659405978`;
- producer branch `planning/issue-1108`;
- draft PR #1109;
- exact producer base `98f0e66c1332f9a3ce47cf56ad352fab2223e8cd`;
- exact producer head `36afc975248e5fede3e1f5dc333041578674cc08`;
- producer work SHA `21519f96055da88abb099219ded6f8fee3ca9f8e`;
- changed paths are exactly:
  - `tools/planning/frontier_maintenance_v3.py` blob `c1ae395df4222dfd307d75f09ae7ec466569ab29`;
  - `tools/planning/frontier_maintenance_v5.py` blob `86050867d2bf168a0bbd38bc2a292edf0eb1be34`;
  - `docs/planning/handoffs/issue-1108.md` blob `a868fc7c7c0cea9a0b55948f4d780a44f0d188dc`.

Review base/current main at claim remained `98f0e66c1332f9a3ce47cf56ad352fab2223e8cd`.

Canonical authority remains Planning Program v1 blob `e3120ec203c4156328770aa86c12fbb7187966dc`, binding Issue #6 comment `5245368879`, activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e`.

## Clean attacks

The following required attacks are clean by exact-head source inspection:

1. **No-route sentinel scope.** `route_is_actionable` treats exactly `NONE` and `NONE_*` as non-actionable while `NONEISH` and `SOME_NONE_ROUTE` remain actionable.
2. **Terminal-state scope.** The new v5 path admits only `DONE` and `SUPERSEDED`; `INVALIDATED`, open wrappers, untrusted wrapper identities, and actionable terminal routes are rejected.
3. **Exact source generation.** Consumption returns the wrapper's exact parsed `(source_issue, source_terminal_comment_id, route)` generation. It does not rewrite or wildcard a later source generation.
4. **v4 composition/API shape.** The new check is composed with existing v4 semantic resolution inside the same closed-transition comment pass. It does not add a third closed-transition comment/API pass.
5. **Path confinement.** PR #1109 changes exactly the three producer-declared paths.
6. **Authority boundary.** The producer does not claim review, verification, integration, readiness, engine-selection, release, decision, or canonical authority.
7. **Execution limitation retained.** Neither producer nor this review claims a full patched v1→v5 execution PASS. Any future clean integration still requires exact-new-main push-triggered workflow acceptance.

## MAJOR finding

### FACTORY-CONVERGENCE-06-REV-MAJ01 — stale ownership generation can be accepted as a terminal no-route resolution

The new function `terminal_no_route_generation_from_comments` delegates ownership validity to `base.reconcilable_terminal_from_comments`.

That inherited parser proves only that the latest terminal record references an earlier ownership record with matching actor/mission and structurally valid fields. It does **not** prove that the referenced ownership generation is still the current valid ownership generation after a later valid `RESUME` or `RECOVER`.

The canonical schema-3 ownership contract is stricter: owner-authored terminal/result comments require the **current unexpired owner**; a stale/recovered actor cannot publish a valid terminal result using an old generation ID. Stale-owner or losing-generation records have zero authority effect.

A valid adversarial sequence therefore remains incorrectly consumable by the patch:

1. actor A owns the factory wrapper under ownership generation A;
2. ownership A becomes stale and a valid recovery creates ownership generation B for actor B;
3. stale actor A later posts a syntactically valid `STATUS(DONE|SUPERSEDED)` referencing generation A with no actionable next route;
4. schema-3 says that terminal has zero authority because A is no longer current owner;
5. `reconcilable_terminal_from_comments` can nevertheless accept it when it is the latest parsed operational record, because it only finds and validates the referenced old owner record;
6. the new v5 terminal-no-route resolver then consumes the wrapper's source generation as resolved.

This can suppress required liveness work using an authority-invalid stale terminal. It violates Issue #1108/#1110's explicit requirement that active/recovered/stale ownership conditions fail closed.

This is a **MAJOR** factory-liveness/authority defect, not merely missing test coverage.

## Required remediation

Route exactly one bounded remediation that:

1. keeps the narrow `NONE` / `NONE_*` classification unchanged;
2. before terminal-no-route generation consumption, proves the terminal's referenced ownership generation is the current valid/winning schema-3 ownership generation for that terminal episode, including recovery/resume supersession rules;
3. rejects an old-owner terminal after a later valid ownership generation;
4. retains fail-closed behavior for `INVALIDATED`, open/untrusted wrappers, malformed ownership, mismatched generation, and actionable routes;
5. preserves exact source-generation isolation and the existing v4 composition/API-pass shape;
6. adds a deterministic regression covering a later valid recovery/current owner followed by a stale prior-owner terminal;
7. does not weaken the mandatory post-publication exact-new-main v1→v5 workflow acceptance requirement.

The remediation must not edit the frozen producer or this review branch and must route a fresh required degraded-independent review before integration.

## Authority boundary

`NOT_CANONICAL`. This review grants no integration, verification-PASS, implementation-readiness, engine-selection, release, decision, or canonical authority. PR #1109 must not be integrated on this review result.
