issue: 2
role: Planning Program v1 bootstrap planner
branch: planning/issue-2
head_sha: 45aa47e1f7d937d152a459817779677055b6f38c
base_sha: 9a0a45169239a5079d901a9e9bc3bf782e889f62
state: REVIEW_READY
completed:
  - Read AGENTS.md and docs/planning/START-HERE.md from the task branch.
  - Read all Issue #2 authoritative inputs in the required order.
  - Loaded project, factory, game-design, and evaluation mandates only after they became necessary for cross-domain mission design.
  - Produced docs/planning/07-planning-program-v1-proposal.md.
  - Performed a producer self-review and recorded corrections in docs/planning/07-planning-program-v1-proposal-amendment-1.md rather than leaving them in chat context.
  - Defined cold-start discovery, derived eligibility, claim/resume/stale-recovery, branch/base, context-loading, evidence, handoff, review, synthesis, verification, canonicalization, liveness, and squash-integration semantics.
  - Defined a bounded first wave with 12 concurrent root missions and 23 total mission issues including review/synthesis/verification/canonicalization/recovery nodes.
  - Defined exact first-wave output paths and shared artifact schemas, plus exact bootstrap-chain output paths in Amendment 1.
remaining:
  - Independent adversarial review by bootstrap Issue #3.
  - Any revisions required by Issue #3 must be handled by the Issue #4 synthesis/revision agent, not self-canonicalized here.
checks_performed:
  - Re-read Issue #2 immediately before deterministic branch claim and confirmed seed PR #1 was squash-integrated.
  - Confirmed planning/issue-2 did not exist before claim and created it from current main@9a0a45169239a5079d901a9e9bc3bf782e889f62.
  - Checked every Issue #2 required-output bullet against the proposal set.
  - Checked all 11 cold-start acceptance questions against Sections 9-14, 21-22, and Amendment 1.
  - Checked that no gameplay code, final engine decision, mass implementation backlog, routine human gate, or self-canonicalization was introduced.
  - Checked that all main integration paths remain squash-only.
  - Producer review found and corrected stale BLOCKED/READY ambiguity, basename context ambiguity, undefined current-wave downstream references, missing non-root priority ranks, and missing canonicalization/recovery output contracts.
evidence:
  - docs/planning/07-planning-program-v1-proposal.md (initial substantive commit 397882a0ececfba907d885e70c899469b1ba6c4f)
  - docs/planning/07-planning-program-v1-proposal-amendment-1.md (corrected substantive head 45aa47e1f7d937d152a459817779677055b6f38c)
  - Issue #2 claim capsule on planning/issue-2
known_problems:
  - The proposal is intentionally split across a base proposal and Amendment 1 because corrections were discovered after the first commit; Issue #4 should fold both into one reviewed candidate.
  - The proposed 6-hour lease plus comment-ordered resume tie-break is explicitly temporary and not truly atomic for existing-branch resumes; Issue #3 must attack it and W1-FAC-02 must replace it in the mature control-plane design.
  - session_id role independence is procedural rather than cryptographically enforced; this is explicitly an open trust-model question.
decisions:
  - Do not instantiate the 50 seed missions directly.
  - After bootstrap verification/canonicalization, instantiate exactly 23 Wave 1 mission issues, with 12 root proposals initially concurrent.
  - Use unique proposal/review/synthesis output paths and immutable upstream work SHAs to avoid requiring unreviewed proposal merges before downstream review.
  - Canonical Planning Program v1 location after Issue #6 is docs/planning/PLANNING-PROGRAM-v1.md.
  - Issue #3 review output is docs/planning/reviews/issue-2-adversarial-review.md.
scope_deviations:
  - None. Work remained planning-only and bounded to Issue #2.
recommended_next_action: A fresh independent Issue #3 adversarial reviewer should read the Issue #2 proposal set at the recorded SHA, attack the claim/recovery/liveness/canonicalization semantics and mission DAG, and produce docs/planning/reviews/issue-2-adversarial-review.md.

## Note on head SHA

The `head_sha` above is the latest substantive-work commit that this handoff describes. The commit containing this handoff necessarily has a later SHA; the final Issue #2 STATUS capsule must record that exact resulting branch head so continuation is reconstructable without a self-referential file SHA.
