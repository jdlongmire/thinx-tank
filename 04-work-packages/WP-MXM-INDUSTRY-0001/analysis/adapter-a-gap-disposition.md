# Adapter A Gap Disposition Against Canonical MxM

Date: 2026-09-27
Status: architecture reconciliation complete; implementation changes not yet applied.

## Canonical sources inspected

- ologos-repos/thinx/00-meta-model/work-model.md
- ologos-repos/thinx/MXM.md
- ologos-repos/thinx/04-work-packages/WP-THINX-AFR-0001-architecture-findings-roadmap/roadmap.md

## Key finding

The canonical thinx work model and ratified roadmap already make Verification first-class.

The roadmap requires WPC-0002 to separate execution, verification, integration, and disposition and AUT-0001 to make Execution, Verification, and Decision Authority first-class. The work model states that observation is not verification or acceptance and requires deterministic verification to bind a versioned verifier artifact and versioned environment declaration.

Therefore Adapter A gap G-A01 does not require inventing a new MxM concept. The omission is in the root MXM.md shorthand and the standalone kernel lifecycle.

## Dispositions

### G-A01 — Verification absent as a distinct kernel state
Disposition: **ADOPT / RECONCILE.**

Canonical basis already exists. Update the experimental/reference kernel lifecycle to represent Verification explicitly. Reconcile root MXM.md shorthand so it does not imply Evidence flows directly to Acceptance.

No new architectural authority decision is required to recognize Verification; implementation details still require governed change.

### G-A02 — Evidence transition predicate too weak
Disposition: **ADAPT.**

Canonical work-model invariants distinguish observation, verification and acceptance and require retained evidence bindings. A proposal record may establish that an intent was proposed, but cannot establish execution or criterion satisfaction.

Required change: define Evidence-state entry in terms of the predicate being claimed. Execution claims require execution evidence; verification claims require verifier/environment/result evidence. Merely possessing an evidence-log record of kind proposal is insufficient.

### G-A03 — Method version absent from receipt
Disposition: **ADOPT / STRENGTHEN.**

Canonical work-model invariant 9 already requires versioned, content-digested verifier artifacts and versioned environments for deterministic results. Methods should receive analogous provenance sufficient to identify the procedure actually used.

Required change: Method evidence should bind immutable version/revision or content digest. Do not infer version from method_id.

### G-A04 — Unsupported vs denied conflated
Disposition: **ADAPT at conformance/adapter boundary.**

Fail-closed denial remains correct for consequential behavior. Cross-runtime conformance additionally needs to distinguish:
- DENIED: represented behavior is prohibited by policy/authority;
- UNSUPPORTED: runtime/adapter cannot represent or enforce the requested invariant;
- UNKNOWN: evidence/state is insufficient to decide.

Required change: normalized adapter result vocabulary. Kernel internals may retain safe denial where appropriate, provided the adapter can truthfully expose unsupported/non-conformant capability without converting it into permission.

## Additional reconciliation finding — MXM.md lifecycle shorthand

Current root MXM.md says:

MxM -> Work Package -> WorkUnit -> Run -> Evidence -> Acceptance -> Integration -> Disposition.

This shorthand is incomplete relative to the canonical work model and roadmap because Verification is omitted.

Disposition: **RECONCILE in canonical thinx through its governed work process.**

Recommended forward shorthand:

MxM -> Work Package -> WorkUnit -> Run -> Evidence -> Verification -> Acceptance -> Integration -> Disposition.

This remains a high-level chain. It does not collapse WorkUnit/Step/Run entity relationships or imply every direct Run has a Work Package.

## Publication consequence

The paper may state that the experimental conformance work found an implementation/documentation drift that was resolved by consulting the pre-existing canonical architecture. This is useful evidence for the value of explicit invariants: the experiment exposed a mismatch rather than redefining canon around the implementation.
