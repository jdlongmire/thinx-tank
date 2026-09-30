---
title: "Git Is the Control Plane"
date: 2026-09-30
tags: ["agents", "gitops", "aioc", "governance"]
draft: false
description: "Most shops configure agents by clicking through consoles and pasting prompts into chat windows. Everything as Code points GitOps discipline at the agent estate itself: prompts, tool allowlists, model bindings, and kill criteria all declared in versioned repos, so decommissioning an agent is a merge and rollback is a git revert."
hero: "img/posts/git-is-the-control-plane/hero.png"
hero_alt: "Navy graphic with amber headline text reading Git Is the Control Plane."
---

Earlier this month [Neel Shah wrote up his pattern](https://medium.com/google-cloud/gitops-for-ai-agents-on-google-cloud-argocd-config-sync-and-gke-03fdad8b0716) for running AI agents on GKE with GitOps. The core of the piece is a repo layout where an agent's system prompt, tool allowlist, model binding, and guardrail config all live as versioned files, and a reconciler (ArgoCD or Config Sync) continuously forces the live cluster to match. A prompt tweak is a one-line diff. Rollback is a git revert. A policy engine blocks a dangerous tool grant before it lands.

Shah's piece is about the runtime layer: how agents get deployed. The deeper move is to point the same discipline one level up, at the control plane itself.

In my AI Operations Center work, the estate is governed through four planes: control, production, assurance, evidence. The control plane holds the policy. Which agents exist, what they may do, who owns them, what evidence posture they run under. And in most shops today, that policy lives in consoles and chat windows. Someone pastes a new system prompt into a managed agent UI. Someone grants a new tool in a settings panel. The agent's behavior changes on a Tuesday and the only record is somebody's memory of having done it.

That is the exact gap my [SOX-for-AI framework](https://blog.thinxai.net/posts/sox-for-ai/) was built to close: inventory and ownership first, then controls, then audit. And it is the gap behind [Nobody Can Fire an Agent](https://blog.thinxai.net/posts/nobody-can-fire-an-agent/): 81 percent of CIOs in Dataiku's survey said they had lost oversight of at least one AI deployment. You cannot decommission what was never declared.

Everything as Code is the answer at the control-plane level. Not just infrastructure as code, which we have had for years. The whole agent estate, declared in versioned repos:

- Agent manifests: identity, named owner, scope, and which assurance plane watches it.
- Prompts as text files: a behavior change is a diff with a reviewer attached.
- Tool allowlists as manifests: what the agent may call, enforced by a policy engine before it lands.
- Model bindings per environment: staging points at the cheap model, production at the evaluated one.
- Kill criteria and shutdown runbooks: written down, versioned, tested.
- The evidence posture: what each agent records, where it goes, how long it is kept.

When that is all in Git, decommissioning an agent becomes a merge request. Delete the manifest, approve, merge, and the reconciler tears the agent down in every environment where it was declared. The shutdown discipline I laid out in [Decommission by Design](https://blog.thinxai.net/posts/aioc-decommission-by-design/) stops being a document people forget and becomes a state transition the platform enforces. You fire the agent by deleting its declaration.

Rollback is the same move. A prompt change that degrades quality in production is a git revert, and the reconciler restores the reviewed state. The drift correction is automatic: a hand edit to a live agent gets reverted to what Git says it should be on the next sync. That kills the quietest failure mode in agent operations. Somebody "fixes" an agent by hand in production during an incident, nobody writes it down, and the next person inherits behavior nobody reviewed. The reconciler does not care why the hand edit happened. It restores the declared state.

There is a second half to this, and GitOps only supplies one. Reconciliation answers "make reality match the declaration." You still need "should this declaration be allowed at all." That is the policy broker in the merge pipeline: a constraint that rejects any agent declaration referencing a tool that is not on an approved list, before it reaches any environment. It is the same policy-broker position from my [agentic execution control plane](https://blog.thinxai.net/posts/agentic-execution-control-plane/): policy evaluated before execution, every time. The dangerous tool grant dies as a declined PR instead of becoming an incident.

None of this requires Kubernetes. The repos are the point. The reconciler is an implementation detail. A small shop gets most of the value from one repo, branch protection, and a nightly job that diffs declared state against actual state and pages someone on drift. The mechanism scales down. The discipline does not.

What changes when Git is the control plane is the answer to every governance question I have raised this month. Who owns this agent? Check the manifest. When did its prompt last change, and who approved it? Check the log. Why does it have access to the billing database? Check the allowlist PR. How do we shut it down? Check the kill criteria. Each answer lives in the repo, with a history, a reviewer, and a revert.

The control plane governs the agents. Git governs the control plane. When both of those are true, oversight stops being a quarterly audit finding and becomes the thing you merge.
