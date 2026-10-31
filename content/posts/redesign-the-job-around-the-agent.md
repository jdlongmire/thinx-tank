---
title: "Redesign the Job Around the Agent"
date: 2026-10-25T07:22:00-05:00
tags: [agents, workforce, governance, operations]
description: "Gartner found only 4 percent of CIOs have plans to redesign roles for a human and agent workforce. The agent gets a written job. The people around it usually do not, and supervision added on top of a full job is supervision that fails."
hero: "img/posts/redesign-the-job-around-the-agent/hero.png"
hero_alt: "Bold text reading Redesign the Job Around the Agent on a deep navy background with amber accents and two job cards, one written and one blank."
---

Four percent. That is the share of CIOs who have a plan to redesign roles for a workforce made of people and agents working together.

[Gartner surveyed 2,002 CIOs and technology executives for its 2027 CIO and Technology Executive Agenda, and CIO Dive reported the workforce findings on October 19](https://www.ciodive.com/news/gartner-survey-CIOs-workforce-revamp/833405/). Only 4 percent reported plans in place to revamp roles with a human and agent workforce in mind. The firms that do have such plans are 2.4 times more likely to be top performers with AI, with CEOs who report value from it. The rest of the picture explains the gap: 58 percent of leaders face increased demand to show cost improvements from prior AI spending, and only 13 percent report significant or transformational value from AI so far. Cost pressure is immediate. Role redesign is not. So the redesign loses.

I read that as an operations failure, not an HR miss. Look at what a typical agent deployment actually writes down.

## One side gets a spec. The other side gets a slogan.

The agent side of a deployment is usually well specified. Instructions. Tool access. Data scope. A budget. An identity. I have argued for each of those in this series, and I still do.

The human side gets one line: a person will supervise it.

Supervision is not a line. It is work. Someone has to read output closely enough to catch a confident error. Someone has to decide which exceptions stop the run and which ones pass. Someone has to notice when the work the agent does well in week one has quietly changed by week six, because [the agent you approved is not the agent running](https://blog.thinxai.net/posts/the-agent-you-approved-is-not-the-agent-running/) after the updates, the new data, and the small instruction edits nobody logged as a release.

When that work is added on top of an unchanged job, it loses to the job. The calendar is already full. The review becomes a glance, then a habit of approval, then a rubber stamp with a name attached. The name still carries the accountability. The hours to discharge it were never assigned. That is the worst arrangement available: blame priced in, capacity priced out.

"Human in the loop" does not fix this. The phrase says nothing about which human, with what knowledge, holding what authority, spending how much time. A junior employee told to watch an agent that does senior work is not a control. A domain expert with no power to pause the run is not a control either. Both are decoration on an org chart.

## Write the human job with the same care as the agent job

Before an agent goes live, I want five things written down for the people around it. They are parallel items, so they get a list:

1. A named supervisor, qualified in the work itself, not just senior in rank. The person checking the output must be able to do the task slowly if the agent vanished tomorrow.
2. Stop authority that works in the tool, not in a meeting. The supervisor can pause the agent, on the spot, without a ticket, a call, or permission from the team that shipped it.
3. The escalation line, in writing. Which decisions the agent finishes alone, which ones it drafts for review, and which ones it may not touch. Put numbers on it where numbers exist: amounts, record counts, customer impact.
4. The review load, priced in hours. Estimate the weekly time the checking actually takes, name what existing work stops or shrinks to make room, and treat the review time as part of the agent's operating cost, the same way [every agent needs a budget](https://blog.thinxai.net/posts/every-agent-needs-a-budget/) for its tokens and tool calls.
5. A changed measure of success. The supervisor's job is now judged in part on the quality of the combined output, theirs and the agent's. If the review still measures only the old output, the old output wins every busy week.

None of this needs a reorganization. It needs one page per deployment, written before launch, owned by the manager who owns the result. That page is also where the handoff lives: [data access is not process context](https://blog.thinxai.net/posts/data-access-is-not-process-context/), and it is not a job description either. The supervisor needs to know what should happen next when the agent finishes, stalls, or hands back something odd, and that knowledge has to be written, not assumed.

## The test I would run

Pick your busiest agent deployment and ask the supervisor two questions. How many hours a week do you spend checking this agent? And what did you stop doing to get those hours?

If the first answer is a shrug and the second answer is nothing, you do not have supervision. You have a name in a field. Gartner's 4 percent is low, but the fix is not a workforce transformation program with a steering committee. It is smaller and harder: for each agent you run, write the human job next to it, with hours and authority attached, before you count the deployment as done.

An agent with no redesigned human job around it is not a workforce change. It is unpaid review work assigned to nobody, waiting for the first bad output to find its owner.
