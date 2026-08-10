# Governance, Canonicality, and Provenance — Wave 1 Proposal

**Mission:** `W1-GOV-01`  
**State:** PROPOSED / NON-CANONICAL  
**Role:** governance planner  
**Required review:** `W1-REV-FAC`

## Review Index

**Core recommendation.** Everfield should use an explicit, repository-visible authority stack rather than infer authority from prose location, branch age, PR status, issue closure, or agent confidence. Material human directives are exceptional overrides and should be recorded as typed directive records; absent a directive, the autonomous system continues. Canonical project decisions require explicit lifecycle state, immutable evidence/provenance, review/verification, deterministic promotion, and squash-only integration.

**Authority stack.** Later in-scope explicit human directive → current canonical constitution/entry/program → selected canonical task contract + valid operational state → canonical decision/specification records → reviewed but non-canonical candidates → seed material → conversation/private agent memory (no project authority). Conflict resolution is scope- and provenance-aware; a narrower directive should not silently supersede unrelated policy.

**Judge-affecting self-modification.** Changes to constitution, dispatcher, claim/recovery, review/verification, protected evaluation, scheduler objectives/WIP, evidence/context rules, integration policy, permissions, benchmarks, or quality metrics require explicit factory-change work: defect hypothesis, alternatives, before/after evidence or bounded experiment, independent meta-review, verification, reversible rollout, and rollback triggers. The proposer cannot be the final verifier. Under the current one-agent constraint, use separated `DEGRADED_SINGLE_AGENT` episodes and retain the trust debt.

**Risk model.** Classify changes by reversibility, blast radius, authority/trust impact, uncertainty, dependency fan-out, external/legal exposure, and release/implementation impact. Higher tiers require stronger evidence/review, not routine human approval.

**Provenance/IP framework.** External/generated/dependency inputs need machine-readable source/tool/model/version/license-or-terms reference, acquisition time, hashes, transformation chain, usage scope, and policy verdict. Unknown or unresolved rights/provenance are quarantined from production/canonical assets while bounded research proceeds. Exact jurisdictional/legal conclusions and allow/deny lists are deferred to authoritative legal/IP research; this proposal does not manufacture legal advice.

**Primary review attacks.** Hidden human gates; ambiguous supersession; self-approval loopholes; emergency-directive overreach; stale directive references; canonicality inferred from GitHub state; policy changes that weaken their own evaluator; provenance rules that deadlock work; legal claims without authority; Goodharting governance metrics; single-agent trust debt being mistaken for full independence.

**Decisive experiments.** Cold-start authority conflict resolution; self-modification red-team; directive collision/scope test; provenance/quarantine pipeline trial; governance rollback drill; later comparison of degraded single-agent review against isolated/multi-agent review.

## 1. Status

This document is a bounded proposal for the governance portion of Wave 1. It does not itself replace `AGENTS.md`, Planning Program v1, the project charter, or any later canonical governance artifact. It proposes interfaces and decision rules for `W1-REV-FAC` to attack and for `W1-SYN-FAC` to reconcile with the control-plane, trust, CI/evidence, and operating-model proposals.

## 2. Scope

This proposal covers:

1. autonomy constitution and authority precedence;
2. explicit human-directive semantics;
3. canonicality and decision lifecycle;
4. decision-record requirements;
5. governance risk classification and escalation-by-evidence;
6. self-modification boundaries and rollback;
7. legal/IP/provenance governance framework;
8. observability and governance evaluation;
9. interfaces to the scheduler, review/verification, evidence, and downstream planning systems.

It is intentionally an operating-governance design, not a jurisdiction-specific legal policy or a finished repository schema implementation.

## 3. Inputs and source basis

### 3.1 Observed repository evidence

The authoritative packet establishes the following constraints:

