# Epic 2: Update Agent Definitions & Channel Bible

**Goal:** Encode the Episode 1 post-mortem quality rules directly into the agent definitions (`.claude/agents/*.md`), channel bible (`productions/channel-bible.md`), and repository structure (`REPO_STRUCTURE.md`) so that no future episode can ship silent, off-palette, out-of-duration-range, or mathematically unverified content.

**Why this matters:** Episode 1 shipped silent, on a black background, and only 66 seconds long because the studio agent prompts lacked hard quality gates. Agents drive all pipeline behavior. Before re-rendering Episode 1 (Epic 4), the agent rules must be updated so the studio team enforces scope, worked examples, write-style reveals, color palette, audio verification, and duration limits.

**Execution order:** #2 in the backlog sequence (after Epic 1 Environment Setup; before Epic 3 TTS and Epic 4 Re-render).

**Estimated effort:** 1-2 days of build loop work

## Status

| Item | Story | Status | Owner | Acceptance Criteria |
|------|-------|--------|-------|---------------------|
| E2-I1 | producer: mandatory scope.md | Done | Fast Path (main session) | `producer.md` contains scope.md authoring requirement; brief references it. |
| E2-I2 | math-reviewer: worked-example enforcement | Done | Fast Path (main session) | `math-reviewer.md` contains worked-example re-derivation rule; unverified claims block sign-off. |
| E2-I3 | storyboardist: per-shot reveal animation & hold content | Done | Fast Path (main session) | `storyboardist.md` requires reveal animation field per shot and no empty hold frames. |
| E2-I4 | animator: palette & write-style animation default | Done | Fast Path (main session) | `animator.md` enforces `#0F172A` background and write-style equation reveals. |
| E2-I5 | narration-engineer: mandatory TTS audio & measured timing | Done | Fast Path (main session) | `narration-engineer.md` requires per-beat audio, ffprobe measured timing.json, and voice profile reference. |
| E2-I6 | editor: music bed, loudness, & duration gate | Done | Fast Path (main session) | `editor.md` enforces music bed, loudness normalization, and ffprobe duration gate [240s, 660s]. |
| E2-I7 | qc-reviewer: frame extraction & hard rejection | Done | Fast Path (main session) | `qc-reviewer.md` requires frame extraction evidence and explicit rejection of silent/off-palette/out-of-range renders. |
| E2-I8 | director: real sign-off on inspected frames | Done | Fast Path (main session) | `director.md` requires actual frame inspection and recording inspected timestamps in signoffs.md. |
| E2-I9 | channel bible & REPO_STRUCTURE updates | Done | Fast Path (main session) | `channel-bible.md` includes Animation Style section; `REPO_STRUCTURE.md` includes scope.md in per-episode tree. |

Status values: **Not started** (no work begun) · **In progress** (build loop running) · **Built** (implemented, awaiting nemesis verification) · **Done** (built and tested, nemesis verdict CLEAN).

## E2-I1: producer — Mandatory scope.md

- **Description:** Add `scope.md` authoring as a mandatory first artifact before the screenwriter starts.
- **Depends on:** none
- **Acceptance criteria:**
  - `producer.md` requires authoring `scope.md` with learning objectives, analogy→concept mapping, 2–3 worked examples with full solutions, out-of-scope list, and target duration.
  - `brief.md` must explicitly cite and inherit duration from `scope.md`.

## E2-I2: math-reviewer — Worked-Example Enforcement

- **Description:** Mandate that math-reviewer verify at least one fully-solved numerical example end-to-end and block unverified claims.
- **Depends on:** none
- **Acceptance criteria:**
  - `math-reviewer.md` requires re-deriving every intermediate algebra step on its own line.
  - Unverified `[MR]` claims block sign-off with `VERDICT: FAIL`.

## E2-I3: storyboardist — Reveal Animation & Hold Content

- **Description:** Require per-shot reveal animation specification (`Write`/`Create`, not `FadeIn`) and a declaration of what stays on screen during narration holds.
- **Depends on:** none
- **Acceptance criteria:**
  - `storyboard.md` template in `storyboardist.md` includes a mandatory `reveal_animation` field for each shot.
  - Hold frames must declare active visual content (no empty backgrounds).

## E2-I4: animator — Palette & Write-Style Animation

- **Description:** Enforce channel color palette (`#0F172A`) and write-style animation default for mathematical equations.
- **Depends on:** none
- **Acceptance criteria:**
  - `animator.md` requires module-level background configuration `config.background_color = "#0F172A"`.
  - MathTex objects must be animated with `Write()` or `Create()`, not `FadeIn()`.

## E2-I5: narration-engineer — Mandatory Audio & Measured Timing

- **Description:** Require per-beat TTS audio generation and measured durations from ffprobe.
- **Depends on:** none
- **Acceptance criteria:**
  - `narration-engineer.md` specifies that every episode must produce per-beat `.mp3` files and `timing.json`.
  - Durations in `timing.json` must be measured via `ffprobe`, never estimated.

## E2-I6: editor — Music Bed, Loudness, & Duration Gate

- **Description:** Require a licensed music bed, audio loudness normalization, and a hard 2.5–11 minute runtime gate.
- **Depends on:** none
- **Acceptance criteria:**
  - `editor.md` mandates muxing narration with a background music bed.
  - Duration must be verified via `ffprobe` to lie within `[150s, 660s]`.

## E2-I7: qc-reviewer — Frame Verification & Hard Rejection

- **Description:** Mandate extraction and visual inspection of rendered frames before approving an episode.
- **Depends on:** none
- **Acceptance criteria:**
  - `qc-reviewer.md` requires extracting at least 8 frames via ffmpeg and recording evidence in `qc-report.md`.
  - Silent, black-background, or out-of-duration videos must be rejected.

## E2-I8: director — Real Sign-off on Rendered Frames

- **Description:** Require director to review actual rendered frames and sign off on concrete timestamps.
- **Depends on:** none
- **Acceptance criteria:**
  - `director.md` requires inspecting extracted frames before approval.
  - `signoffs.md` must record the specific frame timestamps inspected.

## E2-I9: channel bible & REPO_STRUCTURE Updates

- **Description:** Update `productions/channel-bible.md` and `REPO_STRUCTURE.md` with the new quality rules.
- **Depends on:** none
- **Acceptance criteria:**
  - `channel-bible.md` includes an "Animation Style" section (palette, reveals, voice).
  - `REPO_STRUCTURE.md` lists `scope.md` in the per-episode canonical tree.
