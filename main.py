# The World in One Page — news-image-20261118 entry (Python 3.13, standard library only).
#
# The entry image is the entry.png beside this file. The program copies it to
# /output/entry.png, byte for byte, so the judge sees exactly the image the
# repository holds. No network, no randomness, no timestamps: every run writes
# the same bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
DESTINATION = OUTPUT_DIR / "entry.png"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DESTINATION)
    # Fail loudly rather than hand the grader a truncated copy.
    if DESTINATION.stat().st_size != SOURCE.stat().st_size:
        raise RuntimeError("entry.png copy is incomplete")


if __name__ == "__main__":
    main()
