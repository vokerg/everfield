# Issue #738 — serialized attempt-set round-trip remediation

## Frozen source and route
- Mission: `W2-ENG-TECH-UNITY-S3-V5-LINEAGE-ROUNDTRIP-REM-01`.
- Winning ownership generation: Issue #738 comment `5436993525`.
- Base/current-main at claim: `4986dd9c275e44a931e17b855a760f45fa6ae4c0`.
- Canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`.
- Active canonical binding: Issue #6 comment `5245368879`.
- Canonical activation SHA: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`.
- Recovery source: Issue #733 terminal comment `5436935136`, route `BLOCKING_REMEDIATION_OF_SERIALIZED_ATTEMPT_SET_VALIDATOR`.
- Diagnostic evaluator run/job: `33023639005` / `98359776793`.
- Frozen producer preimage blob: `99acf89606ee88d763a1909a1992be102e52bef2`.
- Unchanged recorder blob: `43e2f9da098e46948fd0da03a676859b66ba8789`.

## Diagnostic failure boundary
The fresh exact-main trusted-runner episode reached native S3 PASS and reported candidate work/generation identities, then failed the on-disk sanitized packet validator with `ValueError: attempt set mismatch`. No sanitized artifact was uploaded and no recorder evidence or `PASS_FOR_COMPARISON` authority was created.

The failure was representation-only: the in-memory `attempts` mapping was built in `ATTEMPT_PLAN` order, while production serialization used `json.dumps(..., sort_keys=True)`. Reloaded JSON therefore presented the same exact attempt IDs in sorted object-key order. The validator separately requires ordered equality for `run_registry_refs` and `all_attempt_refs`, so requiring mapping insertion order duplicated and contradicted the serialized representation.

## Bounded remediation
Producer commit `ceb66604211f6f753a7e6268ef52fb264cf6e8a0` changes only `tools/planning/unity_s3_v5_lineage.py`:
- `attempts` now requires exact key membership and cardinality without depending on mapping insertion order;
- ordered `run_registry_refs` and `all_attempt_refs` equality remains unchanged;
- a positive self-test performs the production-equivalent `indent=2, sort_keys=True` JSON serialization/reload, verifies that the mapping order actually changed, and validates the packet successfully;
- negative controls explicitly reject missing, extra, and wrong attempt IDs while retaining the existing reset/workspace/source/resource/run/raw-digest/sensitive-field/path negatives.

No workflow, trigger, permissions, pinned actions, trusted-runner identity, Unity execution semantics, recorder code, historical evidence, authority field, or canonical status changed. No Unity execution was performed from this producer branch.

## Deterministic verification
Local reconstruction of the frozen preimage produced Git blob SHA `99acf89606ee88d763a1909a1992be102e52bef2`, proving the edited source is the exact frozen file plus the bounded diff. The committed producer blob is `e9021d62e5dc0a36eabbb4f51e0663a5847314cb`.

Repository-equivalent checks passed:
- `python3 -m py_compile tools/planning/unity_s3_v5_lineage.py tools/planning/record_unity_s3_v5_lineage.py` — PASS;
- `python3 tools/planning/unity_s3_v5_lineage.py --self-test` — PASS, including production-equivalent round-trip and 12 fail-closed negatives;
- `python3 -m tools.planning.record_unity_s3_v5_lineage --self-test` — PASS with all 5 existing recorder negatives;
- reconstructed recorder Git blob exactly matched `43e2f9da098e46948fd0da03a676859b66ba8789`.

Producer negative cases: `missing_attempt`, `extra_attempt`, `wrong_attempt_id`, `reset_false`, `duplicate_workspace`, `tampered_source`, `wrong_resource`, `wrong_run_head`, `duplicate_registry`, `tampered_raw_digest`, `sensitive_key`, `absolute_path`.

Recorder negative cases: `wrong_run_id`, `wrong_head`, `wrong_workflow`, `tampered_lineage`, `sensitive_field`.

## Required next gate
Fresh independent or degraded-independent security/authority review of the exact immutable remediation head is mandatory. Review must prove the change is limited to representation-order handling, preserves exact attempt membership and ordered registry arrays, leaves evidence/security/runner/authority boundaries unchanged, and keeps all negative controls fail-closed.

Only a clean `PASS_FOR_INTEGRATION` may route a separate explicitly authorized squash-only integration episode. Only after reviewed integration may a fresh exact-current-main evaluator/recorder episode be dispatched. The prior native S3 PASS remains diagnostic-only and is not promoted into durable reviewed evidence or comparison authority.

The owner terminal `STATUS(REVIEW_READY)` binds the exact final branch head containing this handoff and the producer commit; this handoff itself does not grant review, verification, integration, comparison, decision, or canonicalization authority.
