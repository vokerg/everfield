# W2-ENG-PROVIDER-UNITY-LICENSE-CONFIG-MAIN-REV-01

## Review disposition

`CHANGES_NEEDED`

Severity counts:
- BLOCKER: 0
- MAJOR: 1
- MINOR: 0

Trust profile: `DEGRADED_SINGLE_AGENT`.

This is a fresh reviewer episode distinct from the Issue #539 producer actor. The judged producer branch was treated as immutable throughout review. No producer bytes were edited and no provider credential/license value was consumed.

## Frozen judged candidate

- producer issue: #539
- producer terminal comment: `5313098630`
- producer branch: `planning/issue-539`
- producer draft PR: #541
- judged head: `8d4a4d60d6842bca5dab3714100ecc23d205072c`
- PR base at freeze: `67134734904dace3384e95efadff0894b5a4d762`
- PR state: open / draft / unmerged / mergeable / clean
- exact changed-file count: 3
- workflow blob: `c3941aa7aca6e4ca93d67d95dacdd7d8e11f70ee`
- helper blob: `fd8097ec314826265484c5d0a5b1aa0bf184a791`
- producer handoff blob: `97e82b9282391ed9d6f68f6820bc8d402238ef44`
- reviewed input-contract blob: `a4c40fe1f77ec9557dbe0d76af3e947f188c96be`

Exact changed paths:
1. `.github/workflows/w2-eng-provider-unity-license-config-main-diag.yml`
2. `tools/planning/unity_license_config_diag.py`
3. `docs/planning/handoffs/issue-539.md`

No existing evaluator/recorder, generated provider evidence, Unreal, S7, policy, secret configuration, or implementation path is changed.

## Mechanical evidence independently checked

Branch validation run `32005667992`, attempt 1:
- source head: `646c994816d8b58b0ecd5ff04ef16a347ab777bd`
- branch self-test job `95314516056`: `success`
- protected trusted-main job `95314516780`: `skipped`, as required on the planning branch
- job log confirms `GITHUB_TOKEN` permissions `Contents: read`, `Metadata: read`
- job log confirms exact checkout of source head, exact input-contract Git blob check, `python3 -m py_compile`, deterministic `--self-test`, and artifact upload
- self-test artifact: `9279907578`
- GitHub artifact digest: `sha256:7b3f2dbf3c15cba8d5ebb9ba3d49ed1064eb9f4bd462d3636fb245e2c5931ff0`
- reviewer independently downloaded the artifact ZIP and reproduced exactly the same ZIP SHA-256
- contained `selftest.json` SHA-256: `6bb40ee940a66c16816a3e86d0309f0c1da4cfc79086b40b2833d02b61cf6ad2`
- all seven deterministic cases are true: floating complete, bounded help normalization, offline selected-mode isolation, no-authority presence, serial complete, serial-missing exact predicate, unset-mode exact predicate.

The branch evidence is trustworthy for the bounded synthetic behavior it asserts. It is not provider/license evidence.

## Attack results

### PASS — branch/protected-environment separation

The branch job is explicitly gated to `refs/heads/planning/issue-539`, has no `environment:` declaration, and contains no secret-presence expressions. The trusted diagnostic job is explicitly gated to `refs/heads/main` and alone declares `environment: engine-eval`. The branch run mechanically confirms the trusted job is skipped rather than entering the protected environment.

### PASS — least privilege / repository mutation

Top-level workflow permissions are `contents: read`. The trusted diagnostic writes only under runner temporary storage and uploads an Actions artifact. It contains no git commit/push, PR mutation, recorder invocation, evidence-branch creation, or repository-write permission.

### PASS — source / contract binding

The trusted job checks repository/ref identity, exact event SHA checkout, and exact reviewed input-contract blob before protected presence classification. The helper independently recomputes the Git blob identity and rejects contract drift.

### PASS — secret-value boundary

The protected step maps only:
- non-secret `UNITY_AUTH_MODE` from `vars`;
- boolean results of `${{ secrets.NAME != '' }}` for the five declared Unity inputs.

