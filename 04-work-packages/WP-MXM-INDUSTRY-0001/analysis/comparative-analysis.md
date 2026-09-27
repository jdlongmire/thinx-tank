# Comparative Analysis

Status: initial comparison, 2026-09-27.

## Abstraction-level rule

MxM must not present every adjacent framework as a direct competitor. Comparison is by architectural concern and abstraction level.

| Construct | Primary level | Strong MxM overlap | Material distinction to test |
|---|---|---|---|
| NIST AI RMF | organizational risk governance | Morals, governance, trustworthiness | executable/runtime meta-architecture vs organizational guidance |
| OpenAI Agents SDK | agent runtime/application framework | Means, Memory, guardrails, HITL, tracing | whether MxM surfaces survive SDK/runtime replacement |
| Anthropic agent patterns | engineering patterns/product governance | Methods, Means, human control | portable architecture vs provider/product practice |
| MCP | interoperability protocol | Means, context/resources, tool control | governance/identity/reasoning/persistence above protocol |
| Microsoft Agent Framework Harness | runtime harness | context, memory, approvals, modes, tools, model abstraction, observability | critical comparator: MxM must justify a layer above provider-flexible runtime scaffolding |
| Semantic Kernel | agent/workflow runtime | Methods, Means, HITL, process, audit | whether six surfaces and authority semantics add a portable normative layer |
| Academic taxonomies | descriptive research taxonomy | planning, memory, tools, feedback/evaluation | whether MxM addresses a different architectural problem |

## Strongest challenge found

Microsoft Agent Framework defines an Agent Harness as runtime scaffolding that turns a language model into an agent, drives model/tool calls, manages state/context, applies approval policies, and supports multi-step work. It accepts heterogeneous model clients and composes memory, modes, tools, middleware, approvals and observability.

Consequences:

1. Harness-neutral cannot merely mean provider-neutral.
2. Meta-harness must denote a demonstrable layer whose invariants survive replacement of the runtime harness itself.
3. The MxM paper should test at least two materially different runtimes/harnesses.
4. The six surfaces must prove useful semantics beyond convenient grouping.

## Candidate differentiators still alive

A. Six-surface normative decomposition. No source in this initial pass presented the same Mind/Morals/Mission/Memory/Methods/Means decomposition. This is a candidate compositional contribution, not a novelty finding.

B. Mind as an explicit architectural surface. The initial primary-source pass did not identify an equivalent first-class epistemic contract separating reasoning posture from procedural Methods. Deeper literature search is required.

C. Acceptance distinct from approval and execution. Existing frameworks provide strong pre-execution approvals. MxM's post-evidence Operator Acceptance may be materially distinct, but assurance/workflow prior art must be searched.

D. Evidence as governance substrate. Tracing is established. MxM must distinguish authoritative execution/verification/Acceptance evidence from telemetry and audit logging.

E. Runtime-harness replacement invariants. This is currently the strongest empirical discriminator.

## Current conclusion

The broad claim that MxM introduces governed agents is rejected. The narrower claim that MxM may contribute a portable normative meta-architecture above agent runtimes survives this initial pass. No novelty conclusion is warranted yet.
