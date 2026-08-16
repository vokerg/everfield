# W2 Content Frontier Contract v1

**Mission:** `W2-CONTENT-GATE-01`  
**Issue:** #365  
**State:** PRODUCER CANDIDATE / NONCANONICAL  
**Authority:** bounded planning-frontier construction only  
**Owner parallel-frontier directive:** Issue #84 comment `5305563203`

## 1. Purpose

The current Planning v1 graph contains reviewed world/social/narrative/content architecture and a canonical Wave-1 game foundation, but it no longer exposes a runnable continuation lane for concrete engine-neutral narrative/content planning. This contract repairs that DAG liveness/coverage gap without weakening the active engine remediation chain or implementation-readiness barriers.

The operative scheduling rule is domain-scoped convergence: an owned blocking task in one conflict domain does not globally suppress independent eligible work in a non-overlapping domain. Issue #364 remains the correct engine-lane blocking remediation. This packet only constructs a content-planning frontier.

## 2. Exact authority and immutable inputs

- current main at claim: `c043c47acfa3212ca08e87725b25e47a20e8e5e6`;
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- canonical binding: Bootstrap Issue #6 comment `5245368879`;
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- owner convergence directive: Issue #84 comment `5277825639`;
- owner parallel-frontier directive: Issue #84 comment `5305563203`;
- W1-DES-03 exact work: `d19ddc43c9e5f22c6f14e5c978c30a4e6a2f0d8b`;
- W1-REV-GAME exact work: `29b97b5bedee5a9f5317308a74caf38538bfbd70`;
- W1-SYN-GAME exact work: `e74e0b0c95e85f69718868eedae324a298f02f3e`;
- current canonical Wave-1 foundation: `docs/planning/WAVE-1-FOUNDATIONS-v1.md` on claim main;
- W2-GAME-GATE-01 exact compiler work: `d32aa80fd77c7caf6995ecb71b311da5a457c3b6`, terminal comment `5281402332`.

Historical producer/reviewer branches remain immutable. This compiler may consume exact artifacts but does not rewrite them.

## 3. Reconstructed product-design gap

W1-DES-03 intentionally defined information architecture rather than the final world. Its non-goals explicitly excluded the final world, history, lore, NPC cast, factions, relationships, dialogue corpus, quest catalog, regions, festivals, and story arcs. The proposal nevertheless established load-bearing contracts for typed facts, NPC state, social state, knowledge/beliefs/secrets, quest structure, consequences, grounded content, consistency checks, and bounded experiments.

W1-REV-GAME found no blocker requiring engine selection before narrative design. Its relevant corrections were cross-game contracts: narrative/social gates must not silently become universal progression prerequisites; time semantics must be shared; runtime generation needs an authority boundary; originality needs evidence beyond provenance; high-impact branches need content/trajectory sufficiency; and evaluator independence must not be faked.

W1-SYN-GAME accepted those corrections and explicitly states that it does not choose an engine or freeze the final world, lore, NPC cast, quests, or content corpus. It also states that canonical gameplay meaning is engine-independent logical state and that presentation/editor types are adapters rather than sole authority.

The current Wave-1 foundation further states that scheduler readiness applies only dependency edges relevant to the target task/scope and that independent evidence missions are parallelizable when outputs/conflict keys do not collide. Therefore engine selection is not a lawful default prerequisite for the content-planning work below.

## 4. Existing evidence routes that must not be duplicated

W2-GAME-GATE-01 already accounts for the nine `WSN-E*` evidence questions and groups them into later evidence tranches such as world-structure, world-content, content, and evaluator work. This frontier does **not** create duplicate empirical tasks for those IDs.

The initial roots below create bounded candidate product/content definitions that later WSN evidence can test. Existing WSN experiment identities remain `UNRUN_REQUIRED_EVIDENCE` unless exact already-existing evidence says otherwise. No producer root may claim that authored prose or self-review satisfies those experiments.

## 5. Independence test

