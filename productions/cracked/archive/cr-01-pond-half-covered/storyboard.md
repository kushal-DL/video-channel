# Storyboard — cr-01-pond-half-covered
**Title:** When Was the Pond Half-Covered?
**Series:** Cracked | **Episode:** 1 | **Total shots:** 12 | **Estimated duration:** ~6.3 min

---

## Act structure

| Act | Beats | Shots | Transition out |
|-----|-------|-------|----------------|
| Hook | 1–2 | 1 | Full wipe |
| Motivation | 3–4 | 2 | Fade |
| Build-up | 5–10 | 3–8 | — |
| Result | 11 | 9 | Full wipe |
| Worked example | 12–14 | 10–11 | Full wipe |
| Recap | 15–16 | 12 | Fade to end |

---

## Shot 1: The Day 15 Trap

**Beats covered:** 1–2
**Estimated duration:** ~40 s

**Narration lines:**
> Beat 1: Here is a question. A lily pad floats on a pond. Every day, it doubles in size — covering twice as much water as the day before. After 30 days, it covers the pond completely. On which day did it cover exactly half the pond? Take a moment. Most people say Day 15.
>
> Beat 2: They are wrong. Not a little wrong — wrong by a mile. Day 15 is not 50 percent. Not even close. The right answer will surprise you. And once you see why, you will never look at slow-growing things the same way again.

**Visual content:** Dark-slate background (`#0F172A`). A circular pond (blue `#3B82F6` outline, no fill) appears centered. A small green hexagon (lily pad, cream `#F2E3C6`) sits at the center. The question text — "On which day was it exactly half-covered?" — appears in cream below the pond. A "Day 15?" label appears briefly as a callout (orange `#F97316`), then a large `✗` strikes through it.

**concrete_visual:** A circular pond with a tiny lily pad at center — the riddle's real object.

**abstract_symbol:** None in this shot — the hook poses the question without naming the concept.

**reveal_animation:**
- `Create` for the pond circle (geometry — blue)
- `FadeIn` for the lily pad polygon (background element, not math)
- `Write` for the question text overlay (text — cream)
- `Write` for "Day 15?" callout (orange), then `FadeOut` with `✗`

**hold_content:** Pond with tiny lily pad; question text "On which day was it exactly half-covered?" visible throughout Beat 1. "Day 15?" callout and strike-through visible through Beat 2.

**in_state:** Series title card "Cracked — Every riddle hides a law. Break it open." fades in then out before pond appears.

**out_state:** Pond + strike-through visible. `FadeOut` everything → **full wipe** (act boundary: hook → body).

**transition:** Full wipe

---

## Shot 2: Exponential Growth Is Deceptive

**Beats covered:** 3–4
**Estimated duration:** ~40 s

**Narration lines:**
> Beat 3: Exponential growth is deceptive. For most of its run, it looks like nothing is happening. The lily pad is tiny on Day 1, tiny on Day 5, still tiny on Day 10. But the numbers are accumulating quietly — doubling, then doubling again, building toward something enormous.
>
> Beat 4: Your brain is wired for linear thinking. If something takes 30 days total, your instinct says halfway through the time means halfway through the work. That works for filling a glass of water at a steady rate. It fails completely here. Time and coverage are not the same axis.

**Visual content:** Left side: a tall vertical rectangle (blue outline) representing a glass of water. A cream fill bar rises linearly — steady, equal increments, labeled "linear." Right side: same-shaped rectangle stays nearly empty until the last few increments, then fills explosively — labeled "exponential." Both rectangles share a horizontal "Day" axis ticking 1–10 underneath. Labels "linear" and "exponential" in cream at top of each.

**concrete_visual:** Two side-by-side fill bars — a glass of water filling at a steady rate (left) vs. a nearly-empty glass that fills explosively (right).

**abstract_symbol:** "linear" and "exponential" text labels in cream — no formula yet.

**reveal_animation:**
- `Create` for both rectangle outlines (geometry — blue)
- `Create` for the day-axis ticks
- Fill bars animate simultaneously via `ValueTracker` (linear on left, 2^n proportional on right)

