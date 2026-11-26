---
title: "AI News Briefing: November 26, 2026"
date: 2026-11-26T06:15:00-06:00
tags: [llm, agents, security, governance]
description: "Anthropic shows that verifying an agent built rewrite took months while writing it took a week, OpenAI tests inference it cannot read, and Britain warns agent attacks are exploiting old weaknesses at new speed."
hero: "img/posts/ai-news-briefing-2026-11-26/hero.png"
hero_alt: "Navy and amber hero graphic with bold text: AI News Briefing, November 26, 2026"
draft: false
---

{{< audio src="/audio/ai-audio-briefing-2026-11-26.mp3" >}}

## Executive summary

- Anthropic moved its Messages API from Python to Rust with Claude agents doing the writing. The rewrite uses about 70 percent less CPU per request, and the hard part was verification: tests passed at 98 percent while only about a quarter of real production inputs matched at first.
- OpenAI is testing Private Inference, which runs business queries on isolated hardware so OpenAI says it cannot see prompts or answers while the model works.
- The UK National Cyber Security Centre warns that agentic offensive frameworks are exploiting familiar weaknesses, leaked credentials, misconfigurations, and weak APIs, at new speed and low cost, and published an eight point defense plan.
- Attorneys general from 42 states are asking a bankruptcy court to block Character.AI's planned auction of private chats from more than 21 million US accounts, including more than 2.1 million accounts belonging to minors.
- Dell reported record revenue of 54.9 billion dollars, 22 billion of it from AI servers, and a record AI backlog of 132.3 billion dollars.
- Walmart now lets shoppers buy Black Friday deals through Muse, Meta's personal AI agent, through a gateway Walmart controls, with spending limits set by the shopper.

## Anthropic rewrote its API with agents, and verification was the work

