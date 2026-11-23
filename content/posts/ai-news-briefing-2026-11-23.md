---
title: "AI News Briefing: November 23, 2026"
date: 2026-11-23T06:00:00-06:00
tags: [llm, governance, agents, defense]
description: "OpenAI publishes its internal intelligence measure and warns about the next capability window, outside evaluators move inside a frontier lab, and agents gain the ability to move real money under new standards work."
hero: "img/posts/ai-news-briefing-2026-11-23/hero.png"
hero_alt: "Navy and amber hero graphic with bold text: AI News Briefing, November 23, 2026"
draft: false
---

{{< audio src="/audio/ai-audio-briefing-2026-11-23.mp3" >}}

## Executive summary

- OpenAI chief scientist Jakub Pachocki published the lab's internal intelligence measure on November 22: log perplexity has fallen below 0.8, and he expects transformative capability in the 0.68 to 0.70 window.
- OpenAI has begun embedded third party assessments, giving Apollo Research, METR, Transluce, and Goodfire standing access to evaluate its models from inside.
- Stripe Treasury now lets agents initiate fund transfers and vendor payments within customer set limits, with human approval by default and no reversal once a transfer begins.
- OpenAI, Anthropic, Google, and Microsoft are backing shared agent payment standards through the Agentic AI Foundation; agents have already made over 138 million payments through the x402 protocol.
- Sarvam AI released an open weight 105B model checkpoint under Apache 2.0 at $0.15 per million tokens, and Google DeepMind's Genie 4 world model is now generally available.

## OpenAI publishes its secret number, and a warning

