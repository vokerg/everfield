issue: 5
mission_id: BOOTSTRAP-VERIFY-05
role: Cold-start verifier under DEGRADED_SINGLE_AGENT
branch: planning/issue-5
verified_base_main_sha: 03140f8875392450198c22d864664810e03d6865
ownership_generation_comment_id: 5244798747
ownership_kind: VERIFICATION_RESTART
work_sha: 7efe874a1eef6cf91929e96d01e8050131bcfeda
state: BLOCKED
verification_result: FAIL
completed:
  - Re-entered from formal schema-3 FAIL 5244679631 through VERIFICATION_RESTART ownership 5244798747 after Issue #16 provenance integration.
  - Froze exact effective-candidate inputs in docs/planning/reviews/issue-5-bootstrap-final-cold-start-input-manifest.yaml blob af6f2f9972948cc3533cd1dbf81361e3e9470dd9.
  - Kept Issue #16 overlay/base candidate and manifests immutable on main throughout verification.
  - Simulated deterministic composition, restart/refresh ownership, current-base binding, all inherited schema/recovery/review/canonical-binding scenarios, Wave 1 graph, root transforms, activation and squash behavior.
  - Confirmed V5-B03 through V5-B08 regressions pass.
  - Found V5-B09 BLOCKER: header-only promotion leaves present-tense bootstrap Issue #5/#6/#16 clauses in the canonical wrapper without an applicability guard.
  - Recorded simulation artifact docs/planning/reviews/issue-5-bootstrap-final-verification-simulation.yaml blob 274c817ff68d80e6db2194b188c1404dc3b991fc.
  - Recorded FAIL report docs/planning/reviews/planning-program-v1-bootstrap-final-verification.md.
  - Created bounded remediation Issue #18.
remaining:
  - Issue #18 must add a canonical-state applicability guard while preserving generic restart/refresh and all V5-B03 through V5-B08 corrections.
  - Issue #5 must fully verify the Issue #18 payload/current main.
  - Issue #6 remains blocked until exact-current-base PASS with zero BLOCKER/MAJOR.
checks_performed:
  - Verified changed-candidate FAIL -> VERIFICATION_RESTART transition is executable.
  - Verified unchanged-candidate stale-base PASS -> VERIFICATION_REFRESH -> full verification is executable and repeatable.
  - Verified Issue #6 ignores older-base verification results.
  - Verified composition paths/section exclusions are deterministic and fail closed on unresolved targets.
  - Verified promoted wrapper still retains bootstrap-specific present-tense text, causing V5-B09.
evidence:
  - docs/planning/reviews/issue-5-bootstrap-final-cold-start-input-manifest.yaml
  - docs/planning/reviews/issue-5-bootstrap-final-verification-simulation.yaml
  - docs/planning/reviews/planning-program-v1-bootstrap-final-verification.md
  - Issue #18 remediation contract
known_problems:
  - V5-B09 BLOCKER: canonical wrapper lacks explicit rule making bootstrap-numbered clauses provenance-only after terminal active binding.
  - DEGRADED_SINGLE_AGENT remains weaker than true isolated independent context and must reopen when stronger capability exists.
decisions:
  - Record formal FAIL; do not authorize Issue #6.
  - Preserve generic VERIFICATION_RESTART/REFRESH as corrected.
  - Route only the canonical-state applicability defect to separate Issue #18.
scope_deviations:
  - Verification trust remains DEGRADED due repository-visible one-agent constraint 5244416013.
recommended_next_action: Complete Issue #18, squash-integrate its guarded wrapper as non-canonical provenance, then use VERIFICATION_RESTART from this formal FAIL to run full Issue #5 verification again.

## Note on head SHA

`work_sha` contains the FAIL report and simulation. The final BOOTSTRAP_VERIFICATION_STATUS records the later branch head containing this handoff.