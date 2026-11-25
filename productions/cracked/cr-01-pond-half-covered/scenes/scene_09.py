"""Shot 9 — Worked example question + one-step-back rule (Beat 7, part 2).

Same lab + petri dish (continuity from S8; cut transition). The question is
written in cream. A morning timeline strip marks the hours: the naive guess at
9 am is drawn first with a faint half-fill hint, then visually set aside. The
rule is applied — the dish animates backward one hour from noon, the colony
halves, and a marker lands on 11 am with a 50% overlay in orange (mirroring
Shot 7's pond reversal: same container-halving motif, new domain).

A/V sync: SCENE_TARGET_SEC placeholder until timing.json exists.
"""
from manimgx import *

config.background_color = "#0F172A"  # channel palette — mandatory in every scene file

BG    = "#0F172A"
CREAM = "#F2E3C6"
ORG   = "#F97316"
BLUE  = "#3B82F6"

# Beat 7 part 2 (question + rule -> 11 am): [~3:20–3:35]
SCENE_TARGET_SEC = 15.0  # TODO-AVSYNC: replace with value from timing.json


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


class Shot09LabQuestion(Scene):
    def construct(self):
        # ---- In-state: inherit S8 — full dish at noon, scientist, clock chip (cut) ----
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

        full = colony(28)
        self.add(full)

        sci = make_scientist(scale=1.0, walking=False).move_to([4.6, -0.9, 0])
        self.add(sci)

        chip_bg = RoundedRectangle(corner_radius=0.12, width=1.5, height=0.6,
                                   color=CREAM, stroke_width=2).to_corner(UR, buff=0.5)
        clock_txt = Text("noon", font_size=34, color=ORG).move_to(chip_bg.get_center())
        self.add(VGroup(chip_bg, clock_txt))

        # ---- The question (cream) ----
        question = Text("When was the dish half full?", font_size=40, color=CREAM).to_edge(UP, buff=0.6)
        self.play(Write(question), run_time=1.4)

        # ---- Morning timeline strip below the dish (geometry: Create) ----
        tl_y = -2.7
        timeline = Line(np.array([-3.6, tl_y, 0]), np.array([3.6, tl_y, 0]), color=BLUE, stroke_width=3)
        self.play(Create(timeline), run_time=0.8)

        # hour ticks: 9 am ... noon (positions spread across the strip)
        x_of = {"9 am": -2.4, "10 am": -0.8, "11 am": 0.8, "noon": 2.4}
        for label in ("9 am", "10 am", "11 am", "noon"):
            tick = Line(np.array([x_of[label], tl_y - 0.15, 0]), np.array([x_of[label], tl_y + 0.15, 0]), color=BLUE, stroke_width=3)
            lab = Text(label, font_size=26, color=CREAM).next_to(tick, DOWN, buff=0.2)
            self.play(Create(tick), Write(lab), run_time=0.4)

        # ---- Naive guess first: marker at 9 am with a faint half-fill hint ----
        naive_marker = Dot(radius=0.12, color=CREAM, fill_opacity=1).move_to([x_of["9 am"], tl_y, 0])
        self.play(GrowFromCenter(naive_marker), run_time=0.5)
        # faint half-fill hint inside the dish (geometry, low opacity — not a math symbol)
        half_hint = Rectangle(width=1.6, height=3.2, color=CREAM, stroke_width=0,
                              fill_color=CREAM, fill_opacity=0.18).move_to(dish.get_center() + LEFT * 0.85)
        self.play(FadeIn(half_hint), run_time=0.6)

        # ---- The rule applied: dish animates backward one hour; colony halves ----
        half_colony = colony(14)
        self.play(Transform(full, half_colony), run_time=1.2)   # object removal (geometric halving)
        self.play(FadeOut(half_hint), run_time=0.4)

        # marker lands on 11 am with a 50% overlay in orange over the half-filled dish
        rule_marker = Dot(radius=0.12, color=ORG, fill_opacity=1).move_to([x_of["11 am"], tl_y, 0])
        self.play(GrowFromCenter(rule_marker), run_time=0.5)
        pct50 = MathTex(r"50\%", color=ORG).scale(1.2).next_to(dish, UP, buff=0.45)
        self.play(Write(pct50), run_time=0.9)

        # ---- The naive 9 am guess is visually set aside (fade its marker, not math) ----
        self.play(naive_marker.animate.set_opacity(0.3), run_time=0.6)

        # ---- Hold: half-filled dish at 11 am + 50% overlay; 9 am marker set aside (out-state for S10) ----
        # Tail hold — pads the scene to its beat duration (A/V sync fix).
        # X = SCENE_TARGET_SEC - current_animation_duration (~9 s of plays above)
        tail_hold = max(0.5, SCENE_TARGET_SEC - 9.0)  # TODO-AVSYNC: reconcile vs timing.json
        self.wait(tail_hold)
