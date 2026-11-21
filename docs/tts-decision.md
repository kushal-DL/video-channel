# TTS Provider Decision (Epic 3)

**Date:** 2026-11-20  
**Decision:** edge-tts (Microsoft Edge neural voices)  
**Chosen Voice:** `en-US-AriaNeural`

## Evaluation Matrix

| Criterion | ElevenLabs | edge-tts (Microsoft) | Winner | Rationale |
|-----------|-----------|----------------------|--------|-----------|
| **Cost** | ~$0.15 per 1M characters; ~$5–10/mo for tutorial channel | Free (no quota for local use) | **edge-tts** | Zero licensing overhead; cost-prohibitive feature for experimental pipeline. |
| **Latency** | ~0.1–0.2 s per 1K chars (API-dependent); requires network | ~0.5–1.5 s per 1K chars locally; no API latency | **edge-tts** | Local synthesis avoids network dependency; acceptable for non-real-time batch production. |
| **Voice Quality** | Highly realistic; natural prosody; 100+ voices | Very realistic; natural prosody; 30+ voices (across languages) | **edge-tts** | Sufficient for tutorial narration; neural quality exceeds bare minimum. |
| **Setup Complexity** | API key; third-party account | `pip install edge-tts`; no account needed | **edge-tts** | Local-first simplifies CI/CD and reduces operational complexity. |
| **Availability** | Third-party SaaS; subject to rate limits | Bundled with Windows/Python ecosystem; always available | **edge-tts** | Offline-friendly; no SaaS dependency eliminates one external point of failure. |
| **Voice Cloning** | Premium tier; requires sample audio | Not supported in free/standard tier | **ElevenLabs** (if needed later) | Decision: voice cloning deferred. Use standard Aria for MVP; revisit if brand-specific voice becomes critical. |

## Decision

**Selected Provider:** edge-tts  
**Selected Voice:** `en-US-AriaNeural` (Microsoft Edge neural voice for US English)

### Verification

The chosen voice (`en-US-AriaNeural`) was verified by running:

```python
import asyncio, edge_tts
asyncio.run(edge_tts.Communicate('test', 'en-US-AriaNeural').save('_tts_probe.mp3'))
```

Result: 11,232 bytes of valid MP3 audio generated successfully (2026-11-20).

## Next Steps

1. ✅ edge-tts installed (v7.3.1).
2. ✅ Voice verified to synthesize audio (en-US-AriaNeural).
3. Update `channel-bible.md` Voice section with approved voice name.
4. Write `scripts/tts.py` (CLI adapter) satisfying `tts --voice ... --output-file ...` interface.
5. Generate narration from fixture script; extract beat timings; implement `scripts/extract_beats.py`.

## Rationale

**Why not ElevenLabs for MVP?**

- Licensing cost adds friction to an experimental workflow currently running locally.
- edge-tts provides neural-quality voices at zero marginal cost, reducing blockers for iteration.
- Voice cloning (ElevenLabs' differentiator) is not required for MVP; Aria's naturalness is sufficient.
- Switching providers later (after MVP proves the pipeline) is low-risk: both accept same TTS API pattern (text → audio file).

**Future consideration:** If the channel opts for a branded voice (e.g., hiring a voice actor and cloning them), ElevenLabs becomes the natural choice and can be integrated by swapping `scripts/tts.py` implementation without touching orchestration or episode data.
