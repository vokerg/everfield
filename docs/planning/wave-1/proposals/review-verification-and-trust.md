# Independent Review, Verification, and Trust Boundaries — Wave 1 Proposal

**Mission:** `W1-FAC-03`  
**State:** PROPOSED / NON-CANONICAL  
**Role:** verification / trust planner  
**Required reviews:** `W1-REV-FAC`, `W1-REV-TECH`

## Review Index

**Core recommendation.** Replace the vague question “was this independently reviewed?” with a typed **Trust Profile** across five dimensions: authorship separation, private-context separation, candidate-write separation, oracle/evaluator separation, and evidence independence. Review/verification requirements should be claim/risk-class specific, and every result must bind the exact candidate work SHA, base, evidence hashes, evaluator versions, and trust profile.

**Review classes.** `SELF_CHECK` is useful but never independent. `ADVERSARIAL_REVIEW` attacks specification/design/implementation claims without editing the candidate. `CROSS_DOMAIN_REVIEW` attacks interfaces and hidden coupling. `INDEPENDENT_VERIFICATION` executes/reproduces exact acceptance claims against an immutable candidate. `PROTECTED_VERIFICATION` adds held-out/protected or independently controlled oracles. `META_VERIFICATION` is required for judge-affecting changes to review/verifier/evaluator/metric/permission policy. Task contracts declare which class is required; risk can escalate the class but cannot downgrade a canonical gate.

**Current one-agent constraint.** `DEGRADED_SINGLE_AGENT` is a liveness mode, not full independence: new episode, frozen candidate, repository-only judging packet, prior-rationale gate, new evidence before reconciliation, explicit prior roles/trust debt, and reopen when isolated/multi-agent capability exists. Same-context “I will be objective” is `NOT_INDEPENDENT`.

**Evidence sufficiency.** No result may pass because a producer’s own tests/dashboard are green. Evidence must be claim-appropriate and diversified: exact runtime/scenario/invariant evidence for correctness; architecture/interface evidence for structural claims; player + simulation surfaces for gameplay; protected/held-out signals where gaming risk is material; evaluator identity/version and input hashes for subjective judgments. PASS with missing required evidence is invalid, not “low confidence.”

**Disagreement.** Do not resolve reviewer disagreement by majority vote or human default. Normalize exact claims/evidence, classify contradiction vs differing risk tolerance, gather targeted runtime/empirical evidence, run adversarial reevaluation/pairwise candidate comparison where useful, and re-plan when evidence remains insufficient. Dissent stays in provenance even after a decision.

**Permission boundary target.** Producers write candidate surfaces, reviewers write finding surfaces, verifiers write evidence/reports, integrators write only verified promotion surfaces. Protected evaluator/configuration mutation is a separate meta-change route. Where platform permissions cannot enforce this yet, record procedural enforcement and trust debt rather than claiming isolation.

**Primary attacks.** producer edits held-out tests; reviewer patches candidate then passes it; UUID/session laundering; stale-base PASS; hidden evaluator drift; self-authored tests as sole oracle; visible-metric gaming; subjective judge agreement mistaken for truth; permission overlap; protected evidence leakage; review queue becoming a human-style approval bottleneck.

**Experiments.** seeded-defect escape benchmark; candidate-write permission red-team; reviewer disagreement tournament; visible-metric reward-hacking challenge; evaluator-version replay/drift test; protected-evidence leakage probe; base-drift verification refresh; degraded-vs-isolated comparison when stronger capability exists.

## 1. Status

This proposal defines review classes, trust profiles, disagreement handling, protected evaluation boundaries, evidence sufficiency, anti-Goodhart controls, and integration eligibility. It supplies trust/evidence semantics for later reconciliation with control-plane and CI/evidence proposals.

It does not create protected infrastructure or claim that current platform permissions already enforce the target separation. Exact storage, check-report schemas, CI topology, and permission implementation belong to W1-FAC-04 and later technical work.

## 2. Scope

