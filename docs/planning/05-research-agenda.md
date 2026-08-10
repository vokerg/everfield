# Research Agenda — Seed

**State:** SEED

## Purpose

This document records questions that should be answered through explicit research, experiments, competing proposals, or later design work rather than silently converted into assumptions.

It is intentionally broad. Planning Program v1 should convert these into bounded research missions with owners, inputs, outputs, dependencies, and review requirements.

---

## 1. Engine and Runtime Environment

Research questions:

- Which engine best supports autonomous AI development for a project of this size?
- How reliable are command-line builds and tests?
- How well can scenes/resources/assets be modified without interactive-editor-only workflows?
- How merge-friendly are project files under 10–20 concurrent agents?
- Can the engine run deterministic or semi-deterministic headless scenarios?
- Can screenshots/video be captured reliably in CI?
- Can agents inspect useful runtime state without bespoke fragile tooling?
- How mature are testing, profiling, packaging, localization, accessibility, and platform workflows?
- What are the practical build times and CI costs at project scale?
- How easy is it for an agent to recover from malformed project assets?
- What editor automation/MCP/API surfaces exist and how stable are they?

Candidate evaluation should include representative autonomous-development spikes rather than feature-table comparison alone.

## 2. GitHub as the Control Plane

Research questions:

- Which task-state relationships can be represented natively with Issues, sub-issues, dependencies, labels, Projects, PRs, merge queues, and Actions?
- Which relationships require repository-owned machine-readable metadata?
- How should atomic issue claiming work?
- How should stale claims be detected/recovered?
- How should task branches be linked to issues?
- How should handoffs be stored so that they are queryable and versioned?
- Can issue/PR state transitions be enforced through automation rather than conventions?
- How should the scheduler obtain a conflict-free READY frontier?
- What permissions should implementation/review/verifier agents have?

## 3. Agent Entry Point and Context Loading

Research questions:

- What is the minimal root `AGENTS.md` that remains stable enough to load every session?
- Should module-level AGENTS files exist, and how should inheritance work?
- What information belongs in generated work packets versus repository docs?
- How should agents retrieve only relevant specifications?
- How can context pollution and stale instructions be measured?
- How should an agent detect when local context is insufficient and safely broaden retrieval?
- What is the ideal bootstrap command/tool interface?

## 4. Task Granularity and Resumability

Research questions:

- What structural limits make an implementation task safely reviewable and resumable?
- How large can a task become before handoff failure rises sharply?
- Should implementation sessions target one issue only?
- When should one issue contain explicit subtasks versus separate dependent issues?
- How should multi-session work represent WIP commits?
- What makes a handoff objectively good?
- Can handoff quality be benchmarked by forced agent substitution experiments?

## 5. Review and Verification

Research questions:

- What should Review 1 and Review 2 evaluate differently?
- Should Review 2 initially be blind to Review 1 findings?
- Which work classes need two reviews versus stronger/weaker protocols?
- How should reviewer disagreement be resolved autonomously?
- Which tests/scenarios must be protected from implementation agents?
- Should protected verification live in the same repository, another repository, or a service?
- How can evaluator corruption or metric gaming be detected?
- How should verifier failures reopen work?

## 6. Dependency and Conflict Modeling

Research questions:

- What dependency types are required beyond `blocked by`?
- How should interface dependencies differ from hard implementation dependencies?
- How are conflict/ownership surfaces represented?
- Can filesystem paths approximate ownership, or are semantic resource locks required?
- How should task generation avoid giant bottleneck nodes?
- How should the scheduler estimate downstream unblock value?
- How should planning detect when READY frontier width is insufficient for available agents?

## 7. CI and Evidence Topology

Research questions:

- What is the canonical run-report schema?
- What artifacts should be ephemeral versus retained long term?
- Should evidence live in the source repository, a dedicated evidence repository, object storage, or GitHub Actions artifacts?
- How are evidence artifacts content-addressed and referenced from issues/PRs?
- How is provenance protected?
- Which scenarios run on every PR versus nightly/checkpoint/release schedules?
- How are flaky scenarios detected and quarantined without hiding regressions?

## 8. Deterministic Simulation and Replay

Research questions:

- Which parts of the game must be deterministic?
- How should RNG streams be partitioned and seeded?
- What canonical game-state representation is stable enough for hashes/comparison?
- Can physics/animation/rendering nondeterminism be separated from gameplay determinism?
- How should replays remain valid across version/schema changes?
- How can long simulations execute much faster than real-time?

## 9. Machine Playtesting

Research questions:

- What control surface can synthetic players use without bypassing gameplay rules?
- Which tasks need raw input control versus semantic action APIs?
- When are LLM/VLM playtesters useful compared with scripted/search-based agents?
- How should a population of player personas be calibrated?
- Can difficulty estimates be correlated against later human telemetry without creating a human gate?
- How should exploit-hunting agents search the state/action space?
- How can playtest traces be made compact enough for future agents to inspect?

## 10. Visual Asset Production and Review

Research questions:

- What visual styles are most compatible with high-volume AI asset production and long-term consistency?
- Which asset types can be generated reliably and which require stronger tooling?
- How should sprite/animation consistency be represented?
- What canonical visual bible should agents retrieve?
- How are visual references versioned?
- What objective image checks are useful?
- How reliable are multimodal judges for hierarchy, readability, clipping, style, animation, and polish?
- How should important art-direction choices be selected through candidate tournaments?

## 11. Audio Production and Evaluation

Research questions:

- How should music themes, ambience, and SFX identity be specified for AI production?
- How can repetition/fatigue be measured?
- What automated checks can catch clipping, loudness problems, missing cues, or inconsistent mixes?
- How can subjective audio judgments be independently reviewed?
- What licensing/provenance constraints apply to generated assets and tools used?

## 12. Content Architecture

Research questions:

- Which game content should be purely data-driven?
- What requires authored scripts?
- What quest/dialogue/event DSLs are needed?
- How should IDs and references remain stable?
- How are schemas migrated?
- How can content be compiled/validated independently from runtime code?
- How can thousands of content changes be parallelized with low merge conflict?

## 13. Quest and Narrative Architecture

Research questions:

- What quest grammar supports enough variety without custom code per quest?
- How should branching, optional objectives, hidden objectives, timers, world-state mutations, and relationship conditions work?
- How can structural quest solvability be proven or searched?
- How should narrative facts, chronology, character knowledge, relationships, secrets, and faction states be represented canonically?
- How do agents detect contradictions across huge authored corpora?
- How should narrative quality be judged without collapsing it to one score?

## 14. Economy and Progression Simulation

Research questions:

- Which economic variables should be simulated at large scale?
- How should different player personas value time versus currency?
- How can dominant strategies be detected automatically?
- How can unreachable progression states and circular unlock dependencies be detected?
- How should inflation and late-game wealth be modeled?
- How should automation payback periods change over progression?
- What other durable late-game sinks should exist besides automation?

## 15. Automation System Design

Research questions:

- Which classes of repetitive action should be automatable?
- Which should intentionally remain direct player activities?
- Should automation be technological, magical, social/delegated, infrastructural, or a mixture?
- How should automation consume power/resources/maintenance/logistics if at all?
- How does automation interact with NPC labor, property, transport, crafting, farming, animals, fishing, mining, commerce, and exploration?
- How do we prevent automation from converting the game into passive waiting?
- What new higher-order decisions become available after each automation tier?

## 16. Sandbox Diversity

Research questions:

- What constitutes a genuinely viable player lifestyle?
- How do we measure whether multiple lifestyles remain economically/progression viable?
- How much cross-system participation can be required without destroying sandbox freedom?
- Which content is universally foundational versus specialization-specific?
- How do we avoid one optimal route dominating all others?
- How should hybrid lifestyles emerge?

## 17. Perceived Inexhaustibility

Research questions:

- Which forms of content create depth rather than catalog bloat?
- How frequently should new system layers appear?
- How can hidden depth remain discoverable without overwhelming onboarding?
- How much content should be mutually exclusive or playthrough-specific?
- When should procedural/generative systems supplement authored content?
- How do we avoid AI-generated repetition and semantic sameness at extreme content scale?

## 18. UX and Accessibility

Research questions:

- How can a very large possibility space remain understandable?
- How should optional systems reveal themselves?
- How should players discover automation without feeling forced into it?
- How can high-volume content avoid menu/inventory overload?
- Which accessibility requirements must influence architecture early?
- Can synthetic task-completion agents meaningfully test discoverability and usability?

## 19. Factory Benchmarks

Research questions:

- What internal tasks represent realistic factory capabilities?
- How do we benchmark implementation, review, handoff, integration, planning, and verifier behavior?
- How do we seed known subtle bugs and reward-hacking opportunities safely?
- Which metrics indicate a protocol improvement versus benchmark overfitting?
- How frequently should factory benchmarks rotate or expand?

## 20. Self-Improvement Governance

Research questions:

- Who/what may modify the factory constitution?
- Which metrics trigger a factory-improvement issue?
- How are proposed changes compared to the previous protocol?
- What rollback mechanism exists?
- How do we prevent local workers from weakening quality gates to make their current task easier?

## 21. Legal / IP / Provenance

Research questions:

- How should the project preserve the distinction between Stardew Valley as a design-complexity reference and original Everfield content?
- What provenance records are needed for generated visual/audio assets?
- Which third-party tools, models, libraries, asset sources, and licenses are acceptable?
- What automated checks can reduce accidental inclusion of incompatible assets or code?

## 22. Release and Long-Term Maintenance

Research questions:

- Which target platforms are realistic for the autonomous pipeline?
- How are release candidates evaluated?
- What telemetry/crash information should feed back into autonomous issue generation after release?
- How are save migrations and compatibility maintained over long-lived continuous expansion?
- How does the factory decide whether to prioritize new content, debt reduction, balance, or performance after launch?

---

## Research Output Rule

A research mission should not end with a link collection.

It should produce:

- question;
- evidence;
- constraints;
- alternatives;
- recommendation or explicit deferral;
- confidence/uncertainty;
- experiments still needed;
- downstream decisions affected;
- required independent critique.
