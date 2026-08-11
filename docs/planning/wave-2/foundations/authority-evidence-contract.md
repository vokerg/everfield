# W2-AUTH-01 — Authority, Evidence, and Readiness Compiler Contract (Remediated Candidate)

**Mission source:** `W2-AUTH-01`  
**Remediation mission:** `W2-REM-AUTH-01` / Issue #87  
**Source candidate work:** `4f2baf8f97a531ac38491343098ac10c81c12a6b`  
**Source self-review:** Issue #69 comment `5251524689`  
**Task class:** `PLANNING_REVISION`  
**Decision state:** `CANONICAL_CANDIDATE`  
**Authority:** Proposal only; requires `W2-REV-01`.  
**Production implementation authorized:** **No.**

## 1. Scope and non-goals

This candidate closes the Wave 1 acceptance chain:

`TaskClaimContract -> EvidenceRequirement -> CheckPlan -> ExecutionEvidenceEnvelope -> EvidenceSatisfaction -> review/verification -> decision/readiness/integration eligibility`.

Supporting authority shapes are `ActiveDirectiveSet`, `PolicyEpoch`, `ResourceCapabilityState`, `RiskFloor`, `EffectiveRiskConstraint`, `ArtifactIdentity`, `ReviewRouteRegistry`, and `ImplementationReadinessLedger`.

Non-goals:

- replacing canonical Planning Program v1 ownership/dispatch;
- choosing an engine, runtime, CI provider, evaluator, storage provider, serialization/hash algorithm, or physical save format;
- converting planning experiments into production dependencies;
- treating directives, review prose, issue/PR state, aggregate scores, or ledger edits as empirical PASS;
- upgrading `DEGRADED_SINGLE_AGENT` merely because the current master may continue leases.

## 2. Authority boundaries and source distinctions

Observed canonical inputs:

- Planning Program v1 remains dispatch/ownership authority and keeps high-throughput implementation blocked.
- Wave 1 defines one evidence acceptance chain and makes `EvidenceSatisfaction` derived rather than hand-authored truth.
- `ArtifactIdentity` is the durable retained-artifact identity.
- Directives may change policy/goals/ownership assumptions but cannot rewrite observed empirical results.
- Lease continuation changes ownership convenience, not independent-review capability.
- `IR-BLOCKER-EVIDENCE-FOUNDATION` remains OPEN.

Inference introduced here:

- later Wave 2 evidence requires one closed contract-layer type system and deterministic predicate semantics;
- retry selection must be distinct from cross-check evidence aggregation;
- every `RiskFloor` dimension must compile into an immutable effective constraint and survive to promotion/readiness;
- trust insufficiency must remain distinguishable from empirical failure and from absence of evaluable evidence.

Recommendation: adopt these shapes and fixtures as the remediated candidate for `W2-REV-01`.

## 3. Closed contract-layer type system

All objects below are **closed schemas**: unknown fields are invalid unless a field explicitly names a registered extension point. Every field resolves to a primitive below, a closed enum, another structured type in this document, `IdentityRef`, or `VersionedRuleRef`.

### 3.1 Primitive registry v1

```yaml
PrimitiveRegistryV1:
  bool: exactly true | false
  uint: integer >= 0
  positive_uint: integer >= 1
  stable_id: UTF-8 string matching ^[A-Za-z0-9][A-Za-z0-9._:/-]{0,255}$
  stable_type: stable_id
  stable_code: stable_id
  stable_version: stable_id
  sha40: lowercase-or-uppercase hexadecimal string of exactly 40 characters
  digest_hex: hexadecimal string with even length >= 2
  repo_path: nonempty relative UTF-8 path; no leading slash; no '..' path segment
  immutable_ref: stable_id identifying immutable repository/GitHub/workflow content
  string_value: UTF-8 string length 0..4096
  uint_value: uint
```

There is no free `scalar`, `predicate`, `stable_ref`, or other undefined authority-bearing placeholder.

### 3.2 Closed vocabulary

