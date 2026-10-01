# Old Works commitment consequence presentation — implementation-fed candidate

## Status and authority

- mission: `CONTENT-DEMAND-OLD-WORKS-CONSEQUENCE-01`
- issue: #1380
- demand intake: #1377 terminal comment `5926633748`
- implementation source: #1343 / PR #1370
- exact implementation head consumed: `5aefb403b35bde1ab754b9feca2916e3f5b4ea03`
- authored vertical-slice source: `VS:OLD-WORKS-ACCOUNTS-01`
- corrected authored-slice YAML blob: `8d341d534ef4a27929aaabdf5b81a6d5ff86b80e`
- clean authored-slice remediation review: #449, `CLEAN_FOR_BOUNDED_AUTHORED_CONTENT_CONSUMPTION`
- canonical Planning Program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`
- canonical binding: Issue #1147 comment `5675066392`
- canonicality: `NOT_CANONICAL`

This packet supplies candidate player-facing presentation for commitment states that already exist in the bounded Godot first playable. It does not change gameplay code, activate a branch by itself, establish final narrative canon, satisfy BranchImpactEvidence or WSN-E5, or grant integration, production, or release authority.

## Scope and non-goals

The exact executable surface already exposes three hearing responses:

1. `repair_pilot`;
2. `records_first`;
3. explicit `defer`.

Only the first two may close the current Project Table loop. Deferral records a lawful noncommitment and leaves the table incomplete.

This packet adds:

- immediate consequence presentation for the two committed routes;
- explicit non-consent semantics for deferral;
- an append-only mapping to the implementation's existing history events;
- exactly one bounded, non-automatic follow-up hook per committed route.

It does **not** add another quest tranche, a timer, an NPC schedule, a permanent owner, a final restoration policy, a new social scalar, a private-secret requirement, or a historical verdict.

## Frozen truth and agency constraints

Every presentation below preserves these reviewed constraints:

- `MYS:FRAGMENTATION-CAUSE = UNKNOWN_BY_DESIGN`;
- `CLM:FRAGMENTATION-ACCOUNT-A` and `CLM:FRAGMENTATION-ACCOUNT-B` remain incompatible in-world claims with zero truth effect;
- completing a project choice does not increase either claim's authority;
- public commitment does not establish ownership, legitimacy, representation, office, membership, or consent beyond the exact chosen act;
- deferral is not consent-in-waiting;
- retry, reopening, repair, or later reassessment may change current choices but may not erase prior branch/refusal/commitment history;
- ordinary baseline play remains outside this presentation packet's authority.

## Implementation-facing consequence strings

### Repair pilot

The implementation appends `COMMITMENT_REPAIR_PILOT` when the hearing choice is made and `BOUNDED_REPAIR_PILOT_STARTED` when the Project Table closes the loop.

| ID | Surface | Candidate player-facing text |
| --- | --- | --- |
| `OW_CONSEQ_REPAIR_TITLE` | result title | **Repair Pilot — Bounded Start** |
| `OW_CONSEQ_REPAIR_BODY` | immediate result | **The project table records a limited repair pilot as the next shared-use step. Work beyond the pilot remains uncommitted.** |
| `OW_CONSEQ_REPAIR_HISTORY` | history cue | **This commitment stays in the record even if the pilot is later paused, reframed, or replaced by a fresh public choice.** |
| `OW_CONSEQ_REPAIR_TRUTH` | truth guard | **Starting repair does not decide why the Old Works fragmented, or which account was right.** |
| `OW_CONSEQ_REPAIR_FOLLOWUP` | bounded hook | **When observable pilot evidence exists, reassess the bounded pilot: continue it, pause it, or reframe it through a fresh explicit decision.** |

The follow-up is a candidate hook only. It does not create a scheduled objective, guarantee evidence will exist, pre-authorize continuation, or turn a repair outcome into restoration.

### Records-first

The implementation appends `COMMITMENT_RECORDS_FIRST` when the hearing choice is made and `RECORDS_FIRST_PACKAGE_FILED` when the Project Table closes the loop.

| ID | Surface | Candidate player-facing text |
| --- | --- | --- |
| `OW_CONSEQ_RECORDS_TITLE` | result title | **Records First — Package Filed** |
| `OW_CONSEQ_RECORDS_BODY` | immediate result | **The project table records documentation and limited use before broader repair. Broader physical repair remains deferred, not silently selected.** |
| `OW_CONSEQ_RECORDS_HISTORY` | history cue | **The records-first commitment remains part of the route history if a later reassessment opens a different bounded choice.** |
| `OW_CONSEQ_RECORDS_TRUTH` | truth guard | **Filing the package preserves competing accounts; documentation does not convert either account into a finding.** |
| `OW_CONSEQ_RECORDS_FOLLOWUP` | bounded hook | **After a bounded record and present-condition reassessment, make a fresh choice about whether to open a repair pilot or continue records-first.** |

The hook does not auto-select repair, create a deadline, or make record custody a truth/legitimacy authority.

### Explicit deferral / noncommitment

The implementation appends `PUBLIC_COMMITMENT_DEFERRED`, clears the current commitment, and leaves the Project Table completion gate unsatisfied.

| ID | Surface | Candidate player-facing text |
| --- | --- | --- |
| `OW_CONSEQ_DEFER_TITLE` | hearing result title | **No Public Commitment** |
| `OW_CONSEQ_DEFER_BODY` | immediate result | **Nothing is committed. Deferral records nonalignment for now; it is not approval waiting to happen.** |
| `OW_CONSEQ_DEFER_REOPEN` | recovery cue | **The hearing may be reopened only through a new explicit act. The prior deferral remains in the history.** |
| `OW_CONSEQ_DEFER_TABLE` | Project Table cue | **The project table remains open because no supported public commitment was made.** |
| `OW_CONSEQ_DEFER_TRUTH` | truth guard | **Deferring action does not settle the historical dispute.** |

Deferral has no automatic follow-up hook in this packet. The existing recovery route is simply that a later explicit hearing may occur.

## Append-only event/history contract

This presentation binds to the implementation's existing event sequence without inventing persistence that the executable does not have.

### Repair route

1. `COMMITMENT_REPAIR_PILOT`
2. `BOUNDED_REPAIR_PILOT_STARTED`

### Records-first route

1. `COMMITMENT_RECORDS_FIRST`
2. `RECORDS_FIRST_PACKAGE_FILED`

### Deferral

1. `PUBLIC_COMMITMENT_DEFERRED`

Rules:

- new route events append after prior route events; they do not rewrite them;
- later reconsideration cannot reinterpret a prior refusal or deferral as earlier consent;
- a later repair choice cannot erase a records-first commitment, and a later records-first choice cannot erase a repair-pilot commitment;
- Project Table completion may present the current committed outcome but cannot delete earlier investigation, hearing, deferral, or commitment events;
- the implementation's manual `reset_slice()` is a bounded demo-session reset only and must not be presented as production world-history erasure;
- production persistence/migration evidence remains `WSN-E5` debt and is **not** satisfied by this packet.

## Bounded follow-up hooks

Exactly two hooks are authored, one per committed route:

### `HOOK:OW:REPAIR-PILOT-REASSESS`

- prerequisite: observable evidence from the bounded pilot exists in a later authorized implementation;
- legal presentations: continue bounded pilot, pause, or reframe through a fresh explicit decision;
- may not auto-trigger;
- may not invent a timer, schedule, or guaranteed observation;
- may not erase the earlier commitment/history;
- may not settle `MYS:FRAGMENTATION-CAUSE`.

### `HOOK:OW:RECORDS-FIRST-REASSESS`

- prerequisite: a later bounded reassessment of the record and present condition exists;
- legal presentations: continue records-first or make a fresh bounded decision about repair;
- may not auto-trigger;
- may not make archive custody or document count a truth-strength signal;
- may not erase the earlier commitment/history;
- may not settle `MYS:FRAGMENTATION-CAUSE`.

Neither hook is a new active quest/objective. Both remain inert presentation candidates until separately consumed by an authorized implementation episode.

## Compatibility with reviewed consequence semantics

The packet preserves the reviewed authored-slice consequence contracts:

- repair pilot remains bounded and conditionally reversible;
- records-first prioritizes documentation/limited use and defers broader repair;
- later repair remains possible after reassessment rather than being preselected;
- shared foundational play remains legal;
- community-mitigation/alternative goals are not deleted;
- repair/reframe cannot erase prior material, branch, disclosure, refusal, or relationship history;
- no exact time or schedule is introduced;
- no optional/private information is needed for either committed route or for deferral.

The implementation currently represents only bounded in-session state/history. This candidate text does not claim material observed effects, production persistence, empirical human-quality evidence, final branch-impact clearance, or a canonical ending.

## Consumption boundary

This root owns only consequence presentation. It does not consume or modify the unreviewed sibling #1378 world/evidence packet or #1379 participant/dialogue packet. It does not modify gameplay code.

Fresh exact-head review of this packet is required before any integration or implementation consumption.
