# W2-ENG-TECH-S6-REM-02 — formal v5 generation binding remediation

## Scope and frozen provenance

Issue #591 is the exact bounded blocking-remediation successor routed by terminal required review #588 / PR #589 for finding `W2-ENG-TECH-S6-REM-REV-M01`. It preserves remediation Issue #585 / PR #587 at terminal head `917866be1655223ebfc3166a7e1949db738f1ff7` and required review #588 / PR #589 at review head `ec08f8f9a693b1bd67e6715bb28b1582afb37b8b` as immutable provenance.

The already-correct S6 byte-bearing normal captures and real capture-down semantics are not reopened. N1 remains SHA-256 `ec2083126dba2bdb96929bfd4306485ad52116d4dc1c7be8b00fb90d0955056b`; N2 remains SHA-256 `54119fd58b7f625b3b739113bd20fa50c503aed486b84f51885b97a61dfd1b7b`. Both remain 1280×720 candidate-rendered PNG frames with distinct marker bytes. FI1 still executes real `/usr/bin/scrot -z /proc/everfield-s6-capture-down.png` while the candidate is alive and the target state is reachable, and retains exact classification `STATE_REACHABLE_CAPTURE_PIPELINE_UNAVAILABLE`.

## Fresh execution identity

- trigger SHA: `020b4b9e05d26ff551c229d0b274751cd7995ff0`
- Actions run: `32043481976`, attempt 1, success
- generated evidence commit: `4d54ba0ba00c09890e03d1fe10d2c08d1657069f`
- artifact: `9292381852`
- artifact digest: `sha256:d7b2785e47b2bf8c86356d33439a22bbc4befe90d5ea8b6130fff3830cedecb4`
- remediation JSON SHA-256: `383e6ebb1031260564d605fa7d746e83ebe86cc66982ae7de8741175c73952cb`
- independent verifier JSON SHA-256: `78b533d8cb9d990ffaadedf596591fb83ad3f88f2a2a7b3db7de72f05f61bee9`
- generation: `GEN-S6-REM2-2a8d597ef60acfb220e2`

## Formal-to-actual binding correction

Each N1/N2/FI1 attempt now creates an actually absent per-attempt workspace under a fresh temporary run root, records the absent-before and empty-after-create reset facts plus filesystem device/inode, and hashes that observed reset body into its formal `reset_id`. After the Godot process launches with that workspace as `cwd`, the producer observes `/proc/<pid>/cwd`, records the same filesystem identity and exact project-file SHA-256 manifest, and hashes that body into the formal `workspace_id`.

The actual capture binding carries the derived reset/workspace identities. Canonical v5 `gen()` receives the N1/N2 reset IDs, verified flags, and workspace IDs from those executed records; the FI AttemptRecord is likewise rebound to the actual FI reset/workspace evidence. The complete formal v5 generation is retained, including adaptation, adaptation binding, generation/candidate/work identity, all AttemptRecords, `run_registry_refs`, `all_attempt_refs`, reset/workspace fields, resource class, and required injection coverage.

A retained `formal_attempt_bindings` map hashes each formal AttemptRecord and binds it to the exact actual attempt binding plus reset/workspace evidence digests. The independent verifier re-hashes those links and requires formal candidate/generation/result/failure/reset/workspace fields to agree with the actual executed records.

## Independent canonical recomputation and negative controls

The retained independent verifier reports `ok=true`, reasons empty, recomputed adaptation `ACCEPT`, and independently calls canonical v5 `agg()` on the retained generation to obtain exactly `PASS_FOR_COMPARISON`, reasons empty, `valid_envelope=true`. Producer and verifier aggregates are equal.

All routed fail-closed attacks pass: reused normal reset identity, unverified normal reset, reused normal workspace, duplicate and mismatched `run_registry_refs`, duplicate and mismatched `all_attempt_refs`, AttemptRecord candidate tampering, AttemptRecord generation tampering, and formal-to-actual binding substitution. Existing actual-byte N1→N2 substitution, missing-frame, tampered-frame, and capture-down classification controls also remain green.

## Preservation and disposition

Bevy and Defold remain `INCONCLUSIVE_HARNESS_OR_INFRA`. Unity and Unreal Engine remain `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY`. Historical Issue #82 50 `NOT_RUN` cells remain unchanged.

Producer disposition is `PROVISIONAL_S6_FORMAL_V5_REMEDIATED_PASS_FOR_COMPARISON_PENDING_REQUIRED_REVIEW`. This packet is `NOT_CANONICAL` and not trusted comparison authority until exactly one fresh required independent/degraded-independent review judges the exact terminal remediation packet.

Draft PR #594 is the review surface. This task grants no integration authority, engine ranking/selection, gameplay/high-throughput implementation, implementation/readiness, provider/commercial/legal/platform/release authority, verification-PASS, decision, or canonical authority. Any later integration requires separate repository authority and, if authorized, squash-only integration into `main`.
