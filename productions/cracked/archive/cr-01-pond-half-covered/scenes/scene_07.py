from manimgx import *

config.background_color = "#0F172A"

BG    = "#0F172A"
CREAM = "#F2E3C6"
ORG   = "#F97316"
BLUE  = "#3B82F6"


class OneStepBackScene(Scene):
    """Shot 7 — One Step Back (Beat 9, ~20 s)"""

    def construct(self):
        # pond circle
        pond = Circle(radius=1.8, color=BLUE, stroke_width=4)
        pond.move_to([-1.5, 0, 0])

        # fill rectangle simulating pond coverage
        t = ValueTracker(1.0)  # 1.0 = fully covered

        def fill():
            frac = t.get_value()
            h = max(0.01, frac * 3.6)
            r = Rectangle(width=3.6, height=h, color=BLUE, fill_opacity=0.5, stroke_width=0)
            bottom = [-1.5, -1.8, 0]
            r.move_to([bottom[0], bottom[1] + h / 2, 0])
            return r

        fill_rect = always_redraw(fill)

        # Day 30 label
        label30 = Text("Day 30 — 100%", font_size=28, color=CREAM)
        label30.next_to(pond, DOWN, buff=0.4)

        # backward arrow (above pond)
        back_arrow = Arrow(
            start=[0.5, 2.0, 0], end=[-3.5, 2.0, 0],
            color=BLUE, stroke_width=4,
            max_tip_length_to_length_ratio=0.2,
        )
        back_text = Text("one step back", font_size=24, color=BLUE).next_to(back_arrow, UP, buff=0.1)

        # equation (right side)
        equation = MathTex(
            r"\frac{2^{29}}{2^{30}} = \frac{1}{2}",
            color=ORG, font_size=52,
        )
        equation.move_to([3.0, 0.5, 0])

        # --- build scene ---
        self.play(Create(pond))
        self.add(fill_rect)
        self.play(Write(label30))
        self.play(Create(back_arrow), Write(back_text))

        # animate backward: 100% → 50%
        label29 = Text("Day 29 — 50%", font_size=28, color=ORG)
        label29.next_to(pond, DOWN, buff=0.4)

        self.play(
            t.animate.set_value(0.5),
            Transform(label30, label29),
            Write(equation),
            run_time=1.5,
        )
        self.wait(1.5)  # Beat 9 narration

        # out_state: pond at 50%, equation, arrow visible
        self.wait(0.3)
