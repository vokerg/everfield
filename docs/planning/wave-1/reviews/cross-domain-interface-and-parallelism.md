# Cross-Domain Interface and Parallelism Adversarial Review — Wave 1

**Mission:** `W1-REV-CROSS`  
**Trust:** `DEGRADED_SINGLE_AGENT` / DEGRADED  
**Disposition:** `CHANGES_REQUIRED`  
**Findings:** **1 BLOCKER / 11 MAJOR / 4 MINOR / 2 NOTE**

## 1. Exact reviewed synthesis states

This review binds only the exact REVIEW_READY states frozen in `cross-domain-review-input.yaml`:

| Mission | Issue | Status | Work SHA |
|---|---:|---:|---|
| W1-SYN-FAC | #37 | `5248788825` | `896cb799024e5d3c2ce451196f85b67e29edd3bc` |
| W1-SYN-TECH | #38 | `5249311403` | `99805527fa192805b683722e27d72e19aa964fd0` |
| W1-SYN-GAME | #39 | `5249051313` | `e74e0b0c95e85f69718868eedae324a298f02f3e` |

No synthesis candidate was edited by this reviewer. Attack plan was frozen before cross-candidate reconciliation. Current one-agent trust debt remains anchored to Issue #5 comment `5244416013`.

## 2. Executive result

The three domain syntheses are compatible enough for final synthesis; there is no reason to invalidate a domain. They converge on content-addressed authority, exact candidate/base evidence, engine-independent gameplay meaning, typed trust/evidence, no scalar quality oracle, distributed ownership, explicit empirical gates, and a strong implementation-readiness barrier.

However, the combined system still has one **circular authority hole** and several duplicate/shared interfaces that must be made mechanically singular before Wave 1 can become a canonical dependency map.

The circularity is practical: engine/runtime/evaluator evidence requires executable experimental spikes before implementation readiness can be granted, but no synthesis defines a bounded execution authority that clearly distinguishes disposable planning experiments from production/gameplay implementation. A compliant future agent can therefore either stall forever or loosen the implementation barrier by interpretation.

Final synthesis is the appropriate repair surface.

## 3. BLOCKER

### CD-B01 — No bounded `PLANNING_EXPERIMENT` execution class breaks the engine/evidence/readiness cycle

**Cross-domain evidence.** Technical synthesis correctly makes engine selection, hash conformance, ordering, migration, GitHub CAS, protected evidence, evaluator drift, simulation parity, and CI reliability depend on unrun evidence. Several of those evidence families require executable code, builds, runtime state, engine projects, save/load, CI capture, or failure injection. Game synthesis keeps high-throughput/gameplay implementation blocked, and specifically keeps accessibility/current-platform readiness open. Factory synthesis preserves the implementation-readiness barrier but does not define an execution class for disposable technical experiments.

**Failure scenario.** A fresh agent reaches `TECH-EV-ENGINE-SPIKES`. If “any executable gameplay-shaped code before readiness” is forbidden, the engine decision can never obtain its required evidence. If the agent interprets the spike as ordinary implementation, it has silently opened the implementation gate without final verification.

**Required final-synthesis correction.** Define a machine-checkable `PLANNING_EXPERIMENT` authority distinct from `PRODUCTION_IMPLEMENTATION`, with at least:

```yaml
PlanningExperiment:
  experiment_id: <stable>
  evidence_question_refs: []
  decision_refs_blocked: []
  allowed_paths_or_isolated_repo_surface: []
  disposable: true
  canonical_product_dependency_allowed: false
  production_content_authority: NONE
  engine_or_tool_lock_in_authority: NONE
  merge_to_main_policy: <normally evidence/spec only; experimental code excluded or quarantined>
  required_cleanup_or_retention: <rule>
  evidence_contract_ref: <exact>
  review_route: <typed>
  expiry_or_completion_predicate: <typed>
```

Rules must prohibit production features/backlog from laundering themselves as experiments while allowing bounded engine/runtime/evaluator/control-plane spikes needed to resolve planning evidence. Experimental code may be retained as evidence at immutable refs but MUST NOT become production dependency by accident. Promotion of any experiment result into architecture still follows its `EVIDENCE_REQUIRED` predicate and review route.

Until final synthesis defines this class, implementation-readiness and required technical evidence form an ambiguous cycle.

## 4. MAJOR findings

### CD-M02 — `EvidenceRequirement` and `CheckPlan` currently compete as acceptance authority

Factory synthesis defines content-addressed `EvidenceRequirement` / `EvidenceSatisfaction`; technical synthesis defines immutable `CheckPlan` and `ExecutionEvidenceEnvelope`. Both say they determine required checks/applicability/trust and whether claims pass.

