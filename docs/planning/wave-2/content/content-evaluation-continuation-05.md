# CONT-05 bounded content evaluation continuation candidate

**Mission:** `W2-CONTENT-EVAL-CONT-05`  
**Issue:** #1235  
**State:** `PRODUCER_CANDIDATE_NONCANONICAL`  
**Canonicality:** `NOT_CANONICAL`  
**Engine dependency:** engine-neutral

This packet defines a parameterized structural evaluator for later CONT-05 fan-in. It consumes only the exact clean-reviewed CONT-04 fan-in and the terminal clean CONT-05 activation route. It does **not** consume mutable sibling CONT-05 output, apply itself to unfinished sibling packets, select fiction, manufacture runtime evidence, or establish human quality, empirical verification, implementation readiness, production validity, final canon, or canonical authority.

## Frozen authority and input

Execution begins from `main@568848d9e9f4fb798d43aca01f1e4c2e29a00b2f` under ownership comment `5771611100`.

Canonical planning basis:
- binding: Issue #1147 terminal comment `5675066392`;
- program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`;
- activation: `87c85cecfa9a2ffa464c4b36816a138bf41441af`.

CONT-05 routing basis:
- compiler #1230 terminal/integration: `5755329122` / `5755436699`;
- activation Review #1236 terminal/integration: `5755392675` / `5755498638`;
- activation disposition: `CLEAN_FOR_BOUNDED_CONTENT_FRONTIER_CONTINUATION_05_ACTIVATION`.

The only mutable-content predecessor consumed is the exact clean-reviewed CONT-04 fan-in:
- producer #1225 terminal `5750440511`, head `a0ccb6eb0568cc248d3c23b041414123aba39a31`;
- Markdown blob `ed8adb966ac467896ead65a773695b30b81e9974`;
- YAML blob `d2f03329975bbb8ceb0f4765c367e18fa04a8bf7`;
- handoff blob `a41a56071e5da46461b246fa3785412cfef64d25`;
- required Review #1228 terminal `5750477894`;
- review disposition `CLEAN_FOR_BOUNDED_CONTENT_CONTINUATION_04_CONSUMPTION`;
- review report/handoff blobs `67c27ba6c0b6207ac7033bec5ba7927f9fb9a2dc` / `e547515253e0650262072cd119358de7e58ff5bc`.

No sibling CONT-05 mutable bytes are inputs to this packet.

## Scope

This candidate may define:
- exact immutable input identity requirements for later CONT-05 fan-in evaluation;
- a structural check registry and evidence contract;
- exact route-cardinality measurement semantics;
- packet-local reopen-condition classification;
- cross-artifact consistency checks;
- semantic and authority firewalls.

This candidate may not:
- inspect unfinished sibling CONT-05 mutable output;
- rank or score creative alternatives;
- select a site, owner, polity, office, institution, member, character, counterpart, narrative branch, causal truth, chronology, schedule, or final fiction;
- convert a structural check into human-quality or production evidence;
- manufacture runtime route counts or BranchImpactEvidence;
- resolve WSN evidence debt;
- create a concrete objective instance;
- grant integration, verification PASS, implementation/readiness, gameplay implementation, engine, release, production, decision, final-canon, human-quality, or canonical authority.

## Inherited state contract

Every evaluation application must preserve the exact state vocabulary below unless a later separately reviewed authority lawfully changes it.

| Binding | Required state | Evaluator rule |
|---|---|---|
| `SYN-CONT02-OPEN-001` | `OPEN_BOUNDED_SET` | Detect widening or silent narrowing; do not select a member. |
| `SYN-CONT02-OPEN-002` | `OPEN` | Reviewed hypotheses/refinements may remain metadata; they cannot replace the literal state. |
| `SYN-CONT02-OPEN-003` | `OPEN` | Typed interfaces may remain metadata; no office, membership, representation, legitimacy, or consent follows. |
| `SYN-CONT02-OPEN-004` | `OPEN` | Compatibility envelopes may remain metadata; no concrete cross-root binding follows. |
| `SYN-CONT02-OPEN-005` | `OPEN_OPTIONAL` | Private context remains optional, deny-by-default, nonfoundational, and excluded from nonprivate minima. |
| `SYN-CONT02-OPEN-006` | `UNRESOLVED` | Claims, testimony, records, confidence, or repetition cannot establish contested causal truth. |
| `SYN-CONT02-OPEN-007` | `RELATIVE_ONLY` | Exact chronology is not inferred. |
| `SYN-CONT02-OPEN-008` | `BLOCKED_BY_EXACT_PREREQUISITE` | Exact schedule/weather/travel/timed-objective/NPC-reachability claims remain blocked. |
| `SYN-CONT02-OPEN-009` | `LATER_EMPIRICAL_EVIDENCE_REQUIRED` | Structural evidence cannot substitute for reviewed empirical BranchImpactEvidence. |
| `SYN-CONT02-OPEN-010` | `FINAL_CANON_NOT_AUTHORIZED` | Final content selection remains outside this evaluator. |
| `SYN-CONT02-OPEN-011` | `HIGHER_AUTHORITY_NOT_ESTABLISHED` | Structural results do not establish higher authority. |

Descriptive refinements never silently rename or narrow `OPEN-002`, `OPEN-003`, or `OPEN-004`.

## EVAL05:INPUT-PACKET-CONTRACT

The evaluator is defined now and applied only later, after a lawful fan-in route exists. A valid future application must bind immutable identities for all judged packets and their required reviews. At minimum it must record:
- producer issue, terminal comment, head/work SHA, artifact blob SHAs, and exact changed paths;
- required review issue, terminal comment, disposition, report/handoff blob SHAs;
- expected reviewed token;
- evaluator version/blob identity;
- current canonical binding and the fan-in episode that requested evaluation.

Expected CONT-05 root tokens are:
- `W2-CONTENT-WORLD-CONT-05_REVIEWED`;
- `W2-CONTENT-SOCIAL-CONT-05_REVIEWED`;
- `W2-CONTENT-CHAR-CONT-05_REVIEWED`;
- `W2-CONTENT-NARR-CONT-05_REVIEWED`;
- `W2-CONTENT-EVAL-CONT-05_REVIEWED`.

This packet does not assert that those five tokens currently coexist. It does not materialize `W2-CONTENT-SYN-CONT-05`.

## EVAL05:EVIDENCE-CONTRACT

Every nontrivial check result must carry evidence references. Accepted evidence classes are immutable repository/GitHub identities, exact artifact paths at a work SHA, or later separately authorized empirical evidence. Unsupported prose assertion alone is insufficient.

Result vocabulary is deliberately non-numeric:
- `PASS_BOUNDED_STRUCTURAL` — the exact structural invariant is preserved for the judged packet;
- `TRIGGERED` — a declared reopen/failure condition is present;
- `BLOCKED_BY_EXACT_PREREQUISITE` — the requested conclusion depends on evidence that does not exist or is not authorized;
- `NOT_APPLICABLE_NO_ACTIVE_CONCRETE_OBJECTIVE_INSTANCE` — no concrete active objective exists for a route measurement;
- `NOT_EVALUATED_IDENTITY_INCOMPLETE` — immutable judged identity is incomplete, so evaluation fails closed.

No aggregate numeric score, weighted score, hidden quality score, pass percentage, or ranking is permitted.

## EVAL05:CHECK-REGISTRY

A later application must evaluate at least the following structural checks independently:

1. **E05-IDENTITY** — exact producer/review/head/blob/path/token identities are complete and mutually consistent.
2. **E05-STATE-VOCAB** — all 11 inherited states remain exact; refinements do not replace inherited states.
3. **E05-SIBLING-BARRIER** — mutable sibling output was not consumed before the lawful reviewed-token fan-in barrier.
4. **E05-ENTITY-SCOPE** — no unsupported concrete entity, occupant, membership, office, representation, legitimacy, counterpart, or final selection is smuggled through an interface.
5. **E05-EPISTEMIC** — fact, claim, belief, testimony, interpretation, institutional record, knowledge, player exposure, confidence, and generated presentation remain distinct.
6. **E05-PRIVATE** — private information remains deny-by-default, exact-scope, optional, nonfoundational, and excluded from required nonprivate minima.
7. **E05-CHRONOLOGY** — relative-only chronology remains separate from exact date/duration/schedule/weather/travel/timed-objective/NPC-reachability claims.
8. **E05-HISTORY** — material branch/refusal/disclosure/relationship/repair history remains append-only.
9. **E05-RELATIONSHIP** — TRUST, WARMTH, RESPECT, OBLIGATION, RIVALRY, and CAUTION remain independent and separate from legitimacy/public standing.
10. **E05-AGENCY** — refusal, withdrawal, deferral, nonalignment, and unavailable dependencies remain legal and cannot be ground away by gifts, standing, proximity, repetition, prior success, or relationship state.
11. **E05-FOUNDATIONAL** — nonfoundational gates do not compose into a hidden baseline-play tax.
12. **E05-CARDINALITY** — all six route-cardinality contracts use exact minima and lawful null/N/A semantics.
13. **E05-RECOMPUTE** — route measurements are recomputed after activation, refusal, rejection, substitution, recovery, or route loss.
14. **E05-REOPEN** — all 17 reopen-condition classes are present and classified packet-locally with evidence.
15. **E05-BRANCH-IMPACT** — no concrete high-impact/irreversible branch proceeds without separately reviewed BranchImpactEvidence.
16. **E05-WSN** — WSN experiment identity and E3/E4/E5/E8 outcomes are preserved without promotion.
17. **E05-GENERATED** — generated presentation cannot mutate authoritative state or promote truth.
18. **E05-CONSISTENCY** — Markdown/YAML/handoff claims agree on identities, states, counts, route minima, reopen classes, WSN outcomes, and authority.
19. **E05-AUTHORITY** — no structural result is used as human-quality, production, verification-PASS, readiness, implementation, engine, release, decision, final-canon, or canonical authority.

A failure in one dimension cannot be averaged away by passes elsewhere.

## Route-cardinality contract

The six exact route contracts remain:

| Objective | Required minimum |
|---|---|
| `OBJ_CONT:COMPARE_PERSPECTIVES` | 2 materially distinct nonprivate routes |
| `OBJ_CONT:SELECT_DIRECTION` | 2 simultaneously legal differentiated route kinds |
| `OBJ_CONT:CHOOSE_CONTINUED_GOAL` | 2 simultaneously legal distinct goal families |
| `OBJ_CONT02:COMPARE_CAUSAL_ACCOUNTS` | 2 materially distinct nonprivate routes |
| `OBJ_CONT02:SELECT_RESPONSE_PORTFOLIO` | 2 simultaneously legal differentiated response families |
| `OBJ_CONT02:CHOOSE_CONTINUED_GOAL` | 2 simultaneously legal distinct goal families |

Measurement rules:
1. Candidate, envelope, hypothesis, slot, lens, or response-family counts are not runtime route counts.
2. If no concrete active objective instance exists, `observed_active_route_count` must be `null` and status must be `NOT_APPLICABLE_NO_ACTIVE_CONCRETE_OBJECTIVE_INSTANCE`.
3. Private context never counts toward a required nonprivate minimum.
4. A concrete measurement must identify the exact active objective instance and evidence scope.
5. Recompute is mandatory after exactly: `ACTIVATION`, `REFUSAL`, `REJECTION`, `SUBSTITUTION`, `RECOVERY`, `ROUTE_LOSS`.
6. A measured underflow is a structural finding; it is not repaired by counting mutually exclusive, private-only, blocked, or unavailable routes.

This evaluator packet itself authors zero concrete active objective instances.

## Exact reopen-condition registry

Every future application must retain and classify all 17 exact classes:

1. `SOURCE_OR_REVIEW_IDENTITY_DRIFT`
2. `BOUND_INTERFACE_REQUIRES_UNSUPPORTED_CONCRETE_ENTITY`
3. `REVIEWED_BOUNDED_SET_BROADENED_OR_SILENTLY_NARROWED`
4. `MUTABLE_SIBLING_OUTPUT_CONSUMED_BEFORE_FANIN`
5. `PRIVATE_INFORMATION_REQUIRED_FOR_ROUTE_MINIMUM`
6. `PRIVATE_INFORMATION_REQUIRED_FOR_FOUNDATIONAL_PLAY`
7. `FACT_CLAIM_BELIEF_TESTIMONY_KNOWLEDGE_EXPOSURE_AUTHORITY_COLLAPSE`
8. `RELATIONSHIP_OR_LEGITIMACY_SCALARIZED_OR_AUTOMATICALLY_ALIASED`
9. `MATERIAL_HISTORY_ERASED_BY_RETRY_REPAIR_OR_RECONCILIATION`
10. `NONFOUNDATIONAL_GATE_COMPOSITION_BECOMES_DEFACTO_FOUNDATIONAL`
11. `NARRATIVE_ROUTE_CARDINALITY_DROPS_BELOW_REVIEWED_MINIMUM`
12. `MUTUALLY_EXCLUSIVE_BRANCHES_BECOME_JOINTLY_REQUIRED`
13. `EXACT_TIME_SCHEDULE_WEATHER_TRAVEL_OR_NPC_REACHABILITY_BECOMES_REQUIRED`
14. `CONCRETE_HIGH_IMPACT_OR_IRREVERSIBLE_BRANCH_LACKS_REVIEWED_BRANCH_IMPACT_EVIDENCE`
15. `WSN_OUTCOME_REQUIRES_PROMOTION_WITHOUT_EXACT_PREREQUISITE`
16. `GENERATED_PRESENTATION_MUTATES_AUTHORITATIVE_STATE`
17. `STRUCTURAL_RESULT_USED_AS_HIGHER_AUTHORITY`

Allowed application statuses are `TRIGGERED` or `CLEARED_IN_THIS_EVALUATION`, each with evidence. A clear result is packet-local only and never pre-clears a later authored instance.

For this evaluator-definition packet itself, no condition is asserted cleared on behalf of future sibling/fan-in content. Its self-review checks only whether the evaluator contract preserves every class and firewall.

## Semantic firewalls

The evaluator must fail closed if an application collapses any of these boundaries:
- objective fact versus claim/belief/testimony/interpretation/record/knowledge/exposure/confidence/generated presentation;
- private access versus onward-sharing permission;
- relationship dimensions versus legitimacy/public standing;
- repair/reconciliation versus erasure of material history;
- standing/reputation/gifts/proximity/repetition versus consent;
- structural compatibility versus concrete selection;
- structural PASS versus empirical evidence;
- producer/review publication versus canonicality.

Baseline movement, ordinary community interaction, public information, basic repair/crafting, baseline cultivation, ordinary mutual aid, and nonaligned continuation remain protected from hidden foundational gating unless later separately reviewed authority explicitly changes that contract.

## Cross-artifact consistency rules

A future application is structurally inconsistent if:
- a Markdown claim and machine-readable field disagree;
- artifact IDs or review tokens drift;
- count fields disagree with enumerated items;
- `null` route semantics are replaced by fabricated zero/runtime evidence;
- a reopen class is omitted, renamed, or silently pre-cleared;
- WSN outcomes differ across artifacts;
- an authority flag is stronger in one artifact than another;
- an evaluator result is cited as authority it explicitly lacks.

Consistency failure remains a structural defect; it does not authorize the evaluator to rewrite judged content.

## WSN evidence debt

The exact inherited outcomes remain:
- `WSN-E3 = INCONCLUSIVE_TIMED_COVERAGE_BLOCKED`;
- `WSN-E4 = NOT_RUN_BLOCKED_BY_EXACT_PREREQUISITE`;
- `WSN-E5 = PASS_BOUNDED_MODEL_ONLY`;
- `WSN-E8 = INCONCLUSIVE_SCHEDULE_COVERAGE_BLOCKED`.

The evaluator may verify preservation of these labels and prerequisites. It may not promote them into exact schedule, weather, travel, timed-objective, NPC-reachability, production-persistence, human-quality, aggregate-verification, or implementation-readiness authority.

## Authority firewall

A clean structural application means only that the checked bounded structural invariants were preserved for the exact judged packet. It does not mean:
- the content is fun, polished, balanced, desirable, or human-quality approved;
- runtime behavior or persistence has been empirically validated;
- verification has passed;
- implementation is ready or authorized;
- an engine is selected;
- release or production is approved;
- a narrative/world/social/character choice is canonical;
- the result is canonical planning authority.

Those conclusions require their own declared evidence and authority routes.

## Self-review

Attacks performed:
- source/review identity drift;
- sibling mutable consumption;
- inherited-state rename/narrowing;
- unsupported concrete binding;
- private-information leakage or foundational gating;
- epistemic collapse;
- exact-time/WSN laundering;
- history erasure;
- relationship scalarization/legitimacy aliasing;
- refusal/nonalignment bypass;
- hidden foundational-gate composition;
- fabricated route measurement;
- recomputation-trigger loss;
- reopen-condition omission/preclear;
- mutually exclusive route double-counting;
- missing BranchImpactEvidence barrier;
- numeric/weighted quality scoring;
- generated-state mutation;
- cross-artifact inconsistency;
- structural-result authority inflation;
- engine coupling.

Findings: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR**.

Producer self-review grants no root review token.

## Required next gate

Freeze an exact-head draft PR changing only:
- `docs/planning/wave-2/content/content-evaluation-continuation-05.md`;
- `docs/planning/wave-2/content/content-evaluation-continuation-05.yaml`;
- `docs/planning/handoffs/issue-1235.md`.

Then route exactly one fresh independent/degraded-independent `W2-CONTENT-EVAL-CONT-05-REV-01` review against the immutable packet.

Only a clean fresh review may grant `W2-CONTENT-EVAL-CONT-05_REVIEWED`. Producer authorship grants no token. Conceptual `W2-CONTENT-SYN-CONT-05` remains unmaterialized until all five exact CONT-05 reviewed-root tokens coexist.

No integration, verification PASS, implementation/readiness, gameplay implementation, engine selection, human-quality, release/production, decision/final-canon, or canonical authority is created.