```yaml
EvidenceResult: [PASS, FAIL, FLAKY, INCONCLUSIVE, NOT_RUN, NOT_APPLICABLE]
SatisfactionState: [SATISFIED, UNSATISFIED, INCONCLUSIVE, NOT_APPLICABLE]
RequirementMode: [REQUIRED, CONDITIONAL]
TrustLevel: [DEGRADED, FULL]
TrustAssessment: [NOT_EVALUATED, DEGRADED, FULL]
DirectiveEffect: [GOAL, PRIORITY, CONSTRAINT, OWNERSHIP, RESOURCE_ASSUMPTION, POLICY_SUPERSESSION, SAFETY_STOP]
ReadinessState: [OPEN, RESOLVED, SUPERSEDED]
RiskClass: [R0, R1, R2, R3]
ArtifactIntegrity: [PRESENT, MISSING, CORRUPT]
ArtifactRightsState: [CLEAR, RESTRICTED, QUARANTINED, UNKNOWN, NOT_APPLICABLE]
ArtifactVisibility: [NORMAL, PROTECTED]
PredicateResult: [TRUE, FALSE, ERROR]
AttemptFailureClass: [PRODUCT, INFRA, ORACLE, HARNESS]
AttemptPolicyMode: [ALL_ATTEMPTS_MUST_PASS, LATEST_AFTER_RETRYABLE_FAILURE, REGISTERED_VERSIONED]
CheckAggregationMode: [ALL_CHECKS, ANY_CHECK, QUORUM, REGISTERED_VERSIONED]
```

`FULL` is stricter than `DEGRADED`. `NOT_EVALUATED` is not a trust level and never satisfies a minimum trust requirement.

### 3.3 `IdentityRef`

```yaml
IdentityRef:
  algorithm_id: stable_id
  encoding_version: stable_id
  digest_hex: digest_hex
```

The tuple is exact identity. This contract deliberately does not select the cross-runtime canonical algorithm/encoding; that remains `W2-HASH-01` authority.

### 3.4 `VersionedRuleRef`

```yaml
VersionedRuleRef:
  registry_id: IdentityRef
  rule_id: stable_id
  rule_version: stable_version
  evaluator_identity: IdentityRef
  conformance_fixture_set_identity: IdentityRef
```

A versioned rule is valid only when the current `PolicyEpoch.rule_registry_id` exactly matches `registry_id`, the registry contains the exact `(rule_id, rule_version, evaluator_identity, conformance_fixture_set_identity)` tuple, and its evaluator reports conformance. Unknown/unregistered rules fail closed. A rule reference is therefore an extension point, not an undefined semantics escape hatch.

## 4. Deterministic predicate contract

### 4.1 Shape

```yaml
PredicateV1:
  version: 1
  input_bindings:
    - alias: stable_id
      object_identity: IdentityRef
      object_type: stable_type
  expression: PredicateExprV1

PredicateExprV1: one_of
  - {op: CONST, value: bool}
  - {op: EXISTS, field: FieldRefV1}
  - {op: EQ, left: OperandV1, right: OperandV1}
  - {op: NEQ, left: OperandV1, right: OperandV1}
  - {op: GTE_UINT, left: OperandV1, right: OperandV1}
  - {op: LTE_UINT, left: OperandV1, right: OperandV1}
  - {op: CONTAINS, collection: FieldRefV1, value: OperandV1}
  - {op: IN, value: OperandV1, set: [LiteralV1]}
  - {op: AND, args: [PredicateExprV1, ...]}
  - {op: OR, args: [PredicateExprV1, ...]}
  - {op: NOT, arg: PredicateExprV1}

FieldRefV1:
  alias: stable_id
  path: [stable_id, ...]

OperandV1: exactly one of
  field: FieldRefV1
  literal: LiteralV1

LiteralV1: exactly one of
  bool_value: bool
  uint_value: uint_value
  string_value: string_value
  id_value: stable_id
```

Empty `AND`/`OR`, duplicate `input_bindings.alias`, unknown operators, array indexing, implicit coercion, ambient time/environment reads, and unbound fields are invalid.

### 4.2 Evaluation

Evaluation uses only the exact objects named in `input_bindings`. Field traversal is by closed-schema field name. Missing object, missing field, type mismatch, unsupported operator/type pair, unresolved identity, or evaluator error yields `ERROR`; no implementation may coerce `ERROR` to `TRUE`.

Context-specific fail-closed handling is fixed:

- applicability predicate `FALSE` -> `NOT_APPLICABLE`; `ERROR` -> invalid plan / no satisfaction;
- directive expiry/recheck `TRUE` -> recheck required; `FALSE` -> no trigger; `ERROR` -> recheck required;
- substitution predicate `TRUE` -> substitution eligible; `FALSE|ERROR` -> substitution not eligible;
- retry predicate `TRUE` -> retry eligibility may proceed; `FALSE|ERROR` -> retry not eligible;
- policy/risk transition predicate `ERROR` -> transition rejected.

No predicate may directly set an envelope result, `EvidenceSatisfaction.state`, review disposition, or ledger state.

