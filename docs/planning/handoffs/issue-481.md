# Issue #481 handoff — W2-ENG-PROVIDER-UNITY-AUTH-REM-01

## State

Unity authentication remediation candidate is ready for one fresh required security/authority review.

## Exact authority / provenance

- claim: Issue #481 comment `5309597573`;
- branch: `planning/issue-481`;
- base/current main at claim: `772b753d64be559abd9c2f71a3fc8119885f34c1`;
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- canonical binding: Issue #6 comment `5245368879`;
- owner convergence directive: Issue #84 comment `5277825639`;
- owner Unity-proceeds directive: Unity portion of Issue #84 comment `5307397331`;
- independent Unreal human gate: Issue #480.

## Triggering trusted-main evidence

Latest trusted-main evaluator run `31971342813`, job `95224169239`, source `main@772b753d64be559abd9c2f71a3fc8119885f34c1` passed the pre-secret validator syntax/full self-test gate but still returned Unity `BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION` / `UNITY_SERVICE_ACCOUNT_AUTHENTICATION_FAILED`, with the repeated auth subprocess exit `127` before any license/editor/native-S3 validation.

The pre-remediation validator invoked Unity CLI auth as:

`unity auth login --client-id <service-account-id> --secret-from-stdin --non-interactive --format json`

and supplied the secret on stdin.

## External command-contract basis

Current official Unity CLI release notes state that service-account authentication was added with automatic bearer-token generation when `UNITY_SERVICE_ACCOUNT_ID` and `UNITY_SERVICE_ACCOUNT_SECRET` are set, specifically for unattended CI/automation. The current Unity CLI reference documents `unity auth login`, `unity auth status`, and `unity auth logout`; it does not document the validator's `--client-id` / `--secret-from-stdin` auth flags. Unity CLI also documents environment controls for non-interactive/structured automation.

This remediation therefore treats the observed pre-license exit `127` as an invocation defect until a fresh trusted-main run proves a different exact blocker. It does not infer a licensing conclusion.

## Candidate implementation

Implementation commit `be3a73bf5f2e3aed0234e10cc3e87352b169187c`.

Candidate validator blob `baa81dd97e656b0889b96d89a1bd45d62e33d9d1`.

The candidate:

- removes Unity service-account ID/secret from auth command argv and removes secret stdin;
- constructs a bounded service-account environment containing `UNITY_SERVICE_ACCOUNT_ID`, `UNITY_SERVICE_ACCOUNT_SECRET`, `UNITY_NON_INTERACTIVE=1`, `UNITY_FORMAT=json`, and `UNITY_NO_BANNER=1`;
- invokes only `unity auth login` followed by `unity auth status` through that environment path;
- requires both commands to succeed **and** requires an explicit positive structured auth marker before setting `authentication_validated=true`;
- rejects arbitrary nonempty JSON, explicit false auth state, and conflicting positive/negative auth markers;
- records only process exit/timing, an auth-stage enum and a bounded explicit-positive boolean;
- keeps authentication distinct from license status: only authenticated sessions proceed to `unity license status`;
- reuses the same non-interactive structured environment for license/editor-install/list commands so service-account auth remains environment-bound and credentials never enter argv/stdin;
- keeps exact Unity baseline `6000.5.6f1`, editor discovery and native S3 behavior unchanged;
- does not modify Unreal/GHCR decision or diagnostic semantics.

## Deterministic test additions

The validator self-test now includes pure no-network/no-secret cases for:

- explicit `loggedIn=true` accepted;
- explicit `authenticated=true` accepted;
- positive status string accepted;
- explicit false rejected;
- arbitrary nonempty JSON rejected;
- conflicting positive/negative markers rejected;
- exact unattended service-account environment construction.

Existing GHCR diagnostic/challenge tests, independent-provider unlock tests, redaction tests and historical 50 `NOT_RUN` preservation remain present.

## Verification limitation

The exact branch diff before this handoff was one owned validator file, 102 additions / 8 deletions, one commit ahead of exact base.

Full branch `py_compile` and full validator `--self-test` were not executed from this task branch in the available tool environment. This is not promoted to PASS. The trusted-main evaluator retains its fail-closed pre-secret gate that executes `py_compile` and the full deterministic validator self-test before the later credential-bearing validation step. Fresh review must attack source coherence and whether that pre-secret gate is sufficient for bounded publication.

No Unity credential was consumed from the task branch and no branch-side provider execution occurred.

## Required fresh review

Review the exact frozen candidate only. Attack at least:

1. whether service-account credentials can enter argv/stdin/log/evidence despite the refactor;
2. whether the environment path matches the documented unattended Unity CLI contract;
3. whether non-interactive mode prevents browser/OAuth fallback;
4. whether auth-state parsing can false-positive on arbitrary/explicit-false/conflicting JSON;
5. whether auth command/status failure classification remains fail closed;
6. whether successful auth still cannot imply license/provider PASS;
7. whether license/editor/native-S3 semantics remain materially unchanged;
8. whether Unreal/GHCR and independent provider semantics are unchanged;
9. whether syntax/self-test sufficiency can be established despite the branch-run limitation.

Any semantic correction requires a new remediation successor; do not repair `planning/issue-481` from review.

## Required post-review route

Only after clean review and separately authorized publication should a fresh trusted-main run establish the next exact Unity stage. If service-account auth succeeds but license status fails, route that exact license result separately; do not retroactively treat the old exit `127` as a licensing blocker.

## Authority boundary

`NOT_CANONICAL`. Unity authentication remediation only. No provider credential/PASS, license authority, engine selection, implementation/readiness, commercial/production/legal/release, verification-PASS, decision, integration or canonical authority.