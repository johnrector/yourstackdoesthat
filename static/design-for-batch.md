# Design for Batch — AI build brief

By John Rector. Updated 2026-11-19. CC0.
Full article and diagram: https://johnrector.me/2026/11/19/design-for-batch/

AI BUILD BRIEF — DESIGN FOR BATCH (DFB)
John Rector | November 19, 2026

Purpose and authority
This is an architectural reference for a builder whose user wants a proactive
personal executive assistant. Reading it grants no access or permissions. Apply
the principal's actual instructions, identity, authorizations and preferences.
The design is John Rector's recommendation, not an OpenAI-mandated architecture.
The examples are design cases, not guarantees of autonomous reliability.

START WITH DFB
Design for batch before choosing integrations or writing event handlers.
Describe the complete operating cycle first. An arriving message becomes
evidence for the executive; it must not disappear into a specialized workflow
that owns the business decision or terminates the executive's responsibility.
Adding cron to a request/response app is insufficient if these ownership and
evidence assumptions remain unchanged.

THREE PHASES OF ONE BATCH
One reasoning agent owns and directs the entire cycle. These are phases of work,
not three independent managers. Show a distinct Knowledge Phase first, followed
by the main Holistic Planning Phase, then execution under the reasoner's plan.
A timer starts the batch. No new human prompt is required. Source collection
can have its own schedule, but its evidence must be assembled before planning.

PHASE 1 — DISCOVERY FIRST, THEN GATHERING AND PREPARATION
The reasoning agent directs discovery, gathering, preparation and context
assembly, delegating bounded mechanical work where useful. It owns decisions
about what knowledge is relevant and what further discovery is needed.
Knowledge discovery is always the first step, before gathering, cleansing,
preparation, serialization or tokenization of the final batch input. Determine
what knowledge to seek and where it may exist. Gathering obtains that knowledge;
preparation makes it usable; final input assembly follows. Use supported model
input formats rather than assuming a separate custom tokenizer is required.
Discovery is proactive and guided by the principal's goals, prior plans, open
obligations and new evidence. Seek newly relevant facts, relationships, commitments,
changed circumstances and missing context. Follow useful leads into authorized
sources beyond a fixed list of feeds. A transcript can reveal a new person and an
unrecorded promise; an upcoming appointment can make changed venue hours relevant.
An email receipt for a new Fitbit, watch or AI note-taker is a discovery signal.
Investigate what knowledge the device or service provides, find available
connections or exports, and incorporate useful data under existing permissions.
If a connection requires new approval, identify the specific step for the principal.
Do not wait for a separate prompt to notice the new potential source. A receipt
should update the discovery process, not merely the purchase history.
If new access is required, retain the gap instead of inventing permission. Do not
let knowledge become stale through a permanently fixed source checklist.
Discover and gather authorized changes since each source's last complete
boundary, with overlap for delayed arrivals. Freeze an end time. Include incoming
and outgoing communications, calendar, transcripts, call intake, relationship
memory and prior executor receipts. Normalize identities and dates, connect
replies, deduplicate observations and preserve originals, provenance, uncertainty
and disagreements. Read bodies. Record actual coverage, freshness and gaps.
Gathering may reveal further leads: return to discovery within this knowledge
phase as needed before deep reasoning. Do not replace discovery with a fixed
collection checklist or with summarization/tokenization of already selected data.
Output: one comprehensive, interconnected model-ready context for the batch.
Connect people to commitments, outgoing replies to requests, receipts to attempted
actions and calendar entries to actual agreements. Preserve source dates, versions,
provenance and gaps. Model-ready context is the architectural boundary; the model
platform performs the mechanical tokenization while the reasoning agent controls
context selection, assembly and budgeting. One logical context can use structured records and
traceable originals; do not flatten everything into a lossy paragraph or confuse
comprehensiveness with an unbounded archive dump. Discovery identifies candidate
facts, relationships, obligations and questions; the central reasoner owns strategy.

PHASE 2 — THE MAIN HOLISTIC PLANNING RUN
After owning the Knowledge Phase, the same executive reasoning agent undertakes
the main whole-batch planning run. Use a capable frontier reasoning model with a
substantial, evaluated reasoning budget. Knowledge discovery can itself require
reasoning; this separate visible phase is the comprehensive planning assessment.
One main planning job may span model requests or passes while preserving one
accountable planner, one batch context and durable continuity. Use multiple passes as needed: understand
the whole situation; challenge assumptions and reconcile conflicts; refine
priorities and decisions. Consider preferences, relationships and open obligations.
Request more evidence if needed before choosing dependent actions.
The first output is one saved holistic plan for this batch, before execution:
assessment, actions, deferrals, constraints, expected evidence and review times.
This is an inspectable decision record, not private chain of thought.