## 5. Supporting authority objects

### 5.1 `ActiveDirectiveSet`

```yaml
ActiveDirectiveSet:
  set_id: IdentityRef
  directives:
    - directive_id: stable_id
      source_ref: immutable_ref
      scope_refs: [stable_id]
      effect: DirectiveEffect
      payload_identity: IdentityRef
      supersedes: [stable_id]
      valid_from_policy_epoch: IdentityRef
      expires_or_recheck: null | PredicateV1
```

A directive affects compilation only through a `PolicyEpoch`. It cannot mutate an existing envelope result or directly create `EvidenceSatisfaction`. Safety-stop directives halt applicable execution; resumption requires durable authority.

### 5.2 `PolicyEpoch`

```yaml
PolicyEpoch:
  policy_epoch_id: IdentityRef
  predecessor_epoch_id: null | IdentityRef
  active_directive_set_id: IdentityRef
  compiler_contract_version: stable_version
  rule_registry_id: IdentityRef
  review_route_registry_id: IdentityRef
  effective_requirement_refs: [IdentityRef]
  change_reason_refs: [immutable_ref]
```

Any normative waiver/change creates a new epoch and new requirement identity. Historical evidence remains immutable.

### 5.3 `ResourceCapabilityState`

```yaml
ResourceCapabilityState:
  state_id: IdentityRef
  observed_at_ref: immutable_ref
  available_execution_contexts: positive_uint
  isolated_context_available: bool
  independent_actor_or_permission_separation: NONE | PARTIAL | FULL
  protected_oracle_control_available: NONE | PARTIAL | FULL
  concurrency_capacity: positive_uint
  source_refs: [immutable_ref]
  valid_until_or_recheck: PredicateV1
```

The current master lease-continuation directive belongs in `ActiveDirectiveSet`; it does **not** set isolation/separation fields or upgrade trust.

### 5.4 `ReviewRouteRegistry`

```yaml
ReviewRouteRegistry:
  registry_id: IdentityRef
  policy_epoch_id: IdentityRef
  routes:
    - route_id: stable_id
      strictness_rank: uint
      required_independence_modes: [stable_id]
      required_artifact_kinds: [stable_type]
```

Within one registry each `strictness_rank` is unique. Higher rank is stricter. An unknown route or duplicate rank invalidates the registry. This gives deterministic strictest-route selection without inventing lexical ordering.

### 5.5 `RiskFloor`

```yaml
RiskFloor:
  risk_floor_id: IdentityRef
  scope_ref: stable_id
  risk_class: RiskClass
  minimum_trust: TrustLevel
  minimum_review_route: stable_id
  protected_evidence_required: bool
  minimum_distinct_evidence_surfaces: positive_uint
  source_refs: [immutable_ref]
  downgrade_rule: NEW_POLICY_EPOCH_PLUS_REQUIRED_REVIEW
```

A producer/task author may request stricter handling but cannot lower an applicable floor.

### 5.6 `EffectiveRiskConstraint`

```yaml
EffectiveRiskConstraint:
  effective_risk_constraint_id: IdentityRef
  claim_id: stable_id
  policy_epoch_id: IdentityRef
  source_risk_floor_ids: [IdentityRef]
  minimum_trust: TrustLevel
  minimum_review_route: stable_id
  protected_evidence_required: bool
  minimum_distinct_evidence_surfaces: positive_uint
  compile_trace_identity: IdentityRef
```

Compilation across all applicable floors is deterministic:

1. `minimum_trust` = strictest (`FULL` if any floor requires FULL, else DEGRADED).
2. `protected_evidence_required` = logical OR.
3. `minimum_distinct_evidence_surfaces` = maximum.
4. `minimum_review_route` = route with greatest unique `strictness_rank` in the current exact `ReviewRouteRegistry`.
5. Missing/unknown floor, route, registry, or incomparable/invalid registry -> compilation error; no requirement/plan is emitted.

A task-authored stricter constraint may raise any dimension; it may not lower the compiled result.

## 6. Acceptance-chain machine shapes

### 6.1 `TaskClaimContract`

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
      effective_risk_constraint_id: IdentityRef
      readiness_effect_refs: [stable_id]
  forbidden_claims: [stable_type]
  authoritative_input_refs: [immutable_ref]
  output_refs: [repo_path]
