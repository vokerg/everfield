# W2-GAME-EV-WSN-01 — reviewed-fan-in world/social/narrative evidence tranche

**Issue:** #428  
**Mission:** `W2-GAME-EV-WSN-01`  
**Tranche:** `W2-GAME-EV-WORLD-STRUCT-v1`  
**Task class:** `PLANNING_EXPERIMENT / EVIDENCE_REQUIRED`  
**Canonicality:** `NOT_CANONICAL`

## 1. Frozen authority and evidence identity

This experiment consumes only the already-accounted WSN identities from Issue #196 and the clean reviewed content fan-in. It creates no new experiment IDs.

- claim base `main`: `aa906611b8d107e0d4cc531d3c1c380d6b2c0647`
- Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical binding comment: `5245368879`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- game-evidence dependency-map blob: `e4f4e964f9b972ebbc22700c7b0a4e23b1c97593`
- immutable W1-DES-03 work / source blob: `d19ddc43c9e5f22c6f14e5c978c30a4e6a2f0d8b` / `35b7acfd369143f6f1f48dcd1cf43ca90280fee5`
- fan-in Issue #422 work / terminal head: `db4bfbcc7387425989ec5902103e53953db9576b` / `f6edd59b7d029474b3de95b8f57e71e7e14e5573`
- current-main fan-in map blob: `5858bc3e2d87baa3740b2513b08fb938633bba54`
- required fan-in review Issue #426 terminal: `5307505361`
- review work / head: `fccbc2812a422f06007c5d565fb3a4e3c887e76c` / `00cb20796871f9b3eb921382d388b215013130c5`
- current-main review blob: `a154468dcd617c2cb8926b1edb78afe7d4f1942b`
- review disposition: `CLEAN_FOR_BOUNDED_CONTENT_CONSUMPTION`

Root blobs frozen through that review are copied into the corpus. No root/fan-in artifact is edited by this experiment.

## 2. Original predicates retained

The evaluator deliberately retains the original W1-DES-03 experiment semantics rather than replacing them with generic consistency checks.

- `WSN-E1`: duplicate/incompatible facts, chronology defects and branch conflicts must be detected without treating dispute- or branch-scoped alternatives as global contradictions.
- `WSN-E2`: forbidden knowledge must not leak; beliefs may be expressed without becoming objective facts.
- `WSN-E3`: route search must distinguish solvable structures from dead ends/cycles across the original representative quest classes, including timed quests.
- `WSN-E4`: schedule conflicts require concrete schedules plus time/override/travel semantics.
- `WSN-E5`: reversible/irreversible branch state must survive reload, schema migration and downstream availability replay.
- `WSN-E6`: generated candidates must be structurally grounded before subjective quality; invalid facts/secrets/refs are rejected and valid grounded variants remain possible.
- `WSN-E7`: repeated semantic structures must be surfaced without classifying a shared motif alone as a defect.
- `WSN-E8`: long-horizon social/NPC composition must retain legal relationship/knowledge evolution, reachability and deadlock checks.
- `WSN-E9`: multiple critics must expose disagreement and defect categories, objective grounding must outrank preference, and no single critic may become authority.

## 3. Corpus and evaluator

The retained corpus contains **36** deterministic cases. It binds directly to fan-in surfaces such as conflicting-account investigation, shared-use negotiation, project commitment, repair/reframe, aftermath, objective-fact/claim/knowledge separation, branch compatibility, generated-content authority and multidimensional relationship/history semantics.

The standard-library-only evaluator is invoked with:

```bash
python docs/planning/wave-2/evidence/wsn-world-structure-evaluator.py \
  --corpus docs/planning/wave-2/evidence/wsn-world-structure-corpus.json \
  --output /tmp/wsn-world-structure-results.json
```

The committed normalized results are expected to be byte-for-byte equivalent JSON modulo the output path.

Content SHA-256 identities from the executed run:

- corpus: `16a57de56900511cffcd011d26ceb47a8acc134ba4d18cbf1645735dde37b804`
- evaluator: `d74e4ee0a729d9374c97dc3b536b0b5d5b70d473adcebd0435c1676811ce190b`

No mutable repository state, network service, engine, provider credential, random source or clock is consulted by the evaluator.

