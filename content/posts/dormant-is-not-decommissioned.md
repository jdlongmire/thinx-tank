---
title: "Dormant Is Not Decommissioned"
date: 2026-10-23
tags: [agents, security, operations]
description: "Arrakis Security found 76 percent of agents had not run in 60 days while their credentials and triggers stayed live. Not running is not the same as retired, and the difference is a set of controls you can test."
hero: "img/posts/dormant-is-not-decommissioned/hero.png"
hero_alt: "Navy and amber hero graphic with bold text: Dormant Is Not Decommissioned"
draft: false
---

An agent that has stopped running has not stopped being reachable. That is the finding that should bother anyone who runs a fleet.

[Arrakis Security's 2026 Autonomous Agents Threat Report](https://www.wcia.com/business/press-releases/globenewswire/9851072/arrakis-security-report-finds-76-of-ai-agents-are-dormant-but-keep-their-credentials-and-connections/), published October 22, is based on anonymized production telemetry from thousands of agents in customer environments, collected over 12 weeks. The headline number is 76 percent. That share of agents had not run in 60 days, but their credentials still worked and their triggers still fired. Forty-four percent had not run in 180 days.

Dormant did not mean inert. Twenty-four percent of the dormant agents could be started by an unsigned webhook from outside the organization. Seventy percent of all agents in the sample could reach sensitive systems such as cloud storage, AI services, and marketing platforms, and Arrakis says almost none of those connections had verified data loss prevention in place. Eighty-two percent of agents carried at least one exposure, and 46 percent of those carried more than one.

Arrakis chief executive Tal Baron put the ownership problem plainly: "When an employee leaves, their access is removed the same day. When an agent stops being used, nobody removes anything, because in most companies nobody owns it."

I have written that sentence in other forms. In [Nobody Can Fire an Agent](https://blog.thinxai.net/posts/nobody-can-fire-an-agent/) I argued that most shops have no named owner, no kill criteria, and no shutdown runbook for an agent they approved in a hurry. The Arrakis numbers show what happens after the approval meeting ends and attention moves on. The agent does not get fired. It does not get retired. It just stops being used, and everything that made it dangerous stays switched on.

Three things stay live when use stops, and they need to be named separately because they fail separately.

The credential stays live. A key, a token, or a service account that worked on the last run still works on day 90 of silence unless someone revokes it at the issuer or it was built to expire. Silence is not expiry. I made the provider-side version of this point in [Decommission the Keys First](https://blog.thinxai.net/posts/decommission-the-keys-first/): deleting a record on your side is housekeeping, revoking at the provider is the control, and the only proof is a test call where the old credential fails.

The trigger stays live. A schedule, a webhook, a queue subscription, or an event rule that can start the agent does not care that the team moved on. The unsigned webhook finding matters here. If an outside caller can start a dormant agent without a signature, dormancy is not a safety state at all. It is a parked process with a public doorbell.

The connection stays live. The tool grants, the data access, and the downstream systems the agent could reach on its last run are still there on the next start, whoever starts it. That is why the 70 percent reach figure belongs in the same conversation as the dormancy figure. A dormant agent with no reach is clutter. A dormant agent that can reach cloud storage is standing access waiting for a trigger.

I wrote in [Standing Privilege Is Dead](https://blog.thinxai.net/posts/standing-privilege-is-dead/) that access should be provisioned for a task and removed when the task ends. Dormant agents are where that rule goes to die. Nobody decided to keep the privilege. Nobody decided anything. Time passed, and the privilege stayed by default.

The fix is not a cleanup project once a year. It is a clock, an automatic pause, and a reactivation gate.

First, put a dormancy clock in the inventory. Every agent record needs a last-run date, a last successful run date, an owner, and a next review date, all readable in one place. If the inventory cannot answer which agents have not run in 60 days, you do not have an inventory. You have a list of things you once built. Arrakis could produce the 76 percent figure from telemetry. Most shops cannot produce it for their own fleet at all.

Second, let inactivity change the state automatically. At a threshold you set in advance, 30 days, 60 days, pick one and write it down, the platform should disable external triggers and pause the credential. Not delete the agent. Pause it. The work to restart it should be small for a legitimate owner and impossible for an unsigned webhook. Test that last part directly: send the unsigned call and confirm it fails. A control you have not tried to break is a description, not a control.

Third, treat reactivation as re-approval, not as resume. An agent that slept for three months returns to a changed shop. The model under it may have changed, the tools it calls may have changed, and the data it can reach may have grown. I covered the version problem in [The Agent You Approved Is Not the Agent Running](https://blog.thinxai.net/posts/the-agent-you-approved-is-not-the-agent-running/). Reactivation should ask the same questions approval asked: who owns it now, what can it touch, what can it spend, and what would make you shut it down for good. If nobody can answer the ownership question, the answer to reactivation is no. That is the decommission decision arriving by a different door.

Fourth, prove the dormant list every cycle. Pull the agents past threshold. For each one, show the trigger state, the credential state, and the owner response, with dates. A paused credential should show a failed test call. A disabled webhook should show a rejected test start. An agent with an owner who wants it kept should show a new review date, not a verbal assurance. This is the identity discipline from [Every Agent Needs an Identity](https://blog.thinxai.net/posts/every-agent-needs-an-identity/) applied to the end of life instead of the start: if you cannot name it, scope it, and revoke it, you do not control it.

None of this requires buying a new platform first. It requires a query against your own inventory, a threshold written down before the argument starts, and an owner name that is a person, not a team alias. Run the query this week. If the dormant share is anywhere near the Arrakis figure, the next incident review in your shop may not be about an agent that acted badly. It may be about an agent nobody remembered, started by a call nobody signed, using a credential nobody revoked.
