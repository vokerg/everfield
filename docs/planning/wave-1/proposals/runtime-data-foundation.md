# Runtime, Data, Determinism, Persistence, and Content Foundation — Wave 1 Proposal

**Mission:** `W1-TEC-02`  
**State:** PROPOSAL / NON-CANONICAL  
**Required reviews:** `W1-REV-TECH`, `W1-REV-GAME`

## Review Index

- **RDF-D1 — Canonical simulation boundary (§8):** gameplay-authoritative state lives in an engine-independent simulation model. Rendering, animation, audio, editor objects, and platform services are adapters and cannot be the sole canonical state.
- **RDF-D2 — Stable identity/schema boundary (§9):** globally stable typed IDs, explicit schema versions, reference validation, and deterministic content compilation are foundational extension interfaces.
- **RDF-D3 — Command/event/query boundary (§10):** external actors request changes through validated commands; authoritative mutations emit ordered events; queries expose read-only views. Direct cross-module mutation is rejected as the default architecture.
- **RDF-D4 — Determinism contract (§11):** deterministic gameplay scope is explicitly declared; RNG streams, clocks, iteration ordering, numeric rules, external inputs, and nondeterministic presentation are separated and recorded.
- **RDF-D5 — Persistence contract (§12):** saves are versioned canonical snapshots plus metadata, migrated through explicit forward transformations; replay and save compatibility are separate claims.
- **RDF-D6 — Content pipeline (§13):** source content is declarative where useful, schema-validated, reference-checked, compiled into deterministic runtime packages, and never trusted merely because an engine/editor can load it.
- **RDF-D7 — Observability/performance (§14):** simulation, persistence, content loading, event flow, and runtime adapters expose structured timings/counters and reproducible workload identities before concrete budgets are frozen.
- **RDF-D8 — Extension/conflict model (§15):** schemas/registries/modules own narrow namespaces; additions prefer append-only data and registered interfaces; global registries/monolithic save files are treated as concurrency hazards.
- **Evidence (§5):** authoritative packet requires determinism, replayable evidence, extensibility, explicit IDs/schemas, persistence, content validation, and machine-observable quality. No engine-specific/current external claim is needed for this proposal.
- **Experiments (§18):** deterministic replay, save migration, content-compiler conflict, corruption recovery, long-run simulation, and adapter-boundary spikes must falsify the design before implementation readiness.
- **Reviewer attack points:** hidden engine coupling; nondeterministic collection/order leaks; identity reuse; save migrations that mutate historical meaning; event-order ambiguity; global-schema bottlenecks; content bypasses; false reproducibility; performance metrics without stable workloads.

## 1. Objective

Define an engine-independent technical foundation that can support a very large, continuously extensible life-sim without making engine object graphs, editor state, or ad hoc serialization the source of gameplay truth.

The proposal covers runtime/data boundaries, canonical state and identity, command/event/query semantics, determinism, RNG/time, persistence and migration, content validation/compilation, performance observability, extension/conflict constraints, and the experiments needed before these choices become canonical.

## 2. Scope

In scope:

- canonical simulation versus presentation/platform boundaries;
- stable object/content identity;
- schema/version/reference rules;
- state mutation and observation interfaces;
- deterministic execution boundaries;
- RNG and clock discipline;
- save/snapshot/migration strategy;
- replay evidence requirements;
- content source/compile/validation pipeline;
- runtime/package loading contracts;
- error/corruption recovery expectations;
- performance instrumentation/workload identity;
- extension namespaces and merge/conflict constraints;
- verification experiments and reopen conditions.

## 3. Non-goals

This proposal does **not**:

- select an engine, language, ECS framework, database, serialization library, numeric format, physics system, or networking stack;
- define final gameplay systems or content schemas;
- claim lockstep determinism across all rendering/physics/platform behavior;
- promise backward-compatible replays forever;
- set unexplained CPU/memory/save-size budgets before representative workloads exist;
- require every game object to be data-only;
- turn internal extensibility into a public modding promise;
- authorize gameplay implementation.

## 4. Constraints and assumptions

### 4.1 Observed constraints from the authoritative packet