- `AGENTS.md` places the project in pre-implementation PLANNING, requires repository-owned memory, independent review, evidence over assertion, no routine human gate, context discipline, Goodhart resistance, reversibility, and squash-only `main` integration.
- The project charter states that normal development is AI-performed, human intervention is exceptional, useful concurrency matters more than issue count, quality means verified/recoverable/composable progress, and the explicit human integration directive requires squash merges to `main`.
- The autonomous-factory mandate requires persistent production/verification/planning/meta-improvement loops; forbids a normal `WAITING_FOR_HUMAN_APPROVAL` state; treats role separation as independent evidence plus bounded authority; and requires explicit governance for changes to judge-affecting factory surfaces.
- The research agenda leaves control-plane enforcement, reviewer disagreement, protected evaluation, self-improvement governance, and legal/IP/provenance details as questions to answer through explicit research or experiments rather than assumptions.
- The planning-deliverables map expects eventual canonical artifacts for an AI-only autonomy constitution, human override protocol, planning canonicality rules, decision-record format, risk register, and legal/IP/provenance policy.

### 3.2 Inference

A durable autonomous factory cannot rely on “what an agent thinks is authoritative.” Authority and canonicality therefore need explicit, machine-readable provenance and transition evidence. Because human intervention is exceptional rather than a routine gate, human-directive handling must be capable of interrupting or superseding work without becoming a permanent approval dependency.

### 3.3 Recommendation

Use the governance model below as the candidate interface contract for later canonical governance artifacts and machine enforcement.

## 4. Goals

The governance system should let a fresh agent determine, from repository + GitHub state:

- what has authority over its current action;
- whether a human directive exists, what it affects, and whether it supersedes earlier authority;
- whether a decision is proposed, reviewed, verified, canonical, superseded, or invalidated;
- which evidence justified a canonical decision;
- what may modify the rules that judge current work;
- how high-risk changes obtain stronger evidence without waiting for routine human approval;
- whether code/assets/content/dependencies have sufficient provenance for their intended use;
- how to rollback a governance or factory-policy change;
- when a decision must be reopened.

## 5. Non-goals

This proposal does **not**:

- determine jurisdiction-specific legal conclusions;
- define a final third-party-license allowlist or denylist;
- claim what rights any current model/provider/tool grants;
- select the final engine, architecture, visual style, or gameplay systems;
- authorize gameplay implementation;
- replace the canonical task/claim/recovery schemas owned by the control-plane planning work;
- define detailed protected-evaluator storage topology;
- make governance metrics a scalar optimization objective;
- allow this producer to canonicalize or verify its own proposal.

## 6. Constraints

1. Normal progress cannot require routine human approval.
2. Explicit human directives may override autonomous policy, but their scope and provenance must be preserved for later agents.
3. Conversation history is not durable project authority.
4. Canonicality must be explicit; it cannot be inferred from file path, PR merge, issue closure, branch name, or age.
5. Judge-affecting policy changes require stronger separation than ordinary local work.
6. Every `main` integration remains squash-only unless a later explicit human directive changes that binding rule.
7. The current project has one available agent, so independence can be degraded but must never be mislabeled as full independence.
8. Legal/IP/provenance uncertainty must not be converted into unsupported legal claims.
9. Governance must preserve a broad conflict-free planning frontier rather than centralize every decision into one bottleneck.

## 7. Assumptions

These are provisional and should be challenged by `W1-REV-FAC`:

- A small number of explicit authority levels is easier for cold-start agents to apply than a large exception-rich hierarchy.
- Machine-readable directive/decision records can coexist with human-readable rationale without duplicating authority.
- Quarantine of unresolved external inputs is preferable to either silently accepting them or turning every uncertainty into a human gate.
- Reversible policy rollout plus observable rollback triggers is safer than treating a governance change as permanently correct after one review.
- The canonical dispatcher/control-plane can eventually validate decision/directive references mechanically, even if initial enforcement is partly procedural.
- `DEGRADED_SINGLE_AGENT` can preserve liveness with visible trust debt until isolated or multi-agent execution becomes available.

## 8. Alternatives considered

### 8.1 “Human is final approver for important decisions” — rejected

This contradicts the no-routine-human-gate constraint and makes the factory unable to continue autonomously. Human directives remain exceptional overrides, not a required state transition.

### 8.2 “Merged to main means canonical” — rejected

