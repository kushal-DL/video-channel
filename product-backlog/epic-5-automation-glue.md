# Epic 5: Automation glue

**Goal:** Build the orchestration layer that automates the episode production pipeline, enabling one-command episode builds, machine-readable quality gates, and parallel execution of independent workstreams.

**Why this matters:** Manual orchestration of the production pipeline is error-prone and slow. Automation glue ensures consistent execution, reduces human error, enables parallelization of independent tasks, and provides machine-readable status for integration with CI/CD and monitoring systems. This epic transforms the pipeline from a manual process into a reliable, repeatable system.

**Execution order:** #5 in the backlog sequence (after Epic 4 Re-render; before Epic 6 Publishing). It depends on the re-rendered Episode 1 proving the fixed pipeline end-to-end.

**Estimated effort:** 5-7 days of build loop work

## Status

| Item | Story | Status |
|------|-------|--------|
| E5-I1 | One-command episode orchestrator | Not started |
| E5-I2 | Machine-readable gate verdicts | Not started |
| E5-I3 | Parallel animator and narration-engineer execution | Not started |

Status values: **Not started** (no work begun) · **In progress** (build loop running) · **Built** (implemented, awaiting nemesis verification) · **Done** (built and tested, nemesis verdict CLEAN).

## E5-I1: One-command episode orchestrator

- **Description:** Build a CLI tool that orchestrates the complete episode production pipeline from brief to final MP4 with a single command, handling all agent invocations, artifact management, and error recovery.
- **Depends on:** E4-I3 (re-rendered Episode 1 complete, fixed pipeline proven end-to-end)
- **Rationale:** The one-command orchestrator is the crown jewel of automation. It encapsulates all the complexity of the production pipeline behind a simple interface, making it easy to produce new episodes consistently. It handles dependencies, error recovery, and state management automatically.
- **Orchestrator capabilities:**
  - Parse episode brief and determine required steps
  - Invoke appropriate agents in correct order
  - Manage artifact paths and naming conventions
  - Handle dependencies between steps
  - Provide progress updates and status reporting
  - Error recovery and retry logic
  - State persistence (can resume after interruption)
  - Logging and audit trail
- **CLI interface design:**
  ```bash
  # Build complete episode from brief
  ./scripts/orchestrate.py build --slug episode-002 --brief brief.md
  
  # Resume interrupted build
  ./scripts/orchestrate.py resume --slug episode-002
  
  # Check status of build
  ./scripts/orchestrate.py status --slug episode-002
  
  # List all episodes and their status
  ./scripts/orchestrate.py list
  ```
- **Implementation notes:**
  - Use Python with argparse for CLI
  - Implement state machine for pipeline stages
  - Store state in JSON files under `productions/<slug>/state/`
  - Provide verbose and quiet output modes
  - Include dry-run mode for testing
- **Acceptance criteria:**
  - `scripts/orchestrate.py` exists and is executable
  - Can build complete episode from brief with single command
  - Handles all pipeline stages in correct order
  - Provides meaningful progress updates
  - Error recovery works (can resume after failure)
  - State persistence works (can resume after interruption)
  - Logging provides complete audit trail
  - CLI interface is intuitive and well-documented
  - Tested with at least one complete episode build

## E5-I2: Machine-readable gate verdicts

- **Description:** Implement structured, machine-readable verdict files at each quality gate in the pipeline, enabling automated decision-making and integration with monitoring systems.
- **Depends on:** E4-I1
- **Rationale:** Machine-readable verdicts enable automation of quality decisions. Instead of humans reading and interpreting QC reports, the system can automatically decide whether to proceed, retry, or fail based on structured criteria. This is essential for scaling production and integrating with CI/CD.
- **Verdict file schema:**
  ```json
  {
    "gate": "qc-review",
    "episode": "episode-002",
    "timestamp": "2026-11-17T12:00:00Z",
    "verdict": "PASS",
    "score": 95,
    "issues": [
      {
        "severity": "minor",
        "description": "Slight audio pop at 2:15",
        "location": "audio/beat_03.mp3"
      }
    ],
    "criteria": {
      "math_accuracy": {"score": 100, "verdict": "PASS"},
      "audio_quality": {"score": 90, "verdict": "PASS"},
      "visual_quality": {"score": 95, "verdict": "PASS"},
      "sync_accuracy": {"score": 98, "verdict": "PASS"}
    }
  }
  ```
- **Quality gates to instrument:**
  - Script review gate
  - Math review gate
  - Storyboard approval gate
  - Animation render gate
  - Audio quality gate
  - Final QC gate
- **Implementation notes:**
  - Create `scripts/gate-verdict.py` for generating verdict files
  - Define schema in `schemas/gate-verdict.json`
  - Implement validation for verdict files
  - Integrate with orchestrator for automated decision-making
  - Provide human-readable summary alongside machine-readable file
- **Acceptance criteria:**
  - `scripts/gate-verdict.py` exists and generates structured verdict files
  - Verdict files follow defined JSON schema
  - All quality gates produce machine-readable verdicts
  - Orchestrator can parse and act on verdict files
  - Validation ensures verdict files are well-formed
  - Human-readable summaries are also generated
  - Tested with both PASS and FAIL verdicts

## E5-I3: Parallel animator and narration-engineer execution

- **Description:** Refactor the pipeline to allow animator and narration-engineer to work in parallel, reducing total production time by overlapping independent workstreams.
- **Depends on:** E4-I1
- **Rationale:** Animation and narration are largely independent workstreams that can proceed in parallel. The animator works from the storyboard and timing map, while the narration engineer works from the script. Parallelizing these stages can significantly reduce total production time.
- **Parallelization strategy:**
  - After storyboard approval, spawn both animator and narration-engineer
  - Animator works on scene code from storyboard
  - Narration engineer generates audio and timing map from script
  - Both workstreams converge at editor assembly stage
  - Use process pools or async execution for true parallelism
- **Dependency management:**
  - Animator needs: storyboard, continuity register, channel bible
  - Narration engineer needs: script, TTS adapter
  - Editor needs: both animator output and narration output
  - QC needs: final assembled video
- **Implementation notes:**
  - Use Python's `concurrent.futures` or `multiprocessing`
  - Implement proper synchronization and communication
  - Handle partial failures (one workstream fails, other succeeds)
  - Provide progress updates for parallel workstreams
  - Ensure thread-safe file operations
- **Acceptance criteria:**
  - Animator and narration-engineer can run in parallel
  - Total production time is reduced compared to sequential execution
  - Parallel execution produces same quality output as sequential
  - Error handling works correctly for parallel workstreams
  - Progress reporting works for parallel execution
  - Tested with complete episode build
  - Performance improvement is measurable and documented

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Orchestrator becomes too complex | Modular design with clear interfaces between components |
| Parallel execution introduces race conditions | Careful synchronization and testing |
| Machine-readable verdicts are too rigid | Allow override and manual intervention |
| Error recovery is incomplete | Comprehensive testing of failure scenarios |
| Performance improvement from parallelization is minimal | Profile and optimize; focus on CPU-bound tasks |

## Success criteria for epic completion

All three stories are marked **Done** with nemesis verdict CLEAN. The production pipeline can be run with a single command, produces machine-readable quality verdicts at each gate, and executes independent workstreams in parallel to reduce production time. The automation is reliable, well-tested, and significantly improves the efficiency of episode production.
