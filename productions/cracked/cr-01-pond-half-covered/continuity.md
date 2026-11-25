# Continuity Register — cr-01-pond-half-covered

Maintained by the Storyboardist (proposes); Director approves/amends. This register is the single source of truth for recurring motifs, notation choices, character design, and act boundaries so the Animator can replicate every element consistently across shots. Cross-reference: `storyboard.md` shot numbers S1–S12.

---

## 1. Character design spec — "the scientist" (minimal geometric figure)

The scientist is a **stylized figure made only of basic shapes** (no illustration art, no 3D). Same design in every appearance: Shots 1, 2 (hook walk), 8, 9, 10 (lab), 12 (closing walk).

- **Body:** a single vertical capsule/rounded rectangle (cream `#F2E3C6` outline, no fill or dark-slate fill) — height ≈ 1.4× the head diameter.
- **Head:** a circle (same cream outline) sitting on top of the body; radius ≈ 0.5× body width.
- **Lab coat cue:** a short horizontal line across the upper body (cream) to suggest a coat/lab jacket — distinguishes "scientist" from a generic figure without extra art.
- **Walk cycle:** two small alternating foot ticks (short cream lines) under the body while walking; feet stop when she stops. Keep it minimal — 2-frame step, no limb articulation beyond this.
- **Stopping/staring pose:** feet together, body upright, head circle unchanged; a single short vertical "attention" line above the head is optional and must be used identically in S2 and S12 if used at all.
- **Consistency rule (Director confirmation required per brief §8):** this exact figure appears in the hook (S1–S2) and again in the lab worked example (S8–S10). The Animator must reuse one shared `Scientist` manimx group/mobject so proportions, colors, and walk cycle are identical across all appearances. Do not redraw from scratch per scene.
- **No name, no face features** (no eyes/mouth) — archetypal "the scientist" per channel bible House Style.

## 2. Palette usage (exactly 4 roles — no ad-hoc colors)

| Role | Hex | Used for in this episode |
|------|-----|--------------------------|
| Background | `#0F172A` | every scene, via module-level `config.background_color = "#0F172A"` |
| Text / captions | cream `#F2E3C6` | riddle text, labels (`linear growth`, `exponential growth`, day labels), table headers/cells (non-highlighted), caption lines, scientist figure outline |
| Math (equations, symbols) | orange `#F97316` | `fraction(n) = 2^n / 2^30`, `fraction(15) = 2^15 / 2^30`, all `%` overlays (`100%`, `50%`, `0.003%`), fractions `1/2, 1/4, 1/8`, highlighted table row (Day 29), counter numerals |
| Geometry (curves, axes, points) | blue `#3B82F6` | pond outlines, water surfaces, lily pad outlines, petri dish outline + rim, lab bench line, timeline strip, three-icon pattern strip, table grid lines |

**Highlight convention:** the single term/row under discussion is always orange. The Day-29 row in the coverage table (S6) and every `50%` state are the recurring orange highlights. No red, no green, no other hues — lily pads use blue outline + cream center (not a literal green fill), to stay inside the 4-role palette.

## 3. Recurring motifs

