# Factory and Governance Synthesis Candidate — Wave 1

**Mission:** `W1-SYN-FAC`  
**State:** SYNTHESIS CANDIDATE / NON-CANONICAL  
**Review input disposition:** `W1-REV-FAC = CHANGES_REQUIRED`  
**Required next review:** `W1-REV-CROSS`  
**Trust:** `DEGRADED_SINGLE_AGENT`

## Review Index

This synthesis **accepts and corrects** review finding `FG-B01` and every `FG-M02`–`FG-M08`. It does not rewrite producer branches. Instead it defines eight cross-cutting interfaces that close the gaps between governance, task lifecycle, control plane, trust, and CI/evidence:

1. `ActiveDirectiveSet` — machine-valid scoped human directives become an explicit state-snapshot/READY/claim/integration input.
2. `LockExpansion` — an active task may not mutate a newly discovered conflict surface until additional conflict keys are atomically acquired or the work is rerouted.
3. `PolicyEpoch` — active policy version N judges candidate N+1; a candidate policy has zero authority over its own adoption gate.
4. `TrustDebt` — DEGRADED results produce a discoverable debt record with capability-triggered stronger audit/reverification.
5. `EvidenceRequirement` / `EvidenceSatisfaction` — one content-addressed claim contract bridges review trust, CI outcomes/quarantine, and scheduler/integration eligibility.
6. `RiskFloor` — machine-derived non-downgradable minimum review/verification routes for judge-affecting, canonical/systemic, protected/permission, legal/external-sensitive, destructive, and broad-fan-out work.
7. `RetentionEdge` / `ProvenanceAnchor` — any downstream-consumed work/evidence SHA blocks branch/ref/artifact GC until durable reachability is proven.
8. `ArtifactIdentity` — provenance/rights policy and evidence/retention records reference one content identity so quarantined material cannot re-enter through an evidence alias.

`FG-m09` is accepted: the FAC2 GraphQL multi-ref ownership/conflict-lock design is **EXPERIMENTAL_NOT_ADOPTABLE** until its claim/crash/lease spikes pass. Current canonical schema-3 fencing remains the fallback. `FG-m10` and `FG-m11` are also corrected by context-policy hashes and predicate-aware dependency projections. CI/evaluator service incidents and quality-queue metrics remain explicit measurement obligations.

The synthesis preserves: no routine human approval, repository-owned memory, exact candidate/base evidence binding, candidate immutability under judgment, squash-only `main`, bounded context, reviewed evidence rather than green-status compression, and the implementation-readiness barrier.

## 1. Status and exact inputs

This document synthesizes the exact immutable inputs frozen in `docs/planning/wave-1/synthesis/factory-governance-input.yaml`:

| Mission | work SHA |
|---|---|
| W1-GOV-01 | `ffa6b62b3b20c84a152e676b7a5db223daa130e5` |
| W1-FAC-01 | `e7fe3d0eaae22038e661ea941e652a618c3a7ec7` |
| W1-FAC-02 | `095372a41498e8d7e3b25364cba89dbc647b8839` |
| W1-FAC-03 | `70b763a965cdec0fa1f6c025a5b7492b844288fc` |
| W1-FAC-04 | `99b0c7b3bddbad1a71e05f085fd0bd9f2c74e566` |
| W1-REV-FAC | `4ffa7fd8a175bae504280160e8c48a508909e6f3` |

Review status comment `5245732114` records `CHANGES_REQUIRED`, 1 BLOCKER / 7 MAJOR.

This candidate is not a replacement for the producer artifacts as provenance. It is the correction/reconciliation surface that later cross-domain review and final synthesis may accept, revise, or invalidate.

## 2. Scope

The candidate defines the integrated governance/factory semantics for:

- authority and material human directives;
- persistent task / disposable episode lifecycle;
- context, continuation, handoff, and discovered work;
- ownership/conflict expansion and mature-control-plane migration;
- risk classification and review/verification routing;
- trust profiles, protected evidence, and trust debt;
- evidence requirements/satisfaction, CI result semantics, and quarantine;
- shared artifact identity/provenance and evidence retention;
- judge-affecting self-modification/version activation;
- scheduler/WIP/READY inputs and liveness;
- garbage collection/provenance anchors;
- factory measurement and protocol-change experiments.

## 3. Non-goals

