# Review — CONT-06 principal-character / relationship candidate

**Mission:** `W2-CONTENT-CHAR-CONT-06-REV-01`  
**Issue:** #1288  
**Judged producer:** #1271 / PR #1287  
**Disposition:** `CHANGES_NEEDED`  
**Canonicality:** `NOT_CANONICAL`  
**Trust mode:** `DEGRADED_SINGLE_AGENT`

## Review basis

This review is bound to canonical Planning Program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, binding Issue #1147 terminal comment `5675066392`, and activation `87c85cecfa9a2ffa464c4b36816a138bf41441af`.

Producer terminal #1271 comment `5816104402` declared this immutable packet:
- head `a243c98f75f78fcd1dd48c2f4ba1cb808625b056`;
- Markdown blob `d414f4951483e054cbe43d6ca0c47476a0ead4e8`;
- YAML blob `e7c1b850e4ae5b9bfd24ed12dcff743a5a83e444`;
- handoff blob `3f7ff8374a18dffadda2087b52e4bab1e1063b54`;
- draft PR #1287;
- ownership generation comment `5815956032`.

The exact terminal bytes remain addressable at commit `a243c98f75f78fcd1dd48c2f4ba1cb808625b056` and match those terminal blob identities.

## Finding

### MAJOR — `SOURCE_OR_REVIEW_IDENTITY_DRIFT`

The live producer route no longer presents the terminal packet as immutable.

After terminal comment `5816104402`, PR #1287 / branch `planning/issue-1271` advanced to head `86a5281df0ec19f03c599eeb68c47a07a97ba8bb`. Its current producer blobs are:
- Markdown `b895d411da0a27dddc2bf29f9a22c4d427978caa`;
- YAML `300142ee9a5e13a40b51469bf5be5b82d72fecc6`;
- handoff `c65d89fe0586c87cdbe9147651540b04494da8e1`.

Those identities differ from the terminal packet. The newer producer bytes also assert ownership generation `5815974757` as valid and characterize earlier claim-shaped comments as non-owning, while the terminal and frozen handoff bind `5815956032`.

The exact-head PR/terminal/ownership identity required by Review #1288 is therefore not stable. A clean review token cannot be granted from this route even though the frozen terminal bytes remain inspectable.

**Required correction:** bounded remediation #1296 / `W2-CONTENT-CHAR-CONT-06-REM-01` must re-derive valid ownership and freeze one exact producer head/blob set behind a correctly rebound producer terminal before a fresh review.

## Required attacks

| # | Attack | Result |
|---|---|---|
| 1 | Exact terminal/head/PR/blob identity; three-path ownership; no sibling CONT-06 mutable consumption | **MAJOR** — terminal packet no longer equals live PR head/blobs; ownership provenance also diverges. |
| 2 | Preserve all 11 inherited states, especially OPEN-002/003/004 = OPEN and OPEN-005 = OPEN_OPTIONAL | CLEAN on frozen terminal bytes. |
| 3 | No final identity, biography, occupation, membership, office, representation, jurisdiction, legitimacy, counterpart, romance/family ending, relationship ending, or canonical arc | CLEAN on frozen terminal bytes. |
| 4 | Agency laundering / scope broadening / refusal override | CLEAN: DEFERRED is not consent-in-waiting; conditional scope broadening and override channels are denied. |
| 5 | Private-information leakage, onward-sharing inference, revocation/history erasure, foundational/private-minimum gating | CLEAN. |
| 6 | Fact/claim/belief/testimony/interpretation/institutional-record/confidence/knowledge/player-exposure/generated-presentation collapse | CLEAN. |
| 7 | Relationship scalarization, weighting, averaging, ranking, or legitimacy/public-standing aliasing | CLEAN; all six dimensions remain independent. |
| 8 | Material history erased by repair/retry/compensation/reconciliation/reinterpretation/renewed contact/later success/presentation | CLEAN; history remains append-only. |
| 9 | Counterpart-slot inference or silent concrete binding | CLEAN; selected person count remains zero and slots may remain unfilled. |
| 10 | Arc ranking/default/progression laundering or mutually exclusive commitments jointly required | CLEAN; composition is non-ranked, non-default, unselected. |
| 11 | Hidden foundational gating or refusal/nonalignment illegality | CLEAN; baseline shared play remains legal. |
| 12 | Six route-cardinality contracts and six recomputation triggers; no fabricated active-route measurement | CLEAN; all six active instances are false with null observed counts; triggers are ACTIVATION, REFUSAL, REJECTION, SUBSTITUTION, RECOVERY, ROUTE_LOSS. |
| 13 | All 17 reopen-condition classes; no future pre-clearance | CLEAN. |
| 14 | Exact-time/schedule/weather/travel/timed-objective/NPC-reachability laundering | CLEAN; exact-time authority remains absent. |
| 15 | High-impact/irreversible activation without separately reviewed BranchImpactEvidence | CLEAN; BIE04 SIGNALING / OBSERVED-EFFECT / CONTINUED-PLAY barrier retained. |
| 16 | Exact WSN preservation | CLEAN: E3 `INCONCLUSIVE_TIMED_COVERAGE_BLOCKED`; E4 `NOT_RUN_BLOCKED_BY_EXACT_PREREQUISITE`; E5 `PASS_BOUNDED_MODEL_ONLY`; E8 `INCONCLUSIVE_SCHEDULE_COVERAGE_BLOCKED`. |
| 17 | Generated-presentation mutation, engine coupling, early fan-in, or higher-authority inflation | CLEAN. |
| 18 | Markdown/YAML/handoff consistency | Frozen terminal artifacts are internally consistent; the blocking inconsistency is the later live-PR/ownership drift captured in Attack 1. |

## Counts and authority

- BLOCKER: **0**
- MAJOR: **1**
- correction-requiring MINOR: **0**
- non-correction observations: **0**
- root review token granted: **false**
- conceptual `W2-CONTENT-SYN-CONT-06` materialized: **false**

This review grants no integration/publication, verification PASS, implementation/readiness, gameplay implementation, engine selection, human-quality, release/production, decision/final-canon, or canonical authority.

## Required next route

Exactly one blocking remediation is routed: Issue #1296, `W2-CONTENT-CHAR-CONT-06-REM-01`.

That remediation must rebind a valid immutable producer packet and route a fresh independent/degraded-independent review. This `CHANGES_NEEDED` review does not grant `W2-CONTENT-CHAR-CONT-06_REVIEWED` and must not be reused as a clean review token.
