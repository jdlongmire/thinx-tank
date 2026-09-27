---
title: "From Strategy to Coherence: Building an Enterprise Architecture Strategy That Can Govern Change"
date: 2026-09-27
tags: ["enterprise-architecture", "strategy", "governance"]
draft: false
description: "A research-grounded method for turning enterprise intent into coherent architectural choices, investments, roadmaps, standards, and adaptive governance."
---

Enterprise Architecture strategies are often recognizable by their artifacts.

There is a target-state diagram. A technology roadmap. A set of principles. A standards catalog. Perhaps a capability map and a collection of reference architectures.

All of those can be useful. None of them, by itself, is a strategy.

The strategic question is harder:

> **What architectural choices must this enterprise make so that thousands of decentralized decisions remain coherent with its intent?**

That question changes the work.

It means Enterprise Architecture (EA) strategy cannot begin with a preferred technology stack or end with a picture of the desired future. It has to explain how enterprise intent becomes architectural choice, how those choices constrain investment and delivery, and how the enterprise will learn when those choices need to change.

My working definition is:

> **Enterprise Architecture Strategy is the enterprise's reasoned set of architectural choices, principles, guardrails, and transition commitments that translate strategic intent into coherent capability, investment, technology, and delivery decisions, with explicit mechanisms for governance, evidence, and adaptation.**

That definition is a synthesis, not a quotation from an EA framework. It emerged from comparing established EA research and standards against empirical work on where EA actually contributes value, and where the claims outrun the evidence.

The resulting method is compact:

**INTENT → INTERPRET → CHOOSE → EXECUTE → LEARN ↺**

The simplicity is deliberate. A strategy has to be understandable enough to govern decisions while retaining enough structure to preserve traceability.

![Infographic titled "From Strategy to Coherence: A Practical Path to Enterprise Architecture Strategy," showing the five stages (Intent, Interpret, Choose, Execute, Learn), the eight tests of coherence, and the line "Architecture becomes strategy when it governs consequential choices."](/img/posts/building-a-coherent-enterprise-architecture-strategy/from-strategy-to-coherence.jpg)

*The five-stage method and the eight coherence tests, summarized in one view.*

## Strategy does not translate itself

One of the most useful findings in the EA literature is also one of the easiest to overlook: business strategy rarely provides enough specificity to determine stable process and technology choices.

MIT CISR's work on operating models addresses this gap. Ross, Weill, and Robertson describe an operating model as the organization's intended level of business-process integration and standardization, then connect that operating logic to the enterprise architecture required to execute it (Ross, Weill and Robertson, 2006).

That gives us an important architectural principle:

**Intent must be interpreted before it can constrain architecture.**

A strategic objective such as "improve customer intimacy," "operate as one enterprise," "accelerate product introduction," or "exploit AI" is not yet an architecture decision.

The architect has to ask what that objective means operationally.

Which capabilities must change? Which processes must integrate? Which information must be shared? Where is standardization valuable? Where is autonomy intentional? Which risks constrain the design? What must be common across the enterprise, and what should remain local?

The operating model is one useful abstraction for answering those questions. It is not the only one. Capabilities, value streams, information flows, stakeholder concerns, regulatory constraints, ecosystem relationships, security boundaries, and data requirements all help translate strategic intent into architecture-relevant demands.

That is the work of **INTERPRET**.

## 1. INTENT: establish what the enterprise is trying to accomplish

Architecture should begin with an explicit mandate.

That means identifying the mission or purpose, strategic objectives, desired outcomes, value priorities, risk priorities, and relevant external forces.

The output is not yet an architecture. It is an **architecture mandate**.

A useful first test is simple:

> Can every major architecture initiative be traced to an enterprise outcome, material constraint, or risk?

If the answer is no, the enterprise may have architecture activity without architecture strategy.

## 2. INTERPRET: determine what the intent means for the enterprise

Interpretation should establish the operating implications of the enterprise's intent through some combination of operating-model requirements, prioritized capabilities, value streams, information needs, stakeholder concerns, current-state evidence, constraints, assumptions, and decision criteria.

