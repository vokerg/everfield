# W2-EVAL-01 — Evaluator fingerprint, calibration, and drift experiment

**Mission:** `W2-EVAL-01`  
**Task class:** `PLANNING_EXPERIMENT / EVIDENCE_REQUIRED`  
**Branch base:** `main@c7ba185ed9667b717794c19eaa0834ca41aa4c78`  
**Result:** `BOUNDED_PASS_WITH_MATERIAL_DRIFT_DETECTED`  
**Required downstream review:** `W2-REV-01`  
**Universal evaluator authority:** `NONE`  
**Implementation-readiness authority:** `NONE`

## 1. Scope and non-goals

This experiment exercises the minimum evaluator-trust semantics required by the canonical Wave 1 foundations: stable evaluator fingerprints, a frozen calibration corpus, repeated distributions, explicit disagreement and empirical error-correlation groups, backend/model drift detection, bounded reopen thresholds, and a protected-slice variant.

It does **not** select an evaluator provider/model, define a universal quality score, claim that synthetic calibration predicts human judgment, prove evaluator independence, authorize an engine or gameplay architecture, or resolve implementation readiness. All model/provider names below are synthetic fixture identities.

## 2. Canonical constraints carried from Wave 1

The experiment preserves these planning rules:

- `ExecutionEvidenceEnvelope` binds exact evaluator fingerprints and attempt lineage.
- Important subjective/AI decisions use `JudgmentPanelRecord`; multiple calls/model names do not automatically create independent evidence.
- Mutable evaluator backends require fingerprints, calibration, and a drift reopen policy.
- Evaluator/provider version change is a freshness invalidation trigger; stale required evidence makes dependent decisions `INCONCLUSIVE`/OPEN.
- Protected evidence binds evaluator and calibration fingerprints and is `INCONCLUSIVE` when unavailable/corrupt/unverifiable.
- Synthetic evaluators are versioned models, not proxies for humans or a universal fun score.

## 3. Evidence questions and experiment contract

```yaml
PlanningExperiment:
  experiment_id: w2-eval-01-fixture-v1
  task_mission_id: W2-EVAL-01
  evidence_question_refs:
    - EVAL-Q1-fingerprint-required-for-authority
    - EVAL-Q2-repeated-calibration-distribution
    - EVAL-Q3-correlation-is-not-panel-size
    - EVAL-Q4-backend-drift-reopens-authority
    - EVAL-Q5-protected-calibration-slice
  decision_refs_blocked_or_informed:
    - IR-BLOCKER-EVIDENCE-FOUNDATION
    - evaluator-authority-policy
  allowed_ownership_surface: docs/planning/wave-2/evidence/evaluator-drift-calibration.md
  task_branch: planning/issue-78
  disposable: true
  production_dependency_allowed: false
  production_content_authority: NONE
  canonical_game_content_authority: NONE
  engine_lock_in_authority: NONE
  required_review: W2-REV-01
  retention_policy: retain frozen synthetic corpus definition, fingerprints, metrics, and deterministic generation algorithm
  cleanup_or_quarantine_rule: protected slice is a secrecy simulation only; no real holdout or provider secret is committed
  completion_predicate: declared cases reproduce and authority remains bounded to evaluator qualification
```

## 4. Frozen calibration corpus

Corpus identity:

```text
W2-EVAL-CAL-v1
sha256:418187e76e8936fdb16f68b1ee5eb9d9da96cf9361a1a7c5b7b7138d780a9df7
```

The corpus contains 24 deterministic binary calibration cases, balanced 12 positive / 12 negative:

- `C01`–`C16`: `PUBLIC` calibration cases.
- `C17`–`C24`: `PROTECTED_SIMULATION` cases; only aggregate slice metrics are used for ordinary diagnostics.
- reference label: odd 1-based case number → `1`; even → `0`.
- difficulty cycles by pairs: `easy`, `medium`, `hard`, repeat.
- 20 attempts per evaluator configuration, yielding 480 judgments/configuration.

The committed corpus is synthetic and therefore not a real secret holdout. `PROTECTED_SIMULATION` exists only to test whether qualification records can carry aggregate protected-slice authority without requiring ordinary per-case disclosure.

## 5. Evaluator fingerprints

A fingerprint is the SHA-256 of canonical JSON over provider/model family, exact model version, evaluator-code version, rubric identity, prompt identity, toolchain identity, policy epoch, and calibration-corpus identity. Episode/context identity is **not** part of the evaluator fingerprint; it remains separate in `JudgmentPanelRecord`.

