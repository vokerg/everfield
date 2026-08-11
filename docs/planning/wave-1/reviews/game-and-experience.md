# Game and Experience — Wave 1 Adversarial Review

**Mission:** `W1-REV-GAME`  
**State:** REVIEW COMPLETE  
**Disposition:** **CHANGES_REQUIRED**  
**Trust profile:** `DEGRADED_SINGLE_AGENT`  
**BLOCKER:** 0  
**MAJOR:** 8  
**MINOR:** 4  
**NOTE:** 2

## 1. Reviewed provenance

This review binds exact producer results rather than mutable branch tips.

| Mission | Issue | REVIEW_READY comment | work SHA | head SHA | Artifact |
|---|---:|---:|---|---|---|
| W1-TEC-02 | #28 | `5248845557` | `c13389cf1df7ab8e2515a5267bd56869082df1b2` | `eef7c5c009fce5e8c5c9c674c32ad2fe3c31cb60` | `docs/planning/wave-1/proposals/runtime-data-foundation.md` |
| W1-DES-01 | #29 | `5248873867` | `10e1f3cda1f77be81210f769c2224f943810c97b` | `ba2d6bfd6710a83d587184101a2aa5d68a615e03` | `docs/planning/wave-1/proposals/game-design-foundation.md` |
| W1-DES-02 | #30 | `5248900711` | `498679b5c3a473d220723794e66799463ed3ba6f` | `f954d5121e34bb0a629f4461fec88508f1ec32fc` | `docs/planning/wave-1/proposals/economy-progression-automation.md` |
| W1-DES-03 | #31 | `5248925530` | `d19ddc43c9e5f22c6f14e5c978c30a4e6a2f0d8b` | `d7cae4d5e61c95be11544f7da88a6599f2310604` | `docs/planning/wave-1/proposals/world-social-narrative-content.md` |
| W1-EXP-01 | #32 | `5248949220` | `64be52c55d751b37e8d8c4a1758873f4dec64998` | `6058d0d58f41d73da93012a9604df2e50edea509` | `docs/planning/wave-1/proposals/experience-accessibility-media.md` |
| W1-EVAL-01 | #33 | `5248979052` | `a29a9c08f64947b383f4ca6a19fb88032d93777d` | `f41238e948f7ef96718b290012e11210a9e6bba3` | `docs/planning/wave-1/proposals/automated-game-evaluation.md` |

Frozen input/attack plan: `docs/planning/wave-1/reviews/game-experience-review-input.yaml`.

## 2. Independence boundary

This is a fresh reviewer-role episode `w1-rev-game-reviewer-20260811-01` under the repository-visible one-agent constraint. Trust is therefore **DEGRADED**, not full independence.

The six producer candidates were frozen and not edited. The review input set and attack plan were committed before cross-proposal reconciliation. Findings below are based on the exact producer artifacts and their shared interfaces, not producer-private rationale.

## 3. Attack plan

The review attempted to break the combined game/experience design through:

1. nominal sandbox diversity hiding a mandatory progression route;
2. universal-value/progression dominance despite multiple lifestyle labels;
3. automation becoming compulsory or eliminating meaningful play;
4. inconsistent calendar/time/timing semantics across simulation, quests, economy, and accessibility;
5. discovery, secrets, and accessibility requirements contradicting each other;
6. narrative/social gates silently becoming universal progression prerequisites;
7. generated runtime content/NPC behavior escaping determinism, persistence, or canonical-fact rules;
8. content-count and cross-system-link inflation masquerading as depth;
9. semantic-coverage/persona metrics being Goodharted;
10. subjective/protected evaluator correlation or drift laundering uncertain quality into PASS;
11. player-surface and simulation-surface disagreement;
12. originality/reference boundaries becoming prose-only rather than testable policy.

## 4. Summary disposition

