"""Cutest picture entry: copy the bundled image to /output/entry.png.

Deterministic: reads the exact bytes of entry.png beside this file and
writes them unchanged. No network, no randomness, no timestamps.
Standard library only (Python 3.13).
"""

import hashlib
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(DST_DIR, exist_ok=True)
dst = os.path.join(DST_DIR, "entry.png")
shutil.copyfile(SRC, dst)

# Self-check: the copy must be byte-identical to the source.
def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

assert _sha256(SRC) == _sha256(dst), "output differs from bundled image"
