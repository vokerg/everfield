issue: 5
mission_id: BOOTSTRAP-VERIFY-05
role: Cold-start verifier under DEGRADED_SINGLE_AGENT
branch: planning/issue-5
branch_base_sha: c59ad1ef4b9eb1cd42b2349d0f5c7ee7860bddc9
verified_base_main_sha: c822934c74cc5903b057e6d081f5e0a4c3e58226
ownership_generation_comment_id: 5244621850
work_sha: a4d93b9e630a2be227298ab473f6234156eed301
state: BLOCKED
verification_result: FAIL
completed:
  - Acquired schema-3 Issue #5 ownership through BOOTSTRAP_RESUME comment 5244621850 from exact legacy bridge predecessor 5244618992.
  - Froze exact cold-start inputs in docs/planning/reviews/issue-5-final-cold-start-input-manifest.yaml blob ecd42d1060f96babe13273d7f07cbbad8fb24232.
  - Kept the Issue #14 candidate/manifest immutable on main while writing verifier evidence only to planning/issue-5.
  - Executed the required schema-3 scenario matrix and Wave 1 graph compilation in docs/planning/reviews/issue-5-final-verification-simulation.yaml blob ab43108d047759902f363e70a77bfe3f3741a769.
  - Regression-tested V5-B03 through V5-B07 as corrected.
  - Found one remaining BLOCKER V5-B08: no deterministic verification refresh transition after main advances between PASS and Issue #6 claim.
  - Recorded FAIL report at docs/planning/reviews/planning-program-v1-final-cold-start-verification.md.
  - Created bounded remediation Issue #16.
remaining:
  - Issue #16 must add a typed base-drift verification refresh path while preserving all Issue #14 corrections.
  - Issue #5 must re-verify the Issue #16 payload and current main under schema 3.
  - Issue #6 remains blocked until the latest valid exact-current-base verification binding is PASS with zero BLOCKER/MAJOR findings.
checks_performed:
  - Verified candidate blob 9829975eb3b8ac12b7dd8338a3569ff1a50cf309 and manifest blob 1f062de59afcfe8496b4cff0fdff594c2d5fd50c on main@c822934c74cc5903b057e6d081f5e0a4c3e58226.
  - Verified adopted Wave 1 source blob d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd compiles to 23 intended missions, 12 normal roots, no duplicate mission IDs, and no hard-dependency cycle found.
  - Exercised claim, orphan, handoff, stale recovery, stale terminal writer, malformed schema, external retirement, review routing, synthesis states, degraded independence, context fallback, liveness, phase transform, activation window, durable binding, binding mismatch, future version binding, base drift, preactivation claim, and squash-only scenarios.
  - Confirmed all required scenarios PASS except post-PASS/pre-Issue6 base drift, which fails as V5-B08.
evidence:
  - docs/planning/reviews/issue-5-final-cold-start-input-manifest.yaml
  - docs/planning/reviews/issue-5-final-verification-simulation.yaml
  - docs/planning/reviews/planning-program-v1-final-cold-start-verification.md
  - Issue #16 remediation contract
known_problems:
  - V5-B08 BLOCKER: a valid PASS becomes stale when main advances before Issue #6 claims, but no exact schema transition re-acquires verification authority for the unchanged candidate/new base.
  - DEGRADED_SINGLE_AGENT is explicitly weaker than full independent context and must reopen when stronger isolation is available.
decisions:
  - Record formal schema-3 FAIL with one BLOCKER and zero MAJOR findings.
  - Keep Issue #6 blocked.
  - Route V5-B08 through separate Issue #16; do not edit the candidate from the verifier branch.
scope_deviations:
  - Verification uses DEGRADED_SINGLE_AGENT due repository-visible one-agent constraint comment 5244416013; trust degradation is explicit and candidate edits are prohibited.
recommended_next_action: Complete Issue #16 on planning/issue-16, integrate it as non-canonical provenance after review, then re-enter Issue #5 through the refresh/verification transition defined by that exact candidate.

## Note on head SHA

`work_sha` is the commit containing the final FAIL report and all required evidence. The final BOOTSTRAP_VERIFICATION_STATUS must record the later branch head containing this handoff.