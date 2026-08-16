# Issue #421 handoff — provider evidence recorder worktree guard remediation

## Identity

- Mission: `W2-ENG-PROVIDER-RECORDER-REM-01`
- Task class: blocking recovery remediation
- Claim: Issue #421 comment `5307444706`
- Claim/base main: `ff261a900fd475764a08c48336dfb4afb22bdfb0`
- Branch: `planning/issue-421`
- Substantive workflow work: `46e25456483e144b8da9ff5fa74cd8de03f6f523`
- Canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- Canonical binding: Issue #6 comment `5245368879`
- Canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- Owner convergence directive: Issue #84 comment `5277825639`
- Owner parallel-frontier directive: Issue #84 comment `5305563203`

This packet is noncanonical recovery provenance only. It does not itself integrate provider evidence or grant provider, engine-selection, readiness, verification, release, decision, content-fan-in, or canonical authority.

## Recovery evidence

The reviewed credentialed evaluator succeeded on exact trusted `main`:

- evaluator run `31947078310`, attempt 1;
- source/head `ff261a900fd475764a08c48336dfb4afb22bdfb0`;
- artifact `9263590221`, `w2-engine-effective-access-31947078310-1`;
- artifact digest `sha256:114c4199ac6d448d22ab0e4d653e393867fcdeb645d5607905ca6f929d198856`.

Its recorder successor failed:

- recorder run `31947090445`, attempt 1;
- job `95164724147`;
- upstream identity binding, exact source checkout, source/projection identity check, exact artifact download, and validation/projection all succeeded;
- `Verify the checkout has only the bounded generated evidence change` failed;
- bounded evidence-branch/draft-PR publication was skipped.

The same guard failure was observed on prior recorder runs including `31946231740` / job `95162533859` and `31946077520` / job `95162129625`. The historical failed runs remain failed provenance and are not republished or relabeled by this remediation.

## Root cause

The recorder previously ran:

```text
python3 -m py_compile tools/planning/record_provider_effective_access.py
```

inside the checked-out source tree before projection. `py_compile` may materialize `tools/planning/__pycache__/...pyc`, while the later publication guard requires the generated evidence JSON to be the only untracked path. The syntax check could therefore contaminate the checkout that the later fail-closed guard correctly rejects.

The repair does **not** weaken or mask that later guard.

## Exact correction

Only `.github/workflows/engine-eval-evidence-recorder.yml` changes substantively:

1. Syntax validation now reads `tools/planning/record_provider_effective_access.py` and calls Python `compile(..., "exec")` in memory. It does not request bytecode output into the repository checkout.
2. Immediately after the source identity and syntax checks, before artifact download/projection, the workflow asserts:

```text
test -z "$(git status --porcelain --untracked-files=all)"
```

3. The post-projection exact guard remains:

```text
test "$(git status --porcelain --untracked-files=all)" = "?? $EVIDENCE_PATH"
```

so arbitrary tracked or untracked contamination still fails closed.

## Preserved reviewed boundaries

The remediation deliberately leaves unchanged in material semantics:

- trusted-main-only workflow-run predicate;
- exact upstream run id/attempt/name/event/status/conclusion/head branch/head SHA/repository/workflow-id binding;
- exact trusted evaluator workflow path binding;
- source-head ancestry check before publication;
- exact source-head checkout and projection-code SHA binding;
- exact run artifact name/id source and data-only handling;
- recorder permissions (`actions: read`, `contents: write`, `pull-requests: write`) and absence of provider secrets/environment;
- evidence path construction and recorder arguments;
- exact single generated-evidence-path post-projection assertion;
- evidence branch namespace keyed by run id and attempt;
- exact staged-path assertion;
- branch-only push (`HEAD:refs/heads/$EVIDENCE_BRANCH`), never generated-evidence push to `main`;
- draft PR creation against `main`;
- explicit no-authority / later exact-head squash-only integration boundary.

## Verification performed

The terminal packet must be reviewed against the exact branch head, but the producer-side checks are:

- changed workflow remains YAML-shaped with the existing workflow/job/step structure;
- `python3 -m py_compile tools/planning/record_provider_effective_access.py` is removed;
- side-effect-free `compile(path.read_text(...), str(path), "exec")` is present;
- a clean-worktree assertion is present before artifact download and projection;
- the existing exact `?? $EVIDENCE_PATH` post-projection assertion remains unchanged in strength;
- no direct push to `main` is introduced;
- publication remains branch + draft PR;
- task scope is exactly the recorder workflow plus this handoff.

A fresh trusted-main evaluator/recorder execution is intentionally **not** claimed by this branch. Such live recovery evidence can only arise after separately authorized reviewed integration of this remediation.

## Required fresh review

A fresh independent/degraded-independent security/authority review of the exact terminal remediation head is mandatory before integration. It should attack at minimum:

1. exact claim/work/head/PR identity and two-path scope;
2. whether in-memory compilation is actually side-effect-free with respect to the checkout;
3. whether the new pre-projection clean-tree assertion fails closed instead of hiding contamination;
4. whether the later exact single-evidence-path assertion remains intact;
5. whether exact upstream/source/workflow/artifact identity binding is unchanged;
6. whether branch/draft-PR publication still prevents direct generated-evidence publication to `main`;
7. whether no provider/evidence/engine/readiness/verification/canonical authority is inflated.

A clean review may establish only that this bounded recorder remediation is safe for a separately authorized squash-only publication. It does not convert historical failed runs into evidence and does not itself establish provider validation or verification PASS.
