# Issue #41 Handoff — W1-SYN-FINAL

```yaml
issue: 41
mission_id: W1-SYN-FINAL
role: final_planning_synthesizer
branch: planning/issue-41
base_sha: 413e729e8d2d5ac2eb138903f3f2ace07283b23e
ownership_generation_comment_id: 5249348414
state: VERIFICATION_READY
candidate_work_sha: 434633abe311c48715aa6d610112e798208b020b
input_manifest_path: docs/planning/wave-1/synthesis/wave-1-final-input.yaml
input_manifest_blob_sha: 62773e3145dea2594ada316e6e8814782f0936db
candidate_path: docs/planning/wave-1/synthesis/wave-1-canonicalization-candidate.md
candidate_blob_sha: 4b4c409dc23538f23aba3709e4af7fafc8f37280
dependency_map_path: docs/planning/wave-1/synthesis/dependency-map.yaml
dependency_map_blob_sha: 1319c92a7a0f35a931ad6a70e87da753a5008f39
promotion_manifest_path: docs/planning/wave-1/synthesis/next-wave-promotion-manifest.yaml
promotion_manifest_blob_sha: 28146606ff3334ae1ddbb036a48969afb76acb85
cross_review_status_comment_id: 5249340288
cross_review_work_sha: d8cd8d16d9a1ca9eae9e51987f86b767992584c2
cross_review_disposition: CHANGES_REQUIRED
cross_review_blocker_count: 1
cross_review_major_count: 11
all_cross_findings_dispositioned: true
next_wave_total: 18
next_wave_initial_ready: 12
next_wave_planning_experiments: 10
next_wave_production_features: 0
implementation_readiness: BLOCKED
required_verifier: W1-VERIFY-01
canonicality: NON_CANONICAL
```

## Completed

- Bound exact W1-SYN-FAC, W1-SYN-TECH, W1-SYN-GAME, and W1-REV-CROSS work/status states.
- Accepted and corrected CD-B01 plus CD-M02 through CD-M12.
- Defined bounded `PLANNING_EXPERIMENT` authority so executable evidence can be collected without opening production/gameplay implementation.
- Collapsed evidence authority to one normative requirement → compiled CheckPlan → execution envelope → derived EvidenceSatisfaction chain.
- Unified durable ArtifactIdentity, directive/policy boundaries, ResourceCapabilityState, trust debt, scoped ImplementationReadinessLedger, evidence-dependency types, game↔runtime mappings, JudgmentPanelRecord, DomainAuthorityMap, and external-evidence freshness.
- Preserved the current master lease-continuation directive as ownership policy provenance only; it does not fabricate empirical PASS or upgrade independent-review capability.
- Kept current schema-3 ownership/dispatcher authority and squash-only integration intact.
- Kept four global production-readiness blockers OPEN: engine decision, platform scope, current accessibility mapping, and evidence foundation.
- Produced a Wave 2 promotion manifest with 18 missions, exactly 12 initially READY, 10 bounded planning experiments, and zero production feature tasks.
- Corrected the Wave 2 title template to `[PLAN-v1][W2-*]` so the current canonical dispatcher can see the promoted issues.
- Corrected dependency-map hard edges to the canonical `BLOCKED_BY` type/direction; no custom inverse semantics remain.
- Excluded retired accidental Issues #59 and #60 from all promotion data.

## Verification focus

W1-VERIFY-01 should cold-start from repository + GitHub state and independently verify:

1. exact candidate/dependency/manifest blobs and current main base;
2. all cross-review BLOCKER/MAJOR dispositions;
3. no production implementation authority leaks through `PLANNING_EXPERIMENT`;
4. one acceptance/evidence authority chain;
5. directive changes cannot rewrite empirical evidence;
6. lease continuation does not imply stronger independence;
7. four global implementation-readiness blockers remain OPEN;
8. every `EVIDENCE_REQUIRED` decision remains unverified;
9. dependency map uses typed, acyclic hard dependencies;
10. manifest has 18 unique missions, 12 initial READY, 10 planning experiments, zero production tasks, known output schemas, unique output/conflict surfaces, current `[PLAN-v1]` queue prefix, and deterministic prerequisite semantics;
11. canonical promotion destinations are mechanically reconstructable;
12. schema-3 and squash-only integration remain authoritative;
13. Issues #59/#60 are excluded.

## Recommended next action

Publish owner `STATUS(VERIFICATION_READY)` at the final handoff head, close Issue #41, then run W1-VERIFY-01 on a fresh degraded-verifier episode without editing this candidate.
