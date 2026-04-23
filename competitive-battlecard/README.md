# competitive-battlecard

## What it does
Builds a sales-ready competitive battlecard comparing your product against a specific competitor, covering feature comparison, objection handling, and win/loss patterns. Best used when preparing for a competitive deal or briefing a sales team.

## Reference files
- `references/company-context.md` — your product's positioning, features, and pricing (optional; if present, Claude loads it automatically and skips asking)

## Install
Copy this folder into your skills directory, then toggle the skill on in **Customize > Skills**.

## What to change
- `references/company-context.md` — create this file with your product's positioning, differentiators, and pricing so the skill skips the intake question on repeat use. Not required for first run.

## Usage
**Trigger:** "Create a battlecard for [competitor]"
**Output:** PDF battlecard saved to your output folder as `[competitor-name]-battlecard_v1.pdf`

## Model tested on
claude-sonnet-4-6
