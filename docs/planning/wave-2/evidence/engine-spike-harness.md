# W2-REM-ENG-05 — Engine spike harness v5

**Mission:** `W2-REM-ENG-05` / Issue #126  
**Task class:** bounded engine-harness remediation / `EVIDENCE_REQUIRED`  
**Predecessor:** Issue #112 exact work/head `6c5777ca56d43e22cba9b5e776e436d11b846325`  
**Independent review:** Issue #122 exact work/head `c535bb9e94cb0da3aeb0d66dcc2606c034d7412f`, terminal comment `5276962394`  
**Predecessor validator blob:** `7837695c91365273b2c89f3852b401c2f127af54`  
**Authority:** noncanonical `PLANNING_EXPERIMENT` evidence only. This packet neither executes nor scores an engine and creates no engine-selection, production, readiness, implementation, integration, verification, release, or canonicalization authority.

## Remediation scope

This v5 packet changes only the three findings from independent review #122:

- `PG-REM4-M01` — make the closed `result × failure_class` envelope total over malformed value types, including list/dict/container values.
- `PG-REM4-M02` — enforce one-to-one unique retained-attempt registry/reference identity instead of set-only equality.
- `PG-REM4-m01` — reject malformed adaptation/registry container shapes deterministically instead of raising.

All earlier Issue #112 protections remain required and are re-exercised by the same executable validator corpus: candidate/adaptation binding, common S1–S10 feature-slice bounds, closed kind-specific AttemptRecord schema, required-injection uniqueness, cross-candidate attempt rejection, reset/workspace/resource controls, result/failure semantics, no-laundering aggregate behavior, repair-generation lineage, lineage/evidence validity split, S3 authority bounds, S9 package scope, and S10 hidden-context rejection.

## Exact executable packet

The executable source is:

`docs/planning/wave-2/evidence/engine-spike-protocol-fixtures.py`

Local fresh execution on the exact bytes used for this packet produced:

- source bytes: `28352`;
- predicted Git blob identity from `sha1("blob 28352\0" + bytes)`: `2c646988dc16e212f43df6a4ee5ce646622ac2a6`;
- raw validator source SHA-256: `9a50e3e21279a7a94836d6162fee218a0e187bafe292847fd5f0b108df45deea`;
- validator contract SHA-256: `ed1de63a02872c18981259a15eb8393b3d94d5f7af774b4b1f771c1c4e2e77ef`;
- feature-slice SHA-256: `9a2523c4870146b09233397f3773f7a27b1e0135c24a6767d16e34a791aab104`;
- scenario-manifest SHA-256: `be4d7473b01da6b428cd5f3be48de083abd161a4899471303f3ccfeef45c725f`;
- fixture-input SHA-256: `45555e8370f821d66fa8febdd58d475b88c15b0505ab996a4a8954ef8ef11613`;
- result-object SHA-256: `8612a359c029e4d921356d214177a3478a0ee45011f8d26a629850180748a071`;
- deterministic stdout SHA-256: `e4a5279f4abb0a5b7eb4cfc2b4e64615be966c9e656dc4d6a610741b66a82ff0`;
- independent remediation-regression evidence SHA-256: `58294d195025f32235bac3b6a7d4ea0eb20aebe0a79fb760fe80750eb069b9ef`.

`python -m py_compile` succeeded. Two complete runs were byte-identical.

The feature slice and scenario manifest identities intentionally remain unchanged from Issue #112. Validator-contract, fixture-input, result-object, source, and stdout identities change because v5 adds structural closure and new regression cases.

## Closed malformed result/failure envelope

The authority-bearing enum pair is accepted only after scalar shape validation:

- `result` must be a nonempty string and one of `PASS`, `FAIL`, `INCONCLUSIVE`, `NOT_RUN`;
- `failure_class` must be a nonempty string and must be permitted by the closed matrix for that exact result;
- list, dict, null, numeric, boolean, or otherwise non-string values are structural invalid evidence;
- malformed values return aggregate `INCONCLUSIVE` with `valid_envelope=false`; they never reach hash-based membership or comparison authority.

Fresh regressions include:

- `AG-30_unhashable_result`;
- `AG-31_unhashable_failure_class`;
- `AG-42_dict_result`;
- `AG-43_dict_failure_class`.

All return typed structural invalid evidence without exceptions.

## One-to-one retained-attempt registry contract

For both `run_registry_refs` and `all_attempt_refs`:

1. the container must be a list;
2. every member must be a nonempty exact attempt ID string;
3. IDs must be unique;
4. list cardinality must equal retained `attempts` key cardinality;
5. the unique ID set must equal the retained attempt-key set exactly.

This preserves omission/extra rejection and closes duplicate-ref laundering. A duplicated existing ref cannot retain `PASS_FOR_COMPARISON`.

Fresh regressions include:

- `AG-32_duplicate_run_registry_ref`;
- `AG-33_duplicate_all_attempt_ref`;
- `AG-34_null_run_registry_refs`;
- `AG-35_null_all_attempt_refs`;
- `AG-44_string_run_registry_refs`;
- `AG-45_dict_all_attempt_refs`.

All return `INCONCLUSIVE`, `valid_envelope=false`.

## Closed adaptation container contract

Before any set, mapping, numeric, or digest operation, v5 structurally validates the authority-bearing adaptation fields:

- `scenario_id`: nonempty string resolving to one declared S1–S10 scenario;
- `candidate_id`: nonempty string and exact consumer candidate;
- `harness_id`: exact `W2-ENG-HARNESS-v5`;
- `feature_slice_id`: exact `W2-ENG-FEATURE-SLICE-v2`;
- `fixed_input_refs`: unique nonempty-string list containing every scenario-required common ref;
- `mappings`: string-keyed mapping with every required obligation `EQUIVALENT` or `STRICTLY_STRONGER`;
- `bounds`: string-keyed mapping whose required bounds are finite int/float values and not weaker than the common bound;
- `failure_injections`: unique nonempty-string list containing every required injection;
- `start_profile`: mapping with exact cold/reconstruct/common-resource controls;
- the full adaptation must have deterministic canonical-JSON identity before an adaptation binding can be accepted.

Fresh malformed-shape regressions:

- `AG-36_malformed_fixed_input_refs`;
- `AG-37_malformed_mappings`;
- `AG-38_malformed_bounds`;
- `AG-39_malformed_failure_injections`;
- `AG-40_malformed_start_profile`;
- `AG-41_unhashable_adaptation_scenario_id`;
- `AG-46_list_mappings`;
- `AG-47_list_bounds`;
- `AG-48_dict_failure_injections`;
- `AG-49_list_start_profile`.

Each fails closed without exception or comparison authority. Legitimate candidate-native stronger/equivalent mappings remain accepted when common obligations and bounds are preserved.

## Preserved AttemptRecord and aggregation rules

Every retained attempt remains bound to exact `attempt_id`, `scenario_id`, `candidate_id`, and `candidate_generation_id`. Kinds remain closed to `NORMAL` and `FAILURE_INJECTION`.

For `NORMAL` attempts:

- `normal_index` must be an exact positive integer, not boolean;
- indices are unique;
- reset and workspace identities are nonempty and normal attempts cannot reuse them;
- `reset_verified` is exact boolean;
- no injection ID is permitted.

For failure-injection attempts:

- no normal index is permitted;
- exact nonempty injection ID is required;
- each required injection identity appears exactly once;
- a retained failed required injection cannot be overwritten or laundered by a duplicate PASS.

At least two normal attempts are required for comparison. Failed-attempt omission remains visible through registry mismatch. `PASS`/`FAIL` disagreement remains `FLAKY`. `INFRA`, `HARNESS`, or `UNKNOWN` in used attempts remains `INCONCLUSIVE`. Resource asymmetry remains `INCONCLUSIVE`. Harness defect reopens all candidates for that scenario.

## Preserved adaptation/common-slice authority

`W2-ENG-FEATURE-SLICE-v2` and `W2-ENG-SCENARIO-INPUTS-v2` remain the common S1–S10 basis. Candidate adaptation may use native physical representation only when it preserves or strengthens declared common inputs, obligations, bounds, start/resource controls, required injections, S3 real/shared-rule authority, S9 common package target, and S10 no-hidden-context constraint.

No candidate-specific easier workload may gain comparison authority.

## Preserved repair/history semantics

Repair history keeps structural lineage authority distinct from evidence-envelope validity:

- generation IDs cannot repeat;
- predecessor links are exact;
- a repair generation must change work identity and carry a nonempty repair-change ref;
- candidate identity cannot silently change;
- each generation is independently aggregated;
- structurally linked history containing any invalid generation reports `lineage_valid=true`, `evidence_valid=false`, `valid=false`.

This prevents structurally valid lineage from laundering malformed generation evidence.

## Regression corpus

The executable packet contains **71 declared fixture truth classes**:

- 16 equivalence/adaptation cases (`EQ-*`);
- 49 aggregate/attempt/adaptation cases (`AG-*`);
- 6 repair-history cases (`HIST-*`).

The first **51** truth classes are the inherited Issue #112 corpus (16 EQ + 29 AG + 6 HIST) and retain their declared outcomes. The final **20** AG cases are fresh Issue #126 regressions for `PG-REM4-M01`, `PG-REM4-M02`, and `PG-REM4-m01`.

The validator asserts all declared outcomes before emitting semantic digests. Any assertion failure terminates the run and cannot create comparison authority.

## Finding closure

- `PG-REM4-M01`: **RESOLVED** — type/shape checks precede matrix membership; list/dict malformed enum values reject deterministically.
- `PG-REM4-M02`: **RESOLVED** — both retained-attempt registries require unique exact one-to-one identity; duplicate/null/malformed containers reject.
- `PG-REM4-m01`: **RESOLVED** — adaptation and registry container/key shapes are validated before authority-bearing operations.

Self-review against the bounded Issue #126 scope found **0 unresolved BLOCKER / 0 unresolved MAJOR / 0 correction-requiring MINOR**.

## Reopen rules

Reopen this remediation evidence if any of the following changes:

- validator bytes or any published semantic identity;
- feature slice, S1–S10 scenario manifest, or common resource/start contract;
- adaptation-binding fields or canonicalization;
- attempt schema, result/failure matrix, registry contract, or aggregate semantics;
- repair/history validity semantics;
- a fresh independent attack demonstrates an exception, duplicate-ref acceptance, malformed-container comparison authority, or regression of an inherited Issue #112 truth class.

Formal aggregate review `W2-REV-01` remains required. Any eventual main integration remains separately authorized and squash-only.
