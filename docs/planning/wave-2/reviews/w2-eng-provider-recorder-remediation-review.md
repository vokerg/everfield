# W2-ENG-PROVIDER-RECORDER-REM-REV-01 — required security/authority review

## Disposition

`PASS_BOUNDED_PROVIDER_RECORDER_REMEDIATION`

Finding counts: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR**.

This disposition is bounded to the exact Issue #421 remediation packet. It means only that the recorder worktree-guard correction is safe for a separately authorized squash-only publication episode. It does **not** validate a provider, integrate generated evidence, convert historical failed recorder runs into success, establish implementation/readiness or verification PASS, select an engine, authorize release, execute content fan-in, make a project decision, or create canonical authority.

## Review identity and trust

- Review issue: #425 / `W2-ENG-PROVIDER-RECORDER-REM-REV-01`.
- Original claim: `5307481947`; stale recovery intent: `5308440406`; recovered ownership generation: `5308441565`.
- Review branch: `planning/issue-425`.
- Recovered review branch was fast-forwarded without force from `ff261a900fd475764a08c48336dfb4afb22bdfb0` to fresh current `main@3de6f8f276cd1479ceccdea7362420f1e0efa030` before review artifact authorship.
- Trust mode: `DEGRADED_SINGLE_AGENT`; producer/remediation candidate remained immutable during this review.
- Canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`.
- Canonical binding: Issue #6 comment `5245368879`; activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e` remains an ancestor of current main.
- Owner convergence directive: Issue #84 comment `5277825639`; owner parallel-frontier directive: `5305563203`.

## Frozen judged input

Issue #421 / `W2-ENG-PROVIDER-RECORDER-REM-01`:

- claim `5307444706`;
- terminal producer status `5307463195`;
- substantive work `46e25456483e144b8da9ff5fa74cd8de03f6f523`;
- exact terminal head `3878500aecb740bdb4169357a3ab3775eb298237`;
- draft PR #423, still open/draft, exact head above;
- original base `ff261a900fd475764a08c48336dfb4afb22bdfb0`;
- exact changed paths:
  - `.github/workflows/engine-eval-evidence-recorder.yml`;
  - `docs/planning/handoffs/issue-421.md`.

Fresh drift check found current `main` still carries the original recorder-workflow blob `6b58c7669d17917744eed45c2fe4446c459f6e87`, identical to the judged base version. Later unrelated main integrations therefore have not changed the workflow semantics being reviewed.

## Recovery evidence retained by the judged packet

- successful evaluator run `31947078310`, attempt 1, source/head `ff261a900fd475764a08c48336dfb4afb22bdfb0`;
- artifact `9263590221`, `w2-engine-effective-access-31947078310-1`, digest `sha256:114c4199ac6d448d22ab0e4d653e393867fcdeb645d5607905ca6f929d198856`;
- failed recorder run `31947090445`, job `95164724147`, where exact source/run binding, checkout, artifact download and projection succeeded before the worktree guard failed;
- earlier recorder runs `31946231740` and `31946077520` showed the same guard-failure class.

These remain historical provenance. This review does not relabel or republish them.

## Fresh adversarial review

### 1. Exact identity and scope — PASS

PR #423 remains open, draft, unmerged and frozen at head `3878500aecb740bdb4169357a3ab3775eb298237`. The exact base-to-head diff changes two paths only. The workflow portion is exactly **7 additions / 1 deletion** in one pre-projection block; all other workflow text is unchanged.

### 2. Root-cause correction is side-effect-free — PASS

The removed operation is:

```text
python3 -m py_compile tools/planning/record_provider_effective_access.py
```

The replacement reads the source and executes Python `compile(source, filename, "exec")` in memory.

Fresh reviewer mechanical evidence under Python 3.13.5:

- clean Git worktree before in-memory `compile()`: empty porcelain status;
- clean Git worktree after in-memory `compile()`: empty porcelain status;
- no `__pycache__` directory was created;
- the old `python -m py_compile` behavior created `?? __pycache__/x.cpython-313.pyc` in the same controlled setup.

