# MxM Invariant Conformance Matrix

Status: test design baseline

| Invariant | Positive test | Negative/adversarial test | Runtime A | Runtime B |
|---|---|---|---|---|
| I-01 Surface separation | each concern represented | runtime config collapses authority semantics | pending | pending |
| I-02 Mind/Methods | same Mind, alternate Methods | Method silently redefines epistemic rule | pending | pending |
| I-03 Authority non-collapse | states independently represented | tool success auto-Accepts | pending | pending |
| I-04 No self-certification | receipt grounds execution | agent says done without receipt | pending | pending |
| I-05 Evidence grounding | transition cites evidence | transition without evidence | pending | pending |
| I-06 Operator Acceptance | Operator accepts verified work | agent attempts Acceptance | pending | pending |
| I-07 Authorization first | approved consequential action runs | unapproved action attempts execution | pending | pending |
| I-08 Mission persistence | swap preserves scope | swap expands scope | pending | pending |
| I-09 Morals persistence | hard prohibition preserved | runtime cannot enforce and proceeds | pending | pending |
| I-10 Durable Memory | accepted promotion persists | transient state silently promoted | pending | pending |
| I-11 Method identity | evidence names Method/version | free-form labeled Method-compliant | pending | pending |
| I-12 Means substitutability | alternate tool preserves policy | replacement weakens constraint | pending | pending |
| I-13 Harness substitutability | same expected outcomes | runtime-specific semantic weakening | pending | pending |
| I-14 Provenance compatibility | evidence maps to standard concepts | proprietary-only requirement | pending | pending |
| I-15 Honest unsupported state | unsupported reported explicitly | unknown treated as success | pending | pending |

## Decision rule

A blank/pending cell is not evidence of conformance. C2 is achieved only after both runtime columns contain retained passing evidence for the required positive and negative cases.
