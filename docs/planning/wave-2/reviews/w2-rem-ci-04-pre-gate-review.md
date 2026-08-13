# W2-PG-REM-CI-04 — Independent pre-gate review of replacement-evidence provenance remediation

**Mission:** `W2-PG-REM-CI-04` / Issue #115  
**Reviewed issue:** #107 / `W2-REM-CI-04`  
**Reviewed work/head:** `c22bfedf02ca0b79716e4783d77d114c75655bd9`  
**Reviewed validator blob:** `b951064b701045763f72bcd5247cac45329d1fe5`  
**Reviewed report blob:** `38697b9cc93e98cdd39c28061fbb08fc465163e1`  
**Reviewed disposition blob:** `fe8e54118aa6750a707c322c41601c8588215ad9`  
**Reviewed handoff blob:** `4f8469eec6b5c1c53d5aa76ba12aeed4aedba222`  
**Authority:** independent noncanonical pre-gate evidence only; formal aggregate review remains `W2-REV-01`.

## Disposition

`CLEAN_FOR_W2_REVIEW_INPUT`

Independent review found **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR** in the bounded Issue #115 scope. The exact frozen v5 packet mechanically closes `PG-REM-CI3-M01` and preserves the reviewed v4 authority boundaries.

## Attack plan and evidence

The review consumed only the immutable Issue #107 packet plus canonical authority invariants. The validator source was inspected from exact Git blob `b951064b701045763f72bcd5247cac45329d1fe5`; the producer report was not treated as an oracle.

### 1. Replacement-evidence identity

`replacement_ok()` requires the record's `replacement_evidence_id` to equal the frozen expected ID for the keyed replacement. `quarantine()` also rejects duplicate evidence IDs before evaluating individual records. Therefore substitution and duplication cannot preserve `SATISFIED`.

The S27/S28 corpus cases exercise both paths and expect `INCONCLUSIVE`.

### 2. Source-envelope identity and exact bytes

The accepted record must name the frozen expected `source_envelope_id`; duplicate source-envelope IDs are rejected by `quarantine()`. The complete supplied envelope map must canonical-hash to the frozen envelope-set digest before any record can satisfy. `replacement_ok()` then requires the referenced envelope to exist, match its frozen per-envelope digest, match the record's declared digest, and equal the frozen envelope bytes exactly.

Independent canonical-JSON SHA-256 recomputation from the exact embedded structures reproduced:

- `repl-env-short-soak-v1`: `sha256:36ea19895b16624e8b821b7463f82879e094e29912d89d1c541523c2f510377c`;
- `repl-env-static-invariant-v1`: `sha256:1520beba77c89b44dbe01ecd20c4a2ddb1a046ce22df2e47f2495b197483fa0a`;
- complete replacement-envelope set: `sha256:2ac80d5dd1f8e08de84d9409b37c20d99d2251420dc81c50b9ffbfbd4692b9d5`.

The S29/S30/S34 cases cover dangling, wrong, and duplicated envelope identity; all derive `INCONCLUSIVE`.

### 3. Record/envelope agreement and provenance

For every accepted replacement, the validator requires equality between record and exact envelope for `replacement_evidence_id`, candidate, requirement, policy version, replacement/check identity, result, artifact key, `artifact_id`, authoritative hash, and structured provenance. The artifact identity/hash must also match the frozen artifact catalog.

S31 substitutes provenance, S32 mutates the source-envelope result, and S33 mutates source-envelope `artifact_id`; the exact envelope-set hash and record/envelope equality rules force all three to `INCONCLUSIVE`.

### 4. Reconstructability

The emitted result retains the positive replacement records, exact replacement execution envelopes, per-envelope digests, and envelope-set digest. A later reviewer therefore has the complete evidence objects rather than only dangling IDs or producer prose.

### 5. Preserved v4 semantics

Static inspection of the exact validator confirms S1-S26 remain in the corpus and preserve the declared attempt/applicability, PRODUCT/INFRA/FLAKY retry, quarantine-expiry and exact replacement-set, same-candidate reset, predecessor transition/evidence-root, and retained-artifact identity/hash paths.

Independent canonical reconstruction of the embedded predecessor evidence reproduced both the artifact digest and root as `sha256:46f6e1dfd6b56eb2d62c689e0c20de7021ff51123002655550834abd04d8107d`, matching the frozen packet.

The source-identity guard is fail-closed: `bundle()` recomputes a normalized source digest and exits before fixture evaluation when it differs from the declared `VALIDATOR_SOURCE_DIGEST`.

## Finding disposition

`PG-REM-CI3-M01` — **CLOSED by exact reviewed bytes**.

The v5 acceptance path no longer treats replacement evidence identity, source-envelope identity, or provenance as presence-only metadata. Exact value, uniqueness, immutable source bytes/digests, artifact identity/hash, and record/envelope agreement are all mechanically enforced.

No new finding is raised.

## Limits and reopen conditions

This review does not select a CI provider, define a universal INFRA classifier, establish production durability, authorize implementation/gameplay work, establish implementation readiness, authorize integration, perform formal verification, or canonicalize any artifact.

Reopen if a descendant can retain `SATISFIED` while substituting/duplicating replacement evidence identity; using dangling/wrong/duplicated/mutated source envelopes; changing candidate/policy/check/result/artifact identity/hash/provenance without invalidation; changing validator semantics without changing the bound source identity; or regressing any preserved S1-S26 truth class.

## Review result

**CLEAN_FOR_W2_REVIEW_INPUT** — exact Issue #107 packet is suitable as noncanonical input to later formal `W2-REV-01`. Frozen Issue #107 remains immutable and is not re-owned or modified by this review.
