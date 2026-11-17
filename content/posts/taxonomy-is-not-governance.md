---
title: "A Taxonomy Is Not a Governance"
date: 2026-11-16T19:20:00-06:00
tags: [agents, governance, mxm]
description: "McKinsey's agentic coworker runs on three kinds of memory: episodic, procedural, and semantic. The Triadic Memory Fabric covers the same ground and adds the part a taxonomy cannot: tiered admission that decides what a record may do before an agent acts on it."
hero: "img/posts/taxonomy-is-not-governance/hero.png"
hero_alt: "Three kinds of memory on one side, three governed tiers on the other, in amber on navy."
draft: false
---

McKinsey published a guide for banking CIOs in October, [The Rise of the Agentic Coworker](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-rise-of-the-agentic-coworker-a-banking-cios-guide-to-the-next-wave-of-ai), and one of its five foundations is memory. Their sentence is worth quoting in full: three kinds of memory keep coworkers from treating every case as if it were the first. Episodic memory preserves what happened before: prior actions, exceptions, and outcomes for a client. Procedural memory encodes how the work should be done, including where authority limits apply. Semantic memory grounds the coworker in the bank's own vocabulary: product codes, policy definitions, risk appetite, and regulatory citations. A write-back loop records human corrections, so the next coworker inherits the case, the method, and the language.

My first reaction was recognition. This is essentially the Triadic Memory Fabric (TMF), the memory architecture I have been building and running under the MxM fabric. The convergence is real, and I do not think it is an accident. Anyone who runs agents against real work for long enough discovers that memory has to be structured, or the agent treats every case as its first. McKinsey has now said that to the banking industry, with their distribution behind it. Good. The ground is shared. What the two designs do with that ground is not the same, and the difference is the part that decides whether memory helps you or hurts you.

## The kinds describe content. They say nothing about standing.

Take any one of McKinsey's three kinds and ask where it lives. An episode can be one run's log, one team's case history, or the enterprise's ratified record of what happened. A procedure can be a habit one agent picked up, a workstream's standard method, or a governed policy nobody may edit without review. A definition can be a local shorthand, a department's glossary, or the canonical vocabulary the whole institution reports against. The kind is the same in all three cases. The standing is completely different, and standing is what determines whether a record should drive an action.

The TMF splits on exactly that axis. Its three scopes are Macro, Meso, and Micro: the ratified record at the top, the workstream's working memory in the middle, the individual actor's record at the base. Any kind of content can land at any scope. What the scope fixes is who may write it, what evidence it needs, and how far it reaches. McKinsey's split tells you what a memory is. The fabric's split tells you what a memory may do.

## Admission before the fact, not a stop at the point of action

McKinsey's design has one authority control, and it sits inside procedural memory: the procedure encodes where authority limits apply, and the coworker stops at the limit for human approval. That is a real control, and it is better than none. But notice where it operates. It operates at the point of action, at the moment the agent is about to do something, and it depends on the procedure being right and the agent honoring it.

Admission in the TMF runs earlier. A record enters a tier only through that tier's gate: Macro by ratification, Meso by the workstream owner with evidence behind it, Micro by the actor doing the work. The boundary test is need-to-act: a fact belongs in the shared fabric if another actor needs it to act, and not otherwise. Entries age, and stale entries are marked stale rather than quietly trusted. A record that was never admitted is not sitting in the fabric waiting to be misused. There is nothing to stop at the point of action, because the unadmitted record was never there.

The write-back loop shows the gap plainly. McKinsey has human corrections written back so the next coworker inherits them. Written back to where, at what standing, on whose say-so? A correction is the most valuable kind of record an operation produces, and also the easiest to get wrong. In a taxonomy, it lands wherever the loop puts it. In a fabric, it enters at the tier its authority warrants, carries its evidence with it, and displaces what it corrects through a visible supersession. Same loop. Different discipline.

## Why this is not a quibble

I wrote last week about [the next run inheriting the last run's leftovers](/posts/next-run-inherits-leftovers/): shared services an agent can write to become memory that crosses runs, with no admission decision anywhere in the chain. That is the failure mode of memory without governance. The records accumulate, later runs read them as ground truth, and nobody can say which ones deserved that standing. A taxonomy of kinds does not protect against it. You can sort the leftovers into episodic, procedural, and semantic piles and still have no idea which pile entries an agent may act on.

So here is the test I would put to any memory architecture, McKinsey's included. Who can write the procedure your agent will follow next month, and what did they have to show before it counted? When two scopes disagree, which record wins, and where is that written? When a record goes stale, what marks it, and what stops an agent from treating it as current? An architecture that answers those three questions has a governance. One that only names the kinds has a filing system.

## The convergence is the news

None of this diminishes what McKinsey published. The largest consulting firm in the world is now telling bank CIOs that agent memory comes in kinds and must be layered, and that is a genuine marker of where the field has arrived. I have argued the same structure from the build side, most fully in [The MxM Fabric Defined](/posts/the-mxm-fabric-defined/), where memory is one of six governed surfaces rather than a feature of the model.

But a taxonomy is not a governance, and the distance between the two is where agent programs will succeed or fail in the next two years. The kinds tell you what memory is. The tiers tell you what memory may do, who said so, and on what evidence. Build both. If you can only build one first, build the tiers, because an ungoverned taxonomy is just a well-labeled version of the leftovers problem.
