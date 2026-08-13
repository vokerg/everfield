# W2-REV-02 — Fresh aggregate review of the core-game evidence gate and first tranche

**Mission:** `W2-REV-02` / Issue #208  
**Task class:** `ADVERSARIAL_REVIEW / CANONICAL_CANDIDATE`  
**Review mode:** `DEGRADED_SINGLE_AGENT_FRESH_EPISODE`  
**Claim:** Issue #208 comment `5283662524`  
**Review base:** `main@0838298033347d7234f13ba05e9ad08c244a1f69`  
**Reviewed gate packet:** Issue #196 status `5281402332`, head `c9caa318a3a5293f538a3dbd911fae4c667b6a12`, work `d32aa80fd77c7caf6995ecb71b311da5a457c3b6`  
**Reviewed experiment packet:** Issue #197 status `5281620570`, head `19c1266434b9e2c600f3e072e79e7c6840a235d5`, work `7716657e8594f61cddd5818150130d52d6238785`  
**Triggering verification:** Issue #205 `VERIFICATION_STATUS(DONE)` comment `5281448387`, result `FAIL`, finding `W2-READY-M02`  
**Disposition:** **CHANGES_REQUIRED** — `0 BLOCKER / 3 MAJOR / 0 correction-requiring MINOR`.

This review does not edit either reviewed packet. It separates defects in evidence authority from legitimate negative empirical evidence. A failed experiment is retained evidence, not a reason to erase the packet; a reported PASS, however, may not exceed the exact evidence predicate it actually proves.

## 1. Independent reconstruction summary

### 1.1 Issue #196 dependency accounting is coherent

Independent enumeration of `game-evidence-dependency-map.yaml` reproduces the declared six immutable source families:

- `RDF-E1..E8` = 8;
- `GDF-E1..E9` = 9;
- `EPA-E1..E9` = 9;
- `WSN-E1..E9` = 9;
- `EXP-E1..E9` = 9;
- `AGE-E1..E10` = 10.

Total: **54** exact experiment identities. The accounting states reproduce as **42 GROUPED / 4 SUPERSEDED / 8 DEFERRED / 0 RETAINED / 0 omitted / 0 duplicated**. The eight deferrals are `RDF-E1`, `RDF-E2`, `RDF-E3`, `RDF-E5`, `RDF-E6`, `RDF-E7`, `RDF-E8`, and `AGE-E8`. The four supersessions are narrowly and explicitly bound: `RDF-E4`, `EXP-E3`, `AGE-E5`, and `AGE-E6`; each preserves the original historical state as `UNRUN_REQUIRED_EVIDENCE`.

The first frontier in the map is exactly the same 12-ID set consumed by Issue #197:

`GDF-E1`, `GDF-E2`, `GDF-E3`, `GDF-E4`, `EPA-E1`, `EPA-E2`, `EPA-E3`, `EPA-E4`, `EPA-E5`, `EPA-E7`, `AGE-E3`, `AGE-E4`.

### 1.2 `IR-BLOCKER-GAME-EVIDENCE` is correctly scoped

The proposed blocker is a `PRODUCT / DOMAIN` blocker for `SCOPE-CORE-GAMEPLAY-v1`. It blocks core-gameplay implementation and the covered gameplay implementation-readiness decision, while explicitly not blocking unrelated tooling/non-gameplay planning. That is consistent with the canonical typed-dependency model and does not invent a project-wide “all evidence must finish” gate.

The blocker therefore remains a valid candidate readiness entry, but it is **OPEN** and cannot resolve from the reviewed Issue #197 packet.

### 1.3 Issue #197 normalized arithmetic reproduces

The frozen corpus/evaluator/result objects are internally consistent at the level of their declared proxy rules:

- lifestyle proxy: four stage-3 runs and four primary families → declared `GDF-E1` / `EPA-E2` proxy PASS;
- dominance proxy: objective primaries have maximum family frequency 2 → declared `GDF-E2` / `EPA-E3` proxy PASS;
- burden: grower/crafter `low_run=21` > threshold 5 → `GDF-E3` FAIL;
- automation utility sweep over 9 cells gives manual 0 wins / partial 1 / strong 8 → `GDF-E4` and `EPA-E4` FAIL;
- terminal stocks exceed threshold 85 for grower food 94, crafter materials 88, trader coin 97 → `EPA-E1` FAIL;
- social→grower has no bounded recovery → `EPA-E5` FAIL;
- progression summary reports 3 monotonic stages, 4 alternatives/stage, zero unknown requirements → declared `EPA-E7` proxy PASS;
- synthetic policy classes collapse to only two primary families → `AGE-E3` FAIL;
- four seeded adversarial rows have explicit expected/observed classifications that agree → declared `AGE-E4` proxy PASS.