This synthesis does not:

- install a GitHub App, ruleset, CI service, artifact store, or protected evaluator;
- claim the proposed GraphQL ref-lock transaction is proven;
- choose a final lease timestamp store;
- set numeric WIP thresholds without evidence;
- settle jurisdiction/provider/license law;
- make DEGRADED_SINGLE_AGENT equivalent to isolated independent review;
- create gameplay implementation authority;
- canonicalize itself.

## 4. Adopted producer principles

The following producer conclusions are adopted unless cross-domain review later rejects them:

### 4.1 Governance

- scope-aware explicit authority hierarchy;
- material human directives are durable typed records, not hidden conversational dependencies;
- canonicality is explicit and not inferred from path/merge/closure;
- higher risk means stronger evidence/separation, not routine human sign-off;
- judge-affecting changes require a separate factory-change route;
- unresolved rights/provenance routes to quarantine/research, not silent allow or global stop;
- governance metrics remain diagnostic and Goodhart-resistant.

### 4.2 Operating model

- Task is persistent; Episode is disposable;
- one normal mutation owner per task unless coordinated structure is explicit;
- deterministic task branch persists across episodes;
- handoff is evidence/navigation, not ownership authority;
- continuation re-derives canonical/branch/status/evidence before mutation;
- context widens only for named questions/triggers;
- useful work is committed before stop;
- discovered work is typed/bounded and does not auto-create active backlog.

### 4.3 Control plane

- content-addressed canonical graph/contracts are authority;
- GitHub native dependencies/Projects/labels/assignees are mirrors/projections unless canonical policy grants a narrower role;
- READY is derived from exact authoritative state;
- current-base verification and expected-head merge checks are separate invariants;
- `main` is squash-only;
- control-plane automation uses least privilege and reconciliation from durable state;
- scheduler uses deterministic class-first selection and versioned WIP policy, not an opaque scalar.

### 4.4 Trust / verification

- independence is multidimensional, not a UUID/boolean;
- same-context self-check is not independent;
- DEGRADED_SINGLE_AGENT is explicit trust debt;
- verifier/reviewer may not edit the exact candidate they judge;
- material claims require claim-appropriate diversified evidence, not producer tests alone;
- protected oracles are selective, versioned, and meta-governed;
- disagreement routes through discriminating evidence/replanning, not majority/human default;
- integration PASS binds exact candidate/base/evaluator/evidence state.

### 4.5 CI / evidence / measurement

- CI is a structured evidence sensorium;
- Run Reports and evidence artifacts bind exact candidate/base/environment/evaluator versions;
- `FLAKY`, `INCONCLUSIVE`, and `NOT_RUN` are not PASS;
- retries never erase attempts;
- task-specific evidence classes are declared by contract;
- large evidence uses durable refs/indexes rather than context preload;
- canonical/protected evidence receives authority-aware retention;
- factory protocols are benchmarked on quality/escape/flow/recovery/trust tradeoffs, not activity volume.

## 5. Review finding dispositions

### FG-B01 — ACCEPTED_AND_CORRECTED

**Problem:** governance makes material scoped human directives highest authority, but the control-plane READY/claim proof did not bind the active directive set.

**Correction:** define `ActiveDirectiveSet` as a mandatory input to any authoritative state snapshot after a material directive exists.

```yaml
ActiveDirectiveSet:
  version: 1
  set_id: <content hash / immutable state ref>
  evaluated_through: <server-authoritative event/ref>
  directives:
    - directive_id: <stable>
      kind: EMERGENCY_SAFETY | PROJECT_DIRECTION | RESOURCE_CONSTRAINT | PRIORITY | EXPERIMENTAL
      issuer_authority: human_owner
      source_ref: <immutable issue/comment/record ref>
      scope:
        missions: []
        paths: []
        decisions: []
        conflict_keys: []
      statement_hash: <hash of bounded durable statement>
      created_at: <authoritative timestamp>
      supersedes: []
      expires_or_review_condition: null
      state: ACTIVE | SUPERSEDED | EXPIRED
  validation:
    duplicate_or_ambiguous_scope: FAIL_CLOSED
    hidden_chat_only_directive: NOT_DURABLE_AUTHORITY
```

Control-plane state/`ready_proof`/claim/recovery/integration records MUST bind `active_directive_set_id` when a material directive set exists. Eligibility and priority are derived after applying scoped active directives.

