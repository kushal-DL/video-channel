# Video-Channel Environment Documentation

**Generated:** 2026-11-17  
**Purpose:** Reproducible local development environment for manimgx-based math animation production.

---

## System Requirements

| Component | Requirement | Notes |
|-----------|-------------|-------|
| OS | Linux (Ubuntu/Debian tested) | sudo not required if packages pre-installed |
| Python | 3.13+ | manimgx requires Python >= 3.13 |
| Disk space | ~2GB for dependencies + renders | Additional space needed per episode |

---

## Tool Versions (Verified: 2026-11-17)

### Python & manimgx
- **Python:** 3.13.18 (via uv)
- **manimgx:** 0.1.1

### Media Processing
- **ffmpeg/ffprobe:** Not installed locally (requires sudo or alternative install method)
  - Ubuntu: `sudo apt-get install ffmpeg`
  - macOS: `brew install ffmpeg`
  - Snap: `snap install ffmpeg --classic` (if available)
  - **Note:** If sudo is unavailable, use Docker with pre-installed ffmpeg or request admin privileges

### LaTeX Math Rendering
- **Status:** Already present on system (verified via MathTex smoke test)
- **Tested expression:** `x^2` renders correctly via MathTex

---

## Environment Setup Commands

```bash
# 1. Install uv (Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Create virtual environment with Python 3.13
uv venv .venv

# 3. Activate and install manimgx
source .venv/bin/activate
uv pip install --python .venv/bin/python manimgx

# 4. Verify installation
.venv/bin/manimgx --version  # Should print: manimgx 0.1.1
```

---

## Render Command Reference

### Basic render syntax (manimgx v0.1.1)
```bash
.venv/bin/manimgx render <scene_file> <SceneClass> -o <output.mp4>
```

### Example smoke test command
```bash
.venv/bin/manimgx render productions/_smoke/scenes/smoke.py SmokeTest -o /tmp/output.mp4
```

### Available options
- `-r, --resolution WxH` — Pixels (default: 1920x1080)
- `--fps <int range>` — Frames per second (default: 60)
- `--preset <ultrafast|...|placebo>` — Encoding speed preset
- `--crf <float range>` — Video quality, 0-51 (lower = better quality, default: 23.0)

---

## Smoke Test Results

### E1-I2: Basic Render Pipeline
- **Scene:** `productions/_smoke/scenes/smoke.py`
- **Content:** Text + VGroup layout (no MathTex)
- **Render output:** `/tmp/smoke_test.mp4` (80,256 bytes, 4.5s duration)
- **Status:** ✅ PASS

### E1-I3: LaTeX Toolchain Verification
- **Scene:** `productions/_smoke/scenes/smoke_latex.py`
- **Content:** Single MathTex(r"x^2") object
- **Render output:** `/tmp/smoke_latex_test.mp4` (17,288 bytes, 3.5s duration)
- **Status:** ✅ PASS

---

## Known Constraints & Workarounds

### No sudo access
If `sudo apt-get install ffmpeg` fails:
- Use a Docker container with ffmpeg pre-installed
- Use WSL on Windows with proper package installation
- Request admin privileges for system-wide tools

### manimgx import syntax
manimgx v0.1.1 uses its own module namespace:
```python
import manimgx as m

class MyScene(m.Scene):  # Not from manim import *
    def construct(self):
        title = m.Text("Hello")  # All objects prefixed with m.
```

---

## Next Steps (Epic 1 Remaining)

- [ ] E1-I4: Install ffmpeg/ffprobe on system PATH
- [ ] E1-I5: Document productions layout in `productions/README.md`
