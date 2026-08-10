issue: 26
mission_id: W1-FAC-04
role: CI/evidence/factory-measurement planner
branch: planning/issue-26
base_sha: 413e729e8d2d5ac2eb138903f3f2ace07283b23e
ownership_generation_comment_id: 5245588888
work_sha: 99b0c7b3bddbad1a71e05f085fd0bd9f2c74e566
state: REVIEW_READY
completed:
  - Produced docs/planning/wave-1/proposals/ci-evidence-and-factory-measurement.md from the declared factory/evaluation/research/deliverables packet.
  - Defined a structured Run Report bound to exact candidate/base/environment/workflow/evaluator versions and artifact manifest.
  - Defined content-addressed EvidenceArtifact and compact Evidence Index concepts so large evidence stays outside ordinary agent context.
  - Defined PRECHECK, PR_FAST, INTEGRATION, PROTECTED_VERIFY, DEEP_PERIODIC, and FACTORY_BENCHMARK classes with task-specific gating.
  - Defined PASS/FAIL/FLAKY/INCONCLUSIVE/NOT_RUN semantics, retry history preservation, and reviewed quarantine requirements.
  - Defined deterministic/replay evidence, player+simulation surfaces, semantic coverage, evaluator versioning, baselines, and subjective/multimodal evidence rules.
  - Defined authority-aware retention classes and garbage-collection constraints for transient/task/canonical/protected evidence.
  - Defined multidimensional factory measurement and versioned paired protocol-change benchmarks with seeded defects and rollback.
  - Defined ten bounded experiments covering reconstruction, replay, flake injection, GC, protected access, Goodhart, protocol A/B, CI outage, context indexing, and benchmark drift.
remaining:
  - W1-REV-FAC must attack metric incentives, benchmark Goodhart paths, outage liveness, WIP effects, and self-improvement governance.
  - W1-REV-TECH must attack report reproducibility, determinism, artifact identity/retention, flake classification, protected evidence, and real-system evidence.
  - W1-SYN-FAC/W1-SYN-TECH must reconcile storage/enforcement/trust details with sibling proposals.
checks_performed:
  - Review Index measured approximately 3.3 KB UTF-8, below 4,000-byte limit.
  - Proposal/research shape includes all required status/scope/source/goals/constraints/assumptions/alternatives/design/interfaces/evaluation/experiments/failures/risks/questions/reopen/critique/downstream sections.
  - Evidence, inference, and recommendations are separated; no current external product claim is required.
  - Required FLAKY/INCONCLUSIVE/NOT_RUN outcomes cannot become PASS by retries.
  - Retry history remains visible and flake classification does not hide unexplained nondeterminism.
  - Protected evidence remains versioned/auditable and diagnosable rather than opaque authority.
  - Canonical/protected evidence cannot be garbage-collected without authority-aware reachability checks.
  - Factory metrics remain a diagnostic vector and protocol changes require repeated paired benchmark evidence plus rollback.
  - No CI infrastructure, protected oracle, extra current-wave issue, gameplay implementation, self-review gate, or self-canonicalization is created.
  - All main integration remains squash-only.
evidence:
  - docs/planning/wave-1/proposals/ci-evidence-and-factory-measurement.md at work_sha 99b0c7b3bddbad1a71e05f085fd0bd9f2c74e566
  - authoritative packet at activation main 413e729e8d2d5ac2eb138903f3f2ace07283b23e
known_problems:
  - Exact artifact store, protected evidence permissions, and retention durations are intentionally unresolved.
  - Concrete determinism boundaries depend on later runtime/engine evidence.
  - Benchmark suite representativeness and run counts require empirical calibration.
  - CI service topology and cost/performance budgets remain technical implementation work.
decisions:
  - CI is an evidence sensorium; dashboard status is a derived summary, not sufficient proof.
  - Large evidence uses immutable refs/indexes rather than default context preload.
  - Required flaky/inconclusive evidence blocks acceptance unless replaced or the gate is separately reviewed/changed.
  - Retention is authority/event-based before fixed time durations are justified.
  - Factory self-improvement is benchmarked on quality/escape/flow/recovery/trust tradeoffs, never raw speed alone.
scope_deviations: []
recommended_next_action: Leave this proposal NON-CANONICAL and REVIEW_READY. W1-REV-FAC is now eligible because all of its producer prerequisites are REVIEW_READY; W1-REV-TECH remains blocked on its technical/game-evaluation roots.

## Final head note

`work_sha` is the substantive proposal commit. Final schema-3 STATUS must bind the later branch head containing this handoff.