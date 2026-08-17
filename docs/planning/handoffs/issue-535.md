# Issue #535 handoff — Unity license configuration diagnostic

Mission: `W2-ENG-PROVIDER-UNITY-LICENSE-CONFIG-DIAG-01`

## Disposition

`UNITY_LICENSE_CONFIG_DIAGNOSTIC_INCONCLUSIVE`

The intended protected-environment branch diagnostic is not executable under the repository's current `engine-eval` environment protection policy. This is an exact platform gate, not a Unity/provider result.

## Frozen ownership and source

- winning claim comment: `5313029757`
- actor session: `frontier-drain-unity-license-config-diag-gpt56sol-20260817-01`
- source/current main at claim: `e2ae0314dfaf64b3574bcb082710716f5a53925c`
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical binding comment: `5245368879`
- triggering Unity blocker: `UNITY_LICENSE_STATUS_CONFIGURATION_REQUIRED`
- triggering Unity `license status` exit: `4`
- reviewed provider-authority input-contract blob: `a4c40fe1f77ec9557dbe0d76af3e947f188c96be`

## Useful branch work

- branch: `planning/issue-535`
- diagnostic helper commit: `5b3662a664071ee57cf86535d0d68c5fc17a2cbe`
- protected diagnostic workflow commit: `cb26cfed440c58c049d5ee92e6fed2537c8aa321`
- helper: `tools/planning/unity_license_config_diag.py`
- attempted workflow: `.github/workflows/w2-eng-provider-unity-license-config-diag.yml`

These bytes are unreviewed diagnostic work and are not authorized for direct integration.

## Exact failed execution

- workflow run: `32005422424`, attempt `1`
- workflow id: `336020072`
- job: `95313779519`
- source head: `cb26cfed440c58c049d5ee92e6fed2537c8aa321`
- job conclusion: `failure`
- job steps executed: `0`
- runner id: `0`
- runner name: empty
- deployment id: `5940686555`
- environment: `engine-eval`
- GitHub check annotation: `Branch "planning/issue-535" is not allowed to deploy to engine-eval due to environment protection rules.`
- second annotation: `The deployment was rejected or didn't satisfy other protection rules.`

Because the job failed before step execution, no Unity CLI command ran and no secret, credential, or license value was consumed, exposed, hashed, persisted, or uploaded.

## Proven repository gap retained

The reviewed input contract declares Unity modes:

- `service_account_serial` → service account ID + service account secret + `UNITY_LICENSE_SERIAL`;
- `offline_file` → `UNITY_OFFLINE_LICENSE_B64`;
- `floating` → `UNITY_FLOATING_CONFIG_B64`.

The current trusted-main effective evaluator consumes only the service-account ID/secret and therefore cannot distinguish an unavailable license input from an already-supplied but unwired declared licensing mode.

## Exact next route

Create one bounded successor that:

1. carries the presence-only helper semantics forward without trusting this branch by authorship;
2. runs non-secret syntax/self-tests on its task branch without `engine-eval`;
3. requires fresh security/authority review;
4. after separately authorized squash publication, runs a one-shot trusted-main diagnostic under `engine-eval` scoped only to the diagnostic workflow/helper paths;
5. records only `UNITY_AUTH_MODE`, secret-presence booleans, and bounded Unity CLI license/config command-surface metadata;
6. routes either exact effective wiring for the already-present selected mode or exact external configuration input required.

Do not weaken the protected environment to make branch execution possible. Do not bypass review and do not ask the owner to re-enter service-account credentials merely because the protected branch probe was rejected.

## Authority boundary

`NOT_CANONICAL`. No provider authentication/PASS, Unity license authority, editor/native execution, engine selection, implementation/readiness, production/commercial/legal/release, verification-PASS, integration, decision, or canonical authority.
