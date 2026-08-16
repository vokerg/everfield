# Issue #485 handoff — W2-ENG-PROVIDER-UNITY-AUTH-INT-REC-01

## Recovery result

This episode reconstructs the already-clean-reviewed Unity unattended service-account authentication remediation onto current `main` without semantic adaptation.

## Frozen source

- remediation Issue #481 terminal `5309611179`;
- immutable source head `6b5631ddfed6829dec2b09b73adb273480e7f17e`;
- exact reviewed validator blob `baa81dd97e656b0889b96d89a1bd45d62e33d9d1`;
- exact frozen #481 handoff blob `121f60aa78976021b9624b75b0ddcaac91e4fd10`;
- required review Issue #483 terminal `5309620494`;
- review disposition `PASS_BOUNDED_PROVIDER_UNITY_AUTH_REMEDIATION`, 0/0/0;
- review provenance is present on recovery base `main@0c08f0d8776ebff880bf1a7404348b65b28d8ebd`.

## Byte identity

Recovery attaches the exact reviewed Git objects rather than rewriting source:

- `tools/planning/engine_provider_effective_validator.py` -> `baa81dd97e656b0889b96d89a1bd45d62e33d9d1`;
- `docs/planning/handoffs/issue-481.md` -> `121f60aa78976021b9624b75b0ddcaac91e4fd10`;
- this #485 handoff is the only newly authored recovery artifact.

No merge-conflict resolution, semantic adaptation, credential use, workflow change or historical evidence mutation occurs.

## Required post-publication execution

After exact-head squash publication under owner convergence authority, trusted `main` must run validator `py_compile` + complete `--self-test` before provider Secrets, then one fresh credentialed provider evaluation and recorder episode. Only that fresh evidence may establish the next Unity stage.

Issue #480 remains the separate nonclaimable Unreal human Packages-token gate.

## Authority boundary

`NOT_CANONICAL`. Recovery/integration only. No provider credential/PASS, Unity license authority, engine selection, readiness, commercial/production/legal/release, verification-PASS, decision or canonical authority.