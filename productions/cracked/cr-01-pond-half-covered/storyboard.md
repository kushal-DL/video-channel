# Storyboard — cr-01-pond-half-covered

**Episode:** When Was the Pond Half-Covered? (Cracked, ep. 1)
**Source of truth for narration:** `script-reviewed.md` (VERDICT: PASS). All narration lines below are **verbatim** from Part A beats; no paraphrase or invention. Beat numbers and timing labels preserved.
**Style contract:** `channel-bible.md` — palette, reveal rules, concrete→abstract pairing, equation persistence, pacing norms.
**Brief requirements covered:** Section 5a (split-screen in hook), 5b (coverage table in build-up), 5c (one-step-back reversal + generalization), 5d (concrete↔abstract at first formula).

---

## Global conventions (apply to every shot)

- **Background** `#0F172A` set via module-level `config.background_color = "#0F172A"` in every scene file.
- **Palette (exactly 4 roles, no ad-hoc colors):**
  - bg dark slate `#0F172A`
  - text/captions cream `#F2E3C6`
  - math orange `#F97316` (equations, symbols, highlighted terms)
  - geometry blue `#3B82F6` (pond outlines, water surfaces, axes, curves, points)
- **Reveals:** equations/math via `Write()` or `Create()`, never `FadeIn()`; geometry via `Create()`; equation morphs via `Transform()` (never fade-out/fade-in); full wipes only at the three act boundaries marked below.
- **Fades** ≤ 0.8 s; holds at full opacity ≥ 60% of each beat.
- **Fonts:** titles 56 px, body ≥ 30 px, math 60–72 px (per channel bible).
- **No clickbait tropes:** no giant red X marks, no "WRONG!" callouts, no fake suspense text.
- **No 3D.** No character/illustration art beyond simple geometric shapes; the scientist is a minimal stylized figure (see `continuity.md` §1).

### Act boundaries (full wipes allowed ONLY here)

| Boundary | After beat | Transition |
|---|---|---|
| Hook → Body | Beat 1 | full wipe (fade through bg, ≤0.8 s) |
| Build-up → Worked example | Beat 6 | full wipe (fade through bg, ≤0.8 s) — new scene: lab + petri dish |
| Worked example → Recap | Beat 7 | full wipe (fade through bg, ≤0.8 s) |

All other shot-to-shot transitions are fade / slide / zoom / cut / morph as specified per shot below; no wipes mid-act.

### Scene class naming

One manimgx `Scene` subclass per shot: `scene_01.py … scene_12.py`, classes `Shot01HookWalk` … (names in the mapping table at the end).

---

## Shot 1 — Hook walk, Days 1–15 (Beat 1, part 1)

- **Scene class:** `Shot01HookWalk` (`scenes/scene_01.py`)
- **Narration lines (verbatim):**
  - Beat 1 [0:00–~0:20]: "A scientist walks past the same pond every morning on her way to the lab. Day 1, one lily pad, barely the size of her hand. She does not stop. By Day 7, a small cluster drifts near the bank. On Day 15, open water still dominates the surface, and she keeps walking."
- **Visual content:** Top-down view of an oval pond (blue `#3B82F6` outline, dark water fill) centered with ≥0.5 buff margin. The scientist figure (minimal geometric design per continuity.md §1) walks along a straight path at the top edge from left to right; she does not stop. A day counter chip in the upper-left ticks: `Day 1`, then `Day 7`, then `Day 15` (cream text, orange numerals). Lily pads are small blue-outlined circles with cream centers: Day 1 = one tiny pad near the left bank; Day 7 = a cluster of ~4 small pads near that bank; Day 15 = a few scattered small patches, open water still dominant. Pads grow via `Create()`/`GrowFromCenter`; counter ticks are `Write()`.
- **concrete_visual:** a scientist walking past an oval pond each morning while lily pads slowly multiply on the water surface (Day 1 → Day 7 → Day 15 time-lapse).
- **abstract_symbol:** none — no formula yet; this is the character-grounded hook (brief §6: the riddle emerges from her observation, nothing defined in the hook). Justified: concrete-only by design.
- **reveal_animation:** `Create()` for pond outline and each lily pad; `Write()` for day counter ticks.
- **Hold content:** pond + walking scientist + day counter chip remain on screen throughout; at hold, Day 15 state is visible (scattered small pads, mostly open water) with the counter reading `Day 15`.
- **In-state:** cold open — empty bg, then pond outline drawn in (`Create`), scientist enters from left.
- **Out-state:** scientist exits right at the top edge; Day 15 pond state (scattered small pads + counter chip) persists as the base for Shot 2.

