# W2-AUTH-01 — Authority, Evidence, and Readiness Compiler Contract (Remediated Candidate)

**Mission source:** `W2-AUTH-01`  
**Remediation mission:** `W2-REM-AUTH-01` / Issue #87  
**Source candidate work:** `4f2baf8f97a531ac38491343098ac10c81c12a6b`  
**Source self-review:** Issue #69 comment `5251524689`  
**Decision state:** `CANONICAL_CANDIDATE`  
**Authority:** Proposal only; independent `W2-REV-01` remains mandatory.  
**Production implementation authorized:** **No.**

## 1. Scope and invariants

One authority chain governs empirical acceptance:

`TaskClaimContract -> EffectiveRiskConstraint -> EvidenceRequirement -> CheckPlan -> ExecutionEvidenceEnvelope -> EvidenceSatisfaction -> required review/verification -> decision/readiness/integration eligibility`.

Hard invariants:

1. `EvidenceSatisfaction` is the sole empirical acceptance authority.
2. Directives, reviews, PR/issue state, scores, and readiness ledger edits cannot rewrite observations or mint empirical acceptance.
3. Requirement/waiver changes create a new `PolicyEpoch` and new requirement identity.
4. Retry history is append-only; no retry or aggregation may launder prior evidence.
5. Every applicable `RiskFloor` dimension is compiled and cannot be producer-downgraded.
6. Lease continuation does not upgrade `DEGRADED_SINGLE_AGENT` capability or trust.
7. Current production-readiness blockers remain OPEN.

Non-goals: engine/runtime/provider selection, canonical serialization/hash algorithm selection, protected-storage implementation, production dependency promotion, or production implementation authorization.

## 2. Closed contract-layer type system

All machine objects below are closed schemas. Unknown fields are invalid except through the explicit registered-rule extension point. Every authority-bearing field resolves to a primitive, a closed enum, a structured type defined here, `IdentityRef`, `ImmutableRefV1`, or a validated `VersionedRuleRef`. No free `predicate`, `scalar`, `stable_ref`, or undefined authority type exists.

### 2.1 Primitive registry v1

```yaml
PrimitiveRegistryV1:
  bool: exactly true | false
  uint: integer >= 0
  positive_uint: integer >= 1
  stable_id: UTF-8 matching ^[A-Za-z0-9][A-Za-z0-9._:/-]{0,255}$
  stable_type: stable_id
  stable_code: stable_id
  stable_version: stable_id
  sha40: exactly 40 hexadecimal characters
  digest_hex: even-length hexadecimal string, length >= 2
  repo_path: nonempty relative UTF-8 path; no leading slash; no '..' segment
  string_value: UTF-8 length 0..4096
```

### 2.2 Closed enums

```yaml
EvidenceResult: [PASS, FAIL, FLAKY, INCONCLUSIVE, NOT_RUN]
SatisfactionState: [SATISFIED, UNSATISFIED, INCONCLUSIVE, NOT_APPLICABLE]
RequirementMode: [REQUIRED, CONDITIONAL]
TrustLevel: [DEGRADED, FULL]
TrustAssessment: [NOT_EVALUATED, DEGRADED, FULL]
IndependenceMode: [FULL_INDEPENDENT_CONTEXT, DEGRADED_SINGLE_AGENT]
SeparationLevel: [NONE, PARTIAL, FULL]
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
RuleClass: [RETRY, CHECK_AGGREGATION, FRESHNESS]
RetryRuleDecision: [ACCEPT_LATEST, REJECT, INCONCLUSIVE, ERROR]
AggregationRuleDecision: [PASS, NONPASS, INCONCLUSIVE, ERROR]
FreshnessRuleDecision: [FRESH, STALE, ERROR]
ImmutableRefKind: [REPO_BLOB, REPO_PATH_AT_COMMIT, GITHUB_COMMENT, WORKFLOW_ARTIFACT]
```

