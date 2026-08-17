# Issue #512 — Unity license-exit review-finding revision handoff

## Identity

- Mission: `W2-ENG-PROVIDER-UNITY-LICENSE-EXIT-REM-02`
- Task class: `BLOCKING_REMEDIATION`
- Claim: Issue #512 comment `5311584756`
- Branch: `planning/issue-512`
- Current main / merge base: `538b8a3b46b8b095bc43206d4a0ad4fdc151616a`
- Frozen reviewed producer head: `defa1fa6c2cc8dd39a84a864b34b36c47dbaa77b`
- Frozen reviewed validator blob: `e15c9df7eaab9f8a5a6cd96e945b93cbfdb29a7c`
- Frozen Issue #508 handoff blob carried byte-identically: `9f5c79a7259f9d82f18509f630429715e5807e2c`
- Required review source: Issue #510 terminal comment `5311555047`
- Canonical binding: Issue #6 comment `5245368879`
- Canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- Canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- Canonicality: `NOT_CANONICAL`

## Reconstruction fence

Immediately before claim and branch creation, current `main` remained `538b8a3b46b8b095bc43206d4a0ad4fdc151616a`. GitHub compare showed the frozen producer head `defa1fa6c2cc8dd39a84a864b34b36c47dbaa77b` was exactly three commits ahead, zero behind, with merge base equal to current main. The fresh revision branch was therefore created at that immutable descendant to carry the exact reviewed producer bytes without mutating `planning/issue-508` or PR #509.

The carried Issue #508 handoff still has exact blob `9f5c79a7259f9d82f18509f630429715e5807e2c`.

## Corrections applied

Revision commit `48765172871863e94971239a0f36c4231397872b` changes only `tools/planning/engine_provider_effective_validator.py` relative to frozen producer head `defa1fa6...`.

### Review finding `W2-ENG-PROVIDER-UNITY-LICENSE-EXIT-REV-M01`

Exit `3` now preserves Unity's bounded authentication-or-authorization uncertainty in both durable fields:

- stage: `LICENSE_STATUS_AUTHENTICATION_OR_AUTHORIZATION_FAILED`;
- blocker: `UNITY_SERVICE_ACCOUNT_AUTHENTICATION_OR_AUTHORIZATION_FAILED`.

No attempt is made to infer authentication versus authorization without stronger evidence.

### Review finding `W2-ENG-PROVIDER-UNITY-LICENSE-EXIT-REV-m02`

The production path now uses a single pure `unity_license_status_decision(result, data)` evaluator. `validate_unity` consumes that decision directly for:

- structured-envelope validity;
- authentication validation;
- bounded authentication stage;
- license validation;
- bounded state/blocker;
- the sole `proceed_to_editor` decision.

Deterministic self-test cases exercise that same production decision function for:

- exit `0` + active envelope;
- exit `0` + inactive envelope;
- exit `3`;
- exit `4` + valid active envelope;
- exit `4` + invalid envelope;
- exit `6`;
- timeout;
- transient-network signature;
- unknown nonzero exit;
- an aggregate invariant that every nonzero decision keeps authentication false, license false, and `proceed_to_editor=false`.

The pre-existing envelope ambiguity tests remain intact.

## Preserved behavior / authority

- exit `4` remains prospectively `LICENSE_STATUS_CONFIGURATION_REQUIRED` / `UNITY_LICENSE_STATUS_CONFIGURATION_REQUIRED`;
- exit `6`, transient, and unknown nonzero cases remain fail-closed;
- a valid `data.active=true` envelope on any nonzero result remains diagnostic-only;
- exact Unity baseline `6000.5.6f1`, editor install/discovery/native-S3 behavior, service-account environment transport, and redaction remain unchanged outside the shared decision extraction;
- GitHub diff from frozen producer head shows no Unreal/GHCR changes; the embedded Unreal Python remains `if perturb and tick == 137:`;
- historical evaluator run `31988648526` evidence is untouched and retains the labels originally recorded;
- no provider credential was consumed on this branch;
- no provider PASS, license, engine-selection, readiness, verification-PASS, production/commercial/legal/release, decision, integration, or canonical authority is created.

## Verification performed

A non-secret local semantic probe reconstructed from the exact changed decision logic passed all required combinations. It confirmed:

- exit `0` active authenticates, validates the license, and alone may proceed;
- exit `0` inactive authenticates but remains license-blocked and cannot proceed;
- exit `3` returns the auth-or-authorization blocker with auth/license false;
- exit `4` with valid or invalid envelope returns configuration-required with auth/license false;
- exit `6` remains operation-failed;
- timeout/transient remain transient-failure;
- unknown nonzero remains generic process-failed;
- no nonzero case authenticates, validates a license, or proceeds to editor/native-S3.

The changed function snippet parsed successfully with Python `ast.parse`.

GitHub compare from frozen producer head `defa1fa6...` to revision commit `4876517...` reports exactly one changed file, the validator, with the expected blocker correction, pure decision extraction/wiring, and decision-level deterministic tests. No unrelated source drift was observed.

## Verification gap / terminal consequence

The execution environment for this task exposes repository bytes through the GitHub connector but does not provide an executable checkout. Direct container access to GitHub is unavailable because DNS/network access is disabled. Therefore the mandated **exact full-file** commands below could not be independently executed against blob `69d45fa7bde9bd7879460ac661bac83228f113a6`:

```text
python3 -m py_compile tools/planning/engine_provider_effective_validator.py
python3 tools/planning/engine_provider_effective_validator.py --self-test
```

The frozen predecessor's exact full-file verification remains provenance only; it is not substituted for verification of this revised blob. Accordingly this task must terminalize as `CHANGES_STILL_REQUIRED`, not `UNITY_LICENSE_EXIT_REVISION_READY_FOR_REVIEW`.

## Required next gate

Do not integrate this revision. The next eligible continuation is bounded **verification** of exact validator blob `69d45fa7bde9bd7879460ac661bac83228f113a6` from an executable checkout/environment:

1. run exact full-file `py_compile`;
2. run full deterministic `--self-test` and confirm all cases PASS (expected case count remains 38);
3. confirm the exact branch/PR head and changed-path fence;
4. if verification passes, update/route the chain to fresh required independent/degraded-independent security/authority review without altering the verified source blob;
5. if verification fails, route bounded remediation of the exact failure.

No provider credentials are required or authorized for that verification.

## Authority boundary

`NOT_CANONICAL`. This handoff records a bounded source revision with semantic-probe PASS but incomplete exact-full-file verification. It grants no integration authority, provider authentication/PASS, Unity license authority, engine selection, implementation/readiness, verification-PASS, production/commercial/legal/platform/release authority, decision, content fan-in, or canonicalization authority.
