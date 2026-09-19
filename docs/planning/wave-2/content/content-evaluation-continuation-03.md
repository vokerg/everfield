# W2-CONTENT-EVAL-CONT-03 — parameterized consistency and evaluation contract

**Issue:** #1174  
**State:** CONTENT EVALUATION CANDIDATE / NONCANONICAL  
**Conflict domain:** `CONTENT_EVALUATION`  
**Engine dependency:** none  
**Application state:** deferred to later `W2-CONTENT-SYN-CONT-03` fan-in  
**Required next gate:** one fresh independent/degraded-independent review of this exact evaluator packet

## 1. Scope and frozen authority

This packet defines an engine-neutral structural evaluator for the four creative CONT-03 roots. It does **not** read, judge, bind, or name mutable sibling CONT-03 output bytes. Later fan-in may instantiate the contract only from exact clean-reviewed immutable packet descriptors.

Execution basis:

- producer base: `main@5311124d331be58a1a10f5f8bd5f377424733bb7`;
- ownership generation: Issue #1174 comment `5744880911`;
- canonical Planning Program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`;
- canonical binding: Issue #1147 comment `5675066392`;
- canonical activation: `87c85cecfa9a2ffa464c4b36816a138bf41441af`;
- CONT-03 compiler contract/map blobs: `bdae0204774a0ab1a42a32e32cbb7786862017b0` / `a32b4157f7358f5cb3a098dd1d6fdc8d3564ddb9`;
- clean activation Review #1175 terminal `5744391071`, disposition `CLEAN_FOR_BOUNDED_CONTENT_FRONTIER_CONTINUATION_03_ACTIVATION`;
- reviewed CONT-02 fan-in Markdown/YAML blobs: `15d38f751d8baa5649695154db4b84fbb3fdbba4` / `e3f93dc85527a484233e194f7143c91aa10e1c69`;
- clean predecessor remediation Review #1167 terminal `5743361245`;
- reviewed CONT-02 evaluation contract blobs: `fa8e385bd4cca4d6e78c36872e875d515ae4a21f` / `6f9f100574532b2af9332990f4f85189fd58bb7f`.

No mutable CONT-03 sibling output is consumed.

## 2. Parameterization contract

Later fan-in supplies exactly four immutable reviewed packet descriptors:

- `WORLD_CONT_03_PACKET`;
- `SOCIAL_CONT_03_PACKET`;
- `CHAR_CONT_03_PACKET`;
- `NARR_CONT_03_PACKET`.

Each descriptor must bind source issue/mission, terminal producer record, exact immutable head/work SHA, artifact blob identities, exact clean root-review terminal and reviewed token, authority boundary, typed provisional interfaces, OPEN/UNRESOLVED ledger, route-cardinality surfaces, and WSN ledger.

The evaluator never repairs an input, substitutes main bytes for the judged packet, infers a missing review, accepts a token bound to a different generation, or treats PR state/mergeability as review authority.

## 3. Result vocabulary

Bare `PASS` is forbidden. Clean result classes are scope-qualified:

- `PASS_IMMUTABLE_REVIEWED_INPUTS`
- `PASS_WITH_TYPED_OPEN_BINDINGS`
- `PASS_BOUNDED_STRUCTURAL`
- `PASS_RELATIVE_ONLY_EXACT_TIME_BLOCKED`
- `PASS_NO_MUTATION_OR_UPGRADE`
- `NOT_APPLICABLE_NO_ACTIVE_CONCRETE_OBJECTIVE_INSTANCE`
- `OPEN_REVIEW_REQUIRED`

Failures are `BLOCKER`, `MAJOR`, or correction-requiring `MINOR`. Aggregate cleanliness requires zero unresolved findings in those three classes. Numeric aggregation, averaging, scoring, or conversion into quality/readiness authority is forbidden.

## 4. Check catalog

### Identity and packet integrity

`CHK-CONT03-IDENTITY` attacks head/work mismatch, artifact drift, stale or cross-generation review tokens, review reuse after source mutation, substituted integrated bytes, and ambiguous provenance. Identity ambiguity that can affect semantics is a BLOCKER.

### Entity and interface scope

`CHK-CONT03-ENTITY-SCOPE` rejects unsupported final locations, owners, polities, institutions/factions, named principal characters, permanent memberships/offices, biographies, romance/family/endings, final world causes, crop/species catalogs, quotas, schedules, or concrete bindings invented only to close OPEN state.

`CHK-CONT03-INTERFACE` requires reviewed bounded sets to remain exact. OPEN sets may not be narrowed without reviewed authority. Cross-root references before fan-in must remain typed `OPEN`, `OPEN_OPTIONAL`, `OPEN_BOUNDED_SET`, `UNRESOLVED`, or role/interface references.

### Epistemic and private-information firewall

`CHK-CONT03-EPISTEMIC` preserves objective fact vs claim/belief/testimony/institutional record/analysis/generated presentation. Relationship, standing, legitimacy, repetition, or role identity never self-promote a proposition to objective truth.

`CHK-CONT03-PRIVATE` keeps private information deny-by-default. Player exposure is not character knowledge. Trust, standing, proximity, membership, office/role fit, or institutional identity do not grant secret access. Private context cannot satisfy a nonprivate route minimum or foundational play.

### Chronology, branch history, relationships, agency

`CHK-CONT03-CHRONOLOGY` preserves relative-only chronology and rejects exact dates, durations, schedules, weather windows, travel times, timed-objective assumptions, opening hours, or NPC reachability authority without separately reviewed prerequisites.

`CHK-CONT03-HISTORY` preserves material breach/refusal/disclosure/dissent/exclusion/compromise/repair/reconciliation history as append-only and forbids retry/repair from rewriting refusal as consent.

`CHK-CONT03-RELATIONSHIP` preserves multidimensional character relationships and institutional legitimacy without a universal scalar or automatic cross-vector alias. Typed cause/evidence and affected dimensions are required for later deltas.

`CHK-CONT03-AGENCY` requires refusal/nonalignment to remain representable and rejects grind-forced alignment, disclosure, care, labor, commitment, mediation, reconciliation, or arc change.

### Baseline play and consequences

`CHK-CONT03-GATE` preserves foundational gate count 0. Baseline movement, ordinary community interaction, public information, basic repair/crafting, baseline cultivation, and ordinary mutual aid cannot depend on standing, legitimacy, relationship state, private information, specialist scarcity, or composed nonfoundational gates.

`CHK-CONT03-CONSEQUENCE` requires precommitment signaling, affected-goal disclosure, observability, persistence/reversibility semantics, and recovery/mitigation/compensation or meaningful alternatives for later high-impact content. A concrete high-impact or irreversible branch remains forbidden without separately reviewed `BranchImpactEvidence`.

### Route-cardinality contract

`CHK-CONT03-CARDINALITY` preserves all six reviewed objective contracts:

| Objective | Minimum |
| --- | --- |
| `OBJ_CONT:COMPARE_PERSPECTIVES` | >=2 materially distinct nonprivate routes |
| `OBJ_CONT:SELECT_DIRECTION` | >=2 simultaneously legal differentiated route kinds |
| `OBJ_CONT:CHOOSE_CONTINUED_GOAL` | >=2 simultaneously legal distinct goal families |
| `OBJ_CONT02:COMPARE_CAUSAL_ACCOUNTS` | >=2 materially distinct nonprivate routes |
| `OBJ_CONT02:SELECT_RESPONSE_PORTFOLIO` | >=2 simultaneously legal differentiated response families |
| `OBJ_CONT02:CHOOSE_CONTINUED_GOAL` | >=2 simultaneously legal distinct goal families |

Activation, recovery, substitution, rejection, or route loss requires recomputation before an affected objective may remain active.

This evaluator authors zero concrete objective instances. Therefore its own `observed_active_route_count` values are `null` / N/A, never fabricated zero. A later fan-in must emit an exact measurement/status for every active reviewed objective.

### Generated-content and authority firewall

`CHK-CONT03-GENERATED` forbids generated presentation from mutating truth, branch, relationship, legitimacy, private information, character knowledge, quest completion, world state, or canonical state.

`CHK-CONT03-AUTHORITY` forbids structural results from establishing human quality/fun, production persistence, aggregate verification PASS, implementation readiness, gameplay implementation authority, engine selection, release/production, decision/final-canon, or canonical authority.

## 5. Exact reopen-condition registry

The evaluator must preserve and classify all 17 classes; none may be silently deleted or pre-cleared:

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

At application time every class must be explicitly `TRIGGERED` or `CLEARED_IN_THIS_EVALUATION` with evidence. Clearing is packet-local and never deletes the reopen condition.

## 6. WSN evidence ledger

The evaluator reruns no WSN experiment and grants no empirical upgrade. The exact constrained outcomes remain:

- E3 `INCONCLUSIVE_TIMED_COVERAGE_BLOCKED`
- E4 `NOT_RUN_BLOCKED_BY_EXACT_PREREQUISITE`
- E5 `PASS_BOUNDED_MODEL_ONLY`
- E8 `INCONCLUSIVE_SCHEDULE_COVERAGE_BLOCKED`

Any attempted promotion without the exact reviewed prerequisite triggers `WSN_OUTCOME_REQUIRES_PROMOTION_WITHOUT_EXACT_PREREQUISITE`.

## 7. Required fan-in output shape

A later `W2-CONTENT-SYN-CONT-03` application must emit:

1. exact packet and clean review-token identities for all four creative roots;
2. one result for every applicable check;
3. finding counts by severity;
4. typed OPEN/UNRESOLVED ledger;
5. route-cardinality measurement/status for every active reviewed objective;
6. protected foundational-play surfaces;
7. exact retained WSN ledger;
8. all 17 reopen-condition statuses with evidence;
9. explicit negative authority summary;
10. no aggregate numeric score.

This evaluation root grants only the contract token after its own clean review. It does not grant any creative-root token and does not itself permit fan-in materialization.

## 8. Self-review

Adversarial producer self-review attacked: mutable sibling dependency, concrete sibling identity leakage, hidden final-fiction invention, unqualified PASS, numeric-score authority, epistemic collapse, private-information leakage, exact-time overreach, branch/history erasure, relationship/legitimacy scalarization, forced alignment, hidden foundational-gate composition, weakening any of the six route minima, fabricated active-route measurements, reopen-condition loss, WSN laundering, generated-content authority, engine coupling, early fan-in, and higher-authority inflation.

Finding count: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR**.

## 9. Downstream and authority boundary

A clean fresh review of this exact packet may grant only `W2-CONTENT-EVAL-CONT-03_REVIEWED`.

The conceptual `W2-CONTENT-SYN-CONT-03` remains unmaterialized until all five exact CONT-03 reviewed tokens coexist. This packet grants no sibling review result, integration, verification PASS, implementation/readiness, gameplay implementation, engine selection, production/release, decision/final-canon, or canonical authority.

`NOT_CANONICAL`.
