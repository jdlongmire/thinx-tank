---
title: "Every Agent Needs a Budget"
date: 2026-09-24
tags: ["ai-finops", "agents", "enterprise-ai"]
draft: false
description: "Inference spend is moving from the innovation budget to the operating budget. The fix is not cheaper models. It is treating every agent like a cost center with a per-task budget it cannot exceed."
hero: "img/posts/every-agent-needs-a-budget/hero.png"
hero_alt: "Navy and amber graphic with a cost-per-task gauge and the headline Every Agent Needs a Budget"
---

The market forecasters are now projecting over $200 billion in agentic AI spend for 2026, up about 140 percent from last year, and roughly 40 percent of business applications are expected to carry task-specific agents by year end. Against that, the unit economics are still a side conversation in most shops: someone picked the model, the pilots worked, and the invoice from the API provider is a line nobody is watching.

I have watched this exact movie before. Cloud bills started the same way. A team spins up infrastructure for an experiment, nobody tags the resources, finance sees a number six months later that looks like a typo, and then everyone gets a lecture about tagging policy. The difference this time is that an agent does not sit idle waiting to be scheduled. It burns money per loop, per retry, per tool call, and it decides its own retry policy. If the harness does not enforce a budget, the agent will spend what it wants.

## The unit of work comes first

FinOps for AI starts where cloud FinOps started: pick the unit you are buying. For agents, the unit is the completed task. Not the token, not the call, not the session. The token is a cost input the way a kilowatt-hour is a cost input; the thing finance can actually reason about is what one completed unit of work costs.

That means three numbers per agent, measured in production:

1. Cost per completed task, including retries and tool calls, not the happy-path number from a demo.
2. Input and output token volume per completed task, because context bloat is where the money quietly goes.
3. Success rate per completed task, because a cheap agent that fails half the time and re-runs is not cheap. OpenAI's own evaluation playbook makes the same point: compare harnesses on expected cost per successful solve, not on raw capability scores.

If you cannot produce those three numbers for an agent, you do not have an operating expense you can manage. You have a blank check.

## Put the budget in the harness, not the policy doc

Here is where practitioners diverge from pundits. The pundit version says "establish AI spending guidelines." The practitioner version enforces the budget in code at the execution layer.

I have argued before for an [agentic execution control plane](https://blog.thinxai.net/posts/agentic-execution-control-plane/): a layer that sits between the agent and the tools and enforces policy per invocation. Cost enforcement belongs there as one more check alongside identity and permissions. In practice, that check does four things:

- Verifies proposed resource consumption against per-invocation limits (tokens, cost, wall time) before the agent runs.
- Rejects with an explicit budget-exceeded signal so the failure is observable, not silent.
- Routes the task to a cheaper model tier when the task profile fits, instead of defaulting to the frontier model for everything.
- Logs every completed task with its cost, so finance gets real data instead of estimates.

The budget-exceeded rejection matters more than it looks. When an agent blows its budget silently and succeeds, the organization learns that overspending works. When it fails loudly, the owner fixes the loop or raises the budget with a written justification. That feedback loop is the entire discipline in one mechanism.

## Route by economics, not by habit

Most agents I see in the wild run on the best available model for every step, because someone set the default once and moved on. That is the expensive habit to break. The corpus evaluation work I have run internally prices decisions by cost per thousand and tracks control-plane calls per completed task precisely because model choice is the single largest lever on unit cost.

The practical pattern is tiered routing: a small, cheap model for classification, routing, and first drafts; a mid-tier model for the working loop; the frontier model only for the steps where its judgment actually changes the outcome. You find those steps by testing, not by guessing. And when model vendors shift to per-outcome or per-resolution pricing, as several are doing now, the routing layer is also where you compare whether the outcomes are worth the prices.

One caution, grounded in real data: Menlo Ventures found only about 16 percent of enterprise deployments actually qualify as agents with plan-observe-adapt loops. Most are routing-based workflows with a model call in the middle. That is good news for FinOps, because a workflow with a fixed path has predictable cost. The wild spending lives in the true agents with unbounded loops. Put the strictest budgets on the unbounded ones.

## What to do this quarter

If your shop has agents in production, four steps:

First, instrument before you optimize. Log cost per completed task for every agent for two weeks. You will be surprised which ones are expensive, and it will not be the ones you guessed.

Second, set per-task budgets in the harness with hard rejection on overrun. Start generous, tighten quarterly. The point is the mechanism, not the number.

Third, tier your model routing. Move the deterministic steps off the frontier model. Measure the quality delta, not the capability claim.

Fourth, report AI spend to the agent's business owner monthly, next to the outcome metric the agent exists to move. An agent whose cost per completed task is rising while its outcome metric is flat is a candidate for retirement or redesign, not a sacred cow.

## The budget is the governance

I spent two posts this week arguing that AI needs internal-controls discipline modeled on SOX: named humans, documented controls, independent review. FinOps is the same discipline pointed at money instead of risk. The questions are the same: who owns this, what is it allowed to spend, who checks the books.

Agents that can hold payment credentials and transact, which several vendors shipped this year, make this more than an accounting exercise. An agent with a credit card and no budget is not a productivity tool. It is an unauthorized purchasing department. The sooner the budget lives in code, the less of this work ends up as policy archaeology after the invoice lands.
