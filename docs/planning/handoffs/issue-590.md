# Issue 590 handoff — W2-ENG-PROVIDER-RECORDER-IDENTITY-REM-01

## Terminal candidate

- issue: #590
- mission: `W2-ENG-PROVIDER-RECORDER-IDENTITY-REM-01`
- task class: `BLOCKING_REMEDIATION`
- branch: `planning/issue-590`
- winning claim: `5317379253`
- base: `85974cc21f1e3c5c3f189fa6da573a11dc381efb`
- substantive remediation commit: `6ee17a8b4352e5ea39c429ea48c3e9a88a687a11`
- input recorder workflow blob: `8262841a9f944b8695f77a54a003d4f8905fd884`
- corrected recorder workflow blob: `41f60d2b01bd2990331ab11435d2dc40315dd919`
- terminal head: bind the exact SHA containing this handoff from the terminal schema-3 status and exact PR head.
- canonical binding comment: `5245368879`
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- canonicality: `NOT_CANONICAL`

## Frozen failure provenance

Authorized squash publication Issue #584 produced `main@85974cc21f1e3c5c3f189fa6da573a11dc381efb`. That exact push produced evaluator run `32042580744`, attempt 1, success, at exact source/head `85974cc21f1e3c5c3f189fa6da573a11dc381efb`. The downstream recorder run `32042595018`, attempt 1, job `95424460816`, failed in `Bind exact upstream workflow, run, and trusted-main identity` before checkout, artifact download, projection, or evidence-branch publication.

Check annotations also contain a GitHub-side pinned-action download `429 Too Many Requests` warning. That infrastructure warning is preserved separately and is not treated as the identity defect.

## Exact remediation

The prior recorder unconditionally called the GitHub compare endpoint after reading current `main`. When the evaluator source SHA and current-main SHA were identical, the endpoint returned 404 for the identical-SHA comparison even though ancestry was trivially satisfied by exact identity.

The correction changes only that predicate:

```python
if publication_base != expected_head:
    compare = get(f"compare/{expected_head}...{publication_base}")
    if (compare.get('merge_base_commit') or {}).get('sha') != expected_head:
        raise SystemExit('source head is no longer an ancestor of current main')
```

Therefore exact SHA identity bypasses the unnecessary compare call, while every distinct-head case retains the original fail-closed merge-base test.

No other recorder identity, checkout, artifact, projection, worktree, evidence-branch, staged-path, or authority behavior was changed.

## Deterministic non-secret verification

The workflow was reconstructed from the exact frozen input and the pre-change reconstruction recomputed Git blob `8262841a9f944b8695f77a54a003d4f8905fd884`, proving byte identity before the bounded edit. The corrected full workflow recomputed Git blob `41f60d2b01bd2990331ab11435d2dc40315dd919`, matching the committed GitHub blob.

Executed local non-secret checks against the exact corrected workflow text:

- YAML parse: PASS.
- Embedded Python heredoc compilation: PASS for all three Python blocks.
- identical head: PASS; comparison callback was not invoked.
- distinct descendant head: PASS only with `merge_base_commit.sha == expected_head`.
- distinct diverged/non-ancestor head: PASS as a negative control; the check raised exact `source head is no longer an ancestor of current main`.

No provider secret, protected environment, authentication, or provider execution was used by this remediation verification.

## Scope

Changed paths are exactly:

- `.github/workflows/engine-eval-evidence-recorder.yml`
- `docs/planning/handoffs/issue-590.md`

The evaluator workflow, provider validators/contracts, generated provider evidence, credentials, Unity/Unreal state, and S6 evidence remain untouched.

## Required next route

A fresh required independent/degraded-independent review must inspect the exact terminal #590 head. It must verify that exact-head identity avoids the compare API, distinct-head ancestry remains fail closed, all other recorder security/publication boundaries are unchanged, historical evaluator/recorder outcomes are not relabeled, and no provider or integration authority is inflated.

No publication or integration is authorized by this remediation or handoff. Any later publication remains separate and squash-only under then-current authority.

## Authority boundary

`REVIEW_READY` remediation provenance only. No provider credential/PASS, provider-evidence integration, Unity license, Unreal entitlement, engine selection, implementation/readiness, production/commercial/legal/release, verification-PASS, decision, or canonical authority.