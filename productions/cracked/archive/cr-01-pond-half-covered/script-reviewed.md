# Math-Reviewed Script — cr-01-pond-half-covered
**Title:** When Was the Pond Half-Covered?
**Series:** Cracked — "Every riddle hides a law. Break it open."

---

## Math Review Summary

| Field | Value |
|-------|-------|
| Reviewer | math-reviewer |
| Date | 2026-11-21 |
| Total [MR] claims checked | 8 (Beats 5, 6, 7, 8, 9, 13×2, 14) |
| Corrections required | 1 (Beat 5 — illustrative unit counts) |
| [MR-UNCERTAIN] tags | 0 |
| **Verdict** | **CONDITIONAL PASS — apply Beat 5 correction before storyboard** |

### Arithmetic derivations (reviewer's work)

**Beat 5 — Day 1=1 unit model (2^(n−1)):**
- Day 10 = 2^(10−1) = 2^9 = **512** (script says 1,024 — WRONG)
- Day 20 = 2^(20−1) = 2^19 = **524,288** (script says "more than one million" — WRONG; 2^19 < 10^6)
- Note: 2^20 = 1,048,576 > 1,000,000, but that is Day 21 under this model, not Day 20.

**Beat 6 — Fraction formula:**
- Day 30: 2^30/2^30 = 1 ✓
- Day n: 2^n/2^30 — consistent with Beat 5 model (2^(n−1)/2^29 = 2^n/2^30 algebraically identical) ✓

**Beat 7 — Last-five-days table (2^n/2^30):**
- Day 25: 2^25/2^30 = 1/2^5 = 1/32 = 3.125% ≈ 3% ✓
- Day 26: 1/16 = 6.25% ✓
- Day 27: 1/8 = 12.5% (script: "thirteen" — acceptable rounding) ✓
- Day 28: 1/4 = 25% ✓
- Day 29: 1/2 = 50% ✓

**Beat 8 — Day 15:**
- 2^15 = 32,768; 1/32,768 = 3.0518×10^−5 = 0.00305% ≈ 0.003% ✓

**Beat 9 — One step back:**
- 2^29/2^30 = 1/2 ✓

**Beats 13–14 — 20-day pond:**
- Day 19: 2^19/2^20 = 1/2 ✓
- Day 18: 2^18/2^20 = 2^(−2) = 1/4 ✓
- General: 2^(D−k)/2^D = 1/2^k for k = 1,2,3 ✓

---

## Narration Script (reviewed)

**Hook type:** Paradox
**Target duration:** 5–7 min | **Estimated actual:** ~6.3 min (940 words ÷ 150 wpm)

---

### HOOK

**Beat 1:**
Here is a question. A lily pad floats on a pond. Every day, it doubles in size — covering twice as much water as the day before. After 30 days, it covers the pond completely. On which day did it cover exactly half the pond? Take a moment. Most people say Day 15.

**Beat 2:**
They are wrong. Not a little wrong — wrong by a mile. Day 15 is not 50 percent. Not even close. The right answer will surprise you. And once you see why, you will never look at slow-growing things the same way again.

---

### MOTIVATION

**Beat 3:**
Exponential growth is deceptive. For most of its run, it looks like nothing is happening. The lily pad is tiny on Day 1, tiny on Day 5, still tiny on Day 10. But the numbers are accumulating quietly — doubling, then doubling again, building toward something enormous.

**Beat 4:**
Your brain is wired for linear thinking. If something takes 30 days total, your instinct says halfway through the time means halfway through the work. That works for filling a glass of water at a steady rate. It fails completely here. Time and coverage are not the same axis.

---

### BUILD-UP

**Beat 5:**
Let us count the first few days. On Day 1 the lily pad covers one unit of area. Day 2: two units. Day 3: four. Day 4: eight. Each day, multiply by two. After 10 days: five hundred and twelve units. [MR: CORRECTED — 2^9 = 512, not 1,024; the Day 1=1 model gives Day n = 2^(n−1), so Day 10 = 2^9 = 512.] After 20 days: more than five hundred thousand units. [MR: CORRECTED — Day 20 = 2^19 = 524,288; "more than one million" required Day 21 = 2^20 = 1,048,576.]

