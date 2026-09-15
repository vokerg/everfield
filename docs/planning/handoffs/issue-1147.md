# Issue #1147 handoff — verified lease revision canonicalization

## Identity

- mission: `FACTORY-LEASE-CANON-ACT-01`
- winning claim: `5675044294`
- branch: `planning/issue-1147`
- base / verified base: `main@8468daf824aee6e5ef48ffead0918a5512bd4b0c`
- source producer: Issue #1137 terminal `5668329071`, PR #1139, head `e0f87494eea335ff195ace746689b486bc40909d`
- source candidate blob: `2d98f95c58d15bddf7c00be3fd5905aa8ca501e5`
- source manifest blob: `d075d7bd92e1c7636ab77a962a677c521c9db7b5`
- verification: Issue #1138 terminal `5674994717`, result `PASS`, disposition `PASS_FOR_SEPARATE_CANONICALIZATION`
- verification head: `1ffbfd856667e4d3f9e0e787e20371c689c10551`
- prior active binding: Issue #6 comment `5245368879`
- prior canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`

## Promotion

Applied the exact verified manifest v2 transform using canonicalization issue number `1147` as the sole provenance-only runtime parameter.

Exactly four source literals were replaced:
1. candidate title -> canonical title;
2. candidate state -> `CANONICAL`;
3. candidate authority -> canonical planning authority;
4. revision issue -> `Canonicalized by: Issue #1147`.

Every remaining candidate byte is identical to the verified candidate. Program-promotion commit: `d98a31959c925d5ff1c3c19c0e54d082406c799a`. Resulting canonical program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`.

Self-check:
- exact transformed bytes equal recomputed expected output: PASS;
- canonicalized-by issue 1147 appears exactly once: PASS;
- 21,600-second ownership lease semantics preserved: PASS;
- implementation-readiness barrier preserved: PASS;
- squash-only integration rule preserved: PASS.

## Remaining exact route

1. Open an exact-head PR containing only the promoted program plus this handoff.
2. Re-check current main remains `8468daf824aee6e5ef48ffead0918a5512bd4b0c`, PR head and changed paths are exact, and mergeability is clean.
3. Squash-merge only.
4. Verify the resulting main program blob equals `fd4cf1119c3f86acc3af620024eea72235e81ce4`.
5. Publish terminal schema-3 `INTEGRATION_STATUS` on Issue #1147 with the new squash main SHA and durable canonical binding.
6. Only that terminal binding activates the lease semantics.

No implementation-readiness, engine-selection, release, production, or unrelated decision authority is created by this packet.