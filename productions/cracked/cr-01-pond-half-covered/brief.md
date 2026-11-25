# Episode Brief — cr-01-pond-half-covered

**Title:** When Was the Pond Half-Covered?
**Series:** Cracked — "Every riddle hides a law. Break it open."
**Slug:** `cr-01-pond-half-covered`
**Class Level:** 8–9 | **Subject:** Mathematics

---

## 1. Learning Objective

Viewers will be able to explain why Day 29 — not Day 15 — is when the pond is exactly half-covered, using the doubling property of exponential growth: because the pond doubles from Day 29 to Day 30, Day 29 is precisely half, regardless of when you thought "half" should arrive.

**Source:** `scope.md` — Learning Objectives 1–4.

---

## 2. Prerequisites

- Comfortable with multiplication and simple fractions (1/2, 1/4, 1/8)
- Understands exponent notation: 2^1 = 2, 2^2 = 4, 2^3 = 8 — no derivation needed, pattern recognition suffices
- No algebra beyond substitution into a formula
- No prior exposure to logarithms or e required

---

## 3. Common Misconceptions to Address

| # | Misconception | Why it happens | How to correct it |
|---|--------------|----------------|-------------------|
| 1 | **Linear intuition:** "The pond is growing slowly, so it must be near the beginning — nowhere close to full." | Humans have strong linear intuition; exponential growth is invisible until it isn't. | Show the split-screen animation side-by-side: linear fills steadily, exponential looks empty until Day 25–26, then engulfs the pond in days. |
| 2 | **Day 15 guess:** Most people divide 30 by 2 and say "halfway through the time = halfway full." | Confusing the time axis (Day 15 of 30) with the coverage axis (50% of pond area). | Directly show the coverage table: on Day 15 the pond is only 2^15 / 2^30 ≈ 0.003% covered — not 50%. This number should land like a punchline. |
| 3 | **Missing the "one step back" trick:** Even after seeing the answer, viewers may not grasp *why* it must always be one day before full. | The backward reasoning (start from the end state) feels unfamiliar. | Explicitly animate Day 30 → reverse → Day 29: show the pond go from 100% to 50% in one backward step. Then generalize: "it doesn't matter if it's 30 days or 20 days — the answer is always one day before the last." |

---

## 4. Key Math Claims (for Math Reviewer)

All of the following must be verified before the script is locked:

1. The fraction of the pond covered on Day n is 2^n / 2^30, where Day 30 is full coverage. [MR]
2. 2^29 / 2^30 = 1/2, therefore the pond is exactly half-covered on Day 29. [MR]
3. For any pond fully covered on Day D, it was half-covered on Day D−1. [MR]
4. 2^28 / 2^30 = 1/4, therefore the pond was one-quarter covered on Day 28. [MR]
5. On Day 15: 2^15 / 2^30 = 1/2^15 ≈ 0.00003 (approximately 0.003%), not 50%. [MR]

---

## 5. Visual Metaphors

The following visual concepts must appear in the storyboard. The Storyboardist must specify a `concrete_visual` ↔ `abstract_symbol` pair for each:

**a) Split-screen: linear vs. exponential fill**
- Left panel: pond fills by equal slices each day (linear). Looks like a progress bar.
- Right panel: pond is nearly empty until Day 25–26, then fills explosively.
- Both panels share a "day counter" that ticks forward simultaneously.
- This is the hook's visual backbone: show the panels before naming the concept.

**b) Coverage table: 2^n for n = 25 to 30**
- A table with columns: Day | Coverage fraction | % of pond
- Day 29 row highlighted in orange (#F97316): "50.0%"
- Day 30 row: "100%"
- Day 15 row (inset or callout): "0.003%" — the punchline against the Day 15 guess

**c) "One step back" reversal animation**
- Start: pond fully covered (Day 30 label visible)
- Animate backward: pond instantly halves (Day 29 label appears, 50% overlay)
- Narration: "Whatever the last day is, the day before it is always exactly half."
- Then generalize: show a 20-day pond doing the same thing → Day 19 = half.

**d) Concrete ↔ abstract pairing at first formula introduction**
- Left: animated lily pad (polygon growing on water surface)
- Right, appearing simultaneously: `fraction(n) = 2^n / 2^30` in orange
- Never show the formula on a blank background.

---

## 6. Hook

**Type:** Real-world scenario (character-grounded — see channel bible House Style)

**Character:** An unnamed scientist / ecologist — establish them once at the top, then follow them. No name needed. "She" or "he" works; keep it consistent.

**Opening sequence (beats, not lines yet):**
- Day 1: scientist walks past the pond on the way to the lab. One lily pad. Barely registers.
- Day 7: a small cluster near the bank. Still looks like nothing.
- Day 15: water is still mostly clear. She keeps walking.
- Day 25: scattered patches across the surface.
- Day 30: she stops at the bank and stares. The entire pond is gone under green pads. Not a square foot of open water remains.
- The riddle emerges from her observation: if the pond is completely full today, on which day was it half-covered?

**The riddle emerges from her experience**, not from a voice announcing "here is a question." The question the viewer asks themselves — "when was it half-covered?" — IS the hook. The narrator frames it naturally through her walk.

**What the hook must NOT do:**
- Do not open with "Here is a question" or any equivalent
- Do not spoil Day 29 in the hook sequence
- Do not define exponential growth in the hook
- Do not use an abstract hypothetical ("imagine a lily pad") — the character IS the grounding

---

## 7. Target Length

**3–3.5 minutes** (from `scope.md`, within channel gate [120s, 660s]). Pacing arc:

| Segment | Target |
|---------|--------|
| Hook | 30–40 s |
| Motivation (linear intuition vs exponential reality) | 30–35 s |
| Build-up (linear vs. exponential, formula, one-step-back) | 60–80 s |
| Result statement | 20–25 s |
| Worked example (bacteria doubling in petri dish) | 40–50 s |
| Recap & payoff | 20–30 s |

---

## 8. Handoff Notes

- **Screenwriter:** 
  - **Hook:** follow the scientist character past the pond — she sees a full pond on Day 30 and asks when it was half-covered. Never spoil Day 29 in the hook.
  - **Worked example:** DO NOT use "a 20-day pond." Use a different real-world context in a different physical domain. **Suggested: bacteria in a petri dish.** Back in her lab, the scientist cultures bacteria that double every hour. At noon the dish is completely full. When was it half full? Applying the one-step-back rule, it was 11:00 AM.
  - Tag every math claim with [MR].
  - **Target word count: ~450–550 words** (natural 3–3.5 min runtime; do not pad to hit an arbitrary floor).
  - Apply all anti-pattern rules from the channel bible (banned openers, varied sentence rhythm, no em-dashes).

- **Math Reviewer:** verify all five claims in Section 4 by re-derivation. For the worked example, additionally verify: bacteria doubling every hour, dish full at noon — half full at 11am. [MR]

- **Storyboardist:** both split-screen panels (Section 5a) must appear in the hook shot. The coverage table (Section 5b) must appear during the build-up. The "one step back" animation (Section 5c) must appear in the main concept section. The worked example shows the scientist in her lab with the petri dish — same visual metaphor (a container going from empty to full) but new context. Director must confirm the character design is consistent across the hook and worked example shots.
