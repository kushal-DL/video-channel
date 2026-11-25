"""Shot 7 — One-step-back reversal + generalization (Beat 5, full). Brief §5c.

Start: top-down pond fully covered, labeled Day 30 with a 100% overlay.
Reverse one step: half the pads clear away (geometric reveal via FadeOut of pad
shapes only — removing concrete objects, not math), label morphs to Day 29 and
a 50% overlay appears in orange over the remaining half. Then the generalization
(D2, visual-light): a second smaller pond (same canonical oval at smaller scale)
does the same halving: full at Day 20 -> half at Day 19. It must not outstage
the main reversal.

Out-state: Day-30/Day-29 pond pair with 50% overlay + the 20-day pond's half
state — the active hold frame (cut into Shot 7b).

A/V sync: SCENE_TARGET_SEC placeholder until timing.json exists.
"""
from manimgx import *

config.background_color = "#0F172A"  # channel palette — mandatory in every scene file

BG    = "#0F172A"
CREAM = "#F2E3C6"
ORG   = "#F97316"
BLUE  = "#3B82F6"

# Beat 5 (full): [2:10–2:40]
SCENE_TARGET_SEC = 30.0  # TODO-AVSYNC: replace with value from timing.json


def make_pond(width, height, center):
    """Canonical top-down oval pond at the given scale (continuity §3)."""
    water = Ellipse(width=width, height=height, color=BLUE, stroke_width=0,
                    fill_color=BG, fill_opacity=1)
    rim = Ellipse(width=width, height=height, color=BLUE, stroke_width=4)
    pond = VGroup(water, rim).move_to(center)
    return pond


def make_pad_field(pond_center, rx, ry, n=26):
    """A field of lily pads filling an oval (blue outline + cream center)."""
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


class Shot07OneStepBack(Scene):
    def construct(self):
        # ---- In-state: centered pond fully covered at Day 30 (from S6 slide) ----
        main_pond = make_pond(4.8, 3.0, [-1.2, -0.5, 0])
        self.play(Create(main_pond[1]), run_time=0.9)
        field = make_pad_field(main_pond.get_center(), 2.0, 1.2)
        self.play(GrowFromCenter(field), run_time=1.2)

        day30_label = Text("Day 30", font_size=44, color=CREAM).next_to(main_pond, UP, buff=0.5)
        pct100 = MathTex(r"100\%", color=ORG).scale(1.2).move_to(main_pond.get_center())
        self.play(Write(day30_label), run_time=0.8)
        self.play(Write(pct100), run_time=0.8)

        # ---- Reverse one step: half the pads clear away (geometric reveal) ----
        import numpy as np
        left_pads, right_pads = VGroup(), VGroup()
        for pad in field:
            if pad.get_center()[0] < main_pond.get_center()[0]:
                left_pads.add(pad)
            else:
                right_pads.add(pad)
        self.play(FadeOut(right_pads), run_time=1.4)   # pads clearing = removing concrete objects

        # label morphs Day 30 -> Day 29 (Transform, not fade-swap) + 50% overlay in orange
        day29_label = Text("Day 29", font_size=44, color=CREAM).move_to(day30_label.get_center())
        self.play(Transform(day30_label, day29_label), run_time=0.8)
        pct50 = MathTex(r"50\%", color=ORG).scale(1.3).move_to(main_pond.get_center() + LEFT * 1.0)
        self.play(FadeOut(pct100), run_time=0.4)
        self.play(Write(pct50), run_time=1.0)

        # ---- Generalization (D2, visual-light): a smaller 20-day pond does the same ----
        small_pond = make_pond(3.0, 1.9, [3.4, -0.7, 0])   # same oval, smaller scale — must not outstage main
        self.play(Create(small_pond[1]), run_time=0.8)
        s_field = make_pad_field(small_pond.get_center(), 1.25, 0.78, n=16)
        self.play(GrowFromCenter(s_field), run_time=0.9)

        day20_label = Text("Day 20", font_size=34, color=CREAM).next_to(small_pond, UP, buff=0.4)
        s_pct100 = MathTex(r"100\%", color=ORG).scale(0.9).move_to(small_pond.get_center())
        self.play(Write(day20_label), Write(s_pct100), run_time=0.8)

        # same container-halving grammar: one backward step -> half at Day 19
        s_left, s_right = VGroup(), VGroup()
        for pad in s_field:
            if pad.get_center()[0] < small_pond.get_center()[0]:
                s_left.add(pad)
            else:
                s_right.add(pad)
        self.play(FadeOut(s_right), run_time=1.0)
        day19_label = Text("Day 19", font_size=34, color=CREAM).move_to(day20_label.get_center())
        self.play(Transform(day20_label, day19_label), run_time=0.7)
        s_pct50 = MathTex(r"50\%", color=ORG).scale(0.95).move_to(small_pond.get_center() + LEFT * 0.6)
        self.play(FadeOut(s_pct100), run_time=0.3)
        self.play(Write(s_pct50), run_time=0.8)

        # ---- Hold: both halved ponds on screen (out-state; cut into S7b) ----
        # Tail hold — pads the scene to its beat duration (A/V sync fix).
        # X = SCENE_TARGET_SEC - current_animation_duration (~12 s of plays above)
        tail_hold = max(0.5, SCENE_TARGET_SEC - 12.0)  # TODO-AVSYNC: reconcile vs timing.json
        self.wait(tail_hold)
