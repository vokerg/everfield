# Issue #197 handoff — W2-GAME-EV-01

- mission: `W2-GAME-EV-01`
- task class: `PLANNING_EXPERIMENT / EVIDENCE_REQUIRED`
- ownership generation: Issue #197 comment `5281469578`
- claim base: `0838298033347d7234f13ba05e9ad08c244a1f69`
- prerequisite: Issue #196 terminal `REVIEW_READY` comment `5281402332`
- prerequisite head/work: `c9caa318a3a5293f538a3dbd911fae4c667b6a12` / `d32aa80fd77c7caf6995ecb71b311da5a457c3b6`
- dependency-map blob: `e4f4e964f9b972ebbc22700c7b0a4e23b1c97593`
- tranche: `W2-GAME-EV-CORE-v1`
- exact experiment count: **12**
- required next gate: fresh/authorized formal aggregate `W2-REV-01`

## Frozen evidence packet

- report: `docs/planning/wave-2/evidence/core-game-viability-experiment.md` / blob `9f42f00da8ac2778fe0685304dc2a1f8a02321b4`
- corpus/traces: `docs/planning/wave-2/evidence/core-game-viability-corpus.json` / blob `d1a13be94dc1e37fa9d3990886f70ecf71130c0a`
- deterministic evaluator rules: `docs/planning/wave-2/evidence/core-game-viability-evaluator.json` / blob `1131ea7b3367bfe1585c03d89ca04897e0b286ce`
- normalized results: `docs/planning/wave-2/evidence/core-game-viability-results.json` / blob `35939edbb2b7580360bd3c5157dfa24d9657e9bf`

Fresh reconstruction applies the frozen evaluator rules to the frozen corpus and compares the per-ID output to the normalized result object. Missing required inputs fail closed; no aggregate scalar replaces individual outcomes.

## Result

All 12 selected IDs executed:

- PASS: `GDF-E1`, `GDF-E2`, `EPA-E2`, `EPA-E3`, `EPA-E7`, `AGE-E4`
- FAIL: `GDF-E3`, `GDF-E4`, `EPA-E1`, `EPA-E4`, `EPA-E5`, `AGE-E3`
- INCONCLUSIVE: 0
- NOT_RUN: 0

Load-bearing retained failures:

1. grower/crafter low-decision runs reach 21 actions vs threshold 5;
2. manual automation wins no tested cell while strong automation wins 8/9;
3. terminal stock exceeds 85 for grower food (94), crafter materials (88), and trader coin (97);
4. social→grower switching does not recover inside the bounded horizon;
5. four synthetic policy classes collapse to only two primary trajectory families.

`IR-BLOCKER-GAME-EVIDENCE` remains OPEN. Human fun/player preference remains `INCONCLUSIVE_OUT_OF_SCOPE`.

## Authority boundary

This is bounded engine-neutral abstract evidence only. It grants no engine selection, gameplay implementation, production implementation, release, verification PASS, readiness completion, legal/provider, or canonical authority.

A fresh/authorized aggregate `W2-REV-01` must independently review the exact #196/#197 packet before synthesis or remediation consumes these results.
