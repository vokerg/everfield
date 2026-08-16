# Everfield bounded world / setting foundation remediation candidate

**Mission:** `W2-CONTENT-WORLD-REM-01`  
**Issue:** #382  
**State:** REMEDIATION CANDIDATE / NONCANONICAL / REQUIRED FRESH REVIEW PENDING  
**Conflict domain:** `CONTENT_WORLD`  
**Engine dependency:** none for this bounded planning output

## 1. Authority, predecessor, and remediation scope

This packet is a fresh successor candidate to the immutable Issue #366 world/setting producer. It is not canon and it does not rewrite producer or review history. It is bound to:

- Planning Program v1 blob `e3120ec203c4156328770aa86c12fbb7187966dc`;
- Bootstrap Issue #6 binding comment `5245368879`;
- canonical activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- remediation base `main@79f5bd62f7d03ecd954e94a485b0734bd80f1b86`;
- compiler Issue #365 work `fd2fb7d816cf23d60bcc54bd25c7d9a4eaae3dbb`;
- clean activation review Issue #372 terminal comment `5305598079`, head `656930c36d90a166776485cbaf196c39a32fe97e`;
- immutable producer Issue #366 claim `5305649840`, terminal `5305661660`, work `8dc85721e446727f4b2eb59b0c35bd98edb53f20`, head `6f77a245e4905d33448f6dc7e0d898f6e4db3d43`, draft PR #377;
- immutable required review Issue #378 claim `5305668671`, terminal `5305684626`, work/head `0b04440221a63e3906cf24991c846116e68f0cca`, disposition `CHANGES_NEEDED`, review PR #381;
- noncanonical review-provenance squash publication `79f5bd62f7d03ecd954e94a485b0734bd80f1b86`;
- immutable W1-DES-03 work `d19ddc43c9e5f22c6f14e5c978c30a4e6a2f0d8b`;
- immutable W1-SYN-GAME work `e74e0b0c95e85f69718868eedae324a298f02f3e`.

The exact remediation findings are:

- `W2-CONTENT-WORLD-REV-M01`: belief/in-world claim state was not representable independently from objective/disputed fact authority and knowledge exposure;
- `W2-CONTENT-WORLD-REV-M02`: the machine chronology did not mechanically encode the three-era ordering or event containment claimed by the prose.

All other Issue #378 pass findings are preserved as constraints on this successor. The companion `world-setting-facts.yaml` remains the checkable identity/fact/claim/chronology surface. Prose cannot override that typed surface.

## 2. Candidate world promise

Everfield remains a lived-in watershed whose settlements, cultivated spaces, wild commons, routes, habitat, and inherited public works depend on one another. The player-facing promise is participation in a place already carrying obligations, incomplete histories, ecological limits, and competing ideas about what deserves repair, protection, use, restraint, or release.

The thematic proposition remains **care has consequences**. Improvement is contextual rather than a universal meter: making one use easier may create pressure elsewhere, and preservation can be as consequential as expansion. This remains compatible with cultivation, gathering, making, exploration, community life, recurring schedules, quests, discovery, and long-horizon consequences without defining final mechanics, factions, characters, quests, or an engine.

### Originality boundary

This candidate uses broad genre affordances only as functional design vocabulary. It does not import another work's names, characters, locations, town layout, quest lines, dialogue, lore, landmarks, or progression expression. Working labels remain replaceable and noncanonical.

## 3. Preserved design-facing constraints

