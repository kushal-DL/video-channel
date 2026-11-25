# Sign-offs — cr-01-pond-half-covered

Gatekeeper approval log. Each entry records what was verified, decisions made, and the explicit scope of approval. Never approve silently: every handoff artifact is read in full before sign-off.

---

## Storyboard v1.0 — Director review & approval

**Date:** 2026-11-22
**Artifact reviewed:** `storyboard.md` (12 shots, S1–S12) + `continuity.md` register (proposed by Storyboardist)
**Upstream gate already cleared:** Math review **PASS** — see `gates/math-review.json` (verdict PASS, 11/11 claims verified, worked example confirmed end-to-end; single correction C1 "one sixteenth" → "one eighth" applied in script-reviewed.md Part A Beat 7). No re-verification of math was required at this stage.

### What I verified

**1. Narration verbatim check (all 8 beats) — PASS.**
Every shot's narration line is an exact substring of `script-reviewed.md` Part A; every real sentence of Beats 1–8 is covered by a shot line. Confirmed programmatically (substring match after whitespace normalization, `[MR]` tags stripped). Spot-checks:
- S1/S2 = Beat 1 split at "Then Day 30 arrives." — verbatim.
- S3 = Beat 2 full — verbatim.
- S4 = Beat 3 full — verbatim.
- S5/S6 = Beat 4 parts 1/2 — verbatim.
- S7 = Beat 5 full — verbatim.
- **S10 (Beat 7 part 3) says "one eighth"** — the math-corrected value per C1/C9, confirmed present in the storyboard line and matching script-reviewed.md exactly. No residual "one sixteenth" anywhere in shot narration.
- S8/S9 = Beat 7 parts 1/2 — verbatim.
- S11/S12 = Beat 8 parts 1/2 — verbatim.
- **Beat 6** has no dedicated shot line; its full text appears verbatim only in the storyboard's beat-coverage note (voiced over S7 out-state/wipe). This is Flag 1, decided below as D1.

**2. Brief §5 compliance — PASS.**
- **§5a split-screen:** two ponds side by side with a *shared* day counter ticking simultaneously (S4); left = equal-slice progress-bar fill, right = near-empty until ~Day 25 then explosive; Day-10 "both nearly bare" and Day-30 emphasis beats scripted. Panels shown before on-screen naming — see D3 for the ruling on S3's labels and the §8 hook-shot tension.
- **§5b coverage table:** columns `Day | Coverage fraction | % of pond`; rows Days 15, 25–30; Day-15 row carries the **`0.003%` punchline** (orange callout + echoed `Day 15?` tag from S3); **Day-29 row highlighted orange with `50.0%`**; Day-30 row `100%`. All present in S6.
- **§5c one-step-back reversal:** S7 starts fully covered at `Day 30` / `100%`, reverses one step to exactly half at `Day 29` with orange `50%` overlay; generalization to a 20-day pond (`Day 20 → Day 19`) shown visual-light — see D2.
- **§5d concrete↔abstract at first formula:** S5 shows the growing lily pad (left) and `fraction(n) = 2^n / 2^30` in orange (right) appearing *simultaneously* via `Write()`; no formula on a blank background anywhere.

**3. Channel-bible compliance — PASS.**
- **Palette:** exactly the 4 roles (bg `#0F172A`, cream text, orange math, blue geometry); lily pads use blue outline + cream center to stay in-palette; no red/green/ad-hoc hues.
- **Reveals:** all equations/math via `Write()`/`Create()`, never `FadeIn()`; geometry via `Create()`; the S7/S9 "halving" is object removal of concrete pads/dots (explicitly not a math FadeIn) — compliant.
- **Full wipes only at the three act boundaries** (A1 Hook→Body after Beat 1, A2 Build-up→Worked example after Beat 6, A3 Worked example→Recap after Beat 7); all other transitions are cut/slide/zoom/morph; no mid-act wipe.
- **Holds carry active content:** every shot's hold frame is specified with on-screen elements; no empty-background holds.
- **Concrete↔abstract pair named in every shot:** each shot carries explicit `concrete_visual` / `abstract_symbol` fields, with "none — justified" only where the beat is concrete-only by design (S1, S2 hook; S8 setup; S12 close), matching brief §6.
- **Equation persistence:** formula introduced in S5 persists unchanged into S6 (substitution added below, not replacing); no clear-and-redraw.

