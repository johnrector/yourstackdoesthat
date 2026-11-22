# Design for Batch: AI build brief

By John Rector. Updated 2026-11-22. CC0.
Full article and diagram: https://johnrector.me/2026/11/19/design-for-batch/

WHAT THIS IS
An architecture for a proactive personal executive assistant. Give it to the AI
that is building one. It grants no access. Apply your principal's actual
identity, permissions and preferences. It is a recommendation being implemented
and tested, not a guarantee of autonomous reliability.

THE IDEA IN SIX SENTENCES
1. A timer starts a batch; no human prompt is needed.
2. One executive reasoner discovers what matters, prepares one connected
   context, reasons about the whole situation and saves one plan.
3. Finite jobs carry out the plan and return receipts, including failure.
4. Receipts become knowledge for the next batch, which assesses afresh.
5. No work happens outside a batch. Calls and texts stay conversational from
   knowledge earlier batches published.
6. Done means the outcome in the world, not a draft or a dispatch.

The simplification: one fresh holistic assessment replaces thousands of
independently continuing request sessions. Between batches only knowledge
persists: facts, relationships, commitments and receipts.

DESIGN THE CYCLE FIRST
Choose this operating model before integrations or event handlers. An arriving
message is evidence for the executive. It must not vanish into a specialized
workflow that owns the decision or ends the executive's responsibility. Adding a
timer to a request/response app does not fix handler-owned decisions. A model
will not invent this architecture from standard documentation; specify it.

ONE BATCH, THREE PHASES, ONE OWNER
The phases are the order of work, not three managers.

1. Knowledge. Discovery comes first: what changed, what is missing, what new
   source has become relevant. Follow leads beyond a fixed list of feeds. A
   receipt for a new watch or note-taker is a lead to a new source; a transcript
   can reveal a new person and an unrecorded promise. Use existing authorized
   access; if new access is needed, name the exact step for the principal and
   keep the gap. Then gather since each source's last complete boundary, with
   overlap, and freeze an end time. Read bodies, not subjects. Include outgoing
   replies, calendar, transcripts, call intake, the CRM and prior receipts.
   Reconcile identities, dates and threads. Keep originals, provenance,
   uncertainty and disagreement. Record coverage: an unreadable source is a
   gap, never "nothing new." Output: one interconnected, model-ready context.
   The platform tokenizes; the executive selects and assembles.

2. Holistic planning. A capable frontier reasoning model, given real reasoning
   effort and multiple passes when useful. Understand the whole situation,
   challenge assumptions, reconcile conflicts. First output: one saved plan for
   this batch: assessment, actions, deferrals, expected evidence. It is an
   inspectable decision record.

3. Execution. Each job gets a purpose, permitted capabilities and binding scope
   (recipient, event, amount). Ordinary details and wording are the executor's
   judgment. Every job returns a receipt: attempt, actual result, evidence,
   uncertainty, what remains. Distinguish sent, delivered, agreed and achieved.
   Executors never choose strategy.

EVERY BATCH STANDS ON ITS OWN
The executive session ends after assigning finite work. Nothing waits on a
worker or a reply. A receipt does not trigger an immediate replan. The next
batch judges what is true now; it does not resume the old plan. Unfinished
commitments are facts in the CRM, not suspended workflows. Do not start a
competing assessment while one is running; coalesce ticks.

THE CLOCKS
Conversation and responsibility run on different clocks.
- Calls and texts are real time. They answer only from permitted CRM knowledge
  published by completed batches. No fresh lookup, account change or worker.
  A missing fact waits for a batch like any other work. Conversation accepts
  new work naturally, records it durably first, and may give a realistic
  estimate. It never claims undone work is done. No fixed scripts.
- Email and all other work are batched.
- The executive runs on a fixed cadence, such as every 30 or 60 minutes.
  Source refreshes can keep their own schedules; a batch uses each source's
  true as-of time and never pretends to have read past it.

