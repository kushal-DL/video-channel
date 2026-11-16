"""LaTeX toolchain verification smoke test for MathTex rendering."""

import manimgx as m


class SmokeLatex(m.Scene):
    """Minimal LaTeX test: renders a simple mathematical expression."""

    config = {
        "resolution": (854, 480),
        "fps": 15,
    }

    def construct(self):
        # Simple MathTex to verify LaTeX rendering pipeline
        formula = m.MathTex(r"x^2")

        self.play(m.Write(formula))
        self.wait(1.5)
        self.play(m.FadeOut(formula))
