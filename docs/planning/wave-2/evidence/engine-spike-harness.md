# W2-REM-ENG-04 — Engine spike harness v4

**Source mission:** `W2-ENG-02` / Issue #72  
**Prior remediations:** `W2-REM-ENG-02` / Issue #94; `W2-REM-ENG-03` / Issue #104  
**Current remediation:** `W2-REM-ENG-04` / Issue #112  
**Frozen Issue #104 candidate head/work:** `b406193c45c75f6309ea4123d02579d70ebe3591`  
**Frozen v3 harness blob:** `1fb26cb6afa02b7061d37f331cf5a132375ecfc4`  
**Frozen v3 validator blob:** `b7209361fa8c52f599d1e7393d28a2d19658887c`  
**Independent pre-gate review:** Issue #110, review work `8941b0fa66f99d7343d8f792f562f58099776582`, review blob `7587f4f2b7487de94a695b1a0ccc7356368100ce`  
**Review findings:** `PG-REM3-M01`, `PG-REM3-M02`, `PG-REM3-m01`, lifecycle `PG-REM3-B01`  
**Remediation base:** `main@042d140b5d2e0b951da4528e1867514983418d6f`  
**Harness ID:** `W2-ENG-HARNESS-v4`  
**Feature slice ID:** `W2-ENG-FEATURE-SLICE-v2`  
**Scenario manifest ID:** `W2-ENG-SCENARIO-INPUTS-v2`  
**Validator ID:** `W2-ENG-PROTOCOL-VALIDATOR-v4`  
**Required formal review:** `W2-REV-01`

## 1. Scope, non-goals, and authority

This bounded remediation changes only the fail-closed surfaces identified by Issue #110:

1. close the kind-specific `AttemptRecord` schema before sorting or aggregation;
2. bind an accepted `AdaptationManifest` to the exact candidate/scenario that consumes it; and
3. split history lineage validity from evidence-envelope validity so a structurally linked history cannot be mistaken for fully valid evidence.

The exact Issue #104 protections remain in force: common S1–S10 inputs and anti-shrink bounds, cold-start/resource parity, retained-run equality, duplicate required-injection rejection, attempt-to-generation candidate binding, the closed `result × failure_class` matrix, repair-generation lineage, S3/S9/S10 authority limits, and harness-defect reopening.

This validator is `PLANNING_EXPERIMENT` evidence only. It does **not** execute, score, rank, or select an engine; authorize production/gameplay implementation or implementation readiness; turn hashes into semantic-correctness authority; replace `W2-REV-01`; or authorize integration, verification, release, or canonicalization.

## 2. Preserved common feature slice and scenario manifest

The v4 remediation does not modify the engine-neutral feature slice or the S1–S10 common scenario contract. Their semantic identities therefore remain:

- feature slice: `sha256:9a2523c4870146b09233397f3773f7a27b1e0135c24a6767d16e34a791aab104`
- scenario manifest: `sha256:be4d7473b01da6b428cd5f3be48de083abd161a4899471303f3ccfeef45c725f`

The inherited slice still fixes 32 entities, 10 logical actions, three player-facing screens/routes, eight logical assets, save-schema evolution, two semantic merge overlaps, capture identity, 19,200 + 3,200 profiling updates, the common Windows x64 development package placeholder, and the repository-only continuation fixture. Each S1–S10 scenario still has exact common refs, lower bounds, and one required failure injection. Candidate-native representations may differ only through an accepted adaptation that preserves or strengthens those obligations.

## 3. Exact adaptation-to-consumer binding — `PG-REM3-M02`

### 3.1 Closed candidate identity

Every `AdaptationManifest` must contain a nonempty exact string `candidate_id`. Validation is performed with the consuming generation's expected candidate identity. Missing, blank, or mismatched candidate identity is `REJECT` before any execution authority exists.

The preserved adaptation fields remain:

```yaml
AdaptationManifest:
  candidate_id: <exact nonempty candidate identity>
  scenario_id: S1..S10
  harness_id: W2-ENG-HARNESS-v4
  feature_slice_id: W2-ENG-FEATURE-SLICE-v2
  fixed_input_refs: [<all required common refs>]
  mappings:
    <every required obligation>: EQUIVALENT | STRICTLY_STRONGER
  bounds:
    <every scenario minimum>: <candidate value>
  failure_injections: [<every required injection>]
  start_profile:
    cache_mode: COLD
    generated_state_policy: REGENERATE_FROM_REPO
    resource_class: W2-ENG-HOST-COMMON-v2
  resource_exception: false
  undocumented_manual_intervention: false
  mechanism_authority: <S3 REAL_OR_SHARED_RULES>
  package_target: <S9 WINDOWS_X64_DEV_PACKAGE-v1>
  hidden_context_transfer: false
  extra_evidence: []
```

