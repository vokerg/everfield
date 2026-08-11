# W2-AUTH-01 — Authority, Evidence, and Readiness Compiler Contract (Remediated Candidate)

**Mission source:** `W2-AUTH-01`  
**Remediation mission:** `W2-REM-AUTH-01` / Issue #87  
**Source candidate work:** `4f2baf8f97a531ac38491343098ac10c81c12a6b`  
**Source self-review:** Issue #69 comment `5251524689`  
**Decision state:** `CANONICAL_CANDIDATE`  
**Authority:** Proposal only; independent `W2-REV-01` remains mandatory.  
**Production implementation authorized:** **No.**

## 1. Scope and non-goals

One authority chain governs empirical acceptance:

`TaskClaimContract -> EffectiveRiskConstraint -> EvidenceRequirement -> CheckPlan -> ExecutionEvidenceEnvelope -> EvidenceSatisfaction -> required review/verification -> decision/readiness/integration eligibility`.

Hard invariants:

1. `EvidenceSatisfaction` is the sole empirical acceptance authority.
2. Directives, reviews, PR/issue state, scores, and readiness-ledger edits cannot rewrite observations or mint empirical acceptance.
3. Requirement/waiver changes create a new `PolicyEpoch` and new requirement identity.
4. Failed/inconclusive/unrun required evidence cannot disappear through retry or aggregation; only an exact versioned replacement path may discharge it while preserving history.
5. Every applicable `RiskFloor` dimension is compiled and cannot be producer-downgraded.
6. Lease continuation does not upgrade `DEGRADED_SINGLE_AGENT` capability or trust.
7. Current production-readiness blockers remain OPEN.

Non-goals: selecting an engine/runtime/provider; selecting canonical serialization/hash algorithms; implementing protected storage; promoting planning experiments into production dependencies; or authorizing production implementation.

## 2. Authority and derivation distinctions

Observed canonical constraints:

- Wave 1 defines one acceptance chain and makes `EvidenceSatisfaction` derived, not hand-authored truth.
- A required FAIL/FLAKY/INCONCLUSIVE/NOT_RUN cannot yield SATISFIED unless the versioned requirement provides valid replacement evidence; historical evidence is not rewritten.
- Directives may change policy but cannot change observed empirical results.
- `ArtifactIdentity` is the durable artifact identity; hash proves identity, not availability.
- Current lease continuation does not establish independent/multi-agent capability; mandatory independent work remains `DEGRADED_SINGLE_AGENT` under current resource state.
- `IR-BLOCKER-EVIDENCE-FOUNDATION` remains OPEN.

Remediation inference introduced here:

- contract-layer predicates and extension rules need closed input/evaluation semantics;
- retry replacement and alternative-check aggregation must be separate so a mandatory failure cannot be outvoted;
- all four `RiskFloor` dimensions need one immutable `EffectiveRiskConstraint` carried to promotion/readiness;
- trust needs an explicit `NOT_EVALUATED` state.

Recommendation: use the schemas, compiler order, and fixtures below as the candidate contract for `W2-REV-01` attack.

## 3. Closed contract-layer type system

Every machine object below is a closed schema. Unknown fields are invalid except through the explicit registered-rule extension point. Every authority-bearing field resolves to a primitive, closed enum, structured type defined here, `IdentityRef`, `ImmutableRefV1`, or a validated `RuleInvocationV1`. No free `predicate`, `scalar`, `stable_ref`, or undefined authority type exists.

### 3.1 Primitive registry v1

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

### 3.2 Closed enums

