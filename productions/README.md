# Video-Channel Productions Layout

**Purpose:** Single source of truth for artifact paths across all production agents.  
**Slug convention:** `productions/<episode-slug>/` where `<slug>` is descriptive and unique (e.g., `episode-001-introduction-to-calculus`).

---

## Canonical Per-Episode Tree Structure

```
productions/
├── <episode-slug>/
│   ├── brief.md                    # Producer: 1-2 paragraph episode concept, learning objective
│   ├── script.md                   # Screenwriter: Full narration script with timing notes
│   ├── script-reviewed.md          # Math-reviewer: Script after formula verification
│   ├── storyboard.md               # Storyboardist: Shot list with transitions and camera moves
│   ├── continuity.md              # Director: Continuity register (objects, colors, positions)
│   │
│   ├── scenes/                     # Animator: manimgx Python scene files
│   │   └── <episode>_scenes.py     # All scenes for this episode in one file
│   │
│   ├── audio/                      # Narration-engineer & Editor
│   │   ├── narration.mp3           # Full episode voiceover (mono, 48kHz)
│   │   ├── beat_01.mp3             # Beat markers for scene transitions
│   │   └── background_music.mp3    # Optional ambient track (low volume)
│   │
│   ├── timing.json                 # Narration-engineer: Line-by-line duration map synced to audio
│   │
│   ├── signoffs.md                # Director: Approval checklist before render
│   │
│   ├── qc-report.md               # QC-reviewer: Frame extraction, A/V sync check results
│   │
│   ├── release.md                 # Release-agent: Metadata for YouTube (title, description, chapters)
│   │
│   └── final.mp4                  # Editor: Final muxed video with narration + music bed
```

---

## Artifact Descriptions & Ownership

| File | Agent | Description |
|------|-------|-------------|
| `brief.md` | Producer | Episode concept, target audience, learning objective (1-2 paragraphs max) |
| `script.md` | Screenwriter | Full narration script with pedagogical structure; TTS-friendly sentences; math-claim tagged |
| `script-reviewed.md` | Math-reviewer | Script after adversarial verification of all formulas and derivations |
| `storyboard.md` | Storyboardist | Shot list: each visual segment, transitions (cut/cross-dissolve), camera moves |
| `continuity.md` | Director | Continuity register tracking objects, colors, positions across shots to prevent errors |
| `scenes/*.py` | Animator | manimgx Python scenes; one file per episode for organization |
| `audio/narration.mp3` | Narration-engineer | Full TTS voiceover rendered at 48kHz mono |
| `audio/beat_*.mp3` | Editor | Short audio markers for scene transitions (used during final assembly) |
| `timing.json` | Narration-engineer | Line-by-line duration map synced to narration; drives animation pacing |
| `signoffs.md` | Director | Approval checklist confirming script, math, storyboard are locked before render |
| `qc-report.md` | QC-reviewer | Punch list of any issues found during frame extraction and A/V sync verification |
| `release.md` | Release-agent | YouTube metadata: title, description, chapter timestamps from timing.json |
| `final.mp4` | Editor | Final muxed video with narration + music bed; loudness normalized to -16 LUFS |

---

## Per-Episode Slug Naming Convention

- **Format:** `<episode-number>-<topic-description>` (kebab-case)
- **Examples:**
  - `productions/episode-001-introduction-to-calculus/`
  - `productions/episode-002-the-chain-rule-explained/`
  - `productions/episode-003-limits-and-continuity/`

---

## Cross-Agent Path References

This layout is assumed by the following agents (see `.claude/agents/*.md` for details):

| Agent | Uses these paths |
|-------|------------------|
| Producer | `productions/<slug>/brief.md`, `signoffs.md` |
| Screenwriter | `productions/<slug>/script.md` |
| Math-reviewer | `productions/<slug>/script-reviewed.md` |
| Storyboardist | `productions/<slug>/storyboard.md`, `continuity.md` |
| Animator | `productions/<slug>/scenes/*.py` |
| Narration-engineer | `productions/<slug>/audio/narration.mp3`, `timing.json` |
| Editor | All audio files, `final.mp4` output |
| QC-reviewer | `productions/<slug>/qc-report.md`, frame extraction outputs |
| Release-agent | `productions/<slug>/release.md`, chapter timestamps from `timing.json` |

---

## Verification Checklist

- [ ] Every cited path appears as a literal string in at least one `.claude/agents/*.md` file
- [ ] Each artifact has a clear owner (agent) and description
- [ ] Slug naming is consistent across all episodes
- [ ] Directory structure matches this document exactly