**Transition S1→S2: cut.** Same scene continues into the next shot's content — no wipe, no fade; the Day-15 pond and counter carry forward unchanged.

---

## Shot 2 — Hook climax, Day 30 + riddle (Beat 1, part 2)

- **Scene class:** `Shot02HookClimax` (`scenes/scene_02.py`)
- **Narration lines (verbatim):**
  - Beat 1 [~0:20–0:35]: "Then Day 30 arrives. The entire pond is gone under green pads, bank to bank. She stops at the water's edge and stares. On which day was the pond half-covered?"
- **Visual content:** Same top-down pond as Shot 1 (continuity). Pads rapidly multiply across the surface until the whole oval is covered — rendered as a full blue-outlined pad field filling the pond shape (`GrowFromCenter` cascade, then a single filled overlay so "bank to bank" reads clearly). Day counter ticks `Day 30`. The scientist figure stops at the water's edge (right side) and stands still. As the final question is spoken, the riddle appears as cream text centered below the pond: **"On which day was the pond half-covered?"** via `Write()` — no exclamation styling, no clickbait treatment.
- **concrete_visual:** the same pond going from scattered pads to completely covered bank-to-bank; scientist stopping at the water's edge and staring.
- **abstract_symbol:** none — the riddle is posed in words only (brief §6: do not spoil Day 29, do not define exponential growth in the hook). Justified: question text is narration content, not a math symbol.
- **reveal_animation:** `GrowFromCenter` for pad cascade; `Write()` for counter tick and riddle text.
- **Hold content:** fully covered pond + stopped scientist + day counter `Day 30` + the riddle line in cream below the pond. Nothing empty — this is the hook's landing frame.
- **In-state:** inherits Shot 1 out-state: Day-15 pond, counter chip, same framing; scientist re-enters from left and walks to the right bank.
- **Out-state:** fully covered pond + riddle text hold as the final hook frame; then **full wipe** (act boundary Hook → Body).

**Transition S2→S3: full wipe (fade through bg, ≤0.8 s)** — act boundary after Beat 1 per script metadata / channel bible.

---

## Shot 3 — Motivation: linear intuition vs exponential reality (Beat 2)

- **Scene class:** `Shot03Motivation` (`scenes/scene_03.py`)
- **Narration lines (verbatim):**
  - Beat 2 [0:35–1:05]: "Your first instinct is probably Day 15. Thirty days total, so splitting the time in half feels like it should split the coverage in half. That intuition works for a dripping tap that adds an equal cup of water every hour. It fails completely here. Adding the same amount each day is linear growth. Doubling each day is exponential growth. The lily pad was multiplying quietly from the very first morning."
- **Visual content:** Two-part layout, both parts on screen simultaneously (concrete↔abstract pairing):
  - **Left (concrete):** a dripping tap above a cup — water drips at equal intervals and the cup fills by equal increments (a small vertical fill bar beside the cup rises in even steps). This is the "dripping tap" analogy from the narration.
  - **Right (paired symbol + mini-pond):** below/beside it, two short labeled lines appear via `Write()` as they are spoken: `linear growth` and `exponential growth` (cream labels), with a small equal-step bar under "linear" and a small doubling bar (1→2→4) under "exponential". A tiny lily pad on the right side quietly doubles in size each tick, reinforcing "multiplying quietly from the very first morning."
  - The Day-15 guess is acknowledged visually: a cream caption `Day 15?` appears near the top as the first sentence plays (no X mark, no red — just the question restated).
- **concrete_visual:** a dripping tap adding an equal cup of water every hour (equal-step fill), paired with a lily pad quietly doubling in size.
- **abstract_symbol:** `linear growth` / `exponential growth` labels with their step patterns (equal steps vs ×2 steps) — the two named concepts, shown at the same moment as the tap and pad. (No full formula yet; the formula is Shot 5.)
- **reveal_animation:** `Create()` for tap/cup/pond geometry; `Write()` for both labels and the step bars; `GrowFromCenter` for the doubling lily pad.
- **Hold content:** tap + cup fill on left, labeled linear/exponential comparison with step bars on right, tiny doubling lily pad — all persist while narration plays; final hold frame = full two-panel comparison.
- **In-state:** fresh after act-boundary wipe: empty bg, then tap and cup drawn in (`Create`).
- **Out-state:** the linear-vs-exponential comparison panel holds; it slides left and shrinks to become the conceptual seed of Shot 4's split-screen (the "two ponds side by side" is this same idea at pond scale).

**Transition S3→S4: slide + zoom.** The two-panel comparison slides toward center-left while a top-down view zooms in on the right panel's lily pad, landing on the split-screen layout of Shot 4. No wipe (mid-act).

