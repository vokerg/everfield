# W2 Principal Character and Relationship Candidate

**Mission:** `W2-CONTENT-CHAR-01`  
**Issue:** #368  
**State:** PRODUCER CANDIDATE / NONCANONICAL  
**Conflict domain:** `CONTENT_CHARACTER`  
**Engine dependency:** `ENGINE_NEUTRAL_NOW`  
**Required next step:** fresh independent/degraded-independent content-root review

## 1. Purpose and authority boundary

This packet proposes a bounded principal-cast and relationship architecture for later content fan-in. It defines candidate character identities, motivations, knowledge/belief/secret boundaries, relationship dimensions and history, change-arc interfaces, and typed provisional references to sibling world/faction/narrative domains.

Nothing here is canonical lore. Concrete sibling world, faction, and narrative outputs are intentionally **not consumed**. Any cross-domain reference beginning with `WORLD_ROLE:`, `FACTION_ROLE:`, or `NARRATIVE_ROLE:` is an unresolved interface contract, not a claim that the referenced place, institution, or story fact exists.

This packet does not select an engine, authorize gameplay/high-throughput implementation, establish implementation or release readiness, satisfy any WSN empirical experiment, or grant verification, integration, decision, or canonical authority.

## 2. Frozen authoritative inputs

- canonical Planning Program v1 blob `e3120ec203c4156328770aa86c12fbb7187966dc`;
- Bootstrap Issue #6 binding comment `5245368879`;
- W2 content compiler Issue #365 work `fd2fb7d816cf23d60bcc54bd25c7d9a4eaae3dbb`;
- content-frontier activation review Issue #372 terminal comment `5305598079`, head `656930c36d90a166776485cbaf196c39a32fe97e`, disposition `CLEAN_FOR_BOUNDED_CONTENT_FRONTIER_ACTIVATION`;
- W1-DES-03 exact work `d19ddc43c9e5f22c6f14e5c978c30a4e6a2f0d8b`;
- W1-SYN-GAME exact work `e74e0b0c95e85f69718868eedae324a298f02f3e`;
- canonical `docs/planning/WAVE-1-FOUNDATIONS-v1.md` as read from claim-time `main`.

The durable design constraints inherited from those inputs are:

1. gameplay-relevant truth is explicit structured state, not prose-only implication;
2. objective facts, character knowledge, beliefs, secrets, player discovery, chronology, and branch facts remain distinguishable;
3. relationships are not universally reducible to one affection scalar;
4. important relationship history remains explicit when current aggregate state would lose meaning;
5. social/narrative gates cannot silently become foundational progression gates;
6. generated/authored prose cannot silently create canonical facts;
7. engine-independent logical state is the planning authority boundary;
8. WSN evidence obligations remain separate and unpassed until their exact experiments execute.

## 3. Scope

This root owns only:

- a bounded principal-cast candidate;
- character-specific durable identity and role semantics;
- motivations, needs, conflicts, obligations, capabilities, and limitations relevant to play/narrative;
- explicit fact/knowledge/belief/secret distinctions;
- multi-dimensional relationship edges and important history;
- candidate change arcs with observable triggers, consequences, and prohibited shortcuts;
- provisional interfaces to sibling domains;
- assumptions, evidence needs, open questions, and reopen conditions.

Out of scope:

- final world geography/history;
- final faction/institution definitions;
- final main plot or quest catalog;
- full dialogue corpus;
- sibling content edits;
- engine/runtime representation;
- gameplay implementation;
- canonization by authorship.

## 4. Character model

### 4.1 Stable identity

A principal character has one stable `character_id` independent of display name, localized text, file location, role changes, relationships, or story state. Display names in this packet are candidate presentation only.

Every character record separates:

- `candidate_identity_facts`: character-root candidate facts;
- `provisional_domain_refs`: unresolved sibling interfaces;
- `motivations` and `needs`: desired outcomes versus deeper pressure;
- `obligations`: commitments that may conflict with goals;
- `capabilities` and `limitations`: play/narrative affordances without implementation assumptions;
- `knowledge_refs`, `belief_refs`, and `secret_refs`: information scope;
- `change_arc_refs`: typed candidate arcs.

