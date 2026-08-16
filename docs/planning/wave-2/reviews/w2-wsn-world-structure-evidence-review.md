# W2-REV-WSN-01 — aggregate review of WSN world-structure evidence

**Issue:** #430  
**Judged issue:** #428 / `W2-GAME-EV-WSN-01`  
**Task class:** `REQUIRED_REVIEW / AGGREGATE_EVIDENCE_REVIEW`  
**Trust:** `DEGRADED_SINGLE_AGENT`  
**Disposition:** `CHANGES_REQUIRED`  
**Canonicality:** `NOT_CANONICAL`

## 1. Frozen judged packet

This review judges only immutable Issue #428 / draft PR #429 at exact head `7da4412f8ebb218dc2e9b7534d048aab878ac261`.

- producer claim: `5307740866`
- producer terminal: `5307798635`
- producer work: `69838abc5dfa22902150a3470f69f49a9b86448e`
- producer head / PR #429 head: `7da4412f8ebb218dc2e9b7534d048aab878ac261`
- report blob: `ca970df32a210b09c840474c9b718cb035130933`
- corpus blob: `588e8bbe0a44b42046609cdd58302275259c8766`
- evaluator blob: `c8a7c447dbe3d1cca7dad205eaedee436af2d92c`
- results blob: `e70a70b349f9fb64b65b4d98d4960ccf3139468c`
- corpus SHA-256: `16a57de56900511cffcd011d26ceb47a8acc134ba4d18cbf1645735dde37b804`
- evaluator SHA-256: `d74e4ee0a729d9374c97dc3b536b0b5d5b70d473adcebd0435c1676811ce190b`
- dependency-map blob: `e4f4e964f9b972ebbc22700c7b0a4e23b1c97593`
- immutable W1-DES-03 work/source: `d19ddc43c9e5f22c6f14e5c978c30a4e6a2f0d8b` / `35b7acfd369143f6f1f48dcd1cf43ca90280fee5`

The producer branch was not edited by this review.

## 2. Independent reproduction

The retained corpus and evaluator bytes were reconstructed from the exact judged blobs and independently hashed before execution.

Command:

```text
python3 wsn-world-structure-evaluator.py --corpus wsn-world-structure-corpus.json --output results.json
```

Reviewer runtime: CPython `3.13.5`, standard library only for the evaluator. The surrounding execution environment emitted an unrelated spreadsheet-runtime warmup diagnostic on stderr; evaluator exit status was `0` and the generated result bytes were unaffected.

Reproduction identities:

- reconstructed corpus SHA-256 exactly `16a57de56900511cffcd011d26ceb47a8acc134ba4d18cbf1645735dde37b804`;
- reconstructed evaluator SHA-256 exactly `d74e4ee0a729d9374c97dc3b536b0b5d5b70d473adcebd0435c1676811ce190b`;
- generated normalized result Git blob SHA exactly `e70a70b349f9fb64b65b4d98d4960ccf3139468c`, matching the committed results blob;
- generated result SHA-256 `a20b2b32b8581eab0d9ec36f3f326bc4fb4865ad07cad8114f4ecd0d65d025c5`;
- reproduced outcomes: `6 PASS / 2 INCONCLUSIVE / 1 NOT_RUN`, with zero expectation mismatches.

Reproducibility is therefore clean. The findings below concern whether the harness actually exercises the original predicates it labels covered.

## 3. Findings

### MAJOR WSN-R1 — E5 coverage labels substitute for save/reload, schema migration, and availability replay

Original W1-DES-03 `WSN-E5` requires applying reversible/irreversible choices, **save/reload**, migrating a schema version, and replaying downstream content availability; PASS requires branch facts/effects to persist/migrate and availability to match predicates.

The evaluator performs only in-memory list edits. It has no serialization/reload operation, no source/target schema versions, and no assertion of final availability against an expected predicate. It marks `reload`, `migration`, and `availability` covered solely because an E5 case executed and a `preserve` string contains selected labels.

Adversarial check: both nominal passing E5 cases were mutated to contain no meaningful initial availability and no add/remove transitions while retaining their `preserve` labels. The evaluator still returned `WSN-E5: PASS`, with `reload`, `migration`, and `availability` all reported observed.

**Impact:** the producer's E5 PASS and report claim of save/reload plus v1→v2 migration are unsupported by the retained executable evidence. E5 must not be consumed as reviewed PASS.

### MAJOR WSN-R2 — E3 representative quest classes are names, not representative semantics

Original `WSN-E3` requires representative linear, optional, branching, timed, social, collection, and world-state quests plus deliberate soft-lock/cycle defects. Issue #428 additionally requires prerequisite/failure/retry/recovery/alternative-route structures.

