title: "Govern the Door, Not the Agent You Do Not Own"
date: 2026-11-03T07:22:00-06:00
tags: [agents, identity, governance, credentials]
description: "Banks are blocking their customers' outside agents or writing liability for them into their terms, because a customer's password cannot carry a delegation. If you run a portal, the work is at your boundary: an agent door that is scoped, attributable, and revocable."
hero: "img/posts/govern-the-door/hero.png"
hero_alt: "Navy and amber hero graphic with bold text: Govern the Door"
draft: false
---

Most of my recent posts have been about agents inside the enterprise: the ones you buy, build, or approve. This one is about the agents you did none of those things for. They belong to your customers. You did not select them, you cannot patch them, and you will never see their release notes. They arrive at your portal with your customer's password, and from your authentication logs they look exactly like your customer.

The banks just showed everyone how this plays out. [SecureWorld's account of the Axios reporting](https://www.secureworld.io/industry-news/ai-agents-in-bank-accounts) describes major U.S. banks detecting third-party AI agents operating inside customer accounts, in many cases with credentials the customers handed over themselves. Some agents reportedly contacted bank call centers. One bank executive told Axios the hard part is telling an agent a customer authorized apart from one operating on its own.

Hold the reporting at the right strength. Morgan Stanley said it has not observed rogue agents on its platforms, and I have seen no documented case of a completed unauthorized transfer in this reporting. The problem is not a proven loss. The problem is a session the bank cannot attribute, carrying authority the bank never scoped.

## Two answers so far, and neither is a mechanism

The first answer is to block. On JPMorgan's October 13 earnings call, CEO Jamie Dimon said the bank would not let just any outside agent operate inside its systems. Citi says third-party agents may not log in to customer accounts or transact on its platforms. Bank of America is limiting agent access to consumer deposits while it works on who is liable for a payment an agent authorizes. Blocking is honest, and for money movement it is probably right today. It is also temporary. Customers want these tools, and an agent locked out of one firm will be pointed at another.

The second answer is to write terms. Wells Fargo updated its Online Access Agreement on November 2, and Section 15 takes effect November 24. [Tech Times' walk through Section 15](https://www.techtimes.com/articles/329947/20261103/wells-fargo-just-made-you-legally-responsible-every-transaction-your-ai-agent-makes.htm) quotes the operative language. Under Section 15(d), instructions from a customer's agent are treated as initiated and authorized directly by the customer, without further verification. Section 15(e) adds, in the bank's own capitals, that use of an AI agent is at the customer's own risk. A customer who revokes an agent must keep evidence of the revocation and stays responsible for the agent's activity until the bank is notified. Section 15 also lets the bank require agent registration, limit what agents can do, or block them outright.

Read that section as an architecture document, because that is what it is. Every clause exists because a password cannot carry a delegation. It cannot say which agent acted, what the customer actually granted, when the grant ended, or whether this action sat inside it. The bank is answering those questions with contract language because its login cannot answer them at all. Terms decide who pays after the fact. They do not decide what happens in the session.

I have made the borrowed-login argument from the inside twice recently: in [Bring Your Own Agent](https://blog.thinxai.net/posts/bring-your-own-agent/), where an employee's personal agent inherits the employee's grants, and in [yesterday's post](https://blog.thinxai.net/posts/agent-wore-a-contractors-login/) on the contractor's agent reported inside a Pentagon production system. The customer side is worse in one respect. Inside, you can at least issue the agent its own role, as I argued in [Give the Agent a Role, Not Your Login](https://blog.thinxai.net/posts/give-the-agent-a-role/). Outside, you cannot issue anything to software you do not control. You control exactly one thing: the door it comes through.

## Build the agent door

An agent door is a separate, deliberate way in for software acting for a customer. Not a second login page. A grant with a shape. Four tests tell me whether a portal has one.

First, attribution. Can a session record name the agent separately from the customer, in the log, at the time of the action? If your records only show the customer, every later dispute becomes an argument about intent with no evidence. This is the same point I made in [Every Agent Needs an Identity](https://blog.thinxai.net/posts/every-agent-needs-an-identity/), moved outside the firewall: the identity can be a registered agent tied to a customer grant rather than an employee record, but it has to exist as its own entry.

Second, scope that starts at read. The banks' working compromise is read-only access through approved connectors, and it is the right first shape: balances and history yes, money movement no. Writes, when they come, should be capped, named, and expiring. Pay this bill, up to this amount, until this date. That kind of grant is what the Personal Agent Protocol, announced October 6 by Meta and Sierra with several banks as design partners, is trying to standardize, per the Tech Times account above. It is still a draft specification, not deployed infrastructure. Build toward its shape anyway: a scoped token issued for the agent beats a password shared with the agent, draft standard or not.

Third, revocation that runs on your side and leaves a receipt. Wells Fargo puts the evidence burden on the customer: prove you revoked, and you are liable until you notify us. Flip it. When a customer cuts off an agent at your portal, your system should kill the grant, confirm the kill in writing, and keep the record. Revocation a customer has to prove from screenshots is a support process designed to lose disputes, not a control.

Fourth, one story across terms, logs, and operations. If your agreement says an agent's actions are the customer's actions, but your fraud team cannot separate agent sessions in its tooling, the agreement is the only part of that system that works. Legal, security, and the service desk need the same definitions of an authorized agent, an exceeded grant, and a compromised one, before the first dispute, not during it.

## Where this lands

You do not need to run a bank for this to be your problem. Any organization with a customer portal, a partner integration, or a supplier login has the same shape: software will show up acting for people you have a relationship with, holding credentials you issued to those people. The only design questions are whether it comes through a door you built for it, with attribution, scope, and revocation you control, or through your customer's login, where you control none of the three and get to argue about it afterward.

Blocking buys time. Terms buy legal position. Neither buys visibility. Build the door while the traffic is still light enough to build it calmly.
