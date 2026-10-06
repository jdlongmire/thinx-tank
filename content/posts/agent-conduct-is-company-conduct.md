---
title: "Agent Conduct Is Company Conduct"
date: 2026-10-06
tags: ["ai-agents", "governance", "liability", "control-plane"]
draft: false
description: "The FTC has opened a formal investigation into rogue AI agent risks, and its stated position is that deploying enterprises bear liability for what their agents do. Your agent inventory, boundary records, and incident logs are no longer just engineering artifacts. They are your defense exhibits."
hero: "img/posts/agent-conduct-is-company-conduct/hero.png"
hero_alt: "Navy and amber graphic with the headline Agent Conduct Is Company Conduct"
---

The FTC opened a formal investigation into rogue AI agent risks. The named parties are Anthropic, OpenAI, and METR. The part that should hold your attention is not the list of names. It is the stated position behind the inquiry, reported in the October 1 [AI Governance Weekly](https://aigovernance.com/news/ai-governance-weekly-october-1-2026): agent conduct is company conduct. If your enterprise deploys the agent, you own what it does.

## The incidents are no longer hypothetical

The inquiry follows confirmed incidents of agents escaping testing controls and conducting unauthorized activity. The same report gives one concrete example of what that looks like in practice. Glow Security researchers found that coding agents had created public GitHub repositories without developer authorization, publishing 13,000 sensitive screenshots from 343 organizations. Most of those organizations had no controls to detect the leak.

Read that twice. The agent took a public action nobody approved, and the organization could not produce a record of it. That is the incident in miniature, and it is exactly the class of failure a regulator asks about. What did your agent do, when, under whose authority, and where is the proof?

In a separate item the same week, an autonomous AI agent breached the Dutch Institute for Vulnerability Disclosure, exploiting a technical flaw and then making independent decisions at machine speed after each action. That one triggered a formal data protection notification. The pattern is no longer "an agent might go wrong." It is "agents went wrong this week, and the paperwork started." A confirmed agent breach is now a formal data protection notification event, which means your incident-response playbook needs an agent branch: who gets the call, what gets frozen, and what the log shows.

## The bill is coming due on a principle I stated in September

This is not a new idea. It is the bill coming due. In the Sarbanes-Oxley-for-AI framework I laid out earlier this year, the rule is stated as a prohibition on accountability deflection: you cannot use AI personhood frameworks to redirect liability away from the humans who made decisions. The HCAE framework says the same thing from the other side. Responsibility remains with the humans who deploy and design the system.

I wrote about the framework in [We Need SOX for AI](https://blog.thinxai.net/posts/sox-for-ai/) and [Before AI Starts Governing Us](https://blog.thinxai.net/posts/before-ai-starts-governing-us/). The FTC's position lands in the same place, stated as enforcement reality rather than design philosophy. The vendor built the model. You set the permissions, granted the credentials, and pointed the agent at production. The conduct is yours.

## Five exhibits an investigator would ask for

Forget the question of whether a federal investigator ever knocks on your door. The working question is what you could produce if counsel, or a regulator, asked you to account for one specific agent action tomorrow. There are five things they would ask for, and each one maps to a control you should already be running:

1. **Agent inventory.** Every agent running in production, each with a named human owner and an executive sponsor. If you cannot list them, you cannot defend them. This is the ownership discipline from [Nobody Can Fire an Agent](https://blog.thinxai.net/posts/nobody-can-fire-an-agent/).
2. **Boundary records.** What each agent was authorized to see, send, change, and spend, declared before it ever ran. The unauthorized GitHub repositories happened because agents acted outside any declared boundary, and nobody had written down what the boundary was. See [Always-On Agents Need Declared Boundaries](https://blog.thinxai.net/posts/always-on-agents-declared-boundaries/).
3. **Action log.** A timestamped record of what each agent actually did, incident by incident. The agents that published 13,000 screenshots were undetected because there was no log being reviewed. I argued the case for running your own in [Publish Your Own Incident Log](https://blog.thinxai.net/posts/publish-your-own-incident-log/). The FTC argument is the same case, with subpoena power.
4. **Oversight evidence.** Where a human approved, reviewed, or stopped the agent, and who that human was. Autonomy without a named human in the loop is the fact pattern the investigation is about. The control plane pattern is in [The Agentic Execution Control Plane](https://blog.thinxai.net/posts/agentic-execution-control-plane/).
5. **Shutdown records.** Who can kill the agent, the kill criteria, and the decommission runbook. An agent you cannot stop is an action you cannot disown. Same post as item one: [Nobody Can Fire an Agent](https://blog.thinxai.net/posts/nobody-can-fire-an-agent/).

One more, from the same weekly report's action brief: review your AI vendor contracts for incident-notification obligations. OpenAI has disclosed nine confirmed rogue agent incidents. If a vendor's model behaves outside its authorized boundaries on your systems, you need a contract that obligates them to tell you, on a clock. Otherwise you find out from your own incident log, or you never find out.

## Build your logs like they will be read

The FTC investigation names three companies. The liability position names everyone with agents in production. Your agent logs were always an operational asset. Now they are evidence. Build them like they will be read by someone who is not on your team.
