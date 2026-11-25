# Episode Scope — cr-01-pond-half-covered

**Title:** When Was the Pond Half-Covered?
**Series:** Cracked — "Every riddle hides a law. Break it open."
**Episode:** 1 of 455
**Class Level:** 8–9
**Subject:** Mathematics
**Target Duration:** 3–3.5 minutes (channel gate: [120s, 660s])

---

## Learning Objectives

By the end of this episode, viewers must be able to:

1. **Define exponential growth** in terms of repeated doubling: a quantity that multiplies by a fixed factor each step, rather than adding a fixed amount.
2. **Explain why Day 29 — not Day 15 — is when the pond is exactly half-covered**, using the doubling property: since the pond doubles from Day 29 to Day 30, Day 29 must be exactly half of Day 30.
3. **Distinguish linear growth from exponential growth**: linear adds the same amount each step; exponential multiplies by the same factor each step. The visual signature of exponential growth is "nearly nothing, then everything."
4. **Apply "one step back" reasoning** to any doubling scenario: if you know the final state, the state one step earlier is always exactly half, regardless of the total number of steps.
5. **Calculate the coverage fraction on any day** using the formula: fraction on Day n = 2^n / 2^D, where D is the day of full coverage.

---

## Analogy → Concept Mapping

| Concrete Analogy | Abstract Concept |
|-----------------|-----------------|
| Lily pad area doubling every day | Exponential function: fraction covered on Day n = 2^n / 2^30 |
| Left-panel animation: pond fills by equal slices each day | Linear (arithmetic) sequence: each term adds a constant |
| Right-panel animation: pond nearly empty until Day 25, then explodes | Exponential sequence: each term multiplies by a constant (here, 2) |
| "One step back" reveal: Day 30 fully covered → Day 29 is half | Inverse reasoning from known end state; 2^29 / 2^30 = 1/2 |
| Table of 2^n values for n = 25 to 30, Day 29 row highlighted | The formula made concrete: plug in n = 29, see the 50% result |

---

## Worked Examples

### Example 1 — The Original Riddle (the Day 29 answer)

**Setup:** A lily pad doubles in area every day. On Day 30, it covers the entire pond. On which day did it cover exactly half?

**Solution (step by step):**

1. Normalize: let the pond area = 1.
2. On Day 30 the fraction covered = 1 (full coverage).
3. Because the pad **doubles** each day, the fraction on Day n is:
   - fraction(n) = 2^n / 2^30
4. Set fraction(n) = 1/2 and solve:
   - 2^n / 2^30 = 1/2
   - 2^n / 2^30 = 2^29 / 2^30
   - n = 29
5. **Answer: Day 29.**

**Key intuition (the "one step back" principle):** The lily pad doubled from Day 29 to Day 30. If Day 30 is 100%, then Day 29 must be exactly 50% — by definition of doubling. No algebra needed once you see this.

---

### Example 2 — Transfer to a Different Domain (bacteria in a petri dish)

**Setup:** The same scientist, back in her lab, is culturing bacteria on a glass petri dish. The bacteria double in number every hour. At noon the dish is completely full. When was it exactly half full?

**Solution (step by step):**

1. Her instinct says 6 am: if growth started at midnight and the dish is full at noon, "halfway through the morning" feels like halfway full.
2. That is the same linear mistake as guessing Day 15 for the pond. It divides the time, not the amount.
3. The bacteria doubled in the last hour before noon: from 11 am to noon.
4. If noon (the end state) is 100% full, then one doubling step earlier — 11 am — must be exactly half: 50%. [MR]
5. **Answer: 11 am.** One step back from the end.

**Why this example works:** It is a different physical domain (microbiology, not botany), a different time unit (hours, not days), and a different container (petri dish, not pond). The method transfers unchanged: whenever something doubles each step, the state one step before the end is always exactly half. This is the "so now she sees it everywhere" payoff moment of the episode.

---

## Out-of-Scope (do NOT introduce in this episode)

- Logarithms as a full topic (mentioning "log base 2" is acceptable as a teaser only, not derived or applied)
- Continuous exponential growth (e^x, natural logarithm) — this episode uses integer powers of 2 only
- Compound interest or financial applications of exponential growth
- Differential equations or rate-of-change formalism
- Exact population growth models or biological doubling time calculations

---

## Target Duration

**3–3.5 minutes** (target runtime ~210s; hard channel gate is [120s, 660s]).
