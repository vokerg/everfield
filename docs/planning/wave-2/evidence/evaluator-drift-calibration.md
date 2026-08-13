# W2-EVAL-01 — Evaluator fingerprint, calibration, and drift experiment

**Mission:** `W2-EVAL-01`  
**Task class:** `PLANNING_EXPERIMENT / EVIDENCE_REQUIRED`  
**Branch base:** `main@c7ba185ed9667b717794c19eaa0834ca41aa4c78`  
**Result:** `BOUNDED_PASS_WITH_MATERIAL_DRIFT_DETECTED`  
**Required downstream review:** `W2-REV-01`  
**Universal evaluator authority:** `NONE`  
**Implementation-readiness authority:** `NONE`

## 1. Scope and non-goals

This experiment exercises the minimum evaluator-trust semantics required by the canonical Wave 1 foundations: stable evaluator fingerprints, a frozen calibration corpus, repeated distributions, explicit disagreement/correlation groups, backend/model drift detection, bounded reopen thresholds, and a protected-slice variant.

It does **not** select an evaluator provider/model, define a universal quality score, claim that synthetic calibration predicts human judgment, prove evaluator independence, authorize an engine/gameplay architecture, or resolve implementation readiness. All provider/model identities below are synthetic fixtures.

## 2. Canonical constraints and assumptions

Carried constraints:

- `ExecutionEvidenceEnvelope` binds exact evaluator fingerprints and attempt lineage.
- `JudgmentPanelRecord` keeps evaluator fingerprint, episode/context, provider/model family, oracle relation, candidate-write relation, and evidence-source relation distinct.
- Multiple calls/model names do not automatically create independent evidence.
- Mutable evaluator backends require fingerprints, calibration, and drift reopen policy.
- Evaluator/provider version change is a freshness invalidation trigger; stale required evidence makes dependent decisions `INCONCLUSIVE`/OPEN.
- Protected evidence binds evaluator/calibration fingerprints and is `INCONCLUSIVE` if unavailable/corrupt/unverifiable.
- Synthetic evaluators are versioned models, not human proxies or universal fun scores.

Assumptions deliberately bounded to this fixture:

- binary reference labels are treated as known only to measure mechanics;
- deterministic pseudo-random streams model repeat variability, not real provider statistics;
- `PROTECTED_SIMULATION` tests result shape/authority only, not actual secrecy;
- Pearson correlation of binary error indicators is one observable dependence signal, not proof of independence.

## 3. Experiment contract

```yaml
PlanningExperiment:
  experiment_id: w2-eval-01-fixture-v2
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
  retention_policy: retain exact corpus/fingerprint generation rules, metrics, and deterministic reference algorithm
  cleanup_or_quarantine_rule: no real holdout/provider secret is committed
  completion_predicate: all declared cases reproducible and authority bounded to evaluator qualification
```

## 4. Frozen calibration corpus and identity

Exact corpus identity:

```text
W2-EVAL-CAL-v1
sha256:1028afb0a7cd27847c0aaed031a2008c4eefe5e092ae29e7eb01342323ef8683
```

The canonical corpus object contains `version` plus 24 ordered case objects with exactly `id`, `label`, `difficulty`, and `visibility` fields. Cases are generated as follows:

- IDs `C01`–`C24`;
- odd 1-based case number → reference label `1`; even → `0`;
- difficulty cycles by pairs: `easy`, `medium`, `hard`, repeat;
- `C01`–`C16` → `PUBLIC`;
- `C17`–`C24` → `PROTECTED_SIMULATION`.

The identity is SHA-256 over UTF-8 `json.dumps(object, sort_keys=True, separators=(",", ":"))`. Appendix A contains the exact executable constructor that reproduces the hash.

Twenty attempts are executed per case/configuration, yielding 480 judgments per evaluator configuration.

## 5. Evaluator fingerprint identity

A fingerprint is SHA-256 over canonical JSON with exactly these fields:

```yaml
provider_or_model_family: <synthetic family>
model_version: <exact synthetic model version>
evaluator_code: eval-fixture-v1
rubric: binary-calibration-rubric-v1
prompt: judge-binary-v1
toolchain: python-stdlib-reference
policy_epoch: eval-policy-v1
calibration_corpus_sha256: 1028afb0a7cd27847c0aaed031a2008c4eefe5e092ae29e7eb01342323ef8683
```

Observed content-addressed fingerprints:

| Evaluator | Family / model | Fingerprint |
|---|---|---|
| `A1` | fixture-family-A / A-1.0 | `2093ab31a254179b0d89eaac50661c38ec9e6bc84f69cc9f8bc60c02d765db1d` |
| `B1` | fixture-family-B / B-1.0 | `4aa7fd37cc43a59ef1e50d94872fe60e6ff2ef7067faa8cb3515f95d7d1d7dee` |
| `C1` | fixture-family-C / C-1.0 | `f4a9a286e6d2c8e075fa045f65760ecfd3ef59b26b666cbc50798889ea34cc50` |
| `A2-model-drift` | fixture-family-A / A-2.0 | `dfb69983a993ed75ac0a11006b508aeaa98b824142acf476bbca6c0194407691` |

Three episodes (`A1`, `A1-clone`, `A1-clone-2`) intentionally use the **same exact A1 fingerprint** and shared latent stream. Their distinct episode/context references therefore increase call count, not fingerprint diversity.

### Missing-fingerprint case

A synthetic evaluator replaying the A1 prediction stream while omitting its fingerprint is classified:

```yaml
calibration_execution: OBSERVED
high_impact_evaluator_identity: MISSING
qualification_result: INCONCLUSIVE
authority_effect: HIGH_IMPACT_PASS_FORBIDDEN
```

Observed accuracy cannot substitute for missing identity because freshness/drift cannot later bind to that evidence.

## 6. Deterministic evaluator model

Signed reference margins are `easy=2.20`, `medium=1.20`, `hard=0.45`.

```text
score = signed_margin * scale + bias
      + deterministic_gaussian(shared_stream, case, attempt) * sigma
      + optional_episode_noise
prediction = 1 if score >= 0 else 0
```

Profiles:

| Profile | scale | bias | sigma | stream relation |
|---|---:|---:|---:|---|
| A1 | 1.00 | 0.00 | 0.85 | A-v1 shared stream |
| A1-clone | 1.00 | 0.00 | 0.85 | same A-v1 + small episode noise |
| A1-clone-2 | 1.00 | 0.00 | 0.85 | same A-v1 + small episode noise |
| B1 | 1.00 | -0.05 | 0.95 | independent B-v1 stream |
| C1 | 1.00 | +0.05 | 0.90 | independent C-v1 stream |
| A2-model-drift | 0.75 | +0.55 | 1.15 | changed A-v2 stream |

Every Gaussian sample is seeded from the first 64 bits of `sha256(stream|case|attempt)`; episode-noise streams use the same rule.

## 7. Repeated distributions

Twenty full 24-case runs were executed for each primary evaluator.

| Evaluator | Accuracy | Per-run accuracy mean ± population SD | Run range | FPR | FNR | Repeat instability |
|---|---:|---:|---:|---:|---:|---:|
| A1 | 89.38% | 89.38% ± 6.25 pp | 79.17–100.00% | 10.83% | 10.42% | 10.62% |
| B1 | 87.29% | 87.29% ± 6.65 pp | 75.00–100.00% | 15.42% | 10.00% | 12.71% |
| C1 | 86.67% | 86.67% ± 4.68 pp | 79.17–95.83% | 15.42% | 11.25% | 12.92% |
| A2-model-drift | 75.42% | 75.42% ± 7.89 pp | 62.50–87.50% | 39.17% | 10.00% | 21.67% |

`Repeat instability` is the fraction of attempts differing from each case's modal prediction. This retains distribution shape that a single mean would hide.

## 8. Correlation/disagreement cases

Paired metrics use identical 480 `(case, attempt)` positions. `Error correlation` is Pearson correlation of binary error indicators.

