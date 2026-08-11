# Automated Game Evaluation and Synthetic Players — Wave 1 Proposal

**Mission:** `W1-EVAL-01`  
**State:** PROPOSAL / NON-CANONICAL  
**Required reviews:** `W1-REV-TECH`, `W1-REV-GAME`

## Review Index

- **AGE-D1 — Claim-to-evidence matrix (§8):** correctness, architecture, progression/economy, quest/narrative, UX/accessibility, visual/audio, performance, and experiential claims require different evidence combinations; no universal green check or fun score.
- **AGE-D2 — Semantic coverage (§9):** coverage tracks gameplay possibility dimensions—verbs, state transitions, content roles, quest branches, progression regions, NPC/social states, automation/economy operations, failure/recovery, input/accessibility profiles—not just code lines.
- **AGE-D3 — Scenario system (§10):** golden/protected scenarios bind canonical initial state, content/build, actions, seeds, expected invariants/events/player evidence, coverage tags, and evaluator versions; scenario execution should use the real/shared gameplay kernel.
- **AGE-D4 — Synthetic player population (§11):** combine deterministic/scripted, bounded-rational, search/planning, exploit/fuzz, and later LLM/VLM policies with versioned goals/constraints; no persona is a proxy for “the player.”
- **AGE-D5 — Simulation and exploit search (§12):** accelerated deterministic simulation tests economy/progression/reachability/long-horizon state while adversarial search targets loops, dead ends, reward gaming, save/reset abuse, dominant routes, and invariant breaks.
- **AGE-D6 — Subjective evaluation (§13):** subjective quality uses atomic rubrics, exact evidence, randomized/pairwise comparisons where appropriate, multiple independent runs, disagreement, adversarial critique, and evaluator versioning—never unconstrained “is it fun?” authority.
- **AGE-D7 — Protected evaluation (§14):** keep selected high-Goodhart scenarios, benchmark variants, architecture/reward-hacking probes, and evaluator configuration outside producer control while preserving versioned auditability and actionable diagnostics.
- **AGE-D8 — Evaluator lifecycle (§15):** every evaluator/policy/rubric records identity/version/input hashes/environment/results; evaluator changes are judge-affecting and require benchmark/meta-review, while old verdicts reopen only under explicit drift evidence/conditions.
- **Evidence (§5):** project seeds explicitly require structured run reports, deterministic scenarios/replay, semantic coverage, synthetic personas, economy/progression simulation, exploit search, protected tests, visual evidence, specialized oracles, disagreement measurement, and no single fun scalar.
- **Experiments (§18):** seeded-defect detection, semantic-coverage mutation, persona diversity, exploit search, golden/protected scenario leakage, evaluator drift, subjective disagreement, long-simulation reproducibility, and player-vs-simulation surface mismatch tests are required.
- **Reviewer attack points:** metric gaming; coverage taxonomy overfit; golden tests becoming brittle implementation lock; synthetic optimizers defining “good play”; exploit search missing cross-system loops; protected tests becoming opaque; evaluator/model upgrades silently changing truth; subjective panels converging through correlated context; deterministic state passing while UX is broken.

## 1. Objective

Define a game-evaluation architecture capable of supplying autonomous evidence for a large, systemic, long-lived sandbox. The system must detect correctness failures, unreachable/dead progression, dominant strategies, exploits, semantic coverage gaps, narrative/quest inconsistencies, UX/accessibility problems, visual/audio regressions, performance issues, and subjective quality risks without pretending one evaluator or score can replace human-scale judgment.

## 2. Scope

In scope:

- claim-specific evidence requirements;
- semantic gameplay coverage;
- scenario/golden/protected test architecture;
- deterministic/headless/accelerated simulation evidence;
- synthetic-player population and policy versioning;
- exploit/dominant-strategy/adversarial search;
- progression/economy/quest/narrative validation interfaces;
- player-surface + simulation-surface evidence;
- structured subjective/multimodal evaluation;
- evaluator identity/versioning/drift/disagreement;
- protected evaluation and anti-Goodhart controls;
- evidence aggregation/uncertainty/coverage gaps;
- bounded evaluator-calibration experiments.

## 3. Non-goals

This proposal does **not**:

- define a universal `fun_score`, quality score, or reward function for the project;
- claim any current model/agent/VLM can reliably play or judge the final game without experiments;
- specify final game scenarios before game/system design is canonical;
- require all checks to run on every change;
- replace real player-surface evidence with state hashes;
- make synthetic players statistically representative of human populations;
- reveal every protected evaluator input to producers;
- treat protected evidence as unversioned/unchallengeable authority;
- authorize gameplay implementation.

## 4. Constraints and assumptions

### 4.1 Observed constraints

The authoritative packet requires:

1. AI-only development cannot rely on periodic human play as the normal gate.
2. Important claims resolve into inspectable evidence: build/tests/scenarios/invariants/replay/save-load/telemetry/performance/visuals/reviews.
3. Important gameplay scenarios should use the real executable or the same gameplay kernel.
4. Deterministic evidence should bind build/state/seeds/actions/final hashes where practical.
5. Golden end-to-end scenarios should cover important integrated journeys.
6. Both player surface and simulation surface matter.
7. Semantic/game coverage is more important than code coverage alone.
8. Synthetic player populations should include multiple behavior profiles/technologies.
9. Subjective quality should use structured protocols and disagreement, not one unconstrained prompt.
10. Protected independent evaluation is required for Goodhart-sensitive surfaces.
11. The factory/evaluators themselves need benchmark/calibration and versioning.

### 4.2 Assumptions to test

- A layered evaluator portfolio can catch materially different failure classes better than a monolithic judge.
- Semantic coverage taxonomies can be versioned and useful without becoming an optimization target that distorts design.
- Accelerated deterministic simulation can expose long-horizon/economy/progression defects before expensive player-facing execution.
- Several policy classes can reveal route diversity/dominance even though none represents real players fully.
- Selected protected scenarios/probes can improve specification-gaming detection without making debugging impossible.
- Structured subjective evaluator disagreement is more informative than averaging one scalar score.
- Evaluator drift can be measured on frozen evidence/benchmark sets sufficiently to decide when old results need reopening.

## 5. Evidence, inference, recommendation

### 5.1 Evidence

The evaluation seed already specifies candidate run reports, deterministic scenarios, golden journeys, visual evidence, semantic coverage, synthetic personas, subjective protocols, specialized oracles, Goodhart resistance, evaluator versioning, and factory benchmarks. The game mandate/research agenda further require economy/progression simulation, exploit search, quest solvability/narrative consistency, long simulations, and accessible/legible player experience.

### 5.2 Inference

No one evaluator can establish all these claims. A state invariant cannot judge readability; a screenshot cannot prove correct save state; an optimizer can find exploits but cannot define desirable pacing; a subjective critic can prefer a scene while missing unreachable progression.

Evaluation therefore needs a typed claim/evidence graph with explicit coverage gaps and escalation.

### 5.3 Recommendation

Adopt the evaluation topology below as a candidate foundation, then validate evaluator technologies/costs/reliability through the bounded experiments rather than assuming tool capability.

## 6. Alternatives considered

### A. One end-to-end AI player/judge — reject

Conceptually simple but creates one failure/Goodhart surface and weakly separates inability to play, inability to understand, and actual product defects.

### B. Traditional unit/code coverage as primary quality metric — reject

Necessary for code quality but does not establish gameplay state-space, quest progression, economy, player surface, accessibility, or experiential quality.

### C. Golden scenarios only — reject

Strong regression signal but can ossify known paths and miss broad possibility-space failures/exploits. Combine with semantic coverage, generative/adversarial search, and periodic new cases.

### D. Fully visible evaluator suite — reject as universal rule

Visibility aids development, but high-Goodhart probes benefit from some independent/protected variants.

### E. Hidden/protected evaluation as primary suite — reject

Opaque failures damage debugging and specification clarity. Protect selected sensitive subsets; keep most specification/invariant evidence visible and versioned.

### F. Average many subjective judge scores — reject

Correlation can make a panel falsely confident. Preserve rubric dimensions, pairwise decisions, reasons, disagreement, order randomization, and evaluator versions.

## 7. Evaluation vocabulary

- **claim** — bounded assertion requiring evidence;
- **oracle/check** — evaluator for a specific claim/failure mode;
- **scenario** — versioned initial state + actions/conditions + expected evidence/coverage;
- **semantic coverage** — which meaningful game possibility dimensions were exercised;
- **persona/policy** — versioned synthetic player objective/constraints/action strategy;
- **golden scenario** — high-value stable end-to-end regression journey;
- **protected scenario/probe** — evaluator input/configuration not freely controlled by judged producer;
- **evidence bundle/index** — candidate-bound refs/results/coverage/gaps;
- **evaluator drift** — changed verdict/distribution caused by evaluator/config version;
- **escape** — defect later discovered that required earlier evaluator route failed to detect.

