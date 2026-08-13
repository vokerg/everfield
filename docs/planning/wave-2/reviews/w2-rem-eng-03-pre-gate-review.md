# W2-PG-REM-ENG-03 — Independent pre-gate review of Issue #104

**Mission:** `W2-PG-REM-ENG-03` / Issue #110  
**Reviewed remediation:** `W2-REM-ENG-03` / Issue #104  
**Exact reviewed head/work:** `b406193c45c75f6309ea4123d02579d70ebe3591`  
**Harness blob:** `1fb26cb6afa02b7061d37f331cf5a132375ecfc4`  
**Validator blob:** `b7209361fa8c52f599d1e7393d28a2d19658887c`  
**Issue #103 review work/head:** `9fb365e2ad84c04d2e12305b38b40ddc30153530` / `00331d3cc9cbe29fa20f27be159b5730e3f3b142`  
**Disposition:** `CHANGES_NEEDED`  
**Authority:** noncanonical pre-gate evidence only; formal `W2-REV-01` remains required.

## 1. Review boundary and independence

This episode uses actor `w2-pg-rem-eng-03-agent-20260813-0732-01`, did not author or mutate Issue #104, and treats `planning/issue-104` as immutable input. The first substantive judgment came from fresh mechanical reproduction and adversarial mutations against the exact candidate bytes. No engine was executed, scored, ranked, or selected.

The review asks two separate questions: (1) whether the v3 candidate actually closes the Issue #103 attempt-identity findings without new fail-open behavior, and (2) whether Issue #104 has a policy-compliant downstream terminal binding under current repository instructions. Candidate semantics and lifecycle authority are intentionally separated.

## 2. Exact reproduction

The exact committed validator model reproduced all authored fixture classes: 15 equivalence cases, 17 aggregate cases, and 5 history cases. The five published semantic digests reproduced byte-for-byte at the semantic-object layer:

- validator contract: `357e25f9af9ac71804f322797c3ea1aa0c923167178b9c2eb8c84ef3280cbe23`
- feature slice: `9a2523c4870146b09233397f3773f7a27b1e0135c24a6767d16e34a791aab104`
- scenario manifest: `be4d7473b01da6b428cd5f3be48de083abd161a4899471303f3ccfeef45c725f`
- fixture inputs: `3172768f6288135c4b99dfd802882a5394b709b3fa0f74688bd17106a6b3c8ff`
- result object: `d79120f698bd9409bc6956162216a36a85f62592f4eff5db39b6fdc288149029`

Git identity independently fixes the validator source bytes at blob `b7209361fa8c52f599d1e7393d28a2d19658887c`. This episode did not separately recompute the report's raw-source SHA-256 `306285...` from a raw-file transport, so it makes no stronger claim about that auxiliary digest.

### Issue #103 finding closure

Fresh attacks confirm the intended corrections work:

| Attack | Fresh result | Judgment |
|---|---|---|
| retained required-injection PRODUCT FAIL plus duplicate PASS with same `injection_id` | `INCONCLUSIVE`, `valid_envelope=false` | `PG-REM-HARNESS-M01` closed |
| normal attempt with another `candidate_id` | `INCONCLUSIVE`, invalid envelope | `PG-REM-HARNESS-M02` closed |
| required-injection attempt with another `candidate_id` | `INCONCLUSIVE`, invalid envelope | `PG-REM-HARNESS-M02` closed |
| `PASS + PRODUCT` envelope | `INCONCLUSIVE`, invalid envelope | malformed-pair observation closed |

The prior S1–S10 anti-shrink, hidden-warm-state, resource, package, S3 authority, S10 hidden-context, retained-run, flake, and repair-lineage fixtures also reproduce their declared truth classes.

## 3. Findings

### PG-REM3-M01 — MAJOR — Attempt schema is not fail-closed for reset/workspace/index identity

The harness declares exact `reset_id`, exact `workspace_id`, boolean `reset_verified`, and an integer-or-null `normal_index`; it also says unverified/reused reset or workspace evidence becomes `NOT_RUN`. The executable validator does not close those shapes before aggregation.

Fresh counterexamples against the exact v3 semantics:

1. Starting from the clean S1 generation, set normal attempt N1 `reset_id=null` and `workspace_id=null` while leaving `reset_verified=true`; N2 retains its normal IDs. The aggregate still returns **`PASS_FOR_COMPARISON` with `valid_envelope=true`** because only set cardinality is checked.
2. Set one required normal attempt `normal_index=null`; sorting raises a Python `TypeError` instead of returning a typed fail-closed result.
3. Give both required normal attempts the same `normal_index`; the generation can still return **`PASS_FOR_COMPARISON`**.

