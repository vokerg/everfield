# W2 content continuation fan-in — reviewed-root reconciliation

## Status and authority

Mission: `W2-CONTENT-SYN-CONT-01` / Issue #986.

This is a bounded, engine-neutral, **NOT_CANONICAL** synthesis candidate over five immutable clean-reviewed continuation roots. It does not alter any root packet, review result, WSN result, engine decision, implementation-readiness state, release state, or canonical content authority.

Synthesis base: `main@68bc225d2cef9c77857be6eedd79b23c3e7ae353`. Canonical Planning Program v1 blob remains `e3120ec203c4156328770aa86c12fbb7187966dc`, bound by Issue #6 comment `5245368879` with activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e`.

## Frozen reviewed inputs

| Root | Exact source | Clean review | Token |
| --- | --- | --- | --- |
| World | #909 / PR #913 @ `73b549569481a3a937599a152eb87ada806425e7` | #914 comment `5580243890` | `W2-CONTENT-WORLD-CONT-01_REVIEWED` |
| Social | #812 / PR #886 @ `acfcf5220e3ebd31789d9710fe35f75bf659d23d` | #896 comment `5580240650` | `W2-CONTENT-SOCIAL-CONT-01_REVIEWED` |
| Character | #813 / PR #947 @ `5eaaac7b6a63e27c722f1d971317c46c58a8b303` | #984 comment `5622764118` | `W2-CONTENT-CHAR-CONT-01_REVIEWED` |
| Narrative | #972 / PR #981 @ `15f1d8549e984519958bcb3bb9d668fdfe60f888` | #982 comment `5622367842` | `W2-CONTENT-NARR-CONT-01_REVIEWED` |
| Evaluation | #815 / PR #860 @ `4c9fa8bfe989ff80ab2d74b8fae1baa862c540dd` | #875 comment `5557367340` | `W2-CONTENT-EVAL-CONT-01_REVIEWED` |

Review tokens authorize consumption of those exact immutable packets. They do not require source-PR integration and do not upgrade any source packet to canonical content.

## Reconciliation rule

Fan-in binds **semantic interfaces**, not final fiction. A binding is closed only where the reviewed roots jointly support the same bounded meaning. Ambiguous aliases become `BOUNDED_SET` or remain `OPEN`; they are never resolved by guessing a character, faction, owner, timetable, historical cause, or private-information holder.

### World-facing bindings

| Requested role/interface | Fan-in result | Evidence-preserving interpretation |
| --- | --- | --- |
| `WORLD_ROLE:CULTIVATION_ZONE` | **BOUND_INTERFACE** → `WORLD_IFACE:CULTIVATION-MARGIN` | Both preserve productive use, water condition and habitat continuity as separate dimensions; crops, ownership, yields and timed planting remain unresolved. |
| `WORLD_ROLE:CONTESTED_COMMON` | **BOUND_INTERFACE** → `WORLD_IFACE:COMMONS-EDGE` | Shared access/habitat pressure is explicitly contested without settling custodians, quotas or ownership. |
| `WORLD_ROLE:TRANSIT_EDGE` | **BOUND_INTERFACE** → `WORLD_IFACE:OUTER-CONNECTION` | Represents movement/exchange across the bounded setting only; route timetable and external geography remain unknown. |
| `WORLD_ROLE:HUB_COMMUNITY` | **BOUND_LOCUS** → `LOC:SETTLEMENT-CORE` | A reviewed location identity is available; no new institution, polity or ownership claim is inferred. |
| `WORLD_ROLE:COMMON_RESOURCE` | **BOUNDED_SET** → {`WORLD_IFACE:WATER-DEPENDENCY`, `WORLD_IFACE:COMMONS-EDGE`} | The social contract permits resource pressure but does not determine whether a later instance concerns water dependency or commons access. |
| `WORLD_ROLE:SENSITIVE_SITE` | **OPEN** | `LOC:OLD-WORKS` is compatible but sensitivity is not an objective property established by the world root. |
| `WORLD_ROLE:CONT_CONTESTED_SITE` | **BOUNDED_SET** → {`WORLD_IFACE:SHARED-WORKS-JUNCTION`, `WORLD_IFACE:COMMONS-EDGE`, `WORLD_IFACE:CULTIVATION-MARGIN`} | Narrative can target a contested surface without selecting one concrete site here. |
| `WORLD_ROLE:CONT_HISTORY_OR_EVIDENCE_SOURCE` | **BOUND_INTERFACE** → `WORLD_IFACE:HISTORY-TRACE` | Supports material/record evidence while preserving unresolved attribution and exact chronology. |
| `WORLD_ROLE:CONT_AFTERMATH_SURFACE` | **BOUNDED_SET** → reviewed world interfaces affected by the selected branch | No concrete aftermath location is chosen until a later authored instance is separately reviewed. |