- **Day counter chip:** upper-left (hook shots S1–S2) / top-center shared chip (split-screen S4). Cream rounded rectangle, orange numerals, `Write()` on each tick. Format: `Day N`. In the lab, an equivalent **clock chip** ticks by the hour (`9 am`, `11 am`, `noon`) — same visual treatment (cream chip, orange time text) so the "counter" motif transfers from days to hours.
- **Pond shape:** one canonical top-down oval (blue outline, dark water fill), centered with ≥0.5 buff margin, used in S1–S2, S4 (both panels), S6 (tiny speck view), S7 (reversal + 20-day variant), S11 (three small states), S12. The 20-day pond (S7) is the same oval shape at a smaller scale — do not invent a new shape.
- **Lily pad:** small circle, blue outline, cream center; grows via `GrowFromCenter`. One tiny pad = Day 1; cluster near bank = Day 7; scattered patches = Day 15; full field = Day 30.
- **Container-halving motif (the episode's core visual law):** a container at full → reverse one step → exactly half, with an orange `50%` overlay. Appears as: pond S7 (`Day 30 → Day 29`), 20-day pond S7 (`Day 20 → Day 19`), petri dish S9 (`noon → 11 am`). Same animation grammar each time (full state, one backward step, half state + orange 50%). This is the deliberate transfer from pond to lab.
- **"Nearly nothing, then half, then everything" pattern strip:** three small icons — empty speck → half-covered → full container (blue geometry) — appears in S12 closing caption and conceptually frames S11's half/quarter/eighth strip.
- **Coverage table (S6 only):** columns `Day | Coverage fraction | % of pond`; rows Days 15, 25–30; Day-15 row carries the `0.003%` punchline callout; Day-29 row highlighted orange with `50.0%`; Day-30 row `100%`. Table is a one-shot element (does not recur), but its orange Day-29 highlight is the seed of S7's reversal landing.

## 4. Notation choices

- **Main formula:** `fraction(n) = 2^n / 2^30` — introduced in S5, persisted into S6 (equation persistence rule; never cleared and redrawn). Spoken form in narration is "2 to the power of n over 2 to the power of 30"; on-screen symbol uses superscript `2^n`.
- **Substitution:** `fraction(15) = 2^15 / 2^30` (S6), written below the main formula, not replacing it.
- **Fractions for backward steps:** `1/2`, `1/4`, `1/8` (S7 overlays, S10 dish, S11 strip). Always orange.
- **Percentages:** `0.003%`, `50.0%`, `100%` — always orange when they are the math claim; cream only for non-math labels.
- **Time notation (lab):** lowercase `am`/`noon` (`9 am`, `11 am`, `noon`) to match narration wording exactly.
- No logarithms, no `e^x`, no differential notation — out of scope per `scope.md`.

## 5. Act boundaries with full wipes (the ONLY allowed wipes)

| # | Boundary | After beat | Transition | What exits / what enters |
|---|----------|-----------|------------|--------------------------|
| A1 | Hook → Body | Beat 1 | full wipe, fade through bg ≤0.8 s | S2 final frame (full pond + riddle) → S3 tap/cup layout |
| A2 | Build-up → Worked example | Beat 6 | full wipe, fade through bg ≤0.8 s | S7 halved-pond state → S8 lab bench + petri dish |
| A3 | Worked example → Recap | Beat 7 | full wipe, fade through bg ≤0.8 s | S10 one-eighth dish → S11 three shrinking ponds |

All other transitions are cut / slide / zoom / morph (see `storyboard.md` per-shot transition specs). No mid-act wipes; no wipe at the very end (S12 holds to final frame, editor handles fade-to-black in assembly if desired — not a storyboard wipe).

## 6. Director decisions on [DIR-NODECIDE] flags (decided 2026-11-22)

Status: **ALL THREE FLAGS RESOLVED.** Flag text preserved for reference; each item now carries the Director's binding decision. Full rationale in `signoffs.md`.

### Decision D1 — Beat 6 (Result): ADD a dedicated result shot (option b). [RESOLVED]

> *Flag text:* Beat 6 (Result) is currently voiced over S7's out-state/wipe rather than given a dedicated `Shot07bResult` scene. Decide keep-as-is vs. add dedicated result shot with its own hold frame.

**Decision: ADD the dedicated shot.** Insert `Shot07bResult` (`scenes/scene_07b.py`) between S7 and S8, carrying Beat 6's full narration ("The pond was half-covered on Day 29…") over its own ≥6 s hold — well inside the channel-bible 15–45 s shot norm.

- **Hold frame (active content, no empty holds):** the halved pond from S7 persists at left; a large result card is `Write()`n beside it: `Day 29 = 50%` in orange (`#F97316`) on cream text — the episode's answer stated as a claim.
- **Transition:** S7→S7b cut (same scene continues, halved pond persists); S7b→S8 full wipe A2 (act boundary Build-up → Worked example). The wipe now exits the result card, not mid-narration.
- **Why:** the pilot's #1 defect was A/V sync from scenes shorter than their beats; a beat with no dedicated hold frame is exactly that risk. Beat 6 is also the pacing arc's "Result statement" segment (brief §7: 20–25 s) and deserves its own landing, not a transition tail.
- **Consequence for Animator:** scene count becomes 13 (`scene_01.py … scene_12.py` + `scene_07b.py`). The S7→S8 wipe in the act-boundary table is unchanged; it now fires after S7b's hold.

### Decision D2 — S7 generalization (20-day pond): CONFIRMED visual-light, keep as storyboarded. [RESOLVED]

> *Flag text:* script Beat 5 does not mention a 20-day pond; shown visually-light per brief §5c last bullet, supported by "no matter how long the journey took." Confirm visual-light treatment or direct verbal-only / drop.

**Decision: KEEP the compact side-by-side, visual-light.** This is required content, not invention — brief §3 (misconception 3) and §5c's last bullet both mandate generalizing to a shorter-journey pond ("it doesn't matter if it's 30 days or 20 days"). The narration line "no matter how long the journey took" licenses showing it.

- **Constraints (binding for Animator):** no re-derivation, no new formula; the 20-day pond is the same canonical oval at smaller scale (per §3 motif rules); its `Day 20 → Day 19` halving uses the identical container-halving animation grammar as the main pond. It must not out-frame or upstage the Day-30→Day-29 reversal, which remains the shot's hero.
- Note: this is a *generalization* of the law (brief §5c), distinct from the worked example — it does not violate the channel-bible "different real-world context" rule, which governs the Beat 7 petri-dish scene only.

### Decision D3 — S4 naming timing + §8 hook-shot tension: CONFIRMED as storyboarded; no label delay. [RESOLVED]

> *Flag text:* panels shown without on-screen `linear`/`exponential` words (names appear in S3). Confirm this satisfies brief §5a ("show panels before naming"), or delay S3 labels until after S4.

**Decision: CONFIRMED — keep S4 free of the on-screen words; do NOT delay S3's labels.** Two rulings:

1. **Naming order (the flagged question):** The storyboard already shows the two ponds *before* any on-screen naming in the demonstration shot itself, and Beat 3's narration never says "linear" or "exponential" — it describes behavior ("gains an identical slice…", "stays almost empty for three weeks"). S4 is therefore a pure visual demonstration; the names were introduced verbally + labeled in S3 (the motivation beat) where they are *defined*, not spoiled. This satisfies §5a's intent: the viewer sees the contrast before it is named in the proof shot. Delaying S3 labels to after S4 would orphan the definitions and weaken Beat 2 — rejected.
2. **§8 "hook shot" tension (Director ruling, beyond the flag):** brief §8 says both split-screen panels "must appear in the hook shot," but §5a calls the split-screen "the hook's visual backbone." The storyboard places the panels in S4 (body). Ruling: §5a's operative requirement is *show panels before naming*, which D3.1 satisfies; a literal 30-second hook cannot also carry the 30-day fill time-lapse without breaking the hook's "do not define exponential growth" rule (§6) and the ≤50 s hook budget. The split-screen therefore stands in S4 as the body's visual backbone, and its *seed* (the two-panel linear-vs-exponential comparison) is planted in S3 so the idea is continuous from motivation into build-up. No storyboard change required; this interpretation is recorded here as binding for Animator and QC.
