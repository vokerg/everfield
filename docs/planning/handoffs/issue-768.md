# Issue #768 handoff — factory convergence repair

## Scope
Owner-directed bounded repair of the repository frontier-maintenance process. No planning/review/verification/integration/decision/canonical authority is granted by this producer packet.

## Frozen basis
- base `main`: `4986dd9c275e44a931e17b855a760f45fa6ae4c0`;
- canonical binding: Issue #6 comment `5245368879`;
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- producer claim: Issue #768 comment `5489243310`;
- producer recovery generation: Issue #768 comment `5489282264`;
- superseded first producer terminal: Issue #768 comment `5489269964`;
- prior v1 maintenance blob: `912c452c2869d055ac47ffb4da70680ff2f184c1`;
- prior v2 maintenance blob: `9c7f73a1de409fcfe22504dcdaf48a2f0dff5b6e`;
- prior workflow blob: `be4c07ded78e892331356f472d89951d2fc6bfc7`.

## Demonstrated live failures repaired
1. Owner-bound terminal `REVIEW_READY` episodes were not eligible routing sources, stranding Issue #738 / PR #739 before required review.
2. Factory transition wrappers could themselves become routing sources, producing transition-of-transition recursion such as #733 -> #740 -> #751.
3. `NONE_FROM_THIS_TRANSITION` was treated as executable liveness work.
4. Live explicit successor wording `recovery transition: #N` was not recognized, allowing consumed source #733 to be rediscovered repeatedly.
5. A valid terminal `REVIEW_READY` episode could remain GitHub-open; routing only the closed-issue snapshot would still strand that chain. The recovered producer iterates the combined open+recent-closed source set with issue-number deduplication.

## Producer changes
- added `tools/planning/frontier_maintenance_v3.py` as a narrow convergence layer over reviewed v1/v2 primitives;
- split routable terminal semantics from automatic GitHub-close semantics: `REVIEW_READY` may drive a required next route but is not added to the base closable states;
- routes valid terminal episodes from the combined open/recent-closed issue set, deduplicated by issue number;
- added exact no-route sentinel suppression for `NONE_FROM_THIS_TRANSITION`;
- added explicit structural successor recognition for `recovery transition: #N` and `source_transition_issue: N`;
- added retirement of transition wrappers whose source issue is itself a factory transition;
- switched `.github/workflows/planning-frontier-maintenance.yml` to compile and self-test v1/v2/v3, then execute v3;
- permissions, concurrency, exact-SHA checkout, route allowlist, exact-main dispatch, ownership, and authority boundaries are unchanged.

## Verification
- `python3 -m py_compile` of the recovered v3 source: PASS in producer environment;
- focused deterministic v3 invariants executed against a minimal compatibility harness: PASS, including open/closed source deduplication;
- self-tests embedded in v3 also invoke the existing v2/v1 self-tests when run in the repository workflow;
- no route-registry or permission expansion;
- recovered substantive producer head before this handoff update: `03010783a6b6bf140da9ef680dff42463569477d`.

## Required review
Fresh independent/degraded-independent review must inspect the exact immutable recovered producer head and attack at minimum:
- whether REVIEW_READY routing preserves strict owner/ownership/head bindings;
- whether both GitHub-open and closed terminal episodes can route without duplicate materialization;
- whether automatic issue closure remains limited to the prior closable terminal states;
- whether successor regex additions are structural and cannot consume arbitrary issue mentions;
- whether transition recursion and NONE suppression can hide legitimate routes;
- whether v3 preserves generation-aware consumption and retry-safe exact-main dispatch from v2;
- whether workflow permissions and authority boundaries remain unchanged.

A clean review may only route a separately authorized squash-only publication. After reviewed publication, a fresh maintenance run should retire stale #733/#740/NONE wrappers and surface the missing review transition for terminal Issue #738.

`NOT_CANONICAL`. No integration authority by producer status alone.
