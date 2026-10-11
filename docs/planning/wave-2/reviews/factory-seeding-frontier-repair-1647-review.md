# Independent adversarial review — root list cardinality in factory remediation #1647

**Review issue:** #1650 / `FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-14-REV-01`  
**Genuinely independent reviewer execution:** `frontier-distinct-root-review-1650-gpt6-20261011-1402-cph-01`; first valid HANDOFF `RESUME_INTENT` #6108835905, `RESUME` #6108838887 from predecessor `HANDOFF_READY` #6107813440. This review execution is distinct from #1647 source authoring and from the previous claimant who explicitly yielded without reviewing.  
**Disposition: CHANGES_NEEDED — 1 BLOCKER (FSR-1650-B01), 0 separately counted MAJOR, 0 correction-requiring MINOR.** Review-only evidence; NOT implementation verification or integration authority.

## Exact target / boundaries

- Canonical program path `docs/planning/PLANNING-PROGRAM-v1.md` exact blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`; Issue #1147 binding #5675066392 and activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`. Current base `main@3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`.
- Producer #1647 in-lease owner terminal `STATUS(REVIEW_READY)` #6107749574; **OPEN DRAFT** source PR #1648 exact HEAD `4059ee74e96e064f8a99bd011ef9f33f9867a6ad`; corrected parser Git blob `b4cd006d0dcb0175556e9bdfeb3f058045a5a113`. Producer actor `frontier-root-list-remediate-1647-gpt6-20261011-1142-01` is not the independent reviewer.
- Previous independent negative required review #1644 terminal #6107680270 (FSR-1644-B01) and source #1638 PR #1640 exact HEAD `e6bbaddf1e17b23ad9344983c3159d4f30990bfd`. Source #1647 contains **20** PR changed paths; independently enumerated GitHub PR files and exact source/predecessor trees: 18 inherited paths byte-identical, changed paths only `tools/planning/frontier_maintenance.py` and new `docs/planning/handoffs/issue-1647.md`.
- The actual frozen-source `pull_request` Actions run **38129670887** concluded SUCCESS: `validate-pr` job **114441196275** SUCCESS, mutation-capable `maintain` job **114441196853** SKIPPED, source HEAD exact. That is **producer suite evidence**, not independent approval. Existing frozen draft source PR #1648, review-only drafts and earlier verification-only PRs are **unmerged**.

## FSR-1650-B01 — BLOCKER: scalar values laundered into root operational list authority

**Direct executable mechanism, exact parser blob above:** `tools/planning/frontier_maintenance.py:228-306` now correctly calls `_root_mapping_fields` to prohibit borrowing *nested* `extensions.evidence_refs` and `extensions.artifact_paths`. However, at **lines 275-279**, a direct root value with nonempty scalar text is treated as a **singleton list**:

```python
if raw:
    if raw.startswith(("{", "!", "&", "*", "|", ">")):
        return []
    single = yaml_scalar_identity(raw)
    return [single] if single is not None else []
```

Consequently all these YAML documents can yield `list_scalar(body, "evidence_refs") == ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]`:

```yaml
evidence_refs: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

```yaml
evidence_refs: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
```

Yet **PyYAML 6.0.3 `safe_load` independently returns a `str`, not `list`**, for both. The correct positive list forms are `evidence_refs: [aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa]` and a direct-root indented `- aaaa...` sequence. The previous nested-only FSR-1644-B01 scenario now returns no list, so this is a *new* distinct schema/type-boundary failure, not a duplicate nested-key finding.

**Lease-authority consequence:** At exact source `schema3_ownership_lease_state` lines 398-407 the `PROGRESS(EVIDENCE)` branch obtains `evidence_refs = list_scalar(record.body, "evidence_refs")`, checking only nonempty result and `immutable_ref`. A valid root PROGRESS capsule with unchanged source head, actor/generation identity, one root scalar SHA, time before expiry, and EVIDENCE count below three will therefore renew the canonical lease even though the required list is not present as a YAML list. Example: CLAIM at **00:00Z**, forged root scalar PROGRESS at **05:59Z**, lease query at **06:01Z**. Correct schema-3 list-type behavior: owner expired at 06:00Z. Current code: scalar passes `immutable_ref`; lease anchor moves to 05:59Z and falsely remains unexpired until 11:59Z. `schema3_owner_unexpired_at` consumes this anchor, affecting STALE contention and subsequent owner authority. The exact six-hour boundary and fourth EVIDENCE limit exist, but cannot remediate unauthorized *input type acceptance*.

**PR-provenance consequence:** `tools/planning/frontier_maintenance_v7.py` exact inherited blob `28af0a1eeeddcc318b1faeca76c82dfd1efbed87` consumes `base.list_scalar(..., "artifact_paths")` at lines **941**, **945**, **1173** as authoritative source/reviewer/verifier PR-file sets. A single-path PR can be matched by `artifact_paths: "docs/..."` or `artifact_paths: docs/...` even though those are YAML scalars rather than the mandated sequence, bypassing the scalar-versus-list structural requirement. Multi-path matching still requires multiple values; this does **not** allege an invented integration or actual affected historical PR.

**Independent reproducibility:** Local PyYAML 6.0.3 compared root scalar/quoted scalar, legitimate root flow and multiline list, and nested-only cases. Both root scalar forms evaluated as Python `str`; flow/multiline as `list`; nested-only has no root `evidence_refs`. The exact source lines 275-279 unconditionally wrap the scalar into a one-element list. A bounded independent branch-logic simulation showed the forged 05:59Z anchor flips a 06:01Z lease query from expired to unexpired. The entire frozen 1,612-line source module was **not** run locally because public GitHub clone/network is unavailable in the executor; do not misreport producer CI as independent execution.

### Reproduction to execute on frozen source checkout

```python
import importlib.util
import yaml
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "base", Path("tools/planning/frontier_maintenance.py"))
base = importlib.util.module_from_spec(spec)
import sys
sys.modules[spec.name] = base
spec.loader.exec_module(base)

sha = "a" * 40
for body in (f"evidence_refs: {sha}\n",
             f'evidence_refs: "{sha}"\n'):
    assert isinstance(yaml.safe_load(body)["evidence_refs"], str)
    # Current frozen source BUG: returns [sha], should return [].
    assert base.list_scalar(body, "evidence_refs") == [sha]
assert base.list_scalar(f"evidence_refs: [{sha}]\n",
                        "evidence_refs") == [sha]
assert base.list_scalar(f"extensions:\n  evidence_refs:\n    - {sha}\n",
                        "evidence_refs") == []
```

The proposed **fix** must replace the two bug-demonstration assertions with `== []`; add full comment-level `schema3_ownership_lease_state` / `schema3_owner_unexpired_at` regressions verifying root scalar cannot renew, genuine root list can renew before six hours, fourth EVIDENCE denied, HEAD_ADVANCE remains head-bound, no resurrection after expiry, ORPHAN exactly 600s; add v7 regression for **single-file PR** scalar `artifact_paths` rejection across source/review/verifier identity consumers.

## Evidence beyond the finding / scope limits

- The corrected root-boundary parser rejects previously exploited nested-only `evidence_refs`/`artifact_paths`; valid root indented and simple flow lists remain recognized by source inspection and existing tests. Quoted/complex/duplicated/tagged/aliased/shadow-key cases visibly fail closed in the reviewed parser; this review does not claim an exhaustive independent full-harness run.
- The 20 PR file Git SHAs were compared to both exact source and predecessor Git trees: **18/18 inherited blobs identical**, updated base parser blob exact, new producer handoff blob exact. The source PR remains separate from review-only work.
- True historical **NONCANONICAL** integration #1583 squash SHA `ef75cc78a217695097f5d8f6cfb48ea04beaa7de` has one parent `e51703de82b9df3f5e676663d3a04fdc678bd5c6`; prior #1545 source, #1575 verifier and #1577 distinct required review are separate evidence, not generalized readiness.
- No source files, shared workflow, canonical program, gameplay, producer branch, verifier/review predecessor or `main` have been mutated by this independent review. No source publication or new authority is inferred from CI SUCCESS or PR mergeability.

## Required next route

**One mandatory bounded blocking remediation** of `FSR-1650-B01`: preserve all 18 inherited frozen predecessor blobs, source PR #1648 and reviewer-only PR #1650 untouched, make direct-root `list_scalar` reject non-list YAML scalar values, exercise actual lease and v7 single-path source/review/verifier regressions on final HEAD, obtain real read-only final-source CI, then a **new genuinely independent required adversarial review**. A clean review would still require a separately owned current-main-compatible **squash-only NONCANONICAL** source-integration route; no reviewer may merge source or review-only PRs. No canon, gameplay truth/consent, accessibility, final engine selection, implementation-readiness, production or release authority is granted.

**Final verdict: CHANGES_NEEDED / FSR-1650-B01 (1 BLOCKER).**