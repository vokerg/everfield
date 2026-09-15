# Planning Program v1 — Canonical

**State:** CANONICAL  
**Authority:** CANONICAL planning operating model for the current pre-implementation PLANNING phase.  
**Canonicalized by:** Issue #1147  
**Active canonical base while this candidate is inert:** `docs/planning/PLANNING-PROGRAM-v1.md` blob `e3120ec203c4156328770aa86c12fbb7187966dc`, bound by Issue #6 comment `5245368879`, activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e`.

## 1. Exact composition and preservation rule

This candidate is a narrow overlay over the exact active canonical Planning Program v1 identified above.

- Every active canonical clause remains normative unless this candidate explicitly adds a temporal predicate below.
- This revision does not delete, relax, reinterpret, or broaden existing schema-3 structural validity, contention, ownership, handoff, terminal, review, verification, canonical-binding, context, implementation-readiness, or squash-only integration rules.
- On any semantic conflict outside the explicit temporal additions below, the exact active canonical program blob `e3120ec203c4156328770aa86c12fbb7187966dc` wins and verification MUST fail closed.
- The reviewed governance source is Issue #1124 / PR #1125 candidate blob `a59f04feb2c7e0344fdaab1fcbf4fa291e79a107`, cleanly reviewed by Issue #1126 terminal comment `5659773876` with disposition `PASS_FOR_CANONICAL_LEASE_SEMANTICS_REVISION`.

The six-hour value is a new reviewed governance decision. It is not represented as already active canon. Historical repository provenance is evidence for minimizing behavioral divergence only.

## 2. Schema-3 task ownership lease

For a canonical schema-3 ownership generation, define:

```yaml
schema3_task_ownership_lease_seconds: 21600
authoritative_clock: github_server_comment_created_at
expiry_boundary: t >= lease_anchor + 21600s
```

A generation is unexpired at time `t` iff `t < lease_anchor + 21,600 seconds`; it is expired at the exact boundary and thereafter.

This lease applies only to kinds that the effective canonical task contract already declares as creating a schema-3 ownership generation. It does not create eligibility for historical bootstrap work or activate undeclared generic mechanisms.

## 3. Authoritative temporal evidence

For every temporal authority decision in this lease overlay:

1. the sole authoritative timestamp is the GitHub API comment `created_at` of the relevant operational record;
2. timestamps written in comment bodies, extensions, commits, local clocks, workflow clocks, client receive times, or `updated_at` have zero lease authority;
3. `created_at` MUST be a parseable timezone-aware RFC 3339 instant and comparisons are absolute instants;
4. an edited operational comment remains subject to the existing unedited-comment integrity rule; `updated_at` never renews a lease;
5. a required `created_at` that is absent, null, malformed, or timezone-naive makes that record temporally invalid;
6. malformed or missing time on a current-owner record MUST NOT be treated as proof of expiry. Evaluation fails closed and cannot manufacture STALE authority.

Existing lowest-valid-GitHub-comment-ID contention remains the winner rule where the canonical contract already uses it; equal timestamps do not introduce a new tie-break mechanism.

## 4. Ownership-generation anchor

A valid winning ownership-generating record starts its generation lease at its authoritative `created_at`.

```text
lease_anchor(G) = created_at(G)
lease_expires_at(G) = lease_anchor(G) + 21,600 seconds
```

This includes `CLAIM`, `RESUME`, and `RECOVER`, plus only those additional kinds that an effective canonical task contract explicitly defines as a new schema-3 ownership generation. Historical bootstrap-numbered clauses remain `PROVENANCE_ONLY` in `CANONICAL_ACTIVE`. `VERIFICATION_RESTART` / `VERIFICATION_REFRESH` remain usable only where the canonical task graph or a later canonical revision actually declares them.

## 5. PROGRESS renewal

`PROGRESS` renews the existing current generation; it never creates a new generation.

A PROGRESS record renews iff all pre-existing canonical PROGRESS rules hold and the referenced generation is still current and unexpired at `created_at(PROGRESS)`.

