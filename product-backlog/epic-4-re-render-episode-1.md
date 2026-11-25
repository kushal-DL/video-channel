# Epic 4: Re-render & Validate Episode 1 Through the Fixed Pipeline

**Goal:** Run the *fixed* pipeline (Epic 2 quality gates + Epic 3 TTS) over the existing episode-001 to produce a genuinely shippable video, proving end-to-end that the rewritten roster works.

**Why this matters:** A bad pilot already exists — `productions/episode-001-introduction-to-calculus/final.mp4` is silent, black-background, and 66 seconds (see Epic 2 post-mortem). This epic is **not** "make a new pilot"; it is the end-to-end proof that the fixes actually produce a shippable video. It is the first real test of everything in Epics 1–3.

> **Status note:** The original "Pilot Episode End-to-End" work was already attempted and produced an unshippable render. This epic supersedes it: re-run the pipeline on episode-001 with scope.md, a worked example, write-style animation, correct background, real narration + music, and a 2.5–11 min runtime.

**Execution order:** #4 in the backlog sequence (after Epic 3 TTS; before Epic 5 Automation). This is where the re-render of Episode 1 actually lives.

**Estimated effort:** 3-4 days of build loop work

## Status

| Item | Story | Status |
|------|-------|--------|
| E4-I1 | Write episode scope + script with worked example | Not started |
| E4-I2 | Math review and storyboard (per-shot reveal animation) | Not started |
| E4-I3 | Full re-render pipeline test (narration + music, 2.5–11 min) | Not started |

Status values: **Not started** (no work begun) · **In progress** (build loop running) · **Built** (implemented, awaiting nemesis verification) · **Done** (built and tested, nemesis verdict CLEAN).

## E4-I1: Write Episode Scope + Script with Worked Example

- **Description:** Create the complete narrative content for Episode 1 ("Introduction to Calculus") *starting from a mandatory scope.md*, including at least one fully-solved numerical worked example.
- **Depends on:** none (but consumes Epic 2's scope/duration rules)
- **Rationale:** The pilot must establish the channel's pedagogical voice, visual style, and production quality — and this time it must be *scoped first*. Episode 1 failed because scope was never defined; Epic 2 (E2-I1) makes `scope.md` a hard prerequisite.
- **Implementation notes:**
  - Topic: Derivatives as instantaneous rate of change
  - Target audience: High school AP Calculus students or self-learners
  - Duration goal: land in the 2.5–11 min window (150s–660s), measured from the final render — not estimated
  - `scope.md` must contain learning objectives, analogy→concept mapping, 2–3 worked examples with full solutions, out-of-scope list, and target duration
- **Acceptance criteria:**
  - `productions/episode-001-introduction-to-calculus/scope.md` exists with all five required sections
  - `productions/episode-001-introduction-to-calculus/brief.md` references scope.md and inherits its duration target
  - `productions/episode-001-introduction-to-calculus/script.md` contains numbered beats, [MR] tags on math claims, and ≥1 fully-solved worked example with every step on its own line

## E4-I2: Math Review and Storyboard (Per-Shot Reveal Animation)

- **Description:** Adversarially verify all mathematical claims — including re-deriving every worked-example step — and create a shot-by-shot visual plan that specifies the reveal animation per shot.
- **Depends on:** E4-I1
- **Rationale:** Math errors are unforgivable in educational content, and Episode 1's storyboard asked for `Write` but it was never enforced. The storyboard must name the reveal animation (`Write`/`Create`, not `FadeIn`) per shot so the animator can't default to fades.
- **Implementation notes:**
  - Use math-reviewer agent to challenge every [MR]-tagged claim and re-derive each worked-example step end-to-end
  - Storyboard must specify exact manimgx commands for each shot (Write, FadeIn, etc.) — reveal animation is a required field per shot
  - Include transition specs: cut vs cross-dissolve, duration of each; declare what stays on screen during holds (no empty frames)
- **Acceptance criteria:**
  - `productions/episode-001-introduction-to-calculus/script-reviewed.md` exists with all claims verified and worked-example steps re-derived
  - `productions/episode-001-introduction-to-calculus/storyboard.md` lists every shot with visual description, transition type, **and** reveal animation
  - Continuity register (`continuity.md`) documents recurring motifs and notation choices

## E4-I3: Full Re-render Pipeline Test (Narration + Music, 2.5–11 min)

- **Description:** Execute the complete production pipeline from script to final.mp4 with real narration, a music bed, correct background, and a measured runtime in the 2.5–11 min window.
- **Depends on:** E4-I2 (and Epic 3 TTS for real audio)
- **Rationale:** This is the ultimate integration test — proving all agents work together *and* that the Episode 1 defects are actually fixed: non-silent, on-palette (`#0F172A`), in-duration-range, with a worked example.
- **Implementation notes:**
  - Animator renders scenes (write-style reveals, module-level background config) → Narration Engineer produces per-beat audio + measured timing.json → Editor muxes narration + music bed → QC reviewer validates output
  - Must use actual TTS audio (Epic 3), not placeholder voiceover
  - Final video must pass loudness normalization and frame extraction checks; ffprobe duration ∈ [150s, 660s]
- **Acceptance criteria:**
  - `productions/episode-001-introduction-to-calculus/final.mp4` exists, plays correctly, has an audio stream (narration + music), and is on-palette
  - `ffprobe` duration of final.mp4 ∈ [150s, 660s], recorded in export-notes.md and qc-report.md
  - QC report (`qc-report.md`) shows zero critical issues with concrete evidence; nemesis returns VERDICT: CLEAN

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Script timing doesn't match visual pacing | Use timing.json (measured, not estimated) as source of truth; adjust scenes to voice, not vice versa |
| Math rendering fails mid-pipeline | Test LaTeX smoke test (E1-I3) before full render |
| Audio sync drifts during muxing | Use ffmpeg's `-sync 1` flag and verify with ffprobe timestamps |

## Success Criteria for Epic Completion

All three stories marked **Done** with nemesis verdict CLEAN. The re-rendered Episode 1 is fully rendered, QC'd (non-silent, on-palette, in-duration-range, worked example present), and ready for release metadata generation (Epic 6).
