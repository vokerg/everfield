# Evaluation and Evidence — Seed

**State:** SEED

## 1. Problem

An AI-only development system cannot rely on a human periodically launching the game and deciding whether everything feels acceptable.

Everfield therefore needs a network of machine-observable quality signals and specialized evaluators capable of detecting incorrect, incoherent, boring, inaccessible, unbalanced, visually broken, or architecturally dangerous work.

Evaluation infrastructure is not secondary tooling. It is part of the product architecture.

## 2. Core Rule

A claim such as "the feature works" must eventually resolve into inspectable evidence.

Evidence may include:

- build results;
- unit/property/integration tests;
- deterministic simulation;
- scripted gameplay scenarios;
- save/load comparisons;
- replay results;
- state invariants;
- telemetry;
- logs/traces;
- performance metrics;
- screenshots;
- visual diffs;
- short gameplay captures;
- content validation;
- progression graph validation;
- economy simulations;
- synthetic-player trajectories;
- independent reviewer findings.

No single evidence type is sufficient for all questions.

## 3. CI as Sensorium

CI should eventually emit structured machine-consumable reports rather than only green/red status.

Conceptual run report:

```json
{
  "commit": "...",
  "environment": "...",
  "build": {},
  "tests": {},
  "scenarios": {},
  "invariants": {},
  "save_load": {},
  "replays": {},
  "content_validation": {},
  "architecture_validation": {},
  "performance": {},
  "memory": {},
  "visual_evidence": [],
  "telemetry": [],
  "warnings": [],
  "baseline_comparison": {}
}
```

The exact schema is deferred.

## 4. Production Executable Testing

Important acceptance criteria should be tested through the real game executable or the same gameplay kernel used by the real executable.

The project should resist fake integration tests that duplicate gameplay logic inside test-only implementations.

A future machine-play interface may expose operations conceptually similar to:

```text
observe
act
advance
query_state
snapshot
save
load
capture_frame
```

This interface must obey real gameplay rules.

## 5. Deterministic Evidence

Where practical, gameplay execution should be reproducible from explicit inputs:

```text
build SHA
initial canonical state
random seed(s)
input/action sequence
final state hash
telemetry
visual captures
```

This should support exact reproduction by reviewers and verifiers.

Determinism boundaries and unavoidable nondeterminism require explicit design.

## 6. Scenario Testing

Major behaviors should have declarative gameplay scenarios.

Example conceptual scenario:

```text
Given a new farm state
And the player owns seed and a watering tool
When the player tills, plants, waters, advances days, and harvests
Then crop state progresses correctly
And inventory receives the output
And progression/economy observers receive the expected events
And the final state survives save/load
And required player-facing visual states are captured
```

Scenarios should be usable by implementation agents, reviewers, verifiers, regression CI, and checkpoint agents.

## 7. Golden Scenarios

A relatively small high-value end-to-end suite should continuously exercise the integrated game.

Potential future scenarios:

- first morning;
- first planting and harvest;
- first sale;
- first NPC relationship change;
- first quest completion;
- first mine/combat run;
- season transition;
- automation installation and operation;
- region unlock;
- save/load of a mature world.

These are not yet specifications.

## 8. Protected Evaluation Surfaces

Ordinary implementation agents should not control every oracle used to judge their work.

Potential protected surfaces:

- held-out tests;
- independently authored scenarios;
- invariant suites;
- hidden compositional tests;
- architecture policies;
- reward-hacking probes;
- factory benchmarks;
- verifier configuration.

Planning must decide where these surfaces live, who can change them, and how they are versioned.

## 9. Independent Test Authorship

Tests written by the implementer are useful evidence but should not be the only evidence.

Important features should eventually combine some of:

- specification-derived tests authored before implementation;
- implementation-local tests;
- independent test-author agent output;
- integration scenarios;
- held-out verifier tests;
- adversarial exploratory execution.

Mocks should not replace real integration evidence when the acceptance claim depends on real integration.

## 10. Visual Evidence

Game CI should capture deterministic or controlled screenshots for relevant scenarios.

A visual evidence record should eventually associate:

- build SHA;
- scenario ID;
- game/world state;
- location;
- camera;
- time/date/season;
- weather;
- active entities;
- screenshot/video artifact;
- expected baseline/reference where relevant;
- computed diff signals;
- visual-judge results.

Objective checks may detect missing assets, clipping, blank scenes, incorrect layout, unreadable text, or unexpected changes.

Multimodal critics may evaluate hierarchy, readability, thematic consistency, composition, feedback clarity, and polish.

## 11. Simulation Surface and Player Surface

