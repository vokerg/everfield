# W2-CONTENT-SOCIAL-01 — factions, institutions, and social-conflict topology candidate

**Issue:** #367  
**State:** PRODUCER CANDIDATE / NONCANONICAL  
**Conflict domain:** `CONTENT_SOCIAL`  
**Engine dependency:** none for this bounded planning candidate  
**Required next gate:** fresh independent/degraded-independent content-root review before any fan-in

## 1. Authority and exact input binding

This packet is a bounded content-planning candidate. It does not canonize any faction, institution, community, relationship, plot fact, world fact, or branch outcome.

Exact inputs frozen for this producer episode:

- current main / branch base at claim: `dd84256de5033cb9873eb10589847be1d403b042`;
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- canonical binding: Bootstrap Issue #6 comment `5245368879`;
- canonical activation SHA: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- owner parallel-frontier directive: Issue #84 comment `5305563203`;
- W1-DES-03 work: `d19ddc43c9e5f22c6f14e5c978c30a4e6a2f0d8b`;
- W1-SYN-GAME work: `e74e0b0c95e85f69718868eedae324a298f02f3e`;
- canonical `docs/planning/WAVE-1-FOUNDATIONS-v1.md` on the claim base;
- content compiler Issue #365 claim `5305566663`, work `fd2fb7d816cf23d60bcc54bd25c7d9a4eaae3dbb`;
- content-frontier activation review Issue #372 terminal `5305598079`, head `656930c36d90a166776485cbaf196c39a32fe97e`, disposition `CLEAN_FOR_BOUNDED_CONTENT_FRONTIER_ACTIVATION`.

The W1 social architecture requires stable typed identity, multi-dimensional relationship state, important-history preservation, explicit consequences, knowledge/secret boundaries, and structured evidence rather than prose-only truth. The canonical Wave-1 foundation additionally requires every material progression gate to use `ProgressionGateContract` semantics and prevents social/narrative gates from silently becoming foundational.

Existing `WSN-E1..WSN-E9` experiments remain separate empirical authority. This authored packet creates no experiment PASS. In particular, `WSN-E5` branch-persistence and `WSN-E8` long-horizon social/NPC simulation remain unrun evidence obligations unless exact later evidence says otherwise.

## 2. Bounded design objective

Create a social topology that can support farming/life-simulation, making/trade, discovery, community, and world consequence without turning one faction meter into the game's mandatory progression spine.

The candidate uses six social actors with overlapping legitimate interests:

1. **The Commons Assembly** — civic coordination and shared infrastructure.
2. **The Fieldward Cooperative** — cultivation, shared stock, and stewardship.
3. **The Makers' Exchange** — repair, fabrication, trade, and standards.
4. **The Hearth Archive** — records, memory, testimony, and sensitive knowledge stewardship.
5. **The Waykeepers' League** — routes, access, travel support, and field safety.
6. **The Neighbor Network** — informal mutual aid, care, and reciprocal community support.

Names and details above are candidate content, not world canon. Their value is the topology: no actor is a universal moral authority, every actor controls only bounded services/information/opportunities, and conflict comes from competing legitimate priorities rather than a required hero/villain partition.

## 3. Cross-root independence

This root does not read or require mutable outputs from the world, character, or narrative sibling roots.

It uses provisional typed interfaces instead:

- `WORLD_ROLE:HUB_COMMUNITY` — a primary shared settlement/community surface;
- `WORLD_ROLE:CULTIVATION_ZONE` — a place where cultivation/stewardship concerns can occur;
- `WORLD_ROLE:COMMON_RESOURCE` — a shared resource or infrastructure subject to allocation;
- `WORLD_ROLE:TRANSIT_EDGE` — a route/access surface;
- `WORLD_ROLE:SENSITIVE_SITE` — a place where disclosure/access may have consequences;
- `CHAR_ROLE:FACTION_LIAISON` — a future character-facing institutional representative;
- `CHAR_ROLE:INDEPENDENT_MEDIATOR` — a future character role able to support recovery/substitution;
- `CHAR_ROLE:COMMUNITY_NEIGHBOR` — a future noninstitutional community participant;
- `NARR_ROLE:SOCIAL_DISPUTE` — a later narrative container for a social disagreement;
- `NARR_ROLE:PUBLIC_COMMITMENT` — a later narrative record of a declared social choice.

