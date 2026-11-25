"""Shot 4 — Split-screen linear vs exponential fill (Beat 3, full). Brief §5a.

Two oval ponds side by side (canonical shape), each filling over the same
thirty days under ONE shared day counter at top center. Left fills in equal
slices (progress-bar feel); right stays nearly empty then explodes in the
final five days. NO on-screen "linear"/"exponential" words during this shot
(D3: panels shown before naming; names already introduced in Shot 3).

A/V sync: SCENE_TARGET_SEC placeholder until timing.json exists.
"""
from manimgx import *

config.background_color = "#0F172A"  # channel palette — mandatory in every scene file

BG    = "#0F172A"
CREAM = "#F2E3C6"
ORG   = "#F97316"
BLUE  = "#3B82F6"

# Beat 3 (full): [1:05–1:40]
SCENE_TARGET_SEC = 35.0  # TODO-AVSYNC: replace with value from timing.json


def make_pond(width=4.2, height=2.6):
    """Canonical top-down pond at split-screen scale (continuity §3)."""
    water = Ellipse(width=width, height=height, color=BLUE, stroke_width=0,
                    fill_color=BG, fill_opacity=1)
    rim = Ellipse(width=width, height=height, color=BLUE, stroke_width=4)
    return VGroup(water, rim), water


class Shot04SplitScreen(Scene):
    def construct(self):
        # ---- In-state: two ponds + shared day counter (arrives from S3 slide+zoom) ----
        left_pond, l_water = make_pond()
        right_pond, r_water = make_pond()
        left_pond.move_to([-2.75, -0.4, 0])
        right_pond.move_to([2.75, -0.4, 0])

        chip_bg = RoundedRectangle(corner_radius=0.12, width=1.6, height=0.6,
                                   color=CREAM, stroke_width=2).move_to(UP * 3.2)
        chip_txt = Text("Day 1", font_size=34, color=ORG).move_to(chip_bg.get_center())

        self.play(Create(left_pond[1]), Create(right_pond[1]), run_time=1.0)
        self.add(l_water, r_water)
        self.play(FadeIn(chip_bg), Write(chip_txt), run_time=0.6)

        def set_counter(n):
            return Text(f"Day {n}", font_size=34, color=ORG).move_to(chip_bg.get_center())

        # ---- Left pond: identical slice every morning (progress-bar feel) ----
        # Right pond: nearly empty until ~Day 25, then explodes in five days.
        l_fill = Rectangle(width=0.01, height=0.01, color=BLUE, stroke_width=0,
                           fill_color=BLUE, fill_opacity=0.45).move_to(left_pond.get_center())

        # Day 1–9: left rises in equal steps; right stays nearly bare (one tiny pad)
        for d in range(2, 10):
            h = 2.3 * d / 30.0
            new_l = Rectangle(width=3.8, height=h, color=BLUE, stroke_width=0,
                              fill_color=BLUE, fill_opacity=0.45).move_to(left_pond.get_center())
            self.play(Transform(l_fill, new_l), run_time=0.28)
            chip_txt_become = set_counter(d)
            self.play(Transform(chip_txt, chip_txt_become), run_time=0.15)

        tiny_pad = Circle(radius=0.14, color=BLUE, stroke_width=3, fill_color=CREAM,
                          fill_opacity=0.85).move_to(right_pond.get_center() + LEFT * 0.6)
        self.play(GrowFromCenter(tiny_pad), run_time=0.5)

        # ---- "On Day 10, both ponds look nearly bare" — counter pauses on Day 10 ----
        h = 2.3 * 10 / 30.0
        new_l = Rectangle(width=3.8, height=h, color=BLUE, stroke_width=0,
                          fill_color=BLUE, fill_opacity=0.45).move_to(left_pond.get_center())
        self.play(Transform(l_fill, new_l), run_time=0.4)
        self.play(Indicate(chip_txt), run_time=0.8)
        self.wait(1.2)

        # ---- Day 11–24: left keeps its steady climb; right barely changes ----
        for d in range(11, 25):
            h = 2.3 * d / 30.0
            new_l = Rectangle(width=3.8, height=h, color=BLUE, stroke_width=0,
                              fill_color=BLUE, fill_opacity=0.45).move_to(left_pond.get_center())
            self.play(Transform(l_fill, new_l), run_time=0.22)
            chip_txt_become = set_counter(d)
            self.play(Transform(chip_txt, chip_txt_become), run_time=0.12)

        # ---- Day 25–30: right explodes to full over the final five days ----
        r_fill = Rectangle(width=0.01, height=0.01, color=BLUE, stroke_width=0,
                           fill_color=CREAM, fill_opacity=0.8).move_to(right_pond.get_center())
        for d in range(25, 31):
            frac = (d - 24) / 6.0                      # surge: ~0 at day 24 -> full at day 30
            h = max(0.05, 2.3 * min(1.0, frac))
            new_r = Rectangle(width=3.8, height=h, color=BLUE, stroke_width=0,
                              fill_color=CREAM, fill_opacity=0.8).move_to(right_pond.get_center())
            h_l = 2.3 * d / 30.0
            new_l = Rectangle(width=3.8, height=h_l, color=BLUE, stroke_width=0,
                              fill_color=BLUE, fill_opacity=0.45).move_to(left_pond.get_center())
            self.play(Transform(r_fill, new_r), Transform(l_fill, new_l), run_time=0.7)
            chip_txt_become = set_counter(d)
            self.play(Transform(chip_txt, chip_txt_become), run_time=0.25)

        # ---- Hold: Day 30 state — left smoothly full, right exploded to full ----
        # Tail hold — pads the scene to its beat duration (A/V sync fix).
        # X = SCENE_TARGET_SEC - current_animation_duration (~17 s of plays above)
        tail_hold = max(0.5, SCENE_TARGET_SEC - 17.0)  # TODO-AVSYNC: reconcile vs timing.json
        self.wait(tail_hold)
