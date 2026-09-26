---
title: "Nobody Can Fire an Agent"
date: 2026-09-26
tags: ["ai-governance", "agents", "operations"]
draft: false
description: "Dataiku surveyed 685 global CIOs and found 81% have lost oversight of their own AI agents. The missing piece is not monitoring. It is a decommission discipline: an owner, kill criteria, and a shutdown runbook for every agent that ships."
hero: "img/posts/nobody-can-fire-an-agent/hero.png"
hero_alt: "Navy graphic with amber text reading 'Nobody can fire an agent'"
---

Two days ago Dataiku published its Global AI Confessions Report, a Harris Poll survey of 685 global CIOs, and the numbers read like a confession in the literal sense. 81% say they have lost oversight of their own AI agents. 83% lack standardized agent lifecycle management. 47% have already decommissioned more than 20 agents this year, largely in the dark, with no standard process for doing it.

The rest of the survey fills in a specific kind of ugly. 67% of CIOs estimate 51 or more agents are running in production, and 90% say they are confident they have complete tracking of all of them. But 72% cannot consistently confirm whether those agents are delivering the business outcomes they were built for, and only 21% have full, near-real-time visibility into AI costs with attribution by business unit, team, or use case.

So the fleet is tracked but not known. That is the sentence to sit with. The CIO can tell you the agents are running. The CIO cannot tell you what they cost by owner, whether they still do what they were built for, or whether it is time to turn one off. Dataiku's CEO put it the way vendors put things: monitoring tells you an agent is running, managing tells you whether it has earned the right to keep running, and right now, almost nobody can fire an agent.

He is right about the diagnosis, whatever he is selling for the cure.

## The missing half of the lifecycle

This is the half of the SOX-for-AI framework I built [here](https://blog.thinxai.net/posts/sox-for-ai/) that nobody staffs: the end of the lifecycle. Inventory, ownership, controls, audit. Teams get the inventory half done, name owners on paper, and then the agent runs forever. Nobody sets the conditions under which it stops.

Software has called this lifecycle management for years and it means the same thing for agents: birth criteria, operating criteria, and death criteria. The first two get conferences. The third gets nobody. There is no ceremony for retiring an agent, no review, no one whose job includes shutting agents down. So they accumulate. The 47% of CIOs who killed 20 or more agents this year did it without a process, which means they did it the way you delete things at 2 a.m. when something breaks: by hand, under pressure, with incomplete notes.

[Yesterday I argued that every enterprise should keep its own incident log](https://blog.thinxai.net/posts/publish-your-own-incident-log/), one boring entry per event. Decommissioning is the other side of that ledger. An agent retired badly, scoped down quietly, or left running after its project ended is an incident waiting for a log entry. Every retired agent should get one final entry: what it did, why it stopped, which credentials were revoked, which data access was removed.

## What a decommission discipline looks like

This is not a new platform. It is three decisions per agent, made at birth:

- **An owner with off-switch authority.** Not a committee, not a platform team that needs three tickets to change a scope. One named human who can shut the agent down without asking permission. If firing the agent requires a change advisory board, you do not have an off switch. You have a discussion forum.
- **Kill criteria written down.** The agent exists to deliver a specific outcome at a specific cost. Write both down before it ships: the outcome metric, the cost ceiling, the review date. [I made the budget argument earlier this week](https://blog.thinxai.net/posts/every-agent-needs-a-budget/): every agent gets a budget, and a blown budget is a kill condition, not a rounding error. A drifted outcome is the other one. An agent that no longer does what it was built for is not a neutral presence. It is spend with no purpose and a credential nobody is watching.
- **A shutdown runbook.** The boring list: revoke its credentials and rotate the shared ones, remove its data access grants, archive its logs to the retention store, file the final inventory entry, confirm nothing else depended on its output. In [the execution control plane piece](https://blog.thinxai.net/posts/agentic-execution-control-plane/) I argued that destructive operations should be denied by default unless routed through a formal break-glass or decommission workflow. Shutting down an agent is a destructive operation against your own systems. It deserves the same rigor as deleting a volume: evidence the backup exists, a named approver, dual control where the blast radius is large.

None of this is exotic. It is what any serious team does for a database. Agents just arrived faster than the discipline around them.

## Start with the ones you cannot name

The survey says 90% of CIOs are confident they track every agent. Do not trust that number, including about yourself. The practical first move is an inventory reconciliation: list the agents you think are running, then pull the real list from API billing, token usage, identity providers, and platform dashboards, and reconcile the two. The gap between them is your actual fleet.

Every agent in the gap gets the three decisions, or it gets decommissioned. That sounds aggressive. It is cheaper than the alternative, which is what 47% of CIOs did this year: killing agents under pressure with no process and no record.

An agent fleet is a workforce. Every workforce needs hiring standards, and every workforce needs a termination policy. Enterprises wrote the first half in a hurry this year. The survey tells them what the second half looks like when you skip it: 81% standing in front of a fleet they cannot name, cannot cost, and cannot fire.

Write the termination policy before the fleet gets bigger. It will get bigger.
