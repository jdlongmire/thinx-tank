---
title: "Production Is Not a Result"
date: 2026-11-12T07:20:00-06:00
tags: [ai-finops, agents, operations, governance]
description: "Genpact finds 79 percent of enterprises have agents in production, but only 15 percent have fully tied AI investment to P&L outcomes. Deployment is an engineering state, and the missing discipline is a written outcome entry for every production agent."
hero: "img/posts/production-is-not-a-result/hero.png"
hero_alt: "Navy and amber hero graphic with bold text: Production Is Not a Result"
draft: false
---

Genpact published its *Autonomy in Practice* report today, built on a survey of more than 2,000 senior executives at companies with revenues from $1 billion to over $50 billion, across 17 industries and 14 business functions. The headline numbers in [Genpact's release](https://www.prnewswire.com/news-releases/79-of-enterprises-report-ai-agents-in-production-but-only-15-have-fully-tied-ai-investment-to-pl-outcomes-302937385.html) deserve to be read as a set, not separately. 79 percent of enterprises have AI agents in production. Just 20 percent use them broadly and consistently across functions. Only 15 percent have fully tied AI investment to P&L outcomes. And on average, just 49 percent of AI initiatives funded in the past 24 months delivered the value expected.

Read together, those numbers describe an industry that got very good at the first half of the job. Deployment works. Accounting does not.

## Production is an engineering state

An agent in production means specific things. It runs on real systems. It touches real data. It holds credentials, consumes budget, and produces output that other people and systems act on. Those are engineering facts, and they matter. I have spent months on this blog arguing that production agents need named identity, scoped permission, and a decommission path, because production is where the risk lives.

But production says nothing about value. A workflow can run every day, on schedule, inside its permissions, and still move no business line at all. The tickets close faster and the queue downstream grows by the same amount. The drafts get written and the reviewers spend the saved time fixing them. Activity is easy to count. The count is not the result.

That is what the 15 percent figure is really measuring. Tying investment to a P&L line is not a finance exercise bolted on after deployment. It is a claim, made in advance, that this workflow feeds this line, and a record that lets someone check the claim later. 85 percent of surveyed enterprises cannot make that check. They know what they spent. They do not know what it bought.

## Expected value that was never written down

The 49 percent figure bothers me more. Half the funded initiatives delivered the value expected. Expected by whom, recorded where, measured how?

In most funding processes I have seen, the expected value lives in a proposal slide. It is a range, or a headcount equivalent, or a percentage with no baseline under it. Nobody writes down the current cycle time, the current error rate, or the current cost per case before the agent starts, because the proposal is selling the future, not documenting the present. Two years later there is nothing to compare against. The initiative did not fail its target. It never had one in a form that could be checked.

This is the benefit side of a gap I covered on the cost side two days ago in [Route by Outcome, Not by Token](https://blog.thinxai.net/posts/route-by-outcome-not-by-token/). There, the unit was cost per accepted outcome: what a run cost, divided by the work that cleared review. The same discipline applies to benefits. A benefit claim needs an accepted outcome to attach to, a baseline to compare against, and a line owner who agrees the line moved. Without those three, value reporting is a narrative. Narratives always grade well.

## Gains leak across function boundaries

The 20 percent and 9 percent numbers explain where the value goes. Only 9 percent of respondents have completed significant operating model transformation. The rest deployed agents function by function, into workflows that were designed for people handing work to people.

An agent that speeds up one step in a chain does not speed up the chain. It moves the queue. Intake gets faster and review drowns. Drafting gets cheaper and approval becomes the constraint. Each function reports a local gain, and the P&L sees none of it, because the gain was absorbed by the next handoff. This is why Genpact's leading group, 17 percent of respondents, stands out for working across the enterprise rather than function by function, and for treating value capture as a P&L discipline with named owners. The pattern matches what I argued in [Redesign the Job Around the Agent](https://blog.thinxai.net/posts/redesign-the-job-around-the-agent/): the work around the agent has to be redesigned, or the agent's speed just relocates the bottleneck.

## The outcome entry

The fix is a document, and it is short. Before a production agent goes live, I want one page filed with the deployment record, holding six things:

- The workflow, and the named owner of that workflow.
- The P&L line the workflow feeds, named specifically enough that a finance reviewer can find it.
- The baseline, measured before the agent starts: cycle time, error rate, cost per case, or whatever the line actually tracks.
- The target, and the date it will be checked.
- The measurement source, which is the system of record, not the agent's own summary of its work.
- The retirement condition: what result, or absence of result, takes the agent out of production.

None of this is exotic. It is the same reconciliation habit I described in [Done Means Accounted For](https://blog.thinxai.net/posts/done-means-accounted-for/), applied at the level of the deployment instead of the task. There, the check was supplied resources against used resources at task close. Here, the check is claimed benefit against measured benefit at review. Same posture, longer clock.

Then run the review on the production calendar, not the funding calendar. Each cycle, every production agent's entry gets read against its line. Lines that moved keep their agents. Lines that stayed flat get an honest conversation about whether the baseline was wrong, the workflow was wrong, or the agent was never the constraint. Agents with no entry, or an entry nobody has read in two cycles, come out of production until someone files one. That last rule will do more for the 15 percent number than any new platform feature announced this year.

## Count the line, not the launch

Deployment counts will keep rising, and they should. Agents belong in production, doing real work under real controls. But a launch is an input. The P&L does not grade inputs.

If an agent cannot name the line it is supposed to move, the baseline it started from, and the date someone will check, it is not in production in any sense the business should pay for. It is in circulation. File the outcome entry before the next launch, and the 79 percent starts to mean something.