This proposal covers:

1. review/verification role classes;
2. independence/trust dimensions and profiles;
3. candidate immutability and permission boundaries;
4. evidence sufficiency by claim type;
5. finding/disposition semantics;
6. disagreement and uncertainty escalation;
7. protected evaluation surfaces;
8. evaluator/version provenance;
9. anti-Goodhart mechanisms;
10. integration eligibility and base freshness;
11. trust observability and benchmark experiments.

## 3. Inputs and source basis

### 3.1 Observed repository evidence

The authoritative packet establishes:

- the autonomous-factory mandate requires independent critique, transactional handoffs, verification separate from production, protected evaluation consideration, no routine human approval, and explicit governance for factory self-modification;
- Evaluation and Evidence requires inspectable evidence, real executable/gameplay-kernel testing for integration claims, deterministic/reproducible evidence where practical, objective + subjective evaluation, player + simulation surfaces, protected holdouts, independent test authorship, evaluator versioning, disagreement measurement, and explicit Goodhart resistance;
- the research agenda leaves review-policy details, evaluator trust, held-out test ownership, disagreement handling, permissions, and factory benchmarks as explicit research targets;
- the planning deliverables require review policy, verifier protocol, evidence provenance, independent test authorship, disagreement process, protected/held-out testing strategy, review routing, CI run reports, artifact retention, and factory benchmarks before implementation readiness.

### 3.2 Inference

Independence is not a single property. A nominally separate reviewer can still be correlated with the producer through shared private context, candidate-write permission, self-authored evaluators, or identical evidence. Therefore the system should record the actual trust boundary and demand stronger dimensions when the claim is more gameable or higher impact.

### 3.3 Recommendation

Adopt the typed trust/review/evidence model below and benchmark it before translating it into protected permissions/CI policy.

## 4. Goals

For any acceptance, review, verification, or canonicalization decision, a fresh agent should be able to determine:

- what exact candidate/result is being judged;
- what review/verification class was required;
- which actor/episode roles participated;
- which independence dimensions were actually satisfied;
- whether the judging episode could modify the candidate or oracle;
- what evidence supports each critical claim;
- what evaluator/test/rubric versions produced judgments;
- which BLOCKER/MAJOR findings remain unresolved;
- how reviewer disagreement was resolved or preserved;
- whether evidence is still valid for the current base;
- whether integration is eligible without hidden human approval.

## 5. Non-goals

This proposal does **not**:

- assert that one model/session/user account can provide full cognitive independence;
- prescribe one review class for every task regardless of risk;
- require protected/hidden tests for all work;
- define exact CI artifact storage/retention topology;
- define GitHub App/ruleset permission implementation details;
- reduce subjective game quality to a single scalar;
- allow reviewer or verifier role labels to substitute for evidence separation;
- authorize gameplay implementation or canonicalize itself.

## 6. Constraints

1. Producers/implementers cannot be the final judge of important claims about their own work.
2. Important acceptance claims must resolve to inspectable evidence appropriate to the claim.
3. Self-authored tests may contribute evidence but cannot be the only oracle for material integration/quality claims.
4. Candidate state must be immutable during a verification result that claims to bind that candidate.
5. Verification/result authority binds exact work SHA, evidence, evaluator versions, and base.
6. Base or candidate drift invalidates or refreshes verification according to canonical lifecycle rules; results do not float to newer state by inference.
7. Protected evaluators/tests cannot be casually modified by the work they judge.
8. Evaluator disagreement normally triggers machine evidence/reevaluation/replanning, not routine human tie-breaking.
9. Metrics are diagnostic signals; no visible dashboard alone proves quality.
10. Review policy itself is judge-affecting and requires meta-review/verification before weakening.
11. The current one-agent environment may use the canonical degraded mode but must retain explicit trust debt.
12. All `main` integration remains squash-only.

## 7. Assumptions

Provisional assumptions:

