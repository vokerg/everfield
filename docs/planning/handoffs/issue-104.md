# Handoff — Issue #104 / W2-REM-ENG-03

## Identity

- mission: `W2-REM-ENG-03`
- issue: #104
- branch: `planning/issue-104`
- ownership generation: claim comment `5276164972`
- actor session: `w2-rem-eng-03-agent-20260813-0659-01`
- base: `main@c7ba185ed9667b717794c19eaa0834ca41aa4c78`
- authority: noncanonical Wave 2 remediation evidence only

## Immutable predecessor/review packet

- Issue #94 terminal status: comment `5276054674`
- Issue #94 frozen head: `cad3c4b546ae929668d708e6f89b58d9e0817dfb`
- Issue #94 substantive work: `f7e3bace17046c164751d708b0711302c2a68f5c`
- Issue #94 harness blob: `de47169cb0647d783428514e641875d5418ae027`
- Issue #94 validator blob: `e9699ad7d02e1d99fac6d9f41545bf9eeabe5d37`
- Issue #94 disposition blob: `ee2f6808a4633b01d9f504637968d6741f6b4356`
- Issue #94 handoff blob: `ccb31019479a5d57c987e3b76da4894954fff8a4`
- Issue #103 terminal status: comment `5276155477`
- Issue #103 review work: `9fb365e2ad84c04d2e12305b38b40ddc30153530`
- Issue #103 terminal head: `00331d3cc9cbe29fa20f27be159b5730e3f3b142`
- Issue #103 disposition: `CHANGES_NEEDED`
- findings routed here: `PG-REM-HARNESS-M01`, `PG-REM-HARNESS-M02`

Issues #94 and #103 were consumed only at these immutable identities and were not modified or re-owned.

## Completed corrections

1. **Required-injection identity laundering closed.** The aggregate validator now groups retained failure-injection attempts by `injection_id` and requires exactly one retained authoritative attempt for every required injection. Duplicate identities fail closed before result aggregation; a retained required FAIL plus duplicate PASS cannot overwrite or suppress the failure.
2. **Attempt-to-generation candidate binding closed.** Every attempt must bind the enclosing generation `candidate_id`, in addition to exact attempt ID, scenario ID, and generation ID. Cross-candidate normal-attempt and failure-injection substitutions fail closed. Repair history also rejects an undeclared candidate identity change.
3. **Attempt envelope made closed and fail-closed.** The validator now enforces the exact `result × failure_class` matrix. Contradictory records such as `PASS + PRODUCT`, unknown attempt kinds, or kind/injection-field mismatches are invalid evidence envelopes and cannot produce a comparable aggregate.
4. **Existing v2.1 semantics preserved.** Exact run-registry/retained-attempt equality, two-normal-attempt floor, distinct verified reset/workspace identities, common resource class, required injections, PASS/FAIL/PASS flake detection, harness-defect all-candidate reopening, changed-work repair lineage, S3 authority limit, S9 package scope, and S10 hidden-context rejection remain intact.
5. **Executable regression coverage added.** New cases exercise duplicate required-injection FAIL/PASS laundering, cross-candidate normal substitution, cross-candidate injection substitution, malformed PASS/PRODUCT envelope, and cross-candidate repair history. All prior EQ, aggregate, and history truth classes continue to pass their declared assertions.

## Corrected artifact identities

- harness: `W2-ENG-HARNESS-v3`
- validator: `W2-ENG-PROTOCOL-VALIDATOR-v3`
- feature slice: unchanged `W2-ENG-FEATURE-SLICE-v2`
- scenario manifest: unchanged `W2-ENG-SCENARIO-INPUTS-v2`

Exact semantic/source digests from the executable packet:

- validator source: `sha256:306285bed232161d63ba52330f785e2bcaab00cd3b574d65fc584fc56a0132d7`
- validator contract: `sha256:357e25f9af9ac71804f322797c3ea1aa0c923167178b9c2eb8c84ef3280cbe23`
- feature slice: `sha256:9a2523c4870146b09233397f3773f7a27b1e0135c24a6767d16e34a791aab104`
- scenario manifest: `sha256:be4d7473b01da6b428cd5f3be48de083abd161a4899471303f3ccfeef45c725f`
- fixture inputs: `sha256:3172768f6288135c4b99dfd802882a5394b709b3fa0f74688bd17106a6b3c8ff`
- result object: `sha256:d79120f698bd9409bc6956162216a36a85f62592f4eff5db39b6fdc288149029`

The unchanged feature-slice and scenario-manifest digests are evidence that this remediation did not silently alter the comparison workload while closing identity/envelope defects.

## Executed checks

The exact validator bytes were checked with Python 3 standard library only:

- `python3 -m py_compile docs/planning/wave-2/evidence/engine-spike-protocol-fixtures.py`
- `python3 docs/planning/wave-2/evidence/engine-spike-protocol-fixtures.py`

All embedded assertions passed.

Coverage/results:

- 15 equivalence/adaptation fixtures preserve their expected ACCEPT/REJECT outcomes.
- 17 aggregate fixtures preserve the original truth classes and add four fail-closed envelope/identity attacks.
- 5 repair-history fixtures include the valid linked repair plus generation reuse, missing predecessor, same-work masquerade, and cross-candidate-generation rejection.
- duplicate required injection retained FAIL + duplicate PASS: `INCONCLUSIVE`, invalid envelope.
- cross-candidate normal attempt: `INCONCLUSIVE`, invalid envelope.
- cross-candidate required injection: `INCONCLUSIVE`, invalid envelope.
- `PASS + PRODUCT`: `INCONCLUSIVE`, invalid envelope.
- original clean case remains `PASS_FOR_COMPARISON`.
- original product-fail then changed-work linked repair remains `GEN-1=FAIL`, `GEN-2=PASS_FOR_COMPARISON` without rewriting history.

## Finding dispositions / self-review

- `PG-REM-HARNESS-M01`: **RESOLVED** with executable duplicate-identity rejection and retained-failure coverage.
- `PG-REM-HARNESS-M02`: **RESOLVED** with attempt/generation candidate equality plus cross-candidate negatives.
- Issue #103 bounded result/failure-class observation: **RESOLVED** by the closed attempt-envelope matrix and executable malformed-envelope case.
- prior Issue #94 common-slice, anti-shrink, reset/workspace, resource, repair-lineage, S3/S9/S10, and authority-boundary behavior: **NO REGRESSION FOUND**.

Final bounded self-review: **0 unresolved BLOCKER / 0 unresolved MAJOR / 0 correction-requiring MINOR**.

## Authority and downstream route

This remediation does **not** execute, score, rank, or select an engine. It does not create production code, implementation readiness, release/platform certification, integration authority, verification authority, or canonicality.

Once the terminal schema-3 `STATUS(REVIEW_READY)` freezes the exact Issue #104 work/head, that tuple is the corrected substantive W2-ENG-02 remediation input for W2-ENG-03 and formal aggregate `W2-REV-01`, while Issues #72/#94/#103 remain immutable provenance. `W2-REV-01` remains the required independent adversarial authority gate.

Any eventual `main` integration remains squash-only through a separately valid declared route. Issue #104 itself does not authorize integration.

## Continuation state

The bounded remediation is complete. No code/artifact correction remains known inside Issue #104 scope. The only remaining mutation for this episode after committing this handoff is publication of the exact terminal schema-3 `STATUS(REVIEW_READY)` containing the final branch head/work SHA and immutable artifact refs.

The final branch head is intentionally not self-referenced in this file; the terminal Issue #104 status is the authority record for it.
