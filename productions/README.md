# Productions Directory Layout

Canonical reference for all artifact paths used by Video-channel agents.

## Episode Slug Convention

Each episode lives under a unique slug directory:

```
productions/<slug>/
```

**Slug format:** `<topic>-<date>-<version>`  
Examples: `complex-numbers-20261117-v1`, `linear-algebra-intro-20261118-v1`

---

## Directory Tree Structure

```
productions/
├── README.md                          # This file (canonical layout)
├── channel-bible.md                   # Series-wide brand & visual standards
├── backlog.md                         # Living series roadmap
└── <slug>/                            # Per-episode directory
    ├── brief.md                       # Producer: episode concept + goals
    ├── script.md                      # Screenwriter: numbered beats, [MR] tags
    ├── script-reviewed.md             # Math-reviewer: corrected script + notes
    ├── storyboard.md                  # Storyboardist: shots + transitions
    ├── continuity.md                  # Director: recurring motifs/notation register
    ├── scenes/                        # Animator: one .py file per shot
    │   ├── scene_01.py
    │   ├── scene_02.py
    │   └── ...
    ├── render-notes.md                # Animator: deviations + rationale
    ├── audio/                         # Narration-engineer: TTS output
    │   ├── beat_01.mp3
    │   ├── beat_02.mp3
    │   └── ...
    ├── timing.json                    # Narration-engineer: beat durations + metadata
    ├── signoffs.md                    # Director: approval notes per artifact
    ├── final.mp4                      # Editor: master export (final deliverable)
    └── export-notes.md                # Editor: bitrate, loudness, chapters
```

---

## Artifact Ownership & Descriptions

| Path | Owner Agent | Description |
|------|-------------|-------------|
| `channel-bible.md` | Producer | Master brand voice, visual standards, notation conventions for the entire series. |
| `backlog.md` | Producer | Living roadmap of upcoming episodes and production status. |
| `<slug>/brief.md` | Producer | Episode concept, learning objectives, target audience notes. |
| `<slug>/script.md` | Screenwriter | Numbered beats with `[MR]` tags marking all math claims requiring review. |
| `<slug>/script-reviewed.md` | Math-reviewer | Corrected script + detailed notes on each [MR] tag resolution. |
| `<slug>/storyboard.md` | Storyboardist | Discrete shots, in/out states, transition specs, continuity notes. |
| `<slug>/continuity.md` | Director | Living document tracking recurring motifs, notation choices, established metaphors. |
| `<slug>/scenes/*.py` | Animator | One `Scene` class per shot; manimgx renderable code implementing storyboard shots. |
| `<slug>/render-notes.md` | Animator | Deviations from storyboard + technical rationale (e.g., merged cuts for pacing). |
| `<slug>/audio/beat_*.mp3` | Narration-engineer | TTS audio per script beat; separate files enable precise timing control. |
| `<slug>/timing.json` | Narration-engineer | Beat-level durations, start times, metadata for sync with video. |
| `<slug>/signoffs.md` | Director | Approval notes appended to each artifact or consolidated here. Never approve silently. |
| `<slug>/final.mp4` | Editor | Single master export; the canonical deliverable for this episode. |
| `<slug>/export-notes.md` | Editor | Technical metadata: bitrate, loudness target achieved, chapter list if any. |

---

## Literal Path Verification (Agent File Cross-Reference)

All paths below are literal matches found in agent documentation files under `.claude/agents/`:

### Producer
- `productions/channel-bible.md` — cited in producer.md:32, director.md:16
- `productions/backlog.md` — cited in producer.md:33
- `productions/<slug>/brief.md` — cited in producer.md:19, screenwriter.md:30

### Screenwriter
- `productions/<slug>/script.md` — output path (screenwriter.md:35)
- Input: `productions/<slug>/brief.md` + channel bible (screenwriter.md:30)

### Math-reviewer
- `productions/<slug>/script-reviewed.md` — input/output path (math-reviewer.md:27, 31)
- Input: `productions/<slug>/script.md` + brief for context (math-reviewer.md:26)

### Storyboardist
- `productions/<slug>/storyboard.md` — output path (storyboard.md:30, 34)
- Input: `productions/<slug>/script-reviewed.md` + brief + channel bible (storyboard.md:29)
- References continuity register at `productions/<slug>/continuity.md` (storyboard.md:26)

### Director
- `productions/<slug>/continuity.md` — per episode living document (director.md:12, 32)
- `productions/channel-bible.md` — series-wide style reference (director.md:16)
- Sign-off notes in artifact or `productions/<slug>/signoffs.md` (director.md:20, 33)

### Animator
- `productions/<slug>/scenes/*.py` — one file per shot (animator.md:50)
- Input: storyboard at `productions/<slug>/storyboard.md` + channel bible (animator.md:45)
- Output render notes at `productions/<slug>/render-notes.md` (animator.md:46, 51)

### Narration-engineer
- `productions/<slug>/audio/beat_*.mp3` — TTS per beat (narration-engineer.md:13, 48)
- `productions/<slug>/timing.json` — beat durations + metadata (narration-engineer.md:27, 49)
- Input: `productions/<slug>/script-reviewed.md` + channel bible (narration-engineer.md:43)

### Editor
- `productions/<slug>/final.mp4` — master export (editor.md:27, 31)
- `productions/<slug>/export-notes.md` — bitrate/loudness/chapters (editor.md:27, 32)

---

## Build & Render Commands (Reference)

### Rendering a scene file:
```bash
.venv/bin/manimgx render productions/<slug>/scenes/scene_01.py MyScene --crf 50 -o /tmp/output.mp4
```

### Full episode assembly (ffmpeg required):
```bash
# Concatenate audio beats with timing.json metadata, then merge with video renders
# ffmpeg command goes here once installed system-wide.
```

---

## Notes for Agents

1. **Never hardcode absolute paths** — always use relative paths from `productions/` root or episode slug directory.
2. **Slug directories are isolated** — each episode is self-contained; no cross-episode dependencies in file paths.
3. **Continuity.md is living** — update it incrementally as motifs and notation choices emerge.
4. **Signoffs must be explicit** — director never approves silently; append notes to artifacts or `signoffs.md`.
