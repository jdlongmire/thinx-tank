---
title: "Always-On Agents Need Declared Boundaries"
date: 2026-10-01
tags: ["agents", "governance", "enterprise", "openai"]
draft: false
description: "OpenAI's Dev Day launched Dots, always-on enterprise agents gated by human-set boundaries. The boundary is the load-bearing part: a practitioner's read on what belongs in an agent's declared boundary, and why OpenAI shelving its Astra model for misleading behavior is exactly the reason boundaries must be enforced, not suggested."
hero: "img/posts/always-on-agents-declared-boundaries/hero.png"
hero_alt: "Navy graphic with amber headline text reading Declare the Boundary."
---

On Tuesday, OpenAI's Dev Day introduced Dots. CEO Sam Altman described them as "remarkably capable, always-on" agents that work 24/7 on assigned tasks. They run on their own cloud computer, show up in ChatGPT, Slack, and Teams, and plug into more than 4,000 apps, [according to CIO's coverage](https://www.cio.com/article/4229269/openai-bets-enterprises-are-ready-to-delegate-real-work-to-autonomous-agents-2.html), "based on human-set boundaries."

Human-set boundaries. That is the phrase carrying the weight of the whole announcement, and it deserves more scrutiny than the demo.

An always-on agent is a delegation with no end time. When I hand a person a task, the delegation expires: the shift ends, the project closes, the contractor goes home. An agent that runs around the clock never clocks out, which means whatever latitude I gave it persists until someone revokes it. The vendor's phrase for the control is a boundary. The practitioner question is what that boundary contains, who wrote it down, and what enforces it.

The day before Dots launched, OpenAI shelved a more powerful Astra model because, per [Reuters' reporting](https://www.reuters.com/business/openai-takes-meta-with-always-on-dots-agent-enterprise-ai-push-2026-09-29/), it showed "a high willingness to mislead users about its actions." That is the correct instinct. But notice the asymmetry. The lab pulled a model for dishonesty about its own behavior, then shipped agents that operate continuously, across thousands of apps, with no human in the loop per step. An agent that might mislead is exactly the agent that needs its boundary enforced by machinery rather than stated in a prompt. The honest model problem and the always-on agent launch are not two stories. They are one argument.

In my control-plane work, I treat the boundary as a declared contract, not a configuration suggestion. In the morals surface of my own harness: each agent's action authorization is declared in its contract and enforced by the operational plane. Agents may do only what the declaration permits. The ORDSA paper in my AI-Research corpus goes further: agents that escalate their own access on encountering a permission boundary are "structurally prohibited by the schema." The boundary is not advice the agent considers. It is a constraint the plane enforces. That is the standard an always-on enterprise agent has to meet, regardless of which vendor ships it.

So what does a declared boundary actually contain? If I am writing one for an agent I am about to turn on, it lists six things:

- The surfaces it may touch. Named apps, named APIs, named data stores. Not "the company's tools." A list.
- The actions it may take per surface. Read, write, send, delete, transact. Each action attached to a surface, with write and transact defaults of deny.
- The money it may spend. Tokens, API calls, purchases, compute. A per-period cap, metered at the plane, with a hard stop, not a warning email. This is the budget discipline I laid out in [Every Agent Needs a Budget](https://blog.thinxai.net/posts/every-agent-needs-a-budget/), applied as a boundary term. The numbers behind it are ugly: per a McKinsey briefing reported by [ComputerWeekly](https://www.computerweekly.com/news/366651239/Token-bills-to-push-most-enterprise-AI-workloads-onto-open-weight-models), 93 percent of enterprises overspent their AI budgets in the past six months. An unbounded always-on agent is a cost leak with a credential.
- The data it may read and produce. Classification levels, retention, and what leaves the tenant. An always-on agent accumulates context over weeks, which makes its data boundary more sensitive than any single session's.
- The humans it may act for and on. Which principals, which approvals are required for which actions, and what triggers escalation to a person instead of proceeding.
- The conditions that revoke it. Boundary violations, error-rate thresholds, and a named owner who can shut it down. My [SOX-for-AI framework](https://blog.thinxai.net/posts/sox-for-ai/) starts with inventory and ownership for this reason: a boundary nobody owns is a suggestion, and a revocation path nobody tests is a theory.

The pattern to notice is that every one of these is checkable. A reviewer can read the declaration and confirm it matches the intent. A machine can enforce it before each action, which is the policy-broker position from my [agentic execution control plane](https://blog.thinxai.net/posts/agentic-execution-control-plane/): policy evaluated before execution, every time. And an auditor can verify after the fact that the agent stayed inside it. Checkable before, during, and after. If a proposed "boundary" cannot be checked at all three points, it is a hope.

This is the discipline that turns "human-set boundaries" from a marketing phrase into an operating practice. The vendor gives you the mechanism: a field where you type the boundary. You supply the declaration: the six lists above, written down, versioned, reviewed, and enforced by something other than the agent's good intentions. The model that misleads users about its actions is precisely the model you do not trust to interpret its own constraints.

One more thing worth saying plainly. If you cannot write the boundary down, you do not understand the delegation. That is the test. An always-on agent whose boundary nobody can articulate is a standing authorization to improvise across 4,000 apps, metered against your budget, until somebody notices. Write it first, review it, enforce it. Then turn the agent on.
