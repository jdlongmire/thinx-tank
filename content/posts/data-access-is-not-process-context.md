---
title: "Data Access Is Not Process Context"
date: 2026-10-21
tags: [agents, architecture, operations]
description: "Connecting an agent to enterprise data tells it what the records say. Process context tells it how work should flow, who owns each step, and what to do when the flow breaks."
hero: "img/posts/data-access-is-not-process-context/hero.png"
hero_alt: "Navy and amber hero graphic with bold text: Data Access Is Not Process Context"
draft: false
---

On October 20, ARIS launched Process Context for Enterprise AI. In [ARIS's October 20 announcement](https://uktechnews.co.uk/2026/10/20/aris-launches-process-context-for-enterprise-ai-reinforcing-position-as-the-essential-platform-for-ai-ecosystem/), the company describes the product as a layer that gives agents the business understanding they need to do work, not just access to business data. The research behind it was conducted by The Hackett Group in collaboration with ARIS. It surveyed 200 respondents at large and multinational organizations. Eighty-two percent agreed that process context is required for deploying AI agents. Only 21 percent reported comprehensive, real-time visibility into how work flows across their enterprise. Organizations using process context tools were more than five times as likely to report measurable return from their AI investments.

That last figure comes from a study done with the vendor selling the tool, so I read it as directional, not settled. The gap between the first two numbers needs no vendor help to matter. Most shops say agents need to understand how work flows. Few can show, in real time, how work actually flows today.

That gap explains a failure pattern I keep seeing in agent projects. A team connects an agent to the systems of record, gives it search, gives it a set of tools through Model Context Protocol, and calls it ready. The agent can read the ticket, the invoice, the change record, and the customer account. It can call the approved APIs. Then it does the wrong thing in a way that is locally correct. It advances a step that should have waited. It treats an exception as a standard case. It closes work that met the literal field check and missed the business rule sitting two steps upstream.

Data access tells an agent what a record says. Process context tells it what should happen next, under what conditions, and who answers for it.

ARIS puts the definition plainly in the announcement. Process context is the relationships between processes, people, systems, risks, and controls. In its product description, that becomes the processes, roles, systems, rules, risks, and controls that determine what should happen and under what conditions. An agent gets that context through MCP, the same channel that carries tool access. That delivery detail matters. Context that lives in a slide deck or a process manual nobody updates does not reach the agent at runtime. Context delivered as a governed service can be versioned, checked, and changed on purpose.

Consider a payment workflow. The record says a vendor invoice is approved and due. Data access stops there. Process context adds the rest. A vendor bank change inside the last ten days freezes payment until a person revalidates it. An amount over a threshold needs a second approver who is not in the same reporting line as the first. A duplicate check runs against invoices from the last ninety days, not just open ones. If any check fails, the work goes to a named queue with a named owner, not back to the requester with a polite note. An agent with only the record will pay a clean-looking invoice. An agent with the process will stop on the bank change, which was the point of the control.

None of this is new work invented for agents. It is the work enterprise architecture was supposed to produce and keep current. I laid out that structure in [Agentic Enterprise Architecture](https://blog.thinxai.net/posts/agentic-enterprise-architecture/) and made it concrete in [The Architecture Repository](https://blog.thinxai.net/posts/the-architecture-repository/): the repository as the authoritative record of how the enterprise is built and how it is supposed to run. Process context is what that record looks like from the agent's seat. If the repository holds strategy, architecture, roadmaps, and standards but cannot answer a runtime question about a live workflow, the record is an archive, not a control.

I made the control point from the other side in [The Governed Control System](https://blog.thinxai.net/posts/the-governed-control-system/). A control system needs a target state, a reading of the actual state, and a way to act on the difference. Process context carries the first two. The designed flow is the target. Process mining and execution data show the observed flow, including the shortcuts and workarounds people actually use. When the two disagree, I want the agent to work from a stated rule about which one governs, not to guess. Drift between designed and observed flow is not automatically a defect in the work. Sometimes the design is stale. The repository has to say which, and someone has to own that call.

So before I connect an agent to a workflow, I want five things written down for that workflow, in a form the agent can read at runtime.

1. The designed flow. Steps in order, the input and output of each step, and the condition that moves work from one step to the next.
2. The observed flow. How the work actually moved in recent cases, including skipped steps, rework loops, and manual fixes outside the system.
3. Ownership at each step. The role that owns the step, the role that can approve an exception, and the queue where stuck work lands.
4. The rules and controls at each step. Thresholds, separation checks, freeze conditions, and the records each control writes when it fires.
5. The definition of done and the exception path. What counts as complete, what counts as failed, and exactly what happens in each case, including who gets notified.

That is a short list, and most shops cannot produce it for their highest volume workflows without a week of interviews. That is the finding inside the Hackett numbers. The blocker is not model quality and it is not connector count. The shop does not have a current, readable account of its own work.

Three tests show whether the context you hand an agent is real.

First, the trace test. Pick one completed case at random and walk it through the context. Every step the case took should appear, with the rule that allowed it. A step that appears in the case and nowhere in the context means the context is partial. Second, the exception test. Pick one failed or escalated case and do the same. Exception paths are where invented behavior does damage, because the agent will fill a gap with a plausible action unless the path is written. Third, the currency test. Ask when the context last changed and what triggered the change. If the answer is a project date from last year, the context describes a workflow the business may no longer run.

Start narrow. Pick one workflow with volume, a clear owner, and a cost when it goes wrong. Write the five items above for that workflow only, deliver them to the agent as checked context at runtime, and run the three tests on real cases before the agent writes anything. That work is slower than adding another connector. It is also the work that decides whether the agent is operating inside your business or just reading its records at speed.