**Emergency rule:** an explicit safety stop may halt affected mutation immediately. Before resumption/downstream automation depends on that stop, the bounded durable directive record must exist. The no-routine-human-gate principle remains intact: absence of a directive never blocks work.

### FG-M02 — ACCEPTED_AND_CORRECTED

**Problem:** FAC1 can absorb newly discovered required work, but FAC2 conflict keys were acquired only at ownership acquisition.

**Correction:** add `LOCK_EXPAND` semantics to the mature control plane.

```yaml
LockExpansion:
  task: <id>
  ownership_generation: <current>
  observed_head_sha: <current task head>
  existing_conflict_keys: []
  requested_additional_keys: []
  reason_ref: <discovery/scope-decision>
  context_or_review_scope_change: <declared>
```

Before the **first mutation** touching a surface not covered by the current lock set:

1. prove the work is necessary/bounded under FAC1 absorption rules;
2. derive new conflict keys;
3. acquire all added keys atomically against current task ownership/head using the canonical lock mechanism;
4. publish the expansion result and update the task context/review scope;
5. only then mutate.

Failure to acquire means block/reroute as discovered work. A local “conflict-safe” assertion is never enough.

Until the ref-lock experiment is adopted, scope that needs a new conflict key is conservatively **not absorbable** unless the current canonical schema/control plane can represent and fence it; route it instead.

### FG-M03 — ACCEPTED_AND_CORRECTED

**Problem:** judge-affecting policy N+1 could ambiguously choose the review/evaluator policy used to judge its own activation.

**Correction:** define `PolicyEpoch` and the invariant **old policy judges new policy**.

```yaml
PolicyEpoch:
  active_policy_id: N
  candidate_policy_id: N_plus_1
  candidate_authority_before_activation: NONE
  evaluation_policy_id: N
  benchmark_policy_ref: <under N>
  verifier_route_ref: <under N>
  previous_policy_id: N
  rollback_target: N
```

Rules:

- active N defines task compilation, risk floor, required review, evidence requirements, protected evaluator/permission rules, and promotion semantics for N+1;
- N+1 may be simulated in a benchmark but cannot weaken the gate judging itself;
- if N is itself broken such that evaluation is impossible, only a higher explicit canonical/human directive or separately verified emergency recovery protocol may replace the gate; the candidate cannot self-authorize;
- after PASS/integration, terminal state atomically/explicitly changes active policy to N+1 and retains N as rollback/provenance;
- rollback follows the old/current canonical governance route and is evidence-bearing.

This rule applies to scheduler, reviewer/verifier, evaluator, metrics, permissions, context policy, WIP policy, merge/integration policy, and other judge-affecting surfaces.

### FG-M04 — ACCEPTED_AND_CORRECTED

**Problem:** DEGRADED results create trust debt but no authoritative machine-discoverable debt ledger.

**Correction:** define `TrustDebt`.

```yaml
TrustDebt:
  debt_id: <stable>
  subject_ref: <exact review/verification/decision result>
  subject_authority_state: <reviewed/verified/canonical/etc>
  current_profile: DEGRADED_SINGLE_AGENT
  target_profile: FULL_INDEPENDENT_CONTEXT | PROTECTED
  reason_ref: <resource constraint / capability absence>
  affected_downstream_authority_refs: []
  severity: <risk-derived>
  opened_at: <ref/time>
  reopen_trigger: MULTI_AGENT_OR_ISOLATED_CONTEXT_AVAILABLE | <other capability>
  state: OPEN | IN_REVIEW | CLOSED | SUPERSEDED
  closing_result_ref: null
```

A canonical **Trust Debt Index** is derivable from active authority/provenance and MUST remain queryable independent of issue closure. When a recorded capability/resource state satisfies a debt trigger, the scheduler exposes bounded audit/reverification work in the quality pipeline before comparable new production according to risk/impact priority.

Closing debt requires a stronger valid result or explicit reviewed supersession/invalidation. It never disappears because the original task closed.

### FG-M05 — ACCEPTED_AND_CORRECTED

**Problem:** FAC3 evidence sufficiency, FAC4 evidence/check/quarantine semantics, and FAC2 READY/integration did not share one machine contract.