- Recording multiple trust dimensions is more useful than a boolean “independent” field while still small enough for machine validation.
- Most planning/implementation work can use adversarial review plus claim-appropriate verification without hidden tests everywhere.
- High-Goodhart surfaces benefit from at least one oracle/evidence source the producer cannot modify.
- Reviewer findings become more actionable when tied to exact claims/failure scenarios rather than global impressions.
- Disagreement can often be reduced by collecting discriminating evidence rather than adding more unconstrained opinions.
- Role-specific permissions can eventually enforce part of the trust boundary, but current one-agent operations will remain partly procedural.

## 8. Alternatives considered

### 8.1 Boolean `independent: true/false` — rejected

It hides materially different failure modes. A reviewer may have separate context but still edit the candidate or own every evaluator.

### 8.2 One universal two-review rule — rejected

Low-risk local work would serialize unnecessarily, while high-risk judge-affecting work could still be under-protected. Use task/risk-specific classes and dimensions.

### 8.3 Producer tests plus CI green = verified — rejected

The producer can unintentionally or strategically encode the same mistaken interpretation in implementation and tests. Independent/specification-derived/integration evidence is required for material claims.

### 8.4 Majority vote of judges — rejected

Correlated judges can agree for the same wrong reason; votes do not identify which evidence distinguishes candidates. Preserve disagreement and seek discriminating evidence.

### 8.5 Hide every verifier test — rejected

Full secrecy reduces debuggability and can create opaque failures. Protect only surfaces where gaming risk warrants it; visible invariant/specification tests remain valuable.

### 8.6 Human tie-breaker on uncertainty — rejected as default

Contradicts the autonomous factory. Escalate through additional evidence, adversarial evaluation, competing alternatives, and replanning.

### 8.7 Same-session self-review with a new prompt — rejected as independent

It may be a useful self-check but cannot satisfy an independence gate. Under one-agent operation use the explicit degraded protocol and label it accordingly.

## 9. Proposed trust model

### 9.1 Trust dimensions

For each judging episode record:

| Dimension | Meaning | Failure example |
|---|---|---|
| `AUTHORSHIP` | judge did not author the exact candidate under judgment | producer reviews own artifact |
| `PRIVATE_CONTEXT` | judge starts from bounded repo/GitHub packet rather than producer private reasoning | same chat continues with hidden producer rationale |
| `CANDIDATE_WRITE` | judge cannot/does not edit candidate while issuing judgment | verifier fixes candidate then passes it |
| `ORACLE_CONTROL` | judge/producer cannot freely rewrite the sole oracle/evaluator used for PASS | implementer changes held-out threshold |
| `EVIDENCE_SOURCE` | at least required evidence is independently derived/reproduced rather than copied from producer claim | review cites producer summary only |

Optional future dimensions may include platform identity, organization/account separation, or environment isolation if evidence shows they matter.

### 9.2 Trust profiles

#### `NOT_INDEPENDENT`

Used for producer self-checks or same-context critique. Useful evidence, but cannot satisfy an independent review/verification requirement.

#### `DEGRADED_SINGLE_AGENT`

Current liveness fallback when only one project agent/context capability is available. Required minimum:

- new episode identity;
- exact candidate frozen and candidate editing prohibited;
- cold-start input manifest from repository + GitHub state;
- prior-rationale gate until initial evidence/attack plan exists;
- explicit prior role history/resource-constraint reference;
- new evidence/reproduction before reconciling producer claims;
- trust level recorded as DEGRADED;
- reopen condition when isolated/multi-agent execution is available.

This satisfies only tasks whose canonical policy explicitly permits degraded mode.

#### `FULL_INDEPENDENT_CONTEXT`

Minimum target when platform capability exists:

- distinct execution context/actor identity from producer;
- no producer private-context dependency;
- candidate immutable to verifier during judgment;
- independent evidence acquisition;
- role/permission separation appropriate to claim class.

“Full” here means full against the declared project dimensions, not philosophical proof of model independence.

#### `PROTECTED`

