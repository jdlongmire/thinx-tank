---
title: "Route by Outcome, Not by Token"
date: 2026-11-10T07:20:00-06:00
tags: [ai-finops, agents, governance]
description: "Model routing is an economic and governance decision. The unit that matters is cost per accepted outcome, and routes should earn their traffic on that record, including the open-weight tier."
hero: "img/posts/route-by-outcome-not-by-token/hero.png"
hero_alt: "Navy and amber hero graphic with bold text: Route by Outcome, Not by Token"
draft: false
---

Most organizations route model traffic by habit. One default model handles everything, or the biggest model handles everything because nobody wants to be blamed for a weak answer. Then the bill arrives, or the failure rate does, and both look like surprises. They are not surprises. They are the predictable result of a routing decision nobody wrote down.

Routing is not a technical setting tucked inside a prompt. It is an economic decision and a governance decision. The model a task runs on decides what the work costs, what quality comes back, and how much rework I buy afterward. If that decision matters, it belongs on the record.

## The unit is cost per accepted outcome

Cost per token is the wrong unit. Cheap tokens that fail review are the most expensive tokens in the building. A route is economical only when its output passes verification without rework, and that makes the honest measure cost per accepted outcome: the full cost of the run, plus corrections, plus re-runs, divided by the work that actually cleared the bar.

The evidence for this is no longer theoretical. In [an Accenture study of routing and governing coding agents](https://arxiv.org/pdf/2609.28919v1), Abbasi, Aqrawi and Kwartler repriced about 10,000 real sessions and found that a cache-safe router recovered 14 to 21 percent of agentic model spend. The finding that matters more is the crossover: on long, tool-heavy sessions, the highest-priced model cost less per session than the next tier down in 51 to 80 percent of sessions over $100, because it re-read cached context instead of rebuilding it. List price said one thing. Cost per session said the opposite.

Meta made the same point from the other direction yesterday. [i-scoop's report on Muse Ember](https://www.i-scoop.eu/muse-ember/), released November 9, notes that Ember costs exactly the same per token as two rival small models, yet costs about a third as much per task at the same score. Same sticker. Different route. Per-token pricing cannot tell those two apart, and per-token pricing is what most route tables still record.

## Route by task class, declared in advance

My own practice is simple enough to state as a rule. Frontier models go to novel, judgment-heavy work where the thinking is hard. Mid-tier models handle structured production work. Small, fast models handle classification, extraction, and the routing decisions themselves. I spend the top model where it earns its price, I protect usage headroom on volume work, and I treat a quota-constrained tool as the exception, not the default.

The tiers are wide now, which is why the habit costs so much. [Nadir's November 2026 pricing comparison](https://getnadir.com/blog/llm-api-pricing-june-2026-complete-comparison/), re-read from provider pages on November 2, puts list prices from $0.10 input per million tokens at the bottom to $10 at the top, with settled bands in between. A 100x spread means a routing mistake is not a rounding error. It is the budget.

Two failure modes follow directly. Route everything to the largest model and I burn budget on work a small model does cleanly. Route hard or sensitive work to a cheap model and I pay in rework and risk, which are just costs that arrive later wearing different clothes.

## Open-weight models are a tier, not a slogan

Open source and open-weight models belong in the route table as a tier in their own right. A self-hosted open-weight model changes the economics at the root: the per-token API price is replaced by infrastructure I own, so at sufficient volume the marginal cost of a run falls toward the cost of the hardware. Below that volume, a hosted mid-tier model wins outright. Both statements are true, and which one applies is a measurable property of my route record, not a position to argue from principle.

The published numbers show why it has to be measured rather than assumed. [LeanLM's self-hosting cost analysis](https://leanlm.ai/blog/self-hosting-llm-cost) found that published break-even estimates disagree by roughly 50x because they hide utilization and staffing assumptions, and that all-in self-hosting runs 3 to 5 times the raw GPU rental. [The Brief Script's private-LLM cost guide](https://thebriefscript.com/private-llm/) puts self-hosted Llama 3.3 70B break-even against a premium API at about 10 billion tokens a month on owned hardware, and finds it never breaks even against cheap hosted endpoints serving the same class of model. Against a premium API at high sustained volume, self-hosting flips the curve. Against a hosted open-weight endpoint, it may never flip. The route record is where I find out which case I am in.

Open weights also buy a property no API tier can sell: the work stays in-boundary. Sensitive or regulated task classes can run on models inside my own walls, which is the same property offline-capable enforcement depends on. The trade is honest and I name it plainly: I inherit model operations (serving, updates, evaluations), quality varies against the frontier APIs, and license terms differ by model family, so the license is part of the route decision. None of that changes the discipline. An open-weight route earns its traffic on its approval and outcome record, same as any hosted route.

## Routing rules are policy

Because routing is policy, it belongs in the fabric, not in individual prompts. Declared, versioned, and changed on the record, as I described in [The MxM Fabric Defined](https://blog.thinxai.net/posts/the-mxm-fabric-defined/). When a vendor reprices, renames, or retires a model, the route table is what absorbs the change. A prompt buried in one application cannot.

Repricing is not hypothetical. The same [Nadir comparison](https://getnadir.com/blog/llm-api-pricing-june-2026-complete-comparison/) reports a Gemini tier listed at $2 input and $10 output through November 30 that doubles to $4 and $20 on December 1. It also reports threshold cliffs: requests that cross a long-context line get repriced as a whole, at two times the input price in one family and five times in another. Silent drift is not only a provider changing what sits behind a model name. It is also a workload crossing a threshold nobody decided it should cross. A declared route table with dated prices catches both. Habit catches neither.

Budgets attach the same way, to agents and actions, not just to accounts. In [Autonomy Is Earned Per Action, Not Granted Per Agent](https://blog.thinxai.net/posts/autonomy-is-earned-per-action/), I cited the Komodor survey figures: 68.4 percent of organizations spend at least $10,000 a month on agents, 38.4 percent spend $50,000 or more, and poor cost visibility ranks among the top complaints. The action-level record is where cost per run belongs, next to approvals and outcome checks. One record, three questions answered at once: what did it do, was it allowed to, and what did the accepted result cost.

## Routes earn their place

The closing rule is the same one I apply to actions. Measure cost per accepted outcome per route. Promote the routes whose record is clean. Demote or retire the ones whose savings dissolve into corrections and re-runs. A routing change is a behavior change: it resets the evidence, it does not inherit it. A new model behind an old route name starts proving itself from zero.

Write the route table down this week: task class, tier, model, dated price, and the outcome record that justifies the traffic. If a route cannot point to its record, it is not a route. It is a habit with an invoice attached.
