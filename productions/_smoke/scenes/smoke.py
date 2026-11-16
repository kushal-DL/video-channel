"""Smoke test scene for manimgx render pipeline verification."""

import manimgx as m


class SmokeTest(m.Scene):
    """Minimal smoke test: Text + VGroup layout only, no MathTex."""

    config = {
        "resolution": (854, 480),  # Low res for fast smoke test
        "fps": 15,                 # Lower fps for faster render
    }

    def construct(self):
        # Simple text elements to verify basic rendering
        title = m.Text("Video-Channel Smoke Test", font_size=36)
        subtitle = m.Text("ManimGX Pipeline Verification", font_size=20)

        # Group with spacing using VGroup
        group = m.VGroup(title, subtitle).arrange(m.DOWN, buff=0.3)

        self.play(m.Write(group))
        self.wait(1.5)
        self.play(m.FadeOut(group))