### 3.2 Exact binding object

A consuming generation carries the full accepted adaptation plus `adaptation_binding_id`. The validator recomputes the binding from exact canonical JSON over:

```yaml
AdaptationBinding:
  candidate_id: <exact adaptation candidate>
  scenario_id: <exact scenario>
  harness_id: W2-ENG-HARNESS-v4
  feature_slice_id: W2-ENG-FEATURE-SLICE-v2
  scenario_contract_identity: sha256(<exact scenario contract object>)
  adaptation_identity: sha256(<exact adaptation object>)
```

`adaptation_binding_id = sha256(canonical_json(AdaptationBinding))`.

Before attempt authority, the generation must satisfy all of the following:

- `generation.candidate_id == adaptation.candidate_id`;
- `generation.scenario_id == adaptation.scenario_id`;
- adaptation harness/feature identities equal the v4 contract;
- the exact adaptation independently validates as `ACCEPT`; and
- the stored `adaptation_binding_id` exactly equals the recomputed binding ID.

This makes a cross-candidate adaptation copy/relabel fail even when an attacker also recomputes the copied adaptation's binding. A candidate transition remains forbidden inside one repair history unless a later separately reviewed typed transition protocol explicitly authorizes it; changing labels is not a transition mechanism.

## 4. Closed kind-specific `AttemptRecord` — `PG-REM3-M01`

Every retained attempt is validated **before** any sort, reset/workspace comparison, injection lookup, or outcome aggregation.

Common fields require exact generation/scenario/candidate identity, a known kind, a valid closed result/failure-class pair, nonempty string `reset_id`, actual boolean `reset_verified`, nonempty string `workspace_id`, and nonempty string `resource_class`.

Kind-specific rules are:

| Kind | `normal_index` | `injection_id` |
|---|---|---|
| `NORMAL` | positive exact integer; booleans are not integers for this contract; unique within generation | must be `null` |
| `FAILURE_INJECTION` | must be `null` | nonempty exact string |

A malformed record returns typed structural `INCONCLUSIVE` with `valid_envelope=false`; it never reaches Python sorting and therefore cannot crash aggregation. Duplicate normal indices are rejected before sort. After structural validation, **all** retained normal attempts—not just the first two—must have verified resets and pairwise-distinct reset/workspace identities.

The inherited result/failure-class matrix remains closed:

| Result | Allowed failure classes |
|---|---|
| `PASS` | `NONE` |
| `FAIL` | `PRODUCT`, `INFRA`, `HARNESS`, `UNKNOWN` |
| `INCONCLUSIVE` | `PRODUCT`, `INFRA`, `HARNESS`, `UNKNOWN` |
| `NOT_RUN` | `NONE` |

Thus the Issue #104 protections against `PASS + PRODUCT`, cross-candidate attempts, and duplicate required-injection laundering remain structural rather than advisory.

## 5. Aggregate semantics preserved

Only after the v4 generation/adaptation/attempt envelope is valid may outcome authority be derived:

- fewer than two normal attempts → `NOT_RUN`;
- any normal reset not verified → `NOT_RUN`;
- reused normal reset or workspace identity → `NOT_RUN`;
- non-common resource class → `INCONCLUSIVE`;
- duplicate required injection ID → structural `INCONCLUSIVE`, invalid envelope;
- missing required injection → `NOT_RUN`;
- used INFRA/HARNESS/UNKNOWN failure → `INCONCLUSIVE`;
- normal PASS/FAIL disagreement, including PASS/FAIL/PASS → `FLAKY`;
- required injection result other than PASS → `FAIL` unless an earlier ambiguity already failed closed;
- all normal attempts FAIL product behavior → `FAIL`;
- all normal attempts PASS plus all required injection attempts PASS → `PASS_FOR_COMPARISON`;
- explicit harness defect → `INCONCLUSIVE`, reopening all candidates for that scenario.

A failed/flaky/inconclusive generation remains immutable evidence after repair. No retry or repair may erase earlier retained attempts.

## 6. History validity split — `PG-REM3-m01`

History now exposes three explicit fields:

```yaml
valid: <lineage_valid AND evidence_valid>
lineage_valid: <generation/predecessor/candidate/work-transition structure is valid>
evidence_valid: <every generation has valid_envelope=true>
```

A lineage error sets `lineage_valid=false`, `evidence_valid=false`, and `valid=false`. A correctly linked repair history containing one malformed generation envelope reports `lineage_valid=true`, `evidence_valid=false`, `valid=false`, with reason `generation_evidence_envelope_invalid`.

This preserves the distinction requested by Issue #110: linked provenance may still be reconstructable without granting full evidence validity. A generation may legitimately aggregate `FAIL`, `FLAKY`, `NOT_RUN`, or `INCONCLUSIVE` while remaining an evidence-valid envelope; `evidence_valid` is about structural evidence integrity, not favorable outcome.