`FULL` is stricter than `DEGRADED`. `NOT_EVALUATED` is not a trust level. Applicability is a plan property, so `NOT_APPLICABLE` is not an execution-envelope result.

### 2.3 Identity and immutable-reference shapes

```yaml
IdentityRef:
  algorithm_id: stable_id
  encoding_version: stable_id
  digest_hex: digest_hex

ImmutableRefV1: one_of
  - kind: REPO_BLOB
    blob_sha: sha40
  - kind: REPO_PATH_AT_COMMIT
    commit_sha: sha40
    path: repo_path
  - kind: GITHUB_COMMENT
    repository_id: stable_id
    comment_id: positive_uint
  - kind: WORKFLOW_ARTIFACT
    run_id: positive_uint
    artifact_id: positive_uint
    content_identity: IdentityRef
```

Referenced objects must exist and match their declared immutable identity. `IdentityRef` deliberately leaves algorithm/encoding selection to `W2-HASH-01`; this contract closes structure and exact-tuple comparison, not cross-runtime hash authority.

## 3. Closed registered-rule extension point

```yaml
VersionedRuleRef:
  registry_id: IdentityRef
  rule_id: stable_id
  rule_version: stable_version
  evaluator_identity: IdentityRef
  conformance_fixture_set_identity: IdentityRef

RuleRegistry:
  registry_id: IdentityRef
  registry_version: stable_version
  source_refs: [ImmutableRefV1]
  entries:
    - rule_id: stable_id
      rule_version: stable_version
      rule_class: RuleClass
      evaluator_identity: IdentityRef
      conformance_fixture_set_identity: IdentityRef
      exact_input_schema_identity: IdentityRef
      output_contract: RetryRuleDecision | AggregationRuleDecision | FreshnessRuleDecision
      may_accept_disallowed_result_class: false
      may_weaken_effective_risk_constraint: false
      may_ignore_attempt_lineage_or_max: false
```

`(rule_id, rule_version)` is unique and `output_contract` must match `rule_class`. A rule ref is valid only against the exact current registry and matching evaluator/fixture/input identities. Evaluators consume only explicitly supplied immutable inputs: ambient wall time, hidden chat state, mutable network state, and unbound environment values are forbidden. `ERROR` always fails closed. The three `may_*` fields are constants false; any registry that changes them is invalid.

Registered rules may specialize semantics but cannot bypass result-class checks, artifact constraints, effective risk constraints, or lineage/max-attempt bounds.

## 4. Deterministic predicate contract

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
  - {op: IN, value: OperandV1, set: [LiteralV1, ...]}
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
  uint_value: uint
  string_value: string_value
  id_value: stable_id
```

Bindings aliases are unique; paths and AND/OR args are nonempty; operands require exact type equality except explicit uint comparisons; no implicit coercion/indexing/function calls exist. Missing object/field, unknown operator, type mismatch, unresolved identity, or evaluator fault yields `ERROR`.

Context semantics are fixed: applicability FALSE -> NOT_APPLICABLE, ERROR -> no valid plan; directive recheck TRUE/ERROR -> recheck required; substitution TRUE -> eligible and FALSE/ERROR -> ineligible; built-in retry TRUE -> eligible and FALSE/ERROR -> ineligible; policy/risk predicate ERROR -> reject compilation. Predicates never directly set observation, satisfaction, review, or ledger state.

## 5. Policy and capability objects

### 5.1 `ActiveDirectiveSet`

```yaml
ActiveDirectiveSet:
  set_id: IdentityRef
  directives:
    - directive_id: stable_id
      source_ref: ImmutableRefV1
      scope_refs: [stable_id]
      effect: DirectiveEffect
      payload_identity: IdentityRef
      supersedes: [stable_id]
      valid_from_epoch_sequence: uint
      expires_or_recheck: null | PredicateV1
