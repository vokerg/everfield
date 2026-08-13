# W2-REV-03 — Fresh aggregate review of W2-GAME-EV-REM-01

**Issue:** #212  
**Review mode:** `DEGRADED_SINGLE_AGENT_FRESH_EPISODE` with fresh actor/session distinct from Issue #210 producer and Issue #208 reviewer episodes.  
**Claim:** `5283967212`  
**Base:** `main@0838298033347d7234f13ba05e9ad08c244a1f69`  
**Reviewed Issue #210:** terminal status `5283915920`, head `b387a7f27733b52daa0d36f40d2e066041ae90b0`, work `3aa366b24adc66240ba5319b012262f886c0bc14`, PR #211.  
**Disposition:** **CHANGES_REQUIRED — 0 BLOCKER / 3 MAJOR / 0 correction-requiring MINOR**.

This review cold-read the exact frozen model/run/evaluator/result bytes and independently recomputed the mechanical portions before consulting producer dispositions. It does not modify Issue #210.

## 1. What independently reproduces cleanly

The exact Git-blob chain is internally bound:

- model manifest `15e2e3015acd821dfef15fe79ec58537d3642be1`;
- run evidence `eb6cde95d7232f8fec28b17561a457aa716dfb5e`;
- evaluator `f283a5cf6368a4a3f901980fa250eee5a857749b`;
- results `c57be3ef32cb2b915aa736d4c007e671e42680b6`.

Independent calculation from the frozen action effects and 24-action schedules reproduces all four checkpoint/terminal states, no negative resource state, and maximum consecutive low-decision run **2**. The declared foundational and medium/long numeric goal thresholds are satisfied at the specified checkpoints.

Independent calculation also reproduces:

- objective scores and winners: wealth→trader, self-sufficiency→grower, mastery→crafter, social-capital→social, joint-balanced→grower; max objective wins = 2;
- automation utility winners across the 3×3 sweep: manual **1**, partial **3**, strong **5**;
- the retained four-cycle stock pre/conversion/post tuples under the declared cap-conversion rule;
- all eight switching end states from the declared checkpoint states plus recovery action sequences; each retained target-entry predicate is satisfied;
- exact 12-member tranche identity and immutable Issue #197 predecessor linkage.

Accordingly there is no arithmetic-corruption finding. `W2-REV2-M01` is materially improved for exact identity and ordinary schedule-state reconstruction, and the historical negative evidence remains retained.

## 2. MAJOR findings

### W2-REV3-M01 — Optimizer/search and persona-policy classes remain semantic labels over four fixed lifestyle schedules

**Severity:** MAJOR  
**Affects claimed PASS:** `GDF-E2`, `EPA-E3`, `AGE-E3`; also the asserted full closure of `W2-REV2-M02`.

The immutable source questions require:

- `GDF-E2`: optimizer/exploit profiles that can switch across all systems, with dominance judged under meaningful opportunity cost;
- `EPA-E3`: optimizers/search maximizing several objectives independently and jointly;
- `AGE-E3`: actual scripted, bounded-rational, optimizer, and fuzz policies, where different labels must not be cosmetic.

The v2 manifest's `FINITE-POLICY-SEARCH-v2` contains exactly four pre-authored lifestyle schedules (`grower`, `crafter`, `trader`, `social`) and scores those fixed outcomes. It does not retain an optimizer policy generator, action-sequence search frontier, cross-system switching search, search expansion/termination evidence, or independently generated joint-objective candidates. Choosing the highest score among four author-supplied schedules is useful comparison evidence, but it is weaker than the source optimizer/exploit-search question.

Likewise `PERSONA-PORTFOLIO-v2` maps:

- scripted → `POL-GROWER-v2`;
- bounded-rational → `POL-SOCIAL-v2`;
- optimizer → `POL-TRADER-v2`;
- fuzz → `POL-CRAFTER-v2`.

No behavioral algorithm, noise/rationality model, optimizer mechanism, fuzz mutation/generation rule, or per-class decision process is retained. The four traces are meaningfully different **lifestyles**, but the evaluator-class names are assigned after the fact. That is precisely the `AGE-E3` failure mode: persona architecture with cosmetic labels.

**Required correction:** retain deterministic versioned policy mechanisms for at least scripted, bounded-rational/noisy, optimizer, and fuzz classes; run them on the shared exact model; retain generated action/search traces, search frontier/termination or equivalent reconstructable decision evidence; and give the optimizer/exploit path actual cross-system switching/action choice capability. Fixed lifestyle schedules may remain baselines, but cannot by themselves satisfy these three PASS predicates.

### W2-REV3-M02 — Progression mutation and exploit-search PASSes are not mechanically derived from retained executable/closed transformation semantics

**Severity:** MAJOR  
**Affects claimed PASS:** `EPA-E7`, `AGE-E4`; partially reopens `W2-REV2-M01/M02` for these outputs.

