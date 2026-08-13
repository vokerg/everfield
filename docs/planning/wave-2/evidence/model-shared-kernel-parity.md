# W2-REM-SIM-01 — Reconstructable simulation parity corpus and model execution evidence

**Mission:** `W2-REM-SIM-01` / Issue #132  
**Task class / decision state:** `REMEDIATION / EVIDENCE_REQUIRED`  
**Source producer:** `W2-SIM-01` / Issue #83, immutable head `999d67726f849d09dc812529170645332258f32f`, work `709657b7c0a09e46a35ed989e75764ccaddb7033`  
**Independent review:** `W2-PG-SIM-01` / Issue #130, immutable review work/head `450dc3e6880e85a194bda4d5f8afa8baab4d2ca5`, terminal comment `5277039693`  
**Correction scope:** `PG-SIM-M01`, `PG-SIM-M02` only  
**Result:** `INCONCLUSIVE_UPSTREAM_ENGINE_EXECUTION_ABSENT` preserved  
**Production / engine-selection / readiness / canonicalization authority:** **NONE**  
**Required formal review:** `W2-REV-01`

## 1. Scope and non-goals

This remediation repairs only the reconstructability defects found in the positive model-side evidence of Issue #83. It does not edit or reinterpret the immutable producer/review branches, invent a representative engine/shared-kernel candidate, execute an engine, claim shared-kernel parity, select an engine, authorize production code, clear implementation readiness, approve release, integrate to `main`, verify the planning program, or canonicalize any decision.

The producer's fail-closed empirical boundary remains authoritative for this packet:

```yaml
w2_eng_03_empirical_result: INCONCLUSIVE_ENVIRONMENT_BLOCKED
representative_shared_kernel_identity: null
shared_kernel_execution_count: 0
shared_kernel_cells:
  NOT_RUN: 6
parity:
  PASS: 0
  FAIL: 0
  INCONCLUSIVE: 6
```

The only corrected positive claim is that the exact experiment-local abstract-model fixture is now independently reconstructable from retained bytes.

## 2. Immutable provenance and prior findings

The source producer report is Git blob `9d292c63d4316fbe655f08fc026f92dd55aca91c`; its handoff is blob `b0f243acd674a509f3c3dd87e2e7ce2f3c1eaf27`. The independent review is blob `f2059442eceef5614e15275d70aba43fc1ab7dd2`.

Issue #130 found:

- `PG-SIM-M01` — the producer asserted corpus digest `2cff8e26fa0d86a6f08bad97d4e132d53f3c97f9679a12d21f9d437ee05df017`, but retained no single exact canonical machine object/bytes from which that digest could be recomputed without guessing producer-private structure.
- `PG-SIM-M02` — the producer asserted normalized model-result digest `0c29eda299ecd56404a4e958b0521b5cdd40c20acb2861e55c92931b6a64d782` and 6/6 two-evaluator agreement, but retained no evaluator source, full normalized traces, or exact result bytes.

Those producer-local digests remain immutable historical provenance. This remediation does **not** pretend to reconstruct their unpublished serialization. It recreates the same declared scenario/rule semantics in exact retained canonical bytes and publishes new independently recomputable evidence identities.

## 3. Corrected exact corpus evidence — resolves `PG-SIM-M01`

### 3.1 Retained artifact

Path: `docs/planning/wave-2/evidence/sim-parity-corpus-v1.json`

Exact Git blob: `509048efcce60e21a876b2c23471ea31cd5f8ed9`  
Exact file SHA-256: `3b6e2d2ff524fb271910202d96f7d408c9d9fd24944dcf25baa776260b4e9f25`

The file itself is the canonical machine object: UTF-8 JSON, recursively sorted object keys, list order preserved, separators exactly `,` and `:`, `ensure_ascii=false`, and **no trailing newline**. A parser/canonicalizer must reject a corpus file whose retained bytes differ from canonical reserialization.

The object includes, in one identity-bearing machine structure:

- schema `SIM-PARITY-CORPUS-v1`;
- rules version `sim.parity.synthetic.v1`;
- content version `sim.parity.content.v1`;
- the exact initial state;
- the closed failure-reason set in declared list order;
- the rejected-action-is-unchanged rule;
- the exact transition-contract descriptions;
- all six scenario IDs and ordered action tuples.

### 3.2 Domain-separated semantic identity

Semantic corpus identity is:

```text
SHA256(
  UTF8("everfield.sim-parity-corpus.v1") || 0x00 ||
  exact retained corpus file bytes
)
```

