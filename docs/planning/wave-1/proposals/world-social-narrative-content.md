# World, NPC, Social, Narrative, Quest, and Content Architecture — Wave 1 Proposal

**Mission:** `W1-DES-03`  
**State:** PROPOSAL / NON-CANONICAL  
**Required review:** `W1-REV-GAME`

## Review Index

- **WSN-D1 — Canonical fact/state graph (§8):** world, NPC, relationship, faction, chronology, knowledge, quest, and narrative consequences use stable typed facts/state; dialogue/prose is not the only source of truth.
- **WSN-D2 — NPC model (§9):** separate durable identity/facts/relationships/goals/schedule state from presentation; NPC behavior consumes world state and emits observable actions/events under explicit constraints.
- **WSN-D3 — Social model (§10):** relationships are multi-dimensional state/consequences rather than one affection scalar; thresholds may unlock content but important state changes remain explainable and testable.
- **WSN-D4 — Narrative knowledge/consistency (§11):** distinguish objective world facts, character beliefs/knowledge, secrets, chronology, and disputed/branch facts; dialogue/quests validate claims against the appropriate knowledge scope.
- **WSN-D5 — Quest architecture (§12):** quests use versioned goals/preconditions/objectives/effects/failure/branch records and structural solvability checks; custom prose/content can vary without hiding progression logic.
- **WSN-D6 — World-state consequence model (§13):** important actions can change canonical world/social/narrative state through explicit effects/events; consequences are scoped, observable, reversible/irreversible by design, and migration-safe.
- **WSN-D7 — Content production (§14):** AI-generated/authored narrative/content uses typed briefs, provenance, validation, semantic-role/duplication checks, and bounded generation/review; generated text cannot invent new canonical facts silently.
- **WSN-D8 — Consistency/evaluation (§15):** use graph/reference validation, chronology/knowledge contradiction checks, quest reachability, schedule/world-state simulation, repetition metrics, and structured narrative critics; no single “story quality” score.
- **Evidence (§5):** mandates require narrative/questing as first-class, canonical fact/chronology consistency, stable IDs/schemas, quest solvability, generated-content scale, NPC/social/world consequences, and original—not cloned—content.
- **Experiments (§18):** contradictory-fact injection, knowledge leakage, quest state search, schedule conflict, branching world-state, content semantic-sameness, long-horizon NPC/social simulation, and generated-dialogue grounding tests are required.
- **Reviewer attack points:** prose as hidden authority; NPC schedules impossible under world changes; relationship scalar flattening; secret/knowledge leaks; quest soft-locks; mutually inconsistent branches; generated lore drift; narrative state bypassing persistence/migration; content volume overwhelming consistency and review.

## 1. Objective

Define interfaces that let Everfield scale authored and generated world/social/narrative content while keeping gameplay-relevant facts, quests, relationships, NPC behavior, chronology, knowledge, and consequences explicit enough to validate, simulate, persist, review, and extend autonomously.

The proposal does not author the world. It defines the candidate information architecture and evidence requirements future content must obey.

## 2. Scope

In scope:

- world/narrative canonical fact representation;
- NPC durable identity/state, goals, schedules, and observable behavior boundaries;
- relationship/social/faction state;
- character knowledge, beliefs, secrets, chronology, and branch facts;
- quest structure, branches, objectives, preconditions, effects, failure, and solvability;
- world-state/narrative consequence records;
- dialogue/content grounding against canonical state;
- authored/generated content production constraints;
- contradiction/repetition/semantic-sameness detection;
- persistence/versioning/interface obligations;
- narrative/quest/social observability and evidence;
- bounded experiments and reopen conditions.

## 3. Non-goals

This proposal does **not**:

- define the final world, history, lore, NPC cast, factions, relationships, dialogue corpus, quest catalog, regions, festivals, or story arcs;
- choose a final quest/dialogue DSL syntax;
- require every NPC to run a complex autonomous AI model;
- require every relationship to use the same dimensions;
- promise fully procedural/generative narrative;
- decide whether all schedules use exact clock simulation;
- make an LLM-generated statement canonical because it sounds plausible;
- reduce narrative quality to contradiction-free text;
- authorize gameplay implementation.