Adds protected oracle/evaluator or permission boundary appropriate to Goodhart/high-impact risk. Exact protection can be service-, repository-, permission-, or held-out-data-based and must be auditable/versioned.

## 10. Review and verification classes

| Class | Purpose | Candidate mutation | Typical evidence | Result |
|---|---|---:|---|---|
| `SELF_CHECK` | catch obvious producer defects before handoff | producer may edit | local checks, consistency review | not an independent gate |
| `ADVERSARIAL_REVIEW` | try to invalidate design/spec/implementation claims | reviewer does not edit candidate | exact artifacts, failure scenarios, targeted evidence | findings + disposition |
| `CROSS_DOMAIN_REVIEW` | find interface/dependency/concurrency contradictions across reviewed candidates | no candidate editing | exact synthesis states, interface graph, scenario attacks | findings + disposition |
| `INDEPENDENT_VERIFICATION` | reproduce/test acceptance of exact candidate/base | verifier cannot edit candidate | executable/scenario/invariant/evidence bundle | PASS/FAIL |
| `PROTECTED_VERIFICATION` | resist gaming for sensitive/high-impact claims | verifier cannot edit candidate or protected oracle | held-out/protected tests, independently controlled checks, adversarial probes | PASS/FAIL |
| `META_VERIFICATION` | judge changes to review/verifier/evaluator/metrics/permissions | candidate policy frozen | before/after benchmark, escape tests, protected checks, rollback evidence | PASS/FAIL/adopt/reject |

Task contracts declare required classes. A risk/governance rule may escalate to a stronger class; a producer cannot downgrade the declared route to accelerate integration.

## 11. Finding and disposition model

Recommended finding schema:

```yaml
finding_id: <stable>
severity: BLOCKER | MAJOR | MINOR | NOTE
claim_under_attack: <exact claim/acceptance/interface>
candidate_ref: <work sha/path>
failure_scenario: <concrete>
evidence_refs: []
observed_vs_inferred: <distinction>
correction_or_question: <bounded>
disposition: OPEN | ACCEPTED | REJECTED_WITH_EVIDENCE | DEFERRED_EXPERIMENT | INVALIDATES_CANDIDATE
```

Severity semantics:

- **BLOCKER** — proceeding would make acceptance/canonicalization unsafe or logically invalid.
- **MAJOR** — material quality/correctness/architecture/trust risk requiring correction or explicit bounded evidence before acceptance.
- **MINOR** — useful correction not required to establish the central acceptance claim.
- **NOTE** — observation/question/provenance with no current acceptance block.

A PASS is forbidden while required-route BLOCKER/MAJOR findings are unresolved.

## 12. Evidence sufficiency by claim type

Evidence is claim-specific; use the minimum diverse set sufficient to falsify material failure modes.

| Claim type | Minimum evidence direction | Additional evidence when risk/gaming is high |
|---|---|---|
| pure planning/protocol coherence | exact artifacts/SHAs, dependency/state simulation, adversarial failure scenarios | cold-start substitution, race simulation, independent attack |
| code correctness | build/unit/property checks + specification-derived behavior evidence | independent tests, integration scenario, fuzz/property/held-out cases |
| real integration | real executable/kernel path, environment/build SHA, deterministic/replayable scenario where practical | protected scenarios, independent traces, fault injection |
| persistence/determinism | initial state/seed/actions/final hashes/save-load evidence | cross-version/replay/property tests, corruption/migration cases |
| architecture/interface | module/dependency graph + contract/integration checks | static policy oracle, conflict/concurrency simulation, independent architecture review |
| UX/visual | task trace + player surface evidence + objective visual/accessibility checks | randomized pairwise multimodal judges, held-out scenarios, disagreement analysis |
| economy/progression/game quality | simulation surface + synthetic-player cohorts + multidimensional telemetry | exploit search, protected cohorts/scenarios, subjective panels, candidate comparison |
| performance | reproducible benchmark env/build/workload + distribution | independent rerun, regression baseline, stress/long-run cases |
| factory protocol / evaluator change | before/after benchmark + seeded defects/reward-hacking probes + rollback | protected meta-evaluation, independent verification |

