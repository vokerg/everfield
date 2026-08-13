# W2-SIM-01 — Model simulation versus shared-kernel parity evidence

**Mission:** `W2-SIM-01` / Issue #83  
**Task class / decision state:** `PLANNING_EXPERIMENT / EVIDENCE_REQUIRED`  
**Execution episode:** `w2-sim-01-agent-20260813-0840-01`  
**Base:** `main@042d140b5d2e0b951da4528e1867514983418d6f`  
**Result:** **INCONCLUSIVE — NO REPRESENTATIVE SHARED-KERNEL EXECUTION EXISTS**  
**Production / engine-selection / readiness / canonicalization authority:** **NONE**  
**Required independent review:** `W2-REV-01`

## 1. Scope and fail-closed interpretation

Issue #83 asks for parity evidence between abstract/synthetic models and a representative shared-kernel candidate on one frozen differential corpus. Its hard prerequisite token `W2-ENG-03_REVIEW_READY` is now lifecycle-satisfied, but the exact W2-ENG-03 evidence is empirically `INCONCLUSIVE_ENVIRONMENT_BLOCKED`: no admitted engine was materialized, no candidate project or engine-native state exists, and all 50 required candidate × S1–S10 cells are `NOT_RUN`.

This task therefore does **not** manufacture a representative kernel from prose, substitute the ordering fixture for an engine execution, or treat lifecycle `REVIEW_READY` as empirical acceptance. It freezes a small experiment-local model-side differential corpus, executes two independent abstract evaluators against it, and records every shared-kernel comparison cell as `NOT_RUN`.

The resulting artifact is useful planning evidence for a future rerun, but it does not satisfy shared-kernel parity.

## 2. Exact immutable inputs

| Surface | Exact input | Use / authority boundary |
|---|---|---|
| canonical Wave-1 foundation | `main@042d140b5d2e0b951da4528e1867514983418d6f`, blob `a252e3c93702f3ebaecd3e888944a23dbe1b0e1d` | planning foundation; implementation remains blocked |
| authority/evidence contract | Issue #87 work `28cbecc13f679da0b43793525a9befd384df9a6d`, blob `a2cd16e1a20568f72a04e90eea4453b7fb880146`, terminal comment `5252368521` | durable Issue #83 directive requires this corrected successor; required `NOT_RUN` cannot become SATISFIED by lifecycle state |
| ordering evidence | Issue #75 work/head `4abfbe933b5f3a351576ba38f89c9f31e09008da`, report blob `1e9ceba1eb97b4c85d78464109da34c0c4ae0946`, terminal comment `5262786389` | bounded producer evidence for stable causal/tie-break semantics only; not a shared kernel |
| engine comparison | Issue #82 work/head `1575cb3a18c9c7be1776b64c9ec92cc8990a97e0`, report blob `98506154ed10bddaec90966b147793b86f3f1f37`, terminal comment `5276916603` | exact upstream result: `INCONCLUSIVE_ENVIRONMENT_BLOCKED`, 5 candidates, 10 scenarios each, 50 `NOT_RUN`, 0 `PASS_FOR_COMPARISON` |

Frozen predecessor branches were read only and were not re-owned or modified.

## 3. Prerequisite token versus empirical sufficiency

The authority chain distinguishes task lifecycle from evidence truth. For this mission:

```yaml
w2_eng_03_lifecycle: REVIEW_READY
w2_eng_03_empirical_result: INCONCLUSIVE_ENVIRONMENT_BLOCKED
representative_shared_kernel_identity: null
engine_native_state_artifact: null
engine_candidate_execution_envelope: null
shared_kernel_parity_requirement: REQUIRED
shared_kernel_parity_execution: NOT_RUN
shared_kernel_parity_satisfaction: INCONCLUSIVE
```

A valid upstream terminal capsule makes Issue #83 schedulable; it does not create missing empirical bytes. The shared-kernel side remains required and unrun.

## 4. Frozen model-side corpus

The corpus below is deliberately synthetic. It tests deterministic state transition, resource/economy updates, a progression gate, day-boundary state, rejected-action immutability, and an ordering-sensitive pair. It is **not** proposed game balance or canonical content.

### 4.1 Corpus identity

Experiment-local canonicalization only: UTF-8 JSON, recursively sorted object keys, list order preserved, no insignificant whitespace. This local SHA-256 is a fixture identity for this planning episode; it does not claim W2-HASH-01 cross-runtime hash authority.