## 4. Constraints and assumptions

### 4.1 Observed constraints

The authoritative packet requires or strongly suggests:

1. narrative and questing are first-class projects developed alongside mechanics/world content;
2. quest quality includes structural solvability, progression fit, clarity, agency, character consistency, rewards, and path diversity;
3. architecture should use stable IDs, schemas, registries, events, commands, queries, and validated references where appropriate;
4. large generated/authored corpora require canonical facts, chronology, character knowledge, relationships, secrets, and contradiction detection;
5. continuous expansion should make NPCs, dialogue, quests, events, regions, and content cheap to add without invasive unrelated edits;
6. evaluation should combine structural validation with player-facing/subjective evidence;
7. Everfield must remain original; Stardew Valley is a complexity reference, not a source of copied expression/content.

### 4.2 Assumptions to test

- Most gameplay-relevant narrative continuity can be represented as structured facts/relations/events even when prose remains rich and authored.
- Separating objective facts from character beliefs/knowledge can prevent common dialogue/secret leaks.
- Quest structural logic can be validated separately from quest prose/presentation.
- NPC schedule/goals can be represented with enough constraints to detect impossible conflicts without requiring a universal heavyweight planner.
- AI-generated content can scale safely only if briefs and outputs bind explicit canonical facts/allowed inventions/provenance and pass consistency/semantic-diversity review.
- Branching world state can remain tractable if effects are typed/scoped and branch conditions are explicit rather than encoded only in scripts/dialogue.

## 5. Evidence, inference, recommendation

### 5.1 Evidence

Project documents explicitly identify:

- NPC simulation, relationships, dialogue, quests, story/world-state progression, events, chronology, and narrative consistency as design/evaluation surfaces;
- canonical fact graph and contradiction search as candidate narrative oracles;
- quest graph validation/game execution for solvability;
- generated content provenance/consistency needs;
- long-term expansion and high-volume content generation as architectural requirements.

### 5.2 Inference

If prose/script bodies become the only place where facts, preconditions, and consequences exist, automated agents cannot reliably answer “what is true?”, “what does this NPC know?”, “can this quest complete?”, or “what changes after this event?” without interpreting arbitrary text/code.

Therefore gameplay-relevant semantics should be explicit structured state, while prose/presentation references that state.

### 5.3 Recommendation

Adopt the contracts below as a candidate foundation. Keep exact dimensions, DSL syntax, scheduling algorithm, and narrative content downstream and evidence-driven.

## 6. Alternatives considered

### A. Dialogue/scripts are the canonical narrative database — reject

Fast to author but hides facts/branches/knowledge inside arbitrary content and makes consistency, migration, search, and independent validation fragile.

### B. One giant world-state flag registry — reject

Simple initially but becomes a conflict/meaning bottleneck. Prefer typed domain/namespace facts and explicit relationship/reference schemas with generated indexes.

### C. One affection number per NPC — reject as universal model

Legible, but flattens trust, familiarity, rivalry, respect, obligation, faction alignment, secrets, and contextual consequences. Individual systems may use simple scalar dimensions when evidence supports them.

### D. Fully emergent NPC LLM agents with no authored state model — reject as foundation

Could create novelty but makes determinism, continuity, persistence, secret control, quest guarantees, and evidence difficult. Generative behavior can operate inside explicit state/knowledge/action boundaries later.

### E. Every quest as custom code — reject

Allows arbitrary behavior but impedes structural validation, content generation, ownership, and migration. Custom handlers remain escape hatches for exceptional behavior behind typed interfaces.

### F. Fully procedural infinite quest/story generation — reject as default

Scale without authored identity/semantic diversity/continuity can create repetition and incoherence. Use bounded generation where it can be grounded and evaluated.

## 7. Common identity and reference model

Every durable narrative/content object should use stable identity independent of display text/file location:

```text
world_fact_id
character_id
faction_id
relationship_edge_id or typed pair key
location_id
quest_id / quest_instance_id
objective_id
story_arc_id
world_event_id
conversation/dialogue_content_id
content_definition_id
knowledge_fact_id or fact reference
```

