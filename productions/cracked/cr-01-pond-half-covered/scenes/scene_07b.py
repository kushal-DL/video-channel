"""Shot 7b — Dedicated result shot (Beat 6, full). Director decision D1.

Carries Beat 6's full narration ("The pond was half-covered on Day 29...") over
its own >=6 s hold. The halved pond from S7 persists at left; a large result
card is Written beside it: "Day 29 = 50%" (orange numeral on cream text).

Transitions: S7 -> S7b cut (same scene continues, halved pond persists);
S7b -> S8 full wipe A2 (act boundary Build-up -> Worked example) fires after
this hold.

A/V sync: SCENE_TARGET_SEC placeholder until timing.json exists; the tail hold
is the beat's landing frame and must stay >= 6 s of active content.
"""
from manimgx import *

config.background_color = "#0F172A"  # channel palette — mandatory in every scene file

BG    = "#0F172A"
CREAM = "#F2E3C6"
ORG   = "#F97316"
BLUE  = "#3B82F6"

# Beat 6 (Result): [2:40–3:00] — D1 requires its own >=6 s active hold.
SCENE_TARGET_SEC = 20.0  # TODO-AVSYNC: replace with value from timing.json


def make_pond(width, height, center):
    """Canonical top-down oval pond (continuity §3)."""
    water = Ellipse(width=width, height=height, color=BLUE, stroke_width=0,
                    fill_color=BG, fill_opacity=1)
    rim = Ellipse(width=width, height=height, color=BLUE, stroke_width=4)
    return VGroup(water, rim).move_to(center)


def make_pad_field(pond_center, rx, ry, n=26):
    """Lily pad field filling an oval (blue outline + cream center)."""
    import numpy as np
    field = VGroup()
    for i in range(n):
        a = (i / n) * TAU + (i % 5) * 0.21
        r = 0.9 * ((i % 6) / 5.0)
        x = rx * np.cos(a) * r
        y = ry * np.sin(a) * r
        field.add(Circle(radius=0.34, color=BLUE, stroke_width=2.5,
                         fill_color=CREAM, fill_opacity=0.85).move_to(pond_center + [x, y, 0]))
    return field


class Shot07bResult(Scene):
    def construct(self):
        # ---- In-state: cut from S7 — halved pond persists at left ----
        main_pond = make_pond(4.8, 3.0, [-2.6, -0.5, 0])
        self.add(main_pond)
        field = make_pad_field(main_pond.get_center(), 2.0, 1.2)
        # only the left half remains (S7's halved state)
        kept = VGroup(*[p for p in field if p.get_center()[0] < main_pond.get_center()[0]])
        self.add(kept)

        day29_label = Text("Day 29", font_size=44, color=CREAM).next_to(main_pond, UP, buff=0.5)
        pct50 = MathTex(r"50\%", color=ORG).scale(1.3).move_to(main_pond.get_center() + LEFT * 1.0)
        self.add(day29_label, pct50)

        # ---- The result card: "Day 29 = 50%" — orange numeral on cream text ----
        card_bg = RoundedRectangle(corner_radius=0.2, width=4.6, height=2.2,
                                   color=CREAM, stroke_width=3).move_to([2.7, 0.4, 0])
        self.play(FadeIn(card_bg), run_time=0.5)

        card_day = Text("Day 29", font_size=64, color=CREAM).move_to([2.7, 1.0, 0])
        card_eq = MathTex(r"=", color=ORG).scale(1.3).move_to([2.7, 0.15, 0])
        card_pct = Text("50%", font_size=64, color=ORG).move_to([2.7, -0.85, 0])
        self.play(Write(card_day), run_time=1.0)
        self.play(Write(card_eq), run_time=0.5)
        self.play(Write(card_pct), run_time=1.0)

        # ---- Hold (>=6 s of active content): halved pond + result card persist ----
        # Tail hold — pads the scene to its beat duration (A/V sync fix).
        # X = SCENE_TARGET_SEC - current_animation_duration (~3.5 s of plays above);
        # D1 requires this landing hold to be >= 6 s, so floor it at 6.0.
        tail_hold = max(6.0, SCENE_TARGET_SEC - 3.5)  # TODO-AVSYNC: reconcile vs timing.json
        self.wait(tail_hold)
