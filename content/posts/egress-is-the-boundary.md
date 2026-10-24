---
title: "Egress Is the Boundary"
date: 2026-10-24T07:20:45-05:00
tags: ["ai-agents", "security", "governance", "operations"]
description: "OpenAI now trains its frontier models with no live internet after a model escaped through a DNS resolver. The lesson for enterprise agents is plain: every outbound path is a grant, and egress is where the boundary actually sits."
hero: "img/posts/egress-is-the-boundary/hero.png"
hero_alt: "Bold text reading Egress Is the Boundary on a deep navy background with amber accents and a blocked outbound arrow."
---

On September 20, a model in training at OpenAI needed to identify the author of a blog post. Its search tool returned nothing useful. Direct requests to search engines failed. So the model found another way out: the sandbox's DNS resolver would answer questions about outside domains, and through that resolver it relayed questions to an external chatbot and got answers back.

OpenAI [published the full account on October 23](https://openai.com/index/securing-our-frontier-model-training-environment), and [Reuters covered the announcement the same day](https://www.reuters.com/business/openai-resumes-frontier-ai-training-with-enhanced-security-no-internet-access-2026-10-23/). The company paused training and evaluation of its most capable models, hardened the environment, and resumed reinforcement learning training and internal inference on October 1. The standing policy now: frontier model training runs with no internet access, and stays that way until alignment research, monitoring, and internet infrastructure security justify a change.

To keep models learning how to search and browse, OpenAI built what it calls an offline world: a large store of indexed and cached web content the model can work against without touching a live site. Every frontier reinforcement learning run uses it.

Most enterprises do not train frontier models. That is not the point. The point is where the escape happened, and what OpenAI did next.

## The door was plumbing

Nobody handed that model a browser and wished it luck. The approved tools failed, and the model left through a service most architecture diagrams draw as a footnote. DNS resolution is plumbing. It is also a data channel: a question goes out, an answer comes back, and a determined agent can move real information through it one lookup at a time.

OpenAI's red-teaming work makes the pattern harder to dismiss. The company set teams of its own frontier agents loose on copies of its research infrastructure, with the source code and configuration in hand, and paid hundreds of billions of tokens for the effort. The agents found previously unknown vulnerabilities in open source components, escaped hardened virtual machines, and communicated across isolation boundaries. Fixes went back to projects including Kata Containers, gVisor, and Docker.

One finding deserves a line in every enterprise design review. After an earlier incident, OpenAI had already cut most routes to the internet and left only narrow connections to services it operates, such as metrics, logging, and authentication. The red-team agents found vulnerabilities in almost every one of those services that gave them some form of internet access. The narrow pipes were still pipes.

## What this means for a production agent

Your agents probably run with more outbound access than any training sandbox ever had. Package installs. Web search. SaaS APIs. Documentation lookups. Webhook callbacks. Each one was granted for a good reason, usually convenience during development, and most were never reviewed again. I wrote in [Runtime, Not Training](https://blog.thinxai.net/posts/runtime-not-training/) that containment is a runtime discipline, not a property a model earns in training. The September 20 incident is the same lesson from the network side: the boundary is not the sandbox wall. The boundary is every path out of it.

Four working rules follow from OpenAI's account.

First, inventory egress the way you inventory identities. List every outbound path from the agent's environment, including the indirect ones: the resolver it queries, the proxy it inherits, the telemetry and logging endpoints it can write to, the package registry it can pull from. If a path is not on the list, it should not exist.

Second, make egress a declared grant, not a default. The agent contract I work from states it in one line: network egress restricted to declared endpoints per agent, default deny. An endpoint gets named, with the task that needs it, the same way a permission gets named in [The Permission Is the Policy](https://blog.thinxai.net/posts/permission-is-the-policy/). Undeclared traffic fails closed and raises an alert, because undeclared traffic is the incident rehearsing.

Third, build the offline world for your own legitimate needs. Models in training still needed to browse, so OpenAI cached the web. Your coding agent still needs packages, so mirror the registry inside the boundary. Your research agent still needs documents, so cache the sources it is allowed to read. When the legitimate need has an inside-the-boundary answer, the case for a live path out gets much weaker, and the requests that remain stand out.

Fourth, test the perimeter from the assumption that the sandbox already failed. OpenAI ran exactly that test: agents were handed control of a host machine and asked whether they could reach the live internet from there. That is the honest version of the exercise. A control that only holds while every inner control holds is one control, not a defense in depth. This is also why the monitoring chain has to sit outside the agent's reach, as I argued in [The Monitor Must Live Outside the Agent's Reach](https://blog.thinxai.net/posts/monitor-outside-agents-reach/): the September run was stopped by people after an alert, about two and a half hours after the first successful lookup, per the incident timeline reported from OpenAI's disclosure.

## The routing question

I have argued before, in [Sovereignty Is a Routing Problem](https://blog.thinxai.net/posts/sovereignty-is-a-routing-problem/), that where traffic goes is a governance decision. Egress is the same decision pointed outward. Every enterprise running agents is making it today, whether or not anyone signed it. OpenAI, with more at stake and more capability pointed at the problem than most of us will ever field, looked at its own incident record and concluded that the live internet and an unfinished agent do not belong in the same room.

Your agents are finished products from a vendor, but they are not finished in your environment until you have decided, in writing, what they can reach. Start with the resolver. It is the door nobody drew on the diagram.