```

Each `claim_id` occurs exactly once and maps to exactly one evidence requirement and one effective risk constraint. Forbidden authority claims invalidate the contract.

### 6.2 Attempt policy and check aggregation

Attempt semantics and cross-check aggregation are separate layers.

```yaml
AttemptPolicyV1:
  mode: AttemptPolicyMode
  max_attempts: positive_uint
  require_contiguous_lineage: bool
  retryable_failure_classes: [AttemptFailureClass]
  retry_eligibility: null | PredicateV1
  registered_rule: null | VersionedRuleRef

CheckAggregationRuleV1:
  mode: CheckAggregationMode
  quorum_required: null | positive_uint
  registered_rule: null | VersionedRuleRef
```

Closed mode rules:

- `ALL_ATTEMPTS_MUST_PASS`: every executed required attempt in the contiguous lineage must be `PASS`; any PRODUCT/ORACLE/HARNESS/INFRA `FAIL` keeps the check non-passing unless an exact substitution rule replaces that evidence. `registered_rule` must be null.
- `LATEST_AFTER_RETRYABLE_FAILURE`: all non-latest failed attempts must have failure class in `retryable_failure_classes`, every retry transition must satisfy `retry_eligibility` when present, lineage must be contiguous, attempt count <= `max_attempts`, and latest attempt must be PASS. Any PRODUCT or other non-retryable prior failure makes the check non-passing. `registered_rule` must be null.
- `REGISTERED_VERSIONED`: `registered_rule` is required and valid under Section 3.4; built-in retry fields still bound lineage/max attempts and the registered evaluator may only be stricter than those bounds.
- `ALL_CHECKS`: every applicable required check must produce a passing attempt-policy result.
- `ANY_CHECK`: at least one required check must pass and the requirement must explicitly permit this mode.
- `QUORUM`: `quorum_required` is required, <= number of applicable required checks, and that many checks must pass.
- `REGISTERED_VERSIONED` aggregation requires a valid registered rule and may not convert a disallowed EvidenceResult into an allowed one or bypass an effective risk constraint.

Unknown mode/rule, lineage gap/cycle/duplicate attempt ID, retry beyond max, retry after non-retryable failure, or rule-registry mismatch is invalid input, not SATISFIED.

### 6.3 `EvidenceRequirement`

```yaml
EvidenceRequirement:
  requirement_id: IdentityRef
  policy_epoch_id: IdentityRef
  claim_id: stable_id
  effective_risk_constraint_id: IdentityRef
  mode: RequirementMode
  applicability_predicate: PredicateV1
  required_evidence_kinds: [stable_type]
  required_execution_surfaces: [stable_type]
  minimum_distinct_evidence_surfaces: positive_uint
  minimum_trust: TrustLevel
  protected_evidence_required: bool
  minimum_review_route: stable_id
  allowed_result_classes: [EvidenceResult]
  substitution_rules:
    - from_kind: stable_type
      replacement_kind: stable_type
      replacement_predicate: PredicateV1
  quarantine_policy_ref: stable_id
  attempt_policy: AttemptPolicyV1
  check_aggregation_rule: CheckAggregationRuleV1
  freshness_requirement_refs: [stable_id]
```

The four risk-derived fields MUST equal or be stricter than the referenced `EffectiveRiskConstraint`; compiler validation rejects downgrade. `NOT_APPLICABLE` is valid only from pre-execution applicability `FALSE`. `NOT_RUN` cannot satisfy a required applicable claim. Requirement identity binds all normative fields and policy epoch.

### 6.4 `CheckPlan`

```yaml
CheckPlan:
  check_plan_id: IdentityRef
  requirement_id: IdentityRef
  effective_risk_constraint_id: IdentityRef
  candidate_work_sha: sha40
  candidate_head_sha: sha40
  base_main_sha: sha40
  policy_epoch_id: IdentityRef
  applicability:
    state: APPLICABLE | NOT_APPLICABLE
    predicate: PredicateV1
    predicate_result: TRUE | FALSE
    evaluated_input_identity: IdentityRef
  required_minimum_distinct_surfaces: positive_uint
  protected_evidence_required: bool
  required_review_route: stable_id
  checks:
    - check_id: stable_id
      evidence_kind: stable_type
      execution_surface: stable_type
      required: bool
      scenario_or_fixture_ref: immutable_ref
      evaluator_requirement_ref: null | stable_id
  compile_trace_identity: IdentityRef
