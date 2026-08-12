# W2-REM-CI-01 — Corrected CheckPlan / CI reliability evidence

**Source mission:** `W2-CI-01` / Issue #77  
**Remediation mission:** `W2-REM-CI-01` / Issue #91  
**Source frozen head/work:** `0011a9b02f1c7d8d20b81e0fb4faa6dec9bcae59`  
**Source report blob:** `7f9cb919c5e28299b7edbb1ea5495138d1509791`  
**Pre-gate review:** Issue #77 comment `5270075412`  
**Remediation base main:** `c7ba185ed9667b717794c19eaa0834ca41aa4c78`  
**Authoritative foundation:** `docs/planning/WAVE-1-FOUNDATIONS-v1.md` blob `a252e3c93702f3ebaecd3e888944a23dbe1b0e1d`  
**Task class / decision state:** `PLANNING_REVISION / EVIDENCE_REQUIRED`  
**Producer result:** `BOUNDED_PASS` for the corrected provider-independent fixture only; formal independent review remains `W2-REV-01`.

## 1. Scope and non-goals

This remediation preserves the original W2-CI-01 question while correcting three evidence defects identified before the formal Wave-2 aggregate review:

1. quarantine replacement must be exact, version-bound evidence rather than arbitrary truthy values;
2. every evidence episode must bind an exact candidate identity and same-candidate history must be append-only;
3. retention loss/restoration must preserve one durable artifact identity and event lineage.

The experiment still exercises `REQUIRED`, `CONDITIONALLY_REQUIRED`, `OPTIONAL`, and `NOT_APPLICABLE`; required `NOT_RUN`; product/infra/flake retry behavior; quarantine expiry/replacement; retention loss/restoration; and aggregate `EvidenceSatisfaction`.

Non-goals remain unchanged: no CI provider, runner topology, workflow syntax, production CI architecture, universal INFRA classifier, engine decision, implementation-readiness transition, or production dependency is selected or authorized. This remediation does not replace `W2-REV-01`.

## 2. Constraints, assumptions, and authority limits

Canonical Wave-1 constraints retained here:

- `CheckPlan`/execution evidence may not weaken the declared requirement;
- `NOT_APPLICABLE` is resolved separately from `NOT_RUN`;
- required `FAIL`, `FLAKY`, `INCONCLUSIVE`, or `NOT_RUN` cannot silently become SATISFIED;
- replacement/quarantine authority is explicit and versioned;
- retry lineage is retained;
- content hash proves identity, not availability;
- unavailable/corrupt retained evidence reopens authority.

Assumptions are intentionally narrow: the fixture is synthetic, provider-independent, and evaluates only the closed semantics encoded in the reference harness. INFRA-versus-PRODUCT classification is supplied as fixture data and is not claimed to be generally solved.

## 3. Corrected identity model

### 3.1 Exact candidates

Every execution envelope binds both exact `candidate_id` and exact base SHA.

| Candidate | Purpose | Successor relation |
|---|---|---|
| `cand-good-v1` | baseline + retention scenarios | — |
| `cand-product-fail-v1` | same-candidate PRODUCT fail then PASS | — |
| `cand-infra-retry-v1` | permitted INFRA retries then PASS | — |
| `cand-flaky-v1` | FLAKY then PASS + quarantine | — |
| `cand-flaky-v2` | remediated successor | supersedes `cand-flaky-v1` |

The remediated scenario can therefore SATISFY only under `cand-flaky-v2`; starting another root envelope for `cand-flaky-v1` is mechanically rejected as a reset/fork.

### 3.2 Append-only execution envelopes

Each envelope has `envelope_id`, `candidate_id`, `base_sha`, `policy_version`, `previous_envelope_id`, and attempt sets. For one candidate, envelope history must form one append-only chain. A second root envelope for an already-seen candidate is `INCONCLUSIVE` with reason `same_candidate_envelope_reset_or_fork`.

This closes the episode-boundary laundering path identified as PG-M02.

### 3.3 Stable ArtifactIdentity + availability lineage

Each evidence artifact has one stable `artifact_id` and expected content hash. Availability is an ordered event lineage under that same identity:

`REACHABLE(exact hash) -> UNREACHABLE -> REACHABLE(exact hash | wrong hash)`.

The aggregate result retains the complete event list. Exact restoration therefore restores the same historical evidence identity; a fresh unrelated PASS cannot masquerade as restoration. This closes PG-m01.

