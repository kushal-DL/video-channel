# Session Context — Video-Channel

> Rolling context file for Claude. Read this first at the start of a session to recover prior state.
> Update it at the end of meaningful work: what changed, what's done, what's next.

**Last updated:** 2026-11-22 (Epic 4 re-render of cr-01-pond-half-covered — stages 1–4 DONE; stopped before assembly. Stages 5–7 remain.)

---

## Project in one line

Automated production of TED-Ed / 3Blue1Brown style math-tutorial videos (2.5–11 min, one concept + one worked example) using manimgx animation, driven by a team of Claude agents on a local Qwen 3.8 27B model.

## Current repo state (verified 2026-11-22)

- **Epic 1 (Environment)** — Done.
- **Epic 2 (Agent definitions + channel bible)** — Done (TED-Ed style upgrade).
- **Epic 3 (TTS)** — Done (2026-11-20). edge-tts 7.3.1, en-US-AriaNeural.
- **Epic 4 (Re-render Episode 1: cr-01-pond-half-covered)** — IN PROGRESS. Stages 1–4 done; assembly + QC + close-out remain. Status below.
- **Epic 5–7** — Not started.

## Epic 4 pipeline state (cr-01-pond-half-covered)

| Stage | Artifact | Status | Notes |
|-------|----------|--------|-------|
| Scope/Brief/Script | scope.md, brief.md, script.md | **Done** | 705 words / 8 beats / 13 [MR] tags; anti-slop gates PASS |
| 1. Math review | script-reviewed.md, gates/math-review.json | **Done** | All 13 claims re-derived by hand; C9 correction (Beat 7 "one eighth"); no scope/brief touched |
| 2. Storyboard | storyboard.md, continuity.md | **Done** | Shot-by-shot, concrete↔abstract pairs per shot; palette #0F172A/#F2E3C6/#F97316/#3B82F6; scientist consistent across pond+lab |
| 3. Narration | audio/beat_01–08.mp3, timing.json, script-performance.md | **Done** | en-US-AriaNeural; total **215.3 s** (gate [150,660] PASS); 149.9 wpm; ffprobe-measured |
| 4. Scenes | scenes/scene_01–12.py + scene_07b.py (13 files), 13 MP4s, render-notes.md | **Done** | All frame-checked vs storyboard; 2 defects fixed+re-rendered (S2 Day-30 label, S10 garbled MathTex); tail-hold pattern in place |
| 5. Assembly | final.mp4, export-notes.md | **NOT STARTED** | ← NEXT |
| 6. QC | qc-report.md | **NOT STARTED** | |
| 7. Sign-off/close-out | signoffs.md (final), BACKLOG E4-I1/I2/I3 → Done | **NOT STARTED** | |

### A/V sync — the #1 defect from the failed pilot, now handled at scene level

The old pilot looped video 3× because scenes were shorter than their beats. This run fixes it structurally:
- Every scene ends with a tail-hold `self.wait(tail_hold)` where `tail_hold = max(0.5, SCENE_TARGET_SEC - animation_duration)`. The hold is the final action in `construct()`, so trimming it changes only still-frame length — no re-animation needed to shorten a scene.
- **Total rendered video ≈ 308.8 s vs 215.3 s of narration.** The ~93 s difference is tail-hold padding (scenes padded to placeholder targets). The Editor trims/aligns each scene's effective duration to its beat(s) from `timing.json` so final visual duration matches audio within ~1 s. **No looping allowed.**
- Beat → audio durations (from timing.json): B1=33.72, B2=28.51, B3=29.30, B4=30.55, B5=23.50, B6=15.05, B7=29.64, B8=25.03 s.

### Scene → beat mapping (for the Editor)

| Scene file | Class | Beats covered | Rendered dur |
|-----------|-------|---------------|:---:|
| scene_01.py | Shot01HookWalk | Beat 1 part 1 (Days 1–15) | 20.04 s |
| scene_02.py | Shot02HookClimax | Beat 1 part 2 (Day 30 + riddle) | 15.25 s |
| scene_03.py | Shot03Motivation | Beat 2 (full) | 29.67 s |
| scene_04.py | Shot04SplitScreen | Beat 3 (full) | 36.46 s |
| scene_05.py | Shot05Formula | Beat 4 part 1 (formula intro) | 20.46 s |
| scene_06.py | Shot06Day15Table | Beat 4 part 2 (plug-in + table) | 16.38 s |
| scene_07.py | Shot07OneStepBack | Beat 5 (full) | 30.67 s |
| scene_07b.py | Shot07bResult | Beat 6 (result card — dedicated shot, Director option b) | 19.54 s |
| scene_08.py | Shot08LabSetup | Beat 7 part 1 (lab setup) | 21.25 s |
| scene_09.py | Shot09LabQuestion | Beat 7 part 2 (question + rule) | 14.54 s |
| scene_10.py | Shot10LabEighth | Beat 7 part 3 (one eighth) | 19.04 s |
| scene_11.py | Shot11Recap | Beat 8 part 1 (law + strip) | 25.04 s |
| scene_12.py | Shot12PayoffClose | Beat 8 part 2 (Day-30 close) | 20.92 s |

Note: Beats are split across scenes (Beat 1 → S1+S2; Beat 4 → S5+S6; Beat 7 → S8+S9+S10; Beat 8 → S11+S12). The Editor must sum the per-scene durations within a beat and align to that beat's audio duration.

## What was done this session (2026-11-22) — stages 1–4

