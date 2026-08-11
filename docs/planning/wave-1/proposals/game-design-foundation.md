# Game-Design Foundation and Possibility-Space Model — Wave 1 Proposal

**Mission:** `W1-DES-01`  
**State:** PROPOSAL / NON-CANONICAL  
**Required review:** `W1-REV-GAME`

## Review Index

- **GDF-D1 — Pillars (§8):** Everfield should optimize for interacting possibility, player-directed life paths, discovery of hidden depth, progression in agency, and durable world attachment—not feature count.
- **GDF-D2 — Multi-horizon loop (§9):** minute-to-minute actions, day planning, seasonal adaptation, medium-term projects, and long-horizon specialization/infrastructure must each create decisions and feed one another without one mandatory route.
- **GDF-D3 — Possibility-space model (§10):** evaluate breadth as viable trajectories through systems, not catalog counts; lifestyles are soft specializations measured by viability, distinctness, cross-system interaction, and switching cost.
- **GDF-D4 — Layered discovery (§11):** expose enough structure for agency while reserving mechanics, regions, production layers, social/narrative facts, and interaction depth for paced discovery; hidden depth must remain discoverable rather than opaque.
- **GDF-D5 — System decomposition (§12):** decompose around persistent state/verbs/economy/progression interfaces, not genre checklist labels; systems should own clear contracts while content participates across multiple systems.
- **GDF-D6 — Chore and automation policy (§13):** repetition is acceptable while it teaches, expresses mastery, or creates meaningful tradeoffs; low-decision repetition should gain optional relief/automation paths whose capital/logistics costs open higher-order decisions.
- **GDF-D7 — Progression and late game (§14):** progression should increase capabilities, options, scale, knowledge, and leverage rather than only numeric power; late game must create new ambitions and durable resource sinks without invalidating direct-play lifestyles.
- **GDF-D8 — Extensibility (§15):** new content should deepen multiple interaction graphs when possible; content growth is reviewed for semantic roles, dependencies, consequences, and discovery—not volume alone.
- **Evidence (§5):** charter/mandate explicitly require a larger meaningful possibility space, radical sandbox structure, automation as progression, perceived inexhaustibility, continuous expansion, and avoidance of a single canonical playthrough.
- **Experiments (§18):** trajectory viability, chore-burden, discovery cadence, automation escalation, system-coupling, dominant-route, late-game sink, and content-depth simulations must test these hypotheses.
- **Reviewer attack points:** hidden mandatory path; nominal rather than viable lifestyles; automation becoming passive waiting; content-count inflation; discovery opacity; progression currencies collapsing into one optimizer; system decomposition creating cross-domain bottlenecks; late-game escalation erasing cozy/direct play.

## 1. Objective

Define a testable game-design foundation for Everfield that can support a very large meaningful possibility space without assuming that “larger” means more item rows, more quests, or more maps.

The proposal establishes candidate pillars, time-horizon loops, sandbox/possibility-space semantics, discovery and progression principles, system-decomposition rules, chore/automation policy, late-game direction, extensibility criteria, observability, and bounded experiments.

## 2. Scope

In scope:

- game pillars and anti-pillars;
- player-agency and sandbox structure;
- minute/day/season/project/long-horizon loop relationships;
- lifestyle/specialization model;
- system interaction and decomposition principles;
- discovery/unlock philosophy;
- progression and switching/cross-system participation;
- chore/repetition policy;
- automation progression philosophy;
- late-game ambition and economic sinks;
- content-growth/extensibility principles;
- player possibility-space observability;
- failure modes, experiments, and reopen conditions.

## 3. Non-goals

This proposal does **not**:

- enumerate the final feature/system catalog;
- set exact day length, season length, prices, stamina values, drop rates, skill curves, or progression thresholds;
- define final world fiction, NPC cast, quests, regions, crops, machines, enemies, or recipes;
- choose a final visual/audio style;
- assert that every player must use automation or every activity must be equally profitable;
- require every system to interact with every other system;
- define final onboarding/UI solutions;
- turn Stardew Valley into a cloning specification;
- authorize gameplay implementation.

## 4. Intent constraints and assumptions

### 4.1 Observed intent constraints