| Pair | Prediction disagreement | Error correlation |
|---|---:|---:|
| A1 vs A1-clone | 1.88% | 0.8992 |
| A1 vs A1-clone-2 | 1.25% | 0.9333 |
| A1-clone vs A1-clone-2 | 1.88% | 0.8968 |
| A1 vs B1 | 17.08% | 0.1729 |
| A1 vs C1 | 18.54% | 0.1233 |
| B1 vs C1 | 20.62% | 0.0895 |

Panel comparison:

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

The diverse fixture panel performs better and has lower observed pairwise error correlation, but common training data, orchestration, evidence sources, or oracle control can still correlate failure. Panel size is therefore not an independence certificate.

## 9. Backend/model drift case

`A1` and `A2-model-drift` keep corpus, rubric, prompt, evaluator code, toolchain, and policy epoch fixed. Only synthetic backend/model version and behavior change, which changes the fingerprint.

Observed old→new drift across all 480 judgments:

- accuracy `89.38% -> 75.42%` (`-13.96 pp`);
- FPR `10.83% -> 39.17%` (`+28.33 pp`);
- FNR `10.42% -> 10.00%` (`-0.42 pp`);
- repeat instability `10.62% -> 21.67%` (`+11.04 pp`);
- paired prediction disagreement `27.71%`.

Protected-slice drift:

- accuracy `85.63% -> 71.88%` (`-13.75 pp`);
- FPR `16.25% -> 41.25%` (`+25.00 pp`).

The family label remaining “A” cannot justify inheriting A1 qualification.

## 10. Candidate qualification/reopen thresholds

These are **review candidates**, not universal evaluator standards:

1. Missing exact fingerprint → high-impact qualification `INCONCLUSIVE`; PASS forbidden.
2. Any fingerprint change → calibration rerun required before high-impact reuse; old evidence remains historical.
3. Reopen if frozen-corpus accuracy, FPR, or FNR changes by at least `5 percentage points`.
4. Reopen if paired old/new prediction disagreement is at least `10%`.
5. Reopen if repeat instability increases by at least `5 percentage points`.
6. Reopen if protected aggregate accuracy/FPR/FNR changes by at least `5 percentage points`, or required protected evidence becomes unavailable/corrupt/unverifiable.
7. Rubric/prompt/policy change is judge-affecting: new fingerprint + new `PolicyEpoch`; do not classify it as backend-only drift.
8. Corpus revision creates new corpus identity and requires explicit comparison/bridge; historical evidence is not rewritten.

A reopen makes dependent authority OPEN/INCONCLUSIVE until requalification and required review. It is not automatic provider rejection. `A2-model-drift` trips thresholds 3, 4, 5, and 6.

## 11. Protected variant

`C17`–`C24` form an eight-case `PROTECTED_SIMULATION` slice. Ordinary result shape exposes only corpus/fingerprint refs, case count, attempts, aggregate accuracy/FPR/FNR, and availability state; per-case diagnostics are not required.

If this slice is `UNAVAILABLE`, `CORRUPT`, or `UNVERIFIABLE`, its required qualification contribution is `INCONCLUSIVE`. Public calibration cannot silently substitute unless a versioned `EvidenceRequirement` explicitly permits replacement evidence.

Because the synthetic corpus is repository-visible, this demonstrates authority/result-envelope behavior only, not real secrecy, access control, or holdout resistance.

## 12. Alternatives vs recommendation

Alternatives evaluated:

- **Mutable evaluator alias only** (`provider/model=latest`): rejected for high-impact authority because drift cannot be bound reproducibly.
- **Single-run calibration:** rejected because run variability disappears.
- **Panel-count authority:** rejected because three same-fingerprint calls remain one observed correlation group.
- **Different model names imply independence:** rejected; lower fixture correlation is evidence, not proof.
- **Exact fingerprint + frozen corpus + repeated distribution + correlation groups + reopen triggers:** retained as the strongest bounded candidate in this experiment.