Exact formats belong to technical/content synthesis.

References should be schema-validated. Renaming display/localized text must not change logical identity.

## 8. WSN-D1 — Canonical fact/state graph

### 8.1 Fact categories

Candidate categories:

- objective world facts;
- world-state values/conditions;
- historical/chronology facts;
- character identity/background facts;
- relationship/social/faction facts;
- ownership/property/economy facts where narrative-relevant;
- quest/story progression facts;
- discovered/known information;
- secrets/reveal state;
- player choices/commitments;
- disputed/subjective claims with provenance.

### 8.2 Fact record

Conceptual shape:

```yaml
fact_id: <stable>
fact_type: <typed>
subject_refs: []
predicate: <typed relation/property>
object_or_value: <typed>
validity:
  from: <optional chronology/world-state ref>
  until: <optional>
branch_conditions: []
source_or_authority_ref: <definition/event/choice>
visibility: <PUBLIC | DISCOVERABLE | SECRET | SYSTEM_ONLY>
consistency_rules: []
```

Not every state variable needs this exact generic record; domain schemas may compile into a common query/consistency layer.

### 8.3 Canonicality rule

Generated dialogue, summaries, codex text, or NPC utterances do not create new objective facts unless an explicit validated world-state effect/authoring record does so.

## 9. WSN-D2 — NPC simulation model

### 9.1 Durable NPC state

Potential durable dimensions, system-specific:

- identity/traits/background references;
- home/role/faction/relationships;
- schedule/goals/obligations;
- knowledge/beliefs/secrets;
- current location/activity state where gameplay-relevant;
- relationship history/state;
- quest/story/world-state participation;
- inventory/economy/property hooks if relevant;
- temporary mood/status only where it has gameplay consequences.

### 9.2 Schedule/goal separation

A schedule is one execution plan for obligations/preferences, not the character identity. World events, weather, quests, relationship state, emergencies, closures, and player actions may alter it through explicit rules.

### 9.3 Action interface

NPC simulation should produce/consume typed operations such as:

```text
observe world/query state
select eligible activity/goal
request movement/action/service/social interaction
emit event/state effect
update knowledge/relationship where justified
```

Exact behavior algorithm can vary by NPC/system.

### 9.4 Schedule conflict evidence

Validators/simulations should detect:

- impossible travel/time overlaps;
- two exclusive obligations at once;
- inaccessible target locations;
- invalid referenced events/locations;
- permanent idle/dead schedule states;
- story/quest conditions that strand required NPC availability without alternative handling.

## 10. WSN-D3 — Social and relationship model

### 10.1 Multi-dimensional candidate state

Possible dimensions include familiarity, trust, affection, respect, rivalry, obligation, fear, faction standing, romance/partnership state, shared history, secrets known, promises/debts, or context-specific flags.

Do **not** require every NPC relationship to instantiate every dimension.

### 10.2 Relationship effects

Relationship/social state may affect:

- dialogue/content eligibility;
- services/trade/help;
- quests/events;
- gifts/rewards/access;
- schedules/visits;
- information/secrets;
- faction/community response;
- world/narrative branches.

Effects should reference explicit predicates rather than prose heuristics.

### 10.3 History versus current score

Some consequences need history (“player broke promise”) even if a current scalar later recovers. Preserve important events/facts rather than assuming current aggregate state captures all meaning.

### 10.4 Social progression caution

Grinding one repeated gift/action should not automatically satisfy every relationship dimension. Exact anti-grind design is downstream; simulations/repetition metrics should detect degenerate loops.

## 11. WSN-D4 — Knowledge, beliefs, secrets, chronology

### 11.1 Knowledge scopes

Distinguish:

- **objective canonical fact** — what project/world model says is true;
- **character knowledge** — facts a character has learned;
- **character belief** — claim held by a character, potentially false/disputed;
- **player discovered knowledge** — what the player-facing experience has revealed;
- **system-hidden state** — not yet player/character known;
- **branch-specific fact** — true only under a world-state branch.

