# Market Daybook — Brand & Voice (READ THIS FIRST, comply exactly)

This file is the authoritative brand spec for all social content. If anything elsewhere
conflicts with this file, this file wins.

## What we are
- **Market Daybook**: a **free Google Sheet trading journal** (https://marketdaybook.com) — the lead magnet.
- Plus a **Chrome extension**, in **private beta**, public launch ~Aug 2026. NEVER show the extension as
  buyable, installable, or available today. Tease its *benefit* only, on sales days.
- **Goal**: drive traffic to the free journal. On sales days, lead with an extension benefit + soft CTA.
- **Audience**: retail traders who want to be more disciplined and systematic. Process-first, hype-skeptical.

## Voice (non-negotiable)
- **Reader-focused SECOND PERSON.** Every post is about the reader — name THEIR pain point, then show how
  the journal closes the loop: plan → execute → review → better plan.
- **ZERO author self-reference.** Never "I", "we", "my", "our", "I built", "I use". No build-in-public voice.
- **Practical, humble, concrete.** No hype, no clickbait. Banned: "secret", "get rich", profit/return
  promises, PnL or red-arrow gimmicks, guarantees.
- Sample/demo data visible in product screenshots is fine (it shows how the software displays data) — never
  treat it as a profit claim, and don't build copy around specific dollar outcomes.
- **Tagline** (verbatim only, and only if used): "Plan the trade. Record the decision. Review the process."

## Hard guardrails
- No profit/return promises, ever. Beta extension never shown as purchasable/installable.
- Different copy per platform — never an identical cross-post.
- Reddit is never automated.
- **X**: value-only every day EXCEPT Wed/Sun (the link days). No hashtags on X, ever.
- **Instagram**: caption is 3–5 reader-focused sentences ending on ONE genuine question, + 4–5 non-spammy
  hashtags, + one-line alt text. Reference the bio link as "link in bio". Soft CTA wording:
  "Grab the free trade journal template".

## Palette & typography (for any generated visual)
- Graphite `#191B20` (primary background) · Ledger Bone `#F1EDE3` (light background / ink) ·
  Recovery Red `#E34B3E` (accent only).
- Typeface: **Sora** (weight 700 for headlines).
- Dark card (primary) = Graphite bg + Bone text + Red accent rule/mark. Light card (occasional) = Bone bg +
  Graphite text + Red accent.
- `render_card.py` in this repo already encodes all of the above — ALWAYS generate cards with it so palette
  and type are correct by construction.

## Pillars by weekday (America/New_York)
- Mon — Informational (diagnose a pain point)
- Tue — Helpful (actionable tip)
- Wed — Sales (extension benefit + soft CTA; link day)
- Thu — Helpful
- Fri — Informational (the "why" behind the process)
- Sat — Helpful (light / community)
- Sun — Sales-soft (reflection + CTA; link day)

## Angle bank (rotate; do NOT repeat an angle used in the last ~10 days)
- a — journaling feels like a chore and gets skipped
- b — session context rebuilt from memory, so the "why" is lost
- c — the reason for each trade never gets captured
- d — vague vs specific pre-trade plan (trigger / invalidation / size / exit)
- e — revenge / overtrading
- f — rules broken silently
- g — time-of-day / setup patterns stay invisible
- h — spreadsheets fragile / high-friction
- i — planning, execution and review live in disconnected places

Extension benefits (sales days): the side panel keeps the written plan visible DURING execution; record each
trade in-context next to the chart; review feedback that closes the loop. Helpful/Informational days: teach
the behavior and reference the journal softly. Sales days: lead with the extension benefit + CTA.
