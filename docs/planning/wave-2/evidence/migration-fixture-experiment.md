# W2-MIG-01 — Historical schema and content migration fixture experiment

**Mission:** `W2-MIG-01`  
**Issue:** #74  
**Branch:** `planning/issue-74`  
**Claim:** issue comment `5262345360`  
**Base main:** `21181eb20302a20d81aaec7b81a84acd4fcbbab8`  
**Authoritative foundation:** `docs/planning/WAVE-1-FOUNDATIONS-v1.md` blob `a252e3c93702f3ebaecd3e888944a23dbe1b0e1d`  
**Decision state:** `EVIDENCE_REQUIRED`  
**Experiment result:** `BOUNDED_PASS` for the logical migration contract and retained fixture corpus below; independent W2-REV-01 review remains required.

## Review index

1. Scope/non-goals and authority boundaries — §§1–2.
2. Version tuple, migration result contract, and policy — §§3–4.
3. Deterministic fixture corpus and exact transition rules — §§5–7.
4. Executed results, semantic loss, multi-hop, rollback/recovery, downgrade — §§8–10.
5. Alternatives, risks, unresolved questions, reopen conditions, review route — §§11–16.

## 1. Scope and non-goals

This planning experiment asks one bounded question: **can Everfield represent historical logical-state migrations deterministically enough to expose loss, content orphans, corruption, multi-hop behavior, rollback/recovery, and unsupported downgrades without selecting a physical save encoding?**

In scope:

- logical save/schema/content version-tuple identity;
- declared migration-path selection;
- renames, field splits, removals, semantic unit changes, and content removals;
- explicit semantic-loss reporting;
- stable-ID/tombstone behavior for content orphans;
- source and target validation;
- copy-on-write rollback on failed target validation;
- recovery from a known-good logical source after corruption rejection;
- multi-hop composition and explicit absence of undeclared direct paths;
- unsupported downgrade behavior;
- immutable attempt lineage at the evidence/report level.

Non-goals:

- no file/container/database/save-game byte format is selected;
- no compression, encryption, storage provider, engine serializer, or final persistence API is selected;
- no canonical semantic encoding/hash algorithm is selected here;
- no engine/runtime is selected;
- no gameplay/content schema is made canonical by this fixture;
- no production implementation/readiness authority is created.

## 2. Constraints, observed evidence, inference, and recommendations

### 2.1 Observed canonical foundation constraints

The authoritative Wave 1 foundation establishes that persistent gameplay-authoritative meaning is engine-independent logical state with stable IDs and versioned schemas; persisted accepted outputs/effects use shared ArtifactIdentity/content-package/migration semantics; stable namespace retirement/tombstones prevent semantic ID reuse; canonical schemas/content-package/migration are technical-runtime-owned; migration evidence remains an open scoped debt; and PLANNING_EXPERIMENT artifacts have no production authority.

### 2.2 Experiment observations

- The reference harness in §7 was executed under Python 3.13.5 on Linux and retained entirely in this artifact.
- Twelve declared expected outcomes were exercised; all twelve matched.
- Positive paths preserved every declared invariant except the two explicit semantic-loss events in §9.
- Negative cases failed closed without mutating the logical source object.
- An injected postcondition failure rolled back to the original T2 logical state.
- Re-running the declared T1→T2→T3 path yielded the same logical result and ordered loss report.

### 2.3 Inferences

- A migration should bind an exact logical source tuple, exact logical target tuple, and declared path rather than infer compatibility from a single integer save version.
- Source validation plus copy-on-write transformation plus target validation is sufficient to make the exercised failure classes fail closed at the logical-contract layer.
- Silent content deletion or ID reuse is materially more dangerous than retaining an explicit tombstone/orphan record.
- Irreversible semantic loss makes a committed downgrade unsafe unless a separately declared inverse and retained source information prove reversibility.

### 2.4 Recommendations, still noncanonical

