issue: 4
role: Planning synthesizer / revision agent
branch: planning/issue-4
head_sha: 1d7b9a980e74d6999789c86694f3c7fb99e13b99
base_sha: 21a3c1a5053f3697be3f82f6fe73de42423a482b
state: REVIEW_READY
completed:
  - Re-entered from current main after Issue #3 squash integration and re-read AGENTS.md, docs/planning/START-HERE.md, and Issue #4.
  - Claimed planning/issue-4 deterministically from main@21a3c1a5053f3697be3f82f6fe73de42423a482b.
  - Consumed the complete Issue #2 proposal set and Issue #3 adversarial review.
  - Produced one coherent reviewed candidate at docs/planning/08-planning-program-v1-reviewed-candidate.md rather than another amendment layer.
  - Produced docs/planning/reviews/issue-3-finding-dispositions.md covering every Issue #3 finding.
  - Accepted and corrected all 5 BLOCKER and all 6 MAJOR findings; no BLOCKER/MAJOR was silently deferred or rejected.
  - Added docs/planning/08-planning-program-v1-canonicalization-manifest.yaml as the machine-readable verified promotion and exact Wave 1 mission/issue contract source.
  - Added orphan-branch recovery, append-only/server-time capsule validation, ownership generations, stale-writer fencing, review-disposition transition predicates, context budgets, single-use recovery episodes, verified-base pinning, post-merge Wave 1 instantiation, and hard next-wave governors.
  - Corrected an Issue #4 self-review finding so domain syntheses complete REVIEW_READY while only final synthesis/bootstrap final candidates proceed to verification readiness.
  - Empirically checked the current GitHub comment REST resource and confirmed immutable comment ID plus created_at/updated_at are available for capsule ordering/edit detection.
remaining:
  - Bootstrap Issue #5 must independently cold-start verify the exact Issue #4 work state and current main base.
  - Bootstrap Issue #6 remains blocked unless Issue #5 records PASS for the exact candidate/manifest/base tuple.
checks_performed:
  - Mapped every Issue #3 BLOCKER/MAJOR to an explicit ACCEPTED correction in the disposition artifact.
  - Re-checked Issue #4 required-output bullets against candidate sections 9-23 and the machine-readable manifest.
  - Re-checked cold-start task selection, claim/orphan/stale recovery, mutation fencing, handoff, review transitions, context loading, canonicalization, garbage collection, and implementation-readiness guardrails for internal consistency.
  - Verified the manifest enumerates 23 initial Wave 1 missions: 12 roots, 3 domain reviews, 3 domain syntheses, cross review, final synthesis, verifier, canonicalizer, and one recovery task.
  - Verified domain synthesis completion_state is REVIEW_READY and W1-SYN-FINAL completion_state is VERIFICATION_READY.
  - Verified Issue #6 Wave 1 creation is forbidden before squash merge and uses the concrete resulting main SHA before final DONE.
  - Verified canonical promotion binds candidate, manifest, and verified_base_main_sha and preserves squash-only integration.
  - Verified no gameplay code, final engine choice, mass implementation backlog, routine human gate, or self-canonicalization was introduced.
evidence:
  - docs/planning/08-planning-program-v1-reviewed-candidate.md at substantive work commit 1d7b9a980e74d6999789c86694f3c7fb99e13b99
  - docs/planning/reviews/issue-3-finding-dispositions.md
  - docs/planning/08-planning-program-v1-canonicalization-manifest.yaml
  - Issue #3 adversarial review integrated on main@21a3c1a5053f3697be3f82f6fe73de42423a482b
  - GitHub issue-comment REST metadata check for Issue #4 claim comment ID 5243865369 showing created_at and updated_at
known_problems:
  - The temporary ownership fence remains procedural rather than credential-enforced; this is explicit risk/evidence work for W1-FAC-02.
  - Reviewer independence remains procedural cold-start separation until stronger platform/run or credential boundaries are designed by W1-FAC-03.
  - Context and next-wave numeric caps are provisional guardrails with explicit reopen conditions.
decisions:
  - Accept all Issue #3 BLOCKER/MAJOR findings and correct them in the candidate.
  - Do not pre-create Wave 1 issues before Bootstrap Issue #6 squash integration.
  - Bind verification to exact candidate work SHA, canonicalization manifest, and verified main/base SHA.
  - Use one-shot recovery issue branches with at most one successor recovery service issue after accepted recovery integration.
  - Cap later-wave activation at 24 total new issues and 12 initially READY issues pending measured evidence.
  - Keep the candidate REVIEWED-CANDIDATE/NON_CANONICAL until independent Issue #5 PASS and Issue #6 canonicalization.
scope_deviations:
  - Added a machine-readable canonicalization manifest beyond the two minimum Issue #4 output paths because Issue #3 BLOCKER F-04 required the exact promotion/generated-issue transformation to be independently verifiable.
recommended_next_action: A fresh independent Bootstrap Issue #5 verifier should start from repository + GitHub state, inspect this exact branch/head after the final handoff status, verify the candidate/dispositions/manifest as one immutable work state against current main, and record PASS or FAIL without using this synthesizer's private context.

## Note on head SHA

The `head_sha` above is the latest substantive candidate commit. The commit containing this handoff necessarily has a later branch SHA; the final Issue #4 STATUS capsule must record that exact resulting branch head.