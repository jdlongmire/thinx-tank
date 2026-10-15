---
title: "There Is No Device to Enroll"
date: 2026-10-15
tags: [agents, identity, security, byoa]
description: "Personal AI agents are entering the enterprise through OAuth consent, saved passwords, and API keys, acting as the employee who connected them. BYOD gave IT a device to manage. Bring your own agent gives IT an identity problem instead."
hero: "img/posts/bring-your-own-agent/hero.png"
hero_alt: "Navy and amber hero graphic with bold text: There Is No Device to Enroll"
draft: false
---

On October 12, [The Hacker News published a contributed piece from Token Security](https://thehackernews.com/2026/10/bring-your-own-agent-your-employees.html) with a plain title: bring your own agent. Employees are connecting personal AI assistants to work systems, and the assistants are already logged in. Not pasting text into a chatbot. Acting, with permission, inside email, calendars, file stores, and code repositories.

I have spent a month writing about agents the enterprise deploys on purpose. This is the other fleet. Nobody procured it, nobody provisioned it, and in most tenants nobody can list it.

The comparison that matters is BYOD. Bring your own device was painful, but it gave IT a thing to enroll. A phone has a serial number, an operating system, a management profile you can install and a device you can wipe. A personal agent has none of that. It runs on a vendor's servers, or inside a browser, or on a laptop you already trust. There is no device to enroll. There is only a set of grants, tokens, and sessions wearing an employee's name.

Look at how these agents get in. Every path is one your people already use for ordinary apps:

- **OAuth consent.** The agent asks for access to Google Workspace, Microsoft 365, or Slack. The employee clicks Allow. If your tenant lets users consent to third-party apps on their own, that click is the whole procurement process.
- **A text thread.** Some personal agents work over messaging. The user links an account, texts instructions, and the agent acts through whatever was connected.
- **Saved passwords.** Agent browsers sign in with stored credentials. To the application on the other end, the login looks like the employee.
- **API keys and personal access tokens.** For integrations with no official path, employees mint long-lived credentials and hand them over.
- **The laptop itself.** A local agent reads what the machine can read: files, notes, calendars, mail. The perimeter never sees a new device because there is not one.

Three problems follow, and none of them is fixed by a policy PDF that says personal agents are not allowed.

**First, your logs cannot tell the agent from the employee.** The Token Security piece puts it bluntly: nothing in the session distinguishes the two. Your audit trail says the employee read the file, sent the message, or opened the repository. Maybe they did. Maybe their agent did it at 2 a.m. while working a task the employee described in one sentence that morning. I made the attribution argument for deployed agents in [Every Agent Needs an Identity](https://blog.thinxai.net/posts/every-agent-needs-an-identity/). Personal agents fail it by default, because they borrow an identity instead of getting one.

**Second, the agent inherits everything and needs a sliver.** A personal agent acting as an employee gets that employee's full reach: every shared drive, every channel, every system years of role changes have piled up. The actual job is narrow. Summarize my mail. Watch my calendar. Draft replies from these three folders. The grant is the person's whole working life. I covered the corporate version of this failure in [Delegation Is Not Inheritance](https://blog.thinxai.net/posts/delegation-is-not-inheritance/), where sub-agents copied a parent agent's authority instead of receiving a narrower one. A personal agent is inheritance with no parent in sight, just a consent screen.

**Third, offboarding does not reach it.** When an employee leaves, you disable the account. That is the start, not the end. OAuth grants, refresh tokens, API keys, and active sessions can outlive the account if they were issued in ways your identity provider does not centrally revoke. And there is a harder layer the Token Security authors name honestly: the agent's memory. A personal agent that spent a year reading an employee's work knows things. There is no console today that makes a personal agent forget your projects when its owner walks out. You can cut access. You cannot yet cut retained knowledge, which means the time to bound what the agent sees is before it sees everything.

So what do I do with this on a normal Tuesday, without declaring war on tools my people find genuinely useful?

**Close the consent door first.** In most tenants the cheapest control is also the strongest: users should not be able to grant third-party apps access to mail, files, and calendars without admin approval. Route consent through a review. That one setting converts an invisible fleet into a queue of requests you can actually read.

**Build the inventory from the grants, not from a survey.** Do not ask employees what they connected. They will forget, or guess, or tell you what they think you want to hear. Pull the evidence: OAuth grants to agent vendors in your identity provider, sign-ins arriving from vendor cloud ranges, long-lived API keys with no named owner, endpoint findings for local agent installs. That list is the fleet. It will be longer than you expect.

**Attribute, then shrink.** Every grant on that list gets a human owner by name, the same discipline from [Standing Privilege Is Dead](https://blog.thinxai.net/posts/standing-privilege-is-dead/) applied to access nobody remembers approving. Then right-size it. Read-only where read-only does the job. Three folders, not the whole drive. Expiry dates on tokens instead of credentials that live forever. Where the platform cannot shrink the grant, say so in writing and treat that agent as unapproved for sensitive systems. An honest no is better than a grant you pretended was narrow.

**Test retirement before you need it.** Pick one departed employee from last quarter. Chase their grants, tokens, and sessions through every system on your inventory and prove each one is dead. Time it. If the exercise takes days and ends with two maybes, your offboarding runbook has a hole shaped exactly like a personal agent, and now you know before an incident teaches you.

None of this requires banning personal agents. A ban you cannot detect is not a control, it is a hope. The employees bringing these tools are usually your most productive people, and they are telling you something about where the sanctioned tools fall short. Listen to that signal. Then govern the part you can actually govern: the identity, the grant, and the exit.

BYOD took a decade and a lot of MDM software to sort out, and it started with admitting the devices were already inside. This round starts the same way. The agents are already logged in. The only open question is whether your inventory says so.
