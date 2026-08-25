# START HERE — Canonical Planning Entry

**Phase:** PLANNING  
**Authority:** Entry pointer to canonical Planning Program v1 plus active human liveness directives in `/AGENTS.md`.

1. Read `/AGENTS.md` and current `docs/planning/PLANNING-PROGRAM-v1.md`.
2. Parse the program's `Canonicalized by` issue.
3. Resolve the active canonical binding: matching program blob + activation SHA ancestor/equal current main + valid verification/squash provenance.
4. Before frontier selection, reconcile GitHub-open state against trusted schema-3 terminal comments. `DONE`, `SUPERSEDED`, and `INVALIDATED` issues are not eligible merely because GitHub still reports them open.
5. If a trusted terminal record declares `required_next_route`, require either a live successor/recovery issue or a registered repository-internal execution route. Missing transition materialization is liveness work and takes priority over unrelated new work.
6. If binding resolves, query remaining open `[PLAN-v1]` issues and use canonical schema-3 dispatch.
7. If no binding exists and the named issue has no prior canonical binding, execute only its verified post-merge activation sequence.
8. If the issue has a prior binding for a different program blob, fail closed as canonical-binding mismatch and use recovery/reverification.
9. Prefer recoverable/review/revision/verification/integration work before new proposals.
10. Never use chat history as project authority; all `main` integration is squash-only.

Repository automation in `.github/workflows/planning-frontier-maintenance.yml` performs conservative state reconciliation and may dispatch only explicitly registered exact-main workflow routes from `.github/planning-frontier-routes.json`. It grants no review, verification, integration, decision, or canonical authority.
