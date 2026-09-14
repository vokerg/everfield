# W2 character/relationship continuation 02 — bounded candidate

## Status and authority

Mission: `W2-CONTENT-CHAR-CONT-02` / Issue #1051.

This is an engine-neutral, **NOT_CANONICAL** continuation candidate derived only from the clean-reviewed CONT-01 fan-in. It deepens principal-character role slots, relationship/history semantics, agency/refusal, knowledge provenance, and change-arc structure without selecting final named actors, biographies, memberships, romances/family outcomes, secret holders, or sibling CONT-02 bindings.

Producer base: `main@586d4cf9e6ec413246184c27a23424f699ad0137`. Canonical Planning Program v1 blob remains `e3120ec203c4156328770aa86c12fbb7187966dc`, bound by Issue #6 comment `5245368879` with activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e`.

Activation authority is the clean required review Issue #1063 terminal comment `5654948592`, disposition `CLEAN_FOR_BOUNDED_CONTENT_FRONTIER_CONTINUATION_02_ACTIVATION`.

Frozen predecessor consumption authority:
- synthesis Issue #986 terminal `5644862732`;
- exact fan-in Markdown/YAML blobs `b39f535dc71639f3ebc67e33a2d692a2b3a77588` / `78148f50649ada789feb3cca61182e18465bb628`;
- required Review #1009 terminal `5645006619`;
- disposition `CLEAN_FOR_BOUNDED_CONTENT_CONTINUATION_CONSUMPTION`;
- review report blob `830926e5dea3f264b016a61a3268f272b0bc3c2e`.

No sibling CONT-02 mutable output is an input to this packet.

## Character continuation rule

This root defines **character structures and role envelopes**, not final fiction. A slot can state behavioral affordances, history requirements, knowledge rules, agency constraints, and provisional cross-root interfaces while leaving concrete identity `OPEN`.

The packet preserves the reviewed character relationship vector exactly:
`TRUST`, `WARMTH`, `RESPECT`, `OBLIGATION`, `RIVALRY`, `CAUTION`.

Those dimensions are not collapsed into one reputation score, are not aliases for social standing or institutional legitimacy, and may change only through typed cause/evidence. Material relationship history is append-only.

## Principal-character role envelopes

### `CHAR02:SLOT:ROOTED-PRACTITIONER`

Purpose: represent a principal-character slot whose perspective can be grounded in repeated practical interaction with one or more reviewed world-use surfaces without implying ownership, custodianship, institutional office, or final occupation.

Allowed predecessor world interfaces:
- `WORLD_IFACE:CULTIVATION-MARGIN`;
- `WORLD_IFACE:SHARED-WORKS-JUNCTION`;
- `WORLD_IFACE:COMMONS-EDGE`.

Required character semantics:
- practical familiarity is distinct from objective authority;
- observed work can establish only bounded observation/provenance;
- care, use, or repair effort never implies ownership or legitimacy;
- refusal to provide labor, disclose knowledge, accept obligation, or reconcile remains representable.

Provisional sibling hooks: `SOCIAL_ROLE:PRACTICE_STAKE`, `NARR_ROLE:CONT_PERSPECTIVE_HOLDER`, `NARR_ROLE:CONT_AFFECTED_TIE`.

### `CHAR02:SLOT:HISTORY-INTERPRETER`

Purpose: represent a principal-character slot able to interpret records, traces, testimony, or memory while preserving the fan-in distinction between objective observation, claim, belief, testimony, interpretation, and knowledge.

Predecessor world interface: `WORLD_IFACE:HISTORY-TRACE`.

Rules:
- interpretation never promotes itself to objective history;
- testimony carries provenance and may conflict with other testimony;
- strong confidence does not erase the reviewed unresolved fragmentation cause;
- player exposure does not automatically become this character's knowledge;
- private context remains deny-by-default.

Provisional sibling hooks: `SOCIAL_ROLE:HISTORY_STAKE`, `NARR_ROLE:CONT_PERSPECTIVE_HOLDER`, `NARR_ROLE:CONT_PRIVATE_CONTEXT_HOLDER`.

### `CHAR02:SLOT:BOUNDARY-MEDIATOR`

Purpose: represent a principal-character slot whose change pressure can involve movement, exchange, access, or conflicting community claims without fixing faction membership, external geography, route timetables, or diplomatic office.

Predecessor world interface: `WORLD_IFACE:OUTER-CONNECTION`.

Rules:
- mediation or contact does not imply institutional membership;
- repeated access does not imply route safety, schedule authority, or private access;
- compromise may preserve disagreement;
- a refusal to mediate or commit is a valid agency result and cannot be silently treated as failure-state character regression.

