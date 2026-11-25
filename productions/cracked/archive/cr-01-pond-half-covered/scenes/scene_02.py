from manimgx import *

config.background_color = "#0F172A"

BG    = "#0F172A"
CREAM = "#F2E3C6"
ORG   = "#F97316"
BLUE  = "#3B82F6"

MAX_H = 4.0  # max bar height in scene units


def make_bar_outline(x_pos):
    rect = Rectangle(width=1.2, height=MAX_H, color=BLUE, stroke_width=3, fill_opacity=0)
    rect.move_to([x_pos, 0, 0])
    return rect


class ExponentialDeceptionScene(Scene):
    """Shot 2 — Exponential Growth Is Deceptive (Beats 3–4, ~40 s)"""

    def construct(self):
        # ----- two bar outlines -----
        left_outline = make_bar_outline(-2.5)
        right_outline = make_bar_outline(2.5)

        label_lin = Text("Linear", font_size=30, color=CREAM).next_to(left_outline, UP, buff=0.2)
        label_exp = Text("Exponential", font_size=30, color=CREAM).next_to(right_outline, UP, buff=0.2)

        self.play(Create(left_outline), Create(right_outline))
        self.play(Write(label_lin), Write(label_exp))

        # day axis ticks (1–10)
        day_labels = VGroup()
        for d in range(1, 11):
            tick = Text(str(d), font_size=16, color=CREAM)
            tick.move_to([-2.5 + (d - 1) * 0.5 - 2.0, -MAX_H / 2 - 0.4, 0])
            day_labels.add(tick)
        axis_label = Text("Day", font_size=22, color=CREAM).move_to([0, -MAX_H / 2 - 0.4, 0])
        self.play(Create(day_labels), Write(axis_label))

        # ----- animate fill bars simultaneously (10 days) -----
        t = ValueTracker(0)  # 0 → 1 represents Day 1 → Day 10

        def lin_bar():
            frac = t.get_value()
            h = max(0.01, frac * MAX_H)
            b = Rectangle(width=1.2, height=h, color=BLUE, fill_opacity=0.6, stroke_width=0)
            bottom = left_outline.get_bottom()
            b.move_to([bottom[0], bottom[1] + h / 2, 0])
            return b

        def exp_bar():
            frac = t.get_value()
            # Day n = 10 * frac, coverage = 2^n / 2^10
            n = frac * 10
            coverage = (2 ** n) / (2 ** 10) if n > 0 else 0
            coverage = min(coverage, 1.0)
            h = max(0.01, coverage * MAX_H)
            b = Rectangle(width=1.2, height=h, color=ORG, fill_opacity=0.6, stroke_width=0)
            bottom = right_outline.get_bottom()
            b.move_to([bottom[0], bottom[1] + h / 2, 0])
            return b

        lin_fill = always_redraw(lin_bar)
        exp_fill = always_redraw(exp_bar)
        self.add(lin_fill, exp_fill)

        self.play(t.animate.set_value(1.0), run_time=4)
        self.wait(2)  # Beats 3–4 narration

        # out: camera zooms toward exponential bar
        self.play(FadeOut(VGroup(left_outline, lin_fill, label_lin, day_labels, axis_label)))
        self.wait(0.3)