**Correction:** define versioned `EvidenceRequirement` + `EvidenceSatisfaction` per acceptance claim.

```yaml
EvidenceRequirement:
  requirement_id: <content-addressed>
  claim_id: <stable task acceptance claim>
  requirement_version: <version/hash>
  candidate_scope: <task/candidate kind>
  required_items:
    - requirement_item_id: <id>
      evidence_kinds: []
      ci_classes: []
      allowed_results: [PASS]
      minimum_trust_profile: <profile/rule>
      evaluator_or_check_versions: []
      protected_level: P0 | P1 | P2 | null
      semantic_coverage_predicate: null
      applicability_predicate: <typed>
      substitution_policy:
        allowed: false
        alternatives: []
  aggregation_rule: <typed, versioned>
  policy_epoch: <id>
```

```yaml
EvidenceSatisfaction:
  requirement_id: <exact>
  candidate_work_sha: <sha>
  base_main_sha: <sha>
  evidence_refs: []
  run_report_refs: []
  evaluator_refs: []
  independence_profile: <typed>
  item_results: []
  coverage_gaps: []
  result: SATISFIED | UNSATISFIED | INCONCLUSIVE
```

Rules:

- `FLAKY`, `INCONCLUSIVE`, `NOT_RUN` cannot satisfy an item requiring PASS;
- a replacement/quarantine path is valid only if already enumerated by the same requirement version, or a judge-affecting reviewed change creates a new requirement version;
- FAC2 READY/integration consumes `EvidenceSatisfaction`, not raw dashboard status;
- FAC3 verifier judgment cites the same object;
- FAC4 Run Reports/Evidence Index provide the underlying evidence;
- stale candidate/base/evaluator/policy version invalidates satisfaction according to canonical refresh/restart rules.

### FG-M06 — ACCEPTED_AND_CORRECTED

**Problem:** qualitative risk tiers could be producer-downgraded.

**Correction:** define a compiler/control-plane `RiskFloor` before ownership/review route selection.

Minimum non-downgradable triggers:

| Trigger | Minimum route implication |
|---|---|
| modifies judge-affecting surface | `META_VERIFICATION`; risk ≥ R2 |
| changes canonical authority/dispatcher/integration semantics | adversarial review + independent verification; risk ≥ R2 |
| changes protected oracle/evaluator/permission boundary | protected/meta verification; risk ≥ R3 |
| external/legal/provenance-sensitive shipping policy | authoritative evidence + independent review; risk ≥ R2/R3 by blast radius |
| destructive/irreversible migration or release-critical surface | independent verification + rollback/migration evidence; risk ≥ R3 |
| broad cross-domain authority/dependency fan-out | cross-domain review + verification; risk ≥ R2 |

The task compiler/control plane computes the floor from declared owned paths/change classes plus later detected scope expansion. A producer may request stronger review, never a weaker route. Material ambiguity fails upward or creates a bounded classification review; it does not default to R0/R1.

Risk classification result is versioned and included in the task contract/READY proof. Lock expansion or scope changes can raise the floor and therefore the required review route.

### FG-M07 — ACCEPTED_AND_CORRECTED

**Problem:** exact producer/review work SHAs can lose reachability after branch/ref cleanup.

**Correction:** downstream consumption creates a `RetentionEdge`, and material authority creates a `ProvenanceAnchor`.

```yaml
RetentionEdge:
  consumer_ref: <review/synthesis/verification/canonical decision>
  consumed_object:
    type: GIT_COMMIT | GIT_BLOB | EVIDENCE_ARTIFACT | RUN_REPORT | PROTECTED_ARTIFACT
    identity: <sha/hash>
  retention_class: TASK_EVIDENCE | CANONICAL_PROVENANCE | PROTECTED_EVALUATION
  state: ACTIVE | RELEASED_BY_SUPERSESSION
```

```yaml
ProvenanceAnchor:
  authority_ref: <result/decision>
  retained_refs_or_snapshots: []
  authority_graph_hash: <hash>
  retention_policy_version: <ref>
```

GC rules:

- branch/ref deletion requires proving every active consumed Git/evidence object remains reachable through an explicit retained ref or content-addressed durable snapshot;
- PR/issue number alone is not proof of object retention;
- GC runs CAS against expected ownership/retention graph state;
- canonical/protected evidence cannot be compacted/deleted without a separately reviewed retention-policy transition preserving verifiability;
- supersession may release an edge only if no remaining active authority depends on it.

