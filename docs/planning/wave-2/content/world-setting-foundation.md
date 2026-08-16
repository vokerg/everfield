# Everfield bounded world / setting foundation candidate

**Mission:** `W2-CONTENT-WORLD-01`  
**Issue:** #366  
**State:** PRODUCER CANDIDATE / NONCANONICAL / REQUIRED REVIEW PENDING  
**Conflict domain:** `CONTENT_WORLD`  
**Engine dependency:** none for this bounded planning output

## 1. Authority and frozen inputs

This packet is a candidate content definition, not canon. It is bound to:

- Planning Program v1 blob `e3120ec203c4156328770aa86c12fbb7187966dc`;
- Bootstrap Issue #6 binding comment `5245368879`;
- owner parallel-frontier directive Issue #84 comment `5305563203`;
- producer base `main@dd84256de5033cb9873eb10589847be1d403b042`;
- exact compiler Issue #365 work `fd2fb7d816cf23d60bcc54bd25c7d9a4eaae3dbb`;
- exact activation review Issue #372 terminal comment `5305598079`, head `656930c36d90a166776485cbaf196c39a32fe97e`, disposition `CLEAN_FOR_BOUNDED_CONTENT_FRONTIER_ACTIVATION`;
- immutable W1-DES-03 work `d19ddc43c9e5f22c6f14e5c978c30a4e6a2f0d8b`;
- immutable W1-SYN-GAME work `e74e0b0c95e85f69718868eedae324a298f02f3e`;
- canonical `docs/planning/WAVE-1-FOUNDATIONS-v1.md` at the producer base.

The companion `world-setting-facts.yaml` is the checkable identity/fact/chronology surface. Prose in this file cannot override that typed surface.

## 2. Candidate world promise

### 2.1 Working premise

Everfield's bounded setting candidate is a **lived-in watershed whose settlements, cultivated spaces, wild commons, routes, and inherited public works depend on one another**. The player-facing promise is not conquest of an empty frontier. It is participation in a place already carrying obligations, incomplete histories, ecological limits, and competing ideas about what deserves repair, protection, use, or release.

The core thematic proposition is **care has consequences**. Maintaining a route, restoring water access, changing a productive landscape, opening a neglected structure, or choosing not to intervene should alter other world affordances in legible ways. Improvement is therefore contextual rather than a universal meter: making one use easier may create pressure elsewhere, and preservation can be as consequential as expansion.

This premise is deliberately compatible with cultivation, gathering, making, exploration, community life, recurring schedules, quests, discovery, and long-horizon consequences without defining final mechanics, factions, characters, quests, or an engine.

### 2.2 Originality boundary

This candidate uses broad genre affordances such as rural life, cultivation, seasons, community, exploration, and restoration only as functional design vocabulary. It does **not** import another game's town layout, inherited-farm premise, characters, corporations, festivals, magical collectibles, quest lines, dialogue, landmarks, lore, names, or progression structure. Working labels below are newly authored functional labels and are replaceable at fan-in.

Reference works may later be used for complexity comparison or evaluation methodology only under the project's rights/originality rules. Similarity is not evidence of permission or originality.

## 3. Design-facing setting constraints

The world candidate should preserve these constraints unless a reviewed downstream decision explicitly reopens them:

1. **Place before backdrop.** Gameplay-relevant locations have persistent identity, access conditions, and consequences; they are not interchangeable scenery.
2. **Interdependence over isolated upgrade ladders.** At least some material world changes affect more than one location/use/community role.
3. **No universal prosperity score.** Ecological condition, access, productive capacity, safety, cultural continuity, and social use remain separable dimensions.
4. **Recoverability is explicit.** Material changes state whether they are reversible, season-bounded, costly to reverse, or intentionally irreversible.
5. **World knowledge is scoped.** Objective candidate truth, public knowledge, discovered knowledge, secret information, belief, dispute, and branch-specific truth are distinct.
6. **History constrains the present without fully explaining it.** The setting exposes observable historical traces while retaining bounded mysteries rather than authoring certainty to fill every gap.
7. **Time matters but exact calendar design is deferred.** Seasonal/periodic access and chronology are permitted; exact day lengths, season lengths, and schedule algorithms remain downstream `GameTimePolicy` work.
8. **No mandatory supernatural ontology.** Unusual observations may exist, but whether their cause is ecological, technological, social, supernatural, or mixed remains an explicit unresolved boundary until reviewed content chooses otherwise.
9. **Engine neutrality.** Logical identity and world state cannot depend on scene paths, editor objects, engine assets, or runtime-specific types.
10. **Sibling independence.** Factions, characters, and narrative consumers use provisional typed role references until the corresponding sibling roots are reviewed and reconciled.

