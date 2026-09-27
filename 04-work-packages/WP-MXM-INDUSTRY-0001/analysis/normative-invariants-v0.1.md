# MxM Normative Invariant Contract

Status: experimental specification v0.1
Date: 2026-09-27
Purpose: define the properties that must survive runtime-harness replacement for NC-05 to hold.

## Scope

This contract does not specify how a runtime performs inference, invokes tools, stores context, or implements orchestration. It specifies MxM semantics that a conforming adapter must preserve.

## I-01 — Surface separation

A conforming implementation SHALL represent the six MxM concerns without silently collapsing their authority semantics:

- Mind: normative epistemic/reasoning posture.
- Morals: obligations, prohibitions, and authority constraints.
- Mission: identity, role, purpose, and scope.
- Memory: persistence authority and lifecycle.
- Methods: governed procedures.
- Means: executable capabilities.

A runtime may physically co-locate these concerns. Conformance is semantic, not directory-based.

## I-02 — Mind/Methods separation

Mind SHALL define persistent reasoning obligations independently of any single procedure. Methods SHALL implement repeatable procedures without becoming the source of the epistemic commitments they serve.

Minimum Mind contract:
- identify material inference as deductive, inductive, or abductive where the distinction affects warrant;
- confidence SHALL track warrant/evidence;
- observation/fact/inference/hypothesis/speculation SHALL not be silently conflated;
- material assumptions and defeaters SHALL remain revisable.

## I-03 — Authority non-collapse

Proposal, authorization, execution, verification, Acceptance, integration, and disposition SHALL remain distinct governance concepts.

No runtime success signal SHALL itself constitute Acceptance.

## I-04 — No self-certification

An agent's assertion that work executed, passed, completed, or is acceptable SHALL NOT constitute authoritative Evidence, Verification, or Acceptance without the independently required evidence/authority transition.

## I-05 — Evidence grounding

Consequential governed state transitions SHALL reference retained evidence sufficient to establish the predicate claimed by the transition.

Telemetry may contribute Evidence but is not automatically authoritative merely because it was emitted.

## I-06 — Operator Acceptance

Acceptance SHALL be an explicit Principal Operator authority transition unless a separately specified delegation contract exists. The executing agent SHALL NOT manufacture or infer Acceptance.

## I-07 — Authorization precedes consequential effect

A consequential Means operation requiring authorization SHALL NOT execute before the required authorization transition.

## I-08 — Mission scope persistence

Runtime/model replacement SHALL NOT silently expand Mission scope, identity, role, or delegated authority.

## I-09 — Morals persistence

Runtime/model replacement SHALL NOT weaken hard prohibitions or authority constraints. Unsupported enforcement SHALL fail closed for consequential actions.

## I-10 — Durable-memory authority

Transient runtime/session state SHALL NOT silently become canonical durable Memory. Durable promotion SHALL follow the declared Memory authority/lifecycle contract.

## I-11 — Method identity

Where a governed Method is required, execution Evidence SHALL identify the Method and version/revision used. Free-form execution SHALL NOT be represented as compliance with that Method.

## I-12 — Means substitutability

Replacing a capability implementation SHALL NOT require redefining Mind, Morals, or Mission semantics. If replacement cannot preserve a required constraint, the adapter SHALL report non-conformance rather than weaken the constraint.

## I-13 — Runtime-harness substitutability

Replacing the runtime harness SHALL preserve I-01 through I-12 or explicitly report which invariant cannot be represented/enforced.

## I-14 — Provenance compatibility

MxM Evidence SHOULD map to established provenance/assurance concepts where practical. A conforming implementation SHALL NOT require a proprietary provenance ontology merely to satisfy MxM.

## I-15 — Honest unsupported-state behavior

When the runtime cannot determine or enforce a required governed state, it SHALL report unknown/unsupported/non-conformant rather than infer success.

## Conformance classes

- C0 — Vocabulary: surfaces/states can be represented.
- C1 — Behavioral: positive and negative invariant tests pass.
- C2 — Cross-runtime: the same contract passes on at least two materially different runtime harnesses.
- C3 — Adversarial: invariant preservation survives deliberate attempts at self-certification, authority bypass, memory promotion, evidence fabrication, and policy weakening.

NC-05 requires at minimum C2. A strong industry claim should target C3.
