issue: 2
role: Planning Program v1 bootstrap planner
branch: planning/issue-2
head_sha: faf3328999d3c21c3b8cb020ad1f194071fc9eca
base_sha: 9a0a45169239a5079d901a9e9bc3bf782e889f62
state: REVIEW_READY
completed:
  - Read AGENTS.md and docs/planning/START-HERE.md from the task branch.
  - Read all Issue #2 authoritative inputs in the required order.
  - Loaded project, factory, game-design, and evaluation mandates only after they became necessary for cross-domain mission design.
  - Produced docs/planning/07-planning-program-v1-proposal.md.
  - Performed a first producer self-review and recorded corrections in docs/planning/07-planning-program-v1-proposal-amendment-1.md.
  - Performed a second producer self-review and recorded non-root context packets, the Wave 1 main-integration activation barrier, and provenance-merge semantics in docs/planning/07-planning-program-v1-proposal-amendment-2.md.
  - Defined cold-start discovery, derived eligibility, claim/resume/stale-recovery, branch/base, context-loading, evidence, handoff, review, synthesis, verification, canonicalization, liveness, and squash-integration semantics.
  - Defined a bounded first wave with 12 concurrent root missions and 23 total mission issues including review/synthesis/verification/canonicalization/recovery nodes.
  - Defined exact first-wave output paths, shared artifact schemas, non-root context packets, and exact bootstrap-chain output paths.
remaining:
  - Independent adversarial review by bootstrap Issue #3.
  - Any revisions required by Issue #3 must be handled by the Issue #4 synthesis/revision agent, not self-canonicalized here.
checks_performed:
  - Re-read Issue #2 immediately before deterministic branch claim and confirmed seed PR #1 was squash-integrated.
  - Confirmed planning/issue-2 did not exist before claim and created it from current main@9a0a45169239a5079d901a9e9bc3bf782e889f62.
  - Checked every Issue #2 required-output bullet against the complete proposal set.
  - Checked all 11 cold-start acceptance questions against Sections 9-14 and 21-22 of the base proposal plus Amendments 1-2.
  - Checked that every root and non-root mission has an exact output contract/schema class and bounded context packet.
  - Checked that Wave 1 cannot become claimable before bootstrap Issue #6 is squash-integrated to main and its canonical main SHA is recorded.
  - Checked that no gameplay code, final engine decision, mass implementation backlog, routine human gate, or self-canonicalization was introduced.
  - Checked that all main integration paths remain squash-only.
  - Confirmed PR #8 is mergeable and main has not advanced from the task base during this second review.
evidence:
  - docs/planning/07-planning-program-v1-proposal.md (initial substantive commit 397882a0ececfba907d885e70c899469b1ba6c4f)
  - docs/planning/07-planning-program-v1-proposal-amendment-1.md (first correction commit 45aa47e1f7d937d152a459817779677055b6f38c)
  - docs/planning/07-planning-program-v1-proposal-amendment-2.md (second correction commit faf3328999d3c21c3b8cb020ad1f194071fc9eca)
  - Issue #2 claim/status capsules on planning/issue-2
  - PR #8 diff and mergeability state
known_problems:
  - The proposal is intentionally split across a base proposal and two amendments because defects were found during producer self-review; Issue #4 should fold all three into one reviewed candidate.
  - The proposed 6-hour lease plus comment-ordered resume tie-break is explicitly temporary and not truly atomic for existing-branch resumes; Issue #3 must attack it and W1-FAC-02 must replace it in the mature control-plane design.
  - session_id role independence is procedural rather than cryptographically enforced; this is explicitly an open trust-model question.
  - The 23-issue first-wave decomposition remains a hypothesis until Issue #3 attacks coupling/size and Issue #5 cold-start verifies the revised candidate.
decisions:
  - Do not instantiate the 50 seed missions directly.
  - After bootstrap verification/canonicalization, instantiate exactly 23 Wave 1 mission issues, with 12 root proposals initially concurrent.
  - Use unique proposal/review/synthesis output paths and immutable upstream work SHAs.
  - Require a Wave 1 activation barrier tied to the exact Issue #6 squash commit on main before any first-wave claim.
  - Canonical Planning Program v1 location after Issue #6 is docs/planning/PLANNING-PROGRAM-v1.md.
  - Issue #3 review output is docs/planning/reviews/issue-2-adversarial-review.md.
  - Under the explicit human directive on 2026-08-10, PR #8 may be squash-merged to main as PROPOSED provenance after this self-review; that merge does not canonicalize Planning Program v1 or waive Issues #3-#6.
scope_deviations:
  - No gameplay/implementation scope deviation. The only workflow deviation is the explicit human-directed provenance merge timing before Issue #3 independent review; Amendment 2 records that this does not alter canonicality or downstream review gates.
recommended_next_action: After the human-directed squash provenance merge of PR #8, a fresh independent Issue #3 adversarial reviewer should start from current main, review the complete Issue #2 proposal set, attack claim/recovery/liveness/canonicalization semantics and the mission DAG, and produce docs/planning/reviews/issue-2-adversarial-review.md.

## Note on head SHA

The `head_sha` above is the latest substantive-work commit that this handoff describes. The commit containing this updated handoff necessarily has a later SHA; the final Issue #2 STATUS capsule must record that exact resulting branch head so continuation is reconstructable without a self-referential file SHA.
