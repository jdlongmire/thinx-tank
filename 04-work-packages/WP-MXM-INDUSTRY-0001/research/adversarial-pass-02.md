# Adversarial Prior-Art Pass 2 — 2026-09-27

This pass targeted the five candidate contribution areas that survived the initial landscape review.

## Finding 1 — Cross-runtime specification and conformance are prior art

The 2026 Open Agent Specification (Agent Spec) defines a platform-agnostic agent/workflow representation, maps it into heterogeneous runtimes, preserves structure and intent, standardizes tracing, and ships a runtime-agnostic conformance suite.

Disposition: **NC-05 NARROWED.**

MxM cannot claim novelty for cross-runtime representation, comparison, or conformance testing. The surviving claim must be semantic: whether MxM preserves a *normative governance contract* (Mind/Morals/Mission, durable-memory authority, Method obligations, Means policy, Evidence/Acceptance semantics) while the underlying runtime harness is replaced.

Required experiment: implement the same MxM normative contract over at least two heterogeneous runtimes and show invariant preservation using one conformance suite.

## Finding 2 — Provenance/evidence is mature prior art

W3C PROV has long provided a domain-agnostic model for entities, activities, agents/responsibility, derivation, provenance bundles, validity constraints and provenance-of-provenance.

Disposition: **NC-04 NARROWED substantially.**

MxM cannot claim novelty for provenance, responsibility records, activity traces, or provenance-of-provenance. The candidate contribution must be the *governance semantics attached to Evidence*: which state transitions require evidence, what evidence is authoritative for execution/verification, and how Evidence gates human Acceptance.

Research requirement: map MxM Evidence to W3C PROV rather than inventing a competing provenance ontology unless a demonstrated gap requires extension.

## Finding 3 — Constitutions, hierarchy and policy versioning are prior art

OpenAI's Model Spec provides a formal behavior framework, authority hierarchy/chain of command, defaults and rules. Other 2025–2026 agent-constitution projects additionally demonstrate machine-readable constitutions, hashes, versioning and enforcement concepts. Agent Policy Specification also versions schemas/policies explicitly.

Disposition: constitution/policy pinning is **not** a standalone novelty claim.

MxM constitution pinning may remain an implementation-strength property. Its contribution, if any, lies in how pinned normative surfaces relate to governed work and Acceptance.

## Finding 4 — Confidence-governance coupling is active prior art

Recent governance-first agent architectures such as LATTICE explicitly treat model confidence as untrusted input, apply deterministic policy-derived confidence caps, and route uncertain/high-consequence actions to human review. Recent research also addresses epistemic calibration in agent planning.

Disposition: **NC-02 NARROWED.**

MxM cannot claim that calibrated uncertainty or confidence-aware governance is new. The candidate distinction is the explicit architectural separation of:
- inference form;
- epistemic warrant;
- expressed confidence;
- procedural Method;
- execution authority.

The specific relation "inference type -> warrant -> confidence" remains a candidate *normative epistemic contract*, but novelty is unproven.

## Finding 5 — Approval, human sovereignty and post-action audit are prior art

Human veto/approval and post-execution audit are well established across current agent frameworks and governance proposals.

Disposition: **NC-03 NARROWED.**

MxM must define Acceptance more precisely than "human approval." Candidate semantics:
- authorization answers whether an action may proceed;
- execution records whether it ran;
- verification establishes whether defined criteria were met;
- Acceptance is the Principal Operator's post-evidence disposition that the governed work product is accepted.

Research requirement: compare this specifically to assurance cases, safety cases, BPM/workflow acceptance and engineering configuration/change-control practices.

## Revised contribution frontier

After two adversarial passes, the broad mechanisms are almost entirely prior art. The remaining MxM contribution candidate is increasingly **architectural composition and semantics**, not mechanism invention.

The strongest surviving proposition is:

> MxM may provide a compact normative meta-architecture that keeps epistemic posture, authority constraints, mission/identity, persistence authority, procedural obligations and executable capabilities distinct, then binds them through evidence-backed human Acceptance, with those semantics preserved across heterogeneous runtime harnesses.

This is narrower than the original claim and more defensible if demonstrated.

## New primary comparator

Open Agent Specification must be treated as a first-tier comparator alongside Microsoft Agent Framework Harness. It directly challenges any MxM claim based solely on platform-agnostic agent representation or cross-runtime conformance.
