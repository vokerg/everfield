# Required adversarial review — Issue #1594

## Disposition

**CHANGES_NEEDED — 0 BLOCKER / 2 MAJOR / 0 correction-requiring MINOR.**

Reviewed immutable producer Issue #1591 terminal `6053794956`, draft source PR #1593, exact frozen HEAD `fa0c552bab1577f088dba271aeebe64f5150b1e0`, against current `main@3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d` and active canonical binding #1147 comment `5675066392` / program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`.

The verifier-causality remediation for FSR-1589-B01 is materially present and the real #1545 → #1575 → #1577 → #1583 chain is authenticated through distinct source/verifier/reviewer/integrator issues, exact terminals/PRs/heads, verifier PASS with zero material findings, actor separation, verifier-only evidence paths, and actual source publication identity. However, FSR-1589-M01 is not fully remediated.

## Structural and workflow evidence

PR #1593 remains draft/unmerged and is exactly nine paths at the reviewed HEAD. The inherited workflow/v5/v6 and #1556/#1570/#1579/#1585 handoff blobs match the issue contract exactly; substantive change is v7 plus producer handoff #1591.

Final producer run `37737135621` has read-only `validate-pr` job `113179136786` PASS and mutation-capable `maintain` job `113179138470` SKIPPED. The checkout log binds merge ref `63582c2b828f3c7d52f1ae410d3d92fbfa084e55` as exact source `fa0c552...` merged into `main@3d7ce70...`, then runs Python compile and composed v1-v7 self-tests successfully. Authored green CI is treated as producer evidence, not independent review disposition.

## FSR-1594-M01 — MAJOR — nested sequence/flow provenance aliases bypass fail-closed placement

The corrected `_consistent_extension_alias()` rejects a recognized alias if it appears as a direct scalar outside top-level `extensions:`, at the wrong ordinary indentation under `extensions:`, duplicated, null, or conflicting among direct aliases. But its foreign-placement detector is regex-shaped around a line beginning with whitespace immediately followed by the recognized key:

`^([ \t]*)<recognized_key>:\s*...`

That does **not** detect the same recognized authority-bearing alias when nested under `extensions:` as a YAML sequence-item mapping or flow mapping. For example, with a legitimate direct source alias:

```yaml
extensions:
  original_source_issue: 9001
  compatibility:
    - original_source_issue: 9002
```

the helper ignores the contradictory nested sequence mapping and still returns `9001`. Likewise:

```yaml
extensions:
  original_source_issue: 9001
  compatibility: {original_source_issue: 9002}
```

still returns `9001`. The ordinary nested-map form (`compatibility:\n    original_source_issue: 9002`) is rejected, so the defect is specifically an incomplete structural-placement scan rather than intended permissiveness.

The shared operational parser does not independently reject these forms: it extracts schema-3 authority fields conservatively with regex/scalar helpers and performs no full structural YAML rejection that would make sequence/flow occurrences impossible. Therefore a trusted operational capsule can carry contradictory recognized provenance vocabulary in a foreign nested placement while v7 accepts the direct alias as authoritative.

This violates the #1594 mandatory review contract requiring recognized source/review/verifier provenance aliases to be accepted **only** as direct children of the top-level `extensions:` mapping and to fail closed for aliases nested under extensions or otherwise foreign-placed. The same scanner is reused for source, review, and verifier alias groups, so the gap is not confined to one historical spelling.

### Required remediation

Bounded remediation must make recognized provenance alias placement structural/fail-closed rather than relying on the current line-prefix shape. Any occurrence of a recognized source/review/verifier alias must be rejected unless it is exactly one non-null scalar direct child of the single top-level `extensions:` mapping, with all accepted aliases in a synonym group agreeing.

Add explicit adversarial fixtures for at least:
- sequence-item mappings under `extensions:` containing agreeing, conflicting, and null recognized aliases;
- flow mappings under `extensions:` containing agreeing, conflicting, and null recognized aliases;
- the same cases for source, review, and verifier alias families;
- existing legitimate direct extension-only aliases, including real #1583 vocabulary, remaining accepted.

Then require a new exact final producer HEAD, read-only PR compile/composed v1-v7 self-test PASS, mutation job SKIPPED, current-main compatibility, and a **new distinct mandatory required adversarial review**. This reviewer must not correct frozen PR #1593 in place.

## FSR-1594-M02 — MAJOR — losing duplicate ownership contenders incorrectly invalidate the canonical winner

The candidate's `_valid_owner_terminal()` reconstructs a first winning CLAIM or valid STALE recovery, but then applies this unconditional rejection before accepting the terminal:

```text
if any(
    r.kind in {"CLAIM", "RESUME", "RECOVER"}
    and owner.comment_id < r.comment_id < terminal.comment_id
    ...
):
    return False
```

That treats **every** later ownership-shaped contender as authority-displacing, without asking whether it actually won canonical contention. The active program instead requires prefix-scoped reconstruction that rejects losing duplicate CLAIM/RESUME/RECOVER contenders and retains the existing lowest-valid-GitHub-comment-ID winner rule. Premature or losing records cannot supersede the valid current owner. The shared lease helper likewise ignores non-PROGRESS records rather than converting every later contender into a generation change.

Therefore a valid first owner can publish an otherwise authoritative unexpired terminal, yet v7 rejects it solely because a later duplicate claimant lost contention in between. The same false negative applies wherever `_valid_owner_terminal()` authenticates producer, reviewer, verifier, or integrator authority. This does not create false authority, but it can discard valid reviewed/verified publication provenance and suppress the newest implementation demand source, violating the required ownership regressions and convergence/liveness semantics.

### Required remediation

Reconstruct effective ownership transitions canonically rather than rejecting raw later ownership-shaped records. A later record should displace the evaluated owner only when it is itself the valid winning next generation under the applicable CLAIM/HANDOFF/STALE/ORPHAN rules; losing duplicates must have zero authority effect.

Add deterministic fixtures where:
- a first valid CLAIM remains owner despite a later losing duplicate CLAIM before its terminal;
- a valid recovered generation remains owner despite later losing duplicate ownership-shaped contenders;
- an actually winning later valid generation still invalidates a stale prior-owner terminal;
- source, review, verifier, and integrator authentication inherit the same behavior.

Then rerun the same fresh exact-head CI and distinct-review route required for FSR-1594-M01.

## Other mandatory review dimensions

No additional BLOCKER/MAJOR/correction-requiring MINOR was identified in the reviewed frozen head:
- required verifier enforcement is grounded in the immutable source contract (`required_next_route` containing verification), so omission of verifier fields does not bypass #1545's verifier requirement;
- verifier issue/terminal ownership, source terminal/PR/head binding, PASS/zero-findings disposition, verifier PR/head/evidence scope, and actor independence are checked;
- producer/reviewer/verifier substitution and actor-collision negatives are represented;
- exact source/reviewer ownership and STALE recovery gates, one-parent squash identity, ancestry ordering, consumed-latest-no-backfill, v5 successor behavior, and v6 bounded demand regressions remain exercised;
- pull-request validation is read-only and the mutation-capable job is skipped.

These observations do not downgrade FSR-1594-M01 or FSR-1594-M02 or grant integration authority.

## Authority boundary

This review is review-only and **CHANGES_NEEDED**. It grants no merge, integration, verification, canonical, gameplay, private-truth, consent, persistence, accessibility, implementation-readiness, production, legal, shipping, or release authority. PR #1593 and all predecessors remain frozen/unmerged under this review episode.
