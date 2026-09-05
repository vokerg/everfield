# Issue #862 handoff — Unity S3 v5 recorder publication authentication

## Scope

This remediation is the exact bounded successor required by Review #859 finding `W2-ENG-TECH-UNITY-S3-V5-RECORDER-TRIGGER-REM02-REV-M01` against failed producer Issue #845 / PR #853 at immutable head `53463beff138d5854f4268c5be20cdc11554716a`.

No native Unity run was executed. No evaluator topology, source-run gate semantics, engine/provider evidence, canonical engine decision, verification PASS, or integration authority is changed or implied.

## Defect reproduced

The failed producer kept both `actions/checkout` steps at `persist-credentials: false`, but the hosted recorder's final publication step used a plain `git push origin` without any authenticated transport. `contents: write` permission alone therefore did not make evidence-branch publication reachable.

## Remediation

The recorder continues to keep both checkouts non-persisting. Only the final GitHub-hosted evidence-branch publication step receives `${{ github.token }}`. It derives an ephemeral HTTP Basic authorization header and passes that header to exactly one `git push` through process-scoped `GIT_CONFIG_COUNT` / `GIT_CONFIG_KEY_0` / `GIT_CONFIG_VALUE_0` variables. The header is not embedded in the remote URL or written to local Git config, and the shell variable is unset immediately after the push.

`tools/planning/validate_unity_s3_v5_recorder_trigger.py` now requires this exact bounded mechanism, requires exactly two `persist-credentials: false` checkouts, forbids `persist-credentials: true`, forbids token-bearing remote URLs and persistent local HTTP auth config, and includes negative controls for both credential persistence and the original unauthenticated plain-push topology.

## Deterministic validation

Validated against exact Git blob identities from `planning/issue-862`:

- `.github/workflows/unity-s3-v5-lineage-recorder.yml` — `1d9252a36c0ccd2c8ab0c4517a44afdacb078cc0`
- `.github/workflows/unity-s3-v5-lineage-evaluator.yml` — `9f8f09e95577bbfb5e307a7cc3bc352feae68553` (unchanged)
- `tools/planning/validate_unity_s3_v5_recorder_trigger.py` — `a904e914801146688e607b2cc4b3d393321cb38b`
- `tools/planning/unity_s3_v5_recorder_source_gate.py` — `246ecd8c006948f3191c57fedf34276070ac94ee` (unchanged)

Commands:

```text
python3 -m py_compile tools/planning/validate_unity_s3_v5_recorder_trigger.py tools/planning/unity_s3_v5_recorder_source_gate.py
python3 tools/planning/validate_unity_s3_v5_recorder_trigger.py
```

Result:

```text
unity-s3-v5 recorder trigger temporal/static contract: PASS
```

## Review boundary

Fresh independent or degraded-independent review must judge the immutable remediation head before any integration route may exist. The review must re-check at least:

1. native Unity evaluator remains read-only;
2. both recorder checkouts remain non-persisting;
3. repository token exposure is confined to the GitHub-hosted publication step;
4. the exact evidence-branch push is authenticated without token-bearing remote URL or persisted Git HTTP credentials;
5. the validator rejects the original plain-push topology and credential-persistence mutations;
6. no live Unity/provider evidence or PASS authority is inferred from deterministic validation.
