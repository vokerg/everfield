issue: 18
role: Planning Program v1 canonical-state interpretation remediation
branch: planning/issue-18
base_sha: 03140f8875392450198c22d864664810e03d6865
work_sha: 00df46cae3230f380bcee9dd24442d984c73fea0
state: VERIFICATION_READY
completed:
  - Resumed the already-claimed Issue #18 branch from exact current main base.
  - Created docs/planning/12-planning-program-v1-bootstrap-safe-candidate.md.
  - Created docs/planning/12-planning-program-v1-canonicalization-manifest.yaml.
  - Created docs/planning/reviews/issue-5-canonical-wrapper-finding-dispositions.md.
  - Accepted and corrected V5-B09 with a normative applicability guard.
  - Defined PRE_CANONICAL_BOOTSTRAP, CANONICAL_UNBOUND_ACTIVATION, CANONICAL_ACTIVE, and CANONICAL_BINDING_MISMATCH states.
  - Made all bootstrap-numbered clauses PROVENANCE_ONLY after active canonical binding while preserving generic schema-3 mechanisms.
  - Hardened composition so every Issue #16 clause is adopted exactly and only the explicit authority filter/promotion source may override it.
remaining:
  - Issue #5 must re-enter through VERIFICATION_RESTART because Issue #18 changed candidate/manifest.
  - Issue #5 must rerun the complete inherited scenario suite plus the post-terminal single-queue regression.
  - Issue #6 remains blocked until a valid current-base PASS with zero BLOCKER/MAJOR.
checks_performed:
  - Confirmed V5-B09 correction survives header-only canonical promotion byte-identically.
  - Confirmed CANONICAL_ACTIVE exposes exactly one normal queue: open [PLAN-v1].
  - Confirmed bootstrap-numbered clauses cannot create eligibility, replay, priority, or blocking authority after active binding.
  - Confirmed generic VERIFICATION_RESTART/VERIFICATION_REFRESH remain active when declared by the current canonical task graph.
  - Confirmed CANONICAL_UNBOUND_ACTIVATION permits only named Issue #6 post-merge activation.
  - Confirmed canonical-binding mismatch fails closed rather than replaying bootstrap.
  - Confirmed Issue #16/base blobs and adopted Wave 1 blob remain immutable inputs.
  - Confirmed squash-only integration and implementation-readiness barrier remain unchanged.
evidence:
  - docs/planning/12-planning-program-v1-bootstrap-safe-candidate.md
  - docs/planning/12-planning-program-v1-canonicalization-manifest.yaml
  - docs/planning/reviews/issue-5-canonical-wrapper-finding-dispositions.md
  - Issue #5 formal V5-B09 FAIL and Issue #18 contract
known_problems:
  - DEGRADED_SINGLE_AGENT remains weaker than isolated independent verification and must reopen when stronger capability is available.
  - Candidate is NON-CANONICAL until Issue #5 PASS and Issue #6 terminal activation.
decisions:
  - Keep the remediation as a narrow authority/applicability overlay; do not rewrite schema 3, restart/refresh, Wave 1, or canonical binding.
  - Adopt all Issue #16 clauses exactly; forbid invented generic/non-generic partitioning.
  - Treat bootstrap issue text as retained provenance rather than deleting it from the future canonical file.
scope_deviations: []
recommended_next_action: Squash-integrate Issue #18 only as non-canonical provenance after final self-review, then VERIFICATION_RESTART Issue #5 against the exact Issue #18 payload/current main and rerun all scenarios.

## Note on final branch head

`work_sha` is the final substantive candidate/manifest commit. The Issue #18 STATUS capsule and PR should record the later branch head containing this handoff.