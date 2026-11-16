# Video-Channel Brand Bible

**Purpose:** Single source of truth for brand voice, visual style, and pedagogical approach.  
**Audience:** All production agents (Producer, Screenwriter, Animator, Narration Engineer, Editor).

---

## Voice & Tone

### Core Principles
- **Clarity over cleverness:** Every sentence must advance understanding. No jargon without explanation.
- **Encouraging but rigorous:** Students should feel capable of mastering the material.
- **Conversational authority:** Like a knowledgeable tutor, not a lecturer or peer.

### Voice Guidelines
| Do | Don't |
|----|-------|
| Use active voice: "We derive..." instead of "It is derived that..." | Avoid passive constructions in narration scripts |
| Define terms on first use with brief parentheticals | Assume prior knowledge beyond high school algebra |
| Use analogies from everyday life (cooking, sports, music) | Overuse metaphors; keep them relevant to the math concept |

### Sentence Structure for TTS
- Max 25 words per sentence for optimal speech rhythm
- Avoid nested clauses deeper than two levels
- Numbered lists should use "first," "second," "third" rather than bullets in narration

---

## Visual Style (manimgx)

### Color Palette
| Role | Hex | Usage |
|------|-----|-------|
| Primary Blue | `#2563EB` | Main text, key formulas, active elements |
| Accent Orange | `#F97316` | Highlights, important transitions, warnings |
| Background Dark | `#0F172A` | Video background (slate-900) |
| Text Light | `#E2E8F0` | Secondary text, captions |

### Typography
- **Font:** System sans-serif (clean, readable at all sizes)
- **Math font:** Computer Modern (default via MathTex; never override unless necessary)
- **Hierarchy:** Title 48pt → Section 36pt → Body 28pt → Caption 20pt

### Composition Rules
1. **Rule of thirds:** Keep main subject in upper-left or center-third
2. **Breathing room:** Never fill the frame; leave negative space for captions
3. **Consistent framing:** Same aspect ratio (16:9) across all episodes
4. **Motion restraint:** Subtle animations only; avoid flashy transitions that distract from math

---

## Pedagogical Approach

### Script Structure Template
```markdown
[HOOK] — 0:00-0:30
   - Relatable problem or misconception
   - Promise of what will be learned

[CONCEPT] — 0:30-2:00
   - Formal definition with precise language
   - Visual representation immediately follows text

[EXAMPLE] — 2:00-4:00
   - Concrete numerical example
   - Step-by-step derivation on screen

[ABSTRACTION] — 4:00-5:30
   - Generalize from example to theorem/property
   - Connect back to real-world application

[SUMMARY] — 5:30-6:00
   - One-sentence takeaway
   - Preview next episode's connection
```

### Math Claim Tagging (`[MR]`)
All mathematical assertions requiring verification must be tagged in the script:
- `[MR] The derivative of x² is 2x` → triggers math-reviewer adversarial check
- Format: `[MR] <claim>` placed on its own line before visual demonstration

---

## Episode Metadata Standards

### Title Format
`[Episode #]: [Topic] — [Learning Outcome]`  
Example: `Episode 1: Introduction to Derivatives — Understanding Instantaneous Rate of Change`

### Description Template
```markdown
In this episode, we explore [topic]. By the end, you'll be able to:
- [Skill 1]
- [Skill 2]
- [Skill 3]

This builds on previous concepts from [previous episode] and prepares you for [next episode].

Keywords: #calculus #derivatives #matheducation #tutorial
```

### Chapter Markers
Extracted automatically from `timing.json` using scene boundaries. Each chapter should be ≤90 seconds to maintain viewer engagement.

---

## Quality Checklist (Pre-Render)

Before any episode moves to animation/rendering:

- [ ] Script reviewed by math-reviewer with all `[MR]` claims verified
- [ ] Storyboard confirms visual matches narration timing exactly
- [ ] Continuity register updated for recurring motifs/notation
- [ ] Voiceover recorded at 48kHz mono, normalized to -16 LUFS
- [ ] All manimgx scenes use consistent config (resolution, fps)

---

## Version History

| Date | Change | Author |
|------|--------|--------|
| 2026-11-17 | Initial bible created | Doomlord |
