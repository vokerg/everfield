# Planning Program — Seed

**State:** SEED

## 1. Purpose

The immediate objective is not to produce the implementation backlog.

The immediate objective is to design and run a multi-agent planning program that can produce, criticize, synthesize, validate, and continuously revise the technical and game-design plans from which implementation work will later be generated.

The planning program itself must be explicit enough that fresh AI sessions can participate without hidden conversational context.

## 2. Planning Must Be Multi-Agent

No single planner should be trusted to produce the complete project architecture or game design.

The project is too broad and too coupled.

Planning should deliberately create independent viewpoints, expose disagreements, and require synthesis.

## 3. Proposed Planning Stages

### Stage A — Research Missions

Independent agents investigate bounded questions using current primary/authoritative sources where applicable.

Research outputs should separate:

- facts/evidence;
- interpretations;
- recommendations;
- unresolved uncertainty.

### Stage B — Domain Proposals

Domain planners produce concrete candidate specifications.

Each proposal should include:

- goals;
- constraints;
- system boundaries;
- player-facing behavior where relevant;
- dependencies;
- data/contracts;
- observability;
- testing/evaluation approach;
- failure modes;
- alternatives considered;
- open questions.

### Stage C — Independent Critique

Dedicated critics attempt to invalidate proposals rather than improve them politely.

Critique categories should include at least:

- hidden dependencies;
- untestable requirements;
- excessive coupling;
- scalability problems;
- insufficient parallelism;
- game-design contradictions;
- economy/progression exploits;
- subjective-quality blind spots;
- content-production cost;
- agent-context overload;
- reward/metric gaming.

### Stage D — Cross-Domain Synthesis

Synthesis agents reconcile interfaces and contradictions between domains.

The output is not a compromise by default. Where two assumptions cannot coexist, the synthesis agent must choose, justify, or trigger an experiment.

### Stage E — Empirical Spikes

Questions that cannot be resolved credibly through analysis should become bounded experiments.

Examples:

- engine comparison;
- headless execution reliability;
- screenshot capture;
- deterministic replay feasibility;
- merge friendliness of scene/resource formats;
- agent ability to manipulate representative assets;
- visual judge reliability;
- task handoff experiments.

Spikes produce evidence, not production architecture.

### Stage F — Revision

Domain proposals are revised using critiques and spike evidence.

### Stage G — Canonicalization

A proposal becomes CANONICAL only after satisfying its required review/evidence protocol.

Canonical decisions must record assumptions and conditions that would justify reopening them.

### Stage H — Dependency Extraction

Planning agents derive explicit system and work dependencies from the canonical corpus.

The dependency model must distinguish different relationship types rather than flatten everything into one generic dependency.

### Stage I — Testability and Observability Review

Every implementation-relevant requirement is reviewed for how an autonomous verifier can know whether it is satisfied.

Requirements without credible evidence paths are returned for redesign.

### Stage J — Parallelism Review

The planned architecture and work graph are examined specifically for safe concurrent execution.

Reviewers seek:

- bottleneck modules;
- giant shared files;
- unnecessary serialization;
- conflict surfaces;
- hidden global state;
- dependencies that could be replaced by stable interfaces/mocks/contracts.

### Stage K — Issue Generation

Only stable bounded regions of the plan are converted into executable GitHub Issues.

### Stage L — Dependency Audit

Independent agents validate generated issue graphs for:

- cycles;
- missing prerequisites;
- incorrect conflict declarations;
- orphan work;
- oversized tasks;
- ambiguous acceptance criteria;
- missing evidence requirements.

## 4. Candidate Planning-Agent Missions

The following missions are seeds, not final assignments.

### Factory Track

1. **Agent Operating Model Planner** — roles, episode lifecycle, handoffs, context loading.
2. **GitHub Control Plane Planner** — issue states, labels, claims, branches, PRs, merge queues, API behavior.
3. **Dependency/Scheduler Planner** — dependency types, READY frontier, WIP control, task selection.
4. **CI/Execution Planner** — build/test/scenario execution and structured reports.
5. **Evidence Planner** — artifacts, screenshots, videos, telemetry, provenance, retention.
6. **Review/Verification Planner** — independent reviews, verifier role, protected tests, anti-Goodhart controls.
7. **Checkpoint Planner** — global retrospectives, triggers, authority, re-planning.
8. **Factory Benchmark Planner** — internal benchmarks for implementation, review, handoff, planning, integration, reward hacking.
9. **Context Engineering Planner** — AGENTS hierarchy, work packets, retrieval strategy, context minimization.
10. **Factory Security/Integrity Planner** — protected surfaces, permissions, malicious/accidental evaluator corruption.

### Technical/Game Runtime Track

