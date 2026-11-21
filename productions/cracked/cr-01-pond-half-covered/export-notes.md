# Export Notes — cr-01-pond-half-covered

**Date:** 2026-11-21  
**Editor:** automated assembly (Epic 4 / E4-I3)

## Assembly

**ffmpeg binary:** `imageio_ffmpeg` bundled binary — `ffmpeg-win-x86_64-v9.0.2.exe`  
(system ffmpeg not on PATH; `imageio_ffmpeg` package used as fallback)

**Scene files (in storyboard order):**
1. `scenes/PondHookScene.mp4` — Shot 1: hook
2. `scenes/ExponentialDeceptionScene.mp4` — Shot 2: motivation
3. `scenes/CountingDoublingsScene.mp4` — Shot 3: doubling table
4. `scenes/CoverageFormulaScene.mp4` — Shot 4: coverage formula
5. `scenes/LastFiveDaysTableScene.mp4` — Shot 5: Day 25–29 table
6. `scenes/OneStepBackScene.mp4` — Shot 6: one step back
7. `scenes/Day15PunchlineScene.mp4` — Shot 7: Day 15 punchline
8. `scenes/SplitScreenScene.mp4` — Shot 8: split-screen
9. `scenes/ResultStatementScene.mp4` — Shot 9: result
10. `scenes/WorkedExampleSetupScene.mp4` — Shot 10: worked example setup
11. `scenes/WorkedExampleDerivationScene.mp4` — Shot 11: worked example derivation
12. `scenes/RecapScene.mp4` — Shot 12: recap

**Audio beats:** `audio/beat_01.mp3` through `audio/beat_16.mp3` (16 beats, concatenated)

**Assembly method:** Video looped (`-stream_loop -1`) to match audio length, then muxed with `-shortest` taking audio (358.8 s) as the limiting stream.

> **Note on video/audio sync:** The scene renders (low-quality `-ql` via manimgx) total ~122 s of visual content; the narration audio is 358.8 s. For this pilot, the visual content loops to fill the audio duration. Full A/V sync requires the animator to set `self.wait()` durations per `timing.json` in the scene files — tracked as an Epic 7 polish item.

## Loudness

**Target:** -16 LUFS (YouTube standard), TP ≤ -1.5 dBFS  
**Measured input:** -20.59 LUFS, TP -1.13 dBFS, LRA 3.00  
**Normalization:** Two-pass `loudnorm` linear correction applied  
**Result:** Output normalized to approximately -16 LUFS

## Music Bed

**No music bed — pilot episode.**  
Decision: E4-I0 (2026-11-21) — `assets/music/` does not exist on this machine. Music is optional for the pilot. Tracked under E7-I4 for future resolution.

## Duration Gate

| Metric | Value |
|--------|-------|
| Measured duration | 00:05:58.80 (358.80 s) |
| Gate range | [240 s, 660 s] |
| **Result** | **PASS** |

## File

| File | Size |
|------|------|
| `final.mp4` | 6.7 MB |
| Bitrate | ~155 kb/s |
| Video codec | H.264 (copy from scene renders) |
| Audio codec | AAC, 24000 Hz, mono |
