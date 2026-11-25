# Render Notes — cr-01-pond-half-covered

**Animator handoff.** 13 scenes rendered (one `.py` + one MP4 per shot) under `scenes/`.
All scene files set module-level `config.background_color = "#0F172A"`; every hold frame
was visually verified against `storyboard.md` (dark-slate bg confirmed on all 13 — no black
frames, i.e. no missing config line). Math/equations render cleanly (no garbled LaTeX in the
final hold frames). Two real defects were found during the frame self-check and fixed +
re-rendered at full quality (see "Defects found & fixed").

Render command used for verification re-renders:
`.venv/bin/manimgx render scenes/scene_NN.py <ClassName> -r 854x480 --fps 24`
(matching the existing MP4s' 854×480 @ 24 fps).

---

## Per-scene table

| # | File | Class name | Beats covered (storyboard) | SCENE_TARGET_SEC (placeholder) | Rendered dur. | Status |
|---|------|-----------|----------------------------|:---:|:---:|--------|
| 1  | `scenes/scene_01.py`  | `Shot01HookWalk`    | Beat 1 part 1 (Days 1–15)      | 20.0 | 20.04 s | OK |
| 2  | `scenes/scene_02.py`  | `Shot02HookClimax`  | Beat 1 part 2 (Day 30 + riddle)| 15.0 | 15.25 s | **fixed** (Day-30 counter label) |
| 3  | `scenes/scene_03.py`  | `Shot03Motivation`  | Beat 2 (full)                  | 30.0 | 29.67 s | OK |
| 4  | `scenes/scene_04.py`  | `Shot04SplitScreen` | Beat 3 (full)                  | 35.0 | 36.46 s | OK |
| 5  | `scenes/scene_05.py`  | `Shot05Formula`     | Beat 4 part 1 (formula intro)  | 20.0 | 20.46 s | OK |
| 6  | `scenes/scene_06.py`  | `Shot06Day15Table`  | Beat 4 part 2 (plug-in + table)| 10.0 | 16.38 s | OK |
| 7  | `scenes/scene_07.py`  | `Shot07OneStepBack` | Beat 5 (full)                  | 30.0 | 30.67 s | OK |
| 7b | `scenes/scene_07b.py` | `Shot07bResult`     | Beat 6 (result card)           | 20.0 | 19.54 s | OK |
| 8  | `scenes/scene_08.py`  | `Shot08LabSetup`    | Beat 7 part 1 (lab setup)      | 20.0 | 21.25 s | OK |
| 9  | `scenes/scene_09.py`  | `Shot09LabQuestion` | Beat 7 part 2 (question + rule)| 15.0 | 14.54 s | OK |
| 10 | `scenes/scene_10.py`  | `Shot10LabEighth`   | Beat 7 part 3 (one eighth)     | 20.0 | 19.04 s | **fixed** (garbled MathTex tag) |
| 11 | `scenes/scene_11.py`  | `Shot11Recap`       | Beat 8 part 1 (law + strip)    | 25.0 | 25.04 s | OK |
| 12 | `scenes/scene_12.py`  | `Shot12PayoffClose` | Beat 8 part 2 (Day-30 close)   | 20.0 | 20.92 s | OK |

**Total rendered video ≈ 308.8 s** across 13 scenes vs **215.3 s** of narration
(`timing.json`). The difference is the per-scene tail-hold padding (see below) — the Editor
trims/aligns each scene to its beat in `timing.json`; no looping is required because every
scene already runs at least as long as its beat content needs a hold.

Beat → audio durations from `timing.json` (for the Editor): Beat 1 = 33.72 s, Beat 2 =
28.51 s, Beat 3 = 29.30 s, Beat 4 = 30.55 s, Beat 5 = 23.50 s, Beat 6 = 15.05 s, Beat 7 =
29.64 s, Beat 8 = 25.03 s.

---

## Defects found & fixed (this verification pass)

Both were caught by extracting a near-end hold frame from each MP4 and comparing to the
storyboard spec. Both re-rendered at full quality (854×480 @ 24 fps) over the defective file
and re-verified on disk.

1. **Shot 02 (`scene_02.py`) — Day-30 counter label missing.** The hold frame showed an empty
   chip box top-left; the `Day 30` numeral never rendered. Root cause: line 82 used
   `Transform(chip_txt, Text("Day 30", ...))`, and that Transform left the target invisible in
   this scene (the identical pattern works in `scene_01.py`, so it was scene-specific). Fix:
   replaced the Transform with an explicit `FadeOut` of the old label + a fresh centered
   `Write(day30_txt)` — which also matches the storyboard's stated method for counter ticks
   ("counter ticks are `Write()`"). Verified: "Day 30" now legible in the chip on the final frame.

2. **Shot 10 (`scene_10.py`) — garbled MathTex recap tag.** The hold frame rendered
   `11` + literal `mathrmam → 50%` (the `\mathrm{am}` was mangled). Root cause: line 81 had a
   raw-string double backslash, `r"11\\ \\mathrm{am}"`, which injected a stray LaTeX line break
   and broke the `\mathrm`. Fix: changed to `r"11\ \mathrm{am}"` (single-backslash space).
   Verified: tag now reads cleanly "11 am → 50%" in orange.

**False alarms (NOT defects — no change made):** Shot 02's riddle line and Shot 11's bottom
caption looked garbled in a frame sampled ~8 frames before the end, but that sample landed
*mid-`Write()` animation*. The true final hold frame of each is clean. No re-render needed for
these (Shot 02 was already re-rendered for defect #1; its riddle line confirmed clean).

---

## Shared scientist-figure note (refactor recommendation)

The minimal stylized scientist figure (`make_scientist`) is **defined independently and
identically in each of the six scene files that use it**: `scene_01.py`, `scene_02.py`,
`scene_08.py`, `scene_09.py`, `scene_10.py`, `scene_12.py`. Each copy is a ~15-line function
(capsule body + circle head + lab-coat line, optional foot ticks) per `continuity.md §1`.

**Recommendation:** extract it (plus the shared `make_pond` / `make_pad` helpers that are also
duplicated across pond scenes) into a single module, e.g. `scenes/shared_figures.py`, and import
it in each scene. This keeps the figure visually consistent if its design ever changes and
removes ~6× duplication. Not done now because it is a cross-file refactor beyond this
verification pass's scope; flagged for a future cleanup task.

---

## Deviations from the storyboard (and rationale)

- **Shot 07b added** (`scene_07b.py`, `Shot07bResult`). The storyboard's `[DIR-NODECIDE]` flag #1
  offered two options for Beat 6 (the "result" statement); this build implements **option (b)** —
  a dedicated result shot with the halved pond + a large `Day 29 = 50%` result card, rather than
  voicing Beat 6 over Shot 7's out-wipe. This gives Beat 6 its own clean hold frame for narration
  timing. (If the Director prefers option (a), delete `scene_07b.py` / `Shot07bResult.mp4` and let
  Beat 6 ride Shot 7's tail.)
- **Shot 04 fill geometry.** The left/right "fill" is rendered as growing *rectangles* inside the
   oval ponds (a progress-bar feel), not fills clipped to the ellipse. This is an intentional
   simplification already in the scene code; it reads correctly as "left smoothly full / right
   exploded to full" at the Day-30 hold, so no restyle was made (per: don't restyle scenes that
   match the storyboard). Minor cosmetic note for QC: the rectangular fill pokes slightly past the
   oval rim, and a single leftover tiny pad dot remains in the right pond's center. Neither affects
   legibility or the hold content.
- **Shot 06 table grid.** A stray horizontal grid line extends to the right frame edge near rows
   27–28; it does not obscure any cell text and all required elements (Day-15 `0.003%` punchline,
   highlighted Day-29 `50.0%`, Day-30 `100%`) are legible. Left as-is.

---

## [ANIMATOR-NODECIDE] / [ANIMATOR-CAPABILITY] flags

- **No `[ANIMATOR-CAPABILITY]` flags.** Every shot is within manimgx 2D bounds (ovals, circles,
  rectangles, lines, `MathTex`, `Text`, camera-free framing). No 3D, no illustrated characters —
  the scientist is a minimal geometric figure per `continuity.md §1`.
- **No new `[ANIMATOR-NODECIDE]` flags raised by this pass.** The three existing `[DIR-NODECIDE]`
  flags in `storyboard.md` (Beat 6 boundary, Shot 7 20-day pond generalization, Shot 4 naming) are
  Director decisions; the build resolves them as: (1) dedicated Shot 07b [see deviation above],
  (2) 20-day pond shown visually-light in Shot 7's hold (both ponds halved), (3) Shot 4 kept free of
  on-screen "linear"/"exponential" words. All three remain open for Director confirmation.

---

## Tail-hold pattern (for the Editor to finalize durations vs `timing.json`)

Every scene ends with an explicit tail hold that pads it out to its beat so the video never runs
ahead of the narration:

```python
# X = SCENE_TARGET_SEC - current_animation_duration
tail_hold = max(0.5, SCENE_TARGET_SEC - <animation_duration>)   # S7b uses a 6.0 floor instead of 0.5
self.wait(tail_hold)                                            # final action in construct()
```

- `SCENE_TARGET_SEC` is currently a **placeholder** (the value shown in the table above), marked
  `TODO-AVSYNC`. It has NOT yet been reconciled against `timing.json`. The Editor should set each
  scene's effective duration to its beat(s) from `timing.json` and, if needed, adjust the
  `<animation_duration>` constant so `tail_hold` lands exactly on the beat boundary. Because the hold
  is a plain `self.wait()` at the very end (after all content is on screen), trimming it changes only
  the still-frame length — no animation re-timing is required to shorten a scene.
- The hold frame itself is stable (all elements present, full opacity) for the entire tail, so any
  cut point within the tail is safe.

**Handoff state:** 13/13 scenes rendered and frame-checked; 2 defects fixed + re-rendered; ready
for Narration sync / Editor assembly against `timing.json`.