The six proposals are individually strong and deliberately avoid many obvious traps: no single fun score, no final balance invented from prose, no universal money-per-minute model, no requirement that automation be mandatory, explicit generated-content grounding, explicit player/simulation evidence pairing, and no claim that current evaluator technology is already sufficient.

However, the combined candidate still leaves eight material **cross-proposal contracts** implicit. Those gaps can allow two locally compliant implementations or evaluators to disagree about whether a route is optional, whether time advances, whether coverage is meaningful, whether runtime generation is authoritative, whether accessibility research blocks readiness, whether a reference-derived asset is sufficiently original, or whether a subjective panel is genuinely diverse.

Disposition: **CHANGES_REQUIRED**. `W1-SYN-GAME` may proceed by explicitly dispositioning all eight MAJOR findings and preserving the bounded experiments named here. The producer branches remain immutable provenance.

## 5. Findings table

| ID | Severity | Affected surfaces | Failure scenario | Required correction / bounded question |
|---|---|---|---|---|
| GE-M01 | MAJOR | GDF §10; EPA §§9–10; WSN §§10–13 | “Optional” social/narrative/economy systems become hidden foundational prerequisites because each proposal discusses gates/alternatives but there is no shared typed classification of foundational vs specialization/branch-only needs. | Define one versioned progression/gate contract with `FOUNDATIONAL`, `SPECIALIZATION`, `OPTIONAL`, `BRANCH_EXCLUSIVE` (or equivalent) semantics, route/substitution evidence, visibility, and lifestyle impact. Foundational exceptions with one route must be explicit reviewed common-foundation decisions. |
| GE-M02 | MAJOR | RDF §11.3; GDF §9; EPA §§7–8; WSN §§9,12; EXP §10 | Simulation time, day/session pressure, NPC schedules, timed quests, waiting, menus/dialogue, pause/slow assists, and automation all use “time” without one authoritative advancement policy. Accessibility timing assists or UI state can therefore change economy/quest outcomes inconsistently between headless and player execution. | Define versioned `GameTimePolicy`: canonical time domains/units, which contexts advance/freeze/scale simulation, timed-window semantics, real-time inputs, automation/wait rules, pause/menu/dialogue/cutscene behavior, and accessibility alternatives plus evidence of their intended gameplay effects. |
| GE-M03 | MAJOR | GDF §10.1; AGE §9 | Game design requires a machine-readable possibility graph; evaluation says semantic taxonomy emerges from canonical specs, but no stable identity/mapping binds goals/verbs/gates/lifestyles/consequences to coverage dimensions. A test suite can claim broad semantic coverage while never exercising the routes that establish sandbox breadth. | Define a versioned `GameSemanticGraph` or explicit bidirectional mapping from design nodes/edges to runtime/system specs and semantic-coverage obligations. Coverage must report transition/path/lifestyle gaps against the exact graph version. |
| GE-M04 | MAJOR | GDF §13.5; EPA §§10–11; AGE §§11–13 | Both design proposals say manual/direct play remains meaningful and automation is optional, but no acceptance contract says what “meaningful” or “not mandatory” means. Concrete balance can make industrial automation rationally compulsory for basic/narrative legitimacy while still satisfying local prose. | Define a `LifestyleViability` evidence contract by stage/goal: foundational-goal access, direct/manual route availability, burden, automation dependency, decision diversity, switching, and late-game ambitions. Automation can dominate throughput but must not silently become a universal prerequisite unless a reviewed exception changes the design. |
| GE-M05 | MAJOR | RDF §§8,11–13; WSN §§9,11,14; AGE §§10–15 | Future runtime LLM/generative NPC/dialogue/content may affect canonical world state. WSN leaves runtime generation open while RDF requires deterministic/persisted canonical state and AGE requires reproducible real-kernel scenarios. There is no shared authority/replay contract for generated runtime output. | Define `GenerativeRuntimeBoundary`: classify generation as build-time candidate, runtime presentation-only, or canonical-state-affecting. Canonical effects must pass typed commands/effects, bind model/tool/input/output provenance, persist exact accepted state, expose failure/fallback behavior, and either reproduce deterministically or declare/version the nondeterministic evidence boundary. |
| GE-M06 | MAJOR | EXP §§10,18; final implementation-readiness route | EXP correctly requires a later authoritative accessibility/platform research step before implementation/release gates, but this Wave 1 game packet does not itself bind that research as an implementation-readiness prerequisite. Final synthesis could otherwise call architecture “ready” while the required current obligations remain unknown. | `W1-SYN-GAME`/final synthesis must emit an explicit implementation-readiness blocker/next-wave contract for current authoritative accessibility + target-platform research, with source/version/date mapping to architecture/evidence. It may be cleared only by that evidence, not by the architectural checklist in EXP. |
| GE-M07 | MAJOR | GDF reference boundary; WSN §14.4; EXP §§12–15 | Originality/non-cloning is stated as intent/provenance, while exact similarity policy is deferred. High-volume AI narrative/visual/audio generation can therefore remain provenance-complete yet still imitate protected/reference expression too closely. | Define an originality/reference-use policy before shipping-bound content: allowed reference purposes, prohibited source-expression reuse, provenance links, similarity/red-team review across text/visual/audio, escalation/quarantine, and authoritative IP/terms research where needed. Treat similarity diagnostics as evidence, not an automatic legal conclusion. |
| GE-M08 | MAJOR | EXP §14; AGE §§13–15 | “Multiple independent judges” and multimodal panels can still be the same model family/context/rubric with correlated blind spots. The game packet versions evaluators but does not define minimum panel-diversity/trust evidence for important subjective decisions. | Bind subjective evaluation to factory trust semantics: record evaluator family/config/context independence dimensions, evidence-source diversity, protected-oracle control, correlation/disagreement, and a required trust profile by decision risk. Repeated same-configuration calls cannot masquerade as independent evidence. |
| GE-m09 | MINOR | GDF §§8,15; WSN §14; AGE §9 | Encouraging content to participate in multiple systems can be Goodharted into all-to-all cross-links, increasing coupling/state-space/evaluation cost without meaningful decisions. | Add a bounded semantic-role rule: cross-system edges need distinct decision/consequence value and ownership; measure coupling concentration and marginal interaction value, not edge count. |
| GE-m10 | MINOR | AGE §10; GDF sandbox goals | A small golden suite can accidentally become a canonical-playthrough regression path in a game whose value is trajectory diversity. | Require golden suite composition to include several materially different trajectory/system intersections over time and use semantic/protected variants to prevent one-path ossification. |
| GE-m11 | MINOR | EPA §§7–16; GDF §13; EXP §11 | “Time/attention burden” appears in economy, design, and UX evidence but has no shared measurement vocabulary, so a simulator’s attention cost can diverge from actual player input/navigation burden. | Define shared burden evidence fields (active inputs, hold/repeat, travel, supervision, interruption, decision density, omission penalty, real/session time where relevant) and map simulator assumptions to player-surface traces. |
| GE-m12 | MINOR | WSN §§12–13; GDF §§16,22 | Branching/irreversible consequences are allowed and signaled, but no explicit branch-content sufficiency or recovery evidence threshold exists. A “valid” branch may remain technically solvable yet hollow out long-horizon sandbox goals. | Add branch-impact evidence: affected goals/lifestyles/content depth, alternatives, recovery/compensation, and long-horizon trajectory coverage for high-impact irreversible choices. |
| GE-n13 | NOTE | EXP §13 | Deferring final visual/audio style is appropriate; later candidate tournaments must still include production cost/consistency and accessibility evidence, not only preference. | Preserve as a later selection constraint. |
| GE-n14 | NOTE | W1-TEC-01 / W1-SYN-TECH boundary | Engine evaluation is intentionally not a prerequisite of this game review. The eventual selected engine may nevertheless invalidate capture, input, determinism, UI/media, or runtime-generation assumptions. | Cross-domain review/final synthesis must treat engine-spike evidence as a reopen trigger for affected game/experience decisions. |