```

Directives affect compilation only through a subsequent/current policy epoch. They cannot mutate existing evidence or satisfaction. Safety-stop effects halt applicable work; resumption requires durable authority.

### 5.2 `PolicyEpoch`

```yaml
PolicyEpoch:
  policy_epoch_id: IdentityRef
  epoch_sequence: uint
  predecessor_epoch_id: null | IdentityRef
  active_directive_set_id: IdentityRef
  compiler_contract_version: stable_version
  rule_registry_id: IdentityRef
  review_route_registry_id: IdentityRef
  change_reason_refs: [ImmutableRefV1]
```

`epoch_sequence` strictly increases from predecessor. A normative waiver/change creates a new epoch and new downstream requirement identity; historical evidence remains immutable.

### 5.3 `ResourceCapabilityState` and trust derivation

```yaml
ResourceCapabilityState:
  state_id: IdentityRef
  observed_at_ref: ImmutableRefV1
  available_execution_contexts: positive_uint
  isolated_context_available: bool
  independent_actor_or_permission_separation: SeparationLevel
  protected_oracle_control_available: SeparationLevel
  concurrency_capacity: positive_uint
  source_refs: [ImmutableRefV1]
  valid_until_or_recheck: PredicateV1
```

`TrustDerivationV1` is deterministic for accepted evidence under one requirement:

1. no evaluable evidence-bearing accepted attempt -> `NOT_EVALUATED`;
2. all accepted envelopes must reference the requirement's exact capability-state ID;
3. FULL requires every accepted envelope to claim FULL, capability `isolated_context_available=true`, and `independent_actor_or_permission_separation=FULL`; if protected evidence is required, `protected_oracle_control_available=FULL` is additionally required;
4. otherwise achieved trust is DEGRADED.

An envelope claiming FULL under weaker capability is deterministically downgraded to DEGRADED for satisfaction. Lease continuation changes none of these fields/rules.

## 6. Review-route and risk-floor compilation

### 6.1 `ReviewRouteRegistry`

```yaml
ReviewRouteRegistry:
  registry_id: IdentityRef
  registry_version: stable_version
  source_refs: [ImmutableRefV1]
  routes:
    - route_id: stable_id
      strictness_rank: uint
      allowed_independence_modes: [IndependenceMode]
      required_artifact_kinds: [stable_type]
```

Route IDs and strictness ranks are each unique. Higher rank is stricter. Unknown route, duplicate ID/rank, or registry mismatch invalidates compilation.

### 6.2 `RiskFloor`

```yaml
RiskFloor:
  risk_floor_id: IdentityRef
  scope_ref: stable_id
  applicability_predicate: PredicateV1
  risk_class: RiskClass
  minimum_trust: TrustLevel
  minimum_review_route: stable_id
  protected_evidence_required: bool
  minimum_distinct_evidence_surfaces: positive_uint
  source_refs: [ImmutableRefV1]
  downgrade_rule: NEW_POLICY_EPOCH_PLUS_REQUIRED_REVIEW
```

Applicability TRUE includes the floor; FALSE excludes it; ERROR fails closed and prevents an effective constraint.

### 6.3 `EffectiveRiskConstraint`

```yaml
EffectiveRiskConstraint:
  effective_risk_constraint_id: IdentityRef
  task_claim_contract_id: IdentityRef
  claim_id: stable_id
  policy_epoch_id: IdentityRef
  source_risk_floor_ids: [IdentityRef]
  minimum_trust: TrustLevel
  minimum_review_route: stable_id
  protected_evidence_required: bool
  minimum_distinct_evidence_surfaces: positive_uint
  compile_trace_identity: IdentityRef
```

Across all applicable floors: trust is FULL if any requires FULL else DEGRADED; protection is OR; minimum surfaces is max; review route is greatest unique strictness rank in the exact route registry. Missing/unknown floor/route/registry or predicate ERROR -> no valid constraint. Producer/task requirements may raise but never lower a dimension.

## 7. Acceptance-chain machine shapes

### 7.1 `TaskClaimContract`

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
      requirement_key: stable_id
      risk_floor_ids: [IdentityRef]
      readiness_effect_refs: [stable_id]
  forbidden_claims: [stable_type]
  authoritative_input_refs: [ImmutableRefV1]
  output_refs: [repo_path]
```

