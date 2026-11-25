# Channel Bible

Series-wide creative standards for the math-tutorial channel. Every agent (producer through release) defers to this document when choices are ambiguous. Owned by the Producer; changes require a Director sign-off in `signoffs.md`.

## Visual Norms

- **Background:** `#0F172A` (dark slate) — set via module-level `config.background_color = "#0F172A"` in every scene file. Never the default black.
- **Fonts:** default manimgx fonts; titles at 56 px, body text ≥ 30 px, math at 60–72 px.
- **Contrast:** all text must meet 4.5:1 contrast against the background. Gray-on-dark text is a defect.
- **Camera framing:** consistent across episodes; key objects centered with ≥ 0.5 buff margin from frame edges.

## Animation Style

This section is the mandatory animation contract for Animator and Storyboardist.

### Palette (3-color system)

| Role | Color | Hex |
|------|-------|-----|
| Background | dark slate | `#0F172A` |
| Text / captions | cream | `#F2E3C6` |
| Math (equations, symbols) | orange | `#F97316` |
| Geometry (curves, axes, points) | blue | `#3B82F6` |

Use exactly this hierarchy — no ad-hoc colors. Every element on screen must map to one of these four roles.

### Reveals

- Equations and math symbols are revealed with `Write()` or `Create()` — **never `FadeIn()`**.
- Geometry (curves, axes, secants) is drawn with `Create()`.
- Persist the core diagram across beats: keep axes/curve on screen and animate only the new element per beat. Reserve full wipes for act boundaries (title → body, body → outro).
- Hold frames must carry active visual content — no holds on empty backgrounds.

### Voice (narration)

- Tone: warm and unhurried; authoritative but never cold. No filler phrases ("so", "basically", "you know").
- **TTS voice:** `en-US-AriaNeural` (Microsoft Edge neural voice). Verified 2026-11-20 (see `docs/tts-decision.md`).
- Pacing: ~150 wpm (slightly slower than average to let viewers read on-screen equations); target episode duration 2–11 min (hard gate [120s, 660s]). Episode duration is determined organically by topic complexity — never pad a script with filler or repetitive arithmetic to hit an arbitrary duration floor.
- Insert a brief pause (0.3–0.5 s silence) at each concept boundary — after the hook, after the motivation, before the worked example.
- Slow down further during the worked example: give the viewer time to read each substitution step before moving to the next.
- Sentences short and TTS-friendly; math read as spoken language ("d of p over d of t"), with the symbol shown on screen simultaneously.

## Pacing Norms

- 15–45 seconds per shot; fades ≤ 0.8 s, holds at full opacity ≥ 60% of each beat.
- Transitions: fade, slide, zoom, cut, or morph — chosen per shot in the storyboard, never improvised.

## Notation Conventions

- Standard Leibniz notation (d/dx) unless an episode brief says otherwise; defined at first use.
- Bold vectors; angle vs. arc-length conventions fixed per episode in `continuity.md`.

---

## House Style (narrative & pacing contract)

This section describes the target feel for every episode. The local model does not have a reference for TED-Ed or 3Blue1Brown — follow these rules verbatim instead of trying to emulate a named style.

### Hook patterns (pick exactly one per episode)

Every episode must open with one of these four hooks — choose the one that fits the topic most naturally:

| Type | Description | Example opening sentence |
|------|-------------|--------------------------|
| Paradox | State something true that sounds impossible | "Every time you throw a ball, you're solving a differential equation — without knowing it." |
| Real-world scenario | Drop the viewer into a concrete situation first | "You're designing a water slide and need the steepest safe drop — here's the exact calculation engineers use." |
| You-already-do-this | Show the viewer they intuitively know the concept | "You already understand derivatives — every time you check your speedometer you're reading one." |
| Surprising number | Lead with a striking numerical fact | "A single fold of paper, repeated 42 times, would reach the Moon." |

The hook must appear in the first 30–50 seconds. It is a question or claim — never a definition.

### Concrete → abstract rule (mandatory)

Every abstract symbol must be introduced *paired with* a concrete visual analogy, shown on screen at the same moment:

- Introduce the tangible thing first (a moving car, water filling a tank, a shadow lengthening).
- Then show the symbol next to it, not after it.
- Example: animate a car's speedometer needle while `v = ds/dt` appears beside it. Never show the formula alone on a blank background.

The Storyboard artist must specify this pairing explicitly. If a symbol appears without a concrete pair, that shot is incomplete.

### Equation persistence rule

- Keep the working equation on screen across beats; never clear and redraw it just to change one term.
- Highlight the single term under discussion using the orange math color (`#F97316`).
- Use `Transform` to morph one form of the equation into the next — do not fade out and fade in.
- Reserve full screen wipes for act boundaries only (hook → body, body → worked example, worked example → recap).

