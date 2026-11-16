# Episode 1 Script — Math Reviewer Verification

**Slug:** `episode-001-introduction-to-calculus`  
**Reviewer:** math-reviewer agent  
**Date:** 2026-11-17  
**Status:** ✅ VERIFIED CLEAN

---

## Overview

This document records the adversarial verification of all mathematical claims in the episode script. Every claim tagged with `[MR]` has been re-derived, checked for precision, and confirmed to match standard calculus definitions.

---

## Claim-by-Claim Verification

### Claim 1: "Derivative = limit of average rate of change as interval approaches zero"

**Location:** Beat 3 narration  
**Verification Status:** ✅ CONFIRMED

**Re-derivation:**
Starting from the definition of instantaneous velocity at time t:
- Average velocity over [t, t+h] = (p(t+h) - p(t)) / h
- Instantaneous velocity = lim(h→0) [(p(t+h) - p(t)) / h]
- This limit IS the derivative dp/dt evaluated at t

**Potential issues checked:**
- ✅ No ambiguity about "approaches zero" vs "equals zero" (limit handles this correctly)
- ✅ Direction of approach not specified—standard convention is two-sided limit unless stated otherwise
- ✅ Matches Stewart, Thomas, and Spivak calculus textbooks

---

### Claim 2: "Position function p(t) → velocity v(t) = dp/dt"

**Location:** Beat 3 narration  
**Verification Status:** ✅ CONFIRMED

**Re-derivation:**
By definition, if position is given by a differentiable function p(t), then instantaneous velocity at any time t is:
v(t) = lim(h→0) [p(t+h) - p(t)] / h = dp/dt |ₜ

**Potential issues checked:**
- ✅ Implicit assumption that p is differentiable—reasonable for introductory episode
- ✅ Could add footnote about non-differentiable points (corners, cusps), but not needed here
- ✅ Units consistency: [p]/[t] = meters/second ✓

---

### Claim 3: "Units of derivative are 'units of quantity per unit of time'"

**Location:** Beat 5 narration  
**Verification Status:** ✅ CONFIRMED

**Re-derivation:**
Dimensional analysis:
- dp/dt has dimensions [p]/[t]
- If p is position (L) and t is time (T), then dp/dt has dimensions L/T
- This generalizes: any derivative df/dx has units of f per unit of x

**Potential issues checked:**
- ✅ No confusion with partial derivatives or higher-order derivatives introduced prematurely
- ✅ Clear connection to physical interpretation maintained throughout

---

## Notation Consistency Check

| Symbol | Usage in script | Standard usage | Match? |
|--------|-----------------|----------------|--------|
| dp/dt | Leibniz notation for derivative of position w.r.t. time | Standard | ✓ Yes |
| p(t) | Position as function of time | Standard | ✓ Yes |
| h | Small time interval in difference quotient | Standard | ✓ Yes |
| lim(h→0) | Limit notation | Standard | ✓ Yes |

---

## Edge Cases & Ambiguities (None Found)

The script avoids common pitfalls:
- No premature introduction of power rule or differentiation formulas
- No confusion between average and instantaneous velocity beyond the initial contrast
- No misuse of "infinitesimal" as a standalone quantity—properly framed within limits

---

## Recommendations for Future Episodes

1. **Episode 2:** When introducing product/quotient rules, explicitly state domain restrictions (denominator ≠ 0)
2. **Episode 3:** Chain rule episode should clarify inner vs outer function notation upfront
3. Throughout: Consider adding a glossary appendix defining "limit," "derivative," and "differentiable"

---

## Final Verdict

**Status:** ✅ APPROVED FOR PRODUCTION  
All mathematical claims are precise, standard, and free of ambiguity. The script is ready to proceed to storyboard development (E3-I2).

---

*This document will be archived with the episode artifacts for future reference.*
