#!/usr/bin/env bash
# verify-env.sh — Epic 1 verification script for nemesis re-run
# Run from repo root with: ./scripts/verify-env.sh

set -euo pipefail

echo "=== Video-Channel Environment Verification ==="
echo ""

# E1-I1: Verify venv and manimgx
echo "--- E1-I1: Venv + manimgx ---"
.venv/bin/manimgx --version || { echo "FAIL"; exit 1; }
python3 -c "import manimgx as m; print('Import OK')" || { echo "FAIL"; exit 1; }
echo ""

# E1-I2: Render smoke test
echo "--- E1-I2: Smoke Test Render ---"
.venv/bin/manimgx render productions/_smoke/scenes/smoke.py SmokeTest -ql --disable_caching -o /tmp/verify_smoke.mp4 2>&1 || { echo "FAIL"; exit 1; }
if [ ! -s /tmp/verify_smoke.mp4 ]; then echo "FAIL: Empty output"; exit 1; fi
echo ""

# E1-I3: Render LaTeX smoke test
echo "--- E1-I3: LaTeX Smoke Test ---"
.venv/bin/manimgx render productions/_smoke/scenes/smoke_latex.py SmokeLatex -ql --disable_caching -o /tmp/verify_latex.mp4 2>&1 || { echo "FAIL"; exit 1; }
if [ ! -s /tmp/verify_latex.mp4 ]; then echo "FAIL: Empty output"; exit 1; fi
echo ""

# E1-I4: Verify ffmpeg/ffprobe (requires sudo install)
echo "--- E1-I4: ffmpeg/ffprobe ---"
which ffmpeg ffprobe || { echo "SKIP: Not installed (requires sudo apt-get install ffmpeg)"; }
ffmpeg -version 2>&1 | head -3 || true
echo ""

# E1-I5: Verify productions layout doc exists
echo "--- E1-I5: Productions Layout Doc ---"
if [ -f productions/README.md ]; then echo "OK: README exists"; else echo "FAIL: Missing"; fi
echo ""

echo "=== Verification Complete ==="
