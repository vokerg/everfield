# Planning Program v1 — Independent Adversarial Review

## Status

**Review task:** Bootstrap Issue #3  
**Role:** Independent adversarial planning reviewer  
**Result:** CHANGES_REQUIRED  
**Synthesis readiness:** READY_FOR_REVISION, not ready for verification or canonicalization  
**Reviewer session_id:** `39fe500b-3445-47a1-80c9-2fd603d8d138`

This review attempts to invalidate the Planning Program v1 proposal set rather than polish it. The proposal has strong coverage of the intended lifecycle, but the attack found five BLOCKER-class protocol defects and six MAJOR defects that can produce ambiguous ownership, divergent state classification, unsafe canonicalization, or loss of liveness under realistic crash/race conditions.

The correct next step is Bootstrap Issue #4 synthesis/revision. Bootstrap Issues #5 and #6 must remain blocked until the BLOCKER/MAJOR findings below are explicitly dispositioned and the revised candidate is cold-start verified.

## Reviewed mission IDs and immutable SHAs

The review target is the complete Issue #2 proposal set as integrated for non-canonical provenance on `main`:

- integration commit: `main@dee77b0ea93e0beb694d19188061f73e98faa124`;
- provenance source task head recorded by Issue #2: `planning/issue-2@9aa27804ee5c93ce3875deb09dd29cca10dc36cf`;
- `docs/planning/07-planning-program-v1-proposal.md` blob `20daa079e827ea250bf8a031f3746a9474b6748b`;
- `docs/planning/07-planning-program-v1-proposal-amendment-1.md` blob `622f6781e6c6b59f658db4e60a2d6a87141bd08a`;
- `docs/planning/07-planning-program-v1-proposal-amendment-2.md` blob `3bb875ed9e13f58fef2ce41736507a0bc42e00e8`.

The review also consulted the following seed constraints only where needed to test whether a proposal risk violates project intent:

- `docs/planning/01-autonomous-factory-mandate.md` — especially context discipline, role separation, claiming, handoffs, independent review, and factory maturity;
- `docs/planning/06-planning-deliverables.md` — especially the dependency/READY model, review/verification deliverables, planning-to-issue compiler, and implementation-readiness gate.

No prior chat history was used as project authority.

## Review scope and attack plan

The attack covered every category required by Issue #3:

- task selection and derived eligibility;
- new-work exclusion, resume races, stale leases, and orphaned claims;
- branch/session/handoff reconstruction;
- planning-DAG liveness and recovery;
- reviewer/verifier independence;
- context loading and review fan-in;
- hidden human gates and self-canonicalization;
- canonicalization authority and integration races;
- retirement/next-wave growth control;
- evidence requirements and reopen behavior;
- safe concurrency and paths by which agents could silently invent policy.

Severity meanings in this report:

- **BLOCKER** — the candidate can enter an unsafe, ambiguous, or incorrectly canonical state without violating its own written rules; correction is required before cold-start PASS.
- **MAJOR** — the candidate is executable in common cases but has a material ambiguity or scaling/liveness defect that must be corrected or empirically bounded before canonicalization.
- **MINOR** — localized ambiguity that should be folded into the reviewed candidate but does not by itself invalidate the operating model.
- **NOTE** — observation or future measurement target.

## Findings table