## 4. Physical and social topology

The topology is intentionally regional, not a final map. Each node is a stable functional location identity with a replaceable working label.

| ID | Working label | World function | Candidate constraints |
|---|---|---|---|
| `LOC:SETTLEMENT-CORE` | Hearth Cluster | dense civic/service/social node | reachable from productive land and at least two commons routes; not the whole world |
| `LOC:CULTIVATION-MOSAIC` | Patchwork Fields | player/community cultivation and managed habitat | mixed-use rather than a single monoculture; water/access condition can change |
| `LOC:RIPARIAN-CORRIDOR` | Braided Watercourse | watershed connector, habitat, crossings, water use | upstream/downstream effects must remain representable |
| `LOC:COMMONS-BELT` | Open Commons | gathering, grazing/forage, recreation, shared-use tension | cannot be modeled as ownerless infinite resource |
| `LOC:UPLAND-CATCHMENT` | High Catchment | headwaters, weather exposure, remote materials/discovery | route and seasonal accessibility can vary |
| `LOC:OLD-WORKS` | Inherited Works | legacy civic/water/transport structures | function/history partly known; restoration choices may have cross-location effects |
| `LOC:EDGE-HABITAT` | Living Edge | less-managed habitat transition | ecological state and access pressure can diverge |
| `LOC:OUTER-THRESHOLD` | Outer Threshold | interface to places beyond bounded setting | proves the basin is not a sealed universe; final external regions deferred |

### 4.1 Required topology properties

- `LOC:SETTLEMENT-CORE`, `LOC:CULTIVATION-MOSAIC`, and `LOC:RIPARIAN-CORRIDOR` form the minimum daily-life triangle.
- The riparian corridor connects catchment to lower-use areas and provides a causal route for upstream/downstream consequences.
- The old works touch at least two functional zones so restoration is not an isolated dungeon-like switch.
- The outer threshold provides an explicit expansion interface without requiring a second final region now.
- No location implies ownership by a final faction or residence by a final named character.

The companion YAML defines edges and invariants mechanically.

## 5. Chronology candidate

Chronology uses relative eras and ordering anchors rather than invented calendar years.

### `ERA:PRE-WORKS` — layered landscape

The watershed and routes of movement/use existed before the inherited works. The candidate does not assert an untouched wilderness: prior human/community use may have shaped the landscape, and downstream content must not erase that possibility by default.

### `ERA:WORKS-BUILDOUT` — coordinated works period

A past period produced connected public/shared infrastructure across water, movement, storage, or land use. Exact institutions, builders, technology level, political order, and motives are not fixed by this root.

### `EVT:WORKS-FRAGMENTATION` — loss of coordinated maintenance

At some point after buildout, maintenance and shared operation became fragmented. The **fact of fragmentation** is candidate truth; a single cause is not. War, collapse, corruption, disaster, technological failure, supernatural event, or one villain are specifically not authored here.

### `ERA:PATCHWORK-PRESENT` — current adaptation

Current inhabitants use a mixture of maintained, improvised, abandoned, repurposed, and contested systems. This supports visible differences in local condition and lets restoration create tradeoffs rather than simply return the world to an objectively perfect past.

### `EVT:PLAYER-ENTRY` — provisional play-entry anchor

A play-entry event is required as a temporal interface for narrative/quest work, but its cause, player identity, property rights, family history, and exact arrival premise are **not** owned here. It remains `PROVISIONAL_INTERFACE` and may be replaced at fan-in.

## 6. Gameplay-relevant world rules

The following are world-planning rules, not implemented mechanics:

### WR-01 — Local state has causal neighbors

A material intervention may propagate only through declared causal edges. Water, route access, habitat pressure, services, and shared-use capacity should not change globally without an explicit dependency.

