#!/usr/bin/env python3
"""
Beat extraction script for TTS-generated audio.

Reads timing.json and audio directory, maps beats to segments, and outputs
editor-compatible metadata JSON.

Usage:
  python scripts/extract_beats.py productions/tts-fixture
"""

import argparse
import json
import os
import sys
from pathlib import Path


def extract_beats(fixture_dir: str, episode_slug: str = None) -> dict:
    """
    Extract beat metadata from timing.json and audio directory.

    Args:
        fixture_dir: Path to TTS fixture directory (containing timing.json and audio/).
        episode_slug: Optional episode slug for naming output. Defaults to "fixture".

    Returns:
        Dictionary of editor-compatible metadata.
    """
    fixture_path = Path(fixture_dir)
    timing_file = fixture_path / "timing.json"
    audio_dir = fixture_path / "audio"

    # Resolve slug for output filename
    slug = episode_slug or fixture_path.name
    output_filename = f"{slug}-editor-metadata.json"

    # Load timing data
    if not timing_file.exists():
        print(f"Error: {timing_file} not found", file=sys.stderr)
        sys.exit(1)

    try:
        with open(timing_file, "r") as f:
            timing_data = json.load(f)
    except Exception as e:
        print(f"Error reading {timing_file}: {e}", file=sys.stderr)
        sys.exit(1)

    # Validate audio files exist
    if not audio_dir.exists():
        print(f"Error: {audio_dir} not found", file=sys.stderr)
        sys.exit(1)

    # Build editor metadata
    beats = timing_data.get("beats", [])
    editor_metadata = {
        "episode_slug": slug,
        "total_duration_seconds": timing_data.get("total_duration_seconds", 0),
        "beat_count": len(beats),
        "beats": []
    }

    for beat in beats:
        audio_file = audio_dir / beat["filename"]
        if not audio_file.exists():
            print(f"Warning: {audio_file} not found", file=sys.stderr)

        beat_meta = {
            "beat_number": beat["beat_number"],
            "audio_file": str(beat["filename"]),
            "duration_seconds": beat["duration_seconds"],
            "start_time_seconds": beat["start_time"],
            "end_time_seconds": beat["end_time"],
            "text": beat.get("text", "")
        }
        editor_metadata["beats"].append(beat_meta)

    # Write output
    output_path = fixture_path / output_filename
    try:
        with open(output_path, "w") as f:
            json.dump(editor_metadata, f, indent=2)
        print(f"Created: {output_path}", file=sys.stderr)
    except Exception as e:
        print(f"Error writing {output_path}: {e}", file=sys.stderr)
        sys.exit(1)

    return editor_metadata


def main():
    parser = argparse.ArgumentParser(
        description="Extract beat metadata from TTS timing.json and audio files.",
        epilog="Output is written to <fixture>/<slug>-editor-metadata.json"
    )
    parser.add_argument(
        "fixture_dir",
        help="Path to TTS fixture directory (e.g., productions/tts-fixture)."
    )
    parser.add_argument(
        "--episode-slug",
        default=None,
        help="Optional episode slug for output naming. Defaults to fixture directory name."
    )

    args = parser.parse_args()
    metadata = extract_beats(args.fixture_dir, args.episode_slug)

    # Print summary to stdout
    print(f"Extracted {metadata['beat_count']} beats, total {metadata['total_duration_seconds']}s")


if __name__ == "__main__":
    main()
