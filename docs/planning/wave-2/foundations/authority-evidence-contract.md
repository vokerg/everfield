# W2-AUTH-01 — Authority, Evidence, and Readiness Compiler Contract

**Mission:** `W2-AUTH-01`  
**Task class:** `PLANNING_RESEARCH`  
**Decision state:** `CANONICAL_CANDIDATE`  
**Authority:** Proposal only; requires `W2-REV-01`.  
**Production implementation authorized:** **No.**

## 1. Scope and non-goals

This proposal closes the machine contract for the Wave 1 acceptance chain:

`TaskClaimContract -> EvidenceRequirement -> CheckPlan -> ExecutionEvidenceEnvelope -> EvidenceSatisfaction -> review/verification -> decision/readiness/integration eligibility`.

It also closes the supporting shapes `ActiveDirectiveSet`, `PolicyEpoch`, `ResourceCapabilityState`, `RiskFloor`, `ArtifactIdentity`, and `ImplementationReadinessLedger`.

Non-goals:

- replacing canonical Planning Program v1 schema-3 ownership/dispatch;
- choosing an engine, runtime, CI provider, evaluator, storage provider, or physical save format;
- converting planning experiments into production dependencies;
- treating directives, review prose, issue state, PR state, aggregate scores, or ledger edits as empirical PASS;
- upgrading `DEGRADED_SINGLE_AGENT` merely because the current master may continue leases.

## 2. Constraints, inputs, and authority boundaries

Observed canonical inputs:

- Planning Program v1 is the dispatcher/ownership authority and keeps gameplay/high-throughput implementation blocked.
- Wave 1 defines exactly one evidence acceptance chain and makes `EvidenceSatisfaction` derived rather than hand-authored truth.
- `ArtifactIdentity` is the durable retained-artifact identity.
- Directives may change policy/goals/ownership rules but cannot rewrite observed empirical results.
- The current lease-continuation directive changes ownership convenience, not independent-review capability.
- `IR-BLOCKER-EVIDENCE-FOUNDATION` remains OPEN and names W2-AUTH-01 plus downstream evidence/review/synthesis/readiness work in its resolution path.

Inference introduced by this proposal:

- the shared types need one closed compiler boundary and deterministic validation order so later Wave 2 experiments can emit interoperable evidence;
- readiness must compile from typed blocker predicates rather than be directly writable;
- trust insufficiency must remain distinguishable from empirical failure.

Recommendation:

- adopt the schemas, compiler algorithm, and validator fixtures below as the candidate contract for adversarial review.

## 3. Closed vocabulary

```yaml
EvidenceResult: [PASS, FAIL, FLAKY, INCONCLUSIVE, NOT_RUN, NOT_APPLICABLE]
SatisfactionState: [SATISFIED, UNSATISFIED, INCONCLUSIVE, NOT_APPLICABLE]
RequirementMode: [REQUIRED, CONDITIONAL]
TrustLevel: [FULL, DEGRADED]
DirectiveEffect:
  [GOAL, PRIORITY, CONSTRAINT, OWNERSHIP, RESOURCE_ASSUMPTION, POLICY_SUPERSESSION, SAFETY_STOP]
ReadinessState: [OPEN, RESOLVED, SUPERSEDED]
RiskClass: [R0, R1, R2, R3]
IdentityRef:
  algorithm_id: stable_id
  encoding_version: stable_id
  digest_hex: nonempty_hex
```

`FULL` is stricter than `DEGRADED`. `PASS` exists only as an execution/result observation inside an `ExecutionEvidenceEnvelope`; it has no acceptance authority until a conforming `EvidenceSatisfaction` is derived.

`IdentityRef` is deliberately algorithm-parameterized. This contract requires stable exact identity while leaving cross-runtime canonical encoding/hash authority to `W2-HASH-01`.

## 4. Supporting authority objects

### 4.1 `ActiveDirectiveSet`

```yaml
ActiveDirectiveSet:
  set_id: IdentityRef
  directives:
    - directive_id: stable_id
      source_ref: immutable_ref
      scope_refs: [stable_id]
      effect: DirectiveEffect
      payload_hash: IdentityRef
      supersedes: [directive_id]
      valid_from_policy_epoch: policy_epoch_id
      expires_or_recheck: null | predicate
```