| Fixture evaluator | Family / model | Rubric/prompt | Fingerprint |
|---|---|---|---|
| `A1` | fixture-family-A / A-1.0 | v1 / v1 | `96ce45b29189d12fb2c2108ba312f0548a4321d8a15cf3f5d6e5f88de100f5ab` |
| `B1` | fixture-family-B / B-1.0 | v1 / v1 | `00fa0656f0156eaf8f327350b85464f12f9d48dca25488cb07ea4ad46036afa6` |
| `C1` | fixture-family-C / C-1.0 | v1 / v1 | `c9695d49a6a6486498efcd4816097549530884575ea2bb2bf7a7143bf089caf1` |
| `A2-model-drift` | fixture-family-A / A-2.0 | v1 / v1 | `07cd5d7f1a975702cfbbccf9ce6b158d54e722b916123d08a1bf0d54296319bb` |

Three episodes (`A1`, `A1-clone`, `A1-clone-2`) intentionally share the exact `A1` fingerprint and a shared latent-noise stream. Their separate episode IDs therefore increase panel **calls**, not evaluator-fingerprint diversity.

### Missing-fingerprint authority case

A synthetic evaluator producing the same prediction stream as `A1` but omitting its fingerprint is classified:

```yaml
calibration_execution: OBSERVED
high_impact_evaluator_identity: MISSING
qualification_result: INCONCLUSIVE
authority_effect: HIGH_IMPACT_PASS_FORBIDDEN
```

Good observed accuracy cannot substitute for missing evaluator identity because later drift/freshness cannot be bound to that evidence.

## 6. Deterministic reference model

The fixture gives each case a signed margin by difficulty:

```text
easy=2.20, medium=1.20, hard=0.45
```

Prediction is `score >= 0`, where:

```text
score = signed_margin * evaluator_scale + evaluator_bias
      + deterministic_gaussian(shared_stream, case, attempt) * sigma
      + optional_small_episode_noise
```

Evaluator profiles:

| Profile | scale | bias | sigma | stream relation |
|---|---:|---:|---:|---|
| A1 | 1.00 | 0.00 | 0.85 | baseline A-v1 |
| A1-clone | 1.00 | +0.02 | 0.85 | same A-v1 shared stream + small episode noise |
| A1-clone-2 | 1.00 | -0.01 | 0.85 | same A-v1 shared stream + small episode noise |
| B1 | 1.00 | -0.05 | 0.95 | independent B-v1 stream |
| C1 | 1.00 | +0.05 | 0.90 | independent C-v1 stream |
| A2-model-drift | 0.75 | +0.55 | 1.15 | changed A-v2 stream |

Every Gaussian sample is seeded from the first 64 bits of `sha256(stream|case|attempt)`, so reruns are deterministic.

## 7. Repeated calibration distributions

Twenty complete 24-case runs were executed for each primary evaluator.

| Evaluator | Accuracy | Per-run accuracy mean ± population SD | Run range | FPR | FNR | Repeat instability |
|---|---:|---:|---:|---:|---:|---:|
| A1 | 89.38% | 89.38% ± 6.25 pp | 79.17–100.00% | 10.83% | 10.42% | 10.62% |
| B1 | 87.29% | 87.29% ± 6.65 pp | 75.00–100.00% | 15.42% | 10.00% | 12.71% |
| C1 | 86.67% | 86.67% ± 4.68 pp | 79.17–95.83% | 15.42% | 11.25% | 12.92% |
| A2-model-drift | 75.42% | 75.42% ± 7.89 pp | 62.50–87.50% | 39.17% | 10.00% | 21.67% |

`Repeat instability` is the fraction of attempts disagreeing with each case's modal prediction for that evaluator. The range/instability evidence is retained because a single aggregate mean would hide run-to-run variability.

## 8. Correlation and disagreement experiment

Paired metrics use the same 480 `(case, attempt)` positions. `Error correlation` is Pearson correlation of binary error indicators; it is descriptive fixture evidence, not a universal independence proof.

| Pair | Prediction disagreement | Error correlation |
|---|---:|---:|
| A1 vs A1-clone | 2.08% | 0.8873 |
| A1 vs A1-clone-2 | 0.63% | 0.9669 |
| A1-clone vs A1-clone-2 | 2.29% | 0.8744 |
| A1 vs B1 | 17.08% | 0.1729 |
| A1 vs C1 | 18.54% | 0.1233 |
| B1 vs C1 | 20.62% | 0.0895 |

Two three-member panels make the point explicit:

```yaml
correlated_panel:
  calls: 3
  exact_fingerprint_count: 1
  provider_model_family_count: 1
  majority_accuracy: 89.58%
  correlation_group_count: 1
  independence_claim: FORBIDDEN

diverse_fixture_panel:
  calls: 3
  exact_fingerprint_count: 3
  provider_model_family_count: 3
  majority_accuracy: 93.54%
  empirical_error_correlation: lower_than_correlated_fixture
  independence_claim: NOT_PROVEN
```

