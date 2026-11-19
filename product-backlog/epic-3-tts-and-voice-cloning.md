# Epic 2: TTS and Voice Cloning

**Goal:** Implement a production-ready text-to-speech pipeline that generates narration audio from scripts, extracts beat markers for scene transitions, and supports voice cloning for brand consistency.

**Why this matters:** Narration is the backbone of every episode. Without reliable TTS integration, the narration-engineer agent cannot generate timing maps or sync visuals to audio. Voice cloning adds production value and brand recognition.

**Estimated effort:** 2-3 days of build loop work

## Status

| Item | Story | Status |
|------|-------|--------|
| E2-I1 | Evaluate TTS options (ElevenLabs vs local) | Not started |
| E2-I2 | Generate narration pipeline script | Not started |
| E2-I3 | Implement beat extraction from audio | Not started |

Status values: **Not started** (no work begun) · **In progress** (build loop running) · **Built** (implemented, awaiting nemesis verification) · **Done** (built and tested, nemesis verdict CLEAN).

## E2-I1: Evaluate TTS Options

- **Description:** Compare ElevenLabs API vs local models (Coqui/Tortoise) for production use.
- **Depends on:** none
- **Rationale:** ElevenLabs offers studio-quality voices but costs money and requires API keys. Local models are free but slower and lower quality. Need a decision matrix with cost, latency, quality, and reliability metrics.
- **Implementation notes:**
  - Test ElevenLabs with sample script (100 words) — measure generation time, audio quality, prosody
  - Install Coqui TTS locally if not present: `pip install coqui-tts`
  - Compare output on same text; record subjective and objective metrics
- **Acceptance criteria:**
  - Decision document written in `docs/tts-decision.md`
  - ElevenLabs API key stored securely (`.env`) with fallback to local model
  - Cost estimate per minute of narration calculated and documented

## E2-I2: Generate Narration Pipeline Script

- **Description:** Create a Python script that converts a script file into TTS audio + timing.json.
- **Depends on:** E2-I1
- **Rationale:** The screenwriter outputs `script.md`; the narration-engineer needs an automated pipeline to generate audio and extract beat-level durations for animation pacing.
- **Implementation notes:**
  - Parse script beats from numbered headers (`## Beat N:`)
  - Generate TTS per-beat or full-script depending on length
  - Output `.mp3` files named `beat_N.mp3` plus combined narration
  - Write `timing.json` with structure: `{ "beats": [{"id": 1, "text": "...", "duration_ms": 4500}] }`
- **Acceptance criteria:**
  - Script at `scripts/generate_narration.py`
  - Runs against a test script and produces valid audio files + timing.json
  - Handles UTF-8 characters (math symbols, accents) correctly

## E2-I3: Implement Beat Extraction from Audio

- **Description:** Extract beat markers from narration audio for scene transition synchronization.
- **Depends on:** E2-I2
- **Rationale:** Editors need precise audio cues to cut between scenes at meaningful moments in the narration, not arbitrary timestamps.
- **Implementation notes:**
  - Use librosa or pydub to detect silence gaps and phrase boundaries
  - Map beat numbers from timing.json to corresponding audio segments
  - Output metadata for editor's DAW (Avid Media Composer, Premiere Pro)
- **Acceptance criteria:**
  - Beat extraction script at `scripts/extract_beats.py`
  - Produces `.meta` files compatible with standard video editing workflows

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| TTS latency too high for production pipeline | Use ElevenLabs streaming API or batch processing |
| Voice cloning requires large dataset | Start with ElevenLabs voice library; clone only after 10+ episodes |
| UTF-8 encoding issues with math symbols | Test with full LaTeX character set early in E2-I2 |

## Success Criteria for Epic Completion

All three stories marked **Done** with nemesis verdict CLEAN. The TTS pipeline is fully integrated into the production workflow, and editors have precise beat markers to sync scenes to narration.
