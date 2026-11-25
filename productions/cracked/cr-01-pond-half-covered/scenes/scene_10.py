"""Shot 10 — Worked example quantification: one eighth at 9 am (Beat 7, part 3).

Same lab + dish (continuity from S9; cut). Confirms "11 am = half full" with a
persistent orange recap tag. Then the dish animates backward two more hours to
9 am and the colony shrinks to one eighth of the dish area; the fraction 1/8 is
Written in orange, paired at the same moment with the tiny colony speck
(concrete <-> abstract). The morning timeline stays visible with both markers
resolved: "11 am -> 50%" and "9 am -> 1/8".

Out-state: one-eighth dish + 1/8 holds as the final worked-example frame, then
full wipe A3 (act boundary Worked example -> Recap).

A/V sync: SCENE_TARGET_SEC placeholder until timing.json exists.
"""
from manimgx import *

config.background_color = "#0F172A"  # channel palette — mandatory in every scene file

BG    = "#0F172A"
CREAM = "#F2E3C6"
ORG   = "#F97316"
BLUE  = "#3B82F6"

# Beat 7 part 3 (one eighth at 9 am): [~3:35–3:55]
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


class Shot10LabEighth(Scene):
    def construct(self):
        # ---- In-state: inherit S9 — half-full dish at 11 am, timeline present (cut) ----
        bench = Line(LEFT * 5.4, RIGHT * 5.4, color=BLUE, stroke_width=4).move_to(DOWN * 1.6)
        dish = Circle(radius=1.7, color=BLUE, stroke_width=4).move_to([0, 0.2, 0])
        rim = Circle(radius=1.85, color=BLUE, stroke_width=1.5).move_to(dish.get_center())
        self.add(bench, dish, rim)

        import numpy as np
        def colony(n):
            g = VGroup()
            for i in range(n):
                a = (i / n) * TAU + (i % 4) * 0.35
                r = 1.35 * ((i % 5) / 4.0)
                g.add(Dot(radius=0.07, color=CREAM, fill_opacity=1).move_to(dish.get_center() + [r * np.cos(a), r * np.sin(a), 0]))
            return g

        half_colony = colony(14)
        self.add(half_colony)

        sci = make_scientist(scale=1.0, walking=False).move_to([4.6, -0.9, 0])
        self.add(sci)

        # timeline from S9 stays visible (both markers will be resolved here)
        tl_y = -2.7
        timeline = Line(np.array([-3.6, tl_y, 0]), np.array([3.6, tl_y, 0]), color=BLUE, stroke_width=3)
        self.add(timeline)
        x_of = {"9 am": -2.4, "10 am": -0.8, "11 am": 0.8, "noon": 2.4}
        for label in ("9 am", "10 am", "11 am", "noon"):
            tick = Line(np.array([x_of[label], tl_y - 0.15, 0]), np.array([x_of[label], tl_y + 0.15, 0]), color=BLUE, stroke_width=3)
            lab = Text(label, font_size=26, color=CREAM).next_to(tick, DOWN, buff=0.2)
            self.add(tick, lab)

        # ---- Confirm "11 am = half full": persistent orange recap tag beside the dish ----
        # Recap tag "11 am -> 50%" (orange). Single-backslash LaTeX space so the
        # \mathrm{am} renders as upright "am" instead of a stray line break.
        recap_tag = MathTex(r"11\ \mathrm{am}", r"\rightarrow", r"50\%", color=ORG).scale(0.9).move_to([3.4, 2.6, 0])
        self.play(Write(recap_tag), run_time=1.0)

        # ---- Quantify 9 am: dish animates backward two more hours; colony -> one eighth ----
        eighth_colony = colony(4)   # tiny speck in an almost empty dish
        self.play(Transform(half_colony, eighth_colony), run_time=1.4)  # object removal (geometric shrink)

        # fraction 1/8 Written in orange, paired at the same moment with the tiny colony
        frac = MathTex(r"\dfrac{1}{8}", color=ORG).scale(1.3).move_to([3.6, 0.2, 0])
        self.play(Write(frac), run_time=1.2)

        # ---- Timeline now shows both markers resolved: "11 am -> 50%" and "9 am -> 1/8" ----
        m11 = Dot(radius=0.12, color=ORG, fill_opacity=1).move_to([x_of["11 am"], tl_y, 0])
        t11 = Text("50%", font_size=26, color=ORG).next_to(m11, UP, buff=0.2)
        self.play(GrowFromCenter(m11), Write(t11), run_time=0.7)

        m9 = Dot(radius=0.12, color=ORG, fill_opacity=1).move_to([x_of["9 am"], tl_y, 0])
        t9 = Text("1/8", font_size=26, color=ORG).next_to(m9, UP, buff=0.2)
        self.play(GrowFromCenter(m9), Write(t9), run_time=0.7)

        # ---- Hold: one-eighth dish + 1/8 + full timeline with both resolved markers (out-state; wipe A3 after) ----
        # Tail hold — pads the scene to its beat duration (A/V sync fix).
        # X = SCENE_TARGET_SEC - current_animation_duration (~6 s of plays above)
        tail_hold = max(0.5, SCENE_TARGET_SEC - 6.0)  # TODO-AVSYNC: reconcile vs timing.json
        self.wait(tail_hold)