**hold_content:** Both rectangles with their fill bars and labels visible throughout both beats.

**in_state:** Clean (after full wipe from Shot 1).

**out_state:** Both bars filled to Day 10. Labels "linear" and "exponential" persist. Camera zooms into the right (exponential) bar.

**transition:** Zoom into the exponential bar → zoom out to Shot 3

---

## Shot 3: Counting the Doublings

**Beats covered:** 5
**Estimated duration:** ~25 s

**Narration lines:**
> Beat 5: Let us count the first few days. On Day 1 the lily pad covers one unit of area. Day 2: two units. Day 3: four. Day 4: eight. Each day, multiply by two. After 10 days: five hundred and twelve units. After 20 days: more than five hundred thousand units.

**Visual content:** A horizontal sequence of lily pad icons (cream hexagons, increasing in size) labeled Day 1, Day 2, Day 3, Day 4. Each icon appears one beat after the previous. Below each icon: its area in orange (`1`, `2`, `4`, `8`). A "×2" arrow (blue) connects each pair. After Day 4, an ellipsis (`…`) with "Day 10: 512" and "Day 20: 524,288" appearing in orange to the right.

**concrete_visual:** A row of growing lily pad icons with area labels — the doubling made visible as physical growth.

**abstract_symbol:** `a_n = 2^{n-1}` written in orange below the sequence, appearing after the Day 4 icon lands.

**reveal_animation:**
- `FadeIn` for each lily pad icon (background element)
- `Write` for each area label (math — orange)
- `Create` for each `×2` arrow (geometry — blue)
- `Write` for `a_n = 2^{n-1}` formula
- `Write` for "Day 10: 512" and "Day 20: 524,288"

**hold_content:** Full row of icons with area labels and arrows; formula `a_n = 2^{n-1}` visible throughout.

**in_state:** Clean (zoomed out from exponential bar in Shot 2).

**out_state:** Icon sequence + formula `a_n = 2^{n-1}` on screen. Camera slides right to introduce the fraction formula.

**transition:** Slide (right)

---

## Shot 4: The Coverage Formula

**Beats covered:** 6
**Estimated duration:** ~25 s

**Narration lines:**
> Beat 6: Here is how to track coverage precisely. The pond is completely full on Day 30. On Day 30, the fraction covered is two-to-the-30 divided by two-to-the-30 — that is one, full coverage. On any earlier Day n, the fraction covered is two-to-the-n divided by two-to-the-30.

**Visual content:** Left side: a circular pond (blue outline, cream fill growing from center) with a "Day n" label. Right side, appearing **simultaneously** with the pond: the formula `\text{fraction}(n) = \frac{2^n}{2^{30}}` in orange. Below the formula: "Day 30: `\frac{2^{30}}{2^{30}} = 1` (full)" in cream with orange fractions. The pond animates to full coverage as "Day 30" is stated, then animates back to partial as "Day n" is highlighted.

**concrete_visual:** Circular pond with animated fill level (lily pad coverage) keyed to Day n.

**abstract_symbol:** `\text{fraction}(n) = \dfrac{2^n}{2^{30}}` in orange — shown on screen simultaneously with the pond animation, not after.

**reveal_animation:**
- `Create` for the pond circle
- `Write` for the fraction formula (simultaneously with pond creation)
- `Transform` to animate Day 30 fully filled → partial (using `ValueTracker` on fill fraction)

**hold_content:** Pond with current coverage level + fraction formula visible throughout the beat.

**in_state:** Icon sequence from Shot 3 slides off left; pond + formula slide in from right.

**out_state:** Pond at partial coverage; formula `fraction(n) = 2^n / 2^{30}` persistent. Formula stays in top-right corner for Shot 5.

**transition:** Zoom (into the table area, formula shrinks to corner)

---

## Shot 5: Last-Five-Days Table

**Beats covered:** 7
**Estimated duration:** ~30 s

**Narration lines:**
> Beat 7: Now look at the last five days. On Day 25, the pond is about three percent covered. Day 26: six percent. Day 27: thirteen. Day 28: twenty-five. Day 29: fifty. Day 30: one hundred. Half the total coverage happens in a single step — from Day 29 to Day 30.