- schema: `SIM-PARITY-CORPUS-v1`
- rules: `sim.parity.synthetic.v1`
- content: `sim.parity.content.v1`
- corpus SHA-256: `2cff8e26fa0d86a6f08bad97d4e132d53f3c97f9679a12d21f9d437ee05df017`

Initial state:

```json
{"coins":0,"crop":0,"day":0,"energy":10,"level":1,"pending_crop":0,"seed":0,"unlocks":[],"wood":0,"xp":0}
```

Frozen scenario action lists:

```yaml
ECO-01:
  - [earn, 10]
  - [buy_seed, 1]
  - [buy_seed, 1]
  - [plant, 1]
  - [plant, 1]
  - [advance_day, 1]
  - [sell_crop, 2]
PROG-01:
  - [gain_xp, 9]
  - [craft_crate, 1]
  - [gain_xp, 1]
  - [gather_wood, 3]
  - [craft_crate, 1]
SCHED-01:
  - [buy_seed, 1]
  - [earn, 2]
  - [buy_seed, 1]
  - [plant, 1]
  - [advance_day, 1]
  - [sell_crop, 1]
INVALID-01:
  - [buy_seed, 1]
  - [sell_crop, 1]
  - [gather_wood, 11]
  - [gain_xp, 20]
  - [gather_wood, 3]
  - [craft_crate, 1]
ORDER-ADD-SPEND:
  - [earn, 5]
  - [spend, 5]
ORDER-SPEND-ADD:
  - [spend, 5]
  - [earn, 5]
```

### 4.2 Closed transition rules

Rejected actions leave state byte-for-byte logically unchanged.

| Action | Preconditions | Effect |
|---|---|---|
| `earn(n)` | `n >= 0` | `coins += n` |
| `spend(n)` | `n >= 0 && coins >= n` | `coins -= n` |
| `buy_seed(n)` | `n > 0 && coins >= 2*n` | `coins -= 2*n; seed += n` |
| `plant(n)` | `n > 0 && seed >= n` | `seed -= n; pending_crop += n` |
| `advance_day(1)` | exact step `1` | `day += 1; crop += pending_crop; pending_crop = 0; energy = 10` |
| `sell_crop(n)` | `n > 0 && crop >= n` | `crop -= n; coins += 4*n` |
| `gain_xp(n)` | `n >= 0` | `xp += n; level = 1 + floor(xp/10); level >= 2 adds unlock workshop` |
| `gather_wood(n)` | `n > 0 && energy >= n` | `energy -= n; wood += n` |
| `craft_crate(1)` | workshop unlocked and `wood >= 3` | `wood -= 3; coins += 5` |

Failure reason codes are closed for this corpus: `INVALID_AMOUNT`, `INVALID_DAY_STEP`, `INSUFFICIENT_COINS`, `INSUFFICIENT_SEED`, `INSUFFICIENT_CROP`, `INSUFFICIENT_ENERGY`, `INSUFFICIENT_WOOD`, `WORKSHOP_LOCKED`, `UNKNOWN_ACTION`.

## 5. Model-side execution

Two independently structured Python 3.13.5 evaluators were executed locally against the exact frozen action lists: one mutable transition evaluator with rollback-on-reject, and one copy-on-transition evaluator returning a new state. Both produced byte-identical normalized traces and final states.

Model result object identity:

- schema: `SIM-PARITY-MODEL-RESULT-v1`
- corpus digest: `2cff8e26fa0d86a6f08bad97d4e132d53f3c97f9679a12d21f9d437ee05df017`
- normalized result SHA-256: `0c29eda299ecd56404a4e958b0521b5cdd40c20acb2861e55c92931b6a64d782`
- independent evaluator agreement: **6/6 scenarios, exact trace/result equality**

| Scenario | Actions | Accepted | Rejected | Final state summary |
|---|---:|---:|---:|---|
| `ECO-01` | 7 | 7 | 0 | coins=14, day=1, no pending/crop/seed |
| `PROG-01` | 5 | 4 | 1 | xp=10, level=2, workshop unlocked, coins=5, energy=7 |
| `SCHED-01` | 6 | 5 | 1 | coins=4, day=1, crop/pending=0 |
| `INVALID-01` | 6 | 3 | 3 | xp=20, level=3, workshop unlocked, coins=5, energy=7 |
| `ORDER-ADD-SPEND` | 2 | 2 | 0 | coins=0 |
| `ORDER-SPEND-ADD` | 2 | 1 | 1 | coins=5 |

The ordering pair intentionally retains a visible semantic difference. It is consistent with W2-ORDER-01's bounded conclusion that ordering/tie-break decisions can be semantically material. It does not prove a production scheduler.