### FG-M08 — ACCEPTED_AND_CORRECTED

**Problem:** governance provenance identity and CI evidence identity can diverge for the same artifact.

**Correction:** introduce one `ArtifactIdentity` layer; provenance and evidence are facets.

```yaml
ArtifactIdentity:
  artifact_id: <content-addressed hash identity>
  content_hash: <hash>
  storage_refs: []
  kind: CODE | LIBRARY | MODEL_OUTPUT | IMAGE | AUDIO | TEXT | DATA | LOG | TRACE | OTHER
  provenance_ref: <ProvenanceRecord or null>
  evidence_metadata_refs: []
  usage_policy_state: ALLOW | QUARANTINE | REJECT | RESEARCH_REQUIRED | NOT_APPLICABLE
  visibility: NORMAL | PROTECTED
  retention_class: <FAC4 class>
```

Rules:

- every evidence artifact that is also external/generated/derived content references the same content identity and applicable provenance record;
- evidence consumption checks usage policy as well as evidence validity;
- `QUARANTINE` cannot be bypassed by importing the same bytes under another `evidence_id`;
- rights/terms policy and evidence retention remain separate dimensions and can evolve independently while the content identity stays stable;
- protected artifacts still carry identity/provenance even when payload visibility is restricted.

## 6. Minor review finding dispositions

### FG-m09 — ACCEPTED

FAC2’s proposed GraphQL `updateRefs` multi-ref claim/conflict-lock + lease model is classified:

```yaml
mature_lock_protocol_candidate:
  state: EXPERIMENTAL_NOT_ADOPTABLE
  required_before_adoption:
    - FAC2-E1 atomic task_plus_multi_lock CAS
    - FAC2-E2 crash matrix
    - durable_lease_authority experiment
    - ruleset/permission interaction evidence
    - stale-writer terminal-status regression
  current_fallback: canonical schema-3 branch/head/status fencing
```

Synthesis/final canonicalization may create these experiments as bounded planning/technical work; it may not describe the candidate protocol as the active owner primitive until evidence and the required review route pass.

### FG-m10 — ACCEPTED

`ContextManifest` records:

- canonical context-policy/version/hash;
- required packet refs;
- optional loaded refs + trigger/reason;
- explicit material exclusions/forbidden categories;
- size/truncation state.

It MUST NOT enumerate every repository object not loaded.

### FG-m11 — ACCEPTED

Native GitHub dependency/UI state is a projection. Derived queue views include both:

- issue lifecycle (`open/closed`);
- canonical prerequisite predicate (`UNSATISFIED/SATISFIED/INVALID`).

`issue closed` is never directly equivalent to prerequisite satisfaction. FAC2 reconciliation reports mirror divergence; READY consumes the canonical predicate.

## 7. Notes preserved as explicit obligations

### FG-n12 — CI/evaluator service incidents

Define a future typed `ServiceIncident`/`EvidenceServiceIncident` interface in the control-plane/evidence implementation:

- service/evaluator identity;
- affected evidence requirements/tasks;
- start/last-observed state;
- allowed predeclared replacement evidence paths;
- recovery/reconciliation result;
- no implicit waiver.

Unaffected tasks continue; affected claims remain UNSATISFIED/INCONCLUSIVE until evidence exists.

### FG-n13 — Canonical-state queue metrics

Scheduler/factory metrics count canonical state, not GitHub activity proxies. Open PRs, closed producer issues, comments, commits, or raw check count can be diagnostics but never the WIP/priority truth.

## 8. Integrated authority and state snapshot

A mature authoritative scheduler snapshot should conceptually bind:

```yaml
FactoryStateSnapshot:
  snapshot_id: <content/state hash>
  canonical_main_sha: <sha>
  canonical_program_or_policy_epoch: <ref>
  active_directive_set_id: <ref>
  canonical_graph_ref: <content-addressed>
  task_contract_ref: <content-addressed>
  risk_floor_ref: <ref>
  ownership_and_lock_state_ref: <ref>
  trust_debt_index_ref: <ref>
  evidence_requirement_refs: []
  evidence_satisfaction_refs: []
  retention_graph_ref: <ref>
  observed_github_state_ref: <query/event snapshot>
  derived_cache_version: <non-authoritative>
```

