from manimgx import *

config.background_color = "#0F172A"

BG    = "#0F172A"
CREAM = "#F2E3C6"
ORG   = "#F97316"
BLUE  = "#3B82F6"


class WorkedExampleDerivationScene(Scene):
    """Shot 11 — Worked Example Derivation (Beats 13–14, ~65 s)"""

    def construct(self):
        # 20-day pond on left (starts full)
        pond = Circle(radius=1.3, color=BLUE, stroke_width=4)
        pond.move_to([-3.5, 0.5, 0])

        t = ValueTracker(1.0)  # coverage fraction

        def fill():
            frac = t.get_value()
            h = max(0.01, frac * 2.6)
            r = Rectangle(width=2.6, height=h, color=BLUE, fill_opacity=0.5, stroke_width=0)
            bottom = [-3.5, -0.8, 0]
            r.move_to([bottom[0], bottom[1] + h / 2, 0])
            return r

        fill_rect = always_redraw(fill)
        pond_day_label = Text("Day 20", font_size=22, color=CREAM)
        pond_day_label.next_to(pond, DOWN, buff=0.3)

        # --- pre-build ALL three equation states (Shot 11 note: pre-build before first Transform) ---
        eq_generic = MathTex(r"\frac{2^n}{2^{20}}", color=ORG, font_size=46)
        eq_half    = MathTex(r"\frac{2^{19}}{2^{20}} = \frac{1}{2}", color=ORG, font_size=46)
        eq_quarter = MathTex(r"\frac{2^{18}}{2^{20}} = \frac{1}{4}", color=ORG, font_size=46)

        for eq in [eq_generic, eq_half, eq_quarter]:
            eq.move_to([1.5, 1.2, 0])

        # Day labels
        day19_label = Text("Day 19 — 50%", font_size=26, color=ORG)
        day19_label.next_to(pond, DOWN, buff=0.3)
        day18_label = Text("Day 18 — 25%", font_size=26, color=ORG)
        day18_label.next_to(pond, DOWN, buff=0.3)

        # --- Beat 13: show generic formula, then transform ---
        self.play(Create(pond))
        self.add(fill_rect)
        self.play(Write(pond_day_label))
        self.play(Write(eq_generic))
        self.wait(0.8)

        # Day 19: fraction = 1/2
        self.play(
            Transform(eq_generic, eq_half),
            t.animate.set_value(0.5),
            Transform(pond_day_label, day19_label),
            run_time=1.5,
        )
        self.wait(1.0)

        # Day 18: fraction = 1/4
        self.play(
            Transform(eq_generic, eq_quarter),
            t.animate.set_value(0.25),
            Transform(pond_day_label, day18_label),
            run_time=1.5,
        )
        self.wait(1.0)

        # --- Beat 14: pattern table ---
        table_title = Text("Pattern: k steps back from Day D", font_size=26, color=CREAM)
        table_title.move_to([1.5, 2.5, 0])

        # table rows
        rows_data = [
            (r"D - 1", "19", r"\frac{1}{2}\ (50\%)"),
            (r"D - 2", "18", r"\frac{1}{4}\ (25\%)"),
            (r"D - 3", "17", r"\frac{1}{8}\ (12.5\%)"),
        ]
        col_x = [0.5, 2.0, 3.8]
        row_y_start = 1.5
        row_step = 0.65
        table_rows_mobj = VGroup()

        for i, (step, day_val, cov) in enumerate(rows_data):
            y = row_y_start - i * row_step
            c1 = MathTex(step, font_size=28, color=CREAM).move_to([col_x[0], y, 0])
            c2 = MathTex(day_val, font_size=28, color=ORG).move_to([col_x[1], y, 0])
            c3 = MathTex(cov, font_size=28, color=ORG).move_to([col_x[2], y, 0])
            table_rows_mobj.add(VGroup(c1, c2, c3))

        # general formula
        gen_formula = MathTex(
            r"\frac{2^{D-k}}{2^D} = \frac{1}{2^k}",
            color=ORG, font_size=44,
        )
        gen_formula.move_to([2.0, -1.6, 0])

        self.play(
            FadeOut(eq_generic),
            Write(table_title),
        )
        self.play(Create(table_rows_mobj), run_time=1.5)
        self.play(Write(gen_formula))
        self.wait(2.0)  # Beats 13–14 narration

        # out_state: full wipe
        self.play(FadeOut(VGroup(
            pond, fill_rect, pond_day_label,
            table_title, table_rows_mobj, gen_formula,
        )))
        self.wait(0.3)
