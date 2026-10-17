---
title: "The Architecture Repository"
date: 2026-10-17
tags: [enterprise-architecture, ai-agents, architecture-as-code]
description: "The follow-up to Agentic Enterprise Architecture: the concrete Git repository an EA org actually runs on. Numbered baselines, the four focus areas as folders at every level, schemas and policies checked by CI, and a ratification map written as CODEOWNERS."
hero: "img/posts/the-architecture-repository/hero.png"
hero_alt: "Navy and amber hero graphic with bold text: The Architecture Repository"
draft: false
---


In [Agentic Enterprise Architecture](https://blog.thinxai.net/posts/agentic-enterprise-architecture/), I laid out a position: an operating model (Strategy, Architecture, Roadmaps, and Standards at the enterprise, systems, and solutions levels), artifacts held as code, and agents operating the practice under human ratification. A position without an artifact is an opinion. This piece is the artifact: the Git repository the model lives in, structured so that the claims in the first piece are checkable rather than aspirational.

## Where the shape comes from

The layout borrows its grammar from the repository template I use for my own working repos. Not the contents, which are built for a different job, but three structural rules that have held up under daily use.

First, numbered baselines. Top-level areas carry numbers, so the structure has a canonical order that every reader and every agent shares. Nobody debates where a thing goes, because the numbering is the map.

Second, repetition of the same inner shape. In my template, each baseline repeats a small set of sub-areas. Here, the repetition is the model itself: the four focus areas appear as folders inside every level.

Third, the structure is machine-checked. My template ships a layout verifier, a script that fails when a file lands outside the structure or a required area goes missing. The architecture repository keeps that idea and extends it: schemas for every artifact type, checked in CI on every proposed change.

## The structure

![One repository, numbered baselines: the four focus areas repeat as folders at every level, and the structure itself is machine-checked](/img/posts/the-architecture-repository/figure-1-repository-structure.png)

*Figure 1: The reference structure. Ten top-level entries, three of them files at the root, everything else a numbered baseline.*

**00-meta-model/** is the constitution. It holds the schema for every artifact type the repository allows (capability, system, interface, standard, decision, roadmap item), the naming rules, the decisions that govern the repository itself, and the layout verifier. If an object is not described here, it does not exist anywhere else in the tree.

**01-enterprise/, 02-systems/, 03-solutions/** are the three levels, and each holds the same four folders: strategy, architecture, roadmaps, standards. A system's architecture lives beside its own strategy and its own standards, and the enterprise level keeps the same shape at wider scope. A new architect learns the structure once, and it holds at every level. An agent can too, which is the point: the tree is the index, and it never has to be searched, only read.

**04-work-packages/** holds bounded change records: the unit of architecture work, scoped and owned, worked as pull requests against the baselines they change. This is where the TOGAF ADM cycle lands in practice. A pass through the method produces work packages; work packages produce changes; changes are ratified and merged.

**05-evidence/** is the return path [the first piece](https://blog.thinxai.net/posts/agentic-enterprise-architecture/) argued for. Observed-state snapshots from the real estate, validation results, and the drift register live here. Drift between the merged model and the observed estate is recorded as a defect with an owner, which is the standard I set out in [Done Means Accounted For](https://blog.thinxai.net/posts/done-means-accounted-for/), applied to architecture itself.

**06-operations/** holds the runbooks: the reconciliation cadence, how a new level or system gets admitted to the repository, how agent access is granted and revoked.

**policies/** holds the standards compiled into policy-as-code. The human-readable standard lives in the standards folder of its level; its machine-checkable form lives here, and CI fails a change that lets the two drift apart.

Three root files finish it. **CODEOWNERS** is the ratification map: each path in the tree names the humans who approve changes to it, so the Architecture Review Board's authority is expressed as review ownership rather than meeting attendance. **AGENTS.md** is the contract for agents working the repository: what they may propose, what they may never merge, and what records they must leave, under the governed-execution pattern I described in [Governed Execution in Multi-Mode Agent Harnesses](https://doi.org/10.5281/zenodo.23367869). **README.md** is the human entry point.

## What a typed artifact looks like

Every artifact is a file with a schema-checked header. A system, for example:

```yaml
id: SYS-014
name: claims-processing-platform
level: systems
owner: enterprise-architecture
status: target
interfaces: [INT-003, INT-007]
standards: [STD-DATA-002, STD-SEC-001]
```

The header is what CI validates, what agents read first, and what makes the tree queryable without a database. The prose below the header carries the architect's reasoning. Machines check the shape; humans read the argument.

## How a change moves

![How a change moves: propose, validate, ratify, merge, reconcile](/img/posts/the-architecture-repository/figure-2-change-lifecycle.png)

*Figure 2: One path for every change. Agents can run stages 1, 2, and 5. Stage 3 is human, and branch protection is what makes that a fact instead of a norm.*

A change starts as a pull request: a model edit, a decision record, a roadmap adjustment, a new standard. CI validates it against the schemas in 00-meta-model and the rules in policies/. CODEOWNERS routes it to the humans who own the affected cells, and they ratify or reject it. On merge, the change becomes the record: author, diff, validation result, decision, all in the history. Then reconciliation compares the merged model against observed state and files any drift in 05-evidence, where it opens the next proposal.

This is also where the repository doubles as the distribution channel for the agents that work it. Packaged as skills, the schemas, standards, and runbooks are exactly what an assistant needs to draft a conforming proposal, which is the distribution model [The Enterprise Architecture Codex](https://www.eacodex.ai/book/chapter-06-the-enterprise-architecture-codex/) argues for. The repository is not just where the architecture lives. It is how the architecture teaches its operators.

## Starting an EA org on it

Do not build the whole tree on day one. Start with 00-meta-model and the enterprise level: the schemas, the four enterprise folders, CODEOWNERS naming the board, branch protection on. Admit systems as they are actually modeled, one work package at a time. Let solutions arrive through delivery work rather than by migration project. And resist importing the old document archive wholesale: the archive stays where it is as read-only history, and the repository models the estate forward from the current state. An architecture repository that begins by trying to describe everything describes nothing well.

The [first piece](https://blog.thinxai.net/posts/agentic-enterprise-architecture/) in this series argued the discipline was never the problem; the medium and the manual operation were. This is the medium, concretely: one repository, numbered baselines, checked structure, human ratification written into the tooling. An EA org that stands this up at the start does not have an architecture documentation problem to fix later, because it never created one.
