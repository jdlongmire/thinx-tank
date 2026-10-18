---
title: "Decommission the Keys First"
date: 2026-10-18
tags: [security, credentials, operations]
description: "OpenCode's breach ran through a legacy system that was already being decommissioned, and the provider keys stored in it stayed live. Retirement has an order: revoke the credentials at the provider first, then shut the system down."
hero: "img/posts/decommission-the-keys-first/hero.png"
hero_alt: "Navy and amber hero graphic with bold text: Decommission the Keys First"
draft: false
---

On Saturday, October 17, OpenCode disclosed a breach. According to [The Latent's report on the disclosure](https://thelatent.co/models/opencode-says-breach-tied-to-distillation-attack-exposed-users-ai-provider-keys), the company put the affected share at 1.4% of its Console users, the subset who had linked external providers. The email to affected users said someone had gained "unauthorized access to a legacy system that we were in the process of decommissioning," and that provider keys saved in their workspaces may have been exposed. Users were told to revoke the keys through each provider's own dashboard and to watch their accounts for unexpected usage. OpenCode said it is working with Anthropic, OpenAI, and Google on remediation.

Read the email's own wording again. Legacy system. In the process of decommissioning. The system was already on its way out. The keys inside it were not.

A provider key does not retire when the application holding it retires. An OpenAI or Anthropic key stays valid at the provider until someone revokes it there. Deleting the workspace, closing the console, and shutting down the server change where the key is stored. They do not change whether the key works. Whoever copies it before the shutdown owns a working, billable credential after the shutdown, and the system that might have told you it was taken is gone.

Some users said they saw unexpected charges before OpenCode posted anything publicly. The Latent notes it could not independently verify those individual reports, and OpenCode has not published a loss total. The numbers are not the lesson anyway. The structure is: long-lived third-party keys, stored in a system already marked for retirement, still good at the provider after the host was breached. That structure exists in plenty of shops that have never heard of OpenCode. Any tool, console, or internal platform where people paste provider keys becomes a credential store, whether anyone designed it as one or not.

I wrote about decommission discipline for agents in [Decommission by Design](https://blog.thinxai.net/posts/aioc-decommission-by-design/): named owner, kill criteria, a shutdown runbook. The same discipline applies to a system that holds credentials, and the order of operations matters more there. This is the order I want on any retirement I sign off on.

**Inventory what the dying system holds.** Not only its own service accounts. List every credential it stores for users, tenants, and integrations, and name the provider that issued each one. If the inventory starts from the system's own documentation, it will miss the keys users pasted in along the way. Start from the data instead: what secret material is actually in the store.

**Revoke at the issuer, not at the host.** Deleting a key from your database is housekeeping. Revoking it at the provider is the control. Those are different acts, and only one of them stops the key from working. After revocation, verify it: call the provider with the old key and confirm it fails authentication. A retirement record that says "keys deleted" without a failed-auth check against the provider is a claim, not evidence. I made the related point about agent identity in [Every Agent Needs an Identity](https://blog.thinxai.net/posts/every-agent-needs-an-identity/): a credential you cannot revoke is not an identity control, it is a hope.

**Revoke before shutdown, not after.** The sequence is: freeze new credential creation, inventory what is stored, revoke or rotate at each provider, verify the old keys fail, then decommission the infrastructure. Run it in the other order and you destroy the very interface and records you need to find out what was stored. A system in its last month also tends to get the least monitoring and the slowest patching, which is exactly when its stored keys are worth the most to an intruder. The retirement window is part of the exposure, not the end of it.

**Prefer keys that expire on their own.** Stored permanent keys are a convenience that converts every host breach into a provider breach. Where the platform allows it, use short-lived or narrowly scoped credentials issued for a task or a session, so a copied credential has a short useful life and a small blast radius. Where a tool genuinely has to hold user keys, treat that store as a vault: encryption, tight access, audit on every read. Calling it a settings table does not make it one.

**Cap the spend and alarm on it.** A stolen provider key announces itself as usage. A per-key or per-project spend cap bounds the loss, and an alert on unusual usage shortens the time between theft and detection. I argued the spend side in [Every Agent Needs a Budget](https://blog.thinxai.net/posts/every-agent-needs-a-budget/). In this incident the billing signal reached some users before the disclosure did. That is an argument for wiring the signal up on purpose, not for relying on customers to notice charges.

Run the check on your own retirement list this week. For each system scheduled to shut down, ask four questions. What credentials does it store? Whose are they? Where were they revoked, at the provider or only here? Who verified the old keys fail? If the honest answer to the third question is "we deleted the database," the system is not retired yet. The servers are off. The keys are still at work.
