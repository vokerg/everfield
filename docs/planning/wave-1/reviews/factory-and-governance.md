# Factory and Governance — Wave 1 Adversarial Review

**Mission:** `W1-REV-FAC`  
**State:** REVIEW COMPLETE  
**Disposition:** **CHANGES_REQUIRED**  
**Trust profile:** `DEGRADED_SINGLE_AGENT`  
**BLOCKER:** 1  
**MAJOR:** 7  
**MINOR:** 3  
**NOTE:** 2

## 1. Reviewed provenance

This review binds exact producer results; it does not review mutable “latest branch” state.

| Mission | Issue | REVIEW_READY comment | work SHA | head SHA | Artifact |
|---|---:|---:|---|---|---|
| W1-GOV-01 | #22 | `5245434514` | `ffa6b62b3b20c84a152e676b7a5db223daa130e5` | `3c0fe2f1bd1d19bd43e4f65b9c05a8a43c5ac0e3` | `docs/planning/wave-1/proposals/governance-and-canonicality.md` |
| W1-FAC-01 | #23 | `5245474479` | `e7fe3d0eaae22038e661ea941e652a618c3a7ec7` | `a72a4b10e316482bf43a2931c6d306ed0baea547` | `docs/planning/wave-1/proposals/agent-operating-model.md` |
| W1-FAC-02 | #24 | `5245532215` | `095372a41498e8d7e3b25364cba89dbc647b8839` | `67aaf055e0ca5479e5af0b86f8876e5cb848ad90` | `docs/planning/wave-1/proposals/github-control-plane-and-scheduler.md` |
| W1-FAC-03 | #25 | `5245577951` | `70b763a965cdec0fa1f6c025a5b7492b844288fc` | `9f3646b7e4d280ce4ef102d30284f9e631a1a389` | `docs/planning/wave-1/proposals/review-verification-and-trust.md` |
| W1-FAC-04 | #26 | `5245629575` | `99b0c7b3bddbad1a71e05f085fd0bd9f2c74e566` | `8f90b251c5d7736caed53781ae69b0b19787e8b3` | `docs/planning/wave-1/proposals/ci-evidence-and-factory-measurement.md` |

Review input manifest: `docs/planning/wave-1/reviews/factory-governance-review-input.yaml`.

## 2. Independence and evidence boundary

This is a separate reviewer-role episode, `w1-rev-fac-reviewer-20260810-01`, operating under repository-visible one-agent resource constraint comment `5244416013`. Trust is therefore **DEGRADED**, not full independence.

The review branch is the only mutation surface for this episode. Producer candidates were frozen; none was edited. The attack plan and exact input SHAs were committed before detailed producer-body reconciliation. Seed/mandate material was not widened into the packet because the material findings below can be demonstrated directly from the five reviewed outputs and their interfaces.

## 3. Attack plan

The review attempted to invalidate the combined factory/governance model across:

1. authority, directives, supersession, and canonicality;
2. claim/resume/recovery, leases, crashes, conflict locks, and stale writers;
3. context manifests, continuation, handoff, stopping, and scope growth;
4. self-modification, trust boundaries, protected evaluators, and role laundering;
5. evidence requirements, flaky/inconclusive outcomes, substitution, and retention;
6. scheduler/WIP incentives, starvation, quality-queue debt, and Goodhart paths;
7. dependency/READY/liveness derivation and native-mirror drift;
8. merge/base/head/bypass safety;
9. provenance and garbage-collection reachability.

The relevant question was not whether each proposal is sensible in isolation. It was whether a synthesizer could compose them into one deterministic autonomous operating model without inventing missing policy.

## 4. Summary disposition

The five proposals have strong local defenses: no routine human gate, explicit degraded trust, candidate immutability, current-base verification, squash-only integration, evidence indexes rather than green-status compression, non-authoritative Projects/labels, and explicit experimental treatment of the proposed ref-lock substrate.

However, the combined model is **not yet safe to synthesize unchanged**. One authority contradiction can make two compliant schedulers choose different work, and seven additional cross-proposal gaps leave material ownership/trust/evidence/retention behavior to interpretation.

Disposition: **CHANGES_REQUIRED**. `W1-SYN-FAC` may proceed only by explicitly dispositioning every BLOCKER/MAJOR below and preserving the empirical gates named here. The reviewed producer branches should remain immutable provenance; corrections belong in synthesis/revision output.