1. **Place before backdrop.** Gameplay-relevant locations have persistent logical identity, access conditions, and consequences.
2. **Interdependence over isolated upgrade ladders.** Material world changes may affect multiple locations or uses only through declared dependencies.
3. **No universal prosperity score.** Ecological condition, access, productive capacity, safety, cultural continuity, and social use remain separable dimensions.
4. **Recoverability is explicit.** Material changes state whether they are reversible, season-bounded, costly to reverse, or intentionally irreversible if separately authorized.
5. **Truth, claims, and exposure are separate.** Candidate objective truth, design constraint, deliberately unknown truth, in-world claim/belief, dispute, exposure/knowledge, and branch scope are distinct dimensions.
6. **History constrains the present without fully explaining it.** Observable traces may exist while bounded mysteries remain unresolved.
7. **Time matters but exact calendar design is deferred.** Relative era order and event containment are explicit; exact dates, day lengths, season lengths, and schedule algorithms remain downstream `GameTimePolicy` work.
8. **No mandatory supernatural ontology.** Unusual observations may exist without fixing their cause.
9. **Engine neutrality.** Logical identity and world state do not depend on scenes, assets, editor objects, components, or runtime-specific types.
10. **Sibling independence.** Factions, characters, and narrative consumers use provisional typed role references until sibling roots are reviewed and reconciled.

## 4. Physical and social topology

The regional topology and its functional identities are unchanged from the reviewed producer packet:

| ID | Working label | World function | Candidate constraints |
|---|---|---|---|
| `LOC:SETTLEMENT-CORE` | Hearth Cluster | dense civic/service/social node | reachable from productive land and at least two commons routes; not the whole world |
| `LOC:CULTIVATION-MOSAIC` | Patchwork Fields | player/community cultivation and managed habitat | mixed-use; water/access condition can change |
| `LOC:RIPARIAN-CORRIDOR` | Braided Watercourse | watershed connector, habitat, crossings, water use | upstream/downstream effects remain representable |
| `LOC:COMMONS-BELT` | Open Commons | gathering, forage/grazing, recreation, shared-use tension | not an ownerless infinite resource |
| `LOC:UPLAND-CATCHMENT` | High Catchment | headwaters, weather exposure, remote materials/discovery | route and seasonal accessibility can vary |
| `LOC:OLD-WORKS` | Inherited Works | legacy civic/water/transport structures | history partly known; restoration may affect multiple zones |
| `LOC:EDGE-HABITAT` | Living Edge | less-managed habitat transition | ecological state and access pressure can diverge |
| `LOC:OUTER-THRESHOLD` | Outer Threshold | interface to places beyond bounded setting | external regions remain deferred |

Required properties remain: the core/cultivation/riparian daily-life triangle; a directed catchment-to-riparian causal path; old works touching multiple functional zones; an explicit outer expansion interface; and no final faction ownership or named-character residence implied by a location.

## 5. Remediated relative chronology

Chronology remains relative and date-free, but it is no longer an underconstrained prose sequence. The companion YAML now gives every declared era a unique `order_index`, gives the era graph explicit `era_precedes` relations, gives every event an exact declared `era`, and records event-level precedence separately.

The mechanically required era sequence is:

1. `ERA:PRE-WORKS` - layered landscape and prior community use before coordinated inherited works;
2. `ERA:WORKS-BUILDOUT` - period in which connected shared infrastructure was established or substantially coordinated;
3. `ERA:PATCHWORK-PRESENT` - current period of maintained, improvised, repurposed, abandoned, and contested systems.

The event sequence remains:

`EVT:WORKS-BUILDOUT` -> `EVT:WORKS-FRAGMENTATION` -> `EVT:PATCHWORK-PRESENT-START` -> `EVT:PLAYER-ENTRY`.

`EVT:WORKS-BUILDOUT` and `EVT:WORKS-FRAGMENTATION` are contained in `ERA:WORKS-BUILDOUT`. `EVT:PATCHWORK-PRESENT-START` is the start boundary for `ERA:PATCHWORK-PRESENT`; `EVT:PLAYER-ENTRY` is contained later in that same era. The checkable invariants require every event's era to resolve, all era indices to be unique and contiguous, every declared adjacent era pair to be ordered, and event precedence never to move backward across era order.

The fact that coordinated maintenance fragmented remains candidate truth. A single cause remains deliberately unresolved. The play-entry cause, player identity, property rights, family history, and exact arrival premise remain `PROVISIONAL_INTERFACE` concerns outside this root.

## 6. Gameplay-relevant world rules

The preserved world-planning rules remain non-implementation constraints:

- `WR-01`: material effects propagate only through declared causal/state dependencies.
- `WR-02`: shared works use multi-state condition/function, not a universal repaired boolean.
- `WR-03`: resource-relevant state can represent bounded use, regeneration, stewardship, substitution, or access change where material.
- `WR-04`: seasonal condition changes do not change stable logical location identity.
- `WR-05`: important consequences bind cause, affected IDs, branch scope, reversibility, and observable signal.
- `WR-06`: in-world claims and generated prose do not become objective truth without a separate validated fact-authority change.
- `WR-07`: restoring inherited works is not intrinsically or universally the preferred outcome.
- `WR-08`: permanent mutually exclusive world branches require explicit downstream content/evidence support.

## 7. Remediated fact, claim, belief, and knowledge model

### 7.1 Objective/design authority

Durable world records continue to use these fact authority classes:

- `CANDIDATE_OBJECTIVE` - proposed world truth for this packet, still noncanonical project-wide;
- `CANDIDATE_CONSTRAINT` - proposed design invariant;
- `DISPUTED_IN_WORLD` - fact-level state intentionally marked as disputed rather than resolved;
- `UNKNOWN_BY_DESIGN` - deliberately unresolved truth outside this root;
- `PROVISIONAL_INTERFACE` - typed sibling/downstream placeholder.

### 7.2 In-world proposition and claim layer

In-world speech, testimony, rumor, tradition, map annotations, inscriptions, and beliefs use a separate typed layer. A proposition has a stable `PROP:*` identity and describes what could be asserted. An in-world claim has a stable `CLM:*` identity, references exactly one proposition, carries a provisional holder/source role plus a `perspective_key`, records a stance, exposure/knowledge state, branch scope, and a truth relation.

The claim authority is always `IN_WORLD_CLAIM_ONLY`. It is not one of the objective fact authority classes. The same holder role may expose several perspective keys without binding a final character or faction.

The remediation includes two deliberately contradictory provisional accounts of the fragmentation cause. They are allowed by the existing mystery boundary and exist to prove the representation can carry disagreement without promoting either account to truth. Both remain `UNRESOLVED_AGAINST_WORLD_FACT`; neither edits `WF:FRAGMENTATION-CAUSE`.

### 7.3 Exposure is not truth

Knowledge exposure remains `PUBLIC`, `DISCOVERABLE`, `SECRET`, `SYSTEM_ONLY`, or `NOT_APPLICABLE`. Exposure answers who may encounter a record; it does not answer whether a proposition is true. A public false claim, a secret objective fact, and an undisputed but unresolved belief are structurally representable without overloading one field.

### 7.4 Fail-closed promotion rule

`INV:CLAIM-NO-FACT-PROMOTION` requires every `in_world_claims[]` record to remain `IN_WORLD_CLAIM_ONLY` and forbids a claim from creating or mutating a `CANDIDATE_OBJECTIVE` fact by its own presence. Any later truth promotion requires a separate `facts[]` record or reviewed successor edit with ordinary fact authority. `INV:CLAIM-REFERENCES-RESOLVE` also requires claim, proposition, holder role, branch, and exposure references to resolve within the declared world-interface vocabulary.

This closes Issue #378 finding `W2-CONTENT-WORLD-REV-M01` without creating a final character belief system.

## 8. Major unresolved mysteries and invention boundaries

The producer mysteries remain unchanged:

- `MYS:FRAGMENTATION-CAUSE`: local evidence, incomplete records, conflicting accounts, and multiple pressures are allowed; a single global catastrophe, villain/faction, supernatural cause, or technological cause may not become fact here.
- `MYS:WORKS-ORIGINAL-PURPOSE`: repurposing evidence, mismatched components, layered modifications, and partial records are allowed; a master-builder civilization or lost-utopia answer is not fixed.
- `MYS:SEASONAL-ANOMALIES`: repeatable observations without fixed cause and conflicting interpretations are allowed; no magic system, gods, aliens, simulation twist, or universal non-supernatural conclusion becomes canon here.
- `MYS:OUTER-CONNECTIONS`: evidence of exchange, travel, information flow, or obligations is allowed; final neighboring polities/regions or imported sibling factions remain forbidden.

## 9. Provisional sibling interfaces