## 4. Results

| Experiment | Outcome | Bounded evidence |
|---|---|---|
| `WSN-E1` | **PASS** | Incompatible objective facts, duplicate objective facts, invalid chronology and incompatible branch composition are detected; disputed claims and mutually exclusive branch facts are not falsely globalized. |
| `WSN-E2` | **PASS** | Player exposure/relationship/standing do not grant NPC knowledge; false belief remains belief; explicit post-disclosure authorization permits access without belief-to-fact promotion. |
| `WSN-E3` | **INCONCLUSIVE** | Linear/optional/branching/social/collection/world-state routes plus injected dead-end/cycle controls are correctly classified, but the original required timed-quest class cannot be exercised without inventing the deferred time-policy binding. |
| `WSN-E4` | **NOT_RUN** | Exact reviewed `GameTimePolicy` identity and concrete schedule instances are absent. The clean fan-in review explicitly preserves this block. |
| `WSN-E5` | **PASS** | Abstract versioned branch state survives save/reload and v1→v2 migration; irreversible choices retain impact and alternative/compensation obligations; a deliberately lossy migration is detected. This is structural evidence, not validation of a production persistence implementation. |
| `WSN-E6` | **PASS** | Two grounded variants from the same brief remain valid; hallucinated refs, secret/unknown revelation and direct authoritative mutation are rejected independently of prose preference. |
| `WSN-E7` | **PASS** | An exact repeated objective/dialogue/reward signature is clustered while distinct semantic variants sharing the same stewardship motif are not collapsed into that duplicate cluster. |
| `WSN-E8` | **INCONCLUSIVE** | Multiple 12-period player/event traces retain typed relationship dimensions, durable history and authorized knowledge while detecting an unauthorized update; a long-horizon quest dependency route is reachable. Required-NPC reachability and schedule-deadlock predicates remain unexecutable without concrete schedules/time policy. |
| `WSN-E9` | **PASS** | Four versioned critics produce visible ranking disagreement over calibrated strengths/defects; ungrounded candidates fail the objective eligibility gate regardless of prose preference; authority remains `NO_SINGLE_CRITIC`. |

Outcome counts: **6 PASS / 2 INCONCLUSIVE / 1 NOT_RUN**.

No aggregate scalar is used as a quality oracle and no result hides the two incomplete experiments or E4 blocker.

## 5. Important limits

`PASS` here means only that the retained deterministic structural predicate was satisfied by this bounded engine-neutral corpus and evaluator. It does **not** establish:

- canonical world/story truth;
- human fun, emotional impact, writing quality or player preference;
- production save/migration correctness;
- concrete NPC schedule correctness;
- implementation readiness or verification PASS;
- engine selection, provider/legal/commercial suitability, release or production authority.

`WSN-E3` and `WSN-E8` remain explicitly incomplete because their original predicates contain time/schedule-dependent coverage. `WSN-E4` remains fully unrun. A later time-policy/schedule packet must extend evidence without rewriting this negative/incomplete provenance.

## 6. Self-review

The exact packet was attacked for source-predicate weakening, circular pass construction, expected-defect erasure, branch/dispute false positives, belief-to-fact promotion, migration loss, generated canon drift, motif false positives, scalar relationship collapse, critic authority inflation, and accidental execution of E4.

Self-review findings in the bounded producer scope:

- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0

The injected negative controls remain in the corpus/results and are expected to generate diagnostics; detecting those injected defects is evidence of the validator, not a producer finding to erase.

## 7. Required next gate

A **fresh independent/degraded-independent aggregate review** of this exact packet is mandatory before any WSN outcome is consumed as reviewed evidence. The reviewer must:

1. freeze exact corpus/evaluator/results/report blobs and producer head;
2. rerun the evaluator from retained bytes;
3. compare each outcome against the immutable W1-DES-03 predicate and Issue #196 routing;
4. attack E3/E8 incomplete classification and E4 non-execution;
5. reject any claim that structural/synthetic evidence proves human narrative quality or implementation readiness.

Suggested mission: `W2-REV-WSN-01`.

No integration, canonicalization, readiness, implementation, verification-PASS, engine-selection or release authority is created by this producer packet.
