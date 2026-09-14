# W2-CONTENT-EVAL-CONT-02 — parameterized continuation evaluation contract

**Issue:** #1053  
**State:** CONTENT EVALUATION CANDIDATE / NONCANONICAL  
**Conflict domain:** `CONTENT`  
**Engine dependency:** none  
**Application state:** deferred to later `W2-CONTENT-SYN-CONT-02` fan-in  
**Required next gate:** one fresh independent/degraded-independent required root review of this exact evaluator packet

## 1. Scope and authority

This packet defines a reusable, engine-neutral structural evaluation contract for the four creative CONT-02 roots. It does **not** read, judge, bind, or name any mutable CONT-02 sibling output. The later fan-in may instantiate this contract only with exact clean-reviewed immutable packets supplied through the abstract interfaces:

- `WORLD_CONT_02_PACKET`;
- `SOCIAL_CONT_02_PACKET`;
- `CHAR_CONT_02_PACKET`;
- `NARR_CONT_02_PACKET`.

The evaluator is a consistency and authority guard. It is not an author, canonicalizer, human-quality critic, production validator, implementation-readiness gate, verification authority, release authority, or engine-selection authority.

Frozen basis:

- producer base: `main@e82f12b52087f3820294048451fadc8e29418999`;
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- canonical binding: Issue #6 comment `5245368879`;
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- CONT-02 activation review: Issue #1063 terminal `5654948592`, disposition `CLEAN_FOR_BOUNDED_CONTENT_FRONTIER_CONTINUATION_02_ACTIVATION`;
- reviewed predecessor synthesis: Issue #986 terminal `5644862732`, Markdown/YAML blobs `b39f535dc71639f3ebc67e33a2d692a2b3a77588` / `78148f50649ada789feb3cca61182e18465bb628`;
- predecessor required review: Issue #1009 terminal `5645006619`, disposition `CLEAN_FOR_BOUNDED_CONTENT_CONTINUATION_CONSUMPTION`.

No sibling CONT-02 mutable output is consumed.

## 2. Parameterization contract

Each creative input is supplied later as an immutable reviewed packet descriptor. The evaluator requires, but does not fill, the following fields:

1. abstract packet interface;
2. exact source issue and mission;
3. exact terminal producer status;
4. exact immutable head/work SHA;
5. exact artifact blob identities;
6. exact clean root-review terminal status and review token;
7. declared authority/canonicality boundary;
8. declared provisional cross-root interfaces;
9. declared OPEN/UNRESOLVED ledger;
10. exact retained WSN evidence ledger.

An input is structurally admissible only when its frozen identities are internally consistent and its clean review token applies to exactly the supplied immutable packet. The evaluator never repairs a packet, substitutes a newer head, infers a missing review, or treats mergeability/integration as review authority.

## 3. Result vocabulary

Every successful result is scope-qualified. The contract intentionally has no bare `PASS`.

Allowed non-failing result classes are:

- `PASS_BOUNDED_STRUCTURAL` — the declared bounded structure satisfies the tested invariant;
- `PASS_WITH_TYPED_OPEN_BINDINGS` — consistency holds only because unresolved concretion remains explicit and typed;
- `PASS_RELATIVE_ONLY_EXACT_TIME_BLOCKED` — chronology is structurally coherent while exact timing remains unauthorized;
- `PASS_NO_MUTATION_OR_UPGRADE` — evidence or authority is preserved without promotion;
- `PASS_IMMUTABLE_REVIEWED_INPUTS` — exact frozen reviewed identities are preserved;
- `NOT_APPLICABLE_BOUNDED_SCOPE` — the check is outside the packet's declared bounded surface;
- `OPEN_REVIEW_REQUIRED` — no contradiction is asserted, but a later concrete binding needs explicit review.

Failing findings are classified as `BLOCKER`, `MAJOR`, or correction-requiring `MINOR`. Informational notes are non-authoritative and cannot suppress a finding.

A root or fan-in cannot claim aggregate cleanliness if any applicable check has an unresolved BLOCKER, MAJOR, or correction-requiring MINOR.

