# Issue 398 handoff — effective provider access required review

```yaml
protocol: planning-v1
schema: 3
kind: HANDOFF
issue: 398
mission_id: W2-ENG-PROVIDER-EFFECTIVE-REV-01
branch: planning/issue-398
state: REVIEW_READY
review_mode: DEGRADED_SINGLE_AGENT
disposition: CHANGES_NEEDED
findings:
  blocker: 0
  major: 2
  correction_requiring_minor: 0
judged_producer_issue: 373
judged_producer_terminal_comment_id: 5306084733
judged_producer_head_sha: 75728cade4c1646f9a1006e89ccc026234958a2b
judged_producer_pr: 397
claim_comment_id: 5306201352
review_base_sha: 56f8ac296d1eb779a9e684edda0e8a822691a8bf
canonical_program_blob_sha: e3120ec203c4156328770aa86c12fbb7187966dc
canonical_binding_comment_id: 5245368879
canonical_activation_sha: 413e729e8d2d5ac2eb138903f3f2ace07283b23e
integration_authority: false
canonicality: NOT_CANONICAL
```

## Result

Fresh security/authority review of exact Issue #373 / PR #397 returns `CHANGES_NEEDED` with two MAJOR findings:

1. `W2-ENG-PROVIDER-EFFECTIVE-REV-M01`: the evidence recorder uses `contents: write` and directly commits/pushes `HEAD:main`, bypassing the repository's ownership, reviewed-publication, exact-head, and squash-only integration authority model.
2. `W2-ENG-PROVIDER-EFFECTIVE-REV-M02`: evaluator and recorder both check out moving `main`, while evidence is labeled with the upstream event `head_sha`; the consumer also binds the producer by display name rather than proving an exact trusted workflow/code identity. A moving-main race can therefore make the recorded source identity differ from the code that actually produced or projected the evidence.

The full report is `docs/planning/wave-2/reviews/w2-eng-provider-effective-access-review.md`.

## Clean boundaries retained

- Unity and Unreal remain independent provider predicates.
- Local Unity S3 evidence remains local-only and is not promoted to hosted-CI validation.
- Unreal entitlement remains a narrowly scoped external prerequisite and does not block non-secret Unreal preparation or unrelated engines/scenarios.
- The credentialed evaluator has no PR/fork secret-bearing trigger, uses `engine-eval`, and keeps `contents: read`.
- Historical Issue #82's 50 `NOT_RUN` cells remain immutable.
- No commercial/production/legal/release, engine-selection, readiness, verification-PASS, integration, decision, or canonical authority is granted.

## Required next gate

Route exactly one bounded blocking remediation successor `W2-ENG-PROVIDER-EFFECTIVE-REM-01` addressing only M01/M02 plus minimum consistency updates. The remediation must remove direct main self-publication, bind evaluator/consumer execution to exact reviewed source identities, preserve the clean provider/security boundaries above, and then receive a fresh required review.

No Epic credential or resolved Unity ephemeral-license route is required to perform this remediation.