## 8. AGE-D1 — Claim-to-evidence matrix

Candidate mapping:

| Claim | Minimum evidence direction | Stronger evidence when risk warrants |
|---|---|---|
| deterministic gameplay correctness | unit/property/invariant + deterministic scenario/replay | independent/protected scenario, fuzz/state search |
| real integration | shared/production gameplay kernel scenario + save/state/event evidence | full executable player-surface trace/capture |
| persistence/migration | save/load fixtures + migration reports + invariants | historical/protected corruption cases |
| progression reachability | graph/state search + scenarios | adversarial branch/fuzz + long runs |
| economy/automation viability | batch simulation + persona distributions | optimizer/exploit search + real-kernel rerun |
| quest solvability | structural search + referenced-state checks | synthetic execution + branch/expiry adversarial cases |
| narrative consistency | fact/knowledge/chronology checks | independent contradiction search + subjective narrative review |
| UX/accessibility | task-completion trace + player-surface evidence | alternate input/accessibility profiles + independent critic |
| visual/audio correctness | controlled capture + objective technical checks | multimodal/audio structured critics + protected golden cases |
| experiential quality | objective failures cleared + multidimensional telemetry + structured subjective panel | candidate tournament + diverse synthetic play + protected cases |
| performance | reproducible workload distributions | stress/long-run/platform variants |

A task compiler later binds concrete required checks to claims; this proposal does not create a universal fixed pipeline.

## 9. AGE-D2 — Semantic gameplay coverage

### 9.1 Coverage dimensions

Candidate dimensions:

- interaction verbs/actions;
- item/resource/content category transitions;
- world/time/weather/environment transitions;
- progression capabilities/gates/branches;
- quest objective/branch/failure types;
- NPC schedule/social/knowledge/relationship transitions;
- economy source/sink/transform/trade patterns;
- production/automation/logistics operations;
- exploration/region/access transitions;
- combat/risk/failure/recovery types if present;
- save/migration schema/state variants;
- input/control/accessibility profiles;
- UI/task flows;
- narrative/world consequence transitions;
- visual/audio feedback categories;
- error/corruption/recovery cases;
- lifestyle/soft-specialization trajectories.

Exact taxonomy emerges from canonical system specs.

### 9.2 Coverage record

```yaml
semantic_coverage_schema_version: <ref>
scenario_or_run: <id>
covered:
  dimensions: {}
  transitions: []
known_uncovered: []
not_applicable: []
coverage_evidence_refs: []
```

### 9.3 Coverage is diagnostic

100% of a weak taxonomy proves little. Adding meaningless tests to fill a coverage cell is Goodharting. Review coverage schema against real escapes/new systems and maintain protected/novel variants.

### 9.4 Interaction coverage

Prefer transition/interaction coverage over mere object visitation. “Used crop X” is weaker than “plant → growth under condition → harvest → transform → sell/gift/quest/use → persist/reload” where those interactions matter.

## 10. AGE-D3 — Scenario, golden, and replay architecture

### 10.1 Scenario definition

Conceptual schema:

```yaml
scenario_id: <stable>
scenario_version: <version>
purpose/claims: []
build/content requirements: []
initial_state_ref: <canonical snapshot/factory>
seed_manifest: <optional>
input_profile: <optional>
actions_or_policy_ref: <script/policy>
advance_rules: <time/tick>
expected:
  invariants: []
  events/state predicates: []
  save/replay expectations: []
  player_surface_evidence: []
  performance constraints: []
semantic_coverage_tags: []
protected_components: []
```

### 10.2 Golden scenario selection

Keep a small set of integrated journeys that exercise critical system intersections rather than every feature. Candidate categories from the seed include first morning, planting/harvest/sale, social/quest, exploration/combat, season transition, automation, region unlock, and mature save/load; final set follows actual game design.

### 10.3 Scenario evolution

A changed expected result must distinguish:

- intended specification/product change;
- evaluator/scenario correction;
- regression baseline update;
- masking of a defect.

Scenario/expected changes are reviewable evidence changes; protected/golden changes face stronger policy.

### 10.4 Real-kernel principle

Important scenario claims should execute the same gameplay kernel/domain rules as production. Test-only duplicate implementations are not integration evidence.

