# W2-ENG-PROVIDER-RECORDER-IDENTITY-REM-REV-01 — required review

## Review identity

- review issue: #593
- mission: `W2-ENG-PROVIDER-RECORDER-IDENTITY-REM-REV-01`
- task class: `REQUIRED_REVIEW`
- trust mode: `DEGRADED_SINGLE_AGENT`
- reviewer claim: `5317428413`
- review base: `main@85974cc21f1e3c5c3f189fa6da573a11dc381efb`
- canonical binding: Issue #6 comment `5245368879`
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`

The reviewer ownership episode is distinct from producer actor `frontier-drain-provider-recorder-identity-rem-590-gpt56sol-20260817-01`, but stronger human/process isolation is unavailable. This report therefore does not claim full independence.

## Frozen judged candidate

Issue #590 / `W2-ENG-PROVIDER-RECORDER-IDENTITY-REM-01` is immutable judged provenance:

- producer claim: `5317379253`
- producer terminal `STATUS(REVIEW_READY)`: `5317402024`
- producer branch: `planning/issue-590`
- producer base: `85974cc21f1e3c5c3f189fa6da573a11dc381efb`
- substantive remediation commit: `6ee17a8b4352e5ea39c429ea48c3e9a88a687a11`
- exact terminal head: `00fa25decf16bf2774b76ebb353e0ed7c75d46f4`
- exact draft PR: #592, open/draft/mergeable at the exact terminal head, base `main@85974cc21f1e3c5c3f189fa6da573a11dc381efb`
- input recorder workflow blob: `8262841a9f944b8695f77a54a003d4f8905fd884`
- corrected recorder workflow blob: `41f60d2b01bd2990331ab11435d2dc40315dd919`
- producer handoff blob: `0b0c3f005472d920fba0bfb3eedf7c09a831c793`

PR #592 reports exactly two changed files. Cold commit inspection proves the substantive commit changes only `.github/workflows/engine-eval-evidence-recorder.yml` and the terminal commit adds only `docs/planning/handoffs/issue-590.md`.

## Historical failure provenance

Fresh API inspection retains the historical states exactly:

- evaluator run `32042580744`, attempt 1: `completed/success`, event `push`, branch `main`, head `85974cc21f1e3c5c3f189fa6da573a11dc381efb`, workflow id `335536370`, path `.github/workflows/engine-eval-credentialed.yml`;
- recorder run `32042595018`, attempt 1: `completed/failure`, event `workflow_run`, branch `main`, head `85974cc21f1e3c5c3f189fa6da573a11dc381efb`;
- recorder job/check `95424460816` retains the exit-code-1 failure annotation;
- the same check separately retains the pinned `actions/download-artifact` HTTP 429 warning and retry-backoff warning.

The 429 warning is independent infrastructure provenance. This review neither attributes the identity defect to the 429 nor erases the 429 because the identity defect is repaired.

## Independent defect reproduction

Against exact current/source SHA `85974cc21f1e3c5c3f189fa6da573a11dc381efb`, a cold call to GitHub's REST compare resource for the identical SHA returns HTTP 404. The historical recorder called this endpoint unconditionally after reading current `main`, so exact source/current-main identity could fail before checkout and projection even though ancestry was already proven by equality.

The defect is therefore real and bounded to the unnecessary identical-SHA compare call.

## Exact remediation diff

Cold inspection of substantive commit `6ee17a8b4352e5ea39c429ea48c3e9a88a687a11` proves the complete workflow patch is exactly:

```diff
 branch = get('branches/main')
 publication_base = (branch.get('commit') or {}).get('sha')
