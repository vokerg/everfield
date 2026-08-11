# Technical and Evidence Adversarial Review — Wave 1

**Mission:** `W1-REV-TECH`  
**Role:** independent adversarial reviewer  
**Trust:** `DEGRADED_SINGLE_AGENT` / DEGRADED  
**Disposition:** `CHANGES_REQUIRED`  
**Findings:** **0 BLOCKER / 12 MAJOR / 4 MINOR / 2 NOTE**

## 1. Exact reviewed inputs

This review binds only the immutable producer states frozen in `technical-evidence-review-input.yaml`:

| Mission | Issue | Status comment | Work SHA |
|---|---:|---:|---|
| W1-FAC-02 | #24 | `5245532215` | `095372a41498e8d7e3b25364cba89dbc647b8839` |
| W1-FAC-03 | #25 | `5245577951` | `70b763a965cdec0fa1f6c025a5b7492b844288fc` |
| W1-FAC-04 | #26 | `5245629575` | `99b0c7b3bddbad1a71e05f085fd0bd9f2c74e566` |
| W1-TEC-01 | #27 | `5249255787` | `3b1e159932b2d23d6641e0ba3e97dfa72da10219` |
| W1-TEC-02 | #28 | `5248845557` | `c13389cf1df7ab8e2515a5267bd56869082df1b2` |
| W1-EVAL-01 | #33 | `5248979052` | `a29a9c08f64947b383f4ca6a19fb88032d93777d` |

The reviewer did not edit any producer candidate. The attack plan was committed before deep candidate reconciliation. The one-agent constraint is recorded by Issue #5 comment `5244416013`; this result does not claim full independence.

## 2. Executive result

The six proposals are directionally compatible and none is invalidated. They consistently reject premature engine choice, self-authored evidence as sole authority, retry laundering, engine-object canonical state, universal quality scores, and opaque unversioned evaluators.

The material weakness is **composition**. Several proposals independently define run/scenario/evidence/candidate/environment/evaluator identities, determinism manifests, protected evidence, and promotion rules, but the current packet does not yet provide one mechanically composable technical verification contract. Synthesis can repair this without rewriting the producer artifacts.

Proceeding to synthesis is appropriate. Proceeding directly from these producers to implementation readiness, an engine ADR, or protected verification would not be.

## 3. MAJOR findings

### TE-M01 — Evidence identities overlap but do not compose into one authority envelope

**Attack.** W1-FAC-03 defines `EvidenceBundle`; W1-FAC-04 defines `Run Report` and `Evidence Artifact`; W1-TEC-01 defines `engine_eval_run`; W1-TEC-02 defines determinism/save/content identities; W1-EVAL-01 defines scenario/policy/evaluator records. All bind useful provenance, but no exact crosswalk says which fields form the canonical identity of one execution result.

**Failure scenario.** An engine spike and a protected evaluator both cite the same candidate SHA but differ in base, content package, environment, evaluator version, or attempt lineage. A downstream verifier cannot mechanically determine whether the evidence applies to the exact claim.

**Required synthesis correction.** Define one versioned `ExecutionEvidenceEnvelope` (name may differ) with a mandatory identity tuple at least covering candidate work/head/base, build/runtime/toolchain environment, content/schema package identities where applicable, scenario/policy/evaluator versions, input hashes/seeds, attempt lineage, result classification, artifact hashes, and trust profile. Producer-specific records may extend it but may not redefine identity semantics.

### TE-M02 — Deterministic state hashes lack a canonical serialization/normalization contract

**Attack.** W1-TEC-02 requires deterministic state/hash scopes, ordering, numeric rules, and content identity, but intentionally leaves physical encoding/numeric representation open.

**Failure scenario.** Two engine candidates execute semantically identical state but serialize map order, floating-point values, strings, null/default fields, or references differently. Their hashes differ; alternatively two serializers omit different future-affecting defaults and accidentally hash equal.

