# Epic 1: Environment setup

**Goal:** Establish a fully verified, reproducible local development environment for manimgx-based math animation production, including all system dependencies, Python toolchain, LaTeX math rendering, and media processing tools.

**Why this matters:** Every downstream production agent (animator, narrator, editor, QC reviewer) depends on specific tools being available and working correctly. Without a verified environment, renders fail unpredictably and debugging is difficult. This epic eliminates environment-related uncertainty before any creative work begins.

**Execution order:** #1 in the backlog sequence — the foundation everything else builds on (TTS, re-render, automation all assume a working manimgx + LaTeX + ffmpeg toolchain).

**Estimated effort:** 1-2 days of build loop work

## Status

| Item | Story | Status | Notes |
|------|-------|--------|-------|
| E1-I1 | Create project venv and install manimgx | Built | ✅ manimgx 0.1.1, Python 3.13.18 verified |
| E1-I2 | Render smoke test | Built | ✅ /tmp/e1i2_smoke.mp4 (20KB valid MP4) |
| E1-I3 | LaTeX toolchain verification for MathTex | Built | ✅ MathTex(r"x²") renders correctly |
| E1-I4 | Install and verify ffmpeg/ffprobe | Built | ✅ ffmpeg 7.0.2-static, ffprobe 7.0.2-static on system PATH |
| E1-I5 | Codify the productions layout | Built | ✅ productions/README.md with literal-path verification |

Status values: **Not started** (no work begun) · **In progress** (build loop running) · **Built** (implemented, awaiting nemesis verification) · **Done** (built and tested, nemesis verdict CLEAN).

## E1-I1: Create project venv and install manimgx

