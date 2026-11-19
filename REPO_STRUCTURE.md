# Repository Structure

This document defines the canonical directory layout for the Video-channel repository. All agents and automation scripts must follow this structure when creating or referencing artifacts.

## Root Level

```
Video-channel/
├── CLAUDE.md                    # Project instructions, build protocol, environment
├── REPO_STRUCTURE.md            # This file — canonical directory layout
├── .env                         # Environment variables (not committed)
├── .claude/                     # Claude Code configuration
│   ├── agents/                  # Agent definitions (see below)
│   ├── settings.json            # Claude Code settings
│   └── ...
├── plans/                       # Build plans written by athena
│   └── <task>.md                # One plan per build task
├── reviews/                     # Nemesis review reports
│   └── <task>-<timestamp>.md    # One review per verification run
├── product-backlog/             # Engineering automation backlog
│   ├── BACKLOG.md               # Master backlog with status table
│   └── epic-*.md                # Detailed epic files
├── productions/                 # Episode production artifacts
│   ├── README.md                # Productions layout documentation (E1-I5)
│   ├── channel-bible.md         # Channel-wide standards (E4-I1)
│   ├── tts-options.md           # TTS evaluation document (E3-I1)
│   ├── _smoke/                  # Smoke test artifacts (E1-I2, E1-I3)
│   │   └── scenes/
│   │       ├── smoke.py
│   │       └── smoke_latex.py
│   ├── tts-fixture/             # TTS integration test fixture (E3-I3)
│   │   ├── script-reviewed.md
│   │   ├── audio/
│   │   │   ├── beat_01.mp3
│   │   │   └── ...
│   │   └── timing.json
│   └── <episode-slug>/          # Per-episode production directory
│       ├── scope.md             # Episode scope — mandatory first artifact (producer)
│       ├── brief.md             # Episode brief (producer)
│       ├── script.md            # Original script (screenwriter)
│       ├── script-reviewed.md   # Math-reviewed script (math-reviewer)
│       ├── storyboard.md        # Shot-by-shot storyboard (storyboardist)
│       ├── continuity.md        # Continuity register (storyboardist/director)
│       ├── signoffs.md          # Director sign-off records
│       ├── scenes/              # Manim scene code (animator)
│       │   ├── scene_01.py
│       │   └── ...
│       ├── audio/               # Narration audio files (narration-engineer)
│       │   ├── beat_01.mp3
│       │   └── ...
│       ├── timing.json          # Timing map (narration-engineer)
│       ├── final.mp4            # Final assembled video (editor)
│       ├── export-notes.md      # Export/loudness notes (editor)
│       ├── qc-report.md         # QC review report (qc-reviewer)
│       ├── release.md           # Release metadata (release-agent)
│       ├── thumbnail.png        # Thumbnail image (E6-I1)
│       └── gates/               # Machine-readable gate verdicts (E5-I2)
│           ├── script-review.json
│           ├── math-review.json
│           └── ...
├── scripts/                     # Automation scripts
│   ├── tts.py                   # TTS adapter (E3-I2)
│   ├── orchestrate.py           # Episode orchestrator (E5-I1)
│   ├── gate-verdict.py          # Gate verdict generator (E5-I2)
│   ├── chapters.py              # Chapter extraction (E6-I1)
│   ├── thumbnails.py            # Thumbnail generation (E6-I1)
│   ├── preflight.py             # Publish preflight check (E6-I2)
│   ├── scene_snapshots.py       # Snapshot regression tests (E7-I3)
│   ├── archive_episode.sh       # Episode archiving (E7-I5)
│   └── ...
├── docs/                        # Documentation
│   ├── env.md                   # Environment setup documentation (E1-I1)
│   └── render-benchmark.md      # Render benchmark results (E7-I2)
├── tests/                       # Test files
│   └── test_*.py
├── assets/                      # Shared assets (music beds, fonts, etc.)
│   ├── music/
│   ├── fonts/
│   └── brand/
└── .gitignore
```

## Agent Artifact Ownership

