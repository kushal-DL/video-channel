#!/usr/bin/env python3
"""Structural gate for product-backlog/BACKLOG.md.

Enforces the exact format of the master backlog so future edits can't silently
drop an epic, rename a section header, or break the item-ID scheme that other
agents and scripts rely on.

Expected structure (7 epics in execution order):
  - Exactly 8 ``##`` sections: Execution Order + Epic 1..Epic 7.
  - Exactly 30 table-row items matching ``^\\| E[1-7]-...``, unique, with the id
    set equal to EXPECTED_IDS below (no more, no fewer).

Run: python3 tests/test_backlog.py [path-to-backlog]
Exit 0 and print BACKLOG-OK on success; exit 1 with a reason otherwise.
"""
import re
import sys
from pathlib import Path

DEFAULT_PATH = Path(__file__).resolve().parent.parent / "product-backlog" / "BACKLOG.md"

EXPECTED_SECTIONS = [
    "Execution Order (backlog sequence)",
    "Epic 1: Environment Setup",
    "Epic 2: Update Agent Definitions & Channel Bible (from Episode 1 post-mortem)",
    "Epic 3: TTS and Voice Cloning",
    "Epic 4: Re-render & Validate Episode 1 Through the Fixed Pipeline",
    "Epic 5: Automation Glue",
    "Epic 6: Publishing and Release Tooling",
    "Epic 7: Polish and Iteration (surfaced by the re-render)",
]

EXPECTED_IDS = {
    # E1 — Environment Setup
    "E1-I1", "E1-I2", "E1-I3", "E1-I4", "E1-I5",
    # E2 — Update Agent Definitions & Channel Bible
    "E2-I1", "E2-I2", "E2-I3", "E2-I4", "E2-I5",
    "E2-I6", "E2-I7", "E2-I8", "E2-I9",
    # E3 — TTS and Voice Cloning
    "E3-I1", "E3-I2", "E3-I3",
    # E4 — Re-render & Validate Episode 1
    "E4-I1", "E4-I2", "E4-I3",
    # E5 — Automation Glue
    "E5-I1", "E5-I2", "E5-I3",
    # E6 — Publishing and Release Tooling
    "E6-I1", "E6-I2",
    # E7 — Polish and Iteration
    "E7-I1", "E7-I2", "E7-I3", "E7-I4", "E7-I5",
}

# Table-row item: a line beginning with "| E<epic>-<letter><num>" followed by ":" or " |"
ITEM_RE = re.compile(r"^\| (E[1-7]-[A-Z]\d+)(?::|\s)", re.MULTILINE)


def fail(reason: str) -> None:
    print(f"BACKLOG-FAIL: {reason}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    if not path.exists():
        fail(f"{path} does not exist")

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # --- Section headers (## level only, excluding the H1 title) -------------
    sections = [ln[3:].strip() for ln in lines if ln.startswith("## ")]
    if len(sections) != len(EXPECTED_SECTIONS):
        fail(f"SECTIONS-COUNT: expected exactly {len(EXPECTED_SECTIONS)} ## sections, found {len(sections)}")
    for got, want in zip(sections, EXPECTED_SECTIONS):
        if got != want:
            fail(f"SECTION-MISMATCH: expected '{want}', found '{got}'")

    # --- Item rows -----------------------------------------------------------
    ids = ITEM_RE.findall(text)
    if len(ids) != len(set(ids)):
        dupes = sorted({i for i in ids if ids.count(i) > 1})
        fail(f"DUPLICATE-IDS: {dupes}")
    id_set = set(ids)
    missing = EXPECTED_IDS - id_set
    extra = id_set - EXPECTED_IDS
    if missing or extra:
        fail(f"ID-SET-MISMATCH: missing={sorted(missing)} extra={sorted(extra)}")

    print("BACKLOG-OK")


if __name__ == "__main__":
    main()
