# W2-PG-REM-ENG-02 — Independent pre-gate review of corrected engine harness

**Review mission:** `W2-PG-REM-ENG-02` / Issue #103  
**Reviewed remediation:** Issue #94 / `W2-REM-ENG-02`  
**Reviewed terminal status:** comment `5276054674`  
**Reviewed head:** `cad3c4b546ae929668d708e6f89b58d9e0817dfb`  
**Reviewed substantive work:** `f7e3bace17046c164751d708b0711302c2a68f5c`  
**Harness blob:** `de47169cb0647d783428514e641875d5418ae027`  
**Validator blob:** `e9699ad7d02e1d99fac6d9f41545bf9eeabe5d37`  
**Disposition blob:** `ee2f6808a4633b01d9f504637968d6741f6b4356`  
**Handoff blob:** `ccb31019479a5d57c987e3b76da4894954fff8a4`  
**Source producer:** Issue #72 @ `af914fa147f22af1f544f7cdeb07a5e4234c9f8c`  
**Source pre-gate findings:** comment `5270974506`  
**Authority:** non-authority pre-gate evidence only; formal aggregate review remains `W2-REV-01`.

## 1. Disposition

`CHANGES_NEEDED`

Findings: **0 BLOCKER / 2 MAJOR / 0 correction-requiring MINOR**.

The remediation materially closes the original `PG-HARNESS-M01`, producer `SR-m01`, and `PG-HARNESS-m01` defects: the common feature slice and S1–S10 input manifest are explicit, lower bounds are executable, adaptation weakening is rejected, and the published fixture is real Python rather than prose-only truth tables. The recovery continuation also added the missing reset/workspace, failure-class, harness-defect, and repair-generation cases it identified as `REC94-SR-M01`.

However, the exact frozen v2.1 validator still has two identity/uniqueness gaps that allow `PASS_FOR_COMPARISON` from evidence that the harness prose declares invalid. These are validator defects, not merely missing explanatory text, and they sit directly on the no-laundering / immutable-lineage boundary needed before W2-ENG-03 can rely on this packet.

## 2. Cold-start / independence profile

Trust mode: `DEGRADED_SINGLE_AGENT`.

- distinct review episode/actor session: `w2-pg-rem-eng-02-agent-20260813-0651-01`;
- judged Issue #94 payload remained immutable throughout this review;
- this task writes only Issue #103 review/handoff paths;
- exact input identities were frozen before judgment;
- fresh mechanical attacks were constructed before reconciling the remediation's self-review claims;
- repository-visible degraded-mode provenance remains the canonical resource-constraint record referenced by Planning Program v1;
- stronger independent/multi-agent review remains a reopen condition, and formal `W2-REV-01` is not replaced.

## 3. What independently held

### 3.1 Common slice and anti-shrink anchoring

The frozen harness now defines one engine-neutral `W2-ENG-FEATURE-SLICE-v2` before adaptation, including exact logical state, action vocabulary, three player surfaces/routes, eight assets, save evolution, two semantic overlap locations, capture dimensions, profiling workload, common Windows x64 development package, and continuation fixture.

The frozen `W2-ENG-SCENARIO-INPUTS-v2` maps every S1–S10 scenario to exact common refs, minimum numeric bounds, closed obligations, and one required failure injection. Static inspection of `validate()` confirms rejection paths for missing refs, missing/weaker obligations, shrunk declared bounds, missing required injection declarations, warm/non-common start state, resource asymmetry, resource exceptions, hidden manual intervention, abstract S3 mechanism substitution, S9 package substitution, and S10 hidden-context transfer.

This closes the original absence of an immutable workload/equivalence anchor. No candidate-specific physical representation is granted authority to shrink the common logical work.

### 3.2 Existing executable truth classes are real

The validator contains executable EQ-01…EQ-15 fixtures, AG-01…AG-13 aggregate fixtures, and four generation-history fixtures. Static inspection confirms the fixture runner asserts the declared expected outcomes rather than merely printing an expected table. The code also content-addresses validator contract, feature slice, scenario manifest, fixture inputs, and result object using canonical JSON serialization.

The producer-published semantic digests remain exact frozen claims in the reviewed packet. This review did not treat those self-produced digests as sufficient authority; instead it attacked the exact aggregate logic with fresh synthetic records derived from the immutable validator body.

### 3.3 Authority boundaries held

The reviewed packet continues to disclaim engine scoring/selection, production-game-logic authority, implementation readiness, release/platform certification, formal review, integration, verification, and canonicalization. No authority leakage was found in that scope.

## 4. `PG-REM-HARNESS-M01` — MAJOR — duplicate required-injection identity can launder a failed injection

### Evidence

The harness states that every required failure-injection attempt is retained and that a required recovery-injection failure must aggregate to `FAIL`. It also states that omitted historical failed evidence can never become a clean PASS by retry.

The frozen validator first verifies that the run registry and `all_attempt_refs` contain every attempt ID. It then constructs required-injection lookup with:

```python
inj={a.get("injection_id"):a for a in A.values() if a.get("kind")=="FAILURE_INJECTION"}
```

