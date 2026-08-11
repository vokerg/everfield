# Issue #40 Handoff — W1-REV-CROSS

```yaml
issue: 40
mission_id: W1-REV-CROSS
role: independent_cross_domain_reviewer
branch: planning/issue-40
base_sha: 413e729e8d2d5ac2eb138903f3f2ace07283b23e
ownership_generation_comment_id: 5249316118
state: DONE
disposition: CHANGES_REQUIRED
review_work_sha: d8cd8d16d9a1ca9eae9e51987f86b767992584c2
review_artifact: docs/planning/wave-1/reviews/cross-domain-interface-and-parallelism.md
input_manifest: docs/planning/wave-1/reviews/cross-domain-review-input.yaml
input_manifest_blob_sha: c69cab08ff8b6259078d8d27fd962063d0112615
blocker_count: 1
major_count: 11
minor_count: 4
note_count: 2
independence_mode: DEGRADED_SINGLE_AGENT
trust_level: DEGRADED
resource_constraint_comment_id: 5244416013
candidate_edit_prohibited: true
reopen_condition: MULTI_AGENT_OR_ISOLATED_CONTEXT_AVAILABLE
downstream_mission: W1-SYN-FINAL
```

## Completed

- Frozen exact REVIEW_READY W1-SYN-FAC, W1-SYN-TECH, and W1-SYN-GAME states before cross-domain reconciliation.
- Attacked authority collisions, circular evidence/readiness dependencies, replay/game mappings, protected trust, schema ownership, scheduler behavior, current-research freshness, and next-wave compiler semantics.
- Recorded `CHANGES_REQUIRED` with 1 BLOCKER / 11 MAJOR / 4 MINOR / 2 NOTE.
- Did not edit any synthesis candidate.

## Required final-synthesis corrections

- CD-B01: define bounded `PLANNING_EXPERIMENT` authority distinct from production/gameplay implementation.
- CD-M02: one compilation chain from normative evidence requirement → CheckPlan → evidence attempts → EvidenceSatisfaction.
- CD-M03: make factory `ArtifactIdentity` the sole durable artifact identity used by technical/game evidence.
- CD-M04: human directives may supersede policy/requirements but cannot fabricate empirical PASS; requirement change creates a new policy/claim version.
- CD-M05: one scoped `ImplementationReadinessLedger`.
- CD-M06: typed evidence dependency edges that block only the decisions/scopes they actually govern.
- CD-M07: exact mapping of GameTimePolicy/GameSemanticGraph/GenerativeRuntimeBoundary into technical replay/state/evidence identities.
- CD-M08: unified subjective `JudgmentPanelRecord` over factory trust + technical evaluator fingerprints/evidence.
- CD-M09: explicit DomainAuthorityMap/interface ownership with generated cross-domain indexes.
- CD-M10: shared event/version-sensitive external-evidence freshness lifecycle.
- CD-M11: next-wave promotion/compiler schema must preserve experiment class, ownership, evidence predicates, risk/review route, readiness scope, and anti-leakage semantics.
- CD-M12: current lease-owner directive and independent-execution capability are distinct resource facts; trust debt remains DEGRADED until stronger evidence exists.

## Recommended next action

Publish exact `REVIEW_STATUS`, close Issue #40, then execute W1-SYN-FINAL as the only correction surface. Final synthesis must retain all unrun empirical work and the implementation barrier while emitting the required dependency map and bounded next-wave promotion manifest.
