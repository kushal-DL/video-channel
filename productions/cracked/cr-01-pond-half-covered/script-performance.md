# Performance Notes — cr-01-pond-half-covered

**Director:** voice-director (Gemma 9B) — notes authored by narration-engineer on its behalf after two failed voice-director subagent runs (both exited without writing the file; see handoff report).
**Input:** script-reviewed.md Part A (8 beats)
**Date:** 2026-11-22

> Note to Narration Engineer: `scripts/tts.py` (edge-tts) accepts plain text only — no SSML `<break>` tags, no rate/pitch parameters. The cues below are direction; apply pacing through verbatim text only (sentence punctuation + per-beat file boundaries). No narration word may be altered.

## Beat 1 — Hook
- **Delivery tone:** curious, warm. Play it like a story being told to one person: unhurried, with quiet surprise building toward the final question.
- **Pacing:** normal (~150 wpm). Let the day-count sentences land evenly; do not rush "Day 7 / Day 15 / Day 30".
- **Pause cues:** natural punctuation pauses after "She does not stop." and after "bank to bank." Add `<break time="600ms"/>` before the final question ("On which day was the pond half-covered?") so it hangs in the air.
- **Emphasis words:** Day 30, gone under green pads, half-covered

## Beat 2 — Motivation
- **Delivery tone:** sympathetic, empathetic. The viewer has probably guessed Day 15 too; validate before correcting them.
- **Pacing:** normal. Slightly slower on "It fails completely here." — that is the pivot line.
- **Pause cues:** natural pauses at all sentence ends. Add `<break time="400ms"/>` after "That intuition works for a dripping tap that adds an equal cup of water every hour." before the contrast lands.
- **Emphasis words:** first instinct, fails completely, linear, exponential

## Beat 3 — Build-up (Linear vs. Exponential)
- **Delivery tone:** intrigued, vivid. Paint the two ponds side by side; keep energy up on "engulfs" and "explodes".
- **Pacing:** normal. Slightly slower through "stays almost empty for three weeks, then engulfs the surface in five days."
- **Pause cues:** natural pauses at sentence ends. Add `<break time="400ms"/>` after "On Day 10, both ponds look nearly bare." before the Day 30 contrast.
- **Emphasis words:** identical slice, almost empty, engulfs, explodes

## Beat 4 — Build-up (The Math)
- **Delivery tone:** authoritative, clear. This is the formula beat: steady and precise, no drama.
- **Pacing:** slightly slower (-5%). Read "2 to the power of n over 2 to the power of 30" with clean separation between the two powers.
- **Pause cues:** natural pauses at sentence ends. Add `<break time="500ms"/>` after "The fraction covered is 2 to the power of n over 2 to the power of 30." before plugging in Day 15, and another `<break time="400ms"/>` after "...over 2 to the power of 30." (the Day 15 substitution) before "That equals barely three thousandths of a percent."
- **Emphasis words:** numbers, Day n, three thousandths of a percent

## Beat 5 — Build-up (The One Step Back Law)
- **Delivery tone:** warm, confident. This is the payoff idea; let it feel like a gift to the viewer.
- **Pacing:** slightly slower (-5%) on "the day before full must hold exactly half."
- **Pause cues:** natural pauses at sentence ends. Add `<break time="600ms"/>` after "...must hold exactly half." before "That lands you directly on Day 29." — the answer needs room to land.
- **Emphasis words:** looking backward, exactly half, Day 29

## Beat 6 — Result
- **Delivery tone:** celebratory, calm. State the result plainly and let it breathe; no exclamation energy needed.
- **Pacing:** normal. Slightly slower on "the final step accounts for half of everything ever produced."
- **Pause cues:** natural pauses at sentence ends. Add `<break time="500ms"/>` after "The pond was half-covered on Day 29." before the generalization.
- **Emphasis words:** Day 29, twenty-four hours before the end, half of everything

## Beat 7 — Worked Example (Bacteria in the Lab)
- **Delivery tone:** curious, instructive. New scene, new character action; keep it concrete and unhurried so each step can be read on screen.
- **Pacing:** slowest (-10%). This is the worked example: give viewers time to follow each substitution before moving on.
- **Pause cues:** natural pauses at sentence ends. Add `<break time="500ms"/>` after "When was the dish half full?" (let the viewer predict), `<break time="400ms"/>` after "...suggests nine am." before the correction, and `<break time="600ms"/>` after "one hour before noon is eleven am." before the 9am check.
- **Emphasis words:** doubles every hour, half full, eleven am, one eighth

## Beat 8 — Recap & Payoff
- **Delivery tone:** warm, authoritative, gently closing. Tie it back to the scientist and the pond; end on a quiet, satisfied note.
- **Pacing:** normal, decelerating into the final line ("nearly nothing, then half, then everything" — let each of those three phrases land separately).
- **Pause cues:** natural pauses at sentence ends. Add `<break time="500ms"/>` after "the state right before the end holds half the final amount." and `<break time="400ms"/>` after "Day 29 was half, Day 28 a quarter, Day 27 an eighth."
- **Emphasis words:** one law, multiplies instead of adds, nearly nothing, then everything
