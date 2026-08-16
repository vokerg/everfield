# Issue #476 handoff — W2-ENG-PROVIDER-GHCR-DIAG-INT-REC-01

## Recovery result

This episode reconstructs the already-clean-reviewed GHCR authentication-stage diagnostic candidate onto current `main` without semantic adaptation.

## Frozen authority / provenance

- recovery claim: Issue #476 comment `5309568362`;
- recovery base `main`: `5f89fcb2d900e82c6909983eaf5be54b0a6d70b8`;
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- canonical binding: Issue #6 comment `5245368879`;
- owner convergence directive: Issue #84 comment `5277825639`;
- owner Unreal external-access-supplied directive: Issue #84 comment `5309426399`.

Reviewed diagnostic source:

- Issue #472 terminal `5309544191`;
- immutable source head `fdfb75cf826594e2f320c75d9a9d3f90ac34d500`;
- exact reviewed validator blob `38ce3f46d4db05d7d0ca1bd7a1d3f2942465e1fd`;
- exact frozen #472 handoff blob `ceed314d0191d8ec74b06bd0da72319e8e90852d`.

Required review:

- Issue #474 winning claim `5309548763`;
- terminal review `5309559748`;
- disposition `PASS_BOUNDED_PROVIDER_GHCR_DIAGNOSTICS`;
- findings 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR;
- review provenance squash-published as current `main@5f89fcb2d900e82c6909983eaf5be54b0a6d70b8`.

## Byte-equivalent recovery proof

Recovery reuses Git object identity rather than rewriting reviewed source:

- `tools/planning/engine_provider_effective_validator.py` uses exact blob `38ce3f46d4db05d7d0ca1bd7a1d3f2942465e1fd`;
- `docs/planning/handoffs/issue-472.md` uses exact blob `ceed314d0191d8ec74b06bd0da72319e8e90852d`;
- this #476 handoff is the only newly authored recovery artifact.

The intervening current-main change is required-review provenance only and does not edit the validator. No merge-conflict resolution, semantic adaptation, credential use, workflow change, or historical evidence mutation occurs.

## Required publication / execution route

1. Verify exact blob identities and diff scope.
2. Open exact-head current-main draft PR.
3. Squash-publish under owner convergence authority if still mergeable.
4. Let the trusted-main evaluator execute `py_compile` + full validator `--self-test` before provider Secrets are injected.
5. If that gate passes, let the same run perform one fresh credentialed evaluation.
6. Preserve recorder evidence and inspect only sanitized `registry_auth_trace` facts.
7. Route exact next action from fresh `failure_stage`; do not infer owner/PAT/Epic action before that evidence.

## Authority boundary

`NOT_CANONICAL`. Recovery/integration only. No provider credential/PASS, Unreal empirical eligibility, engine selection, implementation/readiness, commercial/production/legal/release, verification-PASS, decision, or canonical authority.