Producer-authored evidence may be part of the bundle but cannot be the sole evidence for important integration/quality claims.

## 13. Evidence Bundle

A material review/verification result should bind an `EvidenceBundle` conceptually containing:

```yaml
claim_set_id: <task acceptance/version>
candidate:
  work_sha: <sha>
  head_sha: <sha>
  base_main_sha: <sha>
environment_refs: []
evidence_items:
  - evidence_id: <id>
    kind: TEST | SCENARIO | INVARIANT | TRACE | SIMULATION | VISUAL | BENCHMARK | REVIEW | OTHER
    artifact_ref: <immutable ref>
    producer: <actor/tool>
    evaluator_version: <if relevant>
    input_hashes: []
    result: <structured>
independence_profile: <trust profile>
known_coverage_gaps: []
```

Evidence without candidate/base binding can become stale. Mutable URLs/dashboards should have an immutable snapshot/hash or be treated as observational context rather than final proof.

## 14. Candidate immutability and permission boundaries

Target role capabilities:

### Producer

- writes task-owned candidate branch/surface;
- may write producer tests/check evidence;
- cannot write protected verifier oracle/configuration used as sole acceptance gate;
- cannot publish the final independent PASS for its own work.

### Reviewer

- writes separate findings/review artifact/status;
- candidate under review is read-only for the review episode;
- requested corrections route to producer/synthesizer/reviser ownership.

### Verifier

- candidate is read-only;
- writes verification evidence/report/status;
- may run protected/held-out evaluators through a controlled interface;
- cannot weaken required checks/thresholds for the candidate it judges.

### Integrator

- may apply only verified deterministic promotion/approved transformation;
- cannot introduce unverified semantic edits while still referencing the old PASS.

### Meta-evaluator maintainer

- changes protected tests/evaluators/rubrics/metrics only through a separate judge-affecting change task with before/after benchmark, review, verification, and rollback.

Where platform permissions cannot enforce these boundaries, the result records `enforcement: PROCEDURAL` and trust debt. W1-FAC-02/FAC-04 should later identify enforceable permission splits.

## 15. Protected evaluation strategy

Use protection proportional to gaming risk.

### P0 — visible specification/evidence

Public tests, invariants, scenarios, rubrics. Best for debuggability and shared specification.

### P1 — independent authorship/control

Tests/scenarios are visible but authored/maintained outside the producer role and cannot be modified by the current task owner.

### P2 — held-out/protected oracle

Some test data/scenarios/evaluator configuration is withheld or permission-protected from the producer. Results still need enough diagnostics/evidence to support remediation without exposing all holdout details.

Recommended protected surfaces include only high-value or gaming-sensitive subsets:

- reward-hacking/specification-gaming probes;
- canonical architecture policies;
- representative held-out gameplay scenarios;
- verifier configuration/threshold policy;
- factory benchmark seeded defects;
- selected regression/golden scenarios where disclosure would make the check trivial to game.

Protected does not mean unversioned or unaccountable. Every oracle has owner, version, change history, input/evidence provenance, and meta-review route.

## 16. Evaluator versioning

Any machine/subjective evaluator result used materially should record enough to replay or interpret drift:

```yaml
evaluator_id: <stable>
evaluator_version: <config/model/rubric version>
rubric_or_policy_ref: <immutable ref>
input_evidence_hashes: []
run_environment_ref: <when relevant>
randomization_seed_or_order: <when relevant>
result: <structured>
confidence_or_uncertainty: <optional, not authority alone>
disagreement_group: <optional>
```

A changed evaluator version does not retroactively invalidate every prior decision, but it can trigger a reopen condition if benchmark evidence shows material escape/decision differences.

## 17. Disagreement protocol

