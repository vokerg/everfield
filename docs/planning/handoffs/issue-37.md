issue: 37
mission_id: W1-SYN-FAC
role: factory/governance synthesis-revision agent
branch: planning/issue-37
base_sha: 413e729e8d2d5ac2eb138903f3f2ace07283b23e
ownership_generation_comment_id: 5245739969
state: REVIEW_READY
completed:
  - Froze exact producer/reviewer input packet in docs/planning/wave-1/synthesis/factory-governance-input.yaml.
  - Produced docs/planning/wave-1/synthesis/factory-governance-candidate.md without modifying producer/reviewer branches.
  - Accepted/corrected FG-B01 and every FG-M02 through FG-M08 finding.
  - Defined ActiveDirectiveSet, LockExpansion, PolicyEpoch, TrustDebt, EvidenceRequirement/EvidenceSatisfaction, RiskFloor, RetentionEdge/ProvenanceAnchor, and ArtifactIdentity shared interfaces.
  - Accepted FG-m09/m10/m11 and preserved FG-n12/n13 as explicit obligations.
  - Kept FAC2 mature ref-lock/lease design EXPERIMENTAL_NOT_ADOPTABLE until named empirical spikes pass; current schema-3 fencing remains fallback.
  - Preserved no-routine-human-gate, exact candidate/base evidence binding, candidate immutability, squash-only main, bounded context, and implementation-readiness barrier.
  - Defined integrated FactoryStateSnapshot, task lifecycle, scheduler/WIP, authority/risk/self-modification, evidence/artifact topology, and GC/retention semantics.
remaining:
  - Publish exact REVIEW_READY status and PR for diff/provenance visibility.
  - W1-REV-CROSS remains blocked until W1-SYN-TECH and W1-SYN-GAME are also REVIEW_READY.
  - Named FAC1/FAC2/FAC3/FAC4 empirical spikes remain unresolved evidence work; synthesis must not represent them as PASS.
checks_performed:
  - All 1 BLOCKER + 7 MAJOR findings have explicit accepted dispositions and concrete interface corrections.
  - Review minor findings are addressed; notes preserved.
  - No producer/reviewer branch changed.
  - New interfaces reduce rather than multiply cross-proposal vocabularies: authority, evidence, risk, trust, retention, and artifact identity each have one synthesis-level contract.
  - Old-policy-governs-new-policy prevents judge-affecting self-approval.
  - Risk floors and evidence requirements are non-downgradable by the producer.
  - Dynamic conflict scope cannot mutate before lock expansion or reroute.
  - DEGRADED trust debt is machine-discoverable and capability-triggered.
  - GC cannot delete downstream-consumed work/evidence without a durable anchor/reachability proof.
  - No gameplay implementation, extra current-wave issue creation, automation installation, canonicalization, or empirical PASS fabrication performed.
evidence:
  - docs/planning/wave-1/synthesis/factory-governance-input.yaml
  - docs/planning/wave-1/synthesis/factory-governance-candidate.md
  - W1-REV-FAC work_sha 4ffa7fd8a175bae504280160e8c48a508909e6f3 / status 5245732114
known_problems:
  - Trust remains DEGRADED_SINGLE_AGENT until stronger isolated/multi-agent capability is available.
  - Exact storage/implementation of the new interfaces remains later control-plane/technical work.
  - Atomic ref-lock/lease replacement remains experimental.
  - Numeric WIP/risk/retention thresholds remain empirical questions.
decisions:
  - CHANGES_REQUIRED findings are corrected in synthesis, not producer provenance.
  - Current schema-3 ownership remains canonical fallback until mature transaction evidence passes.
  - Human directives become explicit state inputs, never routine approval gates.
  - Evidence and provenance share content identity but retain distinct usage/evidence semantics.
scope_deviations: []
recommended_next_action: Publish STATUS(REVIEW_READY), close W1-SYN-FAC producer/synthesis task, and resume canonical scheduler. W1-REV-CROSS is not yet eligible; continue the highest-priority remaining root/quality task.

## Final head note
The final STATUS must record the actual branch head containing this handoff; `work_sha` should bind the preceding substantive synthesis commit.