Result:

`0e87644390072077f42dfa1f084fd3ec991e27779f29970fd5c9b0f2c757a90e`

This domain-separated digest is the corrected `SIM-PARITY-CORPUS-v1` evidence identity for Issue #132. The plain file SHA-256 remains separately published so both exact file transport identity and semantic-domain identity are checkable.

## 4. Corrected deterministic evaluator and full trace evidence — resolves `PG-SIM-M02`

### 4.1 Retained evaluator

Path: `docs/planning/wave-2/evidence/sim-parity-evaluator.py`

Exact Git blob: `35f85763213fcdc2e09a3f15f9f462b595cc3a2e`  
Exact source SHA-256: `05cb2bdb4d163df583746052a926031f99210b41f4d53f904d75654b46bd4c84`

The evaluator is Python standard-library-only and is explicitly `PLANNING_EXPERIMENT` evidence. It loads and validates the exact canonical corpus bytes, then executes two separately implemented evaluators:

1. `mutable_rollback` — applies transitions by in-place mutation with full pre-state rollback on reject;
2. `pure_copy` — computes a copied next state and never mutates rejected input.

Both emit the same normalized per-action schema containing action index, exact action tuple, acceptance boolean, closed reason code or null, complete pre-state, and complete post-state. The tool fails if their canonical normalized trace/result bytes differ.

### 4.2 Retained full normalized result

Path: `docs/planning/wave-2/evidence/sim-parity-model-result-v1.json`

Exact Git blob: `844161f2715d9b53170b3a9ed54414acb2d3910f`  
Exact file SHA-256: `7e4d8e2cd68dbee3ce2c51e40f702b30e25cd05ef1c7f3506610a98eb2b58e85`

The retained result contains the complete per-action trace for every one of the six scenarios, not only final summaries. It binds:

- exact corpus semantic digest `0e87644390072077f42dfa1f084fd3ec991e27779f29970fd5c9b0f2c757a90e`;
- exact evaluator source SHA-256 `05cb2bdb4d163df583746052a926031f99210b41f4d53f904d75654b46bd4c84`;
- evaluator identities `mutable_rollback` and `pure_copy`;
- exact 6/6 normalized trace/result equality;
- every accepted/rejected action, reason code, full pre-state, and full post-state;
- each full final state.

Semantic result identity is:

```text
SHA256(
  UTF8("everfield.sim-parity-model-result.v1") || 0x00 ||
  exact retained result file bytes
)
```

Result:

`876b4a3151c5d5a26411fe269a7daaec912271dcebc0515340b1ebe610e91ef0`

### 4.3 Fresh execution evidence

Exact intended evaluator bytes were syntax-valid and executed twice under Python 3.13.5 against the exact canonical corpus bytes. Both executions returned the same canonical summary line and validated that the retained result file bytes equal freshly derived result bytes.

Deterministic summary stdout SHA-256, including its single trailing newline:

`59a0ac5f94ec76ad0236b0c3aac93363d9351f71244749de02f5a053faaac461`

Fresh execution summary:

```json
{"agreement":{"evaluators":["mutable_rollback","pure_copy"],"exact_normalized_trace_result_equality":true,"scenario_count":6},"corpus_file_sha256":"3b6e2d2ff524fb271910202d96f7d408c9d9fd24944dcf25baa776260b4e9f25","corpus_sha256":"0e87644390072077f42dfa1f084fd3ec991e27779f29970fd5c9b0f2c757a90e","evaluator_source_sha256":"05cb2bdb4d163df583746052a926031f99210b41f4d53f904d75654b46bd4c84","parity_fail":0,"parity_inconclusive":6,"parity_pass":0,"result_file_sha256":"7e4d8e2cd68dbee3ce2c51e40f702b30e25cd05ef1c7f3506610a98eb2b58e85","result_sha256":"876b4a3151c5d5a26411fe269a7daaec912271dcebc0515340b1ebe610e91ef0","scenario_count":6,"shared_kernel_execution_count":0,"status":"PASS"}
```

The independent evaluators agree on all six scenarios with exact full trace equality.

## 5. Model-side semantic reconciliation

The corrected retained traces reproduce the producer's declared scenario-level behavior:

| Scenario | Actions | Accepted | Rejected | Corrected final-state check |
|---|---:|---:|---:|---|
| `ECO-01` | 7 | 7 | 0 | coins=14, day=1, crop/pending/seed=0 |
| `PROG-01` | 5 | 4 | 1 | xp=10, level=2, workshop unlocked, coins=5, energy=7 |
| `SCHED-01` | 6 | 5 | 1 | coins=4, day=1, crop/pending=0 |
| `INVALID-01` | 6 | 3 | 3 | xp=20, level=3, workshop unlocked, coins=5, energy=7 |
| `ORDER-ADD-SPEND` | 2 | 2 | 0 | coins=0 |
| `ORDER-SPEND-ADD` | 2 | 1 | 1 | coins=5 |

The ordering-sensitive pair deliberately remains different. That is bounded synthetic model evidence only; it does not establish a production scheduler.

## 6. Shared-kernel parity remains unexecuted

No representative shared-kernel identity or engine-native execution envelope appeared during this remediation. Therefore the parity matrix remains unchanged:

| Scenario | Abstract model | Representative shared kernel | Parity |
|---|---|---|---|
| `ECO-01` | exact corrected model trace retained | `NOT_RUN` | `INCONCLUSIVE` |
| `PROG-01` | exact corrected model trace retained | `NOT_RUN` | `INCONCLUSIVE` |
| `SCHED-01` | exact corrected model trace retained | `NOT_RUN` | `INCONCLUSIVE` |
| `INVALID-01` | exact corrected model trace retained | `NOT_RUN` | `INCONCLUSIVE` |
| `ORDER-ADD-SPEND` | exact corrected model trace retained | `NOT_RUN` | `INCONCLUSIVE` |
| `ORDER-SPEND-ADD` | exact corrected model trace retained | `NOT_RUN` | `INCONCLUSIVE` |

Counts remain **0 PASS / 0 FAIL / 6 INCONCLUSIVE**. Two abstract evaluators agreeing cannot substitute for a representative shared-kernel execution.

## 7. Evidence versus inference

**Direct retained evidence**

- exact canonical corpus bytes and Git/file/domain identities;
- exact evaluator source bytes and source digest;
- exact full normalized model-result bytes and Git/file/domain identities;
- deterministic 6/6 evaluator equality from fresh execution;
- explicit absence of any representative shared-kernel execution in the source producer lineage.

**Inference / bounded interpretation**

- the recreated machine object faithfully captures the human-readable source producer's declared initial state, transition semantics, reason vocabulary, and six ordered scenario action lists;
- the corrected traces support the same bounded model-only conclusions as the producer's summaries.

The new corrected digests do not prove that the producer's unpublished original digest object had identical bytes; that unknowable producer-private serialization is precisely what `PG-SIM-M01/M02` rejected.

## 8. Failure modes, risks, and reopen conditions

Reopen this remediation if:

- retained corpus bytes no longer canonicalize exactly under the published rule;
- evaluator source digest or retained result bytes do not match the published identities;
- the two evaluator implementations disagree on any normalized trace field;
- a scenario/rule is changed without a new corpus/evidence version;
- any future consumer treats model-only agreement as representative shared-kernel parity;
- an actual representative shared-kernel execution becomes available, in which case parity must be rerun against a separately authorized exact candidate/envelope rather than rewriting this packet.

A future parity-strengthening run must retain full kernel trajectories and exact identity/provenance and remain subject to formal `W2-REV-01`.

## 9. Finding dispositions

- `PG-SIM-M01`: **RESOLVED** — one exact canonical machine-readable corpus artifact is retained; exact file and domain-separated semantic digests are independently recomputable.
- `PG-SIM-M02`: **RESOLVED** — exact evaluator source, complete normalized per-action trace/result bytes, source/corpus/result identities, two-evaluator implementation structure, and fresh deterministic reproduction are retained.

Detailed disposition evidence is in `docs/planning/wave-2/reviews/w2-sim-01-pre-gate-review-dispositions.md`.

## 10. Bounded self-review

- unresolved `PG-SIM-M01`: 0
- unresolved `PG-SIM-M02`: 0
- corpus file canonical-byte check: PASS
- two fresh evaluator executions: PASS, byte-identical summary
- retained result equals fresh derived result: PASS
- independent evaluator agreement: PASS, 6/6 exact full traces
- representative shared-kernel executions: 0
- shared-kernel `NOT_RUN`: 6/6
- parity PASS: 0
- parity FAIL: 0
- parity INCONCLUSIVE: 6
- fabricated engine/kernel evidence: 0
- BLOCKER remaining in remediation scope: 0
- MAJOR remaining in remediation scope: 0
- correction-requiring MINOR remaining in remediation scope: 0
- formal aggregate review still required: `W2-REV-01`

This remediation is noncanonical evidence input only.
