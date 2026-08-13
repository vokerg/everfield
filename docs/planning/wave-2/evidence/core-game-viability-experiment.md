# W2-GAME-EV-01 — Core game viability evidence tranche

**Mission:** `W2-GAME-EV-01` / Issue #197  
**Task class:** `PLANNING_EXPERIMENT / EVIDENCE_REQUIRED`  
**Claim base:** `main@0838298033347d7234f13ba05e9ad08c244a1f69`  
**Ownership:** Issue #197 comment `5281469578`  
**Prerequisite:** Issue #196 terminal `REVIEW_READY` comment `5281402332`, head `c9caa318a3a5293f538a3dbd911fae4c667b6a12`, work `d32aa80fd77c7caf6995ecb71b311da5a457c3b6`  
**Dependency-map blob:** `e4f4e964f9b972ebbc22700c7b0a4e23b1c97593`  
**Tranche:** `W2-GAME-EV-CORE-v1` / 12 exact experiment identities  
**Authority:** bounded engine-neutral abstract evidence only.

## 1. Frozen packet

The packet uses one machine-readable trace corpus, one deterministic engine-neutral evaluator rule set, and one normalized result object:

- `core-game-viability-corpus.json` — blob `d1a13be94dc1e37fa9d3990886f70ecf71130c0a`
- `core-game-viability-evaluator.json` — blob `1131ea7b3367bfe1585c03d89ca04897e0b286ce`
- `core-game-viability-results.json` — blob `35939edbb2b7580360bd3c5157dfa24d9657e9bf`

Fresh reconstruction is mechanical: read the frozen corpus, apply each ordered rule and threshold in the evaluator bytes, and compare the resulting per-ID statuses/evidence against the normalized result object. Missing required inputs fail closed; no aggregate scalar may replace an individual experiment result.

The corpus retains the complete 36-action traces for four distinct lifestyle runs plus exact terminal state, primary-family, burden, objective-route, switching, progression, automation, policy-diversity, and seeded-check observations used by this tranche.

## 2. Source-question binding and outcomes

| ID | Wave-1 question | Result |
|---|---|---|
| `GDF-E1` | Lifestyle trajectory viability simulation | **PASS** |
| `GDF-E2` | Dominant-route red team | **PASS** |
| `GDF-E3` | Chore-burden traces | **FAIL** |
| `GDF-E4` | Automation escalation test | **FAIL** |
| `EPA-E1` | Source/sink lifecycle simulation | **FAIL** |
| `EPA-E2` | Lifestyle viability tournament | **PASS** |
| `EPA-E3` | Dominant-route exploit search | **PASS** |
| `EPA-E4` | Automation payback/burden sweep | **FAIL** |
| `EPA-E5` | Switching/catch-up simulation | **FAIL** |
| `EPA-E7` | Progression graph reachability/fuzz | **PASS** |
| `AGE-E3` | Persona diversity benchmark | **FAIL** |
| `AGE-E4` | Exploit-search benchmark / seeded adversarial checks | **PASS** |

Aggregate accounting: **6 PASS / 6 FAIL / 0 INCONCLUSIVE / 0 NOT_RUN**. All 12 selected identities executed and retain independent outcomes.

## 3. Positive bounded findings

### Lifestyle/route viability — `GDF-E1`, `EPA-E2` PASS

Grower, crafter, trader, and social traces all reach stage 3. Their primary action families remain distinct (`grower`, `crafter`, `trader`, `social`), so this frozen abstract graph does not force one nominal lifestyle route.

This is structural route evidence only. It does not establish human preference, pacing quality, or production balance.

### Dominance pressure — `GDF-E2`, `EPA-E3` PASS

Five independent objective searches resolve to primary families: wealth→crafter, self-sufficiency→grower, mastery→crafter, social-capital→social, balanced→grower. No one family is primary for more than two objectives, satisfying the frozen anti-collapse threshold.

This cannot prove absence of strategies outside the bounded model/search surface.

### Progression reachability — `EPA-E7` PASS

The frozen graph has three monotonic stages, four route alternatives at every stage, and zero unknown-resource requirements. No stage becomes a single universal route in this fixture.

### Seeded adversarial classification — `AGE-E4` PASS

Four bounded seeded cases retain expected/observed classifications: three structural defect cases and one benign high-efficiency case. The evaluator preserves the distinction instead of treating high efficiency itself as a defect.

## 4. Load-bearing failures retained

### `GDF-E3` FAIL — repeated low-decision burden

Maximum consecutive low-decision actions are grower **21**, crafter **21**, trader **4**, social **3**, against a frozen threshold of **5**. The grower/crafter trajectories therefore exhibit exactly the indefinitely repeated burden this experiment is intended to reject.

### `GDF-E4` / `EPA-E4` FAIL — automation frontier collapses toward stronger tiers

The frozen 3×3 sweep covers scale `{1,3,8}` × attention-value `{0.5,1.5,3.0}` using the evaluator formula:

`utility = output*scale - setup/amortization_turns - maintenance - attention_value*attention*scale`

Winner counts are manual **0**, partial **1**, strong **8**. Decision categories do increase by tier, but manual play is rational in no tested cell and stronger automation wins too broadly. The evidence therefore fails both escalation and payback/burden questions rather than tuning the fixture post hoc.

### `EPA-E1` FAIL — missing/insufficient sinks

Three representative trajectories exceed terminal-stock threshold **85** after 36 actions:

- grower food **94**;
- crafter materials **88**;
- trader coin **97**.

This is structural source/sink evidence, not a request to flatten rewards numerically.

### `EPA-E5` FAIL — one pivot does not recover

Grower→trader recovers in 2 turns, trader→crafter in 5, and crafter→social in 2. Social→grower does not satisfy the bounded recovery predicate inside the frozen horizon. Switching is therefore not uniformly viable.

### `AGE-E3` FAIL — policy labels overstate trajectory diversity

The four required policy classes resolve to scripted→grower, bounded→grower, optimizer→crafter, fuzz→crafter. Only **2** unique primary families appear against a threshold of **3**. The traces differ, but the benchmark correctly rejects cosmetic persona diversity at the primary-trajectory level.

## 5. Readiness consequence

`IR-BLOCKER-GAME-EVIDENCE` remains **OPEN**.

Issue #196 requires the covered core-game evidence to contain no required `FAIL`, `INCONCLUSIVE`, or `NOT_RUN` before that blocker can resolve. This exact packet contains six material FAILs, so it cannot authorize `SCOPE-CORE-GAMEPLAY-v1` implementation readiness.

The failures should be reviewed and dispositioned as a bounded set; this task does not instantiate one remediation issue per failed experiment. The required next gate remains a fresh/authorized formal aggregate `W2-REV-01` over the exact #196/#197 packet.

## 6. Human-evidence and authority boundary

The normalized result records `human_fun_or_preference_claim: INCONCLUSIVE_OUT_OF_SCOPE`.

Synthetic traces and deterministic rules are evaluation models, not people. They cannot establish fun, emotional pacing, perceived fairness, final content quality, accessibility, release quality, engine suitability, or production readiness.

No engine selection, gameplay implementation, production implementation, release approval, verification PASS, readiness completion, legal/provider, or canonical authority is created.
