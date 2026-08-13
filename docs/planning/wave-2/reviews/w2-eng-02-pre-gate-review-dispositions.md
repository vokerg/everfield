# W2-REM-ENG-02 — Pre-gate finding dispositions

**Remediation issue:** #94 / `W2-REM-ENG-02`  
**Frozen producer:** Issue #72 / `W2-ENG-02` @ `af914fa147f22af1f544f7cdeb07a5e4234c9f8c`  
**Producer harness blob:** `da29b1b867f01f0efaeda28616f4f5dc329ee2c9`  
**Producer handoff blob:** `3857e514f786b404c1c6948bdf7b3ed68c168920`  
**Independent pre-gate review:** Issue #72 comment `5270974506`  
**Disposition scope:** bounded remediation evidence only; formal `W2-REV-01` remains required.

## Disposition summary

| Finding | Severity | Disposition | Mechanical closure |
|---|---|---|---|
| `PG-HARNESS-M01` | MAJOR | CLOSED | Frozen `FeatureSliceContract` + `ScenarioInputManifest`; exact S1–S10 refs; measurable lower bounds; executable adaptation validation. |
| `SR-m01` | MINOR | CLOSED | Deterministic Python validator/fixtures now consume machine-readable adaptation, attempt, generation, reset/resource, and history objects. |
| `PG-HARNESS-m01` | MINOR | CLOSED | Original equivalence and retry/reset truth classes are executable, asserted, and content-addressed. |
| `REC94-SR-M01` | MAJOR, recovery self-review | CLOSED BEFORE TERMINAL | Inherited v2 executable omitted several original retry/reset truth classes despite claiming coverage; v2.1 adds failure classes, verified reset/workspace lineage, repair-generation history, harness-defect reopening, and complete corresponding fixtures. |

Final bounded self-review: **0 unresolved BLOCKER / 0 unresolved MAJOR / 0 correction-requiring MINOR**.

## `PG-HARNESS-M01`

### Original defect

The frozen producer had intent-level scenario descriptions and an anti-weakening rule, but no immutable common feature/input package against which a reviewer could mechanically decide whether one engine received an easier workload.

### Correction

`W2-ENG-HARNESS-v2.1` binds:

- `W2-ENG-FEATURE-SLICE-v2` with exact logical state, action vocabulary, player surface, eight-asset fixture, save evolution, two semantic merge overlaps, capture dimensions, profiling workload, common Windows x64 development package, and fresh-continuation partial state;
- `W2-ENG-SCENARIO-INPUTS-v2`, where every S1–S10 scenario resolves exact common refs, obligations, lower bounds, and required failure injection; and
- `AdaptationManifest` rules that reject missing refs/obligations, numeric shrinkage, hidden/warm state, stronger resource class, missing failure injections, abstract S3 substitution, package substitution, hidden manual intervention, and hidden S10 context.

Candidate-native physical representation remains permitted only when the common claim is preserved or strengthened.

**Disposition:** CLOSED.

## `SR-m01` / `PG-HARNESS-m01`

### Original defect

The producer's EQ-01…EQ-12 and retry/reset truth cases were Markdown assertions rather than executable evidence.

### Correction

`docs/planning/wave-2/evidence/engine-spike-protocol-fixtures.py` is a standard-library-only `PLANNING_EXPERIMENT` validator. It asserts:

- original EQ-01…EQ-12 outcomes plus bound/resource/obligation negatives;
- clean, flaky, missing-attempt, missing-injection, resource-asymmetry, reset/workspace, injection-failure, infra, and harness-defect aggregate cases;
- the original repair-generation truth: a product-failing generation remains `FAIL`, while a changed-work successor may separately become `PASS_FOR_COMPARISON`; and
- negative history attacks for generation reuse, missing predecessor linkage, and same-work repair masquerade.

Executed semantic digests:

- validator contract: `sha256:48bd4df89b653699f5ae94db267b14a5243a8f02b10a79f4c175a61eb8173e5f`
- feature slice: `sha256:9a2523c4870146b09233397f3773f7a27b1e0135c24a6767d16e34a791aab104`
- scenario manifest: `sha256:be4d7473b01da6b428cd5f3be48de083abd161a4899471303f3ccfeef45c725f`
- fixture inputs: `sha256:9ad8207e1cecdf8d0933881290888e4c1a6d85e83ccb6e377dd0ab3a52b9e565`
- result object: `sha256:ff0163f3e9e185e9eb43519bb67f2f0f138ec8f2391d97a36a8916433f5912a8`

All embedded assertions passed in the recovery episode.

**Disposition:** CLOSED.

## `REC94-SR-M01` — recovery continuation self-review

After recovering stale ownership, the continuation episode independently inspected inherited head `3dcd8ffd05c152da99aab32bce94e57e1a8beb02`.

The inherited v2 artifacts correctly fixed the common-slice MAJOR, but the executable aggregate suite covered only six cases and did not mechanically reproduce several producer truth classes it claimed to preserve: repaired-generation lineage (`R-02`), infra ambiguity (`R-04`), harness-defect reopening (`R-08`), and stronger reset/workspace lineage. Treating that inherited state as terminal would have overstated executable evidence.

v2.1 corrects the gap by:

1. binding every attempt to one candidate generation;
2. typing failure class separately from attempt result;
3. requiring exact verified reset and workspace identities;
4. validating immutable predecessor/change linkage for repair generations; and
5. making harness defects reopen the scenario for all candidates.

**Disposition:** CLOSED BEFORE TERMINAL; no separate successor is required because the finding was discovered and corrected inside the still-live remediation episode before publication of `STATUS(REVIEW_READY)`.

## Preserved authority boundaries

This remediation does **not**:

- execute, score, rank, or select an engine;
- turn hashes into semantic correctness authority;
- convert the Windows x64 common package into a release commitment;
- grant Valve/store/partner/platform certification;
- authorize production gameplay or implementation readiness;
- replace `W2-REV-01`; or
- authorize integration/canonicalization.

Issue #72 remains immutable provenance. The exact Issue #94 terminal work/head, once published, is the only remediation identity downstream consumers may treat as the corrected substantive W2-ENG-02 input.
