# W2-CONTENT-SOCIAL-CONT-02 — bounded social-conflict continuation

**Issue:** #1050  
**State:** CONTENT CANDIDATE / NONCANONICAL  
**Conflict domain:** `CONTENT`  
**Engine dependency:** none  
**Required next gate:** one fresh independent/degraded-independent required root review of this exact packet

## 1. Scope and frozen authority

This packet deepens the reviewed CONT-01 fan-in's social interfaces without selecting final cross-root fiction. It preserves the six reviewed social actors and the four reviewed institutional pressure families, then adds bounded conflict-case, negotiation, disclosure, and gate-composition contracts suitable for later `W2-CONTENT-SYN-CONT-02` fan-in.

Frozen execution basis:

- producer base: `main@586d4cf9e6ec413246184c27a23424f699ad0137`;
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- canonical binding: Issue #6 comment `5245368879`;
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- CONT-02 activation review: Issue #1063 terminal `5654948592`, disposition `CLEAN_FOR_BOUNDED_CONTENT_FRONTIER_CONTINUATION_02_ACTIVATION`;
- reviewed predecessor synthesis: Issue #986 terminal `5644862732`, Markdown/YAML blobs `b39f535dc71639f3ebc67e33a2d692a2b3a77588` / `78148f50649ada789feb3cca61182e18465bb628`;
- predecessor required review: Issue #1009 terminal `5645006619`, disposition `CLEAN_FOR_BOUNDED_CONTENT_CONTINUATION_CONSUMPTION`.

No mutable CONT-02 sibling output is consumed. Cross-root references emitted here are provisional `WORLD_ROLE:*`, `CHAR_ROLE:*`, or `NARR_ROLE:*` interfaces only.

## 2. Preserved reviewed social surface

The packet preserves the reviewed social identities only:

`FAC-COMMONS-01`, `FAC-FIELDWARD-01`, `FAC-MAKERS-01`, `FAC-ARCHIVE-01`, `FAC-WAYKEEPERS-01`, and `COM-NEIGHBOR-01`.

No new faction, institution, polity, owner, character membership, or sibling role assignment is authored.

The four prior pressure families remain the semantic foundation:

1. civic burden / legitimacy;
2. land-resource stewardship / scarcity;
3. records / testimony / confidentiality;
4. repair capacity / access / safety.

Relationship state remains a vector (`trust`, `reliability`, `reciprocity`, `value_alignment`, `public_standing`, scope-specific `access_state`). Institutional legitimacy remains a separate vector (`procedural_fairness`, `responsibility_fulfillment`, `burden_distribution`, `domain_competence`, `transparency_fit`, `constituency_support`). Neither vector is a universal score and neither automatically updates the other.

Material social history is append-only in authority: repair may change current effects but cannot delete a breach, disclosure, compromise, refusal, exclusion, or dissent event.

## 3. CONT-02 conflict-case contracts

A `SocialConflictCase` is a bounded tension packet, not a final quest or canon event. Every case records pressures, reviewed social participants, provisional sibling interfaces, protected baselines, allowed response classes, and authority exclusions.

### `SOC2-CONFLICT-001` — shared-resource burden allocation

Reviewed participants: `FAC-COMMONS-01`, `FAC-FIELDWARD-01`, `COM-NEIGHBOR-01`.

Provisional interfaces: `WORLD_ROLE:COMMON_RESOURCE`, `WORLD_ROLE:CONTESTED_COMMON`, `WORLD_ROLE:CULTIVATION_ZONE`, `NARR_ROLE:SOCIAL_DISPUTE`.

The case may represent disagreement over contribution, stewardship burden, scarcity, restoration, or allocation. It may not settle ownership, crop/species sets, exact yields, quotas, seasons, or final custodians. A valid resolution must preserve baseline cultivation/community participation and expose at least one repair, compromise, substitute, or defer-and-return route.

### `SOC2-CONFLICT-002` — public accountability versus protected testimony

Reviewed participants: `FAC-COMMONS-01`, `FAC-ARCHIVE-01`.

Provisional interfaces: `WORLD_ROLE:CONT_HISTORY_OR_EVIDENCE_SOURCE`, `CHAR_ROLE:INDEPENDENT_MEDIATOR`, `CHAR_ROLE:COMMUNITY_NEIGHBOR`, `NARR_ROLE:PUBLIC_COMMITMENT`.

