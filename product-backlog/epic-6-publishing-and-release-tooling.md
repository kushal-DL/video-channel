# Epic 6: Publishing and release tooling

**Goal:** Build automated tooling that transforms a completed, QC-approved episode into a publication-ready YouTube upload with deterministic chapter markers, optimized thumbnails, and comprehensive preflight validation.

**Why this matters:** Manual publishing is error-prone and inconsistent. Automated release tooling ensures every episode meets quality standards before upload, has proper chapter markers for navigation, eye-catching thumbnails, and complete metadata. This epic closes the loop from production to publication.

**Execution order:** #6 in the backlog sequence (after Epic 5 Automation; before Epic 7 Polish). It depends on a QC-approved re-rendered Episode 1 (E4-I3) with a timing map.

**Estimated effort:** 3-5 days of build loop work

## Status

| Item | Story | Status |
|------|-------|--------|
| E6-I1 | Deterministic chapters and thumbnail extraction | Not started |
| E6-I2 | Publish preflight check | Not started |

Status values: **Not started** (no work begun) · **In progress** (build loop running) · **Built** (implemented, awaiting nemesis verification) · **Done** (built and tested, nemesis verdict CLEAN).

## E6-I1: Deterministic chapters and thumbnail extraction

- **Description:** Build tools that automatically extract chapter markers from the timing map and generate thumbnail candidates from key frames of the rendered video.
- **Depends on:** E4-I3 (re-rendered Episode 1 complete with measured timing map)
- **Rationale:** Chapter markers improve viewer navigation and retention. Thumbnails are critical for click-through rate. Both should be generated deterministically from production artifacts rather than manually created, ensuring consistency and saving time.
- **Chapter extraction requirements:**
  - Parse timing.json to identify beat boundaries
  - Map beats to chapter markers with descriptive titles
  - Generate YouTube-compatible chapter timestamps
  - Validate chapter ordering and timing
  - Output chapter list in format ready for YouTube description
- **Thumbnail generation requirements:**
  - Extract candidate frames at key moments (highlights, key concepts)
  - Generate multiple thumbnail options for A/B testing
  - Apply consistent branding (logo, color scheme, fonts)
  - Output thumbnails at YouTube-recommended size (1280x720)
  - Include text overlay options for title
- **Implementation notes:**
  - Create `scripts/chapters.py` for chapter extraction
  - Create `scripts/thumbnails.py` for thumbnail generation
  - Use ffmpeg for frame extraction
  - Use PIL/Pillow for image manipulation and text overlay
  - Follow YouTube's thumbnail best practices
- **Acceptance criteria:**
  - `scripts/chapters.py` extracts chapters from timing.json
  - Chapter output is YouTube-compatible (timestamps + titles)
  - Chapters are correctly ordered and timed
  - `scripts/thumbnails.py` generates thumbnail candidates
  - Thumbnails are 1280x720 pixels
  - Multiple thumbnail options are generated
  - Branding is applied consistently
  - Output includes ready-to-use YouTube description text with chapters

## E6-I2: Publish preflight check

- **Description:** Build a comprehensive preflight validation tool that checks all aspects of an episode before upload, ensuring nothing is missed and all quality standards are met.
- **Depends on:** E5-I1
- **Rationale:** Preflight checks catch issues before they reach viewers. This tool validates technical quality, metadata completeness, and publishing readiness in one automated pass, reducing the risk of embarrassing mistakes or technical problems after upload.
- **Preflight check categories:**
  - **Technical validation:** Video format, resolution, codec, audio quality, file size
  - **Metadata completeness:** Title, description, tags, chapters, thumbnail
  - **Quality checks:** Loudness levels, sync accuracy, visual quality
  - **Publishing readiness:** All required files present, correct naming conventions
  - **SEO optimization:** Keyword density, title length, tag relevance
- **Check severity levels:**
  - ERROR: Blocks publishing (must fix)
  - WARNING: Should fix but not blocking
  - INFO: Suggestions for improvement
- **Implementation notes:**
  - Create `scripts/preflight.py` for preflight validation
  - Implement checks as individual, testable functions
  - Provide detailed output with file locations and specific issues
  - Support JSON output for automation
  - Include fix suggestions for each issue found
- **Acceptance criteria:**
  - `scripts/preflight.py` exists and runs comprehensive checks
  - All check categories are implemented
  - Output clearly distinguishes ERROR, WARNING, and INFO levels
  - JSON output mode works for automation
  - Preflight check passes on pilot episode
  - Issues found include specific fix suggestions
  - Integration with orchestrator (can be called as part of build pipeline)

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Chapter extraction produces inaccurate titles | Manual review step before publishing |
| Thumbnail generation produces poor quality | Multiple options generated; manual selection |
| Preflight checks are too strict or too lenient | Calibrate based on pilot episode feedback |
| YouTube format requirements change | Keep validation rules configurable and updatable |

## Success criteria for epic completion

Both stories are marked **Done** with nemesis verdict CLEAN. Episodes can be automatically prepared for YouTube publishing with deterministic chapter markers, optimized thumbnails, and comprehensive preflight validation. The tooling reduces manual work and ensures consistent quality across all published episodes.
