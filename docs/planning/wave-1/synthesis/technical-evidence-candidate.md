# Technical and Evidence Synthesis Candidate — Wave 1

**Mission:** `W1-SYN-TECH`  
**State:** SYNTHESIS CANDIDATE / NON-CANONICAL  
**Required next review:** `W1-REV-CROSS`

## 1. Purpose and authority

This document reconciles the exact reviewed work states of W1-FAC-02, W1-FAC-03, W1-FAC-04, W1-TEC-01, W1-TEC-02, and W1-EVAL-01 with W1-REV-TECH `CHANGES_REQUIRED` work `3bbd540b5e3718c3483aa8d1ba6dc1c8ae1ca2b2`.

It is a correction/synthesis surface, not a replacement for producer provenance and not an implementation authorization. It selects **no engine**, installs no GitHub control-plane mechanism, creates no gameplay code, and treats all named empirical work as unrun unless explicitly stated otherwise.

## 2. Exact input binding

The authoritative synthesis packet is `docs/planning/wave-1/synthesis/technical-evidence-input.yaml`. Producer and reviewer branches are immutable for this episode.

Reviewed producer work SHAs:

- W1-FAC-02: `095372a41498e8d7e3b25364cba89dbc647b8839`
- W1-FAC-03: `70b763a965cdec0fa1f6c025a5b7492b844288fc`
- W1-FAC-04: `99b0c7b3bddbad1a71e05f085fd0bd9f2c74e566`
- W1-TEC-01: `3b1e159932b2d23d6641e0ba3e97dfa72da10219`
- W1-TEC-02: `c13389cf1df7ab8e2515a5267bd56869082df1b2`
- W1-EVAL-01: `a29a9c08f64947b383f4ca6a19fb88032d93777d`

Review status: Issue #35 comment `5249289275`, disposition `CHANGES_REQUIRED`, 0 BLOCKER / 12 MAJOR.

## 3. Decision-state taxonomy and promotion barrier

Every technical recommendation carried forward from this synthesis has exactly one state:

- **`CANDIDATE_CONTRACT`** — coherent interface/semantic rule suitable for downstream planning, but still non-canonical until Wave 1 verification/canonicalization.
- **`EVIDENCE_REQUIRED`** — proposed mechanism or capability whose truth/fitness depends on an unrun experiment or current external/platform evidence. It MUST NOT be compiled into implementation as a settled choice.
- **`VERIFIED_DECISION`** — reserved for a later exact evidence result that satisfies its declared promotion predicate and review route. This synthesis creates none.
- **`DEFERRED`** — intentionally unresolved because downstream product/platform/system choices are prerequisites.

A later task compiler MUST preserve this state. `EVIDENCE_REQUIRED` may become `VERIFIED_DECISION` only through the named evidence predicate and its declared review/verification route. A prose recommendation, REVIEW_READY status, or high aggregate score is never that predicate.

This closes TE-M12.

## 4. Unified execution and evidence authority

### 4.1 `ExecutionEvidenceEnvelope` — `CANDIDATE_CONTRACT`

All material runtime, CI, engine-spike, synthetic-player, protected-verification, benchmark, or replay evidence MUST compose through one versioned identity envelope. Domain records may extend it but cannot redefine its identity fields.

Conceptual minimum:

```yaml
execution_evidence_envelope_version: 1
evidence_id: <stable/content-addressed identity>
claim_set_ref: <exact claim/task contract version>
candidate:
  work_sha: <sha>
  head_sha: <sha>
  base_main_sha: <sha>
  build_or_package_ref: <optional immutable ref>
runtime_identity:
  engine_runtime_ref: <version/fingerprint or NOT_APPLICABLE>
  toolchain_refs: []
  environment_fingerprint: <immutable/reproducible identity>
content_identity:
  content_package_hash: <optional>
  canonical_schema_set_ref: <optional>
execution_surface: MODEL_SIMULATION | SHARED_KERNEL | FULL_EXECUTABLE | CONTROL_PLANE | FACTORY_BENCHMARK | OTHER
scenario:
  scenario_id: <stable>
  scenario_version: <version>
  policy_or_action_ref: <immutable ref>
  input_hashes: []
  seeds_or_randomness_manifest: <optional ref>
evaluator:
  evaluator_refs: []
  evaluator_fingerprint_refs: []
attempt:
  lineage_id: <stable>
  attempt_index: <integer>
  retry_reason: <optional typed>
result: PASS | FAIL | FLAKY | INCONCLUSIVE | NOT_RUN | NOT_APPLICABLE
artifacts:
  - content_hash: <hash>
    storage_ref: <locator>
    kind: <typed>
trust_profile_ref: <versioned profile>
known_nondeterministic_surfaces: []
known_coverage_gaps: []
```

