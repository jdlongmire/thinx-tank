# WP-EA-STRATEGY-0001 — Building a Coherent Enterprise Architecture Strategy

Status: active research. Repository: jdlongmire/thinx-tank.
Owner: JD Longmire.

## Purpose

Develop and validate a practical method for constructing a coherent Enterprise Architecture (EA) strategy that connects enterprise intent to executable architectural choices, investment priorities, roadmaps, standards, governance, and measurable outcomes.

This work package is research-led. It will examine established EA, business architecture, operating-model, capability-planning, strategic-planning, governance, and contemporary AI-era approaches before institutionalizing a Thinx-Tank method.

## Research question

**How should an enterprise construct and continuously maintain an architecture strategy that is coherent with enterprise strategy, grounded in current-state evidence, explicit about architectural choices and trade-offs, executable through investment and roadmaps, and adaptable as conditions change?**

## Working thesis

An EA strategy should not be a catalog of technologies, a target-state diagram, or an inventory of architecture initiatives.

It is a reasoned set of enterprise-level architectural choices that explains:

1. what outcomes the enterprise is trying to enable;
2. what operating model and capabilities those outcomes require;
3. what current-state realities constrain change;
4. what architectural principles and target-state characteristics must hold;
5. what choices, trade-offs, and deliberate exclusions follow;
6. what transition states and investments are required;
7. how standards and governance preserve coherence during decentralized execution; and
8. how evidence and outcomes will drive adaptation.

## Candidate strategy chain

**Enterprise Intent → Outcomes → Operating Model → Capabilities → Current-State Evidence → Architectural Drivers & Constraints → Principles → Strategic Architecture Choices → Target State → Gaps → Transition Architectures → Roadmaps & Investment → Standards & Governance → Delivery → Measures & Evidence → Adaptation**

This chain is provisional and will be tested during research.

## Coherence tests

A coherent EA strategy should demonstrate:

- **Vertical coherence:** every significant architecture choice traces upward to enterprise intent and downward to implementation.
- **Horizontal coherence:** business, information/data, application, technology, security, integration, and operating-model decisions do not contradict one another.
- **Temporal coherence:** current, transition, and target states form a plausible sequence.
- **Investment coherence:** funded initiatives correspond to prioritized capability and architecture gaps.
- **Governance coherence:** standards, principles, decision rights, and exception processes reinforce the strategy.
- **Evidential coherence:** claims about the current state, constraints, risks, and outcomes are traceable to evidence.
- **Adaptive coherence:** the strategy can change when assumptions, evidence, technology, mission, or business conditions change without losing architectural integrity.

## Research streams

### RS-1 — Definitions and conceptual boundaries
Distinguish enterprise strategy, EA strategy, enterprise architecture, operating model, target architecture, technology strategy, roadmaps, standards, and governance.

### RS-2 — Strategy-to-architecture translation
Research methods for converting mission, business strategy, objectives, outcomes, value streams, and operating-model choices into architectural drivers.

### RS-3 — Capability-based planning
Evaluate business capability models as the stable bridge between strategic intent, investment, architecture, and delivery.

### RS-4 — Current-state evidence
Determine the minimum useful baseline required for strategic decisions without turning EA strategy development into exhaustive inventory collection.

### RS-5 — Future-state architecture
Research methods for expressing target-state characteristics, architecture principles, strategic choices, trade-offs, dependencies, and deliberate non-goals.

### RS-6 — Transition and roadmapping
Study sequencing, transition architectures, dependency management, investment alignment, optionality, technical debt, and outcome-driven roadmaps.

### RS-7 — Governance and decision rights
Examine how principles, standards, reference architectures, ARBs, exceptions, funding gates, and decision rights maintain coherence.

### RS-8 — Measurement and adaptation
Identify measures for architecture outcomes, strategic alignment, reuse, complexity, risk, delivery effectiveness, and strategy refresh triggers.

### RS-9 — AI-era implications
Research how GenAI, agentic systems, reusable platforms, data/AI governance, and Human-Curated, AI-Enabled practices alter both architecture strategy and the method used to create it.

### RS-10 — Comparative framework analysis
Compare relevant elements of TOGAF, MIT CISR, NIST/federal EA concepts, Gartner EA research, capability-based planning, and other credible primary or authoritative sources. Adopt useful mechanisms only where they strengthen the method.

## Research discipline

- Prefer primary and authoritative sources.
- Distinguish source claims from Thinx-Tank synthesis.
- Preserve provenance for consequential assertions.
- Record conflicting approaches rather than silently harmonizing them.
- Separate empirical findings, practitioner frameworks, standards, and proposed synthesis.
- Assign confidence to major research conclusions where appropriate.
- Treat the candidate method as falsifiable and revisable.

## Planned deliverables

- [x] Work-package charter.
- [ ] Annotated research bibliography and evidence ledger.
- [ ] Comparative framework matrix.
- [ ] EA strategy vocabulary and ontology.
- [ ] Coherence model and tests.
- [ ] Step-by-step EA strategy construction method.
- [ ] Research-backed strategy template.
- [ ] Executive one-page method.
- [ ] 3x3 explanatory graphic.
- [ ] Example worked strategy using a non-proprietary enterprise scenario.
- [ ] HCAE augmentation model for strategy development and maintenance.
- [ ] **Publication deliverable: sourced Thinx-Tank blog post** presenting the validated method, evidence, limitations, and practical application.
- [ ] Publication-quality source notes with primary/authoritative links and claim-level traceability.
- [ ] Final human review and acceptance.

## Relationship to WP-EA-HCAE-0001

WP-EA-HCAE-0001 explains Enterprise Architecture and the leverage GenAI provides to the architect.

This work package addresses the deeper method: **how the architect actually constructs a coherent EA strategy.**

The HCAE WP is therefore a companion and downstream communication asset. Findings here may refine its Strategy → Architecture → Roadmaps → Standards → Delivery model.

## Initial acceptance criteria

The final method must:

1. begin with enterprise intent and outcomes rather than technology preferences;
2. expose assumptions, constraints, trade-offs, and strategic choices;
3. connect strategy to capabilities and architecture;
4. incorporate evidence about the actual current state;
5. define a target state without assuming a single-step transformation;
6. produce actionable transition roadmaps and investment implications;
7. connect architecture strategy to standards, governance, and decision rights;
8. provide traceability from intent through delivery and outcomes;
9. include measurable feedback and explicit adaptation triggers;
10. work in both traditional and AI-enabled enterprises; and
11. preserve human architectural accountability under HCAE; and
12. culminate in a publication-ready Thinx-Tank article whose substantive external claims are supported by traceable sources.

Human-Curated, AI-Enabled (HCAE)


## Publication disposition

The terminal deliverable of this work package is a **Thinx-Tank blog post with sources**. Research artifacts are intermediate evidence and method-development products supporting that publication.

The article should:

- define the problem of EA strategy coherence in practitioner-accessible terms;
- distinguish enterprise strategy, architecture strategy, target architecture, roadmaps, standards, and governance;
- present the validated Thinx-Tank strategy chain and coherence tests;
- identify which elements derive from established research/frameworks and which are Thinx-Tank synthesis;
- use primary or authoritative sources wherever available;
- cite sources adjacent to consequential factual or framework claims and include a references section;
- report meaningful disagreement or limitations in the literature rather than manufacture consensus;
- include practical guidance for constructing and maintaining an EA strategy;
- address the implications of GenAI and HCAE for continuous architecture strategy; and
- be published only after research conclusions and source provenance have been reviewed.

The intended publication location is `content/posts/` in this repository after human acceptance.