Rules:

1. Source must be durable repository/GitHub authority.
2. A directive may affect compilation only through a new/current `PolicyEpoch`.
3. It cannot mutate an existing envelope result or directly emit `EvidenceSatisfaction`.
4. Safety-stop effects halt applicable execution immediately; resumption requires durable authority.

### 4.2 `PolicyEpoch`

```yaml
PolicyEpoch:
  policy_epoch_id: IdentityRef
  predecessor_epoch_id: null | IdentityRef
  active_directive_set_id: IdentityRef
  compiler_contract_version: stable_version
  effective_requirement_refs: [requirement_id]
  change_reason_refs: [immutable_ref]
```

Any requirement waiver/change creates a new epoch and new requirement identity. Historical evidence remains immutable.

### 4.3 `ResourceCapabilityState`

```yaml
ResourceCapabilityState:
  state_id: IdentityRef
  observed_at_ref: immutable_ref
  available_execution_contexts: integer_gte_1
  isolated_context_available: boolean
  independent_actor_or_permission_separation: [NONE, PARTIAL, FULL]
  protected_oracle_control_available: [NONE, PARTIAL, FULL]
  concurrency_capacity: integer_gte_1
  source_refs: [immutable_ref]
  valid_until_or_recheck: predicate
```

The current master lease-continuation directive belongs in `ActiveDirectiveSet`; it does **not** set `isolated_context_available=true`, change separation fields, or upgrade `TrustLevel`.

### 4.4 `RiskFloor`

```yaml
RiskFloor:
  risk_floor_id: IdentityRef
  scope_ref: stable_id
  risk_class: RiskClass
  minimum_trust: TrustLevel
  minimum_review_route: stable_route_id
  protected_evidence_required: boolean
  minimum_distinct_evidence_surfaces: integer_gte_1
  source_refs: [immutable_ref]
  downgrade_rule: NEW_POLICY_EPOCH_PLUS_REQUIRED_REVIEW
```

A producer/task author may request stricter handling but cannot lower the effective floor. Effective requirements use the strictest applicable floor under the current policy epoch.

## 5. Acceptance-chain machine shapes

### 5.1 `TaskClaimContract`

This object specifies what the task is allowed to claim, not whether the claim is true.

```yaml
TaskClaimContract:
  task_claim_contract_id: IdentityRef
  mission_id: stable_id
  policy_epoch_id: IdentityRef
  active_directive_set_id: IdentityRef
  resource_capability_state_id: IdentityRef
  claim_specs:
    - claim_id: stable_id
      claim_type: stable_type
      claim_scope_refs: [stable_id]
      evidence_requirement_id: IdentityRef
      risk_floor_id: IdentityRef
      readiness_effect_refs: [blocker_id]
  forbidden_claims: [stable_type]
  authoritative_input_refs: [immutable_ref]
  output_refs: [repo_path]
```

Validation fails if a claim lacks exactly one evidence requirement, if its risk floor is not applicable, or if a task claims authority forbidden by its class.

### 5.2 `EvidenceRequirement`

```yaml
EvidenceRequirement:
  requirement_id: IdentityRef
  policy_epoch_id: IdentityRef
  claim_id: stable_id
  mode: RequirementMode
  applicability_predicate: predicate
  required_evidence_kinds: [stable_type]
  required_execution_surfaces: [stable_type]
  minimum_trust: TrustLevel
  allowed_result_classes: [EvidenceResult]
  protected_level: [NORMAL, PROTECTED]
  substitution_rules:
    - from_kind: stable_type
      replacement_predicate: predicate
  quarantine_policy_ref: stable_id
  aggregation_rule:
    type: ALL | ANY | QUORUM | CUSTOM_VERSIONED
    parameter: null | scalar
  freshness_requirement_refs: [stable_id]
```

Rules:

- `NOT_APPLICABLE` is valid only when the applicability predicate deterministically evaluates false before execution.
- `NOT_RUN` means required work did not run and cannot satisfy a required claim.
- requirement identity includes policy epoch and all normative fields;
- replacing or weakening a requirement produces a new identity.

