# Video-Channel Product Backlog

## Execution Order (backlog sequence)

The epics below are numbered in **execution order** — the authoritative order they should be tackled. Each epic has a corresponding specification file in `product-backlog/epic-*.md`.

| # | Epic | Status | Why this position |
|---|------|--------|-------------------|
| 1 | **Epic 1: Environment Setup** | Done | Foundation — manimgx, LaTeX, ffmpeg must work before anything renders. |
| 2 | **Epic 2: Update Agent Definitions & Channel Bible** | Done | Fix the rules first. Encodes the Episode 1 post-mortem fixes directly into `.claude/agents/*.md` and `channel-bible.md` so the studio team knows what to produce. |
| 3 | **Epic 3: TTS and Voice Cloning** | Done | Provides real narration + music that the re-render requires. |
| 4 | **Epic 4: Re-render & Validate Episode 1** | Not started | End-to-end proof that the fixed pipeline and updated agents produce a shippable video. |
| 5 | **Epic 5: Automation Glue** | Not started | One-command builds + machine-readable gates, once the fixed pipeline is proven. |
| 6 | **Epic 6: Publishing and Release Tooling** | Not started | Chapters/thumbnails/preflight for a QC-approved episode. |
| 7 | **Epic 7: Polish and Iteration** | Not started | Performance/operational refinements surfaced by the re-render. |

---

## Epic 1: Environment Setup

**Goal:** Establish a fully verified, reproducible local development environment for manimgx-based math animation production.

| Item | Story | Status | Owner | Acceptance Criteria |
|------|-------|--------|-------|---------------------|
| E1-I1 | Create project venv and install manimgx | Built | gaia | `.venv/bin/manimgx --version` prints a version; recorded in `docs/env.md`. |
| E1-I2 | Render smoke test (trivial scene) | Built | gaia | A trivial Text/VGroup scene renders to a non-empty mp4 with exit 0. |
| E1-I3 | LaTeX toolchain verification for MathTex | Built | gaia | `MathTex(r"x^2")` renders correctly; package list recorded in `docs/env.md`. |
| E1-I4 | Install and verify ffmpeg/ffprobe | Built | gaia | `ffmpeg -version` and `ffprobe -version` exit 0 on system PATH. |
| E1-I5 | Codify the productions layout in `productions/README.md` | Built | gaia | Every cited path appears as a literal string in at least one agent file; README lists the canonical per-episode tree. |

---

## Epic 2: Update Agent Definitions & Channel Bible (from Episode 1 post-mortem)

> **Context:** The first pilot render (`productions/episode-001-introduction-to-calculus/final.mp4`) was a silent, black-background, 66-second video that passed QC and was "published." The roster was missing scope definition, worked-example enforcement, animation-style rules, audio verification, and a hard duration gate. This epic encodes those hard quality gates into the agent prompts before re-rendering.

**Goal:** Encode post-mortem quality rules into `.claude/agents/*.md`, `channel-bible.md`, and `REPO_STRUCTURE.md`.

| Item | Story | Status | Owner | Acceptance Criteria |
|------|-------|--------|-------|---------------------|
| E2-I1 | producer: mandatory scope.md | Done | Fast Path (main session) | `producer.md` contains scope.md authoring requirement; brief references it. |
| E2-I2 | math-reviewer: worked-example enforcement | Done | Fast Path (main session) | `math-reviewer.md` contains worked-example re-derivation rule; unverified claims block sign-off. |
| E2-I3 | storyboardist: per-shot reveal animation & hold content | Done | Fast Path (main session) | `storyboardist.md` requires reveal animation field per shot and no empty hold frames. |
| E2-I4 | animator: palette & write-style animation default | Done | Fast Path (main session) | `animator.md` enforces `#0F172A` background and write-style equation reveals. |
| E2-I5 | narration-engineer: mandatory TTS audio & measured timing | Done | Fast Path (main session) | `narration-engineer.md` requires per-beat audio, ffprobe measured timing.json, and voice profile reference. |
| E2-I6 | editor: music bed, loudness, & duration gate | Done | Fast Path (main session) | `editor.md` enforces music bed, loudness normalization, and ffprobe duration gate [150s, 660s]. |
| E2-I7 | qc-reviewer: frame extraction & hard rejection | Done | Fast Path (main session) | `qc-reviewer.md` requires frame extraction evidence and explicit rejection of silent/off-palette/out-of-range renders. |
| E2-I8 | director: real sign-off on inspected frames | Done | Fast Path (main session) | `director.md` requires actual frame inspection and recording inspected timestamps in signoffs.md. |
| E2-I9 | channel bible & REPO_STRUCTURE updates | Done | Fast Path (main session) | `channel-bible.md` includes Animation Style section; `REPO_STRUCTURE.md` includes scope.md in per-episode tree. |
| E2-I10 | House Style / TED-Ed register upgrade | Done | Fast Path (main session) | Post-mortem fixes made the agents *safe*; this made them produce the right *style*. `channel-bible.md` has a House Style section (hook menu, concrete→abstract rule, equation-persistence rule, pacing budget, one-idea-per-beat); screenwriter/animator/storyboard/narration-engineer carry matching guidance; the local model is never told to emulate a named reference. See `_workspace/claude_plans/archive/ted-ed-style-agent-upgrade.md`. |

---

## Epic 3: TTS and Voice Cloning

**Goal:** Implement a production-ready text-to-speech pipeline that generates narration audio from scripts, extracts beat markers for scene transitions, and supports voice cloning for brand consistency.

> **Carried over from the 2026-11-20 audit:** The old `en-US-Standard-A` voice name (a Google Cloud TTS name wrongly attributed to edge-tts) has been removed from `channel-bible.md` and `narration-engineer.md`; voice selection is now explicitly deferred to this epic. `narration-engineer.md` invokes a `tts` CLI and reads the approved voice from the channel bible Voice section — the pipeline script below must satisfy both.

