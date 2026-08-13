# W2-PG-SIM-01 — Independent pre-gate review of W2-SIM-01

**Mission:** `W2-PG-SIM-01` / Issue #130  
**Reviewed mission:** `W2-SIM-01` / Issue #83  
**Reviewed head:** `999d67726f849d09dc812529170645332258f32f`  
**Reviewed substantive work:** `709657b7c0a09e46a35ed989e75764ccaddb7033`  
**Reviewed report blob:** `9d292c63d4316fbe655f08fc026f92dd55aca91c`  
**Reviewed handoff blob:** `b0f243acd674a509f3c3dd87e2e7ce2f3c1eaf27`  
**Disposition:** `CHANGES_NEEDED`  
**Authority:** noncanonical pre-gate evidence only; formal `W2-REV-01` remains required.

## 1. Review boundary and attack plan

This review treats Issue #83 as immutable read-only input. It attacks only whether the frozen packet supports its exact positive model-side claims and correctly preserves the missing shared-kernel side as `NOT_RUN` / `INCONCLUSIVE`.

Attack order:

1. bind exact report/handoff identities;
2. inspect the frozen corpus identity contract for exact-byte reconstructability;
3. inspect the model-result identity and claimed two-evaluator agreement for reproducibility;
4. trace every parity cell and aggregate claim for laundering of absent shared-kernel evidence;
5. inspect upstream W2-ENG-03 propagation and representative-kernel identity;
6. inspect rerun/reopen conditions for any route that can strengthen authority without real kernel execution.

## 2. Exact reviewed evidence

The exact Issue #83 report at reviewed head is Git blob `9d292c63d4316fbe655f08fc026f92dd55aca91c`; the handoff is blob `b0f243acd674a509f3c3dd87e2e7ce2f3c1eaf27`. Both agree on:

- upstream W2-ENG-03 work/head `1575cb3a18c9c7be1776b64c9ec92cc8990a97e0` and result `INCONCLUSIVE_ENVIRONMENT_BLOCKED`;
- `representative_shared_kernel_identity: null`;
- six model scenarios executed;
- six shared-kernel cells `NOT_RUN`;
- zero parity PASS and zero parity FAIL;
- six parity `INCONCLUSIVE` cells;
- corpus SHA-256 `2cff8e26fa0d86a6f08bad97d4e132d53f3c97f9679a12d21f9d437ee05df017`;
- normalized model-result SHA-256 `0c29eda299ecd56404a4e958b0521b5cdd40c20acb2861e55c92931b6a64d782`.

The report defines an experiment-local canonicalization rule in prose and prints the initial state, action lists, transition-rule table, failure reason vocabulary, scenario summaries, and parity matrix.

## 3. Findings

### PG-SIM-M01 — MAJOR — published corpus identity is not independently reconstructable from frozen bytes

The report names `SIM-PARITY-CORPUS-v1` and states that corpus identity uses UTF-8 JSON with recursively sorted object keys, preserved list order, and no insignificant whitespace. However, it never publishes the exact canonical corpus object or exact canonical JSON bytes whose SHA-256 is asserted as `2cff8e26...`.

The human-readable packet separately presents schema/rule/content labels, initial-state JSON, YAML action lists, a prose/table transition specification, and a failure-reason list. It does not define one unambiguous machine object that combines those surfaces, including exact field names, nesting, ordering of rule/failure-code collections, representation of action tuples, and whether prose-only semantic clauses such as rejected-action immutability are identity-bearing.

Therefore an independent reviewer cannot recompute the claimed corpus digest from the frozen packet without guessing a producer-private serialization shape. A digest that cannot be recomputed from retained exact bytes is provenance metadata, not independently checkable evidence identity.

Required correction: publish one exact machine-readable `SIM-PARITY-CORPUS-v1` object or immutable exact byte artifact in the frozen remediation packet, define its canonicalization/domain separation completely, and show that recomputation yields the published digest. Human-readable summaries may remain, but must derive from or bind to that exact object.

### PG-SIM-M02 — MAJOR — 6/6 two-evaluator agreement and model-result digest are not reproducible from retained execution evidence

Issue #83 states that two independently structured Python 3.13.5 evaluators were executed and produced byte-identical normalized traces/final states, then publishes model-result digest `0c29eda2...`. The frozen packet contains neither evaluator source, exact executable fixture, exact normalized per-action traces, nor the exact normalized result object/bytes hashed to that digest.

The report provides only transition rules and final scenario summaries. Those summaries are sufficient to reason about the intended small model manually, but they are not the claimed execution evidence. In particular, a reviewer cannot independently verify that two implementations were actually distinct, that both emitted identical full traces including rejection reason codes and post-action states, or that the asserted result digest corresponds to those traces rather than to an unpublished producer-local object.

Required correction: retain exact evaluator source(s) or one deterministic executable validator plus exact fixture input, publish the complete normalized trace/result artifact, bind source/fixture/result identities, and require a fresh reviewer to reproduce the exact result digest and 6/6 agreement. The evaluator artifacts remain planning-experiment evidence and gain no production authority.

## 4. Fail-closed authority attacks — PASS

No evidence laundering was found in the core parity disposition.

- Every scenario row explicitly marks the representative shared kernel `NOT_RUN` and parity `INCONCLUSIVE`.
- The aggregate counts are `0 parity PASS / 0 parity FAIL / 6 parity INCONCLUSIVE`.
- The report explicitly states that absence of parity FAIL is not evidence of parity success.
- `representative_shared_kernel_identity` remains null; no engine or ordering fixture is substituted for a representative kernel.
- Upstream W2-ENG-03 remains `INCONCLUSIVE_ENVIRONMENT_BLOCKED`; lifecycle `REVIEW_READY` is explicitly distinguished from empirical satisfaction.
- Model agreement is typed only as `BOUNDED_MODEL_ONLY_PASS`; engine fitness/selection, production correctness, scheduler choice, readiness, release, and canonicalization remain `NOT_AUTHORIZED`.

Thus the material findings concern reconstructability of the positive model-side evidence, not a hidden upgrade of the absent shared-kernel side.

## 5. Reopen/rerun contract attack — PASS

The rerun contract correctly requires one exact representative shared-kernel candidate and executed toolchain envelope from a separately authorized upstream route before parity authority can strengthen. It also requires frozen-or-versioned corpus identity, full trajectories, retained divergence, explicit ordering semantics, and later W2-REV-01 adjudication.

The correction for PG-SIM-M01/M02 must preserve those fail-closed conditions and must not use a remediation episode to invent a representative kernel.

## 6. Severity and disposition

- BLOCKER: 0
- MAJOR: 2 (`PG-SIM-M01`, `PG-SIM-M02`)
- correction-requiring MINOR: 0

**Disposition: `CHANGES_NEEDED`.**

Issue #83 remains immutable provenance. Route exactly one bounded remediation successor that adds reconstructable corpus/execution evidence while preserving all six shared-kernel cells as `NOT_RUN` / `INCONCLUSIVE` unless separately authorized real kernel evidence actually exists.

Formal aggregate `W2-REV-01` remains required. This pre-gate review creates no engine-selection, production/readiness, implementation, integration, verification, release, merge, or canonicalization authority.
