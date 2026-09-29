---
title: "AgenticOps Is Here. Drift Is Too."
date: 2026-09-29
tags: ["agents", "agenticops", "oversight", "netops"]
draft: false
description: "Half of large IT shops already run agentic AI that acts in production, and a quarter are comfortable with no human in the loop. My February piece on drift said this exact failure was coming. Here is what to put in place before you grant autonomy."
hero: "img/posts/agenticops-drift/hero.png"
hero_alt: "Navy graphic with amber headline text reading AgenticOps Is Here. Drift Is Too."
---

Last week [Cisco published new research](https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2026/m09/cisco-ai-research-agenticops-scaling-quickly-in-the-enterprise.html) on agentic AI in network operations. The headline numbers are worth sitting with. Fifty-one percent of the surveyed organizations run agentic AI that acts in production today. Eighty-four percent expect an AI-led operating model within twelve months. And twenty-four percent are comfortable with agents acting with no human oversight at all.

The survey was conducted by Omdia across 1,000 IT and network operations leaders at organizations with 500 or more employees. It is not a fringe finding. It is the direction of the industry, stated plainly.

The last number is the one that should make you stop. A quarter of the people running production networks are ready to skip the human entirely.

## I wrote the warning in February

Earlier this year I wrote a piece on what I called the drift problem. The short version: a generative system maintains its confidence across a long session while its fidelity to the original objective quietly degrades. The prose keeps reading cleanly. The tone stays assertive. The substance migrates.

Scale that to agents and it gets worse. An agent drifts across steps the same way, and now it is taking actions, not just generating text. By step thirty it can be competently pursuing something meaningfully different from what it was tasked with. Nobody is watching closely enough to catch the shift, because the whole point of the agent was to run without close watching.

That was the theoretical case in February. Cisco's numbers are the deployment data arriving ahead of the oversight to match it.

## The oversight is being granted on credit

Read the rest of the Cisco findings and you see the gap. Eighty-six percent of respondents say a single integrated platform is the most effective path forward for overseeing agents. Sixty-nine percent require detailed explainability for agent-driven actions. People want the visibility half.

But the autonomy half is moving faster. Eighty-two percent are comfortable letting AI make at least some production network changes without prior human approval. Agents rerouting traffic, adjusting wireless parameters, isolating endpoints, resolving incidents end to end. The wish list includes the control plane. The deployment does not wait for it.

This is the same sequence error I have been writing about all month. [My SOX-for-AI framework](https://blog.thinxai.net/posts/sox-for-ai/) starts with inventory and ownership before anything else, because you cannot govern what you have not cataloged. [Nobody Can Fire an Agent](https://blog.thinxai.net/posts/nobody-can-fire-an-agent/) showed that most shops cannot even decommission the agents they already have. Now the industry wants to hand those same agents the production network with no human in the loop. The governance has to lead the autonomy, not chase it.

## What to put in place first

Before an agent gets autonomy over production systems, it needs all five of these. No exceptions.

An owner and a kill switch. Every agent has a named human accountable for it, written kill criteria, and a shutdown runbook that has been tested. I laid this out in [Decommission by Design](https://blog.thinxai.net/posts/aioc-decommission-by-design/). Autonomy without a documented kill path is just hope with an API key.

One place to see it all. The 86 percent in the survey are right about this. You need a [control plane](https://blog.thinxai.net/posts/agentic-execution-control-plane/) that records what each agent did, why, and with what authority, not twelve dashboards nobody has time to read. If the evidence lives in one place, drift gets caught. If it lives in six places, it does not.

Explainability with evidence, not narrative. A summary of what the agent did is not enough. You need the trace: the inputs it saw, the constraints it operated under, the decision points, the outcome. The Cisco quote I liked best in the announcement came from their own network platform lead: trust is "built on visibility into every decision, explainable context behind every recommendation, and guardrails that ensure deterministic outcomes." Visibility into the decision, not a story about it.

A budget per task. [Every agent needs a budget](https://blog.thinxai.net/posts/every-agent-needs-a-budget/): cost caps, step caps, time caps. A budget is a leash measured in dollars and iterations. When the cap trips, a human looks at what happened before the agent keeps going.

An incident log of your own. OpenAI published six of theirs. [Publish yours](https://blog.thinxai.net/posts/publish-your-own-incident-log/). Agents fail in patterns, and the only way to see the pattern is to write the failures down.

## The rule has not changed

The rule from the drift piece still holds: autonomy should be inversely proportional to decision consequence. Short leashes for high stakes. The more autonomous the agent, the lower the stakes it is allowed to touch.

Twenty-four percent of leaders are comfortable inverting that rule. They are betting that a system which cannot persist fidelity to its own purpose will somehow not drift when nobody is watching. It will. It always does. The only question is whether the oversight is in place to catch it at step five instead of step five hundred.

AgenticOps is coming. It is already in half the production environments in this survey. Build the control plane first, grant the autonomy after, and only as much as you can actually watch. Drift is already here too.
