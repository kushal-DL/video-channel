# Plan: Upgrade Agents for TED-Ed Style Math Videos

**Created:** 2026-11-20
**Author:** Claude (Opus)
**Status:** Implemented 2026-11-20
**Scope:** Documentation/prompt edits only (agent `.md` files + channel bible). No Python code.
**Audit basis:** All 13 agent files read (producer, screenwriter, storyboard, animator, director, math-reviewer, narration-engineer, editor, qc-reviewer, release, athena, gaia, nemesis) + channel bible.

---

## Problem Statement

The user wants TED-Ed / 3Blue1Brown style educational math videos (4–11 min, one concept + one worked example). Two risks were identified:

1. **The local model (Qwen 3.8 27B) has no concept of "TED-Ed style."** Every agent prompt says "math-tutorial YouTube channel" and assumes the model knows what good looks like. A local model needs the style described *explicitly and concretely*, never by naming a reference it has never seen.

2. **manimgx capability is sufficient but under-specified to the agents.** The API mirrors Manim Community Edition (`Scene`, `MathTex`, `Write`, `Create`, `VGroup`, transforms, graphs, camera). That covers all *math* TED-Ed moves (equation reveals, graphs, geometry, morphs, zoom-to-highlight). It does **not** do illustrated characters, hand-drawn art, or 3D — and the user explicitly does not want 3D. So the target is "3Blue1Brown-grade motion math," which manimgx can do. Agents currently lack the visual vocabulary to direct it.

---

## Capability Matrix (what manimgx can/can't do)

| Supported (use freely) | Not supported (do not specify) |
|---|---|
| Step-by-step equation reveals (`Write`/`Create`) | Illustrated characters / people |
| Function graphs, axes, coordinate planes | Painted/photographic backgrounds |
| Geometry: curves, secants, polygons, points | Hand-drawn / sketch aesthetic |
| Equation morphing / `Transform` between steps | 3D scenes (explicitly unwanted) |
| Color-coding variables across steps | Complex illustrative scene art |
| Camera zoom / pan to highlight sub-expressions | |
| Number lines, value trackers, dynamic labels | |

**Conclusion:** Target style = "motion-math explainer" (3B1B-grade), not illustrated-cartoon TED-Ed. This is achievable today with no new dependencies.

---

## Implementation Steps

Highest leverage first. Each step is a prompt/doc edit; all are Fast Path (no athena/gaia/nemesis).

### Step 1 — Channel bible: add "House Style" section (HIGHEST LEVERAGE)
File: `productions/channel-bible.md`

Add a new section that defines the style *without naming TED-Ed*, in model-followable terms:
- **Hook patterns** (pick-one menu): a paradox, a concrete real-world scenario, a "you already do this" reframe, or a surprising number. Give one worked example sentence of each.
- **Concrete→abstract rule:** show the tangible analogy and the symbol on screen *at the same time* (e.g., a ball leaving a ramp while `dy/dx` appears next to the tangent).
- **Equation persistence rule:** keep the working equation on screen; highlight the single term under discussion with the orange math color; never clear and redraw a formula just to change one term — use `Transform`.
- **Pacing arc with time budget** for a ~6 min episode: hook 30–50s, motivation 30–45s, build-up 3–4 min in 20–30s sub-beats, result 20–30s, worked example 60–90s, recap 30–45s.
- **"One idea per frame" rule:** never introduce two new symbols in the same beat.

### Step 2 — Screenwriter agent
File: `.claude/agents/screenwriter.md`
- Add 3–4 concrete **hook example sentences** the model can pattern-match against.
- Add a **voice sample paragraph** showing the target register ("Imagine you're…", second person, present tense).
- Require the worked example to be narrated as a *story* (set up the problem, predict, then solve), not just stated.

### Step 3 — Animator agent
File: `.claude/agents/animator.md`
- Add a **Visual Vocabulary** section with named techniques and the manimgx call for each:
  - Color-track a variable across steps (same color follows `x` everywhere).
  - Persistent diagram + incremental reveal (animate only the new element per beat).
  - Zoom/scale to highlight a sub-expression, then restore.
  - `Transform` one equation into the next instead of fade-swap.