`claim_id` and `requirement_key` are unique within the contract. Each claim has at least one risk floor. Forbidden authority claims invalidate the contract. The compiler derives the exact effective constraint and requirement from this object; the contract does not contain a back-reference to objects it produces.

### 7.2 Attempt policy and check aggregation

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

- ALL_ATTEMPTS_MUST_PASS: every executed attempt in the check lineage must PASS; FAIL is non-passing; FLAKY/INCONCLUSIVE/NOT_RUN is inconclusive; no registered rule.
- LATEST_AFTER_RETRYABLE_FAILURE: only prior FAIL attempts may be retried; each failure class is listed retryable; retry predicate passes when present; lineage contiguous; attempt count <= max; latest PASS. PRODUCT/non-retryable FAIL is non-passing. FLAKY/INCONCLUSIVE/NOT_RUN cannot use this built-in retry and remain inconclusive.
- REGISTERED_VERSIONED attempt mode requires rule class RETRY and still obeys lineage/max/risk/result constraints.
- ALL_CHECKS: all applicable non-replacement required checks execute and pass.
- ANY_CHECK: all applicable non-replacement required checks execute; at least one passes.
- QUORUM: all applicable non-replacement required checks execute; quorum is present, positive, <= check count, and at least quorum passes.
- registered aggregation requires rule class CHECK_AGGREGATION and cannot bypass result/artifact/risk checks.

Unknown mode/rule/class, lineage gap/cycle/duplicate attempt ID, retry beyond max, or retry after ineligible failure -> invalid evidence set.

### 7.3 `SubstitutionRuleV1`

```yaml
SubstitutionRuleV1:
  rule_id: stable_id
  from_evidence_kind: stable_type
  replacement_evidence_kind: stable_type
  eligibility_predicate: PredicateV1
```

A substitution is valid only when the rule exists exactly once; the original deficiency matches `from_evidence_kind`; a replacement-only check with `replacement_evidence_kind` exists in the same exact plan; eligibility TRUE; replacement envelope/artifact IDs are recorded in satisfaction; and replacement evidence independently meets attempt/result/freshness/artifact/trust/effective-risk constraints. FALSE/ERROR means no substitution. Original evidence is retained.

### 7.4 `EvidenceRequirement`

```yaml
EvidenceRequirement:
  requirement_id: IdentityRef
  task_claim_contract_id: IdentityRef
  requirement_key: stable_id
  policy_epoch_id: IdentityRef
  claim_id: stable_id
  effective_risk_constraint_id: IdentityRef
  resource_capability_state_id: IdentityRef
  mode: RequirementMode
  applicability_predicate: PredicateV1
  required_evidence_kinds: [stable_type]
  required_execution_surfaces: [stable_type]
  minimum_distinct_evidence_surfaces: positive_uint
  minimum_trust: TrustLevel
  protected_evidence_required: bool
  minimum_review_route: stable_id
  allowed_result_classes: [EvidenceResult]
  allowed_artifact_rights_states: [ArtifactRightsState]
  substitution_rules: [SubstitutionRuleV1]
  attempt_policy: AttemptPolicyV1
  check_aggregation_rule: CheckAggregationRuleV1
  freshness_rule: null | VersionedRuleRef
```

Contract/requirement key/claim/resource capability must exactly match the producing `TaskClaimContract`. The four risk-derived fields equal or exceed `EffectiveRiskConstraint`; downgrade is invalid. `freshness_rule`, if present, is class FRESHNESS; STALE/ERROR prevents acceptance. `allowed_result_classes` are result classes permitted to contribute a passing empirical input; disallowed observations are retained but cannot contribute to SATISFIED. `QUARANTINED` is never directly acceptable even if mistakenly listed in allowed rights states.

### 7.5 `CheckPlan`