Recommendation: carry the retained candidate into W2-REV-01 as the minimum evaluator-qualification pattern, while treating numerical thresholds as attackable review candidates rather than settled policy.

## 13. Dependencies, interfaces, observability

Interfaces:

- `ExecutionEvidenceEnvelope.evaluator_fingerprints` consumes the exact fingerprint identity.
- `JudgmentPanelRecord.evaluators[]` keeps fingerprint and episode/context separate and records `correlation_groups`.
- `FreshnessRequirement(source_class=EVALUATOR_PROVIDER)` reopens on backend/provider version changes.
- protected evidence binds evaluator fingerprint + calibration fingerprint and fails closed when unavailable.
- `EvidenceSatisfaction` may consume qualified evaluator evidence only under the applicable requirement/risk floor.

Required observability for later real evaluator use:

- exact fingerprint manifest and calibration-corpus identity;
- attempt lineage and repeated distributions, not only aggregate score;
- per-dimension error/disagreement where claim type requires it;
- correlation-group rationale and known common dependencies;
- backend/provider freshness event and old/new comparison;
- protected-slice availability/integrity state;
- threshold/reopen event provenance.

## 14. Observed evidence vs inference

### Observed

- Exact corpus and fingerprint constructors reproduce stable hashes.
- Missing fingerprint blocks the synthetic high-impact authority case.
- Repeated runs expose evaluator-specific instability.
- Same-fingerprint episodes show high error correlation (`0.8968–0.9333`) and low disagreement (`1.25–1.88%`).
- Different fixture families show much lower error correlation (`0.0895–0.1729`) and higher disagreement (`17.08–20.62%`).
- A-1.0→A-2.0 backend/model drift materially degrades accuracy, false-positive rate, stability, protected slice, and paired agreement.

### Inference

The Wave 1 evaluator contract is mechanically usable if evaluator identity, corpus identity, attempt distribution, correlation grouping, and freshness remain separate evidence dimensions. Allowing mutable aliases or panel-count independence would discard material failure evidence in this fixture.

## 15. Failure modes and risks

- Synthetic binary labels do not establish real aesthetic/design/safety/accessibility/gameplay judgment quality.
- Deterministic noise is constructed; numerical correlations are not estimates of real providers.
- Pearson binary-error correlation can miss shared systematic blind spots.
- Multiple families can still share training data, prompts, evidence sources, orchestration, or oracle control.
- A fixed corpus can be leaked/overfit; contamination detection and rotation remain open.
- Aggregate protected metrics can leak cumulatively under adaptive querying; query-budget/privacy analysis is untested.
- Numerical thresholds can become Goodhart targets if made sole authority.
- Producer-side execution remains subject to required independent/degraded-independent review.

## 16. Unresolved questions

- What real evaluator claim classes require separate calibration corpora/risk floors?
- Which dependence measures supplement pairwise error correlation for structured judgments?
- How should calibration corpus rotation preserve longitudinal comparability without leaking holdouts?
- What provider fingerprint fields are actually available/reliable for mutable hosted evaluators?
- What query/retry budget is needed to bound cumulative leakage from protected diagnostics?
- Should threshold magnitude vary by claim risk rather than using one candidate `5 pp`/`10%` policy?

## 17. Reopen conditions

Reopen when:

- provider/model version, evaluator code, rubric, prompt, toolchain, policy epoch, or corpus identity changes;
- fingerprint identity is missing/unreproducible;
- any reviewed material-drift threshold is crossed;
- protected calibration becomes unavailable/corrupt/unverifiable/compromised;
- hidden correlation is discovered outside current groups;
- corpus contamination/overfitting is discovered;
- a dependent claim's risk floor increases;
- stronger isolated/multi-agent capability enables stronger independence evidence;
- W2-REV-01 records a BLOCKER/MAJOR against this contract or evidence.

## 18. Required independent critique and downstream work

`W2-REV-01` must attack at least fingerprint completeness, episode-vs-fingerprint separation, corpus representativeness/contamination, repeated-run sufficiency, correlation-metric blind spots, panel-independence claims, candidate threshold sensitivity/Goodhart risk, protected-slice semantics, and any accidental upgrade from qualification to universal judgment authority.