Identity comparison MUST include every field capable of changing the interpretation of a result. Mutable URLs or dashboard state are observational unless snapshotted/content-addressed.

### 4.2 Evidence extensions

- W1-FAC-04 `Run Report` is an execution/report aggregation extension over this envelope.
- W1-FAC-03 `EvidenceBundle` is a claim-level collection of envelopes plus trust/coverage requirements.
- W1-TEC-01 engine run manifests are engine-comparison extensions.
- W1-TEC-02 determinism/save/content manifests provide runtime/content identity subrecords.
- W1-EVAL-01 scenario/policy/evaluator records provide game-evaluation subrecords.

This closes TE-M01 while retaining domain ownership.

## 5. Canonical semantic state and hash contract

### 5.1 Semantic state boundary — `CANDIDATE_CONTRACT`

Gameplay-authoritative state remains engine-independent logical state. Engine/editor/render/audio/platform representations may adapt or mirror it but cannot be the sole durable meaning of gameplay state.

### 5.2 Canonical semantic encoding — `EVIDENCE_REQUIRED`

Cross-runtime or cross-engine state-hash equality is forbidden as authoritative evidence until a `CanonicalSemanticEncoding` version exists and passes conformance evidence.

The encoding specification must define:

- deterministic field/record ordering;
- map/set ordering and duplicate policy;
- stable ID/reference encoding;
- integer width/range behavior;
- floating/fixed/decimal numeric representation and exceptional-value policy;
- string encoding and Unicode normalization;
- timestamp/time-unit representation;
- null, absent, default, unknown-field semantics;
- schema/content-version inclusion;
- canonical byte or semantic tree representation;
- hash algorithm and hash-scope version;
- treatment of derived/cache/transient state;
- cross-language/runtime conformance vectors.

**Promotion predicate `TECH-EV-HASH-CONFORMANCE`:** at least two independent adapter implementations or engine/runtime candidates consume the same conformance corpus and produce identical canonical semantic encodings/hashes for all required vectors, including adversarial ordering/numeric/string/reference cases, with independent review.

Until then, hashes are valid only within the declared encoding/runtime scope.

This closes TE-M02.

## 6. Determinism, external inputs, and causal ordering

### 6.1 Boundary interaction classes — `CANDIDATE_CONTRACT`

Every canonical-state-affecting adapter/service interaction is classified as one of:

- **`PURE_DETERMINISTIC_INPUT`** — result is fully determined by recorded canonical inputs under a versioned implementation.
- **`RECORDED_NONDETERMINISTIC_INPUT`** — external/nondeterministic input is captured as part of the evidence/replay input stream.
- **`RECORDED_CANONICAL_OUTCOME`** — service/physics/generation may be nondeterministic internally, but the accepted canonical outcome is explicitly recorded and replay substitutes that outcome.
- **`PRESENTATION_ONLY`** — may vary without changing future canonical gameplay state.

Anything outside these classes is not admissible in the deterministic evidence boundary.

Physics, asynchronous platform services, wall-clock features, remote/generative services, and hardware-dependent calculations MUST explicitly select a class before they may affect canonical state.

### 6.2 Replay contract

A replayable claim binds:

- semantic encoding/hash-scope version;
- simulation rules version;
- content/schema package identity;
- game-time model;
- RNG stream algorithms/versions/seeds or recorded outcomes;
- canonical external inputs/outcomes;
- ordered/causal action stream;
- initial snapshot identity;
- expected invariant/event/final-state evidence;
- known presentation-only nondeterminism.

### 6.3 Causality and order — `CANDIDATE_CONTRACT`

Do not equate determinism with one globally serialized event log.

