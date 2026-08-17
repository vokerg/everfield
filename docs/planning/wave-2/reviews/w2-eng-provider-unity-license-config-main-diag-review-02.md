# W2-ENG-PROVIDER-UNITY-LICENSE-CONFIG-MAIN-REV-02

## Disposition

`PASS_BOUNDED_TRIGGER_REMEDIATED_TRUSTED_MAIN_UNITY_CONFIG_DIAGNOSTIC`

Severity counts:
- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0

Trust profile: `DEGRADED_SINGLE_AGENT`.

The judged Issue #547 branch remained immutable. This reviewer episode did not consume provider credential/license values and did not enter `engine-eval`.

## Frozen candidate

- remediation Issue #547 terminal comment: `5313186449`
- draft PR: #551
- exact judged head: `f456ce25cae8aab4178528b0691b766d8dbdf026`
- exact base: `8e25f64637e0dfc61f1b6a6f571fb40335c970f8`
- PR state at freeze: open / draft / unmerged / mergeable / clean
- changed paths exactly:
  1. `.github/workflows/w2-eng-provider-unity-license-config-main-diag.yml`
  2. `tools/planning/unity_license_config_diag.py`
  3. `docs/planning/handoffs/issue-547.md`
- workflow blob: `256cb5db467a44fb9f5f4f383951c62e5aafbb61`
- helper blob: `fd8097ec314826265484c5d0a5b1aa0bf184a791`
- handoff blob: `d0f274d30d1497ec8ed6116edf0873aad09f3f49`
- reviewed input-contract blob remains unchanged: `a4c40fe1f77ec9557dbe0d76af3e947f188c96be`

## Prior finding closure

Issue #543 finding `W2-ENG-PROVIDER-UNITY-LICENSE-CONFIG-MAIN-REV-M01` is mechanically closed.

The final workflow trigger header contains exactly one `push` trigger. It contains no `workflow_dispatch`, `schedule`, `repository_dispatch`, or `workflow_call`. Automatic push routing is limited to:
- branches `main` and `planning/issue-547`;
- paths: the diagnostic workflow, diagnostic helper, and exact reviewed provider-authority input contract.

The remediation branch is needed only to exercise the non-secret synthetic branch job before publication. The protected job is independently hard-gated to `refs/heads/main`.

## Independent mechanical verification

Final remediation run `32006507660`, attempt 1:
- exact source `474f70ff19ccf6dfa36cf0168174af10731cc523` before handoff-only commit;
- branch-selftest job `95316976501`: success;
- trusted-main-diagnostic job `95316977340`: skipped on the remediation branch;
- GITHUB_TOKEN permissions in logs: `Contents: read`, `Metadata: read`;
- exact input-contract Git blob check passed;
- one-shot structural assertion passed;
- `python3 -m py_compile tools/planning/unity_license_config_diag.py` passed;
- all seven deterministic helper self-tests passed;
- artifact `9280192186`;
- GitHub artifact digest `sha256:ead9b3542f2800b927c3686e50a27e0f12c426292c2414822f294364b78aaf3e`;
- independent artifact download reproduced exactly the same ZIP SHA-256;
- contained `selftest.json` SHA-256 `6bb40ee940a66c16816a3e86d0309f0c1da4cfc79086b40b2833d02b61cf6ad2`.

The two earlier remediation runs `32006316758` and `32006442044` failed only in self-referential structural assertions. In both, the protected trusted-main job was skipped. They carry no provider result and no secret/license value exposure. The final exact candidate supersedes those failed synthetic checks.

## Security / authority attacks

### PASS — trigger determinism

No manual, scheduled, repository-dispatch, or workflow-call route remains. A protected diagnostic can therefore be created by this workflow only when the reviewed diagnostic surfaces are published/changed on `main`. Later provider-evidence, S7, content, or unrelated main pushes do not match the path filter.

### PASS — protected-environment separation

Exactly one YAML job declaration contains `environment: engine-eval`, and it is the trusted-main job. The remediation-branch job has no environment and no secret expressions. Final branch execution proves the trusted job is skipped on the planning branch.

### PASS — least privilege and no repository recursion

Workflow permissions are `contents: read` only. The trusted job has no git commit/push, contents write, pull-request write, Actions write, recorder invocation, or evidence-branch creation. It emits only a runner-temporary bounded diagnostic plus an immutable Actions artifact.

### PASS — helper identity and contract semantics

Helper blob `fd8097ec314826265484c5d0a5b1aa0bf184a791` is byte-identical to the helper reviewed in the #539/#543 episode. The remediation did not change credential/presence semantics.

The helper re-computes and requires exact input-contract blob `a4c40fe1...`, preserves exactly the three declared modes, accepts only non-secret mode plus boolean presence flags, has no API for provider/license values, and fixes provider/license/editor/integration/canonical authority to false/noncanonical.

### PASS — raw-help and secret boundary

Unity CLI is pinned to `1.0.0-beta.5`. Raw non-secret help is captured before protected presence evaluation, remains runner-temporary, and only normalized option/subcommand names, exit codes, byte counts and raw-help SHA-256 are persisted. Protected input expressions produce only booleans `${{ secrets.NAME != '' }}` plus non-secret `UNITY_AUTH_MODE`; no credential/license value, value hash, substring, or length enters the helper.

### PASS — provenance / `issue: 539`

The helper retains logical diagnostic root `mission_id=W2-ENG-PROVIDER-UNITY-LICENSE-CONFIG-MAIN-DIAG-01` and `issue=539`. This is acceptable and not an authority ambiguity: #547 is explicitly the bounded remediation of that diagnostic design, while every future protected artifact also binds the exact trusted-main `GITHUB_SHA`, workflow run id/attempt, helper hash in run identity, and exact contract blob. Downstream routing must bind the publication/integration SHA and run identity, not use the logical issue field alone. Changing this provenance field in the trigger-only remediation would have unnecessarily widened the reviewed semantic surface.

## Conclusion

The exact #547/#551 candidate closes the prior MAJOR and is safe for a separately governed squash-only publication. Review PASS does not itself integrate the candidate and does not establish any provider authentication, Unity license validity, editor/native execution eligibility, engine selection, readiness, verification-PASS, release, decision, or canonical authority.

After reviewed publication, the path-scoped trusted-main protected diagnostic artifact is the required fresh verification input. Its bounded disposition may route either already-present-mode effective wiring or an exact missing configuration predicate.

Mandatory reopen condition for trust profile: `MULTI_AGENT_OR_ISOLATED_CONTEXT_AVAILABLE`.
