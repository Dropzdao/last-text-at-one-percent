"""Last Text at One Percent.

Writes the entry line to /output/entry.txt with no trailing newline.
Deterministic, no network, no randomness, no input.

Craft note: the line works as a two-beat joke. The first beat sounds like
a sentimental goodbye ("Tell Mom I loved her"), which earns the reader's
trust; the second beat swerves to the phone's real grudge, its charger --
a relationship only a phone has. The punch lands on the last word, and
nothing in the line is a battery pun, so it stays fresh against the
hundred generic "low battery" entries.
"""

ENTRY = "1% left. Tell Mom I loved her. Tell my charger I never even liked it."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