## 5. Findings table

| ID | Severity | Affected sections | Failure scenario | Required correction / bounded question |
|---|---|---|---|---|
| FG-B01 | BLOCKER | GOV §§9.1–9.2; FAC2 §§9.1, 9.8 | A material scoped human directive changes priority/resource/safety state. Governance says it outranks canonical task state, but FAC2 READY/claim proof has no directive-set input. Two compliant schedulers can disagree on eligibility or claim work contrary to the highest authority. | Define a machine-valid `DirectiveRecord` lifecycle and active directive-set version/hash as an input to state snapshots, READY proofs, claim/recovery, and integration. Emergency stop may act immediately, but downstream resume/reliance requires the durable record. |
| FG-M02 | MAJOR | FAC1 §9.11; FAC2 §§9.4–9.6, 9.8 | An active task discovers acceptance-required work in a previously undeclared conflict surface. FAC1 permits bounded absorption only if “conflict-safe,” while FAC2 acquires conflict keys at claim. No transition atomically expands locks before the new mutation. Two tasks can legally expand into the same surface. | Add `LOCK_EXPAND`/scope-expansion semantics: before first mutation outside current conflict keys, atomically acquire the additional key(s) against current ownership/head or block/reroute as discovered work. Record context/review-scope change. |
| FG-M03 | MAJOR | GOV §9.6; FAC3 §§10, 14, 18–20; FAC4 §§19–20 | Policy version N+1 weakens the evaluator/review/risk rule that is supposed to judge N+1. All proposals say judge-affecting changes need meta-review, but none states which policy version has authority during adoption. The candidate can become self-judging through version ambiguity. | Establish an old-policy-judges-new-policy invariant: active version N governs evaluation/activation of N+1; N+1 has no authority over its own gate. Promotion occurs only after PASS under N (or a strictly higher explicit canonical directive) and records rollback/previous-version pointer. |
| FG-M04 | MAJOR | GOV §§9.6, 11–12; FAC1 §9.3; FAC3 §§9.2, 21–22; FAC4 §18.4 | The project accumulates canonical/review results under `DEGRADED_SINGLE_AGENT`. Later isolation/multi-agent capability becomes available. Proposals say “reopen” and measure debt, but there is no authoritative discoverable set of which decisions must be replayed, so trust debt can remain scattered in prose/comments indefinitely. | Define a typed `TrustDebt` registry/index: subject result/decision, current profile, required target profile, reason/resource constraint, affected downstream authority, OPEN/CLOSED/SUPERSEDED, reopen trigger. Capability change must deterministically expose eligible audit/reverification work. |
| FG-M05 | MAJOR | FAC2 §§9.8, 11; FAC3 §§12–13, 19–20; FAC4 §§9, 11, 13, 16, 23 | A task requires check X. X becomes FLAKY; an independent replacement evidence path exists. FAC4 can describe substitution/quarantine, FAC3 can judge an EvidenceBundle, while FAC2 needs a machine READY/integration predicate. No shared versioned object says whether replacement Y satisfies requirement X. Different components can disagree while all follow their proposal. | Synthesis must define content-addressed `EvidenceRequirement` and `EvidenceSatisfaction` schemas per claim: required class/result/trust/evaluator versions, allowed substitutions/quarantine policy, exact evidence refs, requirement version. Changing/substituting a gate is judge-affecting and creates a new requirement version. |
| FG-M06 | MAJOR | GOV §9.5; FAC3 §§10, 20; FAC2 §§9.8, 10 | Risk tiers are qualitative and review routes can be escalated, but no deterministic minimum-risk trigger or authority says who classifies the work. A producer/control-plane could classify a judge-affecting canonical change as low risk and avoid META/PROTECTED review while remaining consistent with one reading of the proposals. | Define non-downgradable risk floors derived from task/change traits: judge-affecting, canonical/systemic, protected-oracle/permission, external/legal-sensitive, destructive/irreversible, broad fan-out. Compiler/control plane sets minimum route; producer cannot lower it. Ambiguity escalates or requires bounded classification review. |
| FG-M07 | MAJOR | FAC1 §9.4; FAC2 §13; FAC4 §§17, 26 | Domain reviews/syntheses consume producer `work_sha` values that may exist only on never-merged task branches. Later branch/ref cleanup can make Git objects/evidence unreachable even though a downstream canonical decision still cites them. “PR/GitHub objects or other refs” is not a retention proof. | Before any branch/ref deletion, require an authority-graph reachability proof and durable anchor/snapshot for every downstream-consumed work/evidence SHA. Canonical provenance manifests must name retained refs or content-addressed snapshots; GC is CAS-protected and fails closed on unresolved reachability. |
| FG-M08 | MAJOR | GOV §9.7; FAC3 §13; FAC4 §§9.2, 17, 23 | Governance defines external/generated artifact provenance (`provenance_id`, rights/terms verdict); FAC4 defines evidence artifacts (`evidence_id`, content hash, retention/access). The same file/model output can receive independent identities and inconsistent allow/quarantine/retention decisions. A quarantined artifact could still be consumed as “evidence” without a common identity/policy link. | Define a shared content-addressed `ArtifactIdentity` (or mandatory cross-reference) used by provenance and evidence records. Usage-policy/quarantine state must be checked whenever the artifact is consumed, including as evaluation input/evidence. Rights policy and evidence retention remain separate dimensions on the same identity. |
| FG-m09 | MINOR | FAC2 §§9.4–9.7, 15 | The proposed atomic ref-lock/lease replacement is presented prominently but its namespace, transaction composition, durable lease authority, and crash transitions are deliberately unproven. A synthesis could accidentally elevate the design from “spike” to operating policy. | Mark the ref-lock/lease design `EXPERIMENTAL_NOT_ADOPTABLE` until FAC2-E1/E2 plus a durable lease-authority experiment close the state machine. Keep current schema-3 fencing as the canonical fallback until then. |
| FG-m10 | MINOR | FAC1 §9.5 | `ContextManifest.forbidden_or_not_loaded` can be interpreted as enumerating everything excluded. On a large repository, documenting all omitted context can itself consume context/handoff budget and become stale. | Store forbidden-by-default policy categories/packet policy version/hash rather than an exhaustive list; enumerate only explicit exceptions or material deliberately excluded refs. |
| FG-m11 | MINOR | FAC2 §9.2 | Native GitHub `blocked by` mirrors can appear resolved when a producer issue is closed at `REVIEW_READY`, even if a richer downstream result predicate is still unsatisfied. Canonical graph correctly wins, but derived UI can mislead agents/operators. | Mirror predicate-aware derived state alongside native dependency UI and explicitly assert `issue closed != prerequisite result satisfied`; reconciliation should surface this mismatch, never feed native closure directly into READY. |
| FG-n12 | NOTE | FAC4 §§13, 26 | CI outage handling correctly refuses bypass and lets unaffected work proceed, but a durable service-incident/recovery object is not yet defined. | Later control-plane/evidence synthesis should type CI/evaluator service incidents so recovery/replacement evidence remains explicit and observable. |
| FG-n13 | NOTE | FAC2 §10; FAC4 §18 | The proposals correctly reject scalar throughput, but scheduler benchmarking must ensure “quality-pipeline first” does not mistake open PR count, closed producer issues, or review queue volume for verified WIP/priority. | Benchmark queue definitions against canonical result state and measure useful READY frontier/escape outcomes, not GitHub activity counts. |

