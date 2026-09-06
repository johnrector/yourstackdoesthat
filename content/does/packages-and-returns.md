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
It reads the order confirmations and shipping mail as they arrive, keeps a list of what is coming, flags anything late, and counts down return windows so you are told on day twenty-five, not day thirty-one.

## How, in plain terms
A connector to the mail account. A scheduled task each morning that scans for order, shipping, and delivery mail, updates one running list, and speaks up only when something is late or a return window is closing. Some carriers block automated lookups of their tracking pages; the mail is usually enough on its own.