Each domain declares:

- deterministic local ordering key;
- causal dependencies among events/commands;
- cross-domain synchronization points;
- stable tie-breaker for simultaneous otherwise-order-sensitive effects;
- whether operations are commutative/order-independent;
- whether a stronger total order is required for that claim/domain.

A global total order remains a fallback representation, not a default implementation mandate.

**Promotion predicate `TECH-EV-ORDERING`:** contention/replay experiments compare candidate ordering models under representative concurrent domain interactions and demonstrate deterministic reproduction plus acceptable throughput/conflict behavior.

This closes TE-M03 and TE-M04.

## 7. Persistence, schema, content, and migration

### 7.1 Durable identity tuple — `CANDIDATE_CONTRACT`

A save is interpreted by a tuple, not one integer:

```text
(save_envelope_version,
 canonical_schema_set_identity,
 content_package_identity,
 simulation_rules_version,
 migration_tool_version)
```

### 7.2 Migration graph

Each migration edge binds source tuple → target tuple and declares:

- structural transforms;
- semantic transforms;
- renamed/split/merged/removed identity rules;
- orphaned/removed content behavior;
- defaults and whether they are lossy;
- invariants before/after;
- deterministic tool/version identity;
- loss/warning report schema;
- rollback/recovery behavior;
- fixtures and expected hashes where meaningful.

Required properties:

- same input + same migration/tool/content versions is deterministic;
- migration does not mutate source fixtures in place;
- repeated application to an already-target state is rejected or demonstrably idempotent by declared semantics;
- composed historical migration paths are tested, not only adjacent versions;
- unsupported downgrade is explicit and never silently attempted;
- unknown required state or ambiguous semantic removal fails closed or produces a reviewed explicit recovery path.

**Promotion predicate `TECH-EV-MIGRATION`:** historical fixtures spanning multiple schema/content changes, including removed/renamed references and corruption cases, pass independent migration/invariant/recovery tests.

This closes TE-M05.

## 8. Engine evaluation and ADR safety

### 8.1 Candidate discovery — `EVIDENCE_REQUIRED`

The engine candidate set is created from current primary sources under a recorded discovery protocol:

- target/product assumptions currently known;
- search/discovery date;
- inclusion criteria;
- exclusion reason for each materially plausible omitted candidate;
- current source refs;
- material unknowns.

The set is bounded, but “bounded” cannot mean cherry-picked. Review may require adding a candidate if omission evidence is insufficient.

### 8.2 Spike equivalence

Every common spike has:

- engine-neutral scenario intent;
- required observable outcomes;
- evidence fields;
- scale envelope;
- failure injection;
- repetition policy;
- candidate adaptation manifest;
- explicit deviations and adapter/tooling effort.

Before comparative scoring, an independent review confirms the candidate adaptations exercise equivalent claims. If equivalence cannot be established, the dimension is `INCONCLUSIVE` rather than scored by intuition.

### 8.3 Engine decision states

- Engine candidate research/spikes: `EVIDENCE_REQUIRED`.
- Engine selection: `DEFERRED` until all mandatory admission/spike/review predicates are satisfied.
- No engine is `VERIFIED_DECISION` in Wave 1 synthesis.

### 8.4 Conditional Milestone Zero selection

A later ADR may conditionally choose an engine only if it records:

- exact evidence set and target assumptions;
- unresolved risks;
- explicit falsifier;
- deadline/checkpoint or evidence event that reopens the decision;
- exit/migration plan;
- architecture surfaces prohibited from becoming irreversibly engine-specific before the checkpoint.

This closes TE-M06.

## 9. Protected evidence and trust

### 9.1 Protected-result envelope — `CANDIDATE_CONTRACT`

A protected oracle may hide sensitive inputs but MUST publish/refer to a durable result envelope containing:

- exact candidate/base/environment identities;
- protected oracle/evaluator stable ID and version/content hash;
- claim/coverage category;
- result class;
- bounded diagnostic/failure category sufficient to distinguish product failure from infrastructure/evaluator failure;
- immutable protected evidence reference/access-policy reference;
- trust profile;
- calibration/fingerprint result where applicable;
- reveal/change audit references.