## 6. Detailed material findings

### GE-M01 — Optionality lacks one machine-readable gate contract

GDF defines lifestyles and says shared prerequisites must be classified and challenged. EPA explicitly says later synthesis should name foundational needs and provide multiple source/service/substitution routes unless a common mechanic is deliberately foundational. WSN then introduces relationship, quest, knowledge, world-state, schedule, and narrative gates that can alter access and services.

The local proposals agree philosophically, but a future compiler has no shared object that says “this gate is foundational, therefore these alternate routes are required” versus “this is intentionally branch-exclusive.” The failure mode is subtle: every subsystem can claim its prerequisite is reasonable while the composed graph recreates one canonical playthrough.

**Correction:** synthesis must create one gate/need classification and make route/substitution/lifestyle evidence inspectable. Quest/social/world effects must reference it when they block general progression.

### GE-M02 — Time is a cross-cutting gameplay API, not just a clock implementation detail

RDF correctly separates simulation time from wall/presentation/service time. GDF relies on day/season/project horizons; EPA prices player time/attention and waiting; WSN has schedules, availability, timed/expiring quests; EXP explicitly anticipates pause/slow/timing alternatives and session interruption.

Without one policy, an accessibility “slow” option could mean slow presentation only, scale canonical simulation, lengthen quest deadlines, alter production throughput, or stop time in menus while headless simulation never does. Each answer may be defensible locally but they are materially different games.