- Add a short **capability boundary** note: no 3D, no character art — express ideas with graphs, geometry, and motion.

### Step 4 — Storyboard agent
File: `.claude/agents/storyboard.md`
- Add a required **concrete↔abstract mapping** field per shot: name the tangible visual and the math symbol it is paired with on screen.

### Step 5 — Narration voice: TED-Ed register + fix voice-name bug
Files: `productions/channel-bible.md`, `.claude/agents/narration-engineer.md`
- **Bug fix:** both files specify `en-US-Standard-A` and call it the "edge-tts default." That is a **Google Cloud TTS** voice name; edge-tts uses neural names (e.g., `en-US-AriaNeural`, `en-US-GuyNeural`). As written the TTS call fails or falls back silently. Either correct the name to a real edge-tts voice or explicitly mark voice selection as deferred to Epic 3 (TTS) — but stop attributing a Google voice to edge-tts.
- Add TED-Ed narration guidance to the voice profile: warm and unhurried; a beat of silence at each concept boundary; slow down for the worked example; let the viewer read an equation before moving on.
- Note: final voice *selection* is an Epic 3 decision; this step only fixes the latent bug and adds register guidance so Epic 3 inherits the right target.

### Step 6 — Producer agent cleanup
File: `.claude/agents/producer.md`
- Remove the `WebFetch` style note (web tools are disabled per CLAUDE.md; the instruction is dead and misleading to a local model).

---

## Known Blocker (outside this plan, flag before Epic 4)

**Editor's music-bed hard gate has no asset source.** `editor.md` treats a missing background music bed as "incomplete" (hard fail), but there is no `assets/music/` folder (REPO_STRUCTURE lists it; it does not exist on disk). Every Epic 4 episode will fail the editor gate until a licensed/royalty-free music source and provenance tracking exist. Options: (a) source royalty-free beds into `assets/music/` with attribution, or (b) soften the editor gate to "music bed optional for pilot." Decide before attempting a real render. Not fixed in this plan — recorded so it is not rediscovered at render time.

---

## Acceptance Criteria

- `channel-bible.md` has a House Style section with: hook menu, concrete→abstract rule, equation-persistence rule, pacing time-budget, one-idea-per-frame rule.
- `screenwriter.md` contains ≥3 example hook sentences and a voice sample.
- `animator.md` contains a Visual Vocabulary section naming ≥4 techniques, each with the manimgx construct, plus the no-3D/no-character boundary.
- `storyboard.md` requires a concrete↔abstract mapping field per shot.
- `narration-engineer.md` and `channel-bible.md` no longer attribute a Google voice name to edge-tts; TED-Ed register guidance added to the voice profile.
- `producer.md` no longer references WebFetch.
- No capability is specified anywhere that manimgx cannot render (verified against the matrix above).

**Confirmed needing no change:** math-reviewer, release, qc-reviewer (minor wording slip only), editor (correct as a gate — but see blocker below), athena, gaia, nemesis.

## Out of Scope

- TTS (Epic 3), orchestration (Epic 5), publishing (Epic 6).
- Any Python / scene code.
- A full test render (that is Epic 4; this plan only makes the agents ready).

## Risks

| Risk | Mitigation |
|---|---|
| Over-stuffing prompts hurts a 27B model's focus | Keep each addition tight; concrete examples over abstract rules. |
| Style guidance specifies unrenderable visuals | Every technique cross-checked against the capability matrix. |
| manimgx API differs subtly from Manim CE | Flagged for a real render check in Epic 4; this plan avoids asserting exact call signatures beyond the verified smoke-test set. |

## Next Step After This Plan

Epic 3 (TTS) remains the gating dependency for an actual episode. This plan makes the creative agents produce the right *content*; Epic 3 makes it *speakable*; Epic 4 proves it end-to-end.