A `ready_proof` or integration proof cites this snapshot (or equivalent exact refs). A state mutation invalidating any authority input invalidates the proof.

## 9. Integrated task lifecycle

### 9.1 Task creation / compilation

Compiler emits:

- task/mission ID and activation;
- objective/owned paths/conflict keys;
- typed prerequisites/result predicates;
- directive-sensitive scope/priority hooks;
- risk floor and review route;
- evidence requirements;
- context policy + authoritative inputs;
- output/handoff schema;
- downstream edges;
- retention/provenance expectations;
- WIP class/priority rank.

### 9.2 Claim

Current canonical schema-3 claim/fence remains authoritative until mature lock experiment passes.

Future mature claim transaction may replace it only under PolicyEpoch/meta-verification. It must atomically establish task ownership and declared conflict locks, then publish an auditable event. Partial acquisition is invalid.

### 9.3 Work / context / discovery

Episode uses FAC1 Task/Episode/ContextManifest semantics. A discovered change inside current owned+locked+reviewed surface may be absorbed if required and bounded. New conflict key or raised risk floor triggers `LockExpansion` + task review-route/context update before mutation; inability to satisfy these conditions routes discovered work instead.

### 9.4 Handoff / recovery

Handoff remains navigation/evidence. Ownership is re-derived and reacquired by control plane. Context policy, exact evidence refs, risk/trust changes, and retained work SHAs accompany handoff/recovery.

### 9.5 Review / verification

Task contract/risk floor selects FAC3 review class and EvidenceRequirements. Review/verifier consumes exact immutable candidate, requirement version, evidence satisfaction, evaluator/trust profile, and base. Candidate or policy drift routes restart/reverification; judge cannot edit candidate and preserve the old PASS.

### 9.6 Integration

Integrator verifies:

- active directives do not block/alter scope;
- exact policy epoch/risk route completed;
- exact candidate/head/base;
- evidence requirements satisfied;
- required review/verification and trust profile valid;
- unresolved BLOCKER/MAJOR absent;
- retention/provenance anchors materialized;
- expected PR head + verified current base;
- allowed deterministic transformation;
- squash-only merge.

Terminal integration updates authority/provenance; candidate policy becomes active only after successful integration under the old active policy.

### 9.7 GC / retirement

Supersession/terminal state alone does not permit deletion. GC follows active RetentionEdges and artifact policy. Derived Projects/native dependency mirrors can be repaired/deleted independently because they are non-authoritative.

## 10. Scheduler / WIP synthesis

Adopt FAC2 class-first scheduler semantics:

1. canonical/authority recovery;
2. ownership/handoff/stale/orphan recovery;
3. review/revision/verification/integration;
4. new production/proposal;
5. planning/checkpoint replenishment.

State inputs now additionally include `ActiveDirectiveSet`, `RiskFloor`, `TrustDebt` triggers, EvidenceSatisfaction, and current retained-lock/ownership scope.

Do not adopt an inferred unblock score as authority until benchmarked. Within a class use explicit priority rank then deterministic policy keys then issue number.

WIP metrics distinguish:

- active mutation owners;
- work waiting review/revision/verification/integration by canonical result state;
- eligible-but-WIP-blocked work;
- stale/recoverable work;
- trust-debt audits;
- discovered-work candidates (not active issues).

Open PR/closed issue counts are not canonical WIP.

## 11. Governance risk and directive behavior

### 11.1 Directives

Human directives are exceptional external overrides, not approval gates. Material directives become durable scope-aware records and are included in state derivation. A PRIORITY directive cannot silently weaken acceptance/evidence/risk gates; a RESOURCE_CONSTRAINT may enable an already-canonical degraded mode; a PROJECT_DIRECTION directive can invalidate/replan dependent canonical decisions; an EMERGENCY_SAFETY directive can halt affected work immediately.

### 11.2 Risk

RiskFloor is a minimum. Additional uncertainty, dependency fan-out, discovered scope, or review findings may escalate it. A worker cannot lower the task’s route by claiming reversibility or bounded scope.

### 11.3 Self-modification

All judge-affecting changes are governed by PolicyEpoch old-policy-judges-new-policy and FAC3 META_VERIFICATION. Benchmarks/evidence under FAC4 are inputs; the candidate protocol/evaluator has no current authority over its own adoption.

