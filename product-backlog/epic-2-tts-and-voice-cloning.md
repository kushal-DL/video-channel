# Epic 2: TTS and voice cloning

**Goal:** Establish a robust text-to-speech pipeline that produces consistent, high-quality narration audio for all episodes, with a pluggable backend architecture that allows switching between TTS providers and eventually using a cloned voice.

**Why this matters:** Narration is the backbone of tutorial videos. The voice must be clear, consistent, and engaging. A pluggable architecture ensures we can start with readily available TTS options and upgrade to a custom cloned voice when ready, without reworking the entire pipeline. The timing map generated here drives all animation durations, making it critical for sync.

**Estimated effort:** 3-5 days of build loop work

## Status

| Item | Story | Status |
|------|-------|--------|
| E2-I1 | Options evaluation spike (no vendor committed) | Not started |
| E2-I2 | Pluggable TTS adapter contract | Not started |
| E2-I3 | Per-beat audio and timing-map integration | Not started |

Status values: **Not started** (no work begun) · **In progress** (build loop running) · **Built** (implemented, awaiting nemesis verification) · **Done** (built and tested, nemesis verdict CLEAN).

## E2-I1: Options evaluation spike (no vendor committed)

- **Description:** Evaluate candidate TTS option families against fixed decision criteria and produce a comparison document only; this item installs no backend and adopts none as default.
- **Depends on:** none
- **Rationale:** Before committing to any TTS solution, we need to understand the tradeoffs between different approaches. This spike ensures an informed decision based on actual criteria relevant to our use case (quality, cost, local vs cloud, licensing, voice cloning capability).
- **Evaluation criteria:**
  - **Cloning quality:** How well can the option reproduce or clone a specific voice?
  - **Local runnability:** Can it run on our hardware without cloud dependency? What are the hardware requirements?
  - **Licensing:** Is it free for commercial use? What are the attribution requirements?
  - **Audio quality:** Naturalness, clarity, and consistency of output
  - **Latency:** Time to generate audio for a given text length
  - **Cost:** Per-minute or per-character pricing for cloud options
- **Option families to evaluate (minimum 3):**
  - Local open-source voice cloning models (e.g., Coqui TTS, OpenVoice, So-VITS-SVC)
  - Cloud TTS APIs (e.g., ElevenLabs, Amazon Polly, Google Cloud TTS, Azure TTS)
  - Locally runnable CLI tools (e.g., edge-tts, piper-tts)
- **Implementation notes:**
  - Research each option family's documentation and community feedback
  - Note specific model names, API endpoints, and pricing tiers
  - Identify any trial periods or free tiers for cloud options
  - Document hardware requirements for local options (RAM, GPU, disk space)
  - Do NOT install or configure any backend during this spike
  - Focus on gathering information, not implementation
- **Acceptance criteria:**
  - `productions/tts-options.md` is created with comprehensive evaluation
  - Document lists at least 3 option families with specific examples
  - Every family row is scored on exactly three criteria: cloning quality, local runnability (hardware requirements), licensing
  - Additional criteria (audio quality, latency, cost) are also evaluated
  - Document ends with a clear recommendation explicitly marked "pending user model download"
  - No `.claude/agents/*.md` files are modified during this spike
  - No TTS backend is installed or configured

## E2-I2: Pluggable TTS adapter contract

- **Description:** Define the single interface narration-engineer.md's workflow calls so the backend can be swapped when the user's voice-cloning model arrives; implement it against whichever family E2-I1 found locally runnable today, with a named error (never silent failure) for unconfigured backends.
- **Depends on:** E2-I1
- **Rationale:** A pluggable architecture decouples the narration workflow from the specific TTS implementation. This means when we eventually get a cloned voice model, we can swap it in without changing the rest of the pipeline. The adapter pattern provides a consistent interface regardless of backend.
- **Design principles:**
  - Single interface: `synthesize(text: str, output_path: str) -> AudioMetadata`
  - Backend selection via configuration or command-line flag
  - Named errors for all failure modes (not silent failures)
  - Clear documentation of which backends are supported
  - Graceful degradation when optional backends are unavailable
