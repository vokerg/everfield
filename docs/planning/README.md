# Everfield Planning Corpus

## Purpose

This directory is the seed corpus for planning **how Everfield will be planned and built**.

It is deliberately upstream of implementation. The immediate objective is to construct a rigorous autonomous development system and a reviewed planning program capable of producing the eventual architecture, game-design corpus, dependency graph, and executable GitHub Issues.

## Current Maturity

**Phase:** Plan the Plan  
**Implementation authorization:** No  
**Mass issue generation:** No  
**Engine decision:** Open  
**Game design:** Directional only  
**Factory architecture:** Directional only

## Current Documents

- `00-project-charter.md` — project intent, constraints, success conditions, and non-goals for this phase.
- `01-autonomous-factory-mandate.md` — requirements for an AI-only development organization with no routine human gate.
- `02-game-design-mandate.md` — the high-level product and game-design direction that later design agents must preserve.
- `03-planning-program.md` — proposed multi-agent process for producing and criticizing the real plans.
- `04-evaluation-and-evidence.md` — initial requirements for machine-grounded judgment, CI evidence, protected evaluation, and playtesting.
- `05-research-agenda.md` — unresolved questions and research missions that must be explored before major commitments.
- `06-planning-deliverables.md` — expected canonical artifacts before implementation throughput begins.

## Planning Philosophy

The planning process should not ask a single agent to hallucinate a complete backlog for a game of this scale.

The intended process is iterative and adversarial:

```text
human seed intent
  -> independent domain research
  -> competing proposals
  -> cross-domain synthesis
  -> adversarial critique
  -> measurable prototype/spike work where required
  -> revised specifications
  -> dependency extraction
  -> testability review
  -> parallelism review
  -> issue-generation rules
  -> bounded issue generation
  -> dependency audit
  -> execution
  -> checkpoints
  -> re-planning
```

Planning is therefore a persistent subsystem of the factory, not a one-time project phase.

## Canonicality Rule

Documents in this directory may have one of four states:

- **SEED** — records intent, hypotheses, or research prompts. Not yet reviewed.
- **PROPOSED** — a concrete recommendation awaiting adversarial review.
- **CANONICAL** — accepted as the current operating/design rule after review and evidence.
- **SUPERSEDED** — retained for provenance but no longer active.

Current documents are primarily **SEED** artifacts.

## Immediate Goal

The next agents should turn this seed into a **Planning Program v1** that defines:

- planning-agent roles;
- research missions;
- required inputs and outputs;
- critique relationships;
- synthesis order;
- evidence requirements;
- decision protocols;
- dependency extraction rules;
- conditions for converting plans into GitHub Issues.

Only after that program itself has been reviewed should the repository begin producing the detailed technical and game-design plans.
