from manimgx import *

config.background_color = "#0F172A"

BG    = "#0F172A"
CREAM = "#F2E3C6"
ORG   = "#F97316"
BLUE  = "#3B82F6"


class WorkedExampleSetupScene(Scene):
    """Shot 10 — Worked Example Setup (Beat 12, ~20 s)"""

    def construct(self):
        # 20-day pond
        pond = Circle(radius=1.6, color=BLUE, stroke_width=4)
        pond.move_to(ORIGIN)

        # fully covered (fill = 100%)
        fill = Rectangle(width=3.2, height=3.2, color=BLUE, fill_opacity=0.5, stroke_width=0)
        fill.move_to(ORIGIN)

        full_label = Text("Full coverage: Day 20", font_size=30, color=CREAM)
        full_label.next_to(pond, UP, buff=0.4)

        d_label = MathTex(r"D = 20", color=ORG, font_size=46)
        d_label.next_to(pond, DOWN, buff=0.5)

        # "Day 10?" question mark
        guess = Text("Day 10?", font_size=38, color=CREAM)
        guess.move_to([0, 0, 0])  # centered on pond — callout

        # --- build ---
        self.play(Create(pond), FadeIn(fill))
        self.play(Write(full_label))
        self.play(Write(d_label))
        self.wait(0.5)
        self.play(Write(guess))
        self.wait(1.5)  # Beat 12 narration

        # out_state: pond + D=20 + guess persist; camera zooms in
        self.wait(0.3)
