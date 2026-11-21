# Episode Scope — cr-01-pond-half-covered

**Title:** When Was the Pond Half-Covered?
**Series:** Cracked — "Every riddle hides a law. Break it open."
**Episode:** 1 of 455
**Class Level:** 8–9
**Subject:** Mathematics
**Target Duration:** 5–7 minutes

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

### Example 2 — Generalization

**Setup A:** A different pond is fully covered in 20 days (same doubling rule). When was it half-covered?

**Solution:**
- By the same logic: fraction(n) = 2^n / 2^20
- 2^(D−1) / 2^D = 1/2 for any D
- D = 20 → half-covered on **Day 19**

**Setup B (extension):** When was the original 30-day pond one-quarter covered?

**Solution:**
- 2^n / 2^30 = 1/4 = 2^28 / 2^30
- n = 28 → **Day 28** (two steps before full coverage)

**General rule:** A pond covered in D days was half-covered on Day D−1, one-quarter covered on Day D−2, and one-eighth covered on Day D−3.

---

## Out-of-Scope (do NOT introduce in this episode)

- Logarithms as a full topic (mentioning "log base 2" is acceptable as a teaser only, not derived or applied)
- Continuous exponential growth (e^x, natural logarithm) — this episode uses integer powers of 2 only
- Compound interest or financial applications of exponential growth
- Differential equations or rate-of-change formalism
- Exact population growth models or biological doubling time calculations

---

## Target Duration

**5–7 minutes** (hard gate: rendered final.mp4 must be in [300s, 420s]; overall channel gate is [240s, 660s]).
