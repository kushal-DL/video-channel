#!/usr/bin/env python3
"""
scripts/gemma_writer.py

Generates narration scripts using the local Gemma fine-tuned writing model
(gemma-the-writer-mighty-sword-9b) via LM Studio's OpenAI-compatible completions API.
Bypasses tool-calling schemas so Gemma can write pure creative prose without errors.
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path


DEFAULT_API_URL = "http://localhost:1234/v1/chat/completions"
DEFAULT_MODEL = "gemma-the-writer-mighty-sword-9b"
DEFAULT_AUTH_TOKEN = "sk-lm-X8wXAO4p:I6nuoG0hT8kKCCeQFWUx"


def load_settings():
    """Load settings from .claude/settings.json if available."""
    settings_path = Path(__file__).resolve().parent.parent / ".claude" / "settings.json"
    api_url = DEFAULT_API_URL
    auth_token = DEFAULT_AUTH_TOKEN
    model = DEFAULT_MODEL

    if settings_path.exists():
        try:
            with open(settings_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                env = data.get("env", {})
                base_url = env.get("ANTHROPIC_BASE_URL", "http://localhost:1234")
                api_url = f"{base_url.rstrip('/')}/v1/chat/completions"
                auth_token = env.get("ANTHROPIC_AUTH_TOKEN", DEFAULT_AUTH_TOKEN)
                model = env.get("ANTHROPIC_DEFAULT_HAIKU_MODEL", DEFAULT_MODEL)
        except Exception as e:
            print(f"[WARN] Could not parse .claude/settings.json: {e}", file=sys.stderr)

    return api_url, auth_token, model


def build_system_prompt():
    return """You are the Screenwriter for a math-tutorial YouTube channel.
Your job is to translate episode briefs into tight, pedagogically sound narration scripts that read naturally when spoken.

CORE RESPONSIBILITIES:
1) Pedagogical Beat Structure:
   - Target duration is flexible between 2 and 11 minutes based on topic complexity. Write tightly for the concepts provided in the brief. Never pad with filler, repetition, or artificial word-seeking prose to hit a duration floor.
   - Beat 1: Hook (30-50s) - character-grounded riddle or observation. Never open with a definition. Poses a question or paradox.
   - Beat 2: Motivation (30-45s) - connects to real world / prior knowledge.
   - Beats 3-5: Build-up - step-by-step derivation, one concept at a time in 20-30s sub-beats. One new symbol per beat.
   - Beat 6: Result (20-30s) - plain-language statement of the main takeaway.
   - Beat 7: Worked Example (45-75s) - MUST use a completely different real-world domain, not the same problem with different numbers. Solved step by step.
   - Beat 8: Recap & Payoff (30-45s) - ties back to the hook.

2) Strict Anti-Slop & House Style:
   - BANNED OPENERS: Never start a beat with "Here is a...", "Let us...", "Now look at...", "Notice that...", "Recall that...", "The key insight is...". Start directly with the substance.
   - BANNED HYPE: Never say "The answer will surprise you", "You will never look at X the same way", or "wrong by a mile".
   - BANNED BINARY CONTRASTS: Never use "Not X - Y" or "Not 50 percent. Not even close."
   - BANNED EM-DASHES: Do NOT use em-dashes (—). Use periods or natural commas for clean TTS pacing.
   - Vary sentence rhythm: After a long sentence (18-24 words), write a short one (<=8 words).
   - Second person, present tense ("Imagine watching...", "You already know this...").

3) Math-Claim Tagging:
   - Every factual math statement must end with `[MR]` (Math Reviewer tag). Example: "Because the area multiplies by two each day, Day 29 holds exactly half [MR]."

OUTPUT FORMAT:
Return pure Markdown with numbered beats and estimated timings:
## Beat 1: Hook [0:00-0:40]
[Narration text with [MR] tags on math claims]

## Beat 2: Motivation [0:40-1:20]
...
"""


def main():
    parser = argparse.ArgumentParser(description="Generate episode script using local Gemma model.")
    parser.add_argument("--brief", required=True, help="Path to episode brief.md")
    parser.add_argument("--scope", default=None, help="Optional path to episode scope.md")
    parser.add_argument("--out", default=None, help="Output path for script.md (defaults to same dir as brief)")
    parser.add_argument("--temperature", type=float, default=0.75, help="Sampling temperature")
    parser.add_argument("--max-tokens", type=int, default=4096, help="Maximum tokens to generate")
    args = parser.parse_args()

    brief_path = Path(args.brief).resolve()
    if not brief_path.exists():
        print(f"Error: Brief file not found at {brief_path}", file=sys.stderr)
        sys.exit(1)

    with open(brief_path, "r", encoding="utf-8") as f:
        brief_content = f.read()

    scope_content = ""
    if args.scope:
        scope_path = Path(args.scope).resolve()
        if scope_path.exists():
            with open(scope_path, "r", encoding="utf-8") as f:
                scope_content = f"\n\n--- EPISODE SCOPE ---\n{f.read()}"

    output_path = Path(args.out).resolve() if args.out else brief_path.parent / "script.md"

    api_url, auth_token, model_id = load_settings()
    system_prompt = build_system_prompt()

    user_message = f"""Here is the episode brief and production constraints. Write the full narration script following the pedagogical beat structure and math-claim tags.

--- EPISODE BRIEF ---
{brief_content}
{scope_content}

Write the full script now, beat by beat:"""

    payload = {
        "model": model_id,
        "temperature": args.temperature,
        "max_tokens": args.max_tokens,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    }

    req_data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        api_url,
        data=req_data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {auth_token}"
        }
    )

    print(f"Connecting to LM Studio ({api_url})...")
    print(f"Prompting {model_id} (Gemma Writer) for script generation...")

    try:
        with urllib.request.urlopen(req, timeout=300) as response:
            result = json.loads(response.read().decode("utf-8"))
            content = result["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8", errors="ignore")
        print(f"HTTP Error {e.code}: {err_msg}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error communicating with LM Studio: {e}", file=sys.stderr)
        sys.exit(1)

    # Save output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    words = len(content.split())
    lines = content.count("\n") + 1
    print(f"\n[SUCCESS] Script successfully written to: {output_path}")
    print(f"Stats: {words} words, {lines} lines.")


if __name__ == "__main__":
    main()
