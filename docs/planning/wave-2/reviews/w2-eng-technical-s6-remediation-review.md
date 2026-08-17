# W2-ENG-TECH-S6-REM-REV-01 — required review of S6 remediation

## Review identity

- issue: #588
- mission: `W2-ENG-TECH-S6-REM-REV-01`
- trust mode: `DEGRADED_SINGLE_AGENT`
- judged issue: #585 / `W2-ENG-TECH-S6-REM-01`
- judged terminal status: `5316012502`
- judged head: `917866be1655223ebfc3166a7e1949db738f1ff7`
- judged draft PR: #587, open/draft at that exact head
- final judged run: `32029396638`, attempt 1, success, trigger `3835b5ebae6340aa4137c0c0453b39a7e31bf059`
- artifact: `9288296812`
- artifact digest independently recomputed from downloaded ZIP: `sha256:7868a7d499a070bd65b56478384a8eb739d0ccc9a61f5ec9c7a73dd4c650ec1e`
- canonicality: `NOT_CANONICAL`

This review did not mutate, rerun, repair, integrate, or otherwise advance the judged branch.

## Disposition

`CHANGES_NEEDED`

Findings: **0 BLOCKER / 1 MAJOR / 0 correction-requiring MINOR**.

The prior review findings `W2-ENG-TECH-S6-REV-M01` and `W2-ENG-TECH-S6-REV-M02` are materially closed by the remediation. A new MAJOR finding is introduced below because the remediation replaced enough of the S6 harness that unchanged-v5 aggregation is no longer independently reconstructible from the retained packet.

## Independently confirmed remediation facts

The immutable artifact was downloaded and inspected as bytes, not accepted from prose. Its ZIP SHA-256 exactly matches the GitHub artifact digest. It contains both retained normal frames and the final machine evidence.

N1 independently recomputes to SHA-256 `ec2083126dba2bdb96929bfd4306485ad52116d4dc1c7be8b00fb90d0955056b`, Git blob identity `d3630234dc52e14a8d96cd3085ef1e23c4634bc2`, 4380 bytes, PNG, 1280×720. Pixel sampling independently confirms the three rendered screen regions and marker RGB `[255,255,0]` at `(200,200)`.

N2 independently recomputes to SHA-256 `54119fd58b7f625b3b739113bd20fa50c503aed486b84f51885b97a61dfd1b7b`, Git blob identity `4782c5b407c4cdb426dcb5f7d8f9ae427a7e8bdd`, 4380 bytes, PNG, 1280×720. Pixel sampling confirms the same three screen regions and marker RGB `[255,0,255]`. The N1/N2 byte objects are not identical.

The exact Godot source on the judged head selects the marker from `E_ATTEMPT`, writes the attempt/marker into the candidate-produced ready-state record, and draws the marker in `_draw()`. The normal capture path then runs real `/usr/bin/scrot` against the X11 framebuffer. Thus the marker is candidate-rendered, not a host-side image fabrication.

The artifact's N1/N2 capture bindings independently recompute to their retained binding digests and bind candidate, generation, attempt, run identity, exact state, project SHA-256, executable SHA-256, classification, capture mechanism and frame SHA-256/metadata. Substituting the actual N1 bytes for N2 fails the N2 SHA-256 and marker predicate. Missing and byte-tampered frame objects are rejected by the verifier's byte-reading path.

FI1 records exact state `CAPTURE-STATE-042|Godot|GEN-S6-REM-47e2192acf40054ae5a3|FI1|00FFFF|1280x720`, `state_ok=true`, and `candidate_alive_at_capture=true`. The real command `/usr/bin/scrot -z /proc/everfield-s6-capture-down.png` executed and returned exit 1 with zero retained frames, no output path, and stderr `Saving to file ... failed`. The retained classification is exactly `STATE_REACHABLE_CAPTURE_PIPELINE_UNAVAILABLE`, and the verifier rejects evidence whose FI classification is not that exact value. This closes the previous hard-coded-failure defect.

