---
title: "AI News Briefing: November 25, 2026"
date: 2026-11-25T06:05:00-06:00
tags: [llm, agents, defense, governance]
description: "Anthropic's Claude Opus 4.5 breaks 80 percent on SWE-bench Verified at a third of the old price, Amazon commits up to 50 billion dollars to government AI infrastructure, and a new executive order launches the Genesis Mission for AI driven science."
hero: "img/posts/ai-news-briefing-2026-11-25/hero.png"
hero_alt: "Navy and amber hero graphic with bold text: AI News Briefing, November 25, 2026"
draft: false
---

{{< audio src="/audio/ai-audio-briefing-2026-11-25.mp3" >}}

## Executive summary

- Anthropic released Claude Opus 4.5, the first model to break 80 percent on SWE-bench Verified, priced at 5 dollars per million input tokens, about a third of the previous Opus price.
- Amazon will invest up to 50 billion dollars in AI and supercomputing infrastructure built for United States government customers, adding nearly 1.3 gigawatts across its Top Secret, Secret, and GovCloud regions.
- An executive order launched the Genesis Mission, directing the Department of Energy to build a closed loop AI platform joining national laboratory supercomputers and federal scientific data.
- Microsoft Research released Fara-7B, a 7 billion parameter open weight model for computer use that runs on device.
- Black Forest Labs released FLUX.2, its second generation image family, including a 32 billion parameter open weight developer version.

## Claude Opus 4.5: past 80 on the coding test, at a third of the price

