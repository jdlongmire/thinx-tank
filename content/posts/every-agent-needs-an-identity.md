---
title: "Every Agent Needs an Identity"
date: 2026-10-05
tags: ["ai-agents", "identity", "enterprise-security", "non-human-identity"]
draft: false
description: "SpyCloud's 2026 Identity Threat Report found compromised non-human identities are now the leading path into the enterprise, ahead of phishing two to one. Every AI agent your people deploy creates credentials nobody provisioned, nobody owns, and nobody rotates. The fix is boring: give every agent a real identity."
hero: "img/posts/every-agent-needs-an-identity/hero.png"
hero_alt: "Navy and amber graphic with the headline Every Agent Needs an Identity"
---

On September 9, 2026, SpyCloud released its annual Identity Threat Report, and the headline finding should make every CIO put down their coffee: non-human identities (NHIs) are now the most common route attackers take into the enterprise. Compromised NHIs were named the primary entry point by 31% of respondents, nearly twice phishing and social engineering at 17%. NHI-related misuse was also the most commonly reported identity-based event type, at 42%. ([SpyCloud press release](https://spycloud.com/newsroom/spycloud-2026-identity-threat-report-finds-non-human-identities/))

The number that got my attention is the contradiction at the center of the report. Ninety-five percent of organizations believe they have adequate visibility into their AI and machine identity exposures. Only 36% are actually monitoring them. That is not a rounding error. That is 59 points of self-deception. Sixty-eight percent of organizations experienced an identity-based event in the same period, averaging eight events each. The ones who think they can see the problem are, mostly, not looking.

## Agents mint credentials faster than anyone can inventory them

This is a 2026 story, not a background IAM concern, because of what AI agents did to the scale. Every agent an employee connects to Slack, Salesforce, or an internal database creates new credentials: OAuth tokens, API keys, service accounts. Almost none of them land in a central identity inventory. A SANS Institute survey of more than 500 security professionals found 76% of organizations reporting growth in non-human identities, with 74% already running AI agents or automations that need their own credentials. The 2026 Verizon DBIR found employee use of unapproved shadow AI tools tripled, reaching 45% of the workforce. ([SecurifyAI](https://securifyai.co/blog/non-human-identity-why-ai-agent-are-outnumbering-your-workforce/))

The Cloud Security Alliance puts the ratio at 45 non-human identities for every human one. The direction is uniform: enterprises are accumulating a population of machine identities that security teams did not provision, do not track, and often do not know exist.

Here is the mechanism. A service account does not get offboarded. It does not rotate its own credentials. It does not fail an MFA challenge. Once it is exposed, it stays usable for months. As SpyCloud's chief intelligence officer Trevor Hilligoss put it: every one of these identities is a standing invitation that renews itself until someone notices. An AI agent with standing credentials and a long-lived token is not one invitation. It is an invitation that also picks the locks.

## The four-part identity discipline

An agent without an identity is anonymous inside your infrastructure. It calls APIs, reads data, commits code, and when something goes wrong you cannot tell it apart from the legitimate work. The fix is boring, which is why it works. Every agent gets an identity built from four parts:

1. **A unique, attributable identity.** One agent, one identity, distinct from every other agent and every human. Every action the agent takes gets attributed to that identity. No shared service accounts, no credentials passed between agents.
2. **Scoped credentials per capability.** The identity carries only what the agent's assigned work requires. Distinct credential scope per agent, enforced at runtime, not a standing grant to production. This is the permission review from [yesterday's post](https://blog.thinxai.net/posts/permission-is-the-policy/): see, send, change, reconstruct. Ask each question per agent, per credential.
3. **Expiry and rotation.** Credentials die on a schedule whether or not they have been misused. Long-lived tokens are the standing invitation. Short lifetimes plus automatic rotation turn a breach into an inconvenience.
4. **Monitoring and revocation.** The identity shows up in the inventory, its activity is watched, and there is a defined path to kill it. This is the decommission runbook from [Nobody Can Fire an Agent](https://blog.thinxai.net/posts/nobody-can-fire-an-agent/): an owner, kill criteria, and a shutdown that actually revokes the credentials.

None of this is new. It is the same identity lifecycle discipline enterprises built for humans: join, move, leave. Agents just need it applied at machine speed, because they are minted at machine speed. The inventory step was the first control in [We Need SOX for AI](https://blog.thinxai.net/posts/sox-for-ai/). Agent identities belong on it.

## Start with the inventory you think you have

The practical first move is the one the report's contradiction demands. Ninety-five percent of your security leadership believes the exposures are visible. Thirty-six percent are monitoring. Close that gap first. Run a discovery pass across cloud consoles, agent frameworks, SaaS platforms, and developer environments. Every credential you find gets four questions: whose agent is this, what can it touch, when does it expire, and who owns the revocation.

The credentials that have no owner get an owner or get deleted. There is no third option.

An agent is a worker inside your systems with no face, no badge, and, in most enterprises right now, no name. Give it one. Then give it rules.
