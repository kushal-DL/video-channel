#!/usr/bin/env python3
"""Structural verifier for BACKLOG.md using only Python standard library."""

import argparse
import os
import re
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="Verify BACKLOG.md structure")
    parser.add_argument("backlog_path", nargs="?", default=None, help="Path to BACKLOG.md (default: ./BACKLOG.md)")
    return parser.parse_args()


def read_file(path):
    """Read file contents."""
    if not os.path.isfile(path):
        print(f"FILE-MISSING: {path}", file=sys.stderr)
        sys.exit(1)

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def check_h1(content):
    """Check exactly one line starting with '# '."""
    lines = content.split("\n")
    h1_lines = [i for i, line in enumerate(lines) if line.startswith("# ") and not line.strip().startswith("#")]

    # Filter out comment-only lines that start with # but aren't proper H1
    actual_h1 = [i for i, line in enumerate(lines) if re.match(r"^# .+$", line)]

    if len(actual_h1) != 1:
        print(f"H1-COUNT: expected exactly 1, found {len(actual_h1)}", file=sys.stderr)
        sys.exit(1)


def check_sections(content):
    """Check exactly eight ## lines in exact order."""
    lines = content.split("\n")

    # Find all lines starting with '## '
    section_lines = [(i, line) for i, line in enumerate(lines) if re.match(r"^## .+$", line)]

    if len(section_lines) != 8:
        print(f"SECTIONS-COUNT: expected exactly 8 ## sections, found {len(section_lines)}", file=sys.stderr)
        sys.exit(1)

    # Expected order: Conventions header, E1-E6 epics, Gap list
    expected_patterns = [
        r"^## Conventions$",
        r"^## E1: .+$",
        r"^## E2: .+$",
        r"^## E3: .+$",
        r"^## E4: .+$",
        r"^## E5: .+$",
        r"^## E6: .+$",
        r"^## Gap list",
    ]

    for i, (line_num, line) in enumerate(section_lines):
        if not re.match(expected_patterns[i], line):
            print(f"SECTIONS-ORDER: at line {line_num}, expected pattern {expected_patterns[i]}, got '{line}'", file=sys.stderr)
            sys.exit(1)


def check_items(content):
    """Check exactly 25 item headers with unique IDs matching the exact set."""
    lines = content.split("\n")

    # Find all lines starting with '### E' followed by digit, dash, digit, colon
    item_lines = [(i, line) for i, line in enumerate(lines) if re.match(r"^### E[1-6]-I\d+: .+$", line)]

    if len(item_lines) != 25:
        print(f"ITEMS-COUNT: expected exactly 25 items, found {len(item_lines)}", file=sys.stderr)
        sys.exit(1)

    # Extract IDs and check uniqueness
    ids = [re.search(r"^### (E[1-6]-I\d+):\s+", line).group(1) for _, line in item_lines]
    if len(ids) != len(set(ids)):
        print("ITEMS-DUPLICATE: duplicate item IDs found", file=sys.stderr)
        sys.exit(1)

    expected_ids = {
        "E1-I1", "E1-I2", "E1-I3", "E1-I4", "E1-I5",
        "E2-I1", "E2-I2", "E2-I3",
        "E3-I1", "E3-I2", "E3-I3", "E3-I4", "E3-I5", "E3-I6", "E3-I7",
        "E4-I1", "E4-I2", "E4-I3",
        "E5-I1", "E5-I2",
        "E6-I1", "E6-I2", "E6-I3", "E6-I4", "E6-I5"
    }

    actual_ids = set(ids)
    if actual_ids != expected_ids:
        missing = expected_ids - actual_ids
        extra = actual_ids - expected_ids
        if missing:
            print(f"ITEMS-MISSING: {missing}", file=sys.stderr)
        if extra:
            print(f"ITEMS-EXTRA: {extra}", file=sys.stderr)
        sys.exit(1)

    # Check no other line starts with '### ' (only item headers should)
    for i, line in enumerate(lines):
        if re.match(r"^### .+$", line) and not re.match(r"^### E[1-6]-I\d+: .+$", line):
            print(f"ITEMS-EXTRA-HASH: at line {i}, unexpected '### ' header: '{line}'", file=sys.stderr)
            sys.exit(1)


