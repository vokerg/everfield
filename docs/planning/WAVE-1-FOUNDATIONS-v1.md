# Everfield Wave 1 Foundations — Canonicalization Candidate

**Mission:** `W1-SYN-FINAL`  
**State:** CANONICAL PLANNING FOUNDATION  
**Phase after promotion:** PLANNING  
**Implementation readiness:** BLOCKED  
**Required verifier:** `W1-VERIFY-01`

## 1. Purpose

This is the bounded Wave 1 foundation candidate. It reconciles exact W1-SYN-FAC, W1-SYN-TECH, W1-SYN-GAME, and W1-REV-CROSS work states frozen in `wave-1-final-input.yaml`.

The candidate defines the cross-domain contracts that may become canonical planning foundations after independent/degraded-independent verification and squash-only canonicalization. It **does not** select an engine, authorize production/gameplay implementation, settle final game balance/content/style/platforms, or represent unrun evidence as PASS.

The current canonical Planning Program v1 remains the dispatcher/ownership authority. These foundations refine what future planning/evidence work must prove; they do not replace schema-3 ownership or the current `[PLAN-v1]` queue before verified canonicalization.

## 2. Exact input binding

- W1-SYN-FAC work: `896cb799024e5d3c2ce451196f85b67e29edd3bc`
- W1-SYN-TECH work: `99805527fa192805b683722e27d72e19aa964fd0`
- W1-SYN-GAME work: `e74e0b0c95e85f69718868eedae324a298f02f3e`
- W1-REV-CROSS work: `d8cd8d16d9a1ca9eae9e51987f86b767992584c2`
- W1-REV-CROSS status: `5249340288`, `CHANGES_REQUIRED`, 1 BLOCKER / 11 MAJOR
- current Wave 1 base: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- one-agent resource constraint: Issue #5 comment `5244416013`
- current project-owner lease-continuation directive: Issue #27 comment `5249227987`

Any mismatch is a verification failure.

## 3. Foundation decision classes

Every foundation decision is typed:

- `CANONICAL_CANDIDATE` — coherent planning rule proposed for Wave 1 canonicalization; still noncanonical until W1-VERIFY-01 PASS + W1-CANON-01 squash promotion.
- `EVIDENCE_REQUIRED` — empirical mechanism/capability/choice that remains unproven and cannot become settled implementation architecture without its exact evidence predicate.
- `DEFERRED` — intentionally waits for prerequisite product/platform/evidence choices.
- `VERIFIED_DECISION` — reserved for later evidence-backed decisions. **Wave 1 creates none for engine/tool/runtime-specific choices.**

The next-wave compiler preserves these states. No prose, issue closure, PR, or aggregate score upgrades `EVIDENCE_REQUIRED` to `VERIFIED_DECISION`.

## 4. `PLANNING_EXPERIMENT` — correction of CD-B01

### 4.1 Authority class

Wave 1 establishes a bounded planning-experiment execution class so empirical planning can produce executable evidence without opening production implementation.

```yaml
PlanningExperiment:
  experiment_id: <stable>
  task_mission_id: <stable>
  evidence_question_refs: []
  decision_refs_blocked_or_informed: []
  allowed_ownership_surface: <bounded paths/repo/fixture>
  task_branch: planning/issue-N
  disposable: true
  production_dependency_allowed: false
  production_content_authority: NONE
  canonical_game_content_authority: NONE
  engine_lock_in_authority: NONE
  evidence_requirement_ref: <exact>
  check_plan_ref: <compiled>
  required_review: <typed>
  retention_policy: <evidence/code fixture rule>
  cleanup_or_quarantine_rule: <typed>
  completion_predicate: <typed>
```

### 4.2 Rules

1. A planning experiment answers a named evidence question; it is not feature delivery.
2. Experimental executable code/artifacts live only on the task-owned bounded surface or an explicitly declared isolated fixture/spike repository surface.
3. Production/gameplay code may not depend on experimental code by default.
4. Experimental code may be retained immutably as evidence/fixture, but promotion into production requires a later production task after the relevant decision becomes verified and implementation readiness permits it.
5. Experiment output cannot select an engine or architecture unless its declared evidence requirement, independent review route, and promotion predicate all pass.
6. A task that cannot state the evidence question, bounded surface, disposable status, and promotion target is not a planning experiment.
7. The class does not weaken `IR-BLOCKER-*` entries for production implementation.
8. Main integration of an experiment normally promotes only reviewed evidence/specification/canonical fixture material explicitly authorized by its task contract; disposable candidate code stays noncanonical unless the verified promotion manifest says otherwise.

