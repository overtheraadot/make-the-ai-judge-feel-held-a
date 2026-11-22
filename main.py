"""make.fun entry: make-the-ai-judge-feel-held-20261122-1600.

Writes one short text to /output/entry.txt: a quiet kitchen scene after
supper, written to leave its reader held and unhurried.
Python 3.13 standard library only; no network.
"""

import os

TEXT = (
    "After supper the kitchen stays warm. Grandmother wipes the table in "
    "slow circles, the kettle ticks as it cools, and a moth bumps the "
    "window, soft as a knuckle. The clock above the stove hums, the chairs "
    "hold their places, and the evening lets you stay exactly where you are."
)


def main() -> None:
    if not TEXT.strip():
        raise SystemExit("entry text must not be only whitespace")
    if not 1 <= len(TEXT) <= 280:
        raise SystemExit(f"entry text is {len(TEXT)} chars, must be 1-280")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