This violates the packet's exact reset/workspace identity and fail-closed claims and can admit evidence whose independent-attempt ordering/identity is not mechanically established.

**Bounded correction:** validate a closed, kind-specific `AttemptRecord` before sorting or authority derivation. Required NORMAL attempts need positive unique normal indices, nonempty exact reset/workspace identities, and an actual boolean `reset_verified`; malformed/null/wrong-type values must return an invalid typed envelope rather than raise. Add executable negatives for null/empty reset and workspace IDs, wrong-type reset flags, null/non-integer/duplicate normal indices, and ordering ambiguity.

### PG-REM3-M02 — MAJOR — Adaptation candidate identity is declared but not validated

`AdaptationManifest` declares `candidate_id: <exact>` and the W2-ENG-03 packet requires one adaptation per candidate/scenario plus exact candidate identity. Yet `validate(adaptation)` never inspects `candidate_id`.

Fresh counterexamples:

- replace the clean adaptation's `candidate_id` with `OTHER-CANDIDATE` -> **`ACCEPT`**;
- remove `candidate_id` entirely -> **`ACCEPT`**.

Attempt-level candidate binding therefore closes the Issue #103 substitution path only after attempts exist; it does not prove that the adaptation admitted for execution belongs to the candidate that later consumes it. A validator `ACCEPT` can be reused or relabeled across candidate identities without detection.

**Bounded correction:** require a nonempty exact candidate identity in the adaptation validator and bind the accepted adaptation identity to the later generation `(candidate_id, scenario_id, harness_id, feature_slice_id, scenario/adaptation identity)`. Candidate transition/rebinding must require an explicit typed protocol, never implicit relabeling. Add wrong/missing candidate and cross-candidate adaptation-reuse negatives.

### PG-REM3-m01 — MINOR — History validity is ambiguous when a generation envelope is invalid

`history()` records each generation's `valid_envelope`, but its top-level `valid` flag checks only lineage. A linked history containing a generation that aggregates with `valid_envelope=false` can still return top-level `valid=true`.

This is not evidence that the invalid generation can become `PASS_FOR_COMPARISON`; its aggregate remains non-authoritative. However, the overloaded `valid` field can be misread downstream as full evidence validity.

**Bounded correction:** either rename/scope the top-level flag to `lineage_valid`, or make full history validity false when any generation envelope is invalid. Add a fixture that distinguishes lineage validity from evidence-envelope validity.

### PG-REM3-B01 — BLOCKER (lifecycle authority, not candidate semantics) — Issue #104 lacks required draft-PR visibility

Current `main@042d140b5d2e0b951da4528e1867514983418d6f` added the repository instruction that an open draft PR from the exact task branch to `main` must exist **before** terminal `STATUS(REVIEW_READY)`, with PR head equal to terminal `head_sha`.

Issue #104 published `STATUS(REVIEW_READY)` comment `5276247931` at head `b406193c45c75f6309ea4123d02579d70ebe3591` after that directive became current, but a live query found no open PR from `planning/issue-104` to `main`. Therefore that comment must not be used as a current policy-compliant downstream terminal binding.

This finding does **not** invalidate the immutable candidate bytes or authorize Issue #110 to recover/mutate Issue #104. Repair belongs to valid Issue #104 continuation/recovery under its ownership rules, with the draft PR created and verified before a replacement terminal status.

## 4. Disposition

**`CHANGES_NEEDED` — 1 lifecycle BLOCKER / 2 substantive MAJOR / 1 MINOR.**

The exact v3 candidate does close the two Issue #103 MAJOR findings and the malformed result/failure-class observation. It is nevertheless not clean for W2-ENG-03/W2-REV-01 consumption because fresh attacks expose two additional machine-contract gaps, and its existing terminal record fails the current review-visibility invariant.

One bounded remediation successor should correct `PG-REM3-M01`, `PG-REM3-M02`, and clarify `PG-REM3-m01`; its own lifecycle must satisfy the draft-PR-before-terminal rule. The frozen Issue #104 candidate remains immutable provenance. W2-ENG-03 must not execute/score/select engines from this chain until a valid corrected substantive terminal is available.

No production implementation/readiness, release/platform certification, integration, verification, or canonicalization authority is created by this review.