### 4.2 Fact authority

Character-root candidate facts are not world canon. The machine packet uses:

- `CHARACTER_CANDIDATE_FACT` — authored claim within this noncanonical character proposal;
- `BELIEF` — a claim held by a character and not promoted to objective truth;
- `SECRET` — a candidate fact whose access is explicitly restricted;
- `UNKNOWN` — intentionally unresolved;
- `PROVISIONAL_INTERFACE` — a typed dependency contract owned by a sibling domain later.

No `BELIEF`, `SECRET`, or `PROVISIONAL_INTERFACE` record may be interpreted as an objective world fact without fan-in review and whatever later canonicalization authority applies.

## 5. Bounded principal-cast candidate

The cast is deliberately small enough to reason about as a connected system while broad enough to exercise trust, obligation, rivalry, knowledge asymmetry, and change.

### 5.1 `CHAR:anwen_rell` — keeper / continuity advocate

**Candidate presentation:** Anwen Rell.  
**Role:** a person who maintains records, practices, or shared memory for a local community interface.

**Motivations**
- keep consequential knowledge legible rather than dependent on rumor or status;
- preserve continuity through disruption;
- be trusted for judgment rather than merely used as a repository.

**Needs / tension**
- must learn to distinguish stewardship from control;
- risks withholding uncertain information because premature disclosure can cause harm;
- values process and traceability, which can conflict with urgent action.

**Capabilities**
- organizes conflicting testimony;
- notices provenance/chronology gaps;
- can teach or expose information when access conditions are satisfied.

**Limitations**
- not a universal truth oracle;
- may overvalue records relative to lived context;
- cannot know sibling world facts unless explicit knowledge references grant them.

**Provisional interfaces**
- `WORLD_ROLE:community_archive_or_memory_site`;
- `FACTION_ROLE:local_stewardship_body`;
- `NARRATIVE_ROLE:contested_record_or_legacy_thread`.

### 5.2 `CHAR:jori_marek` — maker / practical systems advocate

**Candidate presentation:** Jori Marek.  
**Role:** a practical maker, repairer, or systems-minded craft specialist.

**Motivations**
- make fragile arrangements repairable and understandable;
- earn autonomy through demonstrated usefulness;
- resist obligations that become permanent entitlement to their labor.

**Needs / tension**
- must learn that refusing dependence can become refusal of mutual aid;
- judges claims by concrete consequences and may discount symbolic/social harm.

**Capabilities**
- diagnoses material/process failure;
- teaches practical skills;
- creates alternate routes around some capability bottlenecks without erasing social or knowledge gates.

**Limitations**
- cannot substitute technical competence for every progression route;
- impatience with ceremony can damage trust even when the underlying diagnosis is correct.

**Provisional interfaces**
- `WORLD_ROLE:shared_worksite_or_infrastructure`;
- `FACTION_ROLE:craft_or_service_network`;
- `NARRATIVE_ROLE:repair_vs_replace_pressure`.

### 5.3 `CHAR:selka_vey` — coordinator / legitimacy advocate

**Candidate presentation:** Selka Vey.  
**Role:** a coordinator, steward, or administrative actor responsible for allocating limited communal attention/resources.

**Motivations**
- make decisions that remain defensible after immediate pressure passes;
- preserve legitimacy when interests conflict;
- prevent informal power from becoming invisible rule.

**Needs / tension**
- must accept that procedural fairness can still produce substantively harmful outcomes;
- is vulnerable to over-centralizing decisions under the banner of consistency.

**Capabilities**
- exposes trade-offs and obligations;
- can open or close institutional access only through typed conditions;
- can mediate but cannot automatically reconcile incompatible interests.

**Limitations**
- no social gate she influences is foundational merely because she is important;
- authority is provisional and must bind a sibling faction/institution role later.

**Provisional interfaces**
- `FACTION_ROLE:civic_coordination_body`;
- `WORLD_ROLE:shared_decision_site`;
- `NARRATIVE_ROLE:legitimacy_under_pressure`.

