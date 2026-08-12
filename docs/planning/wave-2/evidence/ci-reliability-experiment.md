# W2-REM-CI-02 — Durable CheckPlan / CI evidence identity remediation

**Source producer:** `W2-CI-01` / Issue #77 @ `0011a9b02f1c7d8d20b81e0fb4faa6dec9bcae59`  
**First remediation:** `W2-REM-CI-01` / Issue #91 @ `0a256ae79880c759bcd698160adaaf3b302426d1`  
**Independent pre-gate review:** `W2-PG-REM-CI-01` / Issue #97 @ `091221bf92699910a01775b4368a7618106f5e14`  
**Review artifact:** `533d4192fecf3e550e57ca630fcea79b9ae17326`  
**Current remediation:** `W2-REM-CI-02` / Issue #99  
**Base main:** `c7ba185ed9667b717794c19eaa0834ca41aa4c78`  
**Authority:** bounded noncanonical planning evidence only; formal aggregate review remains `W2-REV-01`.

## 1. Scope

Issue #97 found three MAJOR defects at durable evidence boundaries in Issue #91:

1. replacement evidence did not itself bind exact `ArtifactIdentity` and was not reconstructable from the published result;
2. successor candidate admission did not validate predecessor evidence lineage;
3. retained-artifact result serialization omitted stable artifact identity and authoritative hash.

This remediation replaces the affected evidence contract with `ci-reliability-reference-v3`. It preserves the already-correct `NOT_RUN`/`NOT_APPLICABLE`, PRODUCT/INFRA/FLAKY retry, exact replacement-set, quarantine-expiry, same-candidate reset rejection, and provider-independent authority semantics.

Non-goals remain: no CI provider, universal INFRA classifier, production CI architecture, engine decision, implementation readiness, integration authority, or canonicalization is selected or authorized.

## 2. Exact v3 identity contracts

### 2.1 ReplacementEvidenceRecord

Every quarantine replacement record now binds all of:

```yaml
replacement_evidence_id: immutable evidence-record identity
replacement_id: exact policy replacement identity
candidate_id: exact candidate
requirement_id: exact quarantine requirement
policy_version: exact quarantine policy version
result: PASS|FAIL|FLAKY|INCONCLUSIVE|NOT_RUN
artifact_key: exact fixture/policy key
artifact_id: exact stable ArtifactIdentity
expected_hash: authoritative content identity
source_envelope_id: exact execution envelope provenance
provenance: retained evidence provenance identity
```

Validation checks the record against both the quarantine policy and the exact artifact-state record. The aggregate result retains the submitted `replacement_evidence` records verbatim. A correct replacement ID with omitted or wrong `artifact_id` cannot satisfy.

### 2.2 CandidateTransitionRecord

A claimed remediation successor is admissible only with an explicit transition record:

```yaml
transition_id: transition-flaky-v1-to-v2
predecessor_candidate_id: cand-flaky-v1
successor_candidate_id: cand-flaky-v2
changed_work_identity: work:remediate-soak-flake:v1
reason: bounded remediation after retained flaky evidence
predecessor_evidence_root: ef6222dbbfd53b2417a1087151c9743bdcff238fb3d72620f3871b264eb31442
```

The evaluator reconstructs the predecessor envelope chain, recomputes its evidence root, verifies predecessor/successor identities, rejects same-candidate masquerade, and retains both the transition record and observed predecessor root in the result object.

A fresh root for `cand-flaky-v2` without the transition is therefore not sufficient evidence of valid remediation lineage.

### 2.3 ArtifactIdentityLineage

Every aggregate result serializes the complete retained artifact record, not only events:

```yaml
artifact_identity_lineage:
  <artifact-key>:
    artifact_id: stable identity
    expected_hash: authoritative content identity
    events:
      - event_id: ...
        state: REACHABLE|UNREACHABLE
        observed_hash: ...
```

Consumption validates `artifact_id` and `expected_hash` against the exact artifact catalog before considering reachability. Replaying the same event list under a different artifact identity or authoritative hash is `INCONCLUSIVE`.

## 3. Preserved evidence algebra

The v3 evaluator retains these rules from Issue #91:

- `CONDITIONALLY_REQUIRED` compiles to `REQUIRED` or `NOT_APPLICABLE` before result gating;
- a required `NOT_RUN` remains unsatisfied;
- PRODUCT failure cannot be laundered by a later PASS for the same candidate;
- explicit FLAKY remains gating;
- INFRA retry may satisfy only when the requirement explicitly permits it, all failed attempts are INFRA-classified, and the terminal attempt is PASS;
- quarantine authority requires exact replacement-set equality and expires at the policy boundary;
- a same-candidate second root envelope is rejected as reset/fork;
- artifact unavailability or identity/hash mismatch reopens authority;
- provider mechanics and classification authority remain outside this synthetic fixture.