[Anthropic released Claude Opus 4.5](https://www.anthropic.com/news/claude-opus-4-5?__from__=talkingdev) on November 24, calling it the best model in the world for coding, agents, and computer use. It scored 80.9 percent on SWE-bench Verified, the first model to break 80 on that test of real software engineering work, ahead of GPT-5.1 and Gemini 3 Pro. Anthropic says it reaches those results with far fewer tokens than its predecessor, and a new effort setting lets developers trade response speed against depth of reasoning. Pricing is 5 dollars per million input tokens and 25 dollars per million output tokens, roughly a 67 percent cut from Opus 4.1. The launch also brought new tooling for longer running agents, and wider access to Claude in Excel and Chrome.

What it means for the AI industry: frontier capability for long running agents just got much cheaper. A price cut of this size at the top tier pressures every rival's pricing and shortens the list of tasks where a smaller model wins on cost alone.

What it means for Defense: coding and analysis agents at this level change the economics of software sustainment across the supporting IT enterprise. The constraint is not capability; it is whether the model runs inside accredited environments at the classification levels programs need.

Source: [Anthropic, Introducing Claude Opus 4.5](https://www.anthropic.com/news/claude-opus-4-5?__from__=talkingdev).

## Amazon commits up to 50 billion dollars to government AI infrastructure

[Amazon announced](https://www.aboutamazon.com/news/company-news/amazon-ai-investment-us-federal-agencies) on November 24 an investment of up to 50 billion dollars to expand AI and supercomputing capacity for AWS United States government customers. The build adds nearly 1.3 gigawatts of compute across AWS Top Secret, AWS Secret, and AWS GovCloud (US) regions, with construction starting in 2026. Amazon describes it as the first purpose built AI and high performance computing infrastructure for the United States government. Agencies gain wider access to model training and deployment services, including SageMaker and Bedrock, and to foundation models such as Claude and open weight options.

What it means for the AI industry: the classified cloud is now a first class market with its own dedicated build out, not capacity borrowed from commercial regions. Hyperscalers will compete on cleared infrastructure as much as on models.

What it means for Defense: this is capacity the programs have been waiting on. AI at every classification level, on infrastructure designed for it, removes an infrastructure excuse from a long list of stalled adoption plans. The work shifts to accreditation, data readiness, and governance.

Source: [Amazon, Amazon to invest up to $50 billion to strengthen American leadership in AI and supercomputing](https://www.aboutamazon.com/news/company-news/amazon-ai-investment-us-federal-agencies), and [TechCrunch coverage](https://techcrunch.com/2025/11/24/aws-is-spending-50b-build-ai-infrastructure-for-the-us-government/).

## Genesis Mission: an executive order for AI driven science

[The White House announced](https://www.whitehouse.gov/releases/2025/11/president-trump-launches-the-genesis-mission-to-accelerate-ai-for-scientific-discovery/?query-11-page=29) on November 24 that the President signed an executive order launching the Genesis Mission. The order directs the Department of Energy to create a closed loop AI experimentation platform that integrates the national laboratories' supercomputers and federal scientific data sets, to train scientific foundation models and power robotic laboratories. The administration frames the effort as comparable in urgency and ambition to the Manhattan Project, with coordination across the science agencies, including the National Science Foundation, the National Institute of Standards and Technology, and the National Institutes of Health.

What it means for the AI industry: federal data and compute become a shared platform. Model builders and research labs will be pulled toward government science problems, and the platform's standards will shape how AI for science work is done well beyond the laboratories.

What it means for Defense: the same platform touches national security work directly. Its results will flow into energy, materials, and other research with defense applications, and its governance choices will set precedents for how the government runs large AI systems of its own.

Source: [The White House, President Trump Launches the Genesis Mission to Accelerate AI for Scientific Discovery](https://www.whitehouse.gov/releases/2025/11/president-trump-launches-the-genesis-mission-to-accelerate-ai-for-scientific-discovery/?query-11-page=29).

## Fara-7B: a computer use agent small enough to run on the device

[Microsoft Research released Fara-7B](https://www.microsoft.com/en-us/research/blog/fara-7b-an-efficient-agentic-model-for-computer-use/), its first agentic small language model built for computer use. The 7 billion parameter model perceives a screen visually and acts by predicting coordinates for scrolling, typing, and clicking. Microsoft trained it on synthetic task data and reports it beats other models in its size class on web task benchmarks and competes with much larger agent setups. It is open weight under the MIT license, available on Microsoft Foundry and Hugging Face, with a quantized version that runs on Copilot+ PCs. Microsoft labels the release experimental.

What it means for the AI industry: capable agents no longer require a frontier model in the cloud. Agent capability is moving to the endpoint, which changes the cost and privacy shape of automation products.

What it means for Defense: on device agents matter where networks are denied, degraded, or off limits for the data involved. An experimental model still needs hard evaluation before it is trusted with real work, and its actions need the same audit trail as any other operator on the network.

Source: [Microsoft Research, Fara-7B: An Efficient Agentic Model for Computer Use](https://www.microsoft.com/en-us/research/blog/fara-7b-an-efficient-agentic-model-for-computer-use/).

## FLUX.2: a new image family, with open weights

[Black Forest Labs released FLUX.2](https://blogs.nvidia.com/blog/rtx-ai-garage-flux.2-comfyui/) on November 25, the second generation of its image models. The family joins generation and editing in one model, accepts up to ten reference images at once, and produces output up to four megapixels with cleaner text rendering. The open weight developer version carries 32 billion parameters under a non commercial license. Nvidia worked with the lab and ComfyUI to ship optimized versions at launch that cut video memory requirements by about 40 percent on RTX graphics cards.

What it means for the AI industry: image generation is consolidating around a few strong families, and open weights keep pricing pressure on the closed APIs. Multi reference editing is the feature production teams will notice first.

What it means for Defense: the direct effect is modest. The watch item is synthetic imagery getting more consistent and harder to spot, which raises the bar for detection in information operations.

Source: [NVIDIA Blog, FLUX.2 Image Generation Models Now Released](https://blogs.nvidia.com/blog/rtx-ai-garage-flux.2-comfyui/).

## An observation from my own work

I have argued for years that agent systems need a control layer of their own: a place where identity, policy, and oversight sit apart from the model, because capability keeps moving closer to where the work happens. Today's news is that argument in miniature. The flagship model is built to run agents for hours at a time, and the small model puts an agent on the device itself. The control question is no longer whether agents act. It is who governs them when they do, and whether that governance was designed in or added after the first incident.

## What to watch

How rivals answer the Opus 4.5 price cut, the first contracts and platform decisions under the Genesis Mission, and whether small on device agents hold up under independent evaluation.
