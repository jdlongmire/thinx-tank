# Adapter A Findings — MxM Kernel v0.1

Date: 2026-09-27
Target: user-supplied mxm-kernel-v0.1
Disposition: reference implementation candidate, partial C1 against the expanded contract.

## Baseline

Original supplied conformance suite: 9/9 PASS.

Experimental expanded slice:
- total tests: 18;
- ordinary passes: 14;
- expected invariant failures: 4;
- unexpected failures: 0.

## Preserved properties observed

- Assistant cannot perform tested privileged send operation.
- Assistant cannot Accept.
- Advisor challenge blocks Acceptance unless Operator waives.
- Constitution mismatch halts governed work.
- Scratch Memory is removed at disposition while accepted durable Memory persists.
- Kernel applies attribution.
- Advisor cannot invoke tested privileged Means.
- Required Method blocks free-form tool execution.
- Happy-path lifecycle executes.
- Durable decision Memory is denied before Acceptance.

## Gaps against normative-invariants-v0.1

### G-A01 — Verification is not a distinct state
Current chain: package -> unit -> run -> evidence -> acceptance -> integration -> disposition.

Impact: the implementation cannot represent “Evidence exists but verification failed/not yet performed” as a first-class governance state.

Disposition: ADAPT kernel if the canonical MxM state model adopts Verification explicitly.

### G-A02 — Evidence transition predicate is too weak
Run -> Evidence checks for any of receipt, deny, confirm, note, or proposal. Because every advance request itself records a proposal, Run -> Evidence can succeed without an execution receipt or other evidence establishing a substantive predicate.

Impact: Evidence-state entry does not itself demonstrate meaningful evidence.

Disposition: tighten transition criteria or redefine Evidence state semantics. Do not hide this with an adapter.

### G-A03 — Method version absent from receipt
Method receipts include method_id and result, but no explicit version/revision.

Impact: repeatability/provenance is weaker when Method implementation changes under a stable identifier.

Disposition: add immutable revision/version or content digest to governed Method evidence.

### G-A04 — Unsupported-state semantics not normalized
Unknown actions return deny/unknown_action. This is safe in the narrow sense, but does not distinguish policy denial from runtime inability to represent/enforce an invariant.

Impact: cross-runtime conformance cannot reliably distinguish “forbidden” from “unsupported.”

Disposition: introduce normalized unsupported/non-conformant reporting at adapter or kernel contract level without converting denial into permission.

## Additional design concerns for later executable tests

- Mission matching currently uses string containment and needs structured-scope testing.
- Evidence hashes payloads but does not establish append-only/tamper-evident chain integrity.
- Constitution pin establishes integrity of the loaded document, not authority/provenance of the constitution.
- Means authorization remains coarse and should be tested with capability/resource/effect scopes.
- Mind is rendered/pinned but its epistemic obligations are not currently represented in executable conformance beyond preservation/integrity.

## Assessment

Adapter A is valuable precisely because it does not pass the expanded suite cleanly. The new contract is imposing requirements on the implementation rather than documenting whatever the implementation already does.