11. **Engine Evaluation Planner** — comparative evidence-based engine decision.
12. **Runtime Architecture Planner** — module boundaries and lifecycle.
13. **Determinism/Simulation Planner** — seeds, state hashes, replay, headless simulation.
14. **Persistence Planner** — save/load, migration, canonical state representation.
15. **Content Architecture Planner** — data-driven schemas, IDs, registries, validation, content compilers.
16. **Tooling Planner** — scenario DSL, validators, authoring and debugging tools.
17. **Performance Planner** — budgets, benchmark harnesses, long simulation.
18. **Platform/Release Planner** — targets, packaging, build reproducibility, release constraints.

### Game Design Track

19. **Core Loop Planner** — minute/day/season/long-horizon loops.
20. **Farming Planner** — farming depth and progression.
21. **Automation Planner** — chore automation, infrastructure, capital sinks, logistics.
22. **Economy Planner** — sources/sinks, markets, progression, simulation.
23. **Items/Crafting/Production Planner** — item ontology and production chains.
24. **World/Exploration Planner** — regions, gates, traversal, secrets, expansion.
25. **Mining/Combat/Dungeon Planner** — underground/exploration challenge loops.
26. **NPC Simulation Planner** — schedules, behavior, world interaction.
27. **Social/Relationship Planner** — friendship, relationships, gifts, social consequences.
28. **Quest/Narrative Architecture Planner** — quest grammar, branching, world state, consistency.
29. **Progression Planner** — cross-system progression graph and unlock cadence.
30. **Buildings/Property Planner** — farm/property/infrastructure expansion.
31. **Skill/Activity Planner** — fishing and other deep optional activities.
32. **Collections/Completion Planner** — collection loops without forcing one canonical playstyle.
33. **Late-Game Planner** — high-agency, high-capital, high-complexity systems.
34. **Sandbox Diversity Planner** — viable lifestyles and anti-dominant-strategy design.

### Experience/Content Track

35. **UX Planner** — interaction, onboarding, menus, accessibility.
36. **Visual Pipeline Planner** — art direction process, asset generation, visual consistency, visual CI.
37. **Audio Planner** — music/SFX pipeline and evaluation.
38. **Narrative Worldbuilding Planner** — lore, chronology, consistency structures.
39. **NPC/Dialogue Content Planner** — scalable authored social content.
40. **Quest Content Planner** — scalable quest production and evaluation.
41. **World Content Planner** — locations, secrets, encounters, events.
42. **Seasonal/Event Content Planner** — calendar-based content and recurring variation.

### Evaluation Track

43. **Synthetic Player Planner** — player personas and automated playtest agents.
44. **Difficulty Evaluation Planner** — challenge and accessibility measurement.
45. **Engagement Evaluation Planner** — multidimensional proxies and judge protocols.
46. **Visual Judge Planner** — objective + multimodal quality evaluation.
47. **Narrative Judge Planner** — consistency, interest, pacing, repetition.
48. **Balance Simulation Planner** — economy/progression simulation and exploit discovery.
49. **Game Semantic Coverage Planner** — coverage beyond code lines.
50. **Adversarial Playtest Planner** — exploit hunting, fuzz/search-based gameplay testing.

The planning program should decide which of these missions need splitting, merging, sequencing, or deletion.

## 5. Cross-Critique Matrix

Planning agents should not merely self-review.

Example directional relationships:

- Scheduler plan is attacked by Context, GitHub Control Plane, and Parallelism critics.
- Automation design is attacked by Economy, Sandbox Diversity, Progression, and Chore-Averse Player planners.
- Quest architecture is attacked by Content Architecture, Narrative Consistency, Progression, and Verification planners.
- Engine recommendation is attacked by CI, Visual Pipeline, Determinism, Git Mergeability, and Agent Ergonomics perspectives.
- Core loop is attacked by Sandbox Diversity, Automation, Progression, UX, and Engagement planners.

A future planning matrix should make these relationships explicit.

## 6. Required Structure of Planning Outputs

Every substantial planning artifact should include:

```text
Status
Scope
Inputs
Goals
Non-goals
Constraints
Assumptions
Evidence
Alternatives
Proposed design
Interfaces/dependencies
Observability/evaluation
Failure modes
Risks
Open questions
Reopen conditions
Required critiques
Downstream artifacts unblocked
```

## 7. Decision Protocol

Important decisions should not default to the first plausible proposal.

Possible resolution paths:

- evidence clearly favors one candidate;
- independent reviewers converge;
- prototype tournament selects a candidate;
- synthetic playtests distinguish candidates;
- tradeoff is encoded as an explicit reversible decision;
- uncertainty remains and decision is intentionally deferred.

## 8. Planning Backlog Discipline

The planning system must support both creation and retirement of work.

Agents should be able to mark planned work as:

- obsolete;
- duplicated;
- superseded;
- invalidated by evidence;
- unnecessary after architectural change.

A self-generating planning system without garbage collection is a failure mode.

## 9. Exit Criterion

This seed planning program should itself be replaced by a reviewed Planning Program v1 before large-scale planning begins.

Planning Program v1 must define exact missions, dependencies, review relationships, artifact schemas, and canonicalization rules.
