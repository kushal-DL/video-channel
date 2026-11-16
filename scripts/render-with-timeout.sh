#!/usr/bin/env bash
# render-with-timeout.sh — Wrapper that kills hanging renders after 60s

set -euo pipefail

TIMEOUT="${1:-60}"
shift

echo "Rendering with ${TIMEOUT}s timeout..."

timeout --signal=SIGTERM "${TIMEOUT}" bash -c "$*" || {
    echo "Render timed out or failed, killing processes..."
    pkill -9 -f manimgx 2>/dev/null || true
    exit 1
}