**Correction:** synthesis must define the game-time contract and make scenario/player-surface evidence exercise the same policy.

### GE-M03 — Possibility-space intent and semantic coverage can drift apart

GDF proposes a machine-readable graph of goals, verbs, systems, capabilities, resources, knowledge, locations, relationships, gates, content families, and consequences. AGE proposes rich semantic coverage but says its taxonomy emerges from later canonical system specs.

If those evolve independently, coverage can be “high” while no evaluator walks an intended lifestyle path or exercises the substitute edges that make a system optional. Conversely, the design graph can accumulate theoretical edges no executable scenario covers.

**Correction:** make graph version → system/runtime spec → coverage obligation traceability explicit. A missing mapping is itself a coverage/design defect.

### GE-M04 — Manual/direct-play viability is a promise without a pass condition

GDF states manual play need not match automated throughput but should remain meaningful; EPA says automation may be highly advantageous yet should not be mandatory for basic/narrative progression and should create higher-order decisions.

These are compatible until concrete rates/gates exist. A designer could accidentally make every late-game goal require industrial production, then argue that manual planting is still “meaningful” as an optional low-throughput activity.

**Correction:** define viability by declared goal/stage cohorts and report automation dependency explicitly. The evidence contract should distinguish “manual action still exists” from “direct-play lifestyle remains capable of meaningful goals.”

### GE-M05 — Runtime generation can escape canonical-state and replay rules

WSN responsibly rejects unconstrained emergent LLM agents as the foundation and grounds generated prose in facts, but leaves runtime generation as an open design question. RDF says any canonical gameplay-affecting randomness/input belongs inside the deterministic/evidence boundary; AGE expects exact scenario/evaluator provenance and replayable state.

A runtime generated NPC decision or dialogue can be purely presentational, or it can reveal knowledge, change a relationship, choose a quest branch, create a reward, or alter world state. Those cases cannot share one loose “AI generation” rule.

**Correction:** classify generation by authority. If it changes canonical state, the accepted effect—not necessarily the model internals—must be persisted/versioned/replayable and auditable through the command/effect boundary.

### GE-M06 — Accessibility research is required but not yet a readiness dependency

EXP carefully avoids pretending its architectural list is standards compliance and requires later current authoritative research. That is correct. The risk is routing: without a typed downstream blocker, final synthesis can forget that the architecture is intentionally incomplete with respect to target-platform/current obligations.