This removes the engine/evaluator/readiness cycle while preserving the implementation barrier.

## 5. Unified authority chain — correction of CD-M02

There is exactly one acceptance chain:

```text
TaskContract / TaskClaimContract
  -> EvidenceRequirement (normative claim requirements under PolicyEpoch)
  -> CheckPlan (compiled execution/applicability plan for exact candidate/base)
  -> ExecutionEvidenceEnvelope attempts/artifacts
  -> EvidenceSatisfaction (derived against exact requirement + plan)
  -> Review / Verification result
  -> Decision / readiness / integration eligibility
```

### 5.1 `EvidenceRequirement`

Normatively declares each claim, required evidence kinds/execution surfaces, applicability predicates, minimum trust profile, allowed result classes, protected level, substitution/quarantine policy, and aggregation rule.

### 5.2 `CheckPlan`

Is generated from one exact `EvidenceRequirement` + candidate/base/policy epoch. It may specialize execution details but may not weaken requirements. `NOT_APPLICABLE` is resolved before execution; `NOT_RUN` means required execution did not occur.

### 5.3 `ExecutionEvidenceEnvelope`

Binds exact candidate work/head/base, environment/toolchain, content/schema package, execution surface, scenario/policy/actions/seeds, evaluator fingerprints, attempt lineage, result, artifacts, trust profile, nondeterministic surfaces, and coverage gaps.

### 5.4 `EvidenceSatisfaction`

Is derived, never hand-authored as truth. Required `FAIL`, `FLAKY`, `INCONCLUSIVE`, or `NOT_RUN` cannot yield SATISFIED unless a versioned requirement explicitly provides valid replacement evidence; changing a requirement creates a new requirement/policy version rather than rewriting the old result.

## 6. One durable artifact identity — correction of CD-M03

`ArtifactIdentity` is the sole durable identity for retained source/content/media/evidence artifacts.

```yaml
ArtifactIdentity:
  artifact_id: <content-addressed/stable>
  content_hash: <hash>
  kind: <typed>
  storage_refs: []
  produced_by_ref: <work/run/source>
  provenance_refs: []
  rights_or_terms_state: CLEAR | RESTRICTED | QUARANTINED | UNKNOWN | NOT_APPLICABLE
  visibility: NORMAL | PROTECTED
  retention_class: <typed>
  access_policy_ref: <optional>
  supersedes: []
```

Execution evidence, protected evidence, originality/reference-use records, retention edges, content packages, and media references use `artifact_id`; a second locator/hash wrapper cannot bypass quarantine/provenance state.

Content hash proves identity, not availability. Canonical/protected artifacts require reachability/integrity auditing and restoration/reopen behavior.

## 7. Directives, policy, and empirical truth — correction of CD-M04

### 7.1 `ActiveDirectiveSet`

Material human/project-owner directives are durable, scoped, versioned authority inputs to READY/claim/recovery/integration state. Hidden chat-only intent is not durable authority after the turn; the directive must be recorded in repository/GitHub state when downstream work depends on it.

Current active directive provenance includes Issue #27 comment `5249227987`: current master agent may continue existing agent leases without waiting for artificial cross-chat ownership separation.

### 7.2 Directive limits

A directive may change project goals, priority, resource assumptions, constraints, ownership/continuation rules, or explicitly supersede a policy requirement within scope. It **cannot** change an observed empirical result, fabricate `EvidenceSatisfaction`, or convert an unrun experiment to PASS.

If a directive intentionally changes/waives a requirement, the authoritative effect is a **new `PolicyEpoch` / TaskClaimContract / EvidenceRequirement version** with provenance. Existing evidence is evaluated against the new rule; old historical evidence is not rewritten.

Emergency safety stop may halt immediately; resumption requires durable scoped authority state.

## 8. `ResourceCapabilityState` and trust debt — correction of CD-M12

Ownership convenience and independent-review capability are separate facts.

```yaml
ResourceCapabilityState:
  state_id: <content-addressed/current>
  available_execution_contexts: <count/capability>
  isolated_context_available: <boolean>
  independent_actor_or_permission_separation: <declared>
  protected_oracle_control_available: <declared>
  concurrency_capacity: <declared/observed>
  source_refs: []
  valid_until_or_recheck: <trigger>
```

The owner directive `5249227987` affects lease continuation; it does not imply isolated/multi-agent review capability. Existing `DEGRADED_SINGLE_AGENT` trust remains DEGRADED. `TrustDebt` closes only after a stronger valid review/verification result under a capability state satisfying its reopen condition, or an explicit reviewed supersession that does not pretend stronger independence occurred.