| Item | Story | Status | Owner | Acceptance Criteria |
|------|-------|--------|-------|---------------------|
| E3-I1 | Evaluate TTS options (ElevenLabs vs local) | Done | gaia | Decision document in `docs/tts-decision.md`; cost/latency/quality matrix; chosen voice is a **real, valid** voice name for the chosen provider (verified by a test synth), and that name is written back into the `channel-bible.md` Voice section. |
| E3-I2 | Generate narration pipeline script | Done | gaia | `scripts/tts.py` produces per-beat `.mp3` + measured `timing.json` from a test script. `narration-engineer.md` updated to call `python scripts/tts.py --voice ... --output-file ... "<text>"`. Note: duration measurement uses mutagen (ffprobe not available on dev machine — verify ffprobe is on PATH before Epic 4). |
| E3-I3 | Implement beat extraction from audio | Done | gaia | `scripts/extract_beats.py` maps timing.json beats to audio segments; outputs editor-compatible metadata. Tested against `productions/tts-fixture/`. |

---

## Epic 4: Re-render & Validate Episode 1 Through the Fixed Pipeline

**Goal:** Run the fixed pipeline (Epic 2 quality gates + Epic 3 TTS) over episode-001 to produce a genuinely shippable video, proving end-to-end that the rewritten roster works.

> **Blocker to resolve before E4-I3 (from the 2026-11-20 audit):** `editor.md` treats a missing background music bed as a hard failure, but no `assets/music/` folder exists on disk (REPO_STRUCTURE lists it but it is absent). E4-I0 below must be resolved first or the editor gate rejects every render.

| Item | Story | Status | Owner | Acceptance Criteria |
|------|-------|--------|-------|---------------------|
| E4-I0 | Resolve the music-bed source | Done | Fast Path | Option (b): `editor.md` updated — music optional when `assets/music/` absent; pilot proceeds without bed, tracked under E7-I4. `narration-engineer.md` updated with mutagen fallback (ffprobe not on PATH on dev machine). |
| E4-I1 | Write episode scope + script with worked example | Not started | producer + screenwriter | `scope.md` (all five sections) → brief references it; `script.md` has [MR] tags and ≥1 fully-solved worked example. |
| E4-I2 | Math review and storyboard (per-shot reveal animation) | Not started | math-reviewer + storyboardist | `script-reviewed.md` re-derives the worked example; `storyboard.md` names a reveal animation per shot, plus the `concrete_visual` ↔ `abstract_symbol` pairing per shot (per House Style). |
| E4-I3 | Full re-render pipeline test (narration + music, 2.5–11 min) | Not started | full studio team | New `final.mp4`: audio stream present, on-palette (`#0F172A`), ffprobe duration ∈ [150s, 660s], QC zero-critical with frame evidence; nemesis CLEAN. |

---

## Epic 5: Automation Glue

**Goal:** Build the orchestration layer that automates the episode production pipeline — one-command builds, machine-readable quality gates, and parallel execution of independent workstreams.

| Item | Story | Status | Owner | Acceptance Criteria |
|------|-------|--------|-------|---------------------|
| E5-I1 | One-command episode orchestrator | Not started | gaia | `scripts/orchestrate.py` builds a full episode from brief; resumable state; tested on one complete build. |
| E5-I2 | Machine-readable gate verdicts | Not started | gaia | `scripts/gate-verdict.py` emits schema-valid JSON at each quality gate; orchestrator acts on it. |
| E5-I3 | Parallel animator and narration-engineer execution | Not started | gaia | Animator + narration run concurrently after storyboard approval; measurable time reduction documented. |

---

## Epic 6: Publishing and Release Tooling

**Goal:** Build automated tooling that transforms a completed, QC-approved episode into a publication-ready YouTube upload with deterministic chapter markers, optimized thumbnails, and comprehensive preflight validation.

| Item | Story | Status | Owner | Acceptance Criteria |
|------|-------|--------|-------|---------------------|
| E6-I1 | Deterministic chapters and thumbnail extraction | Not started | gaia | `scripts/chapters.py` + `scripts/thumbnails.py` produce YouTube-ready chapters (from timing.json) and 1280×720 branded thumbnails. |
| E6-I2 | Publish preflight check | Not started | gaia | `scripts/preflight.py` validates format/metadata/quality/readiness with ERROR/WARNING/INFO levels; passes on the re-rendered pilot. |

---

## Epic 7: Polish and Iteration (surfaced by the re-render)

**Goal:** Refine the production pipeline based on lessons learned from the re-rendered Episode 1 — performance bottlenecks, quality regressions, and operational inefficiencies.

| Item | Story | Status | Owner | Acceptance Criteria |
|------|-------|--------|-------|---------------------|
| E7-I1 | Transition smoothing pass | Not started | animator + director | All transition issues from the re-render QC are addressed; a documented transition style guide exists. |
| E7-I2 | Parallel scene rendering benchmark | Not started | gaia | Benchmark report identifies bottlenecks; measurable render-time improvement documented. |
| E7-I3 | Snapshot regression tests for generated scenes | Not started | gaia | Snapshot framework captures baselines from the re-rendered pilot and flags visual diffs in CI. |
| E7-I4 | Loudness measurement automation and music-bed provenance | Not started | editor + gaia | Automated LUFS/true-peak measurement + normalization; music-bed licensing/attribution tracked. |
| E7-I5 | Episode archiving and cleanup policy | Not started | gaia | Documented archive/cleanup policies implemented as scripts; archived content retrievable, temp files removed safely. |