### 5.3 `CheckPlan`

```yaml
CheckPlan:
  check_plan_id: IdentityRef
  requirement_id: IdentityRef
  candidate_work_sha: sha40
  candidate_head_sha: sha40
  base_main_sha: sha40
  policy_epoch_id: IdentityRef
  applicability:
    state: APPLICABLE | NOT_APPLICABLE
    predicate_trace_hash: IdentityRef
  checks:
    - check_id: stable_id
      evidence_kind: stable_type
      execution_surface: stable_type
      required: boolean
      scenario_or_fixture_ref: immutable_ref
      evaluator_requirement_ref: null | stable_id
  compile_trace_hash: IdentityRef
```

The compiler may specialize execution details but may not delete, relax, or relabel a normative requirement. An applicable required check must appear exactly once unless a versioned aggregation rule explicitly requires multiplicity.

### 5.4 `ArtifactIdentity`

```yaml
ArtifactIdentity:
  artifact_id: IdentityRef
  content_hash: IdentityRef
  kind: stable_type
  storage_refs: [stable_ref]
  produced_by_ref: immutable_ref
  provenance_refs: [immutable_ref]
  rights_or_terms_state: CLEAR | RESTRICTED | QUARANTINED | UNKNOWN | NOT_APPLICABLE
  visibility: NORMAL | PROTECTED
  retention_class: stable_type
  access_policy_ref: null | stable_id
  supersedes: [IdentityRef]
  integrity_state: PRESENT | MISSING | CORRUPT
```

A content hash proves identity, not availability or authority. `MISSING`/`CORRUPT` required evidence reopens dependent satisfaction/readiness.

### 5.5 `ExecutionEvidenceEnvelope`

```yaml
ExecutionEvidenceEnvelope:
  envelope_id: IdentityRef
  requirement_id: IdentityRef
  check_plan_id: IdentityRef
  check_id: stable_id
  attempt_id: stable_id
  prior_attempt_id: null | stable_id
  candidate_work_sha: sha40
  candidate_head_sha: sha40
  base_main_sha: sha40
  policy_epoch_id: IdentityRef
  environment_fingerprint: IdentityRef
  toolchain_fingerprint: IdentityRef
  content_schema_package_ref: immutable_ref
  execution_surface: stable_type
  scenario_policy_action_seed_refs: [immutable_ref]
  evaluator_fingerprint_refs: [immutable_ref]
  result: EvidenceResult
  artifact_ids: [IdentityRef]
  trust_profile:
    level: TrustLevel
    capability_state_id: IdentityRef
    independence_mode: stable_type
  nondeterministic_surfaces: [stable_type]
  coverage_gaps: [stable_id]
  failure_class: null | PRODUCT | INFRA | ORACLE | HARNESS
```

Attempts are append-only. Retries link to prior attempts; a later PASS does not delete or relabel earlier failures.

### 5.6 `EvidenceSatisfaction` — sole empirical acceptance authority

```yaml
EvidenceSatisfaction:
  satisfaction_id: IdentityRef
  requirement_id: IdentityRef
  check_plan_id: IdentityRef
  candidate_work_sha: sha40
  base_main_sha: sha40
  policy_epoch_id: IdentityRef
  evaluated_envelope_ids: [IdentityRef]
  state: SatisfactionState
  reason_codes: [stable_code]
  trust_level_achieved: TrustLevel
  missing_check_ids: [stable_id]
  invalid_or_quarantined_artifact_ids: [IdentityRef]
  derivation_trace_hash: IdentityRef
```

Only the deterministic satisfaction compiler may create this object. No directive, task contract, review, issue/PR status, ledger entry, score, or envelope alone may create `SATISFIED`.

Deterministic derivation, in order:

1. Validate exact identity tuple: requirement, plan, candidate, base, policy epoch.
2. Re-evaluate applicability from the recorded predicate-trace inputs.
3. Reject unknown enums/fields, duplicate required checks without an explicit multiplicity rule, broken attempt lineage, or mismatched identities.
4. Verify every referenced `ArtifactIdentity`; required missing/corrupt/quarantined evidence is not acceptable unless an exact substitution rule passes.
5. Compute achieved trust from envelope trust profiles and current `ResourceCapabilityState`; never infer independence from actor labels or lease authority.
6. If requirement is not applicable, emit `NOT_APPLICABLE`.
7. If any applicable required check is absent or `NOT_RUN`, emit `INCONCLUSIVE`.
8. If any required result is `FAIL`, emit `UNSATISFIED` unless an exact replacement rule supersedes that check.
9. `FLAKY` or `INCONCLUSIVE` emits `INCONCLUSIVE` unless the requirement explicitly defines a valid aggregation/replacement rule.
10. If achieved trust is below the effective `RiskFloor`/requirement minimum, emit `INCONCLUSIVE` with `TRUST_FLOOR_UNMET`.
11. Emit `SATISFIED` only when every applicable normative requirement is met by allowed immutable evidence under the effective trust floor.

## 6. Review, verification, and decision boundary

Review/verification may:

- validate the compiler inputs and derivation;
- find missing, biased, or stale requirements;
- reject candidate reasoning or require a new policy/requirement version;
- determine whether a decision may advance given valid satisfaction objects.

They may not overwrite envelope results or directly turn unsatisfied/inconclusive empirical evidence into `SATISFIED`.

Therefore there is one empirical acceptance authority: derived `EvidenceSatisfaction`. Review/verification remain mandatory promotion authorities where the Planning Program or mission graph requires them.

## 7. Deterministic `ImplementationReadinessLedger`

```yaml
ImplementationReadinessLedger:
  ledger_id: IdentityRef
  policy_epoch_id: IdentityRef
  candidate_scope_ref: stable_id
  entries:
    - blocker_id: stable_id
      category: PRODUCT | TECHNICAL | FACTORY_TRUST | EVIDENCE | ACCESSIBILITY | RIGHTS | PLATFORM | OTHER
      scope: GLOBAL | DOMAIN | FEATURE_CLASS | PLATFORM | TOOLING
      blocks: [stable_scope]
      source_requirement_refs: [IdentityRef]
      resolution_predicate:
        all_satisfaction_refs: [IdentityRef]
        required_review_or_verification_refs: [immutable_ref]
      evidence_satisfaction_refs: [IdentityRef]
      state: ReadinessState
      supersedes: null | blocker_id
  compile_trace_hash: IdentityRef
```

Ledger rules:

1. Inputs are blocker definitions, current policy epoch, exact satisfaction objects, and explicitly required review/verification records.
2. `RESOLVED` is compiler output only when the resolution predicate passes exactly.
3. `OPEN` is the default for missing, stale, mismatched, inconclusive, or insufficient-trust prerequisites.
4. `SUPERSEDED` requires a traced new blocker/policy relation; deletion is not resolution.
5. Any OPEN entry whose `blocks` includes `PRODUCTION_IMPLEMENTATION` keeps that scope implementation-blocked.
6. A new policy epoch recompiles the ledger; it does not mutate historical ledger objects.
7. No scalar aggregate readiness score has authority.

For the current canonical inputs, `IR-BLOCKER-EVIDENCE-FOUNDATION` remains OPEN. This proposal does not satisfy the downstream experimental/review/readiness predicates and therefore cannot resolve it.

## 8. Compiler pipeline

```text
durable directives + capability evidence
  -> ActiveDirectiveSet + ResourceCapabilityState
  -> PolicyEpoch
  -> effective RiskFloor
  -> TaskClaimContract
  -> EvidenceRequirement
  -> CheckPlan(exact candidate/head/base)
  -> append-only ExecutionEvidenceEnvelope attempts
  -> ArtifactIdentity integrity/provenance validation
  -> EvidenceSatisfaction
  -> required review/verification
  -> decision transition + ImplementationReadinessLedger compilation
```

Fail closed on unknown type/field, unresolved identity, stale required external evidence, missing protected evidence, invalid policy transition, or ambiguous prerequisite. Compiler output is identity-bound and includes a derivation/compile trace identity.

## 9. Directive-versus-evidence cases