```

An applicability `ERROR` produces no valid plan. The compiler may specialize execution details but cannot weaken the requirement or effective risk constraint. The distinct required execution surfaces represented by applicable required checks must be >= `required_minimum_distinct_surfaces`; if protected evidence is required, at least one required evidence path must demand a PROTECTED artifact and downstream satisfaction requires it.

### 6.5 `ArtifactIdentity`

```yaml
ArtifactIdentity:
  artifact_id: IdentityRef
  content_hash: IdentityRef
  kind: stable_type
  storage_refs: [stable_id]
  produced_by_ref: immutable_ref
  provenance_refs: [immutable_ref]
  rights_or_terms_state: ArtifactRightsState
  visibility: ArtifactVisibility
  retention_class: stable_type
  access_policy_ref: null | stable_id
  supersedes: [IdentityRef]
  integrity_state: ArtifactIntegrity
```

A content hash proves identity, not availability/authority. Missing/corrupt/quarantined required evidence cannot satisfy unless an exact permitted substitution passes.

### 6.6 `ExecutionEvidenceEnvelope`

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
    independence_mode: stable_id
  nondeterministic_surfaces: [stable_type]
  coverage_gaps: [stable_id]
  failure_class: null | AttemptFailureClass
```

Attempts are append-only. `failure_class` is required when result is FAIL and null otherwise. A later PASS never deletes/relabels prior attempts.

### 6.7 `EvidenceSatisfaction` — sole empirical acceptance authority

```yaml
EvidenceSatisfaction:
  satisfaction_id: IdentityRef
  requirement_id: IdentityRef
  effective_risk_constraint_id: IdentityRef
  check_plan_id: IdentityRef
  candidate_work_sha: sha40
  base_main_sha: sha40
  policy_epoch_id: IdentityRef
  evaluated_envelope_ids: [IdentityRef]
  state: SatisfactionState
  reason_codes: [stable_code]
  trust_assessment: TrustAssessment
  distinct_evidence_surfaces_achieved: uint
  protected_evidence_achieved: bool
  required_review_route: stable_id
  missing_check_ids: [stable_id]
  invalid_or_quarantined_artifact_ids: [IdentityRef]
  derivation_trace_identity: IdentityRef
```

Only the deterministic satisfaction compiler may create this object. No directive, task contract, review, issue/PR status, ledger entry, score, or envelope alone may create `SATISFIED`.

Deterministic derivation order:

1. Validate all closed schemas and exact identity tuple: requirement, effective risk constraint, plan, candidate, base, policy epoch.
2. Re-evaluate applicability against exact bound inputs. `ERROR` invalidates the derivation; `FALSE` yields `NOT_APPLICABLE`, `trust_assessment=NOT_EVALUATED`, zero surfaces, protected=false.
3. Validate check set against requirement, minimum distinct surfaces, protected-evidence requirement, and exact required review route propagation.
4. Reject unknown fields/enums/rules, duplicate checks/attempt IDs, broken/cyclic attempt lineage, excess attempts, retry-ineligible transitions, or mismatched identities.
5. Validate every envelope result is a member of `allowed_result_classes`. A disallowed result invalidates the evidence set; it can never be accepted merely because an aggregation rule would otherwise pass.
6. Validate every referenced `ArtifactIdentity`; missing/corrupt/quarantined required evidence is unacceptable unless an exact substitution rule evaluates TRUE. If protected evidence is required, at least one accepted required artifact must be `visibility=PROTECTED`; otherwise emit `INCONCLUSIVE/PROTECTED_EVIDENCE_FLOOR_UNMET`.
7. Derive each check outcome using its exact `AttemptPolicyV1`; then apply `CheckAggregationRuleV1` across checks. Retry history is never erased.
8. Compute achieved distinct evidence surfaces from accepted required check evidence. If below the effective minimum, emit `INCONCLUSIVE/SURFACE_FLOOR_UNMET`.
9. If no evidence-bearing applicable attempt remains evaluable, set `trust_assessment=NOT_EVALUATED`. Otherwise compute trust from envelope profiles plus exact `ResourceCapabilityState`; never infer independence from actor labels/lease authority.
10. Any absent applicable required check or `NOT_RUN` yields `INCONCLUSIVE/MISSING_REQUIRED_EXECUTION`.
11. Any non-replaced required PRODUCT/ORACLE/HARNESS failure yields `UNSATISFIED`; retryable INFRA behavior follows only the exact attempt policy.
12. `FLAKY`/`INCONCLUSIVE` yields `INCONCLUSIVE` unless an exact registered rule validly resolves it without bypassing allowed-result or risk-floor checks.
13. If trust is `NOT_EVALUATED` or below effective minimum, emit `INCONCLUSIVE/TRUST_FLOOR_UNMET`.
14. Emit `SATISFIED` only if aggregation passes, all required artifacts/risk dimensions pass, all consumed result classes are allowed, and every applicable normative requirement is met by immutable evidence.