The authoritative packet requires or strongly directs:

1. Everfield targets a materially larger **meaningful possibility space** than its reference model.
2. The target structure is “many overlapping games sharing the same world,” not one dominant game plus decorative side activities.
3. Players should be able to emphasize different identities without selecting rigid classes.
4. Expansion should be systemic/combinatorial rather than primarily catalog growth.
5. Perceived inexhaustibility should come from layered discovery and interaction depth, not literal infinite procedural output.
6. Automation is a core progression fantasy and an important route from labor toward infrastructure, logistics, and higher-level agency.
7. Automation should free attention for larger ambitions, not end gameplay.
8. Continuous expansion and cheap content/system extension are expected.
9. Narrative, mechanics, and world/content are first-class spaces that must evolve together.
10. No final balance/content fact is established in the current planning phase.

### 4.2 Assumptions to test

- Players can experience genuinely distinct lifestyles in one shared economy/world without hard classes.
- Optional cross-system dependencies can add coherence without forcing every player through every system.
- New decision layers can replace low-level repetitive work as automation increases.
- A large game can preserve legibility by progressively revealing systems rather than exposing the full possibility graph at once.
- Content that participates in several systems tends to create more perceived depth than isolated collectible/count expansion.
- Late-game capital/infrastructure sinks can coexist with satisfying low-scale direct play if progression is capability-oriented rather than mandatory industrialization.
- Synthetic player/simulation evidence can expose obvious dominant routes, dead systems, burden, and progression dead ends even though final experiential quality also needs structured subjective evaluation.

## 5. Evidence, inference, and recommendation

### 5.1 Evidence from the authoritative packet

The charter and game-design mandate explicitly call for:

- broader meaningful player trajectories;
- sandbox specialization without rigid classes;
- interaction density;
- automation as progression and late-game economic sink;
- continuous system/content expansion;
- discovery of layers larger than initially expected;
- optional direct-play lifestyles;
- narrative and questing as first-class rather than post-hoc content;
- evaluation of whether systems increase meaningful ways to live rather than only content volume.

The research agenda identifies unresolved questions around viable lifestyles, dominant strategies, automation payback and burden, perceived inexhaustibility, discovery cadence, economy/progression simulation, and UX legibility.

### 5.2 Inference

A feature checklist cannot be the primary architecture of game design. If the game is meant to support many trajectories, the more useful object is a graph of **player goals, verbs, resources, knowledge, relationships, locations, systems, and progression gates** and the viable routes among them.

Likewise, “optional” should not mean merely technically skippable. A lifestyle is meaningfully viable when it can sustain goals/progression for a substantial horizon without constantly requiring the supposedly optional dominant route.

### 5.3 Recommendation

Adopt the following pillars and design tests as a Wave 1 candidate baseline. Treat the experiments as gates on strong claims rather than as implementation backlog.

## 6. Alternatives considered

### A. One canonical core path with many optional side activities — reject as target

It can simplify pacing and balance, but contradicts the desired radical sandbox. Some common foundation/onboarding is acceptable; long-horizon play should branch materially.

### B. Every major lifestyle is fully self-sufficient — reject

This risks making the shared world incoherent and systems irrelevant to one another. Prefer **soft dependence**: multiple sources/solutions, optional trade, relationships, services, markets, quests, or infrastructure can bridge systems without mandating one exact activity.

### C. Equalize all activities by one currency-per-minute metric — reject

A scalar can destroy identity and Goodhart the economy. Activities may differ in money, materials, knowledge, relationships, access, risk, convenience, discovery, and personal expression. Viability is multi-dimensional.

### D. Infinite procedural content as the primary inexhaustibility strategy — reject as default

Quantity without semantic consequences becomes repetition. Procedural/generative techniques may supplement authored/systemic depth when they create meaningful variation.

### E. Automate every repeated action as soon as it repeats — reject

Some repetition teaches rules, creates rhythm, offers mastery, or is intrinsically pleasurable. Automation/relief should target **low-decision burden**, not simply repeated animation.

### F. Preserve all manual chores forever for “coziness” — reject

Long-lived mandatory repetition conflicts with progression in agency and creates burden for players pursuing larger-scale goals. Manual paths can remain available without forcing them.

