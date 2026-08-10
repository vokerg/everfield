issue: 16
role: Planning Program v1 final bootstrap liveness remediation
branch: planning/issue-16
base_sha: c822934c74cc5903b057e6d081f5e0a4c3e58226
work_sha: 5b1f4e91904e46e5311b0f9cb3318c32402d53a7
state: VERIFICATION_READY
completed:
  - Accepted and corrected V5-B08 without weakening exact-current-base verification.
  - Added deterministic composite candidate over Issue #14 base candidate blob 9829975eb3b8ac12b7dd8338a3569ff1a50cf309.
  - Excluded Issue #14 non-canonical status/provenance/downstream sections from the future canonical composition while preserving Sections 2-23 with explicit Section 13/19 overrides.
  - Added deterministic manifest composition over base manifest blob 1f062de59afcfe8496b4cff0fdff594c2d5fd50c with explicit source/target path resolution and replace/extend/append semantics.
  - Added generic schema-3 VERIFICATION_RESTART for changed candidate/manifest after terminal verification.
  - Added generic schema-3 VERIFICATION_REFRESH for unchanged-candidate PASS invalidated solely by descendant main movement.
  - Required both transitions to serialize by exact source/tuple/base/head and lowest valid GitHub comment ID, creating one new ownership generation.
  - Required full normal verification evidence and FULL/DEGRADED independence profile after either restart or refresh; neither is a compatibility waiver.
  - Added exact-current-base verification binding selection and Issue #6 eligibility override.
  - Bound the current Issue #5 re-entry to formal FAIL comment 5244679631 and Issue #16 remediation through VERIFICATION_RESTART.
  - Preserved all V5-B03 through V5-B07 corrections, Wave 1 graph, squash-only integration, and implementation barrier through immutable base adoption.
remaining:
  - Bootstrap Issue #5 must re-enter with VERIFICATION_RESTART after this payload is durable on current main and run full verification.
  - Issue #6 remains blocked until the highest valid exact-current-base Issue #5 result for this effective candidate is PASS with zero BLOCKER/MAJOR.
checks_performed:
  - Simulated PASS(C,A) -> main B -> VERIFICATION_REFRESH -> full verify -> PASS/FAIL(B).
  - Simulated repeated base drift requiring another refresh.
  - Simulated candidate change after FAIL/PASS and verified refresh is invalid while restart is required.
  - Checked competing restart/refresh contenders have deterministic one-owner selection.
  - Checked older-base PASS cannot satisfy Issue #6 current-base selection.
  - Checked current Issue #5 formal FAIL 5244679631 supplies a valid source for post-Issue16 VERIFICATION_RESTART.
  - Checked composition excludes Issue #14 Sections 1, 24, 25 to prevent stale non-canonical/downstream instructions in future canonical wrapper.
  - Checked manifest composition source paths resolve in overlay and target paths in evolving effective base; conflicts/missing targets fail closed.
  - Checked Issue #14 root phase/canonical-binding/schema-3/degraded-independence corrections remain inherited.
  - Checked no gameplay/Wave1 issues created and every main integration remains squash-only.
evidence:
  - docs/planning/11-planning-program-v1-bootstrap-final-candidate.md blob d083e5bfa108360818898f9628e939f50b4f3940
  - docs/planning/11-planning-program-v1-canonicalization-manifest.yaml blob bca34638a054d725239b936dd8232a7d274e814d
  - docs/planning/reviews/issue-5-final-verification-finding-dispositions.md
  - Issue #5 formal schema-3 FAIL comment 5244679631
known_problems:
  - Verification churn under frequent main movement may eventually justify an integration lock/scheduler primitive; current refresh path is correct but potentially expensive.
  - DEGRADED_SINGLE_AGENT remains weaker than true isolated independent review and must reopen when stronger capability exists.
  - Git expected-parent fencing remains procedural pending later control-plane work.
decisions:
  - Keep base movement fail-closed; solve liveness with full verification refresh rather than compatibility waiver.
  - Use full verification restart whenever candidate/manifest/adopted payload changes.
  - Use immutable exact-base composition to preserve already-tested Issue #14 semantics rather than restating the full protocol.
  - Keep Issue #16 candidate NON-CANONICAL pending Issue #5 PASS and Issue #6 terminal binding.
scope_deviations:
  - None.
recommended_next_action: After clean pre-merge review, squash-integrate Issue #16 as non-canonical provenance, then post VERIFICATION_RESTART on Issue #5 from source FAIL 5244679631 for the exact Issue #16 payload/current main and run full verification.

## Note on head SHA

`work_sha` is the final substantive remediation commit before this handoff. Final Issue #16 STATUS must record the later branch head containing this handoff.