## 4. Check catalog

### `CHK-CONT02-IDENTITY` — exact immutable reviewed identity

Inputs: all four abstract packet descriptors.

Attack:

- producer head/work mismatch;
- artifact-blob drift;
- clean-review token bound to a different packet generation;
- review result reused after source mutation;
- source packet silently replaced by integrated/main bytes;
- missing or ambiguous authority provenance.

Clean result: `PASS_IMMUTABLE_REVIEWED_INPUTS`.

Any identity ambiguity that could change judged semantics is a BLOCKER.

### `CHK-CONT02-ENTITY-SCOPE` — bounded entity and fiction scope

Attack any concrete invention not jointly authorized by reviewed inputs:

- new final locations, owners, polities, institutions, factions, named principal characters or permanent memberships;
- final biographies, romances/family outcomes, world causes, crop/species catalogs, quotas or schedules;
- concrete branch-to-cast/site assignments created only to close an OPEN interface.

Ambiguous compatible bindings must remain `OPEN`, `OPEN_OPTIONAL`, `UNRESOLVED`, or `BOUNDED_SET`.

Clean result: `PASS_WITH_TYPED_OPEN_BINDINGS`.

### `CHK-CONT02-INTERFACE` — cross-root interface compatibility

The fan-in may reconcile semantic interfaces, not silently strengthen them. For each interface it must record source scope, compatible target type/set, selection authority and unresolved dimensions.

The evaluator fails any binding that:

- broadens a reviewed bounded set;
- narrows an OPEN set without reviewed evidence;
- assigns a concrete sibling identity from mutable provenance;
- changes an interface's authority class;
- hides an incompatibility by renaming identifiers.

Clean result: `PASS_BOUNDED_STRUCTURAL` or `PASS_WITH_TYPED_OPEN_BINDINGS`.

### `CHK-CONT02-EPISTEMIC` — fact/claim/belief/testimony/interpretation separation

Required authority ordering:

1. bounded objective facts require explicit reviewed world authority;
2. claims, beliefs, testimony, institutional records and interpretations do not self-promote to objective fact;
3. relationship state, public standing, legitimacy and role membership do not create truth;
4. generated presentation does not create truth;
5. contradiction/corroboration from an external fact does not retroactively grant source authority.

Clean result: `PASS_BOUNDED_STRUCTURAL`.

### `CHK-CONT02-SECRET` — private information and character knowledge

Private information remains deny-by-default.

The evaluator attacks:

- player exposure becoming character knowledge;
- standing, trust, proximity, membership, role, reputation or repeated testimony granting secret access;
- disclosure to one recipient implying public exposure or onward sharing;
- private context becoming mandatory for route-cardinality minima;
- a later synthesis requiring an unresolved private holder to make baseline play solvable.

Clean result: `PASS_BOUNDED_STRUCTURAL`.

### `CHK-CONT02-CHRONOLOGY` — relative chronology and exact-time prohibition

The reviewed chronology remains relative-only. The known ordering may preserve `ERA:PRE-WORKS → ERA:WORKS-BUILDOUT → ERA:PATCHWORK-PRESENT` and reviewed before/after/contained-by/causal relations.

The evaluator rejects authored exact dates, durations, opening hours, actor schedules, travel times, weather windows or NPC reachability guarantees unless a separately reviewed exact prerequisite exists.

Clean result: `PASS_RELATIVE_ONLY_EXACT_TIME_BLOCKED`.

### `CHK-CONT02-BRANCH-HISTORY` — branch scope and durable material history

Mutually exclusive branches may not be jointly required. Material breach, refusal, disclosure, dissent, exclusion, compromise, repair and reconciliation history is append-only in authority.

Retry or repair may alter current effects but may not erase the material event or rewrite refusal as consent.

Clean result: `PASS_BOUNDED_STRUCTURAL`.

### `CHK-CONT02-REL-HISTORY` — multidimensional relationships and legitimacy

Character relationship dimensions remain:
`TRUST/WARMTH/RESPECT/OBLIGATION/RIVALRY/CAUTION`.