### 11.2 Dialogue grounding

A dialogue/content candidate that asserts a fact should declare or be able to derive:

```yaml
speaker: <character>
asserted_fact_refs: []
required_knowledge_refs: []
required_world_state: []
forbidden_if: []
intent/tone/context: <presentation metadata>
```

Generated prose can add noncanonical stylistic detail only inside a brief’s allowed invention scope.

### 11.3 Leakage check

A character must not reveal a secret/future event/branch fact they cannot know unless the design intentionally marks supernatural/meta knowledge.

### 11.4 Chronology

Historical/world-event records should support ordering/interval constraints and branch applicability. Contradictions like “event B happened before character birth” or mutually exclusive events both asserted in one branch should be machine-detectable where represented.

## 12. WSN-D5 — Quest architecture

### 12.1 Quest definition

Conceptual shape:

```yaml
quest_id: <stable>
version: <schema/content version>
category/tags: []
availability:
  prerequisites: []
  forbidden_conditions: []
  discovery_sources: []
objectives:
  - objective_id: <stable>
    type: <registered>
    parameters: {}
    completion_predicate: <typed>
    optional: false
branches: []
completion_effects: []
failure_expiry_rules: []
rewards: []
world/narrative_effects: []
required_character/location/content_refs: []
```

Exact schema is downstream.

### 12.2 Objective grammar

Favor registered objective/predicate/effect types for structural validation. Custom scripted logic is allowed behind typed contracts but must expose validation/evidence hooks.

### 12.3 Structural solvability

Validators/search should test:

- all referenced entities/content exist;
- prerequisite graph does not accidentally cycle;
- required objective predicates can become true under supported branch/world states;
- required NPC/location remains reachable or alternatives exist;
- mutually exclusive branches are not simultaneously required;
- expiration/time conditions leave a legal completion window when intended;
- rewards/effects do not reference invalid/removed content;
- failure/abandon/retry semantics are explicit.

### 12.4 Quest quality beyond solvability

Solvable is necessary, not sufficient. Later evaluators should inspect clarity, grind, agency, thematic/character fit, pacing, reward, novelty, route diversity, and player-surface comprehension.

## 13. WSN-D6 — World-state consequence model

### 13.1 Effect categories

Explicit effects may include:

- fact/state mutation;
- unlock/lock/availability;
- relationship/faction change;
- NPC knowledge/belief update;
- schedule/role change;
- location/property/world change;
- quest/story branch activation;
- economy/service/content changes;
- discovery/reveal state.

### 13.2 Effect requirements

A material consequence should declare:

- trigger/cause;
- exact affected state/IDs;
- preconditions;
- whether reversible, time-bounded, or permanent;
- downstream content/quest dependencies;
- persistence/migration obligation;
- player-facing evidence/feedback requirement.

### 13.3 Branch explosion control

Not every choice should create a permanent global branch. Use scoped facts/consequences where possible and reserve large mutually exclusive state for choices that justify the content/evaluation cost.

### 13.4 Reversibility

Consequences may be irreversible when intentional and signaled. Recovery/alternative content must be considered so one accidental interaction does not silently destroy major progression without evidence.

## 14. WSN-D7 — Authored/generated content architecture

### 14.1 Content brief

A generation/authorship task should receive a bounded brief such as:

```yaml
content_id: <stable>
content_kind: DIALOGUE | QUEST_TEXT | EVENT | LORE | ITEM_TEXT | OTHER
canonical_context_refs: []
allowed_fact_refs: []
required_fact_refs: []
forbidden_or_secret_refs: []
allowed_invention_scope: <bounded>
character_voice/style_refs: []
world/time/location/context: []
interaction/effect_refs: []
length/format/localization constraints: []
provenance_policy_ref: <ref>
review/evaluation_requirements: []
```

### 14.2 Generation rule

Generated content is a **candidate**, never self-canonical evidence. It must pass schema/reference/grounding/consistency and required subjective review/evaluation.

### 14.3 Semantic sameness

Track repeated structures across large corpora:

