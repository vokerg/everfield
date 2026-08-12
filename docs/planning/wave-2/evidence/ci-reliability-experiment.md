# W2-CI-01 — CheckPlan, flake, quarantine, retention, and CI reliability experiment

**Mission:** `W2-CI-01`  
**Issue:** #77  
**Branch:** `planning/issue-77`  
**Claim:** Issue #77 comment `5264276879`  
**Base main:** `c7ba185ed9667b717794c19eaa0834ca41aa4c78`  
**Authoritative foundation:** `docs/planning/WAVE-1-FOUNDATIONS-v1.md` blob `a252e3c93702f3ebaecd3e888944a23dbe1b0e1d`  
**Task class / decision state:** `PLANNING_EXPERIMENT / EVIDENCE_REQUIRED`  
**Producer result:** `BOUNDED_PASS` for the experiment-local CI semantics only; required independent review remains `W2-REV-01`.

## 1. Scope and non-goals

This bounded planning experiment exercises the Wave 1 acceptance chain:

`EvidenceRequirement -> CheckPlan -> ExecutionEvidenceEnvelope attempts/artifacts -> EvidenceSatisfaction`

It specifically tests:

- `REQUIRED`, `CONDITIONALLY_REQUIRED`, `OPTIONAL`, and `NOT_APPLICABLE` applicability;
- the semantic distinction between `NOT_APPLICABLE` and required `NOT_RUN`;
- retained retry lineage for product failures, infrastructure failures, and flakes;
- temporary quarantine with explicit replacement evidence and expiry;
- retention loss, exact restoration, and hash-mismatched restoration;
- aggregate `EvidenceSatisfaction` over the exact synthetic candidate/base.

Non-goals:

- choosing or validating a specific CI provider, runner topology, workflow syntax, or GitHub Actions feature;
- defining production CI architecture;
- claiming that infrastructure/product failure classification is solved generally;
- authorizing implementation readiness or closing `IR-BLOCKER-EVIDENCE-FOUNDATION`;
- replacing `W2-REV-01`.

## 2. Constraints and authoritative basis

The canonical Wave 1 foundation requires:

1. `CheckPlan` is compiled before execution and cannot weaken `EvidenceRequirement`.
2. Applicability uses `REQUIRED`, `OPTIONAL`, `CONDITIONALLY_REQUIRED`, `NOT_APPLICABLE`.
3. `NOT_RUN` is distinct from `NOT_APPLICABLE`.
4. Required `FAIL`, `FLAKY`, `INCONCLUSIVE`, or `NOT_RUN` cannot yield SATISFIED unless a versioned requirement explicitly provides valid replacement evidence.
5. Retry lineage is retained.
6. Quarantine temporarily changes an explicit requirement with owner/remediation/expiry/replacement evidence; it does not relabel failure PASS.
7. Artifact content hash proves identity, not availability; unavailable/corrupt retained evidence reopens authority.

No external provider documentation was loaded because Issue #77 declares only the Wave 1 foundation as authoritative input and provider mechanics are explicitly outside this experiment's acceptance scope.

## 3. Synthetic requirement and CheckPlan

The experiment uses one fixed synthetic requirement packet, `CI-EXP-REQ-v1`, bound to:

- exact base: `c7ba185ed9667b717794c19eaa0834ca41aa4c78`;
- synthetic policy epoch: `ci-reliability-exp-v1`;
- fixture digest: `sha256:b382dc1b0c7b7b93b111328c1a4fdc95b492d4713117fcec2e4801904440c0ae`;
- reference harness digest: `sha256:879ec2a11549b609ad001efb1ba810c096ee0b3077bda19ed711dc1ce6a0748c`;
- execution environment: Python `3.13.5`, Linux `6.18.35-x86_64`, glibc `2.41`.

| Check | Applicability | Predicate | Artifact required | Infra retry allowed |
|---|---|---|---:|---:|
| `unit` | REQUIRED | — | yes | yes |
| `package` | CONDITIONALLY_REQUIRED | `package_changed == true` | yes | yes |
| `docs` | OPTIONAL | — | no | yes |
| `console-cert` | NOT_APPLICABLE | — | no | no |
| `soak` | REQUIRED | — | yes | yes |

Synthetic retained artifact identities:

- `unit`: `21635bf469d152cfeed09f0299922ed71eb46d237ffa5cadaee2ce86b05fd710`
- `soak`: `3b085dd76e6f4e42da74221f1e9feb07c8aeb5bbe5dac446fa6529b0121c60f1`
- `package`: `ee3f318a22cd8d4d0ba985174f8ff4651764f664e00b8ecf4c6dcf3e15e03b0d`
- quarantine replacement `short_soak`: `00dc1f37cb5bcbe74c0fad11abdd74be1a3de44e12aec66cfb4d696df98ec73f`
- quarantine replacement `static_invariant`: `89d66dbfbd33ab7e833d77b7cb65636657c09baf5eb8bcffc91d1cc1c01760d7`

These hashes are fixture identities only, not project production artifacts.

## 4. Result semantics used by the reference evaluator

The evaluator implements only the bounded semantics needed for this experiment:

1. `NOT_APPLICABLE` is non-gating.
2. An unexecuted OPTIONAL check is recorded `NOT_RUN` but does not gate aggregate satisfaction.
3. A conditional check whose predicate resolves true becomes REQUIRED; if not executed it gates as `NOT_RUN`.
4. A PRODUCT-class `FAIL` on the exact candidate remains failing even if a later same-candidate attempt passes. The later pass cannot launder the retained product failure.
5. INFRA-class failures may be replaced by a later PASS only when the requirement explicitly permits infrastructure retry; every failed attempt remains in lineage.
6. Any explicit `FLAKY` or unexplained divergent PASS/FAIL on the exact candidate remains unsatisfied.
7. An active quarantine may satisfy the requirement only via an explicit versioned replacement set. The original failure remains visible.
8. Quarantine expiry removes the temporary substitution automatically.
9. Required PASS evidence becomes `INCONCLUSIVE` if its retained artifact is unreachable or restored under the wrong content hash.
10. Exact reachability + hash restoration may restore satisfaction because the historical execution result was not rewritten.

These are experiment-local operationalizations of the Wave 1 foundation, not a new canonical schema.

## 5. Executed scenarios

The exact reference harness was executed against 11 scenarios. Canonical result-object digest:

`sha256:57628e3bc66d694367f99ba035f70884ad729cb1a8a74c9bcdf228b09e693263`

| ID | Injection / condition | Key effective result | Aggregate |
|---|---|---|---|
| S1 | package predicate false; optional docs not run | `package=NOT_APPLICABLE`, `docs=NOT_RUN`, required checks PASS | `SATISFIED` |
| S2 | package predicate true but package check absent | `package=NOT_RUN` | `UNSATISFIED` |
| S3 | `unit`: PRODUCT FAIL then PASS on same candidate | retained `unit=FAIL` | `UNSATISFIED` |
| S4 | `unit`: INFRA FAIL, INFRA FAIL, then PASS | retry lineage retained; valid infra replacement | `SATISFIED` |
| S5 | `soak`: FLAKY then PASS | retained `soak=FLAKY` | `UNSATISFIED` |
| S6 | active quarantine at day 7; both declared replacements PASS | `soak=PASS_BY_REPLACEMENT`; original FLAKY retained | `SATISFIED` |
| S7 | same quarantine at day 15, expiry day 14 | `soak=NOT_RUN` after expiry | `UNSATISFIED` |
| S8 | remediated candidate state; normal `soak` PASS | required checks PASS | `SATISFIED` |
| S9 | `unit` PASS artifact becomes unreachable | `unit=INCONCLUSIVE` | `INCONCLUSIVE` |
| S10 | exact `unit` artifact restored at expected hash | `unit=PASS` | `SATISFIED` |
| S11 | reachable restoration at wrong hash | `unit=INCONCLUSIVE` | `INCONCLUSIVE` |

## 6. Applicability truth table

| Declared applicability | Runtime predicate | Executed? | Effective state | Gates aggregate? |
|---|---|---:|---|---:|
| REQUIRED | — | no | `NOT_RUN` | yes |
| REQUIRED | — | PASS | `PASS` | yes |
| CONDITIONALLY_REQUIRED | false | no | `NOT_APPLICABLE` | no |
| CONDITIONALLY_REQUIRED | true | no | `NOT_RUN` | yes |
| OPTIONAL | — | no | `NOT_RUN` | no |
| NOT_APPLICABLE | — | no | `NOT_APPLICABLE` | no |

