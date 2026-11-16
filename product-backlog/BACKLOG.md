# Video-channel — Automation Backlog

Engineering backlog for automating end-to-end production of polished math-tutorial videos. This is NOT the episode-content roadmap: producer.md owns `productions/backlog.md` (episode topics). This file owns tooling and automation work only. Every item below is implemented later through this repo's mandatory build loop (athena -> gaia -> nemesis; animation portions routed to studio agents per CLAUDE.md) — this backlog implements nothing itself.

## Status

| Item | Story | Status |
|------|-------|--------|
| E1-I1 | Create project venv and install manimgx | Not started |
| E1-I2 | Render smoke test | Not started |
| E1-I3 | LaTeX toolchain verification for MathTex | Not started |
| E1-I4 | Install and verify ffmpeg/ffprobe | Not started |
| E1-I5 | Codify the productions layout | Not started |
| E2-I1 | Options evaluation spike (no vendor committed) | Not started |
| E2-I2 | Pluggable TTS adapter contract | Not started |
| E2-I3 | Per-beat audio and timing-map integration | Not started |
| E3-I1 | Channel bible and pilot brief | Not started |
| E3-I2 | Script, adversarial math review, director sign-off | Not started |
| E3-I3 | Storyboard and continuity register mechanics | Not started |
| E3-I4 | Scene code driven by the timing map | Not started |
| E3-I5 | Editor assembly to final.mp4 | Not started |
| E3-I6 | QC gate loop to clean | Not started |
| E3-I7 | Release artifact | Not started |
| E4-I1 | One-command episode orchestrator | Not started |
| E4-I2 | Machine-readable gate verdicts | Not started |
| E4-I3 | Parallel animator and narration-engineer execution | Not started |
| E5-I1 | Deterministic chapters and thumbnail extraction | Not started |
| E5-I2 | Publish preflight check | Not started |
| E6-I1 | Transition smoothing pass | Not started |
| E6-I2 | Parallel scene rendering benchmark | Not started |
| E6-I3 | Snapshot regression tests for generated scenes | Not started |
| E6-I4 | Loudness measurement automation and music-bed provenance | Not started |
| E6-I5 | Episode archiving and cleanup policy | Not started |

Status values: **Not started** (no work begun) · **In progress** (build loop running) · **Built** (implemented, awaiting nemesis verification) · **Done** (built and tested, nemesis verdict CLEAN).

## Epics

- [Epic 1: Environment setup](epic-1-environment-setup.md) — detailed
- [Epic 2: TTS and voice cloning](epic-2-tts-and-voice-cloning.md) — detailed
- [Epic 3: Pilot episode end-to-end (studio pipeline)](epic-3-pilot-episode-end-to-end.md)
- [Epic 4: Automation glue](epic-4-automation-glue.md)
- [Epic 5: Publishing and release tooling](epic-5-publishing-and-release-tooling.md)
- [Epic 6: Polish and iteration (surfaced by the pilot)](epic-6-polish-and-iteration.md)

## Conventions
- Item ids are stable: `E<n>-I<m>`; an id never changes once its item is done.
- Ordering rule: epics appear in fixed order E1..E6; every item's dependencies reference only items that appear earlier in this file (global topological order). An item is ready when all of its dependencies are done.
- Every item has exactly these fields, one line each: Description, Depends on, Acceptance criteria.
- Status is tracked in the table above and in each epic file's own table; update both when an item changes state.
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