## 11. AGE-D4 — Synthetic player population

### 11.1 Policy classes

Use several complementary mechanisms:

**Deterministic scripted policies**
- exact regression/known route;
- reliable reproduction;
- limited novelty.

**Rule-based/behavioral personas**
- novice/low-skill/chore-averse/explorer/social/farmer/industrialist/collector/etc.;
- explicit assumptions and stable comparisons.

**Search/planning/optimization policies**
- maximize defined objectives;
- expose dominance/path efficiency/dead ends;
- dangerous if treated as desirable play.

**Fuzz/chaos/exploit policies**
- strange action sequences, boundary states, resets, save/load, rapid switching;
- target invariants/exploits.

**LLM/VLM interactive policies**
- potentially useful for UI/discovery/open-ended tasks;
- capability/reliability/cost must be benchmarked; no current claim here.

### 11.2 Policy record

```yaml
policy_id/version: <ref>
mechanism: SCRIPTED | RULE_BASED | SEARCH | FUZZ | LLM | VLM | OTHER
goals/objectives: []
knowledge_visible: []
constraints/preferences: []
action_interface: <semantic/game interface>
randomization: <seed/distribution>
model/tool refs: <if relevant>
known_biases/limitations: []
```

### 11.3 Population rule

No aggregate “average synthetic player” should become acceptance authority. Compare distributions and disagreements by policy/goal.

## 12. AGE-D5 — Simulation, dominance, and exploit search

### 12.1 Accelerated simulation

Headless/shared-kernel execution should support game-time acceleration for long-horizon questions where presentation is unnecessary.

Claims include:

- economy resource stocks/flows/sinks;
- progression reachability/velocity;
- automation adoption/payback/burden;
- NPC/social/world-state stability;
- quest/event cadence;
- long-run invariants/performance;
- strategy/path diversity.

### 12.2 Exploit search targets

- unbounded resource/currency loops;
- duplicate/save-reset/reload abuse;
- gate bypass/circular progression;
- dominant low-risk/high-reward route;
- automation recursion/zero-cost loops;
- market/arbitrage loops if markets exist;
- quest/reward repetition;
- world/NPC state contradictions;
- timing/event boundary bugs;
- state corruption/recovery abuse;
- metric/evaluator gaming candidates.

### 12.3 Differential search

When possible, compare:

- same policy across candidate versions;
- different policies on same version;
- abstract simulation versus real-kernel scenario;
- visible evaluator-optimized candidate versus protected probes.

Unexpected differences are evidence questions, not automatic regressions.

## 13. AGE-D6 — Structured subjective evaluation

### 13.1 Objective-first gate

Before subjective judging, surface obvious correctness/structural failures. A beautiful but broken scenario should not win a style/fun comparison merely because judges overlook state corruption.

### 13.2 Rubric pattern

Break broad questions into dimensions, for example:

- clarity/feedback;
- agency/meaningful choice;
- burden/repetition;
- pacing/discovery;
- strategy/lifestyle identity;
- narrative/character consistency;
- visual hierarchy/style identity;
- audio function/emotional fit;
- accessibility concerns;
- novelty/content repetition;
- consequence/recovery fairness;
- late-game ambition.

Not every task uses every dimension.

### 13.3 Comparison protocol

For important subjective choices:

1. bind exact evidence/candidates;
2. clear objective failures;
3. use atomic rubric prompts;
4. randomize candidate order/labels where useful;
5. run multiple independent judge episodes/configurations;
6. record per-dimension reasons/uncertainty;
7. include adversarial critique;
8. measure disagreement;
9. collect discriminating evidence or preserve alternatives when unresolved.

### 13.4 No score authority

Scores may summarize one rubric dimension for analysis but cannot become the sole integration/reward objective.

## 14. AGE-D7 — Protected evaluation

### 14.1 Candidate protected surfaces

- selected held-out gameplay scenarios/variants;
- hidden seeded exploit/specification-gaming probes;
- architecture invariant cases;
- factory benchmark ground truth;
- selected economy/progression personas/seeds;
- visual/UX/accessibility regression cases where disclosure trivializes gaming;
- evaluator thresholds/configuration where needed.

### 14.2 Protection principles

- producer cannot freely modify/read the exact protected ground truth used as sole gate;
- protected artifacts still have stable IDs/versions/change history;
- results expose actionable failure classes/evidence as far as possible;
- protected suite changes follow judge-affecting meta-review/verification;
- visible specification/tests remain the majority development surface where practical.

