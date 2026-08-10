issue: 23
mission_id: W1-FAC-01
role: factory operating-model planner
branch: planning/issue-23
base_sha: 413e729e8d2d5ac2eb138903f3f2ace07283b23e
ownership_generation_comment_id: 5245444590
work_sha: e7fe3d0eaae22038e661ea941e652a618c3a7ec7
state: REVIEW_READY
completed:
  - Produced docs/planning/wave-1/proposals/agent-operating-model.md using only the issue's authoritative input packet.
  - Defined persistent Task vs disposable Episode semantics and durable Work State.
  - Defined authority/evidence-based role classes and role-transition boundaries, including explicit DEGRADED_SINGLE_AGENT trust debt.
  - Defined Context Manifest, trigger-based progressive context widening, and no-silent-truncation rules.
  - Defined continuation/recovery reconstruction before mutation and handoff-as-navigation-not-authority semantics.
  - Defined structured handoff quality, stopping triggers, pre-stop obligations, and forced-substitution benchmark criteria.
  - Defined typed discovered-work routing with strict current-task absorption rules and no uncontrolled same-wave issue creation.
  - Preserved W1-FAC-02 ownership of exact GitHub scheduler/claim/CAS mechanics and W1-FAC-03 ownership of stronger trust policy.
  - Defined seven bounded experiments covering forced substitution, context ablation, stale handoffs, crash recovery, discovered-work storms, multi-episode tasks, and degraded-vs-isolated role separation.
remaining:
  - W1-REV-FAC must independently attack this proposal after W1-GOV-01 and W1-FAC-02 through W1-FAC-04 are REVIEW_READY.
  - W1-SYN-FAC must reconcile this semantic model with exact control-plane, trust, evidence/CI, and governance proposals.
checks_performed:
  - Review Index measured approximately 3.3 KB UTF-8, below the 4,000-byte limit.
  - Proposal/research shape includes status, scope, inputs/source basis, goals/non-goals, constraints, assumptions, alternatives, design, interfaces/conflicts, observability, experiments, failure modes, risks, open questions, reopen conditions, critique, and downstream work.
  - Evidence/inference/recommendation are explicitly separated.
  - No current external claims are required; no unsupported unstable claim is treated as fact.
  - Task/session/branch semantics do not invent competing atomic control-plane rules.
  - Continuation requires current state/branch/evidence reconciliation and independent sampling before mutation.
  - Discovered-work handling cannot silently expand task scope or create uncontrolled active issues.
  - No human-wait state, gameplay implementation, current-wave issue generation, self-review, or self-canonicalization is authorized.
  - All main integration remains squash-only.
evidence:
  - docs/planning/wave-1/proposals/agent-operating-model.md at work_sha e7fe3d0eaae22038e661ea941e652a618c3a7ec7
  - canonical authoritative packet at activation main 413e729e8d2d5ac2eb138903f3f2ace07283b23e
known_problems:
  - Exact machine representation/enforcement of these semantics remains W1-FAC-02 work.
  - Context-budget thresholds and task-size/checkpoint thresholds require empirical measurement rather than this proposal's intuition.
  - DEGRADED_SINGLE_AGENT is weaker than isolated role separation and must reopen when stronger capability exists.
  - Explicit coordinated multi-agent subtask semantics remain an open future design question.
decisions:
  - Task lifetime is persistent and can span disposable episodes; useful state must be repository-reconstructable.
  - Handoffs are evidence/navigation, never ownership authority.
  - Optional context widening starts from a named question and stable retrieval reason.
  - Worker discoveries become typed candidate work unless strictly necessary, bounded, owned, and acceptance-related.
  - Favor finishing/reviewing existing work over comparable-priority WIP proliferation.
scope_deviations: []
recommended_next_action: Leave this output NON-CANONICAL and REVIEW_READY; continue the remaining Wave 1 root frontier while W1-REV-FAC remains dependency-blocked.

## Final head note

`work_sha` is the substantive proposal commit. The final schema-3 STATUS must record the later branch head containing this handoff.