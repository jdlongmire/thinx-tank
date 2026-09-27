# Findings and Recommendations — Research Pass 3

## Finding

Mature systems engineering already supplies verification, validation, assurance, claims/arguments/evidence, stakeholder decision authority and lifecycle governance. MxM should explicitly inherit this lineage rather than imply these ideas originated in agent architecture.

## Recommendation 1 — Reframe MxM's intellectual lineage

Treat ISO/IEC/IEEE 15288 and 15026, W3C PROV and OMG SACM as foundational adjacent engineering standards. The paper should state where MxM adopts their principles and where it adds agent-runtime semantics.

## Recommendation 2 — Define the runtime authority state machine formally

Formalize:

Proposal -> Authorization -> Execution -> Evidence -> Verification -> Acceptance -> Integration -> Disposition

Specify actor authority, entry/exit criteria, required evidence and prohibited shortcuts for every transition.

## Recommendation 3 — Make self-certification a named failure mode

A model must not convert its own assertion of completion into verification or Acceptance. Demonstrate this through negative conformance tests.

## Recommendation 4 — Map Evidence instead of reinventing it

Produce a mapping from MxM Evidence records to W3C PROV and assurance-case concepts. Extend only where a demonstrated agent-runtime requirement is missing.

## Recommendation 5 — Shift publication language

Prefer "contribution", "architecture", "operationalization", "adaptation", and "composition" where supported. Reserve "novel" for claims surviving explicit prior-art and empirical testing.

## Recommendation 6 — Next empirical gate

The next major work item should be a formal MxM invariant/state-transition specification plus a two-runtime experiment. Literature work should continue, but additional reading alone cannot establish NC-05.
