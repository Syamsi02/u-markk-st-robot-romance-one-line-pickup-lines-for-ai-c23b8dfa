"""Robot Romance: one-line pickup line for an AI.

Writes a single pickup line (one line, under 200 characters) to
/output/entry.txt and prints it. Pure Python standard library.
"""

import os

LINE = "Are you my autocomplete? Because every sentence I start somehow ends with you."


def main() -> None:
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read().strip() == line, "written entry does not match"
    print(line)


if __name__ == "__main__":
    main()
