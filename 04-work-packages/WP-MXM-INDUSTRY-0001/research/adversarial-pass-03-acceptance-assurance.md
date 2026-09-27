# Adversarial Prior-Art Pass 3 — Acceptance, Assurance, and Engineering Authority

Date: 2026-09-27

## Purpose

Attack NC-03 (Acceptance) and the related Evidence claim against mature systems-engineering and assurance disciplines.

## Primary findings

### 1. Evidence-backed human engineering decisions are established prior art

ISO/IEC/IEEE 15288 provides a stakeholder-centered system life-cycle framework with agreement, technical, technical-management and organizational processes. Verification and validation are established engineering concerns rather than agent-specific innovations.

NIST's assurance-case definition, drawing on ISO/IEC 15026 and established software-assurance practice, defines an assurance case as a reasoned, auditable artifact containing structured claims, argumentation, evidence and explicit assumptions. NIST SP 800-171A Rev. 3 further describes assessors gathering evidence so designated officials can make objective compliance determinations.

Disposition: MxM cannot claim novelty for the pattern "collect evidence, evaluate it, then a human authority decides."

### 2. Claims/arguments/evidence structure is standardized

ISO/IEC/IEEE 15026-2:2022 specifies assurance-case structure terminology. The ISO/IEC 15026 lineage explicitly connects top-level claims through systematic argumentation to evidence and assumptions in support of stakeholder communication and engineering decisions.

OMG SACM provides a machine-readable metamodel for auditable claims, arguments and evidence, including evidence repositories and explicit relationships between evidence and claims.

Disposition: MxM Evidence must interoperate conceptually with assurance/provenance standards rather than recreate their ontology.

### 3. Assurance over the life cycle is mature

ISO/IEC/IEEE 15026-4:2021, with a successor revision in development, layers assurance processes over ISO/IEC/IEEE 15288/12207. The core concept is achieving a selected claim and showing its achievement.

Disposition: MxM cannot claim novelty merely for evidence-gated lifecycle progression.

### 4. The surviving Acceptance distinction is narrower

The candidate distinction is not "human approval after evidence." It is an **agent-runtime authority state machine** in which:

- proposal is an agent request/intention;
- authorization is permission to proceed;
- execution is an observed effect;
- verification is evidence-backed satisfaction of defined criteria;
- Acceptance is the Principal Operator's explicit post-verification disposition of governed work;
- integration/disposition are subsequent lifecycle states.

The contribution burden is to show that keeping these states distinct prevents concrete autonomous-agent failure modes (self-certification, fabricated completion, approval/acceptance conflation, or provenance loss) and remains portable across runtimes.

This is primarily an application/adaptation of mature engineering governance to AI-agent operation unless evidence establishes a stronger novelty claim.

## NC-03 disposition

**NC-03 RECLASSIFIED: likely ADAPTATION/COMPOSITION, not mechanism novelty.**

Potential contribution wording:

> MxM operationalizes mature verification, assurance, and human decision-authority distinctions as an explicit runtime governance state model for persistent AI aides.

This is a potentially useful industry contribution even if it is not a novel underlying engineering principle.

## Impact on NC-04

Evidence-backed assurance is also mature. NC-04 should be framed as a binding rule between runtime state transitions and evidence, with W3C PROV / ISO 15026 / SACM treated as compatible underlying evidence and assurance models.

## Research consequence

The paper should distinguish at least three kinds of contribution:

1. **novel mechanism** — increasingly unlikely for most MxM components;
2. **novel architectural composition/abstraction** — still plausible;
3. **novel application of mature systems-engineering governance to persistent AI-agent runtimes** — increasingly plausible and independently valuable.

The paper should not treat category 3 as lesser merely because its ingredients have precedent. Architectural contributions often consist in correct decomposition, integration, and operationalization of established principles in a new problem domain.

## Sources

Primary/normative:
- ISO/IEC/IEEE 15288:2023, Systems and software engineering — System life cycle processes.
- ISO/IEC/IEEE 15026-1:2025, Systems and software assurance — Vocabulary and concepts.
- ISO/IEC/IEEE 15026-2:2022, Systems and software assurance — Assurance case.
- ISO/IEC/IEEE 15026-4:2021, Systems and software assurance — Assurance in the life cycle.
- OMG Structured Assurance Case Metamodel (SACM), v2.x.
- NIST assurance-case definitions and NIST SP 800-171A Rev. 3 assurance-case guidance.
