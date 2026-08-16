# Issue #387 handoff — W2-CONTENT-SOCIAL-REM-01

## State

`REVIEW_READY / REMEDIATION_COMPLETE_PENDING_FRESH_REQUIRED_REVIEW`

This task performed only the bounded remediation routed by required review Issue #384. It did not mutate producer #367 or reviewer #384, execute WSN evidence, consume mutable sibling outputs, integrate work, select an engine, authorize implementation/readiness/release, or create canonical authority.

## Ownership

- issue: #387;
- mission: `W2-CONTENT-SOCIAL-REM-01`;
- winning claim: `5305978757`;
- actor session: `w2-content-social-rem-01-gpt56sol-20260816-01`;
- branch: `planning/issue-387`;
- branch base: `32637bf66d8e76a4f029c9ca74f983cbe5535ffb`;
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- canonical binding comment: `5245368879`;
- canonical activation SHA: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- owner convergence directive: `5277825639`;
- owner parallel-frontier directive: `5305563203`.

Ownership was uncontested after claim and rechecked before every branch write.

## Frozen predecessor provenance

### Producer

- Issue #367 / `W2-CONTENT-SOCIAL-01`;
- claim `5305656863`;
- terminal `5305675516`;
- exact producer head `db5d8ff86f4faeafa4a816412a2170cde979fb67`;
- draft PR #380.

### Required review

- Issue #384 / `W2-CONTENT-SOCIAL-REV-01`;
- claim `5305707061`;
- terminal `5305720735`;
- exact review work `f92392a7ded55701b21ca498e2575b5766fa4fd4`;
- exact review head `f10657602500ea30b4cff209082106e037f92fab`;
- draft PR #388;
- disposition `CHANGES_NEEDED`;
- finding count 0 BLOCKER / 2 MAJOR / 0 correction-requiring MINOR;
- review provenance squash publication `32637bf66d8e76a4f029c9ca74f983cbe5535ffb`.

Findings remediated:

- `W2-CONTENT-SOCIAL-REV-M01` — orthogonal social claim/belief typing;
- `W2-CONTENT-SOCIAL-REV-M02` — mechanically complete `ProgressionGateContract` semantics.

## Remediation artifacts

Substantive remediation work head before this handoff: `442539429762569002c3822e8798ceda47ddfd3d`.

Owned successor paths:

- `docs/planning/wave-2/content/factions-social-topology.md`;
- `docs/planning/wave-2/content/factions-social-topology.yaml`;
- `docs/planning/handoffs/issue-387.md`.

No additional schema file was created.

The successor packet composes the exact frozen #367 producer packet with only the explicit M01/M02 corrections. Unchanged producer semantics remain immutable provenance rather than being re-authored from memory.

## M01 closure

The machine-readable successor replaces the conflated old `information_scopes` concept with `SocialClaimBelief`, separating:

- holder/source perspective;
- proposition identity;
- social authority status;
- holder epistemic state;
- dispute status;
- knowledge/player-exposure state;
- exposure scope;
- confidentiality;
- provenance;
- branch applicability;
- separately owned objective-fact reference;
- truth relation.

`objective_fact_authority` is mandatory and fail-closed `false` in this social root. Institutional assertion, testimony, rumor, corroboration, exposure, or branch state cannot promote a social claim into objective world truth. New proposition/fact/branch refs are provisional typed interfaces only.

Disposition: `W2-CONTENT-SOCIAL-REV-M01 = REMEDIATED_PENDING_FRESH_REVIEW`.

## M02 closure

All six social gates bind frozen W1-SYN-GAME `ProgressionGateContract` v1 from exact work `e74e0b0c95e85f69718868eedae324a298f02f3e`.

Every gate now explicitly contains:

- `version: 1`;
- gate ID/class;
- blocks/unlocks;
- gate-level `requirements`;
- routes;
- `visibility_or_discovery`;
- recovery;
- nullable/typed `branch_scope`;
- evidence requirements;
- explicit `exception_rationale: null`.

Every route contains route ID/kind, prerequisite refs, and nonempty `lifestyle_impacts`.

Gate count remains 6 and foundational gate count remains 0. The coalition gate remains `BRANCH_EXCLUSIVE`, preserves ordinary services, and retains `WSN-E5`, `BRANCH_IMPACT_EVIDENCE`, and `ALTERNATIVE_CONTENT_SUFFICIENCY` obligations.

Disposition: `W2-CONTENT-SOCIAL-REV-M02 = REMEDIATED_PENDING_FRESH_REVIEW`.

## Regression self-review

Preserved and re-attacked:

- exact six actor IDs;
- exact ten edge IDs;
- multidimensional relationship semantics and retained meaningful social history;
- zero foundational social gates;
- baseline community, making/repair, cultivation, movement/exploration, public information, and mutual aid alternatives;
- four bounded branch patterns and no permanence authority;
- provisional sibling interfaces only;
- originality/reference-use boundary;
- WSN evidence remains unrun;
- engine-neutral, noncanonical, nonimplementation scope.

Mechanical checks:

- actor count: 6;
- edge count: 10;
- gate count: 6;
- foundational gates: 0;
- branch patterns: 4;
- all routes have `lifestyle_impacts`: yes;
- every gate has explicit `exception_rationale`: yes;
- social claim promotion forbidden: yes;
- WSN PASS claims: 0.

Self-review findings: 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR.

## Required downstream review

Fresh required review successor created as Issue #391 / `W2-CONTENT-SOCIAL-REM-REV-01`.

Issue #391 is intentionally blocked until this remediation terminalizes and an immutable prerequisite-binding comment records:

- terminal remediation schema-3 status comment;
- exact terminal branch head;
- exact draft PR/head/base;
- exact judged paths and substantive work identity.

The reviewer must use a fresh actor/session distinct from this remediation. Under the one-agent resource constraint, `DEGRADED_SINGLE_AGENT` is acceptable only if recorded explicitly; full independence must not be claimed.

A clean review may satisfy only the social root's review prerequisite for later `W2-CONTENT-SYN-01` fan-in. It does not itself grant integration or canonical authority.

## Authority boundary

This remediation grants no content fan-in before fresh review, no engine selection, gameplay/high-throughput implementation, implementation readiness, empirical WSN PASS, verification-PASS, release, decision, integration, or canonical authority. Any later publication to `main` is a separate squash-only authority decision under then-current repository state.