The important invariant is that absence of execution never converts a required check into `NOT_APPLICABLE`.

## 7. Retry lineage findings

### 7.1 Product failure

S3 retains the original PRODUCT failure as authoritative negative evidence for the exact candidate. A later PASS is additional evidence, not a rewrite. Aggregate satisfaction remains `UNSATISFIED`.

A product repair should therefore produce a new exact candidate identity and new CheckPlan/evidence episode rather than claiming the old candidate was always passing.

### 7.2 Infrastructure failure

S4 distinguishes infrastructure unavailability from product behavior. Two INFRA failures remain in lineage; the third PASS may satisfy the requirement only because the synthetic requirement explicitly permits infra retry.

This does not establish a universal classifier. A real system must retain evidence for why an attempt was classified INFRA rather than PRODUCT. Misclassification is a major laundering risk.

### 7.3 Flake

S5 demonstrates that repeated execution cannot average or vote a flake into PASS. The exact candidate remains unsatisfied until a valid versioned requirement provides replacement evidence or a remediated candidate removes the flake.

## 8. Quarantine lifecycle

The synthetic `soak` quarantine is represented as a new temporary requirement version with:

- original result: `FLAKY`;
- bounded owner: the W2-CI-01 fixture episode;
- remediation obligation: restore normal soak reliability;
- expiry: day 14;
- replacements: both `short_soak` and `static_invariant` must PASS;
- no authority to relabel the historical FLAKY result.

Observed lifecycle:

1. Day 0: original soak is FLAKY -> `UNSATISFIED`.
2. Day 7: quarantine active and both replacements PASS -> aggregate `SATISFIED`, but only under the temporary requirement version; the original flake remains visible.
3. Day 15: quarantine expired -> replacement authority disappears -> `UNSATISFIED`.
4. Remediated candidate: normal soak PASS under the non-quarantined requirement -> `SATISFIED`.

Recommendation for downstream design: quarantine must be modeled as a first-class, expiring policy/evidence substitution, never as a label applied to a failed attempt.

## 9. Retention loss and restoration

S9-S11 exercise the Wave 1 rule that content hash proves identity, not availability.

- After a required PASS artifact becomes unreachable, aggregate state reopens to `INCONCLUSIVE`.
- Restoration at the exact expected content hash restores `SATISFIED`; the outage and restoration remain audit history.
- Restoration at a different hash remains `INCONCLUSIVE`; locator availability cannot substitute for identity.

A retained acceptance result therefore needs both identity and reachability/integrity auditing. Long-lived satisfaction cannot rely on a hash whose bytes are no longer retrievable.

## 10. Aggregate EvidenceSatisfaction

The experiment supports a bounded three-state aggregate for these scenarios:

- `SATISFIED`: every currently REQUIRED check has valid evidence under the exact requirement/plan; explicit active replacements count only if the versioned requirement authorizes them.
- `UNSATISFIED`: a required check is FAIL, FLAKY, NOT_RUN, expired-quarantine, or otherwise deterministically missing.
- `INCONCLUSIVE`: required evidence exists historically but cannot currently be verified because retained artifacts are unavailable/corrupt/mismatched, or another explicit inconclusive state is present.

This three-state output is a recommendation for the experiment surface, not a canonical universal enum. The canonical invariant is stronger and simpler: required FAIL/FLAKY/INCONCLUSIVE/NOT_RUN may not silently become SATISFIED.

## 11. Evidence versus inference

### Direct experiment evidence

- exact fixture and harness digests above;
- exact 11-scenario result matrix;
- repeated attempt lineages for PRODUCT fail/retry, INFRA fail/retry, and FLAKY/retry;
- deterministic quarantine active/expired transitions;
- deterministic retention loss/exact restore/wrong-hash restore transitions.

### Inference / recommendation

- real infra classification should itself require retained evidence and possibly independent policy checks;
- quarantine should be a versioned requirement object with expiry rather than a mutable label;
- evidence retention audits should be scheduled or event-triggered for authoritative artifacts;
- provider-specific mechanics should be tested separately before implementation readiness.

## 12. Alternatives considered

