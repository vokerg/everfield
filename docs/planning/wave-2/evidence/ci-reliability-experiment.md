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
predecessor_evidence_root: sha256 of canonical predecessor envelope chain
```

The evaluator independently reconstructs the predecessor envelope chain, recomputes its evidence root, verifies predecessor/successor identities, rejects same-candidate masquerade, and retains both the transition record and observed predecessor root in the result object.

A fresh root for `cand-flaky-v2` without the transition is therefore not sufficient evidence of valid remediation lineage.

### 2.3 ArtifactIdentityLineage

Every aggregate result now serializes the complete retained artifact record, not only events:

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

The executable v3 fixture was run against the exact contract above. Canonical JSON uses sorted keys and compact separators.

Fixture digest: `sha256:9b212a5f89b5ea3c4f2c63617dbadd0e202b8da7dcd1c531944d42e9725b27e8`  
Harness-contract digest: `sha256:fe185e57a52b16c4c14fea1ab7c34bfe2198ef835cb244c3ebed89ffcafecfa5`  
Canonical result-object digest: `sha256:f9ea7aafd662a2dbda75b12863f6e3298c3f20a8fd0b5ec1caea46965ec7a8a2`

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

The result object for S6 contains the exact replacement evidence records; S10 contains the exact transition record plus observed predecessor evidence root; S14-S17 contain complete artifact identity/hash/event records. The durable evidence needed to reconstruct authority is therefore inside the content-addressed result object rather than only in evaluator memory.

## 5. Finding dispositions

### PG-REM-CI-M01 — RESOLVED

Issue #91 validated only a replacement `artifact_key` while consulting global artifact state and then omitted replacement evidence from the aggregate result. V3 binds exact replacement evidence identity, candidate, requirement/policy, replacement ID, `artifact_id`, `expected_hash`, source envelope, result, and provenance. Exact records are retained in `replacement_evidence`.

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