Capabilities are particularly useful because they tend to be more stable than organizational structures or individual systems. Gartner's capability-based planning guidance explicitly connects business and IT strategy to technology roadmaps and investment planning through capabilities (Madan and Jhawar, 2025).

But a capability map is not an architecture.

Capabilities tell us what the enterprise must be able to do. They do not, by themselves, tell us how information should be governed, which processes require integration, which platforms should be shared, where technology should be standardized, how trust boundaries should work, or what investment sequence is feasible.

Capabilities are therefore best treated as a **traceability spine**, supplemented by the views required to make consequential decisions.

The other half of interpretation is evidence.

The NIST CSRC definition of Enterprise Architecture retains a useful discipline from the U.S. federal EA lineage: EA includes a baseline architecture, target architecture, and sequencing plan, grounded in the mission, required information, required technologies, and transitional processes (NIST, 2026).

A baseline matters because strategy that ignores the actual enterprise is aspiration.

But the baseline should be decision-sufficient rather than encyclopedic. The purpose of current-state analysis is to establish the facts necessary to make choices, expose constraints, understand dependencies, and identify meaningful gaps.

## 3. CHOOSE: make the architecture strategy

This is the center of the method.

A target-state diagram can show where the enterprise would like to go. A strategy has to explain the choices that govern how it will get there.

Those choices include what the enterprise will standardize, integrate, centralize or federate, reuse, retire, tolerate, and deliberately avoid. They also determine where autonomy is intentional and which options remain open because the evidence does not yet justify commitment.

This is why I distinguish architecture strategy from framework compliance.

The TOGAF Standard provides architecture-development scaffolding, methods, guidance, governance concepts, and supporting material. The Open Group explicitly describes the 10th Edition as configurable for different architecture practices and use cases (The Open Group, 2022). That makes TOGAF useful method infrastructure.

It does not make the enterprise's choices for it.

Those choices require judgment.

### Stop pretending we can predict the endpoint

Traditional EA disciplines correctly emphasize baseline, target, and transition. We should retain that logic.

What deserves reconsideration is the assumption that the target must always be a highly specified endpoint.

Gartner's 2026 research on future-state architectures argues that volatility and uncertainty have weakened the usefulness of rigid long-range target states. Its proposed alternative emphasizes guidance, guardrails, tiered capability development, iteration, and learning (Blosch, van der Heiden and Ganter, 2026).

That is directionally consistent with a more precise distinction:

**Commit where coherence requires commitment. Preserve options where prediction would manufacture certainty.**

A future-state architecture can therefore contain different kinds of assertions:

- **Commitments:** decisions the enterprise is prepared to govern now.
- **Target characteristics:** properties the future enterprise should exhibit.
- **Guardrails:** boundaries within which decentralized teams may choose.
- **Options:** alternatives intentionally kept open.
- **Hypotheses:** beliefs that should be tested before becoming commitments.

That produces a future state that can guide action without pretending the architect knows everything the enterprise will need several years from now.

## 4. EXECUTE: connect architecture to money and delivery

An architecture strategy that does not affect investment is largely advisory.

Van den Berg et al. studied survey data from 142 participants and compared organizations in the top and bottom quartiles for IT investment-decision outcomes. The higher-performing group reported greater EA maturity, greater use of diagnostic and actionable EA artifacts, and more strategic insights during investment preparation. The authors conclude that EA can add value in the preparation of IT investment decisions, while also calling for further testing of the propositions generated by the study (van den Berg et al., 2019).

That supports an explicit **investment coherence** test:

> Do funded initiatives correspond to the capabilities, dependencies, risks, and architecture gaps the strategy says matter?

Execution translates architecture choices into:

**Gaps → Transition Architectures → Dependencies → Investment Priorities → Roadmaps → Standards → Governance → Delivery**

NIST's baseline-target-sequencing formulation provides useful discipline here. TOGAF likewise provides mechanisms for architecture development and governance. Gartner's recent roadmap guidance emphasizes roadmaps as living, outcome-driven decision assets rather than static detailed plans (Khilare, 2026).

