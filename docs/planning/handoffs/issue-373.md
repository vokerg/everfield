# Issue 373 handoff — effective provider development access

```yaml
protocol: PLANNING-v1
schema: 3
kind: HANDOFF
issue: 373
mission_id: W2-ENG-PROVIDER-EFFECTIVE-01
branch: planning/issue-373
state: REVIEW_READY
authority_mode: OWNER
```

## Scope

This task establishes the per-provider effective-access contract and the
credentialed-main/evidence-recorder boundary. It does not grant commercial,
production, legal, release, engine-selection, or integration authority.

## Implemented in the working branch

- Contract: `docs/planning/wave-2/evidence/provider-effective-access-contract.json`
- Validator: `tools/planning/engine_provider_effective_validator.py`
- Sanitized recorder: `tools/planning/record_provider_effective_access.py`
- Credentialed evaluator: `.github/workflows/engine-eval-credentialed.yml`
- Trusted recorder: `.github/workflows/engine-eval-evidence-recorder.yml`
- Health route: `.github/workflows/engine-eval-health.yml`
- Evidence narrative: `docs/planning/wave-2/evidence/provider-effective-access.md`

## External state

- `engine-eval` exists and is restricted to `main`; no administrator bypass.
- Unity service-account secret names are configured in the Environment; values
  are not present in the repository or evidence. The service-account login is
  valid, but Personal-license activation is rejected for that auth mode.
- Unreal credentials remain absent because Epic/GitHub entitlement and the
  dedicated package-read token have not been lawfully established.

## Checks completed

- Validator and recorder compile with Python 3.
- Validator deterministic self-tests pass, including independent provider
  unlock and secret-redaction checks.
- Historical Issue #82 count is fixed at 50 and mutation is rejected.
- Draft PR #397 targets `main` from the exact task branch; its head is the
  immutable review surface for the current packet.

## Remaining gates

1. CI must still classify the Unity Personal-license/service-account
   incompatibility explicitly unless a lawful ephemeral-runner entitlement route
   becomes available; the local Unity native proof is now durable.
2. Establish the Unreal GitHub↔Epic entitlement and a dedicated least-privilege
   package-read token, then validate an exact 5.8 container/native path.
3. Perform a fresh security review of the workflow boundary and validator,
   address findings on this branch, open a draft PR, and use the repository's
   squash-only integration route. Do not publish `REVIEW_READY` before the
   draft PR head equals the terminal status head.
