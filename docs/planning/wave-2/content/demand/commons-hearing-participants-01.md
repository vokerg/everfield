# Bounded Commons Hearing participants and dialogue — Old Works

**Issue:** #1379  
**Mission:** `CONTENT-DEMAND-COMMONS-HEARING-CHAR-01`  
**State:** implementation-fed candidate / `NOT_CANONICAL`  
**Demand source:** #1377 from implementation #1343 / PR #1370 at observed head `5aefb403b35bde1ab754b9feca2916e3f5b4ea03`

## Scope

This packet supplies the smallest participant and dialogue surface needed by the already-implemented Commons Hearing in `VS:OLD-WORKS-ACCOUNTS-01`.

It binds only the reviewed slice-local negotiation actors already named by the authored vertical slice:

- `CHAR:maelin_sor` — affected-burden voice for this hearing;
- `CHAR:selka_vey` — bounded procedure/coordination voice for this hearing.

These are **hearing presentation roles**, not offices, faction memberships, representatives, custodians, or legitimacy grants. The packet does not select final office holders, establish representation, rank factions, settle institutional legitimacy, or create a universal character/social canon.

The hearing remains scoped to `LOC:OLD-WORKS`, `OBJ:VS:NEGOTIATE-SHARED-USE`, and `QROLE:NEGOTIATE_SHARED_USE`. It does not settle `MYS:FRAGMENTATION-CAUSE`; that mystery remains exactly `UNKNOWN_BY_DESIGN`.

## Reviewed constraints carried forward

The packet preserves the reviewed relationship/history boundary around Maelin and Selka:

- predecessor history `REL_EVT:maelin_selka_burden_objection` remains durable;
- candidate hearing event `REL_EVT:VS:MAELIN-SELKA-HEARING-01` may record a public burden hearing if the player attends;
- acknowledging burden may support RESPECT remaining or increasing;
- dismissing burden may support CAUTION increasing;
- RESPECT and CAUTION may coexist;
- TRUST, WARMTH, OBLIGATION, and RIVALRY are not automatically changed by these lines;
- no current relationship dimension changes without typed cause/evidence;
- no relationship state, public standing, repeated dialogue, or player preference grants information access, consent, authority, or legitimacy.

This content emits presentation and candidate-evidence cues only. It performs no direct relationship-state mutation.

## Participant cards

### `OW_HEARING_PARTICIPANT_MAELIN_01` — Maelin / affected-burden voice

Slice-local purpose: keep material and care burden visible before a public commitment.

Not asserted:
- office or institutional title;
- representation of `FAC-COMMONS-01`, `FAC-MAKERS-01`, or `COM-NEIGHBOR-01`;
- exclusive standing to speak for affected people;
- authority to approve or veto the project;
- knowledge of private secrets.

Hearing stance:
- accepts bounded action only when who carries the work and risk is made visible;
- may remain nonaligned when burden is hidden;
- does not treat procedural validity as closing consequence disputes.

### `OW_HEARING_PARTICIPANT_SELKA_01` — Selka / bounded procedure voice

Slice-local purpose: keep public commitment explicit, scoped, reversible where promised, and distinguishable from consent or legitimacy.

Not asserted:
- office or institutional title;
- final custodian/representative status;
- exclusive authority over the Commons;
- authority to convert participation into consent or objective truth;
- access to any undisclosed private information.

Hearing stance:
- requires the choice and its limits to be stated rather than implied;
- preserves deferral and nonalignment as legal outcomes;
- does not treat a completed procedure as proof that burdens are resolved.

## Dialogue beats

All IDs below are implementation-facing presentation IDs. They have no direct fact, relationship, branch, secret, canon, readiness, production, release, or integration authority.

