# Video-channel

Automated production of **math tutorial videos** using [manimgx](https://github.com/academa-labs/manimgx) for animation. Each episode's artifacts live under `productions/<episode-slug>/` (brief, script, storyboard, scene code, audio, renders). The repo is currently in setup phase — no production code yet.

## Repository structure

All agents and automation scripts **must** follow the canonical directory layout defined in [REPO_STRUCTURE.md](REPO_STRUCTURE.md). This includes:

- Artifact placement (plans/, reviews/, productions/, scripts/, docs/)
- Per-episode directory structure under `productions/<slug>/`
- Naming conventions for files and directories
- Agent artifact ownership rules

Before creating any new files or directories, consult REPO_STRUCTURE.md to ensure compliance. Do not invent alternative layouts or ad-hoc file locations.

## Workspace & session continuity (mandatory)

Claude maintains a `_workspace/` folder for its own planning and context:

- **`_workspace/session.md`** — rolling context file. **Read it first** at the start of a session to recover prior state. **Update it** at the end of meaningful work with: what changed, what's done, what's next.
- **`_workspace/claude_plans/latest/`** — the current active plan(s). Only the plan(s) in flight live here.
- **`_workspace/claude_plans/archive/`** — superseded plans. When a plan is completed or replaced, **move it** from `latest/` to `archive/` (do not delete).

Rules:
1. Every non-trivial plan Claude writes goes in `_workspace/claude_plans/latest/`, not scattered elsewhere.
2. Before starting a new plan, move any stale plan from `latest/` to `archive/`.
3. These are distinct from `plans/` (athena build plans) — `_workspace/` is Claude's own session-level planning, `plans/` is the formal build-protocol output.

## Environment

- Claude Code runs against a **local LM Studio proxy**. Two models are available:
  - **Qwen 3.8 27B** — `anthropic--claude-sonnet-latest` (the default model; proxy alias — the old ID `qwen3.8-27b-fable-5-coding-distilled` is no longer valid)
  - **9B model** ("Qwen 3.8 9B") — use model alias `anthropic--claude-haiku-latest` in agent frontmatter (the old ID `qwen3.5-9b-the-defiant-fable-uncensored-heretic-neo-imatrix-max-mtp` is no longer valid)
- Web tools (WebSearch/WebFetch) are unavailable through the local proxy — do not use them; work from the codebase and local files only.

## Tool execution & anti-loop rules (mandatory)

All agents and sessions must strictly obey these anti-loop rules:
1. **No Identical Retries**: NEVER repeat an identical or near-identical tool call or command that failed. If a command returns an error, carefully inspect the exact error message and correct the arguments/syntax before calling it again.
2. **Two-Strike Circuit Breaker**: If any command, parameter, or sub-task approach fails 2 times consecutively, immediately stop that approach. Switch to a completely different strategy or stop and report the blocker. Never attempt a 3rd try with the same approach.
3. **Strict Scope Verification**: Restrict verification exclusively to the explicit Acceptance Criteria of the task or plan. Never invent auxiliary test suites, secondary stress tests, or benchmark suites beyond what is asked.

## Execution modes & agent routing

To avoid unnecessary latency and token churn, follow this tiered execution model:

### 1. Fast Path (Direct in Main Session — No Athena / Gaia / Nemesis)
Execute directly in the main session without spawning subagents for:
- **Backlog & docs management**: Reordering, renaming, creating, or editing tasks in `BACKLOG.md`, `plans/`, `docs/`, `reviews/`, or `REPO_STRUCTURE.md`.
- **Environment & config edits**: `.claude/settings.json`, `.env`, installing packages/tools, setting environment variables or flags.
- **Bug fixes & targeted patches**: Small bug fixes, syntax corrections, or code updates under ~25 lines where a formal architectural plan is overhead.
- **Quick audits & queries**: Inspecting file trees, checking status, running smoke tests, or verifying syntax.

### 2. Full Build Protocol (Athena → Gaia → Nemesis)
Mandatory **ONLY** for new feature implementations, new automation tools (`scripts/*.py`), or substantial multi-file pipeline changes:

1. **athena** (planner, 27B) — spawn FIRST. Writes an executable implementation plan with acceptance criteria to `plans/<task>.md`. No code until a plan exists.
2. **gaia** (builder, 9B, minimal thinking) — implements the plan exactly: code plus tests, runs them until green, reports actual command output.
3. **nemesis** (red team: 27B attack plan via subagent + 9B execution) — independently re-verifies what gaia claims, checks security gaps and artifact quality, writes `reviews/<task>-<ts>.md`.

On a nemesis `VERDICT: FAIL`, re-spawn **gaia** with the review file as feedback; loop until nemesis returns `VERDICT: CLEAN`.

## Animation studio agents

When a build task is about **video/animation production** — manimgx scenes, renders, voiceover sync, episode assembly — use the animation-studio agent team instead of the generic trio for that portion of work: producer, director, screenwriter, math-reviewer, storyboardist, animator, narrator, editor, qc-reviewer, publisher (roster designed 2026-11-15; see conversation history).

> **TODO:** this section is a placeholder. When the studio agents are created under `.claude/agents/studio/`, replace it with their exact names and invocation rules. Until they exist, studio tasks follow the athena → gaia → nemesis loop above.