| Case | Required result |
|---|---|
| Owner says “continue existing leases” | Ownership compilation may continue; independence/trust unchanged. |
| Owner says “treat failed engine spike as PASS” | Invalid as empirical override; envelope remains FAIL and satisfaction cannot become SATISFIED. |
| Owner legitimately removes a requirement | New directive + PolicyEpoch + requirement identity; old evidence retained; new satisfaction compiled against new rule. |
| Emergency safety stop | Applicable execution/claim eligibility halts; no evidence result is rewritten. |
| Owner requests stricter review | New/effective RiskFloor may increase; existing low-trust satisfaction can become insufficient for the new decision without rewriting old evidence. |

## 10. Degraded-trust cases

`DEGRADED_SINGLE_AGENT` is represented as a trust profile bound to a `ResourceCapabilityState`. It is not equivalent to empirical failure.

- If effective minimum trust is `DEGRADED`, otherwise-valid evidence may derive `SATISFIED` with `trust_level_achieved=DEGRADED`; downstream review must preserve the trust debt.
- If effective minimum trust is `FULL`, the same empirical observations derive `INCONCLUSIVE/TRUST_FLOOR_UNMET`, not FAIL and not SATISFIED.
- The current lease-continuation directive cannot change either outcome.
- A later stronger capability state may support a new evidence/review episode; it does not retroactively relabel the degraded episode.

## 11. Validator fixtures

| ID | Fixture | Expected |
|---|---|---|
| V01 | Required applicable check has PASS envelope, intact artifact, sufficient trust | `SATISFIED` |
| V02 | Required applicable check is `NOT_RUN` | `INCONCLUSIVE/MISSING_REQUIRED_EXECUTION` |
| V03 | Applicability predicate false before execution | `NOT_APPLICABLE` |
| V04 | Required check has FAIL then retry PASS, requirement says ALL_ATTEMPTS_MUST_PASS | `UNSATISFIED` |
| V05 | FAIL then PASS, versioned rule explicitly accepts latest-after-infra-retry and first attempt classified INFRA | derive per rule; retain both attempts |
| V06 | PASS envelope candidate SHA differs from plan | invalid input; no satisfaction object |
| V07 | Required artifact hash matches but storage integrity is MISSING | `INCONCLUSIVE/REQUIRED_ARTIFACT_UNAVAILABLE` |
| V08 | Directive asks to override FAIL without policy/version change | reject directive effect on evidence; remain `UNSATISFIED` |
| V09 | Requirement changed under new PolicyEpoch | new requirement/plan/satisfaction identity; old object unchanged |
| V10 | DEGRADED evidence, effective minimum FULL | `INCONCLUSIVE/TRUST_FLOOR_UNMET` |
| V11 | DEGRADED evidence, effective minimum DEGRADED | may be `SATISFIED`; trust debt preserved |
| V12 | Ledger blocker has all evidence satisfied but mandatory review ref missing | blocker remains `OPEN` |
| V13 | Ledger blocker is manually edited to RESOLVED | invalid ledger; recompute to compiler result |
| V14 | Protected required artifact is QUARANTINED and no substitution passes | `INCONCLUSIVE` |
| V15 | Unknown EvidenceResult enum or extra authority field | invalid input; fail closed |
| V16 | Two claims point to different requirements for same claim ID in one TaskClaimContract | invalid contract; no CheckPlan compilation |

## 12. Observability and evaluation

Every compiler stage emits immutable identities and a trace identity. Minimum diagnostic surface:

- input object IDs and policy epoch;
- exact candidate/head/base;
- applicability decision;
- required/missing check IDs;
- all attempt IDs and failure classes;
- artifact integrity/quarantine state;
- achieved versus required trust;
- reason codes for satisfaction and ledger transitions.

Diagnostics for protected evidence may be bounded, but unavailability/corruption must remain visible as authority-relevant state.

## 13. Failure modes and risks