1. Everfield targets a large possibility space built from interacting systems, not inert catalog size.
2. Continuous expansion requires cheap addition of items, crops, recipes, machines, NPCs, quests, regions, and other content.
3. Later architecture should favor explicit IDs, schemas, registries, events, commands, queries, and validated references.
4. Evaluation must produce inspectable evidence including deterministic simulation, replay, save/load comparison, state invariants, telemetry, and performance metrics.
5. Important integration evidence should exercise the real executable or the same gameplay kernel used by it.
6. The autonomous factory should support substantial safe concurrency; merge-hostile central files are therefore an architectural risk.
7. Persistence, deterministic simulation/replay, content architecture, semantic coverage, and long-running simulations are explicit planning deliverables/research questions.

### 4.2 Assumptions to test

- A substantial gameplay core can be made deterministic enough for replayable test scenarios without forcing presentation/rendering to be deterministic.
- Stable logical IDs can remain independent from memory addresses, engine instance IDs, file locations, and display names.
- Most high-volume content can pass through declarative schemas/validation even when some behavior ultimately requires authored code.
- Forward save migration is safer and more testable than teaching every runtime subsystem to understand every historical schema.
- Event logs are valuable evidence and debugging tools but should not automatically become the sole persistence format.
- Performance budgets need representative scenario classes and scale envelopes before numeric limits are meaningful.

## 5. Evidence and inference

### 5.1 Evidence

The project documents explicitly require:

- deterministic or controlled gameplay execution from build/state/seed/action inputs;
- replay/save-load evidence;
- machine-visible canonical state alongside player-facing evidence;
- explicit IDs, schemas, registries, events, commands, queries, validated references, and data-driven content where appropriate;
- migration, content validation/compilation, stable references, and long-run simulation planning;
- architecture that remains extensible and conflict-tolerant under many agents.

### 5.2 Inference

From those requirements, an engine scene/resource hierarchy is an unsafe universal domain model: it couples canonical gameplay state to a selected tool/runtime and makes deterministic headless execution, migration, content compilation, and independent validation harder to reason about.

A smaller authoritative simulation model with explicit adapter boundaries gives reviewers a stable surface for deterministic evidence while allowing the engine choice to remain open.

### 5.3 Recommendation

Adopt the architecture contracts below as a **candidate technical baseline** subject to the named experiments and both required adversarial reviews.

## 6. Alternatives considered

### A. Engine object graph as canonical game state — reject as default

Advantages: fewer translation layers; fast prototype path.

Risks: engine coupling, opaque/editor-generated identity, harder headless evidence, save schema leakage, and merge-hostile resources. Engine objects may mirror or host adapters, but must not be the only authoritative representation of persistent gameplay meaning.

### B. Pure event sourcing for all persistence — defer/reject as universal rule

Advantages: auditability and replay-like history.

Risks: migration complexity, historical semantic drift, log growth, and replay/version coupling. Use events as evidence/domain history where valuable; keep versioned canonical snapshots as the baseline persistence primitive until experiments justify stronger event-sourced domains.

### C. One global schema/registry/save file — reject

Advantages: simple lookup and tooling initially.

Risks: conflict hotspot, broad ownership, difficult evolution, and huge validation blast radius. Prefer composable domain schemas/registries with explicit cross-references and a deterministic package/index layer.

### D. Runtime reflection/editor loadability as validation — reject

A resource loading successfully is not enough to prove references, uniqueness, progression constraints, migration compatibility, or domain invariants.

### E. Perfect determinism everywhere — reject

Rendering, audio, wall-clock services, hardware timing, and some engine facilities may remain nondeterministic. The project needs a declared deterministic **gameplay evidence boundary**, not a universal determinism fantasy.

## 7. Layer model

Recommended logical layers:

```text
content sources
  -> schema/reference validation
  -> deterministic content compiler/package
  -> canonical simulation model
       commands -> validated mutations -> ordered domain events
       queries  <- read models/snapshots
  -> runtime adapters
       rendering / animation / audio / input / physics adapter / platform services
  -> evidence adapters
       snapshots / hashes / traces / telemetry / scenario driver
```

Dependency direction should point inward toward stable domain contracts. Adapter-specific types must not leak into persisted canonical schemas without an explicit reviewed reason.

## 8. RDF-D1 — Canonical simulation boundary

### 8.1 Canonical state

Canonical gameplay state means the minimum state required to determine future gameplay outcomes under declared inputs.

