# Plan: product backlog for math-tutorial video automation

**Goal** — Produce the engineering/product backlog that will drive end-to-end automation of polished manimgx math-tutorial videos in this repo. "Done" means gaia has created exactly two files: `BACKLOG.md` at the repo root containing verbatim the backlog content specified below (epics E1–E6, 25 items, gap list), plus a stdlib-only structural test script `tests/test_backlog.py` that passes on it. Nothing else is modified or created; no manimgx/ffmpeg/LaTeX installation happens in this task. Routing note per CLAUDE.md: this task itself creates only documentation and one test script (no animation production), so it stays in the athena → gaia → nemesis loop; when backlog items E1–E6 are later implemented, their animation portions must be routed to the studio agents (producer … release-agent) per CLAUDE.md's build protocol.

**Assumptions**
- Deliverable location: `BACKLOG.md` at repo root (the task's default choice; no reason found not to). It is explicitly distinct from the episode-content roadmap that producer.md maintains at `productions/backlog.md`; BACKLOG.md's header says so, and the two never share a path.
- Backlog items are specifications only. Each future item will be implemented through its own build loop (athena → gaia → nemesis), with animation work routed to the studio agents. This task does not execute any of E1–E6.
- Pilot episode is fixed as "Deriving the quadratic formula", slug `pilot-01-quadratic-formula`, because animator.md's canonical example scene is named `DeriveQuadraticFormula` — this keeps cross-file references verifiable by nemesis.
- TTS policy per user instruction: Epic E2 evaluates option families as decision inputs only and defines a pluggable adapter contract; **no vendor or backend is committed anywhere in BACKLOG.md**. edge-tts appears solely as one candidate family inside E2-I1 because narration-engineer.md references it (its `tts` CLI does not exist locally — unverified, flagged). The final backend decision waits on the user's separately downloaded voice-cloning model.
- Environment facts verified 2026-11-15 in this repo: Python 3.14.8 and `uv` (/home/doomlord/.local/bin/uv) present; ffmpeg and ffprobe absent from PATH; manimx/manimpango not installed; latexmk/pdflatex/xelatex not found. Hence E1 items are install-and-verify, and every claim about existing agents below is cited to the `.claude/agents/*.md` file actually read (all 13 agent files were read in full).
- The test script uses only the Python standard library because pytest availability was not verified locally; `python3` itself is confirmed present.

**Changes**

1. Create `/home/doomlord/Documents/Work/repos/Video-channel/BACKLOG.md` — new file at repo root, written with a single Write call containing **exactly** the content of the fenced block below (verbatim: no rewording, no added sections, no dropped lines; inline backticks preserved).

```markdown
# Video-channel — Automation Backlog

Engineering backlog for automating end-to-end production of polished math-tutorial videos. This is NOT the episode-content roadmap: producer.md owns `productions/backlog.md` (episode topics). This file owns tooling and automation work only. Every item below is implemented later through this repo's mandatory build loop (athena -> gaia -> nemesis; animation portions routed to studio agents per CLAUDE.md) — this backlog implements nothing itself.

## Conventions
- Item ids are stable: `E<n>-I<m>`; an id never changes once its item is done.
- Ordering rule: epics appear in fixed order E1..E6; every item's dependencies reference only items that appear earlier in this file (global topological order). An item is ready when all of its dependencies are done.
- Every item has exactly these fields, one line each: Description, Depends on, Acceptance criteria.
- TTS policy: Epic E2 evaluates options and defines the adapter contract only; no item commits a TTS vendor/backend as the channel default until the user's separately downloaded voice-cloning model lands (status tracked as "pending user model download" in `productions/tts-options.md`).

## E1: Environment setup
### E1-I1: Create project venv and install manimgx
- **Description:** Use uv to create `.venv` at repo root, install manimx into it, and record the exact versions used. (Verified 2026-11-15: manimx is not installed.)
- **Depends on:** none
- **Acceptance criteria:** `uv venv .venv && uv pip install --python .venv/bin/python manimgx` exits 0; `.venv/bin/manimgx --version` prints a version string recorded in `docs/env.md`, created by this item.

### E1-I2: Render smoke test
- **Description:** Prove the animator's documented render command works end-to-end with a trivial scene (command form taken from animator.md).
- **Depends on:** E1-I1
- **Acceptance criteria:** `productions/_smoke/scenes/smoke.py` contains one Scene class named `SmokeTest` using only Text and VGroup (no MathTex); `.venv/bin/manimgx productions/_smoke/scenes/smoke.py SmokeTest -ql --disable_caching` exits 0 and produces a non-empty mp4; the exact command and its real output are recorded in `docs/env.md`.

### E1-I3: LaTeX toolchain verification for MathTex
- **Description:** Real math scenes use MathTex, which requires a local TeX distribution (verified 2026-11-15: none found); verify or install one.
- **Depends on:** E1-I2
- **Acceptance criteria:** A second smoke scene `SmokeLatex` containing exactly one `MathTex(r"x^2")` renders with the same command form as E1-I2, exit 0, non-empty mp4; if LaTeX was installed by this item, the package names are recorded in `docs/env.md`.

### E1-I4: Install and verify ffmpeg/ffprobe
- **Description:** editor.md (loudness, chapters), narration-engineer.md (duration probing) and qc-reviewer.md (frame extraction) all assume ffmpeg/ffprobe on PATH; neither was found locally as of 2026-11-15.
- **Depends on:** none
- **Acceptance criteria:** `ffmpeg -version` and `ffprobe -version` both exit 0 after install; versions recorded in `docs/env.md`.

### E1-I5: Codify the productions layout
- **Description:** Every studio agent assumes artifact paths (brief.md, script.md, script-reviewed.md, storyboard.md, scenes/, audio/beat_*.mp3, timing.json, continuity.md, signoffs.md, final.mp4, qc-report.md, release.md) but no document defines them in one place.
- **Depends on:** none
- **Acceptance criteria:** `productions/README.md` lists the canonical per-episode tree under `productions/<slug>/`, each entry citing which `.claude/agents/*.md` file creates it; a check confirms every cited path appears as a literal string in at least one agent file.

## E2: TTS and voice cloning
### E2-I1: Options evaluation spike (no vendor committed)
- **Description:** Evaluate candidate TTS option families against fixed decision criteria and produce a comparison document only; this item installs no backend and adopts none as default.
- **Depends on:** none
- **Acceptance criteria:** `productions/tts-options.md` lists at least 3 option families (e.g., local open-source voice-cloning models the user will download separately, cloud TTS APIs, locally runnable CLI tools such as edge-tts); every family row is scored on exactly three criteria — cloning quality, local runnability (hardware requirements), licensing; the document ends with a recommendation explicitly marked "pending user model download" and no `.claude/agents/*.md` file is modified.

### E2-I2: Pluggable TTS adapter contract
- **Description:** Define the single interface narration-engineer.md's workflow calls so the backend can be swapped when the user's voice-cloning model arrives; implement it against whichever family E2-I1 found locally runnable today, with a named error (never silent failure) for unconfigured backends.
- **Depends on:** E2-I1
- **Acceptance criteria:** `scripts/tts.py` takes beat text and an output path; running it produces a real audio file whose ffprobe duration is greater than 0 for the fixture sentence "The quadratic formula gives x equals negative b plus or minus the square root of b squared minus four ac, over two a."; unconfigured backends exit non-zero with a named error message; `scripts/tts.py --help` lists all supported backend names.

### E2-I3: Per-beat audio and timing-map integration
- **Description:** Prove the full narration contract end-to-end on a fixture script independent of the pilot episode: one audio file per beat plus `timing.json` in exactly the schema narration-engineer.md specifies, which is what drives animation durations downstream.
- **Depends on:** E2-I2, E1-I4
- **Acceptance criteria:** Fixture `productions/tts-fixture/script-reviewed.md` has exactly 5 numbered beats; running the adapter over all beats produces `audio/beat_01.mp3` through `audio/beat_05.mp3`; generated `timing.json` has keys `beats`, `total_duration_sec`, `narration_speed_wpm`; a verification run asserts beat count == audio file count == 5, each `duration_sec` equals the ffprobe duration within 0.05 s, and `total_duration_sec` equals the sum of beat durations within 0.1 s.

## E3: Pilot episode end-to-end (studio pipeline)
Pilot topic is fixed so every check below is deterministic: "Deriving the quadratic formula", slug `pilot-01-quadratic-formula`. All stages run as their named studio agents, and director sign-offs are recorded per director.md ("never approve silently").

### E3-I1: Channel bible and pilot brief
- **Description:** Producer creates `productions/channel-bible.md` — referenced by every downstream agent but not yet on disk — plus the pilot episode brief.
- **Depends on:** none
- **Acceptance criteria:** `productions/channel-bible.md` contains sections for visual norms, pacing norms, and narration voice profile as producer.md requires; `productions/pilot-01-quadratic-formula/brief.md` has numbered sections covering learning objective, prerequisites and misconceptions, key math claims, visual metaphors, and target length.

### E3-I2: Script, adversarial math review, director sign-off
- **Description:** Screenwriter writes the beat-numbered script with [MR] tags; math-reviewer produces the reviewed script; director records explicit approvals for both artifacts.
- **Depends on:** E3-I1
- **Acceptance criteria:** `script.md` numbers every beat and tags each factual math statement with [MR]; `script-reviewed.md` exists with corrections applied inline and unresolved claims marked [MR-UNCERTAIN]; `signoffs.md` contains explicit director approval entries naming both artifacts.

### E3-I3: Storyboard and continuity register mechanics
- **Description:** Storyboardist decomposes the reviewed script into shots; codify who writes `continuity.md`, since both storyboard.md and director.md claim it (rule to be recorded in signoffs: storyboardist proposes, director approves and amends).
- **Depends on:** E3-I2
- **Acceptance criteria:** `storyboard.md` has one shot per scene with narration beat numbers, visual content, in-state, out-state, and transition spec; a scripted check confirms every beat of script-reviewed.md is covered by exactly one shot; `continuity.md` exists with notation, motifs, and transitions sections.

### E3-I4: Scene code driven by the timing map
- **Description:** Animator writes one manimgx scene per storyboard shot using this episode's real `timing.json` (generated via the E2-I3 contract) to set animation durations; self-check render per animator.md.
- **Depends on:** E1-I2, E1-I3, E2-I3, E3-I3
- **Acceptance criteria:** `productions/pilot-01-quadratic-formula/scenes/` has one .py file with one named Scene class per storyboard shot; every scene renders at -ql with exit 0; a scripted check confirms each beat's allocated animation time in its scene equals the matching timing.json duration within 5%; `render-notes.md` exists (may state "no deviations").

### E3-I5: Editor assembly to final.mp4
- **Description:** Editor concatenates renders, muxes narration from timing.json, normalizes loudness toward -16 LUFS per editor.md, and embeds chapters.
- **Depends on:** E1-I4, E3-I4
- **Acceptance criteria:** `productions/pilot-01-quadratic-formula/final.mp4` exists; ffprobe duration equals timing.json `total_duration_sec` within 1 s; the file has one h264 video stream and one aac audio stream; `export-notes.md` records measured integrated loudness (quoted ffmpeg ebur128 output) and the chapter list.

### E3-I6: QC gate loop to clean
- **Description:** qc-reviewer inspects final.mp4 with at most 8 extracted frames, checks A/V sync against timing.json and on-screen math against script-reviewed.md; every critical finding is fixed (re-spawning animator/narration-engineer/editor as needed) and re-checked until none remain.
- **Depends on:** E3-I5
- **Acceptance criteria:** `productions/pilot-01-quadratic-formula/qc-report.md` exists with findings ranked critical to minor, each citing a frame number or timestamp plus exact evidence; every critical finding is marked resolved with the command output proving it; sampled beat-boundary sync drift is at most 0.3 s per qc-reviewer.md's threshold.

### E3-I7: Release artifact
- **Description:** release-agent produces `release.md` from final.mp4, timing.json, and script-reviewed.md.
- **Depends on:** E3-I6
- **Acceptance criteria:** `productions/pilot-01-quadratic-formula/release.md` contains a title, a description stating the learning objective, a chapter list whose MM:SS values equal cumulative beat boundaries from timing.json within 1 s, tags, and a thumbnail frame suggestion.

## E4: Automation glue
### E4-I1: One-command episode orchestrator
- **Description:** A script that runs a full episode hands-off in the fixed agent order (producer -> screenwriter -> math-reviewer -> director gate -> storyboardist -> animator || narration-engineer -> editor -> qc loop until clean -> release), halting with a clear report at any failed gate instead of continuing.
- **Depends on:** E3-I7
- **Acceptance criteria:** `scripts/run_episode.sh <slug>` supports `--dry-run`, which prints exactly the planned agent sequence and performs no work; an unattended run completes one episode end-to-end with no human intervention; a forced-failed gate stops execution before the next stage and exits non-zero.

### E4-I2: Machine-readable gate verdicts
- **Description:** Each stage writes `productions/<slug>/gates/<stage>.json` (status pass/fail plus notes) so the orchestrator branches on JSON rather than prose; director.md's "never approve silently" becomes mechanically enforced.
- **Depends on:** E4-I1
- **Acceptance criteria:** Every gate file parses as JSON with keys `stage`, `status`, `notes`; a fixture episode directory containing one failed gate causes the orchestrator to stop before the next stage (verified by running it).

### E4-I3: Parallel animator and narration-engineer execution
- **Description:** narration-engineer.md states it "runs in parallel with Animator"; make the orchestrator execute both concurrently after the storyboard gate.
- **Depends on:** E4-I1
- **Acceptance criteria:** Orchestrator flag `--parallel` runs scene authoring and audio generation concurrently; an episode produced with it passes all of Epic E3's acceptance checks (final.mp4 duration within 1 s of a serial run, same qc-report verdict).

## E5: Publishing and release tooling
### E5-I1: Deterministic chapters and thumbnail extraction
- **Description:** A script converts timing.json beat boundaries into YouTube chapter lines and extracts the suggested thumbnail frame with ffmpeg.
- **Depends on:** E3-I7
- **Acceptance criteria:** `scripts/make_release.py <slug>` prints a chapter list whose timestamps equal cumulative beat sums exactly (verified by script); `thumbnail.png` extracted at the release.md-suggested timestamp is a valid, non-empty image file.

### E5-I2: Publish preflight check
- **Description:** This environment has no web access through the local LM Studio proxy, so real uploads stay manual; provide a dry-run that validates everything an uploader would need without touching any remote service.
- **Depends on:** E5-I1
- **Acceptance criteria:** `scripts/publish_check.sh <slug>` exits 0 and prints a checklist (final.mp4 present with ffprobe metadata, release.md fields non-empty, chapters generated) when artifacts are complete; it exits non-zero listing exactly the missing pieces otherwise.

## E6: Polish and iteration (surfaced by the pilot)
### E6-I1: Transition smoothing pass
- **Description:** Editor applies crossfades between scene segments where qc-report flagged jarring cuts, as editor.md anticipates ("avoid jarring cuts between scenes").
- **Depends on:** E3-I6
- **Acceptance criteria:** The re-rendered episode's new qc-report contains no "jarring cut" findings at shot boundaries; export-notes.md records the transition parameters used.

### E6-I2: Parallel scene rendering benchmark
- **Description:** No agent file covers render parallelism; measure and document rendering multiple scenes concurrently to decide whether a small local render farm is worth it.
- **Depends on:** E1-I2, E3-I4
- **Acceptance criteria:** `docs/render-benchmark.md` records wall-clock times for serial versus concurrent rendering of the pilot's full scene set with the exact commands used; renders are reproducible (same input gives the same output checksum) or the document explains the observed non-determinism.

### E6-I3: Snapshot regression tests for generated scenes
- **Description:** animator.md and qc-reviewer.md both rely on visual inspection only; add an automated check so future edits to scene code cannot silently change on-screen math.
- **Depends on:** E3-I4
- **Acceptance criteria:** `scripts/scene_snapshots.py <slug>` renders each scene at fixed quality and compares key frames against stored baselines with a pixel-diff threshold; modifying any scene file's visible content makes the check fail (demonstrated once in its test report) while an unmodified re-run passes.

### E6-I4: Loudness measurement automation and music-bed provenance
- **Description:** editor.md assumes a licensed music bed at -25 LUFS relative to narration, but no agent sources, licenses, or records one; automate loudness verification and enforce provenance recording.
- **Depends on:** E3-I5
- **Acceptance criteria:** The assembly step measures integrated loudness with ffmpeg ebur128 and fails the build when it is more than 0.5 LU from the -16 LUFS target unless an explicit override flag is passed; export-notes.md records the music bed file path, source, and license text verbatim.

### E6-I5: Episode archiving and cleanup policy
- **Description:** Per-beat audio and scene renders are large; define retention (keep final.mp4, release.md, timing.json) and prune intermediates with a manifest, since no agent currently manages artifact lifecycle.
- **Depends on:** E3-I7
- **Acceptance criteria:** `scripts/archive_episode.sh <slug> --dry-run` lists exactly the files it would move without moving them; after a real run an archive manifest JSON parses and lists every moved path; re-running dry-run reports nothing left to prune.

## Gap list (capabilities no existing agent file covers)
- TTS backend choice: narration-engineer.md assumes a `tts` CLI with an edge-tts default that does not exist in this environment, and voice cloning appears in no agent file — E2-I1/E2-I2 define the evaluation and contract, but the final backend decision waits on the user's model download.
- Orchestration and gate enforcement: agent order, parallelism (narration-engineer.md) and director gating are prose only; nothing mechanically enforces them until Epic E4 lands.
- Continuity register ownership conflict: both storyboard.md and director.md write `productions/<slug>/continuity.md`; no file defines who wins on concurrent runs — E3-I3 must codify the rule before parallel execution exists (E4-I3).
- Render-farm / scene-level parallelism: absent from every agent file; only benchmarked in E6-I2.
- Automated testing of generated scenes: animator.md and qc-reviewer.md rely on visual inspection; no snapshot or regression test exists until E6-I3.
- Music bed sourcing and licensing: editor.md assumes the asset exists at a fixed loudness offset; no agent creates, licenses, or records provenance for it (E6-I4).
- Upload/publishing execution: release.md says its output "is consumed by your upload pipeline", but no such pipeline exists and web access is unavailable in this environment — only E5's dry-run checks are possible here.
- Asset storage and retention: large mp3/mp4 artifacts have no retention policy, the repo has no .gitignore, and it is not a git repository; version control strategy for renders and audio is undecided until after E6-I5.
- QC loop termination: qc-reviewer.md loops "until nemesis signs off clean" but defines no maximum iteration count or human escalation path when fixes oscillate.
```

2. Create `/home/doomlord/Documents/Work/repos/Video-channel/tests/test_backlog.py` — new file, Python 3 standard library only (no third-party imports; pytest is not assumed). It takes an optional argv[1] as the backlog path, defaulting to `BACKLOG.md` resolved against the current working directory. On success it prints exactly one line `BACKLOG-OK` to stdout and exits 0; on any failure it prints a short check name to stderr and exits 1 (never printing BACKLOG-OK). It must assert, in this order:
   - check `h1`: exactly one line starting with `# `.
   - check `sections`: exactly eight lines starting with `## `, in this exact order — the Conventions header; six epic headers matching regex `^## E[1-6]: `; and a final header starting `## Gap list`.
   - check `items`: exactly 25 item-header lines matching regex `^### E[1-6]-I\d+: `, no other line starts with `### `, ids are unique, and the id set equals exactly: E1-I1, E1-I2, E1-I3, E1-I4, E1-I5, E2-I1, E2-I2, E2-I3, E3-I1, E3-I2, E3-I3, E3-I4, E3-I5, E3-I6, E3-I7, E4-I1, E4-I2, E4-I3, E5-I1, E5-I2, E6-I1, E6-I2, E6-I3, E6-I4, E6-I5.
   - check `fields`: within each item's block (up to the next header line), exactly one line starting `- **Description:**`, one starting `- **Depends on:**`, and one starting `- **Acceptance criteria:**`, all with non-empty values after the colon.
   - check `deps`: every id listed in a Depends-on value exists as an item id AND appears earlier in file order than the referencing item (global topological order); the literal word `none` is allowed instead of ids; nothing else may appear on that line.
   - check `gaps`: the Gap list section contains at least 8 bullet lines starting with `- `.
   - check `tts-policy`: exactly one line in the whole file contains the exact sentence `no item commits a TTS vendor/backend as the channel default`.

**Tests** — The only test is `tests/test_backlog.py` (a structural verifier for BACKLOG.md; it asserts real content: the pinned 25-id set, topological dependency order, per-item field presence, gap-list size, and the TTS non-commitment sentence). Exact commands, all run from `/home/doomlord/Documents/Work/repos/Video-channel`:
- `python3 tests/test_backlog.py` — expect stdout exactly `BACKLOG-OK`, exit code 0.
- Mutation proof (run by nemesis too): make a temp copy with one item header removed and run `python3 tests/test_backlog.py /tmp/backlog-mutated.md` — expect non-zero exit and no `BACKLOG-OK` printed.

**Acceptance criteria**
1. Run `test -f BACKLOG.md && echo EXISTS` from the repo root — expect output `EXISTS`, exit code 0 (backlog at repo root, not under productions/).
2. Run `python3 tests/test_backlog.py` — expect stdout exactly one line `BACKLOG-OK`, exit code 0.
3. Run `grep -c '^### E[1-6]-I' BACKLOG.md` — expect output `25`; run `grep -c '^- \*\*Description:\*\*' BACKLOG.md` and the same for `- **Depends on:**` and `- **Acceptance criteria:**` — each expects `25`.
4. Run `grep -n '^## ' BACKLOG.md | cut -d: -f2-` — expect exactly 8 lines, in order: the Conventions header; `E1:` through `E6:` epic headers (no other ## sections); run `grep -c '^# ' BACKLOG.md` — expect `1`.
5. Run `grep -n 'no item commits a TTS vendor/backend as the channel default' BACKLOG.md | wc -l` — expect `1`; run `grep -c 'pending user model download' BACKLOG.md` — expect exactly `2` (the Conventions TTS-policy line and the E2-I1 acceptance criteria; no other item may mention it).
6. Run `grep -c 'pilot-01-quadratic-formula' BACKLOG.md` — expect exactly `6` (the E3 intro line plus the acceptance criteria of E3-I1, E3-I4, E3-I5, E3-I6 and E3-I7; no other epic may reference it).
7. Mutation check proves the test is not tautological: create a temp copy of BACKLOG.md with one item header line removed (e.g., delete the `### E2-I1:` line) and run `python3 tests/test_backlog.py <that-copy>` — expect non-zero exit code and no `BACKLOG-OK` in output.
8. Run `find . -path ./.claude -prune -o -type f -print | sort` from the repo root — expect exactly these 5 lines: `.env`, `BACKLOG.md`, `CLAUDE.md`, `plans/backlog-video-automation.md`, `tests/test_backlog.py`. Nothing else (no code, no docs/, no scripts/) may have been created by this task.
9. Run `grep -n 'import' tests/test_backlog.py` — expect only standard-library imports (`re`, `sys`, `os`, `argparse` are acceptable; anything else fails), and `python3 -m py_compile tests/test_backlog.py` exits 0.

**Risks**
- Verbatim-copy risk: BACKLOG.md must match the fenced block exactly (25 item headers, slug appearing exactly 5 times); if gaia rewords or "tidies" anything, acceptance criteria 3–6 fail — nemesis should diff the file against the plan's block rather than trusting grep counts alone.
- Long single-file Write: instructing one Write call for BACKLOG.md avoids partial writes; a truncated copy fails criterion 2 immediately (good failure mode).
- Backlog items reference future tooling and unverified APIs: manimgx CLI flags are quoted from animator.md but not yet verified locally until E1-I2 runs; this backlog deliberately asserts no manimgx API details beyond what agent files already state. All such spots stay "to be verified" in the item acceptance text, never as facts.
- `.env` exists at repo root and is excluded from every check above (criterion 8's expected set includes it but nothing reads or prints its contents); neither BACKLOG.md nor the test script may reference secrets.
- Future implementation of E2–E6 will hit this environment's web restriction again: E5-I2 is intentionally dry-run-only, and any item that needs external services must be re-scoped at build time rather than silently deferred.