## 12. Evidence and artifact topology

The integrated identity chain is:

```text
ArtifactIdentity
  -> ProvenanceRecord (when external/generated/derived rights/source policy applies)
  -> EvidenceArtifact metadata (when used as evidence)
  -> RunReport / evaluator result
  -> EvidenceSatisfaction
  -> Review / Verification result
  -> RetentionEdge / ProvenanceAnchor
  -> Canonical decision/integration
```

A single byte-identical artifact cannot escape quarantine by receiving another evidence ID. Conversely, an allowed provenance state does not imply the artifact is good evidence; evidence validity/trust/coverage remains separately evaluated.

## 13. Context / handoff integration

`ContextManifest` references:

- canonical policy/program/graph/task contract;
- relevant ActiveDirectiveSet identity;
- exact prerequisite/status/work refs;
- applicable RiskFloor/TrustDebt/EvidenceRequirement refs;
- issue-declared authoritative inputs;
- optional retrieval refs with named trigger/reason;
- policy-category/hash for forbidden-by-default context;
- size/split state.

Handoffs record these stable refs but never grant authority. Continuation re-derives current versions because directives, evidence satisfaction, trust debt, or policy epoch may have changed since handoff.

## 14. Unresolved empirical work / explicit adoption barriers

These are **not** treated as solved:

### 14.1 Mature atomic ownership / locks

Required evidence:

- FAC2-E1 atomic task + multi-lock CAS;
- FAC2-E2 crash matrix including CAS-before-event;
- lock namespace/ruleset/permission validation;
- durable trusted lease-authority choice and race test;
- lock expansion/reacquisition tests;
- stale-writer terminal-status test.

Until PASS through the required meta-review route: current canonical schema-3 fence remains active.

### 14.2 Main/ruleset/check/merge enforcement

Require FAC2-E4/E5 and any merge-queue E6 evidence before claiming platform enforcement. Squash-only and current-base verification remain binding regardless of GitHub feature choice.

### 14.3 Trust / protected evaluation

Require seeded-defect, Goodhart, permission/leakage, evaluator-version, and DEGRADED-vs-isolated experiments (FAC3-E1/E4/E6/E8) before selecting protected-route thresholds or claiming degraded review is sufficient for high-risk long-term authority.

### 14.4 Evidence / CI

Require flake-injection, retention/GC, protocol benchmark, and benchmark-drift experiments (FAC4-E3/E4/E7/E10) before canonical numeric policies/retention thresholds.

### 14.5 Operating-model context/handoff

Require forced-substitution/context-ablation/discovered-work experiments (FAC1-E1/E2/E5) before freezing context/task-split thresholds.

## 15. Observability

Use a shared diagnostic vector with IDs traceable to the above objects:

- directive conflicts/record latency and READY invalidations;
- risk-floor escalations and attempted downgrades;
- ownership/lock acquisition/expansion conflicts;
- stale-writer fence failures;
- handoff reconstruction/context widening;
- discovered-work absorption vs reroute;
- evidence requirement satisfaction failures by reason;
- FLAKY/INCONCLUSIVE/quarantine age and substitutions;
- review/verifier escape and disagreement;
- TrustDebt opened/aged/closed and stronger-audit outcomes;
- PolicyEpoch benchmark/adoption/rollback;
- protected-evaluator access/change incidents;
- retained object reachability/GC prevention/errors;
- artifact quarantine/usage violations;
- READY frontier, WIP by canonical stage, queue age, verified throughput;
- integration/base/head/squash failures.

No single aggregate score controls scheduling or quality.

## 16. Failure modes defended

- hidden directive changes task selection;
- priority directive weakens quality gate;
- dynamic scope enters unlocked shared surface;
- stale owner writes after recovery;
- N+1 policy evaluates itself;
- degraded trust debt disappears on issue closure;
- producer risk-downgrades own judge-affecting task;
- flaky required check is replaced ad hoc;
- stale green status satisfies changed EvidenceRequirement;
- quarantined external/generated content re-enters through evidence alias;
- reviewed unmerged work SHA becomes unreachable after GC;
- Projects/native dependency state becomes scheduler authority;
- issue closure is mistaken for prerequisite predicate success;
- CI outage becomes silent waiver or global human gate;
- activity metrics drive WIP/priority;
- experimental ref-lock design becomes canonical without spikes;
- candidate policy weakens its own evaluator/permission gate;
- merge expected-head check is used without current-base verification.