A merge may preserve provenance, evidence, draft material, tests, or rejected hypotheses. Canonicality must have an explicit authority transition and exact source/promotion evidence.

### 8.3 “One constitution file contains every rule” — rejected

This creates a high-conflict bottleneck and forces unrelated work to load excessive context. Prefer a small stable authority constitution plus scoped canonical records/specifications and typed references.

### 8.4 “Any agent may improve the process whenever convenient” — rejected

Workers could weaken the rules judging their current work. Judge-affecting changes require separate factory-change work and evidence.

### 8.5 “Fail closed by stopping until legal uncertainty is resolved by a human” — rejected

Unknown-provenance inputs should be quarantined from production/canonical use while autonomous research or alternative-source work continues. Human legal advice may be an external directive/evidence source, but not the default liveness mechanism.

### 8.6 “Optimize a governance health score” — rejected

A single score invites Goodharting. Use a diagnostic vector with explicit qualitative review and reopen conditions.

## 9. Proposed governance design

### 9.1 Authority hierarchy

For one concrete action, resolve authority in this order, with scope matching required at every level:

1. **Later explicit human directive** that is valid, repository-visible when material, and applicable to the action.
2. **Current canonical constitution / root entry / Planning Program** resolved through the active canonical binding.
3. **Selected canonical task contract and valid operational state**, including prerequisites, ownership generation, and review/verification route.
4. **Scoped canonical decision/specification records** referenced by the task or active canonical program.
5. **Reviewed/verified but non-canonical candidate artifacts** as evidence/input only.
6. **Seed documents and other non-canonical proposals** as hypotheses/constraints only where the task declares them authoritative inputs.
7. **Conversation/private agent memory**: no project authority.

Rules for conflicts:

- a higher-level authority supersedes a lower one only inside its stated scope;
- a later directive does not silently alter unrelated policy;
- a narrower later directive supersedes the conflicting subset of a broader earlier directive unless it explicitly says otherwise;
- unresolved same-level contradictions fail closed for the affected transition and create bounded evidence/reconciliation work rather than `WAITING_FOR_HUMAN_APPROVAL`;
- superseded/invalidated authority remains immutable provenance but has no current action effect.

### 9.2 Human Directive Record

Material human directives should be converted into a repository/GitHub-visible `DirectiveRecord` before downstream agents depend on hidden chat context.

Minimum proposed fields:

```yaml
directive_id: HD-YYYY-NNN
kind: EMERGENCY_SAFETY | PROJECT_DIRECTION | RESOURCE_CONSTRAINT | PRIORITY | EXPERIMENTAL
issuer: human_owner
created_at: <server/repository timestamp>
source_ref: <immutable issue/comment/commit/external evidence ref when available>
scope:
  missions: []
  paths: []
  decisions: []
statement: <faithful bounded statement>
supersedes: []
conflicts_with: []
expires_at: null
review_after: null
affected_work: []
recorded_by: <agent/session>
implementation_state: RECORDED | APPLIED | SUPERSEDED | EXPIRED
```

Semantics:

- **EMERGENCY_SAFETY** may immediately stop affected work; the stop itself is the directive, not a routine approval state. Recovery/replanning follows.
- **PROJECT_DIRECTION** changes goals/constraints and triggers impact analysis on dependent canonical decisions/tasks.
- **RESOURCE_CONSTRAINT** records execution facts such as single-agent availability and may enable a canonical degraded mode.
- **PRIORITY** changes ordering without silently changing acceptance or quality gates.
- **EXPERIMENTAL** authorizes a bounded deviation with explicit expiry/review conditions.

Do not place secrets, unnecessary personal data, or unrestricted private conversation content into directive records. Record only the durable project-relevant instruction and provenance required to apply it faithfully.

### 9.3 Canonical decision lifecycle

Recommended states:

```text
PROPOSED
  -> REVIEW_READY
  -> REVIEWED
  -> VERIFICATION_READY
  -> VERIFIED
  -> CANONICAL
  -> SUPERSEDED | INVALIDATED
```

