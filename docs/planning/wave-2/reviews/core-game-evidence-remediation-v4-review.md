# W2-REV-05 — Fresh aggregate review of W2-GAME-EV-REM-03

**Issue:** #223  
**Review mode:** `DEGRADED_SINGLE_AGENT_FRESH_EPISODE`, distinct from Issue #220 producer episodes and Issue #219 prior reviewer episode.  
**Claim:** `5284684395`  
**Base:** `main@81919c6b14ad073cfeab051672f8f6cb7b20d218`  
**Reviewed Issue #220:** terminal status `5284654055`, head `ac9af37d337deae99f6d99eb16ad8332ff6f2166`, substantive work `958f032c659f4bcbf87ab4dc1c307433cb30175a`, draft PR #222.  
**Disposition:** **CHANGES_REQUIRED — 0 BLOCKER / 1 MAJOR / 0 correction-requiring MINOR**.

This review binds the exact immutable Issue #220 packet and independently reconstructs the bounded fictional-game mechanics before reconciling producer dispositions. Issue #220 and its branch remain read-only review inputs.

## Exact reviewed identities

- transition/search blob `7768d407413bdc2762a7589d6942a0274c443b44`;
- automation-decisions blob `4894f429f98143a264a7b88f5a2758dabfa1845e`;
- normalized v4 results blob `648767682537e385f8d9379566049fe21571d2d2`;
- producer disposition blob `1ca974eb53058946ba7e10a9fce6bdb86e0bbf89`;
- Issue #220 handoff blob `4116f96bad49df3c2fd54bf921f18ff375adf509`;
- predecessor Issue #219 review blob `f6a17045b99ee7960c94bdb9380b273e2f1fd038` and review work `713fe301a74dd67e40c4947bcbf6e429d9ff7154`.

## Fresh mechanical reconstruction

### Transition/search

The v4 object materially improves the predecessor: values, comparisons, conjunctions, action references, add/set effects, immutable-pre-state reads, action order, typed event predicates, breadth-first expansion, non-pruning, and retained rows are now explicit machine objects rather than prose expressions.

Using the declared initial state and action order, and **only after adding two conventional rules that the exact object does not itself state** — (a) untouched state fields carry from `pre` to `post`, and (b) `trace_suffix` evaluates the trace including the current action — independent breadth expansion reproduces:

- depth 1: **4** feasible traces;
- depth 2: **16** feasible traces;
- depth 3: **63** feasible traces;
- total retained depth-1..3 rows: **83**;
- first gate violation: `advance_stage`;
- first allowed opportunity event: `market_trade`;
- first repeatable-free-gain violation: `free_step, free_step`;
- first refund-retention violation: `buy_unlock, reset`.

The producer rows are therefore consistent with the intended interpretation. They are not yet a consequence of the exact machine bytes without those extra rules, which is the remaining authority defect below.

### Automation invariant correction

The v4 automation object preserves the v3 `choice_surfaces`, `tier_surfaces`, and retained payback winner counts `1 / 3 / 5`. `expansion.hold` remains exactly the zero-delta option `{coin: 0, capacity: 0}` and is now explicitly declared as the intentional no-op. The false v3 boolean `every_option_changes_at_least_one_fictional_state_field: true` is corrected to `false`; the restricted non-no-op invariant is true.

No option identity, modeled delta, tier membership, or retained payback input changed. `W2-REV4-m01` is therefore mechanically closed as a record correction and does not require a `GDF-E4` rerun.

### Preserved evidence

The v4 result object continues to bind unchanged v3 policy/search and progression provenance and names the same six unaffected v2 IDs with `UNCHANGED_NOT_RERUN_NOT_UPGRADED`. The reviewed-clean v3 results `GDF-E2`, `GDF-E4` subject only to the corrected no-op record, `EPA-E3`, `EPA-E7`, and `AGE-E3` are not materially rewritten by this packet. Historical negative evidence remains predecessor provenance.

## Finding

### W2-REV5-M01 — transition machine still requires unstated frame and trace-context semantics

**Severity:** MAJOR  
**Affects claimed PASS:** `AGE-E4`  
**Reopens:** `W2-REV4-M01` only.

Two load-bearing semantics remain absent from exact `TRANSITION-CHECK-v4`:

1. **No frame rule for untouched state fields.** Effects define only targeted `post[field]` assignments/additions, but the machine never states that `post` is initialized from `pre` or that every untargeted field is preserved. Retained terminal states assume that rule throughout. More importantly, `refund_check` evaluates `post.unlock == true` after action `reset`, while `reset` has no `unlock` effect. Without an explicit frame rule, `post.unlock` is not mechanically defined by the exact transition object, so the `buy_unlock, reset` violation cannot be derived without reviewer-supplied semantics.
2. **`trace_suffix` lacks transition-time trace context.** The predicate says only that “trace ends with” an action array; it does not specify whether event evaluation sees the pre-transition history or the history after appending the current action. The retained `free_step, free_step` first violation requires the current-inclusive interpretation. A pre-transition interpretation shifts the event and changes retained classifications.

These are not stylistic omissions: both directly affect the deterministic violation evidence required by Issue #220. The packet therefore still cannot prove `AGE-E4` from exact bytes alone under the predecessor review’s standard, even though the intended interpretation reproduces the producer rows.

**Required correction:** publish a minimum bounded successor that makes the transition state and event context closed and versioned, including explicit `post` frame semantics for untargeted fields and explicit current-action inclusion/exclusion for trace predicates. Regenerate/rebind the complete retained frontier and rerun only `AGE-E4` unless another exact input materially changes. Preserve the clean automation correction and all unaffected evidence.

## Result disposition

`W2-REV4-m01` is closed. `W2-REV4-M01` is not fully closed because `AGE-E4` still depends on two unstated machine semantics. The v4 producer summary of six affected PASS results is therefore not admissible as a fully reviewed six-PASS packet.

Overall disposition is **CHANGES_REQUIRED**. Route exactly one bounded remediation successor for `W2-REV5-M01`; do not broaden the correction into policy/search, progression mutation, automation tier, or unaffected v2 rewrites.

## Authority and blocker state

`IR-BLOCKER-GAME-EVIDENCE` remains **OPEN** for `SCOPE-CORE-GAMEPLAY-v1`. Human fun/player preference remains out of scope. This review grants no gameplay or production implementation, engine selection, release approval, implementation readiness, verification PASS, legal/provider authority, canonical status, or integration authority beyond separately applicable repository directives. Any main integration remains separately authorized and squash-only.
