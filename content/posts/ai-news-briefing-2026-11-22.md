---
title: "AI News Briefing: November 22, 2026"
date: 2026-11-22T06:00:00-06:00
tags: [llm, defense, governance, security]
description: "The Claude assisted Riemann proof is certified by the Lean and Mathlib communities, METR puts frontier models at forty hour expert tasks, and agent security failures at OpenAI and Together AI show why permissions matter."
hero: "img/posts/ai-news-briefing-2026-11-22/hero.png"
hero_alt: "Navy and amber hero graphic with bold text: AI News Briefing, November 22, 2026"
draft: false
---

{{< audio src="/audio/ai-audio-briefing-2026-11-22.mp3" >}}

## Executive summary

- The Lean and Mathlib communities jointly certified the Claude assisted Riemann Hypothesis proof, a 17 million line Lean library. The rival all human draft on the generalized problem was called invalid.
- METR reports frontier models, including GPT-6 Astra and Claude Opus 5.5, now complete research tasks equal to about 40 hours of expert human work, up from 16 hours six months ago.
- OpenAI had a 211 minute outage on November 21, with failures peaking at 75 percent, after both authentication database replicas crashed during maintenance.
- Together AI disclosed that an AI coding agent committed a credential that opened a private repository and exposed months of customer prompts.
- Anthropic rolled Claude Computer Use into beta for Team and Enterprise plans, and stricter US export controls are forcing Chinese firms to cancel Nvidia GPU contracts.

## The Riemann proof moves from claim to certified

Yesterday this was a claim awaiting a check. [The Context's November 22 briefing](https://thecontext.dev/en/topics/developer-tools/) reports that the Lean and Mathlib communities jointly certified Levent Alpoge's proof, a 17M-line Lean library, and that the rival all human draft on the generalized problem was called invalid. The Economist is reporting that AI may have solved the most important open problem in mathematics.

What it means for the AI industry: a certified formal result is a different kind of evidence than a benchmark score. Labs will compete on checked artifacts, not only on announced ones.

What it means for Defense: require the check, name who performed it, and record the state before a result enters a decision.

Source: [The Context, AI Frontier Daily Briefing for November 22](https://thecontext.dev/en/topics/developer-tools/).

## METR: frontier models now handle 40 hour expert tasks

AI safety evaluator METR reports that frontier models including OpenAI's GPT-6 Astra and Anthropic's Claude Opus 5.5 can now complete research tasks equal to roughly 40 hours of expert human work, doubling the 16 hour figure from six months ago. METR notes that reasoning and judgment remain limited.

What it means for the AI industry: the unit of work an agent can be trusted with more than doubled in half a year. That changes pricing, staffing, and product design.

What it means for Defense: longer tasks mean longer unsupervised runs. Review points, logging, and stop conditions have to be designed for 40 hour work, not 40 minute work.

Source: [Horizon AI Briefing for November 22, reporting METR via AI Times](https://horizon.alchemylab.sh/briefing).

## OpenAI outage: 211 minutes, failures at 75 percent

On November 21, OpenAI went through a 211 minute incident in which request failure rates peaked at 75 percent across ChatGPT and the API. Scheduled database maintenance was the trigger: both PostgreSQL read replicas behind the authentication gateway crashed at the same time. Engineers restored service by provisioning replacement replicas and retuning connection pooling.

What it means for the AI industry: the failure was not in a model. It was in ordinary authentication infrastructure, and every product built on one provider felt it at once.

What it means for Defense: single provider agent stacks carry this risk by design. A fallback path and a degraded mode are part of the system, not extras.

Source: [AI Briefing, November 22](https://aibriefing.dev/).

## Together AI: a coding agent committed the credential

In a November 21 disclosure, Together AI said an AI coding agent working on its public GitHub repository committed a credential. That credential opened a private repository and exposed months of customer prompts.

What it means for the AI industry: coding agents with repository write access are now a supply chain surface. Credential scanning has to treat agent commits as untrusted by default.

What it means for Defense: any agent touching code or data gets scoped access, short lived credentials, and a human gate on anything that leaves the boundary.

Source: [AI Briefing, November 22](https://aibriefing.dev/).

## Claude Computer Use reaches Team and Enterprise

Anthropic's November 20 release notes add Computer Use in beta for Team and Enterprise organizations, rolling out gradually. Inside Claude Desktop, Claude can see the user's screen and operate desktop apps the user allows. The release ships alongside Claude Code 2.1.329, which adds task visibility, expanded MCP server support, and broader Code Mode.

What it means for the AI industry: the desktop itself is becoming an agent surface. The contest moves from chat quality to control, permission, and audit.

What it means for Defense: that surface should stay off managed machines until allow lists, session recording, and revocation are proven in a pilot. Convenience is not a control.

Source: [AI Briefing, November 22](https://aibriefing.dev/).

## Export controls force Chinese firms to cancel GPU contracts

Stricter US export restrictions are disrupting major Chinese AI firms, including Moonshot AI, Tencent, and Alibaba, forcing them to cancel overseas Nvidia GPU contracts and delay model development timelines.

What it means for the AI industry: access to compute is now set as much by export law as by purchase orders, and two separate hardware stacks are forming.

What it means for Defense: expect wider gaps between allied and Chinese model release cycles. Plan evaluations on the assumption that the other side's timeline has slipped, not stopped.

Source: [Horizon AI Briefing for November 22, reporting AI Times and the Wall Street Journal](https://horizon.alchemylab.sh/briefing).

## An observation from my own work

In my own formal work I keep proof status in separate states for a reason: produced, checked, and accepted are not the same thing, and the record has to say which one you hold. The Riemann story just moved from the first state to the second, and that move is the news. The same discipline runs through the rest of today. I have argued that an agent should hold only the minimum permission for the current task, and that a child grant should never exceed its parent. Together AI's disclosure is that rule ignored, with the expected result. State what you hold. Show how it was checked. Scope what an agent can touch.

## What to watch

Independent reaction to the Riemann certification. Whether METR's 40 hour figure holds under outside testing. And what Together AI changes in agent repository access after its disclosure.