### 14.3 Leakage/overfit

Monitor repeated tuning to protected feedback. Rotate/add variants based on real escapes and benchmark whether holdout performance predicts broader outcomes.

## 15. AGE-D8 — Evaluator lifecycle and provenance

### 15.1 Evaluator record

```yaml
evaluator_id: <stable>
evaluator_version: <version/config hash>
evaluator_kind: CHECK | SIMULATOR | POLICY | JUDGE | PROTECTED_ORACLE | AGGREGATOR
implementation/model/tool_ref: <ref>
rubric/policy_ref: <ref>
input_schema_version: <ref>
output_schema_version: <ref>
environment_ref: <ref>
randomization/seed policy: <ref>
benchmark_refs: []
known_limitations: []
```

### 15.2 Result record

Every material result binds:

- candidate/build/content state;
- evaluator version;
- input evidence hashes/scenario/policy;
- environment;
- randomization/order;
- structured outcome;
- uncertainty/disagreement/coverage gaps;
- raw artifact refs as needed.

### 15.3 Evaluator changes

A new model/rubric/threshold/policy version does not silently reinterpret historical evidence. Compare frozen benchmark/evidence sets, quantify decision/escape drift, and establish explicit reopen conditions.

### 15.4 Evaluator failure

Evaluator infrastructure failure is `INCONCLUSIVE/NOT_RUN`, not product PASS. Continue unaffected work or use predeclared replacement evidence; do not invent waivers.

## 16. Evidence aggregation and escalation

### 16.1 Claim status

For each claim maintain:

```text
PASS
FAIL
FLAKY
INCONCLUSIVE
NOT_RUN
```

with evidence refs and coverage gaps.

### 16.2 Contradictory evidence

When checks/judges disagree:

1. verify exact candidate/input/evaluator versions;
2. classify disagreement (fact, coverage, nondeterminism, rubric, subjective preference, policy bias);
3. gather discriminating evidence;
4. rerun/reproduce where justified;
5. preserve disagreement if subjective/underspecified;
6. reopen specification/evaluator rather than force one answer.

### 16.3 Escalation ladder

```text
focused deterministic evidence
 -> independent rerun/review
 -> broader scenario/persona set
 -> adversarial/exploit search
 -> protected evaluation
 -> candidate comparison/tournament
 -> specification/replanning
```

Human intervention is not the routine tie-break.

## 17. Interfaces and dependencies

### W1-TEC-02

Needs deterministic canonical simulation, stable state hashes/snapshots, commands/events/queries, save/replay, accelerated execution, content package identity, workload/performance evidence.

### W1-TEC-01

Engine evaluation should prove automation-friendly headless/CLI execution, deterministic/controlled capture, build/test integration, agent-operable asset/content flow, and profiling/evidence hooks.

### W1-DES-01

Evaluation supplies lifestyle/path diversity, discovery cadence, burden, decision density, semantic role/interaction coverage, and late-game trajectory evidence.

### W1-DES-02

Supplies economy/progression persona simulations, dominance/exploit search, payback/sink/sensitivity/reachability evidence.

### W1-DES-03

Supplies quest solvability, fact/knowledge/chronology consistency, schedule/social/world-state simulations, semantic content repetition, and structured narrative critics.

### W1-EXP-01

Supplies semantic-action task flows, accessibility profiles, controlled media capture, technical media checks, multimodal/audio critics, and evaluator calibration.

### Factory/trust/CI synthesis

Game evaluators consume common EvidenceRequirement/Satisfaction, ArtifactIdentity, protected-evaluation, evaluator-versioning, retention, and trust-boundary semantics.

### W1-SYN-TECH / W1-SYN-GAME

Both syntheses should consume exact evaluation requirements and keep unbenchmarked evaluator technology choices experimental.

## 18. Bounded experiments

### AGE-E1 — Seeded defect/oracle portfolio

Inject known defects spanning state correctness, save/load, progression dead end, economy exploit, quest contradiction, UI feedback, visual defect, and subjective pacing issue into bounded scenarios.

**Pass:** appropriate evaluator classes detect/localize their target defects; no single evaluator is expected to catch all.  
**Failure:** claim/evidence routing or oracle coverage is insufficient.

### AGE-E2 — Semantic coverage mutation

Define a small coverage taxonomy, remove a transition/system interaction from scenarios, then add tests that merely touch objects without exercising semantics.