## 6. Detailed findings

### FG-B01 — Higher-authority directives are absent from the control-plane proof

**Observed.** GOV §9.1 makes a later valid in-scope explicit human directive the highest authority, and §9.2 requires material directives to become repository/GitHub-visible `DirectiveRecord`s. FAC2 §9.1 defines the control-plane authority layers as canonical graph/contract → GitHub operational state → derived cache → local state. FAC2 §9.8 lists the inputs to `READY(T)` and to `ready_proof`, but neither surface binds an active directive set/version.

**Failure scenario.** A resource or priority directive says “do not start domain X until condition Y” or an emergency safety directive stops a surface. Agent A applies the governance hierarchy and treats the task as blocked. Scheduler B applies FAC2’s canonical graph + operational-state proof and claims it because all recorded task prerequisites and locks are satisfied. Both can cite a proposal as support.

**Why BLOCKER.** This is not UI drift; it can authorize the wrong mutation under the project’s highest authority class. A synthesized control plane must have one deterministic input representing material active directives.

**Required correction.** Give directives a closed validity/order/scope/supersession contract and include the resulting active-directive-set identity in state snapshots/READY/claim/recovery/integration proofs. Hidden chat is still non-authoritative: emergency stop can be obeyed immediately, but downstream automation must not depend on it until the durable bounded record exists.