## 17. Risks

- The integrated object model can become bureaucratic if each object requires manual authoring. Control-plane/CI implementation should derive and validate as much as possible from task/evidence metadata.
- `ActiveDirectiveSet` must not capture unnecessary private human conversation; only bounded project-relevant authority is durable.
- TrustDebt audits can flood the quality queue after stronger capability appears; prioritize by risk/downstream authority and batch related audits without hiding debt.
- Risk floors can over-serialize work if triggers are broad; benchmark effects and allow stronger evidence to refine future policy only through PolicyEpoch.
- Retention anchors can grow storage/ref count; later storage design may compact content while preserving hashes/verifiability through reviewed retention policy.
- Artifact policy and evidence validity may have different owners; the shared identity must not conflate legal usage with technical quality.
- The mature atomic-lock experiment may fail; the synthesis explicitly retains schema-3 fallback.

## 18. Open questions

1. Which exact storage/record shape best represents ActiveDirectiveSet without creating a merge-hot central file?
2. How should a material directive be cryptographically/account-authenticated beyond platform author association where necessary?
3. What GitHub/ref/service primitive best implements LockExpansion atomically if FAC2-E1 passes?
4. Where should durable lease authority live if GitHub timestamps + refs are insufficient?
5. What canonical capability record triggers TrustDebt audits when isolated/multi-agent execution becomes available?
6. Which risk triggers and minimum review routes should be hard compiler rules versus table-driven canonical policy?
7. What task-compiler syntax makes EvidenceRequirement expressive without becoming domain-specific boilerplate?
8. How should protected evidence satisfy EvidenceRequirements without exposing protected artifact identities/content beyond the allowed interface?
9. What durable Git/ref/artifact-store anchor minimizes cost while guaranteeing consumed work/evidence reachability?
10. Which ArtifactIdentity fields are universal versus provenance/evidence facets?
11. What ServiceIncident schema lets evidence outages remain autonomous and bounded without ad hoc waiver?
12. Which current DEGRADED bootstrap/Wave 1 decisions should receive highest audit priority when stronger trust becomes available?

## 19. Reopen conditions

Reopen this synthesis if:

- two compliant schedulers can derive different authority/READY from the same canonical + directive state;
- an active task can mutate a newly conflicting surface before lock expansion/reroute;
- a judge-affecting candidate can weaken the policy used to approve itself;
- DEGRADED trust debt is not machine-discoverable after task closure;
- control plane/verifier/CI disagree on whether one EvidenceRequirement is satisfied;
- a producer can downgrade a mandatory risk/review route;
- reviewed work/evidence becomes unreachable after GC;
- quarantined content can be consumed under an alternate evidence identity;
- experimental lock/lease mechanics are promoted without the named evidence;
- context manifests grow by enumerating all omitted repository state;
- native GitHub closure/dependencies affect canonical readiness directly;
- stronger cross-domain review shows these interfaces conflict with technical/game synthesis.

## 20. Verification / next-review contract

This candidate completes at `REVIEW_READY`, not canonicality.

`W1-REV-CROSS` must specifically attack:

- whether the new interface objects create a central serialization bottleneck or can be partitioned/content-addressed;
- whether technical/runtime/evidence architecture can implement ArtifactIdentity/Retention/EvidenceRequirement without circular dependencies;
- whether game/evaluation tasks can express RiskFloor/EvidenceRequirement without over-constraining exploratory design;
- whether PolicyEpoch and TrustDebt are sufficient for future factory self-improvement;
- whether directive/risk/evidence inputs make READY derivation deterministic under high concurrency;
- whether fallback/current schema-3 ownership remains coherent while mature lock experiments are pending.

Any later verification must bind this exact synthesis work SHA plus cross-domain review/synthesis state and current base. No empirical experiment above may be represented as PASS until evidence exists.

## 21. Downstream work unblocked

When this exact synthesis reaches valid `REVIEW_READY`, it contributes one prerequisite to `W1-REV-CROSS` alongside W1-SYN-TECH and W1-SYN-GAME.

It does not create new current-wave tasks, alter canonical control-plane behavior, integrate producer PRs, or authorize gameplay implementation.