- **Implementation notes:**
  - Create `scripts/tts.py` as the main adapter script
  - Support at least one locally runnable backend from E2-I1 evaluation
  - Use argparse for command-line interface
  - Return structured metadata (duration, sample rate, channels)
  - Include comprehensive error handling with descriptive messages
  - Add `--help` documentation listing all supported backends
- **Acceptance criteria:**
  - `scripts/tts.py` exists and takes beat text and an output path as arguments
  - Running it produces a real audio file (mp3 or wav)
  - ffprobe duration of output is greater than 0
  - Test with fixture sentence: "The quadratic formula gives x equals negative b plus or minus the square root of b squared minus four ac, over two a."
  - Unconfigured backends exit non-zero with a named error message (not silent failure)
  - `scripts/tts.py --help` lists all supported backend names
  - Audio output is playable and contains intelligible speech
  - Script handles edge cases (empty text, special characters, long text)

## E2-I3: Per-beat audio and timing-map integration

- **Description:** Prove the full narration contract end-to-end on a fixture script independent of the pilot episode: one audio file per beat plus `timing.json` in exactly the schema narration-engineer.md specifies, which is what drives animation durations downstream.
- **Depends on:** E2-I2, E1-I4
- **Rationale:** This validates the complete narration pipeline from script to audio files to timing map. The timing map is critical because it drives animation durations — if the timing is wrong, the visuals won't sync with the narration. Testing with a fixture script (not the actual pilot) isolates the pipeline validation from creative content decisions.
- **Timing map schema (from narration-engineer.md):**
  ```json
  {
    "beats": [
      {
        "id": 1,
        "text": "Beat text here...",
        "audio_file": "audio/beat_01.mp3",
        "duration_sec": 3.5,
        "start_sec": 0.0,
        "end_sec": 3.5
      }
    ],
    "total_duration_sec": 15.2,
    "narration_speed_wpm": 150,
    "backend": "adapter-name",
    "generated_at": "2026-11-17T12:00:00Z"
  }
  ```
- **Implementation notes:**
  - Create fixture script `productions/tts-fixture/script-reviewed.md` with exactly 5 numbered beats
  - Each beat should be a realistic length (1-3 sentences)
  - Run the TTS adapter over all beats to generate audio files
  - Generate timing.json with accurate duration measurements
  - Use ffprobe to verify durations match actual audio files
  - Include verification script that checks all constraints
- **Acceptance criteria:**
  - Fixture `productions/tts-fixture/script-reviewed.md` has exactly 5 numbered beats
  - Running the adapter over all beats produces `audio/beat_01.mp3` through `audio/beat_05.mp3`
  - Generated `timing.json` has keys: `beats`, `total_duration_sec`, `narration_speed_wpm`
  - Each beat in timing.json has: `id`, `text`, `audio_file`, `duration_sec`, `start_sec`, `end_sec`
  - Verification run asserts: beat count == audio file count == 5
  - Each `duration_sec` equals the ffprobe duration within 0.05 seconds tolerance
  - `total_duration_sec` equals the sum of beat durations within 0.1 seconds tolerance
  - All audio files are non-empty and playable
  - Timing map is valid JSON and parseable

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Local TTS quality is poor | Evaluate multiple options in E2-I1; have cloud fallback |
| Voice cloning model requires expensive hardware | Document requirements clearly; consider cloud GPU options |
| Timing map accuracy issues | Use ffprobe for precise measurements; add tolerance in verification |
| Backend API changes break adapter | Pin versions; write integration tests |
| Audio file format incompatibilities | Standardize on mp3 or wav throughout pipeline |

## Success criteria for epic completion

All three stories are marked **Done** with nemesis verdict CLEAN. The TTS pipeline produces consistent, high-quality audio with accurate timing maps. The pluggable architecture is in place, documented, and tested. The system is ready to swap in a cloned voice model when available without pipeline changes.
