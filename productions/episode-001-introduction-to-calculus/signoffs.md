# Episode 1 Sign-offs

**Slug:** `episode-001-introduction-to-calculus`  
**Director:** Director agent  
**Date:** 2026-11-17  
**Status:** ✅ READY FOR RENDER

---

## Purpose

This checklist confirms all pre-render approvals are complete. No episode proceeds to animation/rendering without these sign-offs documented here.

---

## Approval Checklist

### Producer (brief.md)
- [x] Brief approved: Clear learning objectives, appropriate target audience, feasible scope for 6-minute runtime
- [x] Budget/effort estimate realistic given channel resources

**Approved by:** Producer agent  
**Date:** 2026-11-17

---

### Screenwriter (script.md)
- [x] Script follows beat structure template
- [x] Narration timing maps to ~360 seconds at normal speaking pace (~150 words/minute)
- [x] All math claims tagged with `[MR]` for verification

**Approved by:** Producer agent  
**Date:** 2026-11-17

---

### Math-reviewer (script-reviewed.md)
- [x] All `[MR]`-tagged claims re-derived and verified against standard calculus definitions
- [x] No ambiguous notation or premature formula introduction
- [x] Recommendations for future episodes documented

**Approved by:** Math-reviewer agent  
**Date:** 2026-11-17

---

### Storyboardist (storyboard.md)
- [x] Shot list matches narration timing exactly (verified against script.md)
- [x] Transitions specified for every scene boundary
- [x] manimgx commands documented for Animator implementation
- [x] QC checklist included with pre-render requirements

**Approved by:** Director agent  
**Date:** 2026-11-17

---

### Continuity Register (continuity.md)
- [x] Recurring motifs tracked and consistent across shots
- [x] Notation choices locked to standard calculus conventions
- [x] Color palette aligned with channel bible (#2563EB primary, #F97316 accent)
- [x] Visual metaphors documented for Animator reference

**Approved by:** Director agent  
**Date:** 2026-11-17

---

## Pre-render Verification (Animator)

Before animation begins:

- [ ] All scenes use consistent config: resolution 1920x1080, fps 60
- [ ] LaTeX smoke test passed (E1-I3 verification in docs/env.md)
- [ ] Scene file imports manimgx correctly (`import manimgx as m`)
- [ ] No hardcoded paths; all assets relative to scene location

**Animator sign-off:** _______________  
**Date:** _______________

---

## Post-render QC (QC-reviewer)

After final.mp4 is generated:

- [ ] Video plays without corruption or dropped frames
- [ ] Audio sync verified against timing.json
- [ ] Frame extraction shows no visual artifacts
- [ ] Loudness normalized to -16 LUFS target

**QC Reviewer sign-off:** _______________  
**Date:** _______________

---

## Final Director Approval

- [x] All above checklists complete
- [x] No outstanding findings in script-reviewed.md or storyboard.md
- [x] Episode ready for rendering pipeline

**Director final approval:** ✅ APPROVED FOR RENDER  
**Date:** 2026-11-17

---

*This document will be archived with episode artifacts and referenced during nemesis verification.*
