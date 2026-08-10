issue: 25
mission_id: W1-FAC-03
role: verification/trust planner
branch: planning/issue-25
base_sha: 413e729e8d2d5ac2eb138903f3f2ace07283b23e
ownership_generation_comment_id: 5245540196
work_sha: 70b763a965cdec0fa1f6c025a5b7492b844288fc
state: REVIEW_READY
completed:
  - Produced docs/planning/wave-1/proposals/review-verification-and-trust.md from the declared factory/evaluation/research/deliverables packet only.
  - Defined five trust dimensions: authorship, private context, candidate write, oracle control, and evidence source.
  - Defined NOT_INDEPENDENT, DEGRADED_SINGLE_AGENT, FULL_INDEPENDENT_CONTEXT, and PROTECTED trust profiles without equating procedural separation to cognitive independence.
  - Defined SELF_CHECK, ADVERSARIAL_REVIEW, CROSS_DOMAIN_REVIEW, INDEPENDENT_VERIFICATION, PROTECTED_VERIFICATION, and META_VERIFICATION classes.
  - Defined finding severity/disposition, claim-specific evidence sufficiency, EvidenceBundle binding, candidate immutability, role permission targets, protected evaluation tiers, evaluator versioning, and disagreement protocol.
  - Defined anti-Goodhart controls and exact integration-eligibility conditions including current-base/head/evaluator freshness.
  - Defined nine bounded trust/evaluation experiments including seeded defects, permission red-team, disagreement, Goodhart challenge, evaluator drift, protected leakage, base drift, degraded-vs-isolated replay, and review-queue load.
remaining:
  - W1-REV-FAC must attack role laundering, hidden gates, self-modification, WIP/parallelism, and DEGRADED permissiveness after the full factory packet is ready.
  - W1-REV-TECH must attack permission enforceability, protected-oracle implementation, evidence binding/reproducibility, evaluator provenance, and freshness after the full technical packet is ready.
  - W1-SYN-FAC/W1-SYN-TECH must reconcile exact trust classes with control-plane and CI/evidence implementation proposals.
checks_performed:
  - Review Index measured approximately 3.4 KB UTF-8, below the 4,000-byte limit.
  - Proposal/research shape includes status, scope, inputs/source basis, goals/non-goals, constraints, assumptions, alternatives, design, interfaces, observability, experiments, failure modes, risks, open questions, reopen conditions, required critique, downstream work.
  - Same-context self-review is explicitly NOT_INDEPENDENT.
  - DEGRADED_SINGLE_AGENT remains explicitly weaker than isolated/multi-agent review and carries a reopen condition.
  - Reviewer/verifier candidate mutation is prohibited for a result binding the frozen candidate.
  - Producer-authored tests may contribute but cannot be sole material acceptance evidence.
  - Protected evaluators remain versioned/auditable and require meta-change review rather than opaque authority.
  - Disagreement escalates through targeted evidence/re-evaluation rather than majority or routine human tie-breaking.
  - PASS cannot float across candidate/base/evaluator drift.
  - No gameplay implementation, protected-infrastructure mutation, new current-wave issue generation, self-review gate, or self-canonicalization is authorized.
  - All main integration remains squash-only.
evidence:
  - docs/planning/wave-1/proposals/review-verification-and-trust.md at work_sha 70b763a965cdec0fa1f6c025a5b7492b844288fc
  - authoritative packet at activation main 413e729e8d2d5ac2eb138903f3f2ace07283b23e
known_problems:
  - Exact protected-evidence storage and permission enforcement remain W1-FAC-04/control-plane implementation questions.
  - DEGRADED_SINGLE_AGENT remains correlated and cannot fully remove shared-model reasoning error.
  - Review class thresholds by risk require seeded-defect/escape benchmark evidence.
  - Subjective evaluator diversity cannot be assumed from count alone and needs empirical measurement.
decisions:
  - Independence is a typed multi-dimensional trust boundary, not a UUID or boolean.
  - Candidate under independent verification is immutable; corrections route through revision/restart.
  - Protected evaluation is selective and versioned, not universal secrecy.
  - Evidence sufficiency is claim-specific and material claims require at least one non-producer-only evidence path.
  - Judge-affecting evaluator/review/permission changes require META_VERIFICATION.
scope_deviations: []
recommended_next_action: Leave this proposal NON-CANONICAL and REVIEW_READY; continue W1-FAC-04. Domain reviews remain blocked until all declared producer prerequisites are REVIEW_READY.

## Final head note

`work_sha` is the substantive proposal commit. Final schema-3 STATUS must bind the later branch head containing this handoff.