-compare = get(f"compare/{expected_head}...{publication_base}")
-if (compare.get('merge_base_commit') or {}).get('sha') != expected_head:
-    raise SystemExit('source head is no longer an ancestor of current main')
+if publication_base != expected_head:
+    compare = get(f"compare/{expected_head}...{publication_base}")
+    if (compare.get('merge_base_commit') or {}).get('sha') != expected_head:
+        raise SystemExit('source head is no longer an ancestor of current main')
```

The commit contains 4 additions and 3 deletions in that one file. No other executable line changes.

## Required attacks

### A1 — exact-head bypass is narrowly scoped

**PASS.** Equality is checked only after the recorder independently fetches current `branches/main` and after all upstream Actions-run/workflow identity checks have succeeded. If `publication_base == expected_head`, exact identity itself establishes the source is current main at that observation point. Only the redundant compare call is skipped.

There is no bypass of run id, run attempt, workflow name, event, completed status, success conclusion, head branch, head SHA, repository, workflow id, or exact workflow path.

### A2 — distinct-head ancestry remains fail closed

**PASS.** For every `publication_base != expected_head` case the original compare call remains. Success still requires `(merge_base_commit.sha == expected_head)` exactly. A descendant with exact merge base passes; a diverged/non-ancestor merge base rejects; missing/null merge-base data also rejects.

Independent semantic fixtures executed by this reviewer confirmed:

- identical head: pass with zero compare calls;
- distinct descendant + exact source merge base: pass with one compare call;
- distinct diverged merge base: reject with `source head is no longer an ancestor of current main`;
- distinct head + missing merge base: reject with the same fail-closed error.

### A3 — upstream identity predicates unchanged

**PASS.** Exact cold reads of input blob `8262841...` and corrected blob `41f60d2...`, plus the one-hunk commit patch, prove all upstream run/workflow predicates are unchanged outside the ancestry hunk. The recorder still requires:

- exact run id and run attempt;
- evaluator workflow name;
- `push` event;
- `completed/success`;
- head branch `main`;
- exact head SHA;
- exact repository identity;
- exact workflow id;
- exact trusted workflow path `.github/workflows/engine-eval-credentialed.yml`.

### A4 — downstream projection/publication controls unchanged

**PASS.** Because the substantive workflow commit has exactly one hunk and no other executable changes, all downstream controls remain byte-identical to the reviewed input:

- checkout exact `github.event.workflow_run.head_sha`;
- require checked-out HEAD equals source head;
- require trusted workflow path and projection script exist;
- compile projection code and require clean worktree before projection;
- download only the exact run/attempt artifact name using exact run id;
- project with exact source/run/workflow/publication-base identities;
- require exactly one untracked bounded generated evidence path after projection;
- create immutable `evidence/provider-effective-access/run-${RUN_ID}-attempt-${RUN_ATTEMPT}` branch;
- stage exactly the generated evidence path;
- push only the evidence branch, never `main`;
- preserve `draft_pr_created_by_workflow: false`, `draft_pr_required: true`, and `SEPARATE_NORMAL_OWNERSHIP_EPISODE_OPENS_DRAFT_PR`;
- preserve `integration_authority: false`.

### A5 — historical outcomes are not laundered

**PASS.** Producer handoff and terminal status explicitly retain evaluator success and recorder failure. The remediation does not rewrite or reinterpret the old run. A later trusted-main execution is required to exercise the corrected recorder in protected publication context.

### A6 — infrastructure warning remains separate

**PASS.** The producer records the HTTP 429 warning as separate infrastructure provenance. The remediation touches no action pins, retry behavior, artifact download step, or network behavior.

### A7 — scope and authority

**PASS.** Exact commit history proves no evaluator workflow, provider validator, provider contract, generated provider evidence, credentials, Unity/Unreal state, S6 evidence, or unrelated planning artifact was modified. PR draft/mergeability is compatibility only and grants no publication authority.

No provider credential/PASS, Unity license, Unreal entitlement, provider-evidence integration, engine selection, implementation/readiness, production/commercial/legal/release, verification-PASS, decision, integration, or canonical authority is inferred.

## Findings

- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0

No material defect was found in the exact bounded remediation.

## Disposition

`PASS_BOUNDED_PROVIDER_RECORDER_IDENTITY_REMEDIATION`

Exact Issue #590 / PR #592 is clean for a **separately authorized squash-only publication episode** under then-current main/head/authority checks. This disposition is review provenance only; it is not integration authority.

After any authorized publication, a fresh trusted-main execution must still demonstrate the corrected recorder in its protected runtime context. That future execution must preserve historical run `32042595018` as failure provenance and must not infer provider PASS merely from recorder success.

## Authority boundary

`NOT_CANONICAL`. Required review only. No remediation authorship, provider credential/PASS, provider-evidence integration, engine selection, implementation/readiness, production/commercial/legal/release, verification-PASS, direct integration authority, decision, or canonical authority.