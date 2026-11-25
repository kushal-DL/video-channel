---
name: tight-explainer-script
description: Write and audit spoken explainer video scripts with zero AI slop, zero fake hype, no repetitive math, and crisp spoken cadence.
---

# Tight Explainer Script: Anti-Slop for Spoken Video

Use this skill when drafting, reviewing, or rewriting spoken explainer narration scripts (especially for educational math, science, and riddle breakdown videos).

General anti-slop skills target written essays and blog posts. Spoken narration scripts have distinct failure modes: artificial suspense, repetitive math padding, dramatic em-dash pauses, and throat-clearing setups that sound robotic when read aloud or processed by TTS (Text-to-Speech).

---

## 1. Hard Constraints (Banned Patterns)

### 1. No Mystery-Box Teasing & Inflated Stakes
- **Banned:** 
  - "The right answer will surprise you."
  - "And once you see why, you will never look at X the same way again."
  - "Most people get this completely wrong."
  - "They are wrong. Not a little wrong — wrong by a mile."
  - "Take a moment."
- **Rule:** State the premise, the observation, or the puzzle directly in 1–2 sentences. Let the paradox or puzzle generate its own curiosity without telling the audience how to feel.

### 2. No Throat-Clearing Openers & Meta-Signposting
- **Banned:**
  - "Here is a question..."
  - "Here is how to track..."
  - "Here is the key insight..."
  - "Let us look at..."
  - "Notice that..." / "Recall that..." / "Remember that..."
  - "This means that..." as a sentence starter
- **Rule:** Start immediately with the subject, character, or action. If deleting the first four words leaves a complete sentence, delete them.
  - *Slop:* "Here is the key insight: Day 29 is half."
  - *Fix:* "Day 29 is half."

### 3. One Explanation Per Concept (No Repetitive Padding)
- **Banned:** Explaining the same arithmetic or mechanism across multiple consecutive beats (e.g., explaining $2^{29}$ vs $2^{30}$ in the hook, then re-explaining it in the motivation, then re-explaining the same fraction in the build-up).
- **Rule:** Once a mathematical fact or mechanism lands, advance the argument. Subsequent beats must introduce new visual or conceptual information.

### 4. No Binary Contrast Crutches
- **Banned:**
  - "Not X — Y"
  - "Not 50 percent. Not even close."
  - "Not a little wrong — wrong by a mile."
  - "It's not just about X, it's about Y."
- **Rule:** State what is true directly without staging a fake rejection first.
  - *Slop:* "Day 15 is not 50 percent. Not even close. Day 29 is the answer."
  - *Fix:* "Day 15 covers barely a fraction of a percent. The pond hits fifty percent on Day 29."

### 5. Spoken TTS Cadence (Not Written Essay Prose)
- **Banned:**
  - Em-dash dramatic pauses (`—`) used as conversational crutches (TTS synthesizers like Edge-TTS pause awkwardly on em-dashes).
  - Monotonous sentence length (three consecutive sentences of ~15 words).
  - Summary wrap-up lines at the end of every beat ("And that changes everything.").
- **Rule:**
  - Keep sentences under 25 words.
  - Alternate rhythm: follow a long explanatory sentence (18–24 words) with a short punchy sentence (3–8 words).
  - Punctuate for breath and speech flow: use periods and commas, avoid em-dashes.

### 6. Natural Length (2–11 Minutes, No Floor Padding)
- **Rule:** Episode duration is flexible between 2 and 11 minutes (hard gate [120s, 660s]), determined by the natural complexity of the topic. Short riddles naturally run 2.5–4 minutes (~350–550 words). Never artificially expand a script or repeat calculations just to hit an arbitrary duration floor. Brevity and viewer retention always beat padded length.

---

## 2. Two-Pass Script Workflow

When generating or editing an episode script, execute two distinct passes:

### Pass 1: Pedagogical Structure
Draft the core beats in sequence:
1. **Hook:** Grounded in a concrete observation, character, or paradox (no abstract definitions).
2. **Intuition Gap / Motivation:** Why common intuition defaults to linear thinking and fails here.
3. **Build-Up:** Step-by-step mechanism, one step per beat, tagging every math claim with `[MR]`.
4. **Result:** Clear, plain-language statement of the core law.
5. **Worked Example (Strict Domain Shift):** Must use a completely different real-world context (e.g., bacteria in a petri dish, compound interest, nuclear doubling), NEVER the same problem with different numbers.
6. **Recap:** Tie the law back to the opening riddle.

### Pass 2: The Anti-Slop Audit
Read through every beat and run this checklist:
- [ ] Does any sentence start with "Here is", "Let us", "Notice that", or "This means"? → Delete or rephrase.
- [ ] Is there any fake hype ("The answer will surprise you", "wrong by a mile")? → Strip it.
- [ ] Is the same calculation explained in more than one beat? → Consolidate into the strongest beat.
- [ ] Are there binary contrasts ("Not X, but Y")? → Make them direct statements.
- [ ] Are em-dashes creating awkward speech breaks? → Replace with periods or natural commas.
- [ ] Do sentence lengths vary? → Break up runs of uniform length.

---

## 3. Storyboard Alignment Rule

Visuals and storyboard shots must never invent their own narration lines:
- The Storyboard Artist must import narration beats verbatim from `script-reviewed.md`.
- No storyboard shot may re-introduce clickbait title cards ("Day 15? WRONG!") or floating unanchored abstractions.
- Every shot pairs a `concrete_visual` (real-world object/analogy) with an `abstract_symbol` (mathematical notation) simultaneously.
