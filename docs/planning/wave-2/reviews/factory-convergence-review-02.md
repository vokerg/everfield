# Factory convergence repair review 02

## Scope and trust
Required security/authority review of Issue #768 / draft PR #770 at exact immutable producer head `5760bbcf6a35db03c6f47567a5237f466f495145`.

Trust mode: `DEGRADED_SINGLE_AGENT`. The review actor/session is distinct from producer ownership generations; the producer branch was treated as immutable and was not edited during review.

## Frozen identities
- base/current main during review: `4986dd9c275e44a931e17b855a760f45fa6ae4c0`;
- canonical binding: Issue #6 comment `5245368879`;
- producer terminal: Issue #768 comment `5489322776`;
- PR #770: open, draft, mergeable, exact head `5760bbcf6a35db03c6f47567a5237f466f495145`, base exact current main;
- producer changed paths: exactly 3;
- `tools/planning/frontier_maintenance_v3.py` blob `a37aaa2113f9c136410d4258e6493a35be33042c`;
- `.github/workflows/planning-frontier-maintenance.yml` blob `8a7f21dc98b1904ab4dbce0c0c867034f6ac4fda`;
- `docs/planning/handoffs/issue-768.md` blob `1ed9b6871bb726986a2458c1c3faa5b2756642cf`;
- route registry remained unchanged at blob `8672e108279eab505987d961e1e5f01c4f56c26e`.

## Independent runner validation
A transient review-only workflow on `planning/issue-773` checked out the judged producer SHA directly with `contents: read` only and `persist-credentials: false`.

- workflow run: `33473624080`, attempt 1;
- validation job: `99748232979`;
- exact checkout: `5760bbcf6a35db03c6f47567a5237f466f495145`;
- `python3 -m py_compile` for v1/v2/v3: PASS;
- `frontier maintenance self-test`: PASS;
- `frontier maintenance v2 self-test`: PASS;
- `frontier maintenance v3 self-test`: PASS;
- job conclusion: `success`.

The transient validation workflow was removed from the review branch after the run and is not part of the review PR output.

## Adversarial findings

### R1 — REVIEW_READY routing / closure boundary: PASS
The new routable-terminal validator reuses the existing trusted immutable operational parser and repeats strict issue, OWNER authority, mission/session, ownership-generation, head/work SHA and ordering checks. `REVIEW_READY` is added only to the v3 routable-state set; base `TERMINAL_STATES` remains unchanged, so automatic GitHub issue closure is not broadened.

### R2 — open/closed source convergence: PASS
Routing derives from the combined open + recent-closed issue population and deduplicates by issue number before terminal inspection. This fixes open terminal `REVIEW_READY` episodes without allowing the same issue snapshot to materialize twice in one maintenance invocation.

### R3 — successor consumption specificity: PASS
The added relations are narrow explicit structural forms: `recovery transition: #N` and line-bound `source_transition_issue: N`. Existing v2 rules continue to reject arbitrary prose mentions. This is sufficient for the live #738 -> #733 relationship while preserving trusted-author, creation-generation and non-transition-successor constraints.

### R4 — NONE and recursion suppression: PASS
Exact `NONE_FROM_THIS_TRANSITION` is treated as a no-route sentinel. Unregistered factory-transition sources are not recursively materialized. This removes the observed transition-of-transition churn without suppressing ordinary semantic successor issues.

### R5 — registered direct dispatch and retry: PASS
For the current reviewed route registry, registered routes are exact-main `workflow_dispatch` entries. v3 dispatches them directly from the exact terminal source rather than requiring a wrapper. It validates the workflow/ref contract, binds dispatch markers to exact `(source issue, terminal comment, route)`, checks current-main run state, reuses v2 grace/failure retry semantics, re-fetches the exact source generation immediately before mutation, and caps duplicate workflow/main dispatches within one maintenance invocation.

Existing v2 behavior is preserved: `SUCCESS`/`IN_FLIGHT` suppress duplicate dispatch; `MISSING` within grace suppresses duplicate dispatch; `FAILED` and `MISSING` after grace remain retryable. A direct dispatch creates no review, verification, integration, decision or canonical authority.

### R6 — wrapper retirement / active ownership: PASS
Open wrappers for registered routes, NONE routes, stale/consumed generations and unregistered transition recursion are retirement candidates, but `transition_has_active_operational_state()` preserves active ownership. Historical closed transition/resolution provenance remains available to v2 generation-aware reconciliation.

### R7 — workflow and authority surface: PASS
The production workflow keeps the same schedule/push/manual triggers, `contents: read`, `issues: write`, `pull-requests: write`, `actions: write`, concurrency group, exact event-SHA checkout and pinned checkout action. The only workflow change is compile/self-test/execute v3 instead of v2. Route registry bytes are unchanged. No authority field is upgraded.

## Live-chain consequence check
The exact live topology is consistent with the repaired semantics:
- Issue #738 carries explicit source-transition relationship to #733 and therefore consumes that predecessor rather than causing #733 to be rediscovered;
- terminal Issue #738 is `REVIEW_READY` with an unregistered mandatory review route and becomes eligible for one bounded semantic transition;
- registered Unity re-execution routes can retry directly after a failed run without creating another wrapper issue;
- NONE and registered-route wrappers are cleanup candidates when unowned.

## Non-correction note
The reviewed registry currently contains only `workflow_dispatch` routes. Any future new registered route type must be separately reviewed/implemented; this PASS does not authorize silent expansion of the registry schema or execution authority.

## Findings and disposition
- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0
- non-correction notes: 1

Disposition: `PASS_FOR_INTEGRATION`.

This disposition permits only a separately governed squash-only publication of exact producer head `5760bbcf6a35db03c6f47567a5237f466f495145`. It grants no planning/canonical decision, verification-PASS, gameplay implementation/readiness, provider, engine-selection or release authority. The push-triggered production maintenance run after publication is still required to establish live operational behavior on the resulting exact current `main`.