If protected storage/oracle is unavailable, corrupt, unverifiable, or lacks required identity, the result is `INCONCLUSIVE`; no visible check can silently substitute unless the task contract explicitly declares a reviewed replacement.

### 9.2 Disclosure and change

Protected inputs/configuration changes are judge-affecting meta-changes. Reveal events record scope, actor/authority, reason, affected holdout IDs/versions, and whether compromised cases must be rotated/replaced. Producers cannot approve weakening their own sole protected gate.

### 9.3 Artifact availability

Content hash proves identity, not availability. Canonical/protected evidence retention includes periodic or event-driven reachability/integrity audits plus restoration/escalation behavior. Lost required canonical evidence reopens affected authority rather than leaving an unverifiable PASS.

This closes TE-M07 and incorporates TE-m01.

## 10. GitHub/control-plane evolution

### 10.1 Current authority remains schema 3 — `CANDIDATE_CONTRACT`

The current canonical schema-3 issue/comment/ref fencing protocol remains authority until a later factory/control-plane change is independently benchmarked, reviewed, verified, and canonicalized.

The proposed GitHub GraphQL multi-ref ownership/conflict-lock transaction is **`EVIDENCE_REQUIRED`**, not replacement authority.

### 10.2 Required lock/CAS experiment

`TECH-EV-GH-CAS` must test in the actual repository/account/ruleset environment:

- atomic create/update of task + multiple conflict refs with expected old OIDs/nonexistence;
- duplicate claimant race;
- crash after ref transaction before authority/audit event;
- event without expected refs;
- stale lease renewal/recovery;
- multi-lock acquisition ordering and deadlock avoidance;
- ruleset/ref namespace interactions;
- permission failure;
- webhook duplication/loss and reconciliation;
- lock/ref garbage collection;
- task branch advancement and stale writer fencing;
- squash integration compatibility.

The experimental reconciliation state machine MUST explicitly classify at least:

```text
NO_TRANSACTION
REFS_CREATED_EVENT_MISSING
EVENT_PRESENT_REFS_MISMATCH
ACTIVE_LOCKED_OWNER
STALE_LOCKED_OWNER
RECOVERY_IN_PROGRESS
TERMINAL_LOCK_RELEASE_PENDING
GC_SAFE
```

No state may infer “free” merely because a comment or derived UI field is missing.

### 10.3 Promotion predicate

The mechanism can supersede schema-3 ownership only after repository-specific evidence passes the above race/crash/recovery suite, the permission/ruleset composition is established, and a judge-affecting factory protocol change passes independent meta-review/verification.

This closes TE-M08.

## 11. CI applicability, result algebra, flake, and quarantine

### 11.1 Compiled check plan — `CANDIDATE_CONTRACT`

Before execution, task/claim compilation produces an immutable `CheckPlan`:

```yaml
check_plan_version: <version>
claim_set_ref: <exact>
candidate_ref: <exact>
checks:
  - check_id: <stable>
    applicability: REQUIRED | OPTIONAL | CONDITIONALLY_REQUIRED | NOT_APPLICABLE
    applicability_basis: <typed predicate/evidence>
    allowed_execution_surfaces: []
    minimum_trust_profile: <ref>
    replacement_or_quarantine_policy_ref: <optional>
```

`NOT_APPLICABLE` is a predeclared applicability result, distinct from `NOT_RUN`.

### 11.2 Aggregate rules

- any required `FAIL` => aggregate cannot PASS;
- any required `FLAKY`, `INCONCLUSIVE`, or `NOT_RUN` => aggregate cannot PASS unless a reviewed task-contract rule provides valid replacement evidence for that exact claim;
- conditionally required checks are resolved before aggregate judgment from their recorded predicate inputs;
- optional failure may still create a finding/reopen route but cannot be silently discarded;
- retries append attempt lineage and do not erase prior outcomes;
- infrastructure failures are typed separately in diagnostics but still prevent required-evidence PASS until a valid attempt exists under policy;
- quarantine never converts a failing check to PASS: it replaces one evidence obligation with an explicit scoped temporary contract, owner/remediation, replacement evidence, expiry, and reopen condition.

### 11.3 Cost evidence

Engine/factory CI reports separate:

- cold environment/tool acquisition;
- clean build/import;
- incremental build/test;
- cache warmup/hit/miss behavior;
- execution/capture/profile cost;
- artifact storage/egress where measurable;
- agent action/retry/context burden;
- custom adapter maintenance burden.

This closes TE-M09 and incorporates TE-m02.

## 12. Evaluator/toolchain drift

### 12.1 Fingerprint — `CANDIDATE_CONTRACT`

High-impact evaluator evidence records both declared version and an `EvaluatorFingerprint`:

```yaml
evaluator_id: <stable>
declared_version_refs: []
config_hashes: []
prompt_or_rubric_hashes: []
tool/provider/model refs: []
host/environment refs: []
calibration_corpus_ref: <immutable/protected as needed>
calibration_result_fingerprint: <distribution/hash>
known_unpinnable_components: []
```

### 12.2 Mutable provider policy

Where backend implementation cannot be immutably pinned:

- calibrate on a frozen benchmark/holdout schedule and on material provider/config changes;
- retain result distributions and disagreement, not only one scalar;
- declare drift thresholds/diagnostic criteria by evaluator class;
- cross the threshold => evaluator evidence becomes suspect and affected authority is re-evaluated according to risk;
- missing fingerprint/calibration for a high-impact subjective/protected result => INCONCLUSIVE.

This closes TE-M10.

## 13. Evidence execution surfaces and admissibility

### 13.1 Surface types — `CANDIDATE_CONTRACT`

- `MODEL_SIMULATION` — simplified/abstract model; useful for hypothesis generation, search, distributions, broad sensitivity.
- `SHARED_KERNEL` — executes the same authoritative domain/game rules as production without necessarily rendering full presentation.
- `FULL_EXECUTABLE` — production-shaped executable/player surface plus canonical state evidence.
- `CONTROL_PLANE` — repository/GitHub/CI protocol execution.
- `FACTORY_BENCHMARK` — controlled development-factory task/defect experiment.

### 13.2 Claim admissibility

| Claim | Minimum authoritative surface |
|---|---|
| abstract economy/progression hypothesis | MODEL_SIMULATION, with model identity/limits |
| canonical gameplay rule correctness | SHARED_KERNEL |
| integration of engine adapters/player-visible execution | FULL_EXECUTABLE or exact declared equivalent plus SHARED_KERNEL state evidence |
| persistence/migration | SHARED_KERNEL/current canonical data implementation; full executable when adapter integration is claimed |
| engine autonomous-operability | CONTROL_PLANE + candidate engine spike surfaces |
| factory protocol correctness | CONTROL_PLANE / FACTORY_BENCHMARK |
| UX/visual/audio experiential claim | FULL_EXECUTABLE/player-surface evidence plus required state/evaluator evidence |

Model simulation cannot independently PASS a claim about production/shared-kernel behavior. Differential comparison against the shared kernel is a required calibration when model results influence acceptance/balance decisions.

This closes TE-M11.

## 14. Namespace and schema ownership

### 14.1 Distributed ownership — `CANDIDATE_CONTRACT`

Domain schemas/registries own narrow namespaces. A generated deterministic package/index may compose them, but no ordinary domain task owns one manually edited global registry.

Namespace registry semantics must include:

- stable namespace ID;
- owner/domain;
- allocation and collision check;
- schema/package dependencies;
- transfer/supersession history;
- deprecation/tombstone policy;
- forbidden semantic reuse of retired IDs;
- compile-time duplicate/cycle/reference validation.

This incorporates TE-m03.

## 15. Scenario and expected-result governance

Golden/protected scenario expected-result changes must record a reason class:

- `INTENDED_PRODUCT_SPEC_CHANGE`
- `SCENARIO_OR_ORACLE_CORRECTION`
- `BASELINE_REGEN_WITH_NO_SEMANTIC_CHANGE`
- `DEFECT_FIX_EXPECTATION_UPDATE`
- `OTHER_REVIEWED`

The change binds old/new scenario/evaluator/candidate identities, supporting evidence, and review route. “Make current output green” is not a valid reason.

This incorporates TE-m04.

## 16. Engine/runtime/evidence decision map

