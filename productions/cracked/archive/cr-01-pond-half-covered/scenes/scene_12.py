from manimgx import *

config.background_color = "#0F172A"

BG    = "#0F172A"
CREAM = "#F2E3C6"
ORG   = "#F97316"
BLUE  = "#3B82F6"


class RecapScene(Scene):
    """Shot 12 — Recap — The Law Behind the Riddle (Beats 15–16, ~40 s)"""

    def construct(self):
        # callback to hook pond
        pond = Circle(radius=1.6, color=BLUE, stroke_width=4)
        pond.move_to(ORIGIN)

        # fill = 100% then animate to 50%
        t = ValueTracker(1.0)

        def fill():
            frac = t.get_value()
            h = max(0.01, frac * 3.2)
            r = Rectangle(width=3.2, height=h, color=BLUE, fill_opacity=0.5, stroke_width=0)
            r.move_to([0, -1.6 + h / 2, 0])
            return r

        fill_rect = always_redraw(fill)

        # question text (callback from hook)
        question = Text("On which day was it exactly half-covered?", font_size=26, color=CREAM)
        question.next_to(pond, UP, buff=0.5)

        # answer
        answer = Text("Day 29", font_size=72, color=ORG, weight=BOLD)
        answer.move_to(ORIGIN)

        # series tagline
        tagline = Text("Every riddle hides a law. Break it open.", font_size=26, color=CREAM)
        tagline.to_edge(DOWN, buff=0.4)

        # day29 fraction label
        half_label = MathTex(r"= \frac{1}{2}", color=ORG, font_size=36)
        half_label.next_to(pond, RIGHT, buff=0.5)

        # --- beat 15: reveal ---
        self.play(FadeIn(pond))
        self.add(fill_rect)
        self.play(Write(question))
        self.wait(0.5)

        # animate backward: full → half-covered
        self.play(t.animate.set_value(0.5), run_time=1.2)
        self.play(Write(answer))
        self.play(Write(half_label))
        self.wait(1.0)

        # beat 16: tagline
        self.play(Write(tagline))
        self.wait(2.5)  # Beats 15–16 narration

        # final hold then fade out
        self.play(FadeOut(VGroup(pond, fill_rect, question, answer, half_label, tagline)))
        self.wait(0.5)
