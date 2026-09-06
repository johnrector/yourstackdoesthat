---
title: Send invoices and chase the late ones
domain: small-business
added: 2026-09-06
uses: connector, skill, scheduled task
setup: A connector to the ledger or the invoicing record. A skill for your invoice and your reminder tone.
---
## The need
Invoices go out when the work is done. Reminders go out at thirty days, sixty days, and ninety days, politely, without you remembering.

## What you used to buy
An invoicing app with a monthly fee, and the reminders you sent late because you did not like sending them.

## Your stack does that
It writes the invoice from the job record, sends it, watches for payment, and sends the reminders on schedule in the tone you chose.

## How, in plain terms
A connector to wherever jobs and payments are recorded. A skill with your invoice format and three reminder templates. A scheduled task each morning that checks what is due and what is overdue. Honest note: the ledger is a record; keep the accounting system or the spreadsheet. What goes away is the invoicing layer in front of it. Taking the payment itself still goes through the bank or the processor.
