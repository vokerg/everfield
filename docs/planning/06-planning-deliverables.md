# Planning Deliverables — Seed

**State:** SEED

## Purpose

This document defines the classes of artifacts that should exist before Everfield enters high-throughput implementation.

It is not yet a schedule. It is an artifact map for the future Planning Program v1.

## 1. Project Governance

Expected canonical artifacts:

- Project Charter
- AI-Only Autonomy Constitution
- Human Directive / Override Protocol
- Planning Canonicality Rules
- Decision Record Format
- Risk Register
- Legal/IP/Provenance Policy

## 2. Agent Operating Model

Expected canonical artifacts:

- root `AGENTS.md`
- nested/module context rules
- canonical agent entry-point specification
- role definitions
- task selection protocol
- task claiming protocol
- stale-claim recovery protocol
- branch/session lifecycle
- commit/WIP policy
- structured handoff schema
- continuation-agent protocol
- stopping rules
- discovered-work protocol
- context-loading protocol

## 3. GitHub Control Plane

Expected canonical artifacts:

- issue taxonomy
- issue state machine
- labels/fields conventions
- sub-issue conventions
- dependency conventions
- branch naming/linking rules
- PR lifecycle
- review state representation
- merge/squash rules
- merge queue policy
- automation permissions
- machine APIs/commands for dispatch and claiming

## 4. Dependency and Parallelism Model

Expected canonical artifacts:

- dependency relationship taxonomy
- module ownership map
- conflict-surface representation
- machine-readable dependency schema
- READY frontier algorithm
- WIP policy
- scheduling priority model
- stale-work policy
- dependency-cycle validator
- parallelism health metrics

## 5. Review and Verification

Expected canonical artifacts:

- Review 1 protocol
- Review 2 protocol
- independent verifier protocol
- reviewer disagreement protocol
- protected-evaluation trust model
- protected-test change protocol
- specification-gaming defenses
- evidence sufficiency rules by task type
- integration eligibility rules

## 6. CI / Execution / Evidence

Expected canonical artifacts:

- build strategy
- headless execution strategy
- test taxonomy
- scenario runner specification
- scenario DSL/schema
- deterministic execution strategy
- replay format
- canonical state snapshot/hash strategy
- structured run-report schema
- screenshot/video capture strategy
- telemetry schema
- artifact provenance model
- evidence retention/storage topology
- flaky-test/scenario policy

## 7. Factory Measurement and Self-Improvement

Expected canonical artifacts:

- process metrics catalog
- factory health dashboard specification
- implementation-agent benchmark suite
- handoff benchmark suite
- reviewer benchmark suite
- verifier/reward-hacking benchmark suite
- planning/dependency benchmark suite
- integration/concurrency benchmark suite
- visual/narrative evaluator calibration suites
- factory protocol change process
- rollback protocol

## 8. Engine / Technical Foundation

Expected canonical artifacts:

- engine evaluation rubric
- representative engine spikes
- scored comparison
- engine ADR
- language/runtime ADRs where required
- module architecture
- architecture dependency rules
- event/command/query conventions
- data serialization strategy
- persistence/save architecture
- migration strategy
- determinism boundaries
- performance budgets
- platform targets
- release/build architecture

## 9. Game Design Foundation

Expected canonical artifacts:

- Game Design Bible
- game pillars
- core loop specification
- day/season/long-horizon loop model
- player possibility-space model
- sandbox specialization model
- progression philosophy
- discovery/unlock philosophy
- automation philosophy
- late-game philosophy
- player-agency principles
- chore/repetition policy
- extensibility/content-growth principles

## 10. System Design Specifications

At minimum, planning should decide whether separate canonical specifications are required for:

- world simulation/time/calendar/weather
- player/avatar
- items/inventory
- farming
- animals/ranching
- tools
- gathering
- fishing/optional skill activities
- mining
- combat
- dungeons
- exploration/travel/regions
- crafting
- production chains
- automation
- logistics
- economy/shops/trade
- buildings/property
- NPC simulation
- relationships/social systems
- dialogue
- quests
- story/world-state progression
- events/festivals
- cooking
- collections
- skills/progression
- late-game systems

