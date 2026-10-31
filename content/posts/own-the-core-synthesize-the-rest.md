---
title: "Own the Core. Synthesize the Rest."
date: 2026-10-17
tags: [enterprise-architecture, agents, open-source]
description: "Part three of the agentic EA series. The architecture repository is the core an EA org must own. Everything around it can be synthesized from open source parts. The expensive option is the other one: conceding the core to a COTS platform."
hero: "img/posts/own-the-core-synthesize-the-rest/hero.png"
hero_alt: "Navy and amber hero graphic with bold text: Own the Core. Synthesize the Rest."
draft: false
---


In [The Architecture Repository](https://blog.thinxai.net/posts/the-architecture-repository/), I published the concrete structure of the architecture repository: numbered baselines, typed artifacts, policy checks, human ratification in the tooling. The responses it draws tend to arrive as two questions. First: where are the diagrams, the dashboards, the impact analysis, the portal? Second, right behind it: so the alternative is a commercial EA platform, and you are against buying one?

Both questions assume the repository is competing with a platform. It is not. It is the core the platform would have owned. This piece is about the difference.

## What the core is

An EA function has exactly one asset it cannot rent: the record of the architecture itself. The models, the standards, the decisions, the roadmaps, the evidence of what the estate actually is. Everything else the function touches (views, diagrams, portals, reports) is a rendering of that record, produced for a particular audience at a particular moment.

Renderings are replaceable. Records are not. When the record lives in a vendor's store, in the vendor's format, under the vendor's roadmap, every rendering you love is hostage to a contract. When the record lives in your repository, renderings become a build-out question: which ones do we need, in what order, at what cost. A missing view is a backlog item. It is not a gap in the architecture, and it is not an argument for surrendering the core.

That is the whole claim of the first two pieces in this series, restated as an ownership question. [Agentic Enterprise Architecture](https://blog.thinxai.net/posts/agentic-enterprise-architecture/) set out the model and the operation. The repository piece made it concrete. This one defends the ownership.

## Three doors

![Three doors: buy the platform, build from scratch, or own the core and synthesize the rest](/img/posts/own-the-core-synthesize-the-rest/figure-1-three-doors.png)

*Figure 1: The three postures an EA org can take toward its own platform. Only one of them is platform on demand.*

**Door 1: buy the platform.** A COTS EA system costs a bucket of money before the first model is drawn, and the bucket refills annually. In exchange the vendor holds your record. Their data model becomes your metamodel. Their release cycle becomes your ceiling. When the contract ends, and contracts end, the exit is priced in migration pain, which is not an accident of the business model. It is the business model. This is the concession in the debate, and it should be named as one: conceding the core to a landlord.

**Door 2: build from scratch.** The opposite error. Every portal, every report, every integration hand-built by the EA team. It is slow, it burns the team's scarce hours on commodity plumbing, and it carries a standing vanity risk: a platform your own org built becomes a pet, defended past its usefulness because its builders are in the room. Owning the core does not require inventing the surroundings.

**Door 3: own the core, synthesize the rest.** The record in your repository. The surroundings composed from open source components, each one proven in production somewhere else, each one replaceable without touching the record. Build-out follows proven need: a view gets built when a named audience actually needs it, not when a vendor's feature checklist says a serious EA function should have one.

## The synthesis shelf

![The synthesis ring: open source parts composed around the core](/img/posts/own-the-core-synthesize-the-rest/figure-2-synthesis-ring.png)

*Figure 2: A starting ring, not a shopping list. Each tile names a function and one proven open source way to fill it.*

Synthesis is not a euphemism for hand-rolling. The shelf is stocked:

- **Policy.** The standards in the repository compile to rules, and [Open Policy Agent](https://www.openpolicyagent.org/) is the mature open source engine that evaluates them.
- **Catalog and portal.** [Backstage](https://backstage.io/), Spotify's open source developer portal, already runs software catalogs on exactly this pattern: descriptors held as files in Git, rendered as a browsable catalog. Architecture stakeholders get the same surface over the same kind of source.
- **Diagrams.** Views generated from the models with [diagrams.net](https://www.diagrams.net/) or [Mermaid](https://mermaid.js.org/), refreshed on merge. A diagram becomes a build product, not a drawing someone maintains.
- **Publishing.** An [MkDocs](https://www.mkdocs.org/) site renders the tree for the readers who will never open Git, which is most of the org, and that is fine. They read renderings. The record stays where it belongs.
- **Modeling exchange.** For the work that genuinely wants a canvas, [Archi](https://www.archimatetool.com/) is open source, and the ArchiMate exchange format moves models in and out of the repository without making the tool the record.
- **Agent operation.** The schemas, standards, and runbooks package as skills, so assistants draft and check work against the same sources the humans ratify from.

Swap any tile for a better one next year and the architecture does not notice. That replaceability is not a side benefit. It is the test that tells you the core really is the core: everything around it can change, and the record stands.

## Reading the direction

The industry phrase of the moment is platform on demand, and it is worth being precise about which door it names. Door 1 is platform by license: capability rented on the vendor's terms, record included in the rent. Door 2 is platform by labor: capability produced by your own team's hours, at your own pace. Door 3 is the only one that is on demand in any meaningful sense: a platform assembled from available parts, around a core you own, recomposed as needs change, increasingly operated by agents that read the record directly.

That last clause is where the trend actually points. An agent cannot work a COTS platform's internal database the way it works a repository: proposing changes as diffs, being validated by policy, being refused by branch protection. The more of the platform's operation agents take on, and they will take on most of the mechanical operation, the more the record has to live somewhere an agent can be governed. A bucket of money spent today on a platform agents cannot operate is a bucket spent against the direction.

## The question to ask

When the COTS proposal is on the table, and it will be, ask two questions of it. What does the bucket buy that we cannot synthesize from the shelf when a named need actually arrives? And what do we surrender permanently in exchange? The first question produces a feature list, and feature lists can be argued. The second produces one answer: the record, the history, and the right to recompose our own platform without permission.

Own the core. Synthesize the rest. Replace any part of the surroundings whenever a better part appears, and never ask a landlord for the keys to your own architecture.


---

**Follow-up:** The series continues in [The Governed Control System](https://blog.thinxai.net/posts/the-governed-control-system/), on why agentic enterprise architecture is best framed as a governed control system for the digital ecosystem, with SARS as its operating model and this record at its center.
