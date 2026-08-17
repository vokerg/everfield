# Issue #557 handoff — Unity Personal licensing path diagnostic

Mission: `W2-ENG-PROVIDER-UNITY-PERSONAL-PATH-DIAG-01`

## Disposition

`PERSONAL_PATH_REQUIRES_EXACT_EXTERNAL_USER_SESSION_PREDICATE`

The current Unity Personal route is real and supported by the installed CLI, but the available protected GitHub configuration does not contain a supported unattended user-session transport. Existing service-account credentials must not be treated as a Personal-license substitute.

## Ownership / canonical binding

- winning claim comment: `5313274450`
- actor: `unity-personal-path-diag-gpt56sol-20260817-01`
- source main: `1efddbcf43221cec37fba8cf3febdd5997b7e3c6`
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical binding: Issue #6 comment `5245368879`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- owner Unity-proceeds directive: Issue #84 comment `5307397331`

## Exact protected configuration trigger

Reviewed trusted-main diagnostic run `32007010902`, attempt 1, source `main@1efddbcf43221cec37fba8cf3febdd5997b7e3c6`:
- job `95318471561`: success
- artifact `9280366361`
- artifact SHA-256 `6342485f9e634adc31455c473ca787ffc443634a20ee57a35d95a778c41c25da`
- diagnostic JSON SHA-256 `355b243676f1a78a8f0505c4b4b2a99f92fcdae2cdeda2840cda7386b29785ee`
- `UNITY_AUTH_MODE`: unset/invalid
- service-account ID presence: true
- service-account secret presence: true
- serial presence: false
- offline-license presence: false
- floating-config presence: false
- protected diagnostic disposition: `UNITY_LICENSE_CONFIGURATION_INPUT_REQUIRED_EXACT`.

No credential/license values were exposed by that diagnostic.

## Frozen prior Personal evidence

Issue #373 records:
- Unity Personal entitlement exists for the account/organization;
- user OAuth login succeeds;
- `unity license activate --personal --accept-eula --non-interactive --format json` succeeds under the user OAuth route;
- service-account authentication succeeds;
- Personal activation under service-account authentication returns `SERVICE_ACCOUNT_UNSUPPORTED`;
- exact Unity `6000.5.6f1` local native S3 N1/N2/FI1 processes succeeded.

Issue #398 preserved the boundary that local success does not establish GitHub-hosted ephemeral CI validation and explicitly allowed continued investigation of that exact Personal-license CI condition.

## Fresh exact public CLI evidence

Branch: `planning/issue-557`.

Public non-secret workflow run:
- run `32007413841`, attempt 1
- source head `c69b3f905417687dfa42f98f761ddbc1bd373147`
- job `95319649446`: success
- artifact `9280498374`
- artifact ZIP SHA-256 `2dda91f30f0883e84cbe7c03dd8a8ac28d10ab16107006df4d150fbc9ccc5354`
- diagnostic JSON SHA-256 `69312cca74a87c200e97ae25db06e073fd90775ab4caf42dc3cba206c98ffdb1`
- selftest JSON SHA-256 `d92c977e76d4ff8156681dc18db133828cc4028cde2ae23d92f722449aa45b16`
- observed Unity CLI: exact `1.0.0-beta.5`
- no environment, Actions secret/var, authentication command, user session, provider credential, or license value was used.

Bounded installed help projection:
- `unity license activate --help`: exit 0; `--personal`, `--accept-eula`, `--non-interactive`, `--serial`, `--floating`, and `--file` are present.
- `unity auth login --help`: exit 0; browser/user concepts plus `--client-id`, `--client-secret`, `--secret-from-stdin`, `--no-store`, `--non-interactive` are present.
- no bounded `device`, `session`, `token`, `export`, or `import` concept is exposed by `auth login` help.
- raw help was runner-temporary only and was not uploaded.

The public artifact disposition is `PERSONAL_PATH_REQUIRES_EXACT_EXTERNAL_USER_SESSION_PREDICATE`.

Current first-party Unity CLI documentation independently describes `unity auth login` as opening a browser-based sign-in flow and storing the resulting session locally. Installed-version help remains authoritative for exact installed flags.

## Exact blocker

For standard ephemeral GitHub-hosted runners, the repository currently lacks a reviewed, supported way to establish the already-proven Personal user session **without** one of the prohibited shortcuts:
- storing a user password;
- persisting/copying browser cookies;
- exporting/importing an undocumented session/token;
- pretending service-account auth can activate Personal despite exact `SERVICE_ACCOUNT_UNSUPPORTED` evidence;
- weakening trusted-main / protected-environment controls;
- buying or introducing paid/self-hosted infrastructure contrary to the frozen #373 scope.

Exact reopen predicate:

`SUPPORTED_UNATTENDED_OR_REPRODUCIBLE_USER_OAUTH_SESSION_TRANSPORT_FOR_UNITY_PERSONAL_ON_EPHEMERAL_CI`

A qualifying reopen must be provider-supported and reviewable, must not rely on password/cookie/session exfiltration, and must be independently validated before any Unity CI license PASS.

## What remains eligible

This blocker is scoped to GitHub-hosted Unity Personal license activation/effective access. It does not invalidate the exact local Unity 6000.5.6f1 native S3 evidence, does not globally block other engine/content work, and does not justify setting `UNITY_AUTH_MODE=service_account_serial` without a real serial input.

## Authority boundary

`NOT_CANONICAL`. Diagnostic evidence only. No credential/session/license acquisition, provider authentication/PASS, Unity CI license authority, engine selection, implementation/readiness, production/commercial/legal/release, verification-PASS, integration, decision, or canonical authority.
