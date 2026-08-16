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

During producer recheck, `main` advanced to `3de6f8f276cd1479ceccdea7362420f1e0efa030` by squash-publishing the exact #430 changes-required review provenance. That commit explicitly does not publish #428, clear WSN evidence, or supersede remediation #432. The claim-time base and immutable predecessor/review identities above therefore remain the authority for this remediation episode.

The predecessor packet was reproduced exactly by #430. This episode changes only the four semantic-coverage defects found by that review; E1/E6/E7/E9 and the E4 blocker remain bounded as before.

## Remediation closure

### WSN-R4 / E2 — CLOSED IN PRODUCER SCOPE

The corpus contains explicit unauthorized-access attacks for player visibility, relationship state, social standing, and generated presentation. Those contexts are evidence inputs but are not authorization sources. The evaluator authorizes fact access only from retained explicit knowledge or explicit lawful disclosure, while separately preserving belief-vs-objective handling.

Negative cases for all four leak classes produce `FORBIDDEN_KNOWLEDGE_REVEAL`. The evaluator requirement set names each attack class independently, so omission of one prevents a clean E2 PASS.

### WSN-R2 / E3 — CLOSED FOR NON-TIMED SUBCOVERAGE; TIMED LIMIT RETAINED

Representative quest classes have distinct executable structure rather than a shared `start -> goal` graph:

- linear requires a multi-step single route;
- optional requires direct completion plus a longer optional detour;
- branching requires multiple start alternatives that independently reach the goal;
- social uses an explicit social prerequisite and granted agreement state;
- collection requires multiple item tokens that are actually granted before the goal;
- world-state requires a world-state gate granted by a prior action;
- failure/retry/recovery contains an explicit failure edge, recovery token and retry gate;
- alternative-route contains a blocked prerequisite route plus an independently solvable route;
- dead-end and cycle controls remain deliberately unsolvable and structurally checked.

Timed coverage remains blocked because no reviewed `GameTimePolicy` identity or concrete timed instance exists. E3 therefore remains `INCONCLUSIVE`, not PASS.

### WSN-R1 / E5 — CLOSED IN BOUNDED MODEL

E5 performs an explicit pipeline:

1. apply the branch choice to version-1 state;
2. deterministically JSON-serialize that state;
3. mutate the live in-memory state **after** serialization with an unserialized sentinel;
4. reload from the retained serialized bytes, which must remove that post-save mutation;
5. migrate to explicit schema version 2 while preserving named fields and adding explicit defaults;
6. replay downstream availability from migrated branch facts;
7. compare facts/history/schema and availability with explicit expected post-state.

The skip-reload injection deliberately consumes the mutated live object instead of serialized bytes; `RELOAD_NOT_PERFORMED` is then derived from the surviving post-save sentinel, not directly from the fault label. Skip-migration, history-loss, and availability-corruption controls retain their expected diagnostics. This is bounded model evidence only and does not validate production persistence.

### WSN-R3 / E8 — CLOSED FOR EXECUTABLE SUBCOVERAGE; SCHEDULE LIMIT RETAINED

Long-horizon traces assert, emit, and retain:

- typed `trust` / `respect` / `tension` relationship dimensions;
- exact durable event history;
- exact authorized knowledge state;
- unauthorized-knowledge rejection.

A scalar-collapse fault produces `RELATIONSHIP_DIMENSION_COLLAPSE`; a history-loss fault produces `MATERIAL_HISTORY_LOSS`. Distinct 12-period policies retain different typed relationship/history states. Quest-dependency reachability remains exercised.

Required-NPC reachability and schedule-deadlock predicates remain blocked because concrete schedules and a reviewed time policy are absent. E8 therefore remains `INCONCLUSIVE`.

## Deterministic re-run

Invocation:

```text
python docs/planning/wave-2/evidence/wsn-world-structure-evaluator.py --corpus docs/planning/wave-2/evidence/wsn-world-structure-corpus.json --output /tmp/wsn-world-structure-results.json
```

Retained identities after producer recheck:

- corpus Git blob: `922c2838396e6fbc8b27248d0b56b8635112059f`
- corpus SHA-256: `37fb1bca327770de5208465baec54f59641a22173c17c6709e2e1baf2bba5260`
- evaluator Git blob: `9471520355e79d4358de01bfe363905bf3de962c`
- evaluator SHA-256: `5e1e649c10715e18c8941372f4474230ca33533ad8c9f14056493925fc7d7164`
- results Git blob: `6c75ec437fb8f1a333614c6c2f8336683247bb55`
- results SHA-256: `2b8f7df42a8cf2d025594987b973c0a48cfd9f810cf8d33d5fa776fae41f94f3`
- evaluator version: `wsn-world-structure-evaluator-v3-rem2`
- retained cases: **46**
- expectation mismatches: **0**

Results:

| ID | Outcome | Limit |
|---|---|---|
| E1 | PASS | unchanged bounded contradiction/chronology/branch evidence |
| E2 | PASS | all required leak contexts mechanically covered |
| E3 | INCONCLUSIVE | timed quest coverage blocked |
| E4 | NOT_RUN | reviewed time policy + concrete schedules absent |
| E5 | PASS | bounded serialization/reload/migration/availability replay |
| E6 | PASS | unchanged bounded generated-grounding evidence |
| E7 | PASS | unchanged bounded sameness evidence |
| E8 | INCONCLUSIVE | schedule/NPC-reachability coverage blocked |
| E9 | PASS | unchanged bounded critic-calibration evidence |

Counts remain **6 PASS / 2 INCONCLUSIVE / 1 NOT_RUN**. The unchanged aggregate shape is intentional: remediation strengthens executable support beneath E2/E3/E5/E8 without manufacturing missing time/schedule prerequisites.

## Producer recheck and adversarial checks

The remediated packet was re-attacked specifically against #430 findings:

- E2: all four leak contexts remain independent required coverage and cannot authorize character knowledge;
- E3: the positive fixtures are mechanically distinct and predicate-gated rather than class labels;
- E5: the retained run is clean, and a deliberate evaluator mutant that bypasses reload for every case causes E5 to become `FAIL / EXPECTATION_MISMATCH`, with five cases mismatching because the post-save sentinel survives;
- E5: skip migration, history loss, and bad availability replay retain their negative diagnostics;
- E8: scalar relationship collapse and material history loss remain observable failures, with exact knowledge/history end-state assertions;
- E3/E8 blocked coverage and E4 NOT_RUN remain visible and cannot be averaged away.

Producer self-review in scope after this recheck: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR**.

## Required next gate

A fresh independent/degraded-independent aggregate review of this exact remediation packet is mandatory before any WSN result is consumed as reviewed bounded evidence. The reviewer must reproduce the retained bytes/results, re-attack WSN-R1..R4, check clean-surface regressions, and verify E3/E8/E4 limitations remain fail-closed.

Suggested mission: `W2-REV-WSN-REM-01`.

No integration, canonicalization, human-quality, production-persistence/schedule, implementation-readiness, verification-PASS, engine-selection, release, or decision authority is created here.
