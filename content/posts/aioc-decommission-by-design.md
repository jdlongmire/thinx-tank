---
title: "Decommission by Design"
date: 2026-09-27
tags: ["ai-governance", "agents", "architecture"]
draft: false
description: "AIOC, my AI Operations Center architecture, treats agent decommissioning as a control-plane property: desired-state reconciliation, a registration contract with lifecycle state, and a grant model that revokes. The off switch is not a process. It is architecture."
hero: "img/posts/aioc-decommission-by-design/hero.png"
hero_alt: "Navy graphic with amber text reading 'Decommission by design'"
---

Yesterday I argued that [nobody can fire an agent](https://blog.thinxai.net/posts/nobody-can-fire-an-agent/): Dataiku's survey of 685 global CIOs found 81% have lost oversight of their own AI agents, and the missing piece is a decommission discipline. An owner with off-switch authority. Kill criteria written down at birth. A shutdown runbook. Three decisions per agent, made before it ever runs.

The pushback I expected was that this is more process layered over sprawl. That is the wrong reading. The three decisions are not a form to fill out. They are a description of what an operations architecture for agents has to contain. I built one: the AIOC, the AI Operations Center. Its whole bet is that governance has to be a property of the control plane, not a procedure taped onto a fleet nobody can see. This post maps the three decisions to the architecture.

The timing is not accidental. Last week [Palma.ai raised $1.8M to build a shared permissions and audit layer for agents across enterprise tools](https://runtimewire.com/article/palma-ai-raises-1-8m-agent-governance-patrick-eden), and [meshIQ launched AgentIQ as an in-flow governance layer inside agents' execution loops](https://www.morningstar.com/news/accesswire/1225126msn/meshiq-launches-agentiqtm-as-an-autonomous-trust-layer-to-help-enterprises-govern-ai-agents). The market has decided that governance-over-sprawl is a category. The question is where the governance lives. A vendor checkpoint at the door is a start. A control plane that owns the lifecycle is the finish line. Here is how AIOC is designed to get there.

## The owner is a policy principal, not a name on a wiki

The decommission discipline demands one named human who can shut an agent down without asking permission. In AIOC, that authority is expressed in the policy and grant model, not in a spreadsheet of owners.

The model works like this. Identity and claims from OAuth/OIDC inform authorization; they do not replace it. Agents are replaceable managed resources, selected through governed capability routing, and the grants that let an agent act can be revoked by policy. One named principal holds the authority. Firing the agent is a policy action: revoke the grant, withdraw the route. Not a 2 a.m. manual deletion of a key nobody documented. The off switch is a function the control plane exposes, with a named operator authorized to call it.

This is the same instinct behind the [execution control plane piece](https://blog.thinxai.net/posts/agentic-execution-control-plane/), where destructive operations are denied by default unless routed through a formal workflow. Decommissioning an agent is a destructive operation against your own systems. The architecture treats it that way.

## Kill criteria are registered at birth, drift is detected at runtime

The second demand: write down the outcome metric, the cost ceiling, and the review date before the agent ships. In AIOC this is the capability registration contract. Every agent registers identity, purpose, owner, version, allowed principals, permitted data classes, permitted actions, cost, evidence requirements, and lifecycle state before it ever runs.

That is the birth certificate with the death criteria built in. Owner, purpose, cost ceiling, permitted actions are declared up front, in the same record the control plane reads when it routes work to the agent. The kill criteria are not a separate document that drifts from the running system. They are the contract the running system is bound to.

The second half is desired state versus observed state, reconciled continuously. Enterprise Git holds the declared desired state: what is supposed to be running, with what config, under whose authority. Runtime systems report the observed state. AIOC reconciles the two and records conformance, drift, exception, and reconciliation evidence as a standing property. An agent running that is not in the declared desired state is drift, and the architecture flags it by itself.

This is the inventory reconciliation the last post called for, except it never stops. You do not reconcile the fleet once a quarter and act surprised at the gap. The control plane holds the declared state and the observed state side by side all the time. A blown cost ceiling or a drifted outcome is not a surprise discovered in a spreadsheet review. It is a kill condition the architecture is built to act on.

## The shutdown runbook ends in evidence

The third demand: a shutdown runbook. Revoke credentials, rotate the shared ones, remove data access, archive the logs, file the final inventory entry, confirm nothing depended on the output. In AIOC this is the canonical runtime contract, and it ends where most pipelines stop early: at evaluation.

The contract runs intent to authenticate to authority to classify to policy to capability to route to execute to observe to assure to record evidence, and then to evaluate the outcome. The lifecycle has an evaluation gate at the end. The evidence-producing property means the record survives the retirement: what was intended, what ran, under whose authority, with what resources, with what result.

[I made the case for the incident log earlier this week](https://blog.thinxai.net/posts/publish-your-own-incident-log/). The final log entry of a retired agent is the other side of that ledger. AIOC's bet is that the log entry should not depend on a disciplined human writing it down at 2 a.m. The architecture records the evidence as part of the shutdown workflow, so the retired agent leaves its record behind as a matter of course, not a matter of diligence.

## Governance has to be a property, not a procedure

The [SOX-for-AI framework](https://blog.thinxai.net/posts/sox-for-ai/) laid out inventory, ownership, controls, and audit as the enterprise posture for agents. Decommissioning is the end of that lifecycle, and the whole argument of this week is that it cannot live in process alone. Process layered over sprawl is what the survey measured: 83% of CIOs without standardized lifecycle management, 47% decommissioning agents in the dark this year.

AIOC is my architecture for the other approach. Register the agent with its death criteria. Reconcile declared state against observed state continuously. Revoke by policy. Record the evidence as a property of the workflow. The decommission discipline I described yesterday already exists in that architecture. It is not a form. It is a control plane.

The fleet will get bigger. Build the control plane before it does.