### WR-02 — Maintenance is a state, not a binary unlock

Shared works can be functional, degraded, adapted, unavailable, or transformed. “Repair” must state what function is restored and what new obligations or tradeoffs result.

### WR-03 — Extraction has bounded source state

Gathering/cultivation/material use cannot assume infinite narrative supply where scarcity or regeneration matters. Exact resource simulation remains downstream, but world facts must permit depletion, recovery, stewardship, substitution, or access change to be represented.

### WR-04 — Seasonal variation changes conditions, not identity

A location remains the same logical place when access, water, ecology, activity, or presentation changes seasonally. Exact seasonal timing remains deferred.

### WR-05 — Consequences are typed and observable

Important world changes declare cause, affected IDs, branch applicability, reversibility, and at least one player-observable signal. Prose-only “the valley changed” is insufficient state authority.

### WR-06 — Knowledge does not equal truth

A map, inscription, rumor, testimony, tradition, or NPC statement can be evidence or belief without becoming objective world truth. Downstream content must bind claims to the appropriate fact/knowledge scope.

### WR-07 — The old works are not automatically morally superior

Past infrastructure may be useful, harmful, locally adapted, obsolete, or misunderstood. Restoring every inherited system is not a foundational win condition.

### WR-08 — Large branches carry content cost

World-changing choices should use scoped effects where possible. Mutually exclusive permanent branches are reserved for choices whose downstream content/evidence budget can support them.

## 7. Candidate fact authority model

Every durable candidate fact uses one of these authority classes:

- `CANDIDATE_OBJECTIVE` — proposed world truth for this packet, still noncanonical project-wide;
- `CANDIDATE_CONSTRAINT` — proposed design invariant governing future content;
- `DISPUTED_IN_WORLD` — multiple in-world claims may coexist; this packet does not resolve them;
- `UNKNOWN_BY_DESIGN` — deliberately unresolved question whose answer is outside this root;
- `PROVISIONAL_INTERFACE` — typed placeholder needed by a sibling domain without freezing sibling content.

Knowledge exposure uses `PUBLIC`, `DISCOVERABLE`, `SECRET`, `SYSTEM_ONLY`, or `NOT_APPLICABLE`. A `DISPUTED_IN_WORLD` or `UNKNOWN_BY_DESIGN` record may never be promoted to objective truth merely because prose supplies a plausible answer.

## 8. Major unresolved mysteries and allowed invention boundaries

### `MYS:FRAGMENTATION-CAUSE`

**Question:** Why did coordinated operation of the inherited works fragment?  
**Allowed now:** local evidence, contradictory accounts, incomplete records, multiple contributing pressures.  
**Forbidden now:** asserting one global catastrophe, villain, faction, supernatural cause, or technological cause as truth.

### `MYS:WORKS-ORIGINAL-PURPOSE`

**Question:** Were all old works built for the functions current residents assign to them?  
**Allowed now:** evidence of repurposing, mismatched components, layered modifications.  
**Forbidden now:** a single master-builder civilization or lost-utopia answer without fan-in/review.

### `MYS:SEASONAL-ANOMALIES`

**Question:** Which unusual seasonal observations are ordinary ecology and which, if any, imply another ontology?  
**Allowed now:** repeatable unusual observations with no asserted cause.  
**Forbidden now:** canonical magic system, gods, aliens, simulation twist, or “nothing supernatural exists” conclusion.

### `MYS:OUTER-CONNECTIONS`

**Question:** What political/economic/geographic systems exist beyond the bounded watershed?  
**Allowed now:** evidence that people, goods, information, or obligations can cross `LOC:OUTER-THRESHOLD`.  
**Forbidden now:** final neighboring nations/regions, geopolitical map, or imported sibling factions.

## 9. Provisional sibling interfaces

This root exports role IDs, not concrete sibling entities:

- `ROLE:LOCAL-CIVIC-STEWARD` — any actor/institution responsible for shared civic maintenance;
- `ROLE:LAND-USE-CUSTODIAN` — any actor/institution with legitimate land-use stewardship claims;
- `ROLE:WATER-DEPENDENT-USER` — any actor/group affected by watershed allocation/condition;
- `ROLE:TRAVEL-AND-EXCHANGE-LINK` — any actor/institution connecting the basin outward;
- `ROLE:HISTORY-BEARER` — any character/institution/source preserving a partial account of the past;
- `ROLE:PLAYER-ENTRY` — narrative interface for the player role at `EVT:PLAYER-ENTRY`.