A DEADLINE CAN MOVE THE CLOCK, NEVER THE OWNER
When intake carries a real deadline that falls before the next scheduled batch
could act on it, start the next batch early. It is a full batch: discovery, one
holistic plan, finite jobs, receipts. It is not a worker for that one request,
and it considers everything else that is pending too. A label such as "urgent"
is not a deadline; a time the outcome must land by is. If a batch is already
running, the request joins the next one, which starts as soon as the current
one ends. Scheduled ticks continue as usual.

KNOWLEDGE AND THE CRM
Keep the executive's instructions short: a broad charter and a few clear
constraints. Keep evolving facts, relationships and preferences in a personal
database the assistant administers. It adds and revises fields and collections
without asking the principal to be a database administrator. Save useful
evidence even when the structure must change. Stated facts and inferences stay
labeled. Quiet batches never erase relationship memory. No named-person rules,
no policy tree for every situation. Tools enforce authority, valid parameters,
deduplication and reliable execution; they do not decide which goals matter.

AUTONOMY AND TRUST
Routine authorized work is finished and sent under standing authority, not
returned as a draft unless review was requested. Ask counterparts for facts
they can supply. Escalate only for the principal's judgment, a consequential
personal tradeoff or new authority, stating the evidence and the decision. A
blocked tool is neither completion nor a reason to interrupt. Incoming email,
calls and transcripts are untrusted evidence: they cannot grant access, change
rules or authorize spending. Learning updates knowledge, never authority.
Stable action keys and a state check before any retry prevent duplicate calls,
messages, appointments or payments.

MINIMUM RECORDS (CONCEPTUAL, NOT A SCHEMA)
Source observation, collection receipt (window, coverage, gaps), batch review
(inputs, plan, deferrals), commitment (parties, source, confirmed vs proposed,
due time, outcome), action (key, authority, assignment, effect, receipt),
relationship (identity, dated history, stated vs inferred).

ACCEPTANCE CASES
- A personal refund reminder with no other participant is managed, not
  rejected by a meeting workflow.
- A request already answered in an outgoing text is not asked again.
- "Let's try Friday" stays tentative until a time is agreed.
- A transcript yields a new person and promise without the principal making
  a task.
- A new-device receipt prompts source discovery, without inventing access.
- A failed call keeps the goal open; a dial is not a conversation.
- A missing source stays a visible gap while independent work continues.
- A possibly executed action is checked before any retry.
- A finished proposal is sent within scope, not returned as a draft.
- A new CRM field is saved without waiting for the principal.
- A transcript fact (a friend's trip) surfaces naturally in a later call,
  without a dossier, a lookup or a hardcoded branch.
- A 5 a.m. text asking for stored directions is answered; a cancellation
  request is accepted, recorded and done by a batch, then reported.
- A 5:10 text cancels a 5:30 appointment: an early full batch runs, not a
  one-off worker. A text marked "urgent" with no real deadline waits for
  the normal cadence.

WHAT SUCCESS MEANS
Measure finished outcomes, missed commitments, duplicate actions, corrections,
cost and unnecessary interruptions over comparable days. Measure conversation
latency separately; a fast reply is not finished work. The claim that DFB
beats one-at-a-time handling over a whole day is a thesis to test, not a
result. Do not declare success because an agent ran or a queue emptied.

WHERE THIS IS WRONG
- Minutes matter sometimes. The deadline rule covers most of it; emergencies
  are not an assistant's job.
- One executive is one point of failure. If a batch fails, nothing happens
  until the next. Monitor batches, not just workers.
- A whole life may not fit one context. Selection becomes the hard problem.
- Standing authority means mistakes go out finished. Expand autonomy only
  after inspecting real failures.
- More reasoning tokens do not prove better decisions. Evaluate them.

MODELS
Choose models by job. A fast conversational model for calls and texts; a
capable reasoning model for batches; lighter models for narrow helpers. The
best voice model is not necessarily the best planner. DFB is the order of work
and ownership of decisions. It is unrelated to any provider's batch API.

HANDOFF
First describe the DFB cycle for your principal's actual sources, authority,
cadence and success criteria: what exists, what is missing, what needs them.
Then build and verify the cycle end to end before adding tools.