### Pacing arc (time budget for a ~6-minute episode)

| Segment | Target duration | Notes |
|---------|----------------|-------|
| Hook | 30–50 s | One hook type from the menu above |
| Motivation ("why this matters") | 30–45 s | Connect to real world or prior knowledge |
| Build-up (concept + derivation) | 3–4 min | 20–30 s sub-beats; one new idea per beat |
| Result statement | 20–30 s | Clear, plain-language summary of the main takeaway |
| Worked example | 60–90 s | Narrated as a story: set up → predict → solve step by step |
| Recap | 30–45 s | Tie back to the hook and state what the viewer can now do |

Adjust proportionally for shorter/longer episodes but keep the hook ≤ 50 s and the worked example ≥ 60 s.

### One idea per beat rule

A single narration beat introduces exactly one new symbol, one new step, or one new visual element. If two things need to appear, they need two beats. Never put two new symbols in the same frame without explanation.

---

### Narrative craft — writing anti-patterns (mandatory)

The following are banned in all scripts. They are reliable signals of AI-generated prose and make the channel sound like a textbook, not a person.

**Banned sentence openers — delete and start with the substance instead:**

| Banned pattern | Example of the problem | Fix |
|---|---|---|
| "Here is a/the..." | "Here is the key insight." | State the insight. |
| "Let us..." | "Let us count the first few days." | Count. |
| "Now look at..." | "Now look at the last five days." | "On Day 25, the pond is 3% covered." |
| "Now check..." | "Now check Day 15." | "Day 15: 0.003%." |
| "Notice that..." | "Notice that the coverage doubles." | "The coverage doubles." |
| "Recall that..." | "Recall that we defined..." | Drop the recall — the viewer just watched it. |
| "The key insight is..." | — | State the insight. |
| "This means that..." (as opener) | "This means that Day 29 is half." | "Day 29 is half." |

Rule: **Start every sentence with the substance.** If you can delete the first four words and the sentence still makes sense, delete them.

**Sentence rhythm — vary length deliberately:**

After a long explanatory sentence (20+ words), write a short one (≤8 words). After a short punchy sentence, expand. Three consecutive sentences of similar length is a defect.

Good: *"A rope tied around the Earth at the equator — no slack. Now add exactly one metre of rope and distribute that extra length uniformly. How high does it float above the ground? Sixteen centimetres."*

Bad: *"The rope is tied around the equator and has no slack. When one metre is added, the rope floats uniformly. The height it floats is sixteen centimetres."*  (Three similar-length sentences, all declarative.)

**Sentence count discipline:** If a beat has more than 5 sentences, cut the weakest two. Length is not depth.

---

### Worked example rule (strict)

The worked example must apply the concept in a **different real-world context**, not a parameter tweak of the main example.

| ✗ Wrong | ✓ Right |
|---|---|
| Same lily pad problem but 20 days instead of 30 | Compound interest on a loan — when does the debt first exceed twice the principal? |
| Same projectile, different angle | A 100m sprint — why does a 1% improvement in top speed reduce time by more than 1%? |
| Same function, different coefficient | A nuclear reaction: neutrons doubling per millisecond — when is half the yield released? |

The worked example is the "so this is why it matters" moment. It should feel like a new scene, not a practice problem. Set it up in one or two sentences, let the viewer predict, then apply the same logic they just learned. The transfer of the method to a new domain is the pedagogical payoff.

---

### Character-grounded hooks (Cracked series preferred)

For the Cracked series, anchor the riddle in a **person's concrete experience** of encountering it, not an abstract "imagine a lily pad."

**Why:** A character encountering the riddle gives the Animator concrete scenes to show (a person, a changing object, time passing). Abstract hypotheticals give them nothing but text and diagrams. Character-grounded scripts produce richer, more varied animation.

**Pattern:** A person — a scientist, an engineer, a teacher, a student — is going about a routine when they notice something. The riddle *emerges from observation*. The person's growing curiosity or alarm becomes the episode's dramatic spine.

**Example for a lily pad / exponential growth episode:**

A biologist walks past the same pond every morning on the way to her lab. Day 1: one lily pad — she barely notices. Day 7: a small cluster — interesting. Day 25: maybe a quarter of the pond — she makes a mental note. Day 29: half the pond — she stops and stares. Day 30: she can't see water. The question she asks herself *is* the riddle. The answer emerges from her own reasoning.

This framing gives the Animator:
- A character to follow (walk cycle, costume, expression)
- The pond changing across shots (time-lapse can be implied)
- A day counter the viewer follows alongside the character
- A visual climax (Day 29 → Day 30 pond transition) that lands emotionally, not just mathematically

The character does not need a name unless the episode is biographical. Keep them archetypal: "the biologist", "the engineer", "the physics student."