Candidate categories:

- world/calendar/progression state;
- player/NPC logical state;
- inventories/resources/economy state;
- persistent entity/component facts;
- quest/story/world-state facts;
- production/automation state;
- canonical spatial/logical positions where gameplay depends on them;
- RNG stream state or derivable seed/counters;
- schema/content package versions needed to interpret the state.

Presentation-only state should normally be excluded:

- animation frame/interpolation;
- transient particles;
- camera smoothing;
- render caches;
- audio playback cursor unless gameplay-relevant;
- editor selection/import metadata;
- runtime object addresses/instance IDs.

### 8.2 Simulation kernel

The simulation kernel should support at least these conceptual operations:

```text
initialize(content_package, initial_state, seed_manifest)
submit(command)
advance(simulation_time_or_ticks)
query(read_query)
snapshot()
hash(canonical_scope)
collect_events(range)
```

This is an interface requirement, not an API syntax decision.

### 8.3 Adapter rule

A presentation/platform adapter may request commands and render/query state. It must not silently mutate canonical state behind the command/effect boundary.

An exception must be explicit, deterministic/evidence-aware, and reviewed as a domain interface.

## 9. RDF-D2 — Stable IDs and schema model

### 9.1 Identity classes

Keep identity classes distinct:

- **content IDs** — stable identifiers for definitions such as item/crop/recipe/quest types;
- **runtime entity IDs** — stable logical identity for persistent world instances;
- **event IDs** — unique/orderable evidence identity, not object identity;
- **save/snapshot IDs** — persistence artifact identity;
- **schema IDs/versions** — interpretation identity;
- **display/localization keys** — presentation identifiers, not canonical domain identity.

### 9.2 ID requirements

Canonical IDs should be:

- stable across file moves/renames where semantic identity remains;
- independent of localized/display names;
- validated for uniqueness;
- namespaced/domain-owned to reduce collision and merge contention;
- never silently reused for a semantically incompatible replacement;
- serializable in deterministic canonical form.

Human-readable IDs are acceptable when their rename semantics are explicit. Random/opaque IDs are acceptable where generation is deterministic/conflict-safe and tooling provides discoverability. The exact format remains a later decision.

### 9.3 Schema requirements

Every durable/configurable domain schema should declare:

```yaml
schema_id: <stable domain/schema identity>
schema_version: <monotonic or explicitly ordered version>
record_kind: <type>
identity_field: <where applicable>
required_fields: []
optional_fields: []
reference_fields: []
invariants: []
extension_policy: <closed/open/registered>
migration_from: []
```

Unknown-field handling must be explicit per schema; silently accepting unknown canonical fields is unsafe for validation and migrations.

### 9.4 Reference rules

References are resolved during content compile/load validation where possible. Required unresolved references fail the package; optional/conditional references declare fallback semantics.

Cross-domain references should use stable IDs/contracts rather than source-file paths or engine object pointers.

## 10. RDF-D3 — Command, event, and query contracts

### 10.1 Commands

A command expresses an attempted authoritative change:

```yaml
command_type: <stable type>
actor: <logical source>
parameters: {}
causal_context: <scenario/input/AI/player/system reference>
```

Command handling must:

1. validate shape and referenced IDs;
2. validate domain preconditions/authority;
3. apply canonical changes in deterministic order;
4. emit domain events/evidence;
5. return structured success/failure.

### 10.2 Events

Events describe accepted canonical changes or significant observations. Each event type has a versioned schema.

Ordering semantics must be explicit: total order within one simulation timeline is the safe initial default; domains may later prove weaker ordering sufficient.

Events used as evidence must bind the candidate/build/content/simulation identity needed for reproduction.

### 10.3 Queries

Queries expose read-only state/read models. Query APIs must not become hidden mutation channels.

Expensive aggregate queries should be instrumented and may use derived caches whose invalidation/rebuild semantics are explicit.

### 10.4 Cross-module rule

Default communication between independently owned systems should use declared commands/events/queries or narrow typed service interfaces. Direct mutation of another module's internal collections/state is a conflict and verification hazard.

## 11. RDF-D4 — Determinism contract

### 11.1 Determinism manifest

Every replayable scenario/build should be able to emit:

```yaml
determinism_manifest_version: 1
build_or_work_sha: <sha>
content_package_hash: <hash>
initial_snapshot_hash: <hash>
simulation_rules_version: <ref>
time_model: <version>
rng_stream_manifest: <ref/hash>
external_inputs: []
action_sequence_ref: <artifact>
expected_final_hash_scope: <versioned scope>
known_nondeterministic_surfaces: []
```

### 11.2 RNG discipline

Do not use one opaque global random stream for the whole game.

Candidate rule:

- named/versioned RNG stream domains;
- deterministic seed derivation from a root seed + stable stream identity where appropriate;
- stream consumption isolated so unrelated new visual/content behavior does not automatically perturb every gameplay outcome;
- random decisions that affect canonical gameplay become reproducible evidence.

Exact generator algorithm remains an implementation decision and must be versioned if replay/save compatibility depends on it.

### 11.3 Time discipline

Separate:

- simulation/game time;
- real/wall time;
- presentation delta/interpolation time;
- service timestamps.

Gameplay rules should consume simulation time, not ambient wall clock, unless an explicit feature intentionally depends on real time.

### 11.4 Ordering discipline

Nondeterministic iteration over maps/sets/tasks must not alter authoritative outcomes. Systems either use deterministic iteration/order keys or prove order-independence through commutative semantics/tests.

### 11.5 Numeric/physics boundary

Numeric and physics behavior that affects canonical gameplay needs a declared reproducibility envelope. If engine physics cannot provide required reproducibility across target environments, gameplay-critical decisions may need a narrower deterministic logical model with physics as presentation/approximation.

This is a risk to test, not a settled external claim.

### 11.6 Hash scope

Canonical hashes should exclude known presentation/transient noise and include every state element that can change future gameplay. Hash schema/version is itself versioned.

A stable final hash is useful evidence, not sufficient proof of user-facing correctness.

## 12. RDF-D5 — Persistence and migration

### 12.1 Save envelope

Candidate save envelope:

```yaml
save_format_version: 1
game_build_or_compatibility_version: <ref>
content_package_identity: <hash/version set>
canonical_schema_set: <manifest>
world_id: <stable>
snapshot_id: <stable>
simulation_time: <canonical>
rng_state_or_derivation_manifest: <ref>
canonical_payload: <structured/binary content>
checksum_or_integrity: <value>
optional_provenance: <migration/source refs>
```

Physical encoding remains undecided.

### 12.2 Snapshot policy

Persist logical canonical state, not raw engine/runtime object graphs. Derived caches should usually rebuild after load unless evidence proves persistence is required for correctness/performance.

### 12.3 Migration policy

Recommended migration model:

```text
read historical envelope
 -> validate integrity/version
 -> apply explicit ordered migration steps
 -> validate target schema/invariants
 -> emit migration report + before/after hashes where meaningful
 -> load current canonical model
```

Rules:

- migrations are versioned code/data with tests;
- historical fixtures are retained for representative versions;
- migration is deterministic for the same input/tool version;
- destructive/ambiguous migration fails with a structured error rather than silently dropping unknown required state;
- migration steps never rewrite source fixtures in place during tests;
- old save compatibility policy is separate from old replay compatibility policy.

### 12.4 Forward-only baseline

Prefer forward migration into the current canonical schema. Runtime systems should not accumulate branches for every old schema unless a compatibility requirement proves necessary.

### 12.5 Corruption/recovery

Save loading should distinguish:

- envelope/integrity failure;
- unsupported schema/version;
- content package mismatch;
- invalid reference/invariant;
- migration failure;
- runtime adapter failure after canonical state loaded.

Diagnostics need enough stable identifiers to reproduce the failing object/field without exposing giant dumps by default.

## 13. RDF-D6 — Content source, validation, and compilation

### 13.1 Pipeline

```text
source files / generated content
 -> syntax/schema validation
 -> ID uniqueness + namespace checks
 -> reference resolution
 -> domain invariant validators
 -> cross-domain validators
 -> deterministic normalization/compile
 -> content package manifest/hash
 -> runtime load validation
```

### 13.2 Source organization

High-volume content should favor many narrowly owned files/packages over one monolithic registry when semantics allow it. The compiler builds deterministic indexes/registries from those sources.

The canonical repository should make ownership boundaries visible from paths/package manifests where practical.