A first-tranche root is parallelizable only if all are true:

1. its mutable repository paths are unique;
2. it consumes only immutable common inputs from this compiler/predecessors;
3. it does not require another first-tranche root's produced artifact to begin or complete its bounded proposal;
4. cross-root references are represented as provisional stable role/interface IDs rather than hidden reads of mutable sibling work;
5. contradictions are expected to be resolved at downstream fan-in rather than by producers editing one another;
6. it does not claim final canon, implementation readiness, or empirical PASS;
7. engine choice is unnecessary for the bounded planning output.

If a producer discovers a real dependency on another root, it must record that as a finding/reopen condition and stop short of inventing the missing sibling result.

## 6. First bounded parallel frontier

The reviewed first tranche targets four roots. Four is chosen instead of mechanically filling the 4–6 target because a fifth initial authored vertical slice would genuinely consume multiple root outputs and would therefore be false parallelism.

### 6.1 `W2-CONTENT-WORLD-01` — world/setting foundation candidate

**Conflict domain:** `CONTENT_WORLD`  
**Owned surfaces:**
- `docs/planning/wave-2/content/world-setting-foundation.md`
- `docs/planning/wave-2/content/world-setting-facts.yaml`
- task handoff

**Objective:** propose a coherent bounded setting/world candidate: thematic promise, physical/social setting constraints, region/world topology at the level needed to support gameplay, chronology/history anchors, world rules, major unresolved mysteries, and stable world-fact identities. It may author candidate facts, but every fact remains noncanonical until later reviewed fan-in/canonicalization.

**Must preserve:** objective fact vs belief/secret/branch distinction; chronology; originality/reference boundary; explicit reopen conditions; no engine-specific representation.

**Must not own:** final factions, final named principal cast, final main plot/quest catalog, dialogue corpus, production implementation.

### 6.2 `W2-CONTENT-SOCIAL-01` — factions/institutions/social-conflict topology candidate

**Conflict domain:** `CONTENT_SOCIAL`  
**Owned surfaces:**
- `docs/planning/wave-2/content/factions-social-topology.md`
- `docs/planning/wave-2/content/factions-social-topology.yaml`
- task handoff

**Objective:** propose a bounded faction/institution/community topology with motivations, resources, tensions, cooperation/conflict edges, player-facing relationships, social consequences, and candidate stable IDs. Use abstract location/world-role references where detailed world outputs are not yet reviewed.

**Must preserve:** `ProgressionGateContract` classifications; no faction/social gate silently becomes foundational; multi-dimensional relationship semantics; explicit branch consequences; originality boundary.

**Must not own:** final world geography/history, final named principal character arcs, final main plot, final quest/dialogue corpus.

### 6.3 `W2-CONTENT-CHAR-01` — principal character/relationship candidate

**Conflict domain:** `CONTENT_CHARACTER`  
**Owned surfaces:**
- `docs/planning/wave-2/content/principal-characters-relationships.md`
- `docs/planning/wave-2/content/principal-characters-relationships.yaml`
- task handoff

**Objective:** propose a bounded principal-cast candidate and relationship architecture sufficient to test character identity, motivation, knowledge/belief/secret boundaries, relationship dimensions, goals/obligations, change arcs, and interfaces to world/faction/narrative roles. Where sibling details are unknown, use typed role/faction/world references rather than silently freezing sibling content.

**Must preserve:** knowledge leakage controls; history versus current relationship score; explicit causes/effects; no universal affection scalar; generated prose cannot create canonical facts.

**Must not own:** final faction definitions, final world history/geography, full dialogue corpus, final main plot/quest catalog.

### 6.4 `W2-CONTENT-NARR-01` — narrative/quest/consequence architecture candidate

**Conflict domain:** `CONTENT_NARRATIVE`  
**Owned surfaces:**
- `docs/planning/wave-2/content/narrative-quest-architecture.md`
- `docs/planning/wave-2/content/narrative-quest-architecture.yaml`
- task handoff

