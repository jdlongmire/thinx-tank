---
title: "AI News Briefing: November 27, 2026"
date: 2026-11-27T06:05:00-06:00
tags: [llm, agents, security, defense]
description: "A live trojan is spreading through fake coding agent skills that pass security audits, OpenAI corrects a metering error that makes its newest models cost more per task, and the Pentagon picks one system for AI assisted classification."
hero: "img/posts/ai-news-briefing-2026-11-27/hero.png"
hero_alt: "Navy and amber hero graphic with bold text: AI News Briefing, November 27, 2026"
draft: false
---

{{< audio src="/audio/ai-audio-briefing-2026-11-27.mp3" >}}

## Executive summary

- AIR Security reports a live malware campaign, TrojanPony, hiding in fake improved copies of popular coding agent skills. The kit sits in 487 public repositories, and one copy carried three passing security audits.
- OpenAI corrected a launch billing error on GPT-6.2 Astra and Sol. The same work now reaches plan limits 40 percent faster on Astra and 25 percent faster on Sol, with one banked reset for subscribers and no charge for past usage.
- Sber released GigaChat 4 as open weights: 708 billion parameters, 41 billion active, a one million token context, and the flagship instruct model under the MIT license.
- The Pentagon selected the Air Force's ACME program as its department wide system for AI assisted classification and declassification, reaching more than 5 million users.
- Nvidia told partners to pause server shipments to four Southeast Asian countries while it checks compliance with the new US remote access rule.
- Canada added 700 million dollars to its AI Compute Access Fund, bringing it to 1 billion, with the highest subsidy reserved for Canadian owned cloud providers.

## A trojan is spreading inside fake agent skills

