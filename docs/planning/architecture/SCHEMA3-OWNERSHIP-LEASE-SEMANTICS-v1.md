# Schema-3 Ownership Lease Semantics v1 — Governance Candidate

**Mission:** `FACTORY-LEASE-SEMANTICS-01` / Issue #1124  
**State:** `NONCANONICAL_GOVERNANCE_CANDIDATE`  
**Producer base:** `main@51cc20dbbc4ebbbdea9bbde91e480776b0e4b047`  
**Active canonical binding while this candidate is inert:** Issue #6 comment `5245368879`, Planning Program blob `e3120ec203c4156328770aa86c12fbb7187966dc`  
**Blocked finding:** `FACTORY-CONVERGENCE-06-REM-02-REV-MAJ01`  
**Authority:** candidate clarification only. This file does not change the active canonical program, authorize maintenance code changes, satisfy required review/verification, or grant integration/canonical/readiness/release authority.

## 1. Purpose and minimal decision

The active schema-3 contract defines owner expiry qualitatively but does not currently make expiry mechanically decidable. This candidate closes only that governance gap.

The proposed canonical task-ownership lease is:

```yaml
schema3_task_ownership_lease_seconds: 21600
expiry_boundary: created_at >= lease_anchor_created_at + 21600s
authoritative_clock: github_server_comment_created_at
```

That is a fixed six-hour lease.

This value is proposed, not inferred as already canonical. Repository provenance previously recorded a six-hour task-ownership expectation in Issue #27, but that record was explicitly non-authoritative. Choosing the same duration minimizes behavioral change while converting the previously implicit expectation into an exact reviewable rule. Independent review, canonical-program revision, verification, compatibility checks, and canonicalization remain mandatory before this value has authority.

The inactive Stage-B architecture candidate's IntegrationUnit/global coordination TTLs are a separate protocol and are not changed or activated by this candidate.

## 2. Authoritative timestamp and parsing

For schema-3 temporal authority:

1. only GitHub API comment `created_at` is an authoritative time source;
2. timestamps written inside comment bodies, prose, extensions, branch commits, local clocks, workflow clocks, or client receive times have no lease authority;
3. `created_at` MUST parse as a timezone-aware RFC 3339 instant; fractional seconds are permitted and comparisons are performed as absolute UTC instants;
4. an edited operational comment remains invalid under the existing unedited-comment rule; `updated_at` never becomes a renewal clock;
5. a required `created_at` that is missing, null, malformed, or not timezone-aware makes that operational record temporally invalid and gives it zero authority effect;
6. malformed time on a current-owner record MUST NOT be interpreted as "expired." The evaluator fails closed: it cannot authorize STALE recovery from an unprovable expiry and must route explicit repair/governance recovery instead;
7. equal server timestamps do not create a second tie-break rule. Existing lowest-valid-GitHub-comment-ID contention rules continue to determine winners where applicable.

## 3. Ownership generation and lease anchor

A valid ownership-generating record starts a six-hour lease at that record's authoritative `created_at`.

This applies to every canonical schema-3 kind whose defined effect is a new owner generation, including:

- `CLAIM`;
- `RESUME`;
- `RECOVER`;
- `BOOTSTRAP_RESUME` only where a canonical contract actually permits the bootstrap bridge;
- `VERIFICATION_RESTART` and `VERIFICATION_REFRESH` when a canonical task contract declares those generic mechanisms and they create a new verification ownership generation;
- any later canonical kind only if its canonical definition explicitly says it creates a schema-3 owner generation and does not specify a different reviewed lease contract.

For a generation record `G`:

```text
lease_anchor(G) = created_at(G)
lease_expires_at(G) = lease_anchor(G) + 21,600 seconds
unexpired at t  <=> t < lease_expires_at(G)
expired at t    <=> t >= lease_expires_at(G)
```

The exact expiry instant is therefore stale, not live.

Historical bootstrap-numbered clauses remain provenance-only in `CANONICAL_ACTIVE`; this candidate does not reopen Bootstrap Issue #5 or any other bootstrap work.

## 4. Valid PROGRESS renewal

A `PROGRESS` comment renews only the existing current generation; it never creates a new generation.

A PROGRESS record renews the lease iff all existing canonical PROGRESS validity rules hold, including:

- it references the current unexpired ownership generation;
- `observed_head_sha` equals the current branch head;
- `HEAD_ADVANCE` actually observes a new head;
- `EVIDENCE` carries nonempty immutable evidence references;
- no more than three consecutive valid `EVIDENCE` renewals occur without a valid `HEAD_ADVANCE`;
- all ordinary schema/type/issue/mission/branch/actor/comment-integrity rules hold.

For a valid renewal `P`:

```text
lease_anchor(current_generation) = created_at(P)
lease_expires_at = created_at(P) + 21,600 seconds
```

The consecutive-EVIDENCE counter begins at zero for a new ownership generation. A valid `HEAD_ADVANCE` resets it to zero. A valid `EVIDENCE` increments it. The first three consecutive EVIDENCE renewals are permitted; a fourth consecutive EVIDENCE record is invalid and does not renew the lease. Its timestamp cannot become a later anchor. A later valid HEAD_ADVANCE, if submitted while the lease is still unexpired, resets the counter and renews normally.

An otherwise well-formed PROGRESS arriving at or after expiry is invalid because the current-unexpired-owner prerequisite is already false. It cannot resurrect its generation.

## 5. HANDOFF_READY and terminal owner records

A valid owner-authored `STATUS(HANDOFF_READY)`, terminal `STATUS`, `REVIEW_STATUS`, `VERIFICATION_STATUS`, or `INTEGRATION_STATUS` that canonically requires current-owner authority MUST be created while the generation is unexpired.

At the exact expiry instant or later, an old owner cannot publish an authoritative HANDOFF or terminal result.

A valid HANDOFF_READY published before expiry ends normal IN_PROGRESS ownership for routing purposes. Subsequent continuation uses the existing HANDOFF `RESUME_INTENT` -> winning `RESUME` transition; STALE recovery must not be substituted for a valid handoff.

A valid terminal owner record ends the generation. Later PROGRESS, HANDOFF, or terminal attempts from that generation have zero authority effect.

## 6. STALE recovery temporal predicate

A STALE recovery is valid only if temporal expiry is proven in addition to every existing actor/head/source/current-generation/winning-intent/first-valid-grant predicate.

For a current generation whose latest valid lease anchor is `A`:

1. `RESUME_INTENT(reason=STALE)` is premature and invalid when `intent.created_at < A + 21,600s`;
2. it may be temporally eligible when `intent.created_at >= A + 21,600s`;
3. before accepting the intent, reconstruct all valid generation/PROGRESS records through that comment and prove no later valid renewal, HANDOFF, terminal, or owner generation displaced the source;
4. the lowest valid STALE intent for the same exact source/head remains the winner under existing contention rules;
5. `RECOVER(recovery_reason=STALE)` must bind that winning intent and exact stale source generation, and at `recover.created_at` the source must still be stale with no intervening valid owner/renewal/status;
6. the first valid recovery grant for the winning intent is the only grant that creates the new owner generation.

A losing or premature intent/recovery has zero authority effect and cannot displace the real current owner.

## 7. ORPHAN recovery temporal predicate

The existing canonical orphan maturity is ten GitHub-server minutes.

For valid `ORPHAN_PROBE` comment `O`:

```text
orphan_matures_at = created_at(O) + 600 seconds
```

A `RESUME_INTENT(reason=ORPHAN)` is temporally eligible only when its authoritative `created_at >= orphan_matures_at` and no valid owner appeared after the probe. A premature ORPHAN intent is invalid.

A `RECOVER(recovery_reason=ORPHAN)` is valid only when:

- it binds the lowest valid ORPHAN intent for the exact mature probe/head;
- `recover.created_at >= orphan_matures_at`;
- the branch head still equals the observed probe/head identity required by the existing schema;
- no valid owner appeared after the probe and before the grant;
- all existing actor/source/head/first-valid-grant predicates hold.

The exact ten-minute boundary is mature.

## 8. Winning ownership reconstruction

Any consumer that asks "which ownership generation is current at comment X?" MUST reconstruct authority in GitHub comment order while applying both structural and temporal validity.

Minimum behavior:

1. begin with no owner;
2. accept only structurally valid ownership grants;
3. reject losing duplicate CLAIM/RESUME/RECOVER contenders;
4. apply valid PROGRESS only to the current, still-unexpired generation and update its lease anchor;
5. ignore invalid/premature STALE and ORPHAN intents/grants;
6. accept STALE/ORPHAN RECOVER only after the predicates in Sections 6-7 hold;
7. terminate/transition ownership on valid HANDOFF or terminal status as the canonical state machine requires;
8. never treat the raw latest ownership-shaped comment as current merely because it has the highest comment ID.

