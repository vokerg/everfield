issue: 33
mission_id: W1-EVAL-01
role: game-evaluation planner
branch: planning/issue-33
base_sha: 413e729e8d2d5ac2eb138903f3f2ace07283b23e
ownership_generation_comment_id: 5248952760
work_sha: a29a9c08f64947b383f4ca6a19fb88032d93777d
state: REVIEW_READY
completed:
  - Produced docs/planning/wave-1/proposals/automated-game-evaluation.md from the declared authoritative packet.
  - Defined a claim-to-evidence matrix separating correctness, integration, persistence, progression/economy, quest/narrative, UX/accessibility, visual/audio, experiential, and performance claims.
  - Defined versioned semantic gameplay coverage focused on transitions/interactions rather than object/code touch counts.
  - Defined scenario/golden/protected evidence with canonical state/build/content/actions/seeds/coverage/evaluator binding and the real/shared-kernel principle.
  - Defined versioned synthetic-player policy classes: deterministic, rule-based, search/optimizer, fuzz/exploit, and later benchmarked LLM/VLM mechanisms.
  - Defined accelerated simulation, differential/exploit search, progression/economy/quest/world failure targets, and player-versus-simulation surface checks.
  - Defined structured subjective evaluation with atomic rubrics, randomized/pairwise comparison, multiple independent episodes, disagreement, and adversarial critique.
  - Defined selective protected evaluation with versioning, actionable diagnostics, leakage/overfit monitoring, and meta-governed changes.
  - Defined evaluator identity/version/result provenance, drift replay, inconclusive failure semantics, and evidence escalation.
  - Defined ten bounded experiments for seeded defects, coverage mutation, persona diversity, exploit search, protected leakage, evaluator drift, subjective disagreement, long-run reproducibility, cross-surface mismatch, and evaluator cost/frontier impact.
remaining:
  - Independent adversarial reviews W1-REV-TECH and W1-REV-GAME.
  - Benchmark concrete evaluator/model/tool technologies before adoption; no current capability is assumed by this proposal.
  - Reconcile evaluation contracts into W1-SYN-TECH and W1-SYN-GAME after review outcomes.
checks_performed:
  - Review Index measured at 3165 UTF-8 bytes, below the 4000-byte limit.
  - No universal fun/quality score is introduced; coverage and evaluator metrics are diagnostic vectors.
  - Synthetic personas are explicitly versioned models/assumptions, not proxies for real-player preference.
  - Protected evaluation remains selective, auditable, versioned, and not the primary opaque specification surface.
  - Evaluator/model/rubric changes cannot silently reinterpret historical results; drift/reopen evidence is explicit.
  - Simulation state evidence and player-surface evidence are paired for integration claims so neither launders the other.
  - Current evaluator/tool capability claims are deferred to bounded benchmarks rather than asserted.
  - Scope/non-goals, evidence/assumptions/inference/recommendations, alternatives, interfaces, observability, failure modes, risks, open questions, and reopen conditions are explicit.
  - No gameplay/evaluator implementation or extra current-wave issue generation occurred.
evidence:
  - docs/planning/wave-1/proposals/automated-game-evaluation.md@a29a9c08f64947b383f4ca6a19fb88032d93777d
known_problems:
  - Semantic coverage can itself become a Goodhart surface and needs mutation/escape-driven maintenance.
  - Synthetic policies may be expensive, correlated, or behaviorally unrepresentative; persona/model bias must remain visible.
  - Protected evaluation adds permission/storage/debugging complexity.
  - Subjective evaluator models may share correlated biases and require calibration against frozen/seeded evidence.
  - Evaluation routing cost can collapse useful throughput if stronger routes are applied indiscriminately.
decisions:
  - Evaluation is claim-specific and compositional; no single test, player, score, or judge is sufficient across the game.
  - Semantic transition/interaction coverage is preferred over catalog/code-touch coverage for gameplay possibility-space evidence.
  - Important integration scenarios use the real executable/shared gameplay kernel, not duplicate test implementations.
  - Protected scenarios/probes are a selective anti-Goodhart layer with versioned accountability.
  - Evaluator identity/version/environment/input binding is part of material evidence provenance.
scope_deviations: []
files_or_surfaces_changed:
  - docs/planning/wave-1/proposals/automated-game-evaluation.md
  - docs/planning/handoffs/issue-33.md
next_role_or_action: Publish schema-3 STATUS(REVIEW_READY) bound to the final branch head, keep the proposal NON-CANONICAL, then let W1-REV-TECH and W1-REV-GAME consume the exact work SHA after their complete prerequisite packets are ready.