## 7. Design vocabulary

Use these terms consistently in later synthesis:

- **verb** — meaningful player action category (plant, trade, converse, explore, craft, fight, configure, etc.); exact list not fixed.
- **goal** — player-recognizable desired state, self-authored or game-authored.
- **capability** — new class/scale/quality of action available to the player.
- **resource** — consumable/store of value, including time and attention when modeled.
- **knowledge** — information that changes decisions or access; may be player knowledge, character knowledge, recipe/technical knowledge, etc.
- **gate** — condition controlling access; gates need rationale, alternatives, and visibility.
- **system** — coherent state + rules + verbs + interfaces that create decisions/consequences.
- **content** — authored/generated instances participating in systems.
- **lifestyle / soft specialization** — sustained emphasis on a subset of systems/goals, without irreversible class lock.
- **trajectory** — time-ordered path through goals, systems, capabilities, and world states.
- **burden** — required low-decision player input/time needed to maintain desired state.
- **leverage** — capability that increases output/coverage/optionality per unit of attention.
- **discovery** — acquisition of new actionable knowledge, mechanics, places, relationships, or interactions.

## 8. GDF-D1 — Game pillars

### Pillar 1: Many viable ways to live

Players should be able to build substantial play identities around different mixtures of production, exploration, social life, quests, commerce, collection, infrastructure, combat, crafting, automation, and other later-selected systems.

**Test:** can different synthetic/structured player profiles pursue meaningful medium- and long-horizon goals without converging immediately on the same required activity sequence?

### Pillar 2: Systems compound one another

Content and mechanics should often gain value from cross-system use: a resource may matter for economy, crafting, relationships, quests, production, discovery, or automation rather than belonging to one isolated table.

**Test:** system/content interface graph has meaningful multi-system roles without requiring indiscriminate all-to-all coupling.

### Pillar 3: The world keeps revealing depth

Progress should reveal new mechanics, places, relationships, combinations, strategic information, and scales of operation after players believe they understand the current layer.

**Test:** representative trajectories experience recurring new decision categories, not only higher numerical tiers or reskinned items.

### Pillar 4: Progression increases agency

Progress should change what players can decide, control, automate, specialize in, discover, and build—not only increase numbers.

**Test:** major progression milestones add capabilities/options or reduce chosen burdens while opening new decisions.

### Pillar 5: The world is shared across lifestyles

Specializations should still participate in one coherent world: markets, places, NPCs, events, stories, resources, and consequences can connect different paths.

**Test:** lifestyle paths intersect through optional benefits/consequences without one path becoming universal compulsory homework.

### Anti-pillars

Reject designs that primarily optimize for:

- raw item/quest/map counts;
- one mathematically dominant route;
- mandatory completionist traversal of every system;
- passive progression after automation;
- opaque secrets with no discoverability affordance;
- chores maintained solely to inflate playtime;
- irreversible specialization before players understand consequences;
- progress that only increases output numbers without changing decisions.

## 9. GDF-D2 — Multi-horizon loop model

The final mechanics remain open, but a coherent sandbox should produce decisions at several horizons.

### 9.1 Moment-to-moment

Questions such as:

- what action/interaction do I take now?
- what resource/tool/location is relevant?
- what risk/attention cost does this action have?
- do I continue, switch, explore, or return?

Target: actions have legible feedback and are not dominated by long input sequences with no decisions.

### 9.2 Day / short session

Questions such as:

- which goals deserve limited time/attention today?
- which opportunities/events/weather/relationships/resources matter now?
- what maintenance is necessary versus optional?
- where do I travel and what do I combine in one trip?

Target: a day/session supports planning and tradeoffs without requiring a fixed checklist.

### 9.3 Season / medium cadence

Questions such as:

- which opportunities are temporary or changing?
- what projects/investments should mature over this horizon?
- which relationships/world events/progression gates shift?
- how does the player adapt rather than repeat an identical loop indefinitely?

Exact calendar structure is not decided here; “season” denotes a meaningful medium cadence if retained.

### 9.4 Project horizon

Examples of goal shapes, not fixed features:

- establish a new production chain;
- restore/build/upgrade a property;
- pursue a relationship/faction/story arc;
- explore/unlock a region;
- complete a collection/research objective;
- solve a logistics/automation problem;
- prepare for a high-risk expedition;
- build commercial/social influence.

Projects should link multiple short-term actions into visible player-authored purpose.

### 9.5 Long horizon

Questions:

- what kind of life/economy/infrastructure/social identity has the player built?
- what new scales or layers become possible?
- what remains surprising after mastery of earlier loops?
- what goals remain meaningful when basic scarcity is solved?

Late game must not be “same loop, larger number.”

### 9.6 Loop coupling rule

Every major system should identify which horizons it enriches and what it contributes to other horizons. A system that occupies time but does not create or support decisions/goals at any horizon is suspect.

## 10. GDF-D3 — Possibility-space and sandbox model

### 10.1 Possibility graph

Later game synthesis should maintain a machine-readable conceptual graph with nodes/edges such as:

```text
goals
verbs
systems
capabilities
resources
knowledge
locations
relationships/factions
progression gates
content families
world-state consequences
```

Edges describe enabling, consuming, producing, revealing, requiring, substituting, conflicting, or amplifying relationships.

This is a design/evaluation graph, not necessarily a runtime architecture.

### 10.2 Lifestyle viability

For each proposed soft specialization, test a vector rather than a scalar:

- **goal depth** — substantial medium/long goals exist;
- **economic viability** — can obtain needed general resources through activity/trade/substitutes;
- **progression viability** — meaningful capabilities/unlocks can advance;
- **decision diversity** — repeated play contains choices, not one rote sequence;
- **cross-system optionality** — other systems provide benefits without constant compulsory use;
- **identity distinctness** — choices/constraints feel materially different from other paths;
- **recovery** — mistakes/bad luck do not irreversibly dead-end the lifestyle without warning;
- **switchability** — player can hybridize/switch with understandable cost.

Do not require equal values across lifestyles. Require evidence that differences are intentional and not accidental invalidation.

### 10.3 Foundational versus specialization-specific content

Some shared foundation is inevitable: input/navigation, basic world access, core economy/time, save/progression comprehension, etc. Later design must explicitly classify shared prerequisites and challenge any prerequisite that becomes a hidden mandatory lifestyle.

### 10.4 Multiple solutions

Where practical, important needs should have several sources or exchange paths. Example abstract pattern:

```text
need X
 -> produce directly in system A
 -> trade/buy using value from system B
 -> obtain through relationship/quest C
 -> discover substitute D
```

This supports sandbox coherence without complete self-sufficiency.

## 11. GDF-D4 — Discovery and unlock philosophy

### 11.1 Reveal decisions, not the entire database

Players need enough information to make intentional choices, but the complete interaction graph need not be visible immediately.

Discoverable layers may include:

- new verbs/mechanics;
- new content categories;
- new locations/routes;
- new social/narrative facts;
- new production/automation layers;
- new interactions between known systems;
- new strategic information/market opportunities;
- hidden or alternate progression paths.

### 11.2 Discovery affordances

A hidden element should normally have at least one discoverability channel appropriate to its importance:

- environmental clue;
- NPC/dialogue/quest clue;
- interface hint/collection gap;
- experimentation feedback;
- progression lead;
- map/world signal;
- pattern/recipe inference;
- explicit tutorial/onboarding for foundational rules.

Major progression should not depend on arbitrary unknowable actions unless the obscurity is itself bounded optional content.

### 11.3 Discovery cadence

Avoid a fixed “new thing every N minutes” rule. Instead measure whether representative trajectories have long stretches where only numerical replacement occurs with no new meaningful option/interaction/knowledge.

### 11.4 Recontextualization

High-value discovery can make old content newly meaningful: a new recipe, machine, NPC preference, quest, environmental condition, market, region, or capability can change the value of previously familiar resources.

This is a preferred form of depth because it compounds existing content rather than only appending tiers.

## 12. GDF-D5 — System decomposition principles

Do not freeze decomposition from the seed checklist. A candidate system deserves separation when it has a coherent combination of:

- persistent state/invariants;
- distinctive verbs/decisions;
- progression/economy role;
- content families;
- evidence/testing needs;
- interfaces with several other systems;
- ownership/extensibility benefit from a stable contract.

### 12.1 Candidate domain families

The seed list suggests families such as world/time/weather, player/items, production/farming/animals, gathering/exploration/combat, crafting/automation/logistics, economy/property, NPC/social, quests/story/events, cooking/collections/skills, regions/late-game, UI/accessibility. These are **research partitions**, not canonical modules.

### 12.2 Avoid mega-systems

A “gameplay system” module that owns inventory, economy, quests, NPC state, progression, and world changes becomes a parallelism bottleneck. Shared contracts should be narrow and explicit.

### 12.3 Avoid micro-system fragmentation

Conversely, every item type or mechanic should not require a unique framework. Repeated structural patterns should share content/schema/behavior interfaces where evidence supports it.

### 12.4 Cross-system content role

Content specs should declare semantic roles/interfaces, for example:

```yaml
content_id: <stable>
participates_in:
  - system: <domain>
    role: <input/output/gate/reward/relationship/etc>
discovery_sources: []
progression_effects: []
economy_effects: []
validation_obligations: []
```

Exact schema belongs to content/technical planning.

## 13. GDF-D6 — Chore, repetition, and automation policy

### 13.1 Repetition categories

Distinguish repeated action by purpose:

1. **learning repetition** — teaches rule/timing/system understanding;
2. **mastery repetition** — skill expression improves outcomes;
3. **ritual/rhythm repetition** — intrinsically satisfying routine/attachment;
4. **planning repetition** — same action category but context/choices vary;
5. **maintenance burden** — low-decision input required mainly to prevent loss/keep baseline functioning.

Automation/relief pressure should be strongest on category 5 and on categories that decay into 5 after mastery.

### 13.2 Burden vector

Measure:

- required inputs/actions;
- real/session time;
- travel overhead;
- attention interruption;
- decision density;
- penalty for omission;
- frequency;
- scale sensitivity;
- availability/cost of relief.

No single “chore score” governs acceptance.

### 13.3 Relief ladder

Potential relief forms, not fixed fiction:

```text
better tool / batch action
 -> improved layout/infrastructure
 -> helper/service/delegation
 -> partial automation
 -> full local automation
 -> logistics/network automation
 -> portfolio/operation management
```

Different systems may use social, magical, technological, infrastructural, economic, or other fiction.

### 13.4 Automation rule

Automation should exchange recurring labor for meaningful setup costs/constraints such as capital, resources, space, maintenance, knowledge, relationships, logistics, energy, risk, or opportunity cost. Exact costs are open.

Once established, it should create new choices at a higher level: configuration, optimization, expansion, routing, quality, resilience, trade, specialization, or allocation.

### 13.5 Manual path preservation

A player who enjoys direct labor should be able to continue it where feasible. Do not make industrial scale mandatory for narrative completion or basic legitimacy unless later evidence/design explicitly supports a bounded exception.

Manual play need not equal automated throughput; it must remain meaningful and understandable.

## 14. GDF-D7 — Progression and late-game principles

### 14.1 Progression dimensions

Track progression across multiple dimensions:

- capability/verbs;
- efficiency/leverage;
- scale/coverage;
- knowledge/discovery;
- access/regions;
- relationships/social authority;
- customization/expression;
- production complexity;
- automation/logistics;
- risk tolerance/recovery;
- narrative/world-state influence;
- collection/mastery where relevant.

Avoid collapsing all progression into one level number or universal currency.

### 14.2 Gating principles

A gate should declare:

- purpose;
- what player behavior/knowledge it asks for;
- visibility/foreshadowing;
- alternative routes/substitutions if any;
- consequences for lifestyle viability;
- recovery if missed;
- whether it is foundational or specialization-specific.

### 14.3 Late-game transition

When basic needs/early scarcity are solved, the game should increasingly support:

- large projects and world changes;
- infrastructure/automation/logistics;
- rare knowledge/content chains;
- high-capital choices and durable sinks;
- social/narrative/faction consequences;
- multi-site or broader-scope operations where appropriate;
- optimization/customization/collection goals;
- optional high-difficulty/risk/exploration content;
- new system layers rather than only better numbers.