When valid reviewers/evaluators disagree:

1. normalize the exact candidate/claim/evidence each judged;
2. determine whether disagreement is factual, interpretive, risk-tolerance, evaluator-version, or coverage-related;
3. preserve both judgments and rationales;
4. identify discriminating evidence that could make one failure model more or less plausible;
5. run targeted runtime/simulation/protected/independent evidence collection;
6. if subjective, use structured rubrics, randomized order, pairwise comparison, and additional independent judge runs rather than free-form votes;
7. if alternatives remain plausible, synthesize competing candidates/experiments rather than forcing false certainty;
8. if a BLOCKER/MAJOR cannot be dispositioned with evidence, candidate does not pass;
9. checkpoint/replan if the disagreement exposes a missing specification/evaluator.

Human opinion may arrive as an external directive/evidence source, but it is not the default tie-break path.

## 18. Anti-Goodhart controls

1. **Multiple signals:** no single metric/check/dashboard is sufficient for multidimensional quality.
2. **Protected subset:** keep some high-value probes outside producer control where gaming risk warrants it.
3. **Adversarial search:** explicitly search for cases that satisfy visible metrics while violating intent.
4. **Metric/evaluator versioning:** record changes and compare decision drift.
5. **Randomization/holdout rotation:** where useful, vary cases/order to reduce rote tuning.
6. **Independent evidence source:** at least one required source for material claims should not be producer-authored/reported.
7. **Disagreement monitoring:** collapsing disagreement to zero can itself be suspicious.
8. **No optimization target from diagnostics:** review counts, pass rate, benchmark score, or escape rate should not become a single reward objective.
9. **Meta-review:** evaluator/metric changes are judge-affecting and require separate verification.

## 19. Integration eligibility

A task may enter verified integration/canonicalization only when all canonical requirements for its class are true, including:

```text
exact candidate work/head identified
AND required review classes complete
AND every required BLOCKER/MAJOR disposition acceptable
AND required evidence bundle exists and passes
AND required independent/protected trust profile is satisfied (or explicit canonical degraded mode permits it)
AND verification PASS binds exact candidate + evidence + current base
AND candidate/base/evaluator state has not drifted outside allowed refresh rules
AND required protected checks/statuses pass
AND PR head equals expected verified head
AND current main equals verified base or valid refresh/reverification covers it
AND integrator transformation is exactly allowed
AND squash-only integration rule is satisfied
```

A review `PASS_FOR_SYNTHESIS` is not integration PASS. A green CI status is not canonicality. A merged PR without the required verification provenance is not an accepted integration under this model.

## 20. Review routing by risk/claim

Candidate policy shape:

| Work class | Minimum route |
|---|---|
| local low-risk change with strong deterministic tests | producer SELF_CHECK + required code/integration review as task contract specifies |
| design/planning proposal | ADVERSARIAL_REVIEW → synthesis/revision; verification at canonicalization boundary |
| cross-domain architecture | domain reviews + CROSS_DOMAIN_REVIEW → synthesis → INDEPENDENT_VERIFICATION |
| gameplay/economy/UX quality decision | independent review + multi-surface evidence; PROTECTED_VERIFICATION where metric gaming/coverage risk is material |
| canonical integration/release-critical change | INDEPENDENT_VERIFICATION + exact-base/head integration checks |
| verifier/evaluator/metric/permission/constitution change | META_VERIFICATION with before/after escape benchmark and rollback |

This is a minimum framework; the canonical task compiler may require stronger routes for a specific mission.

## 21. Observability and evaluation

Track diagnostics by review class/trust profile:

- BLOCKER/MAJOR findings per review and later escape rate;
- defect types found by producer vs reviewer vs verifier vs protected oracle;
- false-positive/rejected-finding rate with evidence reason;
- reviewer disagreement rate and time/evidence to disposition;
- findings reopened after later evidence;
- candidate mutation attempted during review/verification;
- evaluator/protected-surface change attempts by judged producers;
- results produced under NOT_INDEPENDENT / DEGRADED / FULL / PROTECTED profiles;
- DEGRADED decisions awaiting stronger audit;
- self-authored-test-only acceptance attempts blocked;
- evidence bundle missing/stale/base-drift failures;
- evaluator version decision drift;
- protected holdout escape detection versus visible tests;
- specification-gaming/reward-hacking probe findings;
- review/verification queue age and READY-frontier effect;
- meta-verification rollback/adoption outcomes.

Do not optimize for fewer findings, higher pass rate, or lower disagreement. Measure whether later independent evidence confirms or escapes the review system.

## 22. Bounded experiments

| ID | Experiment | Pass signal | Failure implication |
|---|---|---|---|
| FAC3-E1 | Seed known BLOCKER/MAJOR defects into representative planning/code candidates; blind/degraded/full reviewers attack them | high-severity injected defects reliably found and correctly localized | review classes/context/evidence insufficient |
| FAC3-E2 | Candidate-write permission red-team during verification | verifier cannot/does not modify candidate then reuse same PASS; mutation invalidates/restarts result | candidate immutability boundary weak |
| FAC3-E3 | Reviewer disagreement tournament with intentionally ambiguous evidence | protocol identifies discriminating evidence and either resolves or preserves justified uncertainty without majority/human default | disagreement process cosmetic |
| FAC3-E4 | Goodhart challenge: candidate optimized to visible metric/tests while violating intent | adversarial/protected evidence detects gaming | oracle diversity/protection insufficient |
| FAC3-E5 | Evaluator-version replay on frozen evidence set | drift is measurable and triggers defined review/reopen thresholds rather than silent reinterpretation | evaluator provenance inadequate |
| FAC3-E6 | Protected-evidence leakage/permission probe | producer cannot access/modify protected oracle beyond declared diagnostics | protected boundary unenforced |
| FAC3-E7 | Base/head drift after PASS | integration rejects stale PASS and routes refresh/reverification | verification binding incomplete |
| FAC3-E8 | When isolation/multiple agents available, replay prior DEGRADED decisions with FULL/PROTECTED profiles | escape/disagreement delta identifies which trust debt needs re-review | degraded mode may be overtrusted |
| FAC3-E9 | Review-queue load benchmark | stronger review classes improve escape detection without collapsing useful throughput/frontier beyond acceptable measured cost | routing over-serializes factory |

## 23. Failure modes and defenses

### Reviewer as editor
**Failure:** reviewer fixes the candidate and then approves it.  
**Defense:** read-only candidate during judging; changes route to reviser/synthesizer ownership.

### Session-ID independence laundering
**Failure:** same private reasoning continues under a new UUID.  
**Defense:** trust dimensions, cold-start packet, prior-rationale gate, explicit degraded profile.

### Self-authored oracle monoculture
**Failure:** implementation and tests share the same mistaken specification.  
**Defense:** independent/specification-derived/integration/protected evidence mix.

### Protected-oracle capture
**Failure:** producer can modify hidden tests/thresholds.  
**Defense:** permission separation and judge-affecting meta-change route.

### Hidden evaluator drift
**Failure:** verdict changes because rubric/model/config changed, not product.  
**Defense:** evaluator version + frozen evidence replay/benchmark.

### Majority-vote certainty
**Failure:** correlated judges agree or disagree without evidence resolution.  
**Defense:** discriminating evidence and structured comparison; preserve dissent.

### Visible metric gaming
**Failure:** work optimizes dashboard while violating intent.  
**Defense:** multi-signal, adversarial, protected/held-out, randomization, meta-review.

### Evidence laundering
**Failure:** reviewer repeats producer's evidence summary as independent proof.  
**Defense:** evidence-source dimension and independent reproduction requirement.

### PASS floats across base/candidate drift
**Failure:** integration uses result for state not verified.  
**Defense:** exact work/head/base/evaluator binding + refresh/restart lifecycle.