Provisional sibling hooks: `SOCIAL_ROLE:CONFLICT_COUNTERPART`, `SOCIAL_ROLE:INSTITUTION_CONTACT`, `NARR_ROLE:CONT_PERSPECTIVE_HOLDER`.

### `CHAR02:SLOT:AFFECTED-TIE-CARRIER`

Purpose: expose a bounded principal relationship-history carrier for later narrative consequence without deciding whether the tie is romantic, familial, professional, factional, or otherwise final.

Rules:
- the concrete counterpart is `OPEN`;
- tie type is `OPEN_BOUNDED_SET`;
- every material change references typed history evidence;
- current warmth/trust/respect/etc. never erases prior breach, refusal, obligation, repair, or disagreement;
- no route may force relationship improvement merely because the player succeeds elsewhere.

Provisional sibling hooks: `SOCIAL_ROLE:COMMUNITY_TIE`, `NARR_ROLE:CONT_AFFECTED_TIE`.

## Relationship and history ledger

Every material relationship event is append-only and uses a stable `REL02:*` identity.

Required fields:
- participants as unresolved slot/entity references;
- branch scope;
- event class;
- affected relationship dimensions;
- signed/typed delta or qualitative transition;
- explicit cause;
- evidence/provenance;
- voluntariness / refusal state;
- knowledge prerequisites;
- persistence/reversibility;
- repair/compensation links if applicable.

Allowed event classes:
- `OBSERVED_SUPPORT`;
- `COMMITMENT`;
- `BREACH`;
- `REFUSAL`;
- `DISCLOSURE`;
- `WITHHELD_DISCLOSURE`;
- `CONFLICT`;
- `COMPROMISE`;
- `REPAIR_ATTEMPT`;
- `RESTITUTION`;
- `RECONTEXTUALIZATION`.

Rules:
1. list order alone is not chronology authority;
2. repair never deletes a material breach;
3. retry never rewrites prior refusal into consent;
4. a relationship event cannot by itself grant objective truth or private information;
5. social standing/legitimacy changes are separate vectors and require their own typed evidence;
6. repeated low-information interaction cannot accumulate unlimited material change.

## Change-arc contract

A candidate arc is a typed state machine, not a predetermined redemption or convergence path.

Arc states:
- `ARC02:BASELINE`;
- `ARC02:PRESSURE_PRESENT`;
- `ARC02:CHOICE_AVAILABLE`;
- `ARC02:RESPONSE_RECORDED`;
- `ARC02:AFTERMATH`;
- `ARC02:REOPENED`.

A material arc transition requires:
- a declared trigger/cause;
- evidence/provenance;
- affected relationship or belief/knowledge dimensions;
- agency mode: `VOLUNTARY | REFUSED | DEFERRED | CONSTRAINED`;
- branch scope;
- reversibility/persistence class;
- history entries created, never overwritten;
- knowledge prerequisites;
- reopen condition where uncertainty remains.

No transition is mandatory merely because it is offered. `REFUSED` or `DEFERRED` can preserve a valid continued-play state. A refusal cannot be bypassed through reputation, legitimacy, repeated gifting, repeated dialogue, proximity, quest completion, or player knowledge.

Material change must be non-grind: repeated equivalent low-information actions cannot substitute for a new cause/evidence event.

## Knowledge and private-information contract

Character epistemic state is separate from truth and from player exposure.

Knowledge states:
- `KNOWN_FROM_OBSERVATION`;
- `KNOWN_FROM_DISCLOSURE`;
- `KNOWN_FROM_PUBLIC_RECORD`;
- `BELIEVED`;
- `HEARD_CLAIM`;
- `INFERRED`;
- `SUSPECTED`;
- `UNKNOWN`.

Every non-`UNKNOWN` state records provenance. A character may hold a false belief or contested claim without changing objective world truth.

Private information defaults to `DENY`. Allowed acquisition routes remain:
- explicit holder disclosure;
- separately validated authority effect;
- public-record scope where the information is actually public.

Relationship score, standing, legitimacy, role membership, physical proximity, repeated interaction, and player exposure never grant private information automatically. Onward private sharing is also deny-by-default.

`NARR_ROLE:CONT_PRIVATE_CONTEXT_HOLDER` remains `OPEN_OPTIONAL`; this packet does not assign a holder or require private context for route cardinality or completion.

## Provisional world interfaces

The reviewed fan-in already resolved these character-facing world aliases, and this continuation preserves them without reading sibling CONT-02 output:

- `WORLD_ROLE:archive_or_memory_surface` → `WORLD_IFACE:HISTORY-TRACE`;
- `WORLD_ROLE:repair_or_shared_work_surface` → `WORLD_IFACE:SHARED-WORKS-JUNCTION`;
- `WORLD_ROLE:boundary_route_or_exchange_surface` → `WORLD_IFACE:OUTER-CONNECTION`.

The following remain unresolved exactly as predecessor authority requires:
- `WORLD_ROLE:shared_decision_surface` → `OPEN`;
- `WORLD_ROLE:care_or_gathering_surface` → `OPEN`;
- `WORLD_ROLE:contested_project_or_resource_surface` → `BOUNDED_SET` with exactly {`WORLD_IFACE:SHARED-WORKS-JUNCTION`, `WORLD_IFACE:WATER-DEPENDENCY`, `WORLD_IFACE:COMMONS-EDGE`}; concrete target selection remains unresolved and downstream-owned.

This root does not select concrete siblings or new world identities.

## Provisional social and narrative interfaces

Social hooks are role requirements only:
- `SOCIAL_ROLE:PRACTICE_STAKE`;
- `SOCIAL_ROLE:HISTORY_STAKE`;
- `SOCIAL_ROLE:CONFLICT_COUNTERPART`;
- `SOCIAL_ROLE:INSTITUTION_CONTACT`;
- `SOCIAL_ROLE:COMMUNITY_TIE`.

They do not assert faction membership, institutional office, legitimacy, authority, friendship, kinship, or final counterpart identity.

Narrative hooks:
- `NARR_ROLE:CONT_PERSPECTIVE_HOLDER`;
- `NARR_ROLE:CONT_AFFECTED_TIE`;
- `NARR_ROLE:CONT_PRIVATE_CONTEXT_HOLDER`.

Concrete binding belongs only to later `W2-CONTENT-SYN-CONT-02` after all five exact clean-reviewed CONT-02 root tokens coexist.

## Agency and refusal invariants

Refusal must remain representable in at least these domains:
- disclosure;
- labor;
- care;
- commitment;
- risk acceptance;
- mediation;
- reconciliation.

A refusal can carry consequences, but it cannot be silently rewritten as consent or force a hidden universal progression gate. Compromise may preserve disagreement. Current relationship state may worsen without removing baseline shared foundational play.

No final romance/family ending, institutional membership, loyalty outcome, redemption outcome, or irreversible identity change is authorized here.

## Chronology and branch scope

Only relative chronology is permitted. Character events can assert `before`, `after`, or `contained-by` relations when evidence exists, but no exact dates, durations, schedules, travel times, weather windows, or NPC reachability guarantees are created.

Branch facts stay branch-scoped. Mutually exclusive histories are not jointly required. Cross-branch reconciliation requires explicit reviewed authority rather than prose collapse.

## WSN evidence boundary

No WSN result is changed:
- E3 `INCONCLUSIVE_TIMED_COVERAGE_BLOCKED`;
- E4 `NOT_RUN_BLOCKED_BY_EXACT_PREREQUISITE`;
- E5 `PASS_BOUNDED_MODEL_ONLY`;
- E8 `INCONCLUSIVE_SCHEDULE_COVERAGE_BLOCKED`.

Therefore this packet cannot establish exact schedules, actor availability, timed dialogue windows, travel/weather guarantees, NPC reachability, production persistence, human-quality PASS, aggregate verification PASS, or implementation readiness.

## Residual OPEN ledger

- final named principal characters;
- final biographies, occupations, faction/institution memberships, romances/family/endings;
- final counterpart identities for relationship histories;
- concrete social-role occupants;
- concrete narrative branch/character assignments;
- optional private-context holder and disclosure event;
- exact dates/durations/schedules/reachability;
- final truth of contested historical claims;
- concrete irreversible/high-impact character/world consequence evidence;
- final canon, human-quality evidence, production validation, and implementation readiness.

## Self-review

Adversarial checks covered sibling mutable consumption, final-biography invention, relationship scalarization, history erasure, consent/refusal bypass, grind-based arc forcing, secret leakage, truth/knowledge collapse, social-legitimacy aliasing, chronology overreach, hidden progression gates, irreversible consequence authorization, WSN laundering, engine coupling, scope expansion, and higher-authority inflation.

Result: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR** in this bounded producer scope.

Required next gate: one fresh independent/degraded-independent review of the exact immutable packet. A clean review may grant only `W2-CONTENT-CHAR-CONT-02_REVIEWED` for later bounded fan-in. It grants no integration, verification PASS, implementation readiness, engine selection, release, decision, final-canon, or canonical authority.
