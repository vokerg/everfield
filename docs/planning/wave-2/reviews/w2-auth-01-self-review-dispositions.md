# W2-AUTH-01 Author Self-Review Finding Dispositions

**Remediation mission:** `W2-REM-AUTH-01` / Issue #87  
**Source candidate work:** `4f2baf8f97a531ac38491343098ac10c81c12a6b`  
**Source finding comment:** Issue #69 comment `5251524689`  
**Authority:** remediation evidence only; does not replace `W2-REV-01`.

## Dispositions

### SR-M01 — MAJOR — machine shapes not closed

**Disposition: CORRECTED.**

The remediated contract adds `PrimitiveRegistryV1`, removes undefined `scalar`/`predicate`/`stable_ref` placeholders, defines all closed enums, adds `IdentityRef` and `VersionedRuleRef`, and specifies `PredicateV1` as a closed AST with exact input bindings, typed literals, fixed operators, `TRUE|FALSE|ERROR` result domain, and context-specific fail-closed error behavior. Unknown fields/operators/rules are invalid.

Mechanical evidence: contract Sections 3–4; fixtures V04, V05, V10, V25, V28.

### SR-M02 — MAJOR — retry/attempt policy not representable

**Disposition: CORRECTED.**

The remediated contract separates `AttemptPolicyV1` from `CheckAggregationRuleV1`. Built-in attempt modes explicitly define `ALL_ATTEMPTS_MUST_PASS` and `LATEST_AFTER_RETRYABLE_FAILURE`, including contiguous lineage, max attempts, retryable failure classes, retry predicates, and failure-laundering behavior. Registered extension rules are exact `VersionedRuleRef` objects and fail closed when absent/mismatched.

Mechanical evidence: contract Sections 6.2 and 6.7; fixtures V06–V10 and V30.

### SR-M03 — MAJOR — RiskFloor partially enforced

**Disposition: CORRECTED.**

The remediated contract introduces `ReviewRouteRegistry` with a deterministic unique strictness rank and `EffectiveRiskConstraint`, compiled from every applicable floor. Trust uses strictest value, protection uses OR, distinct surfaces use max, and review route uses greatest unique rank. The effective constraint is referenced by claim, requirement, plan, satisfaction, promotion, and readiness; requirement/plan downgrade attempts are invalid.

Mechanical evidence: contract Sections 5.4–5.6, 6.3–6.7, 7; fixtures V18–V22, V26, V30.

### SR-m01 — MINOR — trust cannot represent not evaluated

**Disposition: CORRECTED.**

`TrustAssessment` is now `[NOT_EVALUATED, DEGRADED, FULL]`, distinct from normative `TrustLevel`. NOT_APPLICABLE and evidence-absent derivations use `NOT_EVALUATED`, which never satisfies a minimum trust floor.

Mechanical evidence: contract Sections 3.2, 6.7, 10; fixtures V03 and V17.

### SR-m02 — MINOR — allowed result classes only implicit

**Disposition: CORRECTED.**

The satisfaction derivation now has an explicit pre-aggregation step requiring every consumed envelope result to be in `allowed_result_classes`; disallowed results invalidate the evidence set and cannot be rescued by retry/check aggregation.

Mechanical evidence: contract Section 6.7 step 5; fixtures V23 and V30.

## Preservation checks

- `EvidenceSatisfaction` remains the sole empirical acceptance authority.
- Directives still cannot rewrite empirical observations.
- Current lease continuation does not upgrade isolation/independence/trust.
- `DEGRADED_SINGLE_AGENT` remains degraded trust debt.
- `IR-BLOCKER-EVIDENCE-FOUNDATION` remains OPEN.
- `W2-HASH-01` retains concrete canonical serialization/hash selection.
- `W2-REV-01` remains the required independent adversarial review.
- Production implementation remains unauthorized.

## Self-review target

A clean remediation self-review requires zero unresolved BLOCKER/MAJOR against Issue #87 scope, explicit re-attack of all five source findings, and no new authority path introduced by the repairs.