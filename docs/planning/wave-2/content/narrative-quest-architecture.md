# W2 Narrative, Quest, and Consequence Architecture Candidate

**Mission:** `W2-CONTENT-NARR-01`  
**Issue:** #369  
**State:** PRODUCER CANDIDATE / NONCANONICAL  
**Conflict domain:** `CONTENT_NARRATIVE`  
**Required next gate:** fresh independent/degraded-independent root review  
**Integration authority:** NONE

## 1. Purpose and authority boundary

This packet proposes a bounded, engine-neutral narrative/quest/consequence architecture for Everfield. It defines structural story roles, quest grammar, discovery/knowledge boundaries, consequence semantics, and route-evidence obligations without fixing the sibling world, faction, or character candidates.

It is a content-planning candidate only. It does **not** choose an engine, authorize gameplay/high-throughput implementation, establish implementation readiness, satisfy empirical WSN evidence, grant integration/decision/release authority, or make any plot, character, faction, location, event, fact, quest, or dialogue canonical.

Frozen authority inputs:

- Planning Program v1 blob `e3120ec203c4156328770aa86c12fbb7187966dc`;
- canonical binding Issue #6 comment `5245368879`;
- canonical activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- owner parallel-frontier directive Issue #84 comment `5305563203`;
- content compiler Issue #365 claim `5305566663`, exact work `fd2fb7d816cf23d60bcc54bd25c7d9a4eaae3dbb`;
- clean activation review Issue #372 terminal `5305598079`, head `656930c36d90a166776485cbaf196c39a32fe97e`, disposition `CLEAN_FOR_BOUNDED_CONTENT_FRONTIER_ACTIVATION`;
- W1-DES-03 exact work `d19ddc43c9e5f22c6f14e5c978c30a4e6a2f0d8b`;
- W1-SYN-GAME exact work `e74e0b0c95e85f69718868eedae324a298f02f3e`;
- canonical Wave-1 foundation `docs/planning/WAVE-1-FOUNDATIONS-v1.md`.

The sibling roots #366–#368 are **not inputs**. Cross-domain references below are provisional typed roles only.

## 2. Candidate narrative promise

The bounded narrative architecture explores three compatible thematic tensions without assigning final lore:

1. **belonging versus self-direction** — participation in a place/community can create obligations, but belonging is not a universal progression tax;
2. **stewardship versus extraction** — player projects may improve, exploit, preserve, transform, or relinquish shared resources, with visible consequences rather than one moral score;
3. **truth versus useful stories** — objective facts, beliefs, rumors, secrets, and player discoveries can diverge without unreliable claims silently becoming world truth.

These are structural content lenses, not canonical story facts. Downstream fan-in may revise or replace them.

## 3. Sibling-independent interface vocabulary

Only provisional roles may point into unresolved sibling domains:

- `WORLD_ROLE:HOME_REGION` — a player-relevant region/context, not a final place;
- `WORLD_ROLE:CONTESTED_COMMON` — a shared resource/place whose use can carry consequences;
- `WORLD_ROLE:HISTORY_BEARER` — an object/site/institutional record that can expose conflicting claims;
- `FACTION_ROLE:CUSTODIAN` — a social group oriented toward continuity/stewardship;
- `FACTION_ROLE:CHANGE_ADVOCATE` — a group oriented toward transformation/growth;
- `FACTION_ROLE:OUTSIDE_PRESSURE` — an actor representing external demand or leverage;
- `CHAR_ROLE:RETURNING_TIE` — a principal relationship that can surface belonging/history;
- `CHAR_ROLE:LOCAL_WITNESS` — a perspective-holder with bounded knowledge;
- `CHAR_ROLE:COUNTERVOICE` — a perspective-holder who can challenge dominant explanations.

These identifiers are placeholders. Producers must not dereference mutable sibling artifacts. `W2-CONTENT-SYN-01` later resolves compatible concrete identities or records conflicts.

## 4. Story-state model

Narrative state is explicit logical state, not implicit prose.

Stable state families:

- `STATE:NARRATIVE:ORIENTATION_COMPLETE`
- `STATE:NARRATIVE:CONTEST_RECOGNIZED`
- `STATE:NARRATIVE:COMMITMENT_DECLARED`
- `STATE:NARRATIVE:CONSEQUENCE_OBSERVED`
- `STATE:NARRATIVE:RECKONING_OPEN`
- `STATE:NARRATIVE:AFTERMATH_ENTERED`

A state means only the named structural milestone. It does not imply a final location, faction, character, or outcome.

### 4.1 Arc roles

The candidate uses four bounded arc roles:

| Arc role | Structural purpose | Required exit evidence |
|---|---|---|
| `ARC_ROLE:ORIENTATION` | teach that information, relationships, world state, and choices are connected | at least two legal routes expose the core tension; no required social/narrative gate is silently foundational |
| `ARC_ROLE:ENTANGLEMENT` | let player projects intersect with competing perspectives and consequences | player has observable route choice and knows material trade-offs before commitment |
| `ARC_ROLE:RECKONING` | expose conflict between earlier commitments, evidence, and affected parties | branch-impact obligations are evaluated; contradictory claims remain typed as claims |
| `ARC_ROLE:AFTERMATH` | show durable consequences and provide continued goals after major choice | every high-impact branch retains alternative goals/content or an explicit reviewed exception |

The architecture does not require every player to complete all arc roles. Individual quest families classify their progression gates explicitly.

### 4.2 Beat roles

Reusable beat roles are semantic functions, not authored scenes:

- `BEAT_ROLE:INVITATION`
- `BEAT_ROLE:DISCOVERY`
- `BEAT_ROLE:CONTRADICTION`
- `BEAT_ROLE:COMMITMENT`
- `BEAT_ROLE:COST_REVEAL`
- `BEAT_ROLE:CONSEQUENCE`
- `BEAT_ROLE:RECONSIDERATION`
- `BEAT_ROLE:AFTERMATH`

No beat role is a mandatory linear ordering by itself. Quest templates state legal transition edges.

## 5. Knowledge, belief, secret, and reveal contract

Narrative content preserves separate authority layers:

- `OBJECTIVE_FACT_REF` — only a reviewed/fan-in world authority may bind this to candidate objective truth;
- `CLAIM_REF` — a proposition asserted by a perspective-holder; may be true, false, disputed, or unresolved;
- `KNOWLEDGE_REF` — what a character/system actor is entitled to know;
- `PLAYER_DISCOVERY_REF` — what the player-facing experience has revealed;
- `SECRET_REF` — information with an explicit holder/exposure policy;
- `BRANCH_FACT_REF` — a fact true only under a branch predicate.

A reveal may expose a claim without proving it. A character may repeat a false belief without changing objective state. `knowledge` or exposure metadata can never promote a claim to objective fact.

Every narrative assertion-producing content brief must bind:

- perspective-holder role;
- asserted fact/claim refs;
- required knowledge refs;
- forbidden secret refs;
- required branch/world-state predicates;
- allowed invention scope;
- consequence/effect refs if the assertion itself causes state change.

Generated prose remains candidate presentation and cannot mutate canonical facts, gates, relationships, rewards, or world state.

## 6. Discovery architecture

Discovery is modeled as a graph of sources, assertions, and player-visible evidence.

Candidate discovery roles:

- `DISC_ROLE:PUBLIC_RECORD` — broadly accessible source, not necessarily truthful;
- `DISC_ROLE:WITNESS_ACCOUNT` — perspective-bound account;
- `DISC_ROLE:MATERIAL_TRACE` — environment/object evidence that can support or contradict claims;
- `DISC_ROLE:PRIVATE_TESTIMONY` — holder-gated claim;
- `DISC_ROLE:PLAYER_OBSERVATION` — observed state/effect;
- `DISC_ROLE:COMPARATIVE_INFERENCE` — player-facing conclusion enabled by multiple evidence refs.

Critical rules:

1. exposure and truth are orthogonal;
2. optional mysteries may remain unresolved;
3. any foundational gameplay requirement cannot depend on an unknowable arbitrary reveal;
4. an important irreversible choice must surface enough material information to understand the choice class and foreseeable costs, without requiring exhaustive omniscience;
5. chronology-sensitive reveals bind event/order constraints rather than relying on list order.

