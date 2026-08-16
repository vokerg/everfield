# W2-GAME-EV-WSN-REM-01 — WSN semantic-coverage remediation

**Issue:** #432  
**Predecessor:** #428 / PR #429 at `7da4412f8ebb218dc2e9b7534d048aab878ac261`  
**Required review:** #430 / PR #431 at `f0f871ecda2b0044349b9ec333b99986f20406ae`  
**Review disposition:** `CHANGES_REQUIRED` — 0 BLOCKER / 4 MAJOR / 0 correction-requiring MINOR  
**Canonicality:** `NOT_CANONICAL`

## Frozen authority

- claim base `main`: `aa906611b8d107e0d4cc531d3c1c380d6b2c0647`
- Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical binding comment: `5245368879`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- Issue #196 dependency map blob: `e4f4e964f9b972ebbc22700c7b0a4e23b1c97593`
- W1-DES-03 source blob: `35b7acfd369143f6f1f48dcd1cf43ca90280fee5`
- clean content-fan-in review terminal: `5307505361`
- predecessor terminal: `5307798635`
- blocking review terminal: `5307825590`
- blocking review report blob: `0383094398c69362354679cf389a6d666dc9910e`

The predecessor packet was reproduced exactly by #430. This episode changes only the four semantic-coverage defects found by that review; E1/E6/E7/E9 and the E4 blocker remain bounded as before.

## Remediation closure

### WSN-R4 / E2 — CLOSED IN PRODUCER SCOPE

The corpus now contains explicit unauthorized-access attacks for player visibility, relationship state, social standing, and generated presentation. Those contexts are evidence inputs but are not authorization sources. The evaluator authorizes fact access only from retained explicit knowledge or explicit lawful disclosure, while separately preserving belief-vs-objective handling.

Negative cases for all four leak classes produce `FORBIDDEN_KNOWLEDGE_REVEAL`. E2 cannot obtain full required coverage if any attack class is absent.

### WSN-R2 / E3 — CLOSED FOR NON-TIMED SUBCOVERAGE; TIMED LIMIT RETAINED

Representative quest classes now have distinct executable structure rather than a shared `start -> goal` graph:

- linear requires a multi-step single route;
- optional requires direct completion plus a longer optional detour;
- branching requires multiple start alternatives that independently reach the goal;
- social uses an explicit social prerequisite and granted agreement state;
- collection requires multiple item tokens that are actually granted before the goal;
- world-state requires a world-state gate that is granted by a prior action;
- failure/retry/recovery contains an explicit failure edge, recovery token and retry gate;
- alternative-route contains a blocked prerequisite route plus an independently solvable route;
- dead-end and cycle controls remain deliberately unsolvable and structurally checked.

Timed coverage is still blocked because no reviewed `GameTimePolicy` identity or concrete timed instance exists. Therefore E3 correctly remains `INCONCLUSIVE`, not PASS.

### WSN-R1 / E5 — CLOSED IN BOUNDED MODEL

E5 now performs an explicit pipeline:

1. apply branch choice to a version-1 state;
2. deterministically JSON-serialize that state;
3. JSON-reload from retained bytes;
4. migrate to explicit schema version 2 while preserving named fields and adding explicit defaults;
5. evaluate downstream availability rules from migrated branch facts;
6. compare migrated facts/history/schema and replayed availability with explicit expected post-state.

Fault controls deliberately skip reload, skip migration, drop history, and corrupt availability replay. Each produces its expected diagnostic. This is bounded model evidence only and does not validate a production persistence implementation.

### WSN-R3 / E8 — CLOSED FOR EXECUTABLE SUBCOVERAGE; SCHEDULE LIMIT RETAINED

Long-horizon traces now assert, emit, and retain:

- typed `trust` / `respect` / `tension` relationship dimensions;
- exact durable event history;
- exact authorized knowledge state;
- unauthorized-knowledge rejection.

A scalar-collapse fault must produce `RELATIONSHIP_DIMENSION_COLLAPSE`; a history-loss fault must produce `MATERIAL_HISTORY_LOSS`. Distinct 12-period policies retain different typed relationship/history states. Quest-dependency reachability remains exercised.

Required-NPC reachability and schedule-deadlock predicates remain blocked because concrete schedules and a reviewed time policy are absent. E8 therefore remains `INCONCLUSIVE`.

## Deterministic run

Invocation:

```text
python docs/planning/wave-2/evidence/wsn-world-structure-evaluator.py --corpus docs/planning/wave-2/evidence/wsn-world-structure-corpus.json --output /tmp/wsn-world-structure-results.json
```

Retained identities:

- corpus SHA-256: `37fb1bca327770de5208465baec54f59641a22173c17c6709e2e1baf2bba5260`
- evaluator SHA-256: `9cf85fc6579082f4279311e04c8b70bc7827d9dabac9d0806b581d782ae7adc6`
- retained cases: **46**
- expectation mismatches: **0**

Results:

| ID | Outcome | Limit |
|---|---|---|
| E1 | PASS | unchanged bounded contradiction/chronology/branch evidence |
| E2 | PASS | all required leak contexts now mechanically covered |
| E3 | INCONCLUSIVE | timed quest coverage blocked |
| E4 | NOT_RUN | reviewed time policy + concrete schedules absent |
| E5 | PASS | bounded explicit serialization/reload/migration/availability replay |
| E6 | PASS | unchanged bounded generated-grounding evidence |
| E7 | PASS | unchanged bounded sameness evidence |
| E8 | INCONCLUSIVE | schedule/NPC-reachability coverage blocked |
| E9 | PASS | unchanged bounded critic-calibration evidence |

Counts remain **6 PASS / 2 INCONCLUSIVE / 1 NOT_RUN**. The unchanged aggregate shape is intentional: remediation strengthens the executable support beneath E2/E3/E5/E8 without manufacturing the missing time/schedule prerequisites.

## Self-review

The remediated packet was attacked specifically against #430 findings:

- removing/accepting any E2 leak class prevents the intended authority behavior;
- collapsing E3 positive fixtures back to labels-only structure triggers class-specific semantic diagnostics;
- skipped reload/migration, lost history, or wrong availability are detected in E5;
- scalar relationship collapse and material history loss are detected in E8;
- E3/E8 blocked coverage and E4 NOT_RUN remain visible and cannot be averaged away.

Producer self-review in scope: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR**.

## Required next gate

A fresh independent/degraded-independent aggregate review of this exact remediation packet is mandatory before any WSN result is consumed as reviewed bounded evidence. The reviewer must reproduce the retained bytes/results, re-attack WSN-R1..R4, check clean-surface regressions, and verify E3/E8/E4 limitations remain fail-closed.

Suggested mission: `W2-REV-WSN-REM-01`.

No integration, canonicalization, human-quality, production-persistence/schedule, implementation-readiness, verification-PASS, engine-selection, release, or decision authority is created here.
