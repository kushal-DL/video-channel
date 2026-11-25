from manimgx import *
import math

config.background_color = "#0F172A"

BG    = "#0F172A"
CREAM = "#F2E3C6"
ORG   = "#F97316"
BLUE  = "#3B82F6"

MAX_H = 4.5
BAR_W = 1.5
N_DAYS = 30


class SplitScreenScene(Scene):
    """Shot 8 — Split-Screen Comparison (Beat 10, ~30 s)"""

    def construct(self):
        # divider
        divider = Line([0, -3.0, 0], [0, 3.5, 0], color=CREAM, stroke_width=1.5)

        # bar outlines
        left_outline = Rectangle(width=BAR_W, height=MAX_H, color=BLUE, stroke_width=3, fill_opacity=0)
        left_outline.move_to([-2.8, 0, 0])
        right_outline = Rectangle(width=BAR_W, height=MAX_H, color=BLUE, stroke_width=3, fill_opacity=0)
        right_outline.move_to([2.8, 0, 0])

        label_lin = Text("Linear", font_size=30, color=CREAM).next_to(left_outline, UP, buff=0.2)
        label_exp = Text("Exponential", font_size=30, color=CREAM).next_to(right_outline, UP, buff=0.2)

        # day counter
        day_tracker = ValueTracker(0)
        day_counter = always_redraw(
            lambda: Text(f"Day {int(day_tracker.get_value()):02d}", font_size=28, color=CREAM)
            .move_to([0, -3.3, 0])
        )

        # fill bars
        def lin_fill():
            n = day_tracker.get_value()
            frac = n / N_DAYS
            h = max(0.01, frac * MAX_H)
            b = Rectangle(width=BAR_W, height=h, color=BLUE, fill_opacity=0.6, stroke_width=0)
            bottom = left_outline.get_bottom()
            b.move_to([bottom[0], bottom[1] + h / 2, 0])
            return b

        def exp_fill():
            n = day_tracker.get_value()
            if n <= 0:
                h = 0.01
            else:
                frac = (2 ** n) / (2 ** N_DAYS)
                h = max(0.01, frac * MAX_H)
            b = Rectangle(width=BAR_W, height=h, color=ORG, fill_opacity=0.6, stroke_width=0)
            bottom = right_outline.get_bottom()
            b.move_to([bottom[0], bottom[1] + h / 2, 0])
            return b

        left_fill  = always_redraw(lin_fill)
        right_fill = always_redraw(exp_fill)

        self.play(
            Create(divider),
            Create(left_outline), Create(right_outline),
            Write(label_lin), Write(label_exp),
        )
        self.add(left_fill, right_fill, day_counter)
        self.wait(0.3)

        # animate both bars from Day 0 → Day 30
        self.play(day_tracker.animate.set_value(N_DAYS), run_time=5, rate_func=linear)
        self.wait(0.5)

        # Day 15 vertical marker (orange dashed)
        d15_frac = 15 / N_DAYS
        d15_x_lin = -2.8  # left panel center
        d15_x_exp = 2.8
        marker15_left = DashedLine(
            [d15_x_lin - BAR_W / 2, left_outline.get_bottom()[1], 0],
            [d15_x_lin + BAR_W / 2, left_outline.get_bottom()[1] + d15_frac * MAX_H, 0],
            color=ORG, stroke_width=2,
        )
        marker15_right_y = left_outline.get_bottom()[1] + ((2**15) / (2**30)) * MAX_H
        marker15_text = Text("Day 15", font_size=22, color=ORG).move_to([0, left_outline.get_bottom()[1] + d15_frac * MAX_H + 0.2, 0])

        marker29_text = Text("Day 29", font_size=22, color=ORG).move_to([0, left_outline.get_bottom()[1] + 0.5 * MAX_H + 0.2, 0])

        self.play(Write(marker15_text), Write(marker29_text))
        self.wait(1.5)  # Beat 10 narration

        # out: fade to result
        self.play(FadeOut(VGroup(
            divider, left_outline, right_outline,
            label_lin, label_exp,
            left_fill, right_fill,
            day_counter,
            marker15_text, marker29_text,
        )))
        self.wait(0.3)