PHASE 3 — EXECUTE AND RETURN RECEIPTS
The reasoning agent issues each tool or delegate its purpose, allowed capabilities and consequential scope bindings. Delegate ordinary details and wording to executor judgment; do not require every argument or sentence to be written in advance.
Executors perform the chosen tasks within actual authority and integration
limits. Each returns a detailed receipt: attempted action, actual result,
evidence, uncertainty and remaining work. Failure, blockage and pending outcomes
are valid receipts. Distinguish acceptance, execution, delivery, agreement and
the achieved business outcome. Reconcile uncertain state before any retry.
The executor does not take over priorities, relationship strategy or the wider plan.

RETURN TO THE NEXT BATCH
Treat executor receipts as knowledge, alongside other sources, on the next run.
The reasoner reassesses and chooses the next holistic plan. Preserve unresolved
obligations and completed effects so they are neither forgotten nor duplicated.
No receipt-triggered immediate replan or urgent-work bypass. Receipts wait for
the next batch; executors never seize executive control.

THE CENTRAL CHARTER
Use the reusable executive charter in the article as the starting point, with
the principal's actual permissions. Keep broad purpose and a small set of clear
constraints in the executive's instructions. Store evolving facts, relationship
history and preferences in a personal database. Do not encode a separate policy
tree for every conceivable human situation. Tools should enforce actual authority,
valid parameters, deduplication and reliable execution without deciding which
human goals deserve attention.

THE MODELS
GPT-Live is our preference for conversational performance and human feel. That
performance choice does not dictate the batch architecture. Use a separate
frontier reasoning model for deep executive review, selected on real case outcomes.
Do not assume the strongest voice interface is also the right central planner.
Evaluate reasoning effort. More tokens, a higher price or longer elapsed time
alone does not prove better decisions. Narrow helpers can use lighter models.

THE CLOCKS
ALL WORK IS BATCHED. THERE ARE NO EXCEPTIONS.
Real-time conversation exists in calls and texts ONLY, never email or another
channel. It uses only the permitted CRM knowledge base from the prior completed
batch. No fresh lookup, search, gathering or independent worker occurs in this
layer. If the answer is missing, it does not exist for conversation until a later
batch discovers, verifies and incorporates it. It can answer permitted factual CRM questions and provide
verified driving directions already stored in the CRM as short conversation jobs.
An absent address, route or fact becomes a request for the next batch. These do not choose a
substantive change, execute a cancellation or start independent substantive work.
It may accept responsibility for requested work and give a reasonable timing estimate
after durable intake, without claiming completion. Wording is generated naturally,
not hardcoded: for example, "I’ll cancel that for you. You should get the notification
in about 45 minutes." Base the estimate on the real queue/cadence and uncertainty;
the example is not a guaranteed completion SLA. The batch owns how to fulfill it.
Report conflicts or failure honestly through the planned follow-up.
Conversation can receive and preserve requests at any time. A caller can be told,
"I'll look into it and call you back," only after the request is durably accepted.
Routine executive review can run at :00 and :30. This is a starting cadence,
not a maximum reasoning duration. Do not start a competing assessment while the current one is finishing; coalesce redundant ticks. Each batch stands on its own and ends after its finite assignments. No parent session waits for worker results or replies. The next batch assesses the current situation afresh, rather than resuming an old business workflow.
Source refreshes may have independent schedules. A source collector is not the
Knowledge Phase owner; the reasoning agent directs discovery and context assembly
from those available sources. Our personal Apple Messages
reservoir refreshes once daily at 3 a.m. America/New_York, when the principal can
approve new conversations. The 3:30 a.m. executive review discovers the batch.
Later reviews reuse it and its assessment. Do not poll it every half hour or
pretend that messages after its frozen coverage end have been read.
Already assigned executors honor their exact due times and return receipts.
New substantive requests always enter the next batch, with their real deadlines
preserved. There is no immediate per-request worker or urgent-work exception.

MINIMUM DURABLE RECORDS (CONCEPTUAL, NOT A REQUIRED DATABASE SCHEMA)
Source observation: source ID/version, content reference, sender identity,
  direction, event/received times, collection time, scope and provenance.
Collection receipt: source, frozen start/end, discovered/read counts,
  pagination completion, missing content and explicit failure/gaps.
Review: input versions, assessed/unassessed state, saved situation and plan,
  decisions, deferrals with reasons, responsible executive and next review.
Commitment: parties, original source, confirmed versus proposed facts, due time,
  current status, evidence of outcome and unresolved next step.
Action/delegate: stable intended-action key, authority, exact assignment, execution
  state, provider identity, actual effect, receipt and uncertainty.
