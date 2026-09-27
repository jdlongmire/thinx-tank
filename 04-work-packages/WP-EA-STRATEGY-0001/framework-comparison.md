# Comparative Framework Analysis — Coherent EA Strategy

Status: research synthesis in progress  
WP: WP-EA-STRATEGY-0001

## Evaluation dimensions

Each source/framework is evaluated against the same architecture-strategy questions:

1. How is enterprise intent translated into architecture?
2. Is an operating model or equivalent intermediate abstraction used?
3. How are capabilities represented?
4. How is current-state evidence handled?
5. How is future/target state expressed?
6. Are architectural choices and trade-offs explicit?
7. How are transitions and sequencing represented?
8. How are investment and portfolio decisions connected?
9. How do governance and decision rights preserve coherence?
10. How are outcomes measured and the strategy adapted?

## Comparison

| Dimension | MIT CISR | NIST / Federal EA lineage | TOGAF 10 | Gartner 2025–26 | Thinx-Tank synthesis |
|---|---|---|---|---|---|
| Starting point | Operating model derived from strategic needs | Mission and required information/technology | Business drivers, concerns, architecture vision and ADM context | Desired business/IT outcomes and enterprise demands | Enterprise intent and explicit outcomes |
| Strategy translation | Operating model specifies integration/standardization requirements | Mission translated into baseline, target and transition needs | Iterative ADM and configured practice | Outcome/capability-oriented future-state design | Intent → outcomes → operating model → capabilities |
| Capabilities | Critical business/process and IT capabilities | Present but not the central abstraction in the glossary definition | Supported through business architecture and guides | Strong emphasis on capability-based planning | Primary traceability spine, supplemented by value, information, systems and technology views |
| Current state | Existing platforms/process maturity matter | Explicit baseline architecture | Baseline architectures are standard ADM constructs | Six-building-block current-state assessment | Evidence sufficient to support choices; avoid exhaustive inventory |
| Future state | Enterprise architecture implements target operating model | Explicit target architecture | Target architectures across domains | Moving from rigid endpoint toward guidance, guardrails and options | Durable commitments + target characteristics + guardrails + options/hypotheses |
| Explicit choices | Strong at operating-model level: integration and standardization | Less explicit in definition | Principles, requirements, alternatives and decisions supported | Increasing focus on choices/options under volatility | Mandatory: choices, trade-offs, priorities and deliberate exclusions |
| Transition | Architecture maturity/platform evolution | Explicit transitional processes and sequencing plan | Transition architectures, opportunities/solutions and migration planning | Roadmaps tied to outcomes and change | Multiple plausible transition states with dependencies and decision points |
| Investment | Operating model guides IT investment | Sequencing connects change to implementation | Portfolio/migration mechanisms available | Capability-based investment planning emphasized | Investment coherence is a first-class test |
| Governance | Architectural thinking must propagate beyond architects | Governance/risk/control ecosystem is prominent in federal practice | Formal architecture governance capability | Governance included in future-state building blocks and roadmaps | Decision rights, standards, exceptions, ARB/funding gates integrated into strategy |
| Measurement/adaptation | Maturity and management practices | Mission/risk-oriented updates | Iterative ADM and change management | Living roadmaps; iterative learning; guardrails | Measures + evidence + explicit adaptation triggers |

## Framework dispositions

### MIT CISR

**Retain**
- Operating model as an important translation layer.
- Integration and standardization as strategic architectural choices.
- EA as organizing logic rather than technology catalog.
- Architectural thinking and management practices as enterprise capabilities.

**Extend**
- Explicit capability, information, ecosystem, security, data, platform, and AI concerns.
- Options and adaptation under high uncertainty.
- More explicit investment, decision-rights, and evidence traceability.

**Do not assume**
- That the classic operating-model typology alone is sufficient for contemporary digital ecosystems.

## NIST / Federal EA lineage

**Retain**
- Mission grounding.
- Baseline architecture.
- Target architecture.
- Transitional processes.
- Sequencing plan.
- Security/risk integration.

**Extend**
- Target state into target characteristics, guardrails and options where uncertainty makes endpoint prediction brittle.
- Stronger explicit architecture-choice and investment logic.

**Avoid**
- Treating exhaustive documentation as a prerequisite to strategic decision-making.

## TOGAF 10