**Visual content:** A table with three columns — **Day | Fraction | %** — appears centered. Rows build one by one, each row appearing as the narration reaches that day. All fraction and % values in orange. The Day 29 row (`2^29/2^30` | `1/2` | `50%`) is highlighted with orange background and cream text — it arrives with slightly more pause before it appears. Final row (Day 30: 100%) appears last. Formula `fraction(n) = 2^n / 2^{30}` persists in top-right corner (from Shot 4).

| Day | Fraction | % |
|-----|----------|---|
| 25 | `2^25/2^30` = 1/32 | 3% |
| 26 | `2^26/2^30` = 1/16 | 6% |
| 27 | `2^27/2^30` = 1/8 | 13% |
| 28 | `2^28/2^30` = 1/4 | 25% |
| **29** | **`2^29/2^30` = 1/2** | **50%** |
| 30 | `2^30/2^30` = 1 | 100% |

**concrete_visual:** The table itself — numerical evidence made visible, with Day 29 highlighted as the halfway row.

**abstract_symbol:** `\frac{2^n}{2^{30}}` in the Fraction column header; each row shows a specific instance.

**reveal_animation:**
- `Create` for the table outline (geometry — blue)
- `Write` for each row (math — orange) as narration reaches that day
- Day 29 row: `Write` then `Indicate` (scale pulse) on the 50% cell

**hold_content:** Table building progressively; formula in top-right corner; completed rows remain visible.

**in_state:** Fraction formula in corner (from Shot 4). Table slides in from bottom.

**out_state:** Full table visible, Day 29 row highlighted orange. Table persists into Shot 6.

**transition:** Zoom (into Day 15 inset area, table stays)

---

## Shot 6: Day 15 Punchline

**Beats covered:** 8
**Estimated duration:** ~25 s

**Narration lines:**
> Beat 8: Now check Day 15. The fraction covered on Day 15 is two-to-the-15 divided by two-to-the-30 — that is one divided by two-to-the-15. Work it out: approximately 0.003 percent. Not 50 percent. Not even one percent. On Day 15, the lily pad is effectively invisible on the pond.

**Visual content:** The existing table from Shot 5 stays on screen. An inset row appears below the table, slightly separated with a dashed border (blue): Day 15 | `2^15/2^30 = 1/32768` | `0.003%`. The 0.003% value appears in orange and is `Indicate`-pulsed. A thought-bubble callout near the table: "Day 15?" with a large `✗` (referencing the hook). The tiny percentage value and the `✗` are the visual punchline.

**concrete_visual:** The Day 15 inset row in the table — a direct comparison between the guess (Day 15) and the actual value (0.003%).

**abstract_symbol:** `\dfrac{2^{15}}{2^{30}} = \dfrac{1}{32768} \approx 0.003\%` in orange.

**reveal_animation:**
- `Write` for the inset row content
- `Indicate` (pulse) on "0.003%"
- `Write` then `FadeOut` for the "Day 15? ✗" callout

**hold_content:** Full table (Day 25–30) + Day 15 inset row; "0.003%" highlighted throughout.

**in_state:** Table from Shot 5 visible; inset slides in.

**out_state:** Table + Day 15 inset both visible. Everything except the pond outline fades for Shot 7.

**transition:** Fade (table fades; pond expands)

---

## Shot 7: One Step Back

**Beats covered:** 9
**Estimated duration:** ~20 s

**Narration lines:**
> Beat 9: Here is the key insight. The lily pad doubled from Day 29 to Day 30. That means Day 30 is exactly twice Day 29. If Day 30 is 100 percent, then Day 29 must be exactly 50 percent. You do not need to solve an equation. You just need one backward step from the end.

**Visual content:** A large circular pond (blue outline, cream fill = 100%) centered, labeled "Day 30 — 100%". The fill animates **backward** — instantly halving — as a "rewind" effect. When the pond reaches 50% fill, "Day 29 — 50%" label appears in orange. Simultaneously, the equation `\frac{2^{29}}{2^{30}} = \frac{1}{2}` appears to the right of the pond in orange. A large backward arrow (blue) above the pond illustrates the "one step back" motion.