**Required synthesis correction.** Require a versioned canonical semantic serialization/hash contract before cross-runtime hash equality is acceptance evidence: deterministic field/order rules, numeric/float policy, string normalization, null/default handling, stable reference encoding, hash-scope version, and conformance vectors executable by every candidate adapter. Until then hashes are local evidence only.

### TE-M03 — Nondeterministic/external adapter outcomes are not typed tightly enough for replay authority

**Attack.** W1-TEC-02 separates platform/presentation services and says external inputs/nondeterministic surfaces must be declared; engine/evaluator proposals depend on reproducible evidence around them.

**Failure scenario.** Physics, wall-time service, asynchronous platform API, generated content service, or other adapter affects canonical state. A replay records only the command/input, not the nondeterministic outcome that influenced the state, so reproducing the same seed/actions diverges.

**Required synthesis correction.** Type boundary interactions such as `PURE_INPUT`, `RECORDED_INPUT_OR_OUTCOME`, `CANONICAL_OUTCOME`, and `PRESENTATION_ONLY`; specify what is recorded, what is substituted during replay, and what may never affect canonical state without a recorded canonical result. Physics/external-service decisions must explicitly select one category.

### TE-M04 — A total event order is a useful fallback but can silently become a global serialization bottleneck

**Attack.** W1-TEC-02 names total order within one simulation timeline as the safe initial default while later permitting weaker ordering.

**Failure scenario.** Independent simulation domains route every event through one global sequence solely to satisfy determinism. This creates contention, harms parallelism, and couples otherwise independent systems; later removal changes replay semantics.

**Required synthesis correction.** Define causality/order semantics independently from storage/transport: domain-local deterministic order, explicit cross-domain causal edges, stable tie-breakers for simultaneous effects, and conditions requiring a global order. Require contention/performance/replay experiments before promoting one total event stream as implementation architecture.

### TE-M05 — Save migration needs a version-tuple and semantic compatibility contract, not only ordered forward transforms

**Attack.** W1-TEC-02 correctly separates save and replay compatibility and recommends forward migrations with fixtures.

**Failure scenario.** Save schema version advances while content package/schema set changes independently. A migration succeeds structurally but an item/NPC/quest definition was removed or semantically repurposed; the loaded world silently changes meaning.

**Required synthesis correction.** Bind migration source/target tuples including save envelope, canonical schema set, content package identities, and migration tool/version. Require idempotence/composition tests, removed/orphaned-content policy, unsupported downgrade behavior, historical fixtures, structured loss reporting, and rollback/recovery semantics. Silent semantic dropping is forbidden.

### TE-M06 — Engine candidate admission and harness equivalence can still encode selection bias

**Attack.** W1-TEC-01 is explicitly neutral and records candidate-specific deviations, but candidate-set construction and “equivalent” native adaptation remain judgment surfaces.

**Failure scenario.** A favored candidate receives a native implementation while another receives a weak adapter or an unnecessarily difficult spike; or plausible candidates are excluded from discovery without a recorded falsifier. The later score appears evidence-based but the experiment was biased upstream.

**Required synthesis correction.** Require a bounded candidate-discovery rationale/coverage rule, an adaptation manifest for every spike, and independent equivalence review before comparative scoring. Early hard-gate exits must preserve the exact failing evidence. Conditional engine selection must carry an explicit expiry/falsifier/checkpoint so Milestone Zero does not silently become permanent architecture.

### TE-M07 — Protected evidence needs a reproducible public result contract and auditable disclosure path

**Attack.** W1-FAC-03 and W1-FAC-04 correctly protect only selected Goodhart-sensitive surfaces and reject full opacity.

**Failure scenario.** A protected verifier returns FAIL/PASS from inaccessible inputs/configuration but exposes too little to reproduce the judged candidate identity or distinguish evaluator failure from product failure. Conversely, debugging reveals the entire holdout and destroys protection.

**Required synthesis correction.** Define a protected-result envelope exposing candidate/base/environment/evaluator identity, oracle version/hash, result class, coverage category, bounded diagnostic/failure class, and immutable evidence reference while keeping protected inputs behind access policy. Oracle changes/reveals need audited meta-change records. Missing/unavailable protected evidence is `INCONCLUSIVE`, never PASS.