1. **Last-attempt-wins.** Rejected: launders earlier product failure and contradicts retained retry lineage.
2. **Majority vote across retries.** Rejected: can convert flakiness into apparent PASS.
3. **Quarantine as ignored failure.** Rejected: silently weakens the requirement.
4. **Quarantine as explicit replacement requirement.** Recommended bounded model: preserves negative evidence, expiry, owner/remediation, and substitution scope.
5. **Hash-only retention.** Rejected: identity without availability cannot support current verification.
6. **Provider-specific workflow proof in this mission.** Deferred: outside the bounded authoritative input and acceptance criteria.

## 13. Dependencies and interfaces

Inputs:

- canonical Wave 1 foundation blob `a252e3c93702f3ebaecd3e888944a23dbe1b0e1d`;
- Issue #77 task contract;
- exact claim/base recorded above.

Interfaces informed:

- future `EvidenceRequirement` and `CheckPlan` compiler semantics;
- `ExecutionEvidenceEnvelope.attempt_lineage`;
- `EvidenceSatisfaction` derivation;
- ArtifactIdentity reachability/integrity audits;
- quarantine policy records;
- W2-REV-01 cross-domain evidence review.

No production dependency is created.

## 14. Observability and evaluation requirements

A real implementation of these semantics should expose at minimum:

- exact requirement ID/version and policy epoch;
- exact candidate work/head/base;
- compiled applicability decision per check;
- every attempt ID, predecessor, result, and failure class;
- classification evidence for INFRA versus PRODUCT;
- artifact identity, storage refs, reachability, integrity status;
- quarantine owner, remediation, expiry, replacement set, and activation history;
- aggregate EvidenceSatisfaction derivation trace;
- reopen events after retention loss or policy expiry.

The aggregate result must be reconstructable from retained inputs; it must not be an opaque mutable label.

## 15. Failure modes and risks

- **Infra misclassification laundering:** a product failure mislabeled INFRA could be retried into false PASS.
- **Retry truncation:** deleting failed attempts makes last-attempt-wins unavoidable.
- **Predicate drift:** changing conditional applicability after execution can create false NA.
- **Quarantine permanence:** missing expiry/remediation turns temporary substitution into silent waiver.
- **Replacement weakness:** quarantine replacement may be materially weaker than the original check.
- **Artifact aliasing:** restoring different bytes under a reused locator could create false authority.
- **Retention blind spot:** hash remains known while bytes are permanently unavailable.
- **Aggregate overcompression:** a single green status can hide active quarantine/trust debt.
- **Provider mismatch:** this semantic fixture does not prove any CI provider can enforce these transitions atomically.

## 16. Unresolved questions

1. What exact evidence is sufficient to classify an attempt as INFRA rather than PRODUCT?
2. Which check classes may ever permit same-candidate infra retry versus requiring a fresh environment identity?
3. Should active quarantine yield plain `SATISFIED` plus structured debt, or a distinct externally visible satisfaction class?
4. What retention classes require periodic reachability audit versus audit-on-consumption?
5. What provider mechanism should enforce quarantine expiry without depending on mutable labels?
6. How should competing artifact mirrors prove exact-byte restoration and provenance?

These remain open for later design/review; this experiment does not settle them.

## 17. Reopen conditions

Reopen this bounded result if:

- a same-candidate product failure can become SATISFIED solely because a later attempt passes;
- required `NOT_RUN` can be treated as `NOT_APPLICABLE`;
- a quarantine can remain effective after expiry without a new policy version;
- replacement evidence can be weaker without an explicit requirement change;
- artifact loss leaves a dependent decision SATISFIED despite unverifiable required evidence;
- restored bytes can differ from the bound content identity;
- retry lineage is not reconstructable;
- W2-REV-01 identifies a semantic mismatch with the canonical foundation.

## 18. Required independent critique

`W2-REV-01` must independently attack at least:

- whether the experiment accidentally permits failure laundering;
- whether INFRA classification is too trusting;
- whether quarantine replacement is truly explicit and expiring;
- whether retention restoration semantics preserve exact identity;
- whether aggregate satisfaction hides unresolved trust debt;
- whether the fixture overclaims beyond provider-independent semantics.

No independent review disposition is claimed here.

## 19. Downstream work unblocked

This mission becomes `REVIEW_READY` for `W2-REV-01` once the exact report and handoff SHAs are frozen in schema-3 terminal status.