Thus the published **6 PASS / 6 FAIL** object is a faithful application of its own frozen evaluator rules. The review findings below concern whether those rules and traces have enough identity and semantic coverage to carry the stronger Wave-1 evidence claims.

## 2. MAJOR findings

### W2-REV2-M01 — Execution/model identity and attempt lineage are not frozen

**Severity:** MAJOR  
**Affects:** all 12 Issue #197 outcomes; especially any positive evidence authority.

The canonical Wave-1 foundation requires an `ExecutionEvidenceEnvelope` to bind exact candidate work/head/base, content/schema package, scenario/policy/actions/seeds, evaluator fingerprints, attempt lineage, nondeterministic surfaces, and coverage gaps. It also states that `GameSemanticGraph.graph_version` is a required claim/coverage identity for lifestyle, progression, route, and game-possibility evidence. The economy/progression source further defines simulation identity fields including `simulation_suite_version`, `ruleset_or_candidate_sha`, `content_set_version`, initial-state profile, persona policy, seed set, horizon, goal set, assumptions, and output schema.

The reviewed Issue #197 corpus instead binds only the Issue #196 packet/dependency-map identity plus its result inputs. It contains trace summaries, thresholds, action strings, and policy-family labels, but no exact `GameSemanticGraph.graph_version`, no ruleset/candidate/content identity, no versioned initial-state/goal set, no persona-policy fingerprints, no seed/horizon identity, no run-generation/search algorithm identity, and no immutable attempt lineage proving how the observations were generated. The report refers to a “frozen abstract graph,” but no graph/model artifact identity is present in the packet.

Consequently a reviewer can reproduce the arithmetic **from the hand-authored frozen observations**, but cannot reconstruct the observations from one exact game model or prove that two later runs labeled the same way execute the same semantics. That falls short of Issue #196's “exact versioned abstract/shared game model with immutable attempt lineage” resolution predicate and Issue #197's own exact scenario/rules/content/graph/policy identity requirement.

**Required correction:** publish a content-addressed model/run manifest that binds, at minimum, the exact graph version, simulation-rules/GameTimePolicy version where applicable, rules/content/candidate identity, initial state, goal set, policy fingerprints, seed/horizon, generator/search algorithm version, evaluator version, and ordered attempt lineage. Re-run or mechanically regenerate the tranche from that exact manifest. The current Issue #197 packet must remain immutable historical evidence; its observations cannot be retroactively assigned a model identity that was not recorded at execution time.

### W2-REV2-M02 — All six reported PASS results use materially weakened proxy predicates

**Severity:** MAJOR  
**Affects:** `GDF-E1`, `GDF-E2`, `EPA-E2`, `EPA-E3`, `EPA-E7`, `AGE-E4`.

The dependency map explicitly reconstructs each evidence question from the immutable Wave-1 §18 source semantics. The Issue #197 evaluator does not preserve those semantics for its PASS cases:

1. **`GDF-E1` / `EPA-E2`:** the proxy passes when runs reach a minimum stage and primary-family count is high enough. The source questions require profiles/policies to sustain medium/long and foundational/specialization goals through materially different routes/mixes, including cross-system dependencies/substitution. Stage attainment plus a label does not demonstrate sustained needs/goals or distinct dependency structure.
2. **`GDF-E2` / `EPA-E3`:** the proxy passes when no objective-primary label occurs more than twice. The source questions require optimizer/exploit search across systems and a showing that no route dominates most goals/resources/objectives with negligible opportunity cost. Counting which family is labeled primary does not establish opportunity cost, joint-objective search, or exploit absence.
3. **`EPA-E7`:** the proxy passes from three summary flags: monotonic stages, alternatives per stage, and zero unknown requirements. The source requires a compiled graph/state-search model with injected missing/changed requirements and detection of accidental cycles/dead ends while explaining intentional exclusions. No fuzz/injection/search trace is retained.
4. **`AGE-E4`:** the proxy passes because four rows' `expected` and `observed` labels match. The source requires an exploit search to find seeded positive loops/gate bypasses/timing-reset exploits and distinguish them from benign high efficiency using constraints/invariants/review. The packet retains classifications but not the search execution or discovery evidence.

