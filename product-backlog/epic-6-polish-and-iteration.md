# Epic 6: Polish and iteration (surfaced by the pilot)

**Goal:** Refine the production pipeline based on lessons learned from the pilot episode, addressing performance bottlenecks, quality issues, and operational inefficiencies that only become apparent through real production experience.

**Why this matters:** The pilot episode exposes real-world problems that planning and design can't predict. This epic systematically addresses those issues, transforming the pipeline from "works for one episode" to "robust for a series." It's the difference between a proof of concept and a production system.

**Estimated effort:** 5-10 days of build loop work (depends on pilot findings)

## Status

| Item | Story | Status |
|------|-------|--------|
| E6-I1 | Transition smoothing pass | Not started |
| E6-I2 | Parallel scene rendering benchmark | Not started |
| E6-I3 | Snapshot regression tests for generated scenes | Not started |
| E6-I4 | Loudness measurement automation and music-bed provenance | Not started |
| E6-I5 | Episode archiving and cleanup policy | Not started |

Status values: **Not started** (no work begun) · **In progress** (build loop running) · **Built** (implemented, awaiting nemesis verification) · **Done** (built and tested, nemesis verdict CLEAN).

## E6-I1: Transition smoothing pass

- **Description:** Analyze transition quality across the pilot episode and implement improvements to make scene transitions smoother, more professional, and pedagogically effective.
- **Depends on:** E3-I6 (QC review complete)
- **Rationale:** Transitions are often overlooked but significantly impact perceived quality. Poor transitions distract viewers and break immersion. This story systematically improves transition quality based on actual production experience.
- **Transition quality aspects:**
  - Visual smoothness (no jarring cuts or jumps)
  - Timing appropriateness (not too fast, not too slow)
  - Pedagogical effectiveness (supports learning flow)
  - Consistency across episode
  - Professional appearance
- **Improvement strategies:**
  - Standardize transition types and durations
  - Implement easing functions for natural motion
  - Add visual continuity between scenes
  - Optimize transition timing for comprehension
  - Create transition style guide for future episodes
- **Implementation notes:**
  - Review QC report for transition-related issues
  - Analyze specific problematic transitions
  - Implement improvements in scene code
  - Re-render and compare before/after
  - Document transition standards for future use
- **Acceptance criteria:**
  - All transition issues identified in QC are addressed
  - Transition style guide created and documented
  - Before/after comparison shows measurable improvement
  - Transitions are consistent throughout episode
  - Director approves improved transition quality
  - Standards are documented for future episodes

## E6-I2: Parallel scene rendering benchmark

- **Description:** Benchmark and optimize parallel scene rendering to reduce total production time, identifying bottlenecks and implementing improvements.
- **Depends on:** E3-I4 (scene rendering complete)
- **Rationale:** Rendering time directly impacts production throughput. Understanding and optimizing parallel rendering can significantly reduce the time from script to final video, enabling faster iteration and more frequent publishing.
- **Benchmarking requirements:**
  - Measure sequential vs parallel rendering times
  - Identify CPU, memory, and I/O bottlenecks
  - Test different parallelization strategies
  - Measure scalability with increasing scene complexity
  - Document performance characteristics
- **Optimization strategies:**
  - Optimize scene code for parallel execution
  - Tune rendering parameters for speed/quality tradeoff
  - Implement caching for expensive computations
  - Optimize file I/O patterns
  - Consider GPU acceleration options
- **Implementation notes:**
  - Create benchmarking scripts and test scenes
  - Use profiling tools to identify bottlenecks
  - Test optimizations systematically
  - Document performance improvements
  - Provide recommendations for future optimization
- **Acceptance criteria:**
  - Comprehensive benchmarking report completed
  - Performance bottlenecks identified and documented
  - Optimizations implemented where beneficial
  - Measurable improvement in rendering time
  - Performance characteristics documented for planning
  - Recommendations provided for future optimization

## E6-I3: Snapshot regression tests for generated scenes