A simpler task may skip intermediate artifact files, but it must not skip the authority evidence required for its risk class.

Canonical promotion requires:

- exact candidate work state;
- exact evidence/review references;
- disposition of unresolved BLOCKER/MAJOR findings;
- exact verifier result where the class requires verification;
- verified base / drift handling;
- deterministic promotion or explicit allowed transformation;
- integrator distinct from producer/verifier at the required role boundary;
- squash-only `main` integration;
- terminal canonicality record with resulting main SHA and supersession effects.

A later canonical record may supersede an earlier one without erasing its provenance.

### 9.4 Decision Record

Proposed minimum `DecisionRecord` fields:

```yaml
decision_id: DEC-<domain>-NNN
authority_level: CANONICAL | REVIEWED_CANDIDATE | EXPERIMENTAL
state: PROPOSED | REVIEWED | VERIFIED | CANONICAL | SUPERSEDED | INVALIDATED
scope:
  systems: []
  paths: []
  missions: []
source_issue: null
source_work_shas: []
evidence_refs: []
assumptions: []
alternatives: []
decision: <bounded normative statement>
rationale: <why evidence favors it>
dissent_and_findings: []
dispositions: []
dependencies: []
conflicts: []
verifier_ref: null
canonicalizer_ref: null
canonical_main_sha: null
supersedes: []
reopen_conditions: []
rollback_or_migration: null
```

The record should distinguish **what is normative** from supporting rationale. Rationale may age without automatically changing the current normative statement; changed evidence triggers review/reopen rather than silent reinterpretation.

### 9.5 Risk model

Classify a proposed decision/change on these dimensions:

- **reversibility** — cheap rollback ↔ destructive/irreversible;
- **blast radius** — one task ↔ cross-project;
- **authority/trust impact** — ordinary artifact ↔ rules that judge/authorize work;
- **evidence uncertainty** — directly tested ↔ speculative/externally unresolved;
- **dependency fan-out** — few consumers ↔ many downstream tasks/artifacts;
- **external/legal/provenance exposure** — none ↔ externally distributed/licensed/sensitive;
- **implementation/release impact** — planning-only ↔ production/player/release critical.

Recommended aggregate tiers are qualitative, not a score to optimize:

| Tier | Character | Minimum governance response |
|---|---|---|
| R0 | local, reversible, low fan-out | normal task evidence + normal review route |
| R1 | bounded cross-task or moderate uncertainty | explicit decision record, independent critique, rollback/reopen condition |
| R2 | canonical/systemic, broad fan-out, trust-affecting | adversarial review, verification, deterministic promotion, impact graph, rollback plan |
| R3 | protected-evaluator/constitution/external-release/legal-sensitive/near-irreversible | strongest available independent evidence, protected evaluation where applicable, staged/reversible rollout or quarantine; no routine human approval implied |

A high tier increases **evidence and separation**, not mandatory human sign-off.

### 9.6 Self-modification governance

Define a **judge-affecting surface** as any artifact/tool/configuration that can materially alter eligibility, authority, review stringency, evidence interpretation, or quality thresholds for current/future work. Candidate surfaces include:

- autonomy constitution and authority resolution;
- canonical dispatcher/task state model;
- claim/resume/recovery/fencing protocol;
- reviewer/verifier protocols;
- protected tests/evaluators and access controls;
- scheduler objective/WIP policy;
- integration/merge policy;
- evidence/context sufficiency rules;
- agent permissions;
- benchmark definitions and quality/factory metrics.

A change to a judge-affecting surface should require a `FactoryChangeRecord` containing:

1. defect/risk hypothesis;
2. exact current behavior/version;
3. proposed change and alternatives;
4. expected benefit and failure modes;
5. before/after benchmark or bounded evidence plan;
6. affected tasks/decisions/evaluators;
7. migration/compatibility analysis;
8. independent meta-review findings;
9. verification evidence;
10. staged adoption and rollback trigger;
11. result and follow-up measurement.