The case may represent pressure to disclose, corroborate, challenge, or protect testimony. Public exposure, institutional record status, standing, relationship state, or repeated assertion cannot create objective truth or private knowledge. Protected information remains deny-by-default unless one explicit lawful disclosure/acquisition record authorizes a scoped recipient.

### `SOC2-CONFLICT-003` — specialist capacity versus public repair need

Reviewed participants: `FAC-MAKERS-01`, `FAC-WAYKEEPERS-01`, `FAC-COMMONS-01`.

Provisional interfaces: `WORLD_ROLE:CONT_CONTESTED_SITE`, `WORLD_ROLE:TRANSIT_EDGE`, `WORLD_ROLE:COMMON_RESOURCE`, `NARR_ROLE:SOCIAL_DISPUTE`.

The case may represent scarce specialist capacity, safety constraints, prioritization, service substitution, or restitution. It may deny only a bounded specialist/optional/branch surface with a typed reason. It cannot become a universal repair, movement, exploration, or ordinary-service tax.

### `SOC2-CONFLICT-004` — institutional legitimacy under disagreement

Reviewed participants: any subset of the six reviewed social identities; concrete character alignment remains OPEN.

Provisional interfaces: `CHAR_ROLE:FACTION_LIAISON`, `CHAR_ROLE:INDEPENDENT_MEDIATOR`, `CHAR_ROLE:COMMUNITY_NEIGHBOR`, `NARR_ROLE:SOCIAL_DISPUTE`, `NARR_ROLE:PUBLIC_COMMITMENT`.

The case allows evidence-backed disagreement about process, competence, burden distribution, transparency, or constituency support. It cannot collapse legitimacy into popularity, cannot force agreement, and cannot make high legitimacy a private-information or objective-truth capability.

## 4. Assertion, testimony, belief, knowledge, and truth

`SocialAssertionState` keeps the following dimensions orthogonal:

- proposition reference;
- holder/source perspective;
- speech/record class (`CLAIM`, `BELIEF`, `TESTIMONY`, `INSTITUTIONAL_RECORD`, `ANALYSIS`);
- holder epistemic state;
- dispute status;
- exposure scope;
- recipient knowledge effect;
- provenance/evidence;
- branch scope;
- external objective-fact reference, if any;
- truth relation;
- objective-fact authority.

The social root never owns objective-fact promotion. `objective_fact_authority` is always `false`. A separately reviewed external fact may contradict or corroborate an assertion, but the assertion itself cannot create or mutate that fact.

Generated presentation, repetition, institutional endorsement, public standing, relationship strength, role membership, or player visibility cannot change this rule.

## 5. Private-information and disclosure contract

Private/secret information is `DENY_BY_DEFAULT`.

A `SocialDisclosureDecision` may update recipient exposure/knowledge only when it identifies:

1. exact information/proposition reference;
2. current lawful holder or source;
3. recipient scope;
4. authority path (`EXPLICIT_HOLDER_DISCLOSURE`, `VALIDATED_AUTHORITY_EFFECT`, or `PUBLIC_RECORD_SCOPE`);
5. provenance/evidence;
6. resulting exposure and recipient knowledge effect;
7. onward-sharing rule;
8. durable history event;
9. branch scope if applicable.

`public_standing`, `trust`, proximity, institutional membership, role membership, public visibility, generated presentation, repeated testimony, and unrelated service history are never sufficient disclosure authority by themselves.

Player exposure does not imply character knowledge. Character knowledge does not imply public exposure. Disclosure does not alter objective truth.

## 6. Typed relationship and legitimacy changes

Every material relationship or legitimacy update requires one `SocialStateChange` with:

- typed cause;
- evidence/provenance refs;
- exact affected dimensions;
- signed/qualitative effect per affected dimension;
- unaffected dimensions explicitly preserved;
- visibility scope;
- branch scope;
- durability/history event;
- repairability and any reversal/recovery evidence.

No event may silently update all relationship dimensions. No legitimacy observation may automatically update a character relationship vector. No repeated low-risk action may wash out a material breach or disclosure event.

## 7. Negotiation, repair, compromise, and alternatives

Every conflict case exposes bounded `SocialResolutionOption` records. Allowed classes are:

- `REPAIR`;
- `COMPROMISE`;
- `MEDIATION`;
- `SUBSTITUTE_ROUTE`;
- `PUBLIC_DISSENT`;
- `DEFER_AND_RETURN`;
- `BOUNDED_EXCLUSION`.

Each option states prerequisites, protected baselines, tradeoffs, current-state effects, durable history effects, denied surface (if any), recovery/alternative route, truth effect, knowledge effect, and branch scope.

