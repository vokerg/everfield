# Independent mandatory adversarial review — factory scalar-list remediation #1656

**Review issue:** #1661 / `FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-15-REV-01`  
**Reviewer:** genuinely separate execution `frontier-independent-scalar-list-review-1661-gpt6-20261011-2019-cph-01`; sole first CLAIM #6112190505 at GitHub-server 2026-10-11T18:21:24Z. Not source actor #1656, negative reviewer #1650, or issue-materialization execution.  
**Verdict: CHANGES_NEEDED — 1 BLOCKER FSR-1661-B01, 1 MAJOR FSR-1661-M01, 0 correction-requiring MINOR.** This is a review, not an independent full-module CI run, source verification, integration or canonicalization.

## Frozen authority and evidence

- Current `main@3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`, canonical #1147 unedited integration/binding #5675066392, exact canonical `docs/planning/PLANNING-PROGRAM-v1.md` blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Source Issue #1656 valid owner `STATUS(REVIEW_READY)` #6109748773; OPEN/DRAFT/UNMERGED PR #1660 exact HEAD `3d5ebe385d4af096e04520fb3977d3e900bac87b`, main-based, 21 GitHub PR changed paths. Corrected base parser `tools/planning/frontier_maintenance.py` Git blob `2a8bbc64d200ffa2ac4711ea0dbdf8a7c070ed33`; source handoff `docs/planning/handoffs/issue-1656.md` blob `072026d7d4d820552da16afe4b1593dd51aa473d`.
- Source #1647 DRAFT PR #1648 HEAD `4059ee74e96e064f8a99bd011ef9f33f9867a6ad`: independently fetched both PR file lists, 20 predecessor paths, all **19/19 shared blobs identical** except the base parser, and exactly one new #1656 handoff. All unchanged v5/v6/v7, inherited handoffs and maintenance workflow preserve their exact source Git blob identities. Previous truly independent negative review #1650 terminal #6108889365 / reviewer-only DRAFT #1652 HEAD `021fafc34c3fe632bd05072a9dccd4a4f4281fc0`.
- Exact source pull_request Actions run #38144885280, attempt 1, head `3d5ebe...`, completed `success`; `validate-pr` job #114486051232 `success`, mutation-capable `maintain` #114486051711 `skipped`. Producer CI passes the composed self-tests; it cannot certify this distinct adversarial boundary.

## Confirmed fixed regression — FSR-1650-B01

At corrected parser `list_scalar` (`frontier_maintenance.py:230–309`), a nonempty *root plain or quoted YAML scalar* now takes the `if raw: return []` branch. Thus `evidence_refs: <SHA40>`, `evidence_refs: "<SHA40>"`, `artifact_paths: game/foo.gd` and its quoted variant do **not** become singleton lists. Genuine root `evidence_refs: [SHA40]` and properly indented `evidence_refs:\n  - SHA40` remain accepted; nested-only `extensions.evidence_refs`, duplicate root keys, unsupported tags/aliases, block scalars, second examples and leading prose are rejected by the relevant lexical guards. This directly addresses the originally reported **scalar-vs-sequence** defect, subject to the distinct failures below.

## FSR-1661-B01 — BLOCKER: malformed YAML flow sequence grants operational list authority

`_root_mapping_fields` at `frontier_maintenance.py:169–194` **unconditionally skips indented non-root lines**, without checking whether they are legal children of the preceding root value. `list_scalar` at lines 253–281 immediately parses a direct-root inline `[item]` from that root value and returns the items without validating the remaining indented lines. `parse_operational` at lines 476–506 uses the same unchecked root extraction; the lease evaluator at lines 377–411 trusts `list_scalar` for `PROGRESS(EVIDENCE)`.

Adversarial complete root schema-3 capsule (40-character `a` and `b` SHA literals; the appended indented map is **not** a valid YAML child of a completed flow sequence):

```yaml
protocol: planning-v1
schema: 3
kind: PROGRESS
issue: 77
mission_id: M-77
branch: planning/issue-77
actor_session_id: actor-77
state: IN_PROGRESS
ownership_generation_comment_id: 1
observed_head_sha: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
progress_basis: EVIDENCE
evidence_refs: [bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb]
  injected: yes
```

