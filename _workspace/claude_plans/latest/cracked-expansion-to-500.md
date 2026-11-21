# Plan: Expand Cracked Series to ~460 Episodes

**Written:** 2026-11-21  
**Status:** Approved — ready to execute batch by batch  
**Target:** ~460 total episodes (currently 58)  
**New episodes needed:** ~402  
**Batch size:** 40 episodes  

---

## Why phased batches?

Each batch runs as a single workflow with 6–8 generator agents. The generators check a **concept registry** (`productions/cracked/concept-registry.md`) before proposing ideas — this is the primary anti-repetition mechanism. Smaller batches (~65 episodes) mean:

- Each batch's curators have a tractable list to dedup against.
- If a batch produces a weak episode, it's caught and dropped before it poisons later work.
- Easy to review and approve incrementally rather than all at once.

---

## Concept registry

**File:** `productions/cracked/concept-registry.md`  
One line per episode: `Ep NNN | <concept slug> | <bucket>`

This file is **created after Batch A and updated after every batch**. Before the first batch runs we do a one-time write that records the 58 existing episodes. Every subsequent batch's generators are handed this file and must refuse to propose a concept already in it.

---

## Thematic buckets (12 total)

Each bucket has a target episode count and a list of concept families to mine. Existing episodes are noted so generators know what to skip.

| # | Bucket | Target | Already used |
|---|--------|--------|-------------|
| 1 | Sequences, Series & Limits | 40 | exp growth ×2, geom series ×2, arith series, harmonic, telescoping, zeta = 8 |
| 2 | Plane & Circle Geometry | 50 | circumference Δr, Koch snowflake, Thales, centroid, Euler V–E+F, parabola, Möbius = 7 |
| 3 | Number Theory & Modular Arithmetic | 40 | units-digit cyclicity, remainder theorem, divisor counting, modular day-of-week = 4 |
| 4 | Probability (classical & conditional) | 50 | birthday, binomial, Bayes, Monty Hall, Simpson's, nontransitive dice, derangements, coupon collector, complementary = 9 |
| 5 | Combinatorics & Counting | 35 | Pascal's triangle/grid paths, counting principle = 2 |
| 6 | Algebra & Functions | 45 | neg×neg, AM–GM, FTA, Euler's number e = 4 |
| 7 | Calculus & Analysis | 40 | derivative as limit, Rolle's theorem = 2 |
| 8 | Physics — Mechanics & Motion | 40 | projectile 45°, pendulum SHM, Doppler, adiabatic compression = 4 |
| 9 | Physics — Waves, Optics & EM | 40 | rainbow, standing waves, diffraction, diamond TIR, destructive interference, Faraday cage, electrostatic induction = 7 |
| 10 | Physics — Thermodynamics & Modern | 30 | fridge paradox, adiabatic pump = 2 |
| 11 | Topology, Infinity & Logic | 20 | hairy ball, Hilbert's Hotel, Möbius strip, Euler V–E+F = 4 |
| 12 | Applied & Cross-disciplinary | 35 | GPS trilateration, complex numbers/AC, Archimedes, Diffie–Hellman = 4 |

**Total target from buckets:** 465 episodes  
**Already covered:** 57 slots  
**New needed:** 408 — spread across 6 batches of ~68 episodes each

---

## Batch sequence

| Batch | Episode range | Primary buckets | Focus |
|-------|---------------|-----------------|-------|
| **A** | 59–98 (~40) | 3 Number Theory, 5 Combinatorics | Numbers and counting |
| **B** | 99–138 (~40) | 6 Algebra & Functions | Algebraic surprises |
| **C** | 139–178 (~40) | 2 Plane & Circle Geometry (first half) | Triangles, circles, classical geometry |
| **D** | 179–218 (~40) | 2 Geometry continued + 3D solids | More geometry, 3D, conics |
| **E** | 219–258 (~40) | 4 Probability extensions | Randomness II |
| **F** | 259–298 (~40) | 11 Topology/Infinity, 1 Series continued | Infinity, topology, more series |
| **G** | 299–338 (~40) | 7 Calculus & Analysis | Derivatives, integrals, limits |
| **H** | 339–378 (~40) | 8 Physics — Mechanics & Motion | Motion, forces, fluids |
| **I** | 379–418 (~40) | 9 Physics — Waves, Optics & EM | Light, sound, electromagnetism |
| **J** | 419–458 (~40) | 10 Thermo/Modern, 12 Applied | Thermo, modern physics, applied math |