Every important gameplay scenario should attempt to expose both:

### Player Surface

What the player sees/hears and can interact with.

### Simulation Surface

What canonical state, events, telemetry, and performance signals say happened.

A screenshot can look correct while state is wrong. State can be correct while presentation is broken.

Both matter.

## 12. Game Semantic Coverage

Traditional code coverage should not be the only notion of coverage.

Planning should explore semantic coverage such as:

- interaction verbs exercised;
- item/category transitions exercised;
- quest objective types exercised;
- region/gate transitions exercised;
- NPC schedule transitions exercised;
- production/automation operations exercised;
- save-schema variants exercised;
- world-state transitions exercised;
- progression graph regions traversed.

The goal is to know which parts of the game possibility space are actually being tested.

## 13. Synthetic Player Population

Automated playtesting should use multiple behavior profiles rather than one canonical optimizer.

Potential personas include:

- novice;
- low-skill player;
- high-skill player;
- optimizer;
- chore-averse player;
- explorer;
- farmer;
- industrialist;
- social player;
- quest-focused player;
- collector;
- completionist;
- minimalist;
- speedrunner;
- exploit hunter;
- chaos/fuzz player.

Different technologies may power different personas. The planning process should compare deterministic policies, search, learned agents, LLM agents, and multimodal agents where useful.

## 14. Do Not Reduce Fun to One Scalar

The project should explicitly resist creating a single `fun_score` and optimizing against it.

Potential proxies include:

- meaningful decision density;
- repetitive input burden;
- dead travel time;
- viable simultaneous goals;
- strategy diversity;
- progression velocity;
- discovery cadence;
- action-to-feedback latency;
- forced chore burden;
- automation payback period;
- dominant strategy prevalence;
- dead-end frequency;
- content repetition;
- failure recovery cost;
- path diversity.

Subjective evaluator panels interpret these signals rather than replacing them.

## 15. Subjective Judgment Protocol

Subjective quality questions should use structured evaluation rather than an unconstrained "is this good?" prompt.

Candidate pattern:

1. objective failure checks;
2. atomic rubrics;
3. independent judge runs;
4. pairwise comparison where appropriate;
5. randomized candidate order;
6. adversarial critique;
7. disagreement measurement;
8. additional evidence when uncertain;
9. evaluator-version recording.

Important decisions may use candidate tournaments rather than accepting the first viable design.

## 16. Specialized Oracles

Different questions require different evidence and evaluators.

| Question | Candidate evidence/oracles |
|---|---|
| Correctness | tests, invariants, scenarios, replay |
| Architecture | static checks, module graph, architecture critics |
| Visual correctness | screenshot diffs, multimodal critics |
| UX | interactive traces, task-completion playtests, visual critics |
| Quest solvability | graph validation, game execution |
| Quest quality | narrative critics, player cohorts, repetition metrics |
| Difficulty | synthetic cohorts, completion/failure distributions |
| Economy | batch simulations, exploit-seeking agents |
| Performance | profilers, deterministic benchmarks |
| Narrative consistency | canonical fact graph, contradiction search |
| Engagement | multidimensional telemetry plus subjective panels |

## 17. Goodhart Resistance

Agents may optimize whatever metric becomes easiest to satisfy.

The evaluation system should therefore use:

- multiple independent signals;
- protected holdouts;
- adversarial probes;
- randomization;
- metric versioning;
- evaluator disagreement;
- independent verification;
- explicit permissions around verification changes.

No implementation should be accepted merely because it made the visible dashboard greener.

## 18. Evaluator Versioning

Evidence should record the evaluator configuration that produced a judgment.

Conceptual metadata:

```text
judge_id
model/provider family if relevant
rubric version
input evidence hashes
decision
confidence/disagreement
timestamp
```

This allows future agents to separate product changes from evaluator changes.

## 19. Evaluation Escalation Without Humans

When evaluators disagree, the normal escalation path should be additional machine work:

```text
single evaluation
  -> independent reevaluation
  -> adversarial evaluation
  -> collect more runtime evidence
  -> run more player personas
  -> generate competing alternatives
  -> larger decision tournament
  -> checkpoint/re-plan
```

Human input remains optional external intervention, not the default tie-breaker.

## 20. Factory Evaluation

The factory itself needs benchmarks for:

- implementation success;
- handoff continuation;
- review defect detection;
- verifier detection of specification gaming;
- parallel integration conflict;
- planning/dependency quality;
- visual judge reliability;
- quest judge reliability;
- reward-hacking resistance.

Factory protocol changes should be tested against representative benchmark tasks before adoption.
