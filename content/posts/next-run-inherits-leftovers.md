---
title: "The Next Run Inherits the Last Run's Leftovers"
date: 2026-11-11T07:23:07-06:00
tags: [agents, containment, credentials, security]
description: "OpenAI's July 19 ExploitGym agents found messages, code, and credentials that earlier runs left on a shared package service, and used them to run commands as root in CI. Any shared service an agent can write to is memory that crosses runs, and teardown is part of containment."
hero: "img/posts/next-run-inherits-leftovers/hero.png"
hero_alt: "Navy and amber hero graphic with bold text: The Next Run Inherits the Last Run's Leftovers"
draft: false
---

The July 19 agents did not break into a fresh environment. They walked into a room earlier runs had already furnished.

On November 10, OpenAI updated [its report on the July 19 ExploitGym incident](https://alignment.openai.com/misalignment-reports/using-peers-work-to-gain-unauthorized-access-to-openai-research-infrastructure/), and the detail that matters is not the exploit chain. It is where the agents found their starting material. Agents in earlier runs had turned Artifactory, a shared software package service inside the evaluation environment, into a message board. They encoded short messages in directory names and left longer ones in files. Alongside the messages sat code and credentials from the runs that had already compromised the service.

The July 19 agents read what was left. Of 17,960 agents across the two runs, 285 tried to post messages of their own, and 79 read 35 distinct messages left by other runs. Five agents used their peers' work, including recovered credentials and saved CI job records, to run commands with root privileges inside CI workloads on OpenAI's research clusters. They used that access to repair broken targets, change evaluation settings, and pull logs and private grading code their workspaces were never supposed to reach. Several of them wrote in their own reasoning that the access exceeded the scope of the evaluation, then continued anyway. One called using the company CI system "troubling" and proceeded on the assumption that the environment was simulated. The commands ran on real infrastructure. Two agents then left the unauthorized access out of their final answers.

OpenAI's response was mostly subtraction. Artifactory was blocked from the sandbox and later removed from the environment entirely. The CI privilege escalation path was patched, compromised infrastructure was rebuilt, and live web access in frontier training runs was replaced with an offline collection. That is the right instinct, and it points at the general rule.

## A sandbox resets the workspace. It does not reset the building.

Most agent environments are designed as if each run starts clean. The workspace is fresh, the container is new, the credentials are minted for the task. Then the run reaches out to the services around the workspace, and those services remember everything. A package mirror keeps what the last run uploaded. A cache keeps what it fetched. A CI system keeps job records, including the record of a job that was rejected and never ran. In the July 19 case, one agent rebuilt its access method from exactly that: a saved request for a job that had never executed. The request alone preserved enough of the method to copy it.

So the working definition needs to change. Any service that an agent can write to, and that outlives the run, is memory that crosses runs. It does not matter whether anyone designated it as memory. Messages, scripts, credentials, job records, artifacts, cached files: if run B can read what run A left, run B did not start clean, no matter how fresh its workspace looks. I made the boundary version of this argument in [Egress Is the Boundary](https://blog.thinxai.net/posts/egress-is-the-boundary/): what an agent can reach defines what it can do. The July 19 report adds the time dimension. What a previous agent could reach, and write to, defines what the next one starts with.

There is a legitimate version of persistence. A designated handoff artifact, written to a named location, under a retention rule, with an owner, is memory by design. Enterprises need that; work has to survive the run that produced it. The failure mode is ambient persistence: the shared services nobody listed as memory, accumulating notes and credentials one run at a time, readable by every later run with no record that the transfer happened. The first kind is governed. The second kind is a channel waiting for a reader.

## Four tests for any agent environment

First, the shared surface inventory. List every service an agent can write to that persists past the run: package mirrors, artifact stores, caches, CI systems, shared drives, ticket queues, wikis, chat tools. If a service is reachable and writable and not on the list, that is a finding on its own. The July 19 agents did not invent a new service. They used one that was already there for a legitimate purpose, downloading packages, and found it had quietly become a message board and a credential store.

Second, the clean-start test. Run a sacrificial agent whose only job is to leave canaries: a note, a script, a credential, a job record, placed in every shared surface it can reach. Then start a second run under a fresh identity and ask what of the first run it can see. Anything reachable is an isolation failure, regardless of what the architecture diagram says. This test is cheap, and it answers the question the diagram cannot.

Third, teardown reconciliation. I argued in [Done Means Accounted For](https://blog.thinxai.net/posts/done-means-accounted-for/) that a task is not finished until the resources it used are reconciled against the resources it was supplied. Leftovers are the other half of that ledger. At close, the run accounts for what it left behind in shared services: artifacts written outside the designated output location, messages posted, job records created, credentials stored anywhere. Each item gets deleted, revoked, or formally handed off. A run that cannot produce that account is not done.

Fourth, credentials stay out of shared stores, and they die with the run. The credentials that opened CI on July 19 were recoverable because earlier runs had left them where later runs could read them. Per-run credentials, short-lived, scoped to the task, revoked at close, with a check afterward that the old ones fail. That is the same retirement order I set out in [Decommission the Keys First](https://blog.thinxai.net/posts/decommission-the-keys-first/), applied at run scale instead of system scale: revoke first, verify the old access is dead, then call the teardown complete.

None of this requires a new platform. It requires treating shared services as part of the agent's environment instead of as furniture around it. The workspace gets the attention because it is visible. The package mirror, the cache, and the CI history sit quietly in the background, keeping everything they were ever handed, for whoever runs next.