```yaml
EvidenceResult: [PASS, FAIL, FLAKY, INCONCLUSIVE, NOT_RUN]
SatisfactionState: [SATISFIED, UNSATISFIED, INCONCLUSIVE, NOT_APPLICABLE]
RequirementMode: [REQUIRED, CONDITIONAL]
TrustLevel: [DEGRADED, FULL]
TrustAssessment: [NOT_EVALUATED, DEGRADED, FULL]
IndependenceMode: [FULL_INDEPENDENT_CONTEXT, DEGRADED_SINGLE_AGENT]
SeparationLevel: [NONE, PARTIAL, FULL]
CheckRole: [MANDATORY, ALTERNATIVE, REPLACEMENT]
DirectiveEffect: [GOAL, PRIORITY, CONSTRAINT, OWNERSHIP, RESOURCE_ASSUMPTION, POLICY_SUPERSESSION, SAFETY_STOP]
ReadinessState: [OPEN, RESOLVED, SUPERSEDED]
RiskClass: [R0, R1, R2, R3]
ArtifactIntegrity: [PRESENT, MISSING, CORRUPT]
ArtifactRightsState: [CLEAR, RESTRICTED, QUARANTINED, UNKNOWN, NOT_APPLICABLE]
ArtifactVisibility: [NORMAL, PROTECTED]
AttemptFailureClass: [PRODUCT, INFRA, ORACLE, HARNESS]
AttemptPolicyMode: [ALL_ATTEMPTS_MUST_PASS, LATEST_AFTER_RETRYABLE_FAILURE, REGISTERED_VERSIONED]
CheckAggregationMode: [ALL_MANDATORY_ONLY, ANY_ALTERNATIVE, QUORUM_ALTERNATIVE, REGISTERED_VERSIONED]
RuleClass: [RETRY, CHECK_AGGREGATION, FRESHNESS]
RetryRuleDecision: [ACCEPT_REPLACEMENT_PASS, REJECT, INCONCLUSIVE, ERROR]
AggregationRuleDecision: [PASS, NONPASS, INCONCLUSIVE, ERROR]
FreshnessRuleDecision: [FRESH, STALE, ERROR]
ImmutableRefKind: [REPO_BLOB, REPO_PATH_AT_COMMIT, GITHUB_COMMENT, WORKFLOW_ARTIFACT]
```

`FULL` is stricter than `DEGRADED`. `NOT_EVALUATED` is not a trust level. Applicability is a plan property, so `NOT_APPLICABLE` is not an execution-envelope result.

### 3.3 Identity and immutable references

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

Referenced objects must exist and match their immutable identity. `IdentityRef` leaves algorithm/encoding selection to `W2-HASH-01`; this contract closes reference structure and exact-tuple comparison, not cross-runtime hash authority.

## 4. Deterministic predicate and registered-rule contracts

### 4.1 `PredicateV1`

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

Binding aliases are unique; paths and AND/OR argument lists are nonempty; no implicit coercion/indexing/function calls exist. Missing object/field, unknown operator, type mismatch, unresolved identity, or evaluator fault yields `ERROR`.

Context handling is fixed: applicability FALSE -> NOT_APPLICABLE and ERROR -> no valid plan; directive recheck TRUE/ERROR -> recheck required; substitution TRUE -> eligible and FALSE/ERROR -> ineligible; built-in retry TRUE -> eligible and FALSE/ERROR -> ineligible; risk/policy predicate ERROR -> reject compilation. Predicates never directly set observation, satisfaction, review, or readiness state.

### 4.2 Registered rules and exact invocation inputs

```yaml
VersionedRuleRef:
  registry_id: IdentityRef
  rule_id: stable_id
  rule_version: stable_version
  evaluator_identity: IdentityRef
  conformance_fixture_set_identity: IdentityRef

RuleInputBindingV1:
  alias: stable_id
  object_identity: IdentityRef
  object_type: stable_type

RuleInvocationV1:
  rule_ref: VersionedRuleRef
  input_bindings: [RuleInputBindingV1]
  invocation_identity: IdentityRef

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
      may_ignore_mandatory_check_failure: false
      may_ignore_attempt_lineage_or_max: false
```

`(rule_id, rule_version)` is unique and output contract matches rule class. A rule invocation is valid only when its rule exactly matches the current registry and its unique ordered binding map validates exactly against `exact_input_schema_identity`: no missing, extra, duplicate, wrong-type, implicit, or ambient input. `invocation_identity` binds exact rule + exact ordered bindings.

Evaluators consume only bound immutable inputs; ambient wall time, hidden chat state, mutable network state, and unbound environment are forbidden. `ERROR` fails closed. Every `may_*` field is constant false; changing one invalidates the registry. A registered rule may specialize semantics but cannot weaken mandatory checks, result/artifact/risk constraints, or lineage/max-attempt bounds.

