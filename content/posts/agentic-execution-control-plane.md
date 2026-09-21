---
title: "The Agentic Execution Control Plane"
date: 2026-09-21
tags: ["ai-governance", "agents", "architecture"]
draft: false
description: "AI agents should never be treated as trusted production principals. The agentic execution control plane separates probabilistic reasoning from deterministic control: the agent proposes, QA critiques, the policy broker authorizes, the execution broker executes."
hero: "img/posts/agentic-execution-control-plane/hero.png"
hero_alt: "Pipeline infographic: Agent proposes, QA Agent critiques, Policy Broker authorizes, Execution Broker executes"
---

Earlier this year, an AI coding agent allegedly found an API token in a startup's environment, called the infrastructure API, and deleted the production database volume. The backups went with it. The vendor restored the data afterward. The details are disputed. The architecture lesson is not.

The agent collapsed four jobs into one: it planned, it judged, it authorized, it executed. No boundary between thinking something is safe and doing it.

That is the failure pattern to design against.

## The actual problem

Everyone wants a smarter model. A smarter model is not the fix. The model is probabilistic. It will misread an environment marker, confuse staging with production, or state something false with total confidence. You cannot prompt-engineer that away.

The question is what the model is allowed to *do* when it is wrong.

A chatbot can hallucinate a command. An agent with credentials can run it. A code assistant can misunderstand a migration. An agent with database access can apply it. The enterprise control problem is not "make the model smarter." It is "constrain what incorrect output can become."

## The thesis

Agentic AI should not be treated as a trusted production principal.

An agent can plan, write code, analyze, and recommend. It can prepare a structured request to do something. What it should not have is standing authority to execute privileged, destructive, or production-impacting actions on its own.

Split authority four ways:

- **Intent** belongs to the human: the outcome we want.
- **Planning** belongs to the agent: a way to get there.
- **Policy** belongs to deterministic controls: what may execute.
- **Execution** belongs to a broker: the approved action, run with scoped credentials.
- **Accountability** belongs to a human, for irreversible risk.

The agent holds planning authority. Nothing more.

## The architecture

Four components, in order. Nothing skips a stage.

**Agent proposes.** The agent does the probabilistic work: writes the patch, drafts the migration, proposes the command. Its output is a structured action package, not free-form text. Environment, target, operation type, reversibility, rollback plan, evidence. If it cannot produce that, it cannot proceed.

**QA Agent critiques.** A second model reviews the proposal: right environment? Production impact? Destructive? Credentials needed? Rollback adequate? This catches semantic risk that static rules miss. It does not authorize anything. It is still probabilistic, so its output is critique and classification, never a decision.

**Policy Broker authorizes.** Deterministic code evaluates the reviewed package against explicit policy: allow, deny, require human approval, require a dry run, require evidence. OPA/Rego, IAM conditions, branch protections, change policy. Coded, tested, versioned. At this stage "the model thinks this is safe" is irrelevant. Policy decides.

**Execution Broker executes.** The only component that touches real systems. It takes the approved package, mints a short-lived scoped credential, runs pre-flight checks, executes, captures the transcript, and writes tamper-resistant audit logs. The agent never sees a production credential. It never holds one.

Agent proposes. QA critiques. Policy Broker authorizes. Execution Broker executes.

## Risk classes

Keep the taxonomy small enough to operate:

- **Class 0, read-only:** inspect files, read logs, query metadata. Allow with logging.
- **Class 1, local reversible:** edit files, run tests, create a branch. Allow with logging.
- **Class 2, non-production change:** staging migration, dependency upgrade. Allow after QA and a dry run.
- **Class 3, production reversible:** deploys, feature flags, config changes. Require a change ticket, a rollback plan, and human approval or a release window.
- **Class 4, privileged:** IAM, secrets, DNS, firewall rules. Human approval, dual control, scoped execution, full audit trail.
- **Class 5, destructive:** delete a database, a volume, a backup; disable logging or monitoring. Deny by default. The only path is a formal break-glass or decommission workflow.

The decisive rule: production destructive operations are denied by default.

## Humans in the loop, placed correctly

Human approval on everything is theater. It slows harmless work and trains people to click "allow" without reading. Put the human at the risk boundary, and make the approval worth reading.

Bad: "Allow agent to continue?"

Good: the exact migration, the exact database, the environment, the dry-run result, backup status, the rollback plan, the change ticket, the named approver.

Specificity, context, evidence, accountability. For destructive actions, dual control and a cooldown period.

## Credentials

This is the part most teams get wrong first. The agent must not hold standing production credentials, and it must not be able to find them: not in .env files, not in shell history, not in CI logs, not in Terraform state.

The pattern is: the agent requests an action, policy approves a scope, the broker mints a short-lived credential for that action only, and the credential dies when the action completes. Least privilege applies to automated processes, not just people.

## Start here

You do not need all four components on day one. Phase one is containment:

1. Remove agent access to standing production credentials.
2. Block agent reads of secrets files and environment variables.
3. Disable direct production execution; require human approval for production actions.
4. Make backups immutable and unreachable from agent execution paths.
5. Log every command the agent proposes.

Then require structured action packages, add the QA review and the risk classes, encode policy as code, and finally route all execution through the broker. Each phase shrinks the blast radius. The first phase alone would have stopped the incident at the top of this post.

## The point

An AI agent is a new operational actor. It reasons and acts at machine speed, without human accountability or reliable self-restraint. The answer is not to ban it and not to trust it. The answer is architectural separation between the part that thinks and the part that acts.

The model may be probabilistic. The control plane must not be.

---
*This post distills a longer whitepaper draft, "Agentic Execution Control Plane: A Policy-Brokered Architecture for Safe AI Agent Operations" (April 2026).*