- identical quest objective chains with cosmetic substitutions;
- repeated dialogue beats/phrases;
- repeated reward patterns;
- repeated NPC archetype/function with no distinctive consequences;
- lore entries that restate facts without adding decisions/discovery/identity.

Repetition metrics are diagnostic, not automatic rejection.

### 14.4 Provenance/originality

Content must preserve project provenance and the distinction between reference inspiration and original Everfield expression. Exact rights/similarity policy belongs to governance/content synthesis; unknown provenance remains a review/quarantine problem, not silent shipping material.

## 15. WSN-D8 — Consistency and evaluation

### 15.1 Structural checks

- schema/reference validity;
- ID uniqueness;
- quest reachability/branch checks;
- chronology constraints;
- knowledge/secret leakage;
- required NPC/location availability;
- relationship/faction state invariants;
- world-state effect conflicts;
- schedule/obligation conflicts;
- localization/key completeness where relevant;
- provenance/brief linkage.

### 15.2 Simulation/evidence

Use:

- deterministic world/NPC state scenarios;
- long-horizon schedule/social simulations;
- quest state-space search;
- branch transition traces;
- save/load/replay of world/social/quest state;
- synthetic-player quest/path execution;
- content semantic-coverage/repetition reports;
- player-surface dialogue/quest comprehension traces.

### 15.3 Subjective critics

Structured critics can judge:

- character voice/consistency;
- thematic fit;
- dialogue naturalness;
- emotional/narrative coherence;
- quest agency/pacing/reward framing;
- repetition/sameness;
- world identity/discovery value.

Record evaluator/rubric versions and disagreement. No single critic/story score is authority.

## 16. Content/state ownership and extensibility

### 16.1 Domain ownership

Prefer narrow source/content ownership:

- individual NPC/content definitions in separate files/packages where practical;
- quest definitions separated by ID/arc/package;
- world facts/lore/history partitioned by domain/time/region with validated cross-refs;
- generated indexes/registries instead of hand-edited global lists;
- shared schemas/quest grammar/fact ontology as conflict-sensitive surfaces.

### 16.2 Extension seams

Adding a normal NPC/quest/dialogue/event should not require edits to unrelated existing definitions beyond explicit shared-world effects/references.

### 16.3 Schema evolution

Changes to fact/relationship/quest schemas require migration/impact analysis for saves, existing content, validators, evaluators, and generated briefs.

## 17. Interfaces/dependencies

### W1-DES-01

Consumes shared-world, lifestyle, discovery, consequence, system-decomposition, and content-depth principles. World/social content should deepen several trajectories without becoming a mandatory one-route story.

### W1-DES-02

Social/narrative systems may provide access, services, relationships, knowledge, sinks, rewards, or world-state changes that are not reducible to general currency. Economy/progression gates must preserve these distinctions.

### W1-EXP-01

Needs dialogue/quest/social state legibility, discovery, content presentation, accessibility/localization, and player-facing consequence feedback.

### W1-TEC-02

Requires stable IDs/schemas, deterministic canonical state, commands/events/queries, persistence/migrations, content compiler/reference validation, and replay/evidence hooks.

### W1-EVAL-01

Should implement quest reachability, narrative consistency, schedule/world simulation, semantic content coverage, repetition analysis, synthetic quest play, and structured subjective judging.

### W1-SYN-GAME

Must reconcile these contracts with game/economy/experience proposals and W1-REV-GAME findings without prematurely authoring the final content corpus.

## 18. Bounded experiments

### WSN-E1 — Contradiction injection

Create a small fact/chronology/branch corpus and inject duplicate/incompatible facts, invalid chronology, and branch conflicts.

**Pass:** validators identify affected facts/branches with bounded diagnostics and avoid false global contradiction where facts are branch/dispute scoped.  
**Failure:** fact/chronology model lacks expressive scope.

### WSN-E2 — Knowledge/secret leakage

Give several NPCs distinct knowledge/belief sets and generate/select dialogue under changing world state.

**Pass:** utterances never reveal forbidden facts unless explicitly allowed; false beliefs can be expressed without becoming objective fact.  
**Failure:** grounding/knowledge model insufficient.

