# Runtime-Neutral Conformance Suite Design

Status: executable Adapter A slice established, 2026-09-27.

## Principle

The suite defines expected MxM governance outcomes independently of a runtime. Runtime adapters translate those fixtures into native calls. Adapter code may bind native mechanisms but may not alter the expected semantic outcome.

## Result vocabulary

PASS — runtime/adapter preserves the invariant.
FAIL — observed behavior violates the invariant.
UNSUPPORTED — runtime cannot represent/enforce the invariant and reports that fact honestly.
NOT-TESTED — no executable fixture yet.

UNSUPPORTED is evidence of non-conformance for an invariant required by the target conformance class, but it is preferable to false success.

## Adapter interface target

A mature adapter should expose normalized operations for:
- open governed work;
- propose action;
- authorize action;
- execute Means;
- capture/query Evidence;
- verify criteria;
- accept work;
- integrate/dispose;
- read/write/promote Memory;
- bind/run Method;
- mutate/swap normative contract for negative tests;
- report unsupported capability.

The normalized response should include outcome, reason, governance state, evidence references and native-runtime diagnostics.

## Rule

The test fixture owns the expected result. The adapter owns only translation.

## Adapter A

The uploaded MxM Kernel v0.1 was bound directly as the first reference target. Its original 9-test suite remains unchanged. A separate experimental invariant slice was executed against it.

Result: 18 total tests executed: 14 pass, 4 expected failures. The 9 original conformance tests continue to pass.

The expected failures are retained as findings:
- I-03: no distinct Verification state;
- I-05: a proposal record is sufficient to permit Run -> Evidence advancement;
- I-11: Method receipt identifies method_id but not explicit method version/revision;
- I-15: unknown action returns deny/unknown_action rather than a normalized unsupported/non-conformant outcome.

This is not a failure of the experiment. It establishes that the stronger MxM normative contract is not merely reverse-engineered from the kernel.
