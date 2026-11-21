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


class LastFiveDaysTableScene(Scene):
    """Shot 5 — Last-Five-Days Table (Beat 7, ~30 s)"""

    def construct(self):
        # formula in top-right corner (carried from Shot 4)
        corner_formula = MathTex(
            r"\text{fraction}(n) = \frac{2^n}{2^{30}}",
            color=ORG, font_size=26,
        ).to_corner(UR, buff=0.3)
        self.add(corner_formula)

        # --- table header ---
        header_day  = Text("Day", font_size=28, color=CREAM)
        header_frac = Text("Fraction", font_size=28, color=CREAM)
        header_pct  = Text("%", font_size=28, color=CREAM)

        col_x = [-3.5, 0.0, 3.0]
        header_day.move_to([col_x[0], 2.8, 0])
        header_frac.move_to([col_x[1], 2.8, 0])
        header_pct.move_to([col_x[2], 2.8, 0])

        header_line = Line([-4.5, 2.5, 0], [4.5, 2.5, 0], color=BLUE, stroke_width=2)

        self.play(Write(header_day), Write(header_frac), Write(header_pct))
        self.play(Create(header_line))

        # --- build rows one by one ---
        row_y_start = 2.0
        row_step = 0.75
        highlight_box = None

        for i, (day, frac_str, pct_str) in enumerate(TABLE_ROWS):
            y = row_y_start - i * row_step
            is_day29 = (day == 29)

            cell_day  = Text(str(day),  font_size=28, color=ORG if is_day29 else CREAM)
            cell_frac = MathTex(frac_str, font_size=30, color=ORG)
            cell_pct  = MathTex(pct_str,  font_size=30, color=ORG)

            cell_day.move_to([col_x[0], y, 0])
            cell_frac.move_to([col_x[1], y, 0])
            cell_pct.move_to([col_x[2], y, 0])

            row_group = VGroup(cell_day, cell_frac, cell_pct)

            if is_day29:
                # orange highlight box behind Day 29 row
                box = Rectangle(width=9.0, height=0.65, color=ORG, fill_opacity=0.25, stroke_width=0)
                box.move_to([0, y, 0])
                self.play(FadeIn(box), Write(row_group), run_time=0.5)
                self.play(Indicate(cell_pct, color=ORG, scale_factor=1.3), run_time=0.4)
                highlight_box = box
            else:
                self.play(Write(row_group), run_time=0.4)

            self.wait(0.25)

        self.wait(1.5)

        # out_state: table persists into Shot 6
        self.wait(0.3)