Social relationship dimensions remain:
`trust/reliability/reciprocity/value_alignment/public_standing/access_state`.

Institutional legitimacy dimensions remain:
`procedural_fairness/responsibility_fulfillment/burden_distribution/domain_competence/transparency_fit/constituency_support`.

No vector may be scalarized or silently aliased to another. Material changes require typed cause/evidence, affected dimensions, branch/visibility scope and durable history.

Clean result: `PASS_BOUNDED_STRUCTURAL`.

### `CHK-CONT02-GATE` — no hidden foundational progression tax

Foundational gate count remains zero for the reviewed continuation surface. Nonfoundational social and narrative gates may unlock only bounded optional/specialist/branch surfaces.

Baseline movement, ordinary community interaction, public information, basic repair/crafting, baseline cultivation and other shared foundational play cannot depend on faction standing, legitimacy, relationship state, private information, specialist scarcity or a composition of nonfoundational gates.

Any composition that becomes de facto foundational is a reopen condition.

Clean result: `PASS_BOUNDED_STRUCTURAL`.

### `CHK-CONT02-QUEST` — solvability and route cardinality

The exact reviewed minima are immutable:

- `OBJ_CONT:COMPARE_PERSPECTIVES`: at least 2 materially distinct **non-private** routes while active; underflow before activation → `STATE_CONT:PRE_COMPARE_DEFERRED`;
- `OBJ_CONT:SELECT_DIRECTION`: at least 2 simultaneously legal materially differentiated route kinds from `MAINTAIN`, `REDIRECT`, `COMPENSATE_OR_REPAIR`, `DEFER`; underflow → `STATE_CONT:PRE_DIRECTION_DEFERRED`;
- `OBJ_CONT:CHOOSE_CONTINUED_GOAL`: at least 2 simultaneously legal materially distinct goal families; underflow → `STATE_CONT:PRE_GOAL_SELECTION_DEFERRED`.

Reviewed continued-goal families are:

- `GOAL_CONT:MAINTAIN_OR_STEWARD`;
- `GOAL_CONT:REPAIR_OR_COMPENSATE`;
- `GOAL_CONT:LEARN_OR_RECONTEXTUALIZE`;
- `GOAL_CONT:REDIRECT_PROJECT`;
- `GOAL_CONT:NONALIGNED_BASELINE_CONTINUATION`.

Recovery, substitution and new bindings must recompute cardinality before an affected objective remains active. No cross-root binding may reduce a required route set below its minimum.

Clean result: `PASS_BOUNDED_STRUCTURAL`.

### `CHK-CONT02-CONSEQUENCE` — consequence observability and continued play

High-impact consequences require:

- visible precommitment signaling;
- affected-goal identification;
- observability;
- persistence and reversibility semantics;
- recovery, mitigation, compensation or a meaningful alternative;
- no hidden removal of foundational gameplay.

An irreversible concrete world change remains unauthorized without separate `BranchImpactEvidence`, fresh review, meaningful continued play and alternative goals/content.

Clean result: `PASS_BOUNDED_STRUCTURAL`.

### `CHK-CONT02-ORIGINALITY` — reference and authored-content authority

Reviewed prior authored examples, including the Old Works vertical slice, remain noncanonical regression/reference material unless separately granted stronger authority. A continuation may reuse contracts and invariants but may not silently adopt example-specific actors, events or fiction as canon.

Clean result: `PASS_NO_MUTATION_OR_UPGRADE`.

### `CHK-CONT02-GENERATED` — generated presentation has no state authority

Generated text/presentation cannot mutate truth, branch, relationship, legitimacy, private-information, character-knowledge, quest-completion, world-state or canonical state by presentation alone.

Clean result: `PASS_BOUNDED_STRUCTURAL`.

### `CHK-CONT02-WSN` — evidence identity and debt preservation

The evaluator reruns no WSN experiment and creates no new WSN identity.

Retained evidence ledger:

- E1 `PASS`;
- E2 `PASS`;
- E3 `INCONCLUSIVE_TIMED_COVERAGE_BLOCKED`;
- E4 `NOT_RUN_BLOCKED_BY_EXACT_PREREQUISITE`;
- E5 `PASS_BOUNDED_MODEL_ONLY`;
- E6 `PASS`;
- E7 `PASS`;
- E8 `INCONCLUSIVE_SCHEDULE_COVERAGE_BLOCKED`;
- E9 `PASS`.

In particular, E3/E4/E8 remain exact-time/schedule/reachability debt and E5 remains bounded-model evidence only.

Clean result: `PASS_NO_MUTATION_OR_UPGRADE`.

### `CHK-CONT02-AUTHORITY` — higher-authority firewall

No structural result from this contract establishes:

- human quality or fun;
- production persistence or schedule correctness;
- empirical aggregate verification PASS;
- implementation readiness;
- gameplay/high-throughput implementation authority;
- engine selection;
- release;
- final canon;
- decision authority;
- canonicalization.

Clean result: `PASS_NO_MUTATION_OR_UPGRADE`.

## 5. Required evaluation output shape

A later fan-in applying this contract must emit:

1. exact evaluated packet identities and clean review-token identities;
2. one result for every applicable check;
3. finding counts by severity;
4. an explicit typed OPEN/UNRESOLVED ledger;
5. route-cardinality measurements for all active reviewed objectives;
6. explicit protected foundational-play surfaces;
7. retained WSN ledger;
8. reopen conditions triggered or cleared;
9. an authority summary stating what the evaluation does **not** establish.

A single aggregate score is forbidden. Individual check results may not be averaged into authority.

## 6. OPEN and reopen rules

The evaluator preserves OPEN rather than inventing certainty.

Required reopen conditions include:

- exact immutable source/review identity drift;
- a bound interface requires an unsupported concrete entity to remain solvable;
- a reviewed bounded set is broadened or silently narrowed;
- a mutable sibling output is consumed before fan-in;
- private information becomes required for a route minimum or foundational play;
- objective fact/claim/belief/testimony/knowledge/exposure authority collapses;
- relationship or legitimacy vectors are scalarized or automatically aliased;
- material history would be erased by retry/repair/reconciliation;
- nonfoundational gate composition becomes de facto foundational;
- a required narrative route set falls below its reviewed cardinality minimum;
- mutually exclusive branches become jointly required;
- exact schedule/time/weather/travel/NPC reachability becomes necessary;
- a concrete high-impact/irreversible branch lacks reviewed `BranchImpactEvidence`;
- a WSN outcome would need promotion without its exact prerequisite;
- generated presentation would mutate authoritative state;
- any structural result is used as human-quality, production, verification, readiness, engine, release, final-canon or canonical authority.

A triggered reopen condition is never auto-resolved by prose.

## 7. Contract self-review

This producer reviews only the evaluator contract itself, not any mutable sibling CONT-02 packet.

Attacks performed:

- accidental sibling-output dependency;
- concrete sibling identity leakage;
- unqualified PASS semantics;
- hidden aggregate score authority;
- fact/claim/knowledge collapse;
- private-information leakage;
- chronology/time overreach;
- branch/history erasure;
- relationship/legitimacy scalarization;
- hidden foundational-gate composition;
- narrative route-cardinality weakening;
- irreversible consequence authority;
- vertical-slice canon inflation;
- generated-content authority inflation;
- WSN laundering;
- engine coupling;
- human-quality/production/verification/readiness/canon inference.

Result: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR** for this bounded parameterized evaluator contract.

## 8. Downstream rule

A clean fresh review of this exact evaluator packet may grant only token:

`W2-CONTENT-EVAL-CONT-02_REVIEWED`.

That token permits later `W2-CONTENT-SYN-CONT-02` to apply this exact contract to the four exact clean-reviewed creative CONT-02 roots. It does not itself evaluate those roots and does not permit fan-in materialization until all five exact CONT-02 review tokens coexist.

## 9. Authority boundary

`NOT_CANONICAL`.

This packet grants no sibling review result, integration, empirical WSN upgrade, verification-PASS, implementation readiness, gameplay/high-throughput implementation, engine selection, production validation, release, decision, final-canon or canonical authority.
