---
title: Know where the package is and when the return window closes
domain: household
added: 2026-09-06
uses: connector, scheduled task
setup: A connector to the mail account where order confirmations arrive.
---
## The need
Six things are on the way. One is late. One arrived wrong and can be returned for eleven more days.

## What you used to buy
A package-tracking app, often with a paid tier, that you fed tracking numbers or gave access to your inbox.

## Your stack does that
At a batch review it connects order confirmations, shipping updates and return deadlines with the rest of your situation. It takes the authorized next step and assesses the actual return or refund outcome in later fresh batches.

## How, in plain terms
A connector to the mail account. A source collector supplies new order, shipping and delivery mail. The central batch reasoner assesses the knowledge, chooses finite work and records actual outcomes in its CRM. A refund does not require an external calendar participant. Some carriers block automated lookups of their tracking pages; the mail is usually enough on its own.