| Decision | State now | Promotion evidence |
|---|---|---|
| engine-independent canonical gameplay meaning | CANDIDATE_CONTRACT | cross-review + final Wave 1 verification |
| command/event/query typed boundary | CANDIDATE_CONTRACT | cross-review + final Wave 1 verification |
| unified ExecutionEvidenceEnvelope | CANDIDATE_CONTRACT | cross-review + final Wave 1 verification |
| canonical semantic encoding/hash format | EVIDENCE_REQUIRED | `TECH-EV-HASH-CONFORMANCE` |
| external/nondeterministic outcome classification | CANDIDATE_CONTRACT | cross-review + implementation-spec validation |
| concrete causal/event ordering implementation | EVIDENCE_REQUIRED | `TECH-EV-ORDERING` |
| version-tuple migration contract | CANDIDATE_CONTRACT | cross-review; real migrations remain evidence-required |
| concrete save encoding/database | DEFERRED | engine/runtime/content specs |
| GitHub multi-ref ownership/lock CAS | EVIDENCE_REQUIRED | `TECH-EV-GH-CAS` + meta-review/verification |
| current schema-3 ownership authority | CANDIDATE_CONTRACT / retained current authority | superseded only by verified canonical change |
| protected evidence storage topology | DEFERRED | trust/storage/platform experiment |
| protected result envelope | CANDIDATE_CONTRACT | cross-review + final verification |
| engine candidate set and capability matrix | EVIDENCE_REQUIRED | current-source discovery/admission research |
| engine selection | DEFERRED | complete comparative spikes + ADR review route |
| abstract simulation acceptance boundaries | CANDIDATE_CONTRACT | cross-review + final verification |
| specific evaluator/model capability | EVIDENCE_REQUIRED | calibration/benchmark evidence |
| implementation readiness | DEFERRED / BLOCKED | final planning readiness route, not this synthesis |

## 17. Named technical evidence program

The following bounded evidence families are required downstream. They are candidate next-wave work data, not self-instantiated issues here.

### `TECH-EV-GH-CAS`
Repository-specific multi-ref CAS/lease/conflict-lock/race/crash/recovery/GC/ruleset experiment.

### `TECH-EV-ENGINE-ADMISSION`
Current primary-source candidate discovery/admission matrix with selection rationale and target-assumption binding.

### `TECH-EV-ENGINE-SPIKES`
Common S1–S10 autonomous engine spikes with adaptation equivalence review, repeated attempts, failure retention, cost distributions, and fresh continuation.

### `TECH-EV-HASH-CONFORMANCE`
Canonical semantic encoding and cross-runtime conformance vectors.

### `TECH-EV-ORDERING`
Causality/order/replay/contention experiment for domain-local versus stronger event ordering.

### `TECH-EV-MIGRATION`
Historical save/schema/content migration, removal/rename/corruption/recovery matrix.

### `TECH-EV-PROTECTED`
Protected evidence store/result/disclosure/change/availability experiment.

### `TECH-EV-EVALUATOR-DRIFT`
Evaluator fingerprint/calibration/drift/reopen experiment.

### `TECH-EV-SIM-PARITY`
Abstract/model simulation against shared-kernel differential corpus.

### `TECH-EV-CI-RELIABILITY`
CheckPlan aggregation, injected flake/infra failure/quarantine/retention/recovery experiment.

Every family must emit `ExecutionEvidenceEnvelope`-compatible evidence once that schema is canonicalized.

## 18. W1-REV-TECH finding dispositions