Independent executed **PyYAML 6.0.3** `yaml.safe_load` on this exact content raises `ParserError: expected <block end>, but found '<block mapping start>'`, locating the erroneous extra map at line 13. Yet actual frozen source control flow is deterministic: `_root_mapping_fields` drops `  injected: yes`; `list_scalar(body, "evidence_refs")` takes `raw.startswith("[")`, returns the authentic-looking 40-character `b` reference; `schema3_ownership_lease_state` sees unchanged `observed_head_sha`, valid ref, positive evidence count and timestamps and **renews an owner generation from a document that is not YAML at all**. A CLAIM at 00:00Z followed by this malformed EVIDENCE at 05:59Z is incorrectly kept live at 06:01Z rather than expiring at 06:00Z. The same malformed `artifact_paths: [game/foo.gd]\n  injected: yes` can pass base list identity extraction for a single-file PR in inherited v7 source/reviewer/verifier consumers at lines **941 / 945 / 1173**, provided the other separate provenance predicates are satisfied. This does *not* assert a real historical PR was forged.

A minimal regression to run on the exact frozen module (or corrected successor) is:

```python
import importlib.util, sys, yaml
spec = importlib.util.spec_from_file_location("base", "tools/planning/frontier_maintenance.py")
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
sha = "b" * 40
broken = f"evidence_refs: [{sha}]\n  injected: yes\n"
try:
    yaml.safe_load(broken)
except yaml.YAMLError:
    pass
else:
    raise AssertionError("expected invalid YAML")
# Frozen source still returns [sha]; corrected successor MUST return [].
assert base.list_scalar(broken, "evidence_refs") == [sha]
```

The source's own `--self-test` includes scalar-vs-list negatives but **not** this malformed flow-list-with-extra-child witness. Since canonical schema-3 requires structurally valid YAML, accepting malformed source/review/verifier authority is a BLOCKER even though the outer bracketed token itself is a sequence literal. Fix must reject the whole syntactically invalid capsule before granting any operational field authority, not merely skip the child.

## FSR-1661-M01 — MAJOR: claimed HEAD_ADVANCE need not match real branch history

`schema3_ownership_lease_state` at lines 389–397 handles `progress_basis: HEAD_ADVANCE` by testing only `progress_head != observed_head` and replacing the internal SHA. There is no authenticated GitHub task-branch read or immutable branch-history proof in this code path. The existing self-test at lines 1294–1322 and 1409–1425 calls `observed_head_sha: b*40` a real advance solely because it differs from prior `a*40`: it never supplies an actual branch ref/commit proof. An owner can therefore publish a well-formed unedited HEAD_ADVANCE PROGRESS before expiry with a syntactically valid but fabricated different SHA on a branch whose GitHub HEAD is unchanged. The helper renews the six-hour owner lease, and `schema3_owner_unexpired_at` consumes it when evaluating a later STALE route. This is a separate **branch-identity/renewal-proof** gap, not merely the scalar list problem. The canonical requirement is that HEAD_ADVANCE actually observe a new head, not just a different literal.

Independent check: source-level exact control-flow and existing self-test inspection; no false claim that the reviewer executed the full frozen module or retrieved historical branch-ref snapshots. Remediate by obtaining authenticated current branch/ref + commit progression evidence at the authority decision point, or fail closed for a PROGRESS that cannot be proved to correspond to a real head advancement; test unchanged real branch ref with different invented SHA and genuine ref movement separately.

## Adversarial coverage, limits, and required next route

The corrected source clearly rejects the original plain/quoted root scalar and nested-only authority. Compared root list, indented sequence, alias/tag/mapping shadow, duplicate, block scalar and ordinary direct list behavior against the visible exact source and its producer self-tests; verified independently in local PyYAML that the new malformed document is invalid. Existing E1/E2/E3 (maximum three consecutive EVIDENCE), E4 rejection, expired EVIDENCE rejection, unchanged *literal* HEAD_ADVANCE rejection, and 599/600s ORPHAN boundaries are covered in producer `self_test`; no new live execution of the full frozen 1,612-line Python module, Godot, or workflow was performed from this restricted review executor. These cases are **not** independently runtime-certified. The full-module and v7 single-path source/review/verifier negative exercises must be added to the corrected successor's actual read-only exact-head CI.

**Required next route:** materialize **one** bounded mandatory blocking remediation of FSR-1661-B01 and FSR-1661-M01, inheriting all 19 unchanged predecessor blobs and freezing source PR #1660, reviewer PR and older PRs; add real negative malformed-YAML/branch-ref tests in the base and all three v7 provenance consumers, preserve existing scalar cardinality fix, run exact final-head composed CI, then a **new genuinely distinct required review**. No optional reviews, global gameplay gate, or speculative feature issue. Even a subsequent clean review requires separately eligible owner-authorized, compatible **squash-only NONCANONICAL** publication; neither this reviewer-only draft nor source #1660 may be merged from this review. No canonical, gameplay/truth/consent, accessibility, engine, implementation-readiness, production or release authority.