- **Description:** Implement visual regression testing to catch unintended changes in rendered output, ensuring consistency across episodes and preventing quality regressions.
- **Depends on:** E3-I4 (scene rendering complete)
- **Rationale:** As the pipeline evolves, it's important to catch unintended visual changes. Snapshot regression tests provide a safety net that ensures rendered output remains consistent and meets quality standards over time.
- **Regression testing requirements:**
  - Capture baseline snapshots of key frames
  - Compare new renders against baselines
  - Detect visual differences automatically
  - Support both exact and fuzzy matching
  - Generate visual diff reports
- **Test coverage:**
  - Key frames from each scene
  - Text rendering and positioning
  - Mathematical notation rendering
  - Color accuracy
  - Animation frame consistency
- **Implementation notes:**
  - Create snapshot testing framework
  - Establish baseline snapshots from pilot episode
  - Implement comparison algorithms
  - Generate visual diff reports
  - Integrate with CI/CD pipeline
- **Acceptance criteria:**
  - Snapshot testing framework implemented
  - Baseline snapshots captured from pilot episode
  - Automated comparison works correctly
  - Visual diff reports are generated
  - Integration with build pipeline complete
  - Tests catch intentional and unintentional changes

## E6-I4: Loudness measurement automation and music-bed provenance

- **Description:** Automate loudness measurement and normalization, and establish provenance tracking for music beds and audio assets used in episodes.
- **Depends on:** E3-I5 (editor assembly complete)
- **Rationale:** Consistent audio loudness is critical for professional quality. Automated measurement and normalization ensure every episode meets broadcast standards. Music-bed provenance ensures licensing compliance and proper attribution.
- **Loudness automation requirements:**
  - Measure integrated loudness (LUFS)
  - Measure true peak levels
  - Automatically normalize to target loudness
  - Validate against broadcast standards
  - Generate loudness reports
- **Music-bed provenance requirements:**
  - Track source of all music beds
  - Record licensing information
  - Store attribution requirements
  - Maintain license expiration dates
  - Generate attribution credits
- **Implementation notes:**
  - Use ffmpeg/libebur128 for loudness measurement
  - Create music-bed metadata schema
  - Implement automated normalization
  - Generate comprehensive audio reports
  - Integrate with publishing workflow
- **Acceptance criteria:**
  - Loudness measurement automation works correctly
  - Automatic normalization produces broadcast-standard audio
  - Loudness reports are generated for each episode
  - Music-bed provenance tracking implemented
  - Licensing information is recorded and tracked
  - Attribution credits are generated automatically

## E6-I5: Episode archiving and cleanup policy

- **Description:** Establish policies and tooling for archiving completed episodes and cleaning up temporary files, ensuring efficient storage use and easy access to historical content.
- **Depends on:** E3-I7 (pilot episode complete)
- **Rationale:** Without proper archiving and cleanup, storage costs grow unbounded and finding historical content becomes difficult. This story establishes sustainable practices for managing the lifecycle of episode artifacts.
- **Archiving requirements:**
  - Define what to archive (final outputs, key artifacts)
  - Define what to clean up (temporary files, intermediate renders)
  - Implement automated archiving
  - Ensure archived content is easily retrievable
  - Document archiving policy
- **Cleanup requirements:**
  - Identify temporary and intermediate files
  - Implement safe cleanup procedures
  - Preserve essential artifacts
  - Automate cleanup where safe
  - Document cleanup policy
- **Implementation notes:**
  - Create archiving scripts
  - Implement cleanup procedures
  - Document policies clearly
  - Test archiving and restoration
  - Integrate with production workflow
- **Acceptance criteria:**
  - Archiving policy documented and implemented
  - Cleanup policy documented and implemented
  - Automated archiving works correctly
  - Automated cleanup is safe and effective
  - Archived content is easily retrievable
  - Storage efficiency improved

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Pilot-specific issues don't generalize | Focus on systemic improvements, not just pilot fixes |
| Optimization efforts have diminishing returns | Benchmark thoroughly; focus on highest-impact areas |
| Regression tests are too brittle | Use fuzzy matching; focus on meaningful differences |
| Archiving policy is too restrictive or too loose | Review and adjust based on actual usage patterns |

## Success criteria for epic completion

All five stories are marked **Done** with nemesis verdict CLEAN. The production pipeline is refined, optimized, and robust based on real production experience. Performance is improved, quality is consistent, and operational practices are sustainable for a full series production.
