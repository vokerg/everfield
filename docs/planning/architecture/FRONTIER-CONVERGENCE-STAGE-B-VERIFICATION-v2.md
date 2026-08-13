# Frontier Convergence Stage-B verification v2 — Issue #193

**Mission:** `ARCH-CONVERGENCE-VERIFY-01` / Issue #193  
**Verification branch:** `planning/issue-193`  
**Claim generation:** Issue #193 comment `5281032319`  
**Verification base:** `main@3828d50d3345ef0bc5a61321509f590b2e7b2ae1`  
**Trust mode:** `DEGRADED_SINGLE_AGENT_FRESH_VERIFICATION_EPISODE`  
**Disposition:** `PUBLICATION_CAPABILITY_BLOCKED`  
**Stage-B activation:** NOT AUTHORIZED

## 1. Exact frozen candidate

This verification consumes Issue #181 only at its valid terminal schema-3 `STATUS(REVIEW_READY)` comment `5280933066`:

- exact candidate work/head: `ef0187fedc1c00dc9b1f77dec2e84e8c548b8171`;
- candidate PolicyEpoch blob: `73a118e524add90740928c1d623416dc3eaaadec`;
- migration manifest blob: `186c71b76f4749b64647f1ef1bb7adb8b4ac0e17`;
- candidate handoff blob: `ea95c3ec10a4f464b68597ab442a85441812a8e6`;
- exact-head visibility PR: #183, open/draft at the same frozen head;
- candidate state: `NONACTIVE_POLICY_EPOCH_CANDIDATE`;
- candidate publication capability state: `UNPROVEN_PENDING_INDEPENDENT_VERIFICATION`.

The Issue #181 branch and artifacts were treated as immutable read-only inputs. Current canonical Planning Program v1 / Issue #6 authority remains unchanged.

## 2. Verification method and fail-closed rule

The candidate requires a server-enforced exact-old ref transaction equivalent to:

```text
ref          = refs/heads/main
expected_old = A
new          = S
```

PASS requires both logical closure of the mandatory 18-attack suite and concrete repository-specific proof that the available authenticated GitHub transport/credential supports that primitive and applicable repository permission/policy enforcement. Generic REST `force=false`, ordinary PR merge/squash, force push without expected-old binding, and read-then-write are explicitly forbidden substitutes.

No destructive `main` probe was attempted. Capability probing was restricted to connected API introspection and non-mutating execution-host checks.

## 3. Mandatory 18-attack suite

| # | Attack | Independent result |
|---|---|---|
| 1 | Same IntegrationUnit, same base, two publishers | **HOLDS CONDITIONALLY.** Under a true server-side exact-old transaction, the first successful `A -> S1` changes the ref and the second request carrying old `A` must fail before mutation. |
| 2 | Unrelated IntegrationUnits after coordination expiry | **HOLDS CONDITIONALLY.** Coordination overlap does not weaken the exact-old ref arbiter; at most one request from exact base `A` can succeed. |
| 3 | Stale owner and recovered owner overlap | **HOLDS CONDITIONALLY.** The candidate correctly makes comment leases coordination only; split-brain mutation is prevented by the exact-old ref transaction, not lease freshness. |
| 4 | Live PR advances after frozen `H` | **PASS (spec).** Publication source authority is terminal `H`; live PR movement is bookkeeping/provenance only and cannot substitute later bytes. |
| 5 | External `main` forward advance after prepare | **HOLDS CONDITIONALLY.** Any current ref other than exact `A` must reject the request with zero mutation. |
| 6 | External `main` rewind after prepare | **HOLDS CONDITIONALLY.** Exact-old equality rejects a rewound current tip when it is not exactly `A`; this is stronger than non-force ancestry alone. |
| 7 | Delete/recreate or unrelated replacement after prepare | **HOLDS CONDITIONALLY.** Exact current-ref equality is required; replacement identity cannot satisfy old `A`. |
| 8 | Relevant path/dependency/policy drift | **PASS (spec).** Candidate routes relevant drift to `REFRESH_REQUIRED`/blocked outcomes. |
| 9 | Proven disjoint `main` drift | **PASS (spec).** `COMPATIBLE_DISJOINT` is permitted only with complete source/dependency proof; missing legacy dependency data is not treated as disjoint. |
| 10 | Transport failure before update | **PASS (spec).** `TRANSPORT_FAILED_NO_PUBLICATION` is distinct from publication and routes bounded retry/refresh. |
| 11 | Ambiguous response after successful update | **PASS (spec).** Unique `integration_unit_id` marker discovery is required before any retry, preventing duplicate publication when success acknowledgement is lost. |
| 12 | PR divergence or close/link failure | **PASS (spec).** Post-publication PR state is bookkeeping only; divergence records exact `H` and later live head separately. |
| 13 | Negative review provenance authority leak | **PASS (spec).** Negative review storage retains `acceptance_authority: NONE`; storage does not grant canonical/readiness authority. |
| 14 | Producer self-review downgrade | **PASS (spec).** Producer self-review cannot substitute for required independent review/verification. |
| 15 | Legacy packet missing `H`/review/dependency/marker identity | **PASS (spec).** Migration fails closed to `MIGRATION_BLOCKED_REFRESH_REQUIRED`; live PR head is never a fallback. |
| 16 | Historical FAIL/INCONCLUSIVE/NOT_RUN/trust preservation | **PASS (spec).** Candidate and migration manifest explicitly preserve historical result/trust semantics without upgrade. |
| 17 | Concrete repository expected-old publication capability | **BLOCKED.** Repository-specific capability and policy compatibility cannot be proven from this verifier environment; details below. |
| 18 | Main-bound PolicyEpoch activation | **PASS (spec).** Candidate remains inert until a separate activation transition binds exact candidate, verification, capability, activation-parent and effective-main identities. |

