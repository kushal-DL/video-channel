# Video-channel

Automated production of **math tutorial videos** using [manimgx](https://github.com/academa-labs/manimgx) for animation. Each episode's artifacts live under `productions/<episode-slug>/` (brief, script, storyboard, scene code, audio, renders). The repo is currently in setup phase — no production code yet.

## Repository structure

All agents and automation scripts **must** follow the canonical directory layout defined in [REPO_STRUCTURE.md](REPO_STRUCTURE.md). This includes:

- Artifact placement (plans/, reviews/, productions/, scripts/, docs/)
- Per-episode directory structure under `productions/<slug>/`
- Naming conventions for files and directories
- Agent artifact ownership rules

Before creating any new files or directories, consult REPO_STRUCTURE.md to ensure compliance. Do not invent alternative layouts or ad-hoc file locations.

## Environment

- Claude Code runs against a **local LM Studio proxy**. Two models are available:
  - **Qwen 3.8 27B** — `qwen3.8-27b-fable-5-coding-distilled` (the default model)
  - **9B model** ("Qwen 3.8 9B") — registered as `qwen3.5-9b-the-defiant-fable-uncensored-heretic-neo-imatrix-max-mtp`
- Web tools (WebSearch/WebFetch) are unavailable through the local proxy — do not use them; work from the codebase and local files only.

## Build protocol (mandatory)

Whenever building anything from this project's context, run the agent trio in order — never implement build tasks directly in the main session:

1. **athena** (planner, 27B) — spawn FIRST for any build task. It writes an executable plan with acceptance criteria to `plans/<task>.md`. No code until a plan exists.
2. **gaia** (builder, 9B, minimal thinking) — implements the plan exactly: code plus tests, runs them until green, reports actual command output.
3. **nemesis** (red team: 27B attack plan via subagent + 9B execution) — independently re-verifies everything gaia claims, detects spoofed/stubbed work and hallucinations, checks security gaps and artifact quality, writes `reviews/<task>-<ts>.md`.

On a nemesis `VERDICT: FAIL`, re-spawn **gaia** with the review file as feedback; loop until nemesis returns `VERDICT: CLEAN`. Never skip nemesis for anything that ships. Trivial single-line fixes (typos, config values) may be made directly without the loop.

## Animation studio agents

When a build task is about **video/animation production** — manimgx scenes, renders, voiceover sync, episode assembly — use the animation-studio agent team instead of the generic trio for that portion of work: producer, director, screenwriter, math-reviewer, storyboardist, animator, narrator, editor, qc-reviewer, publisher (roster designed 2026-11-15; see conversation history).

> **TODO:** this section is a placeholder. When the studio agents are created under `.claude/agents/studio/`, replace it with their exact names and invocation rules. Until they exist, studio tasks follow the athena → gaia → nemesis loop above.
