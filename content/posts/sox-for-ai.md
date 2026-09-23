---
title: "We Need SOX for AI"
date: 2026-09-22
tags: ["ai-governance", "enterprise-ai", "compliance"]
draft: false
series: "SOX for AI"
description: "Sarbanes-Oxley did not fix lying; it fixed the structure. AI needs the same treatment: named humans, documented controls, independent review, and consequences."
hero: "img/posts/sox-for-ai/hero.png"
hero_alt: "Infographic listing the four pillars: inventory, named ownership, documented controls, independent audit"
---

In [the last post](https://blog.thinxai.net/posts/before-ai-starts-governing-us/) I argued that the real AI risk is governance inversion: institutions reorganizing themselves around what AI systems optimize until the derived system drives the originators. The fix is enforceable structure. Here is what that structure looks like.

## What Sarbanes-Oxley Got Right

Sarbanes-Oxley was enacted after corporate failures exposed how easily financial reporting could be manipulated or obscured when accountability was weak. Its central insight was simple: organizations should not merely promise that their financial controls are sound. Management must be responsible for those controls, assess whether they work, maintain evidence, disclose material weaknesses, and subject those assessments to independent audit.

The principle applies directly to AI. Companies should not be able to deploy systems that materially affect workers, customers, markets, safety, public information, or civil rights and then say, "The model made the decision." If the AI matters, the controls around it must matter.

A fair objection: SOX became compliance theater in places, and it did not prevent 2008. Granted. I am borrowing SOX-the-principle, not SOX-the-law: named humans on the line, documented controls, independent attestation, consequences for failure. The principle survived the law's imperfections. That is the part worth transplanting.

One more distinction. The EU AI Act regulates AI systems as products, with safety requirements sorted by risk class. What I am describing is different: internal-controls accountability for the organizations deploying AI, the way SOX governs the company rather than the product. Both can exist. They solve different problems.

## What "SOX for AI" Would Require

This would not regulate every autocomplete feature or internal brainstorming tool the same way. It focuses on systems whose failures have material consequences. For those systems, organizations should be required to demonstrate four things.

### 1. A complete AI inventory

You cannot govern what you cannot identify. Organizations need a current record of the AI systems they develop, buy, integrate, or allow employees to use in consequential workflows: the system's purpose and scope, the model, provider, version, and connected tools, the data sources, the business and technical owners, the groups affected, the decisions or actions it can influence or execute, and the level of human review and override. A company that cannot identify its material AI systems is not managing AI risk. It is hoping.

### 2. Named accountability

Every consequential AI deployment should have a clearly accountable executive owner, responsible for the system's controls, testing, deployment approval, monitoring, incident response, and remediation. Not an "AI ethics statement." A name. Boards need a defined AI-risk oversight role too, because material AI risk is now operational, legal, reputational, financial, and strategic risk at once. There must be a person, not an algorithm, committee, or vendor contract, who can answer: who approved this, what safeguards were in place, what did you know, and when did you know it?

### 3. Controls before deployment

High-impact AI should be treated more like a production financial system or a safety-critical process than an experimental software feature. Before deployment, organizations should assess whether the use case is appropriate for automation, who could be harmed by false positives, false negatives, hallucinations, or biased outcomes, whether the data is lawful and reliable, whether users understand the system's limits, whether outputs can be challenged and corrected, whether the system can be manipulated through adversarial prompts or poisoned data, and whether humans retain meaningful intervention and shutdown authority. NIST's AI Risk Management Framework, with its Govern, Map, Measure, and Manage functions, offers a useful structure. But a framework becomes durable only when an organization is required to implement it, document it, and answer for failures.

### 4. Change management and audit trails

An AI system is not static. A model can be updated, a vendor can modify its service, a prompt can change, new data can be connected, an agent can be given another tool. A small configuration adjustment can materially change real-world behavior. That means version control for models, prompts, configurations, and connected tools, testing before material changes reach production, clear approval workflows, rollback capability, monitoring after release, and logs sufficient to reconstruct important decisions. The point is not to preserve every byte. The point is to preserve enough reliable evidence to investigate what happened when the system causes harm.

## Independent Assurance Matters

Self-assessment has limits. Every organization believes its controls are adequate until an incident shows otherwise. Higher-risk systems need independent review that tests whether stated controls actually function: are models tested for the risks they are likely to create, are vendors assessed and monitored, do access controls prevent unauthorized use, are changes reviewed and documented, are human overrides real and usable, are incidents detected and remediated, are executives receiving accurate risk information? Audits must test evidence, not slogans.

## The Right Approach Is Risk-Tiered

A serious regime should be proportionate. A low-stakes use, like drafting an internal meeting summary, does not need the same treatment as a system determining eligibility for employment, credit, housing, healthcare, or insurance.

| AI use | Expected governance |
|---|---|
| Low-risk productivity support | Basic privacy, security, acceptable-use policies, transparency |
| Material business processes | System inventory, documented controls, testing, monitoring, change management, executive ownership |
| High-impact decisions or autonomous actions | Independent audit, rigorous pre-deployment assessment, human appeal and override, incident reporting, stronger liability |

The purpose is not to stop innovation. It is to ensure innovation is accountable to the people and institutions it affects.

## Start Monday Morning

I have written this in the language of legislation because that is where it belongs eventually. I wrote about the regulatory case in February on LinkedIn. But nothing here requires an act of Congress to begin. An enterprise could start its AI inventory this week, name its owners, and document its controls. The companies that build this muscle voluntarily will be ready when it becomes mandatory, and they will be governing their systems in the meantime instead of being governed by them.

No consequential AI without a responsible human principal, auditable controls, meaningful recourse, and enforceable accountability.
