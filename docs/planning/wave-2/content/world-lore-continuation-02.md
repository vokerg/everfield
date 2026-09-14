# W2 world/lore continuation 02 — bounded candidate

## Status and authority

Mission: `W2-CONTENT-WORLD-CONT-02` / Issue #1049.

This packet is an engine-neutral, **NOT_CANONICAL** content candidate. It deepens the world-facing interfaces already accepted for bounded continuation consumption by Issue #1009. It does not select final canon, consume sibling CONT-02 mutable outputs, upgrade WSN evidence, authorize implementation, or establish engine/readiness/release/decision authority.

Production base is `main@586d4cf9e6ec413246184c27a23424f699ad0137`. Canonical Planning Program v1 remains blob `e3120ec203c4156328770aa86c12fbb7187966dc`, bound by Issue #6 comment `5245368879`. CONT-02 activation authority is terminal Review #1063 comment `5654948592`, disposition `CLEAN_FOR_BOUNDED_CONTENT_FRONTIER_CONTINUATION_02_ACTIVATION`.

Frozen reviewed predecessor:
- synthesis Issue #986 / terminal `5644862732`;
- synthesis artifacts `content-fan-in-continuation-01.md` blob `b39f535dc71639f3ebc67e33a2d692a2b3a77588` and YAML blob `78148f50649ada789feb3cca61182e18465bb628`;
- required Review #1009 / terminal `5645006619`, disposition `CLEAN_FOR_BOUNDED_CONTENT_CONTINUATION_CONSUMPTION`.

## World continuation rule

This root expands **world structures and evidence surfaces**, not final fiction. Each structure has a stable candidate ID, bounded affordances, explicit unresolved fields, authority classification, and provisional sibling hooks. A later fan-in may reconcile compatible hooks; this producer does not read or bind sibling CONT-02 outputs.

No structure below fixes exact calendar dates, durations, travel times, opening hours, weather windows, NPC schedules/reachability, final ownership, final polity, final crop/species set, or irreversible branch outcome.

## Candidate structures

### `WORLD02:CULTIVATION-MARGIN` — layered productive edge

Purpose: deepen `WORLD_IFACE:CULTIVATION-MARGIN` as a place where productive use, water condition, soil disturbance, and habitat continuity can vary independently.

Bounded dimensions:
- `productive_use_state`: `ACTIVE | RECOVERING | FALLOW | DISPUTED`;
- `water_condition`: `ADEQUATE | STRESSED | VARIABLE | UNKNOWN`;
- `habitat_continuity`: `CONNECTED | FRAGMENTED | RESTORING | UNKNOWN`;
- `access_pressure`: `LOW | MODERATE | HIGH | DISPUTED`.

Facts may state directly observed conditions only. Yield quality, ownership legitimacy, historical blame, crop identity, and seasonal timing remain OPEN unless separately reviewed.

Provisional hooks: `SOCIAL_ROLE:LAND-USE-STAKE`, `CHAR_ROLE:LOCAL-USER`, `NARR_ROLE:LAND-USE-CONSEQUENCE`.

### `WORLD02:COMMONS-EDGE` — shared-access pressure surface

Purpose: deepen `WORLD_IFACE:COMMONS-EDGE` without deciding final custodianship.

The surface records distinct dimensions for physical condition, permitted-use claims, observed use, ecological pressure, and maintenance burden. Conflicting access claims may coexist as claims. No claimant becomes owner, custodian, or legitimate authority merely by frequency of use, public standing, institutional role, or narrative prominence.

Provisional hooks: `SOCIAL_ROLE:COMMONS-STAKE`, `CHAR_ROLE:LOCAL-USER`, `NARR_ROLE:ACCESS-CONSEQUENCE`.

### `WORLD02:OUTER-CONNECTION` — exchange and movement trace interface

Purpose: deepen `WORLD_IFACE:OUTER-CONNECTION` as evidence of exchange and movement beyond the bounded setting while leaving external geography unresolved.

Allowed evidence includes object provenance, recurring traffic traces, repaired infrastructure, hearsay explicitly typed as claim, and branch-local arrival/departure observations. It may not establish a timetable, travel duration, neighboring polity, trade monopoly, route safety guarantee, or always-reachable destination.