## 5. Policy, capability, and trust

### 5.1 `ActiveDirectiveSet` and `PolicyEpoch`

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

Directives affect compilation only through policy; they cannot mutate historical evidence. `epoch_sequence` strictly increases from predecessor. Any normative waiver/change creates a new epoch and downstream requirement identity.

### 5.2 `ResourceCapabilityState` and `TrustDerivationV1`

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

Trust derivation for accepted evidence is deterministic:

1. no evaluable accepted evidence-bearing attempt -> `NOT_EVALUATED`;
2. all accepted envelopes reference the exact requirement capability-state ID;
3. FULL requires every accepted envelope to claim FULL, isolation=true, and actor/permission separation=FULL; protected evidence additionally requires protected-oracle control=FULL;
4. otherwise achieved trust is DEGRADED.

A FULL envelope under weaker capability is downgraded to DEGRADED for satisfaction. Lease continuation changes none of these capability facts.

## 6. Review routes and complete RiskFloor compilation

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

Route IDs/ranks are unique; higher rank is stricter. RiskFloor applicability TRUE includes, FALSE excludes, ERROR blocks compilation. Across all applicable floors: trust = FULL if any requires FULL else DEGRADED; protection = OR; minimum distinct surfaces = max; review route = greatest unique strictness rank. Missing/unknown floor/route/registry or predicate ERROR -> no valid constraint. Producer/task requirements may raise but never lower a dimension.

## 7. Claim, requirement, plan, attempt, artifact, and envelope shapes

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

`claim_id` and `requirement_key` are unique. Each claim has at least one risk floor. The compiler derives downstream objects one-way; the task contract contains no back-reference to objects it produces.

### 7.2 Retry policy: replacement evidence, never history erasure

```yaml
AttemptPolicyV1:
  mode: AttemptPolicyMode
  max_attempts: positive_uint
  require_contiguous_lineage: bool
  retryable_failure_classes: [AttemptFailureClass]
  retry_eligibility: null | PredicateV1
  registered_rule: null | RuleInvocationV1
```

- `ALL_ATTEMPTS_MUST_PASS`: all attempts in the check lineage must PASS; FAIL is non-passing; FLAKY/INCONCLUSIVE/NOT_RUN is inconclusive; no retry replacement exists.
- `LATEST_AFTER_RETRYABLE_FAILURE`: a later PASS may serve as **replacement evidence**, never erasure, only when every earlier non-pass being replaced is FAIL, every failure class is listed retryable, every retry predicate is TRUE when present, lineage is contiguous, attempt count <= max, and latest is PASS. FLAKY/INCONCLUSIVE/NOT_RUN cannot use this built-in replacement.
- `REGISTERED_VERSIONED`: valid RETRY invocation required. `ACCEPT_REPLACEMENT_PASS` is valid only when a later PASS exists in the same contiguous bounded lineage; original non-pass attempts remain retained and the replacement is recorded in satisfaction.

Unknown rule/class, input-binding mismatch, lineage gap/cycle/duplicate, retry beyond max, or ineligible transition invalidates the evidence set.

### 7.3 Alternative-check aggregation: mandatory checks are never voteable

```yaml
CheckAggregationRuleV1:
  mode: CheckAggregationMode
  alternative_evidence_kinds: [stable_type]
  alternative_execution_surfaces: [stable_type]
  quorum_required: null | positive_uint
  registered_rule: null | RuleInvocationV1
```

Aggregation is evaluated **only after every MANDATORY check is satisfied** (directly, by an accepted retry replacement, or by an exact substitution). It has no authority over MANDATORY failures.

- `ALL_MANDATORY_ONLY`: alternative lists empty; quorum null; no alternative gate.
- `ANY_ALTERNATIVE`: alternative kind/surface lists nonempty; at least one ALTERNATIVE check matching the normative lists must pass. Mandatory checks still all pass. Alternative failures remain retained but do not veto the successful alternative.
- `QUORUM_ALTERNATIVE`: normative alternative lists nonempty; quorum is positive and <= number of planned ALTERNATIVE checks; at least quorum alternatives pass after all mandatory checks pass.
- `REGISTERED_VERSIONED`: valid CHECK_AGGREGATION invocation required and may evaluate only ALTERNATIVE checks declared by the exact requirement. It cannot ignore or reinterpret any MANDATORY non-pass.

