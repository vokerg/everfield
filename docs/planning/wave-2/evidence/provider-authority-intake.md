# W2-ENG-PROVIDER-AUTH-PRESEED-01 — Provider authority intake

**Issue:** #347  
**Frozen source main:** `92204cb2e58c792ef4199fe3562ca2192096f5c0`  
**Canonical program blob:** `e3120ec203c4156328770aa86c12fbb7187966dc`  
**Required predecessor review:** Issue #344 terminal `5302539709`, `PASS_BOUNDED_CAPABILITY_WITH_MINOR_NOTE`  
**Engine source:** Issue #82 terminal `5276916603`, 50 historical `NOT_RUN`, unchanged  
**Intake run:** GitHub Actions `31888759105`, trigger `7e98635c6a28a9ebbb388035ee7631777c682be4`  
**Generated evidence commit:** `0358a3cd97178b78959b293383af2c66da0451ff`  
**Run artifact:** `9247964188`, digest `sha256:a41d14e386ca61ea5624791177626dac1d40846f23f9558a3c0242e14fbf19c6`  
**Disposition:** `AUTHORITY_REQUIRED_EXACT`.

## Result

The repository-owned presence probe executed successfully on `ubuntu-24.04` image `ubuntu24 / 20260810.271.1`. It accepts only boolean presence flags and non-secret mode selectors; secret credential values are never passed to the probe.

Current measured state:

| Provider | Frozen baseline | Measured state | Exact current predicate |
|---|---|---|---|
| Unity | `6000.5.6f1` | `AUTHORITY_REQUIRED` | `UNITY_AUTH_MODE` is unset/invalid. All defined supported secret-presence flags are false: service-account id, service-account secret, serial license, offline license material, and floating-license config. |
| Unreal Engine | `5.8` | `AUTHORITY_REQUIRED` | `UNREAL_AUTH_MODE` is unset/invalid. All defined supported input-presence flags are false: Epic-authorized GitHub token, preseed URL, and preseed SHA-256 identity. |

`both_input_sets_present=false`. `effective_provider_authority_validated=false`. `five_candidate_empirical_successor_unlocked=false`.

No provider permission is inferred from absence, workflow success, public web reachability, current-repository `GITHUB_TOKEN`, or account authentication. A presence-only path is structurally incapable of unlocking W2-ENG.

## Fail-closed mechanics

The versioned contract is `docs/planning/wave-2/evidence/provider-authority-input-contract.json`; executable classification is `tools/planning/engine_provider_authority_probe.py`; CI surface is `.github/workflows/w2-engine-provider-authority-probe.yml`.

The deterministic self-test passed all cases:

- empty inputs classify `AUTHORITY_REQUIRED_EXACT`;
- empty inputs never unlock empirical work;
- a partial Unity service-account/serial set is rejected;
- one provider alone never unlocks the five-candidate successor;
- even both complete **presence** sets classify only `BOTH_INPUT_SETS_PRESENT_VALIDATION_REQUIRED`;
- presence can never become effective authority in this probe.

The workflow additionally asserts that provider authority is unvalidated, the empirical successor is locked, 50 historical `NOT_RUN` cells remain preserved, and zero prior cells are promoted.

## Exact reopen predicates

### Unity

A future authority-validation episode must bind one declared supported mode and then independently prove effective license authorization for Unity `6000.5.6f1`:

- `service_account_serial`: `UNITY_SERVICE_ACCOUNT_ID`, `UNITY_SERVICE_ACCOUNT_SECRET`, and `UNITY_LICENSE_SERIAL`; or
- `offline_file`: lawfully supplied `UNITY_OFFLINE_LICENSE_B64`; or
- `floating`: lawfully supplied `UNITY_FLOATING_CONFIG_B64` plus later reachable/licensed-server validation.

Presence is not enough. Account authentication is not editor-license authorization.

### Unreal Engine

A future authority-validation episode must bind one declared supported mode and independently prove exact Unreal Engine 5.8 access:

- `github_token`: `UNREAL_GITHUB_TOKEN` with effective EpicGames/UnrealEngine entitlement; or
- `preseed`: lawfully supplied `UNREAL_5_8_PRESEED_URL` plus exact `UNREAL_5_8_PRESEED_SHA256`, followed by retrieval/version/content validation.

Current-repository `GITHUB_TOKEN` is not assumed to grant cross-repository Epic entitlement.

## Current provider-source semantics

Current first-party Unity documentation describes the Unity CLI as suitable for CI/automation, supports service-account authentication for unattended workflows, and separately supports license activation/status workflows. Current Epic documentation requires an Epic account, GitHub account, account linking/authorization and applicable EULA acceptance before access to the private Unreal Engine source repository. These facts define possible intake routes only; they do not grant this repository authority.

## Security / authority boundary

- no secret values were read, printed, hashed, uploaded, or committed;
- no credentialed provider request was attempted because no supported input mode is configured;
- no S1–S10 scenario was executed;
- no reduced three/four-candidate comparison was created;
- Issue #82 remains 50 historical `NOT_RUN` cells;
- no engine ranking/selection, implementation/readiness, provider/legal/platform/release, verification-PASS, decision, canonicalization, or integration authority is created.

Because this episode creates credential/authority intake machinery, fresh independent/degraded-independent security/authority review is required before any future configured input may be trusted or any credential-consuming validation path may unlock a W2-ENG empirical successor.
