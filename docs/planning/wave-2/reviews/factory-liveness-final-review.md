# Final factory liveness review — Issue #689

Reviewed complete immutable repair candidate Issue #687 / PR #688 at `cef4e41a952e0c0f92fc9d5c2c183b24da7a8c33` against current `main@853ceee085253f05030e617141ad00883d4f6226`.

Trust mode: `DEGRADED_SINGLE_AGENT`.

Disposition: `CHANGES_NEEDED` — 0 BLOCKER / 1 MAJOR / 0 correction-requiring MINOR.

Prior findings M01–M04 are materially closed: latest operational state suppresses stale terminal closure; rejected PR matching is explicit; terminal auto-close requires a same-actor/same-mission ownership generation and concrete head/work SHAs; factory transitions no longer self-consume; registered dispatch retries until a matching exact-main run or trusted machine marker exists, then stops redispatch.

## M05 — edited schema-3 comments are still consumed

Canonical schema-3 gives edited operational comments zero authority effect, but `parse_operational()` currently checks author association/protocol/schema/kind without requiring immutable GitHub comment timestamps. An OWNER could edit a claim or terminal comment after publication and the maintenance tool could still use it to close an issue or materialize/dispatch a route. The conservative maintenance subset must reject any operational comment where `created_at != updated_at` (and fail closed if immutable timestamp data is absent). Dispatch marker comments should receive the same immutability check.

Required next route: one minimal remediation adding immutable-comment timestamp validation plus deterministic self-tests for edited operational and edited dispatch-marker rejection. Preserve all other reviewed behavior unchanged, then perform a fresh final review before integration.
