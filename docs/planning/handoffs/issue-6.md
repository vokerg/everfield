issue: 6
mission_id: BOOTSTRAP-CANON-06
role: Planning integration / canonicalization agent
branch: planning/issue-6
base_sha: a611c4540df1693fb3536a59f032f1a79b51cdc5
ownership_generation_comment_id: 5245233112
verification_status_comment_id: 5245221974
verified_candidate_work_sha: 00df46cae3230f380bcee9dd24442d984c73fea0
verified_manifest_identity: f4e65f408b77a917d1fc61a1dbaee808e978f072
verified_wave_1_blob_sha: d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd
work_sha: 5b1dc4748f4afb938f9a3f9fb1967546e8108ba9
state: INTEGRATION_READY
completed:
  - Claimed Issue #6 from exact verified base main@a611c4540df1693fb3536a59f032f1a79b51cdc5 under schema-3 ownership comment 5245233112.
  - Revalidated Issue #5 PASS 5245221974 and its exact candidate/manifest/Wave1/base tuple.
  - Materialized docs/planning/PLANNING-PROGRAM-v1.md from the verified Issue #18 candidate using only the four allowed header replacements.
  - Applied the verified AGENTS.md PLANNING/entry transformation.
  - Replaced docs/planning/START-HERE.md with the verified canonical entry pointer.
  - Recorded docs/planning/bootstrap-canonicalization-report.md with pre/post merge contract and implementation barrier.
  - Preserved the verified rule forbidding Wave 1 issue creation before the Issue #6 squash commit exists.
remaining:
  - Confirm no open [PLAN-v1] issues exist before merge.
  - Open/review the Issue #6 PR and verify exact changed-file set, no review/CI blockers, expected PR head, and unchanged main base.
  - Squash-merge only if main still equals the verified base and PASS remains valid.
  - After merge, verify canonical materialization at the squash SHA, instantiate exactly 23 Wave 1 issues with that activation SHA, validate them, post mission mapping, and publish terminal schema-3 INTEGRATION_STATUS.
  - Close Issue #6 only after terminal canonical binding exists.
checks_performed:
  - Canonical program branch blob e3120ec203c4156328770aa86c12fbb7187966dc retains verified Issue #18 body and applicability guard.
  - AGENTS.md branch blob 9f65e73a1f16eb731d4068066998361c060f74bf matches verified PLANNING transform.
  - START-HERE branch blob 515dc7b12e1a85f66e780901c1caa0d9afbc55d5 matches verified canonical entry replacement.
  - Issue #5 PASS has zero BLOCKER/MAJOR and is current-base scoped to a611c4540df1693fb3536a59f032f1a79b51cdc5.
  - No gameplay implementation or Wave 1 issue creation has been performed in pre-merge materialization.
evidence:
  - Issue #5 PASS comment 5245221974
  - docs/planning/12-planning-program-v1-bootstrap-safe-candidate.md blob 261d7e5f7f9f1412415116b3e0f127f3e3f1bec7
  - docs/planning/12-planning-program-v1-canonicalization-manifest.yaml blob f4e65f408b77a917d1fc61a1dbaee808e978f072
  - docs/planning/08-planning-program-v1-canonicalization-manifest.yaml blob d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd
  - docs/planning/bootstrap-canonicalization-report.md at work_sha 5b1dc4748f4afb938f9a3f9fb1967546e8108ba9
known_problems:
  - DEGRADED_SINGLE_AGENT remains a trust limitation and must reopen when stronger independent verification capability exists.
  - Until terminal post-merge INTEGRATION_STATUS exists, the canonical materialization is in CANONICAL_UNBOUND_ACTIVATION and normal PLAN-v1 selection must remain inactive.
decisions:
  - Do not create Wave 1 issues before the squash merge.
  - Do not merge any unrelated branch before Issue #6, because current-base PASS would become stale.
  - Use squash-only integration with expected-head protection.
  - Treat the squash result as the concrete activation SHA for all 23 Wave 1 contracts.
scope_deviations: []
recommended_next_action: Open and self-review the Issue #6 PR; if main remains a611c4540df1693fb3536a59f032f1a79b51cdc5 and all checks are clean, squash-merge and immediately execute the verified post-merge activation sequence.

## Note on final branch head

`work_sha` is the canonicalization-report commit. The final pre-merge PR head will also contain this handoff and must be recorded in the Issue #6 integration status after squash.