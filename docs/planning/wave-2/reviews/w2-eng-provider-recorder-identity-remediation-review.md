# W2-ENG-PROVIDER-RECORDER-IDENTITY-REM-REV-01 — recovered required review

## Fresh review identity

- review issue: #593
- mission: `W2-ENG-PROVIDER-RECORDER-IDENTITY-REM-REV-01`
- task class: `RECOVERY_CONTINUATION -> REQUIRED_REVIEW`
- trust mode: `DEGRADED_SINGLE_AGENT`
- mature orphan probe: `5317529728`
- winning recovery intent: `5325439203`
- ownership generation: `RECOVER 5325442322`
- recovered branch: `planning/issue-593`
- recovered starting head: `6335e3da12fc45449170acf8c692436b7ea7aaa2`
- review base/current main at recovery: `85974cc21f1e3c5c3f189fa6da573a11dc381efb`
- canonical binding: Issue #6 comment `5245368879`
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`

The earlier #593 claim `5317428413`, report bytes, terminal status `5317442088`, and PR state were produced before Issue #590 had a valid schema-3 terminal ownership/status generation. Issue #593 comment `5317529070` therefore correctly fixes them as zero-authority historical review provenance. This report does not upgrade that episode. It records a fresh review performed only after producer recovery/terminalization and after canonical orphan recovery of this review branch.

The recovered reviewer episode is distinct from the valid producer recovery episode. Stronger human/process isolation is unavailable, so this review does not claim full independent isolation.

## Frozen judged candidate

The fresh judged producer identity is Issue #590 after its canonical orphan recovery:

- producer recovery ownership: `5317519858`
- valid producer terminal `STATUS(REVIEW_READY)`: `5317527323`
- producer branch: `planning/issue-590`
- producer exact terminal head: `00fa25decf16bf2774b76ebb353e0ed7c75d46f4`
- producer draft PR: #592, freshly observed open/draft/unmerged/mergeable at that exact head, base `main@85974cc21f1e3c5c3f189fa6da573a11dc381efb`
- changed paths exactly `.github/workflows/engine-eval-evidence-recorder.yml` and `docs/planning/handoffs/issue-590.md`
- input recorder workflow blob: `8262841a9f944b8695f77a54a003d4f8905fd884`
- corrected recorder workflow blob: `41f60d2b01bd2990331ab11435d2dc40315dd919`
- producer handoff blob: `0b0c3f005472d920fba0bfb3eedf7c09a831c793`

The producer branch is immutable judged input for this review and was not edited.

## Fresh historical-failure verification

The recovered review re-fetched the historical execution directly rather than relying on the old review report:

- evaluator run `32042580744`, attempt 1: `completed/success`, event `push`, branch `main`, exact head `85974cc21f1e3c5c3f189fa6da573a11dc381efb`, workflow id `335536370`;
- recorder run `32042595018`, attempt 1: `completed/failure`, event `workflow_run`, branch `main`, the same exact head;
- recorder job `95424460816`: step `Bind exact upstream workflow, run, and trusted-main identity` failed; all checkout/projection/publication steps were skipped.

Fresh decoded job-log inspection shows the raw recorder call reached the unconditional `compare/{expected_head}...{publication_base}` call with both values equal to `85974cc21f1e3c5c3f189fa6da573a11dc381efb`, then `urllib.request.urlopen` raised `HTTP Error 404: Not Found` and the step exited 1. The same log separately records an `actions/download-artifact` download warning `429 (Too Many Requests)` followed by retry backoff before the recorder step began. The 429 is therefore separate infrastructure provenance, not the identity-check failure.

## Fresh exact-diff attack

PR #592 was freshly fetched. Its only executable workflow change is exactly this ancestry hunk:

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

Fresh full-file reads of input blob `8262841a...` and corrected blob `41f60d2b...` confirm no other recorder executable line changed. The second PR path is the producer handoff only.

## Fresh semantic fixtures

The recovered review independently exercised the corrected predicate with a comparison callback instrumented for call count and result shape:

- exact source/current-main identity: PASS with **zero** compare calls;
- distinct descendant current main with `merge_base_commit.sha == expected_head`: PASS with exactly one compare call;
- distinct diverged/non-ancestor merge base: FAIL CLOSED with `source head is no longer an ancestor of current main`;
- distinct head with missing merge-base object: FAIL CLOSED with the same error;
- distinct head with null merge-base object: FAIL CLOSED with the same error.

A repository compare read for the two equal SHAs also reports them as `identical`, `ahead_by: 0`, `behind_by: 0`, with merge base equal to the source SHA. This is corroborative topology evidence only; the historical raw `urllib` 404 above is the execution-specific failure provenance being remediated.

## Required attacks

### A1 — exact-head bypass is narrow

**PASS.** The equality test occurs only after exact repository/run/workflow identity checks and a fresh read of `branches/main`. Equality of `publication_base` and `expected_head` is itself the strongest possible ancestry relation, so skipping only the redundant compare request does not weaken source identity.

### A2 — distinct-head ancestry remains fail closed

**PASS.** Every unequal-head case executes the original compare request and retains the exact requirement `merge_base_commit.sha == expected_head`. Diverged, missing, and null merge-base controls reject.

### A3 — upstream run/workflow identity remains exact

**PASS.** Full-file comparison proves the remediation does not change checks for run id, run attempt, workflow name, event `push`, `completed/success`, branch `main`, exact source SHA, repository, workflow id, or exact evaluator workflow path.

### A4 — downstream source/projection/publication controls remain unchanged

**PASS.** Outside the one ancestry hunk, the corrected workflow remains byte-identical to the input. It still:

- checks out the exact upstream source SHA;
- verifies checked-out HEAD and projection-script/workflow identity;
- compiles projection source without worktree side effects and requires a clean tree before projection;
- downloads the exact run/attempt artifact;
- binds source/run/workflow/publication-base identities into projection;
- requires exactly one bounded generated evidence path;
- stages exactly that path;
- publishes only the immutable run/attempt evidence branch, never `main`;
- preserves `draft_pr_created_by_workflow: false`, `draft_pr_required: true`, `SEPARATE_NORMAL_OWNERSHIP_EPISODE_OPENS_DRAFT_PR`, and `integration_authority: false`.

### A5 — historical outcomes remain immutable

**PASS.** Fresh API/run/log reads preserve evaluator `32042580744` as success and recorder `32042595018` / job `95424460816` as failure. The remediation does not rewrite historical evidence. Runtime validation of the correction still requires a future trusted-main execution after any separately authorized publication.

### A6 — infrastructure provenance is not laundered

**PASS.** The 429 warning is independently visible in the historical job log and remains separate from the subsequent 404 identity failure. The remediation touches neither action pins nor artifact-download behavior.

### A7 — scope and authority remain bounded

**PASS.** PR #592 remains exactly two files; only one executable ancestry hunk changes. No evaluator/provider validator or contract, generated provider evidence, credential boundary, Unity/Unreal state, S6 evidence, or unrelated planning artifact changes. Draft/mergeable state is compatibility information only and grants no integration authority.

## Findings

- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0

No material defect was found in the exact recovered producer candidate.

## Disposition

`PASS_BOUNDED_PROVIDER_RECORDER_IDENTITY_REMEDIATION`

Valid recovered Issue #590 / PR #592 is clean for bounded consumption by a **separately authorized squash-only publication episode** under then-current ownership, main/head, review, and integration-authority checks. This required review itself grants no integration authority.

After any authorized publication, one fresh trusted-main evaluator/recorder episode remains necessary to verify protected-runtime behavior of the corrected recorder. A successful recorder run would establish recorder execution only; it must not be inflated into provider PASS, Unity licensing, Unreal entitlement, engine selection, implementation/readiness, verification-PASS, release, decision, or canonical authority.

## Authority boundary

`NOT_CANONICAL`. Recovered required review provenance only. No remediation authorship, provider credential/PASS, provider-evidence integration, engine selection, implementation/readiness, production/commercial/legal/release, verification-PASS, direct integration authority, decision, or canonical authority.