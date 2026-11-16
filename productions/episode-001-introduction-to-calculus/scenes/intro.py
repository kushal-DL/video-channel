"""Introduction to Calculus — Episode 1 pilot scene."""

import manimgx as m


class IntroScene(m.Scene):
    """Opening title and hook for the calculus introduction episode."""

    config = {
        "resolution": (1920, 1080),
        "fps": 60,
    }

    def construct(self):
        # Title card with fade-in animation
        title = m.Text(
            "Introduction to Calculus",
            font_size=72,
            color=m.WHITE,
        )

        subtitle = m.Text(
            "Understanding Derivatives and Rates of Change",
            font_size=36,
            color=m.GRAY_B,
        )

        group = m.VGroup(title, subtitle).arrange(DOWN, buff=0.4)

        self.play(m.FadeIn(group))
        self.wait(2)
        self.play(m.FadeOut(group))