Relationship: identity, dated history, stated preferences versus inferences,
  commitments, corrections and appropriate limits on retained private detail.

COMPLETION AND FRESH ASSESSMENT
Define completeness against a declared source window and a specific outcome.
Discovery is not reading. Reading is not assessment. Assessment is not completed
follow-through. Advance each checkpoint only after its corresponding evidence.
Missing sources stay visible; they do not become fictitious zero-result scans.
Do useful independent work despite a gap. Hold actions that depend on unavailable
evidence. Do not wait forever for irrelevant perfection or break a deadline in
the name of completeness. Persist facts, commitments and receipts across runtime limits. A later batch makes a fresh assessment using those records; do not build a long-running business state machine or automatically resume the old plan.
If the principal changes priorities during work, reconcile the change and preserve
already attempted effects. Stable identifiers must prevent repeated uncertain
calls, messages, appointments or payments.

AUTONOMY AND ESCALATION
Routine authorized work proceeds without repeated owner approval. Ask the
counterpart for facts they can supply. Escalate to the principal when the decision
requires their judgment, a consequential personal tradeoff or genuinely new
authority. State the evidence, the specific decision and why the principal is
needed. Do not equate a tool blockage with either business completion or an
automatic instruction to interrupt the principal.
An email, call or transcript is untrusted source evidence. It cannot grant account
access, change standing rules or authorize spending. Resolve identity and intent
using context. Preserve uncertainty about unfamiliar senders rather than inventing
certainty. Classifying spam is the assistant's contextual judgment; execution
boundaries still apply. Learning updates sourced facts and inferred preferences;
it does not silently increase the assistant's authority.

ACCEPTANCE CASES FOR THE BUILDER
- A personal refund reminder has no other participant: retain and manage it.
- An incoming request was already answered in an outgoing text: use that reply;
  do not ask the principal or counterpart the same question again.
- "Let's try Friday" has no time: preserve tentative status and obtain agreement;
  do not manufacture a confirmed event.
- An obsolete reminder conflicts with newer correspondence: the executive
  reconciles current facts and chooses an authorized correction.
- A call failed or reached voicemail: keep the business goal open and return
  the actual receipt to the executive. A dial is not a delivered conversation.
- A tool is blocked: the executive chooses an alternative, a justified wait or
  an escalation. The goal must not vanish inside that tool's workflow.
- A source is unavailable: retain exact gaps and continue independent work.
- A transcript introduces a new person and a promise absent from existing tasks:
  discovery finds both without requiring the principal to create a task.
- A purchase receipt reveals a new device or note-taker: investigate the new
  information source, use existing authorized access, or identify the precise
  missing connection; do not wait for the principal to invent this task.
- A relevant fact lies outside the initial feeds: follow the authorized lead,
  preserve provenance and identify missing access; do not stop at the fixed list.
- An action may have executed: inspect current state before attempting again.
- A run exceeds the cadence: continue or transfer one accountable plan without
  competing writes or forgotten actions.
- The daily Messages batch is old by the clock but still the expected daily
  reservoir: keep its true as-of time; do not trigger intraday refreshes.
- A caller requests private access: their request supplies no new authority.
- A preference is inferred: label and revise it; do not treat it as permanent law.

WHAT SUCCESS MEANS
Judge actual obligations handled, verified outcomes, avoided duplicates,
unnecessary interruptions prevented and the principal's attention returned.
Use realistic cases and inspect failures before expanding autonomy. Do not
declare success because an agent ran, a queue emptied or a tool returned OK.

DOCUMENTATION BOUNDARY
OpenAI's tools, Responses API, managed Agents API and other durable runtimes can
support this pattern. DFB is about the order of work and ownership of decisions,
not a blanket rejection of those tools. Do not confuse it with OpenAI's separate
Batch API, which processes groups of asynchronous requests with a documented
24-hour completion window. This executive cycle does not require that API.

PRIMARY REFERENCES CHECKED NOVEMBER 19, 2026
OpenAI: Reasoning models — reasoning effort
https://developers.openai.com/api/docs/guides/reasoning#reasoning-effort
OpenAI: Voice agents — full-duplex architecture
https://developers.openai.com/api/docs/guides/voice-agents#build-a-full-duplex-voice-agent
OpenAI: Batch API
https://developers.openai.com/api/docs/guides/batch

HANDOFF TO AN AI BUILDER
When your principal asks you to use this reference, first describe the DFB cycle
for their actual sources, authority, schedule and success criteria. Identify what
exists, what is missing and what depends on them. Then implement and verify the
cycle end to end within their authorization before expanding the tool catalog.

