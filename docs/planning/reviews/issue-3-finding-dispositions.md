# Issue #3 Finding Dispositions — Planning Program v1

**State:** REVIEWED-CANDIDATE SUPPORT  
**Bootstrap issue:** #4  
**Reviewed findings source:** `docs/planning/reviews/issue-2-adversarial-review.md`  
**Candidate:** `docs/planning/08-planning-program-v1-reviewed-candidate.md`

## Status

All BLOCKER and MAJOR findings from Bootstrap Issue #3 are explicitly dispositioned below. No BLOCKER or MAJOR is rejected or silently deferred. The revised candidate remains non-canonical and must pass Bootstrap Issue #5 cold-start verification.

## Disposition table

| Finding | Severity | Disposition | Candidate correction |
|---|---|---|---|
| F-01 | BLOCKER | ACCEPTED | Candidate §11.1 adds `ORPHAN_PROBE` and deterministic orphan recovery for a branch created before any valid claim. A mature server-time probe prevents both immediate takeover and permanent stranding. |
| F-02 | BLOCKER | ACCEPTED | Candidate §§10.3, 12, 13 define ownership generations from immutable GitHub comment IDs plus a mandatory ownership/head fence before every branch mutation. Stale generations fail closed; expiry alone is not revocation. |
| F-03 | BLOCKER | ACCEPTED | Candidate §10 defines capsule schema/version, append-only validity, GitHub server ordering, invalidation of edited/malformed/unsupported-transition capsules, and server-time-derived lease age. |
| F-04 | BLOCKER | ACCEPTED | Candidate §§1, 22 and `docs/planning/08-planning-program-v1-canonicalization-manifest.yaml` make promotion mechanically constrained. Verification covers the promotion manifest and generated Wave 1 contract data; unenumerated transformation requires re-verification. |
| F-05 | BLOCKER | ACCEPTED | Candidate §§14.4–14.5 and 22 bind PASS to `verified_base_main_sha`. Integration requires current `main` to match or an independent compatibility/reverification of every intervening commit. |
| F-06 | MAJOR | ACCEPTED | Candidate §20 rejects pre-merge Wave 1 creation. Bootstrap Issue #6 must squash-merge first, obtain the concrete main SHA, then instantiate Wave 1 and finally post `DONE`. |
| F-07 | MAJOR | ACCEPTED | Candidate §19 defines minimum independence as a distinct cold-start execution context with producer private context excluded; self-selected `session_id` is explicitly insufficient. Stronger platform identity remains a Wave 1 trust-model target. |
| F-08 | MAJOR | ACCEPTED | Candidate §14 defines exact review dispositions and downstream predicates. `CHANGES_REQUIRED` unlocks the declared synthesis/revision mission; `INVALIDATED` unlocks recovery/replanning only. |
| F-09 | MAJOR | ACCEPTED | Candidate §15 adds 4k-character Review Indexes, a mandatory packet budget of min(100k UTF-8 characters, 50% known context window), preflight behavior, targeted retrieval, and no-silent-truncation rule. |
| F-10 | MAJOR | ACCEPTED | Candidate §16 makes recovery issues single-use task/branch episodes. An integrated recovery may instantiate exactly one blocked successor recovery issue, eliminating permanent post-squash branch reuse. |
| F-11 | MAJOR | ACCEPTED | Candidate §23 defines a full next-wave candidate contract, compiler/audit requirements, maximum 24 newly instantiated issues and maximum 12 initially READY issues per activation. Excess candidates remain deferred data. |
| F-12 | MINOR | ACCEPTED | This Issue #4 candidate replaces the base + amendment stack operationally. All three Issue #2 files are explicit immutable inputs; downstream agents use this single candidate rather than the stale two-file enumeration. |
| F-13 | MINOR | ACCEPTED | Candidate §12.3 requires substantive head advance or immutable experimental evidence for renewal and invalidates a fourth consecutive no-head-advance renewal. |
| F-14 | NOTE | ACCEPTED_AS_MEASUREMENT | Candidate §§21 and 24 distinguish useful conflict-free progress from raw branch count and make useful READY-frontier width a measured/reopen signal. |

## BLOCKER disposition rationale

### F-01 — Orphaned branch

The review correctly identified a transaction gap between branch creation and claim comment. Branch creation remains the exclusion primitive for new work, but branch existence without ownership is now a first-class recoverable condition. The recovery path intentionally requires a GitHub-server-aged probe before takeover so two agents cannot both treat the normal short create→claim interval as abandonment.

### F-02 — Stale writer fencing

The candidate does not pretend a lease revokes repository credentials. Instead, authority is the latest valid ownership-generation comment and every mutation must compare both that generation and the exact remote parent. This makes compliant stale writers abort once recovery wins. W1-FAC-02 is still required to replace this procedural fence with stronger machine enforcement.

### F-03 — Hidden status interpreter

“Latest valid capsule” is no longer left to intuition. The validator surface is explicit: schema, required identity fields, branch/SHA checks, transition predicates, append-only/unedited requirement, and GitHub server ordering. Self-authored timestamps cannot extend authority.

### F-04 — Verification/promotion gap

The candidate adds a separate machine-readable canonicalization manifest to the immutable Issue #4 work state. Issue #5 verifies the candidate together with that manifest. Issue #6 may only apply enumerated transformations and deterministic issue generation from the verified data.

### F-05 — Moving main

A PASS is now a relation among candidate SHA, promotion manifest, and `verified_base_main_sha`, not a candidate-only property. Base drift forces compatibility/reverification before authority can transition.

## MAJOR disposition rationale

### F-06 — Unknowable future activation SHA

Resolved by sequencing: merge first, know the SHA, instantiate issues second, post Issue #6 `DONE` last. Every Wave 1 issue is born with a concrete activation SHA.

### F-07 — Reviewer self-confirmation

A distinct UUID remains useful episode metadata but is not an independence gate. The minimum accepted boundary is a fresh execution context with repository/GitHub-only cold start and no producer private context. Lack of stronger platform identity is explicitly a risk, not hidden certainty.

### F-08 — Review state ambiguity

The candidate separates review-task completion from review disposition and states exact downstream predicates. Synthesis is the declared correction owner for `CHANGES_REQUIRED`; invalidation is routed to recovery/replanning.

### F-09 — Context overload

The correction makes context a measurable packet rather than a qualitative aspiration. Review Indexes are mandatory, full source sections are retrieved by stable pointer when findings require them, and over-budget packets must split or retrieve progressively rather than truncate silently.

### F-10 — Recovery/squash lifecycle mismatch

The reusable-service-branch model is removed. Every recovery issue is one-shot and follows ordinary branch lifetime; continuity is preserved by creating at most one successor service issue after accepted integration.

### F-11 — Backlog growth

A final synthesis can record many candidates, but canonicalization cannot instantiate them arbitrarily. The cap and compiler audit make “bounded next wave” testable and reversible.

## Remaining empirical questions

The following are deliberately retained as first-wave evidence work, but none is allowed to weaken the corrected bootstrap safety rules:

- strongest available GitHub/API expected-parent claim/write primitive;
- stronger run/credential identity for independent reviewers/verifiers;
- empirically optimal review-context budget;
- optimal later-wave WIP/frontier caps.

## Verification readiness

The candidate is ready for Bootstrap Issue #5 **cold-start verification**, not canonicalization. Issue #5 must verify the exact Issue #4 work SHA containing the candidate, this disposition artifact, and the canonicalization manifest. A FAIL returns to bounded remediation; only PASS for the exact candidate/base pair can unlock Issue #6.