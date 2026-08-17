# W2-ENG provider Unity license-exit remediation review

## Review identity

- Review mission: `W2-ENG-PROVIDER-UNITY-LICENSE-EXIT-REV-01`
- Review task: Issue #510
- Review claim: Issue #510 comment `5311536139`
- Trust mode: `DEGRADED_SINGLE_AGENT`
- Producer session excluded: `frontier-drain-provider-unity-license-exit-rem-gpt56sol-20260817-01`
- Judged producer task: Issue #508
- Judged producer terminal status: `5311500674`
- Judged PR: #509, draft
- Frozen base: `538b8a3b46b8b095bc43206d4a0ad4fdc151616a`
- Frozen head: `defa1fa6c2cc8dd39a84a864b34b36c47dbaa77b`
- Frozen validator blob: `e15c9df7eaab9f8a5a6cd96e945b93cbfdb29a7c`
- Frozen handoff blob: `9f5c79a7259f9d82f18509f630429715e5807e2c`
- Base validator blob: `112e8140a145fdf80556414358dbdd524416f9fa`
- Canonicality: `NOT_CANONICAL`

## Disposition

`CHANGES_NEEDED`

Finding count:

- BLOCKER: 0
- MAJOR: 1
- correction-requiring MINOR: 1

The exit-4 correction itself is fail-closed and materially fixes the fresh evidence misclassification, but the candidate does not satisfy the full bounded diagnostic contract required for review PASS.

## Frozen candidate / scope fence

At claim and review time PR #509 was open, draft, mergeable, based on `main@538b8a3b46b8b095bc43206d4a0ad4fdc151616a`, and headed by `defa1fa6c2cc8dd39a84a864b34b36c47dbaa77b`.

Changed paths are exactly:

1. `tools/planning/engine_provider_effective_validator.py`
2. `docs/planning/handoffs/issue-508.md`

The validator diff against base is limited to:

- one bounded Unity `license status` process-failure classifier;
- wiring that classifier into the nonzero process path;
- deterministic cases intended to exercise the new classes.

The previously recorded accidental embedded Unreal Python `and` → `&&` transcription is absent from the frozen candidate; the final `UNREAL_NATIVE_SCRIPT` contains `if perturb and tick == 137:`. No Unreal/GHCR logic appears in the PR diff.

## External semantic fence

The current official Unity CLI reference defines the relevant exit classes as:

- `3`: authentication **or authorization** failure;
- `4`: configuration required;
- `6`: the command's primary operation failed.

The reference also states that installed-version `unity --help` is authoritative for the installed command surface. The review therefore treats these published classes as bounded diagnostic categories only; documentation does not establish provider authentication, an active license, or provider PASS.

## Positive security / authority checks

### Exit 4 is now fail-closed and no longer labelled authentication failure

For a failed `license status` process with exit `4`, the candidate emits:

- state `BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION`;
- stage `LICENSE_STATUS_CONFIGURATION_REQUIRED`;
- blocker `UNITY_LICENSE_STATUS_CONFIGURATION_REQUIRED`.

The candidate computes `authentication_validated = ok(license_status) and envelope_valid`; therefore exit `4` cannot authenticate even if `data.active` is structurally valid. The nonzero branch returns before `license_validated` is derived or editor/native-S3 execution can begin.

A reviewer semantic probe reproducing the exact fetched classifier/gate logic confirmed:

- exit `4` + valid `{"data":{"active":true}}` envelope → auth false, license false, configuration-required blocker;
- exit `4` + invalid envelope → auth false, license false, same configuration-required blocker;
- exit `6` + valid envelope → auth false, license false, operation-failed blocker;
- unknown nonzero + valid envelope → auth false, license false, generic process-failed blocker;
- exit `0` + active true → authenticated command and license true;
- exit `0` + active false → authenticated command but license false / blocked.

Thus a nonzero structured envelope is diagnostic-only in the actual candidate wiring.

### Structured-envelope ambiguity remains fail-closed

`unity_license_status_envelope` still rejects:

- a top-level `active` marker;
- missing `data.active`;
- non-boolean `data.active`.

The prior conflicting-marker guard is preserved.

### Secret isolation and bounded evidence are preserved

The remediation does not change credential transport or redaction. Unity service-account values remain environment-only and the failure path copies only bounded process metadata (`exit`, `timed_out`, `seconds`), the envelope-valid boolean, bounded stage/blocker enums, and existing booleans into provider evidence. No raw stderr/stdout, account ID/secret, bearer/session token, cookie, authorization value, or secret hash is added to emitted evidence.

### Historical evidence remains immutable