**Failure scenario.** Factory `EvidenceRequirement` says protected evidence is mandatory, while technical `CheckPlan` compiled under another version says it is conditionally required or not applicable. Scheduler/integrator chooses whichever object it happens to consume.

**Required correction.** Final synthesis must define one direction of compilation, e.g.:

```text
TaskClaimContract / EvidenceRequirement (normative requirement)
  -> compiled CheckPlan (execution plan for exact candidate/base/policy epoch)
  -> ExecutionEvidenceEnvelope attempts
  -> EvidenceSatisfaction (derived verdict against exact requirement + plan)
```

The compiled plan MUST bind the requirement ID/policy epoch and cannot weaken it. Any requirement change creates a new version and invalidates prior satisfaction as declared. There must be no second independent route to PASS.

### CD-M03 — `ArtifactIdentity` and evidence-artifact identities must become one durable object

Factory synthesis defines `ArtifactIdentity` to prevent rights/provenance aliases and GC mistakes. Technical synthesis embeds artifact `content_hash`, `storage_ref`, and `kind` inside evidence envelopes.

**Failure scenario.** The same bytes are quarantined under `ArtifactIdentity` but re-enter verification through a separately constructed evidence artifact with the same hash/another locator and no provenance/rights state.

**Required correction.** `ArtifactIdentity` becomes the sole durable identity for any retained evidence/content/media artifact. `ExecutionEvidenceEnvelope.artifacts[]`, retention edges, originality/reference-use records, and protected evidence refer to `artifact_identity_id` plus role-specific metadata. Locator is not identity. Rights/quarantine state follows the identity across aliases.

### CD-M04 — Human directives may supersede policy but cannot create empirical truth

Factory `ActiveDirectiveSet` correctly elevates durable scoped owner directives. Technical synthesis requires `EVIDENCE_REQUIRED` predicates and old-policy/meta-verification for judge-affecting changes. The boundary between those authorities is not yet explicit.

The current repository demonstrates why this matters: Issue #27 comment `5249227987` validly directs the current master agent to continue the existing lease immediately. That changes ownership/continuation policy for the project operation; it does not prove an engine capability, close trust debt, or make an unrun experiment PASS.

**Required correction.** Final authority model must state:

- directives can change goals, priorities, constraints, resource assumptions, or explicitly supersede policy requirements within scope;
- a directive cannot mutate an observation/evidence result (`FAIL`→`PASS`) or fabricate `EvidenceSatisfaction`;
- if a directive intentionally changes/waives a requirement, it creates a new `PolicyEpoch` / task-claim requirement version with provenance; prior evidence is reevaluated against the new requirement rather than relabeled;
- emergency safety stop remains immediate;
- directive scope is included in READY/claim/integration snapshots.

### CD-M05 — Implementation-readiness blockers are fragmented across domains

Game synthesis has `IR-BLOCKER-ACCESSIBILITY-CURRENT`; technical synthesis marks many decisions `EVIDENCE_REQUIRED`/`DEFERRED`; factory synthesis carries trust debt, rights/provenance quarantine, risk floors, and unverified factory mechanisms.

**Failure scenario.** Final synthesis clears “implementation readiness” because accessibility research passed while engine selection, protected evaluator trust, migration/hash evidence, or material rights/provenance remains unresolved—or blocks all work because one narrow evidence debt is incorrectly treated as global.

**Required correction.** Define one `ImplementationReadinessLedger` with typed blocker scope:

```yaml
blocker_id: <stable>
category: PRODUCT | TECHNICAL | FACTORY_TRUST | EVIDENCE | ACCESSIBILITY | RIGHTS | PLATFORM | OTHER
scope: GLOBAL | DOMAIN | FEATURE_CLASS | PLATFORM | TOOLING
blocks: [PRODUCTION_IMPLEMENTATION, RELEASE, CANONICAL_DECISION, <specific decision IDs>]
source_requirement_refs: []
resolution_predicate: <typed>
evidence_satisfaction_refs: []
state: OPEN | RESOLVED | SUPERSEDED
```

Full implementation readiness requires zero OPEN blockers whose scope includes `PRODUCTION_IMPLEMENTATION`. Narrow blockers must not freeze unrelated planning experiments/research.

### CD-M06 — `EVIDENCE_REQUIRED` needs typed dependency edges or the scheduler can either serialize the wave or leak unproven choices

Technical synthesis names ten evidence families; factory scheduler consumes hard dependencies; game synthesis names many experiments. There is no shared edge type describing what an evidence result actually blocks.