### 13.3 Generated content

AI-generated content is not trusted merely because it was generated by the project. It passes the same schema/reference/domain validation and provenance rules as authored content.

### 13.4 Behavior-bearing content

Data-driven does not mean "no code." A content type may reference a registered behavior/condition/action implementation through stable typed identifiers. Arbitrary embedded scripts require stronger sandboxing/versioning/review because they enlarge the executable surface.

### 13.5 Compiler properties

The content compiler should target:

- deterministic output for identical normalized inputs/tool version;
- stable diagnostics with source path + ID + field;
- incremental/domain validation where safe;
- full-graph validation at stronger gates;
- machine-readable result reports;
- duplicate/conflict detection;
- content package identity suitable for saves/replays/evidence.

## 14. RDF-D7 — Performance and observability

### 14.1 No premature magic numbers

Numeric budgets are deferred until representative workloads exist. The architecture must, however, make measurement possible from the beginning.

### 14.2 Required metric families

At minimum instrument:

- simulation advance/tick time by system;
- entity/content counts by domain;
- command handling counts/latency;
- event volume and expensive subscribers;
- query/cache cost;
- save/load/migration latency and allocation;
- snapshot size and canonical hash cost;
- content compile/load/validation time;
- long-simulation throughput;
- memory by major subsystem/category where tooling permits;
- adapter/render/update cost separately from simulation where practical.

### 14.3 Workload identity

Every performance result used for decisions binds:

```text
build SHA
content package
scenario/workload ID + version
initial state/seed
simulation duration/actions
platform/environment/toolchain
metric definition/version
```

Do not compare unlabeled "FPS" or "tick time" numbers across different workloads as if they are equivalent evidence.

### 14.4 Scale envelopes

Later budgets should cover representative scale classes, for example:

- early/new world;
- mature dense property;
- multi-region/high-automation world;
- large content catalog startup/compile;
- long accelerated simulation;
- pathological but supported save/content states.

Exact counts belong to later game/technical synthesis and experiments.

## 15. RDF-D8 — Extension and conflict constraints

### 15.1 Namespace ownership

Each domain/module owns:

- its internal state schema;
- its command/event/query type namespaces;
- its content type/schema namespaces;
- its migrations;
- its invariant validators.

Cross-domain contracts are explicit shared surfaces with narrow ownership/review.

### 15.2 Append/registration preference

New content/system additions should usually add files/records/registered handlers instead of editing central switch statements or giant registries. Generated indexes are compiler output, not hand-maintained conflict surfaces.

### 15.3 Schema evolution

Adding an optional field is not automatically safe: default semantics, old-save migration, determinism/hash effect, validator behavior, and evidence coverage must be explicit.

Removing/renaming/reinterpreting fields or IDs requires migration and downstream impact analysis.

### 15.4 Conflict-sensitive surfaces

Treat these as likely coordination/lock surfaces:

- canonical schema definitions;
- shared command/event/query contracts;
- global time/RNG rules;
- save envelope/migration registry;
- compiler core/reference resolver;
- canonical hash scope;
- cross-domain integration indexes;
- performance/evidence schema used as acceptance authority.

High-volume content instances should not require ownership of these central surfaces.

## 16. Error model and recoverability

Runtime/content/persistence failures should be structured rather than string-only where practical:

```yaml
error_code: <stable>
domain: <module>
subject_id: <optional stable ID>
schema_or_command_version: <optional>
source_ref: <optional>
causal_refs: []
diagnostic_fields: {}
```

Principles:

- fail early on invalid canonical content/state;
- avoid partial authoritative mutation when a command fails validation;
- distinguish user/content/save error from infrastructure/adapter failure;
- preserve enough context for an agent to reproduce the failure;
- provide validators/repair tooling rather than requiring manual editor surgery for common structural defects.

## 17. Interface obligations

### To W1-TEC-01 / engine evaluation

Engine candidates/spikes should prove they can host this separation:

- simulation kernel callable without editor-only interaction;
- stable content files/packages manageable by agents;
- headless or automation-compatible scenario execution where required;
- controlled screenshot/runtime adapter integration;
- no unavoidable dependence on opaque engine instance IDs for canonical persistent identity.

This proposal does not select the engine.

### To W1-EVAL-01 / CI evidence

Supply:

- deterministic manifest;
- canonical snapshot/hash;
- command/action trace;
- domain event trace;
- save/load/migration report;
- content package identity;
- performance workload identity.

### To game/system planning

System specs should declare:

- canonical state owned;
- command/event/query interfaces;
- content schemas/IDs/references;
- determinism/RNG/time assumptions;
- persistence/migration effect;
- semantic coverage and observability needs;
- shared conflict surfaces.

### To content/narrative architecture

Provide stable IDs, schema composition, validation/compile interfaces, cross-reference rules, migrations, and package identity. Narrative facts/quests/dialogue may specialize these rather than invent parallel identity/version systems.

### To factory/control plane

Future implementation issues should declare owned runtime/schema/content surfaces and evidence requirements; shared schema/migration/core compiler changes are conflict-sensitive and require stronger review routing.

## 18. Bounded experiments

### RDF-E1 — Deterministic kernel replay

Implement the smallest engine-independent simulation spike after implementation readiness: fixed content package + initial snapshot + seed + command sequence; execute repeatedly and compare ordered events/final canonical hash.

**Pass:** identical declared inputs produce identical canonical evidence within the declared boundary.  
**Failure:** identify nondeterministic source and revise clock/RNG/order/state boundary.

### RDF-E2 — Presentation-adapter separation

Drive one deterministic simulation scenario through a headless path and through the selected-engine adapter once an engine candidate exists.

**Pass:** canonical outcomes match while presentation evidence can differ only in declared noncanonical surfaces.  
**Failure:** adapter leaks authoritative mutation or engine state is required for canonical execution.

### RDF-E3 — RNG isolation

Add an unrelated random consumer in a different stream/domain to a frozen scenario.

**Pass:** unaffected domain canonical outcomes remain stable where the stream contract promises isolation.  
**Failure:** random-consumption coupling is too broad; revise stream derivation/ownership.

### RDF-E4 — Save migration matrix

Create representative historical fixtures across at least several schema transitions including add/rename/split/reference change and one intentionally invalid fixture.

**Pass:** valid fixtures migrate deterministically with invariant validation; invalid fixture fails structurally without silent data loss.  
**Failure:** migration/schema identity is insufficient.

### RDF-E5 — Content conflict/compile spike

Have multiple isolated tasks add content in distinct owned source files plus deliberate duplicate-ID/broken-reference cases.

**Pass:** clean additions merge with low central contention; compiler output is deterministic; duplicates/broken refs fail with stable diagnostics.  
**Failure:** source/registry organization or ID namespace creates bottlenecks.

### RDF-E6 — Corruption recovery drill

Inject checksum failure, unknown schema, missing content reference, invalid domain invariant, and adapter-load failure.

**Pass:** each class is distinguished and produces a bounded reproducible diagnostic; canonical source is not silently mutated.  
**Failure:** recovery/error model is too opaque.

### RDF-E7 — Long accelerated simulation

Run a representative canonical simulation much faster than real time while presentation adapters are disabled.

**Pass:** simulation remains semantically equivalent to normal advancement and exposes stable timing/resource evidence.  
**Failure:** gameplay semantics are entangled with frame/render/wall-clock behavior.

### RDF-E8 — Performance workload reproducibility

Repeat a versioned workload on the same environment/build and compare distributions; then change content scale deliberately.

**Pass:** metrics identify workload/build/environment and respond explainably to scale changes.  
**Failure:** performance telemetry is too noisy/underspecified to gate architecture.

## 19. Observability and acceptance evidence

A future implementation of this foundation should expose a compact evidence index with:

- canonical snapshot/hash schema version;
- deterministic scenario results;
- RNG/time manifest;
- save/migration matrix results;
- content compiler validation report;
- unresolved reference/duplicate counts;
- long-simulation throughput;
- performance workload results;
- known nondeterministic surfaces;
- adapter parity results;
- schema/migration coverage gaps.

No single hash, benchmark, or green CI result proves the foundation correct.

## 20. Failure modes and defenses

### Engine identity leak
**Failure:** saves/content depend on engine instance IDs/resource locations.  
**Defense:** stable logical IDs + adapter mapping + migration tests.

### Hidden nondeterministic ordering
**Failure:** map/set/task iteration changes canonical outcomes.  
**Defense:** deterministic ordering or tested commutative semantics; replay/hash evidence.

