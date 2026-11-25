"""Shot 6 — Plug in Day 15 + coverage table punchline (Beat 4, part 2). Brief §5b.

Formula persists from Shot 5 at top (equation persistence; cut transition).
Top zone: substitution line fraction(15) = 2^15 / 2^30 written below the main
formula with n -> 15 highlighted; beside it the lily pad shrinks to a tiny
speck on an otherwise empty pond. Bottom zone: coverage table (Day | Coverage
fraction | % of pond), rows Days 15, 25–30 — Day-15 punchline row written
first (0.003% in orange with the "Day 15?" echo tag), then rows fill down to
the orange-highlighted Day-29 row (50.0%) and Day-30 (100%).

A/V sync: SCENE_TARGET_SEC placeholder until timing.json exists.
"""
from manimgx import *

config.background_color = "#0F172A"  # channel palette — mandatory in every scene file

BG    = "#0F172A"
CREAM = "#F2E3C6"
ORG   = "#F97316"
BLUE  = "#3B82F6"

# Beat 4 part 2 (Day-15 plug-in + table): [~2:00–2:10]
SCENE_TARGET_SEC = 10.0  # TODO-AVSYNC: replace with value from timing.json


class Shot06Day15Table(Scene):
    def construct(self):
        # ---- In-state: persistent formula at top (from S5) + pad on the left ----
        eq = MathTex(r"\mathrm{fraction}(n)", "=", r"\dfrac{2^{n}}{2^{30}}", color=ORG).move_to([1.6, 3.4, 0])
        self.play(Write(eq), run_time=1.4)

        water = Ellipse(width=3.4, height=2.2, color=BLUE, stroke_width=3).move_to([-4.6, 1.9, 0])
        pad = RegularPolygon(n=6, radius=0.55, color=BLUE, stroke_width=3,
                             fill_color=CREAM, fill_opacity=0.85).move_to(water.get_center())
        self.play(Create(water), GrowFromCenter(pad), run_time=1.0)

        # ---- Top zone: substitution line (n -> 15 highlighted) ----
        sub = MathTex(r"\mathrm{fraction}(15)", "=", r"\dfrac{2^{15}}{2^{30}}", color=ORG).move_to([1.6, 2.4, 0])
        self.play(Write(sub), run_time=1.4)
        self.play(Indicate(sub[2]), run_time=0.8)   # the substituted term

        # Pad shrinks to a tiny speck — "practically was empty"
        speck = RegularPolygon(n=6, radius=0.09, color=BLUE, stroke_width=2,
                               fill_color=CREAM, fill_opacity=0.85).move_to(water.get_center())
        self.play(Transform(pad, speck), run_time=1.2)

        # ---- Bottom zone: coverage table (grid via Create, cells via Write) ----
        header = VGroup(
            Text("Day", font_size=30, color=CREAM),
            Text("Coverage fraction", font_size=30, color=CREAM),
            Text("% of pond", font_size=30, color=CREAM),
        )
        rows_data = [
            ("15", r"2^{15} / 2^{30}", "0.003%"),
            ("25", r"2^{25} / 2^{30}", "0.03%"),
            ("26", r"2^{26} / 2^{30}", "0.06%"),
            ("27", r"2^{27} / 2^{30}", "0.12%"),
            ("28", r"2^{28} / 2^{30}", "0.24%"),
            ("29", r"2^{29} / 2^{30}", "50.0%"),
            ("30", r"2^{30} / 2^{30}", "100%"),
        ]
        col_x = [-4.6, -1.6, 1.4]
        top_y = 0.7
        row_h = 0.52

        # grid lines (geometry — Create)
        grid_lines = VGroup()
        for i in range(len(rows_data) + 2):
            y = top_y - i * row_h
            grid_lines.add(Line(LEFT * 4.9, RIGHT * 3.6, color=BLUE, stroke_width=1.5).move_to([0, y, 0]))
        for x in col_x:
            grid_lines.add(Line(UP * (len(rows_data) + 1) * row_h / 2, DOWN * (len(rows_data) + 1) * row_h / 2,
                                color=BLUE, stroke_width=1.5).move_to([x - 0.9, top_y - (len(rows_data) + 1) * row_h / 2, 0]))
        grid_lines[3].set_x(col_x[0] - 1.1)
        grid_lines[4].set_x(col_x[1])
        grid_lines[5].set_x(col_x[2] + 1.1)

        header.arrange(RIGHT, buff=0.8).scale(0.9)
        self.play(Create(grid_lines), run_time=1.0)
        for htxt, x in zip(header, col_x):
            htxt.move_to([x, top_y + 0.35, 0])
        self.play(*[Write(h) for h in header], run_time=1.0)

        # Day-15 punchline row written FIRST (answers "Plug in Day 15")
        r15 = VGroup(
            Text("15", font_size=30, color=CREAM).move_to([col_x[0], top_y - row_h, 0]),
            MathTex(r"2^{15} / 2^{30}", color=ORG).scale(0.62).move_to([col_x[1], top_y - row_h, 0]),
            Text("0.003%", font_size=30, color=ORG).move_to([col_x[2], top_y - row_h, 0]),
        )
        self.play(Write(r15[0]), Write(r15[1]), run_time=0.9)
        self.play(Write(r15[2]), run_time=0.7)

        # echo of the Shot-3 "Day 15?" caption as a small cream tag next to this row
        guess_tag = Text("Day 15?", font_size=26, color=CREAM).next_to(r15[2], RIGHT, buff=0.4)
        self.play(Write(guess_tag), run_time=0.8)

        # rows 25–30 fill down to the highlighted Day-29 and Day-30 rows
        for i, (d, frac, pct) in enumerate(rows_data[1:], start=1):
            y = top_y - (i + 1) * row_h
            cells = VGroup(
                Text(d, font_size=30, color=CREAM).move_to([col_x[0], y, 0]),
                MathTex(frac, color=ORG).scale(0.62).move_to([col_x[1], y, 0]),
            )
            if d == "29":
                pct_cell = Text(pct, font_size=30, color=ORG).move_to([col_x[2], y, 0])
            elif d == "30":
                pct_cell = Text(pct, font_size=30, color=CREAM).move_to([col_x[2], y, 0])
            else:
                pct_cell = Text(pct, font_size=30, color=CREAM).move_to([col_x[2], y, 0])
            cells.add(pct_cell)
            self.play(Write(cells[0]), Write(cells[1]), run_time=0.45)
            self.play(Write(cells[2]), run_time=0.35)

        # Day-29 row highlighted orange (the seed of Shot 7's reversal landing)
        hl = RoundedRectangle(corner_radius=0.08, width=6.6, height=row_h * 0.92,
                              color=ORG, stroke_width=3).move_to([col_x[1] - 0.45, top_y - 6 * row_h, 0])
        self.play(Create(hl), run_time=0.8)

        # ---- Hold: complete table with 0.003% and 50.0% both visible (out-state) ----
        # Tail hold — pads the scene to its beat duration (A/V sync fix).
        # X = SCENE_TARGET_SEC - current_animation_duration (~12 s of plays above)
        tail_hold = max(0.5, SCENE_TARGET_SEC - 12.0)  # TODO-AVSYNC: reconcile vs timing.json
        self.wait(tail_hold)