Fan-in may replace these with reviewed concrete identifiers. If any sibling root proves that an interface cannot be satisfied, that is a fan-in contradiction/reopen condition, not permission for this root to invent the sibling output.

## 4. Social invariants

The candidate is only coherent if all of these remain true:

1. **No universal faction requirement.** No faction membership or standing threshold is `FOUNDATIONAL` in this candidate.
2. **Basic life-play remains socially accessible.** Baseline food acquisition, basic making/repair, ordinary movement, and ordinary community participation cannot be permanently denied by one faction's standing.
3. **Institutional advantage is bounded.** Higher standing may unlock specialist help, priority, better information, cooperative leverage, or branch-specific content; it may not become a hidden all-purpose power score.
4. **Relationship meaning is multi-dimensional.** Trust, reliability, reciprocity, value alignment, and history are distinct. No one scalar is authoritative for all social outcomes.
5. **History survives recovery.** A repaired relationship may become functional again without erasing a broken promise, public endorsement, disclosure, rescue, or betrayal record that later content legitimately references.
6. **Consequences are explainable.** Material access/response changes cite typed causes and affected state instead of hidden prose heuristics.
7. **Negative state is recoverable unless deliberately branch-exclusive.** Ordinary social mistakes must expose a recovery route or alternative route. Irreversible exclusion requires explicit branch classification, signaling, and later branch-impact evidence.
8. **Information has scope.** Public information, institutional records, private testimony, disputed claims, and secrets are not interchangeable.
9. **No authored prose creates objective truth by itself.** Dialogue, summaries, rumors, or generated text can express beliefs or candidate presentation but cannot silently create canonical facts.
10. **No engine semantics leak into the content model.** IDs, gates, consequences, and history are logical planning concepts only.

## 5. Relationship and standing model

### 5.1 Dimensions

Faction/player and important social relationships may instantiate the following dimensions where relevant:

- `trust` — confidence that the player will not misuse vulnerability, access, or information;
- `reliability` — confidence that the player completes accepted obligations and communicates failures;
- `reciprocity` — whether contributions, aid, debts, and favors are balanced or intentionally outstanding;
- `value_alignment` — issue-specific alignment with the actor's declared priorities; disagreement does not automatically imply distrust;
- `public_standing` — the institution/community's visible willingness to endorse or vouch for the player;
- `access_state` — a derived typed state for bounded services/information, never a universal relationship score.

Not every actor needs every dimension. `access_state` must be derived from explicit predicates and history rather than summed from the other dimensions.

### 5.2 Important-history ledger

Material changes append a `SocialHistoryEvent` with:

- stable `event_id`;
- actor and target refs;
- typed cause;
- public/private/disputed visibility;
- dimension effects;
- service/information/branch effects;
- reversibility and recovery refs;
- source/authority provenance;
- optional expiry or supersession without deletion.

Current relationship dimensions are a view over history plus current state. Recovery can supersede an effect while retaining the event. This preserves meaning such as “a promise was broken and repaired” rather than collapsing it to a restored number.

### 5.3 Anti-grind rule

Repeated identical low-risk actions cannot satisfy every dimension. For example, repeated donations may improve reciprocity or public standing but cannot by themselves prove reliability under responsibility, trust with sensitive information, or alignment on a contested issue. Later `WSN-E8`/semantic evidence should attack degenerate social loops.

## 6. Candidate actors

### 6.1 `FAC-COMMONS-01` — The Commons Assembly

**Type:** civic institution / public coordination forum.

**Motivation:** maintain legitimate, legible, broadly usable shared infrastructure and settle competing claims without one specialist interest monopolizing common resources.

**Resources:** meeting/coordination authority, public notices, shared-project prioritization, bounded civic endorsements, and access to common-project opportunities. Exact buildings, geography, and legal structure are deferred to world fan-in.

**Obligations:** publish reasons for material allocations; retain dissent; provide a route for nonmember participation; avoid tying basic life-play to political loyalty.

**Pressure:** deliberative fairness can conflict with urgency, specialist expertise, or commercial throughput.

**Player-facing value:** public-work collaboration, mediation, transparent policy choices, and institutional endorsements for optional civic specialization.