For a valid renewal `P`:

```text
lease_anchor(current_generation) = created_at(P)
lease_expires_at = created_at(P) + 21,600 seconds
```

The existing progress constraints remain intact:

- `observed_head_sha` must equal the current branch head;
- `HEAD_ADVANCE` must actually observe a new head and resets the consecutive-EVIDENCE counter to zero;
- `EVIDENCE` must carry nonempty immutable evidence references;
- at most three consecutive valid `EVIDENCE` renewals may occur without a valid `HEAD_ADVANCE`;
- the fourth consecutive EVIDENCE record is invalid and does not move the lease anchor;
- all ordinary schema/type/issue/mission/branch/actor/comment-integrity rules remain required.

An otherwise well-formed PROGRESS created at or after expiry is invalid and cannot resurrect the generation.

## 6. HANDOFF and terminal owner records

Any owner-authored `STATUS(HANDOFF_READY)`, terminal `STATUS`, `REVIEW_STATUS`, `VERIFICATION_STATUS`, or `INTEGRATION_STATUS` whose effective canonical kind requires current-owner authority MUST be created while the referenced generation is current and unexpired.

At the exact expiry instant or later, a prior owner cannot publish an authoritative handoff or terminal result.

A valid HANDOFF_READY published before expiry preserves the existing HANDOFF continuation route: subsequent continuation uses the canonical HANDOFF `RESUME_INTENT` -> winning `RESUME` transition. STALE recovery MUST NOT be substituted for a valid handoff.

A valid terminal owner record ends that generation according to the existing canonical state machine. Later PROGRESS/HANDOFF/terminal attempts from the ended generation have zero authority effect.

## 7. STALE recovery temporal predicate

STALE recovery is valid only when temporal expiry is proven in addition to every existing structural/source/head/current-generation/winning-intent/first-valid-grant predicate.

For a current generation with latest valid lease anchor `A`:

1. `RESUME_INTENT(reason=STALE)` with `created_at < A + 21,600s` is premature, invalid, and has zero authority;
2. it is temporally eligible at `created_at >= A + 21,600s`;
3. authority must be reconstructed through the intent comment, proving no later valid renewal, HANDOFF, terminal, or owner generation displaced the source;
4. the existing lowest-valid-comment-ID winner rule remains applicable to otherwise valid competing STALE intents for the exact source/head;
5. `RECOVER(recovery_reason=STALE)` must bind the winning intent and exact stale generation and must re-prove staleness/no intervening valid authority at the recovery comment;
6. only the existing first valid recovery grant for that winning intent creates the next owner generation.

Premature or losing STALE records cannot supersede a valid current owner.

## 8. ORPHAN recovery temporal predicate

The existing canonical ORPHAN maturity remains exactly 600 GitHub-server seconds from the authoritative `created_at` of the valid `ORPHAN_PROBE`.

```text
orphan_matures_at = created_at(ORPHAN_PROBE) + 600 seconds
```

A matching `RESUME_INTENT(reason=ORPHAN)` is temporally eligible only at or after that exact boundary and only if no valid owner appeared after the probe. A later valid owner invalidates the orphan route.

`RECOVER(recovery_reason=ORPHAN)` remains subject to all existing exact probe/head, winning-intent, actor/source, no-later-owner, and first-valid-grant predicates. The exact ten-minute boundary is mature.

## 9. Prefix-scoped ownership reconstruction and non-retroactivity

Consumers MUST reconstruct ownership in GitHub comment order through the operational comment being evaluated, applying both structural validity and the temporal predicates in this overlay.

Minimum behavior:

1. accept only structurally valid ownership grants;
2. reject losing duplicate CLAIM/RESUME/RECOVER contenders;
3. apply PROGRESS only to the current still-unexpired generation and update its lease anchor only when valid;
4. ignore premature/invalid STALE and ORPHAN intents/grants;
5. terminate or transition ownership only through valid canonical HANDOFF/terminal transitions;
6. never infer the current owner from the raw latest ownership-shaped comment alone.