- **Description:** Use uv to create `.venv` at repo root, install manimgx into it, and record the exact versions used. (Verified 2026-11-15: manimx is not installed.)
- **Depends on:** none
- **Rationale:** uv provides fast, reproducible Python environment management. Using a dedicated venv isolates manimgx dependencies from the system Python and other projects. Recording versions ensures reproducibility across machines and over time.
- **Implementation notes:**
  - Install uv if not present: `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - Use `uv venv .venv` to create the environment
  - Install with: `uv pip install --python .venv/bin/python manimgx`
  - Pin the exact version in `docs/env.md` for reproducibility
  - Consider creating a `pyproject.toml` or `requirements.txt` for future reference
- **Acceptance criteria:**
  - `uv venv .venv && uv pip install --python .venv/bin/python manimgx` exits 0
  - `.venv/bin/manimgx --version` prints a version string
  - Version string is recorded in `docs/env.md` (created by this item)
  - The venv is created at repo root as `.venv/`
  - No errors during installation

## E1-I2: Render smoke test

- **Description:** Prove the animator's documented render command works end-to-end with a trivial scene (command form taken from animator.md).
- **Depends on:** E1-I1
- **Rationale:** This validates the complete render pipeline: Python imports manimgx successfully, the renderer initializes, scene code executes, frames are generated, and output encoding produces a playable video file. It's the minimum viable proof that animation production can happen.
- **Implementation notes:**
  - Create `productions/_smoke/` directory for test artifacts
  - Scene should be intentionally simple: a few Text objects and VGroup layout only
  - Do NOT use MathTex here (that's E1-I3's job)
  - Use `-ql` (low quality) flag for fast test rendering
  - Use `--disable_caching` to ensure a fresh render every time
  - Record the exact command and its output in `docs/env.md`
- **Acceptance criteria:**
  - `productions/_smoke/scenes/smoke.py` contains one Scene class named `SmokeTest`
  - Scene uses only Text and VGroup (no MathTex, no complex animations)
  - Command: `.venv/bin/manimgx productions/_smoke/scenes/smoke.py SmokeTest -ql --disable_caching`
  - Command exits with code 0
  - A non-empty mp4 file is produced (check file size > 0)
  - The exact command and its real output are recorded in `docs/env.md`

## E1-I3: LaTeX toolchain verification for MathTex

- **Description:** Real math scenes use MathTex, which requires a local TeX distribution (verified 2026-11-15: none found); verify or install one.
- **Depends on:** E1-I2
- **Rationale:** Math tutorial videos require rendering mathematical notation. manimgx's MathTex class depends on an external LaTeX installation to compile TeX expressions into rendered output. Without this, no formulas, equations, or mathematical symbols can appear in videos.
- **Implementation notes:**
  - On Ubuntu/Debian: `sudo apt-get install texlive texlive-latex-extra texlive-fonts-recommended dvipng cm-super`
  - On macOS: Install MacTeX or use `brew install --cask basictex`
  - Verify with: `latex --version` and `kpsewhich` commands
  - The minimal test should render a simple expression like `x^2` or `\frac{a}{b}`
  - If LaTeX packages are missing, install them and note which ones in `docs/env.md`
- **Acceptance criteria:**
  - A second smoke scene `SmokeLatex` is created in `productions/_smoke/scenes/`
  - Scene contains exactly one `MathTex(r"x^2")` object
  - Renders with the same command form as E1-I2 (same flags, same quality settings)
  - Command exits with code 0
  - A non-empty mp4 file is produced
  - If LaTeX was installed by this item, the exact package names are recorded in `docs/env.md`
  - The rendered output visually shows the mathematical expression correctly

## E1-I4: Install and verify ffmpeg/ffprobe

- **Description:** editor.md (loudness, chapters), narration-engineer.md (duration probing) and qc-reviewer.md (frame extraction) all assume ffmpeg/ffprobe on PATH; neither was found locally as of 2026-11-15.
- **Depends on:** none
- **Rationale:** ffmpeg is the backbone of all media processing in the pipeline. It's used for:
  - Audio loudness normalization (editor)
  - Video duration and metadata probing (narration engineer)
  - Frame extraction for QC review (QC reviewer)
  - Final video muxing and encoding (editor)
  - Audio/video synchronization checks
- **Implementation notes:**
  - On Ubuntu/Debian: `sudo apt-get install ffmpeg`
  - On macOS: `brew install ffmpeg`
  - Verify both `ffmpeg` and `ffprobe` commands are available
  - Record versions for reproducibility
  - Test basic functionality: `ffmpeg -version`, `ffprobe -version`
- **Acceptance criteria:**
  - `ffmpeg -version` exits 0 and prints version information
  - `ffprobe -version` exits 0 and prints version information
  - Both versions are recorded in `docs/env.md`
  - ffmpeg and ffprobe are on the system PATH (not just installed in venv)
- **Status & Verification (2026-11-18):**
  - Static release binaries of ffmpeg and ffprobe (v7.0.2) installed to `~/.local/bin/` (in system PATH).
  - Verified `ffmpeg -version` and `ffprobe -version` both exit 0 on system PATH.
  - Verified with `./scripts/e1-verify.sh` and `./scripts/verify-env.sh`.

## E1-I5: Codify the productions layout

- **Description:** Every studio agent assumes artifact paths (brief.md, script.md, script-reviewed.md, storyboard.md, scenes/, audio/beat_*.mp3, timing.json, continuity.md, signoffs.md, final.mp4, qc-report.md, release.md) but no document defines them in one place.
- **Depends on:** none
- **Rationale:** Without a canonical directory layout document, agents may write to inconsistent paths, making it hard to find artifacts, automate processes, or understand the production pipeline. This document serves as the single source of truth for where everything lives.
- **Implementation notes:**
  - Survey all `.claude/agents/*.md` files to find every path reference
  - Create a comprehensive tree structure in `productions/README.md`
  - For each file/directory, note which agent creates it and what it contains
  - Include the per-episode slug convention (e.g., `productions/episode-001-introduction/`)
  - Verify by checking that every cited path appears as a literal string in at least one agent file
- **Acceptance criteria:**
  - `productions/README.md` exists and is comprehensive
  - Lists the canonical per-episode tree under `productions/<slug>/`
  - Each entry cites which `.claude/agents/*.md` file creates it
  - A verification check confirms every cited path appears as a literal string in at least one agent file
  - Document includes descriptions of what each artifact contains
  - Document is clear enough for a new team member to understand the layout

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| manimgx version incompatibilities | Pin exact version, test immediately after install |
| LaTeX installation is large/slow | Use minimal texlive packages initially, add as needed |
| ffmpeg not on PATH after install | Verify with `which ffmpeg` and `which ffprobe` |
| Agent path assumptions differ from reality | Cross-reference all agent files before finalizing layout doc |

## Success criteria for epic completion

All five stories are marked **Done** with nemesis verdict CLEAN. The environment is fully documented in `docs/env.md` and `productions/README.md`, and any team member can set up a working development environment from scratch using the documented steps.