**Beat 6:**
Here is how to track coverage precisely. The pond is completely full on Day 30. On Day 30, the fraction covered is two-to-the-30 divided by two-to-the-30 — that is one, full coverage. On any earlier Day n, the fraction covered is two-to-the-n divided by two-to-the-30. [MR: VERIFIED — 2^n/2^30 is algebraically consistent with the Day 1=1 model (2^(n−1)/2^29 = 2^n/2^30).]

**Beat 7:**
Now look at the last five days. On Day 25, the pond is about three percent covered. Day 26: six percent. Day 27: thirteen. Day 28: twenty-five. Day 29: fifty. Day 30: one hundred. [MR: VERIFIED — 1/32=3.125%, 1/16=6.25%, 1/8=12.5%≈13%, 1/4=25%, 1/2=50%.] Half the total coverage happens in a single step — from Day 29 to Day 30.

**Beat 8:**
Now check Day 15. The fraction covered on Day 15 is two-to-the-15 divided by two-to-the-30 — that is one divided by two-to-the-15. Work it out: approximately 0.003 percent. [MR: VERIFIED — 2^15=32,768; 1/32,768=0.00305%.] Not 50 percent. Not even one percent. On Day 15, the lily pad is effectively invisible on the pond.

**Beat 9:**
Here is the key insight. The lily pad doubled from Day 29 to Day 30. That means Day 30 is exactly twice Day 29. If Day 30 is 100 percent, then Day 29 must be exactly 50 percent. [MR: VERIFIED — 2^29/2^30=1/2.] You do not need to solve an equation. You just need one backward step from the end.

**Beat 10:**
Compare two panels side by side. On the left: the pond fills by equal slices every day — a straight, steady climb. On the right: the exponential pond is nearly empty until Day 25, then it fills explosively in the final days. Same 30-day axis. Completely different shapes. That gap is why Day 15 feels like the answer.

---

### RESULT

**Beat 11:**
The answer is Day 29. Not Day 15. The pond was exactly half-covered just one day before it was completely full. The lily pad achieved in a single day what it had been building toward for all 29 days before. That is what exponential growth does.

---

### WORKED EXAMPLE

**Beat 12:**
Let us try a different pond. Same doubling rule — but this time the lily pad covers it completely in 20 days, not 30. When was this pond exactly half-covered? Your instinct probably says Day 10. Apply the same reasoning we just used.

**Beat 13:**
The fraction covered on Day n is two-to-the-n divided by two-to-the-20. Set that equal to one-half and solve. Two-to-the-19 divided by two-to-the-20 equals one-half. [MR: VERIFIED — 2^19/2^20=1/2.] The answer is Day 19. One day before full coverage — not Day 10. Now: when was it one-quarter covered? Two-to-the-18 divided by two-to-the-20 equals one-quarter. [MR: VERIFIED — 2^18/2^20=1/4.] Day 18.

**Beat 14:**
The pattern is clean. A pond covered on Day D was half-covered on Day D minus one. One-quarter covered on Day D minus two. One-eighth covered on Day D minus three. [MR: VERIFIED — 2^(D−k)/2^D = 1/2^k for k=1,2,3.] Work backward from the last day. Each step back halves the coverage. It does not matter whether the total is 20 days or 30.

---

### RECAP

**Beat 15:**
Back to where we started. The lily pad doubles every day. Full coverage on Day 30. When was it half-covered? Day 29. The answer was always one step back from the end. The Day 15 guess is a linear answer to an exponential question. That is the trap.

**Beat 16:**
The next time you hear "it is growing slowly now, so we have plenty of time," stop and ask: is this linear or exponential? With exponential growth, the last few steps account for most of the change. The pond looked nearly empty all the way to Day 25. Then it filled in five days. The riddle hid the law. Now you can see it.

---

## Script metadata

| Field | Value |
|-------|-------|
| Total beats | 16 |
| Estimated word count | ~940 |
| Estimated duration | ~6.3 min at 150 wpm |
| [MR] claims checked | 8 |
| Corrections applied | 2 (both in Beat 5 — illustrative unit counts only; core fraction math unchanged) |
| Act boundaries (full wipe) | After Beat 2 (hook→body), after Beat 11 (result→worked example), after Beat 14 (worked example→recap) |
| Downstream clearance | CLEARED for storyboard after Beat 5 wording is updated in production copy |