On November 22, OpenAI chief scientist Jakub Pachocki published [OpenAI's "Perplexity and Intelligence" essay](https://www.youtube.com/watch?v=YpsHKp0ogpM), disclosing the lab's internal pretraining curve for the first time. Log perplexity, a measure of how well a model predicts the next token, fell from about 0.99 for GPT-3.5 to 0.91 for GPT-4 and below 0.8 today. At about 0.76, Pachocki says, the model began producing breakthrough results on open mathematics problems. He expects further transformative capabilities in the 0.68 to 0.70 window and admits he does not know what they will be. His proposal: frontier labs should agree on common limits and not cross them until monitoring catches up. Sam Altman publicly backed the proposal. The essay carries its own caveats: perplexity is hard to compare across labs and does not map directly onto useful tasks.

What it means for the AI industry: a shared measure with agreed limits would be the first real coordination point the labs have offered, and it gives buyers a named marker for the next capability step.

What it means for Defense: treat that window as a planning marker. Capability jumps may arrive on a schedule the labs themselves are now naming, and evaluation capacity has to be ready before the models are.

Source: [Coverage of the Pachocki essay and the week's agent payment news](https://www.youtube.com/watch?v=YpsHKp0ogpM).

## Outside evaluators move inside OpenAI

[Fruition's Frontier briefing for November 23](https://fruition.net/frontier/) reports that OpenAI has launched the first phase of embedded third party assessments. Apollo Research, METR, Transluce, and Goodfire now have standing access to evaluate model alignment, safeguards, and monitoring systems from inside the lab's process, rather than in one off audits after release. The limits are part of the record: Apollo and Goodfire are paid by OpenAI, OpenAI can redact findings, and the scope covers agreed claims, models, and time periods.

What it means for the AI industry: "independently evaluated" is becoming a checkable claim in enterprise procurement. Vendors' safety claims will increasingly be read against third party reports, and rival labs will be pressed to match the access.

What it means for Defense: this is the model to copy in acquisition. Continuous outside assessment with named scope beats a one time audit before award.

Source: [The Frontier, November 23, 2026](https://fruition.net/frontier/).

## Stripe lets agents move real money

Stripe Treasury now supports agent initiated fund transfers, currency conversion, and vendor payments within limits the customer defines. By default, agent refunds, payouts, and transfers need human approval. The catch sits in the terms: the customer is solely responsible for every action an agent starts, and once an outbound transaction has begun it cannot be cancelled or reversed. More than 24,000 businesses already use Treasury with agents for read only work; write access is the new step.

What it means for the AI industry: agent permissions on financial rails are now a shipping product surface, not a research topic. Buyers should pilot with tight limits.

What it means for Defense: the pattern transfers to any agent with spending or system authority. Preset limits, approval by default, and no assumption that a bad action can be recalled.

Source: [The Frontier, November 23, 2026](https://fruition.net/frontier/), and [coverage of the Stripe Treasury agent preview](https://www.youtube.com/watch?v=YpsHKp0ogpM).

## Agent payment standards win backing from the rival labs

[Reporting aggregated from CoinDesk](https://zippfeed.com/en-US/a/ai-agent-payment-standards-win-openai-anthropic-backing) says OpenAI, Anthropic, and other technology companies are backing shared standards for how agents communicate, verify identity, and make payments across systems. The Agentic AI Foundation, established under the Linux Foundation in December 2025, brings together rivals including Google and Microsoft. Its working groups are developing guidance on customer authorization, spending limits, identity verification, and emergency controls. Agents have already made more than 138 million payments through the x402 protocol, mostly small purchases of data and computing services, according to Chainalysis. Federal Reserve Governor Michael Barr has warned that agents could move deposits fast enough to trigger bank runs within minutes. The foundation's executive director is plain about the boundary: standards can make it provable who stood behind an agent, but legal liability remains a matter for contracts, regulators, and courts.

What it means for the AI industry: identity and authorization standards decide whose agents get trusted at scale. The payment rail is becoming an agent platform decision.

What it means for Defense: the same three questions apply inside the enterprise. Who stood behind the agent, what was it authorized to do, and who answers when it goes wrong.

Source: [Zipp, reporting CoinDesk, updated November 23, 2026](https://zippfeed.com/en-US/a/ai-agent-payment-standards-win-openai-anthropic-backing).

## Sarvam ships an open weight 105B checkpoint

[YourStory reports](https://yourstory.com/2026/11/sarvam-new-model-make-ai-assistants-cheaper-to-run) that India's Sarvam AI released Sarvam-105B-1711 on November 22, an updated checkpoint of its 105 billion parameter mixture of experts model, with the weights published for download under Apache 2.0. Sarvam reports an eight benchmark average of 73.9, up from 42.6 for the March release, at a blended $0.15 per million tokens, and a 4 bit build that fits a single workstation graphics card. The model targets customer support, voice agents, and agentic tasks, with strength in Indian languages. The benchmark figures are Sarvam's own.

What it means for the AI industry: capable open models at that price keep pressure on hosted pricing, and sovereign model efforts outside the US and China keep gaining ground.

What it means for Defense: a model that runs on one workstation card is an option for disconnected work where a cloud call is not available, subject to the usual evaluation before trust.

Source: [YourStory, November 22, 2026](https://yourstory.com/2026/11/sarvam-new-model-make-ai-assistants-cheaper-to-run).

## Genie 4 world model reaches general availability

[The Frontier](https://fruition.net/frontier/) reports that Google DeepMind's Genie 4, its interactive world model line, is now generally available. Genie generates playable, controllable environments in real time, and world models remain the leading candidates for synthetic training data for robotics and agents.

What it means for the AI industry: world models are quietly becoming infrastructure for embodied and agent training data. Simulation dependent pipelines have a new input to test.

What it means for Defense: synthetic environments for training and rehearsal are the obvious use. The evaluation question is whether skills learned in a generated world transfer to the real one.

Source: [The Frontier, November 23, 2026](https://fruition.net/frontier/).

## An observation from my own work

I have written before that you [govern the door, not the agent you do not own](https://blog.thinxai.net/posts/govern-the-door/): when an agent you cannot control reaches your systems, the controls that work are attribution, scope set before the action, and revocation that leaves a receipt. Today that argument stopped being a blog position and became a payments standard. Stripe's terms put the outcome on the customer. The Agentic AI Foundation's working groups are writing down authorization, limits, and emergency controls. The order of operations is the whole game: identity and limits first, money movement second. Any enterprise that reverses that order will learn the same lesson at transfer speed, with no reversal available.

## What to watch

Whether Anthropic and Google match OpenAI's embedded evaluator access. The first incident report from an agent initiated payment. And independent checks of Sarvam's benchmark claims.