**Correction:** promote the research need into a named implementation-readiness dependency with source-version mapping and evidence ownership. Do not weaken it to “future polish.”

### GE-M07 — Provenance does not establish originality

WSN says Everfield must remain original and explicitly defers exact rights/similarity policy. EXP has strong provenance/media briefs and style tournaments. Those establish where an asset came from, not whether its expressive result is too close to a reference or training prompt/source artifact.

**Correction:** synthesis must require a bounded originality/reference-use evidence route for shipping-bound generated/authored content. Similarity tooling/critics can flag risk but cannot themselves make legal conclusions.

### GE-M08 — Multiple judges can still be one correlated oracle

EXP and AGE both reject a single subjective judge and require versioning/disagreement. But “multiple independent runs” is underspecified for high-impact aesthetic/experiential decisions: the same model, rubric, evidence order, and hidden context can produce repeated correlated votes.

**Correction:** consume the factory trust model explicitly. A panel result should state what differs across evaluators and what does not, and required risk classes should demand a minimum trust/evidence diversity profile rather than a run count.

## 7. Minor findings / notes

- **GE-m09:** reward meaningful cross-system edges, not edge count; broad coupling can itself destroy extensibility and evaluation tractability.
- **GE-m10:** golden journeys need trajectory diversity and rotating/protected variants so the project does not optimize one canonical route.
- **GE-m11:** align simulator “attention/burden” assumptions with real semantic-action/player-surface task traces.
- **GE-m12:** irreversible/branching choices need long-horizon branch-content/goal sufficiency evidence, not just local solvability.
- **GE-n13:** keep style selection open until comparative production/readability/accessibility evidence exists.
- **GE-n14:** selected-engine evidence is a legitimate later reopen trigger for game/experience assumptions.

## 8. Empirical questions that remain valid

The review does **not** demand invented numeric answers. The following producer experiments remain necessary evidence:

- lifestyle viability, dominant-route, burden, automation, discovery, and late-game simulations;
- deterministic kernel/adapter, RNG, migration, content-compiler, long-run, and performance spikes;
- quest solvability, knowledge leakage, schedule conflict, branching persistence, and semantic-sameness tests;
- progressive-disclosure, input substitution, current accessibility mapping, media style/audio/provenance/capture/judge tests;
- seeded evaluator defects, semantic-coverage mutation, persona diversity, exploit search, protected leakage, evaluator drift, subjective disagreement, and player-vs-simulation mismatch.

Synthesis must preserve experiment status as **unrun/unproven** until evidence exists.

## 9. Acceptance self-check

- Exact six producer work/status states are bound.
- Producer candidates were not modified.
- Review trust is explicitly DEGRADED_SINGLE_AGENT.
- Disposition is one of the three allowed values: `CHANGES_REQUIRED`.
- Every MAJOR has a concrete correction or bounded evidence contract.
- No unrun design/evaluator experiment is represented as PASS.
- No gameplay implementation, engine selection, final style, balance value, or content catalog is authorized.
- Downstream route is deterministic: `W1-SYN-GAME` must disposition GE-M01 through GE-M08, then finish at `REVIEW_READY` for `W1-REV-CROSS`.

## 10. Downstream instruction

`W1-SYN-GAME` should preserve the six producer artifacts as immutable provenance and use its own synthesis/revision surface to:

1. disposition GE-M01..GE-M08 explicitly;
2. unify the shared gate/time/semantic-graph/viability/runtime-generation interfaces;
3. create explicit accessibility-readiness and originality/reference-use downstream obligations;
4. bind subjective evaluator requirements to factory trust semantics;
5. preserve all still-unrun experiments and reopen conditions;
6. emit one coherent non-canonical game-domain synthesis candidate for cross-domain review.

This review is non-canonical and authorizes no gameplay implementation.