The v2 manifest names algorithms in prose, but the retained evidence does not contain a closed executable validator or a machine-complete transformation schema from which the reported mutation/search outputs are forced.

For `EPA-E7`, the base graph is represented as nodes/edges, but the `missing_requirement` and `cycle_injection` mutations are strings such as “requires `RESOURCE_GHOST`” and “A requires B,” while the base graph schema contains no closed requirement-expression field. The run evidence then records the expected detector labels. A fresh reader can understand the intended test, but cannot mechanically apply the mutation to the exact graph object and reproduce the detector outcome without inventing additional semantics.

For `AGE-E4`, the manifest already supplies each seeded fixture's trace, expected classification, and violation text; run evidence repeats the trace/classification. The stated search algorithm (“enumerate … to depth<=4”) has no retained search space, transition generator, enumeration trace/frontier, or validator bytes demonstrating that the search itself discovered the seeded defect rather than simply consuming the provided witness trace. The current packet therefore proves classification of provided examples more strongly than exploit-search discovery.

**Required correction:** publish a deterministic machine-complete progression graph/requirement schema plus mutation application and reachability/cycle validator evidence; and publish a deterministic exploit transition/search corpus or executable validator with retained enumeration/search output. The exact outputs must be recomputable from input objects, not from prose mutation/result pairs.

### W2-REV3-M03 — Automation “new decisions” remain counts without the meaningful decision semantics required by GDF-E4

**Severity:** MAJOR  
**Affects claimed PASS:** `GDF-E4`; `EPA-E4` remains useful payback evidence but does not independently close this GDF requirement.

The automation utility arithmetic is valid and materially improves the historical frontier: manual, partial, and strong tiers each win some tested region. However the manifest represents post-tier decisions only as `new_decisions: 1/3/5`, and the run evidence repeats those counts.

The immutable `GDF-E4` pass condition is qualitative but explicit: each burden reduction must open **meaningful allocation/configuration/expansion/logistics choices** rather than only passive waiting. A monotone integer count does not identify the decision categories, their state/action consequences, or whether they are meaningful rather than renamed toggles. Thus the numeric count is another proxy for the source predicate.

**Required correction:** bind exact decision-category identities and at least one state/action consequence or choice surface per tier (for example allocation, configuration, expansion, logistics/risk/quality where actually modeled), then mechanically show the higher tiers open those choices rather than merely decrement attention. Keep the valid utility/payback sweep; do not weaken it.

## 3. Disposition of W2-REV2 findings

- `W2-REV2-M01`: **PARTIALLY RESOLVED**. Exact model/run/attempt identities and schedule-state reconstruction are now strong; M02 above shows progression/exploit generation still lacks machine-complete derivation.
- `W2-REV2-M02`: **PARTIALLY RESOLVED**. Lifestyle goal evidence and opportunity-cost arithmetic are stronger, but M01/M02/M03 show several source predicates remain weakened.
- `W2-REV2-M03`: **STRUCTURAL CHANGES RETAINED, NOT READY FOR CLOSURE**. Historical burden/automation/stock/switch/persona failures are preserved and several model corrections are real, but one persona-policy failure was converted to labels rather than an actual evaluator-policy mechanism and automation decision semantics remain incomplete.

The producer's `12 PASS / 0 FAIL` normalized object is therefore internally consistent with its evaluator, but **not admissible as 12 source-authoritative PASSes**. Downstream authority must keep at least `GDF-E2`, `GDF-E4`, `EPA-E3`, `EPA-E7`, `AGE-E3`, and `AGE-E4` unresolved until the bounded correction is reviewed.

## 4. Blocker and convergence route

`IR-BLOCKER-GAME-EVIDENCE` remains correctly scoped and **OPEN** for `SCOPE-CORE-GAMEPLAY-v1`. No global mega-gate is introduced.

Exactly one bounded remediation successor is warranted. Recommended mission: `W2-GAME-EV-REM-02`, limited to:

1. real versioned policy mechanisms/search traces for optimizer/cross-system switching and scripted/bounded-rational/fuzz evaluator classes;
2. machine-complete progression mutation + exploit-search derivation;
3. exact semantic automation decision categories/consequences;
4. rerun only the affected exact first-tranche IDs while retaining the complete v1/v2 attempt lineage and unaffected evidence identities where valid;
5. one fresh aggregate review afterward.

Do not spawn one issue per experiment and do not alter historical Issue #197 or #210 bytes.

## 5. Authority boundary

Human fun/player preference remains `INCONCLUSIVE_OUT_OF_SCOPE`. This review grants no engine selection, gameplay/production implementation, release, readiness, verification PASS, legal/provider, integration, or canonical authority. Any eventual integration remains separately authorized and squash-only.