## 4. Corrected quarantine model

Normal requirement/policy is `CI-EXP-REQ-v2` / `ci-reliability-exp-v2`.

The quarantine is a separate exact version:

- requirement: `CI-EXP-REQ-v2-q1`;
- policy: `ci-reliability-exp-v2-q1`;
- candidate: `cand-flaky-v1`;
- target check: `soak`;
- expiry: day 14;
- exact replacement set: `short_soak` + `static_invariant`;
- each replacement must bind the exact candidate, exact quarantine policy, exact replacement ID, PASS result, exact expected ArtifactIdentity, and currently reachable exact content hash.

The evaluator requires exact set equality. Missing, extra, arbitrary, wrong-policy, wrong-candidate, non-PASS, wrong-artifact, unavailable, or hash-mismatched replacement evidence cannot yield `PASS_BY_REPLACEMENT`.

This closes PG-M01. The original FLAKY attempts remain present in the source envelope; quarantine supplies temporary replacement authority instead of rewriting historical evidence.

## 5. Executed corrected scenarios

The fixture, harness contract, and result object are each content-addressed from canonical JSON generated by Appendix A. The harness digest is deliberately a digest of the explicit `HARNESS_IDENTITY` contract rather than Python source formatting, so whitespace-only edits cannot change semantic harness identity.

Fixture digest: `sha256:2f07e41bccd8eef9e35ad7bc03e2aad7b6792a62cfc6d1560b933a814604c988`  
Harness contract digest: `sha256:9963302d28ed3057a4e46070b462a91e45aebef6f57829569a3bafe57a53700a`  
Canonical result-object digest: `sha256:b2905c4cf9095ba70c42770505073dc21d616996316f2dc800293d78ca8ea057`

| ID | Injection / condition | Aggregate | Key reason |
|---|---|---|---|
| S1 | baseline; package predicate false | `SATISFIED` | required evidence exact |
| S2 | package predicate true, package not run | `UNSATISFIED` | required `NOT_RUN` |
| S3 | PRODUCT FAIL then PASS, same candidate | `UNSATISFIED` | product failure retained |
| S4 | INFRA FAIL, INFRA FAIL, then PASS | `SATISFIED` | explicitly permitted infra retry |
| S5 | FLAKY then PASS, same candidate | `UNSATISFIED` | flake retained |
| S6 | active quarantine + exact two replacements | `SATISFIED` | exact versioned replacement set valid |
| S7 | one quarantine replacement missing | `INCONCLUSIVE` | replacement set mismatch |
| S8 | arbitrary replacement key only | `INCONCLUSIVE` | replacement set mismatch |
| S9 | exact IDs but wrong bound artifact | `INCONCLUSIVE` | replacement artifact binding mismatch |
| S10 | quarantine expired | `UNSATISFIED` | replacement authority expired |
| S11 | same candidate starts a fresh root envelope | `INCONCLUSIVE` | reset/fork rejected |
| S12 | distinct remediated successor candidate | `SATISFIED` | valid new candidate evidence |
| S13 | required artifact becomes unavailable | `INCONCLUSIVE` | stable artifact identity unavailable |
| S14 | same artifact restored at exact hash | `SATISFIED` | exact restoration with retained lineage |
| S15 | same artifact restored at wrong hash | `INCONCLUSIVE` | content identity mismatch |
| S16 | exact replacement IDs but wrong policy | `INCONCLUSIVE` | replacement policy mismatch |

Appendix A reproduces the fixture, harness-contract, and result-object digests above.

## 6. Evidence versus inference

### Direct evidence

- exact candidate/base binding exists in every result object;
- append-only envelope validation rejects same-candidate reset/fork;
- product and flake negative histories remain gating;
- permitted INFRA retries remain retained while later PASS may satisfy;
- quarantine uses exact replacement-set equality and evidence-bearing replacement records;
- arbitrary/missing/wrong-artifact/wrong-policy replacement probes fail closed;
- retention loss/exact restore/wrong-hash restore share the same stable artifact identity and event lineage;
- all 16 aggregate results and the canonical result digest reproduce deterministically.

### Inference / recommendation

- real INFRA classification should itself require evidence and policy authority;
- production quarantine should use the same exact-set/version/provenance discipline rather than mutable labels;
- authoritative retained artifacts need periodic or consumption-time reachability/integrity checks;
- provider-specific enforcement must be tested separately before implementation readiness.

