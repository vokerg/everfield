# W2-PG-REM-CI-03 — Independent pre-gate review of executable CI remediation

**Review mission:** `W2-PG-REM-CI-03` / Issue #105  
**Reviewed remediation:** `W2-REM-CI-03` / Issue #102  
**Reviewed terminal status:** comment `5276143625`  
**Reviewed work/head:** `f6e8e7ebd120fb5e1b53f0f6e5925dacbc586942`  
**Validator blob:** `f872f8082592be8e2f067fdf4772034d25483c5e`  
**Report blob:** `d98c2ce50f607808efeba0b5071bd319ba7174c4`  
**Disposition blob:** `72b9cb6ea34218064faba886639c5e236c992567`  
**Handoff blob:** `0c10d248066afb1be70b93e8a9eaa9f797adef69`  
**Prior independent review:** Issue #101 @ `b0a09ebdb03c8bd8390d08d54f7d312eeb08ffa1`, artifact `7cef42ea12aea65c886a25a5d79e7359aed0bee1`  
**Authority:** non-authority pre-gate evidence only; formal aggregate review remains `W2-REV-01`.

## 1. Disposition

`CHANGES_NEEDED`

Findings: **0 BLOCKER / 1 MAJOR / 0 correction-requiring MINOR**.

Issue #102 materially closes both Issue #101 findings at the executable/reconstructability boundary: the exact validator is frozen and self-bound, the 26-case corpus executes, published digests reproduce, expiry/replacement-set attacks are executable, and successor transition admission is bound to exact predecessor bytes plus transition/work/reason/root identities. Those corrections held under fresh attack.

However, the v4 quarantine validator regresses one exact durable identity guarantee inherited from `PG-REM-CI-M01`: it requires replacement evidence identity/provenance fields to exist but does not validate their values or resolve them to exact source evidence. Arbitrary or duplicate replacement evidence IDs, a dangling source-envelope ID, and substituted provenance all still produce `SATISFIED`. The report and self-review explicitly claim exact replacement-evidence identity/provenance binding, so this is a mechanical authority gap rather than a documentation preference.

## 2. Cold-start / independence profile

Trust mode: `DEGRADED_SINGLE_AGENT`.

- distinct review episode/actor session: `w2-pg-rem-ci-03-agent-20260813-0709-01`;
- judged Issue #102 payload remained immutable throughout this review;
- exact Issue #102 work/blob identities were frozen before judgment;
- the exact executable was run and independently mutated before reconciling Issue #102's report/disposition rationale;
- this task writes only Issue #105 review/handoff paths;
- repository-visible single-context constraint remains the degraded-mode basis inherited from canonical Planning Program v1;
- formal `W2-REV-01` remains mandatory and this pre-gate result grants no stronger authority.

During the review, `main` advanced from claim base `c7ba185ed9667b717794c19eaa0834ca41aa4c78` to governance-only commit `042d140b5d2e0b951da4528e1867514983418d6f`, adding the canonical draft-PR visibility directive. Before writing review artifacts, `planning/issue-105` was fast-forwarded to that descendant so the branch carries the current operational rule. The immutable Issue #102 judgment target did not change.

## 3. Fresh executable reproduction that held

The exact validator source was reconstructed from blob `f872f8082592be8e2f067fdf4772034d25483c5e` and executed with Python standard library only.

The self-bound source identity reproduced exactly:

- validator source: `sha256:96a016c998d4b1af30f2a1803c6723cdfbad64d6ad23e9ed2b3e83f5a5e5f346`.

The emitted canonical evidence digests reproduced exactly:

- fixture manifest: `sha256:08d009ef6648366835bd2f2c3866572b73b00510c924460471210c10acb20701`;
- fixture cases: `sha256:cfef6f1dfe721504480b6a7f3d6983edeae3f335a507b547511773f0543a97fe`;
- harness contract: `sha256:1a9a14a261047cefdcded2be739af3659b70329fecfa2e8df12a92e47fceb475`;
- result object: `sha256:7b0a8659b0c505bdca1f4cbc2b62e2e9b03d4031b05a01dc1ecb543cf4bb8438`;
- predecessor evidence artifact: `sha256:46f6e1dfd6b56eb2d62c689e0c20de7021ff51123002655550834abd04d8107d`;
- predecessor evidence root: `sha256:46f6e1dfd6b56eb2d62c689e0c20de7021ff51123002655550834abd04d8107d`.

All 26 scenario aggregates matched the frozen `EXPECTED` map. Two complete executions emitted byte-identical JSON (`sha256:e611904bfa8039d174b961395e62a8dec0a58c1b6afe44a5f5f2b6cae3570134` for the pretty-printed output used in this review).

A fresh non-digest source mutation changed the observed source identity to `sha256:831ab31ee65ed6c326637b05a4dc8ef24d06c09b8215d2f966eb8beb813d1a3b`; execution exited nonzero before fixture evaluation with the validator-source mismatch. This confirms the source-binding mechanism itself is effective.

## 4. Issue #101 MAJOR closures that held

### 4.1 `PG-REM-CI2-M01` executable mapping / regression corpus

The source now contains the actual generic evaluator functions and derives the result object from exact in-memory fixture cases rather than a scenario-ID truth switch. Fresh execution reproduced all published identities. The required expiry and exact replacement-set negatives S18-S21 returned `INCONCLUSIVE`, while the valid active quarantine S6 returned `SATISFIED`.

The built-in applicability/retry attacks also held:

- conditional-required `NOT_RUN` → `UNSATISFIED`;
- PRODUCT FAIL then PASS → `UNSATISFIED`;
- permitted INFRA FAIL then PASS → `SATISFIED`;
- FLAKY then PASS → `UNSATISFIED`.

### 4.2 `PG-REM-CI2-M02` predecessor evidence reconstruction

The predecessor evidence bytes are embedded and emitted, with canonical compact-JSON SHA-256 reconstruction. Fresh mutation confirmed that exact transition identity fields are independently enforced: changing predecessor/successor candidate, changed-work identity, transition ID, reason, predecessor artifact digest/root, root algorithm, or claimed observed root yields `INCONCLUSIVE`.

The exact S22-S26 substitution classes also reproduced as `INCONCLUSIVE`, including the stronger attack where predecessor evidence bytes and producer-facing digest/root are changed consistently. The frozen predecessor artifact remains authoritative rather than a producer-updatable matching pair.

No regression was found in replacement ArtifactIdentity/hash checks, quarantine expiry/set equality, same-candidate second-root rejection, or retained artifact identity/hash reachability semantics within the exact cases those functions actually validate.

## 5. `PG-REM-CI3-M01` — MAJOR — replacement evidence identity/provenance fields are presence-only and can be laundered

### Required inherited contract

Issue #97's `PG-REM-CI-M01` correction requires every replacement evidence object to bind at least exact replacement evidence/attempt identity, candidate, quarantine requirement/policy version, replacement ID, exact `ArtifactIdentity` plus expected content hash, result, and provenance/envelope, and requires those fields to be validated and reconstructable from the aggregate result.

Issue #99's v3 identity contract therefore declared `replacement_evidence_id`, `source_envelope_id`, and `provenance` as exact durable identities, not decorative strings. Issue #102 says it preserves that already-correct replacement-evidence behavior, and its self-review marks `replacement evidence exact identity/ArtifactIdentity/hash binding: PASS`.

### Exact validator gap

`replacement_ok(record)` verifies that the required field names are present, then checks only:

- candidate ID;
- requirement ID;
- policy version;
- result = `PASS`;
- artifact key resolves in the catalog;
- artifact ID and authoritative hash match that catalog entry.

The function never compares `replacement_evidence_id`, `source_envelope_id`, or `provenance` to an authoritative identity/value. `quarantine()` checks exact replacement-set keys and `replacement_id`, but likewise never resolves the source envelope or validates evidence-record identity uniqueness/provenance.

### Fresh mechanical attacks

Starting from exact S6 replacement records and changing only the named identity/provenance dimension produced:

| Attack | Derived aggregate |
|---|---|
| `short_soak.replacement_evidence_id = evil-id` | `SATISFIED` |
| `short_soak.source_envelope_id = env-does-not-exist` | `SATISFIED` |
| `short_soak.provenance = producer-substituted` | `SATISFIED` |
| both replacement records reuse the same `replacement_evidence_id` | `SATISFIED` |

The source-envelope boundary is additionally not reconstructable for the positive records. The embedded predecessor artifact contains exact envelopes `env-flaky-1` and `env-flaky-1-static`, but the positive replacement records both name `env-flaky-1`; the static replacement does not bind the exact static envelope identity, and the short-soak replacement has no durable PASS execution envelope whose bytes are resolved by the validator. Changing the static replacement's source-envelope string to `env-flaky-1-static` also remains `SATISFIED`, demonstrating that the current field has no mechanical meaning either way.

Thus the v4 packet proves exact replacement *membership* and exact replacement *ArtifactIdentity/hash*, but not exact replacement evidence-record identity or execution provenance. A producer can substitute or duplicate the durable evidence identity or point at nonexistent/wrong provenance while preserving quarantine satisfaction.

### Required correction

Route one bounded remediation successor that:

1. validates exact `replacement_evidence_id` and uniqueness rather than presence-only;
2. publishes exact replacement execution evidence envelopes or content-addressed immutable references available in the frozen packet;
3. resolves every `source_envelope_id` and verifies candidate, requirement/policy, replacement/check identity, result, ArtifactIdentity/hash, and provenance against the replacement record;
4. validates the exact retained provenance identity/value;
5. retains the exact record + source evidence/ref in the emitted result;
6. adds executable negatives for substituted/duplicate evidence ID, dangling/wrong source envelope, substituted provenance, and record↔source result/artifact mismatch;
7. preserves all existing S1-S26 behavior and the v4 source/predecessor binding.

Successor route created as Issue #107 / `W2-REM-CI-04`. It is blocked until this review terminalizes and remains unclaimed by this reviewer.

## 6. Authority boundaries

No authority leakage was found. Issue #102 continues to disclaim CI-provider selection, universal INFRA-classification authority, production storage guarantees, gameplay implementation, implementation readiness, integration, verification, or canonicalization. This review grants none of those authorities.

The finding is specifically about whether a synthetic quarantine result can be treated as clean evidence under the durable Wave-1 evidence chain. Until Issue #107 repairs the identity/provenance path and later required review accepts the corrected packet, Issue #102 should not be treated as a clean CI input to `W2-REV-01`.

## 7. Required route

Disposition remains `CHANGES_NEEDED` with **0 BLOCKER / 1 MAJOR / 0 correction-requiring MINOR**.

Keep Issue #102 frozen. Do not edit or re-own `planning/issue-102`. Route exactly one bounded successor, Issue #107, to repair `PG-REM-CI3-M01` on a new branch. Formal `W2-REV-01` remains the only declared aggregate independent review authority.