Provisional hooks: `SOCIAL_ROLE:PUBLIC-WORKS-STAKE`, `CHAR_ROLE:LOCAL-USER`, `NARR_ROLE:ACCESS-CONSEQUENCE`.

### `WORLD02:WATER-DEPENDENCY` — dependency without ownership inference

Purpose: deepen `WORLD_IFACE:WATER-DEPENDENCY` as an environmental/maintenance dependency.

The packet separates:
1. physical observation of flow/storage/condition;
2. practical dependency by a world-use surface;
3. claims about entitlement, cause, blame, or priority;
4. private or specialized interpretation.

Water observation cannot establish social entitlement. Social entitlement cannot rewrite physical fact. Exact capacity, seasonal cycles, or timed scarcity remain unasserted.

Provisional hooks: `SOCIAL_ROLE:WATER-DEPENDENT-USER`, `CHAR_ROLE:LOCAL-USER`, `NARR_ROLE:WORKS-CHOICE`.

### `WORLD02:SHARED-WORKS-JUNCTION` — repairable common infrastructure locus

Purpose: deepen `WORLD_IFACE:SHARED-WORKS-JUNCTION` as a bounded location/interface where maintenance decisions leave visible, durable traces.

State dimensions:
- `operability`: `SERVICEABLE | DEGRADED | PARTIAL | UNKNOWN`;
- `repair_trace`: append-only evidence references;
- `access_state`: physical accessibility only, never private-information authority;
- `burden_trace`: observed work/material traces, not automatic attribution.

The surface can support repair and consequence scenarios without making one institution, character, or branch the canonical maintainer.

Provisional hooks: `SOCIAL_ROLE:PUBLIC-WORKS-STAKE`, `CHAR_ROLE:HISTORY-INTERPRETER`, `NARR_ROLE:WORKS-CHOICE`.

### `WORLD02:HISTORY-TRACE` — evidence strata with unresolved attribution

Purpose: deepen `WORLD_IFACE:HISTORY-TRACE` into a fail-closed evidence interface for material traces, records, and contested interpretations.

Every entry is one of:
- `OBSERVED_TRACE`: bounded directly inspectable property;
- `DATED_RELATIVE`: only relative placement in the reviewed era order;
- `CLAIMED_ATTRIBUTION`: proposition plus claimant/provenance;
- `INTERPRETATION`: non-authoritative reading of one or more traces;
- `ABSENCE_RECORD`: explicitly scoped non-observation, never proof of global absence.

No claim or interpretation mutates objective history. Contradictory attributions remain simultaneously representable.

Provisional hooks: `CHAR_ROLE:HISTORY-INTERPRETER`, `NARR_ROLE:CONSEQUENCE-WITNESS`.

### `WORLD02:SETTLEMENT-CORE` — hub locus without polity closure

Purpose: deepen reviewed locus `LOC:SETTLEMENT-CORE` as a shared spatial anchor while preserving OPEN institution, ownership, and polity bindings.

Allowed structural affordances are ordinary community interaction, public-information surfaces, baseline movement through connected public areas, and references to adjacent reviewed world interfaces. Private access, faction control, named office-holding, exact population, and ownership remain outside this root.

Provisional hooks: `SOCIAL_ROLE:PUBLIC-WORKS-STAKE`, `CHAR_ROLE:LOCAL-USER`, `NARR_ROLE:CONSEQUENCE-WITNESS`.

### `WORLD02:AFTERMATH-SURFACE` — typed branch consequence envelope

Purpose: deepen `WORLD_ROLE:CONT_AFTERMATH_SURFACE` without choosing a concrete branch location.

A later reviewed branch may select one or more compatible world surfaces, but the consequence record must state:
- affected interface refs;
- observable physical delta;
- persistence/reversibility class;
- recovery/mitigation evidence needed;
- branch scope;
- whether the delta is `PROPOSED`, `BRANCH_FACT`, or `OBJECTIVE_FACT`.

This root authorizes no irreversible instance. Any irreversible or high-impact concrete authored branch still requires separate `BranchImpactEvidence`, precommitment signaling, continued-play obligations, and review.

## Fact, claim, mystery, and exposure separation