It does not unblock production implementation and does not close any implementation-readiness blocker by itself.

## Appendix A — exact reference harness

```python
import hashlib, json

BASE = "c7ba185ed9667b717794c19eaa0834ca41aa4c78"
REQS = [
    {"id":"unit","applicability":"REQUIRED","artifact_required":True,"allow_infra_retry":True},
    {"id":"package","applicability":"CONDITIONALLY_REQUIRED","predicate":"package_changed","artifact_required":True,"allow_infra_retry":True},
    {"id":"docs","applicability":"OPTIONAL","artifact_required":False,"allow_infra_retry":True},
    {"id":"console-cert","applicability":"NOT_APPLICABLE","artifact_required":False,"allow_infra_retry":False},
    {"id":"soak","applicability":"REQUIRED","artifact_required":True,"allow_infra_retry":True},
]
ART = {
    "unit": hashlib.sha256(b"unit-pass-artifact-v1").hexdigest(),
    "soak": hashlib.sha256(b"soak-pass-artifact-v1").hexdigest(),
    "package": hashlib.sha256(b"package-pass-artifact-v1").hexdigest(),
}
def resolve(req, ctx):
    if req["applicability"] == "CONDITIONALLY_REQUIRED":
        return "REQUIRED" if ctx.get(req["predicate"], False) else "NOT_APPLICABLE"
    return req["applicability"]

def check(req, ctx, attempts, artifact=None, quarantine=None, day=0, replacements=None):
    app = resolve(req, ctx)
    if app == "NOT_APPLICABLE":
        return ("NOT_APPLICABLE", True, "not_applicable")
    if app == "OPTIONAL" and not attempts:
        return ("NOT_RUN", True, "optional_not_run")
    if quarantine:
        if day <= quarantine["expiry_day"]:
            if replacements and all(replacements.values()):
                return ("PASS_BY_REPLACEMENT", True, "active_versioned_quarantine_replacement")
            return ("INCONCLUSIVE", False, "quarantine_replacement_missing")
        return ("NOT_RUN", False, "quarantine_expired")
    if not attempts:
        return ("NOT_RUN", False, "required_not_run")
    if any(a["result"] == "FLAKY" for a in attempts):
        return ("FLAKY", False, "explicit_flaky")
    if any(a["result"] == "INCONCLUSIVE" for a in attempts):
        return ("INCONCLUSIVE", False, "inconclusive_attempt")
    if any(a["result"] == "FAIL" and a.get("class") == "PRODUCT" for a in attempts):
        return ("FAIL", False, "product_fail_retained")
    results = [a["result"] for a in attempts]
    if "FAIL" in results and "PASS" in results:
        infra_only = all(a.get("class") == "INFRA" for a in attempts if a["result"] == "FAIL")
        if not (infra_only and req.get("allow_infra_retry") and attempts[-1]["result"] == "PASS"):
            return ("FLAKY", False, "divergent_attempts")
    elif "FAIL" in results:
        return ("FAIL", False, "failure_no_valid_replacement")
    if attempts[-1]["result"] != "PASS":
        return (attempts[-1]["result"], False, "terminal_nonpass")
    if req.get("artifact_required"):
        if not artifact or not artifact.get("reachable"):
            return ("INCONCLUSIVE", False, "artifact_unreachable")
        if artifact.get("observed_hash") != artifact.get("expected_hash"):
            return ("INCONCLUSIVE", False, "artifact_hash_mismatch")
    return ("PASS", True, "valid_pass")

def aggregate(ctx, attempts, artifacts=None, quarantines=None, day=0, replacements=None):
    artifacts = artifacts or {}
    quarantines = quarantines or {}
    replacements = replacements or {}
    out = {}
    for req in REQS:
        e, sat, reason = check(
            req, ctx, attempts.get(req["id"], []), artifacts.get(req["id"]),
            quarantines.get(req["id"]), day, replacements.get(req["id"])
        )
        out[req["id"]] = {"effective": e, "satisfied": sat, "reason": reason}
    gated = [out[r["id"]] for r in REQS if resolve(r, ctx) == "REQUIRED"]
    if all(x["satisfied"] for x in gated):
        agg = "SATISFIED"
    elif any(x["effective"] == "INCONCLUSIVE" for x in gated):
        agg = "INCONCLUSIVE"
    else:
        agg = "UNSATISFIED"
    return {"aggregate": agg, "checks": out}

good_unit = {"reachable": True, "expected_hash": ART["unit"], "observed_hash": ART["unit"]}
good_soak = {"reachable": True, "expected_hash": ART["soak"], "observed_hash": ART["soak"]}
q = {"soak": {"expiry_day": 14, "original_result": "FLAKY"}}
repl = {"soak": {"short_soak": True, "static_invariant": True}}

S = {}
S["S1_baseline"] = aggregate(
    {"package_changed": False},
    {"unit":[{"result":"PASS","class":"PRODUCT"}], "soak":[{"result":"PASS","class":"PRODUCT"}]},
    {"unit":good_unit, "soak":good_soak})
S["S2_conditional_not_run"] = aggregate(
    {"package_changed": True},
    {"unit":[{"result":"PASS","class":"PRODUCT"}], "soak":[{"result":"PASS","class":"PRODUCT"}]},
    {"unit":good_unit, "soak":good_soak})
S["S3_product_fail_retry"] = aggregate(
    {"package_changed": False},
    {"unit":[{"result":"FAIL","class":"PRODUCT"},{"result":"PASS","class":"PRODUCT"}],
     "soak":[{"result":"PASS","class":"PRODUCT"}]},
    {"unit":good_unit, "soak":good_soak})
S["S4_infra_retry"] = aggregate(
    {"package_changed": False},
    {"unit":[{"result":"FAIL","class":"INFRA"},{"result":"FAIL","class":"INFRA"},{"result":"PASS","class":"PRODUCT"}],
     "soak":[{"result":"PASS","class":"PRODUCT"}]},
    {"unit":good_unit, "soak":good_soak})
S["S5_flaky"] = aggregate(
    {"package_changed": False},
    {"unit":[{"result":"PASS","class":"PRODUCT"}],
     "soak":[{"result":"FLAKY","class":"PRODUCT"},{"result":"PASS","class":"PRODUCT"}]},
    {"unit":good_unit, "soak":good_soak})
S["S6_quarantine_active"] = aggregate(
    {"package_changed": False},
    {"unit":[{"result":"PASS","class":"PRODUCT"}],
     "soak":[{"result":"FLAKY","class":"PRODUCT"}]},
    {"unit":good_unit, "soak":good_soak}, q, 7, repl)
S["S7_quarantine_expired"] = aggregate(
    {"package_changed": False},
    {"unit":[{"result":"PASS","class":"PRODUCT"}],
     "soak":[{"result":"FLAKY","class":"PRODUCT"}]},
    {"unit":good_unit, "soak":good_soak}, q, 15, repl)
S["S8_remediated"] = aggregate(
    {"package_changed": False},
    {"unit":[{"result":"PASS","class":"PRODUCT"}],
     "soak":[{"result":"PASS","class":"PRODUCT"}]},
    {"unit":good_unit, "soak":good_soak})
S["S9_retention_loss"] = aggregate(
    {"package_changed": False},
    {"unit":[{"result":"PASS","class":"PRODUCT"}], "soak":[{"result":"PASS","class":"PRODUCT"}]},
    {"unit":{"reachable":False,"expected_hash":ART["unit"],"observed_hash":None}, "soak":good_soak})
S["S10_retention_restore"] = aggregate(
    {"package_changed": False},
    {"unit":[{"result":"PASS","class":"PRODUCT"}], "soak":[{"result":"PASS","class":"PRODUCT"}]},
    {"unit":good_unit, "soak":good_soak})
S["S11_wrong_restore"] = aggregate(
    {"package_changed": False},
    {"unit":[{"result":"PASS","class":"PRODUCT"}], "soak":[{"result":"PASS","class":"PRODUCT"}]},
    {"unit":{"reachable":True,"expected_hash":ART["unit"],
             "observed_hash":hashlib.sha256(b"unit-pass-artifact-corrupt").hexdigest()},
     "soak":good_soak})

print(json.dumps({k:v["aggregate"] for k,v in S.items()}, sort_keys=True))
print(hashlib.sha256(json.dumps(S, sort_keys=True, separators=(",",":")).encode()).hexdigest())
```