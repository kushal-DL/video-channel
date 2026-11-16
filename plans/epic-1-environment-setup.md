# Epic 1 Implementation Plan

**Generated:** 2026-11-17  
**Author:** athena (planner agent)  
**Status:** Ready for gaia implementation

---

## Executive Summary

This plan implements the remaining work from Epic 1: Environment Setup. The environment is partially configured — venv exists with manimgx installed, smoke test scenes are present but unverified, and ffmpeg/ffprobe are missing system-wide. This plan codifies verification steps, completes missing installations, and documents the productions layout.

---

## Current State Assessment (Verified 2026-11-17)

| Item | Status | Evidence |
|------|--------|----------|
| E1-I1: venv + manimgx | ✅ Built | `.venv/` exists at repo root; `manimgx --version` works (v0.1.1); import test passes |
| E1-I2: Smoke render pipeline | ⚠️ Pending verification | Scenes exist (`smoke.py`, `smoke_latex.py`) but no render output confirmed |
| E1-I3: LaTeX toolchain | ✅ Built | MathTex smoke scene exists; env.md claims successful test of `x^2` expression |
| E1-I4: ffmpeg/ffprobe | ❌ Not installed | Neither binary found on PATH (`which ffmpeg` fails) |
| E1-I5: Productions layout doc | ⚠️ Pending creation | No comprehensive README exists in `productions/` directory |

---

## Implementation Steps

### Step 1: Verify and Document Existing Artifacts (E1-I1, E1-I2, E1-I3)

**Goal:** Confirm what's already built and document exact versions/commands.

| Action | Command | Expected Output |
|--------|---------|-----------------|
| Check manimgx version | `.venv/bin/manimgx --version` | `manimgx 0.1.1` |
| Verify Python version in venv | `source .venv/bin/activate && python --version` | `Python 3.13.x` |
| Test import path | `source .venv/bin/activate && python -c "import manimgx as m; print('OK')"` | `OK` |

**Deliverable:** Update `docs/env.md` with verified versions and commands.

---

### Step 2: Render Smoke Tests (E1-I2, E1-I3)

**Goal:** Prove the render pipeline works end-to-end for both basic and LaTeX scenes.

| Action | Command | Expected Output |
|--------|---------|-----------------|
| Render basic smoke test | `.venv/bin/manimgx render productions/_smoke/scenes/smoke.py SmokeTest -ql --disable_caching -o /tmp/e1i2_smoke.mp4` | Exit 0; file > 50KB |
| Render LaTeX smoke test | `.venv/bin/manimgx render productions/_smoke/scenes/smoke_latex.py SmokeLatex -ql --disable_caching -o /tmp/e1i3_latex.mp4` | Exit 0; file > 20KB |

**Deliverable:** Two non-empty MP4 files in `/tmp/`, exact commands recorded in `docs/env.md`.

---

### Step 3: Install ffmpeg/ffprobe (E1-I4)

**Goal:** Get system-wide media processing tools installed and verified.

| Action | Command | Expected Output |
|--------|---------|-----------------|
| Check current state | `which ffmpeg ffprobe` | Empty or non-zero exit |
| Install via apt | `sudo apt-get update && sudo apt-get install -y ffmpeg` | Exit 0; packages installed |
| Verify binaries on PATH | `ffmpeg -version && ffprobe -version` | Version strings printed, exit 0 |

**Deliverable:** Both binaries available system-wide with documented versions.

---

### Step 4: Create Productions Layout Documentation (E1-I5)

**Goal:** Write a canonical reference for all artifact paths used by agents.

| Action | Details |
|--------|---------|
| Survey agent files | Grep all `.claude/agents/*.md` for path references |
| Map literal strings to artifacts | Confirm each cited path appears as-is in at least one file |
| Write comprehensive README | Document tree structure, per-episode slug convention, artifact ownership |

**Deliverable:** `productions/README.md` with:
- Canonical episode directory layout (`productions/<slug>/`)
- Per-artifact ownership (which agent creates it)
- Artifact descriptions and contents
- Verification that all cited paths are literal matches in agent files

---

## Acceptance Criteria Summary

| Epic Story | Acceptance Criteria |
|------------|---------------------|
| **E1-I1** | `.venv/bin/manimgx --version` exits 0; version recorded in `docs/env.md`; venv at repo root |
| **E1-I2** | `smoke.py` renders to non-empty MP4 with `-ql --disable_caching`; command and output logged |
| **E1-I3** | `smoke_latex.py` contains exactly one `MathTex(r"x^2")`; renders successfully; LaTeX packages documented if installed |
| **E1-I4** | Both `ffmpeg -version` and `ffprobe -version` exit 0; versions recorded in `docs/env.md`; binaries on system PATH |
| **E1-I5** | `productions/README.md` exists, comprehensive, cites agent files for each artifact, includes literal-path verification |

---

## Risk Register

| Risk | Probability | Mitigation |
|------|-------------|------------|
| manimgx version incompatibility with existing scenes | Low | Pin exact version (0.1.1); test immediately after install |
| LaTeX installation fails or is incomplete | Medium | Use `texlive-latex-base` + `texlive-fonts-recommended`; verify with MathTex render |
| ffmpeg not on PATH after install | Low | Verify with `which ffmpeg ffprobe`; document exact paths if non-standard |
| Agent path assumptions differ from reality | Medium | Cross-reference all `.claude/agents/*.md` files before finalizing layout doc |

---

## Dependencies

- **Upstream:** None (standalone epic)
- **Downstream:** Epic 2 (TTS), Epic 3 (pilot episode), Epic 4 (automation glue)

---

## Success Criteria for Epic Completion

All five stories marked **Done** with nemesis verdict CLEAN. Environment fully documented in:
1. `docs/env.md` — versions, commands, smoke test results
2. `productions/README.md` — canonical artifact layout and ownership

Any team member can set up a working development environment from scratch using the documented steps.

---

## Notes for gaia (implementer)

- Run each command in sequence; do not parallelize render tests (they're I/O bound)
- Capture actual stdout/stderr for each verification step — don't assume success without evidence
- If any step fails, document the failure mode and attempted workaround before escalating
- Nemesis will independently re-run all commands; ensure they are idempotent where possible
