# Handoff — Issue #78 / W2-EVAL-01

## State

Producer work is complete on `planning/issue-78` and is ready to freeze as schema-3 `REVIEW_READY`. Required downstream authority remains `W2-REV-01`; this handoff does not self-review the mission into accepted/canonical evaluator policy.

## Exact ownership / base

- issue: `78`
- mission: `W2-EVAL-01`
- ownership claim comment: `5264286447`
- actor session: `w2-eval-01-agent-20260812-1027-01`
- branch base: `main@c7ba185ed9667b717794c19eaa0834ca41aa4c78`
- canonical Wave 1 foundations blob: `a252e3c93702f3ebaecd3e888944a23dbe1b0e1d`
- evidence report blob before this handoff commit: `50723345e6fffddebdbcd7bff1de6458b5989cf1`

## Completed

- Resolved the active Planning Program canonical binding and the terminal W1-CANON-01 Wave 2 activation from repository/GitHub state.
- Re-derived the live frontier rather than trusting issue-number ordering alone; skipped concurrent owner W2-CI-01 and claimed exactly W2-EVAL-01.
- Produced `docs/planning/wave-2/evidence/evaluator-drift-calibration.md` under the declared ownership surface.
- Defined an exact 24-case frozen synthetic calibration corpus, 20 attempts/case/configuration, and reproducible content-addressed corpus/fingerprint identities.
- Exercised missing-fingerprint authority, repeated distributions, same-fingerprint correlated panel episodes, cross-family comparison, backend/model drift, protected-slice semantics, and candidate reopen thresholds.
- Embedded the exact Python-standard-library reference constructor/runner in the report so corpus and fingerprint hashes are independently reproducible from repository state.

## Mechanical evidence / checks

Identity checks reproduced:

- corpus `W2-EVAL-CAL-v1`: `sha256:1028afb0a7cd27847c0aaed031a2008c4eefe5e092ae29e7eb01342323ef8683`
- A1 fingerprint: `2093ab31a254179b0d89eaac50661c38ec9e6bc84f69cc9f8bc60c02d765db1d`
- B1 fingerprint: `4aa7fd37cc43a59ef1e50d94872fe60e6ff2ef7067faa8cb3515f95d7d1d7dee`
- C1 fingerprint: `f4a9a286e6d2c8e075fa045f65760ecfd3ef59b26b666cbc50798889ea34cc50`
- A2-model-drift fingerprint: `dfb69983a993ed75ac0a11006b508aeaa98b824142acf476bbca6c0194407691`

Primary repeated-run metrics reproduced from the embedded algorithm:

- A1: 89.38% accuracy, 10.83% FPR, 10.42% FNR, 10.62% repeat instability.
- B1: 87.29% accuracy, 15.42% FPR, 10.00% FNR, 12.71% repeat instability.
- C1: 86.67% accuracy, 15.42% FPR, 11.25% FNR, 12.92% repeat instability.
- A2-model-drift: 75.42% accuracy, 39.17% FPR, 10.00% FNR, 21.67% repeat instability.

Correlation/drift evidence:

- same-fingerprint A1 episode error correlation: `0.8968–0.9333`; disagreement `1.25–1.88%`;
- different-family pair error correlation: `0.0895–0.1729`; disagreement `17.08–20.62%`;
- correlated three-call panel majority accuracy: `89.58%`, but one fingerprint/correlation group;
- diverse synthetic three-family panel majority accuracy: `93.54%`, but independence remains unproven;
- A1→A2-model-drift: accuracy `-13.96 pp`, FPR `+28.33 pp`, instability `+11.04 pp`, paired disagreement `27.71%`;
- protected-slice accuracy delta `-13.75 pp`, protected FPR delta `+25.00 pp`.

The model-drift case trips every material candidate guardrail relevant to accuracy/error rate, paired disagreement, stability, and protected-slice drift.

## Producer self-review

Initial self-review found one MAJOR-quality reproducibility defect before handoff: the first report revision published content hashes without retaining the exact canonical serialization inputs needed to recompute them. That revision was corrected on-branch before terminal status. The current report embeds exact corpus and fingerprint constructors and re-executes to the recorded identities/metrics.

Post-correction producer review result against the task contract:

- BLOCKER: `0`
- MAJOR: `0`
- MINOR: `2`
  - correlation is measured only with paired binary-error Pearson correlation and can miss shared systematic blind spots;
  - numerical `5 pp` / `10%` reopen thresholds are deliberately candidate policy, not validated universal risk thresholds.

Both minors are explicitly bounded in the report and routed to W2-REV-01.

## Known limitations / risks

- Synthetic calibration does not establish real evaluator quality or human alignment.
- Lower cross-family correlation in the fixture does not prove operational or epistemic independence.
- The protected slice is a result-shape simulation; no real secret/oracle control is tested.
- Corpus contamination/overfit detection, query-budget leakage, provider credential/control separation, and real mutable-backend fingerprint availability remain open.
- Producer-side evidence cannot substitute for required independent/degraded-independent W2-REV-01 judgment.

## Remaining / next action

1. Publish owner `STATUS(REVIEW_READY)` bound to the exact final branch head after this handoff commit.
2. Close Issue #78 as producer-complete only after that status exists; issue closure is not review/canonical authority.
3. W2-REV-01 must review the exact W2-EVAL-01 work SHA together with the other Wave 2 evidence missions.
4. If W2-REV-01 finds BLOCKER/MAJOR defects, use bounded remediation/revision rather than silently editing the reviewed work state.
5. Do not treat this mission as evaluator selection, universal judgment authority, or implementation-readiness evidence by itself.

## Integration rule

No producer self-review or PR substitutes for W2-REV-01. Any eventual `main` integration remains squash-only and must preserve the reviewed authority level rather than silently canonicalizing evaluator policy.
