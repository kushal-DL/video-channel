"""Shot 1 — Hook walk, Days 1–15 (Beat 1, part 1).

Cold open: pond outline drawn in, scientist walks along the top path from
left to right without stopping while the day counter ticks Day 1 -> 7 -> 15.
Out-state: scientist exits right; Day-15 pond state + counter chip persist as
the base for Shot 2 (cut transition).

A/V sync: SCENE_TARGET_SEC is a placeholder until timing.json exists; the tail
hold pads the scene to its beat duration so video never runs ahead of audio.
"""
from manimgx import *

config.background_color = "#0F172A"  # channel palette — mandatory in every scene file

BG    = "#0F172A"
CREAM = "#F2E3C6"
ORG   = "#F97316"
BLUE  = "#3B82F6"

# Beat 1 part 1 (Days 1–15 walk): [0:00–~0:20]
# AVSYNC: target set to full Beat-1 audio duration (33.72 s) so the scene emits a
# real frame-hold up to the beat boundary; S2 then carries only its own tail.
SCENE_TARGET_SEC = 33.72


def make_scientist(scale=1.0, walking=True):
    """Shared minimal scientist figure (continuity.md §1).

    Capsule body + circle head + lab-coat line; two small foot ticks while
    walking. Identical in every scene that uses it — refactor to a shared
    module when the studio consolidates scenes.
    """
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
    """Canonical top-down pond: blue outline, dark water fill (continuity §3)."""
    water = Ellipse(width=width, height=height, color=BLUE, stroke_width=0,
                    fill_color=BG, fill_opacity=1)  # opaque dark water
    rim = Ellipse(width=width, height=height, color=BLUE, stroke_width=4)
    return VGroup(water, rim)


def make_pad(radius=0.22):
    """Lily pad: blue outline + cream center (NOT green — 4-role palette)."""
    c = Circle(radius=radius, color=BLUE, stroke_width=3,
               fill_color=CREAM, fill_opacity=0.85)
    return c


def make_counter_chip(label_text):
    """Day counter chip: cream rounded rect + orange numeral (continuity §3)."""
    bg = RoundedRectangle(corner_radius=0.12, width=max(1.4, 0.32 * len(label_text)),
                          height=0.55, color=CREAM, stroke_width=2)
    txt = Text(label_text, font_size=30, color=ORG)
    chip = VGroup(bg, txt)
    return chip


class Shot01HookWalk(Scene):
    def construct(self):
        # ---- In-state: cold open — pond outline drawn in ----
        pond = make_pond().move_to(DOWN * 0.8)
        self.play(Create(pond[1]), run_time=1.2)          # rim (geometry)

        path_y = 3.4                                       # top-edge walking path
        scientist = make_scientist(scale=1.0, walking=True).move_to([-6.8, path_y, 0])
        self.play(FadeIn(scientist), run_time=0.4)         # enters from left

        chip = make_counter_chip("Day 1").to_corner(UR, buff=0.5)
        self.play(Write(chip[1]), FadeIn(chip[0], run_time=0.3))   # "Day 1" tick

        # ---- Day 1: one tiny pad near the left bank ----
        pad1 = make_pad(radius=0.16).move_to(pond.get_center() + LEFT * 2.0 + DOWN * 0.4)
        self.play(GrowFromCenter(pad1), run_time=0.8)

        # Walk while time passes (she does not stop)
        walk1 = scientist.animate.move_to([-2.5, path_y, 0])
        self.play(walk1, run_time=3.0)

        # ---- Day 7: small cluster near that bank ----
        chip7 = make_counter_chip("Day 7")
        chip7[0].move_to(chip.get_center())
        self.play(Transform(chip[1], Text("Day 7", font_size=30, color=ORG)), run_time=0.5)

        cluster = VGroup(
            make_pad(radius=0.18).move_to(pond.get_center() + LEFT * 2.1 + DOWN * 0.2),
            make_pad(radius=0.14).move_to(pond.get_center() + LEFT * 1.5 + UP * 0.3),
            make_pad(radius=0.16).move_to(pond.get_center() + LEFT * 1.7 + DOWN * 0.7),
            make_pad(radius=0.12).move_to(pond.get_center() + LEFT * 1.1 + UP * 0.1),
        )
        self.play(GrowFromCenter(cluster), run_time=1.4)

        walk2 = scientist.animate.move_to([1.5, path_y, 0])
        self.play(walk2, run_time=3.0)

        # ---- Day 15: a few scattered small patches; open water dominates ----
        self.play(Transform(chip[1], Text("Day 15", font_size=30, color=ORG)), run_time=0.5)
        scattered = VGroup(
            make_pad(radius=0.2).move_to(pond.get_center() + LEFT * 1.6 + DOWN * 0.5),
            make_pad(radius=0.16).move_to(pond.get_center() + RIGHT * 0.4 + UP * 0.35),
            make_pad(radius=0.18).move_to(pond.get_center() + RIGHT * 1.2 + DOWN * 0.3),
        )
        self.play(GrowFromCenter(scattered), run_time=1.4)

        # ---- Out-state: scientist exits right; Day-15 state persists ----
        self.play(scientist.animate.move_to([6.8, path_y, 0]), run_time=2.5)
        self.play(FadeOut(scientist), run_time=0.3)

        # Tail hold — pads the scene to its beat duration (A/V sync fix).
        # manimgx 0.1.1 bug: self.wait() emits NO video frames (only advances the
        # clock + stamps a false container duration). Use an explicit frame-emitting
        # play instead so the hold actually contains ~24 fps of still frames.
        tail_hold = max(0.5, SCENE_TARGET_SEC - 16.0)
        self.play(Indicate(chip[0], scale_factor=1.0, color=CREAM), run_time=tail_hold)