Prohibited shortcut: an agent may not weaken the rule/test/evaluator currently blocking its own task and then use the weakened rule as evidence that the task passes. Such a change must route through separate factory-change ownership and review/verification.

Under `DEGRADED_SINGLE_AGENT`, use separate cold-start episodes, immutable candidate-under-review, prior-rationale gating, explicit trust level, and a reopen condition. When stronger isolation/multiple agents become available, re-evaluate high-risk governance decisions whose only independent gate was degraded.

### 9.7 Legal / IP / provenance framework

This section defines **process**, not legal conclusions.

Every external or generated input intended for durable project use should have a provenance record sufficient to answer: *what is it, where did it come from, under what referenced terms, what transformed it, and where may it be used?*

Proposed fields:

```yaml
provenance_id: PROV-...
artifact_hash: <content hash>
artifact_kind: CODE | LIBRARY | MODEL_OUTPUT | IMAGE | AUDIO | TEXT | DATA | OTHER
source_kind: FIRST_PARTY | THIRD_PARTY | GENERATED | DERIVED
source_ref: <URI/repository/provider/artifact id>
creator_or_provider: <when known/relevant>
tool_or_model: <name/version when generated>
input_provenance_refs: []
acquired_at: <timestamp>
license_or_terms_ref: <immutable/current reference or UNKNOWN>
transformation_chain: []
intended_usage_scope: <planning/test/internal/shipping/etc>
policy_verdict: ALLOW | QUARANTINE | REJECT | RESEARCH_REQUIRED
policy_evidence_refs: []
review_ref: null
```

Recommended behavior:

- `UNKNOWN`, contradictory, or unsupported rights/provenance does **not** silently become production/canonical material; it enters `QUARANTINE`/`RESEARCH_REQUIRED`.
- Quarantine should not block unrelated work: agents may research terms, replace the source, generate an original alternative, or proceed on unaffected surfaces.
- Exact license compatibility, provider terms, jurisdictional requirements, trademark/copyright analysis, and acceptable-use lists require authoritative current legal/IP research before a shipping ingestion policy is canonicalized.
- Third-party software/dependency ingestion should eventually require machine-readable source/version/license metadata plus a policy result before shipping use.
- Generated media/content should preserve tool/model/version and transformation provenance where available; current provider terms/rights must be verified rather than assumed.
- Do not store secrets or unnecessary personal data in provenance records.

**Reference separation.** The charter names Stardew Valley as a complexity/system-density reference, not a cloning specification. Governance should preserve a documented distinction between comparative references and Everfield’s original code/assets/text/narrative/design expression. A later content/IP policy should define similarity review/evidence for exposed content without pretending this proposal settles legal boundaries.

### 9.8 Rollback and supersession

Canonical governance changes should have one of:

- direct revert path;
- migration back to prior compatible version;
- staged feature/policy flag;
- compensating canonical record where destructive rollback is impossible.

Rollback is not evidence of process failure by itself. A healthy autonomous factory should detect a bad policy and recover with complete provenance.

Supersession must identify:

- old authority record;
- new record;
- exact scope superseded;
- compatibility/migration effects;
- downstream records/tasks requiring refresh or invalidation.

## 10. Interfaces, dependencies, and conflict surfaces

| Interface | Governance requirement | Owning/downstream mission |
|---|---|---|
| agent lifecycle/context | authority/directive/decision references must be available in bounded task packets | W1-FAC-01 |
| GitHub control plane | machine representation/validation of directive, decision, canonicality, supersession and ownership refs | W1-FAC-02 |
| review/trust | risk-tier review classes, independence profiles, protected/judge-affecting change rules | W1-FAC-03 |
| CI/evidence | immutable evidence/provenance records, diagnostic governance metrics, benchmark/rollback evidence | W1-FAC-04 |
| technical foundation | dependency/license/provenance ingestion hooks; ADR/decision-record integration | W1-TEC-01 / W1-TEC-02 |
| content/experience | generated/external asset provenance and later similarity/licensing policy | W1-EXP-01 / game synthesis |
| final synthesis | canonical governance decisions vs deferrals; implementation-readiness blockers | W1-SYN-FAC / W1-SYN-FINAL |