**concrete_visual:** Circular pond animating from fully covered (Day 30) backward to half-covered (Day 29) — the reversal made physical.

**abstract_symbol:** `\dfrac{2^{29}}{2^{30}} = \dfrac{1}{2}` in orange, appearing simultaneously with the backward animation.

**reveal_animation:**
- `Create` for the pond circle
- Backward fill animation via `ValueTracker` (1.0 → 0.5)
- `Write` for `2^{29}/2^{30} = 1/2` equation
- `Create` for the backward arrow (blue)

**hold_content:** Pond at 50% coverage; `2^{29}/2^{30} = 1/2` equation; backward arrow; "Day 29 — 50%" label all persist.

**in_state:** Table fades; pond expands from center.

**out_state:** Pond at 50%, equation and "Day 29 — 50%" label visible. Camera slides back to show both fill bars.

**transition:** Slide (back to split-screen)

---

## Shot 8: Split-Screen — The Shape of Exponential Growth

**Beats covered:** 10
**Estimated duration:** ~30 s

**Narration lines:**
> Beat 10: Compare two panels side by side. On the left: the pond fills by equal slices every day — a straight, steady climb. On the right: the exponential pond is nearly empty until Day 25, then it fills explosively in the final days. Same 30-day axis. Completely different shapes. That gap is why Day 15 feels like the answer.

**Visual content:** Screen split into two equal panels with a thin cream divider. **Left panel:** a vertical bar filling linearly — equal increments each day, labeled "Linear" in cream. **Right panel:** a vertical bar filling exponentially — using 2^n/2^30 proportions — nearly flat through Days 1–24, then explosive Days 25–30. Both panels share a horizontal "Day" counter (ticks 1 → 30 simultaneously, animated). At Day 15, a vertical marker line (orange dashed) drops across both panels — left is at 50%, right is visibly near zero. At Day 29, another orange dashed line drops — right panel reaches 50%.

**concrete_visual:** Two side-by-side fill bars with a shared day counter — the difference between linear and exponential made directly visible.

**abstract_symbol:** No formula — labels only ("Linear", "Exponential"). The visual IS the argument.

**reveal_animation:**
- `Create` for both bar outlines (geometry — blue)
- Both fill bars animate simultaneously via `ValueTracker`
- `Create` for Day 15 and Day 29 vertical marker lines (orange dashed)
- `Write` for "Day 15" and "Day 29" callout labels

**hold_content:** Both bars animating; day counter ticking; marker lines at Day 15 and Day 29 visible once placed.

**in_state:** Pond from Shot 7 slides left; split-screen slides in from right.

**out_state:** Both bars fully filled to Day 30. Day 29 orange marker prominent. Fade to result.

**transition:** Fade

---

## Shot 9: Result Statement

**Beats covered:** 11
**Estimated duration:** ~25 s

**Narration lines:**
> Beat 11: The answer is Day 29. Not Day 15. The pond was exactly half-covered just one day before it was completely full. The lily pad achieved in a single day what it had been building toward for all 29 days before. That is what exponential growth does.

**Visual content:** Clean shot. Large centered text: "**Day 29**" in orange at 72 px. Below it in cream: "= 50% coverage". Below that, in smaller cream: "one day before full coverage." The circular pond from Shot 7 reappears (smaller, bottom-right), showing 50% fill as a visual anchor. Everything is calm — this is the reveal beat.

**concrete_visual:** Pond at 50% fill (Day 29 label) — callback to the hook's pond.

**abstract_symbol:** "Day 29" and `= \frac{1}{2}` in orange.

**reveal_animation:**
- `Write` for "Day 29" (large, orange)
- `Write` for "= 50% coverage"
- `Create` for the small pond (bottom-right)

**hold_content:** "Day 29" text, "= 50% coverage", pond at 50% — all persist through the full beat.

**in_state:** Split-screen fades; result card appears.

**out_state:** Result card visible. → **Full wipe** (act boundary: result → worked example).