The independently recomputed artifact hashes also match: remediation JSON `9f115927f95102c37c60ff7125de843b7cdde1b680276a111ece854c274339e4`; verifier JSON `10abd799a04c198de845ba2e47eac06e1473cce4bb8705e6eae255d83f50b02c`.

## MAJOR — W2-ENG-TECH-S6-REM-REV-M01: retained packet cannot independently recompute unchanged-v5 aggregate

The canonical v5 `agg()` contract does substantially more than compare an aggregate label. It validates generation identity, candidate/adaptation binding, one-to-one `run_registry_refs` / `all_attempt_refs`, closed AttemptRecord schemas, normal-index uniqueness, at least two normal attempts, `reset_verified=true`, distinct reset identities, distinct workspace identities, common resource class, exact required injection coverage, failure-class authority and result semantics before returning `PASS_FOR_COMPARISON`.

The judged remediation constructs such a generation only transiently in the producer:
- `v.gen(...)` is called with normal resets `('R1','R2')`, normal workspaces `('W1','W2')`, and `oks=(True,True)`;
- the FI AttemptRecord is then assigned `R3` / `W3` and `reset_verified=True` in memory;
- `v.agg(g)` returns the reported aggregate.

However, the retained `remediation.json` does **not** retain `g`, its AttemptRecords, its registries, or mechanically derived reset/workspace proof. Its `attempts` are a separate raw S6 evidence schema without `reset_id`, `reset_verified`, `workspace_id`, `resource_class`, formal registry refs, or the full formal adaptation/generation envelope. Only `unchanged_v5.adaptation` and the already-computed `unchanged_v5.aggregate` are retained.

The so-called independent verifier therefore cannot recompute `agg()` from retained formal evidence. It recomputes `va(v.adaptation('S6','Godot'),'Godot')`, but then performs `agg=d['unchanged_v5']['aggregate']` and merely compares that stored dictionary to the expected PASS dictionary. Its output field `recomputed_v5_aggregate` is consequently a copy of producer output, not an independent aggregation.

This is material because `PASS_FOR_COMPARISON` is precisely the v5 envelope that depends on the discarded reset/workspace/registry/AttemptRecord invariants. The packet cannot demonstrate that the producer's asserted `R1/R2`, `W1/W2`, and `reset_verified=True` correspond fail-closed to the actual fresh attempt workspaces. A reviewer cannot independently reconstruct or attack the formal aggregate from immutable evidence.

### Required correction

Route exactly one bounded S6 remediation successor. Preserve the now-clean byte-bearing capture and real FI evidence. Add only the minimum formal-evidence binding needed to:
1. derive formal normal/FI AttemptRecords from the actual executed attempt records and their actual fresh workspace/reset identities rather than hard-coded labels;
2. retain the exact v5 generation object, adaptation, registries and AttemptRecords in the immutable artifact;
3. bind those formal records to the same candidate/generation/run/project/executable/capture evidence;
4. make the independent verifier load the retained generation and call canonical v5 `agg()` itself;
5. add negative controls proving reused/unverified reset/workspace or registry/AttemptRecord tampering changes the independently recomputed disposition fail-closed;
6. rerun fresh evidence and route exactly one fresh required review.

Do not reopen or regress the already-corrected retained PNG/substitution behavior or real capture-down execution.

## Preservation and authority

Bevy and Defold remain `INCONCLUSIVE_HARNESS_OR_INFRA`. Unity and Unreal Engine remain `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY`. Historical Issue #82 50 `NOT_RUN` cells and all failed/superseded run provenance remain unchanged.

Because of the MAJOR finding, exact generation `GEN-S6-REM-47e2192acf40054ae5a3` is **not** trusted bounded S6 comparison authority. This review grants no integration authority, engine ranking/selection, gameplay/high-throughput implementation, implementation/readiness, provider/commercial/legal/platform/release, verification-PASS, decision, or canonical authority.