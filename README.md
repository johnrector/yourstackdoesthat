# Your stack does that

**Let your stack do that. Give your attention to something else.**

Apple’s 2009-era “There’s an app for that” invited people to find a capability. Our invitation is to hand over the work. This repository is John Rector’s public guide to personal stacks, Design for Batch (DFB), and the website [yourstackdoesthat.com](https://yourstackdoesthat.com).

App People use software to achieve an outcome. Stack People delegate the outcome to a personal AI. Both benefit from the result; App People launch the app, follow its prescribed steps and push the buttons, while Stack People let the AI carry that work without initiating each job. The relationship is proactive: the assistant notices work and acts within standing authority without waiting for the person to prompt each job. The standard is thoughtful work actually **done**: a proposal reaching its recipient, an appointment change confirmed, a refund outcome understood. A draft or dispatch is not that result.

## Start here

- [Design for Batch](DESIGN-FOR-BATCH.md): architecture, boundaries and acceptance cases.
- [Full article and diagram](https://johnrector.me/2026/11/19/design-for-batch/): the argument and worked examples.
- [AI build brief](static/design-for-batch.md): give this plain-text file to your builder.
- [Executive](prompts/executive.md), [conversation](prompts/conversation.md) and [executor](prompts/executor.md) prompts: starting points to adapt to actual authority and capabilities.
- [Example batch plan](examples/batch-plan.json): illustrative finite assignments, not an executable API contract.

## Three layers

1. **Personal database.** Relationships, preferences, commitments and real outcomes. The person controls the stack and delegates ordinary CRM administration to the assistant. Let it evolve fields and records without making the human a DBA.
2. **Reasoning.** One executive discovers knowledge, gathers and prepares a coherent context, reasons deeply about the whole situation, saves one plan and assigns finite jobs.
3. **Conversation.** Responsive calls and texts from permitted CRM knowledge published by completed batches. New work and missing facts enter the next batch. Email is entirely batched.

Connectors, skills, tools, timers and source reservoirs serve these layers. They do not seize executive responsibility.

## The simplification

One fresh holistic assessment on a timer replaces thousands of independently continuing request sessions. Each batch stands on its own. Between batches retain **knowledge**: facts, relationships, commitments and receipts. Do not suspend a parent session waiting for a worker or automatically resume an old business plan.

Discovery comes first. Preparation connects evidence. High reasoning chooses the whole-batch plan. Executors receive purpose and consequential scope, use judgment on ordinary details and return detailed receipts, even on failure. Those receipts are knowledge for the **next** fresh batch.

**All substantive work is batched.** Calls and texts stay conversational using prior completed CRM knowledge. No fresh fact lookup, urgent bypass, per-request worker or receipt-triggered recovery. A real deadline before the next scheduled batch starts the next full batch early; it never starts a one-off worker.

## Autonomy and growth

Complete ordinary authorized work rather than ask the principal to supervise it. Escalate genuine needs for that person’s judgment or new authority. Imperfect ordinary work is a learning opportunity. Revise general practices, inferences and CRM organization; avoid rules coded for named people. Growth and useful responsibility matter more than tidy records.

DFB is a recommendation we are implementing and testing, not an official model architecture or any provider’s batch API. Choose models by job: a fast conversational model for calls and texts, a capable reasoning model for batches. Better whole-day quality, cost and effectiveness are a thesis to measure against actual outcomes.

## This repository

This is a public reference and static site, **not a turnkey assistant service**. It contains no account credentials or claim that every capability has been implemented.

- `pages/`: authored site pages with front matter.
- `content/does/`: capability examples and setup requirements.
- `content/ledger/`: historical subscription examples, retained as history.
- `static/`: CSS, machine-readable brief and static assets.
- `build.py`: standard-library Python static builder.
- `site/`: generated output, not committed. Netlify builds from Git.

Run `python3 build.py`, then serve `site/` locally. Read [CONTRIBUTING.md](CONTRIBUTING.md) to add useful capabilities or lessons. Every word authored here is [CC0](LICENSE); the Apple slogan remains attributed to Apple. Maintained by [John Rector](https://johnrector.me/).
