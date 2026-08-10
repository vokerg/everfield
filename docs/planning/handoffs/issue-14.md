issue: 14
role: Planning Program v1 bootstrap-boundary remediation synthesizer
branch: planning/issue-14
base_sha: fce7218a1e7a4b03bae04aead80f12f5039848fb
work_sha: 7fa2c5808343876d6659aabd652668e4f8f201cb
state: VERIFICATION_READY
completed:
  - Consumed the Issue #5 second cold-start FAIL and corrected V5-B03 through V5-B07 in one new provenance-preserving candidate/manifest pair.
  - Added durable canonical binding keyed by the current canonical program blob plus its named canonicalization issue; activation SHA remains valid as an ancestor of later main commits.
  - Added fail-closed CANONICAL_BINDING_MISMATCH handling when a current program blob no longer matches a prior binding.
  - Added deterministic AGENTS.md title/Status/Current Phase/cold-start transformations and complete START-HERE replacement so all post-bootstrap entry surfaces report PLANNING.
  - Added schema-3 bootstrap overlay for legacy Issue #5 and unclaimed Issue #6.
  - Added BOOTSTRAP_RESUME so the legacy planning/issue-5 branch can acquire a real fenced schema-3 ownership generation before verification writes.
  - Added BOOTSTRAP_VERIFICATION_STATUS and Issue #6 mission overlay BOOTSTRAP-CANON-06.
  - Added closed schema-3 field types, nullability, ownership/result fencing, typed independence profiles, typed base compatibility evidence, and external retirement semantics.
  - Added repository-anchored DEGRADED_SINGLE_AGENT verification/review mode with immutable-candidate, cold-start-input, evidence-before-rationale, separate-remediation, trust-degradation, and reopen requirements.
  - Preserved the reviewed Wave 1 mission graph by immutable adoption of Issue #4 manifest blob d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd; no gameplay work or Wave 1 issues were created.
  - Performed adversarial self-review and corrected canonical-binding mismatch handling, BOOTSTRAP_RESUME mutation fencing, missing container types, and legacy bridge head typing.
remaining:
  - Bootstrap Issue #5 must re-verify this exact Issue #14 payload and the then-current main base using schema-3 BOOTSTRAP_RESUME and a valid independence profile.
  - Bootstrap Issue #6 remains blocked until Issue #5 records PASS with zero BLOCKER/MAJOR findings.
checks_performed:
  - Verified planning/issue-14 is ahead of and not behind main@fce7218a1e7a4b03bae04aead80f12f5039848fb.
  - Verified branch changes are limited to the final candidate, manifest, finding dispositions, and this handoff.
  - Checked durable activation after later unrelated main merges and fail-closed behavior for changed program blob with old binding.
  - Checked root phase transform covers AGENTS title, Status, Current Phase, cold-start section, and full START-HERE replacement.
  - Checked bootstrap Issue #5 bridge supplies a typed legacy predecessor including branch head and creates schema-3 ownership before repository writes.
  - Checked Issue #6 starts normally in schema 3 from a valid bootstrap verification PASS.
  - Checked specialized review/verification/integration results require current unexpired owner, exact branch head/work binding, and typed evidence/provenance.
  - Checked external retirement can represent never-claimed SUPERSEDED/INVALIDATED work without fabricated ownership.
  - Checked degraded single-agent mode is explicitly labeled DEGRADED and has a mandatory reopen condition.
  - Checked all accepted main integrations remain squash-only and high-throughput implementation remains blocked.
evidence:
  - docs/planning/10-planning-program-v1-final-bootstrap-candidate.md
  - docs/planning/10-planning-program-v1-canonicalization-manifest.yaml
  - docs/planning/reviews/issue-5-reverification-finding-dispositions.md
  - Issue #5 second FAIL report at work_sha 44b93171fcd0734bf8181f75120e52d4c7873ab6
  - Repository-visible single-agent constraint at Issue #5 comment 5244416013
known_problems:
  - Expected-parent fencing is still procedural and should be strengthened by later factory/control-plane work.
  - DEGRADED_SINGLE_AGENT provides liveness but is weaker than true independent context isolation and must be reopened when stronger isolation becomes available.
  - Context and wave-size numeric limits remain provisional measured guardrails.
decisions:
  - Accept and correct every V5-B03 through V5-B07 BLOCKER.
  - Use program identity plus ancestry for durable canonical binding rather than current-HEAD equality.
  - Use one-time typed bootstrap bridge kinds only for Issue #5; Issue #6 starts with normal schema-3 CLAIM.
  - Keep the final bootstrap candidate NON-CANONICAL until Issue #5 PASS and Issue #6 terminal canonical binding.
  - Preserve Wave 1 contracts rather than redesigning them in this remediation.
scope_deviations:
  - None beyond the explicit Issue #14 requirement to define degraded single-agent verification because only one project agent is currently available.
recommended_next_action: Integrate this remediation as non-canonical squash provenance if the final pre-merge review remains clean; then post the exact legacy HANDOFF_READY bridge predecessor on Issue #5 and re-verify this payload under schema 3 DEGRADED_SINGLE_AGENT.

## Note on head SHA

`work_sha` is the final substantive remediation commit before this handoff. The final Issue #14 STATUS comment must record the later branch head containing this handoff.