This is a menu of ambition types, not a requirement that all late games industrialize.

### 14.4 Durable sinks

Automation/infrastructure is one candidate sink, but later economy design should test a diverse sink portfolio: property/world projects, customization, services, collection, research, social/community investment, exploration, risk, maintenance, prestige, etc. Exact systems remain open.

## 15. GDF-D8 — Extensibility and content-growth quality

### 15.1 Content-depth test

For a new content family/object, ask:

1. Which player decisions does it create/change?
2. Which systems does it participate in?
3. What old content can it recontextualize?
4. How is it discovered/understood?
5. Does it enable a new trajectory/goal/strategy or only another count?
6. What progression/economy/narrative consequences can it have?
7. What validation/evidence prevents semantic duplication/broken references?

Not every content item needs many answers; at the catalog level, shallow rows should not dominate growth.

### 15.2 Semantic sameness risk

AI production can generate superficially different content with identical function. Later content/evaluation work should detect clusters with near-identical mechanics, rewards, narrative beats, or decision consequences.

### 15.3 Expansion seams

System specs should expose extension seams for:

- new content instances;
- new modifiers/conditions;
- new rewards/costs;
- new interactions;
- new progression gates;
- new locations/world-state links;
- new quests/dialogue/story consequences;
- new automation/logistics participation where relevant.

A system requiring invasive global edits for routine new content violates the expansion goal.

## 16. Player-agency and consequence principles

### 16.1 Soft commitments

Specialization choices should usually create opportunity costs and identity without premature irreversible class locks. Strong irreversible decisions are allowed when clearly signaled and narratively/mechanically justified.

### 16.2 Failure and recovery

Failure can create stakes, but ordinary experimentation should not casually destroy a long playthrough. Later systems should classify reversible setbacks, costly recovery, permanent world consequences, and true fail states explicitly.

### 16.3 World response

Actions should increasingly have visible consequences: economy, relationships, world state, access, production, narrative, or environment where appropriate. Consequence density helps different trajectories feel authored rather than like isolated minigames.

### 16.4 Player-authored goals

The game should support recognizable goals beyond explicit quests: building a business, collection, relationship network, specialized property, infrastructure system, exploration mastery, wealth, aesthetic world, etc. Exact goals emerge from later system design.

## 17. Observability and evaluation model

Track a design diagnostic vector by representative trajectory/persona:

- systems meaningfully used over time;
- distinct goal categories pursued;
- proportion of progression coming from top one/two activities;
- required cross-system participation;
- viable substitutes/routes for foundational needs;
- decision density versus low-decision burden;
- travel/maintenance overhead;
- automation adoption timing and payback;
- new decision categories unlocked after automation;
- trajectory switching/hybridization cost;
- dominant-strategy prevalence;
- dead-end/unreachable goals;
- discovery/recontextualization events by horizon;
- content semantic-role diversity;
- late-game resource accumulation versus sink demand;
- long stretches without new options/knowledge;
- subjective evaluator disagreement by structured rubric.

Interpret together; do not optimize one scalar.

## 18. Bounded experiments / evidence plan

### GDF-E1 — Lifestyle trajectory viability simulation

Build abstract progression/economy graphs for several candidate lifestyles and hybrid profiles once downstream system proposals exist.

**Pass:** multiple profiles can sustain medium/long goals and foundational needs through materially different routes with understandable cross-system dependencies.  
**Failure:** hidden mandatory path or nominal specialization; revise gates/sources/economy.

### GDF-E2 — Dominant-route red team

Give optimizer/exploit profiles the ability to switch across all systems in an abstract/simulated ruleset.

**Pass:** no single route trivially dominates most goals/resources without meaningful opportunity cost; where dominance exists it is scoped/intentional.  
**Failure:** cross-system economy/progression collapses sandbox diversity.

### GDF-E3 — Chore-burden traces

Record representative action/travel/maintenance/decision traces for early, mid, and mature worlds.

**Pass:** repeated low-decision burden does not scale indefinitely without optional relief; direct-play loops that remain are intentionally satisfying/decisionful.  
**Failure:** introduce batch/infrastructure/automation/design relief or change penalties/frequency.