The architecture roadmap should therefore expose dependencies, decision points, capability increments, investment implications, and the architectural conditions that must hold through intermediate states.

## 5. LEARN: make the strategy falsifiable

An architecture strategy contains assumptions about the enterprise and its future.

Those assumptions should be testable.

The enterprise should observe delivery evidence, architecture conformance, exceptions, capability outcomes, investment performance, operational measures, technology changes, strategic changes, and failures of underlying assumptions.

Then it should adapt.

MIT CISR provides an important caution here. Ross and Quaadgras reported that a 2011 survey of 146 senior IT leaders found that organizations benefiting from their digitized platforms relied on practices promoting organizational learning, including cost transparency, debate over architectural exceptions, post-implementation reviews, and architecture-aware investment decisions (Ross and Quaadgras, 2012).

Architecture therefore has to propagate into how the enterprise thinks and decides.

## Test the strategy for coherence

The five-stage method describes how to build the strategy. It still needs tests.

I currently use eight.

1. **Vertical coherence.** Can architecture choices be traced upward to intent and downward to implementation?
2. **Horizontal coherence.** Are business, information, application, technology, security, integration, workforce, and operating-model decisions mutually compatible?
3. **Temporal coherence.** Do the current state, transition states, and intended future form a plausible sequence?
4. **Investment coherence.** Does funding reinforce the architecture rather than quietly contradict it?
5. **Governance coherence.** Do principles, standards, decision rights, and exceptions reinforce the same strategic choices?
6. **Evidential coherence.** Are consequential claims about the current state, constraints, risks, and outcomes traceable to evidence?
7. **Adaptive coherence.** Is it clear what new evidence or event would cause the strategy to change?
8. **Decision coherence.** When independent teams face materially similar decisions, do they converge where the enterprise intends commonality and legitimately diverge where autonomy is intended?

That last test may be the most operational measure of all.

Architecture exists in the decisions people make.

## Be careful what value you claim

Enterprise Architecture has accumulated some ambitious claims over the years. The research warrants more discipline.

Gong and Janssen's systematic literature review found substantial variation in what researchers and practitioners mean by EA and how they claim it creates value. Only about half of the articles in their review provided empirical evidence for their EA value claims. Their conclusion is especially important: EA should be understood as enabling value creation through context-dependent mechanisms rather than as something that inherently creates value by existing (Gong and Janssen, 2019).

Other empirical work gives us useful, bounded evidence.

Hazen et al. studied 190 manufacturers and found that EA strategic orientation and assimilation were associated with greater agility and indirectly with firm performance (Hazen et al., 2017). That is meaningful evidence for that population. It is not a universal law.

Pattij, van de Wetering and Kusters surveyed 110 EA stakeholders and found that the relationship between EA management and organizational agility was mediated by IT capabilities (Pattij, van de Wetering and Kusters, 2019).

Taken together, these studies support a more defensible formulation:

> **EA strategy creates conditions, constraints, shared understanding, decision information, and governance mechanisms through which capabilities, investments, and delivery can create value.**

That is enough. We do not need to promise magic.

## GenAI changes the economics of continuous architecture

Historically, continuous architecture has been expensive.

The enterprise's strategic intent, capability models, application inventories, standards, architecture decisions, roadmaps, investments, risks, and implementation evidence live across different repositories and organizational boundaries. Architects spend enormous effort assembling enough of that information to reason about consequences.

GenAI can change the economics of that information work.

A grounded AI-enabled architecture capability can help retrieve and synthesize evidence, maintain traceability, identify inconsistencies, compare proposals against architectural principles and guardrails, generate candidate viewpoints, expose assumptions, analyze dependencies, model scenarios, and detect potential architecture drift.

That does not transfer architectural authority to the model.

The human architect remains responsible for determining which sources are authoritative, resolving semantics, interpreting strategic intent, judging trade-offs, disposing of machine-generated findings, and owning consequential decisions.

