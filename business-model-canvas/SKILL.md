---
name: business-model-canvas
description: >
  Builds a complete Business Model Canvas (BMC) with all 9 blocks: Customer Segments, Value Propositions, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partners, and Cost Structure. Use this skill whenever someone wants to map how a business creates, delivers, or captures value — whether for a new venture, an existing company audit, investor materials, or strategic planning. Trigger when the user says "business model canvas", "BMC", "map the business model", "how does [company] make money", "document our business model", "create a canvas for", "walk me through the 9 blocks", or when they share a business idea or company description and want to understand how it works as a system. Also trigger when the user is preparing pitch materials or evaluating a startup's business model logic.
---
<!-- version: 1.0 | tested-on: claude-sonnet-4-6 -->

## Triggers

Use this skill when the user says: "business model canvas", "BMC", "map the business model for [company/idea]", "how does [X] make money", "document our business model", "walk me through the 9 blocks", "create a canvas for [venture]", or when they share a business description and want it structured as a canvas. Also trigger when preparing investor materials or evaluating whether a startup's model is coherent.

## Dependencies

- PDF skill (for final output rendering)
- Web search (optional — only if researching a named public company rather than a user-supplied venture)

## Instructions

**Mode: Co-Worker**

### Goal

Produce a complete, coherent Business Model Canvas for a named business or idea — all 9 blocks populated with specific, grounded content — delivered as a PDF. The canvas should reflect the business as it actually works (or is intended to work), not generic placeholders.

### Process

**Step 1 — Collect the brief**

Ask the user for the following. If they've already provided some of this in their prompt, extract it and only ask for what's missing:

- What business or idea are we mapping? (name, one-line description)
- What do you already know or have decided? (customers, revenue model, key activities, anything concrete)
- What is this canvas for? (internal clarity, investor deck, strategic audit, new venture planning)
- Are there any blocks you want to focus on or challenge?

> **GATE 1 — Input brief confirmed.**
> Summarise your understanding of the business in 2–3 sentences and ask: "Does this capture it correctly before I build the canvas?"
> Do not proceed until the user confirms or corrects.

**Step 2 — Draft all 9 blocks**

Work through the canvas systematically. For each block, produce 3–5 specific, concrete bullet points. Avoid generic filler — every point should be falsifiable (i.e., it could be wrong for a different business).

Use this sequence and logic:

1. **Customer Segments** — Who specifically are we serving? Distinguish between primary and secondary segments if relevant. Avoid "everyone".
2. **Value Propositions** — What problem do we solve or need do we fulfil for each segment? Focus on outcomes, not features.
3. **Channels** — How do customers discover, evaluate, purchase, and receive the value? Map the full journey.
4. **Customer Relationships** — How do we acquire, retain, and grow customers? What does the relationship feel like day-to-day?
5. **Revenue Streams** — How does the business get paid? Be specific about pricing model, frequency, and mechanism.
6. **Key Resources** — What must exist for this model to work? Physical, intellectual, human, financial.
7. **Key Activities** — What does the business actually do every day to deliver the value proposition?
8. **Key Partners** — Who do we rely on that we don't own? Strategic alliances, suppliers, outsourced functions.
9. **Cost Structure** — What are the biggest cost drivers? Fixed vs. variable. Cost-driven or value-driven?

After drafting all 9 blocks, add a brief **"Key Assumptions & Risks"** section (3–5 points). Flag the blocks where the logic is weakest or where an assumption could invalidate the model. Note any known BMC blind spots relevant to this business (e.g., no defensibility signal, no key metrics).

> **GATE 2 — Draft review.**
> Present all 9 blocks plus the Assumptions & Risks section in structured markdown.
> Ask: "Does this reflect how the business actually works? Anything to correct, cut, or sharpen before I produce the PDF?"
> Iterate on any blocks the user flags. Do not produce the PDF until the user explicitly approves.

**Step 3 — Produce the PDF**

Use the PDF skill to render the finalised canvas as a formatted PDF. Structure the document as follows:

- **Cover**: Business name + "Business Model Canvas" + date
- **Canvas layout**: 9 blocks in the standard BMC visual grouping (left/centre/right/bottom), each with its bullet points
- **Key Assumptions & Risks**: separate section at the end

Save to `Resources/Output files/` as `[business-name]_business-model-canvas_v1.pdf`. If a file with that name already exists, increment the version number.

### Output

A formatted PDF with all 9 BMC blocks and a Key Assumptions & Risks section. Saved to `Resources/Output files/`.

## Failure Modes

- If the user provides too little context to populate the canvas meaningfully, ask targeted follow-up questions before drafting — do not fill blocks with generic placeholders.
- If the PDF skill is unavailable, deliver the canvas as a formatted markdown file (.md) instead and note the fallback.
- If the business is a named public company and key facts are unclear, use web search to verify — flag any unverified content with [Unverified].
- If the user wants a Lean Canvas or Startup Canvas instead of a BMC, note the difference briefly and ask which framework they actually want before proceeding.