**Pass:** semantic coverage identifies the meaningful missing transition and resists superficial count inflation.  
**Failure:** taxonomy can be Goodharted too easily.

### AGE-E3 — Persona diversity benchmark

Run scripted, bounded-rational, optimizer, and fuzz policies on a shared simplified sandbox with several viable strategies.

**Pass:** policies produce meaningfully different trajectories/failures; aggregation preserves differences rather than declaring one representative.  
**Failure:** persona architecture has cosmetic labels only.

### AGE-E4 — Exploit search benchmark

Seed known positive loops/gate bypasses/timing-reset exploit plus benign high-efficiency strategy.

**Pass:** search finds seeded exploits and distinguishes them from intended powerful strategy using constraints/invariants/review.  
**Failure:** exploit oracle misses loops or equates efficiency with exploit.

### AGE-E5 — Protected leakage/overfit test

Tune a candidate against visible scenarios while protected variants contain related but nonidentical seeded defects.

**Pass:** protected suite finds specification gaming; producer cannot mutate ground truth; diagnostics support remediation.  
**Failure:** holdout is ineffective or too opaque.

### AGE-E6 — Evaluator drift replay

Run frozen evidence through two evaluator/rubric/model versions including intentional threshold/rubric changes.

**Pass:** changed decisions are attributable/versioned and reopen conditions can be evaluated.  
**Failure:** evaluator changes silently rewrite project truth.

### AGE-E7 — Subjective disagreement tournament

Prepare candidate gameplay/media/narrative evidence with clear, subtle, and genuinely ambiguous differences; run randomized structured judge panels.

**Pass:** obvious defects are consistent, ambiguous cases preserve disagreement/uncertainty, and pairwise order effects are measured.  
**Failure:** panel produces false consensus or uninterpretable scores.

### AGE-E8 — Long deterministic simulation reproducibility

Run the same long scenario/policy/seeds repeatedly and compare canonical state/event/economy/progression summaries.

**Pass:** declared deterministic scope reproduces; nondeterministic dimensions are explicit; performance/cost is measured.  
**Failure:** long-horizon evidence cannot be trusted/replayed.

### AGE-E9 — Player-surface versus simulation mismatch

Seed cases where canonical state is correct but UI/visual/audio feedback is wrong, and vice versa.

**Pass:** paired evidence surfaces catch both directions and prevent one from standing in for the other.  
**Failure:** integration evaluation is surface-blind.

### AGE-E10 — Evaluator cost/frontier benchmark

Run representative task classes with minimal, normal, and high-risk evaluator routes.

**Pass:** stronger routes improve unique defect/escape detection where expected without needlessly serializing all work; costs/queue effects are visible.  
**Failure:** evaluator routing is either weak or collapses throughput/frontier.

## 19. Observability

Track by claim/evaluator/policy/version:

- required evidence completeness;
- PASS/FAIL/FLAKY/INCONCLUSIVE/NOT_RUN;
- semantic coverage dimensions/transitions/gaps;
- golden/protected scenario pass/unique defect yield;
- seeded defect detection/escape rates;
- defect classes unique to each evaluator type;
- scenario flake/reproducibility;
- persona trajectory/path diversity;
- system participation/goal distributions;
- exploit findings/severity/yield;
- progression unreachable/dead-end findings;
- economy dominance/sensitivity/sink findings;
- quest/narrative contradiction/solvability findings;
- player/simulation surface mismatch;
- subjective judge disagreement/order effects;
- evaluator version decision drift;
- protected leakage/overfit incidents;
- evaluation runtime/cost/queue impact;
- evidence artifact retrieval/retention failures.

Never optimize evaluator pass rate or finding count as a standalone goal.

## 20. Failure modes and defenses

### Fun-score Goodhart
**Failure:** agents optimize one engagement/fun number.  
**Defense:** claim/evidence matrix, multidimensional telemetry, structured critics, protected/adversarial tests.

### Coverage theater
**Failure:** tests touch every object but miss meaningful transitions.  
**Defense:** semantic transition/interaction coverage and mutation benchmark.

### Golden-path lock-in
**Failure:** game evolves only around fixed regression journeys.  
**Defense:** semantic coverage, new/protected variants, persona/adversarial search, periodic suite revision.

### Optimizer defines design
**Failure:** fastest-money/progression bot becomes definition of good play.  
**Defense:** multiple objectives/personas; dominance is a failure signal, not preferred experience.