---

## Quality bar (applies to every batch)

These rules are passed verbatim to every generator agent:

1. **Counter-intuitive**: the naive answer must be clearly and demonstrably wrong.
2. **CBSE/NCERT aligned**: the concept revealed must appear in the Indian curriculum at the stated class level. No university-only topics.
3. **Manim-renderable**: the visual resolution must be achievable with 2D animation — no photographs, no 3D solids, no illustrations. At least one on-screen numerical worked example.
4. **Title hides the concept**: the concept name must NEVER appear in the title or the opening.
5. **Not too obvious**: the riddle must require genuine thought — not "why is 2+2=4?" level.
6. **Not too obscure**: accessible to a bright Class 6–12 student with standard CBSE preparation. Avoid graduate-level topology, measure theory, or number-theoretic machinery that CBSE doesn't teach.
7. **Fresh**: the concept must not appear in the concept registry.

---

## Per-batch workflow structure

Each batch runs a 3-phase workflow:

```
Phase 1 — Generate (parallel, ~6–8 agent sub-tasks, one per topic cluster)
  Input: concept-registry.md (read from disk), bucket focus, quality rules
  Output: ~60–80 raw candidates

Phase 2 — Curate
  Input: all raw candidates + concept-registry.md
  Dedup: drop any that overlap an existing concept
  Score: 5-dimension scoring (counter-intuitiveness, visuals, curriculum, variety, worked example)
  Keep: top 40 (score ≥ 32/50)

Phase 3 — Write
  Append new rows to productions/cracked/series-curriculum.md
  Update productions/cracked/concept-registry.md
  Update session.md episode count
```

---

## Concept families per batch (generator prompts reference these)

### Batch A — Numbers, Counting, Algebra

**Number Theory (target 20 eps)**  
Prime factorisation patterns, Fermat's little theorem, GCD/LCM surprises, prime gaps, perfect numbers, amicable numbers, Goldbach conjecture (approachable), Wilson's theorem, integer square roots, digital roots, palindromes and divisibility rules, casting out nines, check-digit algorithms (ISBN, Aadhaar), Fibonacci and GCD, number of zeros at end of n!, representation in different bases.

