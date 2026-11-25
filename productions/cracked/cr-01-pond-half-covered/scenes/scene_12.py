"""Shot 12 — Payoff close: Day 30 walk with new perspective (Beat 8, part 2).

Bookend of the hook. The scientist walks past the fully covered pond again and
stops to look at it "with a new perspective" (calmer framing than Shot 2). A
final caption line is Written in cream — "nearly nothing, then half, then
everything." — with three small icons beside it: empty speck -> half-covered ->
full pond (blue geometry), tying the visual motif to the closing words.

Out-state: final frame holds on scientist + full pond + caption; episode ends
(editor handles fade-to-black in assembly). No out-transition needed.

A/V sync: SCENE_TARGET_SEC placeholder until timing.json exists.
"""
from manimgx import *

config.background_color = "#0F172A"  # channel palette — mandatory in every scene file

BG    = "#0F172A"
CREAM = "#F2E3C6"
ORG   = "#F97316"
BLUE  = "#3B82F6"

# Beat 8 part 2 (Day-30 walk close): [~4:20–4:40]
SCENE_TARGET_SEC = 20.0  # TODO-AVSYNC: replace with value from timing.json


def make_scientist(scale=1.0, walking=True):
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


def make_pond(width=5.4, height=3.0):
    """Canonical top-down pond (continuity §3)."""
    water = Ellipse(width=width, height=height, color=BLUE, stroke_width=0,
                    fill_color=BG, fill_opacity=1)
    rim = Ellipse(width=width, height=height, color=BLUE, stroke_width=4)
    return VGroup(water, rim)


def make_pad(radius=0.22):
    """Lily pad: blue outline + cream center."""
    return Circle(radius=radius, color=BLUE, stroke_width=3,
                  fill_color=CREAM, fill_opacity=0.85)


class Shot12PayoffClose(Scene):
    def construct(self):
        # ---- In-state: arrives from S11 — single full pond; scientist enters along top path ----
        pond = make_pond().move_to(DOWN * 0.7)
        self.play(Create(pond[1]), run_time=1.0)

        import numpy as np
        field = VGroup()
        for i in range(48):
            a = (i / 48) * TAU + (i % 5) * 0.17
            r = 0.92 * ((i % 7) / 6.0)
            x = 2.35 * np.cos(a) * r
            y = 1.35 * np.sin(a) * r
            field.add(make_pad(radius=0.42 + (i % 3) * 0.08).move_to(pond.get_center() + [x, y, 0]))
        for i in range(0, len(field), 16):
            self.play(GrowFromCenter(VGroup(*field[i:i + 16])), run_time=1.0)

        # ---- The scientist walks past the fully covered pond (same top path as S1–S2) ----
        path_y = 3.4
        scientist = make_scientist(scale=1.0, walking=True).move_to([-6.8, path_y, 0])
        self.play(FadeIn(scientist), run_time=0.4)

        # she stops and looks — now with a new perspective (calmer framing than S2)
        self.play(scientist.animate.move_to([3.6, 1.7, 0]), run_time=3.5)
        standing = make_scientist(scale=1.0, walking=False).move_to([3.6, 1.7, 0])
        self.play(FadeOut(scientist), run_time=0.25)
        self.play(Write(standing[0]), Write(standing[1]), Create(standing[2]), run_time=0.8)

        # ---- Closing caption (cream) + three-icon strip: empty -> half -> full ----
        caption = Text("nearly nothing, then half, then everything.", font_size=40, color=CREAM).move_to([0, -3.6, 0])
        self.play(Write(caption), run_time=1.8)

        # three small icons (blue geometry): empty speck -> half-covered -> full
        icon_y = -2.9
        # icon 1: empty pond with a tiny speck
        i1_pond = Ellipse(width=0.9, height=0.6, color=BLUE, stroke_width=3).move_to([-2.4, icon_y, 0])
        i1_speck = Circle(radius=0.05, color=CREAM, fill_opacity=1).move_to(i1_pond.get_center())
        # icon 2: half-covered pond (left half filled)
        i2_pond = Ellipse(width=0.9, height=0.6, color=BLUE, stroke_width=3).move_to([0, icon_y, 0])
        i2_fill = Rectangle(width=0.42, height=0.5, color=BLUE, stroke_width=0,
                            fill_color=CREAM, fill_opacity=0.85).move_to(i2_pond.get_center() + LEFT * 0.21)
        # icon 3: full pond (filled)
        i3_pond = Ellipse(width=0.9, height=0.6, color=BLUE, stroke_width=3,
                          fill_color=CREAM, fill_opacity=0.85).move_to([2.4, icon_y, 0])

        self.play(Create(i1_pond), GrowFromCenter(i1_speck), run_time=0.7)
        self.play(Create(i2_pond), FadeIn(i2_fill), run_time=0.7)
        self.play(FadeIn(i3_pond), run_time=0.7)

        # ---- Hold: scientist + full pond + caption with three-icon strip (final frame; no out-transition) ----
        # Tail hold — pads the scene to its beat duration (A/V sync fix).
        # X = SCENE_TARGET_SEC - current_animation_duration (~12 s of plays above)
        tail_hold = max(0.5, SCENE_TARGET_SEC - 12.0)  # TODO-AVSYNC: reconcile vs timing.json
        self.wait(tail_hold)
