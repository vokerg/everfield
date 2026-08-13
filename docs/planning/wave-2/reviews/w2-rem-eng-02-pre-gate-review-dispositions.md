# W2-REM-ENG-03 — Issue #103 pre-gate finding dispositions

**Remediation issue:** #104 / `W2-REM-ENG-03`  
**Frozen predecessor remediation:** Issue #94 / `W2-REM-ENG-02` work `f7e3bace17046c164751d708b0711302c2a68f5c`  
**Frozen predecessor harness/validator blobs:** `de47169cb0647d783428514e641875d5418ae027` / `e9699ad7d02e1d99fac6d9f41545bf9eeabe5d37`  
**Independent pre-gate review:** Issue #103 work `9fb365e2ad84c04d2e12305b38b40ddc30153530`, terminal comment `5276155477`  
**Review disposition:** `CHANGES_NEEDED`, 0 BLOCKER / 2 MAJOR  
**Authority:** bounded noncanonical remediation evidence; formal `W2-REV-01` remains required.

## Disposition summary

| Finding | Severity | Disposition | Mechanical closure |
|---|---|---|---|
| `PG-REM-HARNESS-M01` | MAJOR | RESOLVED | Failure-injection attempts are grouped before lookup; duplicate `injection_id` values invalidate the envelope. AG-14 retains a PRODUCT FAIL plus duplicate PASS and returns non-comparable `INCONCLUSIVE`. |
| `PG-REM-HARNESS-M02` | MAJOR | RESOLVED | Every attempt must bind `candidate_id == generation.candidate_id`; AG-15/AG-16 reject normal/injection cross-candidate substitution; HIST-05 rejects an untyped candidate switch across repair generations. |
| Issue #103 envelope observation | bounded correction | RESOLVED | Closed `result × failure_class` matrix; AG-17 proves malformed `PASS + PRODUCT` fails closed. |
| prior Issue #94 common-slice/equivalence/reset/history behavior | regression risk | PRESERVED | EQ-01…15, AG-01…13, HIST-01…04 reproduce their prior truth classes. |

Final bounded self-review: **0 unresolved BLOCKER / 0 unresolved MAJOR / 0 correction-requiring MINOR**.

## `PG-REM-HARNESS-M01` — duplicate required-injection identity laundering

### Frozen defect

Issue #103 showed that v2.1 built required-injection authority with a dictionary keyed by `injection_id` without first checking uniqueness. A retained failed attempt could remain in the registry while a later duplicate PASS under the same required ID overwrote it in the lookup and produced `PASS_FOR_COMPARISON`.

### v3 correction

`aggregate()` now performs structural validation before any required-injection result authority:

1. every FAILURE_INJECTION record must have a nonempty `injection_id`;
2. every retained FAILURE_INJECTION is grouped by `injection_id`;
3. any ID with cardinality other than one invalidates the attempt envelope; and
4. only after uniqueness passes may each required scenario injection resolve to its one retained record.

AG-14 is the exact retained-failure attack: S1 keeps two normal PASS attempts, one required-injection PRODUCT FAIL, and a second retained PASS with the same `FI-S1-CACHE-MISS-v2` identity. All four records remain in `attempts`, `run_registry_refs`, and `all_attempt_refs`. v3 returns `INCONCLUSIVE`, reason `duplicate_injection_id:FI-S1-CACHE-MISS-v2`, `valid_envelope=false`.

The failed injection therefore cannot disappear through lookup order or retry identity reuse.

**Disposition:** RESOLVED.

## `PG-REM-HARNESS-M02` — candidate evidence substitution

### Frozen defect

Issue #103 showed that v2.1 bound `attempt_id`, generation ID, and scenario ID but did not compare each attempt's `candidate_id` to the enclosing generation candidate. A generation labeled candidate A could therefore consume candidate B attempts and still reach comparison PASS.

### v3 correction

Structural identity now requires for every retained attempt:

`attempt.candidate_id == generation.candidate_id`

