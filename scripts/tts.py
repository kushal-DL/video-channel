#!/usr/bin/env python3
"""
TTS (Text-to-Speech) CLI adapter using edge-tts.

Generates narration audio from text input. Supports both CLI arguments and stdin.

Usage:
  python scripts/tts.py --voice "en-US-AriaNeural" --output-file out.mp3 "Hello world."
  echo "Hello world." | python scripts/tts.py --voice "en-US-AriaNeural" --output-file out.mp3
"""

import argparse
import asyncio
import sys
import edge_tts


async def synthesize_tts(text: str, voice: str, output_file: str) -> None:
    """
    Synthesize text to speech and save to file.

    Args:
        text: Text to synthesize.
        voice: Edge-tts voice name (e.g., "en-US-AriaNeural").
        output_file: Output MP3 file path.
    """
    try:
        communicate = edge_tts.Communicate(text, voice=voice)
        await communicate.save(output_file)
    except Exception as e:
        print(f"Error synthesizing TTS: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Generate narration audio from text using edge-tts.",
        epilog="Text can be provided as a positional argument or read from stdin."
    )
    parser.add_argument(
        "--voice",
        required=True,
        help="Edge-tts voice name (e.g., 'en-US-AriaNeural')."
    )
    parser.add_argument(
        "--output-file",
        required=True,
        help="Output MP3 file path."
    )
    parser.add_argument(
        "text",
        nargs="?",
        default=None,
        help="Text to synthesize (optional if reading from stdin)."
    )

    args = parser.parse_args()

    # Determine text source: positional argument or stdin
    if args.text is not None:
        text = args.text
    else:
        # Read from stdin if no positional argument provided
        text = sys.stdin.read().strip()
        if not text:
            parser.print_help()
            print("\nError: No text provided (use positional argument or pipe stdin).",
                  file=sys.stderr)
            sys.exit(1)

    # Run async synthesis
    asyncio.run(synthesize_tts(text, args.voice, args.output_file))
    print(f"Generated: {args.output_file}", file=sys.stderr)


if __name__ == "__main__":
    main()
