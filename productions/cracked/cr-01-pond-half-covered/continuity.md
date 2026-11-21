# Continuity Register — cr-01-pond-half-covered
**Title:** When Was the Pond Half-Covered?
**Maintained by:** Storyboard Artist | **Date:** 2026-11-21

---

## Notation established

| Symbol | Meaning | First introduced |
|--------|---------|-----------------|
| `f(n) = 2^n / 2^30` | Fraction of pond covered on Day n (30-day pond) | Shot 4 (Beat 6) |
| `a_n = 2^{n-1}` | Lily pad area on Day n (Day 1 = 1 unit model) | Shot 3 (Beat 5) |
| `2^{D-k} / 2^D = 1/2^k` | General "k steps back" formula for any D-day pond | Shot 11 (Beat 14) |
| `D` | Total days to full coverage (variable) | Shot 11 (Beat 14) |

**Off-by-one anchor:** Day 1 = 1 unit of area (i.e., `a_1 = 2^0 = 1`). Day n = `2^{n-1}` units. Day 30 = `2^{29}` units, normalized to coverage fraction `2^{29}/2^{29} = 1`. Equivalently, coverage fraction on Day n = `2^n/2^{30}` (both forms are algebraically identical — Beat 6 uses the second form; Beat 5 uses the first).

---

## Color assignments

| Element | Color | Hex | Rule |
|---------|-------|-----|------|
| Background | dark slate | `#0F172A` | Every scene file, module-level |
| Text / captions | cream | `#F2E3C6` | All narration labels, beat titles |
| Math (equations, fractions, percentages) | orange | `#F97316` | All `MathTex` and numeric labels |
| Geometry (pond circles, bar outlines, axes, arrows) | blue | `#3B82F6` | All `Create`-animated geometry |
| Day 29 row highlight | orange background | `#F97316` | Table in Shot 5; override cream text with dark-slate on this row for contrast |

**No ad-hoc colors.** If a new visual element doesn't fit these four roles, flag it `[ANIMATOR-NODECIDE]`.

---

## Object persistence rules

| Object | Introduced | Persists through | Removed |
|--------|-----------|-----------------|---------|
| Fraction formula `f(n) = 2^n/2^{30}` | Shot 4 | Shots 4–6 (top-right corner) | Fades at Shot 7 |
| Last-five-days table | Shot 5 | Shots 5–6 | Fades at Shot 7 |
| Circular pond (30-day) | Shot 1 | Shots 1, 7, 9, 12 | End of episode |
| Fill bars (split-screen) | Shot 2 (partial), Shot 8 (full) | Shot 8 only | Fades after Shot 8 |
| 20-day pond | Shot 10 | Shots 10–11 | Full wipe after Shot 11 |

**Equation persistence rule (from channel bible):** The working equation stays on screen across beats. Never clear and redraw. Use `Transform` to morph from one form to the next. Reserve full screen wipes for act boundaries only.

---

## Visual motifs

### "One step back" reversal
- **Description:** A circular pond animates backward — from fully covered to half-covered — illustrating that Day D−1 = 1/2 of Day D.
- **First use:** Shot 7 (Beat 9) — 30-day pond, Day 30 → Day 29.
- **Second use:** Shot 11 (Beat 13) — 20-day pond, Day 20 → Day 19 → Day 18.
- **Reuse note:** This motif is a core "Cracked" series motif — "work backward from the final state." Future episodes with an end-state argument should use the same backward animation pattern.
- **Implementation:** `ValueTracker` on a fill rectangle or `Sector` arc keyed to coverage fraction; animate from 1.0 → 0.5. If pond is a `Circle`, use a `Rectangle` fill overlay or a custom `Sector`.

### Paradox hook
- **Description:** The hook poses the Day 15 guess visually (orange callout) and strikes through it with `✗` — establishing that the viewer's first instinct was wrong before any math appears.
- **First use:** Shot 1 (Beats 1–2).
- **Callback:** Shot 12 (Beats 15–16) — the hook pond returns and "Day 29" replaces the `✗`.

### Split-screen comparison
- **Description:** Two fill bars side-by-side (linear left, exponential right) with a shared day counter. Used to show the shape difference directly.
- **First use:** Shot 2 (Beats 3–4) — brief preview at Days 1–10.
- **Full version:** Shot 8 (Beat 10) — full 30-day animation with Day 15 and Day 29 marker lines.

---

## Act boundaries and transitions

| Boundary | After | Transition | Description |
|----------|-------|-----------|-------------|
| Hook → Motivation | Beat 2 | Full wipe | Strike-through on Day 15 → clean slate for motivation |
| Motivation → Build-up | Beat 4 | Zoom | Zoom into exponential bar |
| Result → Worked example | Beat 11 | Full wipe | "Day 29" result card → clean 20-day pond setup |
| Worked example → Recap | Beat 14 | Full wipe | General formula → callback to hook pond |

---

## Animator handoff notes

1. **Background color:** `config.background_color = "#0F172A"` at module level in every scene file — mandatory.
2. **Shot 7 / Shot 11 — partial pond fill:** manimgx does not have a built-in "partially filled circle" primitive. Use a `Rectangle` fill bar inside a circular mask, or a `Sector` with `angle` keyed to coverage fraction. If neither works cleanly, use a simple vertical fill bar (rectangle) instead — the visual metaphor still holds. Flag with `[ANIMATOR-NODECIDE]` if substituted.
3. **Shot 8 — exponential fill bar:** coverage on Day n = `2^n / 2^30`. Use a `ValueTracker` for n (1 → 30) and set bar height proportionally. Clamp to screen height.
4. **Shot 11 — `Transform` chain:** pre-build all three equation states (generic `2^n/2^20`, Day 19 specific, Day 18 specific) before the first `Transform` to avoid animation glitches.
5. **Equation font size:** math at 60–72 px per channel bible; body labels ≥ 30 px; titles 56 px.
