# W2-ENG provider Unity auth remediation review

## Review identity

- mission: `W2-ENG-PROVIDER-UNITY-AUTH-REM-REV-01`
- review Issue: #483
- trust mode: `DEGRADED_SINGLE_AGENT`
- winning claim: `5309613097`
- producer session excluded: `frontier-drain-provider-unity-auth-rem-gpt56sol-20260816-01`
- judged remediation Issue: #481
- judged claim: `5309597573`
- judged terminal: `5309611179`
- implementation SHA: `be3a73bf5f2e3aed0234e10cc3e87352b169187c`
- validator blob: `baa81dd97e656b0889b96d89a1bd45d62e33d9d1`
- exact immutable judged head: `6b5631ddfed6829dec2b09b73adb273480e7f17e`
- judged draft PR: #482
- judged/current-main base: `772b753d64be559abd9c2f71a3fc8119885f34c1`
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical binding: Issue #6 comment `5245368879`

The producer branch/PR were treated as immutable. No provider credential was consumed by review.

## Disposition

`PASS_BOUNDED_PROVIDER_UNITY_AUTH_REMEDIATION`

Findings:

- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0

The exact candidate is clean for separately authorized noncanonical publication followed by one mandatory fresh trusted-main evaluator run. This review does **not** establish Unity authentication success, license validity, provider PASS, engine selection, implementation/readiness, commercial/production/legal/release authority, verification-PASS, decision authority, integration authority by review alone, or canonicality.

## Triggering evidence

The latest pre-remediation trusted-main provider run `31971342813` / job `95224169239` passed validator syntax/full self-test before secrets, then Unity failed at authentication with `UNITY_SERVICE_ACCOUNT_AUTHENTICATION_FAILED` and repeated auth subprocess exit `127`. License status, editor install and native S3 were therefore not reached.

The historical failure remains pre-remediation evidence and is not reclassified as a licensing result.

## Adversarial review

### 1. Frozen identity / scope — PASS

PR #482 binds exact judged head `6b5631ddfed6829dec2b09b73adb273480e7f17e` to exact base `772b753d64be559abd9c2f71a3fc8119885f34c1` and was mergeable at review claim. Changed paths are exactly:

- `tools/planning/engine_provider_effective_validator.py`;
- `docs/planning/handoffs/issue-481.md`.

The executable diff is confined to Unity authentication/environment handling and deterministic self-tests. Unreal/GHCR code is not changed.

### 2. Credential transport — PASS

The pre-remediation auth command placed the service-account ID in argv and supplied the secret on stdin through undocumented auth flags. The candidate removes both paths.

For Unity authentication, command argv is now exactly the executable plus `auth login` / `auth status`; the service-account values exist only in the subprocess environment returned by `unity_service_account_env()`. `input_text` is no longer used for Unity auth.

Existing `run()` sanitization still redacts exact configured secret values from captured stdout/stderr before any process evidence is emitted. The candidate records process exit/timing and bounded auth-state fields only.

### 3. Documented unattended service-account boundary — PASS

The candidate uses the Unity CLI service-account variables `UNITY_SERVICE_ACCOUNT_ID` and `UNITY_SERVICE_ACCOUNT_SECRET` and supplies automation controls through environment rather than custom secret-bearing auth flags. `UNITY_NON_INTERACTIVE=1` prevents accepting an interactive browser flow as CI evidence; structured output is requested through `UNITY_FORMAT=json` and banner suppression through `UNITY_NO_BANNER=1`.

The review finds no command-line fallback that would accept interactive/OAuth success in the credentialed CI path.

### 4. Explicit auth-state parser — PASS

`unity_auth_status_authenticated()` is fail-closed relative to the predecessor's `bool(nonempty_json)` behavior.

It accepts only explicit positive boolean markers (`authenticated`, `loggedIn`, `signedIn` and normalized `is*` variants) or bounded positive status/state strings. It rejects:

- nonempty JSON with no recognized auth state;
- explicit false markers;
- explicit negative status/state strings;
- any tree containing both positive and negative recognized markers.

