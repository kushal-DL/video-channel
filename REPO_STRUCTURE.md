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
│   ├── series-curriculum.md     # Master curriculum index — all series and episodes
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
│   ├── elementary/              # Series: Math Sparks — Elementary School (Class 1–8)
│   │   ├── series-curriculum.md # Series curriculum — episode list (producer)
│   │   └── <episode-slug>/      # Per-episode production directory (see layout below)
│   ├── middle-school/           # Series: Proof & Power — Middle School (Class 9–10)
│   │   ├── series-curriculum.md # Series curriculum — episode list (producer)
│   │   └── <episode-slug>/
│   ├── high-school/             # Series: The Math Frontier — High School (Class 11–12)
│   │   ├── series-curriculum.md # Series curriculum — episode list (producer)
│   │   └── <episode-slug>/
│   └── cracked/                 # Series: Cracked — math/science riddles (Class 6–12)
│       ├── series-curriculum.md # Series curriculum — episode list (producer)
│       └── <episode-slug>/      # Per-episode production directory
│
│   Per-episode layout (applies to every <series-slug>/<episode-slug>/):
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
| producer | `productions/channel-bible.md`, `productions/series-curriculum.md`, `productions/<series-slug>/series-curriculum.md`, `productions/<series-slug>/<episode-slug>/scope.md`, `productions/<series-slug>/<episode-slug>/brief.md` |
| screenwriter | `productions/<series-slug>/<episode-slug>/script.md` |
| math-reviewer | `productions/<series-slug>/<episode-slug>/script-reviewed.md` |
| director | `productions/<series-slug>/<episode-slug>/signoffs.md`, `productions/<series-slug>/<episode-slug>/continuity.md` (approves/amends) |
| storyboardist | `productions/<series-slug>/<episode-slug>/storyboard.md`, `productions/<series-slug>/<episode-slug>/continuity.md` (proposes) |
| animator | `productions/<series-slug>/<episode-slug>/scenes/*.py`, `productions/<series-slug>/<episode-slug>/render-notes.md` |
| narration-engineer | `productions/<series-slug>/<episode-slug>/audio/*.mp3`, `productions/<series-slug>/<episode-slug>/timing.json` |
| editor | `productions/<series-slug>/<episode-slug>/final.mp4`, `productions/<series-slug>/<episode-slug>/export-notes.md` |
| qc-reviewer | `productions/<series-slug>/<episode-slug>/qc-report.md` |
| release-agent | `productions/<series-slug>/<episode-slug>/release.md` |
| athena | `plans/<task>.md` |
| gaia | Implementation files per plan |
| nemesis | `reviews/<task>-<timestamp>.md` |

## Naming Conventions

- **Episode slugs:** Use kebab-case with a series prefix and sequence number (e.g., `hs-01-sets-venn-diagrams`, `ms-03-linear-equations`, `es-02-skip-counting`, `cr-01-birthday-paradox`)
- **Series slugs:** kebab-case lowercase — the four canonical series are `elementary`, `middle-school`, `high-school`, `cracked`
- **Scene files:** `scene_<NN>.py` where NN is a zero-padded sequence number
- **Audio files:** `beat_<NN>.mp3` where NN is a zero-padded beat number
- **Plan files:** `<task-name>.md` (e.g., `tts-adapter.md`, `orchestrator.md`)
- **Review files:** `<task-name>-<timestamp>.md` (e.g., `tts-adapter-20261117-143022.md`)

## Series Directory Structure

The `productions/` directory is organised by series. Each series has its own subfolder with a `series-curriculum.md` (series overview and episode list) and episode subdirectories beneath it:

```
productions/
├── series-curriculum.md         # Master index across all series
├── elementary/                  # Class 1–8: Math Sparks
│   ├── series-curriculum.md     # Series episode list
│   └── <episode-slug>/
├── middle-school/               # Class 9–10: Proof & Power
│   ├── series-curriculum.md
│   └── <episode-slug>/
├── high-school/                 # Class 11–12: The Math Frontier
│   ├── series-curriculum.md
│   └── <episode-slug>/
└── cracked/                     # Class 6–12: Cracked (math/science riddles)
    ├── series-curriculum.md
    └── <episode-slug>/
```

The slug `cracked` is the canonical series slug for the riddles series ("Cracked").

**Naming convention for episode slugs within a series:**
`<series-prefix>-<NN>-<short-concept>` — e.g. `hs-01-sets-venn-diagrams`, `ms-01-rational-numbers`, `es-01-counting-shapes`, `cr-01-birthday-paradox`.

Series prefix shorthands: `es` = elementary, `ms` = middle-school, `hs` = high-school, `cr` = cracked.

## Per-Episode Directory Structure

Every episode follows this exact structure under `productions/<series-slug>/<episode-slug>/`:

```
productions/<series-slug>/<episode-slug>/
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
- `productions/series-curriculum.md` — Master curriculum index across all series

## Version Control

- All source code, scripts, and documentation are committed to git
- Large binary artifacts (final.mp4, audio files) may be stored in git-lfs or archived separately
- The `.gitignore` file excludes temporary and generated files
- Episode directories are committed as complete units
