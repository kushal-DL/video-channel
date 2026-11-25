"""Shot 8 — Worked example setup: bacteria in the lab (Beat 7, part 1).

Fresh after act-boundary wipe A2. New scene — the lab: bench line across the
frame, scientist figure at right (same minimal design as Shots 1–2), glass
petri dish centered with a bacterial colony of small cream dots that double in
count each hour tick. Clock chip ticks by the hour; at "filling the dish
completely at noon" the colony fills the dish and the clock reads noon with a
100% tag (orange numeral).

A/V sync: SCENE_TARGET_SEC placeholder until timing.json exists.
"""
from manimgx import *

config.background_color = "#0F172A"  # channel palette — mandatory in every scene file

BG    = "#0F172A"
CREAM = "#F2E3C6"
ORG   = "#F97316"
BLUE  = "#3B82F6"

# Beat 7 part 1 (lab setup): [3:00–~3:20]
SCENE_TARGET_SEC = 20.0  # TODO-AVSYNC: replace with value from timing.json


def make_scientist(scale=1.0, walking=False):
    """Shared minimal scientist figure (continuity.md §1) — identical in all scenes."""
    s = scale
    body = RoundedRectangle(corner_radius=0.14 * s, width=0.28 * s, height=0.56 * s,
                            color=CREAM, stroke_width=3)
    head = Circle(radius=0.14 * s, color=CREAM, stroke_width=3)
    head.move_to(body.get_top() + UP * 0.17 * s)
    coat = Line(LEFT * 0.12 * s, RIGHT * 0.12 * s, color=CREAM, stroke_width=2.5)
    coat.next_to(body.get_top(), DOWN, buff=0.08 * s)
    fig = VGroup(body, head, coat)
    if walking:
        f1 = Line(ORIGIN, LEFT * 0.09 * s + DOWN * 0.12 * s, color=CREAM, stroke_width=2.5)
        f2 = Line(ORIGIN, RIGHT * 0.09 * s + DOWN * 0.12 * s, color=CREAM, stroke_width=2.5)
        f1.move_to(body.get_bottom() + LEFT * 0.06 * s)
        f2.move_to(body.get_bottom() + RIGHT * 0.06 * s)
        fig.add(f1, f2)
    return fig


class Shot08LabSetup(Scene):
    def construct(self):
        # ---- In-state: fresh after wipe — bench and dish drawn in (Create) ----
        bench = Line(LEFT * 5.4, RIGHT * 5.4, color=BLUE, stroke_width=4).move_to(DOWN * 1.6)
        self.play(Create(bench), run_time=0.8)

        # glass petri dish: circle with blue outline + thin rim (concrete container)
        dish = Circle(radius=1.7, color=BLUE, stroke_width=4).move_to(UP * 0.2)
        rim = Circle(radius=1.85, color=BLUE, stroke_width=1.5).move_to(dish.get_center())
        self.play(Create(dish), Create(rim), run_time=1.0)

        # scientist stands at the right side (same minimal design as Shots 1–2)
        sci = make_scientist(scale=1.0, walking=False).move_to([4.6, -0.9, 0])
        self.play(Write(sci[0]), Write(sci[1]), Create(sci[2]), run_time=0.8)

        # clock chip in the upper area (same visual treatment as day counter)
        chip_bg = RoundedRectangle(corner_radius=0.12, width=1.5, height=0.6,
                                   color=CREAM, stroke_width=2).to_corner(UR, buff=0.5)
        clock_txt = Text("9 am", font_size=34, color=ORG).move_to(chip_bg.get_center())
        self.play(FadeIn(chip_bg), Write(clock_txt), run_time=0.6)

        # ---- Colony doubles in count each hour tick (small cream dots) ----
        import numpy as np
        def colony(n):
            g = VGroup()
            for i in range(n):
                a = (i / n) * TAU + (i % 4) * 0.35
                r = 1.35 * ((i % 5) / 4.0)
                g.add(Dot(radius=0.07, color=CREAM, fill_opacity=1).move_to(dish.get_center() + [r * np.cos(a), r * np.sin(a), 0]))
            return g

        c = colony(2)
        self.play(GrowFromCenter(c), run_time=0.6)

        # hour ticks: 9 am -> 10 am -> 11 am -> noon, doubling each time
        for label, n in (("10 am", 4), ("11 am", 8)):
            new_c = colony(n)
            self.play(Transform(c, new_c), run_time=0.9)
            self.play(Transform(clock_txt, Text(label, font_size=34, color=ORG).move_to(chip_bg.get_center())), run_time=0.5)

        # "filling the dish completely at noon" — colony fills the dish
        full = colony(28)
        self.play(Transform(c, full), run_time=1.2)
        self.play(Transform(clock_txt, Text("noon", font_size=34, color=ORG).move_to(chip_bg.get_center())), run_time=0.5)

        # 100% tag (orange numeral) over the full dish
        pct100 = MathTex(r"100\%", color=ORG).scale(1.2).next_to(dish, UP, buff=0.45)
        self.play(Write(pct100), run_time=0.9)

        # ---- Hold: bench + scientist + full dish at noon with 100% tag (out-state for S9) ----
        # Tail hold — pads the scene to its beat duration (A/V sync fix).
        # X = SCENE_TARGET_SEC - current_animation_duration (~8 s of plays above)
        tail_hold = max(0.5, SCENE_TARGET_SEC - 8.0)  # TODO-AVSYNC: reconcile vs timing.json
        self.wait(tail_hold)