### 6.2 `FAC-FIELDWARD-01` — The Fieldward Cooperative

**Type:** producer/steward cooperative.

**Motivation:** keep cultivation and resource stewardship resilient across individual setbacks while protecting long-horizon productive capacity.

**Resources:** shared stock, seasonal knowledge, cooperative labor, specialist cultivation support, and stewardship observations.

**Obligations:** maintain viable baseline participation for independent/direct play; distinguish shared-stock stewardship from ownership of all cultivation; communicate scarcity rather than silently gating foundational needs.

**Pressure:** rapid expansion or high-throughput demand can conflict with reserve capacity, ecological caution, or equitable access.

**Player-facing value:** cooperative projects, advanced shared stock, specialist cultivation knowledge, and optional stewardship influence.

### 6.3 `FAC-MAKERS-01` — The Makers' Exchange

**Type:** craft/trade/repair association.

**Motivation:** keep tools, repair capability, knowledge transfer, and exchange dependable while rewarding specialized skill and reliable commitments.

**Resources:** specialist commissions, repair expertise, work-sharing, standards, supply coordination, and trade contacts.

**Obligations:** ordinary repair/crafting access remains available outside high standing; specialist commissions cannot become the sole route to foundational capability.

**Pressure:** standardization and throughput can conflict with local adaptation, commons priorities, or Fieldward reserve constraints.

**Player-facing value:** specialist fabrication/repair, collaborative commissions, trade coordination, and optional mastery recognition.

### 6.4 `FAC-ARCHIVE-01` — The Hearth Archive

**Type:** record/memory institution.

**Motivation:** preserve durable records and testimony while distinguishing public record, private testimony, disputed claims, and material whose disclosure could cause harm.

**Resources:** records, corroboration practices, provenance, contextual research, and bounded access to sensitive testimony.

**Obligations:** never convert belief/testimony into objective fact by institutional assertion alone; document dispute/provenance; protect secrets/private testimony according to explicit scope.

**Pressure:** public transparency can conflict with privacy, trust, or the safety of a sensitive site/person/community.

**Player-facing value:** optional research, context, corroboration, disputed-claim resolution, and branch-sensitive information access.

### 6.5 `FAC-WAYKEEPERS-01` — The Waykeepers' League

**Type:** route/access and field-support association.

**Motivation:** keep movement and discovery safe enough to be sustainable without claiming ownership of exploration itself.

**Resources:** route observations, field support, maintenance coordination, expedition sponsorship, and risk communication.

**Obligations:** baseline movement/exploration cannot require membership; route closure or warning must cite a reason and alternative/recovery when practical.

**Pressure:** access/discovery incentives can conflict with stewardship limits, privacy, scarce maintenance capacity, or disclosure of sensitive locations.

**Player-facing value:** optional expedition support, route knowledge, field-service collaboration, and specialized access planning.

### 6.6 `COM-NEIGHBOR-01` — The Neighbor Network

**Type:** informal community / mutual-aid topology, intentionally not a formal faction.

**Motivation:** maintain reciprocal care and local resilience outside institutional membership.

**Resources:** time, informal knowledge, small-scale aid, introductions, recovery support, and distributed social memory.

**Obligations:** remain plural rather than becoming a single centralized authority; community memory can contain disagreement and incomplete knowledge.

**Pressure:** informal aid may be faster and more humane than formal systems but less scalable, less predictable, and more vulnerable to burnout or unequal reciprocity.

**Player-facing value:** noninstitutional social routes, recovery from ordinary standing failures, mutual-aid choices, and a meaningful community lifestyle that is not reducible to faction optimization.

## 7. Conflict/cooperation topology

The important edges are typed tensions with both cooperative and conflict potential:

| Edge | Parties | Cooperative value | Tension | Player-facing consequence surface |
|---|---|---|---|---|
| `SOC-EDGE-001` | Commons ↔ Fieldward | resilient common provisioning | public allocation vs reserve/stewardship | priority, obligations, civic support |
| `SOC-EDGE-002` | Fieldward ↔ Makers | tools and productive capacity | throughput demand vs long-horizon reserves | commission timing, shared stock, trust |
| `SOC-EDGE-003` | Makers ↔ Waykeepers | repair/logistics for route upkeep | maintenance burden vs expansion | specialist support, route projects |
| `SOC-EDGE-004` | Commons ↔ Makers | common infrastructure delivery | open access vs specialist/commercial priority | procurement/endorsement branch |
| `SOC-EDGE-005` | Commons ↔ Archive | accountable records | transparency vs privacy/confidentiality | public record/disclosure consequences |
| `SOC-EDGE-006` | Archive ↔ Waykeepers | trustworthy discovery records | documentation vs sensitive-site disclosure | information scope/access |
| `SOC-EDGE-007` | Fieldward ↔ Waykeepers | safe access to productive/stewardship areas | access expansion vs protection | route conditions, stewardship standing |
| `SOC-EDGE-008` | Neighbor ↔ Commons | recovery and local legitimacy | informal need vs procedural allocation | aid routes, civic pressure |
| `SOC-EDGE-009` | Neighbor ↔ Makers | practical repair/help exchange | reciprocity vs market valuation | aid/commission alternatives |
| `SOC-EDGE-010` | Neighbor ↔ Archive | community memory/testimony | lived memory vs evidentiary caution | disputed claims, confidentiality |

No edge declares one party universally correct. Downstream narrative can instantiate specific disputes only after reviewed fan-in supplies compatible world/character/narrative facts.

## 8. Player-facing social interfaces

### 8.1 Basic versus specialized access

**Basic access remains ungated by faction standing:** ordinary community interaction, basic repair/craft opportunity, baseline cultivation participation, baseline movement/exploration, public information, and ordinary mutual aid.

**Specialized/optional access may depend on explicit predicates:** sensitive records, advanced shared stock, specialist commissions, expedition sponsorship, civic delegation, institutional endorsement, or branch-specific coalition support.

Each denial must expose the reason class (`missing_reliability`, `unresolved_obligation`, `sensitive_information_trust`, `branch_conflict`, etc.) and either a recovery path, an alternative route, or an explicitly reviewed branch-exclusive consequence.

### 8.2 Information flow

Information is typed as:

- `PUBLIC` — freely shareable;
- `INSTITUTIONAL` — available through a bounded role/service;
- `PRIVATE` — shared by a specific actor under trust/confidentiality scope;
- `DISPUTED` — claim with provenance but no settled objective truth;
- `SECRET` — intentionally restricted; disclosure requires explicit authority/effect;
- `BRANCH_SPECIFIC` — valid only under an explicit branch state.

A faction's confidence in a claim does not upgrade it to objective world fact.

### 8.3 Social consequence vocabulary

Material social outcomes use explicit effect classes:

- dimension change (`trust`, `reliability`, `reciprocity`, `value_alignment`, `public_standing`);
- obligation created/fulfilled/defaulted/forgiven;
- bounded service access changed;
- information scope granted/revoked/disclosed;
- endorsement or public dissent recorded;
- collaboration invitation enabled/disabled;
- branch commitment recorded;
- recovery route opened/closed;
- future response modifier linked to retained history.

## 9. Progression gates

This candidate defines **zero `FOUNDATIONAL` social/faction gates**. If later fan-in makes one of these social gates necessary for a common foundational goal, that is a material design change requiring reclassification, route/substitution analysis, and review.

### `GATE-SOC-COMMONS-DELEGATION-01` — `SPECIALIZATION`

Unlocks optional civic delegation/priority-setting participation. Routes include demonstrated public-work reliability, successful mediation, or an evidence/corroboration contribution relevant to a public question. A failed obligation lowers reliability but can recover through transparent repair, restitution, or later bounded service. It cannot block ordinary community participation.

### `GATE-SOC-FIELDWARD-SHARED-STOCK-01` — `SPECIALIZATION`

Unlocks advanced/scarce cooperative stock or coordinated specialist support. Routes include reciprocity contribution, stewardship reliability, or a substitution approved under declared scarcity rules. Baseline cultivation capability and ordinary independent acquisition remain outside this gate. Recovery addresses damaged stock, unmet obligation, or scarcity rather than demanding generic favor grinding.

### `GATE-SOC-MAKERS-COMMISSION-01` — `OPTIONAL`

Unlocks specialist collaborative commissions. Routes include demonstrated craft reliability, reciprocal contribution, or a partner/reference route. Standard repair/crafting is not gated. A failed commission may require restitution or a lower-risk proof task; repeated trivial transactions cannot substitute for reliability evidence.

