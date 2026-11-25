"""Shot 5 — The formula, paired with the lily pad (Beat 4, part 1). Brief §5d.

Concrete <-> abstract pairing at first formula introduction: left = animated
lily pad doubling on a water surface; right = fraction(n) = 2^n / 2^30 in
orange, Written at exactly the moment the pad grows. Anchor note "Day 30 ->
full" appears with the exponent briefly highlighted (term-under-discussion).

Out-state: formula persists unchanged into Shot 6 (equation persistence; cut).

A/V sync: SCENE_TARGET_SEC placeholder until timing.json exists.
"""
from manimgx import *

config.background_color = "#0F172A"  # channel palette — mandatory in every scene file

BG    = "#0F172A"
CREAM = "#F2E3C6"
ORG   = "#F97316"
BLUE  = "#3B82F6"

# Beat 4 part 1 (formula intro): [1:40–~2:00]
SCENE_TARGET_SEC = 20.0  # TODO-AVSYNC: replace with value from timing.json


class Shot05Formula(Scene):
    def construct(self):
        # ---- In-state: water surface on the left (arrives from S4 zoom-out) ----
        water = Ellipse(width=4.6, height=3.2, color=BLUE, stroke_width=4).move_to([-3.0, -0.3, 0])
        self.play(Create(water), run_time=1.0)

        # Lily pad polygon growing on the surface (blue outline + cream center)
        pad = RegularPolygon(n=6, radius=0.5, color=BLUE, stroke_width=4,
                             fill_color=CREAM, fill_opacity=0.85).move_to([-3.0, -0.3, 0])
        self.play(GrowFromCenter(pad), run_time=1.0)

        # ---- Right: the formula in orange, written as the pad grows (same frame) ----
        eq = MathTex(r"\mathrm{fraction}(n)", "=", r"\dfrac{2^{n}}{2^{30}}", color=ORG).move_to([2.6, 0.4, 0])
        self.play(Write(eq), run_time=1.8)

        # Pad doubles once more while the formula is on screen (concrete echo)
        pad2 = RegularPolygon(n=6, radius=1.0, color=BLUE, stroke_width=4,
                              fill_color=CREAM, fill_opacity=0.85).move_to([-3.0, -0.3, 0])
        self.play(Transform(pad, pad2), run_time=1.2)

        # ---- "Full coverage happens on Day 30" — anchor note + exponent highlight ----
        anchor = Text("Day 30 -> full", font_size=34, color=CREAM).next_to(eq, DOWN, buff=0.6)
        self.play(Write(anchor), run_time=1.2)

        # term-under-discussion: thicken the orange stroke on 2^30 (zoom-to-highlight)
        eq_big = eq.copy().scale(1.15).set_color_by_tex("2^{30}", ORG)
        self.play(eq.animate.scale(1.15), run_time=0.6)
        self.play(Indicate(eq[2]), run_time=1.0)   # the 2^n / 2^30 term
        self.play(eq.animate.scale(1 / 1.15), run_time=0.6)

        # ---- Hold: formula + growing pad + anchor note persist (out-state for S6) ----
        # Tail hold — pads the scene to its beat duration (A/V sync fix).
        # X = SCENE_TARGET_SEC - current_animation_duration (~8 s of plays above)
        tail_hold = max(0.5, SCENE_TARGET_SEC - 8.0)  # TODO-AVSYNC: reconcile vs timing.json
        self.wait(tail_hold)
