# START HERE — Canonical Planning Entry

**Phase:** PLANNING  
**Authority:** Entry pointer to canonical Planning Program v1.

1. Read `/AGENTS.md` and current `docs/planning/PLANNING-PROGRAM-v1.md`.
2. Parse the program's `Canonicalized by` issue.
3. Resolve the active canonical binding: matching program blob + activation SHA ancestor/equal current main + valid verification/squash provenance.
4. If binding resolves, query open `[PLAN-v1]` issues and use canonical schema-3 dispatch.
5. If no binding exists and the named issue has no prior canonical binding, execute only its verified post-merge activation sequence.
6. If the issue has a prior binding for a different program blob, fail closed as canonical-binding mismatch and use recovery/reverification.
7. Prefer recoverable/review/revision/verification/integration work before new proposals.
8. Never use chat history as project authority; all `main` integration is squash-only.
