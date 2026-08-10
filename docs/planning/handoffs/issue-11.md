issue: 11
role: Planning Program v1 verification-remediation synthesizer
branch: planning/issue-11
head_sha: 7ed2d734645adf93910ce60156ec8b45d528fa73
base_sha: c59ad1ef4b9eb1cd42b2349d0f5c7ee7860bddc9
state: VERIFICATION_READY
completed:
  - Read Issue #11 and the exact Issue #5 FAIL report from work commit 26a06f9ab78ede2c69107e3df3d2327e2aed18f0.
  - Created one complete remediated candidate at docs/planning/09-planning-program-v1-remediated-candidate.md.
  - Created one normative schema-2 canonicalization/operational manifest at docs/planning/09-planning-program-v1-canonicalization-manifest.yaml.
  - Created docs/planning/reviews/issue-5-finding-dispositions.md with explicit ACCEPTED_AND_CORRECTED dispositions for V5-B01 and V5-B02.
  - Corrected V5-B01 by making the candidate body canonical-safe, restricting program promotion to three header literal replacements with byte-identical remainder, and adding an explicit post-squash/pre-terminal Issue #6 activation barrier to the candidate and entry-document patches.
  - Corrected V5-B02 by defining a closed schema-2 registry for CLAIM, ORPHAN_PROBE, RESUME_INTENT, RESUME, RECOVER, PROGRESS, STATUS, REVIEW_STATUS, VERIFICATION_STATUS, and INTEGRATION_STATUS.
  - Added exact common fields, per-kind required fields/enums/constants, predecessor/source predicates, deterministic intent/grant tie rules, authority effects, review/verification routing, external supersession/invalidation authorization, and a full transition table.
  - Preserved the reviewed 23-mission Wave 1 DAG by immutable narrow adoption of only the issue_compiler, universal_root_acceptance, wave_1, non_root_optional_retrieval, and next_wave_candidate_schema sections from Issue #4 manifest blob d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd.
  - Explicitly excluded Issue #4 verification_contract and bootstrap_canonicalization from adoption.
  - Performed remediation self-review and fixed an activation-window edge plus a temporary mismatch between candidate wording and manifest transformation count.
remaining:
  - A fresh independent Issue #5 verifier must independently inspect the remediation before reading prior conclusions in detail and then verify the exact Issue #11 work state.
  - Issue #5 must bind this candidate work SHA, manifest identity, adopted Wave 1 blob, simulated issue graph, and then-current main base.
  - Issue #6 remains blocked unless that fresh verification records PASS with zero BLOCKER/MAJOR.
checks_performed:
  - Verified the candidate header literals exactly match the three promotion source strings in the manifest.
  - Verified candidate Section 9 itself requires terminal Issue #6 INTEGRATION_STATUS before normal Wave 1 selection.
  - Verified candidate Sections 29-30 make the bootstrap chain provenance-only only after terminal activation and route the post-squash/pre-terminal window solely to Issue #6 completion.
  - Verified manifest program promotion has exactly three header replacements and all_other_bytes_identical: true.
  - Verified AGENTS/START-HERE replacement text handles the post-squash/pre-terminal activation window without invoking normal liveness recovery.
  - Verified schema 2 registers exactly ten operational kinds and every registered kind has required fields plus predecessor/validity/authority semantics.
  - Verified review CHANGES_REQUIRED vs INVALIDATED routing and domain REVIEW_READY vs final VERIFICATION_READY remain explicit.
  - Verified current branch is ahead of and not behind main; changed files before this handoff were limited to the three required remediation artifacts.
  - Verified no gameplay implementation, engine choice, Wave 1 instantiation, routine human gate, or canonicality claim was introduced.
evidence:
  - docs/planning/09-planning-program-v1-remediated-candidate.md blob 5e60d827ab99fe04e8a23c4addfc59d6f418d281
  - docs/planning/09-planning-program-v1-canonicalization-manifest.yaml blob 9ecad20d9332eb1b649dfcb16beece5cda3fa330
  - docs/planning/reviews/issue-5-finding-dispositions.md
  - Issue #5 FAIL work commit 26a06f9ab78ede2c69107e3df3d2327e2aed18f0
  - adopted Issue #4 manifest blob d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd
known_problems:
  - The schema-2 protocol is still procedural and must later be replaced/tested by W1-FAC-02; this is an explicit risk, not an unresolved bootstrap correctness defect found by this self-review.
  - Reviewer/verifier identity remains procedural until W1-FAC-03 strengthens it; Issue #5 still requires a distinct cold-start context now.
  - Context and wave caps remain provisional with reopen conditions.
decisions:
  - Preserve Issue #4 candidate/manifest as immutable superseded-for-verification provenance rather than editing them.
  - Make the new candidate body safe in both pre-canonical and canonical states so Issue #6 promotion needs only three header literal replacements.
  - Treat the post-squash/pre-terminal window as part of V5-B01 and route it only to Issue #6 completion.
  - Use a closed fail-closed schema-2 operational registry rather than prose-only required fields.
  - Do not merge Issue #11 to main before independent Issue #5 verification; the verifier may consume exact non-main work SHA.
scope_deviations:
  - Added the post-squash/pre-terminal activation-window correction while remediating V5-B01 because it is the same canonical dispatcher consistency surface.
recommended_next_action: A fresh independent Issue #5 verifier should resume planning/issue-5 only after independently reading repository entry state and Issue #11, then verify planning/issue-11 at its exact final head/work state and record PASS or FAIL.

## Note on branch head

The head_sha above is the latest substantive remediation commit. The final Issue #11 STATUS capsule must record the later branch head containing this handoff.