## 9. Scoped implementation-readiness ledger — correction of CD-M05

```yaml
ImplementationReadinessLedger:
  version: 1
  entries:
    - blocker_id: <stable>
      category: PRODUCT | TECHNICAL | FACTORY_TRUST | EVIDENCE | ACCESSIBILITY | RIGHTS | PLATFORM | OTHER
      scope: GLOBAL | DOMAIN | FEATURE_CLASS | PLATFORM | TOOLING
      blocks: []
      source_requirement_refs: []
      resolution_predicate: <typed>
      evidence_satisfaction_refs: []
      state: OPEN | RESOLVED | SUPERSEDED
```

### 9.1 Current global production blockers

At Wave 1 final synthesis the following are OPEN and block `PRODUCTION_IMPLEMENTATION` globally or for the declared product scope:

- `IR-BLOCKER-ENGINE-DECISION` — no evidence-backed engine/runtime selection exists.
- `IR-BLOCKER-PLATFORM-SCOPE` — target platform/product scope is not yet sufficiently bounded for implementation/release requirements.
- `IR-BLOCKER-ACCESSIBILITY-CURRENT` — current authoritative accessibility/target-platform requirements not mapped and independently verified.
- `IR-BLOCKER-EVIDENCE-FOUNDATION` — minimum evidence/check/artifact/evaluator execution contracts have not yet been exercised as a coherent implementation-ready stack.

### 9.2 Scoped blockers/debts

These do not necessarily block all planning experiments but block affected decisions/release scopes:

- open rights/provenance/terms uncertainty for generated/external content;
- unverified GitHub mature lock/CAS mechanism (current schema 3 remains usable authority);
- canonical semantic hash conformance before cross-runtime hash authority;
- migration/order/evaluator/protected-evidence evidence where dependent decisions require them;
- DEGRADED trust debts (quality debt; does not falsely become FULL independence).

Full production readiness requires zero OPEN ledger entries whose `blocks` includes `PRODUCTION_IMPLEMENTATION` for the target product scope.

## 10. Typed evidence dependencies — correction of CD-M06

Dependency edges distinguish:

- `BLOCKED_BY` — hard task/result prerequisite;
- `BLOCKS_DECISION(decision_id)` — evidence required before one decision may advance;
- `BLOCKS_IMPLEMENTATION_SCOPE(scope_id)`;
- `BLOCKS_RELEASE_SCOPE(scope_id)`;
- `INFORMS_DECISION(decision_id)` — useful but not gating by itself;
- `CALIBRATES_EVALUATOR(evaluator_id)`;
- `REOPENS_ON_FAILURE(target_id)`;
- `REVIEW_OF`, `SYNTHESIZES`, `VERIFIES`, `CANONICALIZES`;
- `INTERFACE_WITH`, `CONFLICTS_WITH`, `SUPERSEDES`, `INVALIDATES`.

Scheduler readiness applies only the edges relevant to the target task/decision/scope. Independent evidence missions are parallelizable when outputs/conflict keys do not collide. No “all empirical work complete” global mega-gate exists.

## 11. Runtime/game exact mappings — correction of CD-M07

### 11.1 Canonical gameplay meaning

Persistent gameplay-authoritative meaning is engine-independent logical state with stable IDs/versioned schemas. Rendering/editor/audio/platform types are adapters unless a reviewed contract declares a canonical logical representation.

### 11.2 `GameTimePolicy`

`GameTimePolicy.version` is part of `simulation_rules_version` and must be bound in any evidence/replay involving calendar/schedule/timed quest/economy/automation/timing behavior. Gameplay never reads ambient wall time implicitly.

### 11.3 `GameSemanticGraph`

`graph_version` is required claim/coverage identity for semantic-coverage, lifestyle, progression, route, and game-possibility evidence. Raw edge count is not quality.

### 11.4 Generative runtime boundary

Mappings are normative:

- `BUILD_TIME_CANDIDATE` → artifact/content candidate; no runtime canonical authority before normal validation/review.
- `RUNTIME_PRESENTATION_ONLY` → technical `PRESENTATION_ONLY`.
- `RUNTIME_CANONICAL_EFFECT` → validated canonical command/effect; if generation/service is nondeterministic, accepted output/effect is a `RECORDED_CANONICAL_OUTCOME` unless a stronger deterministic contract is proven.

