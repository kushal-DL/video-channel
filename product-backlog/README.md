# Product Backlog

This directory contains the structured backlog for Video-Channel's development and production pipeline.

## Structure

| File | Purpose |
|------|---------|
| `BACKLOG.md` | Master index of all epics, user stories, and current status |
| `epic-*.md` | Detailed specifications for each epic (goals, acceptance criteria, risks) |

## Status Workflow

Each story progresses through four states:

1. **Not started** — No work begun
2. **In progress** — Build loop running (athena → gaia → nemesis)
3. **Built** — Implemented, awaiting nemesis verification
4. **Done** — Built and tested with nemesis verdict CLEAN

## Epic Naming Convention

- Format: `epic-N-topic.md` where N is the epic number
- Examples:
  - `epic-1-environment-setup.md`
  - `epic-2-tts-and-voice-cloning.md`
