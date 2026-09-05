# Required security/authority review — Issue #859

## Frozen review identity

- mission: `W2-ENG-TECH-UNITY-S3-V5-RECORDER-TRIGGER-REM-02-REV-01`;
- task class: `REQUIRED_SECURITY_AUTHORITY_REVIEW`;
- trust mode: `DEGRADED_SINGLE_AGENT`;
- reviewer ownership: Issue #859 comment `5551671778`;
- current-main basis: `88b704183e99dbd0dd102131c67a99fd0013ff36`;
- canonical binding: Issue #6 comment `5245368879`;
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- judged producer: Issue #845 terminal comment `5550540041`;
- judged PR: #853;
- judged branch/head: `planning/issue-845@53463beff138d5854f4268c5be20cdc11554716a`;
- producer source finding: `W2-ENG-TECH-UNITY-S3-V5-RECORDER-TRIGGER-REV-M01` from Issue #843 terminal comment `5536070954`.

The producer head is immutable review input. This review did not modify the producer branch, launch native Unity, integrate anything, or grant verification/comparison/decision/canonical authority.

## Disposition

`CHANGES_NEEDED`

Counts:

- BLOCKER: 0
- MAJOR: 1
- correction-requiring MINOR: 0
- informational: 0

## Finding `W2-ENG-TECH-UNITY-S3-V5-RECORDER-TRIGGER-REM02-REV-M01` — MAJOR

### Evidence-branch publication has no usable Git authentication

The remediation correctly separates recorder execution into a GitHub-hosted `workflow_dispatch` run and correctly grants that recorder `contents: write`. However, both recorder checkouts explicitly set `persist-credentials: false`, and the publication step later executes only:

```text
git push origin "HEAD:refs/heads/$EVIDENCE_BRANCH"
```

There is no later credential-helper setup, authenticated push URL, `http.extraheader`, or other explicit injection of `${{ github.token }}` for that Git operation. On the fresh GitHub-hosted recorder runner, the checkout action therefore does not leave the repository authentication material that the plain `git push origin` relies on.

This is a liveness/correctness failure in the exact required lifecycle: a source evaluator may become exact-current-main `completed/success`, the recorder may pass all source/artifact/projection gates, and the final immutable evidence-branch publication can still fail because the write-capable token is never presented to Git.

The regression is introduced by the reviewed packet. The current-main predecessor recorder's source-head checkout did not disable persisted credentials; the reviewed producer changes the relevant checkout to `persist-credentials: false` while preserving the unchanged plain push command.

The producer's deterministic validator does not catch this. It requires the recorder to contain `contents: write`, the immutable evidence branch name, and the one-file staged guard, but it has no assertion or negative control proving that the publication command has a bounded authenticated path. The producer handoff likewise states that persisted credentials are disabled and then claims immutable-branch publication is preserved, without accounting for Git authentication.

### Required correction

Route one bounded remediation that restores authenticated evidence-branch publication on the GitHub-hosted recorder without weakening the native Unity trust boundary or exposing a write-capable token to the persistent self-hosted runner. The correction should keep authentication narrowly scoped to the publication operation or otherwise justify the exact hosted-runner credential lifetime; it must not log the token, broaden repository write authority, enable direct-main publication, or create an automatic PR.

Add deterministic/static coverage that fails when the recorder has `persist-credentials: false` plus an unauthenticated plain push, and proves the selected bounded authenticated publication mechanism remains confined to the GitHub-hosted recorder publication path.

## Other reviewed boundaries

The original temporal deadlock is materially corrected: the evaluator's native `lineage` job remains read-only on the persistent Unity runner, a separate GitHub-hosted post-lineage job holds only `actions: write` and dispatches the recorder, and the recorder is a distinct `workflow_dispatch` run. The shared source gate bounds `queued`/`in_progress` polling, requires exact terminal `completed/success`, validates run/attempt/workflow/path/repository/head identities, and requires source head plus recorder workflow code to equal exact current `main` before projection/publication.

Manual or replayed recorder inputs do not by themselves satisfy those gates: they still have to resolve to the exact successful evaluator run and exact current-main identity. The artifact name/run/attempt binding, projection-code identity, one-file staged-path guard, no automatic PR, and authority negatives are otherwise preserved by the reviewed bytes.

Those clean sub-findings do not offset the publication MAJOR because the evidence handoff cannot be relied on to complete.

## Required next route

Exactly one bounded blocking-remediation successor for `W2-ENG-TECH-UNITY-S3-V5-RECORDER-TRIGGER-REM02-REV-M01`.

After correction, require a fresh exact-head independent/degraded-independent security/authority review. Only a clean future `PASS_FOR_INTEGRATION` may route a separate authorized squash-only publication, followed by fresh exact-main end-to-end verification.

`NOT_CANONICAL`. No provider PASS, `PASS_FOR_COMPARISON`, aggregate verification PASS, engine selection/readiness, implementation, production/release, integration, decision, or canonical authority is granted by this review.