A compiler may not inject an easier alternative kind/surface not declared by the exact requirement.

### 7.4 `SubstitutionRuleV1`

```yaml
SubstitutionRuleV1:
  rule_id: stable_id
  from_evidence_kind: stable_type
  replacement_evidence_kind: stable_type
  eligibility_predicate: PredicateV1
```

A substitution is valid only when the original deficient MANDATORY evidence matches `from_evidence_kind`; a REPLACEMENT check of the declared replacement kind exists in the same exact plan; predicate TRUE; replacement envelope/artifact IDs are recorded; and replacement evidence independently passes result/freshness/artifact/trust/effective-risk constraints. FALSE/ERROR means no substitution. History remains retained.

### 7.5 `EvidenceRequirement`

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
  freshness_rule: null | RuleInvocationV1
```

Contract/key/claim/capability IDs exactly match the producing `TaskClaimContract`. The four risk-derived fields equal or exceed `EffectiveRiskConstraint`; downgrade is invalid. Freshness invocation, when present, is class FRESHNESS; STALE/ERROR prevents acceptance. `allowed_result_classes` are classes permitted to contribute passing empirical evidence; disallowed observations remain history but cannot contribute to SATISFIED. QUARANTINED is never directly acceptable even if listed by mistake.

### 7.6 `CheckPlan`

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
      role: CheckRole
      evidence_kind: stable_type
      execution_surface: stable_type
      scenario_or_fixture_ref: ImmutableRefV1
      evaluator_requirement_identity: null | IdentityRef
  compile_trace_identity: IdentityRef
```

Applicability ERROR emits no plan. MANDATORY checks exactly cover the requirement's required evidence kinds/surfaces. ALTERNATIVE checks are allowed only for the exact aggregation-declared alternative kinds/surfaces. REPLACEMENT checks are allowed only for exact substitution rules. Check IDs are unique. Accepted MANDATORY/ALTERNATIVE evidence plus applied REPLACEMENT evidence must meet the distinct-surface floor; no role can silently weaken protection/review requirements.

### 7.7 `ArtifactIdentity`

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

Hash proves identity, not availability. MISSING/CORRUPT and QUARANTINED cannot directly satisfy. Other rights states satisfy only when explicitly allowed by the exact requirement. Deficient mandatory evidence needs an exact valid replacement path.

### 7.8 `ExecutionEvidenceEnvelope`

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

Capability-state ID exactly matches requirement/plan. `failure_class` is required exactly for FAIL. Attempts are append-only. Any envelope for a NOT_APPLICABLE plan is invalid.

## 8. `EvidenceSatisfaction` — sole empirical acceptance authority

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
  accepted_retry_replacements:
    - original_attempt_id: stable_id
      replacement_attempt_id: stable_id
      policy_mode: AttemptPolicyMode
      registered_invocation_identity: null | IdentityRef
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
  missing_mandatory_check_ids: [stable_id]
  invalid_or_quarantined_artifact_ids: [IdentityRef]
  derivation_trace_identity: IdentityRef