**Retain as method scaffolding**
- Iterative architecture development.
- Multiple architecture domains.
- Architecture vision.
- Requirements discipline.
- Transition architectures.
- Opportunities/solutions and migration planning.
- Architecture governance and change management.
- Viewpoint/repository discipline.

**Position**
TOGAF is a configurable architecture-development standard, not itself the enterprise's architecture strategy. The Thinx-Tank method should be compatible with useful TOGAF mechanisms without becoming a restatement of ADM.

## Gartner 2025–26

**Retain for testing**
- Outcome-driven future-state architecture.
- Capability-based planning connecting strategy, portfolios and roadmaps.
- Governance, skills and investment as architecture-strategy concerns.
- Living, consumable roadmaps.
- Guidance and guardrails under volatility.
- Options-based architecture rather than one fixed predicted endpoint.

**Caution**
Much of the accessible material consists of primary Gartner abstracts and articles rather than full research and underlying datasets. Treat prescriptions as framework claims unless independently supported.

## Emerging Thinx-Tank method

The comparative evidence suggests five layers.

### Layer 1 — Intent

Establish:
- mission/purpose;
- strategic objectives;
- desired outcomes;
- value and risk priorities;
- relevant external forces.

Output: **Architecture mandate**.

### Layer 2 — Interpretation

Translate intent through:
- operating-model requirements;
- capabilities;
- value streams;
- information needs;
- stakeholder concerns;
- constraints and assumptions.

Output: **Architectural drivers and decision criteria**.

### Layer 3 — Choice

Determine:
- principles;
- strategic architecture choices;
- trade-offs;
- target characteristics;
- guardrails;
- deliberate exclusions;
- options that remain open.

Output: **EA strategy**.

This is the center of the method. A strategy is meaningful because it makes choices.

### Layer 4 — Execution

Translate choices into:
- gaps;
- transition architectures;
- dependencies;
- roadmaps;
- investment priorities;
- standards/reference architectures;
- governance and decision rights.

Output: **Executable change portfolio and architecture control system**.

### Layer 5 — Learning

Observe:
- delivery evidence;
- architecture conformance and exceptions;
- outcome measures;
- changing assumptions;
- new strategic demands;
- technology/environment changes.

Output: **Evidence-driven adaptation**.

## Proposed compact model

**INTENT → INTERPRET → CHOOSE → EXECUTE → LEARN ↺**

Underlying traceability chain:

**Enterprise Intent → Outcomes → Operating Model → Capabilities → Evidence → Drivers/Constraints → Principles → Architecture Choices → Target Characteristics/Guardrails → Gaps → Transitions → Roadmaps/Investment → Standards/Governance → Delivery → Measures/Evidence → Adaptation**

## Coherence gates

Before an EA strategy is accepted, ask:

1. **Intent:** Can every major architectural choice be traced to an enterprise outcome, constraint, or risk?
2. **Choice:** Does the strategy state what the enterprise will prefer, standardize, integrate, centralize/decentralize, reuse, retire, tolerate, and deliberately avoid?
3. **Cross-domain:** Are business, information/data, application, technology, security, integration, operating-model, and workforce implications mutually compatible?
4. **Transition:** Is there a plausible path from current reality to the intended architecture?
5. **Investment:** Do portfolio and funding decisions correspond to the architecture's priorities and dependencies?
6. **Governance:** Can decentralized delivery teams tell which decisions are constrained, delegated, or require exception?
7. **Evidence:** Are consequential current-state claims, assumptions and constraints traceable?
8. **Adaptation:** Is it clear what evidence or event would cause the strategy to change?

## Research disposition

The current synthesis rejects three weak formulations:

- **EA strategy = target-state diagram.** Insufficient because it omits choices, transitions, investment, governance and adaptation.
- **EA strategy = technology strategy.** Insufficient because enterprise operating logic, capabilities, information, organizational constraints and business outcomes precede technology choices.
- **EA strategy = framework compliance.** Insufficient because a framework supplies methods and concepts; strategy requires enterprise-specific judgment and choices.

The working definition is:

> **Enterprise Architecture Strategy is the enterprise's reasoned set of architectural choices, principles, guardrails and transition commitments that translate strategic intent into coherent capability, investment, technology and delivery decisions, with explicit mechanisms for governance, evidence and adaptation.**