### `GATE-SOC-ARCHIVE-SENSITIVE-01` — `OPTIONAL`

Unlocks sensitive/private/disputed material appropriate to the player's trust and purpose. Routes may include source authorization, demonstrated confidentiality, or a narrowly scoped research need with corroboration. Public records remain public. If downstream narrative ever requires this material for common progression, it must provide a non-secret alternative or reclassify/review the gate.

### `GATE-SOC-WAYKEEPER-SPONSOR-01` — `OPTIONAL`

Unlocks expedition sponsorship, specialist route support, or scarce field resources. Basic movement/exploration remains outside the gate. Routes include route-maintenance contribution, demonstrated field reliability, or a bounded service exchange. Recovery responds to concrete safety/obligation failures.

### `GATE-SOC-COALITION-COMMITMENT-01` — `BRANCH_EXCLUSIVE`

Represents a deliberate public commitment in a high-impact social dispute. It may close a conflicting coalition's simultaneous endorsement while preserving ordinary services and recovery/alternative content. The exact goals/content lost or gained are deferred to fan-in and must later bind branch-impact evidence before an irreversible implementation decision.

## 10. Branch consequence patterns

These are social-state patterns, **not final quests or plot beats**.

### `SOC-BRANCH-COMMON-USE-01` — resilience versus throughput

A dispute over `WORLD_ROLE:COMMON_RESOURCE` can prioritize resilient reserve/public access or higher near-term productive throughput. Effects may change value alignment, obligations, project priority, and specialist support among Commons/Fieldward/Makers. No choice may remove baseline life-play. A later narrative instantiation must expose what changed, why, how long it persists, and which alternatives remain.

### `SOC-BRANCH-DISCLOSURE-01` — transparency versus confidentiality

A disputed record/testimony can be disclosed, protected, or released in a bounded/redacted form. Effects may change Archive trust, Commons public standing, Neighbor testimony willingness, and information visibility. The branch must distinguish objective fact from testimony/dispute; disclosure itself cannot make a claim true.

### `SOC-BRANCH-ACCESS-01` — route access versus stewardship

A `WORLD_ROLE:TRANSIT_EDGE` / `WORLD_ROLE:SENSITIVE_SITE` conflict can favor wider access, conditional access, or temporary protection. Effects may alter Waykeeper/Fieldward alignment and support. Basic world mobility requires an alternative; exact geography and ecological facts are sibling-owned and remain provisional.

### `SOC-BRANCH-AID-01` — institutional allocation versus reciprocal mutual aid

A disruption can be answered primarily through formal allocation, cooperative production, or distributed mutual aid. Effects test whether the Neighbor Network remains a meaningful noninstitutional trajectory while institutions still have distinct value. No route is declared globally superior or mandatory.

High-impact permanence is not granted here. If fan-in makes a branch irreversible or progression-critical, it must bind explicit branch-sufficiency/recovery evidence.

## 11. Social history examples and state interpretation

The following are typed examples, not authored story events:

- `fulfilled_public_commitment` → reliability may rise; retained history can support later endorsement;
- `broke_public_commitment` → reliability/public standing may fall; recovery does not delete the broken-promise event;
- `kept_confidentiality` → Archive/private-source trust may rise without changing value alignment;
- `unauthorized_disclosure` → trust/access may fall while public standing with another actor could rise; dimensions need not move together;
- `repaid_material_obligation` → reciprocity returns toward balance; historical debt remains queryable as resolved;
- `supported_opposed_policy` → issue-specific value alignment changes without automatically changing basic trust or service access;
- `mutual_aid_without_contract` → Neighbor reciprocity/history may change without producing institutional standing.

This explicitly prevents a single “everyone likes the player” meter from laundering conflicting social meaning.

## 12. Originality and reference-use boundary

The candidate actor names, roles, topology, gates, and branch patterns in this packet were authored as Everfield planning material from the repository's abstract design constraints. They are not intended as copies of any named external fictional faction, setting, quest, or dialogue.

Generic real-world concepts such as cooperatives, civic assemblies, craft associations, archives, route maintenance, and mutual aid are used at the level of common institutional patterns, not copied expression.

