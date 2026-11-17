---
title: "The State of the Standards for AI"
date: 2026-11-17T07:22:26-06:00
tags: [governance, compliance, agents]
description: "The framework layer for AI is settled, the EU conformity layer is one standard deep, and the agent layer is still draft work. This is the baseline I will diff against each quarter."
hero: "img/posts/state-of-the-standards-q4-2026/hero.png"
hero_alt: "Navy and amber hero graphic with bold text: The State of the Standards for AI"
draft: false
---

This is the baseline. I plan to revisit the state of the AI standards once a quarter and report only what changed: what got published, what got cited, what slipped, and what got replaced. A baseline has to be plain about what exists today, or the diff next quarter means nothing.

Three layers matter for my work. The framework layer tells an organization how to govern AI. The conformity layer tells a provider how to prove it meets a law. The agent layer would tell an operator how an agent should identify itself, take authorization, and leave evidence at run time. The first layer is settled. The second is one standard deep. The third is still draft work.

## The framework layer is settled

[NIST's AI Risk Management Framework](https://docs.modulos.ai/frameworks/nist-ai-rmf) carries the vocabulary in the United States. Version 1.0, published as NIST AI 100-1 in January 2023, organizes the work as Govern, Map, Measure, and Manage. Its Generative AI Profile, NIST AI 600-1 from July 2024, adds the generative risks and suggested actions. NIST says version 1.0 is being revised under the White House AI Action Plan. No draft and no date have been published, so 1.0 is still the text to build on.

The certifiable counterpart is ISO/IEC 42001:2023. As [Concentric's explainer on ISO 42001](https://concentric.ai/what-is-iso-42001/) puts it, 42001 specifies an AI management system: policy, roles, risk assessment, impact assessment, controls, and audit, in the same management system shape as ISO 27001. Two companions sit next to it. ISO/IEC 23894:2023 gives guidance on AI risk management. ISO/IEC 42005:2025 gives guidance on AI system impact assessment.

That is enough to stand up a program: owners, inventory, assessments, and certification against 42001 if I need outside attestation. What I cannot do is treat that certificate as legal conformity in Europe. It is not.

## The conformity layer is one standard deep

Under the EU AI Act, presumption of conformity comes only from a harmonized standard cited in the Official Journal. Certification to ISO/IEC 42001 gives no such presumption.

The first citation arrived this fall. [Valment's standards tracker](https://www.valment.com/standards) records EN 18286:2026, the quality management system standard for Article 17, as published in July 2026 and cited in the Official Journal on 14 October 2026. [The JTC 21 tracker](https://kla.digital/blog/jtc-21-standards-tracker) confirms the same point from the committee side: as of its 15 October check, EN 18286 was the only prioritized deliverable published and cited.

One standard. It covers the quality management system a provider of a high-risk system must run. It does not cover risk management, logging, transparency, human oversight, accuracy, or cybersecurity in Articles 9 to 15.

The rest are still drafts, and the summer did not go well for them. The tracker and the [September ballot summary summarized by Technspire](https://technspire.com/en/blog/en-18286-official-journal-ai-act-qms-plan) agree on the pattern: prEN 18228 on risk management was rejected at enquiry, prEN 18229-1 on logging was rejected, and prEN 18282 on cybersecurity was rejected. Each now needs comment resolution, a formal vote, Commission assessment, and a citation decision of its own. The amended standardization request that authorizes this work expires on 28 February 2027.

So the conformity position today is narrow and exact. I have a cited path for the Article 17 quality system. For the other high-risk requirements, I have draft text I can design against, but no cited standard I can claim conformity through.

## The agent layer is the thinnest

Nothing ratified standardizes how an agent identifies itself, how it receives and narrows authorization, or how it records what it did, at operational depth.

The closest United States work is new and unfinished. NIST's Center for AI Standards and Innovation launched the [AI Agent Standards Initiative](https://www.governedautonomy.org/standards/nist-caisi-agent-standards/) on 17 February 2026. Its early outputs are requests for information, listening sessions, and a National Cybersecurity Center of Excellence concept paper on agent identity and authorization, in draft on 5 February 2026, with more than 600 comments received and a practice guide still to come. That is a work program, not a standard.

The first government framework written specifically for agents came from Singapore. [The mapping of Singapore's framework](https://governedautonomy.org/standards/imda-agentic-ai/) records that the Infocomm Media Development Authority first published its Model AI Governance Framework for Agentic AI in January 2026 and released version 1.5 on 20 May 2026. It is voluntary guidance: it bounds risk, assigns human accountability, and sets controls across the life cycle. Useful design input. It binds no one and certifies nothing.

That thinness is the fact to hold onto. My agents run today. The standards that would govern their identity and authorization at run time do not exist in final form anywhere I can point to.

## The deadlines moved

Two date changes reset the planning clock.

In Europe, the Digital Omnibus, Regulation (EU) 2026/1744, moved the high-risk obligations. [The deadline tracker built from the Official Journal texts](https://cloudsecuritydesk.com/publications/eu-ai-act-cloud-deployer-timeline) lists the result plainly: Annex III high-risk duties now apply from 2 December 2027, and Annex I duties for AI in regulated products apply from 2 August 2028. The duties that already apply stayed in place, including the general-purpose AI model duties and the Article 50 transparency duties.

In Colorado, the replacement is more complete. [The Colorado guide tracking SB 26-189](https://www.ailawsbystate.com/blog/colorado-ai-act-compliance-guide-2026) records that the governor signed the bill on 14 May 2026, repealing and replacing the original Colorado AI Act effective 1 January 2027, and dropping the earlier duty of care, mandatory impact assessments, and the risk management program requirement in favor of a narrower notice and disclosure regime.

Extra time is not the same as no work. December 2027 arrives on a fixed date whether the remaining harmonized standards are cited or not.

| Layer | Settled piece | Still missing |
|---|---|---|
| Framework | NIST AI RMF 1.0 and ISO/IEC 42001:2023 | NIST revision, no date published |
| Conformity (EU) | EN 18286:2026 cited 14 October 2026 for Article 17 | Cited standards for Articles 9 to 15 |
| Agent | Singapore framework v1.5 as voluntary guidance | Any ratified standard for agent identity, authorization, or evaluation |

## What this means in practice

The settled standards govern the organization. They specify the management system, the risk process, and the roles. They do not govern the run. They do not tell me how an agent authenticates to a tool at 2 a.m., what permission it should carry for one task, or what evidence that run must leave behind.

I wrote about that difference in [The Governed Control System](https://blog.thinxai.net/posts/the-governed-control-system/): conformance to a management system is not fitness at execution time. The same gap shows up in [How Companies Integrate Their Values into the Broader AI Ecosystem](https://blog.thinxai.net/posts/values-into-the-ai-ecosystem/), where the binding has to happen in the execution fabric, not only in policy, and in [The MxM Fabric Defined](https://blog.thinxai.net/posts/the-mxm-fabric-defined/), where behavior lives in artifacts an operator can inspect and change.

My working rule for this quarter is simple. Build the program on the framework layer now. Design against the draft conformity standards, but claim conformity only where a citation exists. For agents, keep my own controls for identity, permission, and evidence, written down as if an auditor will ask for them. Eventually one will.

Next quarter I will diff this page against what actually moved: any new Official Journal citation, any NIST agent deliverable past draft, any date change, and the status of the February 2027 standardization request. If nothing moves, I will say that too.
