#!/usr/bin/env python3
"""
Process Google Form submissions into individual game HTML files.

Google Form fields expected:
  - Column 1: Timestamp (ignored)
  - Column 2: Last Name
  - Column 3: Game code (pasted HTML)

Usage:
  python process_submissions.py responses.csv

Output:
  Creates lastname-game.html for each submission in the current directory.
  If duplicate last names exist, appends a number (smith-game.html, smith2-game.html).
"""

import csv
import sys
import re
from pathlib import Path


def sanitize_name(name: str) -> str:
    """Convert a last name to a safe, lowercase filename slug."""
    name = name.strip().lower()
    name = re.sub(r"[^a-z0-9]", "-", name)
    name = re.sub(r"-+", "-", name).strip("-")
    return name


def main():
    if len(sys.argv) != 2:
        print("Usage: python process_submissions.py responses.csv")
        sys.exit(1)

    csv_path = Path(sys.argv[1])
    if not csv_path.exists():
        print(f"Error: {csv_path} not found")
        sys.exit(1)

    output_dir = Path(__file__).parent
    used_names: dict[str, int] = {}
    count = 0

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)  # skip header row
        print(f"CSV columns: {header}")

        for row in reader:
            if len(row) < 3:
                print(f"  Skipping short row: {row}")
                continue

            _, last_name, code = row[0], row[1], row[2]
            slug = sanitize_name(last_name)

            if not slug:
                print(f"  Skipping empty name row")
                continue

            # Handle duplicate last names
            if slug in used_names:
                used_names[slug] += 1
                filename = f"{slug}{used_names[slug]}-game.html"
            else:
                used_names[slug] = 1
                filename = f"{slug}-game.html"

            filepath = output_dir / filename
            filepath.write_text(code, encoding="utf-8")
            count += 1
            print(f"  Created {filename}")

    print(f"\nDone. {count} game file(s) created in {output_dir}")


if __name__ == "__main__":
    main()