## 4. Executed v3 fixture

The v3 evaluator was executed against the exact published fixture/result manifests in Appendix A. Canonical digests use JSON with sorted keys and compact separators.

Published fixture-manifest digest: `sha256:8068cbc8563faf1c91c983b85baaa25be443236da3cd3980c1c27952d90c14ae`  
Harness-contract digest: `sha256:fe185e57a52b16c4c14fea1ab7c34bfe2198ef835cb244c3ebed89ffcafecfa5`  
Published result-object digest: `sha256:dd171542b1b00b94f8e679cd40e575a0b826df410b0d82216b497f5794da07e6`

| ID | Attack / condition | Aggregate | Required property |
|---|---|---|---|
| S1 | baseline | `SATISFIED` | exact required evidence passes |
| S2 | conditional package required but not run | `UNSATISFIED` | `NOT_RUN` is not `NOT_APPLICABLE` |
| S3 | PRODUCT FAIL then PASS | `UNSATISFIED` | product failure retained |
| S4 | permitted INFRA failures then PASS | `SATISFIED` | bounded retry semantics preserved |
| S5 | FLAKY then PASS | `UNSATISFIED` | flake retained |
| S6 | exact active replacement records | `SATISFIED` | fully bound replacement evidence accepted |
| S7 | replacement omits `artifact_id` | `INCONCLUSIVE` | PG-REM-CI-M01 negative fixture |
| S8 | replacement uses wrong `artifact_id` | `INCONCLUSIVE` | PG-REM-CI-M01 negative fixture |
| S9 | same candidate starts second root | `INCONCLUSIVE` | reset/fork rejected |
| S10 | valid successor + exact predecessor transition/root | `SATISFIED` | PG-REM-CI-M02 positive fixture |
| S11 | successor missing transition | `INCONCLUSIVE` | missing lineage rejected |
| S12 | successor names wrong predecessor | `INCONCLUSIVE` | wrong lineage rejected |
| S13 | same candidate masquerades as predecessor/successor | `INCONCLUSIVE` | identity laundering rejected |
| S14 | retained required artifact unavailable | `INCONCLUSIVE` | retention loss reopens authority |
| S15 | same artifact restored at exact hash | `SATISFIED` | exact restoration accepted |
| S16 | same event list replayed under different artifact ID | `INCONCLUSIVE` | PG-REM-CI-M03 identity substitution rejected |
| S17 | same event list replayed under different expected hash | `INCONCLUSIVE` | authoritative hash substitution rejected |

Appendix A publishes the exact durable data needed for later reconstruction: S6 replacement evidence, S10 transition plus observed predecessor root, and S14-S17 complete stable artifact identity/hash/event records.

## 5. Finding dispositions

### PG-REM-CI-M01 — RESOLVED

Issue #91 validated only a replacement `artifact_key` while consulting global artifact state and then omitted replacement evidence from the aggregate result. V3 binds exact replacement evidence identity, candidate, requirement/policy, replacement ID, `artifact_id`, `expected_hash`, source envelope, result, and provenance. Exact records are retained in the published result object.

S7 and S8 prove omitted/wrong ArtifactIdentity cannot satisfy even when replacement IDs are otherwise correct.

### PG-REM-CI-M02 — RESOLVED

Issue #91 carried `supersedes` only as descriptive candidate metadata. V3 requires a validated `CandidateTransitionRecord`, exact predecessor envelope chain, and recomputed predecessor evidence root before `cand-flaky-v2` may satisfy as a remediation successor.

S10 is the positive transition case. S11-S13 reject missing transition, wrong predecessor, and same-candidate masquerade.

### PG-REM-CI-M03 — RESOLVED

Issue #91 serialized only availability events. V3 serializes and validates `artifact_id`, `expected_hash`, and ordered events for every artifact in `artifact_identity_lineage`.

S16-S17 replay identical event history under substituted identity/hash and fail closed, while S15 restores authority only for the exact original identity/hash.

## 6. Evidence versus inference

Direct evidence from the v3 fixture supports only the closed synthetic semantics above. It does not prove real provider enforcement, correct INFRA classification, replacement semantic adequacy, or production retention durability.

Recommended descendants should retain the same exact identity boundaries while separately evidencing classification authority, provider storage semantics, replacement adequacy, expiry atomicity, and consumption-time integrity.

## 7. Failure modes and residual risks

- A weak external INFRA classifier can still misclassify product failures; this fixture deliberately does not solve that authority problem.
- Exact replacement identity does not prove semantic equivalence to the quarantined check; equivalence remains a review obligation.
- A real backend can violate append-only lineage despite this contract unless storage/enforcement is separately tested.
- Provider/account/policy drift may invalidate a result even when synthetic semantics are correct.
- Evidence roots prove exact supplied predecessor records, not that all real-world predecessor evidence was retained unless acquisition/storage completeness is independently enforced.