## 7. Alternatives considered

1. **Keep boolean replacement flags.** Rejected because arbitrary truthy values can fabricate replacement satisfaction.
2. **Treat each execution episode as independent even for the same candidate.** Rejected because negative evidence can be erased at episode boundaries.
3. **Use fresh candidate identity only in prose.** Rejected because the evaluator cannot enforce it.
4. **Use stable candidate IDs plus append-only envelope chains.** Adopted for this bounded fixture.
5. **Model restoration as a fresh artifact object.** Rejected because it loses outage/restoration provenance.
6. **Model one ArtifactIdentity with ordered availability events.** Adopted for this bounded fixture.

## 8. Dependencies and interfaces

Inputs are limited to canonical `WAVE-1-FOUNDATIONS-v1.md`, frozen Issue #77 source work/status, Issue #77 pre-gate findings, and canonical planning routing.

Interfaces informed remain: future `EvidenceRequirement`, `CheckPlan`, `ExecutionEvidenceEnvelope`, `EvidenceSatisfaction`, ArtifactIdentity reachability auditing, quarantine policy records, and the formal `W2-REV-01` review packet.

No production dependency or canonical decision is created.

## 9. Observability and evaluation requirements

A production-capable descendant should expose at minimum:

- exact candidate work/head/base and policy epoch;
- requirement/check applicability derivation;
- envelope ID, predecessor, and attempt IDs;
- every result and failure class with classification evidence;
- replacement requirement/policy/candidate/artifact bindings;
- stable ArtifactIdentity and ordered availability/integrity events;
- quarantine owner/remediation/expiry/replacement set;
- aggregate derivation trace and reopen events.

The aggregate result must remain reconstructable from retained inputs.

## 10. Failure modes and residual risks

- INFRA misclassification can still launder product failure if classification authority is weak; this remains explicitly unresolved.
- A real evidence store could still lose attempts unless append-only retention is enforced outside this fixture.
- Replacement checks may be semantically weaker than the original check even when identities are exact; equivalence/adequacy remains a review question.
- Provider implementations may not enforce atomic policy expiry, artifact availability, or immutable lineage.
- Mutable evaluator/provider backends require separate fingerprint/calibration/drift controls.

## 11. Unresolved questions

1. What evidence and authority are sufficient to classify INFRA versus PRODUCT?
2. Which requirement classes may permit same-candidate infra retry?
3. What policy proves replacement adequacy relative to the quarantined check?
4. What retention classes require scheduled audit versus audit-on-consumption?
5. Which provider mechanisms can enforce immutable lineage and quarantine expiry?

## 12. Reopen conditions

Reopen this bounded result if any of the following becomes possible:

- a same-candidate negative attempt disappears without a valid successor candidate;
- a second root envelope for the same candidate is accepted;
- quarantine SATISFIES with a missing/extra/arbitrary/wrong-policy/wrong-artifact replacement;
- artifact loss leaves a dependent result SATISFIED;
- restoration at a different content hash restores authority;
- the outage/restoration event lineage is not retained;
- formal `W2-REV-01` finds a mismatch with the canonical foundation.

## 13. Required independent critique

`W2-REV-01` must still independently attack failure laundering, INFRA classification, replacement adequacy, exact-set/version binding, artifact retention semantics, provider overclaim, and readiness leakage. This remediation and its self-review are not an independent schema-3 review result.

## 14. Downstream work unblocked

The corrected W2-CI evidence may replace the frozen Issue #77 producer candidate as the substantive CI input to `W2-REV-01` once Issue #91 publishes terminal `STATUS(REVIEW_READY)` with exact work/head/blob provenance.

No production implementation, readiness blocker closure, synthesis authority, or canonicalization is unlocked by this report alone.

## Appendix A — exact corrected reference harness