No uniqueness check exists for `injection_id`. Python dictionary construction therefore keeps only the last attempt for a duplicated injection ID. The earlier attempt remains fully present in `attempts`, `run_registry_refs`, and `all_attempt_refs`, but drops out of the `used` list and out of the required-injection result check.

### Fresh mechanical attack

Using the exact frozen `aggregate()` logic, construct one S1 generation with:

- normal N1 = PASS and normal N2 = PASS, with distinct verified resets/workspaces;
- `FI-fail`: `kind=FAILURE_INJECTION`, `injection_id=FI-S1-CACHE-MISS-v2`, `result=FAIL`, `failure_class=PRODUCT`;
- `FI-pass`: a later distinct retained attempt with the **same** `injection_id=FI-S1-CACHE-MISS-v2`, `result=PASS`, `failure_class=NONE`;
- both injection attempts present in the run registry and retained-attempt list.

The exact lookup overwrites `FI-fail` with `FI-pass`, and the generation returns:

`PASS_FOR_COMPARISON`

That contradicts the declared aggregate rule `required recovery injection failure -> FAIL` while retaining, rather than omitting, the failed attempt. It is therefore a direct retry/evidence-laundering path.

### Required correction

- enforce exactly one authoritative attempt for every required `injection_id` in a generation, or define an explicit multi-attempt injection lineage whose aggregate cannot discard any failed required attempt;
- reject duplicate required-injection identities before result aggregation;
- ensure every retained required-injection attempt participates in failure-class/result authority;
- add an executable negative fixture with retained FAIL then duplicate PASS under the same required injection ID and require fail-closed behavior;
- preserve exact attempt/run-registry equality and all existing reset/resource/history behavior.

## 5. `PG-REM-HARNESS-M02` — MAJOR — attempt `candidate_id` is not bound to the generation candidate

### Evidence

The harness `AttemptRecord` explicitly includes `candidate_id`, and its mechanical invariants state that every attempt's generation/scenario/**identity** matches the generation object.

The frozen validator's attempt identity check is:

```python
for k,a in A.items():
    if a.get("attempt_id")!=k or a.get("candidate_generation_id")!=gid or a.get("scenario_id")!=sid:
        return {"aggregate":"INCONCLUSIVE","reasons":["attempt_identity_mismatch"]}
```

It never compares `a.candidate_id` to the enclosing generation's `candidate_id`.

### Fresh mechanical attack

Starting from an otherwise clean S1 generation:

- enclosing generation `candidate_id = CAND-A`;
- every retained normal and required-injection attempt `candidate_id = CAND-B`;
- attempt IDs, generation ID, scenario ID, resets, workspaces, resource class, registry, and results remain valid.

The exact frozen `aggregate()` logic still returns:

`PASS_FOR_COMPARISON`

Thus an aggregate can claim candidate A while consuming candidate B attempt evidence. The field exists in the record schema but has no mechanical authority binding.

### Required correction

- require every attempt `candidate_id == generation.candidate_id`;
- validate the generation candidate identity consistently across repair-history entries unless an explicitly typed candidate-transition rule permits a change;
- add negative fixtures for cross-candidate normal-attempt substitution and cross-candidate injection substitution;
- keep changed `candidate_work_id` as the repair-generation mechanism rather than allowing candidate-evidence substitution.

## 6. Additional fail-closed observation

The same aggregate function does not currently enforce result/failure-class coherence such as `PASS` paired with `PRODUCT`; only `INFRA`, `HARNESS`, and `UNKNOWN` classes are automatically `INCONCLUSIVE`. A fresh malformed record with normal `result=PASS` and `failure_class=PRODUCT` can therefore remain in a clean `PASS_FOR_COMPARISON` aggregate.

This review does not count that as a third material finding because the two MAJOR corrections already require a proper attempt-envelope validation pass. The successor remediation should nevertheless add a closed result/failure-class validity matrix so malformed combinations fail closed rather than rely on producer discipline.

## 7. Prior finding dispositions

| Prior finding | Review conclusion |
|---|---|
| `PG-HARNESS-M01` | Substantively closed: exact common slice/input package and anti-shrink validator now exist. |
| `SR-m01` | Substantively closed: executable validator/fixtures exist. |
| `PG-HARNESS-m01` | Substantively closed: equivalence and aggregate truth cases are executable/content-addressed. |
| `REC94-SR-M01` | Its named missing truth classes were added, but the expanded lineage implementation exposes the two new MAJOR gaps above. |

The new findings do not reopen the old common-slice defect; they specifically invalidate reliance on v2.1 aggregate attempt/injection identity as a complete no-laundering proof.

## 8. Required route

Route exactly one bounded remediation successor for the two MAJOR findings. The successor must consume Issue #94 and this review at immutable SHAs, edit only a new branch, publish corrected validator/harness/dispositions/handoff evidence, and remain non-authority input for formal `W2-REV-01`.

Until that remediation is frozen and independently/formally reviewed as required, W2-ENG-03 must not treat Issue #94 v2.1 as a clean engine-comparison evidence packet.

No engine is executed, scored, ranked, or selected by this review.