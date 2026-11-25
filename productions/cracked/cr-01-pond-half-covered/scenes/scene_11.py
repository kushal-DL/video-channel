"""Shot 11 — Recap & payoff: the law + half/quarter/eighth (Beat 8, part 1).

Fresh after act-boundary wipe A3. Top-down pond centered again; a compact
backward-stepping strip shows three states side by side — Day 29 -> 1/2,
Day 28 -> 1/4, Day 27 -> 1/8 — each a small pond with its fraction in orange,
revealed left-to-right via Write() as they are spoken. The governing law is
stated as cream text (not a new formula).

A/V sync: SCENE_TARGET_SEC placeholder until timing.json exists.
"""
from manimgx import *

config.background_color = "#0F172A"  # channel palette — mandatory in every scene file

BG    = "#0F172A"
CREAM = "#F2E3C6"
ORG   = "#F97316"
BLUE  = "#3B82F6"

# Beat 8 part 1 (law + half/quarter/eighth): [3:55–4:20]
SCENE_TARGET_SEC = 25.0  # TODO-AVSYNC: replace with value from timing.json


def make_small_pond(width, height, center):
    """Canonical top-down oval pond at recap scale (continuity §3)."""
    water = Ellipse(width=width, height=height, color=BLUE, stroke_width=0,
                    fill_color=BG, fill_opacity=1)
    rim = Ellipse(width=width, height=height, color=BLUE, stroke_width=3.5)
    return VGroup(water, rim).move_to(center)


class Shot11Recap(Scene):
    def construct(self):
        # ---- In-state: fresh after wipe — three ponds drawn in sequence (Create) ----
        law = Text("One law governs both containers.", font_size=40, color=CREAM).to_edge(UP, buff=0.7)
        self.play(Write(law), run_time=1.6)

        centers = [-3.6, 0, 3.6]
        ponds = [make_small_pond(2.8, 1.9, [c, 0.1, 0]) for c in centers]
        self.play(Create(ponds[0][1]), Create(ponds[1][1]), Create(ponds[2][1]), run_time=1.2)

        # ---- Day 29 -> 1/2 (half coverage) ----
        half_fill = Rectangle(width=1.3, height=1.7, color=BLUE, stroke_width=0,
                              fill_color=CREAM, fill_opacity=0.85).move_to(ponds[0].get_center() + LEFT * 0.65)
        self.play(FadeIn(half_fill), run_time=0.8)
        frac1 = MathTex(r"\dfrac{1}{2}", color=ORG).scale(0.95).next_to(ponds[0], DOWN, buff=0.3)
        day1 = Text("Day 29", font_size=30, color=CREAM).next_to(frac1, DOWN, buff=0.2)
        self.play(Write(frac1), Write(day1), run_time=1.0)

        # ---- Day 28 -> 1/4 (quarter coverage) ----
        quarter_fill = Rectangle(width=0.7, height=1.6, color=BLUE, stroke_width=0,
                                 fill_color=CREAM, fill_opacity=0.85).move_to(ponds[1].get_center() + LEFT * 0.35)
        self.play(FadeIn(quarter_fill), run_time=0.8)
        frac2 = MathTex(r"\dfrac{1}{4}", color=ORG).scale(0.95).next_to(ponds[1], DOWN, buff=0.3)
        day2 = Text("Day 28", font_size=30, color=CREAM).next_to(frac2, DOWN, buff=0.2)
        self.play(Write(frac2), Write(day2), run_time=1.0)

        # ---- Day 27 -> 1/8 (eighth coverage — a small speck) ----
        eighth_fill = Rectangle(width=0.35, height=1.4, color=BLUE, stroke_width=0,
                                fill_color=CREAM, fill_opacity=0.85).move_to(ponds[2].get_center() + LEFT * 0.17)
        self.play(FadeIn(eighth_fill), run_time=0.8)
        frac3 = MathTex(r"\dfrac{1}{8}", color=ORG).scale(0.95).next_to(ponds[2], DOWN, buff=0.3)
        day3 = Text("Day 27", font_size=30, color=CREAM).next_to(frac3, DOWN, buff=0.2)
        self.play(Write(frac3), Write(day3), run_time=1.0)

        # ---- The governing law (cream text; the fractions are the on-screen symbols) ----
        rule = Text("The state right before the end holds half the final amount.", font_size=32, color=CREAM).to_edge(DOWN, buff=0.5)
        self.play(Write(rule), run_time=1.8)

        # ---- Hold: full half/quarter/eighth strip (out-state; cut into S12) ----
        # Tail hold — pads the scene to its beat duration (A/V sync fix).
        # X = SCENE_TARGET_SEC - current_animation_duration (~10 s of plays above)
        tail_hold = max(0.5, SCENE_TARGET_SEC - 10.0)  # TODO-AVSYNC: reconcile vs timing.json
        self.wait(tail_hold)