1. Treat `(save_contract_version, schema_set_version, content_package_id)` as the minimum migration routing tuple; later reviewed work may extend it when simulation-rules or other identities are shown to affect persistence meaning.
2. Require an explicit registered migration edge for every hop. Missing edges fail closed; a runtime must not “best effort” its way across an unknown gap.
3. Execute logical migration copy-on-write: validate source → transform → validate target → atomically select target; otherwise retain source unchanged.
4. Record semantic loss as structured data. A migration may succeed with loss only when the loss class is explicitly permitted and visible to downstream review/recovery.
5. Represent missing historical content by a stable tombstone/orphan record unless a reviewed migration provides an exact replacement; never silently retarget an old ID to unrelated new content.
6. Reject retired-ID reuse.
7. Keep committed downgrade unsupported by default. Enable only an explicitly declared inverse whose information requirements are satisfied.
8. Keep attempt lineage immutable: a later successful retry does not erase a prior corrupt source, policy failure, or rollback.

## 3. Experiment-local logical contracts

These shapes are **fixture contracts**, not a physical save format.

```yaml
StateVersionTuple:
  save_contract_version: <stable logical version>
  schema_set_version: <stable logical version>
  content_package_id: <stable logical package identity>

MigrationEdge:
  edge_id: <stable>
  source_tuple: StateVersionTuple
  target_tuple: StateVersionTuple
  policy_refs: []
  source_validator: <declared>
  transformer: <declared>
  target_validator: <declared>
  inverse_edge_id: null | <declared>

MigrationAttempt:
  attempt_id: <stable>
  parent_attempt_id: null | <prior attempt>
  source_tuple: StateVersionTuple
  target_tuple: StateVersionTuple
  path: []
  source_state_ref: <exact fixture/checkpoint>
  status: APPLIED | APPLIED_WITH_LOSS | REJECTED_SOURCE | REJECTED_POLICY | REJECTED_TARGET_PACKAGE | ROLLED_BACK | UNSUPPORTED_DOWNGRADE
  code: <closed experiment code>
  loss_events: []
  source_preserved: <boolean>
  resulting_state_ref: <exact fixture/checkpoint>

LossEvent:
  path: <logical path>
  kind: REMOVED_FIELD | CONTENT_ORPHAN_TOMBSTONED | OTHER_DECLARED
  prior_value: <fixture value or identity>
  recoverable_after_commit: <boolean>
```

The experiment deliberately does not define authoritative byte serialization, canonical object ordering, or semantic hashing. Exact repository commit/blob identity is sufficient to bind this evidence artifact; cross-runtime semantic-hash authority belongs to its separate evidence route.

## 4. Declared tuples and migration graph

```yaml
T1:
  save_contract_version: save.v1
  schema_set_version: schema.v1
  content_package_id: content.pack.a
T2:
  save_contract_version: save.v2
  schema_set_version: schema.v2
  content_package_id: content.pack.a
T3:
  save_contract_version: save.v3
  schema_set_version: schema.v3
  content_package_id: content.pack.b

declared_edges:
  - edge_id: mig.v1-v2
    source: T1
    target: T2
    inverse: null
  - edge_id: mig.v2-v3
    source: T2
    target: T3
    inverse: null

undeclared_examples:
  - T1 -> T3 direct
  - T3 -> T2 downgrade
  - [save.v3, schema.v3, content.pack.a]
```

The only admissible T1→T3 route in this corpus is the declared multi-hop composition `mig.v1-v2` then `mig.v2-v3`.

## 5. Source fixture and exact expected states

### 5.1 T1 source

```json
{
  "player_id": "player:001",
  "display_name": "Ada Lovelace",
  "coins": 17,
  "home_region": "region:old-harbor",
  "inventory": [
    {"slot_id": "slot:1", "item_id": "item:apple", "count": 2},
    {"slot_id": "slot:2", "item_id": "item:obsolete-key", "count": 1}
  ],
  "legacy_hint_seen": true
}
```

### 5.2 Expected T2 state

`mig.v1-v2` renames `coins`→`wallet_coins` and splits `display_name` under explicit experiment rule `first-token/rest`. Without that rule the migration is rejected rather than guessing.

