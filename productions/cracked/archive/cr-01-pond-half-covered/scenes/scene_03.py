from manimgx import *

config.background_color = "#0F172A"

BG    = "#0F172A"
CREAM = "#F2E3C6"
ORG   = "#F97316"
BLUE  = "#3B82F6"


class CountingDoublingsScene(Scene):
    """Shot 3 — Counting the Doublings (Beat 5, ~25 s)"""

    def construct(self):
        # lily pad icons (hexagons) with area labels — Days 1–4
        days = [1, 2, 3, 4]
        areas = [1, 2, 4, 8]
        icons = VGroup()
        area_labels = VGroup()
        x_start = -4.5

        for i, (d, a) in enumerate(zip(days, areas)):
            x = x_start + i * 2.2
            # scale icon size with area
            size = 0.15 + 0.08 * i
            icon = RegularPolygon(n=6, radius=size, color=CREAM, fill_opacity=0.8, stroke_width=1)
            icon.move_to([x, 0.8, 0])

            day_label = Text(f"Day {d}", font_size=24, color=CREAM).next_to(icon, DOWN, buff=0.15)
            area_label = MathTex(str(a), color=ORG, font_size=36).next_to(day_label, DOWN, buff=0.1)

            icons.add(VGroup(icon, day_label))
            area_labels.add(area_label)

        # arrows between icons
        arrows = VGroup()
        for i in range(len(days) - 1):
            x = x_start + i * 2.2 + 1.1
            arr = Arrow(
                start=[x - 0.4, 0.8, 0],
                end=[x + 0.4, 0.8, 0],
                color=BLUE,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.3,
            )
            x2_label = Text("×2", font_size=20, color=BLUE).next_to(arr, UP, buff=0.05)
            arrows.add(VGroup(arr, x2_label))

        # --- reveal icons one by one ---
        for i in range(len(days)):
            self.play(FadeIn(icons[i]), run_time=0.3)
            self.play(Write(area_labels[i]), run_time=0.4)
            if i < len(days) - 1:
                self.play(Create(arrows[i]), run_time=0.4)

        self.wait(0.5)

        # --- ellipsis + Day 10 and Day 20 ---
        ellipsis = Text("…", font_size=36, color=CREAM).move_to([x_start + 4 * 2.2, 0.8, 0])
        day10 = MathTex(r"\text{Day 10: } 512", color=ORG, font_size=32)
        day20 = MathTex(r"\text{Day 20: } 524{,}288", color=ORG, font_size=32)
        day10.move_to([x_start + 5.0 * 2.2 - 1.5, 0.3, 0])
        day20.next_to(day10, DOWN, buff=0.3)

        self.play(Write(ellipsis))
        self.play(Write(day10))
        self.play(Write(day20))

        # --- formula a_n = 2^{n-1} ---
        formula = MathTex(r"a_n = 2^{n-1}", color=ORG, font_size=44)
        formula.move_to([0, -1.8, 0])
        self.play(Write(formula))
        self.wait(1.5)

        # out_state: formula persists; rest fades
        self.play(FadeOut(VGroup(icons, area_labels, arrows, ellipsis, day10, day20)))
        self.wait(0.3)
