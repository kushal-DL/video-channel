"""Shot 3 — Motivation: linear intuition vs exponential reality (Beat 2, full).

Fresh after act-boundary wipe A1. Two-part layout on screen simultaneously
(concrete <-> abstract pairing): left = dripping tap filling a cup in equal
steps; right = "linear growth" / "exponential growth" labels with step bars
and a tiny lily pad quietly doubling each tick. The Day-15 guess is echoed as
a cream caption near the top (no X mark, no red).

A/V sync: SCENE_TARGET_SEC placeholder until timing.json exists.
"""
from manimgx import *

config.background_color = "#0F172A"  # channel palette — mandatory in every scene file

BG    = "#0F172A"
CREAM = "#F2E3C6"
ORG   = "#F97316"
BLUE  = "#3B82F6"

# Beat 2 (full): [0:35–1:05] — AVSYNC: target = Beat-2 audio duration (28.512 s)
SCENE_TARGET_SEC = 28.512


class Shot03Motivation(Scene):
    def construct(self):
        # ---- In-state: fresh after wipe — tap and cup drawn in (Create) ----
        guess = Text("Day 15?", font_size=48, color=CREAM).to_edge(UP, buff=0.7)
        self.play(Write(guess), run_time=1.2)

        # Left panel: dripping tap above a cup with an equal-step fill bar
        tap_body = Rectangle(width=0.5, height=0.35, color=BLUE, stroke_width=3).move_to([-4.6, 2.6, 0])
        spout = Line(LEFT * 0.18 + DOWN * 0.175, RIGHT * 0.18 + DOWN * 0.175, color=BLUE, stroke_width=3)
        spout.move_to(tap_body.get_bottom())
        tap = VGroup(tap_body, spout)

        cup = VGroup(
            Line([-4.9, -0.6, 0], [-4.9, 1.2, 0], color=BLUE, stroke_width=3),
            Line([-4.1, -0.6, 0], [-4.1, 1.2, 0], color=BLUE, stroke_width=3),
            Line([-4.9, -0.6, 0], [-4.1, -0.6, 0], color=BLUE, stroke_width=3),
        )
        fill = Rectangle(width=0.72, height=0.01, color=BLUE, stroke_width=0,
                         fill_color=BLUE, fill_opacity=0.55).move_to([-4.5, -0.58, 0])

        self.play(Create(tap), Create(cup), run_time=1.2)

        # A drip falls; the fill bar rises in even steps (equal increments)
        drip = Dot(radius=0.06, color=BLUE, fill_opacity=1).move_to([-4.5, 2.3, 0])
        self.play(FadeIn(drip), run_time=0.3)

        # Right panel: the two named concepts with their step patterns
        lab_lin = Text("linear growth", font_size=36, color=CREAM).move_to([1.9, 2.5, 0])
        lab_exp = Text("exponential growth", font_size=36, color=CREAM).move_to([1.9, 1.4, 0])

        # equal-step bars under "linear" (equal heights)
        lin_bars = VGroup()
        for i in range(4):
            h = 0.25 + i * 0.25
            b = Rectangle(width=0.32, height=h, color=BLUE, stroke_width=2).move_to([1.0 + i * 0.45, -0.75 + h / 2, 0])
            lin_bars.add(b)
        # doubling bars under "exponential" (1 -> 2 -> 4 style: heights double)
        exp_bars = VGroup()
        for i in range(3):
            h = 0.18 * (2 ** i)
            b = Rectangle(width=0.32, height=h, color=BLUE, stroke_width=2).move_to([1.35 + i * 0.45, -0.75 + h / 2, 0])
            exp_bars.add(b)

        self.play(Write(lab_lin), run_time=1.0)
        self.play(Create(lin_bars[0]), Create(lin_bars[1]), run_time=0.8)
        # equal increments: fill rises one step per drip
        for i in range(2, 4):
            self.play(FadeIn(drip), run_time=0.25)
            new_fill = Rectangle(width=0.72, height=0.3 + (i - 1) * 0.3, color=BLUE, stroke_width=0,
                                fill_color=BLUE, fill_opacity=0.55).move_to([-4.5, -0.58, 0])
            self.play(Transform(fill, new_fill), run_time=0.7)
            self.play(Create(lin_bars[i]), run_time=0.5)

        # "Doubling each day is exponential growth" — label + doubling bars
        self.play(Write(lab_exp), run_time=1.0)
        for i in range(3):
            self.play(Create(exp_bars[i]), run_time=0.6)

        # Tiny lily pad on the right quietly doubles each tick (concrete echo)
        pad_r = 0.12
        pad = Circle(radius=pad_r, color=BLUE, stroke_width=3, fill_color=CREAM,
                     fill_opacity=0.85).move_to([4.9, 1.4, 0])
        self.play(GrowFromCenter(pad), run_time=0.6)
        for _ in range(2):
            pad_r *= 2
            bigger = Circle(radius=pad_r, color=BLUE, stroke_width=3,
                            fill_color=CREAM, fill_opacity=0.85).move_to([4.9, 1.4, 0])
            self.play(Transform(pad, bigger), run_time=0.9)

        # Tail hold — pads the scene to its beat duration (A/V sync fix).
        # manimgx 0.1.1: self.wait() emits no frames; use an explicit play-hold.
        tail_hold = max(0.5, SCENE_TARGET_SEC - 13.0)
        self.play(Indicate(pad, scale_factor=1.0, color=CREAM), run_time=tail_hold)