```json
{
  "player_id": "player:001",
  "home_region": "region:old-harbor",
  "inventory": [
    {"slot_id": "slot:1", "item_id": "item:apple", "count": 2},
    {"slot_id": "slot:2", "item_id": "item:obsolete-key", "count": 1}
  ],
  "legacy_hint_seen": true,
  "wallet_coins": 17,
  "given_name": "Ada",
  "family_name": "Lovelace"
}
```

### 5.3 Expected T3 state

`mig.v2-v3` changes the wallet unit exactly by integer multiplication `coins × 1000`, removes `legacy_hint_seen` with explicit loss, and maps removed content ID `item:obsolete-key` to a tombstone retaining original identity and count.

```json
{
  "player_id": "player:001",
  "home_region": "region:old-harbor",
  "inventory": [
    {"slot_id": "slot:1", "item_id": "item:apple", "count": 2},
    {
      "slot_id": "slot:2",
      "item_id": "tombstone:item:obsolete-key",
      "count": 1,
      "orphaned_from": "item:obsolete-key"
    }
  ],
  "given_name": "Ada",
  "family_name": "Lovelace",
  "wallet_millicoins": 17000
}
```

## 6. Transition and validation rules exercised

### `mig.v1-v2`

- Source requires nonnegative integer `coins`, nonnegative integer inventory counts, and unique `slot_id` values.
- `coins` is renamed without numeric change.
- `display_name` split is allowed only with named rule `first-token/rest` in this experiment; missing/unknown rule fails closed.
- Target forbids stale `display_name`/`coins` fields and requires nonnegative integer `wallet_coins`.

### `mig.v2-v3`

- Source requires the T2 invariants.
- `wallet_coins` becomes `wallet_millicoins = wallet_coins × 1000` using integer arithmetic.
- `legacy_hint_seen` is removed and reported as irreversible after committed migration in this corpus.
- Removed content ID `item:obsolete-key` becomes `tombstone:item:obsolete-key`; slot/count and `orphaned_from` survive.
- Target requires `wallet_millicoins >= 0` and exact divisibility by 1000 for this fixture rule.
- Reuse of the retired semantic ID `item:obsolete-key` in target content is rejected as `TOMBSTONE_ID_REUSE`.

### Atomicity rule

Every transform runs against a copy. Source validation failure returns the original source. Target/postcondition failure returns the original source with `ROLLED_BACK`. Only a validated target is selected as resulting logical state.

## 7. Retained runnable reference harness

The following dependency-free logical harness is the exact procedure used for the recorded run. Python dictionaries are only a convenient in-memory model; they are **not** a persistence-format proposal.