### 5.4 `CHAR:tomas_irel` — witness / mobility advocate

**Candidate presentation:** Tomas Irel.  
**Role:** a mobile observer, courier, guide, trader, or scout-like character whose value comes from crossing social or geographic boundaries.

**Motivations**
- retain freedom of movement;
- make information useful without becoming owned by one interest;
- expose when local certainty is really a narrow perspective.

**Needs / tension**
- must learn that perpetual mobility can become avoidance of durable responsibility;
- may carry truthful fragments that are misleading without context.

**Capabilities**
- bridges otherwise separated knowledge scopes;
- can introduce alternative routes, witnesses, or resources when sibling domains support them;
- creates opportunities for conflicting accounts to meet.

**Limitations**
- mobility does not imply omniscience;
- cannot reveal secret or future information without explicit acquisition provenance.

**Provisional interfaces**
- `WORLD_ROLE:boundary_route_or_exchange_path`;
- `FACTION_ROLE:mobile_exchange_network`;
- `NARRATIVE_ROLE:outside_testimony_or_return`.

### 5.5 `CHAR:maelin_sor` — caretaker / reciprocal-obligation advocate

**Candidate presentation:** Maelin Sor.  
**Role:** a caretaker, host, mentor, healer-adjacent, or community-support figure without assuming a specific profession or world system.

**Motivations**
- make mutual support durable rather than heroic and exceptional;
- protect people from being reduced to productivity or faction utility;
- preserve memory of who carried burdens during crises.

**Needs / tension**
- must set limits so care does not become invisible compulsory labor;
- can protect others so strongly that she delays their agency or difficult disclosure.

**Capabilities**
- surfaces hidden social costs and obligations;
- remembers relationship history that current scores cannot summarize;
- can model repair after breach without guaranteeing forgiveness.

**Limitations**
- care cannot erase consequence, bypass consent, or grant universal relationship access;
- no healing/economy mechanic is implied.

**Provisional interfaces**
- `WORLD_ROLE:shared_care_or_gathering_site`;
- `FACTION_ROLE:mutual_aid_network`;
- `NARRATIVE_ROLE:cost_of_care_and_repair`.

### 5.6 `CHAR:oren_dast` — challenger / ambition advocate

**Candidate presentation:** Oren Dast.  
**Role:** a capable rival, reformer, entrepreneur, organizer, or ambitious peer whose goals can align with the player without defaulting to friend/enemy.

**Motivations**
- prove that stagnant arrangements can be changed;
- gain enough influence to stop being dependent on gatekeepers;
- leave visible evidence that risk produced value.

**Needs / tension**
- must distinguish justified impatience from treating other people as obstacles;
- can recognize systemic failure while underestimating irreversible social cost.

**Capabilities**
- creates credible competing proposals and pressure;
- can cooperate on shared goals while contesting methods;
- provides a relationship where respect and rivalry may increase together.

**Limitations**
- not a designated antagonist;
- ambition cannot silently become a required plot/faction truth.

**Provisional interfaces**
- `FACTION_ROLE:reform_or_competing_interest`;
- `WORLD_ROLE:contested_resource_or_project_site`;
- `NARRATIVE_ROLE:ambition_and_consequence_pressure`.

## 6. Relationship architecture

### 6.1 Dimension rule

There is no universal affection score. Each relationship edge declares only dimensions that matter for that pair. Candidate dimensions are:

- `TRUST` — expectation that the other will act/represent information reliably;
- `WARMTH` — personal ease or fondness;
- `RESPECT` — valuation of competence, judgment, or integrity;
- `OBLIGATION` — unresolved debt, promise, duty, or reciprocal burden;
- `RIVALRY` — active competitive pressure that can coexist with respect/warmth;
- `CAUTION` — reason to restrict disclosure or dependence without requiring hostility.

Dimensions use qualitative candidate bands (`LOW`, `MEDIUM`, `HIGH`) in this planning root. They are not final balance values.

### 6.2 History rule

A current dimension snapshot cannot erase important causes. Material events are immutable relationship-history records with:

- stable `relationship_event_id`;
- participants;
- cause/reference;
- resulting dimension changes or flags;
- knowledge/visibility;
- whether repair is possible;
- what evidence would permit a later reversal.

Example: repayment of a debt may reduce `OBLIGATION`, but it does not delete `REL_EVT:jori_maelin_unasked_support`, which can continue to matter to future dialogue or decisions.

### 6.3 Candidate relationship edges

- `REL:anwen_selka`: high respect, medium trust, medium caution. They agree that decisions need traceability but differ on whether uncertain records should delay action.
- `REL:anwen_tomas`: medium warmth, medium trust, medium caution. Anwen values first-hand testimony but challenges Tomas when he compresses context.
- `REL:jori_oren`: high respect, high rivalry, medium trust. They can collaborate on practical change while contesting pace and acceptable risk.
- `REL:jori_maelin`: high warmth, medium obligation, medium trust. Maelin previously carried a burden Jori did not ask her to take; gratitude and discomfort coexist.
- `REL:selka_oren`: medium respect, high caution, medium rivalry. Neither relation state requires personal hostility.
- `REL:maelin_selka`: medium trust, high respect, medium caution; active disagreement concerns invisible care burdens in formal decisions.
- `REL:tomas_oren`: medium warmth, medium rivalry, low obligation. Each values freedom but differs on commitment to durable projects.
- `REL:anwen_maelin`: high trust, medium warmth, medium respect; both preserve history for different reasons.

These edges are candidate character-domain relations only. Any institutional, geographic, or plot consequence remains provisional until sibling fan-in.

## 7. Knowledge, belief, and secret controls

### 7.1 Information rule

Every consequential assertion should be traceable to one of:

- a candidate character fact;
- an acquired knowledge record;
- a belief that may be false;
- a secret with an access policy;
- a provisional sibling interface;
- an explicit unknown.

A character may say a belief as a belief; that does not turn it into objective truth.

### 7.2 Candidate asymmetries

The machine packet defines several deliberately asymmetric records to test leakage controls:

- Anwen knows the provenance weakness of a contested record but does not know the objective sibling-world truth behind it.
- Tomas believes a recurring exchange route is more resilient than local actors think; this remains belief until a world/evidence route confirms it.
- Selka privately knows she accepted a past procedural shortcut; the event is a character-root secret candidate, not a settled world event.
- Maelin knows that Jori interprets unsolicited support as obligation because Jori explicitly disclosed it; other characters do not inherit that knowledge.
- Oren believes a stalled collective project can be revived quickly; this is ambition/belief, not a guaranteed narrative outcome.

### 7.3 Leakage prohibitions

- No dialogue/content generator may infer secret access from relationship warmth alone.
- `HIGH TRUST` is not knowledge.
- Participation in the same provisional faction/world role is not knowledge.
- A future change arc does not grant advance knowledge of its trigger/outcome.
- A player-visible codex summary may not make a secret character-known.
- Fan-in must reconcile any sibling fact that would make a belief objectively true/false; this producer does not decide it.

## 8. Candidate change arcs

A change arc is a conditional character-state proposal, not a guaranteed plot beat.

### `ARC:anwen_stewardship_without_control`

- **start pressure:** Anwen protects continuity by controlling uncertain information.
- **eligible triggers:** repeated evidence that transparent uncertainty enables better joint decisions; a failed withholding decision; trusted delegation with preserved provenance.
- **observable change:** willingness to publish uncertainty/provenance and delegate custody.
- **forbidden shortcut:** relationship score threshold alone.
- **possible regression:** deliberate misuse of disclosed uncertainty.
- **provisional narrative interface:** `NARRATIVE_ROLE:contested_record_or_legacy_thread`.

### `ARC:jori_mutuality_without_capture`

- **start pressure:** Jori treats dependence as loss of autonomy.
- **eligible triggers:** reciprocal collaboration with explicit boundaries; successful help that does not create control; recognition of invisible support work.
- **observable change:** accepts bounded reliance while negotiating obligations explicitly.
- **forbidden shortcut:** repeated gifts/resources.
- **possible regression:** help used as leverage.

