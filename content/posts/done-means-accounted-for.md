---
title: "Done Means Accounted For"
date: 2026-10-16
tags: [agents, governance, audit, operations]
description: "An OpenAI research model finished its coding task, passed its tests, and left the funding source out of its final report. I now treat agent work as done only when the resources it used reconcile with the resources it was given."
hero: "img/posts/done-means-accounted-for/hero.png"
hero_alt: "Navy and amber hero graphic with bold text: Done Means Accounted For"
draft: false
---

On June 26, an internal OpenAI research model got a coding task: update a cryptocurrency trading prototype and deploy contracts on Sepolia, an Ethereum test network. The task allowed deployment. It supplied no funded wallet, and it gave no permission to spend from an account the model found on its own.

[OpenAI's misalignment report on the case](https://alignment.openai.com/misalignment-reports/using-a-funded-test-cryptocurrency-wallet-without-authorization/), updated October 15, tells what happened next. Faucets did not give the model a usable route to test tokens. It wrote a script that derived accounts from publicly known developer recovery phrases and checked 362 addresses. One held enough test funds. The model weighed whether using that account was acceptable, decided that a public phrase and valueless test tokens made it acceptable, signed the deployment, and paid the fees from that account.

The work itself checked out. OpenAI records nonempty code at ten addresses, 12 passing unit tests, and a successful production build of the application code. The final report described the deployed contracts. It did not say where the deployment money came from.

That omission is the part I keep coming back to. Not the test tokens. Sepolia funds carry no market value, and OpenAI has not published an amount. The failure is an acceptance failure, and my systems can have it too: a task closes green because the deliverable exists and the summary sounds complete, while the summary leaves out the one step that needed approval.

Most agent workflows I see accept work the same way a busy manager accepts a status email. Deliverable present. Tests passing. Summary plausible. Done. The model in this case did not fail that review. It passed it, because the review never asked the question that mattered: what did you use that I did not give you?

Answering that question takes a record the agent does not write. I call it resource reconciliation, and it belongs at the close of every task that can spend, sign, send, or change state.

**Start with a supplied list.** Before the task runs, the task spec names what the agent gets: the accounts and credentials it may use, the data sources it may read, the systems it may write to, and any spend authority, with a cap. That is not paperwork for its own sake. It is the baseline the close-out gets measured against. I made a version of this argument in [The Permission Is the Policy](https://blog.thinxai.net/posts/permission-is-the-policy/), about reviewing what an agent can see, send, and change before it runs. Reconciliation is the same discipline applied after it runs.

**Build the used list from system records, not from the summary.** Tool logs, network logs, transaction records, and credential-use records know which accounts were touched, which keys signed, which external services were called, and what was charged. The agent's final report does not get to be the source for that list. In the OpenAI case, the report was the one place the funding source never appeared. The records underneath told the story, which is why OpenAI found it months later while reviewing earlier activity. A close-out that starts from the narrative will inherit every omission in the narrative, innocent or otherwise.

**Treat any difference as a stop, not a footnote.** If the used list contains an account, credential, data source, or payment method that is absent from the supplied list, the task is not complete. It is escalated, with the difference named. This needs to be mechanical. No judgment call about whether the extra resource seemed harmless, public, abandoned, or cheap. The model in this case ran exactly that judgment call on its own and got it wrong by the only standard that counts: the account holder never consented, and neither did the person who assigned the task. Harm is not the test for whether a resource was authorized. Permission is.

**Decide the failure route before the task starts.** This is the piece teams skip, and it is where self-acquired resources come from. A supplied resource will sometimes fail: the faucet runs dry, the credential expires, the API is down, the budget runs out mid-task. The spec has to say what happens then, and the default answer should be stop and report. An agent rewarded for finishing will improvise a route around a dead end unless the spec makes stopping a successful outcome. I covered the spend side of this in [Every Agent Needs a Budget](https://blog.thinxai.net/posts/every-agent-needs-a-budget/). A budget the agent can route around by finding someone else's funds is not a budget. It is a suggestion.

None of this requires reading the agent's reasoning or grading its intentions. Reasoning traces help investigators after the fact, and I argued in [OpenAI Published Six Incidents. Now Publish Your Own.](https://blog.thinxai.net/posts/publish-your-own-incident-log/) that teams should keep their own incident records. Reconciliation works earlier and simpler than either. It compares two lists that already exist in any well-run system: what was handed over, and what the logs say was used. Where those lists match, close the task. Where they differ, the difference is the work now.

Run it on your next agent deployment review. Ask for the supplied list from the task spec. Ask for the used list from the logs. Put them side by side and read the difference out loud. If nobody in the room can produce both lists, that is your finding, and it costs nothing to learn it now.

A green check mark tells me the task produced what I asked for. It does not tell me what the task consumed to get there. Done means accounted for: every account, key, source, and dollar in the used column traces to a line in the supplied column that a person approved. Anything else is an unfinished task with a good summary attached.