**Failure scenario.** All evidence families become global `BLOCKED_BY`, creating a serial mega-gate, or none become hard dependencies and implementation starts with unverified assumptions.

**Required correction.** Final dependency model must type evidence edges, at least:

- `BLOCKS_DECISION(decision_id)`
- `BLOCKS_IMPLEMENTATION_SCOPE(scope_id)`
- `BLOCKS_RELEASE_SCOPE(scope_id)`
- `INFORMS_DECISION`
- `CALIBRATES_EVALUATOR`
- `REOPENS_ON_FAILURE`

The scheduler derives readiness from the exact target decision/scope, not “all empirical work complete.” Independent evidence tasks may execute in parallel when conflict/output ownership permits.

### CD-M07 — Game time, semantic graph, and generative authority need exact technical mappings

Game synthesis introduces `GameTimePolicy`, `GameSemanticGraph`, and `GenerativeRuntimeBoundary`; technical synthesis introduces runtime/content identity, replay boundary classes, evidence surfaces, and external outcome classes. They are compatible but not mechanically mapped.

**Required correction.** Final synthesis must specify mappings such as:

- `GameTimePolicy.version` is part of `simulation_rules_version` / claim content identity and is mandatory in replay/evidence where time affects outcomes;
- `GameSemanticGraph.graph_version` is part of claim/coverage identity for semantic-coverage/lifestyle/progression evidence;
- `RUNTIME_PRESENTATION_ONLY` → technical `PRESENTATION_ONLY`;
- `RUNTIME_CANONICAL_EFFECT` must produce a validated canonical command/effect whose nondeterministic service result is `RECORDED_CANONICAL_OUTCOME` (or stronger declared deterministic class);
- build-time generated candidates are content artifacts before canonical runtime identity, not replay-time services;
- accepted generative outputs/effects use shared `ArtifactIdentity` / content-package / migration semantics.

No domain may define a second independent replay authority.

### CD-M08 — Subjective panel trust, evaluator fingerprints, and factory trust profiles need one judgment record

Game `SubjectivePanelTrust` needs evaluator/context/evidence diversity; factory has multidimensional trust profiles and risk floors; technical synthesis has `EvaluatorFingerprint` and `ExecutionEvidenceEnvelope`.

**Failure scenario.** Five calls to one mutable model are counted as a diverse panel because game metadata says “multiple evaluators,” while factory trust and technical fingerprints reveal one correlated context/provider.

**Required correction.** Define a shared `JudgmentPanelRecord` (or equivalent) that binds:

- each evaluator fingerprint;
- episode/private-context relation;
- oracle/evidence-source relation;
- candidate-write permissions;
- prompt/rubric/order randomization refs;
- evidence envelope refs;
- correlation groups/provider/model-family assumptions;
- disagreement/result dimensions;
- factory trust-profile result and risk-floor requirement.

Panel size never upgrades independence automatically. DEGRADED_SINGLE_AGENT remains explicit when stronger isolation is absent.

### CD-M09 — Shared schema/interface ownership needs an explicit authority map to preserve parallelism

All syntheses favor stable IDs, distributed namespaces, generated indexes, typed contracts, and content-addressed manifests. But shared cross-domain objects now include directives, task claims, evidence, artifact identity, semantic graph, time policy, content packages, trust, readiness blockers, and next-wave manifests.

**Failure scenario.** Final synthesis writes all of them into one canonical manually edited “global schema” file or leaves multiple domains free to define the same type, reintroducing central merge contention or semantic forks.

**Required correction.** Emit a `DomainAuthorityMap` / interface registry with, per type:

- canonical schema owner;
- producer namespaces allowed to extend it;
- generated index/package owner;
- cross-domain references allowed;
- mutation/review route;
- conflict keys/output paths;
- version compatibility policy.

Cross-domain aggregate indexes should be generated deterministically from domain-owned sources wherever feasible.

### CD-M10 — Current/external evidence freshness has no shared lifecycle

Engine discovery depends on current primary docs; accessibility blocker depends on current standards/platform rules; originality/rights may depend on provider/terms/legal research; evaluator fingerprints can drift; GitHub control-plane assumptions can change with platform behavior.

**Failure scenario.** A dated evidence package remains structurally reachable and therefore appears valid indefinitely after a target platform, engine version, provider terms, GitHub capability, or evaluator backend changes materially.

**Required correction.** Define `FreshnessRequirement` with source class, evidence date/version, invalidation triggers, optional maximum age only where justified, and re-research predicate. Freshness is event/version-sensitive rather than a universal time TTL. A stale external claim yields `INCONCLUSIVE`/reopen for dependent decisions; it does not erase historical provenance.