The second panel is empirically less correlated in this fixture, but common orchestration, common evidence sources, common oracle control, shared training data, or other hidden dependencies can still correlate failures. Panel size and provider/model-name diversity therefore remain evidence features, not independence certificates.

## 9. Backend/model drift case

`A1` and `A2-model-drift` keep rubric, prompt, evaluator code, corpus, and policy epoch fixed; only the synthetic backend/model version and its behavior change. The fingerprint changes accordingly.

Observed drift relative to A1 across all 480 judgments:

- accuracy: `89.38% -> 75.42%` (`-13.96 pp`);
- false-positive rate: `10.83% -> 39.17%` (`+28.33 pp`);
- false-negative rate: `10.42% -> 10.00%` (`-0.42 pp`);
- repeat instability: `10.62% -> 21.67%` (`+11.04 pp`);
- paired prediction disagreement: `27.71%`.

Protected-slice drift:

- A1 protected accuracy: `85.63%`;
- A2-model-drift protected accuracy: `71.88%`;
- delta: `-13.75 pp`;
- protected FPR: `16.25% -> 41.25%` (`+25.00 pp`).

This is a clear fixture reopen: a version label change cannot inherit prior qualification merely because provider/model family is unchanged.

## 10. Candidate qualification / reopen thresholds

These thresholds are a **bounded Wave 2 candidate policy for review**, not a universal evaluator standard:

1. **Fingerprint presence:** missing exact fingerprint → high-impact qualification `INCONCLUSIVE`; no PASS authority.
2. **Fingerprint change:** any fingerprint change requires calibration rerun before high-impact reuse; old evidence remains historical.
3. **Material calibration drift:** reopen dependent evaluator authority if any frozen-corpus metric changes by at least `5 percentage points` in accuracy, FPR, or FNR.
4. **Behavioral disagreement:** reopen if paired old/new prediction disagreement is at least `10%` on the frozen corpus.
5. **Stability drift:** reopen if repeat-instability increases by at least `5 percentage points`.
6. **Protected slice:** reopen if protected aggregate accuracy/FPR/FNR changes by at least `5 percentage points`, or if the required protected slice is unavailable/corrupt/unverifiable.
7. **Judge-affecting rubric/prompt/policy change:** create a new fingerprint and `PolicyEpoch`; do not compare as if only provider drift occurred.
8. **Calibration-corpus revision:** new corpus identity requires an explicit bridge/comparison episode; historical results are not silently rewritten.

A reopen means the dependent decision/evidence becomes OPEN/INCONCLUSIVE until the new evaluator state is requalified under its applicable requirement and review route. It does not imply automatic provider rejection.

The model-drift fixture trips thresholds 3, 4, 5, and 6.

## 11. Protected calibration variant

`C17`–`C24` model a protected holdout slice. Ordinary qualification output exposes only:

```yaml
protected_slice:
  corpus_ref: sha256:418187e76e8936fdb16f68b1ee5eb9d9da96cf9361a1a7c5b7b7138d780a9df7
  case_count: 8
  evaluator_fingerprint_ref: <exact>
  attempts_per_case: 20
  aggregate_accuracy: <aggregate>
  aggregate_fpr: <aggregate>
  aggregate_fnr: <aggregate>
  availability: AVAILABLE | UNAVAILABLE | CORRUPT
```

No per-case protected diagnostic is required by this fixture's public result envelope. If the protected slice is unavailable/corrupt, its required qualification contribution becomes `INCONCLUSIVE`; public calibration cannot silently replace it unless a versioned `EvidenceRequirement` explicitly authorizes substitution.

Because all cases in this task are synthetic and repository-visible, this tests **result-shape and authority semantics only**, not real holdout secrecy or access control. Real protected-store mechanics remain a separate evidence surface.

## 12. Evidence, inference, and recommendation

### Observed evidence

- Exact fingerprint manifests produce stable content-addressed identities.
- A missing fingerprint blocks high-impact authority even when the underlying prediction stream is otherwise A1-like.
- Twenty repeated runs expose materially different variability across evaluator configurations.
- Same-fingerprint A1 episodes show very high paired error correlation (`0.8744–0.9669`) and very low disagreement (`0.63–2.29%`).
- Different synthetic families show much lower paired error correlation (`0.0895–0.1729`) and higher disagreement (`17.08–20.62%`).
- The A-1.0 → A-2.0 backend/model change causes large calibration, false-positive, stability, protected-slice, and paired-disagreement drift.

### Inference

The Wave 1 evaluator contract is mechanically usable if evaluator identity, calibration corpus, attempt lineage, disagreement/correlation, and freshness are separate typed evidence. Treating call count as independence or allowing a mutable backend to inherit old qualification would lose material failure information in this fixture.

### Recommendation