**4. Continuity register — APPROVED with the amendments recorded in `continuity.md` §6.** Character design spec (minimal geometric scientist figure, one shared mobject across all appearances), 4-role palette usage table, motif register (day-counter chip, canonical pond oval, lily pad states, container-halving motif, pattern strip, one-shot coverage table), notation choices (`fraction(n) = 2^n / 2^30`, `1/2`/`1/4`/`1/8` always orange, lowercase `am`/`noon` time notation), and the three-act-boundary wipe table are all consistent with the storyboard and the channel bible. Approved as the Animator's source of truth for recurring elements.

### Director decisions on [DIR-NODECIDE] flags (binding)

**D1 — Beat 6 (Result): ADD a dedicated result shot.**
Option (b). Insert `Shot07bResult` (`scenes/scene_07b.py`) between S7 and S8 carrying Beat 6's full narration over its own hold. Hold frame: halved pond persists at left + large `Day 29 = 50%` result card (`Write()`, orange numeral on cream). Transitions: S7→S7b cut; S7b→S8 full wipe A2 (the act-boundary wipe now exits the result card, not mid-narration). Rationale: the pilot's #1 defect was A/V sync from scenes shorter than their beats — a beat with no dedicated hold frame is exactly that risk; Beat 6 is also the pacing arc's "Result statement" segment (brief §7) and deserves its own landing. Consequence: scene count becomes 13 (`scene_01.py … scene_12.py` + `scene_07b.py`). Recorded in continuity.md §6, D1.

**D2 — S7 generalization (20-day pond): CONFIRMED visual-light, keep as storyboarded.**
This is required content, not invention: brief §3 (misconception 3) and §5c's last bullet both mandate the shorter-journey generalization ("it doesn't matter if it's 30 days or 20 days"), and "no matter how long the journey took" licenses showing it. Binding constraints for Animator: no re-derivation, no new formula; same canonical oval at smaller scale; identical container-halving animation grammar (`Day 20 → Day 19`); must not outstage the Day-30→Day-29 reversal, which remains the shot's hero. It is a generalization of the law (brief §5c), distinct from the Beat 7 worked example, so it does not conflict with the channel-bible "different real-world context" rule. Recorded in continuity.md §6, D2.

**D3 — S4 naming timing: CONFIRMED as storyboarded; do NOT delay S3's labels.**
The flagged question is satisfied: S4 shows both panels before any on-screen naming *in the demonstration shot itself*, and Beat 3's narration never says "linear"/"exponential" (it describes behavior), so the names introduced in S3 are definitions, not a spoiler. Delaying S3 labels to after S4 would orphan the definitions and weaken Beat 2 — rejected.
**Additional ruling (§8 hook-shot tension):** brief §8 says both split-screen panels "must appear in the hook shot," while §5a calls the split-screen "the hook's visual backbone"; the storyboard places them in S4 (body). Ruling: §5a's operative requirement is *show panels before naming* (satisfied per D3.1); a literal 30-second hook cannot also carry the 30-day fill time-lapse without violating the hook's "do not define exponential growth" rule (§6) and the ≤50 s hook budget. The split-screen stands in S4 as the body's visual backbone, with its seed (the two-panel comparison) planted in S3 for continuity from motivation into build-up. No storyboard change required; this interpretation is binding for Animator and QC. Recorded in continuity.md §6, D3.

### Approval line

**Approved for Animator — storyboard v1.0**, subject to the three decisions above (D1 adds `scene_07b.py`; D2/D3 are confirmations of existing content). The Animator may proceed to scene code using `storyboard.md` + `continuity.md` (with §6 amendments) as the source of truth. Narration is locked verbatim to script-reviewed.md Part A; do not reword any line during animation.

— Director, 2026-11-22
