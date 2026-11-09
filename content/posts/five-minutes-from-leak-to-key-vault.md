---
title: "Five Minutes From Leak to Key Vault"
date: 2026-11-09T07:20:00-06:00
tags: [security, credentials, non-human-identity, incident-response]
description: "Microsoft Threat Intelligence saw an agent move from searching GitHub for a leaked secret to exfiltrating Azure Key Vault data in five minutes. Rotation that waits for a ticket, an owner, or proof of abuse is now too slow."
hero: "img/posts/five-minutes-from-leak-to-key-vault/hero.png"
hero_alt: "Navy and amber hero graphic with bold text: Five Minutes From Leak to Key Vault"
draft: false
---

Five minutes. That is the whole clock.

On November 5, [Microsoft Threat Intelligence reported](https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/) that threat actors are using an agentic AI offensive framework, ARTEX, to search public GitHub repositories for exposed secrets. The searches combine a target organization name with secret keywords and cloud or AI service names, at volume. In at least one case Microsoft observed, an agent went from scanning GitHub for secrets to exfiltrating data from Azure Key Vault in just five minutes.

Searching public code for credentials is an old technique. What changed is the follow-through. A human operator had to find a repository, read the code, work out what a credential opened, and try it. The agent does the searching, the analysis, and the follow-on actions in one run, with little hands-on work from the operator in between.

That compression breaks a remediation habit most organizations still run on. We treat an exposed secret as a hygiene finding. Open a ticket. Find the owner. Ask whether the credential is still in use. Schedule a rotation window. Delete the commit and call the exposure closed. Every step in that sequence assumed the attacker was working at human speed too.

## The retry is the tell

The detail in the Microsoft report that stayed with me is not the five minutes. It is the retries.

When the agent hit Azure Resource Manager with the wrong API version and got an HTTP 400 back, it corrected the version and retried about 28 seconds later, and got a 200. A second sequence took about 60 seconds to fix. A third took about 80. That is troubleshooting, done at machine speed, without a person deciding to try again.

It also signs in early and often. Microsoft observed successful service principal sign-ins as early as October 28, across dozens of applications and multiple tenants. In some cases a credential for a multitenant application was compromised at the vendor that owned the application, then used against downstream tenants. The targets were the operations that return more credentials: storage account keys, App Service settings, connection strings, AI and machine learning connections, and Azure Kubernetes Service credentials. One good secret became a search for the next ones.

The pool is not small, either. In its companion write-up, [GitGuardian reported](https://blog.gitguardian.com/the-agents-have-now-found-your-secrets-on-github-artex-is-abusing-public-secrets-right-now/) that its State of Secrets Sprawl 2026 counted 28.65 million new hardcoded secrets in public GitHub in 2025, and that 64 percent of the valid secrets it found in 2022 were still active. Old leaks did not expire. They waited.

## Deleting the commit fixes nothing

Microsoft states the point plainly: publicly exposed credentials remain usable until revoked or rotated, and removing the original disclosure alone does not remediate the exposure.

I have made a version of this argument before, from the retirement side, in [Decommission the Keys First](https://blog.thinxai.net/posts/decommission-the-keys-first/): when a system goes away, revoke its keys at the provider and verify the old keys fail before you shut anything down. The ARTEX case makes the same point from the exposure side, with a timer attached. If revocation is step four in your process, behind ownership research and a change window, your process is slower than the attack it is supposed to answer.

So I would reorder the work.

First, revoke first and investigate second. For a secret exposed in public code, pre-authorize the on-call responder to rotate or revoke it without waiting for proof of abuse and without waiting for the owning team to confirm it is unused. If rotation breaks something, that breakage is visible, bounded, and fixable. A service principal signing in from an address you do not recognize is none of those things. Breakage you choose beats access you did not.

Second, kill the long-lived secret where you can. Microsoft recommends moving OAuth applications away from secret-based authentication and toward managed identities, which removes the client secret from code entirely. That is the durable fix. A secret that lives for a year and sits in a config file is a standing invitation, and I argued in [Standing Privilege Is Dead](https://blog.thinxai.net/posts/standing-privilege-is-dead/) that standing access is the problem in its general form. Short-lived, federated credentials expire on their own. Long-lived ones expire when someone remembers.

Third, move detection to the sign-in, not the file. Finding the leaked file is useful, but the file may sit in a repository you do not own, copied from one of yours. Microsoft's detection guidance points at the identity logs: look for one address authenticating to three or more service principals, for failed sign-ins followed by a success, and for one application requesting tokens across Resource Manager, Key Vault, Storage, and Graph inside a short window. That pattern is the attack, whether or not you ever find the original leak. I made the broader point in [If the Provider Has to Tell You, You Have No Detection](https://blog.thinxai.net/posts/if-the-provider-has-to-tell-you/): if the first notice comes from outside, your own detection did not fire.

Fourth, answer the vault question before you have to. Microsoft's containment guidance says to rotate everything stored in any Key Vault the affected application could read. That instruction is easy to write and hard to execute if nobody has mapped which applications can read which vaults. Do that mapping now, per application identity, the same inventory work I described in [Every Agent Needs an Identity](https://blog.thinxai.net/posts/every-agent-needs-an-identity/). Include vendor applications in the map. The multitenant case in this report is the warning: a secret you never held, belonging to an application you never wrote, can still open your tenant if that application has standing access to it.

## Run the five-minute test

Here is the test I would run this week. Pick one production application credential. Pretend it appeared in a public repository ten minutes ago. Time the response honestly. Who can revoke it right now, without a meeting? Is that authority written down and pre-approved, or does it depend on finding a specific person? Do you know what breaks when it rotates? Do you know every vault, storage account, and mailbox that identity can reach? Can your logs show you, within the hour, whether that identity signed in from somewhere new?

If any answer is no, you do not have a secrets problem. You have a clock problem, and the clock is now five minutes.

The fix is not a better scanner, though scanning helps. The fix is a response that runs at the speed of the thing it answers: revocation pre-authorized, credentials short-lived by default, detection on identity behavior, and a written map from every application identity to everything it can read. Build that, and a leaked secret becomes a bad five minutes for the attacker instead of for you.
