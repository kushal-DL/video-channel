"""Shot 2 — Hook climax, Day 30 + riddle (Beat 1, part 2).

Inherits Shot 1's out-state (Day-15 pond + counter chip; cut transition).
Pads cascade to full bank-to-bank coverage, counter ticks Day 30, scientist
stops at the water's edge and stares; the riddle is written in cream below.
Out-state: fully covered pond + stopped scientist + riddle line hold as the
final hook frame (act-boundary wipe A1 fires after this scene).

A/V sync: SCENE_TARGET_SEC placeholder until timing.json exists.
"""
from manimgx import *

config.background_color = "#0F172A"  # channel palette — mandatory in every scene file

BG    = "#0F172A"
CREAM = "#F2E3C6"
ORG   = "#F97316"
BLUE  = "#3B82F6"

# Beat 1 part 2 (Day 30 + riddle): [~0:20–0:35]
# AVSYNC: S1 carries the full Beat-1 hold; S2 only needs its own tail.
SCENE_TARGET_SEC = 15.0


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


class Shot02HookClimax(Scene):
    def construct(self):
        # ---- In-state: inherit Day-15 pond + counter chip (cut from S1) ----
        pond = make_pond().move_to(DOWN * 0.55)
        self.add(pond)

        day15_pads = VGroup(
            make_pad(radius=0.2).move_to(pond.get_center() + LEFT * 1.8 + DOWN * 0.5),
            make_pad(radius=0.16).move_to(pond.get_center() + RIGHT * 0.4 + UP * 0.7),
            make_pad(radius=0.18).move_to(pond.get_center() + RIGHT * 1.2 + DOWN * 0.3),
        )
        self.add(day15_pads)

        chip_bg = RoundedRectangle(corner_radius=0.12, width=1.4, height=0.55,
                                   color=CREAM, stroke_width=2).to_corner(UL, buff=0.5)
        chip_txt = Text("Day 15", font_size=30, color=ORG).move_to(chip_bg.get_center())
        self.add(VGroup(chip_bg, chip_txt))

        # ---- Scientist re-enters from left and walks to the right bank ----
        path_y = 3.4
        scientist = make_scientist(scale=1.0, walking=True).move_to([-6.8, path_y, 0])
        self.play(FadeIn(scientist), run_time=0.4)
        self.play(scientist.animate.move_to([2.9, path_y, 0]), run_time=3.5)

        # ---- Day 30: pads cascade until the whole oval is covered ----
        # Counter tick to Day 30 (storyboard: ticks use Write()).
        # Fade the old label out and Write a fresh centered "Day 30" so the
        # numeral is guaranteed legible in the hold frame.
        day30_txt = Text("Day 30", font_size=30, color=ORG).move_to(chip_bg.get_center())
        self.play(FadeOut(chip_txt), run_time=0.25)
        self.play(Write(day30_txt), run_time=0.6)

        field = VGroup()
        import numpy as np
        for i in range(48):
            a = (i / 48) * TAU + (i % 5) * 0.17          # deterministic scatter
            r = 0.92 * ((i % 7) / 6.0)                    # ring radius fraction
            x = 2.35 * np.cos(a) * r
            y = 1.35 * np.sin(a) * r
            field.add(make_pad(radius=0.42 + (i % 3) * 0.08).move_to(pond.get_center() + [x, y, 0]))
        # GrowFromCenter cascade in three waves
        for i in range(0, len(field), 16):
            wave = VGroup(*field[i:i + 16])
            self.play(GrowFromCenter(wave), run_time=1.2)

        # Single filled overlay so "bank to bank" reads clearly (geometry fill)
        full_overlay = Ellipse(width=5.4, height=3.0, color=BLUE, stroke_width=0,
                               fill_color=CREAM, fill_opacity=0.85).move_to(pond.get_center())
        self.play(FadeIn(full_overlay), run_time=1.2)

        # ---- She stops at the water's edge and stares (feet together) ----
        standing = make_scientist(scale=1.0, walking=False).move_to([3.6, 1.9, 0])
        self.play(FadeOut(scientist), run_time=0.25)
        self.play(Write(standing[0]), Write(standing[1]), Create(standing[2]), run_time=0.8)

        # ---- The riddle (cream, centered below the pond; no clickbait styling) ----
        riddle = Text("On which day was the pond half-covered?", font_size=40, color=CREAM)
        riddle.next_to(pond, DOWN, buff=0.55)
        self.play(Write(riddle), run_time=1.6)

        # Tail hold — pads the scene to its beat duration (A/V sync fix).
        # manimgx 0.1.1: self.wait() emits no frames; use an explicit play-hold.
        tail_hold = max(0.5, SCENE_TARGET_SEC - 12.0)
        self.play(Indicate(riddle, scale_factor=1.0, color=CREAM), run_time=tail_hold)
