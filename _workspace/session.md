# Session Context — Video-Channel

> Rolling context file for Claude. Read this first at the start of a session to recover prior state.
> Update it at the end of meaningful work: what changed, what's done, what's next.

**Last updated:** 2026-11-21 (Script quality overhaul — anti-pattern rules added, screenwriter respawned)

---

## Project in one line

Automated production of TED-Ed / 3Blue1Brown style math-tutorial videos (4–11 min, one concept + one worked example) using manimgx animation, driven by a team of Claude agents on a local Qwen 3.8 27B model.

## Current repo state (verified 2026-11-21)

- **Epic 1 (Environment)** — Done.
- **Epic 2 (Agent definitions + channel bible)** — Done (TED-Ed style upgrade). **Updated again 2026-11-21** — added anti-pattern rules, worked example constraint, character-grounded hook guidance to channel-bible.md and screenwriter.md.
- **Epic 3 (TTS)** — Done (2026-11-20). edge-tts 7.3.1, en-US-AriaNeural.
- **Epic 4 (Re-render Episode 1)** — IN PROGRESS. Status below.
- **Epic 5–7** — Not started.

## Epic 4 actual status (BACKLOG is stale — not updated yet)

cr-01-pond-half-covered pipeline state:

| Artifact | Status | Notes |
|----------|--------|-------|
| scope.md | Done | |
| brief.md | **Updated 2026-11-21** | New hook (scientist character) + worked example (bacteria petri dish) |
| script.md | **IN REWRITE** | Screenwriter agent spawned 2026-11-21; old script rejected for AI-slop patterns |
| script-reviewed.md | Stale — will need re-review | Math claims same but context changes; math-reviewer must re-verify |
| storyboard.md | Stale — needs rewrite after new script | Current storyboard is based on old abstract script; needs character scenes |
| audio/ (beat_01–16.mp3) | Stale — regenerate after new script | Based on old script |
| timing.json | Stale | Will be regenerated |
| scenes/ (12 MP4s) | Stale — will need re-render | Based on old storyboard |
| final.mp4 | Stale — pilot only | 358.8s but video loops 3× (122s visual / 358.8s audio) — A/V sync broken |
| signoffs.md | Director signed pilot assembly only | |

**Two blockers before E4-I3 can close:**
1. New script → math review → storyboard → new scenes → new narration → new assembly
2. A/V sync: scenes need self.wait() holds added to match timing.json (scenes too short, video looped)

## What was done this session (2026-11-21)

### Script quality overhaul

User reviewed final.mp4 and identified critical quality problems:
- Video loops 3× (visual content 122s, narration 358.8s — A/V sync broken)
- Script was "AI slop" — classic AI voice patterns throughout
- Story not rich enough — no character, no concrete grounding

**Specific AI tells found in old script:**
- Announce-then-do openers: "Here is the key insight.", "Let us count...", "Now look at...", "Now check..."
- Uniform sentence rhythm (all sentences 15–25 words, metronomic)
- Weak worked example: "same lily pad problem but 20 days instead of 30" = parameter tweak, not new context

**Three files updated (Fast Path):**
1. `productions/channel-bible.md` — added "Narrative craft — writing anti-patterns", "Worked example rule", "Character-grounded hooks (Cracked series preferred)"
2. `.claude/agents/screenwriter.md` — added anti-pattern enforcement section, sentence rhythm guidance, worked example constraint (new context required), self-check list, character-grounded hook guidance
3. `productions/cracked/cr-01-pond-half-covered/brief.md` — Section 6 (Hook) rewritten to scientist-at-pond character hook; Section 8 (Handoff Notes) updated with bacteria petri dish as worked example direction

**Screenwriter agent spawned** to rewrite script.md with:
- Scientist/ecologist walking past pond daily (Day 1 → Day 30)
- Riddle emerges from her observation, not abstract hypothetical
- Worked example: bacteria in petri dish doubling every hour (dish full at noon → half full at 11am)
- Target: 700–750 words, all anti-patterns removed

## Next planned steps (after new script arrives)

1. Math reviewer re-verifies new script (same math claims, new context)
2. Storyboard artist rewrites storyboard with character scenes (scientist, pond, lab, petri dish)
3. Narration engineer regenerates all 16 audio beats
4. Animator re-renders all 12 scenes WITH self.wait() holds matching timing.json
5. Editor re-assembles final.mp4 (this time no looping needed — visual duration ≈ audio duration)
6. QC reviewer + nemesis sign-off
7. Update BACKLOG E4-I1, E4-I2, E4-I3 to Done

## A/V sync fix plan (for Animator re-render)

Each scene needs `self.wait(X)` added before the final FadeOut/wipe, where:
- X = total_beat_duration_for_this_scene - current_animation_duration
- Beat durations are in timing.json (will regenerate after new script/audio)

Scene-beat mapping:
- Scene 1 (Beats 1-2), Scene 2 (Beats 3-4), Scene 3 (Beat 5), Scene 4 (Beat 6),
  Scene 5 (Beat 7), Scene 6 (Beat 8), Scene 7 (Beat 9), Scene 8 (Beat 10),
  Scene 9 (Beat 11), Scene 10 (Beat 12), Scene 11 (Beats 13-14), Scene 12 (Beats 15-16)

Pattern in scene files: add `self.wait(X)` immediately before the final `self.play(FadeOut(...))` call.

## Key constraints to remember

- Local model = Qwen 3.8 27B via `anthropic--claude-sonnet-latest`; 9B tier = `anthropic--claude-haiku-latest`.
- Web tools (WebSearch/WebFetch) disabled through the local proxy.
- manimgx ≈ Manim Community Edition API. No 3D (unwanted), no character/illustration art.
- Follow `REPO_STRUCTURE.md` for all artifact placement.
- Cracked series hook: character-grounded, not abstract hypothetical. Scientist/ecologist character preferred.