`required_review_route` is propagated authority, not empirical PASS. A SATISFIED object still cannot advance a decision/readiness blocker until the required review/verification route is satisfied.

## 7. Review, verification, promotion, and readiness

Review/verification may validate derivation, find missing/biased/stale requirements, reject reasoning, or require a new policy/requirement version. They may not overwrite empirical results or directly turn unsatisfied/inconclusive evidence into SATISFIED.

### 7.1 `PromotionGateInput`

```yaml
PromotionGateInput:
  policy_epoch_id: IdentityRef
  satisfaction_refs: [IdentityRef]
  required_review_route: stable_id
  review_or_verification_records:
    - record_ref: immutable_ref
      route_id: stable_id
      disposition: stable_code
```

A promotion compiler verifies that the strictness rank of every qualifying record route is >= the propagated `required_review_route` and that the declared disposition is allowed by the governing task contract. Unknown/missing route or record fails closed. Review authority remains separate from empirical acceptance authority.

### 7.2 `ImplementationReadinessLedger`

```yaml
ImplementationReadinessLedger:
  ledger_id: IdentityRef
  policy_epoch_id: IdentityRef
  candidate_scope_ref: stable_id
  entries:
    - blocker_id: stable_id
      category: PRODUCT | TECHNICAL | FACTORY_TRUST | EVIDENCE | ACCESSIBILITY | RIGHTS | PLATFORM | OTHER
      scope: GLOBAL | DOMAIN | FEATURE_CLASS | PLATFORM | TOOLING
      blocks: [stable_id]
      source_requirement_refs: [IdentityRef]
      resolution_predicate:
        required_satisfaction_refs: [IdentityRef]
        required_review_route: stable_id
        required_review_or_verification_refs: [immutable_ref]
      evidence_satisfaction_refs: [IdentityRef]
      review_or_verification_refs: [immutable_ref]
      state: ReadinessState
      supersedes: null | stable_id
  compile_trace_identity: IdentityRef
```

Ledger compilation is deterministic:

1. Validate exact policy epoch, blocker schema, referenced satisfactions, and review-route registry.
2. `RESOLVED` only when every required satisfaction is exact/current/SATISFIED and every required review/verification record exists and meets or exceeds the required route.
3. `OPEN` is the default for missing/stale/mismatched/inconclusive/insufficient-trust/insufficient-route inputs.
4. `SUPERSEDED` requires a traced new blocker/policy relation; deletion is not resolution.
5. Any OPEN blocker whose `blocks` includes `PRODUCTION_IMPLEMENTATION` keeps that scope blocked.
6. Policy-epoch change recompiles a new ledger; historical ledger objects are immutable.
7. Manual edits/scalar readiness scores have no authority.

For current canonical inputs, `IR-BLOCKER-EVIDENCE-FOUNDATION` remains OPEN. This candidate cannot resolve downstream experimental/review/readiness predicates.

## 8. One-way compiler pipeline

```text
durable directives + exact capability evidence
  -> ActiveDirectiveSet + ResourceCapabilityState
  -> PolicyEpoch + closed RuleRegistry + ReviewRouteRegistry
  -> applicable RiskFloor set
  -> EffectiveRiskConstraint (strictest of every floor dimension)
  -> TaskClaimContract
  -> EvidenceRequirement (must equal/exceed effective constraint)
  -> CheckPlan(exact candidate/head/base, surface/protection/route constraints)
  -> append-only ExecutionEvidenceEnvelope attempts
  -> ArtifactIdentity integrity/provenance validation
  -> per-check AttemptPolicyV1
  -> cross-check CheckAggregationRuleV1
  -> EvidenceSatisfaction (sole empirical acceptance authority)
  -> required review/verification PromotionGateInput
  -> decision transition + ImplementationReadinessLedger compilation
```

Fail closed on unknown type/field/rule/route, unresolved identity, predicate ERROR, stale required external evidence, missing protected evidence, invalid policy transition, ambiguous prerequisite, or violated risk floor.

## 9. Directive-versus-evidence cases

| Case | Required result |
|---|---|
| Owner says “continue existing leases” | Ownership compilation may continue; capability/trust unchanged. |
| Owner says “treat failed engine spike as PASS” | Invalid empirical override; envelope remains FAIL and satisfaction cannot become SATISFIED. |
| Owner legitimately removes a requirement | New directive + PolicyEpoch + requirement identity; historical evidence retained. |
| Emergency safety stop | Applicable execution/claim eligibility halts; no empirical result rewritten. |
| Owner requests stricter review | Effective floor/route may increase; prior low-route promotion becomes insufficient without rewriting evidence. |