### GDF-E4 — Automation escalation test

For representative chores, map manual → relief → automation tiers plus setup costs and the decisions created after each tier.

**Pass:** each major burden reduction opens meaningful allocation/configuration/expansion/logistics choices rather than only passive waiting.  
**Failure:** revise automation fantasy or add higher-order goals/interactions.

### GDF-E5 — Discovery-cadence / recontextualization audit

Take several planned trajectories and annotate when genuinely new mechanics/interactions/places/knowledge appear and when old content changes meaning.

**Pass:** depth arrives across horizons with clues/affordances; no long mandatory stretch is only number inflation/repetition.  
**Failure:** restructure unlocks/content interactions/onboarding.

### GDF-E6 — System-coupling graph audit

Construct system/content interface graph from detailed specs.

**Pass:** enough cross-links create coherent depth while no mega-system or universal prerequisite becomes a central bottleneck.  
**Failure:** split ownership, add alternatives, or reduce coupling.

### GDF-E7 — Late-game sink/ambition simulation

Simulate representative mature profiles after basic scarcity is solved.

**Pass:** several optional ambitions consume resources/attention and create new decisions; wealth/resources do not become universally meaningless immediately.  
**Failure:** revise sink portfolio/progression layers rather than merely increasing prices.

### GDF-E8 — Content-depth sample review

Generate/design a bounded candidate content set, then classify semantic roles, interaction links, discovery, and trajectory effect.

**Pass:** additional volume increases role/interaction diversity and recontextualizes existing content; duplicate semantic rows are detectable.  
**Failure:** tighten content grammar/generation/evaluation rather than increasing generation volume.

### GDF-E9 — Sandbox comprehension test

Use synthetic task-completion/structured evaluator scenarios on a progressively revealed possibility map/UI prototype later.

**Pass:** players/agents can form intentional goals and discover optional systems without seeing the entire database or being unknowably blocked.  
**Failure:** revise signaling, navigation, gating, and discovery affordances.

## 19. Interfaces and dependencies

### W1-DES-02 / progression-economy-automation

Needs this proposal’s lifestyle viability, burden, automation, progression, gate, and late-game criteria. It owns concrete economic/progression models and simulations.

### W1-DES-03 / narrative-world-content

Needs shared-world/lifestyle/discovery/consequence principles. It owns world, narrative, NPC, quest, and content-space foundations.

### W1-EXP-01 / experience/accessibility/visual-audio process

Needs discovery, legibility, burden, direct-play, and player-agency principles. It owns UX/accessibility/presentation production/evaluation process.

### W1-EVAL-01

Should turn trajectory viability, burden, discovery cadence, dominant-route detection, semantic content diversity, and late-game simulation into machine-observable evaluation surfaces.

### W1-TEC-02

Game systems should later declare persistent state, commands/events/queries, content schemas, determinism, and persistence needs without allowing technical architecture to dictate design decomposition blindly.

### W1-SYN-GAME

Must reconcile game-design proposals and any review findings into one coherent candidate, explicitly deciding which system partitions and metrics become canonical candidates versus experiments.

## 20. Failure modes and defenses

### Hidden mandatory playthrough
**Failure:** “optional” systems all depend on one universal money/material/progression route.  
**Defense:** lifestyle trajectory and prerequisite graph audits; multiple sources/substitutions.

### Nominal lifestyle diversity
**Failure:** labels differ but optimal actions/progression are identical.  
**Defense:** measure identity distinctness, decision diversity, resource/gate structure, and trajectory switching.

### Catalog bloat
**Failure:** AI creates thousands of semantically redundant items/quests.  
**Defense:** content-depth/semantic-role audit and interaction/recontextualization criteria.

### Discovery opacity
**Failure:** depth exists but is effectively unknowable.  
**Defense:** discoverability channels and sandbox comprehension tests.

### Checklist day
**Failure:** every player repeats universal mandatory chores before meaningful choices.  
**Defense:** burden traces, optionality, relief paths, and foundational-prerequisite scrutiny.

### Automation as passive ending
**Failure:** player removes all interaction and waits.  
**Defense:** automation tiers must open higher-order decisions/projects/scales.