| Beat ID | Speaker | Phase | Player-facing line |
|---|---|---|---|
| `OW_HEARING_OPEN_MAELIN_01` | Maelin | opening | “Before we choose a route, name who carries the work if the Old Works fail again.” |
| `OW_HEARING_OPEN_SELKA_01` | Selka | opening | “Then keep the choice bounded: record the scope, the burden, and how we can stop or revise it.” |
| `OW_HEARING_REPAIR_SELKA_01` | Selka | repair-pilot position | “A repair pilot is a trial, not a title to the Works. State the limit before anyone calls it settled.” |
| `OW_HEARING_REPAIR_MAELIN_01` | Maelin | repair-pilot position | “And state who is carrying the repair. If that burden is hidden, I do not support the pilot.” |
| `OW_HEARING_RECORDS_MAELIN_01` | Maelin | records-first position | “Records first is slower, but it leaves the burden visible instead of burying it under urgency.” |
| `OW_HEARING_RECORDS_SELKA_01` | Selka | records-first position | “Then record the limit: document, use narrowly, and reopen repair only by another public choice.” |
| `OW_HEARING_DEFER_SELKA_01` | Selka | defer/nonalignment | “No assent is recorded. Reopen the hearing only when someone chooses to.” |
| `OW_HEARING_DEFER_MAELIN_01` | Maelin | defer/nonalignment | “Then leave the burden on the table too. Deferral is not agreement with either account.” |
| `OW_HEARING_REFUSE_MAELIN_01` | Maelin | refusal | “I won’t endorse a route that hides who carries it. Put that burden in view or leave me unaligned.” |
| `OW_HEARING_REFUSE_SELKA_01` | Selka | refusal | “I won’t call this settled without a bounded scope and a way to revise it. Record nonalignment instead.” |

The refusal beats are legal content, not hidden prerequisites. They do not block the implementation's existing ability to defer commitment, reopen the hearing, or continue ordinary shared play.

## Choice semantics

### Repair pilot

The hearing may present the implemented `repair_pilot` choice only as a bounded, conditionally reversible pilot. Dialogue may surface scope, burden, and the need for visible correction if burden was excluded. It must not imply:

- ownership of the Old Works;
- final Commons approval;
- mystery resolution;
- permanent alignment;
- universal endorsement by Maelin, Selka, or any faction.

### Records first

The hearing may present `records_first` as documentation and limited use before broader repair. Dialogue may surface delayed physical repair as a tradeoff. It must not imply that an archive entry settles the disputed fragmentation cause or that institutional recording turns a claim into objective truth.

### Defer commitment

`defer` is a complete legal hearing result for the bounded interaction. It means:

- no public commitment is recorded;
- no assent is inferred;
- no relationship score is banked toward future consent;
- nonalignment may persist without penalty or hidden progression debt;
- the hearing may later reopen without erasing prior history.

Deferral is not “consent in waiting.”

## Relationship implications

This packet does not create automatic relationship deltas.

Only the following reviewed candidate implications are preserved for later implementation under typed cause/evidence:

| Condition | Candidate dimension implication | Non-implication |
|---|---|---|
| burden is explicitly acknowledged | Maelin/Selka `RESPECT` may remain or increase | does not grant trust, warmth, consent, legitimacy, or access |
| burden is dismissed or hidden | Maelin/Selka `CAUTION` may increase | does not force hostility, rivalry, route failure, or secret denial |
| refusal/nonalignment is respected | may support later evidence for boundary-respecting cooperation | no immediate relationship mutation |
| player repeats dialogue or revisits hearing | none | repetition cannot grind trust, standing, consent, or authority |

`TRUST`, `WARMTH`, `OBLIGATION`, and `RIVALRY` remain unchanged by this packet unless a separately reviewed typed event later supplies evidence.

## Information and privacy firewall

No private secret is required or quoted.

In particular, `INFO:anwen_contested_record_provenance_gap` is not part of any required hearing beat, participant card, refusal, or route choice. The hearing works with public/in-session investigation state already available to the bounded implementation. Relationship state, public standing, institutional procedure, player attendance, or generated dialogue never grants access to that secret.

## Implementation contract

A later bounded implementation consumer may:

- show the two participant cards;
- emit the ten stable beat IDs and associated text;
- choose context-appropriate repair, records-first, defer, or refusal beats;
- append an attended-hearing history event consistent with `REL_EVT:VS:MAELIN-SELKA-HEARING-01`.

A consumer must not:

- make these lines required evidence for objective truth;
- convert dialogue selection into relationship-state mutation without typed evidence;
- create a popularity/approval/relationship scalar;
- use refusal as a hidden foundational gate;
- require private-secret content;
- infer offices, representation, legitimacy, final canon, or faction authority;
- modify sibling #1378 world/evidence or #1380 consequence-owned content as part of this packet.

## Reopen conditions

Re-review or bounded revision is required if later implementation:

- needs a third concrete participant rather than the two already-reviewed actors;
- changes hearing route cardinality or makes refusal/deferral unavailable;
- adds direct relationship mutations;
- requires private information;
- introduces institutional office/representation claims;
- changes the Old Works mystery from `UNKNOWN_BY_DESIGN`;
- turns any presentation ID into fact, secret-access, branch, or authority state.