If later work uses a specific game, book, film, historical institution, image, article, or other source as a reference, it must record purpose, provenance/`ArtifactIdentity` where applicable, allowed/prohibited reuse, and originality/IP review according to the canonical foundation. External reference material cannot silently upgrade candidate content to canon.

## 13. Evidence obligations preserved

This producer creates structured candidate state that later evidence can exercise; it does not execute that evidence.

At minimum downstream evidence/review must still attack:

- contradictory faction/social facts and branch scoping (`WSN-E1` route);
- secret/private/disputed-information leakage (`WSN-E2` route);
- branch consequence persistence/migration and downstream availability (`WSN-E5` route);
- semantic repetition/degenerate repeated social actions within high-volume content (`WSN-E7`/content-semantic-sameness route as compiled downstream);
- long-horizon relationship, knowledge, availability, and schedule composition (`WSN-E8` route);
- subjective social/narrative quality with non-faked evaluator independence (`WSN-E9` route).

Exact experiment execution remains owned by the existing W2 game-evidence dependency routes. This root must not duplicate or terminalize them.

## 14. Assumptions, open questions, and reopen conditions

### Assumptions

- Six social actors are enough to demonstrate a useful topology without becoming a final faction catalog.
- Institutional and informal social routes can coexist without one being a universal progression requirement.
- The provisional world/character/narrative role interfaces can be resolved at fan-in without changing the core social invariants.
- Relationship dimensions listed here are sufficient for the bounded candidate; individual future characters may use a strict subset or add reviewed domain-specific dimensions.

### Open questions for fan-in/evidence

1. Which candidate actor names/roles remain compatible with the reviewed world root?
2. Which concrete characters, if any, embody liaison/mediator/community roles without making them single points of failure?
3. Which social disputes fit the narrative root without making one narrative route mandatory?
4. Which services are truly baseline versus specialist once economy/progression evidence is available?
5. What amount of social-state change is legible to players without turning every interaction into visible meters?
6. Which branch consequences justify permanence, and what content sufficiency is required on each side?
7. How should long-horizon simulation detect social grind, dead-end obligations, or cascading access loss?

### Reopen conditions

Reopen this root before fan-in or later decision if any of these becomes true:

- a sibling reviewed root proves a required provisional interface impossible or contradictory;
- any social/faction gate becomes necessary for a common foundational goal;
- one actor's service becomes the sole route to baseline cultivation, making, movement, knowledge, or community participation;
- downstream design requires a universal relationship scalar;
- a branch becomes irreversible/progression-critical without explicit alternatives and branch-impact evidence;
- candidate information access cannot preserve objective/belief/private/disputed/secret distinctions;
- originality/reference review finds a material external-expression similarity or rights concern;
- empirical WSN evidence materially contradicts the relationship, gate, or consequence assumptions.

## 15. Producer self-review

Self-review attacked the Issue #367 acceptance surface:

- **hidden foundational social gates:** none; all six gates are explicitly `SPECIALIZATION`, `OPTIONAL`, or `BRANCH_EXCLUSIVE`, with baseline alternatives stated;
- **relationship flattening:** no universal affection/faction scalar; dimensions and retained history are separate;
- **contradiction with immutable game contracts:** ProgressionGateContract, structured social state, branch consequence, originality, and evidence separation are preserved;
- **hidden sibling dependencies:** all cross-root references are provisional typed roles and no mutable sibling output is consumed;
- **canon inflation:** all faction names/details remain candidate content and no prose/evidence route is promoted to canonical/verified truth;
- **scope expansion:** no final geography, principal character arc, main plot, quest/dialogue catalog, engine representation, or gameplay implementation is authored;
- **WSN duplication:** evidence experiments are referenced only as unresolved downstream debt;
- **originality leakage:** no specific external fictional content is used as source material.

Producer self-review disposition: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR**.

## 16. Authority boundary and next gate

This packet may proceed only to a **fresh content-root review** of the exact producer head. A clean review may make this root eligible for later `W2-CONTENT-SYN-01` fan-in under then-current repository authority.

It does not select an engine, authorize gameplay/high-throughput implementation, establish implementation readiness, satisfy WSN experiments, create release/production authority, grant integration authority by itself, make a decision canonical, or canonize any faction/social content.