# Issue #512 — Unity license-exit review-finding revision handoff

## Identity

- Mission: `W2-ENG-PROVIDER-UNITY-LICENSE-EXIT-REM-02`
- Task class: `BLOCKING_REMEDIATION`
- Original claim: Issue #512 comment `5311584756`
- Stale recovery intent: `5312653077`
- Current recovery ownership generation: `5312654330`
- Branch: `planning/issue-512`
- Current main / merge base: `538b8a3b46b8b095bc43206d4a0ad4fdc151616a`
- Frozen reviewed producer head: `defa1fa6c2cc8dd39a84a864b34b36c47dbaa77b`
- Frozen reviewed validator blob: `e15c9df7eaab9f8a5a6cd96e945b93cbfdb29a7c`
- Frozen Issue #508 handoff blob carried byte-identically: `9f5c79a7259f9d82f18509f630429715e5807e2c`
- Required review source: Issue #510 terminal comment `5311555047`, disposition `CHANGES_NEEDED`
- Canonical binding: Issue #6 comment `5245368879`
- Canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- Canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- Canonicality: `NOT_CANONICAL`

## Reconstruction and correction fence

The revision was reconstructed from the exact frozen producer descendant of current `main`, without mutating Issue #508 / PR #509 or Issue #510 / PR #511. Revision commit `48765172871863e94971239a0f36c4231397872b` changes only `tools/planning/engine_provider_effective_validator.py` relative to the frozen producer head.

The corrected validator blob is exactly `69d45fa7bde9bd7879460ac661bac83228f113a6`.

The two required-review findings are mechanically closed:

- `W2-ENG-PROVIDER-UNITY-LICENSE-EXIT-REV-M01`: exit `3` now preserves authentication-or-authorization uncertainty in both stage and durable blocker via `LICENSE_STATUS_AUTHENTICATION_OR_AUTHORIZATION_FAILED` and `UNITY_SERVICE_ACCOUNT_AUTHENTICATION_OR_AUTHORIZATION_FAILED`.
- `W2-ENG-PROVIDER-UNITY-LICENSE-EXIT-REV-m02`: `validate_unity` now consumes the same pure `unity_license_status_decision(result, data)` function exercised by deterministic tests; there is no parallel test-only decision model.

Exit `4` remains configuration-required, exit `6` remains operation-failed, timeout/transient behavior remains fail-closed, and unknown nonzero remains process-failed. A structurally valid active envelope on any nonzero process result remains diagnostic-only and cannot authenticate, validate a license, or permit editor/native-S3 execution. Unreal/GHCR behavior and the historical 50 `NOT_RUN` cells are unchanged.

## Exact recovered verification

The stale continuation was recovered without changing validator bytes. The exact GitHub blob `69d45fa7bde9bd7879460ac661bac83228f113a6` was reconstructed in an executable environment from repository bytes and independently re-hashed using Git's blob identity formula before execution:

```text
reconstructed byte length: 49003
git blob sha: 69d45fa7bde9bd7879460ac661bac83228f113a6
expected blob sha: 69d45fa7bde9bd7879460ac661bac83228f113a6
IDENTITY: PASS
```

With `UNITY_SERVICE_ACCOUNT_ID`, `UNITY_SERVICE_ACCOUNT_SECRET`, `UNREAL_GITHUB_TOKEN`, and `UNREAL_GITHUB_USERNAME` explicitly absent, the mandated full-file commands then passed:

```text
python3 -m py_compile tools/planning/engine_provider_effective_validator.py
PASS

python3 tools/planning/engine_provider_effective_validator.py --self-test
PASS — 38/38 deterministic cases
```

The self-test PASS includes exit-0 active/inactive, exit `3`, exit `4` valid/invalid envelope, exit `6`, timeout, transient network, unknown nonzero, the aggregate invariant that no nonzero decision authenticates/licenses/proceeds, GHCR challenge hardening, and secret-free auth-trace assertions.

No provider credential was consumed. This is non-secret branch verification only; it is not provider validation and grants no provider authentication/PASS or license authority.

## Final path fence

The validator source blob remains exactly `69d45fa7bde9bd7879460ac661bac83228f113a6`. The carried Issue #508 handoff remains byte-identical at `9f5c79a7259f9d82f18509f630429715e5807e2c`. This handoff is the only post-verification branch artifact update and exists solely to replace the prior verification-gap record with exact PASS evidence.

Draft PR #514 targets current `main` and is the verification/review surface. No integration authority exists at this stage.

## Terminal disposition and required next gate

The bounded remediation is now `UNITY_LICENSE_EXIT_REVISION_READY_FOR_REVIEW` and may terminalize `REVIEW_READY` once the exact post-handoff branch/PR head and owned-path diff are rechecked.

Next gate: exactly one fresh independent or degraded-independent security/authority review of the corrected exact head. The reviewer must attack exit-3 auth-vs-authz uncertainty, production decision-path coverage, nonzero-valid-envelope false-PASS/editor risk, exit-4 preservation, secret isolation, Unreal/provider independence, historical evidence immutability, exact source reconstruction, and authority inflation. The reviewer must not repair this branch.

After a clean review and separately authorized squash-only publication, one fresh trusted-main pre-secret `py_compile` + full `--self-test` gate and a fresh credentialed evaluator/recorder episode remain mandatory.

## Authority boundary

`NOT_CANONICAL`. This handoff establishes only that the bounded source revision passed its required non-secret exact-blob verification. It grants no integration authority, provider authentication/PASS, Unity license authority, engine selection, implementation/readiness, verification-PASS, production/commercial/legal/platform/release authority, decision, content fan-in, or canonicalization authority.