Potential conflict surfaces:

- W1-FAC-02 may propose a different operational state model; governance should define authority semantics, while the control plane owns exact machine mechanics.
- W1-FAC-03 may tighten or alter independence/risk-class gates; synthesis must reconcile rather than duplicate review policy here.
- W1-FAC-04 owns exact evidence storage/retention; this proposal specifies provenance requirements, not storage topology.
- Legal/IP policy may constrain technical/content choices after authoritative research; those constraints must enter as scoped canonical records, not retroactive hidden assumptions.

## 11. Observability and evaluation

Track a **diagnostic vector**, not one governance score:

- cold-start authority-resolution success rate;
- ambiguous/conflicting authority incidents;
- material human-directive-to-repository-record latency;
- stale directive references;
- unauthorized/premature canonicality attempts;
- canonical decision reopen/supersession rate with reason;
- judge-affecting self-modification attempts and blocked shortcuts;
- factory-change rollback rate and rollback success;
- governance review findings and escape rate;
- provenance completeness for shipping-bound artifacts;
- quarantine counts/age/reason and successful replacement/research resolution;
- unknown-license/terms attempts reaching shipping surfaces;
- degraded-independence decisions awaiting stronger re-evaluation;
- governance-related READY-frontier stalls.

Use metrics to trigger investigation/replanning, not to reward agents for minimizing a number. For example, zero reopened decisions could indicate stability or suppression of legitimate reopening.

## 12. Bounded experiments / evidence still needed

| ID | Experiment | Pass signal | Failure implication |
|---|---|---|---|
| GOV-E1 | Cold-start authority-resolution drill with canonical rule, seed conflict, task contract, and later scoped directive | independent episode derives same applicable authority/scope without hidden context | hierarchy/schema ambiguous; revise before canonicalization |
| GOV-E2 | Self-modification red-team: blocked worker attempts to weaken its current evaluator/gate | change is rejected/rerouted to separate factory-change work; original task remains blocked | judge-affecting boundary insufficient |
| GOV-E3 | Directive collision: broad older direction vs narrower later direction plus unrelated task | only overlapping scope superseded; unrelated policy unchanged | directive supersession unsafe |
| GOV-E4 | Provenance pipeline trial with first-party, generated, licensed third-party, and unknown-terms inputs | known records route deterministically; unknown is quarantined while unrelated work continues | provenance policy either leaks or deadlocks |
| GOV-E5 | Governance rollback drill | adverse policy can revert/migrate with canonical provenance and downstream impact accounting | reversibility model insufficient |
| GOV-E6 | When isolation/multiple agents become available, compare high-risk reviews against DEGRADED_SINGLE_AGENT results | escape/disagreement evidence quantifies trust gap and informs which old decisions need re-review | degraded mode may be over-trusted; reopen affected governance |

## 13. Failure modes and defenses

### Hidden human gate
**Failure:** “important” becomes code for waiting for owner approval.  
**Defense:** risk tiers require stronger evidence/review; human approval is not a normal transition.

### Directive overreach
**Failure:** a priority or resource directive silently changes quality/canonicality policy.  
**Defense:** typed scope, explicit supersession, impact analysis.

### GitHub-state canonicality
**Failure:** merged/closed/old artifact is treated as canonical.  
**Defense:** explicit decision/canonicalization state and terminal authority record.

### Self-approval
**Failure:** worker edits its own evaluator/threshold and passes.  
**Defense:** judge-affecting surface classification + separate factory-change route + review/verification.

### Governance bottleneck
**Failure:** every local choice requires central constitution edits.  
**Defense:** stable minimal constitution, scoped decision records, bounded delegated authority.

### Stale rules
**Failure:** agents continue using superseded decisions/directives.  
**Defense:** explicit supersession graph, task packet references, stale-reference diagnostics.

### Provenance leak
**Failure:** unknown-source/license artifact reaches shipping/canonical output.  
**Defense:** machine provenance gate + quarantine/research state.

