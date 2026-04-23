---
name: north-star-metric
description: Define a North Star Metric (NSM) and 3-5 supporting input metrics that form a metrics constellation. Classifies the business game (Attention, Transaction, Productivity), validates the NSM against 7 effectiveness criteria, and produces a polished PDF ready to share with the team. Use when choosing a North Star Metric, setting up a metrics framework, deciding what to measure, or answering "what is our one key metric?" — even if the user doesn't use the phrase "North Star". Also trigger when a founder, PM, or investor wants to align on a single customer-centric KPI, or when someone asks what to optimise for in their product or business.
---

<!-- version: 1.0 | tested-on: claude-sonnet-4-6 -->

## Triggers

Use this skill when the user says: "define our North Star", "what should we measure", "help me choose a key metric", "set up a metrics framework", "what's our one metric that matters", "OMTM", "north star", "metrics constellation", "what do we optimise for", or when a founder, PM, or investor wants to align a team around a single customer-centric KPI.

## Dependencies

- WeasyPrint (Python package — install with `pip install weasyprint --break-system-packages` if not available)
- No external MCPs required

## Instructions

**Mode: Co-Worker**

Two Simon-in-the-loop gates are built into this workflow. Do not skip them.

### Goal

Identify the single best North Star Metric for a given business — validated against seven effectiveness criteria — pair it with 3–5 supporting input metrics, and deliver the full framework as a polished, team-ready PDF.

### Background: Core Concepts

Keep these definitions in mind throughout the workflow. Do not explain them unprompted — they are for your reference only.

**NSM is NOT**: multiple metrics, a revenue or LTV metric, an OKR, or a strategy.

**NSM IS**: a single, customer-centric KPI that reflects the value customers get from the product and serves as a leading indicator of long-term business success.

**The three business games:**
- **Attention** — How much time do customers spend using the product? (e.g. Spotify, YouTube, TikTok)
- **Transaction** — How many transactions occur between customers and the platform? (e.g. Uber, Airbnb, Stripe)
- **Productivity** — How efficiently can someone complete their work or goals? (e.g. Notion, Dropbox, Canva)

**The seven NSM criteria:**
1. Easy to Understand — clear definition everyone in the org comprehends
2. Customer-Centric — reflects value to customers, not just revenue or internal activity
3. Sustainable Value — indicates habits and long-term engagement, not one-off spikes
4. Vision Alignment — represents meaningful progress toward the company mission
5. Quantitative — measurable with clear numeric tracking
6. Actionable — teams can directly influence it through product, marketing, or ops
7. Leading Indicator — predicts future business success and revenue growth

### Process

**Step 1 — Gather business context**

Ask the user for the following. Keep the request concise — one structured ask, not a long form:
- Company or product name
- What the product does and who it serves (primary customer)
- Business model and revenue model
- Company vision or mission (if known)
- Any metrics currently tracked
- The primary value delivered to customers — what does a successful customer experience look like?

> **GATE 1 — Confirm context before proceeding.**
>
> Summarise the business context back to the user in 3–5 bullet points. Ask: "Does this accurately capture your business? Anything to correct or add before I proceed?"
>
> Do not continue until the user explicitly confirms.

**Step 2 — Classify the business game**

Based on confirmed context, determine which of the three games this business plays. If it straddles two, choose the primary one and note the secondary. State your reasoning in one sentence.

**Step 3 — Propose a North Star Metric candidate**

Propose a single candidate NSM. Then validate it against all seven criteria in a concise table:

| Criterion | Met? | Justification |
|---|---|---|
| Easy to Understand | ✓ / ✗ | One sentence |
| ... | | |

If the candidate fails more than one criterion, propose an alternative and explain the trade-off between the two.

> **GATE 2 — NSM candidate review.**
>
> Present the proposed NSM and validation table. Ask: "Does this feel right as your North Star? Would you like to adjust the wording, or explore an alternative?"
>
> If the user selects an alternative or requests changes, re-validate against all seven criteria before proceeding. Do not generate input metrics until the NSM is locked.

**Step 4 — Define the metrics constellation**

Generate 3–5 input metrics that most directly drive the approved NSM. For each metric provide:
- **Name** — short, unambiguous
- **What it measures** — one sentence
- **How it drives the NSM** — the causal link
- **How to move it** — product, marketing, or operational lever

**Step 5 — Produce the PDF**

Generate a polished, team-ready PDF using WeasyPrint and inline HTML/CSS. Apply these design principles:

- White background, generous margins (40px minimum on all sides)
- Primary colour: deep navy `#1B2A4A`; accent: warm amber `#F5A623`
- Font stack: `'Helvetica Neue', Arial, sans-serif`; headings bold, body regular, 16px base size
- NSM displayed as the hero element — large (36px+), centred, with a subtle amber underline or border
- Criteria table: alternating row shading (`#F7F8FA` / white), column headers in navy
- Input metrics: card-style layout, one metric per card, amber left border, light grey card background
- Section headers in navy, 20px, with generous top padding
- Footer: right-aligned, small grey text, date generated

**PDF structure (in order):**
1. **Header** — Company/product name + "North Star Metric Framework" subtitle
2. **Business Game** — Classification badge + one-sentence rationale
3. **North Star Metric** — The metric, hero-sized and prominent, with a concise paragraph rationale
4. **Criteria Validation** — Table of all seven criteria
5. **Metrics Constellation** — The 3–5 input metrics in card layout
6. **Footer** — Date generated

Save the PDF to: `Resources/Output files/[company-name]-north-star-metric_v1.pdf` in the workspace.

If a file with that name already exists, increment to `_v2`, `_v3`, etc. Never overwrite.

## Failure Modes

- If the user cannot describe the business model or primary customer, ask targeted follow-up questions. Do not proceed with guesses or placeholder content.
- If the business plays two games equally, propose a candidate NSM for each and ask the user to choose one before proceeding.
- If WeasyPrint is unavailable, install it first (`pip install weasyprint --break-system-packages`). If installation fails, deliver the output as a structured markdown file and flag the PDF issue.
- If the user rejects two consecutive NSM proposals without providing direction, ask: "What does success look like for a customer in one sentence?" Anchor the third proposal to their answer.
- If the user skips or dismisses a gate, remind them briefly why the checkpoint matters, then proceed if they still want to skip.
