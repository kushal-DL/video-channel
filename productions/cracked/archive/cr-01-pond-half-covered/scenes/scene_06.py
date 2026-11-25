from manimgx import *

config.background_color = "#0F172A"

BG    = "#0F172A"
CREAM = "#F2E3C6"
ORG   = "#F97316"
BLUE  = "#3B82F6"


TABLE_ROWS = [
    (25, r"\frac{1}{32}", "3\\%"),
    (26, r"\frac{1}{16}", "6\\%"),
    (27, r"\frac{1}{8}",  "13\\%"),
    (28, r"\frac{1}{4}",  "25\\%"),
    (29, r"\frac{1}{2}",  "50\\%"),
    (30, r"1",            "100\\%"),
]


class Day15PunchlineScene(Scene):
    """Shot 6 — Day 15 Punchline (Beat 8, ~25 s)"""

    def construct(self):
        # --- recreate the table from Shot 5 (already built) ---
        col_x = [-3.5, 0.0, 3.0]
        row_y_start = 2.0
        row_step = 0.75

        corner_formula = MathTex(
            r"\text{fraction}(n) = \frac{2^n}{2^{30}}",
            color=ORG, font_size=26,
        ).to_corner(UR, buff=0.3)
        self.add(corner_formula)

        header_day  = Text("Day", font_size=28, color=CREAM).move_to([col_x[0], 2.8, 0])
        header_frac = Text("Fraction", font_size=28, color=CREAM).move_to([col_x[1], 2.8, 0])
        header_pct  = Text("%", font_size=28, color=CREAM).move_to([col_x[2], 2.8, 0])
        header_line = Line([-4.5, 2.5, 0], [4.5, 2.5, 0], color=BLUE, stroke_width=2)

        rows = VGroup()
        for i, (day, frac_str, pct_str) in enumerate(TABLE_ROWS):
            y = row_y_start - i * row_step
            is_day29 = (day == 29)
            cell_day  = Text(str(day), font_size=28, color=ORG if is_day29 else CREAM).move_to([col_x[0], y, 0])
            cell_frac = MathTex(frac_str, font_size=30, color=ORG).move_to([col_x[1], y, 0])
            cell_pct  = MathTex(pct_str, font_size=30, color=ORG).move_to([col_x[2], y, 0])
            rows.add(VGroup(cell_day, cell_frac, cell_pct))

        day29_box = Rectangle(width=9.0, height=0.65, color=ORG, fill_opacity=0.25, stroke_width=0)
        day29_box.move_to([0, row_y_start - 4 * row_step, 0])

        self.add(header_day, header_frac, header_pct, header_line, rows, day29_box)

        # --- Day 15 inset row ---
        inset_y = -2.8
        dashed_top = DashedLine([-4.5, inset_y + 0.4, 0], [4.5, inset_y + 0.4, 0], color=BLUE, stroke_width=1.5)
        dashed_bot = DashedLine([-4.5, inset_y - 0.45, 0], [4.5, inset_y - 0.45, 0], color=BLUE, stroke_width=1.5)

        cell15_day  = Text("15",  font_size=28, color=CREAM).move_to([col_x[0], inset_y, 0])
        cell15_frac = MathTex(r"\frac{1}{32768}", font_size=30, color=ORG).move_to([col_x[1], inset_y, 0])
        cell15_pct  = MathTex(r"0.003\%", font_size=30, color=ORG).move_to([col_x[2], inset_y, 0])

        self.play(Create(dashed_top), Create(dashed_bot))
        self.play(Write(cell15_day), Write(cell15_frac), Write(cell15_pct))
        self.play(Indicate(cell15_pct, color=ORG, scale_factor=1.4))
        self.wait(0.5)

        # callout: "Day 15? ✗"
        callout = Text("Day 15?  ✗", font_size=34, color=ORG)
        callout.move_to([0, inset_y - 1.0, 0])
        self.play(Write(callout))
        self.wait(1.5)  # Beat 8 narration
        self.play(FadeOut(callout))
        self.wait(0.3)