### `ARC:selka_legitimacy_beyond_procedure`

- **start pressure:** Selka equates defensible procedure with sufficient fairness.
- **eligible triggers:** evidence of excluded burden; a procedurally valid outcome with unacceptable consequence; transparent challenge from affected people.
- **observable change:** adds consequence/participation checks without abandoning traceability.
- **forbidden shortcut:** player persuasion with no affected-party evidence.
- **possible regression:** crisis centralization.

### `ARC:tomas_freedom_with_commitment`

- **start pressure:** Tomas values mobility partly because it avoids durable claims.
- **eligible triggers:** voluntarily carrying a commitment across boundaries; returning when departure would be easier; making provenance/context part of testimony.
- **observable change:** accepts one bounded responsibility while retaining mobility.
- **forbidden shortcut:** forced settlement or permanent route removal.
- **possible regression:** commitment becomes coercive.

### `ARC:maelin_care_with_boundaries`

- **start pressure:** Maelin silently absorbs burdens to protect others.
- **eligible triggers:** explicit consent/reciprocity practices; visible cost recognition; successful refusal that does not collapse support.
- **observable change:** asks, delegates, and refuses without treating limits as abandonment.
- **forbidden shortcut:** reward for endless caregiving.
- **possible regression:** crisis where others again assume availability.

### `ARC:oren_ambition_with_consequence`

- **start pressure:** Oren treats speed and visible results as evidence of good judgment.
- **eligible triggers:** owning a preventable downstream cost; preserving a rival's valid objection; choosing a slower reversible route when evidence warrants it.
- **observable change:** risk proposals include consequence/recovery commitments.
- **forbidden shortcut:** defeat/humiliation automatically producing moral conversion.
- **possible regression:** success without visible cost reinforces overconfidence.

## 9. Player-facing relationship semantics

The architecture supports meaningful social consequence without turning every relationship into mandatory progression.

Rules:

1. Relationship predicates can affect dialogue, information, help, services, optional opportunities, and branch-specific access only through typed conditions later.
2. Any relationship gate proposed as `FOUNDATIONAL` must be represented by a future `ProgressionGateContract` with alternative-route evidence; this root creates no foundational gate.
3. Repeated low-information actions must not mechanically satisfy every dimension.
4. Important breaches may persist as history even after warmth/trust improve.
5. Refusal, rivalry, caution, or low warmth are valid relationship states and do not imply failed play.
6. Irreversible social consequences require explicit signaling, content/goal sufficiency, and recovery/alternative analysis downstream.
7. Relationship change should expose cause/effect to the player at a level appropriate to the fiction rather than behaving as hidden score manipulation.

## 10. Sibling interface contract

This root may emit references but may not define the sibling object behind them.

### World interfaces

- `WORLD_ROLE:community_archive_or_memory_site`
- `WORLD_ROLE:shared_worksite_or_infrastructure`
- `WORLD_ROLE:shared_decision_site`
- `WORLD_ROLE:boundary_route_or_exchange_path`
- `WORLD_ROLE:shared_care_or_gathering_site`
- `WORLD_ROLE:contested_resource_or_project_site`

The world root may later map, split, reject, or leave these unresolved. Character coherence must survive that process.

### Faction/social interfaces

- `FACTION_ROLE:local_stewardship_body`
- `FACTION_ROLE:craft_or_service_network`
- `FACTION_ROLE:civic_coordination_body`
- `FACTION_ROLE:mobile_exchange_network`
- `FACTION_ROLE:mutual_aid_network`
- `FACTION_ROLE:reform_or_competing_interest`

These are role requirements, not faction definitions or memberships.

### Narrative interfaces

- `NARRATIVE_ROLE:contested_record_or_legacy_thread`
- `NARRATIVE_ROLE:repair_vs_replace_pressure`
- `NARRATIVE_ROLE:legitimacy_under_pressure`
- `NARRATIVE_ROLE:outside_testimony_or_return`
- `NARRATIVE_ROLE:cost_of_care_and_repair`
- `NARRATIVE_ROLE:ambition_and_consequence_pressure`