The helper exposes no parser/API parameter for credential/license values. It receives only mode and boolean environment inputs. No raw provider result, secret value, secret hash, value substring, or value length is persisted. Presence booleans are intentionally bounded diagnostic metadata and are explicitly marked non-authoritative.

### PASS — mode semantics / false authority

The helper binds the three reviewed modes exactly:
- `service_account_serial` => service-account ID + secret + serial presence;
- `offline_file` => offline-license presence;
- `floating` => floating-config presence.

Unset/invalid mode or a missing selected-mode predicate yields only `UNITY_LICENSE_CONFIGURATION_INPUT_REQUIRED_EXACT`. Complete selected-mode presence yields only `UNITY_LICENSE_MODE_PRESENT_NEEDS_EFFECTIVE_WIRING`. The output fixes provider PASS, Unity-license authority, editor-execution authority, integration authority and canonicality to false/noncanonical values.

### PASS — CLI help handling

The trusted job pins/resolves Unity CLI `1.0.0-beta.5` using the same reviewed installation pattern as the existing evaluator. License/config help is captured before protected presence evaluation. Raw help remains in runner temporary storage and is not uploaded; the helper persists only exit status, byte count, normalized option/subcommand names and raw-help SHA-256.

## Finding

### `W2-ENG-PROVIDER-UNITY-LICENSE-CONFIG-MAIN-REV-M01` — MAJOR

**The candidate is not actually one-shot/path-scoped because `workflow_dispatch` remains enabled.**

The workflow correctly restricts automatic `push` execution with a narrow path set, but the top-level trigger also includes `workflow_dispatch`. After this workflow exists on `main`, an authorized GitHub actor can manually dispatch it on `main` repeatedly. The trusted-main job's `if` condition accepts every such main dispatch, enters protected `engine-eval`, repeats presence measurement, and uploads another valid-looking diagnostic artifact.

This is a material evidence-identity defect even though it does not leak secret values:
- the stated objective and handoff require one path-scoped trusted-main diagnostic resulting from reviewed squash publication;
- repeated manual dispatch can create multiple artifacts for the same reviewed code;
- if environment configuration changes between dispatches, those artifacts can legitimately disagree;
- the candidate defines no canonical attempt-selection rule for those competing artifacts;
- downstream remediation could therefore bind the wrong presence snapshot or treat a later manual rerun as the publication-triggered verification episode.

The defect bypasses the intended path-scoped one-shot trigger and makes the future verification identity non-deterministic. It is therefore correction-required before publication.

### Required correction

Use a separate remediation issue/branch. Do not mutate `planning/issue-539`.

The bounded correction is:
1. remove `workflow_dispatch` from the diagnostic workflow;
2. preserve the existing narrow `push.branches` / `push.paths` routing so the trusted-main diagnostic is triggered only by publication/change of the reviewed diagnostic surfaces;
3. preserve branch synthetic validation without protected inputs; if remediation uses a new planning branch, update/reconstruct only the non-secret branch-test routing necessary to mechanically validate the remediated exact head;
4. add/perform a deterministic structural check proving no manual or schedule trigger is present and the trusted job still requires `refs/heads/main`;
5. preserve all existing read-only permissions, secret-presence-only semantics, contract binding, raw-help boundary, no repository writes, and no provider/license authority;
6. route a fresh required review of the corrected exact head.

No credential, license, provider, Unity CLI semantics, input-contract content, existing evaluator, recorder, or provider-evidence behavior needs changing for this finding.

## Review conclusion

`CHANGES_NEEDED` with 0 BLOCKER / 1 MAJOR / 0 MINOR.

The candidate's core secret-isolation and branch/main separation design is sound, but the manual dispatch trigger violates the exact one-shot evidence contract. PR #541 must not integrate. A fresh bounded remediation and fresh required review are required.

## Authority boundary

`NOT_CANONICAL`. This review grants no integration-by-review, provider authentication/PASS, Unity license authority, editor/native execution, engine selection, implementation/readiness, production/commercial/legal/release, verification-PASS, decision, or canonical authority.

Mandatory reopen condition for trust profile: `MULTI_AGENT_OR_ISOLATED_CONTEXT_AVAILABLE`.
