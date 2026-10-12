---
title: "Your Code Is Not the Moat Anymore"
date: 2026-10-12
tags: ["ai-agents", "saas", "strategy"]
description: "AI agents can now pull apart any product and rebuild it clean-room. That reprices the software moat: COTS, SaaS, and the multiples built on them."
draft: false
hero: "img/posts/your-code-is-not-the-moat-anymore/hero.png"
hero_alt: "Navy and amber graphic with the headline Your Code Is Not the Moat Anymore"
---

Reverse engineering used to be a rare expert discipline. You needed someone who could read assembly like prose and had weeks to spend. Now it is a prompt.

[REA](https://github.com/morluto/rea), with some 130,000 GitHub stars, is a single MCP server that plugs reverse engineering tools into AI agents: native binaries through Hopper, Ghidra, or IDA, plus Electron apps, .NET assemblies, and websites. The pitch is literal. See a feature you like. Understand how it works, down to the binary level. The workflow ends where you would expect: show me the evidence, and build a version for my project.

ArtCraft is what the second half looks like at product scale. Brandon Thomas's project started as an AI image editing tool and pivoted last week to clean-room reimplementations of all seven Adobe creative apps, written in Rust with heavy assistance from Claude Opus 5.5 and open sourced under MIT and Apache licenses. Days later came Word, Excel, and PowerPoint clones. The method is studying behavior and rebuilding from scratch, which is the part that keeps the lawyers calm.

Start with the COTS incumbents. Their moat was decades of features plus switching costs. The feature half is now attackable by a small team with a frontier model. What survives is the part AI cannot clone: certifications, accreditations, contractual liability, support. In regulated markets that is a real moat. A clean-room clone does not come with an authorization to operate. In unregulated markets, pricing power erodes first.

SaaS incumbents look safer until you look closer. Their moat was never just features. It is data gravity, ten years of your records in their cloud, plus the ecosystem of integrations, plus the operational burden of running it yourself. A clone cannot copy your data or your integrations. But two things are moving against them. First, unbundling: suites bundle dozens of features, customers use a fraction, and the clone playbook rebuilds just the slice people actually touch. Second, agents lower integration switching costs, which weakens the ecosystem lock-in over time.

Then the stock market. Software multiples price moat durability. The high gross margins and premium valuations assume the IP stays defensible and the switching costs stay high. If feature parity gets cheap and fast, that assumption breaks for pure-feature moats, and the repricing can front-run reality. Expectations move faster than code. The companies that hold value are the ones whose moats were never just code: data gravity, regulatory position, distribution, and the incumbents turning the same capability inward to out-build everyone else.

One honest caveat. Today's clones are early alpha and parity claims are marketing. Nobody is replacing Photoshop or Excel this quarter. The threat is not this month's alpha. It is the trajectory and the repeatability of the playbook. Every enterprise architect should be asking the same question of their portfolio: what in our stack survives when pulling apart products becomes a commodity? Whatever the answer is, that is the actual moat. Build there.