## 8. Reopen conditions

Reopen if any descendant can:

- SATISFY quarantine with missing/wrong replacement ArtifactIdentity or without reconstructable replacement evidence;
- SATISFY a claimed successor without exact predecessor transition/evidence-root validation;
- substitute a same candidate as a successor;
- reconstruct retention authority from events while changing stable artifact identity or authoritative hash;
- erase required `NOT_RUN`, PRODUCT failure, explicit FLAKY, or same-candidate reset evidence;
- silently grant provider, readiness, integration, or canonical authority from this fixture.

## 9. Downstream and authority boundary

This v3 payload supersedes Issue #91 as the substantive corrected CI remediation input once Issue #99 freezes at exact `STATUS(REVIEW_READY)`. Issues #77, #91, and #97 remain immutable provenance.

Formal aggregate independent adversarial review remains `W2-REV-01`. This remediation creates no implementation-readiness, integration, production-CI, or canonicalization authority.

## Appendix A — exact published fixture/result manifests

The following objects are the published durable manifests whose canonical compact-JSON digests are recorded in §4.

### A.1 Fixture manifest

```json
{
  "artifact_catalog": {
    "package-pass": {"artifact_id": "art-package-pass-v3", "content_hash": "dc9f6e4b62400949d12a88714711ce5cd0c654d768b825fd8151014c310cd40a"},
    "short-soak": {"artifact_id": "art-short-soak-v3", "content_hash": "6868f5813a37470673ab4fa5bc2dfa2de912092b9d02360866627585edb1dfcb"},
    "soak-pass": {"artifact_id": "art-soak-pass-v3", "content_hash": "db3d050bfe46b76e8df9b877cbbb21112a9f704e817d9076b6ccf070f8a73452"},
    "static-invariant": {"artifact_id": "art-static-invariant-v3", "content_hash": "7c47b7ba6d4c0afbf459d890eb6b1435feb095a15815a10f82ea7c3a30d08423"},
    "unit-pass": {"artifact_id": "art-unit-pass-v3", "content_hash": "9f13dde3b3dd154a952368dfefa81a2813eca62b49ed97a0a65aaa48085ef2a1"}
  },
  "base_sha": "c7ba185ed9667b717794c19eaa0834ca41aa4c78",
  "candidate_ids": {"flaky": "cand-flaky-v1", "good": "cand-good-v1", "infra": "cand-infra-retry-v1", "product": "cand-product-fail-v1", "remediated": "cand-flaky-v2"},
  "normal_policy": "ci-reliability-exp-v3",
  "quarantine_policy": {"candidate_id": "cand-flaky-v1", "check_id": "soak", "expiry_day": 14, "policy_version": "ci-reliability-exp-v3-q1", "replacement_ids": ["short_soak", "static_invariant"], "requirement_id": "CI-EXP-REQ-v3-q1"},
  "requirement_id": "CI-EXP-REQ-v3",
  "transition": {"changed_work_identity": "work:remediate-soak-flake:v1", "predecessor_candidate_id": "cand-flaky-v1", "predecessor_evidence_root": "ef6222dbbfd53b2417a1087151c9743bdcff238fb3d72620f3871b264eb31442", "reason": "bounded remediation after retained flaky evidence", "successor_candidate_id": "cand-flaky-v2", "transition_id": "transition-flaky-v1-to-v2"}
}
```

### A.2 Harness contract

```json
{"aggregate_semantics":"required-gate-three-state-v1","artifact_lineage_semantics":"stable-artifact-identity-event-lineage-v2","candidate_chain_semantics":"append-only-exact-candidate-v1","candidate_transition_semantics":"validated-predecessor-evidence-root-v1","harness_version":"ci-reliability-reference-v3","quarantine_semantics":"exact-versioned-replacement-evidence-artifact-v2"}
```

### A.3 Published result object

