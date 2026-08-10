issue: 34
mission_id: W1-REV-FAC
role: independent adversarial reviewer
branch: planning/issue-34
base_sha: 413e729e8d2d5ac2eb138903f3f2ace07283b23e
ownership_generation_comment_id: 5245649591
work_sha: 4ffa7fd8a175bae504280160e8c48a508909e6f3
state: DONE
review_disposition: CHANGES_REQUIRED
blocker_count: 1
major_count: 7
minor_count: 3
note_count: 2
independence_profile:
  mode: DEGRADED_SINGLE_AGENT
  trust_level: DEGRADED
  resource_constraint_comment_id: 5244416013
  candidate_edit_prohibited: true
completed:
  - Froze exact review inputs and attack plan in docs/planning/wave-1/reviews/factory-governance-review-input.yaml before detailed producer reconciliation.
  - Bound W1-GOV-01, W1-FAC-01, W1-FAC-02, W1-FAC-03, and W1-FAC-04 exact REVIEW_READY comments, work SHAs, head SHAs, and artifact paths.
  - Reviewed only the declared producer packet; producer branches/candidates were not edited.
  - Produced docs/planning/wave-1/reviews/factory-and-governance.md with disposition CHANGES_REQUIRED.
  - Recorded 1 BLOCKER, 7 MAJOR, 3 MINOR, and 2 NOTE findings with exact affected proposal sections and concrete failure scenarios.
  - Required synthesis corrections for directive-set authority in READY proofs, dynamic conflict-lock expansion, old-policy-governs-new-policy, trust-debt registry, shared evidence requirement/satisfaction, non-downgradable risk floors, durable work/evidence reachability, and shared provenance/evidence artifact identity.
  - Preserved the experimental/non-adoptable status of unvalidated FAC2 ref-lock/lease mechanisms.
  - Preserved no-routine-human-gate, current-base verification, candidate immutability, squash-only integration, and implementation-readiness barriers.
remaining:
  - W1-SYN-FAC must disposition FG-B01 and every FG-M02 through FG-M08 finding explicitly.
  - W1-SYN-FAC should also disposition the three MINORs and preserve the NOTE measurement obligations where relevant.
  - The FAC2/FAC3/FAC4 experiments named in the review remain evidence questions and cannot be fabricated as PASS by synthesis.
checks_performed:
  - Finding severity counts match the review header/table.
  - Every BLOCKER/MAJOR has a concrete correction or bounded empirical gate.
  - Disposition CHANGES_REQUIRED is allowed by the W1-REV-FAC contract and unblocks W1-SYN-FAC revision/synthesis.
  - Review binds exact producer status/work/head provenance rather than mutable latest branches.
  - Review does not modify or supersede producer candidates.
  - No seed/mandate context widening was necessary to demonstrate the material cross-proposal defects.
  - No gameplay implementation, canonicalization, producer rewrite, or new current-wave issue creation was performed.
evidence:
  - docs/planning/wave-1/reviews/factory-governance-review-input.yaml
  - docs/planning/wave-1/reviews/factory-and-governance.md at work_sha 4ffa7fd8a175bae504280160e8c48a508909e6f3
  - exact producer REVIEW_READY status comments 5245434514, 5245474479, 5245532215, 5245577951, 5245629575
known_problems:
  - Review independence is DEGRADED_SINGLE_AGENT, not full isolation; stronger capability should trigger the canonical trust-debt re-audit once such a registry exists.
  - Several control-plane mechanisms remain intentionally experimental pending FAC2/FAC3/FAC4 empirical spikes.
decisions:
  - CHANGES_REQUIRED rather than INVALIDATED: proposals are strong local inputs but unsafe to combine without interface corrections.
  - FG-B01 is BLOCKER because missing directive-set authority can make compliant schedulers authorize contradictory work under the highest authority class.
  - Corrections belong in W1-SYN-FAC rather than producer branches.
scope_deviations: []
recommended_next_action: Publish final schema-3 REVIEW_STATUS CHANGES_REQUIRED for exact review work/head, close Issue #34, then select W1-SYN-FAC as the highest-priority quality-pipeline task and synthesize all required corrections without editing producer provenance.

## Final head note

`work_sha` is the substantive review commit. Final REVIEW_STATUS must record the later branch head containing this handoff.