# Contributing

Everything here is public domain (CC0). By contributing you release your words the same way. Do not contribute anything you are not willing to give away.

Two kinds of contribution. Both are plain markdown files. Open a pull request; a person reads it.

## A Does entry

One file in `content/does/`, named with a short slug, for example `bill-about-to-be-late.md`.

```
---
title: Know when a bill is about to be late
domain: money
added: 2026-09-06
uses: connector, scheduled task
setup: A connector to the bank, or statements forwarded to a folder.
---
## The need
One to three sentences. The situation, from the person's side.

## What you used to buy
What the app era sold for this need. A category, not a brand, unless the brand is the whole point.

## Your stack does that
What the stack does instead, in the present tense.

## How, in plain terms
Which part of the stack does the work: a connector, a skill, a scheduled task, memory, or a combination. Say what still requires setup. Say where it is rough.
```

Fields:

- `domain` is one of `household`, `money`, `health`, `work`, `school`, `small-business`.
- `added` is the date you wrote it, `YYYY-MM-DD`. It drives the feed.
- `uses` is a comma-separated list from: `connector`, `skill`, `scheduled task`, `memory`.
- `setup` is one sentence on what a person has to stand up. Optional but encouraged.

All four `##` sections are required, with those exact headings.

## A Cancel Ledger line

One file in `content/ledger/`, named `YYYY-MM-DD-slug.md`.

```
---
replaced: A social media scheduler
cost: $15 a month
replaced_by: A scheduled task and a connector to the account
result: replaced
date: 2026-09-06
---
One or two sentences, optional.
```

`result` is `replaced` or `kept`. For a kept line, `replaced_by` holds the reason it was kept. Lines that say "kept" are welcome; they are the Stack Test working.

## Operating recommendation

Use [Design for Batch](https://yourstackdoesthat.com/design-for-batch/) for architecture examples: discovery, preparation, holistic reasoning, finite execution and receipts for the next fresh batch. Only calls and texts stay conversational from permitted preexisting CRM knowledge. All substantive work is batched; email has no live bypass.

Describe finished work and actual outcomes, not merely a draft or dispatch. Let the assistant evolve its own CRM and learn general practices; avoid named-person patches. Preserve actual setup and access gaps. No independently continuing session per request or long-running business state machine.

## The rules

- Provider-neutral. Never name a frontier stack as the one that does it. If only one can today, say "in some stacks" and describe what is needed.
- Honest about setup. "With setup" is a real answer.
- Categories, not brands, in the ledger. A product that lost to a skill file did nothing wrong.
- Nothing for sale, including your own.
- Short declarative sentences. No hype, no emoji, no exclamation marks.
- No business jargon. Write for a person.

## Building the site

`python3 build.py` regenerates `site/` from `pages/`, `content/`, and `static/`. Python 3, standard library only. The `site/` folder is what gets deployed; Netlify runs the script on every deploy. You do not need to run it to contribute.