| Finding | Disposition | Synthesis correction |
|---|---|---|
| TE-M01 | ACCEPTED / CORRECTED | §4 unified execution/evidence envelope + extension rules |
| TE-M02 | ACCEPTED / CORRECTED | §5 canonical semantic encoding + conformance promotion predicate |
| TE-M03 | ACCEPTED / CORRECTED | §6.1 typed deterministic/nondeterministic boundary outcomes |
| TE-M04 | ACCEPTED / CORRECTED | §6.3 causal/domain ordering; total order no longer default implementation mandate |
| TE-M05 | ACCEPTED / CORRECTED | §7 version-tuple migration graph and semantic compatibility tests |
| TE-M06 | ACCEPTED / CORRECTED | §8 candidate discovery rationale, adaptation equivalence review, conditional-selection expiry |
| TE-M07 | ACCEPTED / CORRECTED | §9 protected-result envelope, disclosure/change and availability rules |
| TE-M08 | ACCEPTED / CORRECTED | §10 schema-3 retained; multi-ref CAS remains evidence-required with explicit experiment |
| TE-M09 | ACCEPTED / CORRECTED | §11 immutable CheckPlan, applicability and result aggregation algebra |
| TE-M10 | ACCEPTED / CORRECTED | §12 evaluator fingerprint/calibration/drift reopen policy |
| TE-M11 | ACCEPTED / CORRECTED | §13 typed execution surfaces and claim admissibility |
| TE-M12 | ACCEPTED / CORRECTED | §3 decision states and mandatory evidence-promotion predicates |

All review MAJORs are dispositioned. No review finding is rejected by assertion.

## 19. Interface dependencies for cross-domain review

W1-REV-CROSS should particularly test these interfaces:

1. **Factory ↔ technical evidence:** whether W1-SYN-FAC task/trust/control contracts can carry `ExecutionEvidenceEnvelope`, `CheckPlan`, and decision-state semantics without duplicate authority.
2. **Game ↔ technical state:** whether W1-SYN-GAME world/time/generative/evaluator contracts fit the semantic-state, external-outcome, execution-surface, content-package, and migration contracts here.
3. **Evidence ↔ scheduler:** whether an `EVIDENCE_REQUIRED` decision can be represented as a hard prerequisite without turning every experiment into one serial bottleneck.
4. **Protected trust ↔ debuggability:** whether protected result envelopes expose enough diagnostics while preserving holdout integrity.
5. **Engine ↔ game architecture:** whether engine spikes can exercise representative game/runtime interfaces without prematurely fixing final game mechanics or letting engine-specific objects become canonical state.
6. **Schema ownership ↔ continuous content:** whether distributed namespaces and package composition avoid central merge hotspots while retaining deterministic validation.

## 20. Verification contract for this synthesis

This candidate is `REVIEW_READY` only if the downstream status binds the exact work SHA containing:

- this synthesis;
- exact input manifest;
- all TE-M01..TE-M12 dispositions;
- explicit decision-state map;
- unresolved evidence families;
- implementation-readiness block;
- handoff.

W1-REV-CROSS must treat all `EVIDENCE_REQUIRED` entries as unproven and must attack contradictions with W1-SYN-FAC and W1-SYN-GAME. Final Wave 1 verification may not reinterpret them as settled implementation choices merely because this synthesis passes cross-review.

## 21. Open questions / deferred choices

Still unresolved:

- engine candidate set and engine choice;
- final target platforms;
- final runtime/language/ECS/physics/rendering stack;
- canonical semantic encoding implementation;
- final causal/event scheduling implementation;
- physical save encoding/database;
- protected evidence storage/provider/permission topology;
- mature GitHub ownership-lock implementation;
- exact evaluator technologies/models;
- performance/CI cost budgets;
- exact deep/protected check frequencies;
- final game-system schemas and content-package structure.

## 22. Reopen conditions

Reopen this synthesis if:

- any bound producer/review work SHA changes;
- cross-domain review finds an authority collision or circular dependency among factory/game/technical syntheses;
- evidence records cannot mechanically establish exact candidate/base/environment/content/evaluator identity;
- a supposedly deterministic result depends on an unrecorded nondeterministic outcome;
- cross-runtime hashes are used before encoding conformance passes;
- schema-3 authority is replaced before `TECH-EV-GH-CAS` plus meta-review/verification;
- engine selection occurs without engine admission/spike/ADR evidence;
- protected evidence can PASS while unavailable/unverifiable;
- an `EVIDENCE_REQUIRED` decision is compiled as settled implementation architecture;
- stronger independent execution becomes available and degraded reviews should be rerun.

## 23. Downstream state

This synthesis unblocks `W1-REV-CROSS` only after it reaches exact schema-3 `STATUS(REVIEW_READY)` and the factory/governance and game/experience syntheses are also REVIEW_READY.

It authorizes no gameplay implementation, engine selection, final platform choice, or canonicalization by itself.