The preserved role IDs are:

- `ROLE:LOCAL-CIVIC-STEWARD`;
- `ROLE:LAND-USE-CUSTODIAN`;
- `ROLE:WATER-DEPENDENT-USER`;
- `ROLE:TRAVEL-AND-EXCHANGE-LINK`;
- `ROLE:HISTORY-BEARER`;
- `ROLE:PLAYER-ENTRY`.

Sibling roots may map zero, one, or several concrete entities to these roles. This world packet cannot name who fills them. Claim perspectives such as `fragmentation_account_a` and `fragmentation_account_b` remain provisional perspective keys under `ROLE:HISTORY-BEARER`, not new characters or factions.

## 10. Branch and knowledge discipline

Baseline facts apply to `BRANCH:BASELINE` unless otherwise typed. Downstream branches may add or supersede scoped current-state facts, but may not silently mutate history. Secrets are not automatically mysteries: a secret can have an objective answer hidden from some agents, while an `UNKNOWN_BY_DESIGN` mystery has no answer in this packet.

Claims add a third independent axis. A claim can be public or secret and can agree, disagree, or remain unresolved against objective truth. Neither popularity nor exposure promotes it.

## 11. Evidence, assumptions, and inference

Authoritative planning still requires stable IDs, chronology, fact/knowledge separation, explicit consequences, structural validation, engine-independent logical state, and original expression. Existing `WSN-E1..WSN-E9` remain the empirical route; this remediation does not execute, duplicate, satisfy, or mark any of them PASS.

Preserved bounded assumptions:

- `ASM:WORLD-01`: a bounded watershed can support sufficient gameplay/content variety before external regions are frozen;
- `ASM:WORLD-02`: players can understand cross-location consequences if observable signals and causal edges are explicit;
- `ASM:WORLD-03`: relative chronology is sufficient before exact `GameTimePolicy` mapping;
- `ASM:WORLD-04`: sibling roots can consume role/location IDs without final names or ownership assignments.

## 12. Open questions and reopen conditions

- `OPEN:WORLD-01`: reviewed social root requires topology change -> reconcile at `W2-CONTENT-SYN-01`.
- `OPEN:WORLD-02`: reviewed narrative root requires incompatible chronology -> record contradiction and reconcile at fan-in.
- `OPEN:WORLD-03`: WSN evidence invalidates topology or causal edge -> reopen affected world facts; prose cannot overrule evidence.
- `OPEN:WORLD-04`: originality review finds material similarity -> quarantine and rewrite affected content.
- `OPEN:WORLD-05`: concrete engine dependency discovered -> record only that scoped technical dependency.
- `OPEN:WORLD-06`: product/platform scope requires representation change -> review scoped presentation/access constraints.
- `OPEN:WORLD-07`: reviewed fan-in authorizes a supernatural ontology -> resolve only explicitly authorized mysteries.

## 13. Remediation self-review

Against Issue #382 acceptance criteria:

- exact canonical, producer, review, and publication identities frozen: **PASS**;
- M01 belief/claim representation structurally separated from fact authority and exposure: **PASS**;
- M01 holder/perspective/proposition references stable and provisional: **PASS**;
- M01 fail-closed no-promotion invariant explicit: **PASS**;
- M02 all eras explicitly and relatively ordered: **PASS**;
- M02 event-era membership and event precedence mechanically constrained: **PASS**;
- topology and causal properties preserved: **PASS**;
- sibling independence preserved: **PASS**;
- engine neutrality preserved: **PASS**;
- noncanonical and bounded-scope boundaries preserved: **PASS**;
- originality boundary preserved: **PASS**;
- assumptions/reopen routes preserved: **PASS**;
- WSN evidence state unchanged and no prose PASS claimed: **PASS**;
- no engine choice, gameplay/high-throughput implementation, readiness, release, verification-PASS, integration, decision, or canonical authority claimed: **PASS**.

Unresolved remediation-scope findings: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR**.

This self-review is not the required fresh review. The exact remediation packet must receive a fresh independent or degraded-independent review before it may be clean for bounded `W2-CONTENT-SYN-01` fan-in.