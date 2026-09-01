# Issue #768 handoff — factory convergence repair

## Scope
Owner-directed bounded repair of the repository frontier-maintenance process. No planning/review/verification/integration/decision/canonical authority is granted by this producer packet.

## Frozen basis
- base `main`: `4986dd9c275e44a931e17b855a760f45fa6ae4c0`;
- canonical binding: Issue #6 comment `5245368879`;
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- producer claim: Issue #768 comment `5489243310`;
- latest producer recovery generation: Issue #768 comment `5489304810`;
- superseded producer terminals: `5489269964`, `5489286098`;
- invalidated pre-review Issue #772 was closed unclaimed before judgment;
- prior v1 maintenance blob: `912c452c2869d055ac47ffb4da70680ff2f184c1`;
- prior v2 maintenance blob: `9c7f73a1de409fcfe22504dcdaf48a2f0dff5b6e`;
- prior workflow blob: `be4c07ded78e892331356f472d89951d2fc6bfc7`;
- route registry blob remains `8672e108279eab505987d961e1e5f01c4f56c26e`.

## Demonstrated live failures repaired
1. Owner-bound terminal `REVIEW_READY` episodes were not eligible routing sources, stranding Issue #738 / PR #739 before required review.
2. Factory transition wrappers could recursively become new missing-route sources, producing chains such as #733 -> #740 -> #751.
3. `NONE_FROM_THIS_TRANSITION` was treated as executable liveness work.
4. Live explicit successor wording `recovery transition: #N` was not recognized, allowing consumed source #733 to be rediscovered repeatedly.
5. A valid terminal `REVIEW_READY` episode can remain GitHub-open, so routing only a closed-issue snapshot strands the chain.
6. Registered `workflow_dispatch` routes already are repository-owned execution routes under `AGENTS.md`; wrapping them in transition issues creates unnecessary churn and complicates retry semantics.

## Final producer changes
- adds `tools/planning/frontier_maintenance_v3.py` as a narrow convergence layer over reviewed v1/v2 primitives;
- separates routable terminal semantics from automatic GitHub-close semantics: `REVIEW_READY` may drive liveness routing but is not added to base closable states;
- derives routable sources from combined open + recent-closed issues, deduplicated by issue number;
- recognizes explicit structural successor relations `recovery transition: #N` and `source_transition_issue: N`;
- treats `NONE_FROM_THIS_TRANSITION` as an exact no-route sentinel;
- for repository-registered exact-main `workflow_dispatch` routes, dispatches directly from the exact terminal source and records generation-bound dispatch markers on that source issue; no transition wrapper is required;
- keeps existing v2 retry policy: success/in-flight blocks duplicates, missing-within-grace blocks duplicates, failed/missing-after-grace remains retryable;
- re-fetches the exact routable terminal generation immediately before direct dispatch;
- retires unowned open wrappers for registered routes as `REGISTERED_ROUTE_NEEDS_NO_WRAPPER`;
- suppresses unregistered transition-source recursion while leaving registered execution retries available;
- keeps semantic/unregistered required routes on bounded factory-transition materialization;
- switches `.github/workflows/planning-frontier-maintenance.yml` to compile and self-test v1/v2/v3, then execute v3;
- permissions, concurrency, exact-SHA checkout, action pin, route registry, ownership, review, verification, exact-head, squash-only and authority boundaries are unchanged.

## Verification
- producer-side syntax validation of v3: PASS;
- focused deterministic convergence invariants: PASS for REVIEW_READY routing, open/closed deduplication, successor recognition, NONE suppression, registered-wrapper retirement, unregistered recursion suppression, and consumed-generation handling;
- v3 self-test calls the existing v2 and v1 self-tests before its own assertions when executed by the repository workflow;
- route registry and workflow permissions are unchanged;
- no gameplay, provider, verification-PASS, decision or canonical authority is introduced.

## Required review
Fresh independent/degraded-independent review must inspect the exact immutable final producer head and attack at minimum:
- strict owner/ownership/head/work validation for routable `REVIEW_READY` records;
- separation between routable and auto-closable terminal states;
- open/closed source deduplication and generation-aware successor consumption;
- structural specificity of the new successor relations;
- no-route and transition-recursion suppression;
- direct registered-route dispatch identity, exact-main fencing, retry semantics and marker binding;
- preservation of v2 generation-aware resolved-wrapper compatibility for historical provenance;
- unchanged workflow permissions, action pin, route registry and authority boundaries.

A clean review may route only a separately authorized squash-only publication. After reviewed publication, the push-triggered maintenance run should retire stale/no-route/registered wrappers, surface the missing semantic review transition for terminal Issue #738, and perform registered execution retries without generating more wrappers.

`NOT_CANONICAL`. No integration authority by producer status alone.
