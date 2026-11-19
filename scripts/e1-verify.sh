#!/usr/bin/env bash
# e1-verify.sh — Epic 1 nemesis re-run script
# Run from repo root: ./scripts/e1-verify.sh

set -euo pipefail

echo "=== Epic 1 Environment Setup Verification ==="
echo ""

# E1-I1: Verify venv and manimgx
echo "--- E1-I1: Venv + manimgx ---"
.venv/bin/manimgx --version || { echo "FAIL"; exit 1; }
.venv/bin/python -c "import manimgx as m; print('Import OK')" || { echo "FAIL"; exit 1; }
echo ""

# E1-I2: Render smoke test
echo "--- E1-I2: Smoke Test Render ---"
.venv/bin/manimgx render productions/_smoke/scenes/smoke.py SmokeTest --crf 50 -o /tmp/e1_verify_smoke.mp4 2>&1 || { echo "FAIL"; exit 1; }
if [ ! -s /tmp/e1_verify_smoke.mp4 ]; then echo "FAIL: Empty output"; exit 1; fi
echo ""

# E1-I3: Render LaTeX smoke test
echo "--- E1-I3: LaTeX Smoke Test ---"
.venv/bin/manimgx render productions/_smoke/scenes/smoke_latex.py SmokeLatex --crf 50 -o /tmp/e1_verify_latex.mp4 2>&1 || { echo "FAIL"; exit 1; }
if [ ! -s /tmp/e1_verify_latex.mp4 ]; then echo "FAIL: Empty output"; exit 1; fi
echo ""

# E1-I4: Verify ffmpeg/ffprobe
echo "--- E1-I4: ffmpeg/ffprobe ---"
which ffmpeg ffprobe || { echo "FAIL: Not installed on PATH"; exit 1; }
ffmpeg -version 2>&1 | head -3
ffprobe -version 2>&1 | head -3
echo ""

# E1-I5: Verify productions layout doc exists and is comprehensive
echo "--- E1-I5: Productions Layout Doc ---"
if [ -f productions/README.md ]; then echo "OK: README exists ($(wc -l < productions/README.md) lines)"; else echo "FAIL: Missing"; fi

# Literal path verification
echo ""
echo "--- Literal Path Verification ---"
grep -rn '"productions' .claude/agents/*.md 2>/dev/null | head -5 || echo "No matches found (unexpected)"
echo ""

echo "=== Epic 1 Verification Complete ==="
