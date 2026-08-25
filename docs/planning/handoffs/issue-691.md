# Issue #691 — immutable comment remediation handoff

Source review: Issue #689 / PR #690 over immutable Issue #687 / PR #688 at `cef4e41a952e0c0f92fc9d5c2c183b24da7a8c33`.

## M05 closed
Maintenance now requires GitHub issue/PR comments used as schema-3 operational authority or factory dispatch markers to be immutable: both `created_at` and `updated_at` must be present and exactly equal. Edited or timestamp-ambiguous comments fail closed and are ignored for automatic issue closure, transition materialization, and dispatch-marker idempotence.

## Regression verification
The exact remediation script compiles with Python and its deterministic `self_test()` passes. Tests cover M01–M05: valid owner-bound terminal, later live claim suppression, missing ownership reference, actor mismatch, untrusted terminal, edited terminal, edited ownership claim, rejected-PR predecessor prose, explicit rejected-PR forms, normal-successor versus factory-transition consumption, valid dispatch marker, route mismatch, and edited dispatch marker rejection.

All prior ownership linkage, route allowlist, exact-main dispatch, retry/idempotence, workflow permissions, entry directives, and authority limits are unchanged. Fresh final review is required before squash-only integration.