**transition:** Full wipe

---

## Shot 10: Worked Example Setup — The 20-Day Pond

**Beats covered:** 12
**Estimated duration:** ~20 s

**Narration lines:**
> Beat 12: Let us try a different pond. Same doubling rule — but this time the lily pad covers it completely in 20 days, not 30. When was this pond exactly half-covered? Your instinct probably says Day 10. Apply the same reasoning we just used.

**Visual content:** A fresh circular pond (blue outline, cream fill = 100%) centered, labeled "Full coverage: Day 20". Below it: "D = 20" in orange. A large question mark above "Day 10?" in cream — the wrong instinct surfaced again, mirroring the hook. No math revealed yet — this is setup only.

**concrete_visual:** A new pond labeled "20 days" — recontextualizes the problem.

**abstract_symbol:** `D = 20` in orange; `?` over "Day 10".

**reveal_animation:**
- `Create` for the pond circle
- `Write` for "Full coverage: Day 20" label
- `Write` for `D = 20`
- `Write` for "Day 10?" question mark

**hold_content:** Pond with "D = 20" label; "Day 10?" question mark visible.

**in_state:** Clean (after full wipe from Shot 9).

**out_state:** 20-day pond visible with question mark. Camera zooms in on the pond.

**transition:** Zoom

---

## Shot 11: Worked Example Derivation

**Beats covered:** 13–14
**Estimated duration:** ~65 s

**Narration lines:**
> Beat 13: The fraction covered on Day n is two-to-the-n divided by two-to-the-20. Set that equal to one-half and solve. Two-to-the-19 divided by two-to-the-20 equals one-half. The answer is Day 19. One day before full coverage — not Day 10. Now: when was it one-quarter covered? Two-to-the-18 divided by two-to-the-20 equals one-quarter. Day 18.
>
> Beat 14: The pattern is clean. A pond covered on Day D was half-covered on Day D minus one. One-quarter covered on Day D minus two. One-eighth covered on Day D minus three. Work backward from the last day. Each step back halves the coverage. It does not matter whether the total is 20 days or 30.

**Visual content:**

*Beat 13:*
Fraction formula appears beside the 20-day pond: `\frac{2^n}{2^{20}}` in orange. Set equal to `\frac{1}{2}` → `\frac{2^{19}}{2^{20}} = \frac{1}{2}`. Equation morphs via `Transform` as n → 19. "Day 19" appears in orange beneath the equation. The pond animates backward (100% → 50%), labeled "Day 19 — 50%". Then: equation transforms to `\frac{2^{18}}{2^{20}} = \frac{1}{4}` → "Day 18 — 25%". Pond animates backward again to 25%.

*Beat 14:*
A 3-row pattern table appears (replacing the pond detail):

| Step back | Day | Coverage |
|-----------|-----|---------|
| D−1 | 19 | 1/2 = 50% |
| D−2 | 18 | 1/4 = 25% |
| D−3 | 17 | 1/8 = 12.5% |

General formula: `\frac{2^{D-k}}{2^D} = \frac{1}{2^k}` in orange at bottom. This unifies both the 30-day and 20-day cases.

**concrete_visual:** 20-day pond animating backward through Day 19, Day 18 — the "one step back" technique applied to a new scenario.

**abstract_symbol:** `\frac{2^n}{2^{20}} = \frac{1}{2}` → `\frac{2^{19}}{2^{20}} = \frac{1}{2}` → `\frac{2^{D-k}}{2^D} = \frac{1}{2^k}`

**reveal_animation:**
- `Write` for initial formula `2^n/2^{20}`
- `Transform` from generic formula to `2^{19}/2^{20} = 1/2` (equation morphs)
- Backward pond animation (1.0 → 0.5) simultaneously with equation
- `Transform` again from `2^{19}/2^{20}` to `2^{18}/2^{20} = 1/4`
- `Create` for the 3-row pattern table
- `Write` for general formula `2^{D-k}/2^D = 1/2^k`

**hold_content:** 20-day pond (at current coverage level); current equation; pattern table once built.