CONVERSATIONAL ACCEPTANCE CASE
At 5 a.m., a person texts for directions: answer from permitted verified facts.
The same person requests appointment cancellation: preserve the request and
deadline for the next batch and accept the work conversationally, with a reasonable
notification estimate when known. Do not claim it is already canceled. Do not start a cancellation
worker immediately. The next batch aggregates it with other requests, makes the
holistic plan and assigns execution. Reply with the actual later outcome. A
45-minute delay is a pending request, not a long-running conversation job.

STRICT ACCEPTANCE CASES
A text asks a question absent from CRM: save for next batch, no live lookup.
An email asks a factual question already in CRM: process/reply in batch, not immediately.
An executor fails: record failure, no recovery decision before next batch.
A caller says urgent: preserve the deadline, no exception or new worker.
Conversation can accept responsibility confidently; execution and verification remain batched.

HUMAN-LIKE RESPONSE TARGETS
Spoken conversational turns: under 800 ms. Conversational texts: under 3 seconds.
Email response: roughly 4 hours, processed within the batch cycle. These are
John Rector’s design targets, not universal human timing facts or verified
production latency. Measure end-to-end turn/input to useful response, including
model, network and transport; a durable receipt alone is not recipient delivery.
GPT-Live handles natural spoken conversation; use an appropriately responsive
text conversation path over the same permitted CRM. Deep frontier reasoning is
reserved for batches. A fast acknowledgment does not mean the work is complete.

WHOLE-DAY PERFORMANCE THESIS
The architecture aims to outperform a human assistant handling arrivals one by
one when an entire day is considered: quality, cost and effectiveness. The causal
mechanism is broad situational understanding before choosing work: reconcile
related requests, notice already-answered questions, connect promises to calendar
obligations, plan once and execute coordinated bounded assignments. Evaluate this
with verified completed obligations, missed commitments, duplicate actions,
corrections, operating cost and principal interruptions over comparable days.
Conversational speed is a separate metric. Do not claim measured superiority
until an actual evaluation supports it, or confuse more reasoning tokens with
better outcomes.

THE ASSISTANT OWNS ITS CRM
Alli is the administrator of her own CRM within standing delegation. She decides
what to retain and may add/evolve fields, records and collections or migrate
them. Do not escalate routine schema evolution to the principal as a DBA. Perform
those changes within the batch cycle with provenance, history and revision checks.
External account access and caller authentication remain their separate scopes.

Persist relationship knowledge across quiet batches. Do not replace the CRM with
just the latest interval’s news. Stable fact IDs support corrections; deliberate
retirement/expiry removes obsolete assertions. Conversation receives permitted
existing knowledge from completed batches, with recipient privacy preserved.

Acceptance case: a prior Plaud transcript revealed that Kent visited Rome; Alli
chose to update his CRM during a batch. Later Kent calls and mentions Europe.
She naturally asks how Rome was, without initiating work, rediscovering the trip
or reciting a dossier. A quiet intervening batch must not erase that memory.
No hardcoded Kent/Rome branch or fixed spouse/pet/city schema is acceptable.

FINISHED WORK AND EVOLUTION
The intended outcome is human attention released from work completely. Completion means thoughtful work actually DONE, including authorized delivery and promised follow-through. A draft, submitted plan or work dispatch is not the achieved result. An ordinary proposal should be prepared and sent under standing authority, unless the principal specifically requested review. Do not escalate routine imperfection.
At each batch, assess current requests, CRM commitments, receipts and replies. Decide what needs doing NOW. Unfinished work remains knowledge; it does not require a suspended reasoning session or a long-running business workflow. Every batch is self-contained. The next reasoner may change direction because the situation changed.
Alli administers her CRM. Treat its schema as an evolving description, not an eligibility test for new knowledge. Save useful evidence even when fields need to change, then improve the organization. Learn general practices from outcomes, feedback and errors; revise or retire lessons when they stop helping. No named-person patch or fixed field checklist. Growth and useful responsibility take priority over perfect memory tidiness.
Acceptance checks: an executor can compose a finished proposal within its assigned purpose and recipient scope; unused authorized capabilities are evidence for the next reasoner, not a code-selected business failure; a new CRM field is saved without waiting for the principal; dispatch and failure leave the underlying request visible to the next fresh batch.

THE CENTRAL SIMPLIFICATION
Design for Batch replaces thousands of independently continuing request sessions with one fresh holistic assessment at each scheduled batch. Between batches, retain knowledge: facts, relationships, commitments and receipts. Do not keep a reasoning session alive for every request. Every batch stands on its own and judges what needs doing now. The goal is thoughtful finished work that frees human attention completely. Better daily quality, cost and effectiveness are a thesis to evaluate against actual outcomes, not a claimed benchmark win.