### Automation as mandatory ideology
**Failure:** manual/cozy lifestyles become invalid.  
**Defense:** preserve meaningful manual paths and test lifestyle viability separately from maximum throughput.

### One progression scalar
**Failure:** every system collapses into one XP/currency optimizer.  
**Defense:** multidimensional capabilities/knowledge/access/relationships/resources and scoped gates.

### Irreversible ignorance trap
**Failure:** player commits to specialization before consequences are legible.  
**Defense:** soft commitment default; signal costly irreversible choices.

### Mega-system decomposition
**Failure:** one architecture/domain owns all cross-system state and blocks parallel extension.  
**Defense:** interface graph and later technical conflict review.

### Shallow late game
**Failure:** same early actions with larger prices/output.  
**Defense:** new ambition/system layers, resource sinks, world/social consequences, infrastructure/knowledge.

### Scalar quality gaming
**Failure:** design optimizes “fun,” profit/hour, discovery count, or system-use count.  
**Defense:** diagnostic vector + structured subjective panels + adversarial profiles.

## 21. Risks and unresolved tensions

- Strong cross-system interaction can undermine optional lifestyles if dependencies are not substitutable.
- Too much hidden depth can reduce agency; too much early visibility can overwhelm and spoil discovery.
- Automation can conflict with ritual/cozy enjoyment; burden classification must distinguish enjoyable repetition from maintenance debt.
- Many viable paths complicate authored pacing and narrative/world-state consistency.
- Persistent consequences strengthen identity but can conflict with free switching/recovery.
- Large extensible content space can overload inventory/UI/localization/evaluation even if technical schemas scale.
- Synthetic viability metrics may miss experiential identity; later structured subjective and player-surface evaluation remains necessary.

## 22. Open questions

1. Which systems are truly foundational for every playthrough, and which can be substitute-provided?
2. What time/calendar model best creates planning tradeoffs without schedule anxiety or universal daily checklists?
3. How different should lifestyle economic outputs be before one becomes nonviable versus intentionally specialized?
4. Which manual actions should remain enjoyable deep into the game even when automation exists?
5. What kinds of real consequences can preserve agency without making experimentation punishing?
6. How should story/world progression adapt to players who ignore major system families?
7. How much content should be mutually exclusive, conditional, or playthrough-specific?
8. Which progression layers should be universal knowledge/capability versus system-specific mastery?
9. How should multi-site/large-scale late-game ambitions coexist with small-scale/cozy play?
10. Which possibility-space metrics correlate with structured subjective judgments of depth rather than merely complexity?
11. What discovery clues are needed for optional deep systems without turning the UI into a checklist?
12. Which system boundaries best support both design coherence and safe technical/agent parallelism?

## 23. Reopen conditions

Reopen this proposal if:

- economy/progression simulation shows most viable paths converge on one mandatory route;
- chore traces show burden grows faster than available relief for normal trajectories;
- automation reduces decisions without opening meaningful higher-level goals;
- game-domain review finds a pillar contradicts narrative/world/experience requirements;
- system interface graphs reveal one proposed foundation becomes a central ownership bottleneck;
- synthetic/structured evaluation cannot distinguish nominal from meaningful lifestyle diversity;
- representative UX prototypes cannot make the broad possibility space legible/discoverable;
- late-game simulations cannot sustain several meaningful ambitions after scarcity is solved;
- content-depth audits show cross-system participation creates excessive coupling or semantic sameness persists despite criteria;
- later player evidence contradicts assumptions about repetition, switching, discovery, or scale.

## 24. Required critique and downstream work

Required independent critique: `W1-REV-GAME`.

That review should aggressively test:

- whether “many viable lifestyles” has operational meaning;
- hidden mandatory foundation routes;
- whether automation policy preserves both agency and play;
- whether discovery has enough signaling;
- whether the system-decomposition guidance is implementable without mega-contracts;
- whether late-game principles create qualitatively new choices;
- whether the proposed metrics can be Goodharted;
- whether this foundation leaves enough room for narrative, accessibility, and authored pacing.

Downstream W1-SYN-GAME should consume this exact work state together with the other game/experience proposals and review findings. No conclusion here is canonical by authorship.
