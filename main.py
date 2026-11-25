# One dad joke, written to entry.txt.
#
# The joke is a printer pun, told deadpan: a raise request answered with
# "out of toner and out of patience". The program takes the output
# directory from MAKEFUN_OUTPUT_DIR, defaulting to /output, creates it,
# and writes the single line there.

import os

JOKE = "I asked my printer for a raise. It said it was already out of toner and out of patience."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    entry_path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as file:
        file.write(JOKE)
    print(f"wrote {len(JOKE)} characters to {entry_path}")


if __name__ == "__main__":
    main()
