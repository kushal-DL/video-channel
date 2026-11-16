# Epic 3: Pilot episode end-to-end (studio pipeline)

**Goal:** Produce the first complete tutorial video from brief to final rendered MP4, exercising every stage of the animation studio pipeline and proving that the agent team can work together to deliver a polished, publishable episode.

**Why this matters:** This is the first real test of the entire production system. While epics 1-2 set up the environment and tools, this epic proves they work together in a real production scenario. It validates the agent handoffs, the artifact flow, the quality gates, and the final output quality. Success here gives confidence that the pipeline can scale to a full series.

**Estimated effort:** 5-10 days of build loop work

## Status

| Item | Story | Status |
|------|-------|--------|
| E3-I1 | Channel bible and pilot brief | Not started |
| E3-I2 | Script, adversarial math review, director sign-off | Not started |
| E3-I3 | Storyboard and continuity register mechanics | Not started |
| E3-I4 | Scene code driven by the timing map | Not started |
| E3-I5 | Editor assembly to final.mp4 | Not started |
| E3-I6 | QC gate loop to clean | Not started |
| E3-I7 | Release artifact | Not started |

Status values: **Not started** (no work begun) · **In progress** (build loop running) · **Built** (implemented, awaiting nemesis verification) · **Done** (built and tested, nemesis verdict CLEAN).

## E3-I1: Channel bible and pilot brief

- **Description:** Producer agent writes the channel bible (brand identity, visual standards, tone, audience) and the pilot episode brief (topic, learning objectives, target length).
- **Depends on:** E1-I5 (productions layout documented)
- **Rationale:** The channel bible establishes the creative and brand standards that all subsequent episodes must follow. The pilot brief defines exactly what the first video will teach, setting the scope and expectations for the entire production.
- **Channel bible contents:**
  - Channel name and tagline
  - Target audience description (age, math level, learning goals)
  - Visual style guide (colors, fonts, animation style, character design)
  - Tone and voice guidelines (formal vs casual, humor level, pacing)
  - Brand assets (logo placement, intro/outro format)
  - Quality standards (resolution, audio quality, minimum frame rate)
- **Pilot brief contents:**
  - Episode title and slug
  - Mathematical topic and specific concepts covered
  - Learning objectives (what viewer will be able to do after watching)
  - Target duration (e.g., 8-12 minutes)
  - Prerequisites for viewer
  - Key examples and problems to solve
- **Acceptance criteria:**
  - `productions/pilot/channel-bible.md` exists with all required sections
  - `productions/pilot/brief.md` exists with all required sections
  - Channel bible is comprehensive enough to guide all future episodes
  - Pilot brief is specific enough that scriptwriter can begin work
  - Both documents follow the productions layout conventions from E1-I5

## E3-I2: Script, adversarial math review, director sign-off

- **Description:** Screenwriter writes the narration script with pedagogical structure; math-reviewer adversarially checks all mathematical claims; director approves the final script.
- **Depends on:** E3-I1
- **Rationale:** The script is the foundation of the video. It must be mathematically correct, pedagogically sound, and engaging. The adversarial review process catches errors before they're animated, when they're cheap to fix. Director sign-off ensures creative quality before production begins.
- **Script requirements:**
  - Clear pedagogical structure (hook → context → concept → example → practice → summary)
  - TTS-friendly sentences (avoid overly complex sentence structures)
  - Math-claim tagging for the math reviewer (e.g., `[MATH: quadratic formula derivation]`)
  - Beat-by-beat breakdown with timing estimates
  - Visual cues for animator (e.g., `[SHOW: graph of parabola]`)
- **Math review requirements:**
  - Independent re-derivation of all key mathematical steps
  - Verification of all formulas, theorems, and numerical results
  - Check for edge cases and special conditions
  - Verify pedagogical appropriateness (no skipped steps that would confuse viewers)
- **Acceptance criteria:**
  - `productions/pilot/script.md` exists with complete narration script
  - Script has beat-by-beat structure with timing estimates
  - All math claims are tagged for review
  - `productions/pilot/script-reviewed.md` exists with math reviewer's annotations
  - All math claims verified correct or corrected
  - Director sign-off recorded in `productions/pilot/signoffs.md`
  - Script includes visual cues for animator

## E3-I3: Storyboard and continuity register mechanics

- **Description:** Storyboard artist breaks the script into shots with explicit transition specs; establishes the continuity register to track visual consistency across the episode.
- **Depends on:** E3-I2
- **Rationale:** The storyboard translates the script into a visual plan, specifying exactly what appears on screen at each moment. The continuity register ensures visual consistency (character positions, object states, color schemes) throughout the episode.
- **Storyboard requirements:**
  - One shot per storyboard frame
  - Explicit transition specs between shots (cut, fade, slide, zoom)
  - Camera angles and compositions
  - Object positions and movements
  - Timing annotations matching script beats
  - Visual style notes (colors, fonts, effects)
- **Continuity register contents:**
  - Character/object position tracking
  - State changes (what's on screen, what's been introduced)
  - Color scheme consistency
  - Font and text style consistency
  - Camera position and angle tracking
- **Acceptance criteria:**
  - `productions/pilot/storyboard.md` exists with complete shot-by-shot breakdown
  - Each shot has explicit transition specs
  - `productions/pilot/continuity.md` exists as the continuity register
  - Storyboard covers all script beats
  - Director approves storyboard and continuity register
  - Approval recorded in `productions/pilot/signoffs.md`

## E3-I4: Scene code driven by the timing map

