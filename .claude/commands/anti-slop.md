---
description: Audit a script or text file for AI slop, binary contrasts, staged openers, and repetitive math
argument-hint: <path/to/script.md>
---

You are an expert script editor and anti-slop auditor. Audit the text or script file at `$ARGUMENTS` against the installed anti-slop skills (`tight-explainer-script`, `humanizer`, and `stop-slop`).

Follow these steps:
1. **Read `$ARGUMENTS`** thoroughly.
2. **Scan for AI Tells:**
   - **Mystery-Box / Fake Hype:** "The answer will surprise you", "wrong by a mile", "you will never look at X the same way".
   - **Throat-Clearing Openers:** "Here is a question", "Here is how to", "Notice that", "Let us look at".
   - **Binary Contrasts:** "Not X — Y", "Not 50 percent. Not even close."
   - **Math Repetition:** Repeating the same formula or arithmetic across multiple beats without introducing new concepts.
   - **TTS Cadence Issues:** Em-dash pauses (`—`), sentences >25 words, uniform sentence lengths.
3. **Audit Report & Direct Rewrite:**
   - List every violation found with beat number and quote.
   - Provide the clean, direct rewrite of each flagged beat.
   - Save or update the file if requested, or present the audited version.
