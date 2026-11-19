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

- Tone: authoritative but approachable; no filler phrases ("so", "basically", "you know").
- TTS voice: `en-US-Standard-A` (edge-tts default) until a cloned channel voice is approved.
- Pacing: ~160 wpm; target episode duration 4–11 min (hard gate [240s, 660s]).
- Sentences short and TTS-friendly; math read as spoken language ("d of p over d of t"), with the symbol shown on screen.

## Pacing Norms

- 15–45 seconds per shot; fades ≤ 0.8 s, holds at full opacity ≥ 60% of each beat.
- Transitions: fade, slide, zoom, cut, or morph — chosen per shot in the storyboard, never improvised.

## Notation Conventions

- Standard Leibniz notation (d/dx) unless an episode brief says otherwise; defined at first use.
- Bold vectors; angle vs. arc-length conventions fixed per episode in `continuity.md`.
