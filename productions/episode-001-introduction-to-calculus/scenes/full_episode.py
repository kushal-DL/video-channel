"""Episode 1: Introduction to Calculus — Full Episode Scenes."""

import manimgx as m


class IntroScene(m.Scene):
    """Opening title card with fade-in animation."""

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

        group = m.VGroup(title, subtitle).arrange(m.DOWN, buff=0.4)

        self.play(m.FadeIn(group))
        self.wait(2)
        self.play(m.FadeOut(group))


class SpeedometerHookScene(m.Scene):
    """Hook: speedometer question."""

    def construct(self):
        # Simulated speedometer with text overlay
        gauge = m.Text("65 mph", font_size=96, color=m.WHITE)
        question = m.Text(
            "What does this number really mean?",
            font_size=32,
            color=m.GRAY_B,
        )

        group = m.VGroup(gauge, question).arrange(m.DOWN, buff=0.5)

        self.play(m.FadeIn(group))
        self.wait(4)
        self.play(m.FadeOut(group))


class AverageVelocityScene(m.Scene):
    """Average vs instantaneous velocity explanation."""

    def construct(self):
        # Road with points A and B
        road = m.DashedLine(color=m.GRAY, buff=2)
        point_a = m.Text("A", font_size=48, color=m.WHITE)
        point_b = m.Text("B", font_size=48, color=m.WHITE)

        # Position markers
        marker_a = m.Line(start=[-5, 0], end=[-5, -1.5], color=m.BLUE)
        marker_b = m.Line(start=[5, 0], end=[5, -1.5], color=m.BLUE)

        group = m.VGroup(road, point_a, point_b, marker_a, marker_b).arrange(m.RIGHT, buff=2)

        self.play(m.FadeIn(group))
        self.wait(2)

        # Average velocity formula
        avg_vel = m.MathTex(r"v_{avg} = \frac{\Delta x}{\Delta t}", font_size=48)
        self.play(m.Write(avg_vel, run_time=1.5))
        self.wait(3)
        self.play(m.FadeOut(group), m.FadeOut(avg_vel))


class InstantaneousVelocityScene(m.Scene):
    """Instantaneous velocity concept."""

    def construct(self):
        # Speedometer fluctuating
        gauge = m.Text("Speed", font_size=48, color=m.WHITE)
        needle = m.Line(start=[0.5, -2], end=[1.5, -2], color=m.ORANGE, buff=0.3)

        group = m.VGroup(gauge, needle).arrange(m.RIGHT, buff=1)

        self.play(m.FadeIn(group))
        self.wait(2)

        # Question text
        question = m.Text("But what about right now?", font_size=48, color=m.WHITE)
        self.play(m.FadeOut(group), m.Write(question))
        self.wait(3)
        self.play(m.FadeOut(question))


class DerivativeConceptScene(m.Scene):
    """The derivative concept introduced."""

    def construct(self):
        # Position-time graph with two points
        axes = m.CoordinateAxis(x_length=8, y_length=6, color=m.GRAY)
        curve = m.Parentheses(
            lambda t: 2 * t**2 + 3 * t,
            x_range=[0, 4],
            color=m.BLUE,
            stroke_width=4,
        )

        # Two secant lines approaching each other
        point1 = m.Dot(color=m.RED)
        point2 = m.Dot(color=m.RED)

        group = m.VGroup(axes, curve, point1, point2).arrange(m.RIGHT, buff=0.5)

        self.play(m.FadeIn(group))
        self.wait(2)

        # Difference quotient formula
        diff_quotient = m.MathTex(r"\frac{p(t+h) - p(t)}{h}", font_size=48)
        self.play(m.Write(diff_quotient, run_time=1.5))
        self.wait(3)

        # Key insight text
        insight = m.Text("The derivative IS velocity", font_size=48, color=m.ORANGE)
        self.play(m.FadeOut(group), m.Write(insight))
        self.wait(2)
        self.play(m.FadeOut(insight))


class LimitDefinitionScene(m.Scene):
    """Formal limit definition."""

    def construct(self):
        # Limit notation appearing elegantly
        limit_bar = m.Text("lim", font_size=48, color=m.WHITE)
        h_arrow = m.MathTex(r"h \to 0", font_size=48, color=m.WHITE)
        fraction = m.Fraction(
            numerator=m.MathTex(r"p(t+h) - p(t)", font_size=36),
            denominator=m.MathTex(r"h", font_size=36),
        )

        group = m.VGroup(limit_bar, h_arrow, fraction).arrange(m.RIGHT, buff=0.5)

        self.play(m.FadeIn(group))
        self.wait(2)

        # Color-code parts for clarity
        self.play(fraction.numerator.set_color(m.BLUE), run_time=0.5)
        self.play(fraction.denominator.set_color(m.ORANGE), run_time=0.5)
        self.wait(3)

        self.play(m.FadeOut(group))


class LeibnizNotationScene(m.Scene):
    """Leibniz notation explanation."""

    def construct(self):
        # dp/dt with historical note
        leibniz = m.MathTex(r"\frac{dp}{dt}", font_size=64, color=m.WHITE)
        note = m.Text(
            "Leibniz notation: d of p over d of t",
            font_size=28,
            color=m.GRAY_B,
        )

        group = m.VGroup(leibniz, note).arrange(m.DOWN, buff=0.5)

        self.play(m.FadeIn(group))
        self.wait(3)

        # Units appear
        units = m.Text("meters per second", font_size=36, color=m.ORANGE)
        self.play(m.Write(units, run_time=1.5))
        self.wait(2)
        self.play(m.FadeOut(group), m.FadeOut(units))


class SummaryScene(m.Scene):
    """Summary and preview."""

    def construct(self):
        # Recap points
        point1 = m.Text("Derivative = instantaneous rate of change", font_size=36, color=m.WHITE)
        point2 = m.Text("For position vs time, that's velocity", font_size=36, color=m.WHITE)
        point3 = m.Text("Written elegantly as dp/dt", font_size=36, color=m.WHITE)

        group = m.VGroup(point1, point2, point3).arrange(m.DOWN, buff=0.5)

        self.play(m.FadeIn(group))
        self.wait(3)

        # Preview text
        preview = m.Text("Next: Computing derivatives using rules", font_size=48, color=m.ORANGE)
        self.play(m.FadeOut(group), m.Write(preview))
        self.wait(2)
        self.play(m.FadeOut(preview))


class OutroScene(m.Scene):
    """Closing encouragement."""

    def construct(self):
        # Encouragement text with channel branding
        message = m.Text(
            "Keep asking what things mean,\nnot just memorizing formulas.",
            font_size=48,
            color=m.WHITE,
        )

        self.play(m.FadeIn(message))
        self.wait(3)
        self.play(m.FadeOut(message))


class EndCardScene(m.Scene):
    """End card with episode info."""

    def construct(self):
        # Episode title and next episode teaser
        title = m.Text("Episode 1: Introduction to Calculus", font_size=56, color=m.WHITE)
        subtitle = m.Text(
            "Next: Computing derivatives using rules",
            font_size=32,
            color=m.GRAY_B,
        )

        group = m.VGroup(title, subtitle).arrange(m.DOWN, buff=0.5)

        self.play(m.FadeIn(group))
        self.wait(4)
        self.play(m.FadeOut(group))


class CreditsScene(m.Scene):
    """Final fade to black."""

    def construct(self):
        # Fade to black
        self.play(m.FadeOut(m.VGroup()))
        self.wait(2)
