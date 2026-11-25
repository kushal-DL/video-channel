---
description: Initialize episode production from curriculum, generate scope.md and brief.md (Qwen 27B), and draft narration script (Gemma 9B)
argument-hint: <episode-number> <path/to/series-curriculum.md>
---

You are the Lead Producer and Production Director for the math tutorial channel. Execute the production initialization protocol for the episode specified in `$ARGUMENTS`.

Parse `$ARGUMENTS` into:
1. `EPISODE_NUM`: The target episode number (e.g. `2`).
2. `CURRICULUM_PATH`: Path to the curriculum or part file (e.g. `productions/cracked/curriculum/series-curriculum-part-01.md` or `productions/cracked/curriculum/series-curriculum.md`).

Execute these exact production steps:

---

### Step 1: Locate Episode Metadata
1. Inspect `CURRICULUM_PATH`.
   - If `CURRICULUM_PATH` is a master index containing links to part files (like `series-curriculum.md`), find which part file contains `EPISODE_NUM` and read that part file.
   - Extract the full table row for `EPISODE_NUM`:
     - **Title**
     - **Class Level**
     - **Subject**
     - **Riddle / Hook**
     - **Concept**
     - **Key Visuals**
2. Determine:
   - `SERIES_SLUG`: derived from path (e.g. `cracked`, `elementary`, `middle-school`, `high-school`).
   - `SERIES_PREFIX`: short prefix for episodes (e.g. `cr` for cracked, `ms` for middle school, `hs` for high school, `el` for elementary).
   - `EPISODE_SLUG`: `<SERIES_PREFIX>-<PAD2_NUM>-<short-descriptive-kebab-title>` (e.g. `cr-02-fold-paper-moon`).
   - `EPISODE_DIR`: `productions/<SERIES_SLUG>/<EPISODE_SLUG>`

---

### Step 2: Initialize Directory Structure
Create the canonical directory layout defined in `REPO_STRUCTURE.md`:
```bash
mkdir -p "${EPISODE_DIR}/scenes" "${EPISODE_DIR}/audio" "${EPISODE_DIR}/gates"
```

---

### Step 3: Producer Generates `scope.md` (Qwen 27B)
Write `${EPISODE_DIR}/scope.md` following the standard set in `productions/cracked/cr-01-pond-half-covered/scope.md`:
- **Header**: Title, Series name, Episode number, Class level, Subject, Target duration (determined organically by topic complexity between 2 and 11 minutes, hard gate [120s, 660s]; e.g. 2.5–4 minutes for riddles, 5–10 minutes for multi-step derivations. Never pad to hit an arbitrary floor).
- **Learning Objectives**: 4–5 bullet points covering definition, mechanism, intuition contrast, and formula.
- **Analogy → Concept Mapping**: Markdown table pairing concrete visual analogies with abstract math concepts.
- **Worked Examples**:
  - Example 1: The original riddle / concept solution step by step.
  - Example 2: Transfer to a DIFFERENT real-world domain (e.g. loan growth, physics, biology, computing).
- **Out of Scope**: Explicit list of concepts deliberately omitted to prevent overpromising.

---

### Step 4: Producer Generates `brief.md` (Qwen 27B)
Write `${EPISODE_DIR}/brief.md` following the standard in `cr-01-pond-half-covered/brief.md`:
- **Section 1: Learning Objective**: Plain language summary citing `scope.md`.
- **Section 2: Prerequisites**: Essential prior knowledge.
- **Section 3: Common Misconceptions to Address**: Table (Misconception, Why it happens, How to correct).
- **Section 4: Key Math Claims**: All factual claims tagged with `[MR]` for the Math Reviewer.
- **Section 5: Visual Metaphors**: Explicit concrete visual vs abstract symbol pairs for the Storyboardist.
- **Target Duration**: Must inherit `scope.md` duration verbatim.

---

### Step 5: Draft Script with Gemma Writer (GPU 1)
Run the dedicated script generator using the local fine-tuned Gemma model:
```bash
chmod +x scripts/gemma_writer.py
python3 scripts/gemma_writer.py --brief "${EPISODE_DIR}/brief.md" --scope "${EPISODE_DIR}/scope.md" --out "${EPISODE_DIR}/script.md"
```
*(This sends a clean HTTP request to `gemma-the-writer-mighty-sword-9b` on GPU 1 without Anthropic tool-calling schemas, preventing model crashes and tool errors).*

---

### Step 6: Script Quality & Anti-Slop Audit (Qwen 27B)
1. Read the newly generated `${EPISODE_DIR}/script.md`.
2. Verify against House Style (`productions/channel-bible.md`):
   - Ensure all factual math claims carry `[MR]` tags.
   - Check for banned openers ("Here is a...", "Let us...", "Notice that...").
   - Check for banned hype ("The answer will surprise you", "wrong by a mile").
   - Remove any em-dashes (`—`) and replace with commas or periods.
   - Confirm sentence rhythm has good variance (short <=8 words following long sentences).
3. If minor adjustments are needed, update `${EPISODE_DIR}/script.md`.

---

### Step 7: Production Hand-off Summary
Output a concise report to the user:
- **Episode Initialized**: Slug, Title, Class Level, Target Duration.
- **Artifacts Created**: `scope.md`, `brief.md`, `script.md`.
- **Word & Beat Count**: Summary of the script.
- **Next Production Action**: Hand-off to Math Reviewer (`/anti-slop ${EPISODE_DIR}/script.md` or math verification gate).