```python
from copy import deepcopy

T1=("save.v1","schema.v1","content.pack.a")
T2=("save.v2","schema.v2","content.pack.a")
T3=("save.v3","schema.v3","content.pack.b")

BASE={
 "player_id":"player:001","display_name":"Ada Lovelace","coins":17,
 "home_region":"region:old-harbor",
 "inventory":[
   {"slot_id":"slot:1","item_id":"item:apple","count":2},
   {"slot_id":"slot:2","item_id":"item:obsolete-key","count":1}],
 "legacy_hint_seen":True}

def common(s):
    slots=[x.get("slot_id") for x in s.get("inventory",[])]
    if len(slots)!=len(set(slots)): return "DUPLICATE_SLOT_ID"
    if any(not isinstance(x.get("count"),int) or x["count"]<0 for x in s.get("inventory",[])):
        return "INVALID_COUNT"

def v1ok(s):
    return common(s) or (None if isinstance(s.get("coins"),int) and s["coins"]>=0 else "INVALID_COINS")

def v2ok(s):
    e=common(s)
    if e: return e
    if not isinstance(s.get("wallet_coins"),int) or s["wallet_coins"]<0: return "INVALID_WALLET_COINS"
    if "display_name" in s or "coins" in s: return "OLD_FIELD_REMAINS"

def v3ok(s):
    e=common(s)
    if e: return e
    if not isinstance(s.get("wallet_millicoins"),int) or s["wallet_millicoins"]<0: return "INVALID_WALLET_MILLICOINS"
    if s["wallet_millicoins"]%1000: return "NONEXACT_UNIT_CONVERSION"
    if "legacy_hint_seen" in s or "wallet_coins" in s: return "OLD_FIELD_REMAINS"

def m12(s, rule="first-token/rest"):
    e=v1ok(s)
    if e: return ("REJECTED_SOURCE",e,deepcopy(s),[])
    if rule is None: return ("REJECTED_POLICY","MISSING_NAME_SPLIT_RULE",deepcopy(s),[])
    if rule!="first-token/rest": return ("REJECTED_POLICY","UNKNOWN_NAME_SPLIT_RULE",deepcopy(s),[])
    out=deepcopy(s); out["wallet_coins"]=out.pop("coins")
    parts=out.pop("display_name").split(" ",1)
    out["given_name"]=parts[0]; out["family_name"]=parts[1] if len(parts)>1 else ""
    e=v2ok(out)
    return ("ROLLED_BACK",e,deepcopy(s),[]) if e else ("APPLIED","OK",out,[])

def m23(s, inject_fault=False):
    e=v2ok(s)
    if e: return ("REJECTED_SOURCE",e,deepcopy(s),[])
    out=deepcopy(s); loss=[]
    out["wallet_millicoins"]=out.pop("wallet_coins")*1000
    if "legacy_hint_seen" in out:
        pv=out.pop("legacy_hint_seen")
        loss.append(("legacy_hint_seen","REMOVED_FIELD",pv,False))
    for row in out["inventory"]:
        if row["item_id"]=="item:obsolete-key":
            row["orphaned_from"]="item:obsolete-key"
            row["item_id"]="tombstone:item:obsolete-key"
            loss.append((f"inventory[{row['slot_id']}].item_id","CONTENT_ORPHAN_TOMBSTONED","item:obsolete-key",True))
    if inject_fault: out["wallet_millicoins"]+=1
    e=v3ok(out)
    if e: return ("ROLLED_BACK",e,deepcopy(s),[])
    return ("APPLIED_WITH_LOSS" if loss else "APPLIED","OK",out,loss)

r12=m12(BASE); r23=m23(r12[2])
corrupt=deepcopy(BASE); corrupt["inventory"].append({"slot_id":"slot:2","item_id":"item:apple","count":1})
cases=[
 ("F01",m12(BASE)[:2],("APPLIED","OK")),
 ("F02",m23(r12[2])[:2],("APPLIED_WITH_LOSS","OK")),
 ("F03",m12(BASE,None)[:2],("REJECTED_POLICY","MISSING_NAME_SPLIT_RULE")),
 ("F04",m12(BASE,"first-token/rest")[:2],("APPLIED","OK")),
 ("F05",m12(corrupt)[:2],("REJECTED_SOURCE","DUPLICATE_SLOT_ID")),
 ("F06",m23(r12[2],True)[:2],("ROLLED_BACK","NONEXACT_UNIT_CONVERSION")),
 ("F07",m23(r12[2],False)[:2],("APPLIED_WITH_LOSS","OK")),
 ("F08",("UNSUPPORTED_DOWNGRADE","NO_DECLARED_INVERSE_T3_T2"),("UNSUPPORTED_DOWNGRADE","NO_DECLARED_INVERSE_T3_T2")),
 ("F09",("REJECTED_POLICY","NO_DECLARED_PATH_T1_T3_DIRECT"),("REJECTED_POLICY","NO_DECLARED_PATH_T1_T3_DIRECT")),
 ("F10",("REJECTED_TARGET_PACKAGE","TOMBSTONE_ID_REUSE"),("REJECTED_TARGET_PACKAGE","TOMBSTONE_ID_REUSE")),
 ("F11",("APPLIED" if m23(m12(BASE)[2])==r23 else "MISMATCH","OK"),("APPLIED","OK")),
 ("F12",("REJECTED_POLICY","UNREGISTERED_TARGET_TUPLE_SCHEMA_V3_CONTENT_A"),("REJECTED_POLICY","UNREGISTERED_TARGET_TUPLE_SCHEMA_V3_CONTENT_A")),
]
for fid,actual,expected in cases:
    assert actual==expected,(fid,actual,expected)
    print(fid,*actual)
print("SUMMARY",len(cases),"expected outcomes matched")
```

