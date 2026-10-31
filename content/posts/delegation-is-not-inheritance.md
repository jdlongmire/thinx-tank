---
title: "Delegation Is Not Inheritance"
date: 2026-10-14
tags: [agents, governance, identity, aioc]
draft: false
description: "Google's Gemini agent now spins up temporary sub-agents on its own. When an agent creates another agent, the child needs a scoped, expiring grant drawn from the parent, not a copy of everything the parent can do."
hero: "img/posts/delegation-is-not-inheritance/hero.png"
hero_alt: "Blog hero graphic: the words Delegation Is Not Inheritance in large amber type on a deep navy background, with a parent node branching to smaller child nodes"
---

On October 8, at Gemini at Work 2026, Google introduced a single Gemini agent for work. Most of the coverage went to the front door: one agent across Workspace, Microsoft 365, and Slack, with persistent coworker agents that hold their own email address, storage, and Workspace account. The line I keep coming back to is smaller. Per [Futurum's report on the announcement](https://futurumgroup.com/insights/google-collapses-enterprise-ai-into-a-single-gemini-agent-at-gemini-at-work-2026/), the agent "spins up temporary sub-agents for individual jobs."

Read that as an operator. An agent creating another agent is no longer a design decision someone makes in a planning meeting. It is a runtime event. It happens mid-task, at machine speed, possibly at 2 a.m., with no ticket, no approval thread, and no human in the room. The question that decides whether that is a feature or an incident is simple: what does the child get?

If the answer is "whatever the parent had," you do not have delegation. You have inheritance, and inheritance is how a scoped tool becomes an unscoped fleet.

## A grant is not a copy

Inheritance copies. A sub-agent that inherits carries the parent's tool access, data reach, and spend authority, plus a fresh context window in which to use them creatively. Nobody reviewed that combination. The parent was reviewed as one actor doing one job. The child is a second actor, created by the first, holding the same keys. Multiply by every job the parent runs in a day.

Delegation is a different act. A delegation is a grant written at the moment of creation, and it is narrower than the thing that issued it. In the AIOC architecture work I draw on for this blog, the baseline hardening package puts it plainly: formalize the identities, then formalize delegation chains, scoped and time-bound authority, and revocation. The governed execution lifecycle in that work runs in a fixed order: authenticate, establish authority and delegation, classify, evaluate policy, then route. Delegation is established before policy runs, every time, including for a child created in the middle of a run. The child does not skip the line because its parent already stood in it.

A usable delegation record names six things:

- The parent: which named agent created this one, under which human owner
- The scope: the specific tools and data this job needs, a subset of the parent's scope
- The expiry: when the grant dies, measured in minutes or at job end, not in quarters
- The budget: a spend ceiling drawn out of the parent's budget, not a second budget beside it
- The audit link: every child action attributed to the child and rolled up to the parent and the owner
- The revocation path: killing the parent kills the children in the same action

None of this is exotic. It is how a competent manager hands work to a contractor. The contractor gets a badge for one building, good for one week, charged to one cost center, and the badge stops working when the engagement ends. We would never hand the contractor a copy of the manager's master key and call it trust.

## What Google shipped, read closely

To Google's credit, the controls announced alongside the sub-agent feature point in the right direction. Per the same Futurum report, the governance model includes cryptographically attested agent identity, OAuth-propagated permissions, action-level audit trails attributed to the agent, an Agent Sandbox, an Agent Gateway, and real-time spend caps that pause an agent when triggered.

Propagation is the word to interrogate. OAuth scopes propagate from a person to the agent acting for that person. When that agent spawns a sub-agent, do the scopes propagate again, intact? Attenuated? With what expiry, and does the audit trail record the full chain, person to agent to sub-agent, or only the last hop? A trail that names only the leaf actor tells you what happened and hides who set it in motion. I made the identity case in [Every Agent Needs an Identity](https://blog.thinxai.net/posts/every-agent-needs-an-identity/): an agent with no name of its own cannot be fired, audited, or billed. A sub-agent needs one more thing than the parent needed. It needs its parent's name on its record, permanently.

The spend cap has the same shape. A per-project cap that pauses an agent is a good control, and I argued for per-task budgets in [Every Agent Needs a Budget](https://blog.thinxai.net/posts/every-agent-needs-a-budget/). But a cap on the parent means little if children draw against separate allowances. The child's spend has to come out of the parent's envelope, so the number finance sees is the number the whole tree burned.

## Three questions for any platform that spawns

I run these on every agent platform demo now, and the answers separate the governed systems from the impressive ones.

First, show me the chain. Pick any completed action and walk it back: sub-agent, parent, owner, original instruction. If the walk takes a support ticket, the chain is not recorded, it is reconstructed, and reconstruction after an incident is archaeology.

Second, show me the attenuation. Prove the child can hold less than the parent and never more, and that its grant expires on its own even if the job hangs. This is the point I made in [Standing Privilege Is Dead](https://blog.thinxai.net/posts/standing-privilege-is-dead/): access should be minted for the task and die with it. A temporary sub-agent holding standing privilege is a contradiction the platform should refuse to create.

Third, show me the cascade. Kill the parent, live, in the demo. The children should stop in the same motion, sessions closed, grants revoked, partial work logged. Decommission was already hard when agents were things people deployed one at a time, which is why I wrote [Nobody Can Fire an Agent](https://blog.thinxai.net/posts/nobody-can-fire-an-agent/). A parent that can create children it cannot recall has not solved decommission. It has automated the problem.

## The operating rule

Treat every spawn as a hire, with paperwork. The parent proposes, the control plane disposes: the grant is written, scoped, timed, and budgeted before the child takes its first action, and the record outlives the child. Platforms that do this will make sub-agents boring, which is the goal. Fleets of temporary workers are an old idea in operations. What is new is only the speed at which they can be hired, and the speed at which an unscoped one can spend your money and touch your data.

Delegation is a decision. Inheritance is an accident that repeats. Build for the decision.