def check_fields(content):
    """Check each item has exactly one Description, Depends on, and Acceptance criteria field."""
    lines = content.split("\n")

    # Parse items into blocks (from one ### header to the next ### or end of file)
    item_blocks = []
    current_block = None  # Will hold lines belonging to the current item
    in_item = False

    for i, line in enumerate(lines):
        if re.match(r"^### E[1-6]-I\d+: .+$", line):
            # Save previous block and start new one
            if current_block is not None:
                item_blocks.append(current_block)
            current_block = [line]
            in_item = True
        elif in_item and re.match(r"^### E[1-6]-I\d+: .+$", line):
            # Next item header, save current block and start new one
            if current_block:
                item_blocks.append(current_block)
            current_block = [line]
        elif in_item:
            # Continuation line of the current item
            current_block.append(line)

    # Don't forget the last item
    if current_block is not None and len(current_block) > 0:
        item_blocks.append(current_block)

    # Each block should have exactly 3 field lines
    for idx, block in enumerate(item_blocks):
        description_lines = [l for l in block if re.match(r"^-\s*\*\*Description:\*\*.+$", l)]
        depends_lines = [l for l in block if re.match(r"^-\s*\*\*Depends on:\*\*.+$", l)]
        criteria_lines = [l for l in block if re.match(r"^-\s*\*\*Acceptance criteria:\*\*.+$", l)]

        if len(description_lines) != 1:
            print(f"FIELDS-DESCRIPTION-{idx}: expected exactly 1 Description line, found {len(description_lines)}", file=sys.stderr)
            sys.exit(1)

        if len(depends_lines) != 1:
            print(f"FIELDS-DEPENDS-{idx}: expected exactly 1 Depends on line, found {len(depends_lines)}", file=sys.stderr)
            sys.exit(1)

        if len(criteria_lines) != 1:
            print(f"FIELDS-CRITERIA-{idx}: expected exactly 1 Acceptance criteria line, found {len(criteria_lines)}", file=sys.stderr)
            sys.exit(1)

        # Check non-empty values after colon
        desc_val = description_lines[0].split(":", 1)[1].strip()
        if not desc_val:
            print(f"FIELDS-DESCRIPTION-EMPTY-{idx}: Description value is empty", file=sys.stderr)
            sys.exit(1)

        deps_val = depends_lines[0].split(":", 1)[1].strip().lstrip("**")
        if not deps_val:
            print(f"FIELDS-DEPENDS-EMPTY-{idx}: Depends on value is empty", file=sys.stderr)
            sys.exit(1)

        criteria_val = criteria_lines[0].split(":", 1)[1].strip()
        if not criteria_val:
            print(f"FIELDS-CRITERIA-EMPTY-{idx}: Acceptance criteria value is empty", file=sys.stderr)
            sys.exit(1)


def check_deps(content):
    """Check dependency IDs exist and appear earlier in file order."""
    lines = content.split("\n")

    # Build list of (order, item_id, depends_value)
    items_with_deps = []
    for i, line in enumerate(lines):
        if re.match(r"^### E[1-6]-I\d+: .+$", line):
            # Extract ID from header like "### E2-I1: Options evaluation spike (no vendor committed)"
            match = re.search(r"### (E[1-6]-I\d+):\s+", line)
            if match:
                item_id = match.group(1)

                # Find the Depends on value in subsequent lines
                for j in range(i + 1, len(lines)):
                    dep_line = lines[j]
                    if re.match(r"^### ", dep_line):
                        break
                    if re.match(r"^-\s*\*\*Depends on:\*\*(.+)$", dep_line):
                        deps_value = dep_line.split(":", 1)[1].strip().lstrip("**")
                        items_with_deps.append((i, item_id, deps_value))
                        break

    # Validate each dependency
    for order, item_id, deps_value in items_with_deps:
        # Only 'none' (stripped) is allowed as a literal
        if deps_value.strip() == "none":
            continue

        # Split by comma and strip whitespace
        dep_ids = [d.strip() for d in deps_value.split(",")]

        for dep_id in dep_ids:
            if not re.match(r"^E[1-6]-I\d+$", dep_id):
                print(f"DEPS-FORMAT-{item_id}: invalid dependency ID format '{dep_id}'", file=sys.stderr)
                sys.exit(1)

            # Find the order of this dependency
            dep_order = None
            for o, iid, _ in items_with_deps:
                if iid == dep_id:
                    dep_order = o
                    break

            if dep_order is None:
                print(f"DEPS-MISSING-{item_id}: dependency '{dep_id}' not found as an item", file=sys.stderr)
                sys.exit(1)

            # Dependency must appear earlier in file order
            if dep_order >= order:
                print(f"DEPS-ORDER-{item_id}: dependency '{dep_id}' (order {dep_order}) appears after or at same position as '{item_id}' (order {order})", file=sys.stderr)
                sys.exit(1)


def check_gaps(content):
    """Check Gap list section has at least 8 bullet lines starting with '- '."""
    # Find the Gap list section (header starts with ## Gap list)
    in_gap_section = False
    gap_bullets = []

    for line in content.split("\n"):
        if re.match(r"^## Gap list", line):
            in_gap_section = True
            continue

        if in_gap_section:
            if re.match(r"^-\s*$", line) or re.match(r"^\s*-$", line):
                # Empty bullet, skip
                continue
            if re.match(r"^-\s+", line):
                gap_bullets.append(line)

    if len(gap_bullets) < 8:
        print(f"GAPS-COUNT: expected at least 8 bullets in Gap list section, found {len(gap_bullets)}", file=sys.stderr)
        sys.exit(1)


def check_tts_policy(content):
    """Check exactly one line contains the exact TTS non-commitment sentence."""
    lines = content.split("\n")

    # Count lines containing the exact sentence
    count = 0
    for line in lines:
        if "no item commits a TTS vendor/backend as the channel default" in line:
            count += 1

    if count != 1:
        print(f"TTS-SENTENCE-COUNT: expected exactly 1 occurrence of 'no item commits a TTS vendor/backend as the channel default', found {count}", file=sys.stderr)
        sys.exit(1)


def main():
    args = parse_args()

    # Default path resolution
    if args.backlog_path is None or args.backlog_path == "":
        backlog_path = os.path.join(os.getcwd(), "BACKLOG.md")
    else:
        backlog_path = os.path.abspath(args.backlog_path)

    try:
        content = read_file(backlog_path)
    except Exception as e:
        print(f"READ-ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    # Run all checks in order
    check_h1(content)
    check_sections(content)
    check_items(content)
    check_fields(content)
    check_deps(content)
    check_gaps(content)
    check_tts_policy(content)

    print("BACKLOG-OK")
    sys.exit(0)


if __name__ == "__main__":
    main()