### WSN-E3 — Quest solvability search

Build representative linear, optional, branching, timed, social, collection, and world-state quests plus deliberate soft-lock/cycle defects.

**Pass:** validator/search distinguishes solvable branches from injected dead ends and explains violated predicates.  
**Failure:** objective/gate/effect grammar insufficient.

### WSN-E4 — NPC schedule conflict simulation

Simulate representative schedules under weather/events/closures/quest overrides and travel constraints.

**Pass:** invalid overlaps/inaccessible obligations are detected; override/fallback rules produce valid behavior.  
**Failure:** schedule model too rigid/opaque.

### WSN-E5 — Branching consequence persistence

Apply several irreversible/reversible choices, save/reload, migrate a schema version, and replay downstream content availability.

**Pass:** branch facts/effects persist and migrate consistently; unavailable/available content matches predicates.  
**Failure:** world-state effects are hidden outside canonical persistence.

### WSN-E6 — Generated-content grounding tournament

Generate bounded dialogue/event/quest-text candidates from identical briefs with known facts/secrets and score structural grounding before subjective quality.

**Pass:** invalid fact/secret/reference candidates are rejected independently of prose quality; valid candidates retain variation.  
**Failure:** generation brief/validator cannot constrain hallucinated canon.

### WSN-E7 — Semantic-sameness audit

Generate/author a bounded content batch with deliberately repeated objective/dialogue/reward structures and distinct semantic variants.

**Pass:** diagnostics cluster/reveal repeated patterns without treating legitimate thematic motifs as automatic defects.  
**Failure:** high-volume content can hide functional repetition.

### WSN-E8 — Long-horizon social/NPC simulation

Run many game days/periods under representative world events/player interaction policies.

**Pass:** required NPCs remain reachable under intended conditions, relationships/knowledge evolve legally, no schedule/state deadlocks or impossible quest dependencies emerge.  
**Failure:** interaction model breaks under composition.

### WSN-E9 — Narrative critic disagreement calibration

Freeze a content/evidence set and run multiple structured evaluators/rubrics with known strengths/defects.

**Pass:** disagreement and defect categories are visible; objective grounding failures outrank subjective preference; no single critic becomes authority.  
**Failure:** subjective pipeline is uncalibrated/Goodhart-prone.

## 19. Observability

Diagnostic vector:

- invalid/dangling fact/content references;
- contradiction count by type/scope;
- chronology violations;
- knowledge/secret leakage findings;
- quest unreachable/soft-lock/cycle cases;
- objective/branch type semantic coverage;
- NPC schedule conflict/idle/fallback rates;
- required-character availability failures;
- relationship state transition coverage;
- world-state branch/effect coverage;
- save/load/migration replay mismatch;
- generated-content structural rejection reasons;
- content semantic-sameness/repetition clusters;
- dialogue/quest line/beat repetition;
- synthetic quest completion/failure distributions;
- player-facing clarity/task-completion failures;
- subjective critic disagreement/version drift;
- provenance/brief completeness.

Use together; do not optimize “zero contradictions” by eliminating ambiguity, unreliable narrators, secrets, or branching.

## 20. Failure modes and defenses

### Prose as hidden authority
**Failure:** canonical fact exists only in dialogue/lore text.  
**Defense:** structured fact/effect references; prose is candidate presentation.

### Knowledge omniscience
**Failure:** every NPC knows every world fact.  
**Defense:** explicit knowledge/belief scopes and leakage checks.

### Affection scalar flattening
**Failure:** every social outcome derives from one gift-grind number.  
**Defense:** typed relationship/history state and repetition/effect review.

### Schedule brittleness
**Failure:** event/quest/closure makes NPC impossible to find or logically double-booked.  
**Defense:** schedule constraints, overrides/fallbacks, long-horizon simulation.

### Quest soft lock
**Failure:** required objective/actor/location becomes unreachable.  
**Defense:** graph/state search, branch predicates, failure/retry semantics.

### Branch contradiction
**Failure:** mutually exclusive facts/content are active together.  
**Defense:** scoped branch facts/effect validation.

