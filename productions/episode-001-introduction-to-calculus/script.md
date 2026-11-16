# Episode 1: Introduction to Calculus — Script

**Slug:** `episode-001-introduction-to-calculus`  
**Total estimated duration:** ~6 minutes (360 seconds)

---

## Beat Structure Overview

| Beat # | Duration | Content Focus |
|--------|----------|---------------|
| 1 | 0:00-0:30 | Hook: Speedometer question |
| 2 | 0:30-1:30 | Average vs instantaneous velocity |
| 3 | 1:30-3:00 | The derivative concept introduced |
| 4 | 3:00-4:30 | Formal definition with limit notation |
| 5 | 4:30-5:30 | Notation and units explained |
| 6 | 5:30-6:00 | Summary and preview |

---

## Beat-by-Beat Script

### Beat 1: Hook [0:00-0:30]

[Visual: Close-up of car speedometer needle at 65 mph, then blurring into motion]

**NARRATION:**
Every driver has asked this question while driving: "What does my speedometer actually tell me right now?" Is it an average? A guess? Or something more precise? The answer leads us directly to calculus—and specifically, to derivatives. By the end of this episode, you'll understand exactly what a derivative means in physical terms, not just as symbols on a page.

---

### Beat 2: Average vs Instantaneous Velocity [0:30-1:30]

[Visual: Car traveling between two points marked A and B on a road]

**NARRATION:**
Let's start with something familiar: average velocity. If you drive from point A to point B, covering 60 miles in one hour, your average velocity is 60 miles per hour. Simple division—distance divided by time. But here's the problem: that single number hides everything that happened along the way. Maybe you stopped at a red light for two minutes. Maybe you sped up on the highway. Average velocity smooths over all of it.

[Visual: Speedometer needle fluctuating wildly while car moves between A and B]

**NARRATION:**
What about instantaneous velocity—the speed right now, this exact moment? Your speedometer attempts to answer this question. But how does it do that mathematically? This is where calculus steps in with a powerful idea: we approximate the instant by shrinking time itself.

---

### Beat 3: The Derivative Concept [1:30-3:00]

[Visual: Two points on a position-time graph, getting closer together]

**NARRATION:**
Imagine tracking your car's position over time. At each moment t, you have a position p of t. Now ask: what's the rate of change of position with respect to time? In everyday language, that's velocity. Mathematically, we calculate this by looking at how much position changes divided by how much time passes.

[Visual: Formula appears: (p(t + h) - p(t)) / h]

**NARRATION:**
We write this as the change in position—p of t plus h minus p of t—divided by the change in time, which is just h. This ratio gives us average velocity over a tiny interval of length h. Now here's the key insight: if we shrink h toward zero, this average becomes instantaneous. The derivative of position with respect to time IS velocity.

---

### Beat 4: Formal Definition [3:00-4:30]

[Visual: Limit notation appears elegantly on screen]

**NARRATION:**
We express this precisely using limit notation. The derivative of p at t is defined as the limit, as h approaches zero, of the difference quotient we just saw. In symbols: dp/dt equals the limit as h goes to zero of p of t plus h minus p of t all over h.

[Visual: Each symbol appears sequentially with narration]

**NARRATION:**
Let me unpack this carefully. The numerator measures change in position. The denominator measures change in time. Their ratio is velocity. Taking the limit as h approaches zero means we're asking: "What does this ratio approach when our time interval becomes infinitesimally small?" That limiting value IS the instantaneous rate of change—the derivative.

---

### Beat 5: Notation and Units [4:30-5:30]

[Visual: Leibniz notation highlighted in primary blue color]

**NARRATION:**
You've probably seen this before: dp/dt. This is Leibniz notation, named after the mathematician who formalized calculus in the 1600s. The beauty of this notation is that it reminds you exactly what's happening: d of p over d of t—change in position divided by change in time.

[Visual: Units appear next to formula]

**NARRATION:**
And here's a practical note about units. If position is measured in meters and time in seconds, then dp/dt has units of meters per second. The derivative inherits the "per time" dimension from its denominator. This dimensional consistency is one reason calculus works so well across physics, engineering, economics—any field where quantities change over time.

---

### Beat 6: Summary [5:30-6:00]

[Visual: Return to car on road, now with velocity vector shown]

**NARRATION:**
To recap: the derivative measures instantaneous rate of change. For position versus time, that's velocity. We calculate it by taking a limit of average rates as our time interval shrinks to zero. And we write it elegantly as dp/dt—a notation that's been trusted for over three hundred years.

[Visual: Title card appears]

**NARRATION:**
In the next episode, we'll apply this concept to real functions and compute actual derivatives using rules rather than limits from scratch. Until then—keep asking what things mean, not just memorizing formulas.