## 7. Executable evidence and deterministic identities

Executable artifact: `docs/planning/wave-2/evidence/engine-spike-protocol-fixtures.py`.

The v4 standard-library-only validator was syntax-compiled and executed twice from identical bytes. Both complete stdout streams were byte-identical, and every embedded assertion passed.

Exact v4 identities:

- validator source bytes: `sha256:915d84b10fc1744af6d077bcec5025fd95f02877af341082a45e5cfaa90bc8fa`
- validator contract: `sha256:5f37d97fa2bb263d87a10bc5cfd9311c744e1b80e83d42c8d6a9b202ccfef269`
- feature slice: `sha256:9a2523c4870146b09233397f3773f7a27b1e0135c24a6767d16e34a791aab104`
- scenario manifest: `sha256:be4d7473b01da6b428cd5f3be48de083abd161a4899471303f3ccfeef45c725f`
- fixture inputs: `sha256:15fd95e053acc634a7df2953ab411895fd47b8ee6145465a7faf6623579d3a6b`
- result object: `sha256:f76a166ec79ea08ceb2dc60ad5988f33a108a59cd153fb1157ebf0817fe850ac`
- deterministic stdout: `sha256:6f194aa5426c42e545130160da3eeb2d5e36d05ea3296d2b54c4cb9add177baa`

Any code/contract/feature/scenario/fixture/result change requires re-execution and new identities.

## 8. Fixture evidence

### 8.1 Preserved Issue #104 cases

Every pre-existing equivalence fixture object in the exact Issue #104 validator reproduces its prior ACCEPT/REJECT truth class. AG-01…AG-17 reproduce their prior aggregate classes, including:

- clean PASS remains `PASS_FOR_COMPARISON`;
- PASS/FAIL and PASS/FAIL/PASS remain `FLAKY`;
- missing injection, reused/unverified reset, and reused workspace remain `NOT_RUN`;
- omitted retained attempt, INFRA evidence, harness defect, and stronger resource remain `INCONCLUSIVE`;
- required injection PRODUCT failure remains `FAIL`;
- duplicate required-injection identity, cross-candidate normal/injection attempts, and `PASS + PRODUCT` remain invalid-envelope `INCONCLUSIVE`.

HIST-01…HIST-05 retain their lineage outcomes: the changed-work same-candidate repair remains valid; generation reuse, missing predecessor, same-work repair masquerade, and untyped candidate switch remain invalid.

### 8.2 Fresh Issue #110 attacks

| Fixture | Attack | v4 result |
|---|---|---|
| `EQ-16` | adaptation candidate changed to another exact candidate | `REJECT` |
| `EQ-17` | adaptation candidate removed | `REJECT` |
| `AG-18` | normal `reset_id=null` | structural `INCONCLUSIVE`, invalid envelope |
| `AG-19` | normal `reset_id=""` | structural `INCONCLUSIVE`, invalid envelope |
| `AG-20` | normal `workspace_id=null` | structural `INCONCLUSIVE`, invalid envelope |
| `AG-21` | normal `workspace_id=""` | structural `INCONCLUSIVE`, invalid envelope |
| `AG-22` | `reset_verified=1` instead of actual boolean | structural `INCONCLUSIVE`, invalid envelope |
| `AG-23` | `normal_index=null` | structural `INCONCLUSIVE`, invalid envelope; no exception |
| `AG-24` | `normal_index="1"` | structural `INCONCLUSIVE`, invalid envelope |
| `AG-25` | `normal_index=true` | structural `INCONCLUSIVE`, invalid envelope |
| `AG-26` | duplicate positive normal index | structural `INCONCLUSIVE`, invalid envelope |
| `AG-27` | failure-injection attempt carries a normal index | structural `INCONCLUSIVE`, invalid envelope |
| `AG-28` | candidate B adaptation + recomputed binding reused by candidate A generation | structural `INCONCLUSIVE`, invalid envelope |
| `AG-29` | valid adaptation with substituted binding ID | structural `INCONCLUSIVE`, invalid envelope |
| `HIST-06` | linked same-candidate repair containing malformed generation envelope | `lineage_valid=true`, `evidence_valid=false`, `valid=false` |

These are direct executable closures of `PG-REM3-M01`, `PG-REM3-M02`, and `PG-REM3-m01` rather than prose waivers.

## 9. W2-ENG-03 consumption contract

Before any later engine candidate execution, W2-ENG-03 must freeze:

- this exact v4 harness/validator source and semantic identities;
- corrected W2-ENG-01 admission provenance and current platform/accessibility provenance;
- one exact accepted adaptation per candidate/scenario;
- each generation's exact adaptation object and recomputed binding ID;
- exact candidate identity for every adaptation, generation, and attempt;
- common physical host/container resource profile;
- run registry, reset verification, workspace lineage, required-injection identity, and evidence-retention policy;
- manual-intervention policy; and
- exact repair-generation lineage.

A candidate unable to preserve a common bound is `INCONCLUSIVE` unless an equivalent/stronger mapping passes the exact validator. Adaptation reuse across candidate identities is forbidden. No scalar aggregate can erase hard scenario failures or evidence invalidity.

## 10. Failure controls

| Failure mode | v4 control |
|---|---|
| null/empty reset or workspace admitted | closed nonempty-string validation before aggregation |
| truthy non-boolean reset flag admitted | exact `bool` type check |
| null/string/bool/duplicate normal index passes or crashes sort | positive unique exact-int validation before sort |
| injection record masquerades as normal ordering evidence | failure-injection `normal_index` must be null |
| adaptation for candidate B credited to A | expected-candidate validation + exact adaptation binding |
| accepted adaptation relabeled after validation | generation recomputes content-addressed binding |
| linked history with malformed evidence appears fully valid | separate `lineage_valid` and `evidence_valid`; full `valid` fails |
| duplicate required injection launders failure | inherited unique-ID fail-closed validation |
| attempt from another candidate credited to generation | inherited attempt candidate binding |
| malformed PASS/failure label survives | inherited closed result/failure matrix |
| failed retry disappears | inherited registry/retained-set equality |
| easier candidate-specific workload | frozen common refs + lower bounds |
| hidden warm/editor state | cold/repository-regenerated start profile |
| stronger machine hides tooling cost | common resource class |
| repair rewrites old failure | immutable linked generations + changed work |
| repair silently switches candidate | same-candidate history unless future typed transition exists |
| harness defect benefits one candidate | all-candidate scenario reopen |
| S3 proxy produces convenient hashes | `REAL_OR_SHARED_RULES` authority |
| candidate packages easier target | exact common package placeholder |
| continuation uses private memory | hidden-context rejection |

## 11. Evidence, inference, assumptions, risks, and reopen conditions

**Observed evidence:** frozen Issue #104 harness/validator bytes; exact Issue #110 review bytes; v4 executable fixtures; two byte-identical complete executions; exact semantic/source digests above.

**Inference:** validating identity-bearing records before sorting/aggregation is the smallest fail-closed correction because comparison authority depends on exact evidence identity, while malformed identity has no safe ordering or independence interpretation.

**Recommendation:** downstream W2-ENG-03/W2-REV-01 should consume this v4 packet only after Issue #112 publishes a policy-compliant exact `STATUS(REVIEW_READY)` bound to an already-open draft PR at the same head.

**Assumptions:** no current authoritative contract defines an in-history typed candidate-transition protocol; therefore v4 continues to reject candidate identity changes within one repair history. Hashes identify exact objects but do not prove game semantics.

**Risks:** future scenario fields could require another versioned schema; a future typed candidate-transition protocol would require explicit binding changes; downstream consumers could still misuse `lineage_valid` if they ignore `evidence_valid`, so full `valid` is deliberately false when evidence envelopes are invalid.

Reopen/version this harness if any fresh v4 negative accepts, any malformed record raises instead of returning a typed invalid result, a published digest stops reproducing, adaptation identity cannot be reconstructed, a later typed candidate-transition protocol changes history rules, platform/accessibility evidence invalidates the common slice, or `W2-REV-01` finds a BLOCKER/MAJOR.

## 12. Finding disposition and bounded self-review

- `PG-REM3-M01`: **RESOLVED** — closed kind-specific attempt schema executes before sort/authority; AG-18…AG-27 cover null/empty/wrong-type/duplicate/order ambiguity paths.
- `PG-REM3-M02`: **RESOLVED** — candidate identity is required and expected-candidate checked; exact scenario/adaptation binding is content-addressed; EQ-16/17 and AG-28/29 close relabel/reuse/substitution paths.
- `PG-REM3-m01`: **RESOLVED** — history exposes lineage and evidence validity separately; HIST-06 proves a linked invalid-envelope generation cannot yield full validity.
- Issue #104 corrections: **PRESERVED** — all exact pre-existing fixture objects reproduce their declared truth classes.
- `PG-REM3-B01`: lifecycle closure is enforced by Issue #112's stopping rule: an open draft PR from `planning/issue-112` to `main` must exist and match the final branch head **before** terminal `STATUS(REVIEW_READY)`. The terminal schema-3 record is the durable proof of that step; this artifact does not pre-authorize it.

Bounded substantive self-review: **0 unresolved BLOCKER / 0 unresolved MAJOR / 0 correction-requiring MINOR** in the remediation payload. Formal aggregate `W2-REV-01` remains required.