```

Exactly one of substitution `original_check_id` / `original_artifact_id` is non-null. Retry replacements bind a prior non-pass attempt to a later PASS in the same valid lineage; they never remove the prior attempt.

Deterministic derivation order:

1. validate all closed schemas and exact contract/requirement/risk/plan/capability/candidate/base/policy identities;
2. re-evaluate applicability: ERROR -> no satisfaction; FALSE -> NOT_APPLICABLE, trust NOT_EVALUATED, zero surfaces, protected=false;
3. validate exact MANDATORY/ALTERNATIVE/REPLACEMENT plan roles against requirement, aggregation, and substitution declarations; validate risk/protection/review propagation;
4. validate attempts, lineage/max, retry eligibility, registered rule classes/identities, and every exact `RuleInvocationV1` binding; malformed/under/over-bound input -> no satisfaction;
5. derive per-check attempt outcomes. Any observation used as passing evidence must be in `allowed_result_classes`; disallowed observations remain retained history;
6. record every accepted retry replacement explicitly. A prior MANDATORY non-pass is discharged by retry only if the exact versioned attempt policy validly accepts a later PASS as replacement evidence;
7. evaluate exact freshness invocation using only bound immutable inputs; STALE/ERROR -> INCONCLUSIVE;
8. validate artifacts: integrity PRESENT, rights allowed, never QUARANTINED, exact identity/provenance. A deficient MANDATORY artifact is non-satisfying unless exact substitution independently passes all constraints;
9. resolve MANDATORY checks before aggregation: unresolved FAIL -> UNSATISFIED; unresolved FLAKY/INCONCLUSIVE/NOT_RUN/missing -> INCONCLUSIVE. A MANDATORY non-pass may be discharged only by an accepted retry replacement or exact substitution recorded above;
10. only after all MANDATORY checks are satisfied, apply alternative aggregation. `ALL_MANDATORY_ONLY` needs none; ANY/QUORUM evaluate only declared ALTERNATIVE checks; registered aggregation cannot override a mandatory result;
11. if protection is required, accepted required/replacement evidence includes PROTECTED artifact; else INCONCLUSIVE/PROTECTED_EVIDENCE_FLOOR_UNMET;
12. compute distinct accepted execution surfaces; below floor -> INCONCLUSIVE/SURFACE_FLOOR_UNMET;
13. derive trust using `TrustDerivationV1`; NOT_EVALUATED or below minimum -> INCONCLUSIVE/TRUST_FLOOR_UNMET;
14. SATISFIED only when every MANDATORY obligation is satisfied or exactly replaced, the normative alternative gate (if any) passes, and all result/freshness/artifact/risk/trust constraints pass.

No directive, task contract, envelope, review, issue/PR status, score, or ledger object can independently create empirical SATISFIED.

## 9. Review, promotion, and deterministic readiness

Review/verification may validate derivation, identify missing/biased/stale requirements, reject reasoning, or require new policy. It cannot overwrite empirical results or directly set SATISFIED.

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

Promotion requires exact current SATISFIED refs plus a qualifying record whose route rank >= required route, independence mode is allowed by that route, route-required artifact kinds are present in the immutable record package, and disposition is allowed by the governing task contract. Missing/unknown/weak record -> blocked.

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

RESOLVED is compiler-only: every exact/current required satisfaction is SATISFIED and every mandatory review/verification ref meets route/independence requirements. OPEN is default for missing/stale/mismatch/inconclusive/insufficient trust/route. SUPERSEDED requires traced replacement. Policy changes emit a new ledger; historical ledger objects remain immutable. Manual edits/scalar scores have no authority. Any OPEN blocker that blocks `PRODUCTION_IMPLEMENTATION` keeps that scope blocked.

`IR-BLOCKER-EVIDENCE-FOUNDATION` remains OPEN.

## 10. One-way compiler pipeline and cases

```text
durable directives + exact capability evidence + immutable registries
  -> ActiveDirectiveSet + ResourceCapabilityState
  -> PolicyEpoch + RuleRegistry + ReviewRouteRegistry
  -> TaskClaimContract
  -> applicable RiskFloor set -> EffectiveRiskConstraint
  -> EvidenceRequirement
  -> CheckPlan(exact candidate/head/base/capability; typed check roles)
  -> append-only ExecutionEvidenceEnvelope attempts + ArtifactIdentity
  -> exact retry replacements + substitutions + freshness
  -> mandatory-check gate
  -> alternative-only aggregation
  -> EvidenceSatisfaction
  -> mandatory review/verification PromotionGateInput
  -> decision transition + ImplementationReadinessLedger