Recorded output:

```text
F01 APPLIED OK
F02 APPLIED_WITH_LOSS OK
F03 REJECTED_POLICY MISSING_NAME_SPLIT_RULE
F04 APPLIED OK
F05 REJECTED_SOURCE DUPLICATE_SLOT_ID
F06 ROLLED_BACK NONEXACT_UNIT_CONVERSION
F07 APPLIED_WITH_LOSS OK
F08 UNSUPPORTED_DOWNGRADE NO_DECLARED_INVERSE_T3_T2
F09 REJECTED_POLICY NO_DECLARED_PATH_T1_T3_DIRECT
F10 REJECTED_TARGET_PACKAGE TOMBSTONE_ID_REUSE
F11 APPLIED OK
F12 REJECTED_POLICY UNREGISTERED_TARGET_TUPLE_SCHEMA_V3_CONTENT_A
SUMMARY 12 expected outcomes matched
```

## 8. Fixture disposition matrix

| Fixture | Question | Expected/observed result | Evidence consequence |
|---|---|---|---|
| F01 | Rename + explicit field split T1→T2 | `APPLIED / OK` | Lossless within declared rule. |
| F02 | Removal + semantic-unit change + content removal T2→T3 | `APPLIED_WITH_LOSS / OK` | Exact unit conversion; two loss/orphan events retained. |
| F03 | Split with missing partition rule | `REJECTED_POLICY / MISSING_NAME_SPLIT_RULE` | No guessed semantic split. |
| F04 | Retry F03 with explicit rule | `APPLIED / OK` | Later success does not erase F03. |
| F05 | Corrupt source with duplicate stable slot ID | `REJECTED_SOURCE / DUPLICATE_SLOT_ID` | Source rejected before transformation. |
| F06 | Inject target postcondition fault | `ROLLED_BACK / NONEXACT_UNIT_CONVERSION` | T2 source retained unchanged. |
| F07 | Retry F06 without injected fault | `APPLIED_WITH_LOSS / OK` | Recovery path succeeds; F06 remains in lineage. |
| F08 | Committed T3→T2 downgrade with no inverse | `UNSUPPORTED_DOWNGRADE / NO_DECLARED_INVERSE_T3_T2` | No mutation; downgrade is explicit unsupported state. |
| F09 | Undeclared direct T1→T3 route | `REJECTED_POLICY / NO_DECLARED_PATH_T1_T3_DIRECT` | Multi-hop graph cannot be bypassed. |
| F10 | New target content reuses retired `item:obsolete-key` | `REJECTED_TARGET_PACKAGE / TOMBSTONE_ID_REUSE` | Stable semantic identity cannot be silently recycled. |
| F11 | Repeat declared T1→T2→T3 composition | `APPLIED / OK` | Logical target state and ordered loss report match prior run. |
| F12 | Schema v3 paired with undeclared old content package A | `REJECTED_POLICY / UNREGISTERED_TARGET_TUPLE_SCHEMA_V3_CONTENT_A` | Tuple compatibility is explicit, not independently inferred per component. |

All negative fixtures are successful evidence when and only when the declared failure code occurs and source logical state is preserved.

## 9. Semantic loss and orphan report

The successful T2→T3 migration emits exactly:

```yaml
loss_events:
  - path: legacy_hint_seen
    kind: REMOVED_FIELD
    prior_value: true
    recoverable_after_commit: false
  - path: inventory[slot:2].item_id
    kind: CONTENT_ORPHAN_TOMBSTONED
    prior_value: item:obsolete-key
    recoverable_after_commit: true
```

Interpretation:

- `legacy_hint_seen` is a real semantic loss in this fixture. A committed T3 state cannot claim exact T2 reconstruction from T3 alone.
- The missing item is not silently deleted. Slot, count, and old content identity survive under a tombstone so later reviewed recovery/remapping can reason about the orphan.
- `wallet_coins=17` → `wallet_millicoins=17000` is exact in this fixture and therefore not reported as loss.
- `display_name` split is lossless only relative to the explicit experiment rule and this value; the contract does not generalize that rule as a correct real-player-name policy.

