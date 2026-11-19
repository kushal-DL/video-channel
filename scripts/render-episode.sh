#!/usr/bin/env bash
# render-episode.sh — Render an episode directly to episodes/<slug>/final.mp4

set -euo pipefail

if [ $# -lt 3 ]; then
    echo "Usage: $0 <episode-slug> <scene-name> [resolution]"
    echo "Example: $0 episode-001-introduction-to-calculus IntroScene"
    exit 1
fi

EPISODE_SLUG="$1"
SCENE_NAME="$2"
RESOLUTION="${3:-1920x1080}"

# Determine output path — always use episodes/<slug>/final.mp4
if [[ "$EPISODE_SLUG" == productions/* ]]; then
    # Extract slug from full path (e.g., "productions/ep1/scenes/foo.py" -> "ep1")
    SLUG=$(basename -- "$EPISODE_SLUG" | sed 's/\..*//')
else
    # If it's a directory path like "episode-001-introduction-to-calculus", use as-is
    if [[ -d "$EPISODE_SLUG" ]]; then
        SLUG="$EPISODE_SLUG"
    else
        SLUG=$(basename -- "$EPISODE_SLUG")
    fi
fi

OUTPUT_FILE="episodes/$SLUG/final.mp4"

# Create output directory if it doesn't exist
mkdir -p "$(dirname -- "$OUTPUT_FILE")"

echo "Rendering episode: $EPISODE_SLUG"
echo "Resolution: $RESOLUTION"
echo "Output: $OUTPUT_FILE"

# Render with timeout wrapper (prevents silent hangs)
./scripts/render-with-timeout.sh 240 \
    .venv/bin/manimgx render \
    --resolution "$RESOLUTION" \
    "$EPISODE_SLUG" \
    "$SCENE_NAME" \
    -o "$OUTPUT_FILE"

echo ""
echo "Render complete!"
ls -la "$OUTPUT_FILE"