**Objective:** propose a bounded main-narrative/quest candidate at structural level: themes/conflict trajectory, arc and beat roles, quest grammar, discovery/reveal structure, typed preconditions/objectives/effects/branches/failure/recovery, world-state consequence model, and branch-impact obligations. It may define provisional role IDs and story-state IDs but must not pretend sibling world/faction/character details are settled.

**Must preserve:** `ProgressionGateContract`, `GameTimePolicy`, `GameSemanticGraph`, branch-impact sufficiency, quest solvability, explicit consequence state, no hidden universal narrative gate, no engine-specific scripting syntax.

**Must not own:** final setting bible, final faction details, final character bios, full authored quest/dialogue catalog.

## 7. Why these roots are independent enough

The four roots share immutable contracts and use provisional interface IDs for cross-domain references. None needs another root's prose or YAML to satisfy its own bounded proposal acceptance. Their semantic conflicts are expected and desirable review inputs for fan-in synthesis.

The mutable paths are disjoint. Producers are forbidden from editing sibling paths or a shared aggregate file. The first point at which concrete names/facts/relationships/story beats must become mutually consistent is downstream fan-in, not initial production.

This is analogous to Wave 1's original broad proposal frontier: parallel candidate work first, adversarial reconciliation later.

## 8. Work deliberately deferred from the initial roots

### 8.1 Authored vertical slice

A concrete authored questline with final characters, factions, world locations, dialogue and consequences would consume at least world + social + character + narrative outputs. Creating it as a sibling root would encode a hidden dependency. Route it only after reviewed fan-in freezes the minimum compatible candidate packet.

Suggested later mission: `W2-CONTENT-VS-01`.

### 8.2 Cross-content evidence execution

Existing WSN evidence debt should consume the reviewed/fan-in content packet rather than be duplicated here. Candidate later routes include the already-accounted world-structure/world-content/content/evaluator tranches from W2-GAME-GATE-01.

### 8.3 Content synthesis/fan-in

Suggested later mission: `W2-CONTENT-SYN-01`, after all four roots have the required producer review state. It should reconcile concrete identifiers, world/faction/character/narrative contradictions, progression gates, chronology, secrets, branch impacts, originality risks, and unresolved evidence obligations.

## 9. Required review and activation rule

The compiler may instantiate the four root issues before its own terminal status only as `BLOCKED_PENDING_CONTENT_FRONTIER_REVIEW`.

A fresh independent/degraded-independent review must bind the exact compiler work and root issue contracts. Only disposition `CLEAN_FOR_BOUNDED_CONTENT_FRONTIER_ACTIVATION` makes those exact roots derive READY.

The compiler review must attack:

- hidden producer dependencies;
- shared mutable surfaces;
- accidental engine coupling;
- artificial serialization;
- premature story canon;
- duplicate work versus existing WSN evidence routes;
- fan-in sufficiency;
- whether four roots are genuinely useful and bounded.

`CHANGES_NEEDED` routes one bounded compiler remediation. `INVALIDATED` routes recovery only.

## 10. Root producer lifecycle

After activation, each root independently:

1. re-derives current main/canonical binding and exact clean compiler review;
2. claims exactly once and checks contention;
3. creates its own `planning/issue-N` branch from exact current main;
4. treats common compiler/predecessor inputs as immutable;
5. writes only its owned paths;
6. separates candidate facts/assumptions/evidence/inference/decisions/open questions;
7. opens an exact-head draft PR before terminal `REVIEW_READY`;
8. requires fresh independent/degraded-independent review before any fan-in authority.

## 11. Authority boundary

This contract creates planning concurrency only. It does not:

- choose an engine;
- authorize gameplay/high-throughput implementation;
- make any candidate world fact, faction, character, plot, quest, or dialogue canonical;
- satisfy WSN empirical experiments by prose;
- establish implementation readiness or release approval;
- grant verification-PASS, integration, decision, or canonical authority.

All main integration remains separately authorized and squash-only.
