# W2 content world continuation 05 — scoped triangulation and condition-history deepening

## Status and authority

- mission: `W2-CONTENT-WORLD-CONT-05`
- issue: #1231
- ownership generation: comment `5755515340`
- branch: `planning/issue-1231`
- execution base: `main@e842852c9c7d60cf59923c88bd5174dda1c31853`
- canonical Planning Program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`
- canonical binding: Issue #1147 terminal comment `5675066392`
- canonical activation: `87c85cecfa9a2ffa464c4b36816a138bf41441af`
- CONT-05 compiler: Issue #1230 terminal `5755329122`, published by integration `5755436699`
- CONT-05 activation review: Issue #1236 terminal `5755392675`, disposition `CLEAN_FOR_BOUNDED_CONTENT_FRONTIER_CONTINUATION_05_ACTIVATION`
- activation-review provenance publication: `5755498638`
- canonicality: `NOT_CANONICAL`

This packet consumes only the immutable clean-reviewed CONT-04 fan-in: Issue #1225 terminal `5750440511`, head `a0ccb6eb0568cc248d3c23b041414123aba39a31`, Markdown/YAML/handoff blobs `ed8adb966ac467896ead65a773695b30b81e9974` / `d2f03329975bbb8ceb0f4765c367e18fa04a8bf7` / `a41a56071e5da46461b246fa3785412cfef64d25`; and required Review #1228 terminal `5750477894`, disposition `CLEAN_FOR_BOUNDED_CONTENT_CONTINUATION_04_CONSUMPTION`, report/handoff blobs `67c27ba6c0b6207ac7033bec5ba7927f9fb9a2dc` / `e547515253e0650262072cd119358de7e58ff5bc`. Sibling CONT-05 mutable output is not an input.

The packet deepens world evidence, account comparison, and condition history only. It does not select final fiction, choose a site, establish ownership or polity, settle a contested cause, create exact chronology, instantiate a quest/objective, select a branch, or grant integration, verification-PASS, implementation/readiness, gameplay implementation, engine-selection, release/production, human-quality, decision, final-canon, or canonical authority.

## Frozen inherited state contract

| Binding | Required state |
|---|---|
| `SYN-CONT02-OPEN-001` | `OPEN_BOUNDED_SET` |
| `SYN-CONT02-OPEN-002` | `OPEN` |
| `SYN-CONT02-OPEN-003` | `OPEN` |
| `SYN-CONT02-OPEN-004` | `OPEN` |
| `SYN-CONT02-OPEN-005` | `OPEN_OPTIONAL` |
| `SYN-CONT02-OPEN-006` | `UNRESOLVED` |
| `SYN-CONT02-OPEN-007` | `RELATIVE_ONLY` |
| `SYN-CONT02-OPEN-008` | `BLOCKED_BY_EXACT_PREREQUISITE` |
| `SYN-CONT02-OPEN-009` | `LATER_EMPIRICAL_EVIDENCE_REQUIRED` |
| `SYN-CONT02-OPEN-010` | `FINAL_CANON_NOT_AUTHORIZED` |
| `SYN-CONT02-OPEN-011` | `HIGHER_AUTHORITY_NOT_ESTABLISHED` |

Reviewed refinements and CONT-04 compatibility envelopes remain descriptive interfaces. They do not replace, narrow, close, or bind any inherited state.

## OPEN-001 — exact bounded world-surface set

The world surface remains exactly:

1. `WORLD_IFACE:SHARED-WORKS-JUNCTION`
2. `WORLD_IFACE:COMMONS-EDGE`
3. `WORLD_IFACE:CULTIVATION-MARGIN`

No fourth member is added. No member is preferred, ranked, selected, treated as default, or made a prerequisite for another. All CONT-05 structures below can be instantiated against any one of the exact three surfaces only after later reviewed authority selects an applicable authored instance.

## Immutable CONT-04 world interfaces

CONT-05 may reference, but does not mutate, the reviewed CONT-04 interfaces carried by the fan-in:

- `WORLD04:OBSERVATION-FRAME`
- `WORLD04:ACCOUNT-COMPARISON`
- `WORLD04:CONDITION-TRANSITION`
- `WORLD04_ROLE:PUBLIC_WORLD_EVIDENCE`
- `WORLD04_ROLE:REVERSIBLE_CONDITION_ALTERNATIVE`

The CONT-04 evidentiary labels remain exactly `SUPPORTS`, `WEAKENS`, `NONDISCRIMINATING`, and `INSUFFICIENT_SCOPE`. They describe bearing only and are never truth votes.

## WORLD05:TRIANGULATION-PACKET

`WORLD05:TRIANGULATION-PACKET` groups immutable reviewed evidence references without collapsing their authority classes.

Required fields:

- `surface_ref`: exactly one member of the frozen three-surface set;
- `scope_ref`: a bounded observation scope, never a global-world assertion;
- `observation_frame_refs`: one or more immutable `WORLD04:OBSERVATION-FRAME` references;
- `material_trace_refs`: zero or more bounded physical/condition traces;
- `public_record_refs`: zero or more already-reviewed public/nonprivate records;
- `claim_or_testimony_refs`: zero or more provenance-bound claims/testimony;
- `counterevidence_refs`: zero or more contradictory or weakening evidence references;
- `scoped_absence_refs`: zero or more explicit non-observations with the scope retained;
- `unknowns`: explicit variables preventing stronger inference;
- `private_sidecar_refs`: optional and deny-by-default;
- `authority_class: EVIDENCE_FOR_LATER_REVIEW_NOT_FINAL_WORLD_TRUTH`.

A packet is allowed to contain disagreement. Agreement among references does not prove truth; disagreement does not prove falsity. Source count, repetition, institutional provenance, public standing, relationship state, player exposure, or generated presentation cannot promote an observation, claim, record, or interpretation into objective truth.

A private reference never counts toward a required nonprivate route minimum and its absence must remain legal.

## WORLD05:SCOPE-BOUND-DISAGREEMENT

`WORLD05:SCOPE-BOUND-DISAGREEMENT` prevents local observations from being generalized beyond their evidence scope.

It records:

- two or more evidence/claim references when a disagreement is being represented;
- each reference's observation scope and authority class;
- `scope_relation`: `OVERLAPPING`, `PARTIALLY_OVERLAPPING`, `DISJOINT`, or `UNKNOWN`;
- `disagreement_class`: `OBSERVATION_DIFFERENCE`, `CLAIM_DIFFERENCE`, `INTERPRETATION_DIFFERENCE`, or `MIXED`;
- `resolution_state: UNRESOLVED`;
- explicit unknowns and counterevidence;
- no majority, credibility-score, or winner field.

A scoped absence is evidence only about the declared scope. It cannot establish global non-use, global absence, exact timing, motive, responsibility, ownership, legitimacy, or causal primacy.

## OPEN-006 — causal-account discrimination without causal truth

The inherited candidate account classes remain available without selection:

- `WORLD03:ACCOUNT-MAINTENANCE-DIVERGENCE`
- `WORLD03:ACCOUNT-RESOURCE-PRESSURE`
- `WORLD03:ACCOUNT-ACCESS-USE-CONFLICT`
- `WORLD03:ACCOUNT-MULTICAUSAL-OR-UNDERDETERMINED`

`SYN-CONT02-OPEN-006` remains exactly `UNRESOLVED`.

### WORLD05:ACCOUNT-DISCRIMINATION-LEDGER

This ledger deepens `WORLD04:ACCOUNT-COMPARISON` by preserving item-level evidence provenance and scope rather than producing an aggregate score.

For each `account_ref × evidence_ref` pair it records:

- one exact CONT-04 bearing label: `SUPPORTS`, `WEAKENS`, `NONDISCRIMINATING`, or `INSUFFICIENT_SCOPE`;
- the evidence scope;
- provenance/authority class;
- a short bounded rationale;
- counterevidence refs;
- unknowns.

Ledger invariants:

- no numeric aggregate, rank, vote count, confidence total, preferred account, or winner;
- at least two candidate accounts remain present whenever a comparative question is instantiated;
- evidence can bear on more than one account;
- `NONDISCRIMINATING` and `INSUFFICIENT_SCOPE` remain first-class lawful outcomes;
- the underdetermined/multicausal account remains lawful when evidence does not discriminate;
- `causal_truth: UNRESOLVED`;
- `promotion_authority: LATER_EXPLICIT_REVIEWED_AUTHORITY_ONLY`.

Institutional provenance, repetition, relationship state, public standing, number of supporting items, or player exposure does not settle causal truth.

## WORLD05:CONDITION-HISTORY-CHAIN

This interface composes immutable `WORLD04:CONDITION-TRANSITION` records into an append-only relative history without inventing exact time.

Required fields:

- `surface_ref`: exact frozen surface member;
- ordered `transition_refs`: immutable transition references;
- `relative_order_constraints`: only `BEFORE`, `AFTER`, or `SAME_REVIEWED_ERA_UNKNOWN_ORDER`;
- `retained_trace_refs`: material traces that remain part of history after repair or change;
- `current_observation_refs`: bounded present-scope observations, if any;
- `attribution_state`: normally `UNRESOLVED`;
- `sequence_unknowns`: explicit missing ordering/attribution facts;
- `authority_class: RELATIVE_APPEND_ONLY_HISTORY_ONLY`.

The only inherited era order remains:

`ERA:PRE-WORKS → ERA:WORKS-BUILDOUT → ERA:PATCHWORK-PRESENT`.

No exact date, duration, schedule, weather window, travel time, timed-objective guarantee, or NPC reachability is authored.

Repair, retry, compensation, restoration attempt, reconciliation, reinterpretation, or later success can append a new transition but cannot delete a prior material trace or rewrite the history as if the prior state never occurred.

## WORLD05:CHANGE-ENVELOPE

A `WORLD05:CHANGE-ENVELOPE` is descriptive only. It may state:

- `observed_change_class`: `DEGRADATION`, `REPAIR`, `RECONFIGURATION`, `ACCESS_CHANGE`, `RESOURCE_CONDITION_CHANGE`, or `UNKNOWN`;
- evidence refs and counterevidence refs;
- whether a reviewed reversible-condition alternative exists;
- whether attribution is unresolved;
- residual unknowns.

It never authorizes a concrete high-impact or irreversible branch. Any later concrete high-impact/irreversible instance still requires separately reviewed `BranchImpactEvidence`.

## Exact-surface inquiry packs

These are optional inquiry packs, not selected locations or new candidates.

### Shared works junction

`WORLD05:INQUIRY-WORKS-TRACE-CONTINUITY` may compare material traces, bounded operability observations, access/use evidence, and repair-history transitions. It must leave maintainer identity, ownership, office, exact degradation cause, service interval, schedule, and concrete social/character/narrative carrier unresolved.

### Commons edge

`WORLD05:INQUIRY-COMMONS-PRESSURE-HISTORY` may compare use-pressure observations, scoped absences, condition-history changes, and contradictory stewardship/access claims. It must leave ownership, custodian, quota, closure schedule, legitimacy, species catalog, and concrete branch assignment unresolved.

### Cultivation margin

`WORLD05:INQUIRY-CULTIVATION-DEPENDENCY-HISTORY` may compare productive-use/habitat observations, relative condition changes, practical dependency traces, and contradictory resource/access claims. It must leave crop identity, owner, yield, exact capacity, seasonality, exact habitat cause, and concrete cross-root binding unresolved.

No inquiry pack changes the exact three-member set.

## Provisional interfaces emitted for later fan-in

This packet emits typed interfaces only:

- `WORLD05_ROLE:TRIANGULATION_PACKET`
- `WORLD05_ROLE:SCOPE_BOUND_DISAGREEMENT`
- `WORLD05_ROLE:ACCOUNT_DISCRIMINATION_LEDGER`
- `WORLD05_ROLE:CONDITION_HISTORY_CHAIN`
- `WORLD05_ROLE:CHANGE_ENVELOPE`
- `WORLD05_ROLE:PUBLIC_WORLD_EVIDENCE`
- `WORLD05_ROLE:REVERSIBLE_CONDITION_ALTERNATIVE`

No sibling CONT-05 mutable output is consumed or concretely bound. Institution, membership, office occupant, representation, principal character, relationship counterpart, quest instance, branch, disclosure event, final site, ownership, and polity remain inherited open states or typed placeholders until lawful later fan-in.

## Semantic firewalls

The packet preserves all compiler firewalls:

- objective fact, claim, belief, testimony, interpretation, knowledge, player exposure, and generated presentation remain distinct;
- private information defaults to deny and cannot satisfy required nonprivate route minima or foundational play;
- chronology remains relative-only;
- material history remains append-only;
- TRUST, WARMTH, RESPECT, OBLIGATION, RIVALRY, and CAUTION remain independent and separate from institutional legitimacy/public standing;
- world use, repair, repetition, visibility, or evidence prominence cannot establish ownership, consent, representation, legitimacy, or relationship state;
- refusal/nonalignment remains a legal representable state;
- ordinary shared baseline play remains legal and nonfoundational gates cannot compose into a hidden foundational tax;
- no concrete high-impact/irreversible branch is authorized without later reviewed `BranchImpactEvidence`;
- generated presentation cannot mutate authoritative state, truth, history, knowledge, or canon.

## Route-cardinality preservation

This producer authors zero concrete active objectives. Candidate packets, evidence references, accounts, inquiry packs, or history records are not active-route measurements.

| Objective | Minimum | Active concrete instance | Observed active-route count | Status |
|---|---:|---|---:|---|
| `OBJ_CONT:COMPARE_PERSPECTIVES` | 2 materially distinct nonprivate routes | false | null | `NOT_APPLICABLE_NO_ACTIVE_CONCRETE_OBJECTIVE_INSTANCE` |
| `OBJ_CONT:SELECT_DIRECTION` | 2 simultaneously legal differentiated route kinds | false | null | same |
| `OBJ_CONT:CHOOSE_CONTINUED_GOAL` | 2 simultaneously legal distinct goal families | false | null | same |
| `OBJ_CONT02:COMPARE_CAUSAL_ACCOUNTS` | 2 materially distinct nonprivate routes | false | null | same |
| `OBJ_CONT02:SELECT_RESPONSE_PORTFOLIO` | 2 simultaneously legal differentiated response families | false | null | same |
| `OBJ_CONT02:CHOOSE_CONTINUED_GOAL` | 2 simultaneously legal distinct goal families | false | null | same |

Every later concrete active objective must recompute applicable cardinality after exactly these trigger classes: **activation, refusal, rejection, substitution, recovery, route loss**. Private context never counts toward a required nonprivate minimum.

## Exact reopen-condition evaluation

`CLEARED_PACKET_LOCAL` means only this exact packet does not itself trigger the class. It never pre-clears a later authored instance.

| Reopen class | Packet-local result |
|---|---|
| `SOURCE_OR_REVIEW_IDENTITY_DRIFT` | `CLEARED_PACKET_LOCAL` — exact compiler, activation review, fan-in and review identities are bound. |
| `BOUND_INTERFACE_REQUIRES_UNSUPPORTED_CONCRETE_ENTITY` | `CLEARED_PACKET_LOCAL` — only typed interfaces and immutable reviewed refs are emitted. |
| `REVIEWED_BOUNDED_SET_BROADENED_OR_SILENTLY_NARROWED` | `CLEARED_PACKET_LOCAL` — exact three-surface set is unchanged and unselected. |
| `MUTABLE_SIBLING_OUTPUT_CONSUMED_BEFORE_FANIN` | `CLEARED_PACKET_LOCAL` — no sibling CONT-05 mutable output is consumed. |
| `PRIVATE_INFORMATION_REQUIRED_FOR_ROUTE_MINIMUM` | `CLEARED_PACKET_LOCAL` — private refs cannot satisfy nonprivate minima. |
| `PRIVATE_INFORMATION_REQUIRED_FOR_FOUNDATIONAL_PLAY` | `CLEARED_PACKET_LOCAL` — private context creates no foundational gate. |
| `FACT_CLAIM_BELIEF_TESTIMONY_KNOWLEDGE_EXPOSURE_AUTHORITY_COLLAPSE` | `CLEARED_PACKET_LOCAL` — authority classes remain distinct. |
| `RELATIONSHIP_OR_LEGITIMACY_SCALARIZED_OR_AUTOMATICALLY_ALIASED` | `CLEARED_PACKET_LOCAL` — world evidence creates no relationship or legitimacy alias. |
| `MATERIAL_HISTORY_ERASED_BY_RETRY_REPAIR_OR_RECONCILIATION` | `CLEARED_PACKET_LOCAL` — condition history is append-only. |
| `NONFOUNDATIONAL_GATE_COMPOSITION_BECOMES_DEFACTO_FOUNDATIONAL` | `CLEARED_PACKET_LOCAL` — no new baseline-play gate is introduced. |
| `NARRATIVE_ROUTE_CARDINALITY_DROPS_BELOW_REVIEWED_MINIMUM` | `CLEARED_PACKET_LOCAL` — no active objective exists and all six contracts/triggers are preserved. |
| `MUTUALLY_EXCLUSIVE_BRANCHES_BECOME_JOINTLY_REQUIRED` | `CLEARED_PACKET_LOCAL` — inquiry/evidence structures are optional interfaces, not joint branches. |
| `EXACT_TIME_SCHEDULE_WEATHER_TRAVEL_OR_NPC_REACHABILITY_BECOMES_REQUIRED` | `CLEARED_PACKET_LOCAL` — chronology remains relative-only. |
| `CONCRETE_HIGH_IMPACT_OR_IRREVERSIBLE_BRANCH_LACKS_REVIEWED_BRANCH_IMPACT_EVIDENCE` | `CLEARED_PACKET_LOCAL` — no such branch is authorized. |
| `WSN_OUTCOME_REQUIRES_PROMOTION_WITHOUT_EXACT_PREREQUISITE` | `CLEARED_PACKET_LOCAL` — WSN states remain unchanged. |
| `GENERATED_PRESENTATION_MUTATES_AUTHORITATIVE_STATE` | `CLEARED_PACKET_LOCAL` — presentation has zero mutation authority. |
| `STRUCTURAL_RESULT_USED_AS_HIGHER_AUTHORITY` | `CLEARED_PACKET_LOCAL` — every higher-authority conclusion is denied. |

All 17 remain mandatory downstream reopen triggers.

## WSN evidence debt

Unchanged:

- `WSN-E3 = INCONCLUSIVE_TIMED_COVERAGE_BLOCKED`
- `WSN-E4 = NOT_RUN_BLOCKED_BY_EXACT_PREREQUISITE`
- `WSN-E5 = PASS_BOUNDED_MODEL_ONLY`
- `WSN-E8 = INCONCLUSIVE_SCHEDULE_COVERAGE_BLOCKED`

No exact schedule/weather/travel/timed-objective/NPC-reachability, production-persistence, human-quality, aggregate-verification, or implementation-readiness conclusion follows.

## Residual open ledger

Still unresolved by design:

- final selection among the exact three world surfaces;
- any social/site, character/site, or narrative/site concrete binding;
- final ownership, custodian, polity, office, membership, representation, or legitimacy;
- truth of every contested causal account;
- exact chronology, schedule, weather, travel, timed-objective, or NPC reachability;
- crop/species/yield catalog and exact resource capacity;
- private-context holder and lawful disclosure;
- concrete high-impact/irreversible BranchImpactEvidence;
- inherited OPEN bindings 002/003/004;
- human quality, production persistence, aggregate verification, implementation readiness, gameplay implementation, engine selection, release/production, decision, final canon, and canonicalization.

Conceptual `W2-CONTENT-SYN-CONT-05` remains unmaterialized until all five exact CONT-05 reviewed tokens coexist.

## Self-review

Attacks performed: frozen-source drift; bounded-set widening/silent narrowing; hidden site selection/preference; causal-truth laundering; majority/score/rank authority laundering; scoped-absence globalization; fact/claim/testimony/interpretation/knowledge/exposure collapse; private-information leakage; sibling mutable consumption; unsupported concrete binding; exact-time/schedule/weather/travel/reachability invention; history erasure; ownership/legitimacy inference; relationship/legitimacy aliasing; refusal/agency bypass; hidden foundational gate; route-cardinality weakening or fabricated measurement; mutually exclusive branch coupling; missing BranchImpactEvidence; WSN upgrade; generated-state mutation; engine coupling; higher-authority inflation.

Findings: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR**.

Required next gate: exactly one fresh independent/degraded-independent review of this exact immutable packet. A clean review may grant only `W2-CONTENT-WORLD-CONT-05_REVIEWED`; it grants no early fan-in, integration, verification-PASS, readiness, gameplay implementation, engine selection, release/production, human-quality, decision/final-canon, or canonical authority.