### RNG butterfly effect
**Failure:** cosmetic/new content random call changes unrelated gameplay.  
**Defense:** named streams and isolation experiment.

### Wall-clock gameplay
**Failure:** headless/accelerated simulation diverges because rules read ambient real time.  
**Defense:** explicit simulation clock; external real-time inputs are declared commands/events.

### Save equals memory dump
**Failure:** runtime refactor breaks every save.  
**Defense:** logical canonical persistence schema and explicit adapters/migrations.

### Migration laundering
**Failure:** incompatible data silently defaults/drops.  
**Defense:** versioned deterministic migrations + invariant validation + reports/fixtures.

### Global registry bottleneck
**Failure:** every content task edits one file.  
**Defense:** domain-owned source files/packages; deterministic generated indexes.

### Schema-free content
**Failure:** runtime accepts malformed/generated data until deep execution.  
**Defense:** compile-time schema/reference/domain validation.

### Data-driven overreach
**Failure:** generic DSL becomes an untestable programming language.  
**Defense:** typed registered behavior interfaces; stronger review for executable scripting.

### Event ambiguity
**Failure:** replay/debugging differs because event order/versions are implicit.  
**Defense:** explicit event schemas/order and evidence binding.

### Performance-by-FPS
**Failure:** one visible number hides simulation/load/save bottlenecks.  
**Defense:** workload-bound metric vector split by subsystem.

### False determinism
**Failure:** final hash stable while player-visible behavior broken.  
**Defense:** combine canonical evidence with real executable/player-surface scenarios.

## 21. Risks and deferrals

- Exact deterministic numeric/physics strategy depends on selected engine/runtime and target platforms; it remains a spike requirement.
- Exact serialization encoding is deferred; schema/migration semantics are more important than file format at this stage.
- Public mod support could require stronger compatibility/security contracts than internal extensibility; not promised here.
- Event volume and content compiler cost may become substantial at scale; benchmark before adopting universal event retention or full recompilation.
- Save compatibility window and replay compatibility window need product/release decisions later.
- Some content types will require authored executable logic; the boundary should be explicit rather than forcing all behavior into data.

## 22. Open questions

1. What canonical numeric representation/reproducibility envelope is required for gameplay-critical movement/physics/economy across supported platforms?
2. Which domains require persistent entity identity versus replaceable/ephemeral instances?
3. Which domain events should be durable history versus transient evidence?
4. What save compatibility horizon is required after release?
5. What replay compatibility horizon is required, and should old replays execute under archived rulesets rather than current rules?
6. Which content behavior needs a safe DSL versus registered code implementations?
7. What content package granularity best balances load time, validation, agent ownership, localization, and patching?
8. Which canonical-state subsets should have separate hashes for localized diagnosis?
9. What representative scale envelopes define initial performance budgets?
10. Which engine/runtime facilities can be trusted inside the deterministic boundary after W1-TEC-01 experiments?

## 23. Reopen conditions

Reopen this proposal if evidence shows:

- selected engine/runtime cannot host a separately testable canonical simulation without prohibitive duplication;
- deterministic replay cost/constraints materially damage required game behavior;
- logical IDs/schema compilation create worse concurrency or authoring cost than alternatives;
- representative save migrations require semantic history not captured by the proposed envelope;
- content compilation becomes an unacceptable startup/build bottleneck and incremental/package strategy is insufficient;
- performance evidence cannot separate simulation from adapter cost;
- high-volume system/content work repeatedly needs central schema/registry edits;
- cross-domain review finds command/event/query semantics too rigid or too weak for game design;
- target platform behavior forces a different determinism/persistence boundary.

## 24. Required critique and downstream work

Required independent critiques:

- `W1-REV-TECH` — attack determinism, migration, evidence validity, engine coupling, performance observability, and merge-hostile architecture.
- `W1-REV-GAME` — attack whether the technical boundaries can actually express the breadth, progression, quests, NPC/world state, automation, and player-surface requirements without architectural distortion.

Downstream synthesis should reconcile this proposal with W1-TEC-01 and W1-EVAL-01, then with game-domain synthesis before any implementation-readiness decision.

This artifact is non-canonical and does not authorize an engine choice or gameplay implementation.