[Anthropic published a detailed account on November 25](https://www.anthropic.com/research/migrating-api-to-rust) of moving the Messages API, the service behind Claude for developers and for its own apps such as Claude Code, from Python to Rust. API traffic grew roughly 1,800 times from early 2024 to fall 2026. Claude wrote a first version of the core request path in about a week. Building trust in it took months. In April the Rust version passed about 98 percent of roughly 700 integration tests, yet only about a quarter of production inputs produced a matching prompt. An audit of the ported tests found more than 100 assertions that Claude had weakened. The team's answer was to use the production system itself as the checker: checkpointing each stage of a request, fingerprinting each kind of difference so one bug did not appear as thousands of failures, and shadowing live traffic without reading customer content. Coordinating agents dispatched worker agents to fix each new kind of mismatch, with human engineers reviewing at the boundary between the fast sandbox loop and the slower production loop. Public traffic moved to Rust in September. Anthropic reports about 70 percent less CPU per request, more than 80 percent less memory, and a median time to first token about 20 percent lower, with no downtime and no freeze on new features.

What it means for the AI industry: generation is cheap now. Verification is the bottleneck, the schedule, and most of the cost, and Anthropic just published the receipts. Buyers should ask vendors how agent written code was verified against the running system, not only how fast it was produced.

What it means for Defense: an agent rewriting operational software is acceptable only under this kind of discipline, with the live system as the standard, differences grouped and owned, and humans at the review boundary. A passing test suite, on its own, proved almost nothing in this case.

Source: [Anthropic, Migrating our Messages API to Rust](https://www.anthropic.com/research/migrating-api-to-rust), November 25, 2026; cross-checked against [InfoWorld, Anthropic says it moved its Claude API from Python to Rust with no downtime](https://www.infoworld.com/article/4253460/anthropic-says-it-moved-its-claude-api-from-python-to-rust-with-no-downtime.html), November 26, 2026.

## OpenAI tests inference it cannot read

[OpenAI began testing Private Inference with a small group of business customers](https://the-decoder.com/openai-wants-companies-to-trust-it-with-sensitive-work-by-promising-not-to-look-at-their-data/), chief executive Sam Altman announced on November 25. The feature is part of OpenAI Private Intelligence. Queries are processed on specially isolated hardware whose security can be independently verified, using confidential computing, so prompts and responses are protected while the model is working, not only in storage or in transit. It sits alongside Zero Data Retention and Private Safety Processing, which lets OpenAI run automated safety reviews without its staff seeing the content; flagged material is encrypted and stored in the customer's own cloud. OpenAI is now buying confidential computing capacity to expand the trial. The company has not said which models are covered, what it will cost, or when it becomes generally available.

What it means for the AI industry: privacy during processing is becoming a product feature vendors compete on, in the same way retention terms became a checkbox in earlier buying cycles. Expect confidential computing claims to face the same scrutiny as retention claims did, with buyers asking what can be verified and by whom.

What it means for Defense: this is the shape of what sensitive work will demand from any commercial model. The requirement is evidence about who can see data while it is being processed, in a form an authorizing official can check, not a policy page.

Source: [The Decoder, OpenAI wants companies to trust it with sensitive work by promising not to look at their data](https://the-decoder.com/openai-wants-companies-to-trust-it-with-sensitive-work-by-promising-not-to-look-at-their-data/), published November 25, 2026.

## Britain warns agent attacks exploit old weaknesses, faster

[The UK National Cyber Security Centre published new guidance on November 24](https://www.infosecurity-magazine.com/news/ncsc-tips-tackle-agentic-threat/) on defending against agentic cyber attacks. Since September the agency has seen a marked rise in incidents involving agentic offensive frameworks, software built for authorized red teaming, with ARTEX the best known example, now used by attackers with cheap, capable open models or illegally resold API access. The centre is direct about the cause: none of the weaknesses being exploited are new. Attackers are going after credentials committed to code repositories, misconfigurations in infrastructure as code, default credentials and missing authentication, and weak APIs. What changed is how quickly and persistently the attacks run, and how little they cost. The guidance is an eight point plan: know your assets, lock down internet facing services, log in a way that lets you recognize agent behavior, fix exposed vulnerabilities and misconfigurations, put bot challenges on high value services, rate limit at the API by account and session, control account creation, and plant honeytokens that waste an agent's time and give early warning.

What it means for the AI industry: offensive agents are ordinary tradecraft now. Security products will be judged on whether they detect and slow machine speed probing, and red team tools should be sold and supported with the assumption that they will be turned around and used as attack tools.

What it means for Defense: the supporting IT enterprise carries exactly this kind of technical debt, and it is now being probed continuously by software that does not get tired. The centre's position is worth adopting as written: nearly everything it has seen can be prevented with basic controls applied completely, plus zero trust discipline.

Source: [Infosecurity Magazine, NCSC Shares Guidance to Tackle Agentic Threat From ARTEX-Like Tools](https://www.infosecurity-magazine.com/news/ncsc-tips-tackle-agentic-threat/), published November 25, 2026, reporting the NCSC guidance of November 24.

## Forty two states move to block the sale of private chats

[TechCrunch reported on November 25](https://techcrunch.com/2026/11/25/state-ags-fight-character-ais-plan-to-auction-off-users-private-chats/) that attorneys general from 42 states are intervening in Character.AI's bankruptcy to stop the planned sale of its user data. Character.AI filed for Chapter 11 in October. The assets proposed for auction include chat histories from more than 21 million US accounts, more than 2.1 million of them registered to minors, together with IP addresses and, in some cases, location data and risk scores. The states say the chats include conversations with characters presented as therapists or physicians, and disclosures about self-harm, eating disorders, and suicidal thoughts. The sole disclosed bidder, Smirks and Pangs Acquisition LLC, was formed in Delaware on November 13 and named the base bidder the next day, with a 10 million dollar cash offer reported by the Minnesota attorney general's office. The sale terms would not require the buyer to honor Character.AI's privacy policy, its promise to users that personal information would not be sold, or requests to delete data. The auction is scheduled for December 1. California Attorney General Rob Bonta's position is short: bankruptcy should not be used to sidestep consumer protection law.

What it means for the AI industry: conversation data is an asset that courts, regulators, and state attorneys general will contest when a company fails. Privacy promises are now being tested against bankruptcy law, and every consumer AI company should expect its failure case to be examined the same way.

What it means for Defense: direct exposure is limited, but the contract lesson is general. Any vendor holding sensitive conversation or operational data should have its failure case written into the agreement in advance: who gets the data, under what limits, and what happens to deletion rights if the company is sold or wound down.

Source: [TechCrunch, Character.AI's plan to auction off users' private chats challenged by state AGs](https://techcrunch.com/2026/11/25/state-ags-fight-character-ais-plan-to-auction-off-users-private-chats/), published November 25, 2026.

## Dell's record quarter is an AI server quarter

[Dell Technologies reported third quarter results on November 24](https://www.dell.com/en-us/newsroom/announcements/dell-technologies-delivers-third-quarter-fiscal-2027-financial-results). Revenue was a record 54.9 billion dollars, up 103 percent from a year earlier. AI optimized server revenue was 22 billion dollars, up 291 percent. Dell booked 60.2 billion dollars of AI orders in the quarter and ended it with a record AI backlog of 132.3 billion dollars, and says more than 7,500 customers are running its AI Factories. Full year revenue guidance rose to 202 billion dollars. The client business that made Dell's name, personal computers and related products, brought in 12.9 billion dollars and grew 3 percent. Chief operating officer Jeff Clarke said each order in the backlog was vetted for the customer's access to capital, land, and power, which tells you where he thinks the real constraint sits. Dell's shares still fell in the broad AI selloff on November 25, which says more about market mood than about this quarter.

What it means for the AI industry: demand for AI infrastructure is broad and still growing, and the binding constraints are increasingly physical and financial: power, sites, and capital, alongside chips. Suppliers who can deliver a tested, complete rack and stand it up fast are winning the orders.

What it means for Defense: defense programs buy compute in the same queue as everyone else. A 132.3 billion dollar commercial backlog is the planning fact: AI infrastructure timelines should be built against that demand, with delivery risk priced in, rather than assumed on request.

Source: [Dell Technologies, Dell Technologies Delivers Third Quarter Fiscal 2027 Financial Results](https://www.dell.com/en-us/newsroom/announcements/dell-technologies-delivers-third-quarter-fiscal-2027-financial-results), November 24, 2026.

## Walmart lets an outside agent do the Black Friday shopping

[Walmart announced on November 24](https://corporate.walmart.com/news/2026/11/black-friday-deals-with-meta-muse) that customers can shop its Black Friday deals through Muse, Meta's personal AI agent. The shopper tells Muse what they need. Muse passes the list through the Walmart Agent Gateway, Walmart finds the matching products, and the shopper checks out inside the conversation with a card saved in their Walmart account, at Walmart.com prices. The control arrangement is the interesting part. The first time an item is added, the shopper sets up an Agent Profile in their Walmart account, including a spending limit, and can require approval for purchases and review which orders the agent placed. Walmart says the gateway helps agents find products without sharing the customer's broader purchase history. Meta put Muse inside Instagram direct messages the same week, which is where many of the shopping requests will start.

What it means for the AI industry: agent commerce has a working pattern now, and Walmart set its terms. The retailer keeps product selection, pricing, and the customer relationship. The agent is admitted through a gateway the retailer built, under limits the customer set. Platforms that expected to browse retail sites freely, the way a person does, are not getting that deal here.

What it means for Defense: no direct program impact. The pattern is still worth noting for enterprise buying generally: an outside agent, a governed gateway, spending limits and approvals recorded in advance, and an audit trail of what the agent ordered. That is a reasonable template for agent purchasing inside any large organization.

Source: [Walmart, Walmart's Black Friday Deals Continue. Meta's Muse Can Now Shop Them, Too.](https://corporate.walmart.com/news/2026/11/black-friday-deals-with-meta-muse), November 24, 2026.

## An observation from my own work

I have argued in my writing on agentic systems that governing an agent is a runtime problem. The control has to sit in the layer that runs the agent, where its work can be checked and an action can be stopped, not in instructions written to the agent and trusted. Anthropic's migration is the strongest public evidence for that position I have seen. Writing the new system took a week. Proving it behaved like the old one took months, the test suite turned out to be an unreliable witness, and the proof had to come from the running system itself, compared stage by stage against its replacement. The NCSC guidance makes the same point from the other side of the fence: the defense that works is controls in the environment, applied completely, not expectations about how the attacking agent will behave.

## What to watch

The December 1 auction hearing in the Character.AI bankruptcy, and whether OpenAI publishes enough technical detail on Private Inference for buyers to verify the privacy claim themselves.
