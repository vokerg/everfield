# W2-REV-WSN-REM-01 — Aggregate review of remediated WSN evidence

**Issue:** #437  
**Judged remediation:** #432 / PR #436  
**Judged head:** `6bf56ccc25db8deccf2b6a5f35e5d5de4586bd77`  
**Trust mode:** `DEGRADED_SINGLE_AGENT`  
**Disposition:** `CLEAN_FOR_BOUNDED_WSN_CONSUMPTION`  
**Finding counts:** 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR  
**Canonicality:** `NOT_CANONICAL`

## Frozen identity

Review was performed against immutable remediation Issue #432 at exact head `6bf56ccc25db8deccf2b6a5f35e5d5de4586bd77`, draft PR #436, with:

- substantive remediation work `27508bcd166645b013fb8a312e642382963b2cfa`;
- report blob `0feb04a4a9bfdc71893ab3619621f62f862858f7`;
- corpus blob `922c2838396e6fbc8b27248d0b56b8635112059f`;
- evaluator blob `9471520355e79d4358de01bfe363905bf3de962c`;
- results blob `6c75ec437fb8f1a333614c6c2f8336683247bb55`;
- handoff blob `20da87f69a992f6116cddf1085151b4f30936bd7`.

The judged branch/PR was not edited. Review base is `main@3de6f8f276cd1479ceccdea7362420f1e0efa030`. Canonical Planning Program v1 remains blob `e3120ec203c4156328770aa86c12fbb7187966dc`, binding comment `5245368879`, activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e`.

Predecessor aggregate review #430 terminal `5307825590` returned `CHANGES_REQUIRED`, 0 BLOCKER / 4 MAJOR / 0 correction-requiring MINOR, findings WSN-R1 through WSN-R4 affecting E5, E3, E8, and E2 respectively.

## Independent reproduction

Exact retained corpus and evaluator bytes were reconstructed from the judged Git blobs and independently hashed before execution.

Environment: CPython `3.13.5`.

Invocation equivalent to:

```text
python wsn-world-structure-evaluator.py --corpus wsn-world-structure-corpus.json --output reproduced-results.json
```

Identity checks:

- corpus SHA-256: `37fb1bca327770de5208465baec54f59641a22173c17c6709e2e1baf2bba5260` — exact;
- evaluator SHA-256: `5e1e649c10715e18c8941372f4474230ca33533ad8c9f14056493925fc7d7164` — exact;
- reproduced results SHA-256: `2b8f7df42a8cf2d025594987b973c0a48cfd9f810cf8d33d5fa776fae41f94f3` — exact retained result;
- evaluator version: `wsn-world-structure-evaluator-v3-rem2`;
- retained/reproduced cases: 46;
- expectation mismatches: 0;
- reproduced outcome counts: 6 PASS / 2 INCONCLUSIVE / 1 NOT_RUN.

The exact deterministic packet therefore reproduces byte-for-byte at the normalized result boundary.

## Re-attack of prior MAJOR findings

### WSN-R4 / E2 — CLOSED

The exact corpus contains separate no-access attacks for player visibility, relationship state, social standing, and generated presentation. The evaluator derives fact authorization only from explicit retained knowledge or explicit lawful access; none of the four context classes grants knowledge.

Fail-closed attacks performed by this review:

- removing the relationship-state attack makes E2 `INCONCLUSIVE` with missing `relationship_state_leak` coverage;
- changing that attack to grant explicit access while retaining the expected forbidden result makes E2 `FAIL` by expectation mismatch.

Belief remains distinct from objective fact and lawful disclosure remains independently representable. WSN-R4 is closed in the exact bounded packet.

### WSN-R2 / E3 — CLOSED FOR EXECUTABLE SUBCOVERAGE; REQUIRED LIMIT RETAINED

The non-timed fixtures are materially distinct machine structures and the evaluator checks their semantics rather than merely their class labels: linear sequencing, optional detour, independent branches, social prerequisites/grants, multi-item collection, world-state grant/gate, failure/recovery/retry token, blocked-vs-open alternative route, deliberate dead end, and reachable cycle.

Fail-closed attacks performed by this review include collapsing the optional fixture to a trivial direct path, which produces `OPTIONAL_ROUTE_SEMANTICS_MISSING` and makes E3 fail. Removing the actual social prerequisite structure likewise yields a `SOCIAL_PREDICATE_MISSING` mismatch.

Timed quest coverage remains explicitly blocked because reviewed `GameTimePolicy` identity and concrete timed instances do not exist. E3 correctly remains `INCONCLUSIVE`, not PASS. WSN-R2 is closed for the executable non-timed scope without laundering the missing timed prerequisite.

### WSN-R1 / E5 — CLOSED IN THE BOUNDED MODEL

The exact evaluator performs observable operations in sequence: version-1 state construction, deterministic serialization, post-save live-state sentinel mutation, reload from retained serialized bytes, explicit migration to schema version 2 with named preservation/defaults, and downstream availability replay from migrated branch facts.

The skip-reload control detects the surviving post-save sentinel as `RELOAD_NOT_PERFORMED`; skip-migration, history-loss, and availability-corruption controls retain independent diagnostics.

This review additionally replaced the evaluator's reload selection globally with direct live-state reuse, without changing corpus fault labels. The mutant makes E5 `FAIL` with exactly five expectation mismatches: `reversible`, `irreversible`, `drop-history-control`, `skip-migration-control`, and `availability-mismatch-control`. Only the deliberately expected `skip-reload-control` remains matched. Reload evidence is therefore observable independently of the `skip_reload` label.

Claims remain bounded structural/model evidence; no production persistence correctness is inferred. WSN-R1 is closed.

### WSN-R3 / E8 — CLOSED FOR EXECUTABLE SUBCOVERAGE; REQUIRED LIMIT RETAINED

The evaluator asserts exact typed `trust` / `respect` / `tension` end state, exact durable event history, exact authorized knowledge state, and unauthorized-knowledge rejection across materially distinct traces.

The retained scalar-collapse and material-history-loss controls are visible failures. Review mutants that disable either injected fault while retaining the expected diagnostic make E8 fail on the corresponding case, confirming those controls are executable rather than decorative labels.

Concrete NPC reachability and schedule-deadlock coverage remains blocked because reviewed schedules/time policy are absent. E8 correctly remains `INCONCLUSIVE`. WSN-R3 is closed for executable subcoverage without upgrading the blocked schedule predicates.

## Clean-surface regression review

E1, E6, E7, and E9 retain their bounded clean behavior under exact reproduction:

- E1 preserves objective-fact contradiction/duplicate checks, chronology failure, branch incompatibility, and disputed/branch false-positive controls;
- E6 preserves grounded-reference/secret/direct-mutation negatives and two valid grounded variants;
- E7 preserves exact repeated-cluster detection while leaving semantically distinct controls separate;
- E9 preserves critic disagreement, grounding priority, and `NO_SINGLE_CRITIC` authority.

E4 remains exactly `NOT_RUN / BLOCKED_BY_EXACT_PREREQUISITE`; no time policy or schedules were fabricated.

## Reviewed outcomes

| ID | Reviewed outcome | Boundary |
|---|---|---|
| WSN-E1 | PASS | bounded structural contradiction/chronology/branch evidence |
| WSN-E2 | PASS | bounded knowledge/leakage predicates |
| WSN-E3 | INCONCLUSIVE | timed quest coverage remains blocked |
| WSN-E4 | NOT_RUN | exact time-policy + schedule prerequisite absent |
| WSN-E5 | PASS | bounded model serialization/reload/migration/availability evidence only |
| WSN-E6 | PASS | bounded generated-grounding evidence |
| WSN-E7 | PASS | bounded semantic-sameness evidence |
| WSN-E8 | INCONCLUSIVE | NPC reachability/schedule-deadlock coverage remains blocked |
| WSN-E9 | PASS | bounded critic-calibration evidence |

No aggregate scalar upgrades E3, E4, or E8.

## Disposition and authority boundary

Disposition: **`CLEAN_FOR_BOUNDED_WSN_CONSUMPTION`** with 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR.

This disposition permits downstream consumers, under separately valid then-current dependency authority, to treat only the exact supported predicates/results above as reviewed bounded WSN evidence. It does not convert E3/E8 to PASS or E4 to executed evidence, establish human fun/emotional/final narrative quality, validate production persistence or scheduling, choose an engine, authorize gameplay/high-throughput implementation, establish implementation/readiness or verification-PASS, approve release/decision, canonicalize content, or grant integration authority.

Any publication of #432 or this review provenance to `main` is a separate fresh authority episode and must be squash-only.