| ID | Severity | Affected section | Failure scenario | Evidence | Required correction |
|---|---|---|---|---|---|
| F-01 | BLOCKER | Base §§9.4, 9.6, 9.11; Amendment 1 §2 | An agent successfully creates `planning/issue-N` and crashes before posting `CLAIM`. Every later new claimant sees the branch and must enter resume/recovery, but the branch has no `IN_PROGRESS` lease to expire and is not `HANDOFF_READY`. Normal recovery has no defined entry condition, so one crash can strand the task. | New-work exclusion is branch creation first, comment second. Stale recovery is defined only for an `IN_PROGRESS` task with an expired lease. No orphan-branch/no-claim state exists. | Add an explicit orphan-claim state and recovery rule. A branch that exists without a valid ownership capsule after a short server-time grace must be recoverable through a deterministic takeover protocol that records observed head, verifies no useful owner state exists, and never requires an alternate normal task branch. |
| F-02 | BLOCKER | Base §§9.4–9.6, 16, 17.1 | A legitimate owner keeps working after its six-hour lease expires. A recovery agent wins `RESUME_INTENT` and starts editing the same branch. The expired owner then pushes a fast-forward based on a newer local/remote state or otherwise mutates after takeover. The comment lease did not revoke write authority, so two sessions can be active owners. | Leases and `session_id` values are issue-comment conventions. The protocol does not require a lease-generation/fencing check immediately before every branch mutation and does not define a compare-and-swap ownership token for branch updates. The proposal itself admits resume serialization is not truly atomic. | Introduce fencing semantics before Wave 1 activation: monotonically ordered lease/takeover generation, mandatory re-read of latest ownership generation immediately before every mutation/push, fast-forward/expected-head-only writes, and a hard rule that any stale generation stops on mismatch. If current tooling cannot provide an enforceable enough fence, this must remain a failed empirical question rather than be declared safe. |
| F-03 | BLOCKER | Base §§9.3–9.6, 9.11; Amendment 1 §2 | Two cold-start agents classify the same issue differently because one accepts a malformed, edited, unsupported-transition, or future-dated capsule and the other rejects it. A bad `lease_expires_at` can also make a task appear owned indefinitely or immediately stale. | Operational state depends on the “latest valid structured status capsule,” but the proposal never defines validity, authoritative ordering, edit handling, timestamp authority, or the exact transition validator. Lease timestamps are self-authored fields rather than explicitly derived from an authoritative server timestamp. | Define an append-only capsule protocol with an exact schema/version, allowed authoring role, transition matrix, prerequisite checks, ordering by immutable GitHub comment identity/server creation time, and explicit treatment of edited comments. Derive lease expiry from authoritative creation time plus the policy TTL; do not trust arbitrary self-declared future times. Invalid capsules must be ignored deterministically and explainably. |
| F-04 | BLOCKER | Base §§11.6, 14, 21; Amendment 1 §8; Amendment 2 §3 | Issue #5 or `W1-VERIFY-01` passes an exact synthesis SHA, then the integration agent “materializes” it into canonical files, rewrites entry documents, and instantiates issue bodies. A copy error, omission, or discretionary interpretation changes operational policy after the verified SHA. The result becomes canonical even though the actual canonical diff/issue graph was never what the verifier tested. | Verification is tied to the synthesis candidate SHA. Canonicalization is described as a later transformation with broad verbs such as materialize, update, instantiate, promote, and supersede. No verified promotion manifest constrains source SHA → destination path → exact generated issue contract. | Make canonicalization a mechanically constrained promotion. The synthesis candidate must emit a machine-readable canonicalization manifest containing each source artifact/SHA, destination path, authority transition, supersession action, and exact issue contract/manifest to instantiate. The verifier must verify that manifest. The integrator may perform only byte-identical or explicitly enumerated transformations. Any unverified transformation requires a post-materialization verification before activation/merge. |
| F-05 | BLOCKER | Base §§9.7, 14, 21; Amendment 2 §§3–4 | The verifier passes a candidate based on main state M1. Before canonicalization merges, `main` advances to M2 with a new governance rule, human directive, or incompatible planning change. The integration agent checks only the candidate/PR head SHA and verification status, so GitHub can still squash-merge the stale candidate into a logically different base. | The merge rule requires expected **head** SHA but does not pin/revalidate the verified **base/main** SHA. Canonical authority can therefore be granted against repository state the verifier never inspected. | Record `verified_base_main_sha` for every verification. Immediately before integration require current `main` to equal that SHA, or run an explicit bounded compatibility/reverification step covering every intervening main commit. A changed binding directive must invalidate the old PASS until reverified. |
| F-06 | MAJOR | Amendment 2 §3 | Issue #6 pre-creates Wave 1 issues before its squash merge. Their activation block contains `required_main_sha: <the squash commit produced by Issue #6 integration>`, a value that cannot exist yet. After merge, one agent may treat the placeholder as a dynamic reference while another treats the prerequisite as unresolved forever. | The amendment permits pre-merge instantiation but does not mandate an atomic post-merge patch of all 23 issue contracts or define the placeholder as a typed reference resolved through one specific status capsule. | Prefer the simpler rule: instantiate Wave 1 issues only after Issue #6 has squash-merged and its resulting main SHA is known. If pre-creation is retained, define a typed dynamic reference plus a mandatory post-merge issue-body update and validation pass before any issue can become READY. |
| F-07 | MAJOR | Base §§13, 17.2; Factory Mandate §§6, 11 | A producer starts a new execution episode, generates a fresh UUID, and performs its own review. The recorded reviewer `session_id` differs, so the proposal’s procedural test passes even though evidence acquisition and framing are not independent. | The program says identity is recorded through self-authored per-episode `session_id` and explicitly admits this is not a strong identity guarantee. The seed mandate says the important property is independent evidence acquisition and bounded authority, not cosmetic role labels. | Define operational independence as a distinct cold-start execution context with no producer private context, plus role-exclusion history recorded in issue state. Use a platform/run identity when available; a self-selected UUID alone must never satisfy an independence gate. Keep stronger credential separation as a bounded follow-up, but make the minimum independence test falsifiable now. |
| F-08 | MAJOR | Base §§9.2–9.3, 10.2, 11.3–11.6; Amendment 1 §2 | `W1-REV-TECH` returns `CHANGES_REQUIRED`. One cold-start agent interprets “completed review” as sufficient to unlock synthesis, another expects `CHANGES_REQUESTED` producer revision first, while a third treats any review task as `DONE` regardless of an `INVALIDATED` disposition. The graph state is therefore not derivable from one exact transition predicate. | Review dispositions (`PASS_FOR_SYNTHESIS`, `CHANGES_REQUIRED`, `INVALIDATED`) and issue states (`DONE`, `CHANGES_REQUESTED`, etc.) are both defined, but their mapping and the exact prerequisite predicates for downstream synthesis are not. Several DAG clauses say only “completed review.” | Add a mission-class transition table and machine-readable prerequisite predicates. Define exactly which review disposition maps to which terminal task state, whether `CHANGES_REQUIRED` goes directly to synthesis or producer correction, who owns that correction, and which dispositions do **not** unlock downstream work. |
| F-09 | MAJOR | Base §§9.9, 11.2–11.4, 17.3–17.4; Factory Mandate §5 | Each of six broad root producers emits a very large artifact. A domain reviewer is required to load all six immutable outputs plus status capsules and the program; synthesis then loads the same set plus review findings. The mandatory context exceeds a practical model window and the reviewer silently truncates or shallowly samples evidence. | The proposal mandates progressive context disclosure but places no size budget on root artifacts, evidence ledgers, review fan-in, or synthesis packets. “Bounded” is qualitative only. The seed mandate explicitly treats irrelevant/excessive context as a design defect. | Add measurable artifact/context budgets: maximum mandatory packet size or section/evidence-index budgets, preflight context accounting, required compact claim/interface/evidence indexes, and an automatic split/escalation rule when a domain review packet exceeds the budget. |
| F-10 | MAJOR | Base §§9.11, 11.7; Amendment 1 §9 | `W1-REC-01` fixes a liveness incident and its PR is squash-merged. The same deterministic recovery branch is later “resumed” for a new incident. Its ancestry is now behind/divergent from the squash commit on `main`; without a defined reset/rebase/new-episode branch rule, the next PR can include stale prior commits/diff or require prohibited history rewriting. If recovery changes are not merged, the restored state may never become canonical. | The service mission is explicitly reusable on one deterministic branch, but normal integration is squash-only and no reusable-branch lifecycle is defined after a squash merge. | Make each liveness activation a distinct episode with its own deterministic child issue/branch, or define an explicit service-branch reset mechanism owned by the dispatcher after each episode. Also define which recovery outputs/remediations require review/integration before they affect canonical graph state. |
| F-11 | MAJOR | Base §§11.5–11.6, 22; Amendment 1 §8; Planning Deliverables §14 | `W1-SYN-FINAL` emits hundreds of `next_wave_candidates`; `W1-CANON-01` instantiates them because the only bound is prose saying “bounded next wave.” The project recreates the mass-backlog failure mode through the canonical path. | `next_wave_candidates` has no required mission-contract schema, count/WIP cap, or issue-compiler validation rule. The seed deliverables explicitly require issue sizing, dependency extraction, issue validation, and graph audit before mass generation. | Define a next-wave candidate schema identical in rigor to the planning issue contract, plus a hard instantiation/WIP cap or frontier budget. Excess candidates remain deferred data, not GitHub issues. Require an issue-compiler validation/audit step before canonicalization creates the next wave. |
| F-12 | MINOR | Amendment 1 §7 versus Amendment 2 authority/preamble | The “exact bootstrap-chain output paths” section still lists the Issue #2 proposal set as only the base proposal plus Amendment 1. A literal context loader following that list can omit Amendment 2, even though Amendment 2 later states it is part of the complete proposal set. | Amendment 2 was added later but does not explicitly replace the older two-file enumeration. Issue #2 handoff/status corrects this operationally, but the proposal set is internally untidy. | Issue #4 must take all three Issue #2 files as explicit immutable inputs and replace the amendment stack with one reviewed candidate. Remove the stale two-file enumeration from operational guidance. |
| F-13 | MINOR | Base §9.4 | A session can repeatedly renew a lease with low-value `PROGRESS` capsules and monopolize a task without materially advancing work. | Renewal requires head/checks but does not define minimum useful progress, maximum renewal count, or checkpoint routing for repeated renewals. | Require renewal evidence of substantive branch-head advance or a bounded check/experiment result; after repeated renewals without unblock value, route the task to recovery/checkpoint review. |
| F-14 | NOTE | Base §§11–12, 15, 17.4 | The advertised 12-wide root frontier is filesystem-conflict-safe, but semantic dependencies may collapse it earlier than expected. | Several roots intentionally overlap on control plane, evidence, runtime, and evaluation. The proposal does plan synthesis/review for semantic conflicts and already records frontier width as a metric. | Keep this as an explicit first-wave measurement/reopen trigger. Do not treat “12 branches existed” as evidence that 12-way useful parallelism was achieved. |

