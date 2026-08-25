# Factory liveness remediation review — Issue #685

Reviewed immutable remediation Issue #682 / PR #684 at `040ddf86a4c2a71a89693c741a05986ff96be5a1` against current `main@853ceee085253f05030e617141ad00883d4f6226`.

Trust mode: `DEGRADED_SINGLE_AGENT`.

Disposition: `CHANGES_NEEDED` — 0 BLOCKER / 2 MAJOR / 0 correction-requiring MINOR.

Prior findings M01/M02 are closed: a later operational record suppresses stale-terminal closure, and predecessor `CHANGES_NEEDED` prose no longer retires a live PR. Deterministic self-tests cover both.

## M03 — terminal reconciliation does not validate ownership linkage

`parse_operational()` accepts any trusted-author comment with protocol/schema/kind/state. A malformed owner-authored `STATUS(DONE)` missing or mismatching its ownership generation/head/work binding can therefore close an issue even though canonical schema-3 gives that comment zero authority effect. Auto-close must remain conservative: require issue identity, mission/actor identity, OWNER authority mode, a valid earlier ownership-generating comment id from the same actor, and exact-looking head/work bindings before storage closure. Unsupported/ambiguous terminal forms must remain open for agent reconciliation.

## M04 — transition creation can permanently suppress dispatch retry

`consumed_sources` treats the generated factory-transition issue itself as a consumed predecessor. If the workflow fails after creating the transition issue but before a registered dispatch is accepted/recorded, later maintenance runs skip the source entirely and never retry. A factory-transition issue must not count as a non-transition successor. Existing transition issues should remain eligible for registered dispatch until an explicit trusted factory dispatch marker or an already-observed matching fresh run is recorded; after that marker, automatic redispatch must stop and the transition issue owns downstream handling.

Required next route: one bounded remediation of M03/M04, preserving #682/#684 immutable, followed by fresh review.