## 10. Degraded-trust cases

`DEGRADED_SINGLE_AGENT` is capability-bound trust debt, not empirical failure.

- If minimum trust is DEGRADED, otherwise-valid evidence may be SATISFIED with `trust_assessment=DEGRADED`; downstream review preserves the debt.
- If minimum trust is FULL, the same observations yield `INCONCLUSIVE/TRUST_FLOOR_UNMET`.
- If no evidence-bearing attempt can establish trust, the result uses `NOT_EVALUATED`, never an invented DEGRADED/FULL value.
- Lease continuation changes none of these outcomes.
- Later stronger capability supports a new episode; it does not relabel old evidence.

## 11. Validator fixtures

| ID | Fixture | Expected |
|---|---|---|
| V01 | Applicable required PASS, intact artifact, enough surfaces/protection/trust | `SATISFIED` |
| V02 | Required applicable check is NOT_RUN | `INCONCLUSIVE/MISSING_REQUIRED_EXECUTION` |
| V03 | Applicability PredicateV1 deterministically FALSE | `NOT_APPLICABLE`, trust `NOT_EVALUATED` |
| V04 | Predicate input missing/type mismatch | invalid plan/derivation; no satisfaction |
| V05 | Unknown predicate operator or unbound alias | invalid schema; fail closed |
| V06 | FAIL then PASS under ALL_ATTEMPTS_MUST_PASS | `UNSATISFIED` |
| V07 | INFRA FAIL then PASS under LATEST_AFTER_RETRYABLE_FAILURE, contiguous lineage, eligible retry | check may pass; both attempts retained |
| V08 | PRODUCT FAIL then PASS under LATEST_AFTER_RETRYABLE_FAILURE | non-passing/`UNSATISFIED`; retry laundering rejected |
| V09 | Retry lineage gap/cycle or attempts > max | invalid evidence; no satisfaction |
| V10 | REGISTERED_VERSIONED retry rule absent from exact registry | invalid evidence; no satisfaction |
| V11 | PASS envelope candidate SHA differs from plan | invalid input; no satisfaction |
| V12 | Required artifact hash matches but integrity MISSING | `INCONCLUSIVE/REQUIRED_ARTIFACT_UNAVAILABLE` |
| V13 | Directive asks to override FAIL without policy/version change | reject override; empirical result unchanged |
| V14 | Requirement changed under new PolicyEpoch | new requirement/plan/satisfaction identity; old object unchanged |
| V15 | DEGRADED evidence, minimum FULL | `INCONCLUSIVE/TRUST_FLOOR_UNMET` |
| V16 | DEGRADED evidence, minimum DEGRADED | may be SATISFIED; trust debt preserved |
| V17 | No evaluable evidence-bearing attempt | trust `NOT_EVALUATED`; cannot satisfy required claim |
| V18 | Floor requires PROTECTED but accepted required artifacts all NORMAL | `INCONCLUSIVE/PROTECTED_EVIDENCE_FLOOR_UNMET` |
| V19 | Floor requires 2 distinct surfaces but plan/evidence has 1 | plan invalid or satisfaction `INCONCLUSIVE/SURFACE_FLOOR_UNMET` |
| V20 | Producer requirement lowers FULL floor to DEGRADED | requirement compilation invalid |
| V21 | Producer requirement lowers protected/surface floor | requirement compilation invalid |
| V22 | Promotion record route rank below effective route | promotion/readiness remains blocked despite SATISFIED evidence |
| V23 | Evidence result class absent from `allowed_result_classes` | invalid evidence set; no SATISFIED derivation |
| V24 | Required protected artifact QUARANTINED; no exact substitution TRUE | `INCONCLUSIVE` |
| V25 | Substitution predicate ERROR | substitution rejected; original deficiency remains |
| V26 | Ledger has SATISFIED evidence but mandatory route/record missing | blocker remains OPEN |
| V27 | Ledger manually edited RESOLVED | invalid ledger; recompute OPEN/derived state |
| V28 | Unknown object field/enum/rule/route | invalid input; fail closed |
| V29 | Duplicate claim ID or multiple requirement bindings | invalid TaskClaimContract |
| V30 | ANY/QUORUM aggregation attempts to admit disallowed result or bypass risk floor | invalid/non-satisfying; floor/result checks dominate aggregation |

## 12. Observability and diagnostics