```json
{
  "schema": "ci-reliability-results-v3",
  "scenario_aggregates": {
    "S1_baseline": "SATISFIED", "S2_conditional_not_run": "UNSATISFIED", "S3_product_fail_retry": "UNSATISFIED", "S4_infra_retry": "SATISFIED", "S5_flaky": "UNSATISFIED", "S6_quarantine_active_valid": "SATISFIED", "S7_replacement_omitted_artifact_id": "INCONCLUSIVE", "S8_replacement_wrong_artifact_id": "INCONCLUSIVE", "S9_same_candidate_reset": "INCONCLUSIVE", "S10_successor_valid": "SATISFIED", "S11_successor_missing_transition": "INCONCLUSIVE", "S12_successor_wrong_predecessor": "INCONCLUSIVE", "S13_successor_same_candidate_masquerade": "INCONCLUSIVE", "S14_retention_loss": "INCONCLUSIVE", "S15_exact_restore": "SATISFIED", "S16_identity_swap_same_events": "INCONCLUSIVE", "S17_expected_hash_swap_same_events": "INCONCLUSIVE"
  },
  "S6_replacement_evidence": {
    "short_soak": {"artifact_id": "art-short-soak-v3", "artifact_key": "short-soak", "candidate_id": "cand-flaky-v1", "expected_hash": "6868f5813a37470673ab4fa5bc2dfa2de912092b9d02360866627585edb1dfcb", "policy_version": "ci-reliability-exp-v3-q1", "provenance": "synthetic-fixture-v3", "replacement_evidence_id": "repl-ev-short_soak", "replacement_id": "short_soak", "requirement_id": "CI-EXP-REQ-v3-q1", "result": "PASS", "source_envelope_id": "env-flaky-1"},
    "static_invariant": {"artifact_id": "art-static-invariant-v3", "artifact_key": "static-invariant", "candidate_id": "cand-flaky-v1", "expected_hash": "7c47b7ba6d4c0afbf459d890eb6b1435feb095a15815a10f82ea7c3a30d08423", "policy_version": "ci-reliability-exp-v3-q1", "provenance": "synthetic-fixture-v3", "replacement_evidence_id": "repl-ev-static_invariant", "replacement_id": "static_invariant", "requirement_id": "CI-EXP-REQ-v3-q1", "result": "PASS", "source_envelope_id": "env-flaky-1"}
  },
  "S10_candidate_transition": {"changed_work_identity": "work:remediate-soak-flake:v1", "predecessor_candidate_id": "cand-flaky-v1", "predecessor_evidence_root": "ef6222dbbfd53b2417a1087151c9743bdcff238fb3d72620f3871b264eb31442", "reason": "bounded remediation after retained flaky evidence", "successor_candidate_id": "cand-flaky-v2", "transition_id": "transition-flaky-v1-to-v2"},
  "S10_predecessor_evidence_root_observed": "ef6222dbbfd53b2417a1087151c9743bdcff238fb3d72620f3871b264eb31442",
  "S14_unit_artifact_identity_lineage": {"artifact_id": "art-unit-pass-v3", "expected_hash": "9f13dde3b3dd154a952368dfefa81a2813eca62b49ed97a0a65aaa48085ef2a1", "events": [{"event_id":"unit-pass-e0","state":"REACHABLE","observed_hash":"9f13dde3b3dd154a952368dfefa81a2813eca62b49ed97a0a65aaa48085ef2a1"},{"event_id":"unit-e1-loss","state":"UNREACHABLE","observed_hash":null}]},
  "S15_unit_artifact_identity_lineage": {"artifact_id": "art-unit-pass-v3", "expected_hash": "9f13dde3b3dd154a952368dfefa81a2813eca62b49ed97a0a65aaa48085ef2a1", "events": [{"event_id":"unit-pass-e0","state":"REACHABLE","observed_hash":"9f13dde3b3dd154a952368dfefa81a2813eca62b49ed97a0a65aaa48085ef2a1"},{"event_id":"unit-e1-loss","state":"UNREACHABLE","observed_hash":null},{"event_id":"unit-e2-restore","state":"REACHABLE","observed_hash":"9f13dde3b3dd154a952368dfefa81a2813eca62b49ed97a0a65aaa48085ef2a1"}]},
  "S16_unit_artifact_identity_lineage": {"artifact_id": "art-swapped", "expected_hash": "9f13dde3b3dd154a952368dfefa81a2813eca62b49ed97a0a65aaa48085ef2a1", "events": [{"event_id":"unit-pass-e0","state":"REACHABLE","observed_hash":"9f13dde3b3dd154a952368dfefa81a2813eca62b49ed97a0a65aaa48085ef2a1"},{"event_id":"unit-e1-loss","state":"UNREACHABLE","observed_hash":null},{"event_id":"unit-e2-restore","state":"REACHABLE","observed_hash":"9f13dde3b3dd154a952368dfefa81a2813eca62b49ed97a0a65aaa48085ef2a1"}]},
  "S17_unit_artifact_identity_lineage": {"artifact_id": "art-unit-pass-v3", "expected_hash": "11d31bcde2b39adf074772ffd52f6431dbef826c3866190be73638d0964b07d1", "events": [{"event_id":"unit-pass-e0","state":"REACHABLE","observed_hash":"9f13dde3b3dd154a952368dfefa81a2813eca62b49ed97a0a65aaa48085ef2a1"},{"event_id":"unit-e1-loss","state":"UNREACHABLE","observed_hash":null},{"event_id":"unit-e2-restore","state":"REACHABLE","observed_hash":"9f13dde3b3dd154a952368dfefa81a2813eca62b49ed97a0a65aaa48085ef2a1"}]}
}
```