Replay normally reuses accepted canonical outcomes, not a new external model call. Persisted accepted outputs/effects use shared ArtifactIdentity/content-package/migration semantics.

### 11.5 Causality/determinism

Domains declare deterministic local ordering, causal edges, synchronization points, and stable tie-breakers. Global total order is not a default architecture mandate. Cross-runtime state-hash authority remains `EVIDENCE_REQUIRED` until canonical semantic encoding conformance passes.

## 12. Shared judgment record — correction of CD-M08

Important subjective/AI panel decisions use `JudgmentPanelRecord`:

```yaml
JudgmentPanelRecord:
  panel_id: <stable>
  claim_set_ref: <exact>
  candidate_refs: []
  evidence_envelope_refs: []
  evaluators:
    - evaluator_fingerprint_ref: <exact>
      episode_or_context_ref: <exact>
      provider_or_model_family: <group>
      oracle_control_relation: <typed>
      candidate_write_relation: <typed>
      evidence_source_relation: <typed>
  rubric_or_prompt_hashes: []
  order_randomization_ref: <optional>
  correlation_groups: []
  dimension_results: []
  disagreement: <structured>
  factory_trust_profile: <typed>
  result: <structured/no universal score>
```

Multiple calls or model names do not automatically create independent evidence. Trust/risk-floor requirements determine whether the panel is sufficient. Mutable evaluator backends require fingerprints/calibration and drift reopen policy.

## 13. Domain authority and interface ownership — correction of CD-M09

A canonical `DomainAuthorityMap` assigns one schema owner for each shared type and permits domain extensions through explicit namespaces. Aggregate indexes are generated when practical.

| Shared type | Canonical owner | Extension producers |
|---|---|---|
| ActiveDirectiveSet / PolicyEpoch / ResourceCapabilityState | governance/factory | task compiler, scheduler |
| TaskClaimContract / EvidenceRequirement / EvidenceSatisfaction / RiskFloor | governance/factory | technical/game claim definitions |
| CheckPlan / ExecutionEvidenceEnvelope / EvaluatorFingerprint | technical/evidence | factory CI, engine, game evaluation |
| ArtifactIdentity / RetentionEdge / ProvenanceAnchor | governance/evidence shared foundation | technical/game/media/content |
| ImplementationReadinessLedger | final/cross-domain governance | all domains add scoped entries |
| GameTimePolicy / GameSemanticGraph / ProgressionGate / LifestyleViability | game design | technical/evaluator read/compile |
| canonical schemas/content package/migration/determinism | technical runtime | game content schemas within assigned namespaces |
| next-wave promotion/dependency compiler | canonical planning program/final synthesis | domain candidates provide data |

No ordinary domain task may manually edit a global aggregate registry unless its task owns that generated/compiled output. Stable namespace allocation/retirement/tombstones prevent semantic ID reuse.

## 14. External evidence freshness — correction of CD-M10

`FreshnessRequirement` is event/version-sensitive:

```yaml
FreshnessRequirement:
  requirement_id: <stable>
  source_class: ENGINE_DOC | PLATFORM_RULE | ACCESSIBILITY_GUIDANCE | PROVIDER_TERMS | LEGAL_IP_RESEARCH | GITHUB_CAPABILITY | EVALUATOR_PROVIDER | OTHER
  evidence_ref: <immutable snapshot/citation record>
  observed_date: <date>
  source_version_or_scope: <ref>
  invalidation_triggers: []
  maximum_age: null | <only when justified>
  rerequest_predicate: <typed>
  dependent_decision_refs: []
```

A changed engine/platform/provider/terms/evaluator/GitHub version or target scope can reopen freshness without deleting historical evidence. Stale required external evidence makes dependent decisions INCONCLUSIVE/OPEN, not silently valid forever.

## 15. Protected evidence

Protected evidence publishes a durable result envelope with exact candidate/base/environment/evaluator/oracle identities, coverage category, result, bounded diagnostics, ArtifactIdentity evidence ref, trust profile, calibration fingerprint, and reveal/change audit refs. Unavailable/corrupt/unverifiable protected evidence is INCONCLUSIVE.

Protected oracle/config changes are judge-affecting PolicyEpoch changes. Disclosure/compromise events are auditable and rotate/retire affected holdouts as required.

## 16. CI result semantics

`CheckPlan` is compiled before execution. Applicability states are `REQUIRED`, `OPTIONAL`, `CONDITIONALLY_REQUIRED`, `NOT_APPLICABLE`. Execution result `NOT_RUN` is distinct from `NOT_APPLICABLE`.

