# ARCH-CONVERGENCE-REV-02 — Independent architecture review

**Issue:** #167  
**Reviewed issue:** #163 / `ARCH-CONVERGENCE-REM-02`  
**Reviewed head:** `d1278e755fe71a4a718618b661f94dc1a51cb285`  
**Reviewed candidate blob:** `42e130f4c0faf4db181b26d9f7e3ae86e270f6f7`  
**Reviewed PR:** #165 at the exact reviewed head  
**Review base:** `main@268f697ad788942a2b6ff373fee1d20d32715e52`  
**Trust profile:** `DEGRADED_SINGLE_AGENT`; fresh independent reviewer episode; candidate immutable and not edited here.  
**Disposition:** `CHANGES_REQUIRED`  
**Findings:** 0 BLOCKER / 2 MAJOR / 0 correction-requiring MINOR.

## Scope

Revision 2 materially fixes the two findings from Issue #152: the checked `main` base now has a pre-mutation CAS-equivalent guard, and the global publication lease plus IntegrationUnit ownership have explicit discoverable generation/recovery state machines. The review nevertheless found two new publication-authority gaps.

## Attack results

- **Checked-base race:** PASS. A one-parent squash commit `S(parent=A)` published only by non-force ref update fails before mutation if `main` has moved away from A.
- **Global ledger topology:** PASS. One PolicyEpoch-bound control issue, server-time generations, deterministic contention, and stale recovery are specified.
- **Lease/IntegrationUnit authority through publication:** FAIL / `ARCH-REV2-M01`. The mandatory authority recheck occurs on acquisition, while Section 6 immediately before publication rechecks only PR head and `main`. A generation can expire and be superseded while the old actor remains continuously inside the critical section; the old actor can still attempt the otherwise-valid `A -> S` publication. The main CAS prevents two sibling commits from both landing, but it does not guarantee that the still-authoritative generation is the one that lands.
- **Source PR-head movement:** FAIL / `ARCH-REV2-M02`. The final `PR head == H` test is observational. If the source PR advances after that read but before the main ref update, `S` built from H may still publish because the server-enforced condition protects only base A. The result remains the H packet, but the candidate declares current PR-head equality to be a publication precondition and may then close a PR whose current head contains later commits.
- **Disjoint versus relevant main churn:** PASS. Relevant path/dependency/policy/control drift fails closed; provably disjoint churn can proceed without global re-review.
- **Review-provenance leakage and recursion:** PASS. Negative review provenance keeps `acceptance_authority: NONE`; producer self-review does not become independent acceptance; review-of-review is not invented.
- **Aggregate review, verification, canonicality, readiness, history:** PASS. These remain separate typed gates.
- **Activation boundary:** PASS. A separately reviewed schema/PolicyEpoch with effective-from identity and migration rules is still required.

## Findings

### ARCH-REV2-M01 — MAJOR — publication is not bound to still-current IntegrationUnit/global-lease authority

The recovery state machines can supersede an expired owner, but publication does not prove that the publishing actor's IntegrationUnit generation and global lease generation are still current at the mutation boundary. An extra ordinary read just before the ref update would only narrow the same check-to-write interval.

**Required correction:** define a publication-authorization mechanism whose validity cannot be superseded between authority validation and the `main` mutation, or redesign lease semantics so the atomic publication operation itself is the sole safe winner rather than treating an independently expiring comment lease as mutation authority. The correction must cover both IntegrationUnit and global lease generations while preserving bounded stale recovery, and must test recovery occurring while the old actor is continuously executing inside the critical section.

### ARCH-REV2-M02 — MAJOR — source-head equality remains outside the atomic publication condition

The base CAS closes `main` movement but not source PR movement. The design requires `PR head == H`, yet that condition can become false after the final read and before `main` publication without causing the main ref update itself to fail.

**Required correction:** choose one coherent model. Either current source/PR-head equality is a real publication precondition and must be enforced without a residual read/write gap, or immutable terminal H is the sole integration authority and later PR-head movement must be explicitly irrelevant, with PR linkage/closure semantics that do not imply later commits were integrated. The current hybrid is not fail closed.

## Disposition

`CHANGES_REQUIRED`. `ARCH-REV2-M01` and `ARCH-REV2-M02` are bounded architecture defects; Revision 2 is not invalidated. Exactly one bounded remediation successor should revise the immutable Issue #163 candidate and then return through the bounded fresh re-review route. No canonical protocol/schema revision, migration, IntegrationUnit execution, global lease acquisition, direct-main-ref publication, readiness transition, or workflow activation may treat Revision 2 as passed architecture.

This review grants no merge, integration, canonicalization, readiness, production, implementation, verification, release, or legal/provider authority.