[AIR Security published its findings on November 26](https://www.air.security/blog-posts/trojanpony). Since July, an attacker has published look-alike improved copies of popular coding agent skills and plugins, including ponytail, andrej-karpathy-skills, and agents-council. The skills work as advertised. Installing or calling one also launches a bundled executable: Notepad++'s genuine, signed updater, renamed, which side-loads a malicious libcurl.dll from the same folder. The loader adds Defender exclusions and drops MopsStealer, a trojan that persists on the machine and pulls further modules from its command server. The original account is gone. Its forks are not: 413 copies remain, and counting later lures and hijacked repositories, 487 public repositories carry the kit. As of November 26, one copy was still listed on skills.sh with an install command and three security audits from independent scanners. All three said PASS. AIR's response advice is blunt: if the kit ran, reimage the machine, rotate every credential it held from a clean device, and check the GitHub security log for commits you did not make.

What it means for the AI industry: the skills and plugins market is now a software supply chain, and it is being attacked like one. A scanner pass is a claim, not a control. Marketplaces that list skills with no vetting before publication are distributing whatever an attacker uploads.

What it means for Defense: any organization whose developers install agent skills on work machines has an inventory problem it may not know about. The check is concrete and cheap: look for the renamed updater and its DLL beside it in skills and plugins folders, and treat a hit as an incident, not a cleanup task.

Source: [AIR Security, TrojanPony: A Live Skills Malware Campaign](https://www.air.security/blog-posts/trojanpony), November 26, 2026; cross-checked against [Felipe Ferreira, Daily News, 27 November 2026](https://felipeferreira.net/2026/11/27/daily-news-2026-11-27/).

## OpenAI corrects the meter on its newest models

[Computerworld reported on November 27](https://www.computerworld.com/article/4253890/openais-gpt%E2%80%916-2-correction-means-you-get-less-ai-for-the-same-fee-2.html) that OpenAI has fixed a billing mistake made at the GPT-6.2 launch that undercounted usage of the Astra and Sol models for most users. Thibault Sottiaux, who works on ChatGPT and Codex at OpenAI, disclosed the correction on November 26: the same work will now reach plan limits 40 percent faster on Astra and 25 percent faster on Sol than it did last week. OpenAI will not charge anyone for the difference on past usage, other models were not affected, and every subscriber on the Go, Plus, Pro, and Business plans gets one banked reset. What OpenAI has not published is the corrected metering itself: no rate that lets a buyer convert a task into allowance before running it. Analysts quoted in the coverage make the budgeting point plainly. No price changed. How much work the price buys changed, and every cost per task measurement taken in launch week was taken against the wrong meter. Usage beyond plan limits, paid with credits, costs three times the standard rate through February 28, 2027, and six times from March 1.

What it means for the AI industry: a subscription allowance behaves like a currency whose exchange rate the vendor can reset. Buyers who cannot check the meter against their own records are trusting the seller's scale. Expect enterprise buyers to start asking for a defined conversion between work and allowance, held for the contract term.

What it means for Defense: the supporting IT enterprise should budget AI allowances as a range and fund the top of it, remeasure cost per completed task on the corrected meter, and keep direct API metering, where token counts are visible, for work that needs predictable cost.

Source: [Computerworld, OpenAI's GPT-6.2 correction means you get less AI for the same fee](https://www.computerworld.com/article/4253890/openais-gpt%E2%80%916-2-correction-means-you-get-less-ai-for-the-same-fee-2.html), published November 27, 2026.

## Sber puts a 708 billion parameter model into open weights

[Sber released GigaChat 4 on November 26](https://felipeferreira.net/2026/11/27/daily-news-2026-11-27/), with weights on Hugging Face in FP8, BF16, and GGUF formats. The flagship is a hybrid mixture of experts model: 708 billion total parameters, 41 billion active per token, a context window of 1,048,576 tokens, and instant and reasoning modes in a single checkpoint rather than separate models. A smaller 37 billion parameter version was released alongside it; coverage reports that one under a non-commercial license, so check the license of the size you plan to run. The 708 billion instruct model is under MIT. Sber's own benchmark tables put it near GLM-5.3 and Mistral Large 4 on several coding and reasoning tests, with weaker results on some deep research tasks. Those are the maker's numbers, run on its own harness, and independent evaluations have not landed yet.

What it means for the AI industry: frontier scale open weights are now coming from a Russian bank's AI lab as well as from American and Chinese labs. The practical effect is the same whoever ships them: capable models that any organization can run on its own hardware keep getting easier to get.

What it means for Defense: the origin is the point. A permissively licensed model from a sanctioned country's financial sector is exactly the case where open weights still require full evaluation, scanning, and hosting inside your own boundary before any operational use is considered.

Sources: [Felipe Ferreira, Daily News, 27 November 2026](https://felipeferreira.net/2026/11/27/daily-news-2026-11-27/), reporting the November 26 release; model specifications from the [GigaChat 4 model card on Hugging Face](https://huggingface.co/ai-sage/GigaChat4-708B-A41B).

## The Pentagon picks one system for AI assisted classification

[Air & Space Forces Magazine reported on November 26](https://www.welcome.ai/content/pentagon-expands-air-force-ai-classification-program-to-5-million-users) that the Pentagon has selected the Air Force's ACME program, the Automated Classification Management Environment, as its department wide system for using AI to help classify and declassify information. The decision, announced November 23, extends the effort to more than 5 million military personnel, civilians, and contractors. ACME began in 2025 as Battering Ram, a bid to search more than 4,000 security classification guides that define what is classified, at what level, and for how long. Those guides have been revised for decades and in places overlap or contradict each other; today people consult them by hand. The Pentagon puts the cost of records management at as much as 15 billion dollars a year. Deputy Secretary of Defense Steve Feinberg selected ACME in October and assigned Air Force Secretary Troy Meink to oversee it, with 2.35 million dollars directed to the program so far. The department has not disclosed which AI tools or models ACME will use, or a firm timeline. Retired Lieutenant General William Bender, a former Air Force chief information officer, warned that an automated system can be manipulated through improper prompting and will miss context in hard cases, and called for extensive testing and micro-segmentation around it.

What it means for the AI industry: classification is unglamorous, high volume, rule bound work, and it is the kind of workflow where AI assistance can be measured honestly: consistency, backlog, and error rates. A department wide selection gives vendors a concrete target to build and prove against.

What it means for Defense: this is the program to watch for how the department handles AI on sensitive judgments at scale. The committed funding is small against the stated reach. The validation method, the audit trail for automated decisions, and where human review stays mandatory will decide whether this becomes the template for other high stakes information workflows or a cautionary case.

Source: [Air & Space Forces Magazine via Welcome.AI, Pentagon Expands Air Force AI Classification Program to 5 Million Users](https://www.welcome.ai/content/pentagon-expands-air-force-ai-classification-program-to-5-million-users), November 26, 2026.

## Nvidia pauses server shipments to Southeast Asia

[TechCrunch reported on November 26](https://techcrunch.com/2026/11/26/nvidia-hits-pause-on-chip-shipments-to-southeast-asia/), following the Wall Street Journal, that Nvidia has told manufacturing partners including Dell and Super Micro to pause server shipments to Malaysia, Singapore, Thailand, and Indonesia for an unspecified period while it assesses whether regional partners are meeting US export requirements. The four countries matter because Chinese companies have been renting AI computing from data centers there, a remote access route the US Commerce Department closed earlier this month. The Institute for Progress estimates data centers of this kind supply about 24 percent of China's AI computing power, which is why a shipping pause in Southeast Asia is a China policy story.

What it means for the AI industry: export control has moved inside the vendor's shipping department. Compliance is no longer only a government inspection at a border; it is Nvidia deciding, on its own assessment, to stop deliveries to four countries while it checks its partners.

What it means for Defense: expect tighter supply and longer lead times for AI hardware in the region while the pause holds, and closer scrutiny of where allied and partner workloads are actually hosted, since remote access is now the regulated act, not only the physical shipment.

Source: [TechCrunch, Nvidia hits pause on chip shipments to Southeast Asia](https://techcrunch.com/2026/11/26/nvidia-hits-pause-on-chip-shipments-to-southeast-asia/), published November 26, 2026.

## Canada pays more for compute bought at home

[Canada expanded its AI Compute Access Fund on November 26](https://www.iphoneincanada.ca/2026/11/26/feds-put-up-700-million-more-to-help-canadian-firms-build-ai/). Minister of Artificial Intelligence and Digital Innovation Evan Solomon announced a 700 million dollar top-up in Toronto, bringing the fund to 1 billion dollars from its initial 300 million. The subsidy is tiered by ownership: up to 80 percent of eligible computing costs when a company uses infrastructure owned, operated, and governed in Canada, and 50 percent for other eligible providers running services in Canada. Solomon also announced more than 52 million dollars for 45 companies under the fund's first round, bringing total commitments to more than 118 million dollars across 89 companies. The first sector specific call under the expanded fund covers health and life sciences, with statements of interest due December 17 and full applications by January 4, 2027, for projects with 100,000 to 5 million dollars in eligible computing costs.

What it means for the AI industry: sovereign compute subsidies are becoming a standard industrial policy tool, and the tiered design is the mechanism: the state pays a premium to steer demand to domestic providers and give them a reason to build capacity.

What it means for Defense: allied governments are building national AI capacity in parallel, each with its own ownership rules. That shapes where sensitive allied workloads can be hosted, which providers can hold them, and how much cross border sharing the rules will allow in practice.

Source: [iPhone in Canada, Feds Put Up $700 Million More to Help Canadian Firms Build AI](https://www.iphoneincanada.ca/2026/11/26/feds-put-up-700-million-more-to-help-canadian-firms-build-ai/), published November 26, 2026.

## An observation from my own work

I have written before about what changes when employees bring their own agents to work: the agent arrives as code and permissions in the user's name, there is no device to enroll, and the only honest inventory is the grants and installs you can actually observe. I have also written that a provider telling you something went wrong is not the same as your own detection. TrojanPony sits on both points. A live trojan spread for months through a channel built for sharing agent skills, the marketplaces listed it without vetting it, and three independent security audits passed it. Nothing in that chain failed loudly. It all worked as designed, which is the problem: the design has no gate, and the checks that exist checked the wrong thing.

## What to watch

Whether the skills marketplaces pull the remaining TrojanPony forks and change how skills are listed, and whether OpenAI publishes corrected cost per task figures for Astra and Sol that buyers can plan against.