The recursive traversal cannot turn an arbitrary string/user object into authenticated state. A stricter-than-necessary parser may create a future false negative, but cannot create false provider authority; fresh trusted-main execution is the required compatibility proof.

### 5. Process success cannot be overridden by parser — PASS

`authentication_validated` requires all three conditions:

- `auth login` process success;
- `auth status` process success;
- explicit positive structured status.

A positive parser result cannot override a failed login/status process. Failure stage remains bounded (`LOGIN_PROCESS_FAILED`, `STATUS_PROCESS_FAILED`, `STATUS_NOT_EXPLICITLY_AUTHENTICATED`).

### 6. Authentication remains separate from licensing — PASS

Only after `authentication_validated=true` does the candidate invoke `unity license status`. `license_validated` remains a separate field and provider state cannot become `VALIDATED_DEVELOPMENT_ACCESS` from auth alone.

The existing license-active predicate remains unchanged: structured license data must explicitly report `data.active is true`.

Therefore this remediation cannot convert service-account login success into a license, commercial, production, release or provider PASS claim.

### 7. Environment propagation to later Unity CLI commands — PASS

The same service-account/non-interactive structured environment is supplied to license status, editor install and installed-editor listing. This does not put credentials into argv/stdin and preserves the intended unattended session across subprocesses.

Exact Unity editor baseline remains `6000.5.6f1`; editor discovery and native S3 implementation are unchanged. Removal of repeated CLI `--non-interactive`/`--format json` flags from these commands is compensated by the corresponding global environment controls and does not relax provider authority gates.

### 8. Unreal / provider independence — PASS

The patch does not change GHCR challenge/token diagnostics, Unreal provider execution, `derive_frontier()`, independent provider unlock semantics, historical 50 `NOT_RUN` preservation, or commercial/production/legal/release/engine-selection flags.

Issue #480 remains the exact nonclaimable Unreal human credential gate and is unaffected.

### 9. Deterministic test coverage — PASS FOR BOUNDED PUBLICATION

The candidate adds pure deterministic cases for explicit positive auth forms, explicit false, arbitrary nonempty JSON, conflicting positive/negative markers and exact service-account environment construction. Existing GHCR and independent-provider tests remain in the file.

Producer honestly recorded full-branch `py_compile` / complete `--self-test` as NOT_RUN in the task environment. This review does not rewrite those fields as executed PASS.

Exact patch inspection shows coherent Python structure and consistent helper/call signatures. More importantly, the trusted-main credentialed evaluator still performs `python3 -m py_compile` and the full validator `--self-test` **before** the later step that injects provider Secrets. A latent syntax/self-test defect therefore fails before credential consumption or generated provider evidence.

This closes the producer execution limitation for bounded publication. The first post-publication trusted-main run remains mandatory executable confirmation.

## Functional uncertainty is fail-closed, not a review finding

The exact structured shape returned by the current Unity CLI service-account `auth status` path is intentionally not assumed from prose. If the CLI's real structured status lacks one of the recognized explicit markers, the candidate will remain blocked at `STATUS_NOT_EXPLICITLY_AUTHENTICATED`; it will not false-pass. Such a fresh observed mismatch would justify a narrowly evidenced parser adaptation and fresh review, not invalidate the security correction made here.

Likewise, if authentication succeeds and `unity license status` exposes a later exact licensing condition, that is a new downstream gate and must be routed separately.

## Required next route

1. Open exact-head draft review PR and terminalize this review.
2. Publish review provenance under separate owner-convergence authority.
3. Publish exact reviewed #481 candidate onto then-current `main` if current-main compatible; otherwise use byte-equivalent recovery without semantic drift.
4. Let trusted-main `py_compile` + full self-test execute before provider Secrets.
5. Obtain one fresh credentialed provider run and matching recorder evidence.
6. Route only the exact fresh Unity stage: auth parser/process, license, editor install, or native S3 as observed.

## Authority boundary

`NOT_CANONICAL`. Required security/authority review only. No provider credential/PASS, Unity license authority, engine selection, implementation/readiness, commercial/production/legal/release, verification-PASS, decision, integration-by-review, or canonical authority.