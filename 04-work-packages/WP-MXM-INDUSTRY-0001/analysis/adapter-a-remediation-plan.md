# Adapter A Remediation Plan

Date: 2026-09-27
Status: planned; implementation authority remains with the repositories of record.

## Change set A — canonical thinx reconciliation

Repository: ologos-repos/thinx

1. Reconcile MXM.md lifecycle shorthand to include Verification.
2. Ensure the shorthand points to work-model.md for authoritative verification semantics.
3. Do not duplicate WPC/AUT/CAR semantics into MXM.md.
4. Run repository conformance checks.

## Change set B — reference kernel

Repository: reference kernel repository once established/imported.

1. Add Verification to lifecycle states/transitions.
2. Separate evidence capture from verification result.
3. Tighten Evidence transition predicates.
4. Bind Method version/revision/content digest in receipts.
5. Add normalized adapter/conformance outcomes: PASS/FAIL/DENIED/UNSUPPORTED/UNKNOWN as appropriate.
6. Preserve all original v0.1 negative controls.
7. Re-run original suite plus expanded invariant suite.

## Acceptance target

Adapter A reaches C1 only when every required I-01 through I-15 behavioral invariant has an executable positive/negative test or an explicitly justified non-applicable disposition, with no unacknowledged FAIL or NOT-TESTED state.

C1 does not establish the meta-harness claim. C2 still requires Adapter B on a materially different runtime.
