# Issue #208 handoff — W2-REV-02

- mission: `W2-REV-02`
- task class: `ADVERSARIAL_REVIEW / CANONICAL_CANDIDATE`
- review mode: `DEGRADED_SINGLE_AGENT_FRESH_EPISODE`
- ownership generation: Issue #208 comment `5283662524`
- review base: `0838298033347d7234f13ba05e9ad08c244a1f69`
- reviewed Issue #196 status/head/work: `5281402332` / `c9caa318a3a5293f538a3dbd911fae4c667b6a12` / `d32aa80fd77c7caf6995ecb71b311da5a457c3b6`
- reviewed Issue #197 status/head/work: `5281620570` / `19c1266434b9e2c600f3e072e79e7c6840a235d5` / `7716657e8594f61cddd5818150130d52d6238785`
- triggering W2-READY-02 status/finding: `5281448387` / `W2-READY-M02`
- review artifact: `docs/planning/wave-2/reviews/game-evidence-gate-and-tranche-review.md`
- review artifact blob: `a52dac557cf96a8412d3c88bcf16217aeab67243`
- disposition: **CHANGES_REQUIRED**
- findings: `0 BLOCKER / 3 MAJOR / 0 correction-requiring MINOR`

## Findings

1. `W2-REV2-M01` — the experiment packet does not freeze the exact `GameSemanticGraph.graph_version`, rules/content/model identity, policy/seed/horizon identities, generation/search algorithm, or immutable attempt lineage required to reconstruct observations from one exact model.
2. `W2-REV2-M02` — all six historical PASS results (`GDF-E1`, `GDF-E2`, `EPA-E2`, `EPA-E3`, `EPA-E7`, `AGE-E4`) use proxy predicates that materially weaken their immutable Wave-1 source questions. They are not admissible as readiness PASS on the reviewed packet and remain unresolved for downstream authority.
3. `W2-REV2-M03` — the six historical FAIL results expose load-bearing burden, automation, accumulation, switching, and synthetic-policy-diversity weaknesses. `IR-BLOCKER-GAME-EVIDENCE` therefore remains materially OPEN.

## Clean portions retained

- all 54 dependency identities independently account exactly once: 42 grouped / 4 superseded / 8 deferred;
- first-tranche membership is exactly 12 and matches Issue #197;
- `IR-BLOCKER-GAME-EVIDENCE` is accepted as a correctly scoped `SCOPE-CORE-GAMEPLAY-v1` blocker and is not a global mega-gate;
- the normalized 6 PASS / 6 FAIL object faithfully applies the packet's own frozen proxy evaluator; the review defect is the proxy's authority/semantic coverage, not arithmetic corruption;
- synthetic evidence remains non-human-preference evidence.

## Required next

Create exactly one bounded `W2-GAME-EV-REM-01` successor. It must retain Issue #197 as immutable predecessor evidence, freeze exact model/run identities, restore original source predicates, address the retained negative findings without tuning them away, rerun all 12 IDs, and route one fresh aggregate review. Do not create one remediation issue per failed experiment.

Only after a clean fresh review may a bounded synthesis refresh of the authoritative Issue #199 lineage consume the blocker/evidence, followed by fresh readiness verification.

## Authority boundary

No engine selection, gameplay/production implementation, release, readiness, verification PASS, legal/provider, integration, or canonical authority is granted. Any eventual integration is noncanonical review provenance and squash-only.
