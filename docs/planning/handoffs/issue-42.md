# Issue #42 Handoff — W1-VERIFY-01

```yaml
issue: 42
mission_id: W1-VERIFY-01
role: verifier
branch: planning/issue-42
base_sha: 413e729e8d2d5ac2eb138903f3f2ace07283b23e
ownership_generation_comment_id: 5249434402
state: DONE
result: FAIL
verification_work_sha: 02251284ed221b0f3fee965413202d865ccc71a9
candidate_work_sha: 434633abe311c48715aa6d610112e798208b020b
manifest_identity: 28146606ff3334ae1ddbb036a48969afb76acb85
adopted_wave_1_contract_blob_sha: d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd
verified_base_main_sha: 413e729e8d2d5ac2eb138903f3f2ace07283b23e
report_path: docs/planning/wave-1/reviews/wave-1-cold-start-verification.md
simulation_artifact_path: docs/planning/wave-1/reviews/wave-1-final-verification-simulation.yaml
simulation_artifact_blob_sha: e9179df108fa1741d7a426a34f450f16dfdd2486
cold_start_input_path: docs/planning/wave-1/reviews/wave-1-final-cold-start-input.yaml
cold_start_input_blob_sha: 70d2b472b14da70572087c652fa29a7080250d7f
blocker_count: 0
major_count: 2
minor_count: 1
independence_mode: DEGRADED_SINGLE_AGENT
trust_level: DEGRADED
resource_constraint_comment_id: 5244416013
remediation_scope: dependency_map_and_promotion_manifest_hard_graph_parity
canonicalizer_ready: false
```

## Verification result

FAIL with 0 BLOCKER / 2 MAJOR / 1 MINOR.

Everything outside dependency-map/compiler parity passed: canonical entry/binding, exact payload/base, all cross-review dispositions, planning-experiment barrier, singular evidence authority, directive/independence boundaries, four OPEN production-readiness blockers, EVIDENCE_REQUIRED states, manifest counts/queue prefix/output schemas/ownership, manifest hard-graph acyclicity, promotion reconstructability, squash-only authority, and exclusion of Issues #59/#60.

## Material findings

### W1V-M01

The foundations dependency type registry does not include `SYNTHESIZES_AFTER_REVIEW`, but the verified dependency map uses that edge type. A canonical consumer would need to invent relation semantics.

### W1V-M02

The promotion manifest contains the correct full hard prerequisites, but the dependency map encodes only ACC/ENG-03/SIM as `BLOCKED_BY`; review/synthesis/verification prerequisites are represented with semantic relation edges rather than the same hard graph. The two canonical promotion artifacts therefore do not expose equivalent hard-dependency authority.

## Narrow remediation required

Use a separate remediation issue/branch. Do not edit the candidate from this verifier episode. The remediation should:

1. encode every promotion-manifest hard prerequisite in the dependency map using registered `BLOCKED_BY` edges in `task -> prerequisite` direction;
2. remove or replace `SYNTHESIZES_AFTER_REVIEW` with registered relation types or supplemental non-readiness metadata;
3. mechanically compare manifest hard prerequisites and dependency-map hard edges for equality;
4. preserve all candidate semantics, counts, readiness blockers, queue prefix, and Wave 2 mission bodies;
5. produce a new exact candidate/dependency/manifest tuple for full verification restart.

The nonblocking symbolic prerequisite-suffix grammar note may be formalized in the same remediation if it can be done without broadening scope.

## Next action

Publish exact schema-3 `VERIFICATION_STATUS(FAIL)` at the final branch head, close Issue #42 for this episode, create one bounded remediation issue, integrate its noncanonical provenance as allowed, then restart W1-VERIFY-01 through the canonical verification-restart lifecycle against the new exact payload.