**in_state:** 20-day pond from Shot 10 at 100%; formula appearing beside it.

**out_state:** Pattern table + general formula visible. → **Full wipe** (act boundary: worked example → recap).

**transition:** Full wipe

---

## Shot 12: Recap — The Law Behind the Riddle

**Beats covered:** 15–16
**Estimated duration:** ~40 s

**Narration lines:**
> Beat 15: Back to where we started. The lily pad doubles every day. Full coverage on Day 30. When was it half-covered? Day 29. The answer was always one step back from the end. The Day 15 guess is a linear answer to an exponential question. That is the trap.
>
> Beat 16: The next time you hear "it is growing slowly now, so we have plenty of time," stop and ask: is this linear or exponential? With exponential growth, the last few steps account for most of the change. The pond looked nearly empty all the way to Day 25. Then it filled in five days. The riddle hid the law. Now you can see it.

**Visual content:** Callback to Shot 1's pond — same circle, same tiny lily pad — fades in. The question text "On which day was it exactly half-covered?" reappears (cream). A `Write` animation reveals "**Day 29**" in large orange over the question text. The pond animates from full → half. Bottom of screen: series tagline in cream — *"Every riddle hides a law. Break it open."* Final hold: pond at 50%, "Day 29" in orange, tagline in cream.

**concrete_visual:** Return to the original pond from the hook — visual closure.

**abstract_symbol:** "Day D−1" in orange; `\frac{1}{2}` written beside the pond.

**reveal_animation:**
- `FadeIn` for the callback pond (background)
- `Write` for the question text (callback from Beat 1)
- `Write` for "Day 29" in large orange (the answer, landing emphatically)
- Backward pond animation (full → half)
- `Write` for tagline in cream

**hold_content:** Pond at 50%, "Day 29" text, tagline — all persist through Beat 16.

**in_state:** Clean (after full wipe from Shot 11).

**out_state:** Hold for 2 s → `FadeOut` to end card.

**transition:** Fade to end

---

## Shot summary

| Shot | Title | Beats | Duration | Transition out |
|------|-------|-------|----------|----------------|
| 1 | The Day 15 Trap | 1–2 | ~40 s | Full wipe |
| 2 | Exponential Growth Is Deceptive | 3–4 | ~40 s | Zoom |
| 3 | Counting the Doublings | 5 | ~25 s | Slide |
| 4 | The Coverage Formula | 6 | ~25 s | Zoom |
| 5 | Last-Five-Days Table | 7 | ~30 s | Zoom |
| 6 | Day 15 Punchline | 8 | ~25 s | Fade |
| 7 | One Step Back | 9 | ~20 s | Slide |
| 8 | Split-Screen Comparison | 10 | ~30 s | Fade |
| 9 | Result Statement | 11 | ~25 s | Full wipe |
| 10 | Worked Example Setup | 12 | ~20 s | Zoom |
| 11 | Worked Example Derivation | 13–14 | ~65 s | Full wipe |
| 12 | Recap | 15–16 | ~40 s | Fade to end |

**Total estimated:** ~385 s ≈ 6.4 min ✓ (within 240–660 s gate)

---

## Flags

**[DIR-NODECIDE] none** — all shots have named concrete visuals and abstract symbols.

**[ANIMATOR-NOTE] Shot 2 / Shot 8:** The fill-bar fill animation requires a `ValueTracker` or `updater` pattern on a `Rectangle`'s height. Standard manimgx approach; flag if the runtime version lacks `Rectangle.set_fill` updater support.

**[ANIMATOR-NOTE] Shot 7 / Shot 11:** The backward pond animation (100% → 50%) uses a reverse `ValueTracker` on a `Circle`'s fill opacity/proportion. If manimgx doesn't support partial circle fill natively, substitute a `Rectangle` fill bar or a `Sector` arc to represent coverage percentage.

**[ANIMATOR-NOTE] Shot 11, Beat 13–14:** Two `Transform` calls in sequence on the same equation object (generic → Day 19, Day 19 → Day 18). Ensure the `Transform` target objects are pre-built before each call to avoid VGroup mismatch.
