# Required Review — Issue #1375 / FACTORY-CONTENT-DEMAND-LIVENESS-01-REV-01

## Exact subject
- producer issue: #1373
- producer terminal: comment 5926547886
- producer head: `a958c15b8242ffdf86d4d59619a74a6ad164f993`
- producer PR: #1374
- base: `main@05abfa094edc87b7f9766192e74477775eb7919e`
- v6 blob: `7d4c7c26a85bdf1457112fadb44ed559a2abdaea`
- workflow blob: `bb38c760d0b9b5251cd8247ed659853367605a2a`
- producer handoff blob: `39a297d4abc91820fd0695710650854e97480075`
- changed paths: exactly 3
- PR state at review: draft, mergeable

## Disposition
`CLEAN_FOR_FACTORY_CONTENT_LIVENESS_INTEGRATION`

Findings:
- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0
- informational: 2

## Review attacks

### 1. Prior maintenance semantics
PASS. v6 imports/composes v5 and does not mutate v1-v5. The existing reconciliation, readiness-dead-end, transition, dispatch, temporal ownership, and dedupe logic remains delegated to v5 before the new content-liveness step.

### 2. Source eligibility
PASS for the active implementation transition. The current producer contract `IMPLEMENTATION / FIRST_PLAYABLE_BOOTSTRAP` and required implementation review contract `IMPLEMENTATION_REVIEW_TEST` are recognized. Factory issues and titles containing `IMPLEMENTATION-READINESS` are explicitly excluded. Sources must also be trusted, open, non-PR `[PLAN-v1]` issues.

### 3. Empty-lane predicate
PASS. v6 does not create an intake while an open trusted content root or prior content-demand intake exists. Matching is prefix-scoped to W2 content or explicit demand-intake/root namespaces rather than generic body text, avoiding the current implementation/review issues merely mentioning content.

### 4. Dedupe and retry
PASS. Open/completed trusted `FACTORY-CONTENT-DEMAND-<source>` issues consume that source. Closed duplicate/not-planned wrappers do not consume it, so a failed materialization attempt cannot permanently dead-end the lane.

### 5. Bounded creation
PASS. A maintenance execution selects at most one unconsumed source and performs at most one intake creation. Concrete implementation producers are preferred over review sources; once producer demand is consumed, a later review/test source can seed a distinct follow-up intake.

### 6. No CONT-08 resurrection
PASS. The generated contract explicitly forbids automatic continuation tranches and permits 1–4 roots only when causally traceable to exact implementation/review/playtest demand. It also permits a bounded no-op instead of inventing backlog.

### 7. Authority boundary
PASS. The intake grants no final canon, implementation, verification PASS, readiness, integration, production/release, legal/provider, or certification authority. Successor roots retain their own review/test/fan-in obligations.

### 8. Workflow wiring
PASS. The workflow compiles v1-v6, runs `frontier_maintenance_v6.py --self-test`, and executes v6 for maintenance. Validation and production entry points therefore cannot silently diverge.

### 9. Changed-path scope
PASS. PR #1374 changes only the new v6 layer, the maintenance workflow entry point, and the producer handoff.

## Independent validation
The exact v6 source was independently reconstructed from the frozen producer blob and passed:
- Python syntax compilation;
- deterministic v6 selection/dedupe self-test under an isolated v5 compatibility stub.

The review environment cannot resolve github.com from the shell, so a full checkout/full-chain local execution was not possible. This is informational rather than correction-requiring because v1-v5 are byte-unchanged, v6 explicitly calls `v5.self_test()`, and the deployed workflow will run the complete composed self-test before maintenance logic on every main push/schedule/dispatch.

## Informational notes
1. The implementation source classifier is deliberately bounded to the current first-playable/gameplay/playable role vocabulary plus implementation-review-test. If future implementation task-class vocabulary changes, the classifier must be extended rather than silently treating unrelated work as demand.
2. Intake dedupe is by source issue, not by every source commit. Current lifecycle provides a second demand source through the implementation-review issue; future long-lived implementation issues should use new bounded successor/review issues rather than relying on endless same-issue commit-driven intake churn.

Neither note blocks the current first-playable factory repair.

## Integration condition
Producer PR #1374 may be squash-integrated only while its head remains exactly `a958c15b8242ffdf86d4d59619a74a6ad164f993`, current main remains merge-compatible, and no newer owner directive invalidates the bounded demand-driven interpretation.
