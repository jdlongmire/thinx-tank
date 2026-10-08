---
title: "The Blocker Is Not the Control Plane"
date: 2026-10-08
tags: [ai governance, runtime enforcement, control plane]
description: "Collibra's acquisition of trail ML proves runtime governance is now a buy decision. But a blocker is one control, not a framework: policy authorship, ownership, and the evidence trail are still yours to build."
hero: "img/posts/blocker-is-not-control-plane/hero.png"
hero_alt: "Navy and amber hero graphic with bold text: The Blocker Is Not the Control Plane"
---

On October 5, Collibra acquired Munich-based AI governance startup trail ML. The write-up at [Complete AI Training](https://completeaitraining.com/news/collibra-acquires-trail-ml-to-automate-ai-governance/) lays out the package: agents that review evidence and assess controls, requirements mapped against the EU AI Act, ISO 42001, and NIST AI RMF, and an integration that lets Collibra block a non-compliant agent action before it executes. The startup claims 4x faster deployment of AI solutions and 70 percent faster compliance execution, attributed to customer outcomes rather than lab benchmarks.

I read this as a milestone, and not for the reason in the headline. This is the first big-platform admission that pre-deployment governance is the wrong speed for agents. Autonomous systems act in milliseconds. Traditional reviews happen in days or weeks. Buying trail ML is Collibra saying, on the record, that point-in-time assessment is finished as a model. That is exactly the argument in my [SOX for AI](https://blog.thinxai.net/posts/sox-for-ai/) series, and the market just spent money to agree with it.

So buy the thesis. Do not confuse the thesis with the product.

The core of trail ML's approach is a Copy-on-Write mechanism: agents propose actions but cannot write to customer systems without human approval. That is a good control. It is also one control. A control plane needs four things, and the blocker is only the third:

1. **Inventory.** Which agents exist, what they can touch, who built them.
2. **Ownership.** One named human who answers for each agent's behavior.
3. **Controls.** The interceptor. This is what Collibra just bought.
4. **Audit.** An immutable, attributable record of what was allowed, what was blocked, and why.

Nobody sells you one through four in a single acquisition. Items one, two, and four are organizational work. They live in your registry, your org chart, and your evidence store. A vendor can give you a very good number three and you will still fail an audit if the other three are stubs.

Before you trust any runtime-governance demo, run it through these four questions:

1. **Who writes the policy, and in what form?** If the rule cannot be written as code, versioned, and diffed, it is not a control. It is a preference with a dashboard. I argued for policy-as-code in [Git Is the Control Plane](https://blog.thinxai.net/posts/git-is-the-control-plane/); it applies to bought blockers exactly as much as to home-grown ones.
2. **Is the block in the execution path, or advisory?** A flag that fires after the fact is surveillance, not enforcement. Ask to see the action fail in the demo, not a warning.
3. **Does every gate produce an attributable record?** If the block does not land in an audit trail, your auditors will not care that it exists. An interceptor that blocks silently is a black box with good intentions. See my piece on running your own [incident log](https://blog.thinxai.net/posts/publish-your-own-incident-log/); the same logic applies to the vendor's block events.
4. **Who adjudicates when the blocker stops real work?** Every control has a false-positive rate. The exception workflow is the actual product, not the blocker. If the vendor cannot show you the override path and the record it leaves behind, you are buying future outages with excellent intentions.

There is also a second-order effect nobody in the acquisition announcements mentions. Runtime enforcement does not remove the compliance bottleneck. It moves it. Instead of reviewing attestations every quarter, your people write policy-as-code and triage exceptions in real time. That is a different skill set and, usually, a different org chart. The acquisition buys you no part of that transition.

The Copy-on-Write idea is worth keeping, because it names the right execution posture: agents operate in propose mode until a principal with authority moves them to commit mode. That is the same authority-envelope discipline I keep coming back to. But it is a design principle, not a product feature. Principles have to be enforced by the plane, across every agent, no matter whose logo is on the blocker.

Buy the blocker. Build the plane.