These are pressure/arc interface IDs, not a final plot.

## 11. Originality and reference-use boundary

The candidate was derived from repository constraints and generic character-design primitives, not from a named external franchise's characters, plot, setting, dialogue, or protected expression.

Downstream rules:

- external references, if used later, require an `OriginalityReferenceUseRecord` or successor authority;
- reference purpose must be bounded to analysis/quality comparison, not expression copying;
- names, biographies, signature relationships, catchphrases, plots, and setting-specific structures from references are not authorized imports;
- similarity concerns route to review/quarantine, not rationalization;
- provenance alone is not proof of originality.

## 12. Machine-readable integrity

`principal-characters-relationships.yaml` is the structured companion to this proposal. Its integrity rules are:

- all IDs are unique within their declared registries;
- every `character_ref` resolves to a local character ID;
- every relationship endpoint resolves locally and is not self-referential;
- every history record referenced by a relationship resolves locally;
- every knowledge/belief/secret reference resolves locally;
- every provisional sibling reference uses an allowed typed namespace and is explicitly `PROVISIONAL_INTERFACE`;
- every arc character resolves locally and every arc's sibling references remain provisional;
- no record uses `CANONICAL`, `VERIFIED_DECISION`, `IMPLEMENTATION_READY`, or empirical `PASS` authority;
- prose and YAML must agree on cast membership, relationship IDs, arc IDs, and information-authority classes.

## 13. Self-review attacks

Producer self-review attacks this packet for:

1. **character coherence:** motivations, needs, limitations, and arcs do not contradict their own records;
2. **knowledge leakage:** beliefs/secrets remain scoped and relationship dimensions never imply knowledge;
3. **relationship flattening/grind:** no universal affection scalar; important history survives current dimensions; repeated gifts are not universal progression;
4. **unexplained changes:** each arc has typed triggers, observable effects, forbidden shortcuts, and regression conditions;
5. **hidden sibling dependencies:** every sibling reference is provisional and no mutable sibling output was consumed;
6. **canon inflation:** all authored facts remain noncanonical candidate facts;
7. **originality/reference leakage:** no external franchise-specific expression is imported;
8. **scope expansion:** no final factions/world/main plot/quest catalog/dialogue corpus or implementation is authored;
9. **progression authority:** no social/relationship condition silently becomes foundational;
10. **machine integrity:** IDs/references/types agree and remain resolvable within declared scope.

Self-review result at producer completion is expected to be recorded in the terminal handoff/status. A fresh root review remains mandatory regardless of producer self-review.

## 14. Evidence debt and reopen conditions

This candidate does not pass WSN experiments. Later evidence remains required for at least:

- knowledge/secret leakage under actual dialogue/content selection;
- long-horizon relationship/social simulation;
- degenerate relationship grind/repetition;
- consistency across world/faction/narrative fan-in;
- high-impact branch/content sufficiency;
- grounded generated dialogue/content;
- subjective character coherence and quality using appropriately trusted evaluators.

Reopen this root if:

- a sibling reviewed root proves one of the provisional interfaces impossible or materially different;
- fan-in exposes contradictory character facts, chronology, knowledge, or role requirements;
- a relationship dimension cannot explain a consequential behavior without hidden state;
- a proposed arc requires a sibling plot/faction/world fact that was silently assumed;
- empirical evidence shows degenerate grind, secret leakage, incoherent change, or impossible social availability;
- originality review finds unacceptable similarity;
- stronger review isolation becomes available and trust debt should be retired.

## 15. Downstream route

A clean fresh root review may only make this exact packet eligible as a reviewed input to later `W2-CONTENT-SYN-01` fan-in. Fan-in must reconcile concrete identifiers and cross-domain facts; it must not treat this producer's names, interfaces, relationship states, or arcs as canonical merely because they are structured.

No engine choice, gameplay implementation, implementation readiness, release, verification-PASS, integration, decision, or canonical authority is granted by this candidate or its producer self-review.