Every compiler stage emits immutable input IDs, policy epoch, exact candidate/head/base, predicate result/trace identity, required/missing checks, all attempt IDs/failure classes, retry-policy decision, artifact integrity/quarantine/visibility, achieved versus required surfaces/protection/trust, required versus supplied review route, and reason codes. Protected diagnostics may redact payloads but not authority-relevant availability/corruption state.

## 13. Failure modes and controls

- **Policy laundering:** change requirement in place -> new PolicyEpoch/identity required.
- **Predicate ambiguity:** implementation-specific expression semantics -> closed PredicateV1 + ERROR fail-closed behavior.
- **Retry laundering:** hide prior failure -> append-only lineage + exact AttemptPolicyV1.
- **Aggregation laundering:** ANY/QUORUM bypasses disallowed result/floor -> result/floor validation precedes aggregation.
- **Directive laundering:** owner assertion becomes empirical truth -> directives affect policy only.
- **Trust laundering:** lease/actor labels imply independence -> capability-bound trust.
- **Risk-floor laundering:** only trust enforced -> EffectiveRiskConstraint compiles trust/protection/surfaces/review route.
- **Artifact laundering:** hash exists but evidence unavailable/quarantined -> integrity/rights/visibility participate in satisfaction.
- **Readiness laundering:** manual resolve/scalar score -> compiled exact ledger and promotion route.
- **Compiler monoculture:** common derivation defect -> W2-REV-01 adversarial review plus downstream conformance evidence.

## 14. Dependencies and interfaces

Primary consumers remain `W2-ENG-03`, `W2-SIM-01`, and `W2-REV-01`. `W2-CI-01`, `W2-PROTECT-01`, `W2-EVAL-01`, and `W2-HASH-01` should emit compatible identities/evidence without gaining authority to weaken this chain. `W2-HASH-01` retains canonical serialization/hash selection; this contract only closes the structure of identity references.

Canonical Planning Program v1 remains ownership/dispatch authority.

## 15. Unresolved questions intentionally delegated

1. Cross-runtime canonical serialization/hash algorithm -> `W2-HASH-01`.
2. Protected-evidence storage/access mechanics -> `W2-PROTECT-01`.
3. CI provider execution/retention mechanics -> `W2-CI-01`.
4. Mutable evaluator fingerprint/calibration thresholds -> `W2-EVAL-01`.
5. Final engine and target product/platform scope -> evidence/review missions elsewhere.
6. Concrete contents of the first RuleRegistry/ReviewRouteRegistry -> later policy synthesis/review; unknown registry entries fail closed meanwhile.

## 16. Reopen conditions

Reopen if any path can mint SATISFIED without the satisfaction compiler; predicates differ across conforming implementations; unregistered retry/aggregation rules carry authority; retries erase prior failures; a producer lowers any effective floor dimension; disallowed result classes reach SATISFIED; missing/quarantined required evidence satisfies without exact substitution; lease continuation upgrades independence; review-route requirements disappear before promotion/readiness; readiness resolves without exact satisfaction plus required review/verification; or W2-HASH-01 requires a different structural identity boundary.

## 17. Review Index

1. **Closure:** Sections 3–4 eliminate undefined authority-bearing primitives/predicates; unknown fields/operators/rules fail closed.
2. **Retry correctness:** Sections 6.2 and 6.7 separate attempt policy from check aggregation; V06–V10 attack retry laundering and unregistered rules.
3. **All RiskFloor dimensions:** Sections 5.4–5.6 deterministically compile trust, protection, distinct surfaces, and review route; V18–V22 attack every downgrade path.
4. **Single empirical authority:** Section 6.7 alone creates empirical SATISFIED; review/promotion/readiness consume but cannot rewrite it.
5. **Trust absence:** `NOT_EVALUATED` is explicit; V03/V17 prevent invented trust.
6. **Allowed results:** derivation step 5 and V23 explicitly reject disallowed result classes before aggregation.
7. **Current trust/readiness:** lease continuation does not upgrade capability; `IR-BLOCKER-EVIDENCE-FOUNDATION` remains OPEN.
8. **Delegated authority:** W2-HASH/PROTECT/CI/EVAL retain their concrete mechanism questions; this candidate claims no production authorization.

Suggested `W2-REV-01` attacks: construct predicate evaluator divergence; retry-launder PRODUCT failure; use ANY/QUORUM to bypass a floor; lower protected/surface/review dimensions independently; use SATISFIED evidence with a weaker review route to resolve a blocker; or smuggle authority through an unregistered versioned rule.