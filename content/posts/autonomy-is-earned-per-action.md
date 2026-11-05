---
title: "Autonomy Is Earned Per Action, Not Granted Per Agent"
date: 2026-11-05T07:20:00-06:00
tags: [agents, governance, operations, agenticops]
description: "Komodor's November 4 survey shows agent fleets at scale and autonomy held back by blanket restrictions. The way forward is to promote individual actions to autonomous operation on the strength of their approval record, and to demote them automatically when that record breaks."
hero: "img/posts/autonomy-is-earned-per-action/hero.png"
hero_alt: "Navy and amber hero graphic with bold text: Autonomy Is Earned Per Action"
draft: false
---

The fleets are already here. [Komodor's 2026 Agentic Operations Survey](https://www.globenewswire.com/news-release/2026/11/04/3395406/0/en/komodor-survey-finds-more-than-50-of-engineering-organizations-face-control-and-governance-issues-as-they-scale-agentic-operations.html), released November 4 from responses by 1,000 engineering and technology leaders, found that nearly 84% run fleets of 10 or more operational agents. The leading uses are production work: self-remediation and AI SRE at 44.2%, incident investigation at 43.2%.

The control picture has not kept up. Building safe guardrails was the most cited challenge at 53.6%, followed by governance and security at 50.4%, and 42.7% named insufficient visibility into agent permissions. And 75.7% hold autonomy back with restrictions: agents limited to read-only tasks, human approval required for changes, or automated actions confined to noncritical workloads.

I read that last number as a holding pattern, not a strategy. Those restrictions are real controls and I would keep most of them today. But a restriction applied to a whole agent has no exit. It says nothing about what the agent has to prove, action by action, before the restriction lifts. So the organization sits in one of two states: the agent asks about everything forever, or someone gets tired of asking and loosens the whole grant at once. Neither state is earned.

## The unit is wrong

An agent is not one risk. It is a bundle of actions with very different risks sitting behind one permission set.

Take a remediation agent. Restarting a stateless service that failed a health check is a bounded act with a clean test for success. Scaling a deployment during an incident changes cost and capacity. Editing a database record to close an incident can be hard to reverse and hard to detect if it was wrong. Under a per-agent setting, all three get the same treatment: all approved by a human every time, or all let loose together.

That is why the approval queues fill up with the easy cases. The operator reviewing a routine restart for the fortieth time is spending attention the database edit needed. I made the related point in [Approval Is Not a Control](https://blog.thinxai.net/posts/approval-is-not-a-control/): an approval only counts if the approver had the evidence and the attention to catch the bad case. Blanket approval wastes both on the actions that stopped needing review weeks ago.

## Promote the action

Make autonomy a property of an action, where an action means the operation, the class of target, and the conditions under which it runs. Restart this class of service, when the health check fails in this way, inside this environment. That action keeps an approval record: what the agent proposed, whether the human approved it as proposed, corrected it, or rejected it, and whether the outcome check passed afterward.

Promotion then becomes a rule written in advance, not a judgment call made under schedule pressure. An action graduates to running without per-instance approval when its record shows a set number of consecutive approvals without correction, all inside its declared bounds, with outcome checks passing. Pick the number before the pilot starts. Twenty clean runs is a defensible start for a reversible action. An irreversible one may never graduate, and writing that down is also a decision worth having on record.

Graduation is not freedom. The action still runs under its identity, its budget, and its declared bounds, and its runs still get logged and sampled. What changes is the human's job: from approving each instance to reviewing the record, the exceptions, and the outcome rate. That is a review a person can actually do well.

Demotion has to be automatic, or promotion means nothing. The action drops back to approval on the first corrected proposal, the first failed outcome check, or the first run outside its conditions. No meeting, no discretion. And a change to the agent itself resets the record for its actions: new model, new instructions, new tool set, new memory policy. As I argued in [The Agent You Approved Is Not the Agent Running](https://blog.thinxai.net/posts/the-agent-you-approved-is-not-the-agent-running/), approval attaches to a version. A changed agent has not earned anything yet. Its actions start accumulating a record again from zero.

## The record has to exist first

None of this works on the visibility the survey reports. If 42.7% of organizations cannot see agent permissions clearly, they cannot build a per-action record, because they do not know which actions are running, under which grants, against which targets. The first work is unglamorous: an inventory of actions, not just agents, drawn from logs and grants rather than from vendor dashboards and self-reports.

Spending makes the same point from the other side. In the same survey, 68.4% of respondents spend at least $10,000 a month on AI agents and 38.4% spend $50,000 or more, while a quarter rank poor cost visibility and spending limits among their top challenges. An action-level record is also where cost belongs: what this action costs per run, and what it saved or broke, is the evidence both for promotion and for keeping the action at all.

So the sequence I would run is plain. Inventory the actions your agents actually take. Put each one under approval with a record that captures corrections and outcomes, not just clicks. Write the promotion and demotion rules before the first action graduates. Then let the record, not frustration and not a vendor's autonomy setting, decide what runs on its own.

Autonomy is coming either way, because fleets of ten or more agents cannot be supervised one click at a time. The only choice is whether it arrives action by action, with evidence, or all at once the afternoon someone widens a grant to clear a queue. I know which of those two I want to explain after an incident.