```yaml
CheckPlan:
  check_plan_id: IdentityRef
  requirement_id: IdentityRef
  effective_risk_constraint_id: IdentityRef
  resource_capability_state_id: IdentityRef
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
      replacement_only: bool
      scenario_or_fixture_ref: ImmutableRefV1
      evaluator_requirement_identity: null | IdentityRef
  compile_trace_identity: IdentityRef
```

Applicability ERROR emits no plan. Required non-replacement checks cover the requirement's normative evidence kinds/surfaces and minimum distinct surfaces. Replacement-only checks do not count toward normal minima unless a valid substitution is actually applied. Risk fields must exactly match/exceed the requirement/effective constraint.

### 7.6 `ArtifactIdentity`

```yaml
ArtifactIdentity:
  artifact_id: IdentityRef
  content_hash: IdentityRef
  kind: stable_type
  storage_locator_ids: [stable_id]
  produced_by_ref: ImmutableRefV1
  provenance_refs: [ImmutableRefV1]
  rights_or_terms_state: ArtifactRightsState
  visibility: ArtifactVisibility
  retention_class: stable_type
  access_policy_id: null | stable_id
  supersedes: [IdentityRef]
  integrity_state: ArtifactIntegrity
```

Hash proves identity, not availability. MISSING/CORRUPT and QUARANTINED cannot directly satisfy. Other rights states satisfy only when listed by the exact requirement. A deficient artifact requires an exact valid substitution rather than a manual waiver.

### 7.7 `ExecutionEvidenceEnvelope`

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
  resource_capability_state_id: IdentityRef
  environment_fingerprint: IdentityRef
  toolchain_fingerprint: IdentityRef
  content_schema_package_ref: ImmutableRefV1
  execution_surface: stable_type
  scenario_policy_action_seed_refs: [ImmutableRefV1]
  evaluator_fingerprint_refs: [IdentityRef]
  result: EvidenceResult
  artifact_ids: [IdentityRef]
  trust_profile:
    level: TrustLevel
    independence_mode: IndependenceMode
  nondeterministic_surfaces: [stable_type]
  coverage_gaps: [stable_id]
  failure_class: null | AttemptFailureClass
```

Capability-state ID must equal requirement/plan. `failure_class` is required exactly for FAIL. Attempts are append-only. Any envelope for NOT_APPLICABLE plan state is invalid.

### 7.8 `EvidenceSatisfaction` — sole empirical acceptance authority

```yaml
EvidenceSatisfaction:
  satisfaction_id: IdentityRef
  requirement_id: IdentityRef
  effective_risk_constraint_id: IdentityRef
  check_plan_id: IdentityRef
  resource_capability_state_id: IdentityRef
  candidate_work_sha: sha40
  base_main_sha: sha40
  policy_epoch_id: IdentityRef
  evaluated_envelope_ids: [IdentityRef]
  applied_substitutions:
    - substitution_rule_id: stable_id
      original_check_id: null | stable_id
      original_artifact_id: null | IdentityRef
      replacement_envelope_ids: [IdentityRef]
      replacement_artifact_ids: [IdentityRef]
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

Exactly one of `original_check_id` / `original_artifact_id` is non-null per applied substitution. Only this deterministic compiler creates empirical SATISFIED.

Ordered derivation:

1. validate closed schemas and exact contract/requirement/risk/plan/capability/candidate/base/policy identities;
2. re-evaluate applicability: ERROR -> no satisfaction; FALSE -> NOT_APPLICABLE, trust NOT_EVALUATED, zero surfaces, protected=false;
3. validate check set and exact risk/surface/protection/review-route propagation;
4. validate attempt IDs, lineage/max, retry eligibility, rule class/identity; malformed input -> no satisfaction;
5. derive per-check attempt outcome. Any observation used as a passing empirical input must have result in `allowed_result_classes`; a disallowed result remains historical but cannot contribute to SATISFIED;
6. evaluate freshness rule using exact immutable inputs; STALE/ERROR -> INCONCLUSIVE;
7. validate artifacts: required integrity PRESENT, rights state allowed, never QUARANTINED, and exact identity/provenance. Deficiency is non-satisfying unless a valid substitution independently passes all constraints;
8. if protection required, accepted required evidence includes at least one PROTECTED artifact; else INCONCLUSIVE/PROTECTED_EVIDENCE_FLOOR_UNMET;
9. apply cross-check aggregation only after steps 4–8; aggregation cannot rescue disallowed results, invalid artifacts, freshness, or risk floors;
10. compute distinct accepted execution surfaces; below minimum -> INCONCLUSIVE/SURFACE_FLOOR_UNMET;
11. derive trust by `TrustDerivationV1`; NOT_EVALUATED or below minimum -> INCONCLUSIVE/TRUST_FLOOR_UNMET;
12. missing/NOT_RUN required execution -> INCONCLUSIVE/MISSING_REQUIRED_EXECUTION;
13. non-replaced PRODUCT/ORACLE/HARNESS FAIL -> UNSATISFIED; INFRA FAIL follows only the exact attempt policy; unresolved retry state -> INCONCLUSIVE;
14. FLAKY/INCONCLUSIVE remains INCONCLUSIVE unless a valid registered rule returns a permitted stricter resolution without bypassing steps 5–11;
15. SATISFIED only when aggregation passes and every applicable normative result/freshness/artifact/substitution/risk/trust constraint passes.

`required_review_route` is propagated authority, not empirical truth. SATISFIED alone never authorizes promotion/readiness.

## 8. Review, promotion, and readiness

Review/verification may validate derivation, identify biased/stale/missing requirements, reject reasoning, or require new policy. It cannot overwrite empirical results or directly set SATISFIED.

```yaml
PromotionGateInput:
  policy_epoch_id: IdentityRef
  satisfaction_refs: [IdentityRef]
  required_review_route: stable_id
  review_or_verification_records:
    - record_ref: ImmutableRefV1
      route_id: stable_id
      independence_mode: IndependenceMode
      disposition: stable_code
```

Promotion requires exact current SATISFIED refs and at least one qualifying record with route rank >= required route, independence mode allowed by that route, required route artifacts present, and disposition allowed by the governing task contract. Missing/unknown/weak route or record -> blocked.

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
        required_review_or_verification_refs: [ImmutableRefV1]
      evidence_satisfaction_refs: [IdentityRef]
      review_or_verification_refs: [ImmutableRefV1]
      state: ReadinessState
      supersedes: null | stable_id
  compile_trace_identity: IdentityRef
```

RESOLVED is compiler-only: all exact/current required satisfactions are SATISFIED and every mandatory review/verification ref meets route/independence requirements. OPEN is default for missing/stale/mismatch/inconclusive/insufficient trust/route. SUPERSEDED requires traced replacement. Policy change emits a new ledger. Manual edit/scalar score has no authority. Any OPEN blocker whose `blocks` includes `PRODUCTION_IMPLEMENTATION` keeps that scope blocked.

`IR-BLOCKER-EVIDENCE-FOUNDATION` remains OPEN.

## 9. One-way compile direction

```text
durable directives + exact capability evidence + immutable registries
  -> ActiveDirectiveSet + ResourceCapabilityState
  -> PolicyEpoch + RuleRegistry + ReviewRouteRegistry
  -> TaskClaimContract
  -> applicable RiskFloor set -> EffectiveRiskConstraint
  -> EvidenceRequirement
  -> CheckPlan(exact candidate/head/base/capability)
  -> append-only ExecutionEvidenceEnvelope attempts + ArtifactIdentity
  -> AttemptPolicyV1 + exact substitutions + freshness
  -> CheckAggregationRuleV1
  -> EvidenceSatisfaction
  -> mandatory review/verification PromotionGateInput
  -> decision transition + ImplementationReadinessLedger