### Generated canon drift
**Failure:** AI prose invents accepted lore/facts.  
**Defense:** bounded briefs, grounding refs, structural validation, candidate-only authority.

### Infinite content sameness
**Failure:** huge quest/dialogue catalog repeats the same semantic structure.  
**Defense:** semantic-role/repetition clustering plus structured reviewers.

### Custom-code escape hatch dominates
**Failure:** every quest/content object bypasses schemas through scripts.  
**Defense:** registered objective/effect grammar; custom handlers expose validation/evidence contracts and face stronger review.

### Contradiction-free blandness
**Failure:** validators encourage generic safe prose.  
**Defense:** objective structural gates followed by independent subjective/character/world-identity evaluation.

### Narrative state outside saves
**Failure:** reload/migration changes quest/social truth.  
**Defense:** canonical state/effect persistence and migration replay tests.

## 21. Risks and tensions

- Structured facts can become over-engineered if every stylistic detail is normalized; only gameplay/continuity-relevant semantics need canonical structure.
- Rich branching increases content/evaluation/state-space cost; scope branches intentionally.
- Dynamic NPC simulation can conflict with authored quest availability/pacing; explicit overrides/fallbacks are necessary.
- Strong relationship dimensions improve depth but increase UI/authoring/evaluation complexity.
- Generated content can increase variety while also amplifying semantic sameness or canon drift.
- Hidden secrets/unreliable beliefs are desirable narrative devices but complicate naïve contradiction checking.
- Extensive structural validation cannot prove writing quality, character appeal, or emotional impact.

## 22. Open questions

1. Which world/narrative facts deserve canonical structured representation versus remaining presentation-only lore?
2. What minimum relationship dimensions are shared, if any, versus NPC/faction-specific?
3. How should schedules combine authored routines with reactive goals/events?
4. Which quest objective/effect types cover most content without becoming a general programming language?
5. How should temporary/seasonal/timed quests avoid anxiety/soft locks while preserving world cadence?
6. How should unreliable narrators/disputed history be represented and evaluated?
7. What branching scope is sustainable for autonomous content production and verification?
8. What content generation is safe to perform dynamically at runtime versus author/build time?
9. How should character voice/style references be versioned and evaluated?
10. What narrative facts/choices can become economically/progression significant without making story participation mandatory?
11. Which NPC/social simulations need determinism for tests and which can tolerate bounded variation?
12. How should localization interact with generated dialogue/content and consistency checks?
13. What provenance/similarity evidence is required for high-volume generated narrative/visual/audio-adjacent content?

## 23. Reopen conditions

Reopen if:

- fact/knowledge schemas cannot express important branching/unreliable-narrator cases without excessive complexity;
- quest solvability validators miss common soft locks in representative content;
- NPC schedule simulation repeatedly conflicts with authored quest/story needs;
- generated-content grounding rejects too much legitimate creative variation or permits canon drift;
- semantic-sameness evaluation cannot distinguish healthy motifs from repetitive content;
- persistence/migration cannot preserve world/social/quest consequences reliably;
- game review finds narrative architecture forces one canonical playthrough or weakens sandbox lifestyles;
- technical constraints make structured fact/quest/content tooling too merge-hostile or expensive;
- UX/accessibility evidence shows state/consequences cannot be communicated legibly;
- later subjective/player evidence shows structurally valid narrative remains incoherent or emotionally flat.

## 24. Required critique and downstream work

Required independent critique: `W1-REV-GAME`.

Review should attack:

- whether structured facts are sufficient but not overreaching;
- hidden prose/script authority;
- knowledge/secret leakage;
- NPC schedule/quest composition failures;
- relationship-grind degeneracy;
- quest soft locks/branch contradictions;
- generated-content canon drift/semantic repetition;
- persistence/migration of consequences;
- conflicts with sandbox viability, progression/economy, experience/accessibility, and technical architecture.

W1-SYN-GAME should reconcile this exact reviewed work with the other game/experience candidates. This artifact is non-canonical and authorizes no content catalog or gameplay implementation.
