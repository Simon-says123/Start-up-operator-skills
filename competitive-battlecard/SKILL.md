---
name: competitive-battlecard
description: Build a sales-ready competitive battlecard comparing your product against a specific competitor — positioning, feature comparison, objection handling, and win/loss patterns. Use when preparing for a competitive deal, briefing a sales team, or responding to "why not [competitor]?" questions. Also trigger when a user shares win/loss notes, a competitor's pricing page, or asks how to counter a specific rival.
---

<!-- version: 1.0 | tested-on: claude-sonnet-4-6 -->
<!-- note: name field uses noun form per owner's explicit override of gerund standard -->

## Triggers

Use this skill when the user says: "create a battlecard for [competitor]", "build me a competitive battlecard", "how do we stack up against [competitor]", "I need to prep for a deal where [competitor] is in the mix", "what's our counter to [competitor]", "help me handle objections about [competitor]", or when they upload win/loss notes, a competitor's pricing page, or a feature comparison and want a structured output.

## Dependencies

- Web search tool
- PDF skill (for final output)
- Optional: user-supplied materials (win/loss notes, feature lists, pricing docs, sales call transcripts)
- Optional: `references/company-context.md` — your product's positioning, features, and pricing. If present, Claude loads it automatically and skips asking.

## Instructions

**Mode: Co-Worker**

### Goal

Produce a single-page, scannable battlecard a sales rep can reference during a live call. Output covers: competitor overview, feature comparison, where you win, where they win, objection responses, landmines to plant, and win/loss patterns.

### Process

**Step 1 — Intake**

Collect the following from the user:

1. **Your product/company** — what you sell, who you sell to, your pricing model, and 2–3 core differentiators. Skip if `references/company-context.md` exists — load it instead.
2. **The competitor** — name and URL (if known).
3. **Any materials to incorporate** — win/loss notes, feature lists, pricing sheets, sales call transcripts. Ask the user to upload if relevant.
4. **Context** — preparing for a specific deal, a general sales brief, or internal training? This determines tone and depth.

> **GATE 1 — Intake confirmation.**
> Summarise what you've collected: "I'll build a battlecard for [Your Product] vs [Competitor] using [materials listed]. Sound right?"
> Wait for confirmation before proceeding.

**Step 2 — Research**

Using web search, investigate the competitor:

- Current product offerings and feature set
- Pricing tiers and model
- Target market and ICP
- Recent product launches or announcements
- Customer reviews and sentiment (G2, Capterra, Reddit, Trustpilot)
- Funding, headcount, and growth signals if relevant

User-supplied materials take precedence over web findings wherever they conflict.

**Step 3 — Draft the battlecard**

Produce a draft with these sections in order:

1. **Company Snapshot** — Founded, HQ, funding/revenue, target market, one-sentence positioning.
2. **Quick Comparison** — Table: Capability | Us | Them | Edge. Cover 5–8 feature areas plus pricing and support.
3. **Where We Win** — 3–5 advantages, each with a proof point or specific capability statement.
4. **Where They Win** — 2–3 honest competitor strengths, each with a counter-positioning response.
5. **Objection Responses** — Table: Prospect Says | Respond With. Cover 3–5 common objections.
6. **Landmines to Plant** — 3–5 questions to ask the prospect that surface competitor weaknesses naturally.
7. **Win/Loss Patterns** — When you tend to win, when you tend to lose, and what tips the scale.

Keep every section scannable — short bullets, bold key phrases, tables where possible.

> **GATE 2 — Review before finalising.**
> Present the full draft in-chat. Ask: "Does this look accurate? Any sections to adjust before I save the final PDF?"
> Iterate until approved, then proceed to Step 4.

**Step 4 — Save output**

Use the PDF skill to produce a formatted PDF. Save to `Resources/Output files/` as `[competitor-name]-battlecard_v1.pdf`. Increment the version number if a file with that name already exists.

## Failure Modes

- If the user cannot identify their own product's differentiators and no `references/company-context.md` exists, stop and ask before researching — the "Us" column cannot be populated without this.
- If web search returns no usable information on the competitor, notify the user and ask whether to proceed with user-supplied materials only or abort.
- If the PDF skill is unavailable, save the battlecard as a markdown file to `Resources/Output files/` and notify the user.
- If user-supplied materials conflict with web findings, flag the conflict explicitly and ask which source to prioritise before drafting.