Sibling roots may map zero, one, or several concrete entities to each role. This packet cannot name who fills them.

## 10. Branch and knowledge discipline

Baseline facts apply to `BRANCH:BASELINE` unless their record says otherwise. A downstream branch may add/supersede scoped facts, but it must not mutate history silently. If a bridge is removed in one branch, for example, the location and past bridge event remain referencable while current access state changes.

Secrets are not automatically mysteries. A secret may have a defined objective answer hidden from some agents; an `UNKNOWN_BY_DESIGN` mystery has no answer in this packet. Review should reject content that conflates those states.

## 11. Evidence, assumptions, and inference

### Evidence carried from authoritative planning

- Everfield requires narrative/quest/world-state planning as a first-class design surface.
- Stable IDs, chronology, fact/knowledge separation, explicit consequences, and structural validation are required architecture properties.
- Canonical gameplay meaning is engine-independent logical state.
- Originality requires original content rather than cloned expression.
- Existing `WSN-E*` experiments remain the empirical route; this prose does not pass them.

### Candidate inferences

- A watershed gives a compact causal topology for cultivation, settlement, travel, commons use, and consequences without requiring a final large map.
- Shared inherited infrastructure provides history and restoration affordances while supporting multiple interpretations rather than a single “restore the past” thesis.
- A patchwork present creates space for long-horizon change and conflicting uses without requiring a global apocalypse.

These are design inferences, not empirical findings.

### Material assumptions

- `ASM:WORLD-01`: a bounded watershed can support sufficient gameplay/content variety before external regions are frozen.
- `ASM:WORLD-02`: players can understand cross-location consequences if observable signals and causal edges are explicit.
- `ASM:WORLD-03`: relative chronology is sufficient for this root; exact calendar mapping can remain deferred.
- `ASM:WORLD-04`: sibling roots can consume role/location IDs without requiring final names or ownership assignments.

## 12. Open questions and reopen conditions

| ID | Question / trigger | Required response |
|---|---|---|
| `OPEN:WORLD-01` | reviewed social root cannot express its conflicts without changing world topology | fan-in may revise topology; do not let social producer mutate this branch |
| `OPEN:WORLD-02` | reviewed narrative root requires a chronology relation incompatible with the partial order here | fan-in records contradiction and selects/revises with review |
| `OPEN:WORLD-03` | WSN evidence shows the topology cannot support required route/schedule/world-state scenarios | reopen affected facts/edges; prose does not overrule evidence |
| `OPEN:WORLD-04` | originality review finds substantial expressive similarity to an external work | quarantine/rewrite implicated labels, events, or structures before promotion |
| `OPEN:WORLD-05` | a concrete engine dependency is discovered | record scoped technical dependency; do not retrofit engine assumptions into world truth |
| `OPEN:WORLD-06` | product/platform scope requires representation changes | revise presentation/access constraints only as needed; preserve logical identities unless separately reviewed |
| `OPEN:WORLD-07` | fan-in chooses a supernatural ontology | resolve only mysteries explicitly authorized by that reviewed decision; do not backfill unrelated facts |

## 13. Self-review

Producer self-review against Issue #366 acceptance criteria:

- authoritative compiler/review identities frozen: **PASS**;
- stable IDs/types and authority/knowledge/branch states: **PASS**;
- chronology represented as an explicit acyclic partial order in companion YAML: **PASS**;
- topology and invariants mechanically representable: **PASS**;
- sibling references provisional and typed: **PASS**;
- originality/reference boundary explicit: **PASS**;
- material assumptions and reopen conditions explicit: **PASS**;
- engine choice/readiness/canonical authority excluded: **PASS**;
- existing WSN empirical evidence not duplicated or marked passed: **PASS**.

Unresolved producer-scope findings: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR**.

This self-review is not the required fresh content-root review. The packet is not eligible for fan-in until that review independently/degraded-independently attacks world consistency, chronology, fact authority, hidden sibling dependency, canon inflation, originality leakage, and scope.