## Detailed failure analysis

### F-01 — Claim creation has an unrecoverable crash window

This is a concrete cold-start liveness failure, not a theoretical race. Section 9.4 deliberately uses deterministic branch creation as the exclusion primitive and posts the ownership capsule only afterward. That ordering is sensible for duplicate prevention, but it creates a transactional gap. If the agent disappears after the branch is created, every later agent correctly refuses to create an alternate branch. Yet Section 9.6 only declares `IN_PROGRESS` work recoverable after a lease expiry, and no lease exists.

The liveness service can diagnose that the graph is stuck, but the normal branch has no defined legal takeover state. A protocol whose first mutation can strand a task cannot pass the Issue #5 scenario “task branch existing with no useful handoff” without an orphan-claim rule.

### F-02 — Lease expiry is not ownership revocation

The proposal treats a six-hour comment lease as if expiry made the branch safely recoverable. Expiry only changes what a compliant observer believes; it does not fence the old session from writing. This matters even with well-behaved agents because a long experiment, temporary API outage, suspended execution, or clock/state lag can cause the old session to continue after expiry.

The minimal planning-phase remedy is not necessarily a full dispatcher service, but it must include a write-fencing convention strong enough to make stale writers fail closed: current lease generation must be re-read immediately before every branch mutation, branch writes must be expected-head/fast-forward only, and a lease-generation mismatch must terminate the stale episode. The mature control plane can later replace this procedural fence with a machine-enforced claim primitive.

