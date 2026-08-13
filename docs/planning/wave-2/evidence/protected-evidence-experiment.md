# W2-PROTECT-01 — Protected evidence storage, disclosure, and availability experiment

**Mission:** `W2-PROTECT-01`  
**Task class:** `PLANNING_EXPERIMENT / EVIDENCE_REQUIRED`  
**Branch base:** `main@d82720d6e692e2a8e196fdc3942676549b77c3e7`  
**Result:** `BOUNDED_PASS_WITH_OPEN_PRODUCTION_QUESTIONS`  
**Required downstream review:** `W2-REV-01`  
**Production dependency authority:** `NONE`

## 1. Scope and non-goals

This experiment tests the minimum protected-evidence semantics required by the canonical Wave 1 foundations: a durable public result envelope bound to exact candidate/base/evaluator/oracle identities; a single `ArtifactIdentity` for protected retained evidence; bounded diagnostics that do not disclose holdout content; explicit unavailable/corrupt handling; access/change/reveal audit; holdout compromise/rotation; and producer/verifier permission separation.

It does **not** select a storage provider, encryption scheme, key-management system, secret manager, CI vendor, evaluator implementation, or production authorization model. The fixture is a logical reference model, not a security proof. No result here upgrades implementation readiness or establishes that a future deployment is resistant to a privileged host, side channel, compromised operator, or malicious runtime.

## 2. Authoritative constraints carried from Wave 1

The experiment preserves these canonical planning rules:

- `ArtifactIdentity` is the sole durable identity for retained evidence; content hash proves identity, not availability.
- Protected evidence publishes a durable result envelope with exact candidate/base/environment/evaluator/oracle identity, coverage category, result, bounded diagnostics, protected artifact reference, trust profile, calibration fingerprint, and reveal/change audit references.
- Unavailable, corrupt, or unverifiable protected evidence is `INCONCLUSIVE`.
- Protected oracle/config changes are judge-affecting `PolicyEpoch` changes.
- Disclosure/compromise is auditable and requires affected holdout rotation/retirement.
- A producer may not self-weaken the sole acceptance gate or fabricate `EvidenceSatisfaction`.

## 3. Evidence question and fixture contract

```yaml
PlanningExperiment:
  experiment_id: w2-protect-01-logical-fixture-v1
  task_mission_id: W2-PROTECT-01
  evidence_question_refs:
    - PROTECT-Q1-public-envelope-without-holdout-leak
    - PROTECT-Q2-availability-and-integrity-fail-closed
    - PROTECT-Q3-permission-separation
    - PROTECT-Q4-auditable-disclosure-and-rotation
  decision_refs_blocked_or_informed:
    - IR-BLOCKER-EVIDENCE-FOUNDATION
    - protected-evidence-provider-selection
  allowed_ownership_surface: docs/planning/wave-2/evidence/protected-evidence-experiment.md
  disposable: true
  production_dependency_allowed: false
  production_content_authority: NONE
  engine_lock_in_authority: NONE
  required_review: W2-REV-01
  retention_policy: retain report and deterministic fixture vectors as planning evidence
  cleanup_or_quarantine_rule: no secret/holdout payload is committed; fixture tokens are synthetic labels only
  completion_predicate: all declared logical cases produce expected outcomes and caveats remain explicit
```

The reference fixture uses Python standard-library semantics (`hashlib.sha256`, deterministic JSON serialization) only to check the logical transitions below. The protected payload is represented as bytes; the public envelope stores only its content hash / artifact identity and bounded result metadata.

## 4. Public result envelope

Synthetic retained protected payload:

```text
{"scenario":"protected-eval","score":0.875,"failures":["edge-7"]}
```

SHA-256 / `ArtifactIdentity`:

```text
sha256:d3f58c513e2e2c34903036acf596fdb04269373170bb2ecf1a9a949efde7917c
```

Expected public envelope shape:

```yaml
candidate_work_sha: candidate-work-sha-demo
base_sha: d82720d6e692e2a8e196fdc3942676549b77c3e7
environment: fixture-python-stdlib
evaluator_fingerprint: eval-fixture-v1
oracle_identity: oracle-policy-v1
coverage_category: protected-holdout-fixture
result: PASS
bounded_diagnostics: score bucket 0.85-0.90; 1 bounded failure category
artifact_identity:
  artifact_id: sha256:d3f58c513e2e2c34903036acf596fdb04269373170bb2ecf1a9a949efde7917c
  content_hash: d3f58c513e2e2c34903036acf596fdb04269373170bb2ecf1a9a949efde7917c
  visibility: PROTECTED
trust_profile: DEGRADED_SINGLE_AGENT_FIXTURE
calibration_fingerprint: cal-fixture-v1
store_state: AVAILABLE
```

The envelope deliberately excludes the protected payload, oracle plaintext, reveal material, and exact failure examples. Its diagnostic detail is sufficient to distinguish a score bucket and failure category while withholding the protected fixture itself.

## 5. Deterministic case matrix

| Case | Stimulus | Expected | Observed | Authority effect |
|---|---|---|---|---|
| P01 | Protected bytes reachable and SHA-256 matches `ArtifactIdentity` | `PASS` fixture result may be published | `PASS` | Bounded logical pass only |
| P02 | Protected store unavailable | `INCONCLUSIVE` | `INCONCLUSIVE` | Gate cannot pass |
| P03 | Bytes reachable but content hash differs | `INCONCLUSIVE` | `INCONCLUSIVE` | Gate cannot pass; integrity incident |
| P04 | Public envelope scanned for synthetic oracle tokens | no oracle plaintext present | no token present | Leak probe passes for declared serialization surface |
| P05 | Producer attempts protected reveal | deny + audit | denied | Producer cannot reveal sole holdout |
| P06 | Producer attempts oracle rotation | deny + audit | denied | Producer cannot self-change judge |
| P07 | Verifier performs authorized reveal | allow + audit | allowed | Disclosure becomes explicit event |
| P08 | Verifier rotates after compromise | allow; retire v1; activate v2 | allowed | New PolicyEpoch/oracle identity required |
| P09 | Old v1 result evaluated after v1 retirement | reopen, never silently inherit | `REOPEN_REQUIRED` | No authority transfer to v2 |
| P10 | Audit event mutated after publication | chain verification fails | failed as expected | Tampering detectable in reference model |

All ten cases matched their expected logical outcomes in the reference execution.

## 6. Permission model exercised

```yaml
roles:
  producer:
    read_payload: false
    reveal: false
    rotate: false
    write_result: true
  verifier:
    read_payload: true
    reveal: true
    rotate: true
    write_result: true
  reviewer:
    read_payload: false
    reveal: false
    rotate: false
    write_result: false
```

This model separates **candidate/result production** from **holdout control**. A producer can emit a candidate-bound result envelope but cannot reveal or rotate the protected oracle. A verifier can perform those judge-affecting actions, and every attempt—allowed or denied—is retained in the audit stream.

This is a logical permission boundary only. A real provider must prove that its execution/runtime/credential boundaries actually enforce the declared role relation.

## 7. Audit and rotation evidence

Reference audit sequence:

```yaml
- seq: 1
  actor: producer
  action: reveal
  oracle: oracle-policy-v1
  allowed: false
- seq: 2
  actor: producer
  action: rotate
  oracle: oracle-policy-v1
  allowed: false
- seq: 3
  actor: verifier
  action: reveal
  oracle: oracle-policy-v1
  allowed: true
- seq: 4
  actor: verifier
  action: rotate
  oracle: oracle-policy-v1
  allowed: true
  reason: compromise detected
```

Each event was chained using SHA-256 over deterministic JSON plus the previous event hash. The valid chain verified; mutating event 2 from `allowed: false` to `allowed: true` caused verification failure. Final valid event hash:

```text
a6ee2ef17f2d9dce8c2aa49414274b5125975828cec6e1932943c8c5d105a0a1
```

Compromise transition:

```yaml
retired: oracle-policy-v1
activated: oracle-policy-v2
trigger: DISCLOSURE_COMPROMISE
authority_for_old_v1_result: REOPEN_REQUIRED
```

The critical rule is identity, not merely secrecy: after rotation, evidence generated under `oracle-policy-v1` remains historical evidence and cannot silently satisfy a requirement compiled for `oracle-policy-v2`.

## 8. Availability and integrity semantics

A content hash alone is insufficient. The fixture treats protected evidence as usable only when all of the following hold:

1. the result envelope binds the exact candidate/base/evaluator/oracle identities;
2. the referenced `ArtifactIdentity` is reachable;
3. retrieved bytes match the retained content hash;
4. the evaluator/calibration identity is still valid for the applicable policy epoch;
5. required audit/reveal/rotation state does not invalidate the holdout;
6. the current actor has permission for the requested operation.

Failure of (2) or (3) yields `INCONCLUSIVE`, not `PASS`, `NOT_APPLICABLE`, or a cached success. Restoration can make the artifact available again, but any compromise/policy change still requires re-evaluation against the current requirement.

## 9. Leak probe and bounded diagnostics

The public serialization was searched for the synthetic holdout labels `holdout:SECRET_ORACLE_V1` and `holdout:SECRET_ORACLE_V2`; neither appeared. The public output carries only an oracle **identity**, protected artifact identity/hash, coarse score bucket, and one bounded failure category.

This passes only the declared serialization leak probe. It does not test timing channels, artifact-size inference, logs outside the envelope, provider telemetry, exception traces, screenshots, model memorization, or privileged filesystem access. Those remain mandatory provider-specific attack surfaces before production authority.

## 10. Evidence vs inference vs recommendation

### Observed evidence

- Valid reachable bytes reproduced the retained SHA-256 identity and allowed the fixture `PASS` result.
- Unavailable and hash-mismatched evidence both yielded `INCONCLUSIVE`.
- Public envelope contained neither synthetic oracle secret token.
- Producer reveal/rotation attempts were denied; verifier reveal/rotation attempts were allowed.
- Audit-chain mutation was detected.
- Compromise rotation retired `oracle-policy-v1`, activated `oracle-policy-v2`, and forced old-result reopen.

### Inference

These cases are sufficient to show that the Wave 1 protected-evidence contract is internally implementable as a fail-closed logical state machine without disclosing full holdout content in the ordinary result envelope.

### Recommendation

Carry this logical contract into provider/CI design as a minimum acceptance harness. Do **not** choose a protected-store implementation until a provider-specific experiment demonstrates real credential separation, secret handling, retention/restoration, audit immutability, leak resistance, and operational rotation under the same envelope semantics.

## 11. Failure modes and risks retained

- A storage provider may expose protected bytes through logs, metadata, snapshots, backups, support tooling, or privileged operators despite a clean application envelope.
- `SHA-256` identity/integrity in this fixture is not encryption, access control, authenticity, or proof that the producing environment was uncompromised.
- A verifier with reveal authority can itself compromise a holdout; auditability reduces silent mutation but does not prevent malicious authorized disclosure.
- Single-agent fixture execution is `DEGRADED`; it does not establish independent control-plane separation.
- Coarse diagnostics can still leak information cumulatively across repeated attempts; retry/query budgets and differential leak analysis are untested.
- Artifact deletion/restoration races, backup integrity, key rotation, revocation latency, and disaster recovery are not exercised.
- Evaluator fingerprint/calibration drift is delegated to W2-EVAL-01 and may reopen protected evidence even when storage is healthy.

## 12. Reopen conditions

Reopen this evidence or its dependent decision when any of the following occurs:

- protected store/provider, credential topology, encryption/key model, or audit mechanism changes;
- a disclosure, suspected compromise, or unauthorized access event occurs;
- the oracle/config/calibration changes in a judge-affecting way;
- a required protected artifact becomes unreachable, corrupt, or unverifiable;
- a leak probe finds holdout content or an unbounded diagnostic surface;
- stronger multi-agent/isolated permission separation becomes available and can replace the degraded trust profile;
- W2-EVAL-01 shows evaluator/calibration drift affecting the result;
- W2-REV-01 identifies a BLOCKER/MAJOR in the logical contract or evidence claims.

## 13. Required independent critique and downstream work

`W2-REV-01` must independently attack at least: candidate/base/oracle binding, leak-surface completeness, fail-closed availability semantics, producer/verifier separation, audit tamper model, rotation/reopen semantics, and any accidental promotion of this logical fixture into a production security claim.

This task informs `IR-BLOCKER-EVIDENCE-FOUNDATION` and the protected-evidence portion of Wave 2 review. It does not by itself resolve the blocker, select a provider, or authorize implementation readiness.