**Combinatorics (target 20 eps)**  
Pigeonhole principle, graph theory handshaking lemma, Königsberg bridge problem, inclusion-exclusion, stars-and-bars, Catalan numbers, derangements (beyond what's covered), counting paths with obstacles, number of triangles from a point set, number of diagonals in a polygon, number of subsets, Ramsey theory (accessible version), four-colour theorem (accessible), chromatic number.

**Algebra & Functions (target 25 eps)**  
Vieta's formulas, AM-GM-HM chain of inequalities, Cauchy-Schwarz (accessible), quadratic discriminant surprises, completing the square visually, floor/ceiling functions, absolute value inequalities, functional equations (f(x+y)=f(x)f(y)), piecewise functions, inverse functions, logarithm laws (surprises), change of base, exponential vs polynomial growth race, e as a natural base.

### Batch B — Geometry

**Plane Geometry (target 20 eps)**  
Angle bisector theorem, inscribed angle theorem extensions, power of a point, radical axis, nine-point circle, Ptolemy's theorem, Simson line, Apollonius circle, pick's theorem, Morley's trisector theorem, Napoleon's theorem, Desargues' theorem (accessible), Stewart's theorem.

**Circle & Conic Geometry (target 15 eps)**  
Tangent-chord angle, alternate segment theorem, cyclic quadrilateral properties (opposite angles sum to 180°), Ptolemy revisited, ellipse reflection property (whisper gallery), hyperbola reflection property, conic sections from cone slices, eccentricity, focus-directrix definition for ellipse.

**3D & Solid Geometry (target 15 eps)**  
Platonic solids and why only 5, volume:surface-area ratio and why cells are small, sphere packing (kissing number problem), cross-sections of a cube, prince Rupert's cube, Cavalieri's principle, volume of a torus, Euler characteristic for other surfaces, net unfolding of solids.

### Batch C — Probability & Topology/Infinity

**Probability — Extensions (target 41 eps)**  
Geometric distribution (expected waiting time), negative binomial, Poisson (rare events), law of large numbers (and when it's misleading), central limit theorem (dice sum approaches bell), regression to the mean, gambler's ruin, random walks, St. Petersburg paradox, Buffon's needle, birthday problem generalisations, coincidence paradoxes, prosecutor's fallacy, false negative/positive tradeoffs, two-envelope paradox, Sleeping Beauty problem (accessible), optimal stopping / secretary problem.

**Topology, Infinity & Logic (target 16 eps)**  
Cantor's diagonal argument (uncountable infinities), different sizes of infinity, the barber paradox / Russell's paradox, Zeno's paradoxes resolved, Gabriel's horn (finite volume, infinite surface), four-colour theorem, Jordan curve theorem, projective plane, Klein bottle, the infinite monkey theorem, supertasks.

### Batch D — Calculus & Series

**Calculus (target 30 eps)**  
MVT (car speedometer), L'Hôpital's rule (0/0 indeterminate forms), related rates (ladder problem, inflating balloon), volumes of revolution, arc length, Newton's method (root finding), implicit differentiation (surprising curves), chain rule visual, optimisation problems with counter-intuitive answers, Taylor series, Stirling's approximation, Euler–Maclaurin formula.

**Series & Limits (remaining ~32 eps)**  
p-series convergence test, ratio test, integral test visually, power series radius of convergence, Fourier series (square wave), alternating series (Leibniz), Abel's theorem, Cesàro summation, Basel problem (π²/6), Stirling's approximation, product formula for π, Wallis product.

### Batch E — Physics I

**Mechanics (target 36 eps)**  
Conservation of momentum (Newton's cradle), angular momentum, gyroscope precession, center of mass surprising cases, torque and mechanical advantage (levers), Kepler's laws (equal areas), gravitational slingshot, terminal velocity, Bernoulli's principle (airplane lift, curve ball), surface tension (why water striders walk), capillary action, friction paradoxes, coefficient of restitution (bouncing ball height), yo-yo mechanics, bicycle stability, coriolis effect.

**Waves, Optics & EM (remaining ~33 eps)**  
Young's double slit, thin-film interference (soap bubble colours), Malus's law (polarisation), magnetic force on a moving charge, Lenz's law (falling magnet in a copper tube), mutual inductance, LC oscillations, skin effect, electromagnetic spectrum surprises, photoelectric effect, blackbody radiation, fluorescence, fiber optics total internal reflection, mirage formation, gravitational lensing (accessible), speed of light measurement history.

### Batch F — Physics II + Applied

**Thermodynamics & Modern Physics (target 28 eps)**  
Carnot efficiency limit, entropy (why ice doesn't unfreeze spontaneously), latent heat (why sweating cools), heat pump efficiency > 100%, thermal expansion surprises, Boyle's law visual, Gay-Lussac's law, specific heat (why sand burns feet, water doesn't), blackbody peak wavelength, photoelectric effect (particle nature of light), de Broglie wavelength, Heisenberg uncertainty principle (accessible), radioactive decay half-life, nuclear binding energy.

**Applied & Cross-disciplinary (target 31 eps)**  
RSA encryption basics, binary and powers of 2, error-correcting codes (Hamming), data compression (Huffman), sorting algorithm complexity, binary search efficiency, map projections (Mercator distortion), great circle routes, compound interest (Rule of 72), present value paradox, game theory (prisoner's dilemma, Nash equilibrium), auction theory, Braess's paradox, epidemic SIR model, the mathematics of voting (Arrow's impossibility), DNA probability, pharmacokinetics (drug half-life), signal-to-noise ratio, information entropy (Shannon).

---

## Execution checklist

- [x] Existing 58 episodes written
- [x] Create concept-registry.md (one-time setup, do before Batch A)
- [x] Batch A (eps 59–98): Number Theory + Combinatorics
- [x] Batch B (eps 99–138): Algebra & Functions
- [x] Batch C (eps 139–178): Geometry I (plane, triangles, circles)
- [x] Batch D (eps 179–218): Geometry II (3D, conics, coordinate)
- [x] Batch E (eps 219–258): Probability extensions
- [x] Batch F (eps 259–298): Topology + Infinity + Series
- [x] Batch G (eps 419–455): Calculus & Analysis (retry, wrote after H/I/J)
- [x] Batch H (eps 299–338): Physics — Mechanics
- [x] Batch I (eps 339–378): Physics — Waves, Optics & EM
- [x] Batch J (eps 379–418): Thermodynamics, Modern Physics, Applied
- [x] Split into 23 part files of 20 episodes each (series name on each file)
- [x] COMPLETE — 455 episodes, 23 part files
