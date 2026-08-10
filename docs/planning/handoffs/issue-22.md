issue: 22
mission_id: W1-GOV-01
role: governance planner
branch: planning/issue-22
base_sha: 413e729e8d2d5ac2eb138903f3f2ace07283b23e
ownership_generation_comment_id: 5245380374
work_sha: ffa6b62b3b20c84a152e676b7a5db223daa130e5
state: REVIEW_READY
completed:
  - Produced docs/planning/wave-1/proposals/governance-and-canonicality.md using only the issue's authoritative packet.
  - Defined a scoped authority hierarchy, typed human-directive semantics, canonical decision lifecycle, decision-record schema, qualitative risk tiers, judge-affecting self-modification governance, provenance/quarantine framework, rollback/supersession rules, interfaces, observability, failure modes, and reopen conditions.
  - Preserved no-routine-human-gate, repository-memory, independent-review, Goodhart-resistance, reversibility, broad-frontier, and squash-only constraints.
  - Deferred jurisdiction/provider/license-specific legal conclusions to authoritative bounded research instead of making unsupported legal claims.
  - Defined six bounded governance experiments, including cold-start authority resolution, self-modification red-team, directive collision, provenance/quarantine, rollback, and later degraded-vs-isolated review comparison.
  - Named W1-REV-FAC as the required independent adversarial critique and did not instantiate additional current-wave work.
remaining:
  - W1-REV-FAC must independently attack this proposal after all of its required factory/governance producer inputs are REVIEW_READY.
  - W1-SYN-FAC must later reconcile accepted findings with W1-FAC-01 through W1-FAC-04.
checks_performed:
  - Review Index measured approximately 3.0 KB UTF-8, below the 4,000-byte limit.
  - Proposal/research shape includes status, scope, inputs/source basis, goals/non-goals, constraints, assumptions, alternatives, design, interfaces/dependencies/conflicts, observability/evaluation, bounded experiments, failure modes, risks, open questions, reopen conditions, required critique, and downstream work.
  - Observed repository evidence is separated from inference and recommendations.
  - Material alternatives are represented and rejected with rationale.
  - No current external legal/provider/license claim is treated as settled fact; unresolved specifics are explicitly deferred to authoritative research.
  - No gameplay implementation, final engine choice, self-canonicalization, or new current-wave issue generation is authorized.
  - All main integration remains squash-only.
evidence:
  - docs/planning/wave-1/proposals/governance-and-canonicality.md at work_sha ffa6b62b3b20c84a152e676b7a5db223daa130e5
  - authoritative packet at activation main 413e729e8d2d5ac2eb138903f3f2ace07283b23e
known_problems:
  - Exact legal/IP/license policy remains intentionally unresolved pending authoritative research.
  - DEGRADED_SINGLE_AGENT remains weaker than isolated independent review and must be reconsidered when stronger isolation/multiple agents are available.
  - Exact machine storage/enforcement of DirectiveRecord/DecisionRecord is an interface for W1-FAC-02 rather than settled here.
decisions:
  - Recommend explicit scope-aware authority records; never infer canonicality from merge/path/closure.
  - Treat higher governance risk as requiring stronger evidence/separation, not routine human approval.
  - Treat unknown provenance/rights as quarantined/research-required rather than silently allowed or globally blocking.
  - Require separate factory-change work for judge-affecting self-modification.
scope_deviations: []
recommended_next_action: Leave this producer output NON-CANONICAL and REVIEW_READY; continue the Wave 1 root frontier while W1-REV-FAC remains blocked until all required producer inputs are ready.

## Final head note

`work_sha` is the substantive proposal commit. The final schema-3 STATUS must record the later branch head containing this handoff.