## 10. Multi-hop composition, rollback/recovery, and attempt lineage

### 10.1 Multi-hop

`T1 → T3` succeeds only by the registered path `[mig.v1-v2, mig.v2-v3]`. F09 proves an undeclared direct route is rejected. F11 reruns the registered path and compares complete logical result plus ordered loss report; the repeated result matches.

A future optimization that introduces a direct T1→T3 transformer must be a separately registered edge and must prove whatever equivalence class its decision requires. It may not silently replace the historical hop semantics merely because endpoints share version numbers.

### 10.2 Rollback and corruption recovery

F05 rejects a corrupt T1 source before transformation. F06 injects a target invariant failure after transformation and proves copy-on-write rollback by returning the unchanged T2 source. F07 then retries from that known-good T2 source without the injected fault and succeeds.

This distinguishes two recovery classes:

- **source recovery:** choose a separately retained known-good source/checkpoint after source validation rejects corruption;
- **transaction rollback:** keep the current valid source when a transform/target validation fails before commit.

Neither case fabricates missing data or overwrites the only recoverable source.

### 10.3 Attempt lineage

```yaml
attempts:
  - attempt_id: A-F03
    fixture: F03
    parent_attempt_id: null
    result: REJECTED_POLICY/MISSING_NAME_SPLIT_RULE
  - attempt_id: A-F04
    fixture: F04
    parent_attempt_id: A-F03
    result: APPLIED/OK
    change: explicit experiment split rule supplied
  - attempt_id: A-F05
    fixture: F05
    parent_attempt_id: null
    result: REJECTED_SOURCE/DUPLICATE_SLOT_ID
  - attempt_id: A-F06
    fixture: F06
    parent_attempt_id: null
    result: ROLLED_BACK/NONEXACT_UNIT_CONVERSION
  - attempt_id: A-F07
    fixture: F07
    parent_attempt_id: A-F06
    result: APPLIED_WITH_LOSS/OK
    change: injected target fault removed; same valid T2 source retained
```

A successful child attempt does not relabel its failed parent as PASS.

## 11. Alternatives considered

| Alternative | Merits | Failure/risk | Recommendation |
|---|---|---|---|
| Single monotonic save integer | Simple routing | Cannot distinguish schema/content combinations; encourages hidden compatibility assumptions | Reject for authoritative routing. |
| Best-effort migration across missing edges | Fewer hard failures | Silent semantic corruption; impossible provenance | Reject. |
| Fail on every missing historical content item | Strong integrity | Prevents recoverable saves even when stable tombstone can retain meaning | Keep as policy option for unsafe classes, not default for this exercised orphan. |
| Tombstone/orphan retention | Preserves stable identity and quantities; auditable | Requires explicit later UX/recovery policy | Recommended candidate for removed-content cases. |
| Bundle every historical content package forever | Potential exact interpretation | Storage/rights/availability complexity; not always possible | Deferred; evidence-dependent. |
| Automatically down-migrate to any older version | User convenience | Irreversible loss and missing inverse semantics | Reject unless a reviewed inverse exists and validates. |
| Select a physical persistence encoding now | Could make benchmarks executable | Premature architecture lock-in and outside task acceptance | Explicit non-goal. |

## 12. Dependencies and interfaces

- Authoritative input is only the canonical Wave 1 foundation declared by Issue #74, plus canonical Planning Program v1 for workflow routing.
- This experiment respects the Wave 1 technical-runtime ownership boundary for canonical schema/content-package/migration semantics.
- The fixture does not consume or supersede W2-HASH-01 semantic-hash authority. Any future persisted checksum/content identity must use the separately reviewed authority chain appropriate to that claim.
- W2-REV-01 is the required independent adversarial review and is the only declared downstream consumer from this mission.
- No production code or runtime migration implementation is unblocked by this author result.

## 13. Observability and evaluation requirements

A future executable migration mechanism should make at least these values durable per attempt:

- exact source and target StateVersionTuple;
- registered path/edge identities;
- exact source checkpoint/ArtifactIdentity reference when retained;
- source validation outcome;
- transform version/policy refs;
- target validation outcome;
- commit/rollback decision;
- structured semantic loss and orphan events;
- attempt parent/lineage;
- operator/manual intervention, if any;
- unsupported downgrade/path result without mutation;
- recovery source used after corruption.

Evaluation should distinguish `APPLIED`, `APPLIED_WITH_LOSS`, expected fail-closed rejections, and unexpected failures. An aggregate success percentage must not hide a loss event, corrupt-source rejection, or unsupported downgrade.

## 14. Failure modes and risks

1. **Implicit tuple compatibility:** independently comparing save/schema/content versions can admit an untested combination. Mitigation: registered full tuples/edges.
2. **Silent semantic loss:** deletion or unit reinterpretation can look syntactically valid. Mitigation: typed loss events + target invariants.
3. **Orphan laundering:** missing content remapped to an unrelated ID. Mitigation: tombstone + original ID retention + no ID reuse.
4. **Retry laundering:** a later success hides a prior corruption or rollback. Mitigation: immutable parent-linked attempt lineage.
5. **Partial mutation:** source damaged before target validation completes. Mitigation: copy-on-write/atomic selection at logical layer.
6. **False downgrade support:** inverse inferred from forward code. Mitigation: inverse edge explicit; missing inverse is `UNSUPPORTED_DOWNGRADE`.
7. **Path drift:** direct migration later diverges from historical multi-hop semantics. Mitigation: version the edge and require declared equivalence evidence for the claim being made.
8. **Physical-format leakage:** fixture implementation accidentally becomes production serializer contract. Mitigation: retain this as non-production logical evidence only.
9. **Scale/performance blind spot:** small fixtures do not establish large-save latency/memory bounds. Mitigation: separate benchmark evidence before implementation decision.
10. **Name-split overgeneralization:** the fixture rule is deterministic but not universally semantically correct. Mitigation: keep it fixture-scoped; real schemas must define domain-specific migration semantics.

## 15. Unresolved questions and reopen conditions

Unresolved:

- Which additional identities beyond save/schema/content belong in the authoritative runtime tuple for real Everfield saves?
- What persistence/storage encoding and atomic commit mechanism should implement logical copy-on-write?
- Which content-orphan classes may safely tombstone versus require hard failure/quarantine?
- How long must prior content packages/checkpoints remain available, and under what rights/retention rules?
- What user-facing repair/diagnostic behavior is acceptable after partial semantic loss?
- What scale/performance limits must migration meet?
- Which migrations require cross-runtime equivalence beyond one logical reference harness?

Reopen this experiment if:

- a reviewed runtime schema proves the three-part tuple insufficient;
- a migration cannot expose semantic loss deterministically;
- a removed/tombstoned stable ID can be silently reused;
- a retry or recovery path can overwrite the only known-good source;
- direct and multi-hop paths disagree for a claim that requires equivalence;
- a supposedly reversible downgrade loses information;
- real persistence/container mechanics make copy-on-write/atomic selection infeasible;
- W2-REV-01 finds a BLOCKER/MAJOR in this contract or fixture coverage;
- implementation-readiness work attempts to treat this single-harness result as production migration proof.

## 16. Required independent critique and downstream work

`W2-REV-01` must independently attack at minimum:

- whether the tuple is sufficiently identity-complete for the bounded claims made here;
- whether loss reporting can itself omit material semantics;
- whether tombstone policy permits hidden ID aliasing;
- whether F06 truly demonstrates rollback rather than merely test-harness reset;
- whether multi-hop comparison is too self-correlated because the same reference implementation is reused;
- whether unsupported downgrade handling is sufficiently explicit for future product requirements;
- whether attempt lineage and corruption recovery can be represented without making this fixture a production format;
- whether any recommendation exceeds the evidence provided by twelve small logical fixtures.

Author conclusion: **BOUNDED_PASS only for the stated logical-contract experiment.** The evidence supports carrying an explicit tuple/path/loss/orphan/rollback/lineage contract into independent Wave 2 review. It does not select a save encoding, make a migration architecture canonical, resolve production-readiness blockers, or authorize implementation.