This mission provides `W2-EVAL-01_REVIEW_READY` evidence for `W2-REV-01` after terminal schema-3 status. It informs `IR-BLOCKER-EVIDENCE-FOUNDATION` but does not resolve it, select an evaluator, or authorize implementation readiness.

## Appendix A — exact reproducibility reference

```python
import hashlib, json, random

MARGIN = {"easy": 2.20, "medium": 1.20, "hard": 0.45}


def canonical_hash(obj):
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def build_corpus():
    cases = []
    difficulty = ("easy", "medium", "hard")
    for i in range(24):
        cases.append({
            "id": f"C{i+1:02d}",
            "label": 1 if i % 2 == 0 else 0,
            "difficulty": difficulty[(i // 2) % 3],
            "visibility": "PUBLIC" if i < 16 else "PROTECTED_SIMULATION",
        })
    return {"version": "W2-EVAL-CAL-v1", "cases": cases}


CORPUS = build_corpus()
CORPUS_HASH = canonical_hash(CORPUS)
assert CORPUS_HASH == "1028afb0a7cd27847c0aaed031a2008c4eefe5e092ae29e7eb01342323ef8683"


def fingerprint(family, model_version):
    manifest = {
        "provider_or_model_family": family,
        "model_version": model_version,
        "evaluator_code": "eval-fixture-v1",
        "rubric": "binary-calibration-rubric-v1",
        "prompt": "judge-binary-v1",
        "toolchain": "python-stdlib-reference",
        "policy_epoch": "eval-policy-v1",
        "calibration_corpus_sha256": CORPUS_HASH,
    }
    return canonical_hash(manifest)


assert fingerprint("fixture-family-A", "A-1.0") == "2093ab31a254179b0d89eaac50661c38ec9e6bc84f69cc9f8bc60c02d765db1d"
assert fingerprint("fixture-family-B", "B-1.0") == "4aa7fd37cc43a59ef1e50d94872fe60e6ff2ef7067faa8cb3515f95d7d1d7dee"
assert fingerprint("fixture-family-C", "C-1.0") == "f4a9a286e6d2c8e075fa045f65760ecfd3ef59b26b666cbc50798889ea34cc50"
assert fingerprint("fixture-family-A", "A-2.0") == "dfb69983a993ed75ac0a11006b508aeaa98b824142acf476bbca6c0194407691"

PROFILES = {
    "A1": ("A-v1", 1.00, 0.00, 0.85, "A1", 0.05),
    "A1-clone": ("A-v1", 1.00, 0.00, 0.85, "A1clone", 0.05),
    "A1-clone-2": ("A-v1", 1.00, 0.00, 0.85, "A1clone2", 0.05),
    "B1": ("B-v1", 1.00, -0.05, 0.95, "B1", 0.00),
    "C1": ("C-v1", 1.00, +0.05, 0.90, "C1", 0.00),
    "A2-model-drift": ("A-v2", 0.75, +0.55, 1.15, "A2", 0.00),
}


def seed(*parts):
    raw = "|".join(map(str, parts)).encode()
    return int(hashlib.sha256(raw).hexdigest()[:16], 16)


def gauss(*parts):
    return random.Random(seed(*parts)).gauss(0, 1)


def predict(profile_name, case, attempt):
    stream, scale, bias, sigma, eps_stream, eps_sigma = PROFILES[profile_name]
    sign = 1 if case["label"] == 1 else -1
    score = sign * MARGIN[case["difficulty"]] * scale + bias
    score += gauss(stream, case["id"], attempt) * sigma
    if eps_sigma:
        score += gauss(eps_stream, case["id"], attempt) * eps_sigma
    return int(score >= 0)


# Execute every profile over CORPUS["cases"] and attempt=0..19.
# Reported aggregate, paired-disagreement, correlation, and panel metrics derive from those judgments.
```

The appendix is disposable planning-experiment logic with no production dependency authority.
