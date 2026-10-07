---
title: "Standing Privilege Is Dead"
date: 2026-10-07
tags: ["ai-agents", "identity", "zero-standing-privilege", "enterprise-security"]
draft: false
description: "At Navigate 2026, SailPoint announced Zero Standing Privilege for people, service accounts, and AI agents: just-in-time provisioning with conditions, replacing always-on access. With 79% of enterprises running agents in production and 2% governing them, the identity I wrote about two days ago is only half the job. The other half is taking away the keys."
hero: "img/posts/standing-privilege-is-dead/hero.png"
hero_alt: "Navy and amber graphic with the headline Standing Privilege Is Dead"
---

"Standing privilege is dead." That is SailPoint CTO Chandra Gnanasambandam, speaking at the company's Navigate 2026 conference in Austin yesterday. The occasion was a launch called Zero Standing Privilege: just-in-time provisioning, with conditions, replacing always-on access for people, service accounts, and AI agents alike. ([SailPoint press release](https://www.sailpoint.com/press-releases/sailpoint-unlocks-a-secure-agentic-era-with-autonomous-identity-security))

The stat behind the launch comes from SailPoint's Horizons of Identity Security report: 79% of enterprises already run AI agents in production, but only 2% have deployed identity security tools built to govern them. Sit with those two numbers for a moment. Four out of five enterprises have a production agent fleet. One in fifty has the tooling to govern what the fleet touches. The gap between the fleet and the governance is the whole problem in one number.

Two days ago this blog gave every agent an identity: a name, scoped credentials, expiry, and a revocation path. ([Every Agent Needs an Identity](https://blog.thinxai.net/posts/every-agent-needs-an-identity/)) This post is the part that makes the identity matter. An identity tells you who acted. Standing privilege is what that identity can still do when nobody is watching. If an agent's credentials never expire and cover everything it might someday need, the identity is a label on a loaded gun.

## The standing grant assumes a review that never happens

The reason standing access is the agent problem, not a background IAM concern, is speed. SailPoint president Matt Mills put it plainly at the same conference: no security admin is reviewing access for a group of agents making 10,000 tool calls a second. That is not a staffing problem. It is a physics problem.

A standing grant, a permanent API key, a role that never expires, a token minted at deployment and never rotated, is built on the assumption that someone reviewed it once and will review it again. Humans get a version of that through join-move-leave: a person changes roles, a manager notices eventually, access gets trimmed. Agents change tasks every few seconds. Their access has to change that fast, which means it has to be computed, not administered.

Standing privilege also has a persistence problem that agents make worse. A service account that never rotates its credentials is already a standing invitation. An AI agent with standing credentials is the same invitation plus an actor: it does not just hold the keys, it can decide to use them, be tricked into using them, or have them stolen from its context at machine speed. The SpyCloud finding from the identity post still applies: each of these identities is an invitation that renews itself until someone notices. With agents, nobody notices, because there is no quarterly review cycle for a fleet of 1.3 billion.

## Three parts, all boring

Zero standing privilege is not a product feature. It is a design principle: the credential follows the work, not the worker. Three parts:

1. **Credentials mint at need, not at hire.** The agent gets its credential when the task starts, bound to the task: this identity, these systems, this scope, this purpose. When the task ends, the credential dies. Nothing carries over to tomorrow's work. No standing key means no standing target.
2. **Everything has a TTL.** Any credential that outlives one task expires on a clock, not on someone's suspicion. Short lifetimes plus automatic rotation turn a stolen token from a permanent foothold into a window that closes by itself. The expiry is a property of the credential, not a ticket in a queue.
3. **Effective privilege, not paper privilege.** Just-in-time provisioning with conditions means the grant is evaluated against what the agent can actually touch at runtime, not the role description written when the account was created. Right-sizing is continuous: the permission shrinks back the moment the justification does. This is the permission review from [The Permission Is the Policy](https://blog.thinxai.net/posts/permission-is-the-policy/), enforced per execution instead of per quarter.

None of this is exotic. It is the identity lifecycle discipline from the identity post, applied at the cadence agents actually operate. The SOX-for-AI framework I have been building in this series starts with inventory: every agent, every credential, every permission. ([We Need SOX for AI](https://blog.thinxai.net/posts/sox-for-ai/)) Zero standing privilege is what the inventory is for.

## What changes Monday

Start with the inventory. For every standing credential an agent holds, ask one question: what breaks if this credential dies tonight? If nothing breaks until the agent next runs, the credential should not exist between runs. Replace it with issuance on start and death on completion.

For the credentials that cannot die tonight, attach a clock. Pick the shortest TTL the work tolerates: hours, not months. Then write the revocation path next to it, from [Nobody Can Fire an Agent](https://blog.thinxai.net/posts/nobody-can-fire-an-agent/): an owner, kill criteria, a shutdown that actually revokes. The expiry is a policy, not a hope.

One caution. Just-in-time issuance does not answer what the agent should be allowed to do. It answers how long it holds the answer. You still need the four-question review: see, send, change, reconstruct. JIT makes the approved answer expire before it can be abused. It does not approve the answer.

## The vendors are selling the plane

SailPoint is selling a platform for this now. Their Autonomous Agents are a fleet of specialized agents that watch the agentic lifecycle: continuously monitoring runtime actions, intercepting threats, right-sizing permissions at machine speed. That is the right shape. It is also worth noticing what it implies.

Governing agents at machine speed is itself an agentic job. The governance plane is becoming agents watching agents. That is exactly what [the control plane post](https://blog.thinxai.net/posts/agentic-execution-control-plane/) described: the plane enforces budget, scope, and policy at runtime, because review time is already gone. SailPoint arrived at the same conclusion from the identity side. The control plane and the identity plane are converging on the same point: enforcement has to live inside the execution loop, not outside it.

Which is why the CTO's line works as a title. The always-on grant belonged to an era when the number of identities was small enough to review and the speed of their actions was slow enough to watch. Agents ended both. Give your agents names. Then take their keys.