### Review as routine human gate
**Failure:** disagreement/uncertainty waits for owner.  
**Defense:** machine escalation path and explicit no-human-default rule.

### Excessive protection
**Failure:** every check becomes hidden, opaque, and hard to debug.  
**Defense:** protect only gaming-sensitive subsets; retain visible specification/invariant evidence.

### Review serialization collapse
**Failure:** quality queues throttle all useful parallel work.  
**Defense:** risk-based routing, WIP/scheduler coordination, benchmark FAC3-E9, parallel independent reviews where conflict-free.

## 24. Risks

- Trust-profile complexity can become ceremony; automate derivation from task/permission/evidence metadata where possible.
- Protected tests can become stale or wrong; they require versioning, ownership, meta-review, and challenge mechanisms.
- One-agent degraded mode has correlated failure risk that no procedural separation fully removes.
- Subjective evaluator panels can share model/provider biases; diversity must be measured rather than assumed.
- Strict candidate immutability can slow trivial fixes; correctness of the authority boundary matters more than saving one review loop for high-risk gates.
- Evidence bundles may become large; FAC-04 should use stable artifact refs/indexes rather than injecting all evidence into context.
- Permission enforcement may vary by GitHub/account/tool capability; unsupported boundaries must remain explicit procedural trust debt.

## 25. Open questions

1. Which concrete trust-profile dimensions should be mechanically derivable versus self-reported?
2. Which task/risk classes require PROTECTED rather than FULL independent verification?
3. Where should protected scenarios/evaluators live, and how can agents receive actionable failure evidence without leaking the holdout?
4. What permission split can make reviewer/verifier candidate-write prohibition enforceable in GitHub/tooling?
5. How many independently authored tests/scenarios are enough for each claim class before marginal benefit falls?
6. What benchmark escape rates justify upgrading/downgrading a review route?
7. How should evaluator disagreement thresholds trigger more evidence versus alternative candidate generation?
8. Which past DEGRADED decisions must be replayed when stronger isolation becomes available?
9. How can protected evaluator changes be tested without exposing all future reward-hacking probes?
10. What evidence retention is required to replay older verdicts under a new evaluator version?

## 26. Reopen conditions

Reopen if:

- reviewer/verifier roles can mutate the candidate without invalidating their judgment;
- important claims repeatedly pass only producer-authored evidence and later escape;
- seeded-defect benchmarks show low independent detection;
- `DEGRADED_SINGLE_AGENT` is treated operationally or rhetorically as FULL independence;
- protected checks are writable/visible in ways that make gaming trivial;
- evaluator version changes materially alter decisions without detectable provenance;
- disagreement repeatedly resolves by unsupported majority vote or human escalation;
- evidence bundles cannot reproduce claimed PASS state;
- stale-base/candidate/evaluator results reach integration;
- review queues materially collapse verified throughput without corresponding escape reduction;
- a metric/check becomes a de facto sole quality oracle;
- stronger isolation/permission capabilities become available and current procedural boundaries can be enforced more strongly.

## 27. Required independent critique

`W1-REV-FAC` should attack review-routing cost, role laundering, hidden human gates, factory self-modification, WIP/parallelism effects, and whether DEGRADED mode is too permissive.

`W1-REV-TECH` should attack candidate/evidence binding, permission enforceability, protected-oracle implementation assumptions, evaluator/version provenance, base/head freshness, and whether proposed evidence classes are executable/reproducible.

Both reviewers should attempt seeded Goodhart and self-approval scenarios rather than only inspect the prose model.

## 28. Downstream work unblocked

This proposal supplies required inputs to `W1-REV-FAC` and `W1-REV-TECH`, and trust/evidence interfaces for W1-FAC-02, W1-FAC-04, W1-EVAL-01, and later synthesis.

It creates no protected infrastructure, additional current-wave issues, or canonical policy by authorship. Any adopted trust/evaluator/permission system must follow the Wave 1 review/synthesis/verification/canonicalization route.