### F-03 — “Valid status” is a hidden interpreter

Derived READY/BLOCKED state is a good direction, but determinism depends entirely on the word “valid.” The proposal does not define a validator. It also lets the capsule itself supply timestamps that determine ownership duration. That means the cold-start agent must invent policy for malformed fields, unsupported transitions, conflicting capsules, edited comments, or implausible lease times.

This is exactly the class of hidden policy the program is trying to eliminate. Validity must become explicit data/schema plus a transition algorithm, not reviewer common sense.

### F-04 — Verification stops one step too early

The most serious authority defect is the gap between “verified candidate” and “canonical state.” Bootstrap Issue #6 and `W1-CANON-01` do more than merge a verified blob: they move/transform artifacts, update entry points, mark supersession, and create GitHub issues. Those actions define the actual dispatcher that the next cold-start agent will obey.

If the verifier passes only the synthesis SHA, the integration agent can accidentally or intentionally change semantics after the quality gate. Independence of the integration role does not solve this; it only changes who can make the unverified mistake. The canonicalization plan must itself be part of the verified object, and the integration diff/issue manifest must be constrained to that plan.

### F-05 — Expected PR head is insufficient for canonical integration

Checking `expected_head_sha` protects against the candidate branch moving. It does not protect against the base moving. A new main commit can change `AGENTS.md`, the canonical Planning Program, or another binding rule between verification and merge. The candidate can remain byte-identical while its meaning relative to the repository changes.

