---
description: Extract keyframes from a Manim video, critique visual/math quality, and save feedback.md
argument-hint: <path/to/video.mp4>
---

You are a meticulous Manim math animation reviewer and visual quality assurance engineer. Analyze the rendered video at `$ARGUMENTS` without exceeding a **25-frame budget at 720p** (~23K visual tokens, keeping total context well under 110K tokens).

Follow these exact steps:

1. **Validate & Prepare Paths**
   - Confirm `$ARGUMENTS` exists. Determine its parent directory (`VIDEO_DIR`) and filename without extension (`VIDEO_NAME`).
   - Create a temporary folder at `/tmp/manim_review_${VIDEO_NAME}` (remove it first if it already exists).

2. **Extract Keyframes Within Token Budget (Max 25 Frames @ 720p)**

   Manim videos are sequences of short animations separated by holds, and every scene ends with a `FadeOut` to an empty background — so blind uniform sampling (`fps=`) lands on fades, transitions and dead air by chance, wasting the frame budget on near-empty frames. **Never sample blindly.** Prefer, in order:

   - **A. manimgx storyboard (best — exact play-end frames).** If a matching `.py` scene file exists in `VIDEO_DIR` or its `scenes/` subdirectory and `manimgx` is installed (e.g. `.venv/bin/manimgx`), render the storyboard:
     `manimgx inspect <scene.py> [SceneName] -o /tmp/manim_review_${VIDEO_NAME}/storyboard.png`
     The PNG shows one annotated frame per play/wait end — exactly the completed-animation states, with zero fade frames. Read it (it may span multiple sheets) and use those as your keyframes; note each sheet's `t=…` captions for timestamps. If this yields enough distinct frames to cover the episode, skip B/C entirely.
   - **B. Scene-change extraction.** Run ffprobe for duration, then:
     `ffmpeg -i "$ARGUMENTS" -vf "select='gt(scene,0.04)',scale=1280:-2,showinfo" -fps_mode vfr -q:v 2 "/tmp/manim_review_${VIDEO_NAME}/frame_%03d.jpg" 2> "/tmp/manim_review_${VIDEO_NAME}/timestamps.txt"`
     (Use `-fps_mode vfr`, not the deprecated `-vsync`.) Note: on a mostly-static video with small content, scene scores stay tiny — if this yields **fewer than 5 frames**, fall back to C. If it yields more than 25, keep an evenly spaced subset of 25 and delete the extras.
   - **C. Hold-midpoint sampling (fallback).** Uniform `fps=` sampling is only acceptable as a last resort, and even then: after extracting at `FPS = min(1, 25 / duration)`, measure each frame's non-background pixel fraction (e.g. with PIL) and **drop frames that are near-empty** (below ~0.5% non-background pixels — fades and dead air), replacing them by re-sampling the midpoint of the longest remaining gaps until you have ≤25 informative frames. A frame is only worth its token cost if it shows a completed state.
   - Map each kept `frame_XXX.jpg` to its approximate video timestamp (`MM:SS`) using `timestamps.txt` or the frame index.

3. **Inspect Frames & Source Code**
   - Read all remaining keyframes in chronological order (batch-read them cleanly without printing verbose base64 logs).
   - If a matching `.py` Manim script exists in `VIDEO_DIR` or its `scenes/` subdirectory (or is referenced in the workspace), read it — before extraction if you plan to use method A above, and always — to cross-check mathematical intent against what actually rendered. Also note each scene's declared colors: if the code declares a background color that contradicts what the frames show (e.g. `background_color` set on a per-class `config = {...}` dict), flag it as a render-config issue in the report rather than assuming the video is correct — manimgx reads settings from its global `config`/CLI, not from arbitrary class attributes.

4. **Critique Quality & Content**
   Evaluate every frame for:
   - **Layout & Visual Overlap:** Overlapping LaTeX equations, labels colliding with axes/curves, text clipped by screen edges, or cramped margins.
   - **Legibility & Pacing:** Font sizes too small, poor color contrast against the background, leftover objects that weren't faded out (`FadeOut`/`Uncreate`), or abrupt/unpolished transitions.
   - **Mathematical & Content Accuracy:** Wrong signs, mismatched equation steps, mislabeled graph axes, incorrect geometric proportions, or broken LaTeX rendering (`?` or raw TeX artifacts).

5. **Write `feedback.md` & Clean Up**
   - Write the complete report to `${VIDEO_DIR}/feedback.md` using this structure:
     - **Summary & Overall Score** (1–10)
     - **Critical Issues (Must Fix)** — bullet points with `[Timestamp MM:SS]`, exact description of the visual/math bug, and the suggested Manim code fix (e.g., `.scale()`, `.next_to()`, `buff=`, `FadeOut()`).
     - **Pacing & Polish Suggestions** — minor layout, color, or animation timing improvements.
     - **Frame-by-Frame Log** — brief timestamped notes of what appears on screen.
   - Delete `/tmp/manim_review_${VIDEO_NAME}` once `feedback.md` is saved.
   - Confirm in chat that `${VIDEO_DIR}/feedback.md` has been created and summarize the top 3 issues found.