```python
import copy, hashlib, json

BASE = "c7ba185ed9667b717794c19eaa0834ca41aa4c78"
POLICY_NORMAL = "ci-reliability-exp-v2"
POLICY_QUARANTINE = "ci-reliability-exp-v2-q1"
HARNESS_IDENTITY = {
    "harness_version":"ci-reliability-reference-v2",
    "candidate_chain_semantics":"append-only-exact-candidate-v1",
    "quarantine_semantics":"exact-versioned-replacement-set-v1",
    "artifact_lineage_semantics":"stable-artifact-event-lineage-v1",
    "aggregate_semantics":"required-gate-three-state-v1",
}

def h(s):
    return hashlib.sha256(s.encode()).hexdigest()

def canonical_digest(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()

ARTIFACTS = {
    "unit-pass":{"artifact_id":"art-unit-pass-v2","content_hash":h("unit-pass-artifact-v2")},
    "soak-pass":{"artifact_id":"art-soak-pass-v2","content_hash":h("soak-pass-artifact-v2")},
    "package-pass":{"artifact_id":"art-package-pass-v2","content_hash":h("package-pass-artifact-v2")},
    "short-soak":{"artifact_id":"art-short-soak-v2","content_hash":h("short-soak-artifact-v2")},
    "static-invariant":{"artifact_id":"art-static-invariant-v2","content_hash":h("static-invariant-artifact-v2")},
}
CANDIDATES = {
    "good":{"candidate_id":"cand-good-v1","base_sha":BASE,"supersedes":None},
    "product":{"candidate_id":"cand-product-fail-v1","base_sha":BASE,"supersedes":None},
    "infra":{"candidate_id":"cand-infra-retry-v1","base_sha":BASE,"supersedes":None},
    "flaky":{"candidate_id":"cand-flaky-v1","base_sha":BASE,"supersedes":None},
    "remediated":{"candidate_id":"cand-flaky-v2","base_sha":BASE,"supersedes":"cand-flaky-v1"},
}
REQUIREMENT = {
    "requirement_id":"CI-EXP-REQ-v2","policy_version":POLICY_NORMAL,
    "checks":[
        {"id":"unit","applicability":"REQUIRED","artifact_key":"unit-pass","allow_infra_retry":True},
        {"id":"package","applicability":"CONDITIONALLY_REQUIRED","predicate":"package_changed","artifact_key":"package-pass","allow_infra_retry":True},
        {"id":"docs","applicability":"OPTIONAL","artifact_key":None,"allow_infra_retry":True},
        {"id":"console-cert","applicability":"NOT_APPLICABLE","artifact_key":None,"allow_infra_retry":False},
        {"id":"soak","applicability":"REQUIRED","artifact_key":"soak-pass","allow_infra_retry":True},
    ],
}
QUARANTINE_POLICY = {
    "requirement_id":"CI-EXP-REQ-v2-q1","policy_version":POLICY_QUARANTINE,
    "source_requirement_id":"CI-EXP-REQ-v2","candidate_id":CANDIDATES["flaky"]["candidate_id"],
    "check_id":"soak","expiry_day":14,
    "replacement_set":[
        {"replacement_id":"short_soak","artifact_key":"short-soak"},
        {"replacement_id":"static_invariant","artifact_key":"static-invariant"},
    ],
}

def attempt(aid,result,klass,artifact_key=None):
    return {"attempt_id":aid,"result":result,"class":klass,"artifact_key":artifact_key}

def envelope(eid,candidate_key,attempts_by_check,previous=None,policy=POLICY_NORMAL):
    c=CANDIDATES[candidate_key]
    return {"envelope_id":eid,"candidate_id":c["candidate_id"],"base_sha":c["base_sha"],"policy_version":policy,"previous_envelope_id":previous,"attempts":attempts_by_check}

ENVELOPES = {
    "good":envelope("env-good-1","good",{"unit":[attempt("u-good-1","PASS","PRODUCT","unit-pass")],"soak":[attempt("s-good-1","PASS","PRODUCT","soak-pass")]}),
    "product":envelope("env-product-1","product",{"unit":[attempt("u-prod-1","FAIL","PRODUCT"),attempt("u-prod-2","PASS","PRODUCT","unit-pass")],"soak":[attempt("s-prod-1","PASS","PRODUCT","soak-pass")]}),
    "infra":envelope("env-infra-1","infra",{"unit":[attempt("u-infra-1","FAIL","INFRA"),attempt("u-infra-2","FAIL","INFRA"),attempt("u-infra-3","PASS","PRODUCT","unit-pass")],"soak":[attempt("s-infra-1","PASS","PRODUCT","soak-pass")]}),
    "flaky":envelope("env-flaky-1","flaky",{"unit":[attempt("u-flaky-1","PASS","PRODUCT","unit-pass")],"soak":[attempt("s-flaky-1","FLAKY","PRODUCT"),attempt("s-flaky-2","PASS","PRODUCT","soak-pass")]}),
    "flaky_reset":envelope("env-flaky-reset","flaky",{"unit":[attempt("u-flaky-reset-1","PASS","PRODUCT","unit-pass")],"soak":[attempt("s-flaky-reset-1","PASS","PRODUCT","soak-pass")]},previous=None),
    "remediated":envelope("env-remediated-1","remediated",{"unit":[attempt("u-rem-1","PASS","PRODUCT","unit-pass")],"soak":[attempt("s-rem-1","PASS","PRODUCT","soak-pass")]}),
}

def art_state(key,events):
    a=ARTIFACTS[key]
    return {"artifact_id":a["artifact_id"],"expected_hash":a["content_hash"],"events":events}

def reachable_event(eid,observed_hash): return {"event_id":eid,"state":"REACHABLE","observed_hash":observed_hash}
def unavailable_event(eid): return {"event_id":eid,"state":"UNREACHABLE","observed_hash":None}

BASE_ARTIFACT_STATES = {
    "unit-pass":art_state("unit-pass",[reachable_event("unit-e0",ARTIFACTS["unit-pass"]["content_hash"])]),
    "soak-pass":art_state("soak-pass",[reachable_event("soak-e0",ARTIFACTS["soak-pass"]["content_hash"])]),
    "package-pass":art_state("package-pass",[reachable_event("package-e0",ARTIFACTS["package-pass"]["content_hash"])]),
    "short-soak":art_state("short-soak",[reachable_event("short-e0",ARTIFACTS["short-soak"]["content_hash"])]),
    "static-invariant":art_state("static-invariant",[reachable_event("static-e0",ARTIFACTS["static-invariant"]["content_hash"])]),
}

def resolve(req,ctx):
    if req["applicability"]=="CONDITIONALLY_REQUIRED":
        return "REQUIRED" if ctx.get(req["predicate"],False) else "NOT_APPLICABLE"
    return req["applicability"]

def latest_artifact_status(state):
    if not state or not state.get("events"): return ("INCONCLUSIVE","artifact_state_missing")
    last=state["events"][-1]
    if last["state"]!="REACHABLE": return ("INCONCLUSIVE","artifact_unreachable")
    if last.get("observed_hash")!=state.get("expected_hash"): return ("INCONCLUSIVE","artifact_hash_mismatch")
    return ("PASS","artifact_reachable_exact")

def validate_envelope_chain(envelopes,candidate_id):
    if not envelopes: return (False,"missing_evidence_envelope")
    seen_ids,prev=set(),None
    for i,env in enumerate(envelopes):
        if env["envelope_id"] in seen_ids: return (False,"duplicate_envelope_id")
        seen_ids.add(env["envelope_id"])
        if env["candidate_id"]!=candidate_id or env["base_sha"]!=BASE: return (False,"candidate_or_base_mismatch")
        if i==0 and env.get("previous_envelope_id") is not None: return (False,"first_envelope_has_predecessor")
        if i>0 and env.get("previous_envelope_id")!=prev: return (False,"same_candidate_envelope_reset_or_fork")
        prev=env["envelope_id"]
    return (True,"valid_append_only_chain")

def check_attempts(req,attempts,artifact_states):
    if not attempts: return ("NOT_RUN",False,"required_not_run")
    ids=[a["attempt_id"] for a in attempts]
    if len(ids)!=len(set(ids)): return ("INCONCLUSIVE",False,"duplicate_attempt_id")
    if any(a["result"]=="FLAKY" for a in attempts): return ("FLAKY",False,"explicit_flaky")
    if any(a["result"]=="INCONCLUSIVE" for a in attempts): return ("INCONCLUSIVE",False,"inconclusive_attempt")
    if any(a["result"]=="FAIL" and a.get("class")=="PRODUCT" for a in attempts): return ("FAIL",False,"product_fail_retained")
    results=[a["result"] for a in attempts]
    if "FAIL" in results and "PASS" in results:
        infra_only=all(a.get("class")=="INFRA" for a in attempts if a["result"]=="FAIL")
        if not (infra_only and req.get("allow_infra_retry") and attempts[-1]["result"]=="PASS"):
            return ("FLAKY",False,"divergent_attempts")
    elif "FAIL" in results: return ("FAIL",False,"failure_no_valid_replacement")
    if attempts[-1]["result"]!="PASS": return (attempts[-1]["result"],False,"terminal_nonpass")
    artifact_key=req.get("artifact_key")
    if artifact_key:
        if attempts[-1].get("artifact_key")!=artifact_key: return ("INCONCLUSIVE",False,"attempt_artifact_binding_mismatch")
        status,reason=latest_artifact_status(artifact_states.get(artifact_key))
        if status!="PASS": return ("INCONCLUSIVE",False,reason)
    return ("PASS",True,"valid_pass")

def validate_quarantine(candidate_id,day,replacement_evidence,artifact_states):
    q=QUARANTINE_POLICY
    if candidate_id!=q["candidate_id"]: return ("INCONCLUSIVE",False,"quarantine_candidate_mismatch")
    if day>q["expiry_day"]: return ("NOT_RUN",False,"quarantine_expired")
    required={x["replacement_id"]:x for x in q["replacement_set"]}
    if set(replacement_evidence.keys())!=set(required.keys()): return ("INCONCLUSIVE",False,"replacement_set_mismatch")
    for rid,spec in required.items():
        ev=replacement_evidence[rid]
        if ev.get("replacement_id")!=rid: return ("INCONCLUSIVE",False,"replacement_id_mismatch")
        if ev.get("candidate_id")!=candidate_id: return ("INCONCLUSIVE",False,"replacement_candidate_mismatch")
        if ev.get("policy_version")!=q["policy_version"]: return ("INCONCLUSIVE",False,"replacement_policy_mismatch")
        if ev.get("result")!="PASS": return ("INCONCLUSIVE",False,"replacement_nonpass")
        if ev.get("artifact_key")!=spec["artifact_key"]: return ("INCONCLUSIVE",False,"replacement_artifact_binding_mismatch")
        status,reason=latest_artifact_status(artifact_states.get(spec["artifact_key"]))
        if status!="PASS": return ("INCONCLUSIVE",False,reason)
    return ("PASS_BY_REPLACEMENT",True,"exact_versioned_replacement_set_valid")

def aggregate(candidate_key,ctx,envelopes,artifact_states=None,day=0,quarantine=False,replacement_evidence=None):
    c=CANDIDATES[candidate_key]
    artifact_states=copy.deepcopy(artifact_states or BASE_ARTIFACT_STATES)
    ok,chain_reason=validate_envelope_chain(envelopes,c["candidate_id"])
    result={"candidate_id":c["candidate_id"],"base_sha":c["base_sha"],"policy_version":POLICY_QUARANTINE if quarantine else POLICY_NORMAL,"envelope_ids":[e["envelope_id"] for e in envelopes],"chain_validation":chain_reason,"artifact_event_lineage":{k:v["events"] for k,v in sorted(artifact_states.items())},"checks":{}}
    if not ok:
        result["aggregate"]="INCONCLUSIVE"
        return result
    merged_attempts={}
    for env in envelopes:
        for check_id,attempts in env["attempts"].items(): merged_attempts.setdefault(check_id,[]).extend(attempts)
    for req in REQUIREMENT["checks"]:
        app=resolve(req,ctx)
        if app=="NOT_APPLICABLE": outcome=("NOT_APPLICABLE",True,"not_applicable")
        elif app=="OPTIONAL" and not merged_attempts.get(req["id"]): outcome=("NOT_RUN",True,"optional_not_run")
        elif quarantine and req["id"]==QUARANTINE_POLICY["check_id"]: outcome=validate_quarantine(c["candidate_id"],day,replacement_evidence or {},artifact_states)
        else: outcome=check_attempts(req,merged_attempts.get(req["id"],[]),artifact_states)
        result["checks"][req["id"]]={"effective":outcome[0],"satisfied":outcome[1],"reason":outcome[2]}
    gated=[result["checks"][r["id"]] for r in REQUIREMENT["checks"] if resolve(r,ctx)=="REQUIRED"]
    if all(x["satisfied"] for x in gated): result["aggregate"]="SATISFIED"
    elif any(x["effective"]=="INCONCLUSIVE" for x in gated): result["aggregate"]="INCONCLUSIVE"
    else: result["aggregate"]="UNSATISFIED"
    return result

def replacement_ev(rid,artifact_key,candidate_id=None,policy=None,result="PASS"):
    return {"replacement_id":rid,"candidate_id":candidate_id or CANDIDATES["flaky"]["candidate_id"],"policy_version":policy or POLICY_QUARANTINE,"result":result,"artifact_key":artifact_key}

VALID_REPLACEMENTS={"short_soak":replacement_ev("short_soak","short-soak"),"static_invariant":replacement_ev("static_invariant","static-invariant")}
FIXTURE={"base_sha":BASE,"requirement":REQUIREMENT,"quarantine_policy":QUARANTINE_POLICY,"candidates":CANDIDATES,"artifact_identities":ARTIFACTS,"envelope_ids":{k:v["envelope_id"] for k,v in ENVELOPES.items()}}
RESULTS={}
RESULTS["S1_baseline"]=aggregate("good",{"package_changed":False},[ENVELOPES["good"]])
RESULTS["S2_conditional_not_run"]=aggregate("good",{"package_changed":True},[ENVELOPES["good"]])
RESULTS["S3_product_fail_retry"]=aggregate("product",{"package_changed":False},[ENVELOPES["product"]])
RESULTS["S4_infra_retry"]=aggregate("infra",{"package_changed":False},[ENVELOPES["infra"]])
RESULTS["S5_flaky"]=aggregate("flaky",{"package_changed":False},[ENVELOPES["flaky"]])
RESULTS["S6_quarantine_active_valid"]=aggregate("flaky",{"package_changed":False},[ENVELOPES["flaky"]],day=7,quarantine=True,replacement_evidence=VALID_REPLACEMENTS)
RESULTS["S7_quarantine_missing_replacement"]=aggregate("flaky",{"package_changed":False},[ENVELOPES["flaky"]],day=7,quarantine=True,replacement_evidence={"short_soak":VALID_REPLACEMENTS["short_soak"]})
RESULTS["S8_quarantine_arbitrary_key"]=aggregate("flaky",{"package_changed":False},[ENVELOPES["flaky"]],day=7,quarantine=True,replacement_evidence={"arbitrary":replacement_ev("arbitrary","short-soak")})
bad_art_repl=copy.deepcopy(VALID_REPLACEMENTS); bad_art_repl["static_invariant"]=replacement_ev("static_invariant","short-soak")
RESULTS["S9_quarantine_wrong_artifact"]=aggregate("flaky",{"package_changed":False},[ENVELOPES["flaky"]],day=7,quarantine=True,replacement_evidence=bad_art_repl)
RESULTS["S10_quarantine_expired"]=aggregate("flaky",{"package_changed":False},[ENVELOPES["flaky"]],day=15,quarantine=True,replacement_evidence=VALID_REPLACEMENTS)
RESULTS["S11_same_candidate_reset_rejected"]=aggregate("flaky",{"package_changed":False},[ENVELOPES["flaky"],ENVELOPES["flaky_reset"]])
RESULTS["S12_remediated_successor"]=aggregate("remediated",{"package_changed":False},[ENVELOPES["remediated"]])
loss_states=copy.deepcopy(BASE_ARTIFACT_STATES); loss_states["unit-pass"]["events"].append(unavailable_event("unit-e1-loss"))
RESULTS["S13_retention_loss"]=aggregate("good",{"package_changed":False},[ENVELOPES["good"]],artifact_states=loss_states)
restore_states=copy.deepcopy(loss_states); restore_states["unit-pass"]["events"].append(reachable_event("unit-e2-restore",ARTIFACTS["unit-pass"]["content_hash"]))
RESULTS["S14_exact_restore"]=aggregate("good",{"package_changed":False},[ENVELOPES["good"]],artifact_states=restore_states)
wrong_restore_states=copy.deepcopy(loss_states); wrong_restore_states["unit-pass"]["events"].append(reachable_event("unit-e2-wrong",h("unit-pass-artifact-corrupt")))
RESULTS["S15_wrong_hash_restore"]=aggregate("good",{"package_changed":False},[ENVELOPES["good"]],artifact_states=wrong_restore_states)
wrong_policy=copy.deepcopy(VALID_REPLACEMENTS); wrong_policy["short_soak"]=replacement_ev("short_soak","short-soak",policy="wrong-policy")
RESULTS["S16_quarantine_wrong_policy"]=aggregate("flaky",{"package_changed":False},[ENVELOPES["flaky"]],day=7,quarantine=True,replacement_evidence=wrong_policy)

print(json.dumps({k:v["aggregate"] for k,v in RESULTS.items()},sort_keys=True))
print(canonical_digest(FIXTURE))
print(canonical_digest(HARNESS_IDENTITY))
print(canonical_digest(RESULTS))
```