World records use stable proposition and claim identities:
- `PROP:WORLD02:*` identifies a proposition without asserting truth;
- `CLM:WORLD02:*` identifies an in-world assertion with claimant/provenance;
- `FACT:WORLD02:*` exists only when this packet has explicit bounded objective authority for an observation;
- `MYST:WORLD02:*` records deliberately unresolved causal/identity questions.

Rules:
1. a claim never promotes itself to fact;
2. repeated claims never promote themselves to fact;
3. knowledge/exposure controls who may know an item, not whether it is true;
4. public visibility does not imply objective truth;
5. secret/private handling does not imply falsity;
6. generated presentation never mutates authority.

The prior fragmentation-cause uncertainty remains unresolved. Any strong faction, character, record, or narrator assertion about cause must remain a claim or interpretation unless a separately reviewed authority effect closes it.

## Relative chronology

The only governing era order remains:

`ERA:PRE-WORKS → ERA:WORKS-BUILDOUT → ERA:PATCHWORK-PRESENT`.

CONT-02 may add relative event bands only:
- `EVB:WORLD02:PRE-WORKS-USE` contained by `ERA:PRE-WORKS`;
- `EVB:WORLD02:BUILDOUT-ALTERATION` contained by `ERA:WORKS-BUILDOUT`;
- `EVB:WORLD02:PATCHWORK-REPAIR` contained by `ERA:PATCHWORK-PRESENT`;
- `EVB:WORLD02:PRESENT-OBSERVATION` contained by `ERA:PATCHWORK-PRESENT` and ordered after any cited `PATCHWORK-REPAIR` trace when evidence supports that relation.

These are ordering bands, not exact dates or durations. List order alone is not chronology authority; every asserted relation must be explicit.

## Cross-root interface contract

This root may emit only provisional interfaces:
- `SOCIAL_ROLE:WATER-DEPENDENT-USER`
- `SOCIAL_ROLE:PUBLIC-WORKS-STAKE`
- `SOCIAL_ROLE:COMMONS-STAKE`
- `SOCIAL_ROLE:LAND-USE-STAKE`
- `CHAR_ROLE:HISTORY-INTERPRETER`
- `CHAR_ROLE:LOCAL-USER`
- `NARR_ROLE:CONSEQUENCE-WITNESS`
- `NARR_ROLE:WORKS-CHOICE`
- `NARR_ROLE:ACCESS-CONSEQUENCE`
- `NARR_ROLE:LAND-USE-CONSEQUENCE`

No concrete sibling entity is required. Unresolved bindings remain `OPEN` or `OPEN_BOUNDED_SET` until the later CONT-02 fan-in.

## WSN evidence boundary

No WSN result is changed:
- E3 `INCONCLUSIVE_TIMED_COVERAGE_BLOCKED`
- E4 `NOT_RUN_BLOCKED_BY_EXACT_PREREQUISITE`
- E5 `PASS_BOUNDED_MODEL_ONLY`
- E8 `INCONCLUSIVE_SCHEDULE_COVERAGE_BLOCKED`

Therefore this packet cannot establish exact schedules, timed windows, travel/weather guarantees, actor availability, NPC reachability, production persistence, human-quality PASS, aggregate verification PASS, or implementation readiness.

## Residual OPEN ledger

- final custodians/owners/polity;
- concrete crop/species/yield catalog;
- exact water capacity and seasonal behavior;
- external geography and route timetable;
- final cause of historical fragmentation;
- concrete sensitive-site identity;
- final narrative branch-to-site assignment;
- exact social/character role occupants;
- exact dates/durations/schedules/reachability;
- concrete irreversible/high-impact BranchImpactEvidence;
- final canon and production-quality determination.

## Self-review

Attacks performed: sibling mutable consumption, invented final canon, fact/claim promotion, private-information leakage, chronology overreach, hidden schedule assumptions, ownership/polity inference, irreversible consequence authorization, WSN laundering, engine coupling, scope expansion, and higher-authority inflation.

Result: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR** within this bounded producer scope.

Required next gate: one fresh independent/degraded-independent review of the exact immutable packet. A clean review may grant only `W2-CONTENT-WORLD-CONT-02_REVIEWED` for later bounded fan-in. It grants no integration, verification, readiness, engine-selection, release, decision, final-canon, or canonical authority.