Character world-role aliases close only where meaning is exact enough: `archive_or_memory_surface` → `WORLD_IFACE:HISTORY-TRACE`; `repair_or_shared_work_surface` → `WORLD_IFACE:SHARED-WORKS-JUNCTION`; `boundary_route_or_exchange_surface` → `WORLD_IFACE:OUTER-CONNECTION`. `shared_decision_surface`, `care_or_gathering_surface`, and `contested_project_or_resource_surface` remain bounded/open because multiple reviewed world interfaces fit.

### Social, character, and narrative bindings

The social root establishes reviewed institutions and pressures, but it does not establish which principal character permanently fills `CHAR_ROLE:FACTION_LIAISON`, `CHAR_ROLE:INDEPENDENT_MEDIATOR`, or `CHAR_ROLE:COMMUNITY_NEIGHBOR`. Those assignments remain **OPEN**. This prevents biography, membership, or faction-canon invention.

Narrative `SOCIAL_ROLE:CONT_AFFECTED_GROUP`, `CONT_STEWARDSHIP_OR_SERVICE`, and `CONT_COUNTERPRESSURE` bind to the **typed social pressure/obligation surface**, not to one mandatory faction. A concrete branch may later select compatible carriers from `SOC-PRESS-001..004` only with branch-local evidence and review.

Narrative `CHAR_ROLE:CONT_PERSPECTIVE_HOLDER` binds to the character packet's bounded testimony/provenance capability: any concrete assignment must preserve that character's explicit knowledge provenance. `CHAR_ROLE:CONT_AFFECTED_TIE` binds to the reviewed multidimensional relationship/history contract, not to a universal relationship score. `CHAR_ROLE:CONT_PRIVATE_CONTEXT_HOLDER` remains **OPEN and optional**; private context stays deny-by-default, never counts toward required route minima, and may remain unused.

World-root hooks such as `SOCIAL_ROLE:WATER-DEPENDENT-USER`, `PUBLIC-WORKS-STAKE`, `COMMONS-STAKE`, `LAND-USE-STAKE`, `CHAR_ROLE:HISTORY-INTERPRETER`, `CHAR_ROLE:LOCAL-USER`, and the four `NARR_ROLE:*` hooks remain typed compatibility points. No exact actor/character/quest assignment is required to make this fan-in coherent.

## Epistemic and information reconciliation

The roots agree on one authority ordering:

1. reviewed objective world observations may support bounded objective facts;
2. claims, interpretations, beliefs and testimony remain non-authoritative unless a separately reviewed authority effect says otherwise;
3. character knowledge requires an allowed acquisition/disclosure route;
4. player exposure is not character knowledge;
5. relationship, public standing, legitimacy, role membership and generated presentation do not grant private information;
6. generated text never mutates truth, secret, branch, relationship, knowledge or canon state.

No cross-root contradiction was found under that ordering. In particular, the world root's unresolved fragmentation cause remains unresolved even if an institution or character makes a strong claim about it.

## Chronology and branch reconciliation

The only current world chronology authority is the relative order `ERA:PRE-WORKS → ERA:WORKS-BUILDOUT → ERA:PATCHWORK-PRESENT` plus reviewed relative layer/event relations. The fan-in therefore permits relative `before/after/contained-by` constraints but **no exact dates, durations, opening hours, actor schedules, travel times, weather windows, or NPC reachability guarantees**.

Narrative branch facts stay branch-scoped. Mutually exclusive branches are never jointly required. Social and relationship history are append-only: retry, restitution, repair, compromise, or reconciliation may update current effects but may not erase material history.

## Progression gates and foundational play

Social and narrative continuation each report foundational gate count `0`. Fan-in preserves that result.

- Social specialization/optional/branch-exclusive gates cannot become universal progression taxes.
- Narrative `GATE:NARR-CONT:CONSEQUENCE_REASSESSMENT` remains OPTIONAL.
- `GATE:NARR-CONT:PUBLIC_RECOMMITMENT` remains BRANCH_EXCLUSIVE.
- `GATE:NARR-CONT:AFTERMATH_STEWARDSHIP` remains SPECIALIZATION.
- Relationship worsening, faction standing, legitimacy, service scarcity, private information, or unavailable specialists cannot remove baseline movement, ordinary community interaction, public information, basic repair/crafting, baseline cultivation, or other shared foundational play.

Composition that would make several non-foundational gates jointly unavoidable is a reopen condition, not an implied new foundational gate.

## Narrative route-cardinality preservation

The exact remediation reviewed by #982 is preserved without weakening:

- `OBJ_CONT:COMPARE_PERSPECTIVES`: at least **2 materially distinct non-private** routes while active; private context never counts; underflow transitions to `STATE_CONT:PRE_COMPARE_DEFERRED` before activation.
- `OBJ_CONT:SELECT_DIRECTION`: at least **2 simultaneously legal materially differentiated direction route kinds**; underflow transitions to `STATE_CONT:PRE_DIRECTION_DEFERRED`.
- `OBJ_CONT:CHOOSE_CONTINUED_GOAL`: at least **2 simultaneously legal materially distinct goal families**; underflow transitions to `STATE_CONT:PRE_GOAL_SELECTION_DEFERRED`.

Recovery and substitution must recompute cardinality before the required objective continues. No world/social/character binding in this synthesis is allowed to collapse a required route set below those minima.

## Relationship, legitimacy, agency, and consequence reconciliation

Character relationship dimensions and social relationship/legitimacy dimensions are distinct vectors. They are **not aliases** and may not be scalarized into one reputation score. Any cross-vector effect requires a typed cause and evidence; history remains durable.

Character refusal remains legal in disclosure, labor, care, commitment, risk and reconciliation domains. Social compromise may preserve disagreement. Player favor, success, standing, or legitimacy never forces an arc conversion.

High-impact consequences require visible precommitment tradeoffs, persistence/reversibility semantics, affected-goal impact, and recovery/mitigation/compensation or meaningful alternative play. An irreversible concrete world change remains unauthorized here and would require separate BranchImpactEvidence plus review.

## Evaluation result

The reviewed evaluation contract was applied to the reconciled candidate.

- Entity/type scope: **PASS** for bound interfaces; ambiguous role aliases are retained as typed OPEN/BOUNDED_SET rather than silently conflated.
- Epistemic/secret/knowledge separation: **PASS**.
- Relative chronology / unsupported exact schedule: **PASS**, with exact timing deliberately blocked.
- Branch compatibility and durable history: **PASS**.
- Relationship multidimensionality / anti-grind / agency: **PASS**.
- Progression-gate classification and baseline-play preservation: **PASS**.
- Quest graph, failure/recovery, and reviewed route-cardinality minima: **PASS** at bounded structural level.
- Consequence observability/recovery/alternative obligations: **PASS** at bounded structural level.
- Originality/reference and vertical-slice authority: **PASS**; the Old Works slice remains noncanonical regression/reference material.
- Generated-content authority: **PASS**.
- WSN identity/outcome preservation: **PASS**.
- Mutable sibling dependency: **PASS**; all five inputs are frozen immutable reviewed packets.

These are structural fan-in results, not human-quality, fun, production, verification, readiness, or canon evidence.

## Residual OPEN ledger

1. Concrete `WORLD_ROLE:SENSITIVE_SITE` identity.
2. Final choice within `WORLD_ROLE:COMMON_RESOURCE` and narrative contested/aftermath bounded sets for any authored instance.
3. Concrete principal-character ↔ social-role/institution assignments.
4. Concrete narrative branch ↔ faction/character/site assignments.
5. Optional private-context holder and any lawful disclosure event.
6. Exact chronology position for new social/relationship events beyond reviewed relative ordering.
7. GameTimePolicy, schedules, closures, timed windows, weather/travel interaction, NPC reachability.
8. Concrete BranchImpactEvidence for any high-impact/irreversible authored branch.
9. Final biographies, memberships, romances/family/endings, ownership, polities, crop/species catalogs and final world causes.
10. Human-quality evidence, production persistence, aggregate verification, final canon and implementation readiness.

No OPEN item is silently converted into a prerequisite for current foundational play.

## WSN evidence debt

No WSN experiment is rerun, renamed, duplicated, or upgraded:

- E1 PASS
- E2 PASS
- E3 `INCONCLUSIVE_TIMED_COVERAGE_BLOCKED`
- E4 `NOT_RUN_BLOCKED_BY_EXACT_PREREQUISITE`
- E5 `PASS_BOUNDED_MODEL_ONLY`
- E6 PASS
- E7 PASS
- E8 `INCONCLUSIVE_SCHEDULE_COVERAGE_BLOCKED`
- E9 PASS

E3/E4/E8 can move only after the exact reviewed timing/schedule/reachability prerequisites exist. E5 remains bounded-model evidence and proves no production persistence.

## Self-review

Adversarial checks covered root identity, role-binding non-invention, epistemic leakage, chronology overreach, branch incompatibility, hidden foundational-gate composition, relationship scalarization/history loss, character-agency collapse, narrative cardinality soft locks, consequence insufficiency, WSN laundering, vertical-slice canon inflation, generated authority, engine coupling, scope expansion, and higher-authority inflation.

Result: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR** in this bounded synthesis scope.

Required next gate: one fresh independent/degraded-independent review of the exact immutable three-file synthesis packet. A clean review may grant only `CLEAN_FOR_BOUNDED_CONTENT_CONTINUATION_CONSUMPTION`; it grants no integration, verification PASS, implementation readiness, engine selection, release, final canon, decision, or canonical authority.
