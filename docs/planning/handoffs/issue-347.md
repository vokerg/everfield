# Handoff — Issue #347 / W2-ENG-PROVIDER-AUTH-PRESEED-01

## Lifecycle

- task class: `AUTHORITY_INTAKE_ENABLEMENT`
- producer branch: `planning/issue-347`
- winning claim: `5302557208`
- frozen source main: `92204cb2e58c792ef4199fe3562ca2192096f5c0`
- canonical binding comment: `5245368879`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- producer substantive work commit: `f118e8d5036995424c94fd5520cb2b863cbe8b1a`
- disposition: `AUTHORITY_REQUIRED_EXACT`
- required fresh security/authority review: pending route from terminal status
- integration authority: none

## Immutable predecessor authority

- W2-ENG source Issue #82 terminal comment: `5276916603`
- historical engine matrix: 5 candidates × 10 scenarios = `50 NOT_RUN`, unchanged
- CI remediation Issue #343 terminal: `5302522499`
- CI remediation head/work: `8d8eee1d1b7d7cad63b3fecc52fcb6639c236160` / `3cc6f039170ce0c19288426aded252a1081896fb`
- CI fresh required review Issue #344 terminal: `5302539709`
- review head/work: `b8e066882b5e57ddabbd618bed67dfceb26ba199` / `c0624781bd72ca79224bc688862ae726f6f86ce9`
- review disposition: `PASS_BOUNDED_CAPABILITY_WITH_MINOR_NOTE`
- review explicitly allowed this narrow provider-authority successor but granted no provider permission, W2-ENG empirical PASS, implementation/readiness, or integration authority

## Exact producer surfaces

- presence-only probe: `tools/planning/engine_provider_authority_probe.py`
- input contract: `docs/planning/wave-2/evidence/provider-authority-input-contract.json`
- workflow: `.github/workflows/w2-engine-provider-authority-probe.yml`
- producer report: `docs/planning/wave-2/evidence/provider-authority-intake.md`
- machine presence evidence: `docs/planning/wave-2/evidence/ci/provider-authority/presence.json`
- deterministic self-test: `docs/planning/wave-2/evidence/ci/provider-authority/selftest.json`
- run identity: `docs/planning/wave-2/evidence/ci/provider-authority/run-identity.txt`

## CI evidence

- GitHub Actions run: `31888759105`
- workflow trigger SHA: `7e98635c6a28a9ebbb388035ee7631777c682be4`
- generated evidence commit: `0358a3cd97178b78959b293383af2c66da0451ff`
- artifact id: `9247964188`
- artifact name: `w2-engine-provider-authority-31888759105-1`
- artifact digest: `sha256:a41d14e386ca61ea5624791177626dac1d40846f23f9558a3c0242e14fbf19c6`
- presence JSON blob: `43c944ec8ff76754cfdb71b426b6a984eb6d3b23`
- self-test JSON blob: `89ac54c8beea583e745800cd454472504f4747b7`
- runner: `ubuntu-24.04`, image `ubuntu24 / 20260810.271.1`

Pinned workflow dependencies:

- `actions/checkout@11d5960a326750d5838078e36cf38b85af677262`
- `actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02`

## Measured provider state

### Unity `6000.5.6f1`

- `UNITY_AUTH_MODE`: unset/invalid
- service-account id presence: false
- service-account secret presence: false
- serial-license presence: false
- offline-license presence: false
- floating-config presence: false
- state: `AUTHORITY_REQUIRED`
- effective authorization validated: false
- account authentication treated as editor-license authorization: false
- credential values read: false

Exact supported reopen modes:

1. `service_account_serial` with `UNITY_SERVICE_ACCOUNT_ID`, `UNITY_SERVICE_ACCOUNT_SECRET`, and `UNITY_LICENSE_SERIAL`; or
2. `offline_file` with lawfully supplied `UNITY_OFFLINE_LICENSE_B64`; or
3. `floating` with lawfully supplied `UNITY_FLOATING_CONFIG_B64`.

A later reviewed validation path must still prove effective license authorization for the frozen baseline. Presence alone is not authorization.

### Unreal Engine `5.8`

- `UNREAL_AUTH_MODE`: unset/invalid
- Epic-authorized GitHub-token presence: false
- preseed URL presence: false
- preseed SHA-256 presence: false
- state: `AUTHORITY_REQUIRED`
- effective authorization validated: false
- current-repository `GITHUB_TOKEN` treated as cross-repository Epic entitlement: false
- credential values read: false

Exact supported reopen modes:

1. `github_token` with `UNREAL_GITHUB_TOKEN` whose effective access can later be proven against the exact EpicGames/UnrealEngine 5.8 identity; or
2. `preseed` with lawfully supplied `UNREAL_5_8_PRESEED_URL` plus exact `UNREAL_5_8_PRESEED_SHA256`, followed by retrieval/version/content validation.

## Fail-closed result

The machine result is:

```text
overall_state=AUTHORITY_REQUIRED_EXACT
both_input_sets_present=false
effective_provider_authority_validated=false
five_candidate_empirical_successor_unlocked=false
historical_not_run_cells_preserved=50
prior_not_run_promoted=false
```

The self-test passes all required negatives: empty input, partial Unity input, one-provider-only input, and even both complete presence sets cannot become effective authority or unlock W2-ENG through this probe.

## Security boundary

The workflow passes only boolean secret-presence expressions into the executable probe. The probe has no credential-value arguments and records no credential values. No credentialed provider request was attempted because neither supported provider mode is configured.

Fresh independent/degraded-independent security/authority review is required because this branch defines credential/authority intake machinery. The review must judge the exact producer head and must not edit this branch.

The reviewer must attack at least:

1. accidental secret-value exposure through expressions, environment, command output, artifacts, URLs, or git persistence;
2. fail-open semantics where presence or workflow success could be confused with effective authorization;
3. Unity account-authentication versus editor-license separation;
4. Unreal token scope versus actual EpicGames source entitlement;
5. whether the supported-mode contract is complete enough to make the current `AUTHORITY_REQUIRED_EXACT` claim truthful without claiming arbitrary secrets do not exist;
6. deterministic negative fixtures and historical `NOT_RUN` preservation;
7. branch/workflow trust: no future configured credential may be treated as trusted merely because this draft branch can observe its presence;
8. authority inflation into empirical PASS, engine selection, readiness, provider/legal/platform/release, decision, canonicality, or integration.

## Next transition if review is clean

If review trusts this packet, the current frontier is an **external authority/configuration trigger**, not another repository-local CI task. The trigger is satisfied only when one declared Unity mode and one declared Unreal mode are actually configured by an authorized operator/owner. After that state change, a fresh reviewed validation episode may prove effective authorization and exact engine-content identity.

Do not create a generic environment-recovery issue while the exact provider predicates above remain unsatisfied. Do not run only Bevy/Defold/Godot or otherwise shrink the five-candidate comparison. Do not create a W2-ENG empirical successor until both provider inputs are effectively validated under a trusted path.

## Authority boundary

This packet creates no provider permission, legal clearance, W2-ENG empirical PASS, engine ranking/selection, gameplay/high-throughput implementation, production/readiness, platform/release authority, verification-PASS authority, decision authority, canonicality, or integration authority. Any eventual publication to `main` remains separately authorized and squash-only.