### CD-M11 — The next-wave promotion manifest must carry the authority/evidence/readiness semantics, not only issue titles and dependencies

Issue #41 already requires typed bounded promotion data, but the three syntheses now introduce decision states, evidence families, risk floors, artifact ownership, blocker scopes, and experimental execution restrictions.

**Failure scenario.** Final synthesis emits a new issue for “engine spike” with a dependency but omits `PLANNING_EXPERIMENT`, output conflict keys, evidence-promotion target, risk/review route, and readiness scope. The next wave regresses to prose interpretation.

**Required correction.** Next-wave compiler schema must include or resolve at least:

- mission ID / role / priority;
- task class including `PLANNING_EXPERIMENT` where relevant;
- authoritative input refs;
- exact owned output paths/conflict keys;
- hard and typed evidence dependencies;
- decision IDs/evidence predicates it can advance;
- `RiskFloor` / required review/verification classes;
- decision state (`CANDIDATE_CONTRACT`, `EVIDENCE_REQUIRED`, etc.);
- implementation-readiness blocker scope affected;
- context budget/retrieval triggers;
- handoff/status route;
- downstream promotion target;
- explicit non-production/canonicality restrictions for experiments.

Compiler validation must reject collisions, cycles, missing evidence routes, and experiment→production authority leakage.

### CD-M12 — Lease ownership override and independence capability are separate resource facts

The current owner directive makes the master agent the continuation owner of existing leases; it does **not** create a second independent execution context. Factory `TrustDebt` and technical/game degraded trust therefore remain open.

**Failure scenario.** Final synthesis interprets “all leases are yours” as `MULTI_AGENT_OR_ISOLATED_CONTEXT_AVAILABLE`, closes degraded review debt, and upgrades prior results to FULL independence without new evidence.

**Required correction.** Define a machine-visible `ResourceCapabilityState` distinct from `ActiveDirectiveSet`, covering available concurrent/isolated execution contexts, permission separation, protected-oracle control, and any relevant agent/tool capability. TrustDebt reopen/closure uses this capability state plus new stronger results—not ownership convenience. The active directive `5249227987` should be included in the final active directive set for operational provenance but must not alter trust profile by implication.

## 5. MINOR findings

### CD-m13 — `RetentionEdge` should cover generated compiler inputs, not only final evidence

If a next-wave issue contract depends on a schema/policy/graph blob, GC must retain that exact source even when the generated index is retained.

### CD-m14 — Readiness ledger should retain negative evidence and supersession history

Resolving a blocker must not delete the failed/outdated evidence that explains why the blocker existed or what changed.

### CD-m15 — Cross-domain version tuples should use one compatibility vocabulary

Schema, game-time, semantic-graph, evaluator, task-policy, content-package, and engine/runtime versions should declare compatibility as exact/compatible/migration-required/incompatible rather than each inventing different prose semantics.

### CD-m16 — Bounded context indexes should surface unresolved cross-domain risks first

Fresh agents executing evidence/verification work should see active blocker/evidence/dependency summaries before large historical provenance, while retaining exact refs for targeted retrieval.

## 6. NOTES

### CD-N01 — No domain is attempting to seize canonical authority prematurely

All three syntheses remain NON_CANONICAL, preserve squash-only integration, and explicitly route through cross-review/final verification.

### CD-N02 — Distributed ownership is a coherent shared design principle

Factory conflict keys, technical schema namespaces, and game semantic/content IDs all favor narrow ownership plus generated composition. Final synthesis should preserve that structure rather than centralizing for convenience.

## 7. Disposition

`CHANGES_REQUIRED`.

- BLOCKER: 1
- MAJOR: 11
- MINOR: 4
- NOTE: 2

`W1-SYN-FINAL` may proceed and MUST explicitly disposition CD-B01 and CD-M02 through CD-M12. The final synthesis must preserve every unrun evidence obligation and may not declare high-throughput/gameplay implementation readiness merely by composing the three synthesis candidates.

## 8. Reopen conditions

Reopen this cross-review if:

- any of the three bound synthesis work SHAs changes;
- final synthesis cannot eliminate the planning-experiment/readiness circularity;
- more than one acceptance/evidence authority can independently produce PASS;
- human directive semantics can fabricate evidence or silently close trust debt;
- a game canonical effect bypasses the technical replay/state boundary;
- next-wave compiler data omits risk/evidence/ownership/readiness semantics;
- shared interface ownership collapses into a central manual bottleneck;
- stronger isolated/multi-agent review capability becomes available.