## 7. Quest grammar

A quest definition is a versioned state machine with a typed objective graph.

Minimum fields:

- stable `quest_template_id` and version;
- `quest_role` and optional arc/beat role refs;
- availability predicates, forbidden predicates, discovery sources;
- `ProgressionGateContract` refs;
- typed objectives with completion predicates;
- objective dependency edges;
- branch choices and branch predicates;
- success, failure, abandonment, expiry, retry, and recovery semantics;
- typed effects and consequence refs;
- timed-window refs, where used;
- provisional world/social/character role refs;
- observability/player-feedback obligations;
- `GameSemanticGraph` mapping obligations;
- evidence/reopen refs.

### 7.1 Lifecycle

Availability is distinct from acceptance and activation:

`UNAVAILABLE -> AVAILABLE -> ACCEPTED -> ACTIVE -> {SUCCEEDED | FAILED_RECOVERABLE | FAILED_TERMINAL | ABANDONED}`

A template may add explicit suspended/deferred substates, but no hidden state transition may carry gameplay-authoritative meaning only in prose.

### 7.2 Objective graph rules

- required objective dependencies must be acyclic, unless a declared bounded loop has a monotonic progress measure and legal exit;
- optional objectives cannot become hidden prerequisites for required completion;
- mutually exclusive branch objectives cannot both be required;
- each required objective must have at least one satisfiable route under every supported state in which the quest can become active;
- required characters/locations use provisional roles and need fallback/substitution semantics until fan-in resolves concrete availability;
- completion predicates and effects use registered typed semantics or a custom-handler contract exposing equivalent validation/evidence hooks.

### 7.3 Failure and recovery

Every template must declare:

- whether failure is possible;
- whether it is recoverable;
- retry reset semantics;
- state preserved across retry;
- abandon/reaccept semantics;
- alternate route or compensation when an actor/location/resource becomes unavailable;
- whether expiry is intended and, if so, how the legal completion window is proven.

A quest cannot become a permanent soft lock simply because a presentation beat, NPC, or location is unavailable.

## 8. Representative structural quest roles

These are grammar fixtures, not a final quest catalog.

### `QROLE:INVESTIGATE_CONFLICTING_ACCOUNTS`

Purpose: compare at least two claims and one independent evidence source before choosing whether to act.

- no required conclusion about which claimant is truthful;
- success can be “sufficiently informed” rather than “discover one canonical answer”;
- supports knowledge-route substitutions;
- exposes `CLAIM_REF` vs `OBJECTIVE_FACT_REF` separation.

### `QROLE:NEGOTIATE_SHARED_USE`

Purpose: resolve or defer a contested-use problem through multiple route kinds.

- possible routes include service, trade, relationship, quest, knowledge, or substitute;
- no route is assumed foundational;
- consequences can alter access/relationships/availability but remain explicitly scoped.

### `QROLE:COMMIT_TO_PROJECT`

Purpose: make an informed project/branch commitment with explicit costs, affected goals, and reversibility.

- branch-exclusive only when the branch truly excludes goals/content;
- irreversible versions require `BranchImpactEvidence`;
- later reconsideration is either a declared recovery route or explicitly unavailable and signaled.

### `QROLE:REPAIR_OR_REFRAME`

Purpose: respond after a prior consequence rather than resetting the world.

- may repair material damage, repair a relationship, compensate, disclose evidence, or accept a changed route;
- recovery does not erase important history records;
- restored access does not imply restored trust or identical world state.

### `QROLE:AFTERMATH_AMBITION`

Purpose: provide medium/long-horizon goals after a major branch.

- must consume branch-specific consequences;
- must not collapse to a cosmetic epilogue;
- ensures high-impact choices preserve meaningful continued play.

## 9. Progression-gate policy

This producer creates **no `FOUNDATIONAL` narrative gate**. All candidate narrative gates below are scoped as `OPTIONAL`, `SPECIALIZATION`, or `BRANCH_EXCLUSIVE`. Any later promotion to `FOUNDATIONAL` requires explicit reviewed common-foundation authority and route/substitution evidence.

Candidate gates:

- `GATE:NARR:DEEP_HISTORY_INQUIRY` — `OPTIONAL`
- `GATE:NARR:TRUSTED_TESTIMONY_ACCESS` — `SPECIALIZATION`
- `GATE:NARR:PUBLIC_COMMITMENT` — `BRANCH_EXCLUSIVE`
- `GATE:NARR:RECONCILIATION_ROUTE` — `OPTIONAL`
- `GATE:NARR:AFTERMATH_LEADERSHIP` — `SPECIALIZATION`

Every gate declares multiple routes where appropriate, visibility/discovery, miss/failure/recovery, branch scope, and later evidence obligations.

Narrative/social participation may create unique goals, services, information, relationships, and consequences; it does not silently become a universal prerequisite for unrelated foundational progression.

## 10. Time-policy binding

This packet does not invent exact day, season, timer, or pause values.

Any timed quest/window binds a `GameTimePolicy` version at fan-in/evidence time and declares:

- window ID;
- `clock_domain: SIMULATION | CALENDAR | REAL_EXTERNAL`;
- policy context;
- pause/scale semantics delegated to the bound policy;
- accessibility timing alternatives;
- opening/closing predicates;
- retry/recovery behavior;
- evidence scenario refs.

Ambient wall time is never an implicit gameplay input. `REAL_EXTERNAL` requires explicit authoritative design and cannot appear merely because a UI timer exists.

Representative fixtures use only `SIMULATION` or `CALENDAR` and leave exact duration unset.

## 11. Consequence contract

Material consequences are explicit state transitions.

`ConsequenceContract` fields include:

- stable consequence ID;
- cause/trigger ref;
- affected domain/state refs;
- preconditions;
- effect operations;
- reversibility class;
- reversal/precondition route if any;
- persistence/migration obligation;
- observability/player-feedback obligation;
- downstream content/quest dependencies;
- branch-impact ref when high-impact;
- compensation/alternative goal refs where restoration is impossible.

Reversibility classes:

- `REVERSIBLE` — a legal state transition can restore the affected capability/state, while history may remain;
- `CONDITIONALLY_REVERSIBLE` — restoration requires explicit predicates/cost/route;
- `IRREVERSIBLE` — state cannot be restored in the supported branch; signaling and `BranchImpactEvidence` are mandatory.

No narrative text itself performs the transition.

## 12. Branch-impact sufficiency

High-impact choices must be evaluated as content/trajectory changes, not merely flag changes.

Each irreversible or branch-exclusive decision records:

- affected goals/lifestyles;
- unavailable content;
- alternative goals/content;
- recovery or compensation;
- signaling/player-surface obligation;
- long-horizon scenario refs;
- minimum aftermath content family obligations.

Candidate branch families:

### `BRANCH_FAMILY:PUBLIC_ALIGNMENT`

A visible commitment changes some relationships/access, but must preserve at least one non-aligned route to shared foundational gameplay and at least one meaningful continued narrative goal.

### `BRANCH_FAMILY:COMMONS_TRANSFORMATION`

A player-backed transformation may be irreversible at the world-state level. It must create distinct downstream projects/maintenance/consequences rather than only remove content.

### `BRANCH_FAMILY:DISCLOSURE_OR_WITHHOLDING`

Publishing or withholding sensitive information can alter knowledge/relationships. Withholding cannot erase objective evidence; disclosure cannot magically make a claim true.

No branch may hollow out the sandbox without an explicit reviewed exception backed by long-horizon evidence.

## 13. GameSemanticGraph interface

This candidate does not assign a canonical `graph_version`. At fan-in, the resolved narrative packet must map:

- narrative goals;
- quest verbs/objectives;
- knowledge/discovery nodes;
- narrative gates;
- relationship/world role interfaces;
- consequence nodes;
- content families;
- alternative/recovery routes.

Required semantic edge types include `REQUIRES`, `ENABLES`, `REVEALS`, `SUBSTITUTES`, `CONFLICTS`, and `CHANGES`.

Every edge used as evidence needs a `semantic_value_ref` explaining what decision, route, or consequence changes. Coverage must report routes/branches/trajectories, not raw object/edge counts.

## 14. Structural solvability and anti-soft-lock obligations

A later validator/search must be able to establish, for each exact resolved quest:

1. all refs exist and types match;
2. required objective graph has no accidental cycle;
3. every active required predicate can become true through a supported route;
4. mutually exclusive branches are never simultaneously required;
5. role availability has substitution/fallback or explicit legal failure/recovery;
6. timed windows have a legal completion window under the bound `GameTimePolicy`;
7. success/failure/abandon/retry transitions terminate or progress monotonically;
8. rewards/effects reference valid content/state;
9. irreversible consequences have branch-impact records;
10. branch-specific facts do not leak across incompatible branches.

The producer packet defines these obligations; it does not claim the WSN experiments have run.

## 15. Content-generation boundary

Quest/dialogue/event/lore prose is presentation content bound to typed briefs.

A brief includes allowed/required facts or claims, forbidden secrets, perspective/knowledge scope, branch context, effect refs, invention scope, provenance/originality policy, and review requirements.

Generation classes follow the Wave-1 authority boundary:

- build-time generated content remains candidate until normal review;
- runtime presentation-only content cannot mutate gameplay-authoritative state;
- any later runtime canonical effect must occur through a validated command/effect contract and persist the accepted outcome.

Outage or grounding failure uses a declared fallback/inconclusive route; it never invents emergency canon.

## 16. Evidence debt and review attacks

All `WSN-E1..WSN-E9` remain `UNRUN_REQUIRED_EVIDENCE`. This packet neither executes nor passes them.

Relevant future attacks include:

- `WSN-E1` contradiction/chronology/branch injection;
- `WSN-E2` knowledge and secret leakage;
- `WSN-E3` quest solvability and injected soft locks/cycles;
- `WSN-E5` reversible/irreversible branch persistence;
- `WSN-E6` generated-content grounding;
- `WSN-E7` semantic sameness;
- `WSN-E8` long-horizon composition/availability;
- `WSN-E9` critic disagreement calibration.

The required #369 root review additionally attacks:

- fake choice where branches reconverge without distinct consequence value;
- hidden foundational narrative/social gates;
- chronology or secret leakage through availability/discovery;
- hollow irreversible branches;
- sibling dependency leakage;
- scope/canon/authority inflation.

## 17. Assumptions, uncertainty, and reopen conditions

Assumptions requiring later evidence/fan-in:

- the five quest-role fixtures cover enough structural variety to be useful without becoming a final catalog;
- provisional sibling roles can resolve without forcing one sibling candidate to rewrite another;
- branch-impact obligations can keep major choices meaningful at tractable content cost;
- timed quests can be expressive while all exact timing remains under shared `GameTimePolicy`;
- sufficient narrative goals can remain optional/specialized while still feeling first-class.

Reopen this architecture if:

- fan-in cannot resolve provisional roles without hidden mutable dependencies;
- representative quests require cycles/custom handlers the grammar cannot validate;
- soft-lock search misses common failure modes;
- optional/specialized narrative gates compose into de facto foundational progression;
- knowledge/claim separation cannot represent unreliable/disputed histories;
- branch-impact alternatives are too shallow to support continued play;
- time-policy binding cannot model intended windows without anxiety/inaccessibility;
- persistence/migration cannot preserve consequence state;
- structural validation pushes authored content toward blandness or fake choice;
- originality/reference or generated-content controls prove insufficient.

## 18. Producer self-review

Self-review target before terminal status:

- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0

Checks:

- owned paths only;
- no sibling artifact consumed;
- no engine/runtime syntax selected;
- no `FOUNDATIONAL` narrative gate authored;
- quest lifecycle/failure/retry/recovery explicit;
- knowledge/truth/exposure distinct;
- timed windows bind policy rather than values;
- irreversible branches bind branch-impact obligations;
- WSN evidence remains unrun;
- no integration, implementation-readiness, verification, decision, release, or canonical authority claimed.

## 19. Downstream route

If fresh required review returns clean for this exact root, the packet may satisfy the narrative-root review prerequisite for later `W2-CONTENT-SYN-01` fan-in only.

Concrete final names, locations, factions, characters, questlines, dialogue, chronology, and vertical-slice authorship remain downstream. Fan-in must reconcile this root with independently reviewed sibling roots rather than treating this packet as canonical truth.
