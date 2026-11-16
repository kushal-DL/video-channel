# Episode 1 Storyboard

**Slug:** `episode-001-introduction-to-calculus`  
**Total scenes:** 24  
**Estimated duration:** ~6 minutes at 15fps average

---

## Shot List with Transitions

| # | Time | Visual Description | Transition | Duration | manimgx Commands |
|---|------|-------------------|------------|----------|------------------|
| 1 | 0:00-0:03 | Title card: "Introduction to Calculus" fades in over dark background | FadeIn → Hold | 3s | `FadeIn(Text("Introduction to Calculus"))` |
| 2 | 0:03-0:06 | Subtitle appears below title | CrossDissolve | 3s | `FadeIn(Text("Understanding Derivatives..."))` |
| 3 | 0:06-0:15 | Fade to car speedometer close-up (simulated with text overlay) | Cut | 9s | `FadeOut(group)` → `Write(Text("Speedometer at 65 mph"))` |
| 4 | 0:15-0:25 | Speedometer needle blurs, suggesting motion | CrossDissolve | 10s | `Blur(speedometer_text)` or animation effect |
| 5 | 0:25-0:30 | Return to dark background with question text | FadeIn | 5s | `FadeIn(Text("What does this number mean?"))` |
| 6 | 0:30-0:40 | Road scene: points A and B marked, car traveling between them | Cut | 10s | Draw road line with markers using VGroup and DashedLine |
| 7 | 0:40-0:50 | Average velocity formula appears next to road | CrossDissolve | 10s | `Write(MathTex(r"v_{avg} = \frac{\Delta x}{\Delta t}"))` |
| 8 | 0:50-1:00 | Speedometer needle fluctuating wildly while car moves | Cut | 10s | Animate speedometer value oscillating with Write/FadeOut cycles |
| 9 | 1:00-1:10 | Question text appears: "But what about right now?" | FadeIn | 10s | `FadeIn(Text("Instantaneous velocity?"))` |
| 10 | 1:10-1:30 | Position-time graph with two points, getting closer | CrossDissolve | 20s | Draw parabola curve; add two tangent lines approaching each other |
| 11 | 1:30-1:45 | Difference quotient formula appears over graph | FadeIn | 15s | `Write(MathTex(r"\frac{p(t+h) - p(t)}{h}"))` with annotation arrows |
| 12 | 1:45-2:00 | Shrink the interval visually (points move closer) | CrossDissolve | 15s | Animate h decreasing; show ratio stabilizing |
| 13 | 2:00-2:15 | "This IS velocity" text appears clearly | FadeIn → Hold | 15s | `FadeIn(Text("The derivative = instantaneous velocity"))` |
| 14 | 2:15-2:30 | Limit notation elegantly animates onto screen | CrossDissolve | 15s | Each symbol (lim, h→0, fraction) appears sequentially |
| 15 | 2:30-2:45 | Full limit formula displayed with color-coded parts | FadeIn | 15s | Color-code numerator (blue), denominator (orange), limit bar |
| 16 | 2:45-3:00 | "Leibniz notation" label appears next to dp/dt | CrossDissolve | 15s | `Write(MathTex(r"\frac{dp}{dt}"))` with historical note |
| 17 | 3:00-3:15 | Units appear: meters per second next to formula | FadeIn | 15s | Animate units sliding into place from right side |
| 18 | 3:15-3:30 | Return to car on road with velocity vector shown | CrossDissolve | 15s | Draw tangent line representing instantaneous direction |
| 19 | 3:30-4:00 | Summary text appears in three bullet points | FadeIn → Hold | 30s | Use VGroup with Text objects for each summary point |
| 20 | 4:00-4:30 | Preview of next episode: "Computing derivatives using rules" | CrossDissolve | 30s | Show equation symbols (d/dx, product rule) fading in/out |
| 21 | 4:30-5:00 | Closing encouragement text with channel branding | FadeIn → Hold | 30s | `FadeIn(Text("Keep asking what things mean..."))` + logo |
| 22 | 5:00-5:30 | End card: Episode title, next episode teaser | CrossDissolve | 30s | Two-column layout with title left, teaser right |
| 23 | 5:30-5:45 | Fade to black | FadeOut | 15s | `FadeOut(all_elements)` |
| 24 | 5:45-6:00 | Black screen (end) | — | 15s | No commands; audio continues |

---

## Transition Notes

- **CrossDissolve:** Used for conceptual shifts or when introducing new mathematical ideas. Duration: ~3 seconds typical.
- **Cut:** Used for returning to concrete examples or maintaining pacing during explanation. Duration: instantaneous.
- **FadeIn/FadeOut:** Used for emphasis, summary points, and title cards. Duration: 1 second standard.

---

## Continuity Notes

| Element | First Appearance | Last Appearance | Consistency Check |
|---------|------------------|-----------------|-------------------|
| Car on road | Shot 6 | Shot 18 | Same color scheme (blue car, gray road) throughout |
| Speedometer graphic | Shot 3 | Shot 8 | Identical design; needle animation style consistent |
| Mathematical notation font | Shot 7 | Shot 20 | Computer Modern via MathTex throughout |
| Color palette | Shot 1 | Shot 24 | Primary blue (#2563EB), accent orange (#F97316) used consistently |

---

## Animator Notes for Scene Implementation

- **Shot 10-12:** The approaching tangent lines should use `FadeIn` with slight scale animation to emphasize convergence
- **Shot 14-15:** Limit notation should appear character-by-character using `Write` on each symbol individually
- **Shot 17:** Units should slide in from the right edge using a simple translation animation
- **All formulas:** Use `MathTex` with consistent sizing (36pt for inline, 48pt for standalone)

---

## QC Checklist (Pre-render)

- [ ] All scene durations sum to ~360 seconds total
- [ ] Transitions match narration timing exactly (verify against script.md)
- [ ] No overlapping animations that could confuse viewers
- [ ] Mathematical notation renders correctly with LaTeX toolchain verified in E1-I3
