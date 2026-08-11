# W2-AUTH-01 Author Self-Review Finding Dispositions

**Remediation mission:** `W2-REM-AUTH-01` / Issue #87  
**Source candidate work:** `4f2baf8f97a531ac38491343098ac10c81c12a6b`  
**Source finding comment:** Issue #69 comment `5251524689`  
**Authority:** remediation evidence only; does not replace independent `W2-REV-01`.

## Source finding dispositions

### SR-M01 — MAJOR — machine shapes not closed

**CORRECTED.** The remediated contract defines `PrimitiveRegistryV1`, closed enums, `IdentityRef`, `ImmutableRefV1`, `RuleRegistry`, `RuleInvocationV1`, and a closed `PredicateV1` AST with exact bindings, typed operators, `TRUE|FALSE|ERROR`, and fail-closed context semantics. Unknown fields/operators/rules or under/over-bound registered-rule invocations are invalid.

Evidence: contract Sections 2–4; fixtures V04–V05, V11–V12, V35, V39.

### SR-M02 — MAJOR — retry/attempt policy not representable

**CORRECTED.** `AttemptPolicyV1` is separate from `CheckAggregationRuleV1`. Built-in modes define all-attempts and latest-after-retryable-failure semantics with contiguous lineage, max attempts, retryable failure classes, retry predicates, and explicit behavior for PRODUCT/INFRA/FLAKY/INCONCLUSIVE/NOT_RUN. Registered rules use exact typed invocations with immutable input bindings and cannot weaken lineage/risk/result constraints.

Evidence: contract Section 7.2 and Section 7.8; fixtures V06–V12, V32, V39.

### SR-M03 — MAJOR — RiskFloor only partially enforced

**CORRECTED.** `RiskFloor` has deterministic applicability and `EffectiveRiskConstraint` compiles every dimension: strictest trust, OR protection, maximum distinct surfaces, and greatest review-route rank. Requirement/plan/satisfaction/promotion/readiness carry these constraints; producer downgrade invalidates compilation.

Evidence: contract Section 6, Sections 7.4–8; fixtures V20–V25, V33, V38.

### SR-m01 — MINOR — trust cannot represent not evaluated

**CORRECTED.** Normative `TrustLevel` is distinct from `TrustAssessment=[NOT_EVALUATED,DEGRADED,FULL]`. `TrustDerivationV1` is capability-bound and defines when FULL is possible. No evaluable evidence yields NOT_EVALUATED, which cannot satisfy a required claim.

Evidence: contract Sections 2.2 and 5.3; fixtures V17–V19.

### SR-m02 — MINOR — allowed result classes implicit

**CORRECTED.** Satisfaction derivation explicitly requires every observation used as a passing empirical input to be in `allowed_result_classes`; disallowed observations remain retained history but cannot contribute to SATISFIED. Aggregation cannot bypass the check.

Evidence: contract Sections 7.4 and 7.8; fixtures V26 and V32.

## Additional pre-terminal closure corrections

The remediation author-side attacks also closed these defects instead of deferring them:

- defined the rule registry itself, including class/output/conformance semantics;
- added `RuleInvocationV1` so retry/aggregation/freshness evaluators are bound to one exact rule plus one exact ordered immutable input map; missing/extra/duplicate/wrong-type inputs fail closed;
- replaced vague immutable references with `ImmutableRefV1`;
- made substitution evidence explicit in the same plan and satisfaction object;
- made freshness a typed registered invocation with immutable inputs and fail-closed STALE/ERROR behavior;
- closed independence mode as an enum and made FULL trust capability-derived;
- fixed substitution original-object typing;
- added deterministic RiskFloor applicability; predicate ERROR blocks compilation;
- removed producer/output identity cycles from `TaskClaimContract` by using a unique `requirement_key` and deriving downstream objects one-way.

## Preservation checks

- `EvidenceSatisfaction` remains sole empirical acceptance authority.
- Directives cannot rewrite observations.
- Lease continuation does not upgrade capability/trust.
- `DEGRADED_SINGLE_AGENT` remains degraded trust debt.
- `IR-BLOCKER-EVIDENCE-FOUNDATION` remains OPEN.
- `W2-HASH-01` retains algorithm/encoding selection authority.
- `W2-REV-01` remains mandatory independent adversarial review.
- Production implementation remains unauthorized.

## Required second self-review

Re-attack every source finding plus the additional closure corrections above. A clean remediation authoring pass requires zero unresolved BLOCKER/MAJOR in Issue #87 scope and a Review Index <=4000 UTF-8 chars.