For the six nominal positive non-timed classes, the corpus uses the same graph in every case: `start -> goal`. The class is only a string placed into the coverage set. No optional branch, branching alternative, social predicate, collection predicate, world-state gate, failure/retry/recovery, or alternative route is represented or evaluated.

The overall E3 result is already `INCONCLUSIVE` because timed coverage is correctly blocked, but the report's positive claim that the other representative classes were exercised is materially overstated. A future timed case could otherwise flip E3 to PASS without repairing these semantic gaps.

### MAJOR WSN-R3 — E8 relationship/history coverage is not validated and permits scalar collapse

Issue #428 requires E8 to verify durable history retention, non-collapse of relationship dimensions, and preservation of material events across distinct long-horizon traces. Original W1-DES-03 also requires relationships/knowledge to evolve legally.

The evaluator computes `rel`, `knowledge`, and `history`, but only unauthorized knowledge and event-horizon errors can affect the case result. `rel` and `history` are never asserted, compared to expectations, or emitted into the normalized evidence. Nevertheless every trace is labeled as covering `relationship`.

Adversarial check: all relationship deltas in the two nominal long-horizon policy traces were collapsed to one scalar dimension. Both policy cases still matched and E8 still reported `relationship` observed.

**Impact:** E8 correctly remains globally `INCONCLUSIVE` because schedule/reachability coverage is blocked, but its claimed positive relationship/history sub-evidence is not supportable and must be corrected rather than carried forward.

### MAJOR WSN-R4 — E2 PASS omits required relationship/social-standing/generated-presentation leak attacks

Issue #428 explicitly requires E2 injections covering relationship state, player visibility, social standing, and generated presentation where explicit information access is absent. The retained E2 corpus covers player exposure, belief-vs-objective separation, explicit knowledge, and one explicitly allowed post-disclosure case, but contains no relationship-state, social-standing, or generated-presentation leak case.

The evaluator's self-declared E2 `REQ` set omits those required attack classes, so their absence cannot make E2 incomplete.

**Impact:** the E2 PASS weakens the selected task contract. E2 requires added cases/evaluator predicates or a fail-closed `INCONCLUSIVE` disposition.

## 4. Clean / retained observations

- `WSN-E1`: bounded contradiction/chronology/branch controls are coherent for the tested corpus; no material review defect found.
- `WSN-E4`: `NOT_RUN` is correct. Reviewed `GameTimePolicy` identity and concrete schedules remain absent; inventing them would be evidence laundering.
- `WSN-E6`: the bounded structural grounding fixtures reject unknown references, secret revelation, and direct authoritative mutation while accepting two grounded variants; no material defect found in that limited structural claim.
- `WSN-E7`: exact functional repetition is clustered while a shared motif alone does not collapse distinct structures; no material defect found in the bounded fixture.
- `WSN-E9`: disagreement is observable and the explicit grounding-eligibility gate prevents the ungrounded control from becoming eligible; no single critic is granted authority. This remains synthetic calibration, not human-quality evidence.
- Authority boundaries in the producer packet remain explicit: no human fun/narrative-quality, production persistence/schedule correctness, readiness, verification-PASS, engine-selection, release, decision, or canonical authority is established.

## 5. Disposition and required remediation

Finding counts: `0 BLOCKER / 4 MAJOR / 0 correction-requiring MINOR`.

Disposition: **`CHANGES_REQUIRED`**. The exact Issue #428 packet is reproducible but is **not clean for bounded WSN consumption** because executable coverage is weaker than the predicates for E2, E3, E5, and E8.

Required remediation must be a separate producer/revision episode and must not edit this review:

1. E5: implement an explicit versioned save → reload → migrate → downstream-availability replay model with expected post-state assertions and negative controls.
2. E3: represent distinct non-timed quest-class semantics and Issue #428 prerequisite/failure/retry/recovery/alternative-route obligations instead of coverage-by-label; keep timed coverage blocked until its real prerequisite exists.
3. E8: make typed relationship state and durable history observable/asserted, include non-collapse/history-loss controls, and retain schedule/reachability as blocked until real prerequisites exist.
4. E2: add relationship-state, social-standing, and generated-presentation leakage controls (plus player visibility) or mark unsupported portions inconclusive.
5. Preserve every existing negative/inconclusive/not-run result; remediation may not rewrite E4 or manufacture time/schedule evidence.
6. Re-run a fresh aggregate review on the exact remediated packet before any WSN outcome is consumed as reviewed evidence.

## 6. Authority boundary

This review is noncanonical review provenance only. It does not integrate Issue #428, canonicalize content, select an engine, authorize gameplay/high-throughput or production implementation, establish human narrative quality, grant readiness or verification PASS, approve release/decision, or clear the retained E3/E8/E4 time/schedule limitations.
