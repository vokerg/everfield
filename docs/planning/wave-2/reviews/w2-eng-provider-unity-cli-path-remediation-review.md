# W2-ENG provider Unity CLI path remediation review

## Review identity

- Issue #491 / `W2-ENG-PROVIDER-UNITY-CLI-PATH-REM-REV-01`
- trust mode: `DEGRADED_SINGLE_AGENT`
- claim `5309649082`
- judged Issue #489 claim `5309642489`, terminal `5309647639`
- judged implementation `9d5350f9e13ff51dfd6c73de4ab26be22b084e76`
- judged workflow blob `94b740e1b9ca25fc6c23b767d681cc21a497cfac`
- judged head `2545d823b3a9fbcb4a184d8b726b380f90c1c0cf`
- judged draft PR #490
- base `eb30f078fe6ff4f27a54998163b66ebd22d9c84d`

## Disposition

`PASS_BOUNDED_PROVIDER_UNITY_CLI_PATH_REMEDIATION`

Findings: 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR.

## Adversarial result

1. Scope is exactly the credentialed evaluator workflow plus producer handoff; validator/provider semantics are unchanged.
2. The install step still runs before any provider secret expression is introduced. It has no `${{ secrets.* }}` binding.
3. The previously assumed `$HOME/.unity/bin/unity` publication is removed. `command -v unity` supplies the executable actually usable by the shell after the pinned installer and PATH setup.
4. Empty discovery and non-executable discovery fail closed with `test -n` / `test -x`.
5. `readlink -f` canonicalizes the discovered path; empty/non-executable canonical output fails closed again.
6. Exact version `1.0.0-beta.5` is checked by invoking the exact canonical path later written to `GITHUB_ENV`.
7. The resolved path is not derived from PR/user input. The job is restricted to trusted repository `main`, exact event SHA, GitHub-hosted runner state and the existing Unity installer path. Under that trust model, path/newline injection is not a new user-controlled surface. Any resolution/version anomaly terminates before secrets.
8. Trusted-main checkout, `contents: read`, `engine-eval`, pre-secret validator `py_compile`/full self-test, later secret-bearing validation, evidence sanitization and artifact boundaries remain in the same order and materially unchanged.
9. A successful path check is not provider authentication, license validation or provider PASS. Fresh trusted-main execution remains mandatory.

The existing remote Unity installer supply-chain boundary is not broadened by this remediation; this review does not grant it additional authority or treat version output alone as provider evidence.

## Required next route

Publish this review provenance only under separate convergence authority. Publish exact reviewed #489 bytes onto then-current main directly if compatible, otherwise via byte-identical recovery. Then inspect one fresh trusted-main evaluator/recorder episode. Route only the exact next Unity stage observed.

## Authority boundary

`NOT_CANONICAL`. No provider credential/PASS, Unity license authority, engine selection, readiness, release, verification-PASS, decision, integration-by-review or canonical authority.