These are not harmless implementation details: the proxy rules remove load-bearing parts of the source evidence predicates. Under the canonical authority chain, a `CheckPlan` may specialize execution but may not weaken the `EvidenceRequirement`.

**Review disposition of the historical results:** the six historical FAIL results remain negative evidence. The six reported PASS results are **not admissible as PASS for readiness/satisfaction of their Wave-1 questions** on this packet; for downstream authority they must be treated as unresolved/INCONCLUSIVE until a corrected exact-model execution satisfies the original predicates. This review does not rewrite the immutable Issue #197 result object.

**Required correction:** compile evaluator predicates directly from the source questions and retain the missing evidence dimensions: foundational/specialization goal satisfaction and dependency routes; optimizer/search trajectories and opportunity costs; progression fuzz/injection/cycle evidence; exploit-search discovery traces and constraint/invariant decisions. Thresholds/proxies may remain diagnostics, but cannot replace the source predicate.

### W2-REV2-M03 — Six load-bearing empirical failures keep the core-game blocker materially OPEN

**Severity:** MAJOR  
**Affects:** `GDF-E3`, `GDF-E4`, `EPA-E1`, `EPA-E4`, `EPA-E5`, `AGE-E3`; `IR-BLOCKER-GAME-EVIDENCE`.

Even before correcting M01/M02, the current bounded model reports six direct negative observations:

- repeated low-decision runs reach 21 actions for grower/crafter;
- manual automation wins 0/9 tested utility cells while strong automation wins 8/9;
- representative terminal stocks exceed the frozen accumulation threshold in three resource/persona cases;
- one tested social→grower pivot has no bounded recovery;
- four synthetic policy classes collapse to two primary trajectory families.

These are exactly the kinds of product/evaluator weaknesses the blocker was designed to expose. They may not be erased by averaging, threshold relaxation solely to obtain green results, or by letting technical/factory evidence substitute for game evidence.

**Required correction:** one bounded first-tranche remediation should investigate and correct the common model/design/evaluator causes, then rerun the exact 12-ID tranche under the M01/M02-corrected evidence contract. Preserve the current failed observations as predecessor attempt evidence. The remediation should address burden/relief, automation frontier, source/sink structure, switching viability or explicit intentional exclusion, and synthetic-policy diversity without assuming every issue is solved by numeric tuning.

## 3. Review disposition of the gate

`IR-BLOCKER-GAME-EVIDENCE` is **ACCEPTED AS A CORRECTLY SCOPED OPEN BLOCKER**, not rejected and not resolved.

The gate structure itself does not need to become broader. Its resolution predicate is directionally correct: no required FAIL/INCONCLUSIVE/NOT_RUN for the covered claim, exact model execution, per-experiment outcomes, independent review, and fresh synthesis/readiness disposition. M01/M02 show that Issue #197 has not yet met the exact-execution/evidence-predicate portions of that resolution contract; M03 independently shows the current model has material negative outcomes.

No full-core-game implementation-readiness synthesis may omit the accepted blocker. A narrower readiness scope may exclude `SCOPE-CORE-GAMEPLAY-v1` only if it says so explicitly.

## 4. Required convergence route

Exactly one bounded remediation successor is warranted; do **not** create one issue per failed experiment.

Recommended successor mission: `W2-GAME-EV-REM-01`.

It should:

1. freeze the exact model/graph/rules/content/policy/run identities and immutable predecessor-attempt lineage;
2. restore the original Wave-1 pass/failure semantics rather than proxy-only PASS rules;
3. address the six retained negative findings without laundering them;
4. rerun all 12 exact tranche members and retain independent per-ID results;
5. publish an exact-head review-ready packet for one fresh aggregate review.

After a clean fresh aggregate review, a bounded synthesis refresh of the authoritative Issue #199 lineage may consume the accepted blocker and reviewed evidence, followed by fresh readiness verification. If the blocker remains OPEN after valid evidence, readiness must remain blocked rather than cycling verification to obtain a PASS.

## 5. Authority boundary

This review grants no engine selection, gameplay implementation, production implementation, release approval, implementation readiness, verification PASS, legal/provider, or canonical authority. It does not convert synthetic policy behavior into human fun/preference evidence. Main integration, if separately authorized, is noncanonical review provenance and squash-only.