### TE-M08 — The proposed GitHub multi-ref ownership/lock transaction is still an experiment and cannot yet replace schema-3 authority

**Attack.** W1-FAC-02 is careful to call GraphQL `updateRefs` + lock refs a spike, but the proposal also sketches future state semantics around fence refs.

**Failure scenario.** Multi-ref CAS succeeds and audit comment fails, lock refs collide with rulesets, reconciliation races with recovery, or a crashed worker leaves a lock set whose task state cannot be mechanically resolved. A later implementation treats the sketch as already-proven authority.

**Required synthesis correction.** Keep current schema-3 behavior as the verified fallback until a repository-specific CAS/lock experiment passes. Define the experimental reconciliation state machine for `REFS_CREATED_EVENT_MISSING`, event-without-valid-ref, lock partiality (if any API behavior differs from assumptions), lock ordering/deadlock avoidance, lease renewal, GC, and stale recovery. Promotion requires measured repository evidence, not documentation alone.

### TE-M09 — CI result aggregation has no exact algebra for required/conditional/NOT_RUN checks

**Attack.** W1-FAC-04 correctly distinguishes PASS/FAIL/FLAKY/INCONCLUSIVE/NOT_RUN and says retries cannot erase failures.

**Failure scenario.** A task report summarizes PASS while one conditionally required integration or protected check was NOT_RUN because applicability was evaluated differently by producer and verifier. Both local schemas are valid but aggregate authority differs.

**Required synthesis correction.** Compile a versioned required-check set from the task/claim contract before execution. Define applicability/`NOT_APPLICABLE` separately from `NOT_RUN`, aggregate truth tables for required/optional/quarantined checks, infrastructure failure semantics, quarantine expiry/replacement evidence, and a rule that missing required execution yields INCONCLUSIVE/FAIL according to the contract, never PASS.

### TE-M10 — Tool/evaluator/provider drift can stale evidence without a source-code version change

**Attack.** W1-FAC-03/04 and W1-EVAL-01 record evaluator versions and discuss drift, but “version” can be insufficient for hosted or mutable tools.

**Failure scenario.** The same evaluator/model/provider identifier produces materially different outputs after backend change. Old benchmarks are compared to new verdicts as if evaluator identity were stable.

**Required synthesis correction.** Define an evaluator/environment fingerprint containing every observable immutable/configurable identifier plus calibration corpus/result fingerprint where provider internals are not pin-able. Schedule calibration for mutable evaluators, define drift thresholds/escalation, and reopen affected evidence when calibration crosses the declared boundary. Missing identity/fingerprint makes high-impact subjective/protected evidence inconclusive.

### TE-M11 — Abstract simulation versus production/shared-kernel evidence admissibility is not mechanically typed

**Attack.** W1-EVAL-01 correctly uses both accelerated simulation and real/shared-kernel reruns; W1-TEC-01/02 require production-like evidence for material integration claims.

**Failure scenario.** A fast abstract economy/progression simulator passes a claim about real gameplay state transitions even though its rules have diverged from the canonical kernel. The “simulation evidence” label obscures that it is a model of the product rather than execution of the product.

**Required synthesis correction.** Type evidence execution surfaces (`MODEL_SIMULATION`, `SHARED_KERNEL`, `FULL_EXECUTABLE`, etc.) and map claim classes to admissible surfaces. Abstract/model simulations generate hypotheses/distribution evidence unless cross-validated against the shared kernel for the relevant rule set. Integration/correctness claims must state when the production/shared kernel is mandatory.

### TE-M12 — Named experiments need an explicit promotion barrier so proposal language cannot harden into implementation truth

**Attack.** All six proposals responsibly label many choices as experiments, candidates, or deferred evidence.

**Failure scenario.** A downstream implementation task quotes a recommended lock-ref design, deterministic event ordering, engine hard gate, or protected-evidence topology as if it already passed the named experiment because the proposal itself reached REVIEW_READY.