A required FAIL/FLAKY/INCONCLUSIVE/NOT_RUN cannot produce SATISFIED. Retry lineage is retained. Quarantine changes the explicit evidence requirement temporarily with owner/remediation/expiry/replacement evidence; it never relabels a failure PASS.

## 17. Engine decision state

Engine discovery/admission and S1–S10 representative spikes remain `EVIDENCE_REQUIRED`. The candidate set uses current primary sources, inclusion/exclusion rationale, exact tested versions, equivalent scenario intent, adaptation manifests, repeated failures/retries/costs, and independent equivalence review.

No engine is selected in this candidate. Any later conditional Milestone Zero engine ADR must bind evidence, unresolved risks, a falsifier/checkpoint, exit plan, and prohibited irreversible engine-specific dependencies before the checkpoint.

## 18. Accessibility, platform, originality, and rights

- Target platform/product scope must be established enough to research current requirements.
- Current authoritative accessibility/platform obligations must be mapped to architecture and real task evidence before `IR-BLOCKER-ACCESSIBILITY-CURRENT` resolves.
- Provenance is necessary but not sufficient for originality/reference-use acceptance.
- Originality/reference-use records bind candidate ArtifactIdentity, reference purpose, allowed/prohibited reuse, similarity/adversarial evidence, and current rights/terms research.
- Unknown/restricted material remains quarantined for the affected shipping/release scope; it does not silently enter through another evidence alias.

## 19. Game foundation candidate

Wave 1 adopts as canonical candidates, still subject to later evidence:

- many viable trajectories rather than one mandatory playthrough;
- multi-horizon loops and progression increasing agency/capability;
- `ProgressionGateContract` with FOUNDATIONAL/SPECIALIZATION/OPTIONAL/BRANCH_EXCLUSIVE classifications and explicit routes/recovery/evidence;
- multi-dimensional economy/progression value, not one money-per-time metric;
- automation as optional leverage with higher-order decisions, not passive end-state or universal legitimacy requirement;
- `LifestyleViabilityEvidence` distinguishing real direct-play viability from mere presence of manual verbs;
- explicit world/NPC/social/narrative/quest facts, knowledge, chronology, branches, effects, and structural solvability;
- generated prose/media as grounded candidates, not silent canonical truth;
- progressive experience legibility, semantic input abstraction, accessibility architecture, controlled media provenance/evaluation;
- semantic coverage bound to `GameSemanticGraph.graph_version`;
- synthetic players/evaluators as versioned models, not proxies for humans or a universal fun score.

Exact content catalog, balance values, final calendar, style, evaluator technology, and final systems remain DEFERRED/EVIDENCE_REQUIRED.

## 20. Factory/governance foundation candidate

Wave 1 adopts as canonical candidates:

- repository/GitHub state as durable project memory; sessions disposable;
- schema-valid typed ownership/status and exact work/base evidence;
- one normal mutation owner per task unless coordinated structure is explicit;
- narrow conflict/ownership surfaces and deterministic task branches;
- active directives as durable scoped inputs;
- old policy judges candidate judge-affecting policy (`PolicyEpoch`);
- multidimensional trust with explicit DEGRADED debt;
- `RiskFloor` preventing producer review-route downgrade;
- task-specific evidence requirements and structured CI evidence;
- retention edges/provenance anchors protecting consumed evidence;
- scheduler class priority favoring recovery/quality/integration over comparable new production;
- WIP governors, no routine human approval, Goodhart-resistant metrics;
- squash-only `main` integration;
- proposed mature GitHub multi-ref lock/CAS remains EVIDENCE_REQUIRED; current schema 3 remains authority.

## 21. Cross-review finding dispositions

| Finding | Disposition | Final correction |
|---|---|---|
| CD-B01 | ACCEPTED / CORRECTED | §4 `PLANNING_EXPERIMENT` breaks experiment/readiness cycle without production authority |
| CD-M02 | ACCEPTED / CORRECTED | §5 one requirement→plan→envelope→satisfaction authority chain |
| CD-M03 | ACCEPTED / CORRECTED | §6 one `ArtifactIdentity` across domains |
| CD-M04 | ACCEPTED / CORRECTED | §7 directives may change policy, never fabricate empirical truth |
| CD-M05 | ACCEPTED / CORRECTED | §9 scoped `ImplementationReadinessLedger` |
| CD-M06 | ACCEPTED / CORRECTED | §10 typed evidence dependency edges |
| CD-M07 | ACCEPTED / CORRECTED | §11 exact game-time/semantic/generative mappings to technical authority |
| CD-M08 | ACCEPTED / CORRECTED | §12 shared judgment/evaluator/trust record |
| CD-M09 | ACCEPTED / CORRECTED | §13 `DomainAuthorityMap` and generated aggregates |
| CD-M10 | ACCEPTED / CORRECTED | §14 shared freshness lifecycle |
| CD-M11 | ACCEPTED / CORRECTED | next-wave manifest includes task class/evidence/risk/readiness/ownership extensions and compiler validation |
| CD-M12 | ACCEPTED / CORRECTED | §8 directive ownership and independent resource capability separated |