- **Policy laundering:** changing a requirement in place. Mitigation: new `PolicyEpoch` and requirement ID.
- **Retry laundering:** hiding failed attempts. Mitigation: append-only attempt lineage and aggregation rules.
- **Directive laundering:** treating project-owner authority as empirical truth. Mitigation: directives affect policy compilation, never envelope observations.
- **Trust laundering:** equating lease continuation, repeated model calls, or actor labels with independence. Mitigation: capability-bound trust derivation plus `RiskFloor`.
- **Artifact laundering:** hash exists but evidence is unavailable/quarantined. Mitigation: ArtifactIdentity integrity/rights state participates in satisfaction.
- **Readiness laundering:** manually resolving blockers or using a scalar score. Mitigation: compiled ledger and exact resolution predicates.
- **Compiler monoculture:** a buggy compiler could consistently mis-derive authority. Mitigation: W2-REV-01 adversarial review plus downstream validator fixtures/cross-implementation evidence where required.

## 14. Dependencies and interfaces

Primary consumers:

- `W2-ENG-03` consumes exact reviewed authority/evidence contracts to bind comparative engine-spike claims.
- `W2-SIM-01` consumes exact reviewed authority/evidence contracts to bound model/shared-kernel parity claims.
- `W2-REV-01` reviews this candidate with all other Wave 2 evidence roots.
- `W2-CI-01`, `W2-PROTECT-01`, `W2-EVAL-01`, and `W2-HASH-01` should emit evidence compatible with these identities without gaining authority to weaken them.

The canonical Planning Program remains the ownership/dispatch authority; this proposal does not replace schema 3.

## 15. Unresolved questions

1. Exact canonical serialization/hash algorithm for identity values remains owned by `W2-HASH-01`; until reviewed evidence exists, the schemas require stable exact identity but do not claim cross-runtime canonical hash authority.
2. Concrete protected-evidence storage/access mechanics remain owned by `W2-PROTECT-01`.
3. Concrete CI provider execution/retention mechanics remain owned by `W2-CI-01`.
4. Mutable evaluator fingerprint/calibration thresholds remain owned by `W2-EVAL-01`.
5. The final engine and target product/platform scope remain evidence-required elsewhere.

## 16. Reopen conditions

Reopen this contract if:

- two objects can independently create empirical PASS/SATISFIED authority;
- a directive can mutate an existing empirical result without a new policy/requirement identity;
- a producer can lower an applicable `RiskFloor`;
- a retry can erase prior failed evidence;
- required missing/quarantined evidence can still satisfy without an explicit substitution rule;
- lease continuation can be interpreted as an independence upgrade;
- readiness can become RESOLVED without exact satisfaction plus required review/verification predicates;
- W2-HASH-01 demonstrates that assumed stable identity fields need a different canonical encoding boundary;
- stronger multi-agent/isolation capability becomes available and degraded-trust rules can be tightened.

## 17. Review Index

Review these points first:

1. **Single acceptance authority:** Section 5.6 makes `EvidenceSatisfaction` the only object that can accept empirical evidence; directives, reviews, envelopes, task contracts, issue/PR state, scores, and ledger edits cannot mint `SATISFIED`.
2. **Compile direction:** Section 8 is one-way from durable directives/capability through policy, risk floor, claim/requirement/plan, immutable execution evidence, satisfaction, mandatory review/verification, then readiness.
3. **Directive boundary:** Sections 4.1–4.2 and 9 require policy/version changes rather than rewriting observations.
4. **Master lease directive:** Sections 4.3 and 10 explicitly preserve current lease continuation without upgrading isolation or independence.
5. **Risk floor:** Section 4.4 prevents producer-authored downgrade of trust/review requirements.
6. **Invalid cases:** V02, V06–V10, V12–V16 cover NOT_RUN, identity mismatch, unavailable/quarantined evidence, directive override, policy change, degraded trust, manual readiness edits, and unknown fields.
7. **Deterministic readiness:** Section 7 makes `RESOLVED` compiler-only and keeps current `IR-BLOCKER-EVIDENCE-FOUNDATION` OPEN.
8. **No production authorization:** This candidate is planning-only and cannot resolve the full readiness chain by itself.

Suggested adversarial attacks for `W2-REV-01`: construct a path that mints `SATISFIED` without the satisfaction compiler; lower a risk floor from a producer surface; reuse old evidence after a policy epoch change; launder a failed attempt through retry; resolve a blocker without mandatory review; or infer FULL independence from the lease directive.