The conditional concurrency results above are not promoted to repository capability evidence. They establish that the candidate's safety argument is coherent **if and only if** the concrete exact-old primitive is actually available and policy-compatible.

## 4. Concrete repository capability attack — BLOCKED

### 4.1 Connected GitHub write surface is not the required primitive

The available connected GitHub ref-update action exposes the target branch/ref, a new SHA, and a force boolean. It does **not** expose an `expected_old` object ID or an equivalent compare-and-swap precondition. Therefore it is exactly the class of generic REST ref update that the frozen candidate forbids as a substitute for `GIT_RECEIVE_PACK_EXACT_OLD_REF`.

No REST update was used as capability proof and no `main` mutation was attempted.

### 4.2 Repository permission/policy compatibility is not provable

The connected app's attempt to read `branches/main/protection` returns GitHub `403 Resource not accessible by integration`. The accessible repository rulesets endpoint returns an empty ruleset list, but that does not prove the absence, applicability, or bypass semantics of branch protection that the app is not authorized to inspect.

Therefore `repository_permission_policy_compatibility` remains `UNPROVEN`.

### 4.3 Execution host has no usable native Git transport

Non-mutating host checks found:

```text
git version 2.47.3
git ls-remote https://github.com/vokerg/everfield.git HEAD
  -> fatal: Could not resolve host: github.com
credential helper: none
auth environment among GITHUB_TOKEN/GH_TOKEN/GIT_ASKPASS/SSH_AUTH_SOCK: none
```

Thus this verifier cannot establish an authenticated native Git push/receive-pack path, cannot perform an authorized scratch-ref stale-old rejection probe, and cannot show that repository policy permits the required primitive without bypass.

This is an execution/repository-capability blocker, not evidence that native Git exact-old semantics are false in general.

## 5. Candidate defect review

Within the frozen candidate text and migration manifest, no separate correction-requiring BLOCKER, MAJOR, or MINOR was identified in attacks 1–16 and 18. The specification correctly refuses to infer repository capability from generic Git protocol facts.

Counts for candidate-text defects:

```yaml
unresolved_blocker: 0
unresolved_major: 0
correction_requiring_minor: 0
```

Capability state is separate and remains:

```yaml
publication_capability_state: UNPROVEN
repository_permission_policy_compatibility: UNPROVEN
verification_disposition: PUBLICATION_CAPABILITY_BLOCKED
```

Because the candidate itself requires `publication_capability_state: PROVEN` and repository permission/policy compatibility `PROVEN` for PASS, a PASS would be invalid.

## 6. Required continuation

Stage-B remains inactive. Do **not** create or execute an activation transition from this result.

A later fresh verification/recovery episode may retry the same exact candidate only when an authorized environment can provide all of the following without destructive `main` mutation:

1. authenticated native Git push/receive-pack access to `vokerg/everfield` or authoritative equivalent exact-old capability evidence;
2. permission to create/use an isolated scratch ref;
3. a stale-old rejection experiment proving zero ref mutation when the request carries an obsolete old object ID;
4. authoritative visibility into applicable repository branch-protection/rules/permission behavior, proving the primitive does not bypass required policy;
5. exact revalidation that Issue #181 terminal identities and the current canonical binding remain unchanged/compatible.

If those conditions are met, rerun the full suite rather than upgrading this blocked result by prose.

## 7. Authority boundary

This report is noncanonical verification provenance only. It does not activate `PLAN-STAGE-B-v2`, change the Issue #6 canonical binding, authorize direct publication to `main`, grant integration authority, or grant implementation readiness, production, release, engine-selection, legal/provider, gameplay, or application-domain authority.
