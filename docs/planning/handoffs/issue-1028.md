# Issue #1028 handoff — W2-ENG-DECISION-FORMAL-CONT-01

## Purpose

This continuation exists only to consume the explicit owner authority in Issue #919 comment `5651198366` and publish the reviewed Godot `4.7.1-stable` selection as a durable selected-engine record.

## Frozen authority

- canonical binding: Issue #6 comment `5245368879`
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- producer: Issue #804 terminal `5521287905`
- producer exact head: `456043100eddc3de20b18f2a29e889c8c64fb90f`
- required review: Issue #832 terminal `5536194396`
- review disposition: `CLEAN_FOR_FORMAL_ENGINE_DECISION_GATE`
- formal gate: Issue #895 terminal `5580950990`
- authority trigger: Issue #919 comment `5651198366`
- authorized selected engine: Godot `4.7.1-stable`

## Owned output

- `docs/planning/SELECTED-ENGINE.md`
- `docs/planning/handoffs/issue-1028.md`

No producer, review, provider, content, compiler, or readiness artifact is owned by this continuation.

## Publication semantics

The branch artifact is publication material only. The selected-engine record becomes `CANONICAL_SELECTED_ENGINE_RECORD` only if the exact authorized PR is squash-published to `main`. The terminal Issue #1028 integration status must bind the actual squash/main SHA.

The authority is intentionally narrow:

- selected engine: Godot `4.7.1-stable`;
- implementation readiness: false;
- gameplay/high-throughput implementation: blocked;
- provider/comparison/aggregate verification PASS: not granted;
- production/release/legal/platform authority: not granted.

## Required post-publication route

After exact authorized publication, materialize exactly one fresh implementation-readiness continuation under the active canonical program. That successor must independently reconcile the canonical selected-engine record with the current readiness/evidence ledger and route fresh independent verification. It must not treat engine selection as implementation readiness and must not reopen generic five-engine comparison work absent new controlling evidence or authority.

## Integration constraints

- exact bounded authority source: #919 comment `5651198366`;
- merge method: squash only;
- current-main/head compatibility must be re-derived immediately before integration;
- draft PR existence or mergeability does not itself grant canonical authority;
- no additional human engine-selection approval is required by the authority record;
- no readiness authority is inherited from this integration.