## 6. Shared-kernel parity matrix

There is no exact representative shared-kernel candidate identity to execute. Therefore the model results above are not compared against synthetic or guessed engine output.

| Scenario | Abstract model | Representative shared kernel | Parity disposition |
|---|---|---|---|
| `ECO-01` | executed | `NOT_RUN` | `INCONCLUSIVE` |
| `PROG-01` | executed | `NOT_RUN` | `INCONCLUSIVE` |
| `SCHED-01` | executed | `NOT_RUN` | `INCONCLUSIVE` |
| `INVALID-01` | executed | `NOT_RUN` | `INCONCLUSIVE` |
| `ORDER-ADD-SPEND` | executed | `NOT_RUN` | `INCONCLUSIVE` |
| `ORDER-SPEND-ADD` | executed | `NOT_RUN` | `INCONCLUSIVE` |

Counts: 6 model executions, 6 shared-kernel `NOT_RUN`, 0 parity PASS, 0 parity FAIL, 6 parity INCONCLUSIVE.

The absence of parity FAIL is not evidence of parity success.

## 7. Admissible claim classes

| Claim | State after this episode | Reason |
|---|---|---|
| synthetic model fixture is internally deterministic | `BOUNDED_MODEL_ONLY_PASS` | two independent evaluators agree exactly on frozen corpus |
| shared-kernel parity for this corpus | `INCONCLUSIVE / NOT_RUN` | no representative kernel execution exists |
| abstract model may stand in for production/shared-kernel correctness | `NOT_AUTHORIZED` | parity requirement unrun |
| engine fitness or engine selection | `NOT_AUTHORIZED` | W2-ENG-03 produced no comparative engine evidence |
| production scheduler/order choice | `NOT_AUTHORIZED` | ordering evidence remains bounded planning evidence |
| implementation readiness / release / canonicalization | `NOT_AUTHORIZED` | upstream and global readiness gates remain open |

No aggregate score is produced.

## 8. Rerun contract

A future parity rerun must preserve this episode and may strengthen authority only when all of the following exist:

1. one exact representative shared-kernel candidate with immutable candidate/work identity and an executed engine/toolchain envelope;
2. the representative identity is established by an authorized upstream decision/evidence route, not selected ad hoc by W2-SIM-01;
3. `SIM-PARITY-CORPUS-v1` remains frozen before candidate adaptation, or any corpus change creates a new version/digest and does not rewrite this result;
4. shared-kernel execution exposes exact initial state, ordered actions, accepted/rejected actions with reason mapping, every post-action logical state, rules/content identity, environment/toolchain identity, and retained artifacts;
5. comparison checks full normalized trajectories, not only final totals;
6. any semantic divergence is retained, classified, and cannot be hidden by later PASS;
7. ordering-sensitive cases bind explicit logical ordering/tie-break rules rather than wall-time arrival;
8. independent `W2-REV-01` remains the adjudication route for stronger authority.

If an eventual representative kernel cannot express this experiment-local synthetic fixture without changing semantics, that is a recorded coverage/adaptation gap; it is not permission to weaken the model fixture after seeing results.

## 9. Disposition and downstream use

**Result: `INCONCLUSIVE_UPSTREAM_ENGINE_EXECUTION_ABSENT`.**

This episode establishes a frozen model-side seed corpus and demonstrates internal abstract-model determinism only. It does not complete the core shared-kernel parity comparison because the exact upstream engine episode contains no executable candidate evidence.

`W2-REV-01` may consume this artifact as explicit evidence that the parity requirement remains open. It must not interpret Issue #83 lifecycle completion, an open PR, or model-side reproducibility as shared-kernel parity satisfaction.

Reopen the empirical portion when W2-ENG-03 is rerun successfully or another separately authorized route establishes an exact representative shared-kernel candidate and execution envelope.

## 10. Bounded self-review

- fabricated shared-kernel runs: 0
- parity PASS claims: 0
- hidden upstream `NOT_RUN`: 0
- model corpus scenarios: 6
- independent model evaluator agreement: 6/6
- ordering-sensitive negative/control pair retained: yes
- production/game-balance claims from synthetic rules: 0
- unresolved core parity requirement: **yes — all 6 shared-kernel cells**
- report-level BLOCKER/MAJOR requiring correction before independent review: 0 identified
- required independent adversarial review: `W2-REV-01`

The correct lifecycle action is to freeze this bounded, fail-closed evidence packet for review without upgrading the unrun shared-kernel requirement.