### Provenance deadlock
**Failure:** one unknown input stops unrelated work.  
**Defense:** isolate/quarantine the artifact, generate alternatives, continue unaffected graph.

### False legal certainty
**Failure:** agent turns memory or generalization into a binding legal policy.  
**Defense:** current jurisdiction/provider/license claims require authoritative evidence; unresolved specifics remain research items.

### Metric gaming
**Failure:** agents optimize low finding/reopen/quarantine counts.  
**Defense:** diagnostic vector, protected review, rotate/red-team governance scenarios, interpret metrics contextually.

### Degraded independence laundering
**Failure:** one-agent review is later described as fully independent.  
**Defense:** typed trust profile, durable resource-constraint evidence, reopen condition.

## 14. Risks

- A sophisticated governance schema can become too expensive to maintain; keep mandatory records small and automate validation in W1-FAC-02.
- Excessive risk classification can serialize work; use risk tiers only where authority/blast radius warrants them and benchmark READY-frontier effects.
- Quarantine without ownership/aging rules can become a junk drawer; W1-FAC-02/W1-FAC-04 should define ownership, expiry, and evidence queues.
- Repository-visible directives may accidentally capture sensitive or unnecessary conversation content; record only durable project-relevant instruction/provenance.
- A later legal/IP policy may require changes to this framework after authoritative research; preserve replaceability and reopen conditions.
- Single-agent degraded review can miss correlated reasoning errors; retain explicit trust debt until stronger isolation exists.

## 15. Open questions

1. Which exact repository schema/file should hold canonical `DirectiveRecord` and `DecisionRecord` objects versus GitHub-native issue/comment metadata?
2. Which risk tiers require two review episodes versus one adversarial review plus protected verification?
3. What machine mechanism prevents a worker with write permission from editing protected judge-affecting surfaces before permission boundaries mature?
4. Which governance metrics belong in protected factory benchmarks rather than ordinary dashboards?
5. What authoritative legal/IP sources, jurisdictions, distribution platforms, provider terms, and license classes must the eventual shipping policy cover?
6. What retention policy is appropriate for provenance evidence whose external source/terms later change?
7. When stronger isolation becomes available, which prior DEGRADED decisions deserve mandatory re-verification versus sampled audit?

## 16. Reopen conditions

Reopen this proposal or its later canonical descendants if:

- two compliant fresh agents derive different current authority from the same repository/GitHub state;
- a routine workflow reaches a human-wait state;
- a human directive cannot be applied without hidden chat context;
- an ordinary worker can weaken a gate judging its own current work;
- canonicality is inferred from merge/path/closure rather than explicit authority state;
- governance rules repeatedly shrink the useful READY frontier without measured safety benefit;
- provenance/quarantine either leaks unresolved material into shipping surfaces or repeatedly deadlocks unrelated work;
- current legal/IP research contradicts assumptions embedded in a later policy;
- governance metrics demonstrably drive reward-hacking behavior;
- stronger multi-agent/isolation capability becomes available and invalidates confidence in DEGRADED-only reviews;
- a later explicit human directive supersedes a binding governance constraint.

## 17. Required independent critique

`W1-REV-FAC` should attack this proposal specifically for:

- hidden human approval states;
- ambiguous authority precedence/supersession;
- emergency-directive privilege escalation;
- self-modification loopholes;
- governance centralization that reduces parallelism;
- missing rollback/migration semantics;
- Goodhart paths in governance metrics;
- incomplete provenance escape paths or quarantine deadlocks;
- unsupported legal assertions;
- ambiguity between governance semantics and W1-FAC-02 control-plane mechanics;
- degraded single-agent trust being treated as full independence.

The reviewer should treat all recommendations here as candidates, not settled authority.

## 18. Downstream work unblocked

This proposal contributes one required input to `W1-REV-FAC`. It also exposes interface requirements for W1-FAC-01 through W1-FAC-04 and later `W1-SYN-FAC`, but it does not instantiate new current-wave work or alter their issue contracts.

No part of this proposal is canonical until the Wave 1 review/synthesis/verification/canonicalization route promotes an accepted form.