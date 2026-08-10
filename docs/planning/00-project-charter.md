# Project Charter — Seed

**State:** SEED, except explicitly marked canonical human directives

## 1. Project

Everfield is an AI-native, large-scale farming / life / exploration sandbox whose reference model for systemic density is **Stardew Valley**, while intentionally targeting a substantially broader player possibility space, deeper late-game progression, and far greater extensibility.

The game and the development system are both products of the project.

## 2. Primary Experiment

The project asks whether a genuinely complex commercial-scale game can be designed, implemented, tested, reviewed, expanded, balanced, and maintained predominantly through autonomous AI-agent loops when the work is decomposed into explicit, measurable, resumable contracts.

The expected answer must come from the resulting system and game, not from a one-shot prototype.

## 3. Non-Negotiable Development Constraint

All normal development activity is performed by AI agents.

This includes:

- planning;
- architecture;
- programming;
- tests;
- CI;
- debugging;
- code review;
- verification;
- integration;
- game design;
- quest design;
- narrative production;
- balance;
- visual design and review;
- content generation;
- performance work;
- checkpoint retrospectives;
- backlog generation and retirement;
- improvement of the agent-development system itself.

A human may intervene with an explicit directive, but the factory must never require routine human approval to make progress.

## 4. Development System Objective

The mature factory should support approximately 10–20 or more useful concurrent agent sessions when sufficient independent work exists.

Concurrency is useful only when tasks are safe to execute independently. The planning and architecture process must therefore maximize a broad conflict-free work frontier rather than merely produce many issues.

The target behavior is:

```text
fresh agent
  -> canonical entry point
  -> obtain role/task
  -> claim or resume work
  -> load bounded context
  -> modify bounded ownership surface
  -> execute real checks
  -> inspect structured evidence
  -> iterate
  -> commit/push
  -> leave reconstructable handoff
  -> independent review
  -> revision
  -> second independent review
  -> independent verification
  -> controlled squash integration
  -> dependency graph unlocks more work
```

## 5. Product Objective

The game should eventually feel larger than the player expects and support many meaningful ways to live in its world.

The target is not merely a larger item count than Stardew Valley. It is a larger **possibility space** created by interacting systems, optional specializations, progression paths, exploration, relationships, narrative, economy, automation, production, discovery, and authored content.

The desired experience is closer to:

> many overlapping games sharing the same world

than:

> one main game with several side activities.

## 6. Automation as a Core Fantasy

Automation is a central progression axis, not a convenience toggle.

A broad design hypothesis to preserve for later validation:

```text
manual execution = low capital cost + high labor cost
automation       = high setup/capital cost + low recurring labor
```

Most substantially repetitive chores should eventually have an automation path, but automation should be expensive, gated, infrastructural, and capable of serving as a deep late-game economic sink.

Automation should free the player to operate at a higher level of ambition rather than remove gameplay.

## 7. Sandbox Principle

The game should avoid a single canonical playthrough.

Different players should be able to emphasize different overlapping identities such as farming, exploration, mining, combat, commerce, crafting, social progression, quests, collecting, property development, optimization, industrial production, or automation without selecting a rigid class.

Progression gates are allowed. Forced uniform progression is not the design target.

## 8. Extensibility Principle

Continuous expansion is expected.

Architecture and content pipelines should therefore make it cheap to add new:

- items;
- crops;
- resources;
- recipes;
- production chains;
- machines;
- buildings;
- NPCs;
- dialogue;
- quests;
- enemies;
- regions;
- activities;
- world events;
- progression layers.

Extensibility is both a software requirement and a content-production requirement.

## 9. Quality Principle

Success is not defined by generated code volume or number of closed issues.

The factory should optimize for:

> verified, recoverable, safely composable progress.

No implementation agent is the final authority on its own correctness.

No single test suite or subjective score is the final authority on product quality.

## 10. Current Phase Goal

The immediate project output is not game code.

It is a reviewed **plan for producing the plans** that will later define:

1. the autonomous factory;
2. the technical architecture;
3. the full game-design space;
4. the evaluation and evidence system;
5. the dependency-aware GitHub Issue graph;
6. the checkpoint and re-planning machinery.

## 11. Explicit Non-Goals of the Current Phase

Do not yet:

- choose the final engine without comparative evaluation;
- freeze the final visual style;
- author the complete quest catalog;
- enumerate the complete game feature set;
- create thousands of implementation issues;
- treat the current Stardew-derived model as a cloning specification;
- create gameplay code merely to demonstrate activity.

## 12. Success Condition for Leaving the Planning Bootstrap Phase

The bootstrap phase is complete only when the repository contains a reviewed process that can autonomously produce, criticize, revise, and validate the detailed plans required for implementation.

## 13. Main-Branch Integration Policy — Canonical Human Directive

This section is a binding human directive even while the surrounding charter remains a SEED artifact.

**Every pull request or task integrated into `main` must be integrated using squash merge.**

Consequences:

- task branches may preserve many WIP/review/correction commits during execution;
- accepted work lands on `main` as one squash commit per integrated PR/task outcome;
- merge commits are not an allowed normal integration method;
- rebase-merge is not an allowed normal integration method;
- agents must not bypass this rule merely because repository settings expose other merge buttons or APIs;
- future branch, PR, merge-queue, reviewer, and integration protocols must preserve squash-only integration to `main` unless a later explicit human directive supersedes it.

This directive exists to keep `main` history task-oriented while allowing agents to work iteratively and leave recoverable WIP history on task branches.