```

Unknown type/field/rule/route, unresolved identity, predicate ERROR, stale freshness, artifact deficiency, invalid policy transition, ambiguous prerequisite, or floor downgrade fails closed.

## 10. Directive and degraded-trust cases

| Case | Required result |
|---|---|
| “continue existing leases” | ownership may continue; capability/trust unchanged |
| “treat failed spike as PASS” | invalid empirical override; observation stays FAIL |
| legitimate requirement removal | new directive + PolicyEpoch + requirement identity; history unchanged |
| emergency safety stop | halt applicable work; do not rewrite observations |
| stricter review directive | new/effective route may increase; old weaker promotion becomes insufficient |
| DEGRADED evidence, minimum DEGRADED | may satisfy if all other constraints pass; debt remains |
| DEGRADED evidence, minimum FULL | INCONCLUSIVE/TRUST_FLOOR_UNMET |
| no evaluable evidence | trust NOT_EVALUATED; required claim cannot satisfy |

Later stronger capability supports a new episode; it never relabels old evidence.

## 11. Validator fixtures

| ID | Fixture | Expected |
|---|---|---|
| V01 | applicable required PASS, intact allowed-rights evidence, enough surfaces/protection/trust | SATISFIED |
| V02 | required applicable check NOT_RUN | INCONCLUSIVE/MISSING_REQUIRED_EXECUTION |
| V03 | applicability predicate FALSE | NOT_APPLICABLE + NOT_EVALUATED |
| V04 | predicate missing input/type mismatch | ERROR; no plan/satisfaction |
| V05 | unknown predicate operator/unbound alias | invalid schema |
| V06 | FAIL then PASS under ALL_ATTEMPTS_MUST_PASS | UNSATISFIED |
| V07 | retryable INFRA FAIL then PASS under valid LATEST policy | may pass; both retained |
| V08 | PRODUCT FAIL then PASS under LATEST policy | UNSATISFIED/non-passing |
| V09 | FLAKY then PASS under built-in LATEST | INCONCLUSIVE; built-in retry ineligible |
| V10 | lineage gap/cycle/duplicate/over max | invalid evidence set |
| V11 | registered rule absent/wrong class/identity | invalid/no authority |
| V12 | registry sets any `may_*` true | invalid registry |
| V13 | candidate or capability-state ID differs from plan/requirement | invalid; no satisfaction |
| V14 | artifact MISSING/CORRUPT | non-satisfying absent valid substitution |
| V15 | directive attempts FAIL->PASS | reject override; observation unchanged |
| V16 | new PolicyEpoch changes requirement | new identities; history unchanged |
| V17 | DEGRADED evidence, minimum FULL | INCONCLUSIVE/TRUST_FLOOR_UNMET |
| V18 | envelope claims FULL but capability lacks isolation/FULL separation | achieved trust DEGRADED |
| V19 | no evaluable evidence | NOT_EVALUATED; cannot satisfy |
| V20 | protected floor but accepted evidence all NORMAL | INCONCLUSIVE/PROTECTED_EVIDENCE_FLOOR_UNMET |
| V21 | floor needs 2 surfaces, plan/evidence has 1 | invalid plan or INCONCLUSIVE/SURFACE_FLOOR_UNMET |
| V22 | producer lowers FULL->DEGRADED | invalid requirement compilation |
| V23 | producer lowers protection/surface floor | invalid requirement compilation |
| V24 | producer supplies weaker review route | invalid requirement compilation |
| V25 | promotion record route weak or independence mode disallowed | promotion/readiness blocked |
| V26 | PASS observation absent from allowed_result_classes | cannot contribute to SATISFIED |
| V27 | artifact rights state not allowed or QUARANTINED | non-satisfying absent exact substitution |
| V28 | substitution predicate ERROR | no substitution |
| V29 | replacement check absent from same plan | substitution invalid |
| V30 | replacement evidence below any result/freshness/artifact/trust/risk constraint | substitution cannot satisfy |
| V31 | freshness rule STALE/ERROR | INCONCLUSIVE |
| V32 | ANY/QUORUM/registered aggregation tries to bypass result/artifact/risk constraint | cannot satisfy |
| V33 | ledger SATISFIED evidence but required review missing/weak | blocker OPEN |
| V34 | ledger manually edited RESOLVED | invalid; recompute |
| V35 | unknown object field/enum/rule/route | invalid; fail closed |
| V36 | duplicate claim/requirement key or zero risk floors | invalid TaskClaimContract |
| V37 | applied substitution has both/neither original check/artifact IDs | invalid satisfaction object |
| V38 | RiskFloor applicability predicate ERROR | no effective constraint/requirement compilation |

## 12. Observability and failure controls

Every stage emits immutable input IDs, policy epoch, exact candidate/head/base/capability, predicate outcomes, required/missing checks, attempt lineage/failure classes, rule identities/decisions, substitutions, freshness, artifact integrity/rights/visibility, achieved-vs-required surfaces/protection/trust, review route/independence, and reason codes. Protected payloads may be redacted; authority-relevant availability/corruption cannot be hidden.

Controls: closed predicates prevent evaluator ambiguity; new epochs prevent policy laundering; append-only lineage prevents retry laundering; exact registries prevent extension laundering; planned/recorded replacement evidence prevents substitution laundering; result/artifact/risk checks dominate aggregation; capability-bound trust prevents lease/label laundering; `EffectiveRiskConstraint` closes all four floor dimensions; exact promotion routes and compiled ledger prevent readiness laundering.

## 13. Interfaces, delegated questions, and reopen conditions

Primary consumers remain `W2-ENG-03`, `W2-SIM-01`, and `W2-REV-01`. `W2-CI-01`, `W2-PROTECT-01`, `W2-EVAL-01`, and `W2-HASH-01` emit compatible evidence/identities without authority to weaken this chain.

Delegated concrete decisions: serialization/hash selection -> W2-HASH-01; protected storage/access -> W2-PROTECT-01; CI execution/retention -> W2-CI-01; evaluator calibration/fingerprint mechanics -> W2-EVAL-01; engine/platform/product scope -> declared evidence/review missions.

Reopen if conforming predicate evaluators can disagree; any undefined authority field/rule exists; retries/aggregation/substitution bypass evidence; any producer lowers trust/protection/surface/review floor; disallowed result/artifact reaches SATISFIED; lease continuation upgrades independence; weak review resolves promotion/readiness; or readiness resolves without exact satisfaction plus required review/verification.

## 14. Review Index

1. **Closure:** Sections 2–4 define primitives, immutable refs, exact rule registry, and predicate AST/error behavior; V04–V05/V11–V12/V35 attack escapes.
2. **Retry vs aggregation:** Sections 7.2/7.8 separate attempt and check layers; V06–V10/V32 attack laundering.
3. **Substitution/freshness:** Sections 7.3–7.8 require planned replacement evidence and exact freshness rules; V27–V31/V37 attack ambiguity.
4. **All RiskFloor dimensions:** Section 6 compiles trust/protection/surfaces/review route; V20–V25/V38 attack downgrade/applicability paths.
5. **Single empirical authority:** only Section 7.8 creates SATISFIED; downstream review/readiness only consume it.
6. **Trust absence/capability:** Section 5.3 defines deterministic NOT_EVALUATED/DEGRADED/FULL derivation; V17–V19 attack trust laundering.
7. **Allowed result/artifact states:** requirement + satisfaction steps explicitly gate acceptance; V26–V27 attack bypass.
8. **Current state:** lease continuation leaves degraded trust unchanged; evidence-foundation blocker remains OPEN; no production implementation authorized.

Suggested `W2-REV-01` attacks: predicate divergence; malicious rule registry; retry-launder PRODUCT failure; substitution without planned replacement; aggregation floor bypass; independent review-route downgrade; false FULL trust from weak capability; or readiness resolution with a weak/missing review record.