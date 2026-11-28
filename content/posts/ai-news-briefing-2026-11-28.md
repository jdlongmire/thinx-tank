---
title: "AI News Briefing: November 28, 2026"
date: 2026-11-28T06:02:00-06:00
tags: [llm, agents, security, defense]
description: "Hackers breached the Air Force Cloud One platform and reportedly reached its control plane, the Bank of England warns that AI financing now tops four trillion dollars in exposure, and decision models get cheaper."
hero: "img/posts/ai-news-briefing-2026-11-28/hero.png"
hero_alt: "Navy and amber hero graphic with bold text: AI News Briefing, November 28, 2026"
draft: false
---

{{< audio src="/audio/ai-audio-briefing-2026-11-28.mp3" >}}

## Executive summary

- Reuters reports that hackers breached Cloud One, the Air Force flagship cloud platform, and that one source says the intruders reached its control plane. The scope is unknown and migrations to the platform are paused.
- The Bank of England's November Financial Stability Report puts hyperscaler bond sales above 305 billion dollars this year and total debt plus off balance sheet commitments above 4 trillion dollars.
- Liquid AI's d1.3-ultra ties for first on the Artificial Analysis Decision Index at 76.4, with a claimed cost about 60 percent lower per million tasks.
- Ant Group open sourced LingSante-3.1-flash, a 560 billion parameter medical model under the MIT license, and Sakana AI's 30 billion parameter Namazu Small beat a 120 billion parameter model on Sakana's own benchmark average.
- Poland signed a five year, roughly 300 million dollar deal for Palantir AI software, keeping all keys, servers, and information under Polish control.

## Hackers breach the Air Force cloud, and reportedly reach the control plane

