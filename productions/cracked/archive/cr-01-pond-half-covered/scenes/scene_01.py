from manimgx import *

config.background_color = "#0F172A"

BG    = "#0F172A"
CREAM = "#F2E3C6"
ORG   = "#F97316"
BLUE  = "#3B82F6"


class PondHookScene(Scene):
    """Shot 1 — The Day 15 Trap (Beats 1–2, ~40 s)"""

    def construct(self):
        # --- in_state: series title card ---
        title = Text("Cracked", font_size=48, color=CREAM)
        tagline = Text("Every riddle hides a law. Break it open.", font_size=28, color=CREAM)
        tagline.next_to(title, DOWN, buff=0.3)
        card = VGroup(title, tagline).move_to(ORIGIN)
        self.play(FadeIn(card, run_time=0.5))
        self.wait(1.5)
        self.play(FadeOut(card, run_time=0.5))
        self.wait(0.2)

        # --- pond ---
        pond = Circle(radius=1.8, color=BLUE, stroke_width=4)
        pond.move_to(UP * 0.5)

        # lily pad — small hexagon at center
        lily = RegularPolygon(n=6, radius=0.18, color=CREAM, fill_opacity=0.9, stroke_width=1)
        lily.move_to(pond.get_center())

        # question text
        question = Text("On which day was it exactly half-covered?", font_size=28, color=CREAM)
        question.next_to(pond, DOWN, buff=0.5)

        self.play(Create(pond))
        self.play(FadeIn(lily))
        self.play(Write(question))
        self.wait(1.5)  # Beat 1 narration plays

        # --- Beat 2: Day 15? callout and strike-through ---
        guess = Text("Day 15?", font_size=36, color=ORG)
        guess.next_to(question, DOWN, buff=0.4)
        self.play(Write(guess))
        self.wait(0.5)

        cross = Cross(guess, stroke_color=RED, stroke_width=6)
        self.play(Create(cross))
        self.wait(1.5)  # Beat 2 narration plays

        # --- out_state: full wipe (act boundary) ---
        self.play(FadeOut(VGroup(pond, lily, question, guess, cross)))
        self.wait(0.3)