---

## Shot 4 — Split-screen linear vs exponential fill (Beat 3) — brief §5a

- **Scene class:** `Shot04SplitScreen` (`scenes/scene_04.py`)
- **Narration lines (verbatim):**
  - Beat 3 [1:05–1:40]: "Picture two ponds filling side by side over the same thirty days. The left pond gains an identical slice of water every morning, like a steady progress bar. The right pond stays almost empty for three weeks, then engulfs the surface in five days. On Day 10, both ponds look nearly bare. By Day 30, one fills smoothly while the other explodes. That visual illusion is why the scientist walked past without noticing."
- **Visual content:** Split-screen, two oval ponds side by side (same pond shape as Shots 1–2 for continuity), each with its own small label area above:
  - **Left panel (linear):** fills by an identical slice every morning — a progress-bar feel; water level rises in equal steps day by day.
  - **Right panel (exponential):** nearly empty until ~Day 25, then explodes to full over the final days (pads/water surge in the last five days).
  - **Shared day counter:** one counter chip at top center ticks `Day 1 → … → Day 30` simultaneously for both panels (the brief's "shared day counter ticking simultaneously").
  - Key scripted moments get a beat of emphasis: at "On Day 10, both ponds look nearly bare" the counter pauses on `Day 10` with both ponds visibly near-bare; at "By Day 30" the left is smoothly full and the right has just exploded to full.
  - **Panels are shown BEFORE any naming:** no words "linear"/"exponential" appear during this shot (brief §5a: show panels before naming the concept). The names were already introduced verbally in Shot 3; here they stay unnamed on screen.
- **concrete_visual:** two ponds filling side by side over thirty days — left as a steady progress bar, right nearly empty then exploding — with one shared day counter ticking for both.
- **abstract_symbol:** none on screen (by design: brief §5a says show the panels before naming the concept; the linear/exponential labels were already shown in Shot 3). Justified: this shot is the pure visual demonstration that motivates the names.
- **reveal_animation:** `Create()` for both pond outlines and water/pad fills; `Write()` for counter ticks; fills animate as level rises / pad cascade (geometry, not math — no FadeIn of symbols involved).
- **Hold content:** both ponds + shared day counter on screen throughout; final hold = Day 30 state: left smoothly full, right exploded to full, counter reading `Day 30`.
- **In-state:** arrives from Shot 3's slide+zoom: the zoomed lily pad resolves into the right panel pond; left panel pond drawn in beside it.
- **Out-state:** Day-30 split-screen holds; then a gentle zoom out + fade as we move to "track the coverage with numbers" (Shot 5). The right panel's exponential pond is the one that carries forward conceptually into the formula shot.

**Transition S4→S5: zoom out + fade (≤0.8 s).** Mid-act, no wipe; the right (exponential) pond remains faintly visible at frame edge during the fade as a visual anchor for "the math of this pond."

---

## Shot 5 — The formula, paired with the lily pad (Beat 4, part 1) — brief §5d

- **Scene class:** `Shot05Formula` (`scenes/scene_05.py`)
- **Narration lines (verbatim):**
  - Beat 4 [1:40–~2:00]: "Track the coverage with numbers. Full coverage happens on Day 30. On Day n, the fraction covered is 2 to the power of n over 2 to the power of 30."
- **Visual content:** Concrete↔abstract pairing at first formula introduction (brief §5d — never a formula on a blank background):
  - **Left:** an animated lily pad on a water surface — a polygon growing on the pond's surface (blue `#3B82F6` water, pad outline in blue with cream center), visibly doubling in area as a small day tick advances.
  - **Right, appearing simultaneously:** the formula in orange `#F97316`:
    `fraction(n) = 2^n / 2^30`
    revealed via `Write()` at exactly the moment the pad grows (same frame — not sequential).
  - As "Full coverage happens on Day 30" is spoken, a small anchor note appears beside the formula: `Day 30 → full` in cream, with the exponent `2^30` briefly highlighted by thickening its orange stroke (term-under-discussion highlight per channel bible).
- **concrete_visual:** an animated lily pad polygon growing on a water surface, doubling each morning.
- **abstract_symbol:** `fraction(n) = 2^n / 2^30` in orange, shown at the same time as the growing pad; anchor note `Day 30 → full`.
- **reveal_animation:** `Write()` for the formula (mandatory — never FadeIn for math); `Create()`/`GrowFromCenter` for the pad and water surface.
- **Hold content:** growing lily pad on left + orange formula on right + `Day 30 → full` anchor note, all persisting while narration plays; final hold = formula fully written with the pad mid-growth beside it.
- **In-state:** arrives from Shot 4's zoom-out: the exponential pond resolves into the water surface on the left; formula area is empty until spoken.
- **Out-state:** formula `fraction(n) = 2^n / 2^30` stays on screen and carries forward into Shot 6, where Day 15 is plugged in (equation persistence rule — never clear and redraw).

**Transition S5→S6: cut.** Same layout continues; the formula persists unchanged while new terms are added below it. No wipe (mid-act).

---

## Shot 6 — Plug in Day 15 + coverage table punchline (Beat 4, part 2) — brief §5b

- **Scene class:** `Shot06Day15Table` (`scenes/scene_06.py`)
- **Narration lines (verbatim):**
  - Beat 4 [~2:00–2:10]: "Plug in Day 15, and the fraction is 2 to the power of 15 over 2 to the power of 30. That equals barely three thousandths of a percent. The surface looked empty on Day 15 because it practically was empty. Nearly the entire month produces almost zero visible change."
- **Visual content:** Two zones, formula persists from Shot 5 (equation persistence):
  - **Top zone — substitution (concrete↔abstract):** below the persistent `fraction(n) = 2^n / 2^30`, a new line is written via `Write()` in orange:
    `fraction(15) = 2^15 / 2^30`
    with the `n → 15` substitution highlighted (the `15` term thickened). Beside it, the lily pad from Shot 5 shrinks to a tiny speck on an otherwise empty pond surface — "practically was empty."
  - **Bottom zone — coverage table (brief §5b):** a table with columns **Day | Coverage fraction | % of pond**, rows for Days 15, 25–30:

    | Day | Coverage fraction | % of pond |
    |-----|-------------------|-----------|
    | 15  | 2^15 / 2^30       | **0.003%** (punchline callout) |
    | 25  | 2^25 / 2^30       | 0.03%     |
    | 26  | 2^26 / 2^30       | 0.06%     |
    | 27  | 2^27 / 2^30       | 0.12%     |
    | 28  | 2^28 / 2^30       | 0.24%     |
    | 29  | 2^29 / 2^30       | **50.0%** (row highlighted orange `#F97316`) |
    | 30  | 2^30 / 2^30       | **100%**  |

    - The **Day 15 row** carries the punchline callout: `0.003%` in orange, visually set against the earlier Day-15 guess (the caption `Day 15?` from Shot 3 is echoed as a small cream tag next to this row — "this is why that guess fails").
    - The **Day 29 row** is highlighted in orange `#F97316` with `50.0%`.
    - The **Day 30 row** reads `100%`.
    - Table drawn via `Create()` for grid lines; cell text via `Write()`. Rows appear top-to-bottom as the counter concept implies, but the Day-15 punchline row is written first (it answers "Plug in Day 15"), then rows 25–30 fill down to the highlighted Day-29 and Day-30 rows.
- **concrete_visual:** a nearly empty pond surface with one tiny lily pad speck on it (the Day-15 reality), paired with the coverage table as the "ledger" of the pond's growth.
- **abstract_symbol:** `fraction(15) = 2^15 / 2^30` in orange, plus the full coverage table (Day | Coverage fraction | % of pond) — shown simultaneously with the tiny-pad-on-empty-water visual.
- **reveal_animation:** `Write()` for the substitution line and all numeric cells; `Create()` for table grid lines; `GrowFromCenter`/shrink for the pad speck. No FadeIn on any math element.
- **Hold content:** persistent formula at top + substitution line + tiny pad on empty water (left) + full coverage table with Day-15 punchline and highlighted Day-29 row (right/bottom). Final hold = complete table with `0.003%` and `50.0%` both visible.
- **In-state:** inherits Shot 5's formula at top of frame; lily pad present from Shot 5, now shrinking to a speck as Day 15 is plugged in.
- **Out-state:** the table holds with Day-29 row highlighted orange — this highlight is the visual seed for Shot 7 (the one-step-back reversal lands on exactly that `50.0%`). Formula + table persist out of frame via a slide-down as the pond re-centers for the reversal.

**Transition S6→S7: slide.** The coverage table slides down and off; the top-down pond (from Shots 1–2) re-enters centered, already fully covered at Day 30. Mid-act, no wipe.

---

## Shot 7 — One-step-back reversal + generalization (Beat 5) — brief §5c

- **Scene class:** `Shot07OneStepBack` (`scenes/scene_07.py`)
- **Narration lines (verbatim):**
  - Beat 5 [2:10–2:40]: "The shortcut to the answer is looking backward from the finish line. On Day 30, the pond is one hundred percent covered. Because the coverage doubled every single morning, the day before full must hold exactly half. That lands you directly on Day 29. One step back from full is always fifty percent, no matter how long the journey took."
- **Visual content:** The reversal animation (brief §5c):
  - **Start:** top-down pond fully covered, labeled `Day 30` with a `100%` overlay (cream label, orange numeral).
  - **Reverse one step:** animate backward — the coverage instantly halves: half the pads clear away, leaving exactly half the pond covered. The label morphs to `Day 29` and a `50%` overlay appears in orange over the remaining half. This is the core "one step back" reveal.
  - **Generalization (brief §5c last bullet):** after the pond reversal lands, a second, smaller pond appears beside it — a **20-day pond** — doing the same thing: full at `Day 20`, reverse one step → half at `Day 19`. The narration says "no matter how long the journey took," which supports this generalization; it is shown visually-light (a compact side-by-side of the two ponds each halving in one backward step) rather than a full re-derivation.
    - *Note:* the reviewed script's Beat 5 does not itself mention a 20-day pond — the generalization lives in brief §5c and is supported by the line "no matter how long the journey took." Kept visual-light per task instructions; flagged in `continuity.md` for Director confirmation.
- **concrete_visual:** a fully covered pond reversing one step to half coverage (Day 30 → Day 29), then a second, shorter-journey pond (20 days) doing the same halving — two containers both showing "one step back = half."
- **abstract_symbol:** `100%` → `50%` overlays on the ponds, with day labels `Day 30 → Day 29` and `Day 20 → Day 19`. (These are the numeric states of the one-step-back law; no new formula is introduced here — the formula from Shot 5 remains conceptually active but is not redrawn.)
- **reveal_animation:** `Create()` for pond geometry; the halving is a geometric reveal (pads clearing via `FadeOut` of pad shapes only — this is removing concrete objects, not revealing math, so it does not violate the no-FadeIn-for-math rule); labels and `%` overlays via `Write()`.
- **Hold content:** both ponds on screen throughout; final hold = Day-30/Day-29 pond pair with `50%` overlay + the 20-day pond showing its own half state. Nothing empty — the two halved ponds are the active content.
- **In-state:** arrives from Shot 6's slide: centered top-down pond, fully covered at Day 30 (continuity of pond shape from Shots 1–2).
- **Out-state:** the `Day 29 = 50%` state is the answer; it holds as the final build-up frame before the act-boundary wipe into the worked example. The "one step back" halved-pond motif carries forward conceptually to the petri dish (same container-halving idea, new domain).

**Transition S7→S8: full wipe (fade through bg, ≤0.8 s)** — act boundary Build-up → Worked example after Beat 6 per script metadata / channel bible. New scene: lab + petri dish.

---

## Shot 8 — Worked example setup: bacteria in the lab (Beat 7, part 1)

- **Scene class:** `Shot08LabSetup` (`scenes/scene_08.py`)
- **Narration lines (verbatim):**
  - Beat 7 [3:00–~3:20]: "Back in her lab, the scientist cultures bacteria in a glass petri dish. The colony doubles in size every hour, filling the dish completely at noon."
- **Visual content:** New scene — the lab (brief §8 handoff; same container metaphor, new context):
  - A simple lab bench line across the frame (blue `#3B82F6`); the scientist figure (same minimal design as Shots 1–2, per continuity.md §1) stands at the right side.
  - **Center:** a glass petri dish — a circle with a blue outline and a thin rim (concrete container). Inside, a bacterial colony: small cream dots that double in count each hour tick.
  - A clock chip in the upper area ticks by the hour; as "filling the dish completely at noon" is spoken, the colony fills the dish and the clock reads `noon` with a `100%` tag (orange numeral).
- **concrete_visual:** a scientist in her lab culturing bacteria in a glass petri dish; the colony doubles every hour until it fills the dish at noon.
- **abstract_symbol:** none yet — setup only; no formula or % claim is asserted beyond the `100%` full-dish state tag (a concrete fill level, not a new symbol). Justified: this is the worked-example setup beat; symbols arrive in Shot 9 with the question and rule.
- **reveal_animation:** `Create()` for bench, dish outline, rim; `GrowFromCenter` for colony dots doubling; `Write()` for clock ticks and the `100%` tag.
- **Hold content:** lab bench + scientist + petri dish full of colony at noon with `100%` tag — all persist while narration plays.
- **In-state:** fresh after act-boundary wipe: empty bg, then bench and dish drawn in (`Create`).
- **Out-state:** full dish at noon holds; the dish stays centered as the question is posed (Shot 9). The "container going from empty to full" motif matches the pond.

**Transition S8→S9: cut.** Same lab scene continues; dish persists, a clock/question element is added. No wipe (mid-act within worked example).

---

## Shot 9 — Worked example question + one-step-back rule (Beat 7, part 2)

- **Scene class:** `Shot09LabQuestion` (`scenes/scene_09.py`)
- **Narration lines (verbatim):**
  - Beat 7 [~3:20–3:35]: "When was the dish half full? Splitting the morning in half suggests nine am. The one-step-back rule gives the exact truth: one hour before noon is eleven am."
- **Visual content:** Same lab + petri dish (continuity from Shot 8):
  - The question appears as cream text: **"When was the dish half full?"** via `Write()`.
  - A small timeline strip below the dish marks the morning hours with a clock; the naive guess is shown first: a marker at `9 am` with a faint half-fill hint (the "splitting the morning in half" intuition) — drawn, then visually set aside.
  - **The rule applied:** the dish animates backward one hour from noon → the colony halves, and a marker lands on `11 am` with a `50%` overlay in orange over the half-filled dish (mirroring Shot 7's pond reversal — same container-halving motif, new domain).
- **concrete_visual:** the petri dish reversing one hour from full at noon to half-full at 11 am; a morning timeline with markers at 9 am (naive guess) and 11 am (rule answer).
- **abstract_symbol:** `50%` overlay on the half-filled dish + time labels `noon → 11 am` (one doubling step back); the naive `9 am` marker shown and set aside. These are the numeric states of the one-step-back rule applied hourly.
- **reveal_animation:** `Write()` for question text, clock markers, `%` overlay; geometric halving of colony via object removal (not math FadeIn). No FadeIn on symbols.
- **Hold content:** dish + timeline + question text throughout; final hold = half-filled dish at 11 am with `50%` overlay and the 9 am marker set aside beside it.
- **In-state:** inherits Shot 8: full dish at noon, scientist at bench, clock chip present.
- **Out-state:** half-full dish at 11 am holds; carries into Shot 10 where the 9 am fraction is quantified (the dish stays on screen, equation persistence for the worked example).

**Transition S9→S10: cut.** Same lab scene continues; dish persists while the 9 am substitution is added. No wipe (mid-act within worked example).

---

## Shot 10 — Worked example quantification: one eighth at 9 am (Beat 7, part 3)

- **Scene class:** `Shot10LabEighth` (`scenes/scene_10.py`)
- **Narration lines (verbatim):**
  - Beat 7 [~3:35–3:55]: "At eleven am, the dish was half full. At nine am, it held barely one eighth of its final volume."
  - *(Note: this is the math-corrected line — script-reviewed.md Part A Beat 7 now reads "one eighth," per correction C1/C9. The storyboard uses the corrected verbatim text.)*
- **Visual content:** Same lab + dish (continuity):
  - Confirm `11 am = half full`: a small recap tag `11 am → 50%` in orange beside the dish (persistent from Shot 9).
  - **Quantify 9 am:** the dish animates backward two more hours from 11 am to 9 am; the colony shrinks to one eighth of the dish area. A fraction appears via `Write()` in orange: `1/8`, paired with the tiny colony speck in the mostly empty dish (concrete↔abstract at the same moment).
  - The morning timeline from Shot 9 stays visible, now showing both markers resolved: `11 am → 50%` and `9 am → 1/8`.
- **concrete_visual:** the petri dish shrinking to one eighth of its area by 9 am — a tiny colony in an almost empty glass dish.
- **abstract_symbol:** `1/8` (the fraction at 9 am) in orange, shown simultaneously with the one-eighth-filled dish; recap tag `11 am → 50%`.
- **reveal_animation:** `Write()` for the `1/8` fraction and timeline tags; geometric shrink of colony via object removal. No FadeIn on math.
- **Hold content:** dish at one-eighth fill + `1/8` fraction + full morning timeline with both resolved markers — all persist while narration plays. This is the worked example's landing frame.
- **In-state:** inherits Shot 9: half-full dish at 11 am, timeline present.
- **Out-state:** one-eighth dish + `1/8` holds as final worked-example frame; then **full wipe** (act boundary Worked example → Recap).

**Transition S10→S11: full wipe (fade through bg, ≤0.8 s)** — act boundary after Beat 7 per script metadata / channel bible.

---

## Shot 11 — Recap & payoff: the law + half/quarter/eighth (Beat 8)

- **Scene class:** `Shot11Recap` (`scenes/scene_11.py`)
- **Narration lines (verbatim):**
  - Beat 8 [3:55–4:20]: "One law governs both containers. Whenever growth multiplies instead of adds, the state right before the end holds half the final amount. Day 29 was half, Day 28 a quarter, Day 27 an eighth."
- **Visual content:** Recap ties back to the hook's pond (character-grounded payoff):
  - Top-down pond centered again (continuity of shape from Shots 1–2). A compact backward-stepping strip shows three states side by side: `Day 29 → 1/2`, `Day 28 → 1/4`, `Day 27 → 1/8` — each a small pond with its fraction in orange, revealed left-to-right via `Write()` as they are spoken.
  - The governing law is stated as cream text (not a new formula): the half/quarter/eighth fractions are the on-screen symbols paired with the three shrinking pond states.
- **concrete_visual:** the same pond stepping backward through Day 29 → Day 28 → Day 27, each state visibly smaller coverage — "nearly nothing, then half, then everything" in reverse.
- **abstract_symbol:** `1/2`, `1/4`, `1/8` fractions (orange) paired with the three pond states; day labels `Day 29 / Day 28 / Day 27`.
- **reveal_animation:** `Create()` for the three small ponds; `Write()` for each fraction and day label. No FadeIn on math.
- **Hold content:** three shrinking pond states with their fractions + day labels, all persisting while narration plays; final hold = full half/quarter/eighth strip.
- **In-state:** fresh after act-boundary wipe: empty bg, then the three ponds drawn in sequence (`Create`).
- **Out-state:** the half/quarter/eighth strip holds; it is the conceptual bridge to the closing walk (Shot 12).

**Transition S11→S12: cut.** Same recap layout continues into the final line; no wipe (mid-recap, not an act boundary — the only allowed wipes are the three marked boundaries).

---

## Shot 12 — Payoff close: Day 30 walk with new perspective (Beat 8, part 2)

- **Scene class:** `Shot12PayoffClose` (`scenes/scene_12.py`)
- **Narration lines (verbatim):**
  - Beat 8 [~4:20–4:40]: "She walks past the pond on Day 30 with a new perspective. Any doubling system hides the same pattern: nearly nothing, then half, then everything."
- **Visual content:** Return to the character (bookend of the hook):
  - The scientist figure walks past the fully covered pond again — this time she stops and looks, now "with a new perspective" (she pauses at the water's edge as in Shot 2, but the framing is calmer).
  - A final caption line appears via `Write()` in cream: **"nearly nothing, then half, then everything."** with three small icons beside it — an empty pond speck → a half-covered pond → a full pond (blue geometry), tying the visual motif to the closing words.
- **concrete_visual:** the scientist walking past the fully covered pond on Day 30 and stopping to look at it with new understanding; a three-icon strip of empty → half → full ponds.
- **abstract_symbol:** none — the close is character + pattern statement, no new symbol introduced (the fractions were already shown in Shot 11). Justified: payoff/character beat, concrete-only by design.
- **reveal_animation:** `Create()` for pond and icons; `Write()` for caption line. Scientist walks via position animation.
- **Hold content:** scientist at the water's edge + fully covered pond + closing caption with three-icon strip — all persist to the final frame. No empty hold.
- **In-state:** arrives from Shot 11: the half/quarter/eighth strip resolves into the single full pond; scientist enters from left along the top path (same path as Shots 1–2).
- **Out-state:** final frame holds on scientist + full pond + caption; episode ends. No out-transition needed (end of video).

**Transition S12→(end): none.** Hold final frame to black per editor's assembly notes (not a storyboard wipe — the three allowed wipes are already used at act boundaries).

---

## Scene → Beat mapping table

| Shot | Scene class | File | Beats covered | Beat timing label |
|------|-------------|------|---------------|-------------------|
| 1 | `Shot01HookWalk` | `scenes/scene_01.py` | Beat 1 (part 1: Days 1–15) | [0:00–~0:20] |
| 2 | `Shot02HookClimax` | `scenes/scene_02.py` | Beat 1 (part 2: Day 30 + riddle) | [~0:20–0:35] |
| 3 | `Shot03Motivation` | `scenes/scene_03.py` | Beat 2 (full) | [0:35–1:05] |
| 4 | `Shot04SplitScreen` | `scenes/scene_04.py` | Beat 3 (full) | [1:05–1:40] |
| 5 | `Shot05Formula` | `scenes/scene_05.py` | Beat 4 (part 1: formula intro) | [1:40–~2:00] |
| 6 | `Shot06Day15Table` | `scenes/scene_06.py` | Beat 4 (part 2: Day-15 plug-in + table) | [~2:00–2:10] |
| 7 | `Shot07OneStepBack` | `scenes/scene_07.py` | Beat 5 (full) | [2:10–2:40] |
| 8 | `Shot08LabSetup` | `scenes/scene_08.py` | Beat 7 (part 1: lab setup) | [3:00–~3:20] |
| 9 | `Shot09LabQuestion` | `scenes/scene_09.py` | Beat 7 (part 2: question + rule → 11 am) | [~3:20–3:35] |
| 10 | `Shot10LabEighth` | `scenes/scene_10.py` | Beat 7 (part 3: one eighth at 9 am) | [~3:35–3:55] |
| 11 | `Shot11Recap` | `scenes/scene_11.py` | Beat 8 (part 1: law + half/quarter/eighth) | [3:55–4:20] |
| 12 | `Shot12PayoffClose` | `scenes/scene_12.py` | Beat 8 (part 2: Day-30 walk close) | [~4:20–4:40] |

**Beat coverage check:** all 8 beats covered. Beat 6 (Result, "The pond was half-covered on Day 29…") is **carried inside Shot 7's hold/out-state** — the `Day 29 = 50%` reversal IS the result statement; its narration line ("The pond was half-covered on Day 29. Halfway in time was Day 15, but halfway in growth happened twenty-four hours before the end. When a process doubles, the final step accounts for half of everything ever produced.") is spoken over Shot 7's final hold and the S7→S8 wipe. *Note to Director:* Beat 6 has no dedicated shot; it is voiced during the transition out of Shot 7. If a dedicated result shot is preferred, split Shot 7 into reversal (Beat 5) + result statement (Beat 6). Flagged below as [DIR-NODECIDE].

---

## [DIR-NODECIDE] flags

1. **Shot 7 / Beat 6 boundary:** The reviewed script's Beat 6 (Result) is a standalone beat, but its content ("The pond was half-covered on Day 29…") is the verbal landing of Shot 7's reversal animation. I have placed Beat 6's narration over Shot 7's out-state/wipe rather than giving it a dedicated shot. **Director to decide:** (a) keep as-is (Beat 6 voiced during S7→S8 wipe), or (b) add a dedicated `Shot07bResult` scene for Beat 6 with its own hold frame (e.g., the halved pond + a large `Day 29 = 50%` result card). Option (b) adds ~1 shot and is cleaner for narration timing.
2. **Shot 7 generalization (20-day pond):** The reviewed script's Beat 5 does not mention a 20-day pond; the generalization comes from brief §5c last bullet and is supported by the line "no matter how long the journey took." I have shown it visually-light (compact side-by-side, no re-derivation). **Director to confirm** this visual-light treatment is acceptable, or direct that it be dropped/kept verbal-only.
3. **Shot 4 naming:** Brief §5a says show panels BEFORE naming "linear"/"exponential." I have kept Shot 4 free of those on-screen words (names were introduced verbally + as labels in Shot 3). **Director to confirm** this satisfies the brief's intent, or whether Shot 3's labels should be delayed until after Shot 4.

---

## Continuity declarations (shot-to-shot)

- **S1→S2:** Day-15 pond state + counter chip carry forward unchanged; scientist re-enters and walks to full coverage. Same top-down framing, same pond shape.
- **S2→S3:** Full wipe (act boundary). New layout: tap/cup + linear-vs-exponential comparison. The "Day 15?" caption from S3 echoes the hook's unanswered riddle.
- **S3→S4:** Slide+zoom; the right panel's lily pad resolves into the split-screen's exponential pond. Linear/exponential idea persists at pond scale (unnamed on screen in S4).
- **S4→S5:** Zoom out + fade; the exponential pond becomes the water surface for the formula pairing. Formula introduced here and persists to S6.
- **S5→S6:** Cut; formula `fraction(n) = 2^n / 2^30` persists at top (equation persistence). Day-15 substitution added below; pad shrinks to a speck. Table appears with Day-15 punchline + highlighted Day-29 row.
- **S6→S7:** Slide; table exits down, pond re-centers fully covered at Day 30. The orange-highlighted Day-29 `50.0%` from the table is exactly what the reversal animation lands on.
- **S7→S8:** Full wipe (act boundary). New scene: lab + petri dish. Container-halving motif transfers from pond to dish.
- **S8→S9:** Cut; full dish at noon persists; question + timeline added; rule applied → half at 11 am.
- **S9→S10:** Cut; half-full dish at 11 am persists; backward two more hours → one eighth at 9 am with `1/8` fraction.
- **S10→S11:** Full wipe (act boundary). Recap: three shrinking pond states (half/quarter/eighth) — returns to the hook's pond shape.
- **S11→S12:** Cut; half/quarter/eighth strip resolves into single full pond; scientist walks past with new perspective; closing caption + three-icon strip hold to end.

**Recurring motifs (full register in `continuity.md`):** day counter chip, top-down oval pond shape, container-halving motif (pond → petri dish), orange-highlighted 50% state, "nearly nothing, then half, then everything" pattern strip.