The final system decomposition should emerge from planning rather than blindly follow this list.

## 11. Content Architecture

Expected canonical artifacts:

- content ontology
- stable ID/reference model
- schema/versioning rules
- validation rules
- content compiler strategy
- quest schema/grammar
- dialogue representation
- NPC fact/consistency representation
- world lore/chronology representation
- item/crop/recipe/etc. schemas
- localization architecture
- content ownership/merge strategy
- high-volume AI content production process

## 12. Experience Design

Expected canonical artifacts:

- UX principles
- input/navigation model
- onboarding/discovery model
- UI architecture
- accessibility requirements
- visual-direction process
- visual bible format
- asset-generation process
- visual consistency/evaluation process
- audio-direction process
- audio asset/evaluation process

## 13. Automated Game Evaluation

Expected canonical artifacts:

- golden scenario suite
- game-semantic coverage model
- synthetic-player architecture
- player persona catalog
- difficulty measurement strategy
- economy simulation framework
- progression reachability checks
- exploit-search strategy
- long-simulation strategy
- quest solvability validation
- narrative consistency validation
- engagement proxy framework
- subjective judge protocols
- evaluator versioning/provenance

## 14. Planning-to-Issue Compiler

Before mass issue generation, the project should define how canonical specifications become executable work.

Expected artifacts:

- issue schema/template
- epic/sub-issue rules
- acceptance-criteria requirements
- allowed/forbidden modification-surface rules
- dependency extraction rules
- evidence requirement rules
- test requirement rules
- issue sizing rules
- automatic issue validation
- orphan requirement detection
- issue graph audit process

## 15. Milestone Zero Specification

The first implementation milestone should primarily validate the factory.

Candidate success statement:

> A fresh agent can obtain a READY task, claim it safely, branch from main, implement a deterministic player-visible change, run real CI, generate structured evidence and visual artifacts, hand the unfinished/finished work to another fresh agent, pass two independent reviews and protected verification, then squash-integrate safely and unlock downstream work.

Milestone Zero should exercise the entire autonomous lifecycle before implementation throughput is increased.

## 16. First Gameplay Walking Skeleton Specification

After Milestone Zero, define the smallest coherent gameplay flow that exercises multiple real systems.

Directional example:

```text
launch
 -> load tiny world
 -> move
 -> interact with soil
 -> plant
 -> water
 -> advance time
 -> harvest
 -> inventory update
 -> sell
 -> currency update
 -> save
 -> reload
 -> reproduce expected state
```

The actual slice must be planned after engine/runtime decisions.

## 17. Checkpoint System

Expected canonical artifacts:

- micro-checkpoint triggers
- macro-checkpoint triggers
- checkpoint input evidence
- checkpoint role/context
- authority to create/retire/reprioritize work
- architecture health checks
- parallelism health checks
- gameplay/system health checks
- evaluator/factory health checks
- milestone reconsideration rules

## 18. Implementation Readiness Gate

High-throughput implementation should not begin merely because many documents exist.

The readiness decision should require evidence that:

- the agent entry path is defined;
- work can be claimed safely;
- dependencies/conflicts are machine-readable;
- tasks are resumable;
- CI produces structured evidence;
- review and verification are independent;
- protected quality surfaces exist or have an approved implementation path;
- architecture permits meaningful concurrency;
- initial game design is coherent enough to define the first vertical slice;
- Planning Program v1 can continue producing/revising future work autonomously.

## 19. Important Constraint

These deliverables should not all be produced serially by one agent.

Planning Program v1 must determine which can be developed concurrently, which require competing proposals, which require empirical spikes, and which are downstream syntheses.

The deliverable graph itself is one of the first dependency graphs Everfield must design correctly.
