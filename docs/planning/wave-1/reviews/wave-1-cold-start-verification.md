# Wave 1 Cold-Start / Coherence Verification

**Mission:** `W1-VERIFY-01`  
**Episode:** `w1-verify-01-verifier-20260811-01`  
**Independence:** `DEGRADED_SINGLE_AGENT` / DEGRADED  
**Result:** **FAIL**  
**Counts:** **0 BLOCKER / 2 MAJOR / 1 MINOR**

## 1. Exact payload verified

Verification started from repository + GitHub state and froze its input before substantive judgment in `docs/planning/wave-1/reviews/wave-1-final-cold-start-input.yaml` (blob `70d2b472b14da70572087c652fa29a7080250d7f`).

Current base: `main@413e729e8d2d5ac2eb138903f3f2ace07283b23e`.

Canonical entry remains valid:

- `AGENTS.md` blob `9f65e73a1f16eb731d4068066998361c060f74bf`;
- `START-HERE.md` blob `515dc7b12e1a85f66e780901c1caa0d9afbc55d5`;
- canonical program blob `e3120ec203c4156328770aa86c12fbb7187966dc`;
- Issue #6 terminal binding comment `5245368879`, squash main SHA `413e729e8d2d5ac2eb138903f3f2ace07283b23e`.

Exact W1-SYN-FINAL payload:

- Issue #41 `STATUS(VERIFICATION_READY)` comment `5249425339`;
- branch head `346bb9df14bbe5dfbd18fbabd05bcbe3b949b3a2`;
- candidate work SHA `434633abe311c48715aa6d610112e798208b020b`;
- foundations candidate blob `4b4c409dc23538f23aba3709e4af7fafc8f37280`;
- dependency map blob `1319c92a7a0f35a931ad6a70e87da753a5008f39`;
- promotion manifest blob `28146606ff3334ae1ddbb036a48969afb76acb85`.

The candidate was immutable during this episode.

## 2. Cold-start and dispatcher result

PASS.

A fresh reader derives:

1. canonical program active under Issue #6 binding;
2. current queue is open `[PLAN-v1]`;
3. open graph before this verifier contains conditional recovery #21, this verifier #42, and blocked canonicalizer #43;
4. exact W1-SYN-FINAL VERIFICATION_READY makes #42 eligible;
5. #43 remains blocked until valid verifier PASS;
6. high-throughput/gameplay implementation remains blocked.

The Wave 2 issue title template correctly stays `[PLAN-v1][W2-*]`, so the current dispatcher can see the next wave after canonicalization.

## 3. Candidate-contract checks that PASS

The candidate successfully closes the prior cross-review architecture findings at the candidate-contract level:

- bounded `PLANNING_EXPERIMENT` permits disposable evidence spikes but forbids production dependency/content authority/engine lock-in;
- one acceptance path exists: TaskClaimContract/EvidenceRequirement → CheckPlan → ExecutionEvidenceEnvelope → derived EvidenceSatisfaction → review/verification/decision;
- one durable `ArtifactIdentity` prevents locator aliases from bypassing provenance/quarantine;
- directives may change goals/policy/resource/ownership assumptions but may not alter observed evidence or fabricate EvidenceSatisfaction;
- the current master lease-continuation directive `5249227987` does not upgrade independent-context capability;
- DEGRADED_SINGLE_AGENT trust debt remains visible;
- four global `PRODUCTION_IMPLEMENTATION` blockers remain OPEN: engine decision, platform scope, current accessibility mapping, evidence foundation;
- engine choice, mature GitHub lock/CAS, cross-runtime hash authority, concrete ordering/migration/protected/evaluator/simulation/CI mechanisms remain `EVIDENCE_REQUIRED` or `DEFERRED`;
- game-time, semantic-graph, generative-runtime and technical replay/evidence identities are explicitly mapped;
- current schema-3 and squash-only integration remain authoritative;
- retired accidental Issues #59/#60 are excluded.

## 4. Promotion-manifest mechanical checks that PASS

Independent derivation from manifest version 2 confirms:

- 18 unique missions (≤24);
- exactly 12 initially READY (≤12);
- 10 `PLANNING_EXPERIMENT` missions;
- zero production-feature missions;
- current `[PLAN-v1]` queue prefix;
- known output schemas only (`proposal_research_v1`, `adversarial_review_v1`, `synthesis_v1`, `verification_v1`);
- unique conflict keys and noncolliding output surfaces (apart from the single mission owning its own synthesis directory/two files);
- original `next_wave_candidate_schema` required fields are present on every mission;
- manifest hard-prerequisite graph is acyclic.

Independent topological layers:

```text
Layer 0: AUTH, GH, ENG-01, ENG-02, HASH, MIG, ORDER, PROTECT, CI, EVAL, PLAT, RIGHTS
Layer 1: ACC, ENG-03
Layer 2: SIM
Layer 3: REV
Layer 4: SYN
Layer 5: READY
```

## 5. MAJOR finding W1V-M01 — dependency-map edge type registry mismatch

The final foundations candidate registers typed dependency relations including:

`BLOCKED_BY`, `BLOCKS_DECISION`, `BLOCKS_IMPLEMENTATION_SCOPE`, `BLOCKS_RELEASE_SCOPE`, `INFORMS_DECISION`, `CALIBRATES_EVALUATOR`, `REOPENS_ON_FAILURE`, `REVIEW_OF`, `SYNTHESIZES`, `VERIFIES`, `CANONICALIZES`, `INTERFACE_WITH`, `CONFLICTS_WITH`, `SUPERSEDES`, and `INVALIDATES`.

The exact verified dependency map instead contains an undeclared edge type:

`SYNTHESIZES_AFTER_REVIEW`.

A fresh compiler cannot treat an unregistered relation as equivalent to `SYNTHESIZES` or `BLOCKED_BY` without inventing policy. Because the dependency map is a canonicalization output and final verification explicitly requires typed dependency correctness, PASS is forbidden.

**Required remediation:** use only registered relation kinds, or deliberately revise the foundations type registry through the same review/verification route.

## 6. MAJOR finding W1V-M02 — dependency-map hard graph is weaker than promotion manifest

The promotion manifest correctly declares hard prerequisites for:

- `W2-REV-01`: all 15 root/evidence missions at REVIEW_READY;
- `W2-SYN-01`: qualifying W2-REV-01 result;
- `W2-READY-01`: W2-SYN-01 VERIFICATION_READY.

The dependency map does not encode those as complete `BLOCKED_BY` hard edges. It uses `REVIEW_OF` for review inputs and `SYNTHESIZES_AFTER_REVIEW` / `VERIFIES` for the final chain.

A consumer deriving the hard graph from `BLOCKED_BY` edges in `WAVE-1-DEPENDENCY-MAP-v1.yaml` would therefore see only ACC/ENG-03/SIM prerequisites and a weaker graph than the promotion manifest.

This violates the candidate's goal of singular, mechanically composable authority and makes the two promotion artifacts non-equivalent.

**Required remediation:** make the dependency map mechanically mirror **every** promotion-manifest hard prerequisite using `BLOCKED_BY` edges in `task → prerequisite` direction. Supplemental relation edges may remain only if they are registered and cannot change readiness semantics.

## 7. MINOR W1V-m01 — symbolic prerequisite suffix grammar

Manifest prerequisites consistently use literals such as `W2-PLAT-01_REVIEW_READY`, `W2-REV-01_PASS_OR_CHANGES_REQUIRED`, and `W2-SYN-01_VERIFICATION_READY`; the compiler contract defines the corresponding terminal meanings.

This is sufficient to understand the current bounded manifest, but a later compiler should formalize the string grammar or use structured prerequisite objects rather than rely indefinitely on suffix convention.

This is nonblocking for the current remediation because the exact strings and meanings are unambiguous in one bounded manifest.

## 8. Simulation evidence

Immutable simulation artifact:

`docs/planning/wave-1/reviews/wave-1-final-verification-simulation.yaml` blob `e9179df108fa1741d7a426a34f450f16dfdd2486`.

It records PASS/FAIL per verification obligation, independent topological layering, counts, and exact findings.

## 9. Result and routing

**FAIL** — 0 BLOCKER / 2 MAJOR / 1 MINOR.

The failure is narrow: foundations semantics, promotion manifest, readiness barriers, and Wave 2 composition are otherwise acceptable. Remediation should modify only the dependency-map/compiler-parity surface (and, if desired, formalize the nonblocking prerequisite grammar) on a separate remediation issue/branch. The verifier must not edit the candidate it judges.

After remediation is integrated as noncanonical provenance and a new exact candidate/dependency/manifest tuple exists on current main/provenance as required by the workflow, W1-VERIFY-01 should re-enter through the canonical verification restart path and rerun the full suite.

## 10. Independence profile

This is **DEGRADED_SINGLE_AGENT**, not full independence:

- distinct verifier episode from W1-SYN-FINAL and W1-REV-CROSS;
- candidate immutable;
- cold-start input manifest frozen before judgment;
- repository/GitHub evidence acquired before reconciling prior rationale;
- source candidate never edited by verifier;
- resource constraint comment `5244416013` retained;
- reopen condition remains `MULTI_AGENT_OR_ISOLATED_CONTEXT_AVAILABLE`.
