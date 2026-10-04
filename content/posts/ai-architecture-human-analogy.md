---
title: "AI Architecture, a Human Analogy"
date: 2026-10-04
tags: ["ai-architecture", "agents", "llm"]
description: "Five parts, five human analogies: what the LLM, RAG, MCP, harness, and agent each actually do, plus the three confusions to stop making."
hero: "img/posts/ai-architecture-human-analogy/hero.png"
hero_alt: "AI Architecture: A Human Analogy"
draft: false
---

Most confusion about AI systems comes from mashing the parts together. The model is not the agent. The protocol is not the tool. Retrieved text is not knowledge inside the model.

I put together this explainer to keep the five parts straight, one human analogy each:

**1. LLM = language-and-tool-use engine.** Like the language centers of a brain, not the whole brain. It understands prompts, generates language, and can choose or format tool requests. Limitation: it can sound confident and be wrong.

**2. RAG = retrieval into context.** Like asking a librarian, not owning the library. It finds relevant passages and adds them to the prompt so the model can cite what it was given. Limitation: wrong or stale retrieval can still mislead.

**3. MCP = standard connector.** Like going to a hardware store when you need a tool you do not already have. A protocol for discovering and calling external tools across APIs, data, files, and services. Limitation: it gives access, but the tool may be unavailable, untrusted, or not appropriate.

**4. Harness = runtime.** Like the whole body working in coordination. It holds memory and state across steps, routes the model to RAG, MCP, and skills, enforces permissions and policy, monitors and recovers from errors, and runs the workflow loop. Limitation: bugs, misconfiguration, or poor policy can cause failures.

**5. Agent = LLM + harness.** The goal-directed actor. You set the goal; it plans, uses the LLM to decide the next step, uses the harness for memory, tools, and execution, and returns an outcome, not just text. Like a person with a team. Limitation: only as good as the goal, the tools, and the guardrails provided.

The strip at the bottom is the part I care about most. Three distinctions that keep every architecture conversation honest:

- The model is not the agent. An LLM generates language; it does not set goals or take action.
- The protocol is not the tool. MCP is a standard; tools are the actual capabilities.
- Retrieved text is not knowledge inside the model. RAG adds information to the prompt; it is not permanently stored.

Tools extend capability. People give it purpose.

![AI Architecture, a human analogy explainer](/img/posts/ai-architecture-human-analogy/ai-architecture-analogy.jpg)
