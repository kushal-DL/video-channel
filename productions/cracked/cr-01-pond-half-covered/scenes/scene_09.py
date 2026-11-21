from manimgx import *

config.background_color = "#0F172A"

BG    = "#0F172A"
CREAM = "#F2E3C6"
ORG   = "#F97316"
BLUE  = "#3B82F6"


class ResultStatementScene(Scene):
    """Shot 9 — Result Statement (Beat 11, ~25 s)"""

    def construct(self):
        # large "Day 29" answer
        answer = Text("Day 29", font_size=72, color=ORG, weight=BOLD)
        answer.move_to([0, 1.5, 0])

        sub1 = MathTex(r"= 50\% \text{ coverage}", color=CREAM, font_size=44)
        sub1.next_to(answer, DOWN, buff=0.3)

        sub2 = Text("one day before full coverage", font_size=30, color=CREAM)
        sub2.next_to(sub1, DOWN, buff=0.25)

        # small pond at bottom-right for visual anchor (50% fill)
        pond = Circle(radius=0.9, color=BLUE, stroke_width=3)
        pond.to_corner(DR, buff=0.5)

        fill_rect = Rectangle(width=1.8, height=0.9, color=BLUE, fill_opacity=0.5, stroke_width=0)
        fill_rect.move_to([pond.get_center()[0], pond.get_center()[1] - 0.45, 0])

        pond_label = Text("Day 29", font_size=18, color=ORG)
        pond_label.next_to(pond, DOWN, buff=0.1)

        # --- reveals ---
        self.play(Write(answer))
        self.play(Write(sub1))
        self.play(Write(sub2))
        self.play(Create(pond), FadeIn(fill_rect), Write(pond_label))
        self.wait(2.0)  # Beat 11 narration

        # out_state: full wipe (act boundary)
        self.play(FadeOut(VGroup(answer, sub1, sub2, pond, fill_rect, pond_label)))
        self.wait(0.3)
