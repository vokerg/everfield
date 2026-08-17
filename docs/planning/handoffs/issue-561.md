# Issue #561 handoff — headless Unity Personal user-login behavior

Mission: `W2-ENG-PROVIDER-UNITY-PERSONAL-HEADLESS-DIAG-01`

## Disposition

`HEADLESS_USER_LOGIN_REQUIRES_INTERACTIVE_BROWSER_OR_PERSISTENT_SESSION`

The exact pinned Unity CLI Personal/user-login route has now been tested on a standard GitHub-hosted headless runner without credentials or user input. No supported device/noninteractive user-login flow was discovered.

## Ownership / canonical identity

- winning claim comment: `5313303151`
- actor: `unity-personal-headless-diag-gpt56sol-20260817-01`
- source main: `1efddbcf43221cec37fba8cf3febdd5997b7e3c6`
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical binding: Issue #6 comment `5245368879`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- predecessor Issue #557 terminal: `5313297388`

## Frozen predecessor facts

Issue #557 established from exact public CLI `1.0.0-beta.5` help that:
- Personal activation exists (`license activate --personal`);
- user login exposes browser/user concepts;
- service-account automation flags exist;
- no bounded device/session/token/export/import surface exists;
- historical Issue #373 proves Personal activation succeeds under user OAuth and exact service-account Personal activation returns `SERVICE_ACCOUNT_UNSUPPORTED`.

Protected trusted-main run `32007010902` separately established:
- service-account ID/secret presence true;
- `UNITY_AUTH_MODE` unset;
- serial/offline/floating inputs absent.

## Exact headless behavior evidence

Branch `planning/issue-561`.

Workflow run:
- run `32007667644`, attempt 1
- source head `a1c2f70ab62f91e9a1fa9d942f9529a24824f17f`
- job `95320404192`: success
- exact Unity CLI expected/observed `1.0.0-beta.5`
- no protected environment, Actions secret/var, credential, session, license value, or user input used.

Invocation:
`unity auth login --no-store --non-interactive --format json`
under a hard 20-second timeout, with stdout/stderr quarantined to runner-temp files that were never printed, hashed, committed, or uploaded.

Bounded result:
- process exit `124` (timeout)
- timed out: true
- browser interaction indicated: true
- device-code flow indicated: false
- service-account requirement indicated by this user invocation: false
- output was not a completed valid JSON result
- post-attempt `auth status` signed-in user: false
- disposition: `HEADLESS_USER_LOGIN_REQUIRES_INTERACTIVE_BROWSER_OR_PERSISTENT_SESSION`.

Artifact:
- artifact `9280594687`
- artifact ZIP SHA-256 `01c50ba0c44774b8cedcbb3a5453226da94180403bdc75b6acfd287548cc0560`
- diagnostic JSON SHA-256 `f6a65be544914984e08e650256b78e5aab1ba9e026c59311cda2b2ffb7c23f2e`
- selftest JSON SHA-256 `1a248458d01e809bc074e59c84767d13d7098f63e8f48bef64b9835393943c15`
- raw OAuth/login/status output was excluded from the artifact and destroyed after bounded projection.

The deterministic self-tests prove browser URL/state-shaped source data is not emitted by the projector and that no raw-output hash is recorded.

## External/provider gate now exact

The remaining GitHub-hosted Unity Personal CI blocker is:

`SUPPORTED_UNATTENDED_UNITY_LICENSE_INPUT_OR_PERSISTENT_INTERACTIVE_USER_SESSION_EXECUTION_CONTEXT`

The current standard ephemeral runner cannot establish the proven Personal user session unattended. Service-account credentials already present in `engine-eval` cannot substitute for Personal activation because exact prior provider evidence returned `SERVICE_ACCOUNT_UNSUPPORTED`.

Safe reopen options are limited to provider-supported inputs/contexts, for example:
1. an already-owned valid serial license supplied through the protected environment and selected as `service_account_serial`;
2. a provider-supported exact offline-license input valid for the target execution context;
3. a configured floating-license input/server already available to the owner;
4. a persistent execution context in which the owner can lawfully complete the browser-based user login and retain the local Unity session, if such infrastructure is already approved/available.

Do not paste license values or session material into issues/comments. Do not store user passwords/cookies, export undocumented sessions/tokens, or weaken protected-environment controls. Do not buy or introduce new paid/self-hosted infrastructure merely to satisfy this task without an explicit owner decision.

If none of the safe reopen options is available, Unity remains CI-provider-blocked while the previously proven local Unity native S3 evidence remains valid only at its bounded local scope.

## Authority boundary

`NOT_CANONICAL`. Headless behavior evidence only. No user login completion, provider authentication/PASS, Unity CI license authority, engine selection, implementation/readiness, release, verification-PASS, integration, decision, or canonical authority.
