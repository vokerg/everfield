# Issue #181 handoff — ARCH-CONVERGENCE-CANON-01

State target: `REVIEW_READY` after exact-head draft PR creation and terminal status publication.

## Frozen inputs

- producer base: `main@082740ff455b2dd81966bdb06a413000d2e704bc`;
- current canonical authority during production: Planning Program v1 / Issue #6, unchanged;
- Revision-3 provenance: Issue #174 candidate blob `4c9543671f2d650ee1c45797d1eee3c1cd3145e0`, already squash-integrated only as noncanonical provenance;
- independent architecture review: Issue #176 exact head `d723b791fee6c4ffcf509f5dd7b21657da57e08d`, disposition `PASS_FOR_CANONICAL_REVISION`, review blob `56a3a07a0265ee8ea2e07cd7786197ce6d3b2813`, already squash-integrated only as noncanonical review provenance.

## Candidate outputs

- `docs/planning/architecture/FRONTIER-CONVERGENCE-POLICY-EPOCH-v2.md` — blob `73a118e524add90740928c1d623416dc3eaaadec`;
- `docs/planning/architecture/FRONTIER-CONVERGENCE-MIGRATION-v2.yaml` — blob `186c71b76f4749b64647f1ef1bb7adb8b4ac0e17`;
- this handoff.

## Producer result

The candidate keeps Stage-B inactive and defines a closed PolicyEpoch/migration/verification boundary. It preserves immutable terminal `H` authority, review/verification/canonicality/readiness separation, negative-review `acceptance_authority: NONE`, historical result/trust preservation, squash-only publication, and fail-closed compatibility/migration semantics.

The only candidate publication primitive is `GIT_RECEIVE_PACK_EXACT_OLD_REF`: a server-enforced update carrying exact checked base `A` and new squash commit `S`. Official Git protocol documentation establishes the native push update command shape `old-id new-id refname`, and GitHub documentation establishes authenticated Git push support. This producer episode deliberately does **not** convert those generic protocol facts into repository-specific capability authority.

Repository capability is frozen as:

```yaml
repository_capability_state: UNPROVEN_PENDING_INDEPENDENT_VERIFICATION
fallback_if_unproven: PUBLICATION_CAPABILITY_BLOCKED
```

Ordinary REST ref updates, PR merge/squash endpoints, force pushes, and read-then-write sequences remain forbidden fallbacks unless a later verified revision proves equivalent exact-old semantics.

Producer self-review: 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR for the bounded schema/migration scope. Producer self-review is provenance only.

## Required next route

Create exactly one fresh independent/degraded-independent Stage-B verification episode after this task terminalizes. The verifier must bind the exact Issue #181 terminal head/work and all three artifact blobs, then attack every required scenario in the migration manifest.

Most importantly, PASS requires a concrete repository capability/permission proof for the chosen exact-old primitive. A verifier that cannot establish the native Git transport/credential and stale-old rejection semantics must return `PUBLICATION_CAPABILITY_BLOCKED`/FAIL rather than infer capability.

A verification PASS may unlock only a separately scoped activation/canonical-binding transition. It does not itself activate Stage-B or grant application readiness, production, release, engine, legal/provider, or gameplay authority.

## Authority boundary

This packet is a non-active canonicalization candidate. Current `AGENTS.md`, `START-HERE.md`, `PLANNING-PROGRAM-v1.md`, and Issue #6 binding are unchanged. No direct-main publication, Stage-B activation, canonical binding change, verification completion, readiness, production, implementation, release, engine, legal/provider, or gameplay authority is granted by this producer episode.