### FG-M02 — Scope absorption can outrun acquired conflict locks

**Observed.** FAC1 §9.11 allows current-task absorption when newly discovered work is necessary, bounded, and “inside owned/conflict-safe surface.” FAC2 §9.6 derives conflicts from contract-declared `conflict_keys` acquired atomically at claim/resume/recovery.

**Failure scenario.** Two independent tasks start with disjoint keys. Each discovers a necessary change to the same shared schema/configuration. Each sees the change as bounded and required for acceptance. There is no defined operation that expands its lock set before touching the shared surface.

**Required correction.** The semantic absorption rule must be conditional on **currently held** conflict keys, not a local judgment that the work seems safe. New key required → atomically acquire all added keys against current ownership/head → record scope/context/review impact → mutate. Failure to acquire means block/reroute/discovered-work, not “small opportunistic fix.”

### FG-M03 — A judge-affecting candidate can ambiguously choose the policy that judges it

**Observed.** GOV §9.6 forbids a worker from weakening the rule judging its own work and requires `FactoryChangeRecord` evidence/review/verification. FAC3 defines `META_VERIFICATION` for evaluator/metric/permission/constitution changes. FAC4 §§19–20 requires before/after benchmarks and meta-review before protocol adoption.

**Gap.** None explicitly states which **active policy version** is authoritative while candidate version N+1 is being evaluated.

**Failure scenario.** N requires protected verification for scheduler-policy changes. N+1 proposes that this class only needs normal independent verification. If the task compiler/reviewer loads N+1’s route as soon as the candidate exists, N+1 weakened its own gate without directly “editing the current evaluator.”

**Required correction.** Versioned two-phase authority: N remains the evaluator/routing authority for N+1; N+1 has zero authority until verified promotion. Any migration test may simulate N+1 but not use it as the acceptance gate. Record previous version and rollback target in terminal promotion.

### FG-M04 — Degraded independence creates debt without a deterministic debt ledger

**Observed.** FAC1/FAC3 correctly label one-agent role separation degraded and require reopening when stronger isolation exists. FAC3 observability tracks “DEGRADED decisions awaiting stronger audit.” FAC4 factory metrics also tracks current DEGRADED trust debt.

**Gap.** No proposal defines the authoritative object/index from which “awaiting stronger audit” is derived.

**Failure scenario.** After months of autonomous work, isolated execution becomes available. Canonical decisions, reviews, and verifier results contain dispersed trust profiles/reopen prose. The dispatcher has no deterministic query for which authoritative descendants should be replayed or sampled first.

**Required correction.** Typed debt records linked to the exact result/decision and downstream authority graph. Capability/resource-state change should make a bounded audit/reverification frontier derivable. Clearing debt requires a stronger result or explicit reviewed supersession; it cannot disappear because an issue was closed.

### FG-M05 — Evidence requirements and evidence satisfaction are described by three components but not shared

**Observed.** FAC3 defines claim-specific evidence sufficiency and an `EvidenceBundle`. FAC4 defines Run Reports, Evidence Artifacts, task-gated evidence classes, flaky/inconclusive outcomes, quarantine, substitutions, and Evidence Indexes. FAC2 requires evidence/check state in READY/integration mechanics and rulesets.

**Failure scenario.** Required check `save_replay/v3` is quarantined after a proven infrastructure flake. FAC4 policy permits a specific independent integration scenario as replacement. The verifier judges the EvidenceBundle sufficient, but the scheduler/ruleset still sees the original required check non-PASS—or the opposite, an old green status satisfies the UI while the evidence requirement version changed.

**Required correction.** One content-addressed requirement contract per acceptance claim and one satisfaction object resolving exact evidence to that requirement version. Required fields should cover allowed result states, CI/evidence class, minimum trust profile, evaluator/check version, substitutions, protected requirement, applicability, and coverage constraints. Quarantine/substitution changes the requirement under a judge-affecting route rather than mutating an informal list.

