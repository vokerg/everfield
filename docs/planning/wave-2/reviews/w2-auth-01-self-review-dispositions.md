# W2-AUTH-01 Author Self-Review Finding Dispositions

**Remediation mission:** `W2-REM-AUTH-01` / Issue #87  
**Source candidate work:** `4f2baf8f97a531ac38491343098ac10c81c12a6b`  
**Source finding comment:** Issue #69 comment `5251524689`  
**Authority:** remediation evidence only; does not replace independent `W2-REV-01`.

## Source finding dispositions

### SR-M01 — MAJOR — machine shapes not closed

**CORRECTED.** The remediated contract defines a primitive registry, closed enums, exact identity/immutable-reference shapes, `RuleRegistry`, `RuleInvocationV1`, and a closed `PredicateV1` AST with exact bindings and fail-closed errors. Unknown fields/operators/rules or under/over-bound registered-rule invocations are invalid.

Evidence: contract Sections 3–4; fixtures V04–V05, V11–V13, V39.

### SR-M02 — MAJOR — retry/attempt policy not representable

**CORRECTED.** `AttemptPolicyV1` is separate from alternative-check aggregation. Retry semantics are contiguous, bounded, class/predicate-gated, append-only, and any accepted later PASS is recorded as explicit replacement evidence. A mandatory failure can never be hidden by aggregation.

Evidence: contract Sections 7.2–7.3 and 8; fixtures V06–V09, V33–V36, V43.

### SR-M03 — MAJOR — RiskFloor only partially enforced

**CORRECTED.** `EffectiveRiskConstraint` deterministically compiles strictest trust, OR protection, maximum distinct surfaces, and greatest review-route rank. Requirement/plan/satisfaction/promotion/readiness carry these constraints; producer downgrade invalidates compilation.

Evidence: contract Section 6 and Sections 7–9; fixtures V21–V26, V37, V42.

### SR-m01 — MINOR — trust cannot represent not evaluated

**CORRECTED.** Normative `TrustLevel` is distinct from `TrustAssessment=[NOT_EVALUATED,DEGRADED,FULL]`; capability-bound derivation defines when FULL is possible. No evaluable evidence yields NOT_EVALUATED and cannot satisfy a required claim.

Evidence: contract Section 5.2; fixtures V18–V20.

### SR-m02 — MINOR — allowed result classes implicit

**CORRECTED.** Every observation used as passing empirical evidence must be in `allowed_result_classes`; disallowed observations remain retained history but cannot contribute to SATISFIED. Neither retry nor aggregation can bypass the check.

Evidence: contract Sections 7.5 and 8; fixtures V27 and V36.

## Additional pre-terminal closure corrections

Author-side adversarial passes also closed defects discovered while repairing the source findings:

- `RuleInvocationV1` binds every retry/aggregation/freshness evaluator to one exact ordered immutable input map; missing/extra/duplicate/wrong-type inputs fail closed.
- Check roles are a closed enum `MANDATORY | ALTERNATIVE | REPLACEMENT`, eliminating ambiguous boolean combinations.
- ANY/QUORUM aggregation applies only to explicitly declared ALTERNATIVE checks after every MANDATORY check has passed or been exactly replaced; a mandatory FAIL/FLAKY/INCONCLUSIVE/NOT_RUN cannot be outvoted.
- Accepted retry PASSes are explicit replacement evidence recorded in `EvidenceSatisfaction`; prior attempts remain append-only history.
- Substitution evidence is explicit in the same plan and satisfaction object.
- Freshness is a typed registered invocation with immutable inputs and fail-closed STALE/ERROR behavior.
- Independence mode is closed and FULL trust is capability-derived.
- RiskFloor applicability is deterministic; predicate ERROR blocks compilation.
- Producer/output identity cycles were removed from `TaskClaimContract` via a unique `requirement_key` and one-way downstream derivation.

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

Re-attack every source finding plus all additional closure corrections above. A clean remediation authoring pass requires zero unresolved BLOCKER/MAJOR in Issue #87 scope and a Review Index <=4000 UTF-8 chars.