Each agent is responsible for specific artifacts. This table maps agents to the files they create or modify:

| Agent | Creates/Modifies |
|-------|-----------------|
| producer | `productions/channel-bible.md`, `productions/<slug>/scope.md`, `productions/<slug>/brief.md` |
| screenwriter | `productions/<slug>/script.md` |
| math-reviewer | `productions/<slug>/script-reviewed.md` |
| director | `productions/<slug>/signoffs.md`, `productions/<slug>/continuity.md` (approves/amends) |
| storyboardist | `productions/<slug>/storyboard.md`, `productions/<slug>/continuity.md` (proposes) |
| animator | `productions/<slug>/scenes/*.py`, `productions/<slug>/render-notes.md` |
| narration-engineer | `productions/<slug>/audio/*.mp3`, `productions/<slug>/timing.json` |
| editor | `productions/<slug>/final.mp4`, `productions/<slug>/export-notes.md` |
| qc-reviewer | `productions/<slug>/qc-report.md` |
| release-agent | `productions/<slug>/release.md` |
| athena | `plans/<task>.md` |
| gaia | Implementation files per plan |
| nemesis | `reviews/<task>-<timestamp>.md` |

## Naming Conventions

- **Episode slugs:** Use kebab-case, descriptive slugs (e.g., `pilot-01-quadratic-formula`, `ep-02-completing-the-square`)
- **Scene files:** `scene_<NN>.py` where NN is a zero-padded sequence number
- **Audio files:** `beat_<NN>.mp3` where NN is a zero-padded beat number
- **Plan files:** `<task-name>.md` (e.g., `tts-adapter.md`, `orchestrator.md`)
- **Review files:** `<task-name>-<timestamp>.md` (e.g., `tts-adapter-20261117-143022.md`)

## Per-Episode Directory Structure

Every episode follows this exact structure under `productions/<slug>/`:

```
productions/<slug>/
├── scope.md              # Required: Episode scope (mandatory first artifact)
├── brief.md              # Required: Episode brief
├── script.md             # Required: Original script
├── script-reviewed.md    # Required: Math-reviewed script
├── storyboard.md         # Required: Shot-by-shot storyboard
├── continuity.md         # Required: Continuity register
├── signoffs.md           # Required: Director sign-offs
├── scenes/               # Required: Manim scene code
│   └── scene_*.py
├── audio/                # Required: Narration audio
│   └── beat_*.mp3
├── timing.json           # Required: Timing map
├── final.mp4             # Required: Final video
├── export-notes.md       # Required: Export notes
├── qc-report.md          # Required: QC report
├── release.md            # Required: Release metadata
├── thumbnail.png         # Optional: Thumbnail
└── gates/                # Optional: Machine-readable gate verdicts
    └── *.json
```

## Build Loop Artifacts

The mandatory build loop (athena → gaia → nemesis) produces these artifacts:

1. **Plan:** `plans/<task>.md` — Written by athena before any implementation
2. **Implementation:** Various files depending on the task
3. **Review:** `reviews/<task>-<timestamp>.md` — Written by nemesis after verification

## Automation Script Conventions

All automation scripts in `scripts/` follow these conventions:

- Python scripts use argparse for CLI interface
- Shell scripts use set -euo pipefail
- All scripts support --help
- Scripts output to stdout and return exit code 0 on success, non-zero on failure
- Scripts are idempotent where possible
- Scripts log to stderr for debugging, output results to stdout

## Documentation Conventions

- `docs/env.md` — Environment setup, versions, installation instructions
- `docs/render-benchmark.md` — Performance benchmark results
- `productions/README.md` — Productions layout documentation
- `productions/channel-bible.md` — Channel-wide creative standards
- `productions/tts-options.md` — TTS options evaluation

## Version Control

- All source code, scripts, and documentation are committed to git
- Large binary artifacts (final.mp4, audio files) may be stored in git-lfs or archived separately
- The `.gitignore` file excludes temporary and generated files
- Episode directories are committed as complete units
