# Issue #539 handoff — reviewed trusted-main Unity license configuration diagnostic candidate

Mission: `W2-ENG-PROVIDER-UNITY-LICENSE-CONFIG-MAIN-DIAG-01`

## Disposition

`UNITY_LICENSE_TRUSTED_MAIN_DIAGNOSTIC_READY_FOR_REVIEW`

This candidate repairs the exact Issue #535 execution-architecture failure without weakening the protected `engine-eval` environment. The planning branch runs only deterministic non-secret self-tests. The protected presence-only diagnostic is hard-gated to trusted `main` and can execute only after fresh review plus separately authorized squash publication.

## Ownership / canonical binding

- winning claim comment: `5313066064`
- actor session: `frontier-drain-unity-license-config-main-diag-gpt56sol-20260817-01`
- producer base at claim: `e2ae0314dfaf64b3574bcb082710716f5a53925c`
- current `main` before handoff write: `67134734904dace3384e95efadff0894b5a4d762`
- current-main drift is one disjoint immutable provider-evidence publication only; it preserves the exact Unity blocker and does not touch this candidate's owned paths
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical binding comment: `5245368879`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- owner Unity-proceeds directive: Issue #84 comment `5307397331`

## Frozen predecessor

Issue #535:
- terminal comment: `5313059364`
- disposition: `UNITY_LICENSE_CONFIG_DIAGNOSTIC_INCONCLUSIVE`
- failed protected branch run: `32005422424`, attempt 1
- failed job: `95313779519`
- job steps executed: `0`
- runner id: `0`
- exact GitHub annotation: `Branch "planning/issue-535" is not allowed to deploy to engine-eval due to environment protection rules.`
- no Unity command, credential value, or license value was consumed.

## Exact producer candidate

Branch: `planning/issue-539`

Substantive candidate head before this handoff: `646c994816d8b58b0ecd5ff04ef16a347ab777bd`.

Owned implementation paths and blobs at that head:
- `.github/workflows/w2-eng-provider-unity-license-config-main-diag.yml` — blob `c3941aa7aca6e4ca93d67d95dacdd7d8e11f70ee`
- `tools/planning/unity_license_config_diag.py` — blob `fd8097ec314826265484c5d0a5b1aa0bf184a791`

Reviewed input contract remains immutable:
- `docs/planning/wave-2/evidence/provider-authority-input-contract.json`
- blob `a4c40fe1f77ec9557dbe0d76af3e947f188c96be`

## Branch verification

Workflow run `32005667992`, attempt `1`, source head `646c994816d8b58b0ecd5ff04ef16a347ab777bd`:
- branch self-test job `95314516056`: `success`
- protected `trusted-main-diagnostic` job `95314516780`: correctly `skipped` on the planning branch
- branch job performed exact checkout, contract-blob check, `python3 -m py_compile`, deterministic helper self-tests, and non-secret artifact upload
- immutable self-test artifact `9279907578`
- artifact digest `sha256:7b3f2dbf3c15cba8d5ebb9ba3d49ed1064eb9f4bd462d3636fb245e2c5931ff0`

No protected environment or secret expression is attached to the branch job.

## Candidate security / execution boundaries

1. Workflow permissions are `contents: read` only.
2. Branch job is restricted to `refs/heads/planning/issue-539`, has no `environment:` declaration, no provider network call, and no secret-expression inputs.
3. Trusted diagnostic job is restricted to `refs/heads/main` and uses `environment: engine-eval` only there.
4. Workflow push paths are restricted to its workflow file, helper, and exact reviewed input contract. Provider-evidence, S7, content, or unrelated main pushes do not retrigger this diagnostic.
5. Trusted-main job pins Unity CLI `1.0.0-beta.5`, verifies exact main checkout and input-contract blob, then captures only non-secret CLI help before evaluating any secret-presence expressions.
6. Raw CLI help remains runner-temporary. Persisted diagnostic data contains only help exit codes, byte counts, normalized option/subcommand names, and raw-help SHA-256.
7. The protected step receives only the non-secret `UNITY_AUTH_MODE` selector and boolean `${{ secrets.NAME != '' }}` presence signals for the five declared Unity inputs. It never receives credential/license values, hashes, lengths, or substrings.
8. The helper validates the exact reviewed contract and can emit only:
   - `UNITY_LICENSE_MODE_PRESENT_NEEDS_EFFECTIVE_WIRING`; or
   - `UNITY_LICENSE_CONFIGURATION_INPUT_REQUIRED_EXACT` with exact missing declared input names.
9. Presence never grants provider authentication, license validity, editor/native execution eligibility, provider PASS, integration authority, or canonicality.
10. The trusted-main job writes nothing to the repository; it uploads one immutable diagnostic artifact only. It cannot create a recorder/evidence-branch recursion.

## Triggering Unity state

Latest trusted-main evidence remains:
- baseline `6000.5.6f1`
- state `BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION`
- blocker `UNITY_LICENSE_STATUS_CONFIGURATION_REQUIRED`
- `unity license status` exit `4`, timeout false
- authentication/license/editor/native-S3 validation false.

The candidate deliberately does not relabel or repair that provider state. Its only purpose is to identify the exact configured licensing mode/presence boundary and installed CLI command surface after reviewed publication.

## Required next gate

Fresh independent/degraded-independent security/authority review of the exact candidate head and draft PR is mandatory. Reviewer must attack:
- branch-vs-main job gating;
- protected-environment scoping;
- workflow permissions and path-trigger recursion;
- secret-expression semantics and any possibility of value leakage;
- raw CLI-help handling/normalization;
- exact input-contract binding and mode classification;
- false provider/license authority;
- source/current-main drift and changed-path scope.

A review PASS grants no integration-by-review. A separately authorized squash-only publication is required before the protected trusted-main diagnostic may execute.

## Authority boundary

`NOT_CANONICAL`. Diagnostic machinery only. No provider authentication/PASS, Unity license, editor/native execution, engine selection, implementation/readiness, production/commercial/legal/release, verification-PASS, integration-by-authorship, decision, or canonical authority.
