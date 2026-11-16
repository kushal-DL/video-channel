# Epic 3: Pilot Episode End-to-End

**Goal:** Produce the first full episode from brief to final render, validating every agent handoff in a real-world scenario.

**Why this matters:** Individual components working doesn't guarantee end-to-end success. This epic proves the entire pipeline—from producer brief through QC review—can deliver a polished video ready for YouTube release.

**Estimated effort:** 3-4 days of build loop work

## Status

| Item | Story | Status |
|------|-------|--------|
| E3-I1 | Write pilot brief and script | Not started |
| E3-I2 | Math review and storyboard | Not started |
| E3-I3 | Full render pipeline test | Not started |

Status values: **Not started** (no work begun) · **In progress** (build loop running) · **Built** (implemented, awaiting nemesis verification) · **Done** (built and tested, nemesis verdict CLEAN).

## E3-I1: Write Pilot Brief and Script

- **Description:** Create the complete narrative content for Episode 1: "Introduction to Calculus."
- **Depends on:** none
- **Rationale:** The pilot must establish the channel's pedagogical voice, visual style, and production quality. It serves as both a learning resource and brand introduction.
- **Implementation notes:**
  - Topic: Derivatives as instantaneous rate of change
  - Target audience: High school AP Calculus students or self-learners
  - Duration goal: ~6 minutes (360 seconds) at 15fps = 24 frames per second average
- **Acceptance criteria:**
  - `productions/episode-001-introduction-to-calculus/brief.md` exists with clear learning objectives
  - `productions/episode-001-introduction-to-calculus/script.md` contains numbered beats, [MR] tags on math claims
  - Script total duration maps to ~6 minutes when read at normal pace

## E3-I2: Math Review and Storyboard

- **Description:** Adversarially verify all mathematical claims and create a shot-by-shot visual plan.
- **Depends on:** E3-I1
- **Rationale:** Math errors are unforgivable in educational content. The storyboard ensures visuals match narration timing exactly, preventing rework during rendering.
- **Implementation notes:**
  - Use math-reviewer agent to challenge every [MR]-tagged claim
  - Storyboard must specify exact manimgx commands for each shot (Write, FadeIn, etc.)
  - Include transition specs: cut vs cross-dissolve, duration of each
- **Acceptance criteria:**
  - `productions/episode-001-introduction-to-calculus/script-reviewed.md` exists with all claims verified
  - `productions/episode-001-introduction-to-calculus/storyboard.md` lists every shot with visual description and transition type
  - Continuity register (`continuity.md`) documents recurring motifs and notation choices

## E3-I3: Full Render Pipeline Test

- **Description:** Execute the complete production pipeline from script to final.mp4.
- **Depends on:** E3-I2
- **Rationale:** This is the ultimate integration test—proving all agents can work together without breaking the build.
- **Implementation notes:**
  - Animator renders scenes → Editor muxes with narration → QC reviewer validates output
  - Must use actual TTS audio (Epic 2) or placeholder voiceover
  - Final video must pass loudness normalization and frame extraction checks
- **Acceptance criteria:**
  - `productions/episode-001-introduction-to-calculus/final.mp4` exists and plays correctly
  - `productions/episode-001-introduction-to-calculus/timing.json` maps narration to scene boundaries
  - QC report (`qc-report.md`) shows zero critical issues

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Script timing doesn't match visual pacing | Use timing.json as source of truth; adjust scenes to voice, not vice versa |
| Math rendering fails mid-pipeline | Test LaTeX smoke test (E1-I3) before full render |
| Audio sync drifts during muxing | Use ffmpeg's `-sync 1` flag and verify with ffprobe timestamps |

## Success Criteria for Epic Completion

All three stories marked **Done** with nemesis verdict CLEAN. The pilot episode is fully rendered, QC'd, and ready for release metadata generation (Epic 5).