AG-15 changes one otherwise-valid normal attempt to `OTHER-CANDIDATE`; AG-16 changes the required injection attempt. Both return structural `INCONCLUSIVE` with `valid_envelope=false` before outcome aggregation.

Repair history also requires every generation in the history to retain the root candidate identity absent an explicitly typed candidate-transition rule. HIST-05 switches a successor generation and all its attempts to `OTHER-CANDIDATE`; `history()` rejects it with `candidate_identity_changed_without_typed_transition`. Changed `candidate_work_id`, not candidate substitution, remains the repair mechanism.

**Disposition:** RESOLVED.

## Closed result/failure-class envelope

Issue #103 additionally observed that v2.1 could accept `result=PASS` with `failure_class=PRODUCT`. v3 defines this closed matrix:

| Result | Allowed failure classes |
|---|---|
| `PASS` | `NONE` |
| `FAIL` | `PRODUCT`, `INFRA`, `HARNESS`, `UNKNOWN` |
| `INCONCLUSIVE` | `PRODUCT`, `INFRA`, `HARNESS`, `UNKNOWN` |
| `NOT_RUN` | `NONE` |

Every unlisted combination invalidates the envelope. AG-17 mutates an otherwise clean S1 normal PASS to `failure_class=PRODUCT`; it deterministically returns `INCONCLUSIVE`, `valid_envelope=false`.

This preserves existing INFRA/HARNESS/UNKNOWN semantics: valid FAIL attempts with those classes remain typed evidence and cause aggregate `INCONCLUSIVE`; they are not converted to PRODUCT or silently ignored.

**Disposition:** RESOLVED.

## Regression evidence

The corrected validator was syntax-compiled and executed with Python standard library only. Embedded assertions prove:

- EQ-01…EQ-15 retain their exact prior outcomes: 5 ACCEPT / 10 REJECT;
- AG-01 clean remains `PASS_FOR_COMPARISON`;
- AG-02 and AG-13 remain `FLAKY`;
- AG-03/04/05/10/11 remain `NOT_RUN`;
- AG-06/07/09/12 remain `INCONCLUSIVE`;
- AG-08 remains `FAIL`;
- HIST-01 retains `GEN-1=FAIL` and linked changed-work `GEN-2=PASS_FOR_COMPARISON`;
- HIST-02/03/04 remain invalid;
- AG-14/15/16/17 and HIST-05 close the new attack paths.

Exact v3 digests:

- validator source bytes: `sha256:306285bed232161d63ba52330f785e2bcaab00cd3b574d65fc584fc56a0132d7`
- validator contract: `sha256:357e25f9af9ac71804f322797c3ea1aa0c923167178b9c2eb8c84ef3280cbe23`
- feature slice: `sha256:9a2523c4870146b09233397f3773f7a27b1e0135c24a6767d16e34a791aab104`
- scenario manifest: `sha256:be4d7473b01da6b428cd5f3be48de083abd161a4899471303f3ccfeef45c725f`
- fixture inputs: `sha256:3172768f6288135c4b99dfd802882a5394b709b3fa0f74688bd17106a6b3c8ff`
- result object: `sha256:d79120f698bd9409bc6956162216a36a85f62592f4eff5db39b6fdc288149029`

## Prior Issue #94 findings remain closed

This successor does not reopen `PG-HARNESS-M01`, producer `SR-m01`, `PG-HARNESS-m01`, or `REC94-SR-M01`. The exact common feature slice, S1–S10 manifest, anti-shrink adaptation rules, reset/workspace/resource lineage, repair-generation history, harness-defect reopening, S3/S9/S10 authority boundaries, and no-engine-selection scope are preserved.

## Authority boundary and route

Issue #104 remains noncanonical planning evidence. It does not execute or select an engine, claim production/readiness authority, replace formal `W2-REV-01`, or authorize integration/canonicalization.

Once Issue #104 publishes exact terminal `STATUS(REVIEW_READY)`, its frozen work/head becomes the corrected substantive W2-ENG-02 remediation input for downstream W2-ENG-03/W2-REV-01 while Issues #72/#94/#103 remain immutable provenance.
