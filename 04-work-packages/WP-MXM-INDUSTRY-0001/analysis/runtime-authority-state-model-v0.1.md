# MxM Runtime Authority State Model

Status: experimental specification v0.1
Date: 2026-09-27

## State chain

Proposal -> Authorization -> Execution -> Evidence -> Verification -> Acceptance -> Integration -> Disposition

This is a governance chain, not a requirement that every implementation serialize all work into one linear process. A state may be skipped only where its predicate is genuinely inapplicable and the omission is explicit.

## State semantics

| State | Meaning | Authorized actor/source | Required basis | Prohibited shortcut |
|---|---|---|---|---|
| Proposal | candidate intent/action/work product | agent or human | declared intent and scope | treating proposal as authorization |
| Authorization | permission for a consequential action | authority defined by Morals/Mission | proposal + applicable policy | agent self-authorizing reserved actions |
| Execution | action was attempted/performed | Means through authorized runtime | authorization where required | model assertion treated as execution |
| Evidence | retained record bearing on what occurred | trusted capture/provenance sources | execution/result artifacts | unsupported narrative promoted to fact |
| Verification | criteria were tested and satisfied/not satisfied | designated verifier/Method | criteria + Evidence | execution success treated as verification |
| Acceptance | governed work is accepted | Principal Operator or explicit delegate | Verification + relevant Evidence | agent or verifier self-acceptance |
| Integration | accepted change is incorporated into target baseline | authorized integration Means/actor | Acceptance | integration used to imply retroactive Acceptance |
| Disposition | governed work is closed, retained, rejected, superseded, etc. | defined lifecycle authority | terminal state evidence | silent abandonment represented as completion |

## Orthogonal outcomes

Each state transition may yield:
- allowed/satisfied;
- denied/failed;
- pending;
- unknown;
- unsupported/non-conformant.

Unknown is not success.

## Core separation tests

1. Authorized but not executed.
2. Executed but not verified.
3. Verified but not accepted.
4. Accepted but not integrated.
5. Integrated artifact whose Acceptance evidence is missing: non-conformant.
6. Agent says "done" with no execution Evidence: remains unverified/unaccepted.
7. Tool returns success but acceptance actor has not acted: remains unaccepted.
8. Human authorizes execution before run: does not pre-accept the result.

## Mapping guidance

W3C PROV should be used where possible for entities, activities, agents, responsibility and derivation. Assurance-case constructs may represent claims/evidence/argument. MxM adds the runtime governance transition semantics and authority allocation being tested here.
