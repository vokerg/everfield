# Effective provider development access

Mission: `W2-ENG-PROVIDER-EFFECTIVE-01` (Issue #373)

This packet separates lawful development execution from commercial, production,
legal, licensing, release, and integration authority. A provider is unlocked
only by its own validated native path. Unity and Unreal are never combined into
one prerequisite, and the historical Issue #82 set of 50 `NOT_RUN` cells remains
immutable.

## Current bootstrap observations

- The `engine-eval` GitHub Environment exists with a custom deployment policy for
  `main`, administrator bypass disabled, and no reviewers configured. Version
  variables are `UNITY_EDITOR_VERSION=6000.5.6f1` and
  `UNREAL_ENGINE_VERSION=5.8`.
- Unity CLI `1.0.0-beta.5` is installed locally. A Unity Personal account and
  Personal license were created and activated through the official user OAuth
  path. A Unity service-account login also succeeds, but Unity explicitly
  rejects Personal-license activation for service accounts. Therefore the
  service account is a valid identity probe, not a portable Personal-license
  entitlement for an ephemeral CI runner.
- The exact Unity editor `6000.5.6f1` is installed locally at the arm64 editor
  path. Three fresh native editor processes passed S3 N1/N2/FI1 with observed
  checksums `405227`, `405227`, and `405122`; the durable non-secret packet is
  `provider-effective-access-local-unity.json`. This unlocks only Unity
  development-dependent technical cells in the local evidence frontier.
- The existing Epic/Unreal account and mailbox evidence are insufficient to
  establish the required GitHub↔Epic entitlement. The private
  `EpicGames/UnrealEngine` repository is not visible to the current GitHub
  identity, and unauthenticated GHCR access returns authorization required.
  No Unreal token is stored or inferred from those observations.

## Durable implementation

- `tools/planning/engine_provider_effective_validator.py` performs independent,
  fail-closed Unity and Unreal checks and emits only boolean/state/process
  observations. Unity native S3 uses three fresh editor processes (N1, N2,
  FI1); Unreal's authenticated registry/container path remains blocked until
  an entitled token is supplied.
- `.github/workflows/engine-eval-credentialed.yml` consumes credentials only
  on trusted `main`, in `engine-eval`, with `contents: read`. It never runs for
  pull requests or forks and uploads a sanitized data artifact.
- `.github/workflows/engine-eval-evidence-recorder.yml` is the separate trusted
  `contents: write` recorder. It accepts only a successful trusted-main run,
  validates a strict schema, projects fixed non-secret fields, and appends
  evidence to `main` without consuming provider credentials.
- `.github/workflows/engine-eval-health.yml` provides a weekly/dispatch health
  route with no issue or PR spam.

The workflow result is evidence, not authority. No commercial, production,
legal, release, engine-selection, or integration authority is derived from it.