- **Description:** Animator writes manimgx Python scenes that follow the storyboard and are synchronized to the timing map generated by the narration engineer.
- **Depends on:** E3-I3, E2-I3 (timing map integration)
- **Rationale:** This is where the creative vision becomes actual animation code. The timing map ensures that animations sync perfectly with the narration. The animator follows the storyboard exactly while implementing the visual style from the channel bible.
- **Scene code requirements:**
  - One scene file per major section of the episode
  - Named in/out states for each scene element
  - Synchronization to timing map beat boundaries
  - Follow channel bible visual standards exactly
  - Clean, well-commented code
  - Efficient rendering (avoid unnecessary recomputation)
- **Animation standards:**
  - Smooth transitions (no jarring jumps)
  - Appropriate animation speeds (not too fast, not too slow)
  - Visual hierarchy (important elements stand out)
  - Consistent with storyboard and continuity register
- **Acceptance criteria:**
  - Scene code exists in `productions/pilot/scenes/`
  - All scenes render successfully with `-ql` quality
  - Animations sync with timing map beat boundaries
  - Visual style matches channel bible
  - Code follows manimgx best practices
  - Animator self-checks rendered frames for quality
  - Director reviews and approves rendered scenes

## E3-I5: Editor assembly to final.mp4

- **Description:** Editor muxes video tracks with narration audio, adds music bed, normalizes loudness, adds chapter markers, and exports the final MP4.
- **Depends on:** E3-I4, E2-I3
- **Rationale:** The editor brings all the pieces together into a cohesive final product. Proper audio mixing, loudness normalization, and chapter markers are essential for a professional viewing experience.
- **Assembly requirements:**
  - Mux video tracks with corresponding narration audio
  - Add background music bed at appropriate volume
  - Normalize audio loudness to broadcast standards (-14 LUFS for YouTube)
  - Add chapter markers at major section boundaries
  - Export in YouTube-optimized format (H.264, AAC, 1080p)
- **Audio standards:**
  - Narration clearly audible over music
  - No clipping or distortion
  - Consistent volume throughout
  - Professional-sounding audio mix
- **Acceptance criteria:**
  - `productions/pilot/final.mp4` exists and is complete
  - Video plays back correctly from start to finish
  - Audio and video are synchronized
  - Loudness is normalized to broadcast standards
  - Chapter markers are present and correctly placed
  - File format is YouTube-optimized
  - Director reviews and approves final assembly

## E3-I6: QC gate loop to clean

- **Description:** QC reviewer inspects the final output, extracts frames for visual inspection, checks A/V sync, verifies on-screen math against reviewed script, and iterates until clean.
- **Depends on:** E3-I5
- **Rationale:** Quality control is the final gate before release. The QC reviewer catches issues that earlier stages may have missed, ensuring the video meets all quality standards before it's published.
- **QC checklist:**
  - Frame-by-frame visual inspection (extract key frames)
  - A/V sync verification against timing map
  - On-screen math verification against reviewed script
  - Transition smoothness check
  - Audio quality check (no artifacts, proper levels)
  - Visual quality check (no glitches, proper rendering)
  - Pedagogical flow check (does the video teach effectively?)
- **Issue severity levels:**
  - Critical: Breaks understanding or has obvious errors
  - Major: Noticeable quality issues
  - Minor: Small imperfections
  - Cosmetic: Trivial issues that don't affect viewing
- **Acceptance criteria:**
  - QC reviewer inspects final output thoroughly
  - All critical and major issues are identified and fixed
  - QC report exists at `productions/pilot/qc-report.md`
  - Report lists all issues found with severity levels
  - Issues are tracked to resolution
  - Final verdict is "CLEAN" (no critical or major issues remaining)
  - Director approves QC report

## E3-I7: Release artifact

- **Description:** Release agent generates all metadata, title, description, chapter timestamps, tags, and thumbnail spec for YouTube release.
- **Depends on:** E3-I6
- **Rationale:** Proper metadata and release assets are essential for discoverability and professional presentation on YouTube. The release agent ensures all technical and creative requirements for publishing are met.
- **Release artifacts:**
  - Optimized title (SEO-friendly, includes keywords)
  - Detailed description with timestamps
  - Chapter markers in description
  - Relevant tags for discoverability
  - Thumbnail image spec (or actual thumbnail)
  - Category and audience settings
  - Privacy and scheduling settings
- **Metadata requirements:**
  - Title under 60 characters for full visibility
  - Description includes learning objectives
  - Timestamps for each major section
  - Tags include topic, difficulty level, series name
  - Thumbnail is eye-catching and relevant
- **Acceptance criteria:**
  - `productions/pilot/release.md` exists with all metadata
  - Title is optimized for YouTube search
  - Description includes chapter timestamps
  - Tags are relevant and comprehensive
  - Thumbnail spec is provided (or thumbnail image)
  - All metadata follows YouTube best practices
  - Director approves release artifacts

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Math errors discovered late | Adversarial review at script stage catches most errors |
| Animation quality below expectations | Director reviews at each stage; QC gate catches issues |
| Timing sync problems | Timing map drives both narration and animation |
| Production takes too long | Scope pilot to manageable length; focus on core concepts |
| Audio quality issues | Use professional TTS; normalize loudness; QC review |

## Success criteria for epic completion

All seven stories are marked **Done** with nemesis verdict CLEAN. The pilot episode is a complete, polished, publishable video that demonstrates the full production pipeline working end-to-end. The video is mathematically correct, pedagogically effective, visually appealing, and professionally produced.
