# Issue #547 handoff — trigger-remediated trusted-main Unity configuration diagnostic

Mission: `W2-ENG-PROVIDER-UNITY-LICENSE-CONFIG-MAIN-REM-01`

## Disposition

`UNITY_LICENSE_TRUSTED_MAIN_DIAGNOSTIC_REMEDIATED_READY_FOR_REVIEW`

This remediation closes required-review finding `W2-ENG-PROVIDER-UNITY-LICENSE-CONFIG-MAIN-REV-M01` without mutating the frozen producer/review branches and without entering protected `engine-eval` from the task branch.

## Frozen authority / ownership

- winning claim comment: `5313138953`
- actor: `unity-license-config-main-rem-gpt56sol-20260817-01`
- source/current main at claim: `8e25f64637e0dfc61f1b6a6f571fb40335c970f8`
- current main immediately before handoff: `8e25f64637e0dfc61f1b6a6f571fb40335c970f8`
- canonical Planning Program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical binding: Issue #6 comment `5245368879`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- owner Unity-proceeds directive: Issue #84 comment `5307397331`

## Frozen predecessor / review

Producer Issue #539 / PR #541 remains immutable:
- producer terminal `5313098630`
- judged producer head `8d4a4d60d6842bca5dab3714100ecc23d205072c`
- helper blob `fd8097ec314826265484c5d0a5b1aa0bf184a791`

Required review Issue #543 / PR #546 remains immutable:
- review terminal `5313131077`
- disposition `CHANGES_NEEDED`, 0 BLOCKER / 1 MAJOR / 0 MINOR
- finding `W2-ENG-PROVIDER-UNITY-LICENSE-CONFIG-MAIN-REV-M01`
- exact defect: `workflow_dispatch` allowed repeated manual trusted-main protected diagnostics and competing evidence identities.

## Exact remediation bytes

Branch: `planning/issue-547`

Substantive exact head before this handoff: `474f70ff19ccf6dfa36cf0168174af10731cc523`.

- helper `tools/planning/unity_license_config_diag.py`: blob `fd8097ec314826265484c5d0a5b1aa0bf184a791`, byte-identical to the reviewed #539 helper.
- workflow `.github/workflows/w2-eng-provider-unity-license-config-main-diag.yml`: blob `256cb5db467a44fb9f5f4f383951c62e5aafbb61`.

The workflow correction is bounded to trigger/control-plane behavior plus branch structural verification:
- `workflow_dispatch` removed;
- no schedule/repository_dispatch/workflow_call trigger;
- automatic trigger is push-only;
- push branches are `main` plus `planning/issue-547` for non-secret branch verification;
- push paths remain only diagnostic workflow, helper, exact reviewed input contract;
- `permissions: contents: read` only;
- exactly one `environment: engine-eval`, on trusted-main job only;
- trusted job hard-gated to `refs/heads/main`;
- remediation branch job has no environment and no secret expressions.

## Branch verification

Two early synthetic validation attempts failed only inside the newly-added structural assertion and never entered the protected job:
- run `32006316758`: assertion inspected its own forbidden-trigger literal;
- run `32006442044`: follow-up assertion counted its own environment/write-permission literals.

Those failures were corrected before terminalization. In both runs, `trusted-main-diagnostic` was skipped and no provider/license value or Unity provider command was consumed.

Final exact validation:
- run `32006507660`, attempt 1
- source head `474f70ff19ccf6dfa36cf0168174af10731cc523`
- branch-selftest job `95316976501`: `success`
- trusted-main-diagnostic job `95316977340`: `skipped`
- structural one-shot trigger check: PASS
- `python3 -m py_compile`: PASS
- deterministic helper self-test: PASS, all seven cases true
- immutable artifact `9280192186`
- artifact ZIP digest `sha256:ead9b3542f2800b927c3686e50a27e0f12c426292c2414822f294364b78aaf3e`
- reviewer-side/local re-download reproduced exact ZIP SHA-256 above
- contained `selftest.json` SHA-256 `6bb40ee940a66c16816a3e86d0309f0c1da4cfc79086b40b2833d02b61cf6ad2`

No protected environment input was consumed on this branch.

## Required next gate

Open an exact-head draft PR and route one fresh independent/degraded-independent security/authority review. Reviewer must verify M01 is closed mechanically and attack all non-push triggers, branch/main environment separation, path recursion, permissions, helper byte identity, exact contract binding, secret-presence-only semantics, raw-help handling, no repository writes, and authority inflation.

A clean review grants no integration-by-review. Separately authorized squash publication is required before the trusted-main diagnostic may enter `engine-eval`.

## Authority boundary

`NOT_CANONICAL`. Trigger remediation and diagnostic machinery only. No credential/license value consumption, provider authentication/PASS, Unity license authority, editor/native execution, engine selection, implementation/readiness, production/commercial/legal/release, verification-PASS, integration-by-authorship, decision, or canonical authority.