No cross-review BLOCKER/MAJOR remains unresolved **at the candidate-contract level**. Empirical items remain open by design.

## 22. Canonical promotion plan

If and only if W1-VERIFY-01 returns valid current-base PASS with zero BLOCKER/MAJOR, W1-CANON-01 may mechanically promote the exact verified artifacts:

- `docs/planning/wave-1/synthesis/wave-1-canonicalization-candidate.md` → `docs/planning/WAVE-1-FOUNDATIONS-v1.md`
- `docs/planning/wave-1/synthesis/dependency-map.yaml` → `docs/planning/WAVE-1-DEPENDENCY-MAP-v1.yaml`
- `docs/planning/wave-1/synthesis/next-wave-promotion-manifest.yaml` → `docs/planning/WAVE-2-PROMOTION-MANIFEST-v1.yaml`

Promotion is byte-identical content except an optional mechanically verified header-state substitution in the foundations document:

- `State: VERIFICATION CANDIDATE / NON-CANONICAL` → `State: CANONICAL PLANNING FOUNDATION`
- add canonicalization provenance identifying W1-CANON-01 and its squash main SHA without changing normative body semantics.

Current `PLANNING-PROGRAM-v1.md` remains the dispatcher and schema-3 operational authority unless a separately verified canonical revision explicitly changes it.

## 23. Next wave

The verified promotion manifest contains **18** bounded Wave 2 candidates and exactly **12** initially READY candidates. All are planning/research/evidence/review/synthesis/checkpoint missions. No production gameplay feature is instantiated.

The initial frontier intentionally maximizes independent evidence generation across authority/compiler, GitHub control plane, engine admission/harness, hash/migration/ordering, protected evidence, CI reliability, evaluator drift, platform scope, and rights/originality research.

Blocked successors combine those results into comparative engine spikes, accessibility mapping, simulation parity, cross-evidence review, decision synthesis, and a later implementation-readiness reevaluation.

## 24. Verification obligations

W1-VERIFY-01 must cold-start from repository + GitHub state and verify at minimum:

1. exact four input work SHAs/statuses and current base;
2. all CD-B01/CD-M02..M12 dispositions exist and are non-circular;
3. `PLANNING_EXPERIMENT` cannot authorize production/gameplay implementation;
4. one acceptance authority chain exists;
5. directives cannot fabricate EvidenceSatisfaction;
6. current master lease directive is represented without upgrading independence capability;
7. global implementation-readiness blockers remain OPEN;
8. all EVIDENCE_REQUIRED decisions remain unverified;
9. dependency map is acyclic and typed;
10. next-wave manifest has 18 unique missions, ≤24 instantiated, exactly 12 initial READY, unique output/conflict surfaces, valid review/downstream routes, and no production issue;
11. every promotion candidate satisfies original `next_wave_candidate_schema` required fields plus extension checks;
12. promotion destinations and byte/content identity are mechanically reconstructable;
13. current schema-3/squash-only authority remains active;
14. closed/retired accidental Issues #59/#60 are not part of the promotion graph;
15. provenance retains exact Wave 1 synthesis/review/evidence refs.

PASS is forbidden with unresolved verification BLOCKER/MAJOR.

## 25. Reopen conditions

Reopen these foundations if:

- final verifier finds an authority collision/cycle or promotion manifest defect;
- a planning experiment becomes a production dependency without a new verified promotion route;
- human directives can create empirical PASS or close trust debt by implication;
- more than one object can independently declare the same claim SATISFIED;
- evidence/artifact aliases bypass provenance/quarantine;
- engine/game/runtime state bypasses declared canonical/replay boundaries;
- a next-wave task lacks bounded ownership/evidence/review/readiness semantics;
- external/current source changes invalidate a relied-upon decision;
- stronger independent execution capability becomes available and trust-debt audits should run;
- evidence proves a candidate foundation wrong.