[Reuters reported on November 27](https://www.reuters.com/world/hackers-breach-us-air-force-flagship-cloud-one-computing-platform-2026-11-27/) that hackers breached Cloud One, the Air Force's flagship cloud computing platform, in an intrusion discovered within the past month during upgrade work. Cloud One combines Microsoft, Amazon, Oracle, and Google services and carries scores of applications, including personnel, pay, and logistics systems, the Cloud-Based Command and Control system that collates air defense radar feeds, and a system that tracks bombs and missiles across more than 200 locations. One source told Reuters the intruders exploited a software vulnerability to reach the control plane, the layer Reuters likens to a universal remote, from which aircraft status or spare parts movement could in principle be checked. Reuters could not establish who the hackers were, the full scope, or whether data was stolen. The discovery has paused migrations of back office applications to Cloud One, blocked updates to applications already running there, and led to some administrator rights being revoked. Cyber Command is assessing the damage. The Air Force declined to comment on the security posture of specific systems.

What it means for the AI industry: shared cloud control planes are the highest value target on any platform, and AI tools that scan wide surfaces for flaws raise the speed at which they get attacked. Control plane monitoring is a product requirement now, not an add-on.

What it means for Defense: the supporting IT enterprise should treat control plane access as its own incident class, with separate monitoring, separate credentials, and a rehearsed plan for operating while the platform itself is distrusted.

Source: [Reuters, Hackers breach US Air Force flagship Cloud One computing platform](https://www.reuters.com/world/hackers-breach-us-air-force-flagship-cloud-one-computing-platform-2026-11-27/), November 27, 2026; cross-checked against [Vector Defense, November 28, 2026](https://vector.news/defense).

## The Bank of England prices the AI buildout as a financial stability risk

The [Bank of England's Financial Stability Report for November 2026](https://www.bankofengland.co.uk/financial-stability-report/2026/november-2026), published November 26, says hyperscaler bond issuance is set to exceed 305 billion dollars in 2026, about 8 percent of global investment grade issuance, and that total potential exposure, counting debt plus off balance sheet commitments such as leases and guarantees, is just over 4 trillion dollars. The Bank calls the financing increasingly complex, circular, and opaque, and warns that this deepens interconnections so stress in one area is more likely to spread to others. The same report notes that frontier AI capabilities keep growing, notably in agents and open weight models, and that recent incidents show how hard autonomous agents are to control.

What it means for the AI industry: the buildout now runs on credit markets. AI revenue expectations are load bearing for bond prices well beyond the tech sector, and a revision in those expectations would reprice far more than AI stocks.

What it means for Defense: defense AI programs ride on commercial cloud capacity that is debt financed. Capacity planning should carry a financing scenario, not just a technical one, and contracts should say what happens if a provider's cost of capital jumps.

Source: [Bank of England, Financial Stability Report, November 2026](https://www.bankofengland.co.uk/financial-stability-report/2026/november-2026), published November 26, 2026.

## A decision model ties for first at a lower claimed cost

[The Maivia Gazette reported on November 28](https://maivia-gazette.com/2026/11/28/liquid-ai-releases-d1-3-ultra-tying-bison-31b-on-a-decision-benchmark-at-a) that Liquid AI launched d1.3-ultra on November 27. The model ties Bison 31B for the top score, 76.4, on the Artificial Analysis Decision Index v2.1, a benchmark that measures decision making rather than conversation. Liquid AI says it costs about 60 percent less per million tasks; that claim is the company's and has not been independently verified. The d1 family returns calibrated probabilities in a single pass. This version adds ranked lists of options, reads text, images, and audio, and has a 64K token context, sold through Liquid AI's console and API for automated approvals, triage, and document processing.

What it means for the AI industry: decision models are a distinct category with a distinct unit price, cost per accepted decision. A tie at the top with a lower claimed cost puts price pressure on every general model doing approval and triage work today.

What it means for Defense: high volume screening, logistics triage, and document routing are natural fits, provided each automated decision carries an audit record and a reversal path. A probability without a record is not a decision system.

Source: [The Maivia Gazette, Liquid AI releases d1.3-ultra](https://maivia-gazette.com/2026/11/28/liquid-ai-releases-d1-3-ultra-tying-bison-31b-on-a-decision-benchmark-at-a), November 28, 2026, reporting the November 27 launch.

## Ant Group open sources a 560 billion parameter medical model

[MarkTechPost reported on November 28](https://www.marktechpost.com/2026/11/28/ant-group-lingsante-3-1-flash-open-source-medical-ai/) that Ant Group's Afu team open sourced LingSante-3.1-flash, a medical model with 560 billion total parameters, about 25 billion active per token, a one million token context, and an MIT license. On the new InclusionMed evaluation it ranks first among open models, and its model card reports the top score, 65.72, on HealthBench Professional in a nine model comparison. The scores are Ant's own. The model is built for clinical reasoning, medical search, and tool using agents, and it is weaker on general coding tasks.

What it means for the AI industry: open weights keep entering specialist fields that closed vendors priced as premium. A permissively licensed medical model at this scale resets what hospitals and health platforms expect to pay for.

What it means for Defense: military health is a plausible user of a self hostable medical model, and the conditions are the usual ones: evaluate locally on your own cases, verify the weights, and keep clinical decisions with clinicians until the evidence supports more.

Source: [MarkTechPost, Ant Group Releases LingSante-3.1-flash](https://www.marktechpost.com/2026/11/28/ant-group-lingsante-3-1-flash-open-source-medical-ai/), published November 28, 2026.

## A 30 billion parameter model beats a 120 billion parameter one on research tasks

[MarkTechPost reported on November 26](https://www.marktechpost.com/2026/11/26/sakana-ai-namazu-small-30b-nemotron-3-nano/) that Sakana AI released Namazu Small, a 30 billion parameter reasoning model built by continued pretraining and post-training on Nvidia's Nemotron 3 Nano base. Sakana reports a 60.1 average across 25 benchmarks, ahead of the 120 billion parameter Nemotron 3 Super at 56.2, with the largest gains in web research and long document work: 73.5 on BrowseComp against 36.1 for Super. Closed book knowledge is the weak spot, and all scores are self reported. Weights are not yet released; on-premises details are due in December.

What it means for the AI industry: post-training on an open base is beating raw scale on research tasks. That lowers the cost of capable research agents and shifts value from model size to training method.

What it means for Defense: small models designed to run in your own environment fit work that cannot leave the boundary. The knowledge gap is the caution: a research model that grounds answers in retrieved documents is a different tool from one answering from memory, and it should be tasked accordingly.

Source: [MarkTechPost, Sakana AI Releases Namazu Small](https://www.marktechpost.com/2026/11/26/sakana-ai-namazu-small-30b-nemotron-3-nano/), November 26, 2026.

## Poland buys Palantir AI and keeps the keys

[Wireframe News' November 27 edition](https://read.wireframenews.com/p/the-daily-fri-november-27-2026-4), reporting Reuters from November 27, says Poland signed a five year deal worth about 300 million dollars for Palantir software that uses AI to support army commanders' decisions. Poland's defence minister said all keys, servers, and information stay with its armed forces. In the same week, North Rhine-Westphalia became the first German state to decide to leave Palantir, choosing a Munich based replacement to run on police owned infrastructure from late 2027.

What it means for the AI industry: sovereignty terms are part of the product now. Two European governments answered the same question in opposite directions, and both insisted on local control of keys and infrastructure.

What it means for Defense: this is the adoption pattern for US built AI platforms among allies: the software can be American, the control arrangement cannot be. Vendors who cannot offer that split will lose deals they would otherwise win.

Source: [Wireframe News, The Daily, November 27, 2026](https://read.wireframenews.com/p/the-daily-fri-november-27-2026-4), reporting Reuters, November 27, 2026.

## An observation from my own work

I have argued in this blog for years that the control plane is where governance either holds or fails, most directly in [An Alliance Is Not a Control Plane](https://blog.thinxai.net/posts/alliance-is-not-a-control-plane/). Cloud One is that argument with stakes attached. An organization can govern every application on a platform, every agent, every credential, and still lose the platform itself if the control plane is treated as plumbing. The control plane is the asset. Monitor it like one.

## What to watch

The Air Force damage assessment on Cloud One, and whether the Bank of England's warning changes the price of the next round of AI borrowing.
