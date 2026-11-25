# Render Notes — cr-01-pond-half-covered

**Animator:** fork (anthropic--claude-sonnet-latest)
**Date:** 2026-11-21
**Render resolution:** 854×480, 15 fps, preset ultrafast (pilot quality)

## Render results

| Scene | Class | MP4 duration | Status | Notes |
|-------|-------|-------------|--------|-------|
| scene_01.py | PondHookScene | 13.5 s | PASS | Layout: Cross intentionally overlaps "Day 15?" text |
| scene_02.py | ExponentialDeceptionScene | 10.3 s | PASS | Layout: tiny axis labels (font_size=16) flagged small — readable at 480p |
| scene_03.py | CountingDoublingsScene | 11.3 s | PASS | Layout: ellipsis character flagged small (cosmetic) |
| scene_04.py | CoverageFormulaScene | 8.1 s | PASS | No layout issues |
| scene_05.py | LastFiveDaysTableScene | — | PASS | Layout: highlight box edge through fraction text — intentional overlap |
| scene_06.py | Day15PunchlineScene | 7.3 s | PASS | Layout: Day 29 highlight box edge — intentional |
| scene_07.py | OneStepBackScene | 6.3 s | PASS | No layout issues |
| scene_08.py | SplitScreenScene | 10.6 s | PASS (after fix) | Bug fixed: Unicode arrows → removed, replaced with ASCII text |
| scene_09.py | ResultStatementScene | 8.3 s | PASS | No layout issues |
| scene_10.py | WorkedExampleSetupScene | 7.3 s | PASS | No layout issues |
| scene_11.py | WorkedExampleDerivationScene | 16.6 s | PASS | No layout issues |
| scene_12.py | RecapScene | — | PASS | Layout: "Day 29" text intentionally centered over pond |

**All 12 scenes rendered. Total pilot render time: ~72 s.**

## Substitutions from storyboard spec

1. **Shots 1, 7, 9, 10, 11, 12 — pond fill:** manimgx does not have a native partially-filled circle primitive. Substituted a `Rectangle` fill overlay behind a `Circle` outline. The fill bar simulates coverage fraction. `[ANIMATOR-CAPABILITY: partial circle fill → rectangle fill overlay]`

2. **Shot 2 — fill bars (Scene 2):** Used `ValueTracker` + `always_redraw` on `Rectangle` height for both linear and exponential bars simultaneously. Standard pattern — works as specified.

3. **Shot 11 — Transform chain:** Pre-built all three equation states (`eq_generic`, `eq_half`, `eq_quarter`) before the first `Transform` call per storyboard note — no glitches.

## Bug fixed during render

- **scene_08.py:** `Text("Day 15 →", ...)` and `Text("← Day 29", ...)` caused `UnicodeEncodeError` on Windows CP1252 (the `→`/`←` characters). Removed the arrows; labels now read "Day 15" and "Day 29". Visual intent preserved.

## Render command used

```bash
python -m manimgx render <file>.py <ClassName> --resolution 854x480 --fps 15 --preset ultrafast
```

Note: `manimgx` CLI is installed in the Windows user scripts directory but not on PATH in Git Bash. Used `python -m manimgx` instead.

## Flags for editor

- All 12 MP4 files are in `productions/cracked/cr-01-pond-half-covered/scenes/`
- Narration audio files are expected at `productions/cracked/cr-01-pond-half-covered/audio/beat_*.mp3`
- `timing.json` drives A/V sync
- Concatenate in order: scene_01 through scene_12
- No music bed (pilot — per E4-I0 decision; note in export-notes.md)