For an authority transition, both sides matter: the exact verified candidate and the exact verified base. A changed base should force a compatibility decision or re-verification, not silently inherit an old PASS.

### F-06 — Pre-merge activation SHA is unknowable

The activation barrier is conceptually correct and substantially improves the base proposal. The remaining defect is representational: a future squash commit SHA cannot be embedded as a concrete hard prerequisite before the merge creates it. The program should avoid a placeholder whose interpretation is left to later agents. Post-merge issue creation is simpler and keeps the activation fact concrete from birth.

### F-07 — Different UUID is not independent evidence acquisition

The seed factory mandate is precise that role separation is about independent evidence acquisition and bounded authority, not personalities. The proposal’s `session_id` mechanism is useful for episode tracking but insufficient as the gate itself. A producer can satisfy `session_id A != session_id B` without losing its prior framing/context.

The bootstrap can still operate before strong identity infrastructure exists, but the minimum rule should require a separate cold-start execution context with no producer private context and record enough run provenance for a later auditor to detect role reuse. Stronger credential/model diversity can remain a first-wave trust-planning question.

### F-08 — State machine and review disposition are two partially overlapping languages

The proposal has both issue states and review dispositions, but no normative mapping between them. This matters because eligibility is supposed to be derived without human interpretation. A review with serious but synthesizable findings is not the same thing as an invalidated upstream design, and those must unblock different paths.

Issue #4 should make each mission class expose exact allowed transitions and exact downstream predicates, preferably as machine-readable fields in the issue contract rather than prose words such as “completed.”

### F-09 — The context budget has no budget

Progressive disclosure controls which files are loaded, but it does not control how large those files may become. The first-wave root missions are broad enough that six compliant artifacts could individually be substantial. Domain review and synthesis then deliberately fan them in.

Without a measurable packet budget, “load only the authoritative inputs” can still mean “load more context than can be inspected reliably.” The program should budget mandatory context and require compact indexes/digests that are themselves traceable to full evidence.

### F-10 — Reusable recovery state conflicts with squash-only branch history

`W1-REC-01` is the only mission explicitly intended to have repeated activations on the same branch. That makes it different from normal task-lifetime branch semantics. Squash integration breaks the branch ancestry relationship that would make indefinite reuse straightforward. The program needs an episode model, not merely repeated handoff comments on one branch.

This can be fixed without giving recovery broad policy authority: a stable service issue can dispatch bounded child recovery episodes, each with deterministic ownership and ordinary review/integration rules.

### F-11 — Next-wave issue generation lacks a hard governor

The proposal correctly refuses to instantiate the 50 seed missions. However, the final synthesis can create an arbitrary `next_wave_candidates` list, and canonicalization is told only to instantiate a “bounded” next wave. That moves the backlog explosion risk rather than eliminating it.