```

Fail closed on unknown type/field/rule/route, unresolved identity, rule-input mismatch, predicate ERROR, stale freshness, artifact deficiency, invalid policy transition, mandatory non-pass without exact replacement, or risk-floor downgrade.

| Case | Required result |
|---|---|
| owner says “continue existing leases” | ownership may continue; capability/trust unchanged |
| owner says “treat failed spike as PASS” | invalid empirical override; observation remains FAIL |
| legitimate requirement removal | new directive + PolicyEpoch + requirement identity; history unchanged |
| emergency safety stop | halt applicable work; do not rewrite observations |
| stricter review directive | new/effective route may increase; old weaker promotion becomes insufficient |
| DEGRADED evidence, minimum DEGRADED | may satisfy if all other constraints pass; trust debt remains |
| DEGRADED evidence, minimum FULL | INCONCLUSIVE/TRUST_FLOOR_UNMET |
| no evaluable evidence | NOT_EVALUATED; required claim cannot satisfy |

## 11. Validator fixtures

| ID | Fixture | Expected |
|---|---|---|
| V01 | mandatory PASS, intact allowed-rights evidence, enough surfaces/protection/trust | SATISFIED |
| V02 | mandatory NOT_RUN | INCONCLUSIVE/MISSING_REQUIRED_EXECUTION |
| V03 | applicability predicate FALSE | NOT_APPLICABLE + NOT_EVALUATED |
| V04 | predicate missing input/type mismatch | ERROR; no plan/satisfaction |
| V05 | unknown predicate operator/unbound alias | invalid schema |
| V06 | FAIL then PASS under ALL_ATTEMPTS_MUST_PASS | UNSATISFIED |
| V07 | retryable INFRA FAIL then PASS under valid LATEST policy | may satisfy check; both attempts retained + replacement recorded |
| V08 | PRODUCT/non-retryable FAIL then PASS under LATEST policy | UNSATISFIED |
| V09 | FLAKY then PASS under built-in LATEST | INCONCLUSIVE; no built-in retry replacement |
| V10 | lineage gap/cycle/duplicate/over max | invalid evidence set |
| V11 | registered rule absent/wrong class/identity | invalid/no authority |
| V12 | registry sets any `may_*` true | invalid registry |
| V13 | registered invocation omits/adds/duplicates/wrong-types a binding | invalid invocation |
| V14 | candidate/capability ID differs from plan/requirement | invalid; no satisfaction |
| V15 | artifact MISSING/CORRUPT | non-satisfying absent exact replacement |
| V16 | directive attempts FAIL->PASS | reject override; observation unchanged |
| V17 | new PolicyEpoch changes requirement | new identities; history unchanged |
| V18 | DEGRADED evidence, minimum FULL | INCONCLUSIVE/TRUST_FLOOR_UNMET |
| V19 | envelope claims FULL but capability lacks isolation/FULL separation | achieved trust DEGRADED |
| V20 | no evaluable evidence | NOT_EVALUATED; cannot satisfy |
| V21 | protected floor but accepted evidence all NORMAL | INCONCLUSIVE/PROTECTED_EVIDENCE_FLOOR_UNMET |
| V22 | floor needs 2 surfaces, accepted evidence has 1 | INCONCLUSIVE/SURFACE_FLOOR_UNMET |
| V23 | producer lowers FULL->DEGRADED | invalid requirement compilation |
| V24 | producer lowers protection/surface floor | invalid requirement compilation |
| V25 | producer supplies weaker review route | invalid requirement compilation |
| V26 | promotion record route weak or independence mode disallowed | promotion/readiness blocked |
| V27 | PASS observation absent from allowed_result_classes | cannot contribute to SATISFIED |
| V28 | artifact rights not allowed or QUARANTINED | non-satisfying absent exact substitution |
| V29 | substitution predicate ERROR | no substitution |
| V30 | replacement check absent/wrong role/kind | substitution invalid |
| V31 | replacement evidence below result/freshness/artifact/trust/risk constraint | substitution cannot satisfy |
| V32 | freshness STALE/ERROR | INCONCLUSIVE |
| V33 | ANY_ALTERNATIVE: one MANDATORY FAIL + one ALTERNATIVE PASS | UNSATISFIED; mandatory failure cannot be outvoted |
| V34 | QUORUM_ALTERNATIVE: mandatory checks pass, quorum alternatives pass, another alternative FAIL | may SATISFY; failed alternative retained because it was not mandatory |
| V35 | compiler injects undeclared easy alternative kind/surface | invalid plan |
| V36 | registered aggregation attempts to ignore MANDATORY non-pass | invalid/non-satisfying |
| V37 | ledger SATISFIED evidence but required review missing/weak | blocker OPEN |
| V38 | ledger manually edited RESOLVED | invalid; recompute |
| V39 | unknown object field/enum/rule/route | invalid; fail closed |
| V40 | duplicate claim/requirement key or zero risk floors | invalid TaskClaimContract |
| V41 | substitution has both/neither original check/artifact IDs | invalid satisfaction object |
| V42 | RiskFloor applicability predicate ERROR | no effective constraint/requirement compilation |
| V43 | retry replacement record points outside exact contiguous lineage or to non-PASS replacement | invalid satisfaction object |

## 12. Observability and failure controls

Every stage emits immutable input IDs, policy epoch, exact candidate/head/base/capability, predicate results, check roles, missing mandatory checks, attempt lineage/failure classes, accepted retry replacements, rule/invocation identities, substitutions, freshness, artifact integrity/rights/visibility, achieved-vs-required surfaces/protection/trust, review route/independence, and reason codes. Protected payloads may be redacted; authority-relevant availability/corruption cannot be hidden.

Controls: closed predicates prevent evaluator ambiguity; exact rule invocations prevent extension-input ambiguity; new epochs prevent policy laundering; append-only attempts + explicit retry-replacement records prevent retry laundering; MANDATORY/ALTERNATIVE/REPLACEMENT roles prevent aggregation laundering; exact planned substitutions prevent artifact laundering; capability-bound trust prevents lease/label laundering; `EffectiveRiskConstraint` closes trust/protection/surfaces/review route; exact promotion records and compiled ledger prevent readiness laundering.

## 13. Interfaces, open questions, and reopen conditions

Primary consumers: `W2-ENG-03`, `W2-SIM-01`, and mandatory independent `W2-REV-01`. `W2-CI-01`, `W2-PROTECT-01`, `W2-EVAL-01`, and `W2-HASH-01` should emit compatible evidence/identities without authority to weaken this chain.

Delegated concrete decisions:

- serialization/hash selection and cross-runtime conformance -> `W2-HASH-01`;
- protected storage/access mechanics -> `W2-PROTECT-01`;
- CI execution/retention mechanics -> `W2-CI-01`;
- evaluator calibration/fingerprint mechanics -> `W2-EVAL-01`;
- engine/platform/product scope -> declared evidence/review missions.

Reopen if conforming predicate/rule evaluators can disagree on identical bound inputs; any undefined authority field/input exists; a mandatory non-pass can be outvoted rather than exactly replaced; retry/substitution can erase history; a producer lowers any risk dimension; disallowed result/artifact reaches SATISFIED; lease continuation upgrades independence; weak review resolves promotion/readiness; or readiness resolves without exact satisfaction plus mandatory review/verification.

## 14. Review Index

1. **Closure:** Sections 3–4 define primitives, immutable refs, exact rule registry/invocations, and predicate error behavior; V04–V05/V11–V13/V39 attack escapes.
2. **Required-failure invariant:** Sections 7.2–7.3 and 8 separate explicit replacement from alternative aggregation; V06–V09/V33–V36/V43 attack retry/aggregation laundering.
3. **Substitution/freshness:** Sections 7.4–8 require planned replacement evidence and exact freshness invocation; V28–V32/V41 attack ambiguity.
4. **All RiskFloor dimensions:** Section 6 compiles trust/protection/surfaces/review route; V21–V26/V42 attack downgrade/applicability paths.
5. **Single empirical authority:** only Section 8 creates SATISFIED; downstream review/readiness consume but cannot rewrite it.
6. **Trust absence/capability:** Section 5.2 defines deterministic NOT_EVALUATED/DEGRADED/FULL; V18–V20 attack trust laundering.
7. **Allowed results/artifacts:** requirement + satisfaction explicitly gate passing evidence; V27–V28 attack bypass.
8. **Current state:** lease continuation leaves degraded trust unchanged; evidence-foundation blocker remains OPEN; no production implementation authorized.

Suggested `W2-REV-01` attacks: registered-rule input substitution; mandatory FAIL hidden behind ANY/QUORUM; fake retry replacement outside lineage; substitution without planned replacement; risk/review-route downgrade; false FULL trust from weak capability; or readiness resolution with weak/missing review evidence.