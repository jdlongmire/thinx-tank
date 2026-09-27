# Prior Art Research Ledger

Status: initial primary-source pass, 2026-09-27.

Primary sources are preferred. Peer-reviewed surveys are included as secondary landscape checks and labeled accordingly.

## Initial primary-source findings

| Source | Relevant construct | Relationship to MxM | Initial disposition | Confidence |
|---|---|---|---|---|
| NIST AI RMF / NIST AI 600-1 | AI risk governance and trustworthiness | overlaps Morals/governance at organizational level | generic AI risk governance already satisfied | HIGH |
| OpenAI Agents SDK | agents, tools, guardrails, sessions, HITL, tracing | overlaps Means, Memory, approvals, Evidence/observability | mechanisms individually established prior art | HIGH |
| Anthropic agent guidance | workflows/agents, human control, permissions, transparency | overlaps Methods, Means, Morals and human authority | principles/mechanisms established prior art | HIGH |
| Model Context Protocol | prompts, resources, tools; explicit control allocation; authorization | overlaps Means/context interfaces and control | capability/context protocol established prior art | HIGH |
| Microsoft Agent Framework Harness | provider-flexible runtime scaffolding, state/context, approvals, memory, modes, tools, observability | closest runtime-harness comparator | MxM must prove a layer above runtime harness composition | HIGH |
| Microsoft Semantic Kernel | agents, orchestration, HITL, repeatable process, audit | overlaps Methods, Means and workflow governance | mechanisms individually established prior art | HIGH |
| Li (COLING 2025) | unified taxonomy of tool use, planning/RAG, feedback learning | challenges broad taxonomy novelty | full-text comparison pending | MEDIUM |
| Luo et al. (ACL 2026) | agent-memory taxonomy | challenges Memory novelty | TMF-specific comparison pending | MEDIUM |
| Yehudai et al. (ACL 2026) | agent evaluation taxonomy | supports explicit falsifiable evaluation | adopt as evaluation context | MEDIUM |

## Claims eliminated by this pass

Human approval, guardrails, persistent/session memory, tool mediation, tracing, provider abstraction, runtime harnesses, workflow enforcement, and human control are established prior art.

## Candidate contribution remaining

The defensible question is narrower: whether MxM supplies a useful model- and runtime-harness-neutral meta-architectural decomposition and authority contract that preserves normative reasoning posture, constraints, mission/identity, persistence semantics, procedural governance and capability boundaries across heterogeneous runtimes, while separating execution evidence and human Acceptance from model self-report.

That claim remains unproven.