### Synthetic-player anthropomorphism
**Failure:** policy behavior interpreted as human preference.  
**Defense:** explicit policy assumptions/limitations and later player-surface/subjective evidence.

### Protected oracle opacity
**Failure:** failures cannot be debugged.  
**Defense:** structured failure categories/evidence, protect ground truth not accountability.

### Protected overfit
**Failure:** repeated feedback leaks the holdout.  
**Defense:** variants/rotation/leakage metrics/meta-review.

### Evaluator drift
**Failure:** model/rubric upgrade silently changes verdicts.  
**Defense:** versioning/frozen replay/drift benchmark/reopen policy.

### Correlated judge panel
**Failure:** multiple runs share same bias/context and create false confidence.  
**Defense:** independent episodes/configurations, randomized order, dissent/adversarial critic, protected evidence.

### State-hash false proof
**Failure:** state is correct but player experience broken.  
**Defense:** pair simulation and player surfaces.

### Screenshot false proof
**Failure:** rendering looks correct while simulation/state wrong.  
**Defense:** same paired evidence requirement.

### Expensive-everything pipeline
**Failure:** every task waits on full simulation/VLM/long-run suite.  
**Defense:** task/risk-specific evidence routes plus periodic/deep/protected tiers.

## 21. Risks and tensions

- Semantic coverage schemas can become large/brittle as systems grow; they need domain ownership and versioning.
- Protected evaluation improves anti-Goodhart resistance but increases trust/permission/storage complexity.
- Large persona populations can consume compute while still missing real player motivations.
- Deterministic simulation can bias architecture if applied beyond the gameplay evidence boundary.
- Subjective evaluator models may share correlated training biases and drift.
- Long simulations/exploit search can generate false positives requiring explanation rather than automatic nerfs.
- High evaluation cost can reduce autonomous throughput; routing must be measured against escape reduction.

## 22. Open questions

1. Which semantic coverage dimensions provide strong predictive value without becoming an unmaintainable taxonomy?
2. Which golden scenarios best exercise the first real walking skeleton and later mature-game intersections?
3. Which evaluator technologies can reliably operate the eventual real game UI versus simulation API, and at what cost/latency?
4. Which protected surfaces give the highest anti-Goodhart value?
5. How should persona policies be selected/calibrated against later observed player behavior without turning analytics into one target persona?
6. What state/action abstraction supports both real gameplay and accelerated simulation without creating a fake test implementation?
7. How should exploits be distinguished from creative emergent strategies?
8. Which subjective dimensions require multimodal temporal evidence rather than static captures/state summaries?
9. How much evaluator disagreement is acceptable for different claim/risk classes?
10. What evaluator drift threshold/escape evidence should reopen old decisions?
11. How should protected evaluator storage/permissions/diagnostics integrate with the chosen CI/control-plane architecture?
12. What evaluation-cost/WIP policy keeps quality-pipeline throughput healthy as the game grows?

## 23. Reopen conditions

Reopen if:

- seeded-defect benchmarks show evaluator classes miss their intended failure modes;
- semantic coverage is easily gamed or too costly to maintain;
- synthetic policies converge despite intended diversity or do not correlate with relevant real-kernel failures;
- exploit search produces intolerable false negatives/positives;
- protected suites fail to find visible-metric gaming or become too opaque to remediate;
- evaluator version drift materially changes decisions without usable diagnostics;
- subjective panels show large correlated/order bias on benchmark cases;
- long deterministic simulation cannot reproduce or is too costly for intended evidence classes;
- real implementation cannot expose both player and simulation surfaces without duplicated gameplay logic;
- evaluation routing collapses READY/quality throughput without proportional escape reduction;
- later real player evidence contradicts strong synthetic/subjective evaluator assumptions.

## 24. Required critique and downstream work

Required independent critiques:

- `W1-REV-TECH` — attack determinism, real-kernel execution, evidence reproducibility, protected infrastructure, evaluator versioning, CI/cost, and fake-integration risks.
- `W1-REV-GAME` — attack whether semantic/persona/subjective evaluation actually represents the intended sandbox, narrative, progression, accessibility, visual/audio, and experiential claims without Goodharting them.

W1-SYN-TECH and W1-SYN-GAME should consume this exact reviewed work and treat concrete evaluator tool/model choices as experimental until benchmarked. This artifact is non-canonical and authorizes no gameplay/evaluator implementation.