### FG-M06 — Risk classification can be self-downgraded

**Observed.** GOV §9.5 defines useful R0–R3 dimensions/tiers. FAC3 §20 maps work classes to minimum review routes and allows escalation. FAC2 can check that required independence is satisfiable.

**Gap.** No deterministic rule derives the **minimum** tier/route from task properties, and no authority is named for classification.

**Failure scenario.** A producer changes a verifier threshold or branch-rule permission but labels the task “bounded/reversible R1.” The route never reaches META/PROTECTED review even though the change is judge-affecting.

**Required correction.** Encode risk-floor triggers in the canonical compiler/governance policy. At minimum judge-affecting surfaces, canonical/systemic changes, protected-oracle/permission changes, external/legal-sensitive use, destructive migration, and broad authority fan-out must force specified minimum routes. Producer can request stronger review, never weaker. Unclassifiable material work fails upward or routes a bounded classification review.

### FG-M07 — Exact reviewed SHAs can lose their durable anchor

**Observed.** FAC1 §9.4 correctly says consumers use immutable `work_sha`. FAC2 §13 allows branch deletion after integration if work/evidence SHAs remain reachable through PR/GitHub objects or retained refs. FAC4 §17 requires canonical provenance evidence to remain reachable.

**Failure scenario.** A producer proposal is reviewed and synthesized by exact task-branch work SHA but the producer branch is never itself merged. Later housekeeping deletes that branch because the issue is terminal and PR discussion is considered sufficient. Git reachability/retention changes and a later verifier can no longer retrieve the exact reviewed blob/commit.

**Required correction.** Treat downstream consumption as a retention edge. Before branch/ref deletion, materialize a durable retained ref or content-addressed snapshot manifest for all consumed work/evidence SHAs; prove reachability through the authority graph. A PR number is provenance metadata, not by itself a retention guarantee.

### FG-M08 — Provenance identity and evidence identity can diverge for the same artifact

**Observed.** GOV §9.7 gives external/generated artifacts a provenance record including hash, source, terms/policy verdict and quarantine state. FAC4 §9.2 gives evidence artifacts a separate ID/hash/storage/retention/access model; FAC3 EvidenceBundles then consume artifact refs.

**Failure scenario.** A generated image/dataset/model output is quarantined by the provenance policy but separately ingested as an evidence artifact with no mandatory provenance link. A reviewer or benchmark later consumes it because the evidence index only knows its `evidence_id`.

**Required correction.** Share one content-addressed artifact identity or require an immutable cross-reference between evidence and provenance records. Consumption must evaluate both evidence validity and usage/provenance policy. Retention class and legal/usage verdict are distinct fields, not competing identity systems.

## 7. Minor findings and notes

### FG-m09 — Experimental ref-lock design needs an explicit non-adoption marker

FAC2 is appropriately candid that `updateRefs` composition, lock namespace, rulesets, lease authority, and crash states require FAC2-E1/E2. The risk is synthesis prose accidentally treating the proposal as selected architecture. Preserve the current canonical schema-3 fence until the experiment closes the full transaction/lease state machine; label the replacement design `EXPERIMENTAL_NOT_ADOPTABLE` in synthesis/dependency output.

### FG-m10 — Context manifests should not enumerate the universe they did not load

FAC1 §9.5’s `forbidden_or_not_loaded` is useful conceptually, but exhaustive omission lists scale with repository size. Prefer canonical context-policy/version hash + categories + explicit material exclusions/exceptions.

### FG-m11 — Native dependency UI can imply the wrong result predicate

FAC2 correctly keeps the canonical graph authoritative. Still, a closed producer issue at `REVIEW_READY` can look “done” to native dependency UI while a downstream task needs a specific result/disposition. Derived views should expose predicate satisfaction separately and never map issue closure directly to canonical READY.

### FG-n12 — CI outage should become a typed service incident

FAC4 already blocks unsafe PASS and lets unaffected work continue. Later synthesis/control-plane work should make the incident/recovery object machine-visible so replacement evidence and recovery are auditable without inventing a waiver.

### FG-n13 — Quality-queue metrics must use canonical result state

