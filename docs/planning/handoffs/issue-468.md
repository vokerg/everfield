# Issue #468 handoff — W2-ENG-PROVIDER-GHCR-INT-REC-01

## Recovery result

This episode reconstructs the already-reviewed GHCR Bearer-challenge remediation onto current `main` without semantic adaptation.

## Frozen authority / provenance

- recovery claim: Issue #468 comment `5309491676`;
- recovery base `main`: `acd37488b26dcb8dfcac434989ad42ddd85d1423`;
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- canonical binding: Issue #6 comment `5245368879`;
- owner convergence directive: Issue #84 comment `5277825639`;
- owner Unreal external-access-supplied directive: Issue #84 comment `5309426399`.

Reviewed source remediation:

- Issue #463 terminal comment `5309463811`;
- immutable source head `aa2e377eddf63bc03b31b70cbbc7f4a33efaf7c3`;
- reviewed validator blob `66696dd6a7d5b8a228aef0010cf64ffd233827bb`;
- frozen #463 handoff blob `7cdc02be1f74a5564029f0df532a6f9a6620ded5`.

Required review:

- Issue #466 terminal comment `5309484055`;
- disposition `PASS_BOUNDED_PROVIDER_GHCR_REMEDIATION`;
- findings 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR;
- review provenance squash-published as `acd37488b26dcb8dfcac434989ad42ddd85d1423`.

## Byte-equivalent recovery proof

At recovery start current `main` still contained the exact pre-remediation validator blob `b766b48149f43e3630a50aa4aba885b70db2fdff`. The intervening reviewed S6/review-provenance publications did not modify the validator.

Recovery uses Git object identity rather than rewriting reviewed source text:

- `tools/planning/engine_provider_effective_validator.py` is attached to this recovery tree using exact existing reviewed blob `66696dd6a7d5b8a228aef0010cf64ffd233827bb`;
- `docs/planning/handoffs/issue-463.md` is attached using exact frozen producer handoff blob `7cdc02be1f74a5564029f0df532a6f9a6620ded5`;
- this recovery handoff is the only newly authored recovery artifact.

No merge-conflict resolution, semantic adaptation, provider credential use, workflow change, or historical evidence mutation occurs in this episode.

## Verification / stopping rule

Before publication:

1. prove the recovery branch validator blob is exactly `66696dd6a7d5b8a228aef0010cf64ffd233827bb`;
2. prove the recovered #463 handoff blob is exactly `7cdc02be1f74a5564029f0df532a6f9a6620ded5`;
3. run only non-secret syntax and deterministic `--self-test` validation against the recovered validator;
4. verify the diff is limited to the validator, frozen #463 handoff, and this #468 handoff;
5. verify exact-head PR compatibility with then-current `main`;
6. squash-publish only under owner convergence authority.

A fresh trusted-main credentialed provider execution is mandatory after publication. This recovery itself does not establish provider PASS or Unreal empirical eligibility.

## Authority boundary

`NOT_CANONICAL`. Recovery/integration only. No provider credential/PASS, Unreal unlock, engine selection, implementation/readiness, commercial/production/legal/release, verification-PASS, decision, or canonical authority.