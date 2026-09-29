# W2 content social continuation 07 — procedure, representation, legitimacy evidence, recusal, remedy, and interinstitutional conflict

## Status and authority

- mission: `W2-CONTENT-SOCIAL-CONT-07`
- issue: #1310
- branch: `planning/issue-1310`
- ownership generation: comment `5875513729`
- execution foundation: `main@0f2c1e4e174b7ff9c2dd95a5d51ab7cdca041ecc`
- canonical Planning Program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`
- canonical binding: Issue #1147 terminal comment `5675066392`
- canonical activation: `87c85cecfa9a2ffa464c4b36816a138bf41441af`
- CONT-07 compiler: Issue #1306 terminal `5827305785`
- clean activation Review #1308 terminal `5827378595`, disposition `CLEAN_FOR_BOUNDED_CONTENT_FRONTIER_CONTINUATION_07_ACTIVATION`
- frozen predecessor: clean-reviewed CONT-06 fan-in #1302 / Review #1304
- canonicality: `NOT_CANONICAL`

This packet consumes only the exact clean-reviewed CONT-06 fan-in and immutable interfaces it exposes. It consumes no sibling CONT-07 mutable output. It deepens social/institutional interfaces without selecting any final institution, polity, membership, office, occupant, representation, jurisdiction, legitimacy, consent state, concrete cross-root binding, active objective, or final canon.

## Frozen predecessor identities

- fan-in producer #1302 terminal `5827101152`, head `1c5966d1965c4ca36bb2ef53561137a2ff88e61a`
- fan-in Markdown/YAML/handoff blobs:
  - `1689cb397173556e87d0dce507bd64712da1eaf2`
  - `400b929442fb36b63318a9eecaca6a08ca12f05e`
  - `55943d3b98a928fea0c34d7a924ba705a70f3936`
- required Review #1304 terminal `5827159994`
- review disposition `CLEAN_FOR_BOUNDED_CONTENT_CONTINUATION_06_CONSUMPTION`
- review report/handoff blobs:
  - `f5ea0e5327c2828e9a88f3b08a84f94f3aac8006`
  - `4d6106a602004557102f441faf29ed0fe3e34476`
- predecessor reviewed token `W2-CONTENT-SYN-CONT-06_REVIEWED`

The predecessor exposes the social interfaces `SOCIAL06:MANDATE-SCOPE-DOSSIER`, `SOCIAL06:LEGITIMACY-EVIDENCE-DELTA`, `SOCIAL06:PARTICIPATION-DISSENT-TRACE`, `SOCIAL06:RECUSAL-SUBSTITUTION-PLAN`, `SOCIAL06:REMEDY-APPEAL-CHAIN`, and `SOCIAL06:INTERINSTITUTIONAL-CLAIM-GRAPH`. They are immutable reviewed inputs here, not mutable dependencies.

## Exact inherited state contract

The packet preserves all eleven states exactly:

| Binding | Required state |
| --- | --- |
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

The exact world surface remains the unselected three-member bounded set `WORLD_IFACE:SHARED-WORKS-JUNCTION`, `WORLD_IFACE:COMMONS-EDGE`, and `WORLD_IFACE:CULTIVATION-MARGIN`. This social packet does not rank, prefer, default, widen, narrow, or select that set.

The six compatibility envelopes remain immutable, descriptive, and nonselecting:

- `ENVELOPE-05-A-EVIDENCE-TRIANGULATION`
- `ENVELOPE-05-B-REFUSAL-SAFE-PORTFOLIO`
- `ENVELOPE-05-C-APPEND-ONLY-AFTERMATH`
- `ENVELOPE-05-D-OPTIONAL-PRIVATE-CONTEXT`
- `ENVELOPE-05-E-EXCLUSIVE-COMMITMENT-GUARD`
- `ENVELOPE-05-F-BRANCH-IMPACT-BARRIER`

## SOCIAL07:PROCEDURE-CLAIM-REGISTER

This interface records claims that a procedure was available, invoked, followed, departed from, contested, or unresolved without converting procedural status into objective truth or legitimacy.

Required fields:

- `procedure_ref`: typed candidate procedure/interface reference, never a final institution;
- `claimant_role_ref`: typed role/interface placeholder, never a selected occupant;
- `procedure_claim_class`;
- `scope_ref`: bounded subject matter or decision surface;
- `public_evidence_refs`: immutable reviewed nonprivate evidence;
- `institutional_record_refs`: institutional records kept semantically separate from fact;
- `counterclaim_refs`;
- `scoped_absence_refs`;
- `unknowns`;
- `authority_class: PROCEDURE_CLAIM_ONLY_NOT_LEGITIMACY_OR_TRUTH`.

Allowed `procedure_claim_class` values:

- `PROCEDURE_AVAILABLE_CLAIM`
- `PROCEDURE_INVOKED_CLAIM`
- `PROCEDURE_FOLLOWED_CLAIM`
- `PROCEDURE_DEPARTURE_CLAIM`
- `PROCEDURE_CONTESTED`
- `PROCEDURE_STATUS_UNRESOLVED`

Invariants:

- a procedure record does not prove that its outcome is correct, legitimate, consensual, representative, or binding;
- institutional repetition or apparent regularity does not promote a procedure claim into objective fact;
- absence of a recorded objection is not consent;
- dissent, recusal, substitution, rejection, withdrawal, and nonalignment remain representable;
- generated presentation cannot change the register;
- no score, majority weight, prestige weight, confidence scalar, or procedural winner is defined.

## SOCIAL07:MANDATE-BOUNDARY-TRACE

This interface deepens `SOCIAL06:MANDATE-SCOPE-DOSSIER` by recording bounded claims about what a candidate mandate is asserted to cover and where that coverage is contested or unknown.

Required fields:

- `mandate_ref`: immutable reviewed mandate/interface reference;
- `asserted_scope_refs`;
- `excluded_scope_refs`;
- `contested_boundary_refs`;
- `source_claim_refs`;
- `public_evidence_refs`;
- `private_sidecar_refs`: optional and deny-by-default;
- `unknowns`;
- `scope_state`;
- `authority_class: MANDATE_BOUNDARY_DESCRIPTION_ONLY`.

Allowed `scope_state` values:

- `ASSERTED_WITHIN_SCOPE`
- `ASSERTED_OUTSIDE_SCOPE`
- `BOUNDARY_CONTESTED`
- `SCOPE_EVIDENCE_INSUFFICIENT`
- `SCOPE_UNRESOLVED`

Rules:

- mandate scope cannot be broadened by popularity, relationship state, proximity, gifts, repeated requests, prior success, office claims, or generated presentation;
- a candidate mandate never establishes final jurisdiction, membership, office, representation, legitimacy, consent, or authority;
- private information cannot be required to establish a public/nonprivate minimum;
- a later clarification appends evidence; it does not erase prior contested-boundary history.

## SOCIAL07:REPRESENTATION-CLAIM-TEST

This interface records whether the minimum declared evidence roles needed to examine a bounded representation claim are present. It does not establish representation.

Each test contains:

- `representation_claim_ref`;
- `represented_role_or_group_ref`: typed unresolved role/interface;
- `claimant_role_ref`;
- `declared_basis_classes`;
- `required_public_evidence_roles`;
- `available_public_evidence_refs`;
- `counterclaim_refs`;
- `dissent_trace_refs`;
- `mandate_boundary_trace_ref`, when applicable;
- `private_context_refs`: optional only;
- `test_state`;
- `representation_status: UNRESOLVED`;
- `authority_class: REPRESENTATION_CLAIM_EXAMINATION_ONLY`.

Allowed `test_state` values:

- `EVIDENCE_ROLES_PRESENT_FOR_BOUNDED_EXAMINATION`
- `PUBLIC_EVIDENCE_ROLE_MISSING`
- `MANDATE_BOUNDARY_UNRESOLVED`
- `DISSENT_REQUIRES_RETENTION`
- `CLAIM_BASIS_CONTESTED`
- `INSUFFICIENT_SCOPE`

No count, vote, unanimity, institutional provenance, public standing, relationship state, or exposure threshold turns this test into a representation decision. Refusal or nonalignment is not evidence for representation merely because another route remains available.

## SOCIAL07:LEGITIMACY-EVIDENCE-MATRIX

This interface deepens `SOCIAL06:LEGITIMACY-EVIDENCE-DELTA` into a nonaggregating matrix of evidence bearing on explicitly declared legitimacy claims while keeping legitimacy distinct from objective fact and relationship state.

Each row contains:

- `legitimacy_claim_ref`;
- `evidence_ref`;
- `evidence_authority_class`;
- `bearing`;
- `scope_limits`;
- `dependency_refs`;
- `counterevidence_refs`;
- `unknowns`.

The only allowed bearing vocabulary is:

- `SUPPORTS`
- `WEAKENS`
- `NONDISCRIMINATING`
- `INSUFFICIENT_SCOPE`

Matrix invariants:

- bearings are qualitative and scoped, never votes or weights;
- evidence count, source count, repetition, majority, unanimity, office, public standing, relationship value, player exposure, or presentation salience cannot establish legitimacy;
- contradictory evidence remains visible;
- shared-origin evidence is not multiplied into independent confirmation;
- `legitimacy_status` remains `UNRESOLVED`;
- the matrix cannot establish ownership, membership, office, representation, jurisdiction, consent, objective truth, or final authority;
- no aggregate score, rank, tier, winner, threshold, recommendation, or preferred claimant exists.

## SOCIAL07:RECUSAL-SUBSTITUTION-LEDGER

This interface deepens `SOCIAL06:RECUSAL-SUBSTITUTION-PLAN` as append-only transition provenance.

Each entry records:

- `procedure_ref`;
- `role_slot_ref`;
- `event_class`;
- `event_basis_refs`;
- `prior_role_state_ref`;
- `successor_role_slot_ref`: optional unresolved role slot only;
- `scope_limits`;
- `retained_dissent_refs`;
- `retained_refusal_refs`;
- `unknowns`;
- `selection_effect: NONE`.

Allowed `event_class` values:

- `RECUSAL`
- `SUBSTITUTION_REQUESTED`
- `SUBSTITUTION_ACCEPTED_WITHIN_SCOPE`
- `SUBSTITUTION_REJECTED`
- `WITHDRAWAL`
- `DEFERRAL`
- `ROLE_AVAILABILITY_LOST`
- `ROLE_STATE_UNRESOLVED`

A substitution event may expose a typed successor slot but cannot select a concrete occupant. Recusal, withdrawal, or refusal is never rewritten into consent by a later substitution. A later valid route does not erase prior events. Relationship dimensions, popularity, gifts, standing, proximity, grinding, prior success, office claims, or institutional prestige cannot force substitution or return.

## SOCIAL07:REMEDY-APPEAL-DELTA-LEDGER

This interface deepens `SOCIAL06:REMEDY-APPEAL-CHAIN` by retaining append-only deltas across remedy, appeal, repair, compensation, rejection, and unresolved aftermath.

Each delta contains:

- `subject_ref`;
- `prior_remedy_state_ref`;
- `event_class`;
- `public_evidence_refs`;
- `optional_private_context_refs`;
- `observed_effect_refs`;
- `residual_effect_refs`;
- `counterevidence_refs`;
- `scope_limits`;
- `unknowns`;
- `restoration_status`.

Allowed `event_class` values:

- `REMEDY_PROPOSED`
- `REMEDY_ACCEPTED_WITHIN_SCOPE`
- `REMEDY_REJECTED`
- `APPEAL_INVOKED`
- `APPEAL_DECLINED`
- `REPAIR_OBSERVED_WITHIN_SCOPE`
- `COMPENSATION_OBSERVED_WITHIN_SCOPE`
- `RESIDUAL_EFFECT_OBSERVED`
- `OUTCOME_UNRESOLVED`

Allowed `restoration_status` values:

- `NOT_EVALUATED`
- `SCOPED_EFFECT_OBSERVED`
- `RESIDUAL_EFFECT_RETAINED`
- `RESTORATION_UNRESOLVED`

There is no `FULLY_RESTORED`, global reset, universal repaired flag, or history-deletion operation. Remedy, appeal, repair, compensation, reconciliation, reinterpretation, later success, or renewed participation cannot erase earlier material, refusal, dissent, relationship, or failed-restoration history.

## SOCIAL07:INTERINSTITUTIONAL-CONFLICT-FRAME

This interface deepens `SOCIAL06:INTERINSTITUTIONAL-CLAIM-GRAPH` without selecting final institutions or resolving competing authority.

Each frame contains:

- `claimant_role_refs`: two or more typed unresolved institutional-role/interface references when instantiated;
- `contested_subject_ref`;
- `procedure_claim_refs`;
- `mandate_boundary_refs`;
- `representation_claim_refs`;
- `legitimacy_matrix_refs`;
- `recusal_substitution_refs`;
- `remedy_appeal_refs`;
- `public_evidence_refs`;
- `counterclaim_refs`;
- `private_context_required: false`;
- `conflict_state`;
- `selection_effect: NONE`.

Allowed `conflict_state` values:

- `CLAIMS_COEXIST_UNRESOLVED`
- `SCOPE_CONFLICT_UNRESOLVED`
- `PROCEDURE_CONFLICT_UNRESOLVED`
- `REPRESENTATION_CONFLICT_UNRESOLVED`
- `LEGITIMACY_CONFLICT_UNRESOLVED`
- `INSUFFICIENT_SCOPE`

No claimant may be ranked, preferred, defaulted, selected, or declared legitimate by this frame. A later concrete high-impact or irreversible activation remains inert without separately reviewed `BranchImpactEvidence`.

## Information and authority firewalls

Objective fact, claim, belief, testimony, interpretation, institutional record, confidence, entity knowledge, player exposure, scoped absence, and generated presentation remain separate semantic classes.

Institutional records are records, not objective truth. Public standing is not legitimacy. Relationship dimensions are not institutional authority. Player exposure does not create character/entity knowledge. Repetition, majority, unanimity, confidence, source prestige, relationship state, office claims, or presentation salience cannot promote a claim into fact.

Generated presentation is read-only with respect to authoritative state.

## Private-information firewall

Private access and onward sharing remain `DENY_BY_DEFAULT`. Private context is optional and nonfoundational. Its absence is legal.

Private-only material cannot satisfy:

- a required nonprivate evidence role;
- a route-cardinality minimum;
- baseline-play access;
- public representation evidence;
- public mandate evidence;
- a required legitimacy-evidence role.

A permission for one use does not imply onward sharing or broader scope. Revocation/withdrawal is retained as history and cannot be silently undone.

## Relationship, standing, and agency separation

`TRUST`, `WARMTH`, `RESPECT`, `OBLIGATION`, `RIVALRY`, and `CAUTION` remain independent dimensions. No aggregate affinity/reputation scalar exists, and none aliases to legitimacy, representation, office, membership, jurisdiction, public standing, or consent.

Refusal, withdrawal, deferral, substitution, recusal, rejection, and nonalignment remain legal. They cannot be rewritten by popularity, gifts, grinding, proximity, prior success, relationship state, public standing, membership claims, office claims, or repeated attempts.

Ordinary baseline play remains legal; optional/private/nonfoundational gates cannot compose into a hidden foundational tax.

## Route-cardinality invariants

This packet authors zero concrete active objective instances. Therefore:

- `observed_active_route_count: null`
- status: `NOT_APPLICABLE_NO_ACTIVE_CONCRETE_OBJECTIVE_INSTANCE`

The six exact contracts remain unchanged:

1. `OBJ_CONT:COMPARE_PERSPECTIVES` — minimum 2 materially distinct nonprivate routes.
2. `OBJ_CONT:SELECT_DIRECTION` — minimum 2 simultaneously legal differentiated route kinds.
3. `OBJ_CONT:CHOOSE_CONTINUED_GOAL` — minimum 2 simultaneously legal distinct goal families.
4. `OBJ_CONT02:COMPARE_CAUSAL_ACCOUNTS` — minimum 2 materially distinct nonprivate routes.
5. `OBJ_CONT02:SELECT_RESPONSE_PORTFOLIO` — minimum 2 simultaneously legal differentiated response families.
6. `OBJ_CONT02:CHOOSE_CONTINUED_GOAL` — minimum 2 simultaneously legal distinct goal families.

Any later active instance must recompute after exactly `ACTIVATION`, `REFUSAL`, `REJECTION`, `SUBSTITUTION`, `RECOVERY`, or `ROUTE_LOSS`. Interface, candidate, claim, claimant, ledger, matrix, evidence, or procedure counts are not active-route measurements. Blocked, unavailable, private-only, or mutually exclusive routes cannot be double-counted.

## Reopen-condition registry

All 17 classes remain present and available:

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

Packet-local self-review pre-clears no future instance.

## Branch-impact barrier

No concrete high-impact or irreversible branch is activated here. Any later concrete activation requires separately reviewed `BranchImpactEvidence` with applicable:

- `BIE04:SIGNALING`
- `BIE04:OBSERVED-EFFECT`
- `BIE04:CONTINUED-PLAY`

Procedure compatibility, mandate evidence, representation claims, legitimacy evidence, remedy availability, or apparent reversibility cannot substitute for that barrier.

## WSN limits

The packet preserves exactly:

- E3 `INCONCLUSIVE_TIMED_COVERAGE_BLOCKED`
- E4 `NOT_RUN_BLOCKED_BY_EXACT_PREREQUISITE`
- E5 `PASS_BOUNDED_MODEL_ONLY`
- E8 `INCONCLUSIVE_SCHEDULE_COVERAGE_BLOCKED`

No exact schedule, weather window, travel duration, timed-objective guarantee, NPC reachability, production persistence, empirical WSN promotion, implementation-readiness, release, or canonical claim is authored.

## Fan-in barrier

Conceptual `W2-CONTENT-SYN-CONT-07` remains unmaterialized. This producer does not grant `W2-CONTENT-SOCIAL-CONT-07_REVIEWED`. Only a fresh required review of the exact immutable terminal packet may grant that token, and all five exact CONT-07 reviewed tokens are required before fan-in materialization.

## Producer self-review

The authored packet was attacked for:

- source/review/canonical identity drift;
- sibling CONT-07 mutable consumption;
- inherited-state rename or closure;
- world bounded-set widening/narrowing/selection;
- concrete institution, office, occupant, membership, representation, jurisdiction, legitimacy, consent, or cross-root binding;
- procedure or institutional-record laundering into objective truth;
- representation by count, unanimity, popularity, standing, or relationship state;
- legitimacy aggregation, score, rank, tier, winner, or threshold;
- mandate broadening by repetition or social state;
- recusal/substitution/refusal history erasure;
- universal-restoration laundering;
- private-information foundationalization or leakage;
- relationship scalarization or legitimacy aliasing;
- refusal/nonalignment bypass;
- hidden foundational gates;
- route-cardinality weakening or fabricated measurement;
- recomputation-trigger loss;
- reopen-condition loss or future preclearance;
- BranchImpactEvidence bypass;
- WSN promotion;
- exact-time inference;
- early fan-in;
- engine coupling;
- higher-authority inflation;
- Markdown/YAML inconsistency.

Finding counts: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR**.

This self-review grants no root token.

## Required next route

Exactly one fresh independent/degraded-independent review mission: `W2-CONTENT-SOCIAL-CONT-07-REV-01`.

That review must bind the exact terminal producer head, exact draft PR, and exact Markdown/YAML/handoff blobs. Only a clean review with 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR may grant `W2-CONTENT-SOCIAL-CONT-07_REVIEWED`.

No integration/publication, verification PASS, implementation/readiness, gameplay implementation, engine selection, human-quality, release/production, decision/final-canon, or canonical authority is created by producer authorship.