FAC2/FAC4 correctly reject activity metrics. Benchmarks should explicitly verify that open PR count, closed producer issue count, and GitHub queue volume do not substitute for canonical WIP/result state when applying quality-first scheduling.

## 8. Cross-proposal contradictions / interface obligations

The following are synthesis obligations, not optional polish:

1. **Authority → scheduler:** GOV’s directive hierarchy must become an explicit FAC2 state/READY input.
2. **Scope → locking:** FAC1 discovered-work absorption must call FAC2 lock expansion or reroute before touching new conflict surfaces.
3. **Governance version → trust/evidence:** GOV/FAC3/FAC4 need one old-policy-governs-new-policy activation rule.
4. **Trust debt → dispatcher:** FAC3’s degraded-trust debt needs a discoverable canonical registry and trigger semantics.
5. **Trust/evidence → control plane:** FAC3 evidence sufficiency and FAC4 run/check/quarantine semantics need one machine EvidenceRequirement/Satisfaction contract FAC2 can evaluate.
6. **Risk → review routing:** GOV risk dimensions must set non-downgradable FAC3 review-class floors.
7. **Work/evidence consumption → GC:** FAC1 immutable work SHAs and FAC4 evidence retention must become FAC2 GC reachability edges.
8. **Artifact provenance → evidence:** GOV provenance policy and FAC4 EvidenceArtifact identity must share/cross-bind content identity and usage policy.

These interfaces should appear explicitly in `W1-SYN-FAC`; otherwise the synthesis has merely concatenated proposals.

## 9. Required empirical questions before canonical adoption

The following proposal elements remain evidence questions and must not be promoted as established implementation decisions merely because the prose is coherent:

- **FAC2-E1/E2:** Can the actual GitHub repository/account/ruleset/permission setup implement all-or-none task + conflict-lock CAS and deterministic crash recovery?
- **Lease authority:** Which durable trusted timestamp/event substrate closes stale-owner recovery without an opaque scheduler-only database?
- **FAC2-E4/E5/E6:** Can branch/ruleset/check/merge configuration enforce the intended trust boundary and squash/current-base invariants, including any merge queue?
- **FAC3-E1/E4/E6/E8:** How much defect escape/reward-hacking/protected-oracle leakage remains under degraded/full/protected profiles?
- **FAC4-E3/E4/E7/E10:** Can flake classification, evidence retention, protocol benchmarks, and benchmark-drift controls survive injected failures/GC/Goodhart pressure?
- **FAC1-E1/E2/E5:** Do the proposed handoff/context/discovered-work rules improve substitution and prevent scope/WIP explosion without hiding critical context?

Synthesis may declare these as blocked empirical follow-ups; it must not fabricate PASS results.

## 10. Disposition and next action

**Disposition: `CHANGES_REQUIRED`.**

The reviewed proposals remain valuable inputs and none is `INVALIDATED`. `W1-SYN-FAC` is the correct correction surface. It must:

1. explicitly disposition **FG-B01** and every **FG-M02–FG-M08** finding;
2. produce one coherent authority/state/evidence/trust/retention interface rather than five parallel vocabularies;
3. preserve the explicit experimental status of unvalidated control-plane mechanisms;
4. separate canonical operating rules from empirical work that still needs spikes;
5. preserve no-routine-human-gate, current-base verification, candidate immutability, squash-only integration, and the implementation-readiness barrier;
6. retain exact producer/review provenance and the current DEGRADED trust profile.

`W1-SYN-FAC` should not modify the reviewed producer branches or retroactively reinterpret their REVIEW_READY results. It owns the synthesis/revision artifact and must record every accepted/rejected/deferred finding with evidence.

## 11. Reopen conditions / review limitations

Reopen this review if:

- a producer branch/work SHA changes despite the frozen REVIEW_READY result;
- a new proposal version is substituted without a fresh review episode;
- stronger isolated/multi-agent review becomes available and reveals additional material findings;
- an FAC2/FAC3/FAC4 experiment produces evidence contradicting a finding or exposing a new blocker;
- synthesis invents a new interface not traceable to the reviewed proposals/findings;
- a later explicit human directive changes authority, integration, or trust constraints.

This review’s DEGRADED trust remains explicit. The result is sufficient for the currently canonical single-agent liveness mode, but it should not be described later as full independent review.