`COMPROMISE` may preserve disagreement. `PUBLIC_DISSENT` may reduce scoped standing or alignment without changing truth. `BOUNDED_EXCLUSION` is illegal if it removes baseline movement, ordinary community interaction, public information, baseline cultivation, basic repair/crafting opportunity, or ordinary mutual aid.

Irreversible concrete world change is not authorized. Any later high-impact concrete aftermath requires separate `BranchImpactEvidence` and review.

## 8. Nonfoundational gate-composition invariant

The six reviewed social gates retain their classes:

- `GATE-SOC-COMMONS-DELEGATION-01` — `SPECIALIZATION`;
- `GATE-SOC-FIELDWARD-SHARED-STOCK-01` — `SPECIALIZATION`;
- `GATE-SOC-MAKERS-COMMISSION-01` — `OPTIONAL`;
- `GATE-SOC-ARCHIVE-SENSITIVE-01` — `OPTIONAL`;
- `GATE-SOC-WAYKEEPER-SPONSOR-01` — `OPTIONAL`;
- `GATE-SOC-COALITION-COMMITMENT-01` — `BRANCH_EXCLUSIVE`.

Foundational gate count remains `0`.

CONT-02 adds a composition rule: no combination, dependency chain, branch convergence, or repeated-use expectation may make these gates jointly mandatory for a common foundational goal. A nonfoundational gate may unlock only its bounded specialist/optional/branch surface. If later design would require two or more of these gates in sequence for baseline play, the composition fails closed and must reopen for explicit review; it may not silently become a de facto foundational gate.

## 9. Chronology, branch, and consequence scope

New social-history instances may use only relative ordering (`before`, `after`, `contained_by`, `caused_by`, `responds_to`) against reviewed event roles. No exact date, duration, schedule, opening hour, travel time, weather window, or NPC reachability guarantee is authored.

Branch-scoped consequences remain branch-scoped. Mutually exclusive commitments are never jointly required. Repair/reconciliation may supersede current penalties but cannot erase material branch or disclosure history.

## 10. OPEN cross-root interfaces

The following remain intentionally unresolved:

- concrete `WORLD_ROLE:*` instance selection for any conflict case;
- concrete `CHAR_ROLE:*` holder, mediator, liaison, or participant assignment;
- concrete `NARR_ROLE:*` quest/branch/consequence binding;
- exact proposition-to-objective-world-fact bindings;
- final actor-to-institution membership where not already reviewed social identity;
- exact chronology positions beyond relative constraints;
- any private-information recipient not authorized by a concrete disclosure record;
- exact schedules, timed windows, weather/travel interaction, or NPC reachability;
- any irreversible/high-impact concrete aftermath without separate evidence and review.

OPEN is not failure and cannot become hidden progression debt.

## 11. WSN evidence boundary

This producer reruns no experiment and upgrades no result.

- E3 remains `INCONCLUSIVE_TIMED_COVERAGE_BLOCKED`;
- E4 remains `NOT_RUN_BLOCKED_BY_EXACT_PREREQUISITE`;
- E5 remains `PASS_BOUNDED_MODEL_ONLY`;
- E8 remains `INCONCLUSIVE_SCHEDULE_COVERAGE_BLOCKED`.

Structural consistency here does not establish human quality, production persistence, schedule correctness, verification-PASS, implementation readiness, release readiness, or canon.

## 12. Producer self-review

Adversarial checks attacked:

- new faction/polity/ownership invention;
- concrete sibling binding;
- assertion/testimony/record → objective-fact promotion;
- secret/private leakage through standing, trust, membership, proximity, or player exposure;
- relationship/legitimacy scalarization;
- untyped or global relationship effects;
- history erasure through repair/retry;
- hidden foundational gate composition;
- baseline-play exclusion;
- one-way consequences without repair/compromise/alternative;
- exact-time/schedule/reachability invention;
- WSN laundering;
- engine coupling;
- implementation/readiness/release/canon authority inflation.

Result: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR**.

Required next route: exactly one fresh independent/degraded-independent review of this immutable three-file packet. A clean review may grant only `W2-CONTENT-SOCIAL-CONT-02_REVIEWED` for later bounded `W2-CONTENT-SYN-CONT-02` fan-in.

## 13. Authority boundary

`NOT_CANONICAL`. This producer grants no integration, verification-PASS, implementation readiness, gameplay/high-throughput implementation, engine selection, release, decision, final-canon, or canonical authority.