I call that operating principle **Human-Curated, AI-Enabled (HCAE)**.

Curation is continuous. It begins with source authority and continues through interpretation, verification, decision, and feedback. It is not an approval click after an AI system has generated an answer.

## A practical construction sequence

If I were standing up an EA strategy tomorrow, I would work through this sequence:

1. Establish the architecture mandate.
2. Define the outcomes the enterprise is trying to produce.
3. Interpret the operating implications of those outcomes.
4. Identify and prioritize the affected capabilities.
5. Establish decision-sufficient evidence about the current state.
6. Make drivers, constraints, assumptions, and decision criteria explicit.
7. Make the strategic architecture choices.
8. Define target characteristics, commitments, guardrails, options, and deliberate exclusions.
9. Identify gaps, transition architectures, and dependencies.
10. Align investments and roadmaps to those transitions.
11. Encode the choices into standards, reference architectures, governance, and decision rights.
12. Measure outcomes and test assumptions.
13. Adapt when the evidence changes.

Then ask the eight coherence questions.

If the answers do not line up, the architecture is telling you something.

## Architecture becomes strategy when it governs consequential choices

The purpose of EA strategy is not to predict every system an enterprise will operate five years from now.

It is to make today's distributed decisions add up to an intentional enterprise while preserving the ability to learn.

That requires enough architecture to constrain decisions, enough evidence to justify those constraints, enough governance to preserve coherence, and enough humility to change when reality proves an assumption wrong.

The method is simple enough to remember:

**INTENT → INTERPRET → CHOOSE → EXECUTE → LEARN ↺**

The hard part is **CHOOSE**.

That is where architecture becomes strategy.

---

## References

Blosch, M., van der Heiden, G. and Ganter, F. (2026) *Build Future-State Architectures to Provide Guidance and Guardrails*. Gartner, 4 August 2026. https://www.gartner.com/en/documents/8226161

Gong, Y. and Janssen, M. (2019) 'The value of and myths about enterprise architecture', *International Journal of Information Management*, 46, pp. 1–9. doi:10.1016/j.ijinfomgt.2018.11.006.

Hazen, B.T., Bradley, R.V., Bell, J.E., In, J. and Byrd, T.A. (2017) 'Enterprise architecture: A competence-based approach to achieving agility and firm performance', *International Journal of Production Economics*, 193, pp. 566–577. doi:10.1016/j.ijpe.2017.08.022.

Khilare, A. (2026) *Why Most EA Roadmaps Fail and How to Build One That Works*. Gartner, 8 July 2026.

Madan, P. and Jhawar, A. (2025) *Ignition Guide to Business Capability-Based Investment Planning*. Gartner, 6 May 2025.

National Institute of Standards and Technology (NIST) (2026) *Enterprise Architecture (EA), CSRC Glossary*. Definitions sourced from CNSSI 4009-2022 and related federal sources. https://csrc.nist.gov/glossary/term/enterprise_architecture

Pattij, M., van de Wetering, R. and Kusters, R. (2019) 'From Enterprise Architecture Management to Organizational Agility: The Mediating Role of IT Capabilities', *BLED 2019 Proceedings*, paper 31.

Ross, J.W. and Quaadgras, A. (2012) *Enterprise Architecture Is Not Just for Architects*. MIT CISR Research Briefing, XII(9).

Ross, J.W., Weill, P. and Robertson, D.C. (2006) *Enterprise Architecture as Strategy: Creating a Foundation for Business Execution*. Boston, MA: Harvard Business School Press. https://cisr.mit.edu/publication/enterprise-architecture-as-strategy

The Open Group (2022) *The TOGAF Standard, 10th Edition*. Reading, UK: The Open Group. https://publications.opengroup.org/standards/togaf

van den Berg, M., Slot, R., van Steenbergen, M., Faasse, P. and van Vliet, H. (2019) 'How enterprise architecture improves the quality of IT investment decisions', *Journal of Systems and Software*, 152, pp. 134–150. doi:10.1016/j.jss.2019.02.053.