A hard frontier/WIP budget plus an issue-compiler validator would turn “bounded” into a testable property. Candidate missions beyond the budget can remain in the dependency map for future checkpoint selection without becoming active GitHub work.

## Cross-domain contradictions

1. **Atomic-enough ownership versus explicit factory safety.** The program presents deterministic branch creation plus leases as sufficient to operate Wave 1, while the factory mandate says a task should have exactly one active owner and claiming must verify stale/duplicate state. The orphan-branch and unfenced-expiry scenarios show that the current protocol does not yet preserve that invariant in all allowed states.
2. **Progressive context versus large review fan-in.** The context-loading protocol minimizes file count, while the mission graph requires reviewers/synthesizers to consume five or six potentially unbounded broad artifacts. The two goals are not reconciled by a measurable context budget.
3. **Exact-SHA verification versus discretionary canonicalization.** The program strongly prefers immutable upstream SHAs, then allows the final authority transition to transform/materialize content and issue contracts after verification. That breaks the exact-object principle at the most sensitive step.
4. **Repository/GitHub state as deterministic memory versus undefined capsule validity.** The program correctly removes hidden chat state, but still requires each agent to infer what makes a GitHub status capsule valid. That inference is hidden operational policy unless codified.
5. **Squash-only integration versus reusable recovery branch.** Normal branch lifetime assumes one task culminating in a squash integration. `W1-REC-01` is designed as a repeatedly resumed service task without a post-squash branch lifecycle, creating a direct lifecycle mismatch.

## Unresolved empirical questions

These questions should be answered by Issue #4 only if necessary to choose a bootstrap-safe rule; otherwise they should become explicit first-wave experiments without weakening the corrected protocol:

1. Which GitHub operation available to agents can provide the strongest expected-head / compare-and-swap semantics for task-branch writes without force-push?
2. What authoritative GitHub metadata should define status ordering and lease start time, and how should edited comments be detected/invalidated?
3. What practical mandatory-context budget allows one reviewer to deeply inspect six planning artifacts; at what threshold must review be split?
4. Can the platform expose a stable execution/run identity sufficient to enforce “different cold-start execution context,” or must the first-wave trust model add a separate reviewer dispatcher/credential boundary?
5. Can Issue #6 cleanly perform `merge -> obtain main SHA -> instantiate issues -> post DONE` as one integration episode; if yes, this is preferable to pre-creating issues with an unresolved activation SHA.

None of these empirical questions requires routine human approval.

## Disposition

**CHANGES_REQUIRED.**

The proposal is **ready for synthesis/revision by Issue #4**, because the defects are bounded and have concrete correction paths. It is **not ready for cold-start PASS, canonicalization, or Wave 1 activation** in its current form.

Issue #4 must explicitly disposition every BLOCKER and MAJOR finding. In particular, no revised candidate should advance to Issue #5 unless it can demonstrate all of the following from repository + GitHub state alone:

- a branch-created-before-claim crash has a deterministic recovery path;
- an expired lease cannot leave two compliant sessions authorized to write the same task branch;
- capsule validity/state transition/lease timing is deterministic and append-only enough to reconstruct;
- the exact canonicalized files and generated issue contracts are covered by verification, not transformed afterward without another gate;
- canonical integration is bound to both candidate SHA and verified main/base SHA;
- review dispositions map to exact downstream eligibility states;
- required review/synthesis context has an enforceable budget/splitting rule;
- reusable recovery work has a lifecycle compatible with squash-only integration;
- next-wave issue instantiation has an explicit hard governor and validation step.

## Required next action

Bootstrap Issue #4 should consume this review plus the complete three-file Issue #2 proposal set, fold the amendments into one candidate, and create explicit finding dispositions. Accepted fixes should be incorporated directly into the candidate; rejected findings require concrete counter-evidence; unresolved BLOCKER/MAJOR items must become bounded empirical questions that keep the affected transition non-canonical until resolved.
