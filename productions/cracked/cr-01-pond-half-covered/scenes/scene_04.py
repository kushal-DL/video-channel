from manimgx import *

config.background_color = "#0F172A"

BG    = "#0F172A"
CREAM = "#F2E3C6"
ORG   = "#F97316"
BLUE  = "#3B82F6"


class CoverageFormulaScene(Scene):
    """Shot 4 — The Coverage Formula (Beat 6, ~25 s)"""

    def construct(self):
        # --- pond on left ---
        pond = Circle(radius=1.4, color=BLUE, stroke_width=4)
        pond.move_to([-2.5, 0, 0])

        # fill rectangle inside pond (simulate coverage)
        t = ValueTracker(1.0)  # fraction covered (0 to 1)

        def fill():
            frac = t.get_value()
            h = max(0.01, frac * 2.8)  # max height = diameter of pond
            r = Rectangle(width=2.8, height=h, color=BLUE, fill_opacity=0.5, stroke_width=0)
            r.move_to([-2.5, -1.4 + h / 2, 0])
            return r

        fill_rect = always_redraw(fill)
        day_label = Text("Day n", font_size=28, color=CREAM).next_to(pond, DOWN, buff=0.3)

        # --- formula on right (shown SIMULTANEOUSLY with pond) ---
        formula = MathTex(
            r"\text{fraction}(n) = \frac{2^n}{2^{30}}",
            color=ORG,
            font_size=42,
        )
        formula.move_to([2.0, 0.5, 0])

        day30_note = MathTex(
            r"\text{Day 30: } \frac{2^{30}}{2^{30}} = 1 \quad (\text{full})",
            color=CREAM,
            font_size=32,
        )
        day30_note.next_to(formula, DOWN, buff=0.5)

        # reveal pond and formula simultaneously
        self.play(Create(pond), Write(formula), run_time=1.2)
        self.add(fill_rect)
        self.play(Write(day30_note), Write(day_label))
        self.wait(0.8)

        # animate: Day 30 (full) → partial (Day n)
        self.play(t.animate.set_value(0.4), run_time=1.5)
        self.wait(1.5)  # Beat 6 narration

        # out_state: formula moves to top-right corner; pond stays
        formula_corner = formula.copy().scale(0.6).to_corner(UR, buff=0.3)
        self.play(
            Transform(formula, formula_corner),
            FadeOut(day30_note),
            run_time=0.8,
        )
        self.wait(0.3)