Later recovery cannot retroactively invalidate a terminal result that was authoritative at the time it was published. Conversely, a stale prior-owner terminal published after a valid later ownership generation is invalid.

## 10. Stage-B separation

Inactive Stage-B IntegrationUnit/global coordination TTLs are a separate protocol surface. This candidate does not activate, copy, reinterpret, or conflate those TTLs with schema-3 task ownership.

## 11. Mandatory verification scenarios

Fresh verification/compatibility MUST exercise at least:

1. CLAIM at `12:00:00Z`; STALE intent `17:59:59.999Z` invalid; exact-boundary `18:00:00Z` temporally eligible;
2. valid PROGRESS at `17:00Z` moves the boundary to `23:00Z`; STALE at `18:01Z` remains invalid;
3. EVIDENCE E1/E2/E3 renew; E4 without HEAD_ADVANCE is invalid and anchor remains E3;
4. PROGRESS at exact expiry cannot resurrect the generation;
5. old-owner terminal at/after expiry is invalid;
6. valid HANDOFF before expiry routes through HANDOFF RESUME, not STALE;
7. ORPHAN intent before 600s invalid and at exact 600s eligible; a later owner invalidates ORPHAN;
8. losing duplicate CLAIM/RESUME/RECOVER records never supersede the valid winner;
9. malformed/missing/naive required `created_at` fails closed without manufacturing staleness;
10. prefix-scoped evaluation preserves a terminal valid at its publication point against later recovery, while rejecting stale prior-owner terminal publication after valid recovery;
11. `CANONICAL_ACTIVE` bootstrap-numbered work remains provenance-only and generic restart/refresh is not broadened beyond declared tasks;
12. inactive Stage-B TTLs remain inactive and separate.

PASS is forbidden with any unresolved BLOCKER or MAJOR or correction-requiring MINOR finding against these semantics or any regression in the active canonical base.

## 12. Activation and canonicalization boundary

This file is `NOT_CANONICAL`. Creating, reviewing, merging, or making its PR mergeable does not change the active binding.

The required authority sequence is:

1. fresh required verification/compatibility of this exact candidate and companion manifest against then-current `main` and the active canonical base;
2. correction/restart if candidate or manifest bytes change after verification;
3. a separately scoped canonicalization episode with explicit authority, expected-head/base checks, and squash-only publication;
4. durable publication of a new canonical binding for the promoted program blob before any consumer may rely on the six-hour predicate;
5. only after that binding is active may the blocked factory maintenance remediation re-derive and consume these temporal semantics;
6. that maintenance remediation remains independently review-gated before integration.

Until those gates complete, Issue #6 comment `5245368879` and program blob `e3120ec203c4156328770aa86c12fbb7187966dc` remain the sole active canonical basis.


## 13. Deterministic promotion contract

The companion revision manifest is the sole authority for mechanically promoting this verified noncanonical candidate into the canonical program path. Promotion is permitted only after a fresh exact-payload verification PASS and a separately authorized canonicalization issue exists.

The promotion operation has exactly one runtime provenance parameter: the positive GitHub issue number of that separately authorized canonicalization episode. That parameter may affect only the canonical provenance header identifying the binding issue. It is not a semantic option and may not alter this lease overlay, the inherited active-base semantics, or any other byte.

The manifest defines exactly four header replacements: title, state, authority, and revision-issue provenance. Every source literal must occur exactly once; the canonicalization issue number is encoded as canonical base-10 digits with no leading zero and substituted only into the declared canonicalized-by output literal; every remaining candidate byte is copied identically. Missing/duplicate source literals, an unbound or wrong canonicalization issue, any candidate/manifest identity drift, or any other byte mutation fails closed.

The canonicalization issue contract must bind the exact verified candidate blob and exact verified manifest identity before the parameter is usable. Its terminal schema-3 integration record must be published on that same issue and bind the resulting canonical program blob. This mechanical provenance substitution does not waive verification, expected-head/base checks, squash-only integration, or durable binding requirements.

Any change to this candidate or companion manifest after verification requires a fresh full verification episode before promotion.