The replacement therefore removes the recorder's own bytecode side effect rather than hiding it.

### 3. New pre-projection clean-tree assertion — PASS

The remediation adds:

```text
test -z "$(git status --porcelain --untracked-files=all)"
```

immediately after exact source-head/script identity and syntax validation, before artifact download/projection.

Fresh mechanical negatives showed the underlying porcelain command reports both tracked contamination (`M x.py`) and untracked contamination (`?? junk.tmp`). The zero-length assertion therefore fails closed on either class; it does not ignore or whitelist arbitrary worktree state.

### 4. Post-projection exact single-path guard — PASS

The existing later assertion remains outside the modified hunk and unchanged:

```text
test "$(git status --porcelain --untracked-files=all)" = "?? $EVIDENCE_PATH"
```

The remediation does not relax this to a substring, glob, ignore rule, or multi-path allowance. After projection, exactly the generated evidence path must still be the sole worktree change.

### 5. Trusted upstream/source identity binding — PASS

Because the workflow diff modifies only the syntax/clean-tree block, the following reviewed checks remain byte-identical in the judged workflow:

- repository identity `vokerg/everfield`;
- exact upstream run id and attempt;
- workflow name, event `push`, completed/success conclusion;
- head branch `main`, exact head SHA, source repository;
- exact upstream workflow id and fetched workflow path `.github/workflows/engine-eval-credentialed.yml`;
- source-head ancestry to publication-base main;
- checkout of exact source head;
- exact `git rev-parse HEAD == SOURCE_HEAD_SHA` check;
- projection code records the same source/projection SHA.

No moving-main execution or display-name-only trust regression is introduced.

### 6. Artifact/data boundary — PASS

The exact artifact download step is outside the modified hunk and unchanged: run-specific artifact name, exact upstream run id and GitHub token are retained. Projection still consumes the JSON as data through `record_provider_effective_access.py`; the remediation introduces no execution of artifact-controlled code.

### 7. Permissions and provider-secret isolation — PASS

Workflow permissions remain `actions: read`, `contents: write`, `pull-requests: write`. The recorder still has no provider secret/environment material. The remediation adds only local Python source reading and Git status inspection.

### 8. Bounded publication / no direct-main push — PASS

Publication logic is unchanged:

- deterministic evidence branch `evidence/provider-effective-access/run-${RUN_ID}-attempt-${RUN_ATTEMPT}`;
- exact staged-path assertion;
- `git push origin "HEAD:refs/heads/$EVIDENCE_BRANCH"` only;
- draft PR opened against `main`;
- no generated-evidence `HEAD:main` push;
- PR body continues to state later integration requires separate authority, fresh expected-head checks and squash-only publication.

### 9. Historical failure provenance — PASS

No historical run data or durable evidence path is changed by PR #423. The handoff explicitly preserves prior recorder failures as failed provenance and requires a fresh post-integration trusted-main execution for any new evidence handoff.

### 10. Authority inflation — PASS

Neither the workflow patch nor handoff claims provider validation/PASS, evidence integration, engine selection, implementation/readiness, verification PASS, release, content fan-in, decision or canonical authority. The review likewise grants none.

## Findings

No correction-requiring findings remain in the bounded review scope.

- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0

## Residual limits / next lawful step

The exact #421 remediation may proceed only through a **separate freshly derived integration-authority episode**. Before publication, that episode must re-check current main, exact PR/head compatibility, ownership, higher-priority work, and squash-only authority. After any valid integration, only a **fresh trusted-main evaluator/recorder execution** can demonstrate that evidence publication now passes end-to-end. Historical failures cannot satisfy that proof.

`PASS_BOUNDED_PROVIDER_RECORDER_REMEDIATION` is therefore a security/process review result only and remains `NOT_CANONICAL`.
