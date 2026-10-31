---
title: "Your Code Is Not the Moat Anymore"
date: 2026-10-12
tags: [agents, saas, strategy]
description: "AI agents can now pull apart any product and rebuild it clean-room. That reprices the software moat: COTS, SaaS, and the multiples built on them."
draft: false
hero: "img/posts/your-code-is-not-the-moat-anymore/hero.png"
hero_alt: "Navy and amber graphic with the headline Your Code Is Not the Moat Anymore"
---

Reverse engineering used to be a rare expert discipline. You needed someone who could read assembly like prose and had weeks to spend. Now it is a prompt.

[REA](https://github.com/morluto/rea), with some 130,000 GitHub stars, is a single MCP server that plugs reverse engineering tools into AI agents: native binaries through Hopper, Ghidra, or IDA, plus Electron apps, .NET assemblies, and websites. The pitch is literal. See a feature you like. Understand how it works, down to the binary level. The workflow ends where you would expect: show me the evidence, and build a version for my project.

[ArtCraft](https://getartcraft.com/) is what the second half looks like at product scale. Brandon Thomas's project started as an AI image editing tool and pivoted last week to clean-room reimplementations of all seven Adobe creative apps, written in Rust with heavy assistance from Claude Opus 5.5 and open sourced under MIT and Apache licenses. Days later came Word, Excel, and PowerPoint clones. The method is studying behavior and rebuilding from scratch, which is the part that keeps the lawyers calm.

Before the playbooks, rank what actually survives. Not all moats erode at the same speed. Data gravity survives: ten years of your records cannot be cloned. Regulatory position survives: a clean-room clone does not come with an authorization to operate. Distribution survives: the channel and the customer relationship are not in the binary. Integration complexity survives: the hundred connectors around the product are harder to rebuild than the product. What dies first is the pure-feature moat, the thing that was only defensible because rebuilding it used to cost more than buying it.

Enterprises should triage their portfolio into three buckets. The exposed bucket holds pure-feature tools and internal utilities, the things you buy because building them was never worth it. For these, clean-room rebuild just joined build-versus-buy as a third option, and the math changed. The durable bucket holds systems of record and regulated workloads, where data gravity and compliance do the defending. Leave those alone. The strategic bucket holds where you differentiate. That is where investment goes. Then take the vendor list and ask each strategic vendor one question: what is your moat beyond features? The ones with a good answer keep their pricing power. The ones without it are about to discount.

VARs face the same shift from the other side of the table, and the math favors them if they move early. Product margin compresses as features get cheaper to replicate. Services margin expands as customers need help rethinking their stacks. The playbook has three moves. First, sort vendor lines by moat durability and lean into the vendors whose moats are regulatory, data-heavy, or integration-deep. Expect price pressure everywhere else. Second, build the advisory practice now: stack-rethink assessments, clone-versus-keep analysis, integration of best-of-breed rebuilds. Customers are about to make these decisions with or without you. Third, name the risk honestly. If customers can rebuild directly, the middleman gets cut out. The defense is becoming the advisor they call before they rebuild, not the reseller they route around.

Then the stock market. Software multiples price moat durability. The high gross margins and premium valuations assume the IP stays defensible and the switching costs stay high. If feature parity gets cheap and fast, that assumption breaks for pure-feature moats, and the repricing can front-run reality. Expectations move faster than code. The companies that hold value are the ones whose moats were never just code: data gravity, regulatory position, distribution, and the incumbents turning the same capability inward to out-build everyone else.

One honest caveat. Today's clones are early alpha and parity claims are marketing. Nobody is replacing Photoshop or Excel this quarter. The threat is not this month's alpha. It is the trajectory and the repeatability of the playbook.

Two questions to close. Enterprises: what in your portfolio survives when pulling apart products becomes a commodity? VARs: where does your margin live in five years? Whatever the answers are, that is the actual moat. Build there.