Carry forward the exact-fingerprint + frozen-corpus + repeated-distribution + explicit-correlation-group pattern as the minimum candidate evaluator qualification contract. Require W2-REV-01 to attack the proposed thresholds and claim boundaries before any synthesis treats them as accepted planning policy.

## 13. Failure modes and risks retained

- Synthetic binary calibration is not evidence about real aesthetic, design, safety, accessibility, or gameplay judgment quality.
- The deterministic noise model is constructed; its numerical correlations are illustrative, not estimates of real providers.
- Pearson correlation of binary errors is only one dependence signal and can miss shared systematic blind spots.
- Three provider/model families can still share training data, prompts, evidence sources, orchestration, or oracle control.
- A fixed corpus can be overfit or leaked; corpus freshness/rotation and contamination detection require separate evidence.
- Aggregate protected metrics can still leak information across repeated adaptive queries; query-budget/privacy analysis is not exercised.
- Thresholds can create Goodhart pressure if treated as sole acceptance metrics; qualitative/adversarial findings must retain authority.
- Calibration against synthetic reference labels cannot establish alignment with humans or product goals.
- Current execution is producer-side planning evidence; `W2-REV-01` remains the independent/degraded-independent authority gate.

## 14. Reopen conditions

Reopen this evidence or dependent evaluator authority when:

- provider/model version, evaluator code, rubric, prompt, toolchain, policy epoch, or calibration corpus identity changes;
- a required fingerprint field is absent or cannot be reproduced;
- any reviewed material-drift threshold is crossed;
- protected calibration evidence becomes unavailable/corrupt/unverifiable or is compromised;
- new evidence shows hidden correlation not represented by current `correlation_groups`;
- calibration corpus contamination/overfitting is discovered;
- a dependent claim changes risk floor or requires stronger evaluator trust;
- stronger isolated/multi-agent capability permits a stronger independence test;
- W2-REV-01 records BLOCKER/MAJOR findings against this contract or its evidence.

## 15. Required independent critique and downstream effect

`W2-REV-01` must independently attack at least:

- fingerprint completeness and collision/identity assumptions;
- whether episode identity is correctly separated from evaluator fingerprint;
- frozen-corpus representativeness and contamination/overfit risk;
- repeated-run sufficiency and retained distribution shape;
- correlation metric blind spots and panel-independence claims;
- whether `5 pp` / `10%` candidate reopen thresholds are too weak, too strong, or Goodhart-prone;
- protected-slice disclosure and unavailable-evidence semantics;
- any accidental upgrade from evaluator qualification to universal judgment authority.

This mission informs `IR-BLOCKER-EVIDENCE-FOUNDATION` and `W2-REV-01`. It does not by itself resolve the blocker, select an evaluator, or authorize implementation readiness.

## Appendix A — reproducibility algorithm

The executed reference can be reconstructed with Python standard library semantics:

```python
import hashlib, random

MARGIN = {"easy": 2.20, "medium": 1.20, "hard": 0.45}
PROFILES = {
    "A1":          ("A-v1", 1.00,  0.00, 0.85, "A1",       0.05),
    "A1-clone":    ("A-v1", 1.00, +0.02, 0.85, "A1clone",  0.05),
    "A1-clone-2":  ("A-v1", 1.00, -0.01, 0.85, "A1clone2", 0.05),
    "B1":          ("B-v1", 1.00, -0.05, 0.95, "B1",       0.00),
    "C1":          ("C-v1", 1.00, +0.05, 0.90, "C1",       0.00),
    "A2-model-drift": ("A-v2", 0.75, +0.55, 1.15, "A2",    0.00),
}

def seed(*parts):
    raw = "|".join(map(str, parts)).encode()
    return int(hashlib.sha256(raw).hexdigest()[:16], 16)

def gauss(*parts):
    return random.Random(seed(*parts)).gauss(0, 1)

def case(i):
    # i is zero-based
    label = 1 if i % 2 == 0 else 0
    difficulty = ("easy", "medium", "hard")[(i // 2) % 3]
    visibility = "PUBLIC" if i < 16 else "PROTECTED_SIMULATION"
    return f"C{i+1:02d}", label, difficulty, visibility

def predict(profile, i, attempt):
    name, label, difficulty, _ = case(i)
    stream, scale, bias, sigma, eps_stream, eps_sigma = PROFILES[profile]
    sign = 1 if label == 1 else -1
    score = sign * MARGIN[difficulty] * scale + bias
    score += gauss(stream, name, attempt) * sigma
    if eps_sigma:
        score += gauss(eps_stream, name, attempt) * eps_sigma
    return int(score >= 0)

# Execute i=0..23 and attempt=0..19 for every profile.
# Metrics in this report derive from those 480 judgments/profile.
```

The appendix is evidence reproducibility support only; it is disposable planning-experiment logic and has no production dependency authority.