The already-published evidence blob `c17c9771a37ed1d8706f27dfef13db8754b5a50a` for evaluator run `31988648526` remains unchanged on `main` and still records its original blocker `UNITY_SERVICE_ACCOUNT_AUTHENTICATION_FAILED` with Unity exit `4`. PR #509 does not touch that evidence path. Corrected classification is therefore prospective only.

### Trusted-main pre-secret gate remains intact

The trusted evaluator workflow remains outside the PR diff and still performs `py_compile` plus the validator's full `--self-test` before the credential-bearing validation step. No provider credential was consumed by this review branch.

### Authority boundary remains bounded

Neither candidate code nor handoff grants provider authentication/PASS, Unity license authority, engine selection, implementation/readiness, verification-PASS, production/commercial/legal/release authority, decision authority, integration-by-review, or canonicality.

## Findings

### W2-ENG-PROVIDER-UNITY-LICENSE-EXIT-REV-M01 — MAJOR — exit 3 durable blocker narrows an auth-or-authorization result to authentication-only

**Observed candidate behavior**

`unity_license_status_failure` handles exit `3` with:

- stage: `LICENSE_STATUS_AUTHENTICATION_OR_AUTHORIZATION_FAILED`;
- blocker: `UNITY_SERVICE_ACCOUNT_AUTHENTICATION_FAILED`.

The added regression test hard-codes the same pair.

**Why this is material**

Unity's bounded exit-code contract says code `3` is authentication **or authorization** failure. The stage preserves that uncertainty, but the durable blocker enum discards it and positively claims authentication failure. The blocker is a routing/diagnostic field, so downstream automation or an operator can be directed toward credential replacement when the actual condition is authorization/entitlement. That reproduces the exact class of over-attribution this remediation chain is intended to remove.

This fails review attack 4 and the producer contract requiring exit `3` to remain an exact authentication/authorization classification.

**Required correction**

Use a blocker enum that preserves the documented disjunction, for example a bounded `UNITY_SERVICE_ACCOUNT_AUTHENTICATION_OR_AUTHORIZATION_FAILED`, and update deterministic tests/handoff wording accordingly. Do not infer which side of the disjunction occurred without stronger evidence.

### W2-ENG-PROVIDER-UNITY-LICENSE-EXIT-REV-m02 — correction-requiring MINOR — new nonzero/envelope tests do not exercise the `validate_unity` integration path

**Observed candidate tests**

The new exit-4-valid-envelope case evaluates `active_ok` independently and then tests only `unity_license_status_failure(exit4)`. The `unity_license_nonzero_never_authenticates_or_licenses` case evaluates `not (ok(result) and active_ok and active_value is True)` over synthetic process dictionaries.

Neither test invokes `validate_unity` with a stubbed `license status` result containing the corresponding JSON envelope. Consequently these cases do not verify that the real wiring returns before license/editor execution or that the final provider output keeps `authentication_validated=false` and `license_validated=false`.

**Why correction is required**

The source currently wires the gate correctly, and the reviewer semantic probe confirmed the intended behavior. But the producer task explicitly required deterministic self-tests for exit `4` with valid/invalid envelopes and proof that no nonzero case creates provider/license PASS. The current tests prove component predicates, not that integration invariant; a future wiring regression could satisfy the added tests.

**Required correction**

Add deterministic integration-level tests that drive `validate_unity` (or an extracted pure Unity license-status evaluator used by `validate_unity`) with synthetic exit/envelope combinations and assert the final provider state/booleans. At minimum cover exit `3`, exit `4` + valid active envelope, exit `4` + invalid envelope, exit `6`, timeout/transient, unknown nonzero, and exit `0` active/inactive controls. No provider credentials or network calls should be needed.

## Verification note

The producer handoff records exact-blob `py_compile` PASS and full `--self-test` PASS (38/38). In the reviewer environment the repository is available through the GitHub connector rather than as an executable checkout, so the exact full candidate file could not be independently materialized for a second full-script invocation. That producer result is retained as provenance but is not used to waive finding `m02`. The reviewer instead executed a non-secret semantic probe from the exact fetched candidate snippets and performed static review of the frozen PR patch. A corrected candidate's fresh review must independently execute the exact frozen blob's `py_compile` and full deterministic self-test before PASS.

## Required next state

Do not integrate PR #509. Route one bounded remediation/revision that changes only the judged validator and required handoff/provenance:

1. preserve auth-or-authorization uncertainty in the exit-3 blocker;
2. add integration-level deterministic nonzero/envelope tests;
3. preserve the already-correct exit-4 fail-closed classification, secret isolation, historical evidence immutability, Unreal/provider independence, and all authority boundaries;
4. route a fresh required review of the corrected exact head.

No provider credentialed execution is required or authorized for the remediation/review branch. Only after a clean reviewed squash-only publication may a fresh trusted-main evaluator/recorder episode consume credentials, after its pre-secret syntax/full-self-test gate.