**Required synthesis correction.** Every technical synthesis decision must be typed at least as `CANDIDATE_CONTRACT`, `EVIDENCE_REQUIRED`, `VERIFIED_DECISION`, or `DEFERRED`. Each `EVIDENCE_REQUIRED` decision binds concrete experiment/evidence IDs and an explicit transition predicate; implementation-readiness compiler must refuse to promote it as settled architecture until that predicate is met.

## 4. MINOR findings

### TE-m01 — Evidence artifact locator durability needs explicit health checking

Content hash establishes identity but not availability. Add scheduled/reconciliation checks for retained authoritative artifacts and a restoration/escalation path when storage references disappear.

### TE-m02 — Engine cost comparison should separate cold-start tool acquisition from steady-state build cost

Keep setup/cache population, incremental build/test, artifact storage, and agent/tool adapter maintenance as separate distributions so one warm-cache figure cannot dominate.

### TE-m03 — Schema namespace ownership needs collision and retirement semantics

Narrow namespaces reduce merge conflicts, but synthesis should specify how namespaces are allocated, transferred, deprecated, and checked for semantic collisions across packages.

### TE-m04 — Scenario expected-result changes should bind reason class

W1-EVAL-01 distinguishes intended product change, evaluator correction, regression-baseline update, and defect masking. Make that reason mandatory metadata for changed golden/protected expectations.

## 5. NOTES

### TE-N01 — The packet correctly keeps external/current engine capabilities out of memory-based assertions

W1-TEC-01's `UNKNOWN` discipline is a strong anti-bias property and should survive synthesis.

### TE-N02 — The packet consistently rejects one-scalar authority

Scheduler priority, factory metrics, engine comparison, synthetic players, and subjective quality all preserve multidimensional evidence. Cross-domain synthesis should avoid reintroducing an aggregate gate accidentally.

## 6. Contradictions and reconciliation requirements

No producer pair contains a fatal contradiction. The following tensions are intentionally left to synthesis:

- GitHub/ref authority versus repository/schema-3 operational authority during migration to a mature control plane;
- deterministic logical kernel versus candidate-native engine facilities;
- transparent debugging versus protected oracle secrecy;
- fast model simulation versus production/shared-kernel evidence;
- centralized evidence identity versus distributed domain ownership;
- global event order simplicity versus parallel simulation/concurrency.

Synthesis should resolve these as versioned interfaces and staged evidence transitions, not choose one side by assertion.

## 7. Empirical questions that remain open

The review does not answer unrun experiments. At minimum the following remain empirical:

- repository-specific GraphQL multi-ref CAS and lock/ruleset behavior;
- claim/recovery crash and GC races;
- engine candidate current-source admission and all comparative spikes;
- cross-runtime deterministic serialization/hash conformance;
- persistence migrations over real content/schema changes;
- real/shared-kernel replay and accelerated-simulation parity;
- protected-evidence storage/access/disclosure behavior;
- evaluator drift/calibration reliability;
- CI flake/quarantine and evidence-retention recovery;
- factory/evaluator reward-hacking benchmarks.

## 8. Disposition

`CHANGES_REQUIRED`.

- BLOCKER: 0
- MAJOR: 12
- MINOR: 4
- NOTE: 2

`W1-SYN-TECH` may proceed and must explicitly disposition TE-M01 through TE-M12. It must preserve all unrun experiments as evidence obligations and must not select an engine or declare implementation readiness.

## 9. Reopen conditions

Reopen this review if:

- a producer work SHA changes;
- synthesis cannot create one exact evidence/provenance identity across the six domains;
- an engine is selected before the comparative evidence/ADR route is satisfied;
- current schema-3 authority is replaced by an unverified lock-ref/control-plane mechanism;
- deterministic hashes are used cross-runtime without conformance rules;
- protected or model-simulation evidence is admitted beyond its declared trust/execution surface;
- stronger independent execution becomes available and the degraded review can be rerun with higher trust.