### Stage 1 — Math review (math-reviewer agent): PASS
Re-derived all 13 [MR] claims by hand before accepting any. Priority checks confirmed: Day 29 = half; Day 15 ≈ 0.003%; petri dish full at noon → half at 11am; 6am = 1/2^6 < 2%. Wrote `script-reviewed.md` (corrected script) + `gates/math-review.json`. **C9 correction:** Beat 7 worked-example wording fixed to "one eighth" (this is the version TTS used). No scope/brief touched.

### Stage 2 — Storyboard (storyboard-artist agent): PASS
Shot-by-shot `storyboard.md` from script-reviewed.md per brief §5: split-screen linear-vs-exponential in hook shots, coverage table in build-up, "one step back" reversal animation, scientist + petri dish in worked example. Every shot names its concrete_visual ↔ abstract_symbol pair (channel bible rule). `continuity.md` updated: scientist figure consistent between pond and lab scenes; palette #0F172A / #F2E3C6 / #F97316 / #3B82F6; act boundaries marked.

### Stage 3 — Narration (narration-engineer agent): PASS
`audio/beat_01–08.mp3` via scripts/tts.py (en-US-AriaNeural), `timing.json` ffprobe-measured, total **215.3 s** within [150, 660]. 149.9 wpm (~150 target).
- **Deviation:** voice-director subagent failed twice → narration-engineer authored `script-performance.md` itself in the specified format (flagged in its header). Non-blocking.
- **Known limitation (non-blocking):** edge-tts via scripts/tts.py takes plain text only — no rate/SSML, so the intended −10% slow-down for Beat 7 couldn't be applied at synthesis time. If a slower worked-example delivery is wanted later: add a `rate` param to scripts/tts.py (build-protocol task) or post-process.

### Stage 4 — Scenes (animator agent): PASS
All 13 scene files + 13 MP4s rendered and frame-checked against storyboard.md. Background #0F172A confirmed on all 13 (no black frames). Math renders cleanly. **Two real defects found & fixed + re-rendered:**
1. Shot 02 — Day-30 counter label missing (Transform left target invisible) → replaced with FadeIn/FadeOut + fresh `Write(day30_txt)`.
2. Shot 10 — garbled MathTex `\mathrm{am}` tag (raw-string double backslash injected a line break) → fixed to single-backslash space; now reads "11 am → 50%".

`render-notes.md` written: per-scene table, shared-scientist-figure refactor recommendation (extract `make_scientist`/`make_pond`/`make_pad` into `scenes/shared_figures.py` — flagged for future cleanup, not done), deviations + rationale, tail-hold pattern explanation.

**Director sign-offs recorded in signoffs.md:** storyboard v1.0 approved; narration locked verbatim to script-reviewed.md Part A. Three Director flags resolved:
- **D1 (Beat 6 boundary):** ADD dedicated result shot `scene_07b.py` for Beat 6 (halved pond + "Day 29 = 50%" card) — de-risks A/V sync by giving every beat its own hold frame. Scene count → 13.
- **D2 (Shot 7 20-day pond):** generalization stays visual-light, must not outstage the Day-30→Day-29 reversal.
- **D3 (Shot 4 naming):** S4 stays free of on-screen linear/exponential words; no label delay.

## REMAINING WORK — stages 5–7 (next session picks up here)

### Stage 5 — ASSEMBLY (editor agent) ← NEXT ACTION
Mux the 13 scenes + narration + music bed, normalize loudness, chapter markers from timing.json. Export `final.mp4` + `export-notes.md`.
- **No video looping allowed:** final visual duration must match audio (215.3 s) within ~1 s.
- Trim/align each scene's tail-hold so per-beat visual duration matches that beat's audio duration from timing.json (see mapping table above). Because holds are plain `self.wait()` at the end, trimming is safe — no re-animation.
- Beat 6 rides its dedicated Shot07bResult; do NOT let it ride Shot07OneStepBack's tail (Director D1 decision).

### Stage 6 — QC (qc-reviewer agent)
Extract frames, check A/V sync vs timing.json, on-screen math vs script-reviewed.md, readability/contrast, transition smoothness. Write `qc-report.md` with severity-ranked punch list. Loop back to animator/narration-engineer/editor until clean.

### Stage 7 — SIGN-OFF & CLOSE-OUT
- Director sign-off in `signoffs.md` for each handoff (math review, storyboard, scenes, final).
- Update `_workspace/session.md`: mark Epic 4 items done, record actual durations.
- Update `product-backlog/BACKLOG.md` E4-I1/I2/I3 statuses to Done with dates.

## Key constraints to remember

- Local model = Qwen 3.8 27B via `anthropic--claude-sonnet-latest`; 9B tier = `anthropic--claude-haiku-latest`.
- Web tools (WebSearch/WebFetch) disabled through the local proxy. **The proxy is flaky** — it threw transient HTTP 500s mid-session that killed an agent run; if a command fails with a 500, wait ~20 s and retry once, then switch strategy per the two-strike rule.
- **Duration window: 2–11 min** (hard gate [120s, 660s]). No padding to hit a floor; write tight, no slop.
- manimgx ≈ Manim Community Edition API. No 3D, no character/illustration art (scientist is a minimal geometric figure).
- Follow `REPO_STRUCTURE.md` for all artifact placement.
- Cracked series hook: character-grounded (scientist/ecologist), not abstract hypothetical.

## Anti-loop rules (mandatory)

1. No identical retries — inspect the exact error, correct args before re-calling.
2. Two-strike circuit breaker — 2 consecutive failures on an approach → stop that approach, switch strategy or report blocker. Never a 3rd try of the same thing.
3. Strict scope verification — verify only against explicit acceptance criteria; no invented test suites.