Consumers evaluating an earlier terminal comment must use only authority records available through that terminal comment. Later recovery cannot retroactively invalidate a terminal record that was valid when published, while a stale prior owner's terminal after a valid recovery remains invalid.

## 9. Adversarial examples

### A. Premature and exact-boundary STALE

Ownership generation starts at `2026-09-14T12:00:00Z`. No renewal occurs.

- STALE intent at `17:59:59.999Z`: invalid.
- STALE intent at `18:00:00Z`: temporally eligible.
- If the exact-boundary intent wins all existing contention predicates, its first valid RECOVER may create the next generation.
- A terminal result from the old owner at `18:00:00Z` is invalid because the old lease is already expired at the boundary.

### B. Renewal moves the boundary

CLAIM at `12:00Z`; valid PROGRESS at `17:00Z`.

- original `18:00Z` boundary is superseded;
- current boundary becomes `23:00Z`;
- STALE intent at `18:01Z` is premature and invalid;
- STALE intent at `23:00Z` may be eligible.

### C. EVIDENCE renewal cap

After a generation or HEAD_ADVANCE, valid EVIDENCE renewals E1, E2, E3 each renew and increment the consecutive counter. E4 without an intervening HEAD_ADVANCE is invalid and does not move the anchor. Staleness is calculated from E3's `created_at`. A valid HEAD_ADVANCE before that expiry resets the counter and renews the lease.

### D. ORPHAN exact boundary

Probe O at `12:00Z`.

- ORPHAN intent at `12:09:59.999Z`: invalid;
- intent at `12:10:00Z`: may be eligible if no owner appeared;
- any owner appearing after O and before the grant invalidates the orphan route.

### E. Losing contenders

Owner B is current. A later duplicate CLAIM C, or a RECOVER that does not bind the winning intent/source tuple, is invalid regardless of timestamp and cannot make B stale or non-current. A valid no-route terminal from B remains attributable to B.

### F. Stale prior-owner terminal

Owner A expires; valid winning recovery creates owner B. Any later owner-authored terminal from A has zero authority because A is no longer current, even if A's terminal body references its old generation correctly.

## 10. Canonicalization boundary

This candidate deliberately does not edit `docs/planning/PLANNING-PROGRAM-v1.md`, its active Issue #6 binding, or maintenance implementation.

The required authority sequence is:

1. fresh required governance review of this exact candidate;
2. if clean, a separately scoped canonical-program/manifest revision that incorporates these exact lease semantics without weakening existing schema-3 rules;
3. fresh verification of the revised canonical candidate, including the adversarial examples above and compatibility with active work;
4. separately authorized squash-only canonicalization that publishes a new durable canonical binding;
5. only after that binding is active may the blocked factory remediation re-derive and consume this lease predicate;
6. fresh required review of that remediation remains mandatory before any separately authorized integration.

No review or integration of this candidate may be treated as canonicalization.

## 11. Review attack surface

Required review must independently verify at least:

- six-hour / 21,600-second value is an explicit proposed governance choice and not falsely represented as already canonical;
- exact-boundary semantics are deterministic;
- GitHub server `created_at` is the sole lease clock;
- malformed/missing timestamps fail closed without manufacturing staleness;
- valid PROGRESS renewals and the three-EVIDENCE cap are reconstructed correctly;
- fourth consecutive EVIDENCE cannot renew;
- expired generations cannot self-renew;
- premature STALE and ORPHAN recoveries have zero authority effect;
- exact-boundary valid recovery remains live;
- losing contenders never supersede winning ownership;
- HANDOFF and terminal semantics are preserved;
- historical bootstrap clauses are not reopened;
- inactive Stage-B coordination TTLs are not conflated with schema-3 task ownership;
- no maintenance, integration, verification-PASS, readiness, release, or canonical authority is claimed.

Producer self-review: 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR.

## 12. Non-authority

Until the full sequence in Section 10 completes, this document is `NOT_CANONICAL`. It grants no maintenance implementation authority, no integration authority, no verification PASS, no implementation readiness, no engine selection, no production/release authority, and no application-domain decision authority.
